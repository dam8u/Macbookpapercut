#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the MOO-208 deliverable: MOO-211's six cures, drafted, priced and reproduced in full.

Two layers of markup, and the deliverable says so in terms:

  * `<u>…</u>` is the AMENDATORY layer against the Code of Virginia. Subdivision D 1 and
    subsection M 2 are new language in a new section, so each sits inside one `<u>` span, and
    **no cure adds a tag** — which is why every one leaves §1's `<u>`/`</u>` at 62 / 62. The
    enactment clauses carry no amendatory markup at all, not being amendatory text.
  * **bold** marks what a cure WOULD ADD and ~~strikethrough~~ what it WOULD STRIKE (only M4). That is the
    PROPOSAL layer. It is not amendatory markup, it is not in the store, and **nothing in it is
    enacted or agreed.**

Each provision is reproduced by applying the cures to the LIVE text, so it cannot drift from the
store, and each is verified by stripping the proposal layer and comparing character for character
with the live provision.

    python3 build_pack.py          # writes moo208-cures.md
"""
import json, os, re, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cures import CURES, build

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
HERE = os.path.dirname(os.path.abspath(__file__))
AO, AC, DO, DC = "\x01", "\x02", "\x03", "\x04"   # proposal-layer add / delete, open and close


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def get(p):
    r = urllib.request.Request(base() + p, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"]})
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def line_containing(s1, needle):
    k = s1.index(needle)
    return s1[s1.rfind("\n", 0, k) + 1:s1.find("\n", k)]


def unproposal(s):
    """Strip the proposal layer and return the LIVE provision: DROP what a cure would add, and
    RESTORE what it would strike. Merely unwrapping the markers would return the cured text and
    make the check vacuous."""
    s = re.sub(AO + ".*?" + AC, "", s, flags=re.S)
    return s.replace(DO, "").replace(DC, "")


def render(s):
    return (s.replace(AO, "**").replace(AC, "**")
             .replace(DO, "~~").replace(DC, "~~"))


def apply_cures(prov, ids, by_id):
    """Apply each named cure to `prov`, wrapping the new words in proposal-layer sentinels."""
    out, applied = prov, []
    for cid in ids:
        c = by_id[cid]
        f, _ = build(c, tagged=False)
        assert out.count(f) == 1, f"{cid}: FIND resolves {out.count(f)}x in the provision"
        if c["mode"] == "insert_after":
            cut = f.index(c["at"]) + len(c["at"])
            r = f[:cut] + AO + c["ins"] + AC + f[cut:]
        elif c["mode"] == "insert_before":
            r = AO + c["ins"] + AC + f
        else:
            # A replacement strikes the old words and adds the new ones, so the layer needs both.
            # The separating space goes INSIDE the add span, so stripping restores the original
            # spacing exactly rather than leaving a double space.
            r = f.replace(c["at"], DO + c["at"] + DC + AO + " " + c["ins"] + AC, 1)
        out = out.replace(f, r, 1)
        applied.append(cid)
    # The proof: strip the proposal layer and we must be back at the live provision exactly.
    assert unproposal(out) == prov, "proposal layer does not strip back to the live provision"
    return out, applied


def main():
    doc = get(f"/api/issues/{MOO42}/documents/bill-text-s8")
    body = doc["body"]
    rev = max(int(x) for x in re.findall(r"^### 0\.0-(\d+) ", body, re.M))
    s1 = sec1(body)
    by_id = {c["id"]: c for c in CURES}

    d1 = line_containing(s1, "<u>**D. 1.** The Board shall not accept an election")
    m2 = line_containing(s1, "<u>2. A member, retiree, beneficiary, applicant")
    e3 = line_containing(s1, "**3. That § 51.1-142.4 of the Code of Virginia, as created")
    title = line_containing(s1, "pilot program; death benefits; designation of beneficiary;")

    # Which cures land in which provision — asserted, not assumed.
    for cid, prov, pname in (("S1", m2, "M 2"), ("S3", d1, "D 1"), ("S5", d1, "D 1"),
                             ("M4", d1, "D 1"), ("S2", e3, "enactment 3"),
                             ("M3", e3, "enactment 3")):
        f, _ = build(by_id[cid], tagged=False)
        assert prov.count(f) == 1, f"{cid}'s FIND is not 1x in {pname}"

    d1_new, _ = apply_cures(d1, ["S3", "S5", "M4"], by_id)
    m2_new, _ = apply_cures(m2, ["S1"], by_id)
    e3_new, _ = apply_cures(e3, ["S2", "M3"], by_id)

    # Totals, and the tag invariant, proved on §1 rather than asserted.
    all_new = s1
    for cid in ("S1", "S2", "S3", "S5", "M3", "M4"):
        f, r = build(by_id[cid], tagged=False)
        all_new = all_new.replace(f, r, 1)
    total = len(all_new) - len(s1)
    assert total == sum(c["delta"] for c in CURES), (total, sum(c["delta"] for c in CURES))
    assert all_new.count("<u>") == 62 and all_new.count("</u>") == 62

    rows = "\n".join(
        f"| **{c['id']}** | {c['grade']} | {c['where']} | **{c['delta']:+d}** | "
        f"{c['counsel']} | none |" for c in CURES)

    out = f"""# MOO-208 — MOO-211's six cures: drafted, priced, anchored, and **enacted nowhere**

