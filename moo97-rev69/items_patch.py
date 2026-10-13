#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 69 — the patches to `bill-text-s8-item-list`.

Three things: item 130's stale annotation is REPLACED (held -> declined), item 132 is marked with
the card's result, and items 132, 133 and 134 are moved out of the retained-record subsection and
back into the live list. The move is done in apply.py, which asserts §7 contiguous 1 to 134 and
the last live item preceding the "### 7.1" heading both before and after.
"""

# --- slice replacements: (start marker, end marker) -> replacement ----------
SLICES = []


def sl(_id, label, start, end, repl, must_contain=None):
    SLICES.append(dict(id=_id, label=label, start=start, end=end, repl=repl,
                       must_contain=must_contain))


ITEM130 = """    **ANNOTATION, store revision 69 — route (b) is DECLINED by the Policy Director, as a decision and not by implication, and so is (b) + (c). This annotation REPLACES store revision 67's, which recorded the recommendation as *held*: a record that says *held* against a decision that says *declined* is a defect of the record.** The declination is of 13 October 2026, out of [MOO-164](/MOO/issues/MOO-164), with the reasoning at [`moo164-policy-director-disposition`](/MOO/issues/MOO-164#document-moo164-policy-director-disposition) §6.

    - **The ground is incidence.** Subdivision G 4's *"a failure of the Board to act upon such a request … shall not extend that aggregate"* caps **the Board's own** clocks, so there those words make the Board bear its own delay. Subdivision M 2 clause (ii)'s aggregate caps **the member's** tolling, so the identical words make the **member** bear it. **The form is conserved and the effect reverses.** Route (b) must never be drafted on any issue or in any store revision, and **must never be written up as a conforming amendment.** The standing statement is [`standing-drafting-directions`](/MOO/issues/MOO-97#document-standing-drafting-directions) Part A5.
    - **Route (b) also buys less than this item's own table said, and the Director's note corrects it.** The subdivision D 4 / D 5 filing-date retention and the 15-day duty to act on the application are **one sentence, 112 characters apart, and it is the sentence *after* clause (ii)** — so **no amendment confined to clause (ii) reaches either limb on any reading.** Route (b) could only ever have bought limb (i), and limb (i) is already bounded: **m8-a**, enacted at store revision 67, closes clause (ii) with *"provided that the aggregate of all periods so excluded shall not exceed 90 days"*, so the member's tolling is bounded at 120 days plus at most 90 instead of running without end, **and the incidence is not reversed — she can never lose her qualifying retirement through the Board's delay.**
    - **Route (c) is adopted instead**, in [MOO-164](/MOO/issues/MOO-164): candidate 164-7 with the trigger limb (B) that revision 5 found had been dropped. It reaches all three remaining limbs and moves no figure. **Why not (b) + (c), which was the real question:** clause (ii) would be bounded twice, by two instruments for one concept, the second drafted as an exception to the first — and the only case (b) uniquely covers is the case where unbounded tolling **favours** the member, whose floor MOO-164's Edit 164-4 already protects without any filing by anyone.
    - **Limb (iv) is answered as to the date and not as to the remedy.** Candidate 164-7-B is taken, so the request class under the definition of *"final qualifying retirement date"* in subsection A gets a determinate date too. **It still has no deemed denial and therefore no case decision**, where the reconsideration class has one. The Director has carded that asymmetry and **it is being drafted nowhere.**
    - **[MOO-92](/MOO/issues/MOO-92)'s third residual — M 2's uncapped tolling, which is what this item is — is closed by this decision.** Nothing in it is open to the Drafting Specialist and nothing is drafted for it. **One mechanical consequence for anyone holding a cut against this clause: a FIND ending *"...before the Board acts upon the request."* with a trailing full stop no longer resolves**, because m8-a appends to that sentence. Re-derive it against the live body."""


sl("I1",
   "item 130 — the stale HELD annotation is replaced by the declination",
   "    **ANNOTATION, store revision 67 — the recommendation in this item is HELD by the Policy "
   "Director, and limb (i) is now backed by a different device.**",
   "Re-derive it against the live body.",
   ITEM130,
   must_contain="it is held, not declined")


ITEM132_ADD = """

    **ANNOTATION, store revision 69 — THE CARD IS ANSWERED AND THREE OF THE FOUR ANSWERS ARE IN THE TEXT.** The Policy Director accepted **f1-b**, **f4-a**, **f14-move** and **f11-authority** at **18:35:16 UTC on 12 October 2026** (card `829fa6d2`). Store revision 69 enacts the three that are drafting, in five substitutions: subdivision G 4 (three) and subsections B and L (one each). Record: §0.0-69, sweep §5.46, drafter's note §6.0-69 of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8).

    - **f1-b — enacted, with the Director's words reproduced verbatim and two conforming limbs added, each recorded at §6.0-69 items 2 and 3 and each reversible in one substitution.** (i) *"that is not a qualifying retirement"*, without which the exception — confined only by *"for the purposes of this subdivision"* — reached **a member who retired in a qualifying retirement** and pulled a retiree out of § 51.1-163, which is the class [MOO-161](/MOO/issues/MOO-161)'s F1 rated fatal and the class the standing direction protects. (ii) *"and for those purposes the member shall not be treated as having retired before the date of death in such a retirement"*, because the approved words define the **noun** *"a retirement before the date of death"* while the branch's own condition is the **verb** *"the member has not retired"* — without the limb **the approved answer did not reach the class it was approved to reach.**
    - **One residual of f1-b declined with its reason, and it is the first thing the next pass is told to attack.** A disability retiree **already in payment** whose effective date the Board *re-determines* after her death is, on the words, a member whose effective date the Board determined after the death. **f1-a's limb would close it and f1-a was not selected**, so taking it now would be re-deciding the card.
    - **f4-a — enacted. The card described option (a) and did not draft it, so the words are mine and the policy is the Director's.** The greater-of now runs only where subdivision C 2 of § 51.1-165 and the § 51.1-162 determination are payable to the same person or persons; where they are not, **the C 2 benefit is paid and the benefit determined under the preceding sentence is not.** The branch is a semicolon clause and **not a sentence of its own, because that sentence now carries five references to *"the preceding sentence"* and all five mean one sentence.** Consequence, stated because it decides who is paid: where C 2's own switch to § 51.1-162 B fails, C 2 requires payment under § 51.1-163, so the family takes a **refund** where store revisions 67 and 68 would have paid an **allowance** — which is what Chapter 1 does for that family today. **No person is worse off than under present law and the act buys that class nothing.**
    - **f14-move — enacted, word for word, net zero characters.** The bar leaves subsection L and stands in subsection B after the sentence that makes an accepted election the only route to a purchase. *"Subsection L"* is cited nowhere in the act, so nothing strands, and no citation count changes.
    - **f11-authority — commissioned as [MOO-207](/MOO/issues/MOO-207)**, assigned, self-contained, and **not drafting**: the *"complete in itself"* authority under Va. Const. art. IV, § 12 for subdivision G 4's two *"notwithstanding"* displacements, which reach subdivision C 1 of § 51.1-165 and subsection F of § 51.1-165.01 and are accompanied by no amendment to either.
    - **Closed by the selection of their alternatives, and kept rather than deleted: f1-a, f1-c, f4-b and f4-c.** **Still open and still drafted word for word: (3) f12-ninety** — the § 51.1-162 C waiver floor stays at the thirtieth day after the notice — **and (4) f3-operative**, so a member who elected the straight life option under subdivision A 1 of § 51.1-165 may still have no death benefit for the subsidy to buy. **This annotation decides neither.**
    - **[MOO-200](/MOO/issues/MOO-200)'s pass landed at 00:15 UTC on 13 October 2026, after this card was answered, and three of its findings bear on these answers.** **F14** is *aggravated* by f14-move: subsection L exists to tell localities and school boards that the act does not reach them, and the subsection addressed to them now says nothing on the subject — and F14's separate point, that the bar has **no time anchor** while subdivision D 4 determines eligibility as of the filing date of the complete application, survives the move unchanged. **F6 and F7** attack the sentence f4-a amends — F7 that the greater-of comparison *"changes no amount for anyone"*, F6 that the named assumption set is not identifiable because § 51.1-124.3 defines *"actuarial equivalent"* by *"actuarial tables **adopted** by the Board"* — and **f4-a neither cures nor worsens either.** **MOO-200's eighteen findings are not disposed in store revision 69; that is the next revision.**"""


TAIL132 = ("Say whether you want that authority hardened before the drafting request goes to "
           "Division of Legislative Services.")

sl("I2",
   "item 132 — the card's result, marked at the end of the item",
   TAIL132, TAIL132, TAIL132 + ITEM132_ADD, must_contain="authority hardened")

# find/replace patches (none beyond the slices)
ITEM_PATCHES = []
