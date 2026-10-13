# -*- coding: utf-8 -*-
"""The six cures the Policy Director approved at MOO-208, as CUT in store revision 73.

Data only. Each cure is a FIND/READ pair applied inside the §1 slice, in document order, with its
anchor re-counted at the moment it is applied and never against the base.

**Two of the six depart from the approved string, and both departures are mechanical.** Neither
adds, removes or qualifies a proposition; each is the kind of defect the approved words carry on
their face and that this drafter is required to see.

  * **S3.** The approved insert opens *", and that that designation determines…"*. Item 7 is a
    three-clause series whose single conjunction sits before the last clause — *"…that the member
    may make or change…, and that nothing in this subdivision requires…"*. Inserting a clause
    carrying its own *"and"* in front of that last clause yields **"A, B, and C, and D"**, the
    same series defect substitution 3 of the composite spent four characters to avoid in the outer
    series. **The insert takes no conjunction: −4, so +123 and not +127.** The approved form is
    recoverable by adding one word.
  * **M3.** The approved insert ends *"…to state a matter in that report,"*. In enactment clause 3
    clause (iii) the only antecedent for *"that report"* is **"the last report and evaluation
    required by that subsection"** — the clause names no other report — so the approved words
    would continue only those provisions requiring a statement in the **last** report, which is
    not what clause (iii) continues the duties for. **The referent is named in the act's own
    standing phrase, "the report required by subsection J" (14× in §1): +24, so +119 and not
    +95.** This is the rule against cross-referencing by paraphrase, applied to a paraphrase.

No cure carries a `<u>` tag: S1, S3, S5 and M4 sit inside an open span (subsection M 2 and
subdivision D 1 are wholly new language, so a tag would nest), and S2 and M3 sit in enactment
clause 3, which is not amendatory text and carries no markup. §1 stays at 62 / 62.
"""

