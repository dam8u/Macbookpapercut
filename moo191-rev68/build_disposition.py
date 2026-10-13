#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build `moo195-disposition` on MOO-191 from the live base. Nothing here writes to the store.

Every character count, every anchor count, every passage and every reconstruction in the output is
computed from the live `bill-text-s8` body at the moment this runs. The prose is mine; the text is
the document's. Run:

    python3 build_disposition.py > disposition.md
"""
import re, sys

sys.argv = [sys.argv[0]]
src = open("candidates.py", encoding="utf-8").read().replace("sys.exit(main())", "")
ns = {"__name__": "cand"}
exec(compile(src, "candidates.py", "exec"), ns)

get, sec1, C = ns["get"], ns["sec1"], ns["C"]
MOO42, KEY, series_of, shape = ns["MOO42"], ns["KEY"], ns["series_of"], ns["shape"]
ADV = ns["ADV"]

from markdiff import mark, check  # noqa: E402

FAIL_A = "A failure to state in the Board's certification"
FAIL_Z = "The member shall file the notice of retirement required by § 51.1-153"
SERIES_A = "The Board's certification shall also state that,"
TITLE_FIND = "pilot program; post-retirement employment; reports."
TITLE_T1 = "pilot program; death benefits; post-retirement employment; reports."
TITLE_T2 = ("pilot program; death benefits; designation of beneficiary; post-retirement "
            "employment; reports.")


def failure_of(s):
    return s[s.index(FAIL_A):s.index(FAIL_Z)]


PASSAGE = (("the certification series of subdivision D 1, in full as it would read", series_of),
           ("subdivision D 1's failure sentence, in full as it would read", failure_of))

doc = get(f"/api/issues/{MOO42}/documents/{KEY}")
body = doc["body"]
S1 = sec1(body)
REV = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", body, re.M))
DOCREV = doc["latestRevisionId"][:8]
CAND = {c["id"]: c for c in C}

# ---- invariants of the base, asserted before a word of the document is written ----------------
REGION = S1[S1.index(SERIES_A):S1.index(FAIL_Z)]
assert REGION.count("<u>") == REGION.count("</u>") == REGION.count("~~") == 0
assert S1.count("<u>") == S1.count("</u>") == 62
assert S1.count(ADV) == 1 and body.count(ADV) == 3
assert body.count(TITLE_FIND) == 1
ITEMS0, AT0 = shape(S1, ns["ADV_OPEN"])
assert (ITEMS0, AT0) == (7, 5)

TITLE_LINE = re.search(r"^\*\*A BILL to amend.*$", body, re.M).group(0)
assert TITLE_FIND in TITLE_LINE

CAVEAT = ("**Internal working draft. Not a Division of Legislative Services bill, not cleared by "
          "counsel or by DLS, not legally sufficient for introduction. Pre-decisional and "
          "internal.**")

# ------------------------------------------------------------------ per-decision prose ----------
# Each entry: the decision heading, the candidates in it, what I recommend, and the case against.
DECISIONS = [
    dict(n=1, finding="F1", sev="Serious", ids=["D1"],
         head="Give the advice an object",
         what="""The advisory tells the member to look and does not tell her what she is looking at.
§ 51.1-162 B rewards doing nothing and punishes doing the wrong thing: the member who has filed no
designation is paid through branch two, in the order of precedence, while the member who has
designated a non-qualifying person is paid by neither branch. The advisory urges action without
saying which, so a member with no designation who reads it and acts can destroy the protection she
already had. Counsel's Ms R scenario is the concrete case and the 137 characters are its but-for
cause.""",
         rec="""**Take it.** This is the only finding on which the enacted words can cause the harm
