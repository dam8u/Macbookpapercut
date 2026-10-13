#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 73 — §7 item 135 CLOSED, and items 137 and 138 opened.

Item 135 asked the Director whether to open subsection M to cure F3. The Director approved form
M-a and it is enacted as S1. The item is closed on the record of what was cut, and it closes
carrying the finding that the cure it asked for **narrows the channel without closing it** — which
is item 137.

Item 137 and item 138 are the two adverse results of this revision's cross-reference sweep. Both
are drafted, priced and anchored. **Neither is enacted and neither is agreed.**

Data only; apply73.py performs the write.
"""

MARK = "**CLOSED IN STORE REVISION 73**"

# ---- item 135: the label, and the closure ---------------------------------------------------
H135_F = ("135. **NEW IN STORE REVISION 70, out of the cross-reference sweep for that revision "
          "(§5.47 direction 2, check 1) — drafted in two forms and enacted nowhere. F3's "
          "exception does not close the subsection M channel, because subdivision M 2 does not "
          "look at subdivision D 1.**")
H135_R = ("135. **" + MARK + " — you approved form M-a at [MOO-208](/MOO/issues/MOO-208) and it "
          "is enacted as S1, +115, in subsection M 2. NEW IN STORE REVISION 70, out of the "
          "cross-reference sweep for that revision (§5.47 direction 2, check 1); drafted in two "
          "forms, one enacted. F3's exception did not close the subsection M channel, because "
          "subdivision M 2 does not look at subdivision D 1 — and the cure does not close it "
          "either, for a reason this item did not reach. See item 137.**")

T135_F = ("    **Why it is not cut.** It opens subdivision M 2, which store revision 70's "
          "commission did not open; it reverses nothing you decided, but it changes the effect "
          "of something you did decide, and that is yours and not mine. **The whole of the "
          "reasoning is at §6.0-70 item 5 and §5.47 direction 2, check 1.** Read with item 133.")
T135_R = (
    "    ~~**Why it is not cut.** It opens subdivision M 2, which store revision 70's commission "
    "did not open; it reverses nothing you decided, but it changes the effect of something you "
    "did decide, and that is yours and not mine.~~ **The whole of the reasoning is at §6.0-70 "
    "item 5 and §5.47 direction 2, check 1.** Read with item 133.\n\n"
    "    **" + MARK + ". What was cut.** Form **M-a**, at **+115 and no markup**, in subsection "
    "M 2's first sentence: *\"…a matter this section requires to be stated in it**, other than a "
    "failure to state that the Board advises the member to review the member's designation of "
    "beneficiary**, may obtain…\"*. The anchor resolved **1× inside the §1 slice** at the moment "
    "it was applied and the cure left `<u>`/`</u>` at **62 / 62**, subsection M 2 being wholly "
    "new language so that a tag would have nested. **Form M-b is not cut and is now spent.** The "
    "conformed phrase stands at **4× in §1**, byte-identical in every place — item 7, "
    "subdivision D 1's exception, D 1's subsection J limb and now M 2's exception.\n\n"
    "    **And the thing this item did not reach, which is why it closes into item 137.** M 2's "
    "**second** sentence deems *\"Every determination, **certification**, redetermination, …\"* "
    "a determination of the Board for the purposes of the subsection. **M-a excepts the advice "
    "failure from the failure-to-state limb and leaves the determination limb untouched**, so the "
    "same member can bring the same grievance as a person *\"adversely affected by a "
    "determination of the Board under this section.\"* This item argued that the channel was open "
    "because M 2 does not look at D 1; **it is also open because M 2 looks at the certification "
    "itself.** Item 137 carries the cure.")

# ---- the two new items ----------------------------------------------------------------------
ITEM137 = (
    "137. **NEW IN STORE REVISION 73, out of the cross-reference sweep for this revision (§5.49 "
    "check 4) — drafted in one form and enacted nowhere. The cure you approved for F3 narrows the "
    "subsection M channel and does not close it.** You approved S1 in form M-a and it is enacted. "
    "**It excepts the advice failure from subsection M 2's failure-to-state limb. M 2's second "
    "sentence independently deems a *certification* a determination of the Board** — *\"Every "
    "determination, **certification**, redetermination, recertification, reduction, cancellation, "
    "rescission, restoration, crediting of service credit, placement on a waiting list, "
    "expiration of a reservation, denial of an election, and refusal to accept an election under "
    "this section is a determination of the Board for the purposes of this subsection, whether or "
    "not another provision of this section expressly provides for review of it.\"* So a member "
    "whose certification omits the advice may still seek reconsideration as a person *\"adversely "
    "affected by a determination of the Board under this section\"*, on the determination clock "
    "and not on subdivision D 1's.\n"
    "\n"
    "    **Why this is a route and not a reading, in the act's own words.** Subdivision D 1 "
    "disapplies *\"the second sentence of subdivision M 2\"* for the member. **That "
    "disapplication exists for no other reason than that the determination limb is otherwise "
    "available** — if the deeming sentence did not reach a certification's content, there would "
    "be nothing to disapply. And it disapplies the sentence only *\"to such a failure\"*, which "
    "after F3 and S1 **no longer includes the advice failure**. The one failure you have twice "
    "decided should not be reviewable is therefore the one failure for which the deeming sentence "
    "is left in force. *(The contrary reading is respectable: a specific exception controls a "
    "general deeming, and a court would be slow to let the determination limb restore a review "
    "the General Assembly had just excepted. The text does not say so.)*\n"
    "\n"
    "    **The cure, form M-c. +216, no markup, one sentence, in subsection M 2 after the deeming "
    "sentence.** FIND: *\"is a determination of the Board for the purposes of this subsection, "
    "whether or not another provision of this section expressly provides for review of it.\"* — "
    "154 characters, resolving **1× inside the §1 slice** of the cut text. READ: that sentence "
    "followed by *\"A certification is not a determination of the Board for the purposes of this "
    "subsection by reason only of a failure to state in it that the Board advises the member to "
    "review the member's designation of beneficiary.\"* **The cure leaves `<u>`/`</u>` at 62 / "
    "62** and requires **no conforming amendment anywhere**: the five declaratory *\"is a "
    "determination of the Board for the purposes of subsection M\"* clauses were each checked and "
    "**none of them reaches a certification**, so the deeming of a certification lives only in "
    "this sentence.\n"
    "\n"
    "    **Why it is not cut.** It is a further opening of subsection M, which is yours and not "
    "mine, and the words are not among the six you approved. **The alternative is to leave it**: "
    "the exception then reads as narrowing one limb of M 2 while the other limb is open, which is "
    "defensible and which no reader of subsection M can see. §6.0-73 item 3. Read with item 135."
)

ITEM138 = (
    "138. **NEW IN STORE REVISION 73, out of the cross-reference sweep for this revision (§5.49 "
    "check 5) — drafted in one form and enacted nowhere. The saving clause you approved for the "
    "frozen descriptions does not reach the subdivision G 4 death notice, which is the one "
    "document a survivor ever receives.** You approved S5 and it is enacted at +310. It freezes "
    "*\"a statement **this subdivision** requires\"* of the effect of a provision of § 51.1-162, "
    "§ 51.1-163, § 51.1-165 or § 51.1-165.01 to the provision **as it reads on the date the "
    "certification is given**. **Subdivision D 1 is not the only provision of the section that "
    "compels such a description.**\n"
    "\n"
    "    **Subdivision G 4 compels three of them, in the notice the Board gives on the member's "
    "death:** the right under **subsection C of § 51.1-162** of a beneficiary entitled to the "
    "entire allowance to waive it; **the period that subsection states within which the waiver "
    "must be made**, together with any extension of it under G 4; and the right under "
    "**subsection B of § 51.1-162** of the person to whom an allowance is payable to elect the "
    "member's accumulated contributions instead. **None of the three is frozen.** If § 51.1-162 C "
    "were amended to change the waiver period, the Board would be compelled by G 4 to state the "
    "new period and would have no saving clause — and the person reading that notice is a "
    "survivor acting on a deadline, not a member with years in hand. **The defect S5 cures "
    "survives in the worse place.**\n"
    "\n"
    "    **The cure, form S5-w. +48 over S5 as enacted, no markup, and it replaces S5's own "
    "sentence rather than adding one.** FIND: S5's sentence as enacted, 310 characters, "
    "resolving **1×** in the cut text. READ: *\"A statement **this section** requires of the "
    "effect of a provision of § 51.1-162, of § 51.1-163, of § 51.1-165, or of § 51.1-165.01 is a "
    "statement of that provision as it reads on the date **the statement, notice, or "
    "certification** is given, and a statement that conforms to that provision as it then reads "
    "satisfies **the provision of this section that requires it**.\"* Three changes, each "
    "mechanical: the subdivision becomes the section; the date is supplied by **the act's own "
    "compound *\"that statement, notice, or certification\"***, which subsection A already "
    "carries; and the satisfaction clause follows. **No conforming amendment anywhere**, and the "
    "sentence stays in subdivision D 1, where the compelled descriptions are densest.\n"
    "\n"
    "    **Why it is not cut.** The words you approved are enacted, and widening them reaches a "
    "provision — subdivision G 4 — that the MOO-208 commission did not put in front of you. **The "
    "alternative is a parallel sentence in G 4**, which this drafter does not recommend: two "
    "constructions of one concept in two places is how the chapter's vocabulary rule gets broken. "
    "§6.0-73 item 4."
)
