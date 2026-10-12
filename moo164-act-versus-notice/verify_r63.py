# -*- coding: utf-8 -*-
"""MOO-164 anchor re-check at **store revision 63** (document revision 79) — the ninth and tenth
base moves. Supersedes verify_r6.py, which ran at store revision 61.

Scope note, and it changed at store revision 63: every anchor is counted **over enacted §1 only**.
Store revisions 62 and 63 quote three of these strings in the §0 revision narrative and in the §5
sweep, so a whole-document count now returns 2 or 3 for those three and 1 for the rest. §1 is what
is amended; the narrative is not. Counting whole-document would have produced a false alarm, and
counting §1 only is what the apply kit has always done.

Expected: twelve anchors (nine edit/patch FINDs + three held candidates), every one exactly 1 in §1,
on each of three bases — store revision 63 as it stands, + the MOO-141 patch at revision 5 (Edit 3
at 30 days), + it at revision 6 (Edit 3 at 120 days) — and a +490 amendment delta on every base.
Requires head63.md = bill-text-s8 at store revision 63. Nothing is written to the store."""
import re, sys

head = open('head63.md', encoding='utf-8').read()
i = head.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', head[i + 5:])
BILL = head[i:i + 5 + m.start()]
print(f'store revision 63, enacted §1 = {len(BILL)} characters')

E1_F = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_R = ("every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. "
        "For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, "
        "the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or "
        "last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board "
        "first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to "
        "make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by "
        "this section.</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R5 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"


def build(e3):
    out = BILL
    for f, r in ((E1_F, E1_R), (E2_F, E2_R), (E3_F, e3)):
        assert out.count(f) == 1, f[:60]
        out = out.replace(f, r, 1)
    return out


BASES = [("store rev 63", BILL),
         ("store rev 63 + MOO-141 patch rev 5", build(E3_R5)),
         ("store rev 63 + MOO-141 patch rev 6", build(E3_R6))]

EDITS = [
 ("164-1 card (b)",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after the Board gives the person who filed the request written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request"),
 ("164-2 card (h)",
  "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
  "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect, the determination takes effect on the first day"),
 ("164-3 card (j)",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request"),
 ("164-4 F-5",
  "within the period this definition allows for acting upon it",
  "within the period allowed by this section for acting upon it"),
 ("164-5 F-9",
  "any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition by reason of the Board's action upon a request"),
 ("164-6 conforming",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
  "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
]
HELD = [
 ("c-1", "For the purposes of this subdivision an application for a disability retirement allowance is pending"),
 ("c-2", "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending."),
 ("card (i) insertion point", "The Board shall act upon a request for reconsideration within 90 days."),
 # new at store revision 63 — the two sentences item 124 option (d) enacted, and the anchor
 # candidate 164-7 at §13.4 would attach to. Counted, not applied.
 ("164-7 anchor (item 130)", "the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection."),
 # NB: the short form of this anchor — "and the Board shall state every such delay in the report
 # required by subsection J." — resolves TWICE (D 1's lateness sentence and D 4's incomplete-
 # application sentence). The span below is long enough to be unique. §13.1 records why.
 ("164-8 anchor (first required)", "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J."),
]

fail = 0
for name, base in BASES:
    out, delta = base, 0
    print(f"\n== {name}  ({len(base)} chars)")
    for tag, f, r in EDITS:
        c = out.count(f)
        print(f"   {tag:18s} FIND count {c}  delta {len(r)-len(f):+d}")
        if c != 1:
            fail += 1
        else:
            out = out.replace(f, r, 1); delta += len(r) - len(f)
    for tag, f in HELD:
        c = base.count(f)
        print(f"   held: {tag:30s} FIND count {c}   (not applied)")
        if c != 1: fail += 1
    n = out.count('’'); out = out.replace('’', "'")
    print(f"   amendment delta {delta:+d} | apostrophes normalised {n} | final length {len(out)}")
    if delta != 490: fail += 1
    if n != 4: fail += 1

# the classification count, which moved from 19 to 21 at store revision 63
print('\n== occurrence classification over §1')
for p in ('acts upon', 'act upon', 'acting upon', 'action upon'):
    print(f'   {p!r:14s} {BILL.count(p)}')
tot = sum(BILL.count(p) for p in ('acts upon', 'act upon', 'acting upon', 'action upon'))
print(f'   total {tot}  (expected 21: was 19 at store revision 61; +2 from the two sentences'
      f' store revision 63 inserted in M 2)')
if tot != 21: fail += 1

print("\nFAILURES:", fail)
sys.exit(1 if fail else 0)