**Nothing in this document is enacted and nothing is agreed. All six are decisions for the Policy
Director.** Internal working draft, pre-decisional, not a Division of Legislative Services bill,
not cleared by counsel or by DLS, not legally sufficient for introduction.

Verified on document revision `{doc['latestRevisionId']}` (number {doc.get('latestRevisionNumber')}),
**store revision {rev}**, §1 **{len(s1):,}** characters. Every FIND counted **inside the §1 slice**.
Kit, verification script and this builder at `moo211-cures/`.

## 1. What changed since counsel read the text, and what did not

**Counsel verified on store revision 70. Store revision 71 landed first and moved §1 by +1,455.**
Every one of the six FIND strings still resolves **exactly 1× inside the §1 slice**, and **all
nineteen counts counsel asserts about §1 re-count exactly** — the tag counts at 62/62, the
conformed phrase at 3×, the *"for the purposes of subsection M"* family at 6× and 5×, M 2's three
operative clauses, M 1's *"content of a complete application"*, and the wider *"Nothing in this
section"* formula at 3×. **Nothing in the counsel pass was spent by the intervening revision.**

**One measurement moved, and it moved the wrong way.** Counsel's S4 rests on the length of D 1's
*"shall also state"* sentence, measured at store revision 70 as 3,447 characters and 576 words.
At store revision {rev} it is **{len(_sentence(s1)):,} characters and {len(_sentence(s1).split())} words** — **+{len(_sentence(s1)) - 3447} and
+{len(_sentence(s1).split()) - 576} in one revision.** S4 is the recorded cost of holding F5, which is the Director's
decision and which this document does not reopen.

## 2. The six cures, priced

| # | Grade | Provision it edits | **Delta** | MOO-211 said | `<u>` tags |
|---|---|---|---|---|---|
{rows}

**Total if all six were taken: {total:+d}**, and §1's `<u>`/`</u>` would stay at **62 / 62**.

### Why no cure carries a `<u>` tag, and why that matters

Counsel wrote `<u></u>` tags into five of the six. **All five are wrong, for two different
reasons**, and this is the one thing in the pass that would have damaged the text:

* **S1, S3, S5 and M4 sit inside an open `<u>` span.** Subsection M 2 and subdivision D 1 are
  wholly new language in a new section, so each is already inside one span. Counsel's tags would
  have **nested**, taking §1 from 62/62 to **63/63** and breaking the standing post-condition.
* **S2 and M3 sit in enactment clause 3, which carries zero `<u>` tags in 6,176 characters** — the
  enactment clauses not being amendatory text, exactly as the title line is not redlined.

So the amendatory layer is untouched by all six, and **counsel's S2 figure (+118) is right for the
wrong reason**, being the figure net of tags counsel also wrote. **M3 is off by one** on counsel's
own words: **+95, not +94.**

## 3. The provisions, in full, as they would read

**Markup key.** `<u>…</u>` is the **amendatory** layer against the Code of Virginia and is in the
store. **Bold** marks what a cure **would add**; no cure strikes anything. The **proposal layer is
not in the store and is not enacted.** Each provision below was built by applying the cures to the
live text and is verified by stripping the proposal layer back to it character for character.

### 3.1 Subdivision M 2 of § 51.1-142.4, with **S1** (form M-a) — the cure for F3

{render(m2_new)}

### 3.2 Subdivision D 1 of § 51.1-142.4, with **S3**, **S5** and **M4**

{render(d1_new)}

