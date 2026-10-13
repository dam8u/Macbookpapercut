#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-211's six cures, re-drafted and re-priced for store revision 71. ENACTS NOTHING.

Data only. Each cure is a FIND/READ pair with the delta this kit measures, not the delta
[MOO-211](/MOO/issues/MOO-211) asserted. Five of counsel's six figures do not hold, for two
separate reasons, and the reasons are the interesting part:

  * **The markup.** Counsel wrote `<u></u>` tags on five of the six cures. Three of those
    insertion points (S1, S3, S5) sit INSIDE an open underscored span — subsection M 2 and
    subdivision D 1 are wholly new language — so the tags would NEST. Two (S2, M3) sit in
    enactment clause 3, which carries **zero** `<u>` tags in 6,176 characters, because the
    enactment clauses are not amendatory text and are not redlined, exactly as the title line is
    not. **So no cure carries a tag, and all six leave `<u>`/`</u>` at 62/62.**
  * **Arithmetic.** M3 is off by one independently of the markup.

`counsel` is what MOO-211 §9 handed over. `delta` is measured. Nothing in this file is agreed:
every one of the six is a decision for the Policy Director.
"""

# Each cure:
#   id        counsel's label
#   grade     counsel's grade
#   where     the provision the cure edits
#   decides   the policy question the Director has to answer to take it
#   find      the anchor, counted inside the §1 slice
#   mode      insert_after | insert_before | replace_token
#   at        the token inside the FIND that locates the edit
#   ins       the new words, WITHOUT markup — see the module note
#   counsel   the figure MOO-211 §9 handed over
#   delta     the figure this kit measures
CURES = [
    dict(
        id="S1", grade="serious", where="subsection M 2, first sentence",
        decides="Whether to open subsection M, which the MOO-208 commission did not open. This is "
                "form M-a at §7 item 135. It is the only cure that reaches the finding the "
                "composite could not reach from inside subdivision D 1.",
        find="or by a failure of the Board to state in a certification or notice a matter this "
             "section requires to be stated in it, may obtain",
        mode="insert_after", at="stated in it",
        ins=", other than a failure to state that the Board advises the member to review the "
            "member's designation of beneficiary",
        counsel="+115 net / +122 with tags", delta=115,
        note="Inside M 2's open span, so no tags. +115. Item 135's own +116 counted a second "
             "comma the FIND already supplies, and item 135's READ string writes the tags that "
             "would nest; both are corrected in the item.",
    ),
    dict(
        id="S2", grade="serious", where="enactment clause 3, clause (v)",
        decides="Whether the failure-to-state limb of subsection M survives the act's expiry on "
                "1 July 2033. Clause (v) today continues subsection M for a determination, a "
                "failure to determine and a failure to give notice, and not for a failure to "
                "state. Touches no operative text.",
        find="and subsection M of that section as it applies to such a determination or to a "
             "failure to make such a determination or to give such a notice",
        mode="insert_after", at="such a notice",
        ins=", or to a failure of the Board to state in a certification or notice a matter that "
            "section requires to be stated in it",
        counsel="+118", delta=118,
        note="Counsel's +118 is right, but it is the figure net of the tags counsel also wrote. "
             "The enactment clauses carry no markup, so +118 is also the figure with markup. "
             "Correct for the wrong reason.",
    ),
    dict(
        id="S3", grade="serious", where="subdivision D 1, item 7, second proposition",
        decides="Whether to limit F2's terminus to death before retirement. The proposition as "
                "enacted is accurate only where the member dies before retiring, and § 51.1-162 "
                "is captioned 'Death before retirement'. Counsel's alternative — replacing "
                "'before the member's death' with 'before the member retires' — reverses the "
                "Director's F2 decision; this cure does not.",
        find="may make or change that designation under subsection A of that section at any time "
             "before the member's death",
        mode="insert_after", at="before the member's death",
        ins=", and that that designation determines the payment of a benefit under that section "
            "only where the member dies before retirement",
        counsel="+127", delta=127,
        note="Inside D 1's open span, so no tags. +127. The FIND resolves 1x in §1 and 2x in the "
             "document; the second is a record quotation, so apply inside the §1 slice.",
    ),
    dict(
        id="S5", grade="serious", where="subdivision D 1, immediately before the failure sentence",
        decides="Whether the six frozen descriptions of §§ 51.1-162, 51.1-163, 51.1-165 and "
                "51.1-165.01 follow those sections when they are amended. Today they do not, and "
                "the same sentence uses 'as amended or renumbered' for the Internal Revenue Code "
                "and for nothing else.",
        find=" A failure to state in the Board's certification every matter this subdivision "
             "requires to be stated in it",
        mode="insert_before", at=None,
        ins=" A statement this subdivision requires of the effect of a provision of § 51.1-162, "
            "of § 51.1-163, of § 51.1-165, or of § 51.1-165.01 is a statement of that provision "
            "as it reads on the date the certification is given, and a statement that conforms "
            "to that provision as it then reads satisfies this subdivision.",
        counsel="+310", delta=310,
        note="Inside D 1's open span, so no tags. +310. This is the largest of the six and the "
             "only one that adds a sentence to the subdivision.",
    ),
    dict(
        id="M3", grade="moderate", where="enactment clause 3, clause (iii)",
        decides="Whether subdivision D 1 survives the expiry for the subsection J reporting "
                "duties. Clause (iii) continues 'every provision of that section to which "
                "subsection J refers'; subdivision J 1 names D 2, D 6, D 7, G 1, G 2, G 3, G 4 "
                "and G 5, and does not name D 1.",
        find="every provision of that section to which subsection J refers",
        mode="insert_after", at="subsection J refers",
        ins=", and every provision of that section that requires the Board to state a matter in "
            "that report,",
        counsel="+94", delta=95,
        note="Counsel's +94 is off by one on the words counsel wrote; measured +95. Enactment "
             "clause, so no tags.",
    ),
    dict(
        id="M4", grade="moderate", where="subdivision D 1, item 7, third proposition",
        decides="Whether the no-fault clause reaches a procedure adopted under subsection M 1. "
                "As enacted it says 'nothing in this subdivision', and the act uses the wider "
                "'nothing in this section' three times elsewhere in §1.",
        find="that nothing in this subdivision requires the member to review the designation",
        mode="replace_token", at="this subdivision",
        ins="this section, and no procedure adopted under subsection M,",
        counsel="+42", delta=42,
        note="Inside D 1's open span and counsel wrote no tags here, so +42 holds. Widens the "
             "first limb only; the second limb ('or affects any benefit...') stays keyed to the "
             "subdivision, for the reason counsel gives.",
    ),
]

# The three arithmetic/citation corrections counsel raised against this kit's own record.
# Each is a demonstrated error of fact in my record layer, not a policy question.
RECORD_CORRECTIONS = [
    ("m1", "§7 item 135", "M-a stated +116, measured +115; M-b stated +101, measured +121. Both "
                          "READ strings also write <u></u> tags that would nest inside M 2's "
                          "open span."),
    ("m2", "§5.47 direction 2 check 9", "the re-anchored MOO-176 Edit 1 string is 151 characters, "
                                        "not 150."),
    ("M1", "§6.0-70 item 6 and §8", "the series carries eight propositions of law and one "
                                    "advisory, not six and one, so the drafted scope 'every "
                                    "matter other than the advice' is exactly right and there is "
                                    "no residue to cure and no (i)-(vii) renumbering needed."),
    ("M2", "§5.47 direction 1 row 3", "the conforming-amendment column does not hold. The "
                                      "citation to subsection A carries the source of the power; "
                                      "it does not carry the timing, which is the drafter's "
                                      "inference and would not follow an amendment to A."),
    ("M5", "§5.47 direction 1 row 7", "Dean v. Paolicelli, 194 Va. 219 (1952) has no title "
                                      "holding. The authority is City of Richmond v. Pace, 127 "
                                      "Va. 274, 103 S.E. 647 (1920). The proposition is right; "
                                      "the case is wrong."),
    ("§5", "§5.47 direction 2 check 10", "a matching character delta is a checksum, not a proof. "
                                         "Two offsetting changes pass it and so does a "
                                         "zero-character change, and this revision contains one. "
                                         "The standing rule becomes a line diff against the "
                                         "fetched base."),
]


def build(c, tagged=False):
    """Return (find, read) for a cure. `tagged=True` reproduces counsel's defective form."""
    f = c["find"]
    o, z = ("<u>", "</u>") if tagged else ("", "")
    if c["mode"] == "insert_after":
        cut = f.index(c["at"]) + len(c["at"])
        return f, f[:cut] + o + c["ins"] + z + f[cut:]
    if c["mode"] == "insert_before":
        return f, o + c["ins"] + z + f
    return f, f.replace(c["at"], o + c["ins"] + z, 1)
