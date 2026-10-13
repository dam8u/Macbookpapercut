# -*- coding: utf-8 -*-
"""Re-splice the §6 reproductions from `bill-text-s8` at **store revision 68** for **revision 6**
of the MOO-164 cut. Supersedes repro65.py.

Revision 6 is the first splice that carries **eleven** edits, not six: the Policy Director's
disposition promoted candidates 164-7 (with F19's limb (B)), 164-7-B, 164-8, 164-10, 164-11 and
(c-2) from held to applied. 164-7 and 164-7-B are one sentence in the applied text — 164-7-B's
two-trigger form — followed by 164-7's saving sentence.

Every provision is located **by content, not by line index**. Store revisions 62, 63, 65, 66, 67 and
68 all moved lines of §1; store revisions 66 to 68 alone grew enacted §1 from 121,576 to 131,066
characters, which is why §6 was stale for the sixth time.

Writes repro68.json. Nothing is written to the store.

Run: python3 repro68.py      (reads bill.md)
"""
import json
import re

head = open('bill.md', encoding='utf-8').read()
i = head.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', head[i + 5:])
sec1 = head[i:i + 5 + m.start()]
LINES = [l.strip() for l in sec1.split('\n') if l.strip()]


def line(prefix):
    """The one §1 line whose text, with <u> and ** stripped, starts with prefix."""
    hits = [l for l in LINES if re.sub(r'<u>|\*\*', '', l).startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0]


def mark(text, subs):
    for f, r in subs:
        assert text.count(f) == 1, ('not unique', f[:70], text.count(f))
        text = text.replace(f, r, 1)
    return text


# --- 1. subsection A interpretation paragraph. NOT amended by this cut -------------------------
# Store revision 68 re-cast this paragraph: the giving rule is new and now covers certifications,
# and the three-day extension is confined to mailing. MOO-141 Edit 1's FIND for store revision 65 is
# DEAD here; the bold-italic insertion below uses the REPAIRED anchor and is MOO-141's to re-cut.
A = mark(line('For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, a written statement'), [(
    "every period within which a person may or must act that runs from the giving of that statement, notice, or certification is extended by three days.</u>",
    "every period within which a person may or must act that runs from the giving of that statement, notice, or certification is extended by three days. ***For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.***</u>")])

# --- 2. definition of "final qualifying retirement date" — Edit 164-4 + MOO-141 Edit 2 ----------
DEF = mark(line('"Final qualifying retirement date" means the date that is 12 months'), [
    ("within the period this definition allows for acting upon it",
     "within the period ~~this definition allows~~ **allowed by this section** for acting upon it"),
    ("no later than 15 days after it acts upon the request.",
     "no later than 15 days after ~~it acts upon~~ ***it gives its decision upon*** the request."),
])

# --- 3. subdivision D 1 — Edit 164-5 + Edit 164-8 (promoted at revision 6) ----------------------
D1 = mark(line('D. 1. The Board shall not accept an election'), [
    ("any notice of a date required by that definition upon the Board's action upon a request",
     "any notice of a date required by that definition ~~upon~~ **by reason of** the Board's action upon a request"),
    ("the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
     "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. **Where the Board gives any notice described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice already filed, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes any notice previously filed.**"),
])

# --- 4. subdivision G 2 — Edit 164-2 + Edit 164-12, which is candidate (c-2) --------------------
G2 = mark(line('2. If the member does not retire in a qualifying retirement'), [
    ("or has not given it within 60 days after the determination date, the determination takes effect on the first day",
     "or has not given it within 60 days after the determination date, **or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect,** the determination takes effect on the first day"),
    ("and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.",
     "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. **Notwithstanding the definition in subdivision 4, and for the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which the Board grants or denies it.**"),
])

# --- 5. G 4 suspension and pendency passage — Edit 164-6; (c-1) is NOT applied ------------------
s = sec1.find('The Board shall not make a determination under subdivision 2, and shall not give the notice required by subdivision 2, while an application')
k = 'such a request is pending from the date on which the member files it until the date on which the Board first acts upon it.'
e = sec1.find(k, s) + len(k)
assert s > 0 and e > s
G4 = sec1[s:e].replace('’', "'")   # apostrophes normalised, per §8
G4 = mark(G4, [
    ("within the period allowed to it for acting upon the request shall not extend that aggregate",
     "within the period ~~allowed to it~~ **allowed by this section** for acting upon the request shall not extend that aggregate"),
])

# --- 6. subsection M 1, 2, 3 -------------------------------------------------------------------
# M 2 now carries five MOO-164 edits (164-10, 164-11, 164-7/164-7-B, 164-1, 164-3) and MOO-141's
# Edit 3. Substitutions are ordered front to back and every FIND is asserted unique.
M1 = line('M. 1. The Board shall adopt and publish')
M2 = mark(line('2. A member, retiree, beneficiary, applicant, personal representative'), [
    # Edit 164-10 — F6: give M 2's 90-day duty a commencement.
    ("The Board shall act upon a request for reconsideration within 90 days.",
     "The Board shall act upon a request for reconsideration within 90 days **after the request is filed**."),
    # Edit 164-11 — F12: conform the enacted expiry-notice sentence's period formula.
    ("Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file",
     "Where the Board does not act upon a request for reconsideration within ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request**, the person who filed the request may file"),
    # Edit 164-7 — route (c), in 164-7-B's two-trigger form, with F19's limb (B) and F20's saving.
    ("and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
     "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. **Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of \"final qualifying retirement date\" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. Except for the purposes of the duty of the Board under this subsection to act upon an application no later than 15 days after it acts upon the request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.**"),
    # Edit 164-1 — card (b): the tolling endpoint.
    ("until 30 days after the Board acts upon the request, except that (i)",
     "until 30 days after the Board **gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board** acts upon the request **and in no case later than 48 days after the Board acts upon the request**, except that (i)"),
    # Edit 164-3 — card (j): clause (ii)'s stranded formula.
    ("excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
     "excluding any period after the expiration of ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request** and before the Board acts upon the request"),
    # MOO-141 patch Edit 3, at its revision 6 — 120 days.
    ("retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request",
     "retains its filing date for the purposes of subdivisions D 4 and D 5 until ***120 days after*** the Board acts upon the request"),
])
M3 = line('3. The sentence of subsection B of § 2.2-4021')

out = {'A': A, 'DEF': DEF, 'D1': D1, 'G2': G2, 'G4': '> ' + G4, 'M1': M1, 'M2': M2, 'M3': M3}
json.dump(out, open('repro68.json', 'w'), ensure_ascii=False)
for k2, v in out.items():
    print(f'{k2:4s} {len(v):7d}')
print('store revision 68 §1 length', len(sec1))
