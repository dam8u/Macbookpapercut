# -*- coding: utf-8 -*-
"""MOO-97 store revision 62 — FIND/READ pairs.

Every entry is (id, label, find, replace, expected_count).
Base-independent: no offsets, no line numbers. apply.py asserts each FIND
occurs exactly expected_count times in the live body before touching it.
"""

EDITS = []
def E(i, label, find, repl, n=1):
    EDITS.append(dict(id=i, label=label, find=find, repl=repl, n=n))

# ---------------------------------------------------------------- MOO-169 F1+F2
E("E1", "F1/F2 fatal — delete E1's notification window, carry the retiree carve-out",
"where clause (i) of this subdivision applies and the member dies after the Board has received the notification of the member's effective date of retirement required by subdivision D 1 and before that date, the Board shall determine the benefit payable under this subdivision under § 51.1-162 as on the death of a member in service",
"where clause (i) of this subdivision applies and the member has not retired before the date of death, the Board shall determine the benefit payable under this subdivision under § 51.1-162 as on the death of a member in service")

# ------------------------------------------------- MOO-169 F1 conforming + M5
E("E2", "F1 conforming + M5 — D 1's first proposition: same scope, and C 1 / F displaced only as to § 51.1-163",
"The Board's certification shall also state that, where a member whose election the Board has accepted dies after the Board has received the notification of the member's effective date of retirement required by this subdivision and before that date, the benefit payable on the member's death is determined under subdivision G 4 and under § 51.1-162 as on the death of a member in service and not under subdivision C 1 of § 51.1-165 or under subsection F of § 51.1-165.01;",
"The Board's certification shall also state that, where a member whose election the Board has accepted dies without having retired, the benefit payable on the member's death is determined under subdivision G 4 and under § 51.1-162 as on the death of a member in service and not under the provisions of subdivision C 1 of § 51.1-165 or of subsection F of § 51.1-165.01 that require benefits to be paid in accordance with § 51.1-163;")

# ----------------------------------------------------------------- MOO-169 F9
E("E3", "F9 — restate § 51.1-165 C 2 with its identity condition; drop the invented payee rule",
"that where the member dies while in service and subdivision C 2 of § 51.1-165 otherwise applies, that subdivision provides the greater of the benefit payable in accordance with § 51.1-163 and the benefit payable under subsection B of § 51.1-162, each payable to the person entitled to it under the provision under which it is determined, and that the Board shall pay",
"that where the member dies while in service and subdivision C 2 of § 51.1-165 otherwise applies, that subdivision provides for the payment of benefits in accordance with § 51.1-163, except that where the contingent annuitant or annuitants under the option elected are the same person or persons who would receive a monthly benefit under subsection B of § 51.1-162 and that monthly benefit would be greater, that subdivision provides for the payment of benefits in accordance with that subsection, and that the Board shall pay")

# ---------------------------------------------------------------- MOO-169 F10
E("E4", "F10 — the § 51.1-162 B proposition: survival is necessary, the designation decides",
"that subsection B of § 51.1-162 provides a retirement allowance on the death of a member in service only where the member is survived by a spouse, a minor child or a parent and no benefit is payable under subsection C of that section;",
"that subsection B of § 51.1-162 provides a retirement allowance on the death of a member in service only where no benefit is payable under subsection C of that section and only to a surviving spouse, minor child, or parent whom the member has designated under subsection A of that section or who is entitled in the order of precedence that subsection B of that section states where the member has made no designation or the person designated has predeceased the member and no other designation has been made;")

# ----------------------------------------------------------------- MOO-169 M6
E("E5", "M6 — § 51.1-162 C's in-service condition, omitted",
"that subsection C of § 51.1-162 provides a retirement allowance, where the member's death results from a cause compensable under the Virginia Workers' Compensation Act (§ 65.2-100 et seq.), to the member's surviving spouse, minor children, or parents as that subsection provides;",
"that subsection C of § 51.1-162 provides a retirement allowance, where the member dies in service from a cause compensable under the Virginia Workers' Compensation Act (§ 65.2-100 et seq.), to the member's surviving spouse, minor children, or parents as that subsection provides;")

# ----------------------------------------------------------------- MOO-169 m3
E("E6", "m3 — § 51.1-162 A's payee rule, omitted",
"and that where no benefit is payable under subsection B of § 51.1-162, subsection A of that section provides for the payment of the member's accumulated contributions.",
"and that where no benefit is payable under subsection B of § 51.1-162, subsection A of that section provides for the payment of the member's accumulated contributions to the person the member has designated or, where the member has made no designation, to a surviving relative in the order of precedence that section states.")