they exist to prevent, and store revision 67 has already done the hard half of the work: item 4 of
the series now states **both** branches of § 51.1-162 B, so the certification contains the
predicate and D1 only points the member at it. The addition creates no duty, adds no defined term,
invents no mechanism and states nothing that is not already in the section it cites. *"That
section"* resolves to § 51.1-162, which is named earlier in the same item.""",
         against="""Seventy-two more characters in an item that is already the densest in the
series, and a member who is told to consider *"the effect of that designation under subsection B"*
still has to go and read subsection B to find out what the effect is. The alternative — spelling
the trap out in the certification — is a much larger addition and was not asked for."""),
    dict(n=2, finding="F2", sev="Serious", ids=["D2b", "D2a", "D2c"],
         head="The terminus of the advice",
         what="""*"Before completing payment"* is the act's own phrase and it is the wrong deadline
for this advice. Subdivision G 5 makes the completion of payment the last moment the **purchase**
can be undone, which is why the phrase was chosen; nothing in § 51.1-162 A fixes a **designation**
at that moment. A designation is revocable until the member dies. The window in which
redesignating changes the § 51.1-162 outcome runs about 27 months on the act's own dials and
without end for a member who does not retire, so the advice expires at the first of four legs. The
recorded second reason for the deadline at §6.0-65 item 5 was not true and **was withdrawn at store
revision 68**; the first reason stands.""",
         rec="""**Take D2b.** D2a is counsel's wording verbatim and I do not recommend it: with
F1's object inserted, *"under that subsection"* takes *"subsection B of that section"* as its
nearest antecedent, and the power to designate is in **A**. D2b is the same policy with the
referent named — a repair, not a change. **D2c is the same policy if F1 is declined**, where
*"that subsection"* is safe because subsection A of § 51.1-162 is then the only subsection named in
the item before the pronoun.""",
         against="""The longest addition of the three live options, and it states a power the
member already has under a section the act does not amend for this purpose. A reader could ask why
the certification recites § 51.1-162 A's revocability but not the rest of it. Against that: the
present words carry an implicature that completing payment does something to the designation, and
it is false — store revision 62 was cut to stop the certification misleading her."""),
    dict(n=3, finding="F3", sev="Serious", ids=["D3c", "D3b", "D3a"],
         head="The channel — the question the Director reserved at MOO-188 §3.4",
         what="""D 1's failure sentence reaches *"every matter this subdivision requires to be
stated"*, so omitting the advisory is reviewable under subsection M and reportable under subsection
J. The Director accepted that, did not except the advisory, and asked whether the channel is worth
more argument than the advice is worth. **Counsel's answer is: keep the subsection J limb, drop the
subsection M limb** — because M review's only possible output is a remand that cannot give the
claimant anything, § 2.2-4029 barring the court from supplying the designation itself, while the J
report gives the money committees the same fact at no litigation cost and with no claimant needed.
Counsel also states the honest counter: an advisory excepted from M review is enforceable by
nobody.""",
         rec="""**This one is policy and I make no recommendation on whether to take it.** It
reverses a decision the Director took deliberately, and the trade — an unenforceable advisory
against a disproportionate litigation surface — is theirs. **On drafting, if it is taken, take
D3c.** D3a is counsel's single substitution and has two defects: it says *"is not a failure for the
purposes of subsection M"* in the sentence immediately after the one deeming it a failure, so the
subdivision asserts both in consecutive sentences, and it turns on *"the advice this subdivision
requires to be stated"*, an operative term the subdivision nowhere defines. D3b cures both but
excepts *"the advice described in the next sentence"* — a cross-reference by position, which breaks
if any later revision inserts a sentence between the two, and then defines the advice in a closing
sentence to make the position work. **D3c carves the exception into the deeming clause itself and
names the matter in the subdivision's own words, so it needs neither the position nor the
definition, and it is 131 characters shorter than D3b.**""",
         against="""All three forms create a two-tier failure sentence, where six of the seven
matters are reviewable and the seventh is not, and a reader has to hold both tiers in mind. If the
Director would rather not have the tier at all, the alternative is to decline F3 and take **D6**
(decision 6), which closes the fault argument that the live channel is most likely to produce."""),
    dict(n=4, finding="F4", sev="Moderate", ids=["D4"],
         head="Placement — move the advisory to the end of the series",
         what="""Item 4 of the series ends by pointing forward to *"subsection C of that section"*
and item 6 is what explains subsection C. Before store revision 65 those two sat adjacent; the
advisory is now wedged between a forward reference and its resolution. Independently, the advisory
is about the **subsection A** designation and the only item that says what subsection A does is
item 7, which now follows it — so the member is told to review her designation under subsection A
two items before she is told what subsection A provides.""",
         rec="""**Take it, and note that it reverses a recorded decision of yours.** The issue
description's point 2 and §6.0-65 item 2 placed the advisory immediately after the § 51.1-162 B
proposition on the reasoning that the advice must be its own semicolon item and visibly advice.
**D4 preserves both of those properties** — it is still its own item, still introduced by
*"that"*, still the only item in a different register — and it moves it next to the subsection A
item, which is the one it is about. **It costs zero characters**: the relocation is exactly
offsetting, which I verified rather than assumed.""",
         against="""The advisory then closes the series, which gives the least legally substantive
item the most emphatic position, and a template editor reading top to bottom meets the six
propositions first. That is arguably the opposite of what F5 asks for. The counter is that the
closing position is also where a reader looks for what to do next."""),
    dict(n=5, finding="F5", sev="Moderate", ids=["D5"],
         head="A route for the advice",
         what="""The advisory names no manner, no form, no office and no enclosure. § 51.1-162 A
says the designation *"must be made in a manner prescribed by the Board"*, so the route exists in
Board procedure, and nothing in § 51.1-142.4 requires the Board to put it in front of the member at
the moment it compels the advice. The cheapest compliance path is to drop the 137 characters in as
paragraph 7 of 7 in the same register as the six propositions of law, where a member reads past
it.""",
         rec="""**Hold it, and I flag a consequence the Director should weigh before deciding.**
D5 is the light form: a **Board** duty to state the manner, which keeps the advisory's no-duty
property. But it adds a new matter inside subdivision D 1, so **D 1's failure sentence reaches it
too** — taking D5 while declining F3 enlarges exactly the channel F3 is about, by a matter that is
administrative detail. D5 and D3c compose cleanly; D5 alone does not. **The heavier form counsel
names — adding the designation review to the written acknowledgment D 1 already requires before the
Board may accept an election — is not drafted here**, because it moves the advisory measurably
closer to a member obligation and MOO-188 §3.3 deliberately avoided that. I will draft it on
instruction; I will not choose it.""",
         against="""Against holding: nominal compliance really can defeat the whole advisory, and
D5 is the cheapest thing that makes the route visible. Against taking: it compels an administrative
particular in a statute and enlarges the failure sentence."""),
    dict(n=6, finding="F6", sev="Moderate", ids=["D6"],
         head="The no-fault clause",
         what="""*"Is advised to review … before completing payment"* creates no duty, but advice
with a deadline attached is the raw material for a fault argument, and the General Assembly will
have enacted the words. The concrete case is a sentence in a Board reconsideration decision — *"The
certification advised the member to review her designation … She did not"* — which is legally
irrelevant to a statutory entitlement but rhetorically decisive in the one forum where the Board
decides.""",
         rec="""**Conditional, and the condition is decision 3.** Counsel would not spend the
characters unless F3's M-limb exception is declined, and I agree. **Decline D6 if you take D3c;
take D6 if you decline F3.** If the advisory stays reviewable under subsection M, the fault
argument is worth closing for 156 characters; if the M limb is gone, the forum in which the
argument bites is largely gone with it.""",
         against="""156 characters to rebut an argument with no doctrinal footing, and a
no-fault clause invites the question of why the other six items do not need one. It also states a
negative, which lengthens an item that F1 and F2 are already lengthening."""),
    dict(n=7, finding="F9", sev="Minor", ids=["D9"],
         head="Name the actor",
         what="""*"That the member **is advised** to review"* is a passive with no human actor: the
carrier sentence's subject is *"The Board's certification"*, a document. Read strictly the item is
a statement of fact that advice was given rather than the giving of it, and it is the only item in
a seven-item list of propositions of law that is self-verifying — true because the Board states
it.""",
         rec="""**Take it.** Seven characters. This is the one finding that is a defect against my
own drafting rule rather than a policy judgement: name the actor in every duty, and do not use a
passive where the actor matters. *"The Board advises the member to review"* keeps every no-duty
property, because *"advises"* is the Board's verb and imposes nothing on the member. It does change
words you approved verbatim at MOO-188 §3.3, which is why it is here and not applied.""",
         against="""Your recorded reason at §6.0-65 item 1 — that the operative verb belongs to
the Board's carrier sentence, so the actor, the addressee, the writing and the moment are already
named — is a good pragmatic answer, and counsel rated the finding minor on the strength of it. If
you prefer the enacted words, nothing breaks."""),
]

