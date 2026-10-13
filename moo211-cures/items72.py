#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-208 store revision 72 — §7 items 133 and 135 corrected out of MOO-211's counsel pass.

Item 135 is the card the Policy Director will act from, and **both of its character figures are
wrong and both of its READ strings write `<u></u>` tags that would nest** inside subsection M 2's
open span. Item 133's recorded scope rests on a miscount of the certification series. Neither
item's DRAFTED WORDS change: what changes is the arithmetic, the markup, and the description.

Corrections are appended in place and marked, in the form store revision 70 established. Nothing
is enacted and nothing is agreed.

    python3 items72.py --dry-run
    python3 items72.py
"""
import json, os, re, sys, urllib.request, urllib.error

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8-item-list"
CEILING = 524288


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def req(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(base() + path, data=data, method=method, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", ""),
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


MARK = "**CORRECTED IN STORE REVISION 72**"
M211 = "[MOO-211](/MOO/issues/MOO-211)"

# ---- item 135, form M-a: the arithmetic and the nesting tags ------------------------------
A_F = ("READ: *\"or by a failure of the Board to state in a certification or notice a matter this "
       "section requires to be stated in it<u>, other than a failure to state that the Board "
       "advises the member to review the member's designation of beneficiary</u>, may obtain\"*. "
       "**+116 characters, and no conforming change anywhere else.**")
A_R = (
    "READ, as this item first wrote it and **struck through here so that it cannot be lifted from "
    "this card by mistake**: ~~*\"…requires to be stated in it<u>, other than a failure "
    "to state that the Board advises the member to review the member's designation of "
    "beneficiary</u>, may obtain\"* — +116 characters~~. " + MARK + ", on " + M211 + " m1 and "
    "on a markup check that pass did not make. **Two things in that READ string were wrong and "
    "the second would have damaged the text.**\n\n"
    "    **The markup. Subsection M 2 is wholly new language and the insertion point sits inside "
    "an open `<u>` span**, so the tags written above would have **nested**, taking §1 from 62/62 "
    "to 63/63 and breaking the standing post-condition on the tag counts. **The cure carries no "
    "tags.** READ, corrected: *\"or by a failure of the Board to state in a certification or "
    "notice a matter this section requires to be stated in it, other than a failure to state that "
    "the Board advises the member to review the member's designation of beneficiary, may "
    "obtain\"*.\n\n"
    "    **The arithmetic. +115, not +116** — the FIND already ends *\"in it, may obtain\"*, so "
    "the existing comma is retained and the insertion is the 115-character form without a "
    "trailing comma, not the 116-character form substitution 4 used in subdivision D 1. "
    "**+115 characters, no markup, and no conforming change anywhere else.** Re-resolved on store "
    "revision 71: the FIND still resolves **1× inside the §1 slice**, and the cure leaves "
    "`<u>`/`</u>` at **62 / 62**.")

# ---- item 135, form M-b: the arithmetic ---------------------------------------------------
B_F = ("*\"…a matter this section requires to be stated in it<u>, other than a matter that the "
       "provision of this section requiring it to be stated expressly excepts from this "
       "subsection</u>, may obtain\"* — **+101 characters**,")
B_R = ("*\"…a matter this section requires to be stated in it, other than a matter that the "
       "provision of this section requiring it to be stated expressly excepts from this "
       "subsection, may obtain\"* — ~~+101 characters~~ **+121 characters**, " + MARK + " on " +
       M211 + " m1: the figure was out by 20 and neither this item nor that pass could "
       "reconstruct the arithmetic that produced 101, and **the tags are dropped for the same "
       "reason as M-a**. The **+42 in D 1** this form also needs has **no drafted words in this "
       "card and remains unpriced**, so M-b's true cost is +121 plus an undrafted edit, against "
       "M-a's +115 and nothing. **A second reason to prefer M-a**, beyond the one below: M-b "
       "creates a standing invitation, because after it any future exception written anywhere in "
       "the section silently withdraws subsection M review with no reader of subsection M able to "
       "see which matters are excepted without auditing the whole section,")

# ---- item 135: the residue paragraph, which rests on the same miscount --------------------
C_F = ("**What neither form does.** Neither reaches item 7's other two propositions — the power to "
       "re-designate and the no-fault clause — because D3c's exception does not, and you left "
       "that residue to counsel's next pass. **Widening the exception to all three propositions "
       "is a third decision and it should be taken once, in both D 1 and M 2 together**, not "
       "twice in different places.")
C_R = (
    "**What neither form does — and " + MARK + ": this is not a residue and there is no third "
    "decision.** Neither form reaches item 7's other two propositions, the power to re-designate "
    "and the no-fault clause, because D3c's exception does not. **This item recorded that as a "
    "gap to be closed. It is not a gap: it is the right answer.** Those two clauses are "
    "**propositions of law**, not advice — " + M211 + " M1 establishes that item 7 carries one "
    "advisory and two propositions of law, so the certification series carries **eight "
    "propositions of law and one advisory**, not six and one. **The whole point of F3 was to "
    "except the advice from subsection M review, and the whole point of leaving the propositions "
    "of law alone is that a member or survivor should keep review of a misstated or omitted "
    "proposition of law.** Widening the exception to all three would **remove review of two "
    "propositions of law that nobody proposed to remove it from**. **So the exception correctly "
    "names the advice and only the advice, in both D 1 as enacted and in either form of this "
    "cure.** *(This extension of M1 to this item is the drafter's and not counsel's; counsel made "
    "the point against §7 item 133. If you read it the other way, say so and it is one more "
    "substitution — but it is not a defect to be fixed silently.)*")

# ---- item 135: counsel's second route, which inverts the subdivision ----------------------
D_F = ("**No cure inside D 1 can work**, because the defect is that M 2 does not look at D 1. The "
       "clause has to go in M 2.")
D_R = (
    "**No cure inside D 1 can work**, because the defect is that M 2 does not look at D 1. The "
    "clause has to go in M 2.\n\n"
    "    **" + MARK + " — " + M211 + " agreed this item and added the argument that settles it, "
    "plus a second harm this item had missed.**\n\n"
    "    **The argument that settles it: D 1 expressly disapplies M 2's second sentence, and you "
    "cannot disapply a provision that does not apply of its own force.** The disapplication is "
    "intelligible only on the premise that M 2 reaches the failure independently of D 1, so **the "
    "drafter's own words foreclose the contrary reading.** The contrary reading at its best is "
    "not *expressio unius* but the specific governing the general (*Dodson v. Potomac Mack Sales "
    "& Serv.*, 241 Va. 89 (1991)) with the presumption against surplusage (*Hubbard v. Henrico "
    "Ltd. P'ship*, 255 Va. 335 (1998)), on which the exception must do something and the only "
    "thing left is to make D 1 exhaustive. It loses structurally: **D 1 can add to subsection M "
    "by defining; it cannot subtract from subsection M except by amending subsection M.** The "
    "exception is not nugatory — it withdraws D 1's clock and D 1's disapplication — but it is in "
    "the wrong provision to do the job it was taken for, and the contrary reading is strong "
    "enough to litigate and not strong enough to rely on.\n\n"
    "    **The second harm, and it inverts the subdivision.** By carving the advice failure out "
    "of the **whole** sentence, D3c also carved it out of *\"the second sentence of subdivision M "
    "2 does not apply to such a failure where the person adversely affected is the member.\"* So "
    "**for the advice failure M 2's second sentence applies in full**: the certification is itself "
    "*\"a determination of the Board for the purposes of this subsection, whether or not another "
    "provision of this section expressly provides for review of it.\"* A member whose "
    "certification omits the advice can plead the certification as a reviewable determination — "
    "**a channel the member whose certification omits one of the propositions of law does not "
    "have**, because for her the second sentence is disapplied. **The member whose certification "
    "omits the least legally substantive of the seven items now has the widest channel of any "
    "member in the subdivision.** That is the opposite of F3's purpose and it is a second, "
    "independent reason the clause has to move to M 2.")

# ---- item 133: the scope paragraph, on the miscount --------------------------------------
E_F = ("**The alternative, if you want the strict scope, is that renumbering**; it is one cut over "
       "one sentence and it would also give the M exception a handle. §6.0-70 item 6.")
E_R = (
    "~~**The alternative, if you want the strict scope, is that renumbering**; it is one cut over "
    "one sentence and it would also give the M exception a handle.~~ §6.0-70 item 6. "
    "\n\n    " + MARK + " — " + M211 + " M1: **there is nothing to scope around and no "
    "renumbering is needed.** After F4 and F1/F2/F6/F9, **item 7 carries one advisory and two "
    "propositions of law** — the power to re-designate and the no-fault clause — so **the "
    "certification series carries eight propositions of law and one advisory, not six and one.** "
    "The instruction *\"the six propositions of law and not the advisory\"* was therefore "
    "**under-inclusive by two**, and the drafted scope *\"every matter other than the advice\"* "
    "reaches **all eight** and excepts the one — **which is exactly what the instruction "
    "intended.** The asymmetry recorded above was an artefact of the miscount and does not arise "
    "on the drafted words. **The (i)–(vii) renumbering your commission forbade is not needed for "
    "anything, and the three-way split is a solution to a problem that does not exist.** The "
    "drafted words stand unchanged at +253.")

# ---- item 133: the premise, narrowed ------------------------------------------------------
F_F = "**Both are framed on absence. Neither reaches a matter that is stated and wrong.**"
F_R = (
    "**Both are framed on absence. Neither reaches a matter that is stated and wrong.** "
    "\n\n    " + MARK + " — " + M211 + " Finding 2: **that premise is overstated, and narrowing "
    "it lowers this card's priority.** **Most misstatements decompose into omissions**, because "
    "each required matter is required *with its qualifiers*. The required matter here is *\"that "
    "the Board advises the member to review the member's designation of beneficiary\"* — and "
    "**this card's own worked example**, a template rewritten to *\"Your beneficiary designation "
    "on file with VRS will apply to this purchase,\"* **does not state that matter at all.** It "
    "is an omission; it is inside D 1's failure sentence and inside M 2's limb; and this card "
    "used it to prove a gap it does not fall into. The same holds for the propositions of law: "
    "dropping *\"only to a surviving spouse, minor child, or parent\"* from the § 51.1-162 B "
    "proposition is a **failure to state the required matter**, not a misstatement outside it. "
    "**The real gap is additive misstatement only** — the Board states the required matter "
    "correctly and adds something false beside it (*\"and your designation will lapse if you do "
    "not act before completing payment\"*). That is **narrower than this card describes and rarer "
    "than a template rewrite**, and it is worth knowing before 253 characters are spent on it.")

PATCHES = [
    dict(id="I1", label="item 135 M-a: +115 not +116, and the nesting tags dropped",
         find=A_F, repl=A_R),
    dict(id="I2", label="item 135 M-b: +121 not +101, tags dropped, the +42 unpriced",
         find=B_F, repl=B_R),
    dict(id="I3", label="item 135: the 'residue' is the right answer, not a gap",
         find=C_F, repl=C_R),
    dict(id="I4", label="item 135: the disapplication argument, and the inversion",
         find=D_F, repl=D_R),
    dict(id="I5", label="item 133: eight propositions, so no renumbering", find=E_F, repl=E_R),
    dict(id="I6", label="item 133: the premise narrowed to additive misstatement",
         find=F_F, repl=F_R),
]


def item(b, num):
    i = b.index(f"\n{num}. ")
    m = re.search(r"\n\d{3}\. ", b[i + 6:])
    return b[i:i + 6 + m.start()] if m else b[i:]


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live = doc["body"], doc["latestRevisionId"]
    print(f"live: revision {live} (number {doc.get('latestRevisionNumber')}), {len(body)} chars")

    for p in PATCHES:
        c = body.count(p["find"])
        assert c == 1, f"{p['id']} ({p['label']}): FIND resolves {c}x, expected 1"
    out = body
    for p in PATCHES:
        out = out.replace(p["find"], p["repl"], 1)
        print(f"   {p['id']}: {p['label']}  {len(p['repl']) - len(p['find']):+d}")

    # Post-conditions: the drafted WORDS of both cards are untouched; only description moves.
    for num in ("133", "135"):
        print(f"   item {num}: {len(item(body, num))} -> {len(item(out, num))} chars")
    # M-a's corrected READ must be present, untagged, and the tagged form gone.
    ok = ("other than a failure to state that the Board advises the member to review the member's "
          "designation of beneficiary, may obtain")
    assert out.count(ok) == 1, f"M-a's corrected untagged READ occurs {out.count(ok)}x"
    # The defective tagged READ is preserved verbatim, per the convention that a correction does
    # not rewrite the original away — but it must be unmistakably dead, or someone lifts it.
    bad = ("to be stated in it<u>, other than a failure to state that the Board advises the "
           "member to review the member's designation of beneficiary</u>, may obtain")
    assert out.count(bad) == 1, f"M-a's nesting READ occurs {out.count(bad)}x, expected 1 struck"
    k = out.index(bad)
    assert "~~" in out[k - 60:k] and "~~" in out[k:k + len(bad) + 60], \
        "M-a's nesting READ is not struck through — it could be lifted from the card"
    assert "<u>" not in out[out.index(ok) - 200:out.index(ok)], \
        "M-a's corrected READ has a tag near it"
    # The drafted +253 limb in item 133 is untouched.
    kept = ("or the statement in the Board's certification of any matter this subdivision "
            "requires to be stated in it")
    assert body.count(kept) == out.count(kept) == 1, "item 133's drafted limb moved"
    assert out.count("\n136. ") == body.count("\n136. "), "item count moved"
    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    print(f"   document {len(body)} -> {len(out)}  ({len(out) - len(body):+d}) | "
          f"headroom {CEILING - len(out)}")

    if "--dry-run" in sys.argv:
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out-items-72.md"),
             "w", encoding="utf-8").write(out)
        print("DRY RUN — nothing sent")
        return

    title = doc.get("title") or ""
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title[:300], "format": "markdown", "body": out,
                   "baseRevisionId": live})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:600]}")
        sys.exit(2)
    if res.get("body") != out:
        print("WRITE RETURNED A DIFFERENT BODY — treat as failed")
        sys.exit(2)
    print(f"WRITE OK — revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(res['body'])} chars")


if __name__ == "__main__":
    main()