# ------------------------------------------------------- MOO-169 F5 + m2 (D 1)
E("E7", "F5 + m2 — the incomplete-certification remedy: all matters, the member's own period, one window",
"A failure to state in the Board's certification every matter required by the preceding sentence is a failure of the Board for the purposes of subsection M; a person adversely affected by it may seek review under subsection M no later than 30 days after the date on which the notice required by subdivision G 4 is given to that person; and the Board shall state every such failure in the report required by subsection J.",
"A failure to state in the Board's certification every matter this subdivision requires to be stated in it is a failure of the Board to state in a certification a matter this section requires to be stated in it for the purposes of subsection M; a person adversely affected by it may seek review under subsection M no later than 30 days after the date on which the certification is given to the member or, where that person is not the member, no later than 30 days after the date on which the notice required by subdivision G 4 is given to that person; the second sentence of subdivision M 2 does not apply to such a failure; and the Board shall state every such failure in the report required by subsection J.")

# ----------------------------------------------------------------- MOO-169 F6
E("E8", "F6 — M 2's third window was empty everywhere but D 1; give it the chapter's own 30 days",
"or, in the case of a failure to state a matter, within the period provided by the provision that requires the matter to be stated,",
"or, in the case of a failure to state a matter, within 30 days after the certification or notice is given or, where the provision that requires the matter to be stated provides a longer or later period, within that period,")

# ------------------------------------------------------------ MOO-169 F3 + F4
E("E9", "F3 + F4 — M 2's class list, both lists: drop the adverse-determination gate, restore the bounded notice class",
"personal representative of a deceased member's estate, person who claimed any benefit payable on the death of a member and whom the Board determined is not entitled to it, or employer that paid on a member's behalf,",
"personal representative of a deceased member's estate, person who has claimed any benefit payable on the death of a member, person to whom this section requires a notice to be given in respect of a benefit payable on the death of a member, or employer that paid on a member's behalf,",
2)

# ----------------------------------------------------------------- MOO-169 M9
E("E10", "M9 — express saving of § 2.2-4026, so the enumeration is not read as an implied repeal",
"shall have a right to seek judicial review thereof in accordance with Article 5 (§ 2.2-4025 et seq.) of the Administrative Process Act.",
"shall have a right to seek judicial review thereof in accordance with Article 5 (§ 2.2-4025 et seq.) of the Administrative Process Act. Nothing in this subsection limits the right of any person under § 2.2-4026 to seek judicial review of a case decision.")

# ------------------------------------------------------------ MOO-169 F8 + M2
E("E11", "F8 + M2 — charge the reinstated amount against D 2 and engage the excess machinery; delete the stranded contingency words",
"the Board shall reinstate the amount released, together with any contingency amount released with it, no later than 30 days after the determination is reconsidered or reviewed, and the rule of this subdivision that no certified subsidy is settled more than once does not prevent the settlement of an amount so reinstated.",
"the Board shall reinstate the amount released no later than 30 days after the determination is reconsidered or reviewed, the amount so reinstated shall be charged against the limitations in subdivision D 2 notwithstanding that the amount available to be reserved is thereby exceeded, and the rule of this subdivision that no certified subsidy is settled more than once does not prevent the settlement of an amount so reinstated.")

# ----------------------------------------------------------------- MOO-169 M3
E("E12", "M3 — the release can be required twice of the same amount",
"the Board shall release the amount settled under this subdivision and shall restore it to the amount available under the limitation stated in the first sentence of subdivision D 2 only to the extent the amount settled has not been paid to the retirement system under subsection N,",
"the Board shall release the amount settled under this subdivision and shall restore it to the amount available under the limitation stated in the first sentence of subdivision D 2, to the extent the amount settled has not been paid to the retirement system under subsection N and to the extent it has not already been released and not reinstated,")

# ----------------------------------------------------------------- MOO-169 M1
E("E13", "M1 — \"that date\" has no referent where the subsidy settled under subdivision G 1",
"The Board shall, no later than 90 days after that date or, where that date is the date of the member's death, no later than 90 days after the date on which the Board learns of the death, redetermine",
"The Board shall, no later than 90 days after the date on which the certified subsidy is settled under subdivision 1 or under this subdivision, as the case may be, or, where that date is the date of the member's death, no later than 90 days after the date on which the Board learns of the death, redetermine")