COMBINED = [
    dict(ids=["DALL"], head="F1, F2, F6 and F9 in one item, at the present position"),
    dict(ids=["DALL4"], head="F1, F2, F6 and F9 with F4's relocation"),
]


def sentences(out):
    """Whether the candidate changes how many sentences subdivision D 1 contains."""
    d = out.count(". ") - S1.count(". ")
    if d == 0:
        return "no sentence longer or shorter"
    return f"{'one' if abs(d) == 1 else abs(d)} sentence{'' if abs(d) == 1 else 's'} " + \
           ("longer" if d > 0 else "shorter")


def render(cid):
    """One candidate: its edits verbatim, the counts taken, and every touched passage in full."""
    c = CAND[cid]
    out = S1
    rows = []
    for find, read in c["edits"]:
        n_doc, n_1 = body.count(find), out.count(find)
        assert n_1 == 1, f"{cid}: anchor resolves {n_1}x in §1"
        rows.append((find, read, n_doc, n_1))
        out = out.replace(find, read, 1)
    items, at = shape(out, c["probe"])
    print(f"#### Candidate {cid} — {c['finding']} — **{len(out) - len(S1):+,} characters** "
          f"(§1 {len(S1):,} → {len(out):,})\n")
    for k, (find, read, n_doc, n_1) in enumerate(rows, 1):
        lead = f"**Substitution {k} of {len(rows)}.** " if len(rows) > 1 else "**Substitution.** "
        print(lead + f"FIND is {len(find):,} characters and resolves **{n_1}× in §1** "
                     f"({n_doc}× in the document"
              + ("; the others are record quotations at §0.0-65, §0.0-68 and §8, so the "
                 "substitution is scoped to §1" if n_doc > 1 else "") + ").\n")
        print("- **FIND**\n\n  ```\n  " + find + "\n  ```\n")
        print("- **READ**\n\n  ```\n  " + read + "\n  ```\n")
    for label, span in PASSAGE:
        old, new = span(S1), span(out)
        if old == new:
            continue
        marked, was, amended = mark(old, new)
        check(marked, was, amended, old, new)
        print(f"**{label[0].upper() + label[1:]}.**\n")
        print("> " + marked.replace("\n", " ") + "\n")
    print(f"*After: the series has {items} items and the advisory is item {at} of {items}; "
          f"`<u>`/`</u>` {out.count('<u>')} / {out.count('</u>')}, unchanged; no figure moves, no "
          f"designator is renumbered, no section joins or leaves the act, no defined term is added "
          f"and the subdivision is {sentences(out)}.*\n")
    if c["note"]:
        print(f"*Drafting note on this candidate: {c['note']}.*\n")