### 3.3 Enactment clause 3, with **S2** (clause (v)) and **M3** (clause (iii))

{render(e3_new)}

### 3.4 The title line and the enacting clause — **no cure touches either**

The title line stands as store revision 70's T2 left it:

{title}

`Be it enacted by the General Assembly of Virginia:` is untouched, the act's section footprint is
unchanged — it amends §§ 51.1-142.2 and 51.1-162 and adds § 51.1-142.4 — and **no cure adds,
renumbers or removes a section, a subdivision designator or a defined term.**

## 4. What each cure decides

{_decides(CURES)}

## 5. Cross-reference check

**Performed on store revision {rev}, in both directions, for all six cures. Result: no conforming
amendment is needed for any of them, and one existing conforming-amendment note was wrong and is
corrected.**

* **S1** writes into M 2 the same phrase the enacted text already uses three times, so the
  exception would appear a fourth time **in one vocabulary**. Subsection J is unaffected: J 1's
  catch-all (*"every other matter this section requires the Board to state in that report"*, 1× in
  §1) is a duty to report, not a channel of review. **No conforming amendment.**
* **S2 and M3** edit enactment clause 3 only. Enactment clauses are not cited by any provision of
  the act — *"enactment"* resolves nowhere in §1 as a cross-reference — so **nothing can be
  stranded by either.** **No conforming amendment.**
* **S3** adds a limitation to a proposition **about** § 51.1-162 A and B. It does not amend
  § 51.1-162, which this act reproduces at length under art. IV, § 12 and which must stay
  reproduced unchanged. **No conforming amendment** — and S3 is the cure that stops D 1's gloss on
  a section of general application from being wrong for retired members.
* **S5** is a rule of construction for statements D 1 already requires. It names §§ 51.1-162,
  51.1-163, 51.1-165 and 51.1-165.01 **by section**, not by paraphrase. **No conforming
  amendment**, and it cures the defect in §5.47 row 3 described below.
* **M4** widens one limb of the no-fault clause from *"this subdivision"* to *"this section, and
  no procedure adopted under subsection M,"*. Checked against subdivision G 4 and subsection N for
  a collision: **the second limb must stay keyed to the subdivision**, because widening *"or
  affects any benefit"* to the section would collide with G 4's death-benefit computation. **M4 as
  drafted widens the first limb only.** **No conforming amendment.**
* **Corrected in store revision 72:** §5.47 direction 1 **row 3's conforming-amendment column did
  not hold.** It said no conforming amendment was needed for *"at any time before the member's
  death"* because *"the words are tied to A, so the statement follows A if A is amended."* **The
  citation carries the source of the power; it does not carry the timing** — the temporal
  proposition is this drafter's inference, so if A were amended to fix a moment of irrevocability,
  D 1 would still compel the old proposition. Record patches R1 and R6.

## 6. Drafter's note

**On the record, not on the text — store revision 72, record only.** §1 is **byte-for-byte**
unchanged, proved by diff and not by delta. Five demonstrated errors of fact in the record are
corrected in place (R1–R9), and §7 items 133 and 135 are corrected on the item list.

1. **The title authority did not hold.** §5.47 row 7 and §6.0-70's T2 item both cited
   *Dean v. Paolicelli*, 194 Va. 219 (1952) for the sufficiency of a title line. **That case has no
   title holding** — it decides eligibility for state office and special legislation. The authority
   is ***City of Richmond v. Pace*, 127 Va. 274, 103 S.E. 647 (1920)**. **The proposition was
   correct Virginia law; only the case was wrong**, and under *Pace* the consequence runs the other
   way: **T2 was never constitutionally required**, the death-benefit provisions being already
   germane to the stated object. T2 is the better title, not a save.
2. **A matching character delta is a checksum, and the record called it a proof.** Check 10 said
   §1 moved by exactly the 634 characters the six substitutions account for, *"which is the
   arithmetic proof that nothing else in §1 changed."* **It is not.** Two offsetting changes pass
   it, and so does any zero-character change — and §6.0-70 item 4 records that store revision 70
   **contains one**, F4's relocation of the series' *"and"*. **The standing rule from store
   revision 72 is a line diff against the fetched base**, and `rec72.py` is the first kit to carry
   it: its decisive post-condition is that §1 after is **identical** to §1 before.