# id        the Director's label, approved per-item at MOO-208
# where     the provision cut
# find      the anchor, counted inside the §1 slice at the moment of application
# mode      insert_after | insert_before | replace_token
# at        the token inside the FIND that locates the edit
# ins       the new words, without markup
# delta     measured
# approved  the figure approved at MOO-208, where this cut departs from it
CURES = [
    dict(
        id="S3", where="subdivision D 1, item 7, the second proposition",
        find="may make or change that designation under subsection A of that section at any time "
             "before the member's death",
        mode="insert_after", at="before the member's death",
        ins=", that that designation determines the payment of a benefit under that section only "
            "where the member dies before retirement",
        delta=123, approved=127,
        why="F2's terminus is accurate only where the member dies before retiring, § 51.1-162 "
            "being captioned 'Death before retirement'. The clause states the limit instead of "
            "reversing the Director's F2 decision.",
        depart="The approved insert opened ', and that that designation…'. Item 7's single "
               "conjunction belongs to its last clause, so the inserted clause takes none: −4.",
    ),
    dict(
        id="M4", where="subdivision D 1, item 7, the third proposition",
        find="that nothing in this subdivision requires the member to review the designation",
        mode="replace_token", at="this subdivision",
        ins="this section, and no procedure adopted under subsection M,",
        delta=42, approved=42,
        why="The no-fault clause as enacted was keyed to the subdivision; the act uses the wider "
            "'Nothing in this section' formula three times elsewhere in §1, and a procedure "
            "adopted under subsection M 1 is not in this subdivision at all.",
    ),
    dict(
        id="S5", where="subdivision D 1, the sentence before the failure sentence",
        find=" A failure to state in the Board's certification every matter this subdivision "
             "requires to be stated in it",
        mode="insert_before", at=None,
        ins=" A statement this subdivision requires of the effect of a provision of § 51.1-162, "
            "of § 51.1-163, of § 51.1-165, or of § 51.1-165.01 is a statement of that provision "
            "as it reads on the date the certification is given, and a statement that conforms "
            "to that provision as it then reads satisfies this subdivision.",
        delta=310, approved=310,
        why="The descriptions of §§ 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 that this "
            "subdivision compels did not follow those sections when amended, and the same "
            "sentence already says 'as amended or renumbered' for the Internal Revenue Code and "
            "for nothing else.",
    ),
    dict(
        id="S1", where="subsection M 2, first sentence",
        find="or by a failure of the Board to state in a certification or notice a matter this "
             "section requires to be stated in it, may obtain",
        mode="insert_after", at="stated in it",
        ins=", other than a failure to state that the Board advises the member to review the "
            "member's designation of beneficiary",
        delta=115, approved=115,
        why="F3's exception sat in subdivision D 1, which subsection M 2 does not look at, so the "
            "M channel stayed open on M 2's own terms. This is the cure in form M-a — the "
            "exception named in M 2, in the words the act already uses.",
    ),
    dict(
        id="M3", where="enactment clause 3, clause (iii)",
        find="every provision of that section to which subsection J refers",
        mode="insert_after", at="subsection J refers",
        ins=", and every provision of that section that requires the Board to state a matter in "
            "the report required by subsection J,",
        delta=119, approved=95,
        why="Clause (iii) continues 'every provision of that section to which subsection J "
            "refers'; subdivision J 1 names D 2, D 6, D 7, G 1, G 2, G 3, G 4 and G 5, and does "
            "not name D 1, so D 1's reporting duty expired with the act.",
        depart="The approved insert ended 'in that report'. Clause (iii)'s only antecedent for "
               "that phrase is 'the last report', so the referent is named in the act's own "
               "standing phrase instead: +24.",
    ),
    dict(
        id="S2", where="enactment clause 3, clause (v)",
        find="and subsection M of that section as it applies to such a determination or to a "
             "failure to make such a determination or to give such a notice",
        mode="insert_after", at="such a notice",
        ins=", or to a failure of the Board to state in a certification or notice a matter that "
            "section requires to be stated in it",
        delta=118, approved=118,
        why="Clause (v) continued subsection M past the 1 July 2033 expiry for a determination, "
            "for a failure to determine and for a failure to give notice — and not for a failure "
            "to state a matter, which is the limb F3 and S1 are about and the limb whose harm "
            "surfaces last, on the member's death.",
    ),
]

TOTAL = sum(c["delta"] for c in CURES)                  # 827
APPROVED_TOTAL = sum(c["approved"] for c in CURES)      # 807

# §1 lines the cut may touch, and nothing else: D 1, subsection M 2, enactment clause 3.
LINES_CHANGED = 3

# Standing post-conditions, re-asserted on this cut. (needle, before, after)
TERMS = [
    ("<u>", 62, 62),
    ("</u>", 62, 62),
    ("the member is advised to", 0, 0),
    ("that the Board advises the member to review the member's designation of beneficiary", 3, 4),
    ("for the purposes of subsection M", 6, 6),
    ("is a determination of the Board for the purposes of subsection M", 5, 5),
    ("subdivision D 1", 4, 4),
    ("the report required by subsection J", 14, 15),
    ("as amended or renumbered", 2, 2),
    ("Nothing in this section", 3, 3),
    ("item 5", 0, 0),
    ("item 7", 0, 0),
    ("as it reads", 0, 1),
    ("by a failure of the Board to state in a certification or notice a matter this section "
     "requires to be stated in it", 1, 1),
    ("where the provision that requires the matter to be stated provides a longer or later "
     "period, within that period", 1, 1),
    ("whether or not another provision of this section expressly provides for review of it", 1, 1),
    ("the content of a complete application", 1, 1),
    # M3 names the report in the act's standing phrase, so it adds no further "that report":
    # the two that exist are in subdivision J 1 and subsection J's own text, both untouched.
    ("that report", 2, 2),
    # D 1 carries three "nothing in this subdivision" clauses. M4 widens the no-fault clause
    # only; the other two are about duties this subdivision alone creates and stay keyed to it.
    ("nothing in this subdivision", 3, 2),
    # The series is re-shaped by nothing in this cut. Store revision 70 left it at seven items
    # and six semicolons; store revision 71 added two items. This cut adds none.
    ("; and that the Board advises the member", 1, 1),
]