# ===================================================================== the document =============
print(f"""# MOO-191 — disposition of [MOO-195](/MOO/issues/MOO-195)'s pass 21 on the designation-review advisory

{CAVEAT}

**Base: store revision {REV}, document revision `{DOCREV}`.** §1 is **{len(S1):,}** characters with
`<u>`/`</u>` at **{S1.count('<u>')} / {S1.count('</u>')}**; the certification series of subdivision
D 1 has **{ITEMS0} items** and the advisory is item **{AT0} of {ITEMS0}**. Every count, anchor,
passage and character movement below was computed against that base at the moment this document was
built, and every anchor was re-counted in the document and in §1 separately. **An anchor counted
yesterday is not an anchor**, and the base has moved three times since the pass was written — store
revisions 66, 67 and 68, with **67 amending subdivision D 1 itself**.

## 0. What this document is, and what it is not

Pass 21 returned **11 findings — 0 fatal, 3 serious, 5 moderate, 3 minor — and 11 null results**.
Two of them were about statements in my own record rather than the enacted words, and **those are
already corrected, in place and marked, at store revision {REV}**, which is record-only. Two more
are carded. **The remaining seven each reverse or widen a word the Policy Director approved
verbatim at [MOO-188](/MOO/issues/MOO-188) §3.3 and §3.4. They are drafted here word for word,
re-verified, and enacted nowhere.** Choosing among them is the Director's and not mine; drafting
them, and telling you where counsel's own words would not survive a drafter's reading, is mine.

**How to read a candidate.** Each gives the FIND and READ strings verbatim, the counts I took, the
character movement, and then the affected passage **in full as it would read** — not the changed
fragment. Nothing here is applied to the store.

**The marking convention, and why it is not underline and strikethrough.** Subdivision D 1 sits
inside an open `<u>` run: § 51.1-142.4 is a new section, so it is new language underlined end to
end in the bill text, and the passage carries no marker of its own (asserted before this document
was written: 0 `<u>`, 0 `</u>` and 0 `~~` from the series' first word to the failure sentence's
last). Underlining a candidate's addition there would nest a marker inside a marker, and striking
one would read as language deleted from the **Code** rather than from the **draft**. So each
candidate's own delta is marked **[ADDED: …]** and **[STRUCK: …]** *against the draft*, and the
`<u>`/`</u>` balance is reported for each. **In the bill as introduced, every word of these
passages is underlined.** Each marking is asserted to reconstruct both the live text and the
post-edit text exactly; a candidate that failed that assertion would not appear.

## 1. Disposition of all eleven findings

| # | Sev | What counsel found | Disposition |
|---|---|---|---|
| **F1** | Serious | The advisory can cause the loss it exists to prevent | **Drafted, not enacted** — decision 1, candidate D1. I recommend taking it |
| **F2** | Serious | *"Before completing payment"* is the wrong terminus, and the recorded reason was untrue | **Record corrected at store revision {REV}**; text **drafted, not enacted** — decision 2, candidates D2b (recommended), D2a, D2c |
| **F3** | Serious | The channel: keep subsection J, drop subsection M — **the Director's reserved question** | **Drafted, not enacted** — decision 3. No recommendation on whether; **D3c on how** |
| **F4** | Moderate | The placement splits the series' only forward reference from its resolution | **Drafted, not enacted** — decision 4, candidate D4, at zero characters. I recommend taking it |
| **F5** | Moderate | Advice with no route; nominal compliance defeats it | **Light form drafted, not enacted** — decision 5, candidate D5. I recommend holding it. The acknowledgment form is **not** drafted: it moves toward a member obligation, which MOO-188 §3.3 avoided |
| **F6** | Moderate | A contributory-fault argument in the forum where the Board decides | **Drafted, not enacted** — decision 6, candidate D6. Conditional on decision 3 |
| **F7** | Moderate | The failure sentence catches omission and misses misstatement | **Carded** as §7 item 133, new at store revision {REV}, drafted in full and enacted nowhere. Not in the scope of a cut commissioned as one edit, and it is a property of a sentence approved at store revision 62 |
| **F8** | Moderate | Title and single object, Va. Const. art. IV, § 12 | **Ripe, and larger than the pass thought** — the title was opened at store revision 67. The cure is **drafted** at §6 below, for the Director and for the Editor's risk section |
| **F9** | Minor | A passive with no human actor: the advisor named is a document | **Drafted, not enacted** — decision 7, candidate D9, at seven characters. I recommend taking it |
| **F10** | Minor | The record sent the channel question to the wrong card | **Applied** at store revision {REV}. §6.0-65 item 6 repointed from MOO-192 to [MOO-195](/MOO/issues/MOO-195), and the answer recorded. Nothing outstanding |
| **F11** | Minor | The issue description overstated §5.43's vocabulary claim | **Applied** at store revision {REV}. §5.43 direction 1 given the precision; **no text change required** — the compound is new to the act and to § 51.1-162 and is still the right noun. Nothing outstanding |

**The eleven null results are not reproduced here.** They are in the pass at
[MOO-195](/MOO/issues/MOO-195) and I accept them as stated. **N2** and **N3** are the two that
carry weight for drafting: no short-form referent crosses the insertion, and the no-duty reading of
*"is advised to"* is secure.

## 2. What store revision {REV} already did, so it is not re-litigated here

Store revision {REV} is **record-only**: §1 is character-for-character what store revision 67 left,
and the apply script asserted that before it wrote. It made **four corrections to records I wrote
at store revision 65** — §6.0-65 item 5's false second reason for the deadline, withdrawn (F2);
§6.0-65 item 6's wrong card, repointed (F10); §5.43 direction 1's vocabulary claim, given its
precision (F11); and §5.43 check 4, which was spent and had conflated two things (N8) — and added
**two new §7 items**, 133 for F7 and 134 closing item 129's conservator residual. **No enacted word
was changed, added or struck.**

Two things store revision 67 changed about the findings, which I restate because they change what
you are deciding:

1. **F1 is weakened and not cured.** Item 4 of the series now states both branches of § 51.1-162 B.
   The certification therefore does tell the member the no-designation rule, one item before the
   advice. **It still does not tell her that designating a non-qualifying person destroys that
   rule**, which is the whole of F1's harm.
2. **F8 is ripe and larger.** The title was opened at store revision 67 and now reads *"to amend
   and reenact §§ 51.1-142.2 **and 51.1-162** of the Code of Virginia"*, so the act amends a
   death-benefit section on its face — while the *"relating to"* clause still names no death
   benefit, beneficiary or designation.

## 3. The seven decisions""")

