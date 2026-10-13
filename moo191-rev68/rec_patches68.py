# -*- coding: utf-8 -*-
"""Store revision 68 — record-only patches out of MOO-195's pass 21.

Four in-place corrections to records I wrote at store revision 65. No word of §1 moves.
Each FIND was counted on the live body (store revision 67, document revision ea3b25b0) and
resolves exactly once; apply68.py re-counts before writing.
"""

PATCHES = [
    dict(
        id="P1", label="§6.0-65 item 5 — the second reason for the deadline is not true (MOO-195 F2)",
        n=1,
        find=(
            "**The advisory's deadline is the same event, and it is the right one twice over:** it "
            "is the last moment at which the purchase can still be undone, and the whole window "
            "during which re-designating changes the outcome."
        ),
        repl=(
            "**The advisory's deadline is the same event, and it is the last moment at which the "
            "purchase can still be undone.** **Correction, store revision 68 — the second reason "
            "this item gave is not true and is withdrawn.** As written at store revision 65 the "
            "item continued *\"and the whole window during which re-designating changes the "
            "outcome.\"* **Nothing in § 51.1-162 A fixes a designation at the completion of "
            "payment.** A's own words contemplate redesignation at any time — *\"If no "
            "designation has been made, or the death of the designated person occurs prior to the "
            "death of the member and another designation has not been made\"* — so the window "
            "in which re-designating changes the § 51.1-162 outcome runs to the earlier of the "
            "member's death and the last of the act's retirement-date legs: about 27 months on the "
            "act's own dials (subsection E's 12 months to pay and 1 to credit, and the two "
            "retirement-date definitions in subsection A), and without end for a member who does "
            "not retire. *\"Before completing payment\"* closes the **first** of those legs. "
            "[MOO-195](/MOO/issues/MOO-195) F2, verified at source on 12 October 2026. **The "
            "enacted deadline is the Policy Director's approved word and is not changed by this "
            "record revision**; whether to extend it, re-point it or leave it stand is before the "
            "Director at [MOO-191](/MOO/issues/MOO-191) with the words drafted."
        ),
    ),
    dict(
        id="P2", label="§6.0-65 item 6 — the channel question was sent to the wrong card (MOO-195 F10, F3)",
        n=1,
        find=(
            "**If the counsel gate at [MOO-192](/MOO/issues/MOO-192) thinks the channel is worth "
            "more argument than the advice is worth, the Director has said they will re-take that "
            "one point; it is one clause either way, and the clause is this item.**"
        ),
        repl=(
            "**The Director has said that if the counsel pass thinks the channel is worth more "
            "argument than the advice is worth, they will re-take that one point; it is one clause "
            "either way, and the clause is this item.** **Correction, store revision 68 — this item "
            "sent that question to the wrong card.** As written at store revision 65 it named the "
            "counsel gate at [MOO-192](/MOO/issues/MOO-192), which is the subsection E1 gate and "
            "has the channel out of scope. **The question went to pass 21 at "
            "[MOO-195](/MOO/issues/MOO-195)**, which answered it: **keep the subsection J limb and "
            "drop the subsection M limb**, because M review's only possible output is a remand that "
            "can give the claimant nothing — § 2.2-4029 bars a court from supplying the "
            "agency action — while the J report puts the same fact before the money committees "
            "at no litigation cost and with no claimant needed. **That recommendation is not "
            "enacted here**: it reverses a point the Director decided at MOO-188 §3.4, and it "
            "is before the Director at [MOO-191](/MOO/issues/MOO-191) with the words drafted. "
            "[MOO-195](/MOO/issues/MOO-195) F3 and F10."
        ),
    ),
    dict(
        id="P3", label="§5.43 direction 1 — the compound is not in § 51.1-162 A (MOO-195 F11)",
        n=1,
        find="are the same concept and not a second one |",
        repl=(
            "are the same concept and not a second one. **Precision, store revision 68:** the "
            "compound *\"designation of beneficiary\"* does **not** itself appear in § 51.1-162 "
            "A — A's words are *\"designate who is to receive a refund of accumulated "
            "contributions\"*, *\"the designated beneficiary\"*, *\"the designation\"* and *\"If no "
            "designation has been made.\"* **This row's claim is that the component vocabulary is "
            "A's, and that claim holds as written.** The compound is new to the act and to "
            "§ 51.1-162, and it is nonetheless the right noun, because A does pay *\"the "
            "designated beneficiary\"* and does call the act *\"the designation.\"* No text changes. "
            "[MOO-195](/MOO/issues/MOO-195) F11 |"
        ),
    ),
    dict(
        id="P4", label="§5.43 check 4 — answer (7) has since been answered, and the check conflated two things (MOO-195 N8, F5, F8)",
        n=1,
        find=(
            "**It remains true that a reader of § 51.1-162 learns nothing from § 51.1-162** "
            "— that exposure is §7 item 129 answer (7), which is **not** answered here and "
            "which would change the act's footprint and its title line."
        ),
        repl=(
            "**It remains true that a reader of § 51.1-162 learns nothing from § 51.1-162** "
            "— that exposure is §7 item 129 answer (7), which is **not** answered here and "
            "which would change the act's footprint and its title line. **Two corrections, store "
            "revision 68.** First, **answer (7) has since been answered**: the Policy Director "
            "approved **s162c-conforming** at 18:04:59 UTC on 12 October 2026 and store revision 67 "
            "enacted it, so § 51.1-162 is now reproduced in full as amended in §1, the "
            "title line names it, and the first enactment clause follows. Second, this check "
            "**conflated two things**: answer (7) is specifically the § 51.1-162 **C** "
            "waiver-period operative override and its conforming amendment, not the general point "
            "that a reader of § 51.1-162 learns nothing from § 51.1-162. **The advisory "
            "overrides nothing and does not enlarge answer (7)** — "
            "[MOO-195](/MOO/issues/MOO-195) N8. What the advisory does leave open is a different "
            "and smaller exposure, an instruction with no addressable machinery, which is "
            "[MOO-195](/MOO/issues/MOO-195) F5 and is before the Director at "
            "[MOO-191](/MOO/issues/MOO-191). **And the exposure the conforming amendment did not "
            "cure is [MOO-195](/MOO/issues/MOO-195) F8:** the title line now names § 51.1-162, "
            "but its *\"relating to\"* clause still says nothing of death benefits or beneficiary "
            "designations, and subdivision D 1 now compels seven statements about them."
        ),
    ),
]