# Anchors this commission forbids disturbing: MOO-176 revision 6's three edits, re-anchored for
# Edit 1 in §5.47 direction 2 check 9 (151 characters, per MOO-211 R4). Each must resolve 1× in
# §1 before and after.
UNTOUCHED = [
    ("MOO-176 rev 6 Edit 1 (re-anchored)",
     "every period within which a person may or must act that runs from the giving of that "
     "statement, notice, or certification is extended by three days.</u>"),
    ("MOO-176 rev 6 Edit 2",
     "it shall give the member written notice of that date no later than 15 days after it acts "
     "upon the request."),
    ("MOO-176 rev 6 Edit 3",
     "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts "
     "upon the request"),
]


# ---------------------------------------------------------------------------------------------
# NOT ENACTED. One finding on the cut text, drafted so that it can be priced and decided, and
# enacted nowhere. It is the Director's decision and nobody has agreed it.
#
# S1 excepts the advice failure from subsection M 2's FAILURE-TO-STATE limb. M 2's second
# sentence independently deems a **certification** a determination of the Board for the purposes
# of the subsection, and subdivision D 1 disapplies that sentence only "to such a failure" — that
# is, to the failures D 1's own deeming sentence reaches, which no longer include the advice
# failure. So after S1 the member may still bring the same grievance under M 2's DETERMINATION
# limb. The disapplication in D 1 is itself the proof that the determination limb is an
# independent route: it exists for no other reason.
PROPOSED = [
    dict(
        id="M-c", where="subsection M 2, after the deeming sentence",
        find="is a determination of the Board for the purposes of this subsection, whether or not "
             "another provision of this section expressly provides for review of it.",
        mode="insert_after",
        at="expressly provides for review of it.",
        ins=" A certification is not a determination of the Board for the purposes of this "
            "subsection by reason only of a failure to state in it that the Board advises the "
            "member to review the member's designation of beneficiary.",
    ),
    # S5 freezes the compelled descriptions of §§ 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 to
    # the date of the certification — but only for statements "this subdivision requires", and
    # subdivision D 1 is not the only provision of the section that compels such a description.
    # Subdivision G 4 requires the Board to state, in the notice it gives on the member's death,
    # the rights under subsections B and C of § 51.1-162, the waiver period that subsection C
    # states, and the election that subsection B gives — and that notice is the one document a
    # survivor ever receives. S5 does not reach it. The cure generalises S5's own sentence to the
    # section, and dates it by the act's own compound "that statement, notice, or certification".
    dict(
        id="S5-w", where="subdivision D 1, S5's sentence, generalised to the section",
        find=" A statement this subdivision requires of the effect of a provision of § 51.1-162, "
             "of § 51.1-163, of § 51.1-165, or of § 51.1-165.01 is a statement of that provision "
             "as it reads on the date the certification is given, and a statement that conforms "
             "to that provision as it then reads satisfies this subdivision.",
        mode="replace_all",
        at=None,
        ins=" A statement this section requires of the effect of a provision of § 51.1-162, of "
            "§ 51.1-163, of § 51.1-165, or of § 51.1-165.01 is a statement of that provision as "
            "it reads on the date the statement, notice, or certification is given, and a "
            "statement that conforms to that provision as it then reads satisfies the provision "
            "of this section that requires it.",
    ),
]


def build(c):
    """Return (find, read) for a cure."""
    f = c["find"]
    if c["mode"] == "insert_after":
        cut = f.index(c["at"]) + len(c["at"])
        return f, f[:cut] + c["ins"] + f[cut:]
    if c["mode"] == "insert_before":
        return f, c["ins"] + f
    if c["mode"] == "replace_all":
        return f, c["ins"]
    return f, f.replace(c["at"], c["ins"], 1)
