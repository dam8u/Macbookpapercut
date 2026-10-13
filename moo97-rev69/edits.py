#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 69 — the Policy Director's four answers of 12 October 2026, 18:35:16 UTC
(card 829fa6d2 on MOO-97): f1-b, f4-a, f14-move and f11-authority.

f11-authority is a request to counsel and not a drafting answer, so it is routed and not cut.
Not selected, and therefore closed by the selection of their alternatives: f1-a, f1-c, f4-b, f4-c.
Not selected and still open as drafted options: f12-ninety, f3-operative.

Every FIND below was counted on the live body of store revision 68 (document revision
db67d2bb, §1 = 131,066 characters) and resolves exactly once in §1 and once in the document.
"""

EDITS = []


def ed(_id, label, find, repl, n=1, n1=1):
    EDITS.append(dict(id=_id, label=label, find=find, repl=repl, n=n, n1=n1))


# ---------------------------------------------------------------------------
# f1-b — MOO-189's FATAL F1, in the reviewer's own words, which the Director
# approved verbatim. A retirement whose effective date the Board fixes after the
# member is dead is not a retirement before the death, for the whole of G 4.
# ---------------------------------------------------------------------------
# The Director's approved words are reproduced word for word. Two conforming limbs are added
# and each is on the record at §6.0-69 rather than silent:
#   (1) "that is not a qualifying retirement" — without it the exception, confined only by
#       "for the purposes of this subdivision", reaches the member who retired in a QUALIFYING
#       retirement, which is the class MOO-161 F1 rated fatal and the Director's standing
#       direction A1 exists to protect;
#   (2) the second limb — the exception as approved defines the noun "a retirement before the
#       date of death", and the branch's own condition is the verb "the member has not retired
#       before the date of death". Without the limb the approved answer does not reach the class
#       it was approved to reach.
ed("69-A",
   "f1-b: a retirement that is not a qualifying retirement and the effective date of which the "
   "Board determines after the death is neither a retirement before the date of death nor a "
   "retirement in which the member has retired, for the purposes of subdivision G 4",
   "Clause (i) of this subdivision does not apply where the member has retired in a retirement "
   "that is not a qualifying retirement before the date of death.",
   "Clause (i) of this subdivision does not apply where the member has retired in a retirement "
   "that is not a qualifying retirement before the date of death, except that a retirement that "
   "is not a qualifying retirement and the effective date of which the Board determines after "
   "the date of the member's death is not a retirement before the date of death for the purposes "
   "of this subdivision, and for those purposes the member shall not be treated as having "
   "retired before the date of death in such a retirement.")

# ---------------------------------------------------------------------------
# f4-a — confine the greater-of to the case where § 51.1-165 C 2 and the
# preceding sentence pay the same person, and leave the non-coincident case
# entirely to § 51.1-165 C 2. The card's option (a) is described and not
# drafted, so these words are mine; the policy is the Director's.
# ---------------------------------------------------------------------------
ed("69-B",
   "f4-a: the greater-of operates only where subdivision C 2 of § 51.1-165 and the preceding "
   "sentence are payable to the same person or persons",
   ", and where that subdivision applies the Board shall pay the benefit it provides or the "
   "benefit determined under the preceding sentence, whichever is greater,",
   ", and where that subdivision applies and the person or persons to whom that subdivision "
   "requires a benefit to be paid are the same as the person or persons to whom the benefit "
   "determined under the preceding sentence would be payable, the Board shall pay the benefit "
   "that subdivision provides or the benefit determined under the preceding sentence, whichever "
   "is greater,")

ed("69-C",
   "f4-a: and where they are not the same, subdivision C 2 of § 51.1-165 alone governs — joined "
   "to the same sentence by a semicolon so that every \"preceding sentence\" in it keeps one "
   "referent",
   ", and shall pay it to the person to whom the provision under which the greater benefit is "
   "determined requires it to be paid.",
   ", and shall pay it to that person or those persons; and where that subdivision applies and "
   "the person or persons to whom that subdivision requires a benefit to be paid are not the "
   "same as the person or persons to whom the benefit determined under the preceding sentence "
   "would be payable, the Board shall pay the benefit that subdivision provides and shall not "
   "pay the benefit determined under the preceding sentence.")

# ---------------------------------------------------------------------------
# f14-move — the state-system eligibility bar leaves subsection L's
# local-mandate disclaimer for subsection B, where the grant it qualifies is.
# Word for word the same sentence; nothing but its place changes.
# ---------------------------------------------------------------------------
BAR = ("No person whom the definition of \"eligible member\" in subsection A excludes, including a "
       "teacher, an employee of a political subdivision, and a member of a retirement system "
       "established under Chapter 2 (§ 51.1-200 et seq.), Chapter 2.1 (§ 51.1-211 et seq.), or "
       "Chapter 3 (§ 51.1-300 et seq.), is eligible to make an election under this section.")

ed("69-D",
   "f14-move: struck from subsection L, which is left as the local-mandate disclaimer alone",
   " upon any local retirement system. " + BAR + "</u>",
   " upon any local retirement system.</u>")

ed("69-E",
   "f14-move: re-enacted in subsection B, immediately after the sentence that makes the election "
   "the only route to a purchase and before the avoidance-of-doubt sentence",
   "if, and only if, the Board has accepted the member's election under subsection D. For the "
   "avoidance of doubt,",
   "if, and only if, the Board has accepted the member's election under subsection D. " + BAR
   + " For the avoidance of doubt,")

# ---------------------------------------------------------------------------
# anchors that must still resolve exactly once in §1 after this revision
# ---------------------------------------------------------------------------
UNTOUCHED = [
    ("A1: the G 4 condition stays a condition on retirement status",
     "where clause (i) of this subdivision applies and the member has not retired before the "
     "date of death"),
    ("f4-c not selected: the savings clause stays",
     "Nothing in the preceding sentence reduces a benefit payable under subdivision C 2 of "
     "§ 51.1-165"),
    ("m8-a, store revision 67",
     "provided that the aggregate of all periods so excluded shall not exceed 90 days"),
    ("the act's footprint",
     "A BILL to amend and reenact §§ 51.1-142.2 and 51.1-162 of the Code of Virginia"),
    ("§ 51.1-162 reproduced in Code order",
     "§ 51.1-162. Death before retirement."),
    ("store revision 65's advisory",
     "that the member is advised to review the member's designation"),
    ("f12-ninety not selected: the waiver floor is unchanged",
     "before the thirtieth day after the notice is given"),
    ("the eligibility bar, wherever it sits — exactly one copy",
     BAR),
]

TERMS = ["§ 51.1-162", "§ 51.1-163", "§ 51.1-165", "§ 51.1-165.01", "§ 51.1-153", "§ 51.1-156",
         "eligible member", "qualifying retirement", "before the date of death",
         "preceding sentence", "subdivision C 2 of § 51.1-165", "Chapter 2 (§ 51.1-200",
         "is eligible to make an election under this section"]