3. **The F3 residue does not exist.** The instruction to §7 item 133 was that the misstatement limb
   reach *"the six propositions of law and not the advisory."* **Item 7 carries one advisory and
   two propositions of law**, so the series carries **eight propositions of law and one advisory**.
   The drafted scope, *"every matter other than the advice"*, reaches all eight and excepts the one
   — **exactly what the instruction intended.** The asymmetry the record described was an artefact
   of the miscount. **No residue, no three-way split, and the (i)–(vii) renumbering the commission
   forbade is not needed for anything.**
4. **Item 135's two figures were wrong and its two READ strings would have nested tags.** M-a was
   stated at +116 and is **+115** (the FIND already supplies the comma); M-b was stated at +101 and
   is **+121**, and M-b's further *"+42 in D 1"* **has no drafted words and remains unpriced**, so
   M-b costs +121 plus an undrafted edit against M-a's +115 and nothing.
5. **An ambiguity I resolved, and it is the drafter's call and not counsel's.** Item 135 recorded
   as a defect that neither form of the M 2 cure reaches item 7's other two propositions. **That is
   not a defect: it is the right answer.** Those two clauses are **propositions of law, not
   advice**, and the purpose of F3 was to except the advice. Widening the exception to all three
   would **remove subsection M review from two propositions of law that nobody proposed to remove
   it from.** So the exception correctly names the advice and only the advice, in D 1 as enacted
   and in either form of this cure. **If the Director reads it the other way it is one more
   substitution — but it should not be fixed silently.**
6. **What I did not do.** **F5 stays held and no acknowledgment form exists anywhere in this
   draft.** E1 is untouched and under the [MOO-192](/MOO/issues/MOO-192) gate. **F7 is not cut**;
   §7 item 133 stays open, with its premise narrowed — most misstatements decompose into omissions
   already inside D 1's failure sentence, including item 133's own worked example, so **the real
   gap is additive misstatement only**. No cure is enacted. **No provision that was not agreed has
   been added to the bill text.**

## 7. Open questions for the Policy Director

1. **S1 — do I open subsection M 2?** The MOO-208 commission did not open it, and **no cure inside
   D 1 can work.** Counsel agrees with the finding and recommends **form M-a (+115)**, and so do I,
   for the reason that decides it: M-b's generic hook creates a **standing invitation**, since
   after it any future exception written anywhere in the section silently withdraws subsection M
   review with no reader of subsection M able to see which matters are excepted.
2. **S2 — does the failure-to-state limb survive 1 July 2033?** Counsel's most serious finding, and
   it is not about this revision. **+118, enactment clause only, touches no operative text.**
3. **S3 — is item 7's terminus limited to death before retirement?** **+127**, and it does not
   reverse your F2 decision; counsel's shorter alternative does.
4. **S5 — do the six frozen descriptions follow the sections they describe?** **+310**, the largest
   of the six and the only one that adds a sentence to the subdivision.
5. **M3 — does D 1 survive the expiry for the subsection J duties?** **+95.** Note this is the
   enforcement half of F3, and after S1 it is **not** the only consequence attached to the advice.
6. **M4 — does the no-fault clause reach a procedure adopted under subsection M 1?** **+42**, first
   limb only.
7. **Item 135's scope, at §6 note 5 above** — confirm that the exception names the advice only.

**If you take any of them, say which and in what order; D 1 cures touch one line and I will cut
them as one revision with each anchor re-counted at the moment it is applied.**

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or
by DLS, not legally sufficient for introduction. Pre-decisional and internal.**
"""
    open(os.path.join(HERE, "moo208-cures.md"), "w", encoding="utf-8").write(out)
    print(f"wrote moo208-cures.md  {len(out)} chars | store revision {rev} | total {total:+d}")
    print(f"  D 1 {len(d1)} -> {len(unproposal(d1_new))} (strips back: "
          f"{unproposal(d1_new) == d1})")
    print(f"  M 2 {len(m2)} -> {len(unproposal(m2_new))} (strips back: "
          f"{unproposal(m2_new) == m2})")
    print(f"  E 3 {len(e3)} -> {len(unproposal(e3_new))} (strips back: "
          f"{unproposal(e3_new) == e3})")


def _sentence(s1):
    a = s1.index("The Board's certification shall also state that,")
    z = s1.index(". A failure to state in the Board's certification") + 1
    return s1[a:z]


def _decides(cs):
    return "\n".join(f"**{c['id']} — {c['where']}.** {c['decides']} *{c['note']}*\n"
                     for c in cs)


if __name__ == "__main__":
    main()