# ----------------------------------------------------------------- MOO-169 M4
E("E14", "M4 — track the Code's qualifiers on the § 51.1-162 C waiver and the § 51.1-162 B election",
"of any right under subsection C of § 51.1-162 of a person entitled to any benefit payable on the member's death to waive the allowance and of the period stated in that subsection within which the waiver must be made, of any right of such a person under subsection B of § 51.1-162 to elect to be paid the member's accumulated contributions or a lump sum in lieu of any other benefit under that section,",
"of any right under subsection C of § 51.1-162 of a beneficiary entitled to the entire amount of a retirement allowance under that subsection to waive the allowance and of the period stated in that subsection within which the waiver must be made, of any right under subsection B of § 51.1-162 of the person to whom an allowance is payable under that subsection to elect to be paid the member's accumulated contributions or a lump sum in lieu of any other benefit under that section,")

# ----------------------------------------------------------------- MOO-169 m1
E("E15", "m1 — \"person under a disability\" and \"fiduciary\" given the § 8.01-2 standard",
"or, where that person is a minor or is under a disability, to that person's guardian, conservator, committee, or other fiduciary and,",
"or, where that person is a minor or is a person under a disability as defined in § 8.01-2, to that person's guardian, conservator, committee, or other fiduciary within the meaning of that section and,")

# =================================================== The Director's seven answers
E("E16", "DIRECTOR f3-a + f3-b — the greater-of's measure and payee",
"and where that subdivision applies the Board shall pay the benefit it provides or the benefit determined under the preceding sentence, whichever is greater.",
"and where that subdivision applies the Board shall pay the benefit it provides or the benefit determined under the preceding sentence, whichever is greater, the two being compared on the basis of actuarial equivalence as of the date of the member's death determined on the assumptions then in use by the Board, and shall pay it to the person to whom the provision under which the greater benefit is determined requires it to be paid.")

E("E17", "DIRECTOR f14-supp — a further notice where the Board later determines an amount differently",
"from the date it is given to that other person.",
"from the date it is given to that other person; and where the Board after giving that notice determines the amount of a benefit differently, it shall give that person a further notice stating the determination and the reasons for it no later than 30 days after making it, and the period within which that person may seek review under subsection M of that determination runs from the date that further notice is given.")

E("E18", "DIRECTOR f7-toll — the § 51.1-162 C waiver does not expire before the 30th day after a late notice",
"The Board shall state in the report required by subsection J every failure to give the notice required by the preceding sentence to a person within the period this subdivision allows for the giving of it to that person.",
"The Board shall state in the report required by subsection J every failure to give the notice required by the preceding sentence to a person within the period this subdivision allows for the giving of it to that person. Where the Board gives a notice required by this subdivision on the death of a member later than 30 days after the death, the period stated in subsection C of § 51.1-162 within which a waiver must be made does not expire before the thirtieth day after the notice is given to the person entitled to make it.")

E("E19", "DIRECTOR m2-lateness — lateness reviewable for 30 days after the Board cures it",
"at any time before the Board makes the determination, gives the notice, or makes the payment, or, in the case of a failure to state a matter,",
"at any time before the Board makes the determination, gives the notice, or makes the payment or, where the Board has made the determination, given the notice, or made the payment late, within 30 days after it does so, or, in the case of a failure to state a matter,")

E("E20", "DIRECTOR f10-b — confine the Program to Chapter 1 members, in the definition's own chapter form",
"No teacher and no employee of a political subdivision is eligible to make an election under this section.",
"No teacher and no employee of a political subdivision is eligible to make an election under this section. No member of a retirement system established under Chapter 2 (§ 51.1-200 et seq.), Chapter 2.1 (§ 51.1-211 et seq.), or Chapter 3 (§ 51.1-300 et seq.) is eligible to make an election under this section.")

E("E21", "DIRECTOR f11-disclose — a § 51.1-162 benefit is not charged against the D 2 limitations",
"Upon the settlement of a certified subsidy under subdivision G 1 or G 4, the Commonwealth shall pay the amount settled to the retirement system from an appropriation made for that purpose.",
"Upon the settlement of a certified subsidy under subdivision G 1 or G 4, the Commonwealth shall pay the amount settled to the retirement system from an appropriation made for that purpose. Nothing in this section charges a benefit payable under § 51.1-162 against the limitations stated in subdivision D 2.")