for d in DECISIONS:
    print(f"\n### Decision {d['n']} — {d['finding']} ({d['sev']}): {d['head']}\n")
    print("**What counsel found.** " + " ".join(d["what"].split()) + "\n")
    print("**My recommendation.** " + " ".join(d["rec"].split()) + "\n")
    print("**The case against, stated because you are the one deciding.** "
          + " ".join(d["against"].split()) + "\n")
    for cid in d["ids"]:
        render(cid)

print("""## 4. The combined takes

If you take more than one of F1, F2, F6 and F9, they belong in **one** item rather than in
successive cuts: each of D1, D2b, D2c and D6 substitutes on the same FIND string, so applying two
of them in sequence would leave the second with a dead anchor. The two combined candidates below
carry all four at once. **DALL4 is DALL plus F4's relocation at zero marginal characters**, and if
you take F4 at all, the other findings must be applied at the **new** position rather than the old
— which is what DALL4 does.""")

for d in COMBINED:
    print(f"\n### {d['head']}\n")
    for cid in d["ids"]:
        render(cid)

# ------------------------------------------------------------------ F8, the title --------------
t1 = body.replace(TITLE_FIND, TITLE_T1, 1)
t2 = body.replace(TITLE_FIND, TITLE_T2, 1)
assert body.count(TITLE_FIND) == 1
print(f"""## 5. F7 — carded, not cut

The misstatement limb is **§7 item 133**, new at store revision {REV}, where the words are drafted
in full and enacted nowhere. I did not cut it here for three reasons, each of which I would give
again: it is a property of the failure sentence the Director approved at **store revision 62**, not
of the 137 characters this cut added; it reaches all seven matters and not only the advisory, so it
is not within a commission of one edit; and it **interacts with decision 3** — an advisory excepted
from subsection M review needs no misstatement limb either, and the limb would then reach only the
six propositions. **Decide F3 first.**

## 6. F8 — the title, drafted

The act's title line, live at store revision {REV}:

> {TITLE_LINE}

The clause names no death benefit, no beneficiary and no designation, while subdivision D 1 now
compels seven statements about §§ 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 and the act amends
§ 51.1-162 on its face. Counsel rates a Va. Const. art. IV, § 12 challenge **unlikely to succeed**
— Virginia construes the clause liberally and sustains a title that gives fair notice and does not
mislead, *Dean v. Paolicelli*, 194 Va. 219 (1952) — and worth disclosing because the cure is free.
**I agree, and I add that the cure is now cheaper than disclosure**: the title is already open.

The anchor resolves **{body.count(TITLE_FIND)}× in the document**. Two candidates, and the title
line is not inside a `<u>` run, so it is shown plainly:

- **FIND**: `{TITLE_FIND}`
- **T1**, minimal, **{len(TITLE_T1) - len(TITLE_FIND):+d} characters**: `{TITLE_T1}`
- **T2**, full, **{len(TITLE_T2) - len(TITLE_FIND):+d} characters**: `{TITLE_T2}`

**I recommend T2.** The object the act now embraces is not only the payment of a death benefit but
the member's designation of one, which is what subdivision D 1's seven statements and the advisory
are about; a title that names the benefit and not the designation gives fair notice of six of the
seven items. T1 is the smaller footprint and I would not resist it. **Either is a change to the
title line, which is not within this commission, so neither is applied** — and the Editor needs the
risk section either way.

## 7. Cross-reference check — performed, result: no conforming amendment needed by any candidate

| What I checked | Result |
|---|---|
| Sections cited by any candidate | § 51.1-162 subsections A, B and C, and subsections J and M of § 51.1-142.4. **Every one is already cited in §1**; no candidate cites a section the act does not already reach, so no section outside the act is touched and nothing is stranded |
| Short-form referents crossing an insertion | **None.** *"That section"* in D1, D2a and D2b resolves to § 51.1-162, named earlier in the same item; *"that subsection"* in D2a resolves to **subsection B**, which is why D2b exists and D2a is not recommended; *"that subsection"* in D2c resolves to subsection A of § 51.1-162, the only subsection named in the item before the pronoun |
| References by position | **One, and it is why D3c exists.** D3b excepts *"the advice described in the next sentence"*, which breaks if any later revision inserts a sentence between the two. D3c names the matter in the subdivision's own words and needs no position |
| Undefined operative terms | **One, and it is why D3c exists.** D3a turns on *"the advice this subdivision requires to be stated"*, which the subdivision nowhere defines. No candidate adds a defined term, and none uses a second word for a concept the act already names |
| Anchors of the other open cuts | Re-counted over §1 **after** each candidate's substitution. No candidate disturbs any of them; the series stays at seven items in every case and the `<u>`/`</u>` balance is unchanged in every case |
| D 1's failure sentence | Reaches *"every matter this subdivision requires to be stated"*, so **D5 adds a matter to it** and D3a, D3b and D3c take one out of its subsection M limb. That is the F3/F5 interaction, stated at decisions 3 and 5 rather than drafted around |
| Subsection J's catch-all | *"Every other matter this section requires the Board to state in that report"* picks up every candidate's reporting limb; nothing is stranded |

## 8. Drafter's note

**Structure choices.**

1. **Nothing is applied.** The commission was one edit, that edit is cut as store revision 65, and
   each of the seven findings reverses or widens a word approved verbatim at
   [MOO-188](/MOO/issues/MOO-188) §3.3 or §3.4. Choosing among them is policy; drafting them is
   not. Where I think the drafting is wrong I say so and offer the repair, and where the choice is
   yours I say that too.
2. **Candidates are grouped by decision, not by finding**, because F1, F2, F6 and F9 all substitute
   on the same FIND string and cannot be applied independently in sequence. The combined takes at
   §4 exist for that reason, not for convenience.
3. **Each passage is reproduced in full as it would read** — the certification series, or the
   failure sentence, or both where a candidate touches both — rather than as a changed fragment,
   because the test of this text is whether a reader understands the rule without the note.
4. **The whole series is given rather than the single item**, because four of the thirteen
   candidates move or re-point material between items and an item shown alone would hide that.

**Ambiguities I resolved, and how.**

1. **How to mark a delta inside an already-underlined section.** `<u>` and `~~` are the act's
   markers against the **Code**. Subdivision D 1 is inside an open `<u>` run, so using them for a
   candidate's own delta would either nest a marker or assert a deletion from the Code that is not
   happening. **Resolved:** ADDED/STRUCK brackets against the draft, the convention stated at the
   head, and the `<u>`/`</u>` balance reported for every candidate. I record this because the first
   rendering of these candidates used `<u>` and `~~` inside the run and produced markup no drafter
   would accept.
2. **D2a's *"that subsection"*.** Counsel's verbatim words are ambiguous once F1's object is
   inserted before them, because the nearest antecedent becomes subsection B and the power is in A.
   **Resolved:** D2b names the subsection and is recommended; D2a is reproduced as counsel wrote it
   so the choice is visible, not silently improved.
3. **F2 without F1.** D2a and D2b both carry F1's words inside them, so neither could be applied if
   F1 is declined. **Resolved:** D2c drafts F2 alone, with the referent checked for that case.
4. **D3b's reference by position and its undefined term.** **Resolved:** D3c, which excepts the
   matter in the subdivision's own words. This is the one place I have drafted beyond what counsel
   proposed, and it is a drafting repair within counsel's own policy, not a different policy.
5. **Where F4 leaves the other candidates.** Taking F4 and then one of F1, F2, F6 or F9 against the
   old position would leave a dead anchor. **Resolved:** DALL4 applies all of them at the new
   position, and §4 says so.
6. **Whether to draft F5's acknowledgment form.** It is the cheapest real fix and it moves the
   advisory toward a member obligation, which MOO-188 §3.3 deliberately avoided. **Resolved:** not
   drafted, named as available, and I will draft it on instruction. I am not resolving a policy by
   drafting choice.
7. **Whether to cut F7 and F8 here.** Both reach text outside the 137 characters. **Resolved:** F7
   is carded as §7 item 133 and F8's cure is drafted at §6 but not applied, both with reasons.

**Open questions for the Policy Director.**

1. **Decision 3 is the gate.** F3 governs whether D6 is worth its characters and whether F7's
   misstatement limb reaches the advisory at all. **Please decide F3 first**; D5's consequence also
   turns on it.
2. **Decision 5.** Hold D5, take D5 with D3c, or instruct me to draft the acknowledgment form?
3. **Decision 4 reverses your recorded placement decision.** It costs nothing and preserves both
   of your stated reasons, but it is your decision to unmake.
4. **F8's title cure** is a change to the title line and therefore outside this commission.
   Instruct, and it goes in the next revision that opens the title; the Editor needs the risk
   section regardless.
5. **Decision 7 changes four of your approved words.** Seven characters, and I recommend it, but
   your recorded reason for the present words is a good one.

## 9. Reproducing this

In `moo191-rev68/` at the repository root. `candidates.py` re-counts every anchor on the live base
and reports each candidate's movement and the shape of the series; `markdiff.py` does the word-level
marking and asserts that each marking reconstructs both the live and the post-edit text;
`markup2.py` prints the passages alone; `build_disposition.py` builds this document. **None of them
writes to the store.** `markup.py` is superseded — it diffed character by character and printed two
candidates with no marking at all.

```
python3 candidates.py          # anchors, counts, movement, series shape
python3 build_disposition.py   # this document
```

## 10. Caveat

""" + CAVEAT)
