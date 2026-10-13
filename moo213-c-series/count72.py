# -*- coding: utf-8 -*-
"""MOO-213 — count every quotation the C-series entries make, against the LIVE bill at store revision 72.

RE-BASE, 13 October 2026. This file is `count70.py` re-pointed at store revision 72 and nothing
else. Not one counted string, asserted count, `where` or note is changed from the revision-70 pass;
the diff against `count70.py` is confined to this header and the two run labels. That is the
dateline rule applied: the entries do not re-date by assertion, they re-date because the counts were
re-printed at the new base and held. Keep `count70.py` as the record of the revision-70 pass.


Discipline, from the Policy Director's MOO-206 answer 1 and §4:

  * Nothing is carried forward on trust from MOO-90, MOO-111, MOO-133, MOO-160, MOO-172 or
    MOO-202. Every string a drafted entry puts inside quotation marks is counted here, on the
    live store text, and the count is printed in the record. That is where C2's quotation
    defect came from, and this file is the thing that stops it repeating.
  * Counts are taken over **enacted § 51.1-142.4 only** unless the row says otherwise. The
    whole document is inflated by the §0 revision narratives, which quote the operative
    strings; enacted §1 is inflated by §§ 51.1-142.2 and 51.1-162 and by the title and the
    enactment clauses.
  * Code strings are counted against the MOO-210 `law.lis.virginia.gov` retrievals, not
    against the bill, and are labelled CODE.
  * `want` is the count the drafted entry asserts. A row marked PRESENT-0 or ABSENT-n is the
    C2 defect repeating and fails loudly here rather than reaching an artifact.

Base: `bill-text-s8` on MOO-42, document revision 368f5e41-56ab-4138-8bda-8553ae8eab04,
store revision 72 (13 October 2026). Whole document 502,586 chars; enacted §1 134,012 chars;
enacted § 51.1-142.4 102,357 chars.

Result of the re-base: 66 strings counted, **0 assertions failed**. Every count the ten drafted
entries assert at revision 70 also holds at revision 72, including all four superseded quotations
still at 0 and all six cures still present.

Run:  python3 count70.py          (reads $PAPERCLIP_TASK_SCRATCH_DIR/bill.md)
Writes nothing to the store.
"""
import os
import re
import sys

SCRATCH = os.environ.get('PAPERCLIP_TASK_SCRATCH_DIR', '.')
HERE = os.path.dirname(os.path.abspath(__file__))
CODE_DIR = os.path.join(os.path.dirname(HERE), 'moo210-counsel')

doc = open(os.path.join(SCRATCH, 'bill.md'), encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
SEC = S1[S1.index('### <u>§ 51.1-142.4.'):S1.index('### § 51.1-162.')]

print(f'== live base, store revision 72: whole document {len(doc)}; enacted §1 {len(S1)}; '
      f'enacted § 51.1-142.4 {len(SEC)}')

CODE = {}
for name in ('51.1-153', '51.1-155', '51.1-155.1', '51.1-156', '51.1-124.3'):
    p = os.path.join(CODE_DIR, f'lis-{name}.txt')
    CODE[name] = open(p, encoding='utf-8').read() if os.path.exists(p) else ''


def norm(s):
    """Fold only the typographic variation the two bodies differ in."""
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    s = s.replace('—', '--').replace('–', '-')
    s = re.sub(r'</?u>', '', s)          # the live body underlines new matter
    s = s.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', s)


BODIES = {'142.4': norm(SEC), 's1': norm(S1), 'doc': norm(doc)}
for k, v in CODE.items():
    BODIES['code:' + k] = norm(v)

rows, fails = [], []


def q(entry, want, s, where='142.4', note=''):
    n = BODIES[where].count(norm(s))
    ok = (want is None) or (n == want)
    if not ok:
        fails.append((entry, where, want, n, s[:72]))
    rows.append((entry, s, where, n, want, ok, note))
    return n


# ============================================================ C4 — CURED, and stays in as cured
q('C4', 0, 'may be settled', note='the drafted defect MOO-99 S1 found; must be absent')
q('C4', 1, 'the certified subsidy for the election is settled under this subdivision',
  note='the enacted automatic operator, death/disability/error rescission limb')
q('C4', 4, 'the certified subsidy is settled', note='the operator family, all automatic')

# ============================================================ C5 — the admission ambiguity
q('C5', 1, '"Unreduced retirement eligibility date" means the earliest date on which the member '
           'may retire under § 51.1-153, or under subsection A or C of § 51.1-155.1')
q('C5', 1, '"Qualifying retirement" means a service retirement under § 51.1-153, or under '
           'subsection A or C of § 51.1-155.1')
# MOO-99 S4's ALTERNATIVE fix, enacted section-wide rather than definition-wide:
q('C5', 1, 'For the purposes of this section the member may retire under subsection A or C of '
           '§ 51.1-155.1 only where the member has incurred an involuntary separation, or the '
           "member's office has been lawfully abolished, as the case may be, on or before the "
           "date as of which the member's unreduced retirement eligibility date is determined",
  note="MOO-99 S4's alternative fix, enacted; this is what closes the projection reading")
q('C5', 1, 'who is involuntarily separated from state service', where='code:51.1-155.1',
  note='§ 51.1-155.1 A, the condition the confinement restates')
q('C5', 0, 'For the purposes of this definition, the member may retire under subsection A or C',
  note="S4's fix in its definition-only form — NOT the form enacted; must not be quoted as enacted")

# ============================================================ C6 — the cap and the report
q('C6', 2, 'notwithstanding that the amount available to be reserved is thereby exceeded',
  note='the over-cap command, live and unchanged')
q('C6', 1, 'and the certified subsidy for the election is settled under this subdivision '
           'notwithstanding that the rescinded determination had taken effect')
# fix 1 — the bounded trigger, ENACTED, and the two further limbs enacted with it
q('C6', 1, 'upon an application filed no later than the date on which the determination took '
           'effect', note='fix 1 enacted: the trigger is bounded for the ordinary filer')
q('C6', 1, 'upon an application the filing of which did not require a waiver of a ninety-day '
           'notification period set forth in subsection A or B of § 51.1-156',
  note='second limb, enacted — this is also C16 cure 1')
q('C6', 1, 'upon an application as to which the Medical Board has made a certification described '
           'in clause (ii) of subsection H of § 51.1-156',
  note='third limb, enacted — C16 cure 2, AND the limb that carries no outer date: see C6 §residual')
# fix 2 — the report list, ENACTED
q('C6', 1, 'the number of determinations rescinded and the service credit restored under '
           'subdivision G 4', note='fix 2 enacted')
q('C6', 1, 'every amount by which a reservation reinstated under subdivision G 4 caused a '
           'limitation in subdivision D 2 to be exceeded', note='fix 2 enacted, second item')
# fix 3 — the report tail, ENACTED in different words from the drafted form
q('C6', 1, 'and (b) the date of the last rescission under subdivision G 4 that has occurred on or '
           'before the date stated in clause (a)', note='fix 3 enacted, in the drafter\'s own words')
q('C6', 0, 'until the first December 1 following the later of that date and the date of the last '
           'rescission under subdivision G 4',
  note='fix 3 in its MOO-99 S5 form — NOT the form enacted; must not be quoted as enacted')
# fix 4 — the enactment clause, ENACTED
q('C6', 1, 'and to make every refund, payment, notice, determination, rescission, restoration, '
           'and reinstatement required by § 51.1-142.4', where='s1',
  note='fix 4 enacted, third enactment clause (i)')
q('C6', 1, 'the reporting and evaluation duties in subsection J of § 51.1-142.4 shall continue in '
           'effect until the last report and evaluation required by that subsection has been '
           'submitted', where='s1', note='fix 4 enacted, third enactment clause (iii)')
q('C6', 1, 'to the Chairmen of the House Committee on Appropriations and the Senate Committee on '
           'Finance and Appropriations no later than 15 days after the reinstatement, which '
           'notice shall not identify any member', note='the disclosure duty, live')
q('C6', 1, 'shall state every reinstatement and every such excess in the report required by '
           'subsection J; and shall accept no further election until the excess is eliminated',
  note='the two further controls, live')
q('C6', 1, 'an excess is eliminated when the aggregate of the amounts charged against the '
           'limitation in the first sentence of subdivision D 2 no longer exceeds that limitation')
q('C6', 1, 'certifies that: (a) the disability and its cause existed on the date the member’s '
           'employment was terminated', where='code:51.1-156',
  note='§ 51.1-156 H clause (ii) — carries no outer date, which is C6’s surviving limb')
q('C6', 1, 'good cause shall exist and the Board shall waive such ninety-day notification periods',
  where='code:51.1-156', note='H is mandatory once the Medical Board certifies — the pass-12 ban')

# ============================================================ C12 — the cap moves, not the cost
q('C12', 1, '$3,000,000')
q('C12', 1, 'a contingency amount equal to `[20]` percent of that certified subsidy',
  note='the contingency is a BRACKETED figure at revision 70, not a settled 20 percent')
q('C12', 0, 'non-completion', note='the bill carries no non-completion concept at all')
q('C12', 2, 'shall recertify the certified subsidy to reflect the service credit so credited',
  note='the enacted C11 repair, which reaches C12’s per-member arithmetic')
q('C12', 2, 'to complete payment by the completion date',
  note='D 7’s no-release carve-out for the non-completer')

# ============================================================ C13 — the settlement bar
q('C13', 1, 'No certified subsidy is settled under this subdivision after the reservation for the '
            'election has been released in full in accordance with subdivision D 7 and has not '
            'been reinstated under this subdivision, or after a determination under subdivision 2 '
            'or 3 has taken effect and has not been rescinded, reversed, or modified',
  note='the bar AS CURED — pass 17’s one-amendment cure, enacted, both limbs')
q('C13', 0, 'no certified subsidy is settled under this subdivision after the reservation for the '
            'election has been released in accordance with subdivision D 7 or after a '
            'determination under subdivision 2 or 3 has taken effect',
  note='the bar as pass 17 quoted it — SUPERSEDED. Not quotable at revision 70')
q('C13', 1, 'the service credit to be purchased is reduced to the amount the member may purchase '
            'as recertified')
q('C13', 1, 'if a recertification under subdivision 6 reduces the certified subsidy')
q('C13', 1, 'as though the determination had not been made')
q('C13', 1, 'Where a reservation has been released otherwise than in accordance with subdivision '
            'D 7, or has been released in accordance with that subdivision where a determination '
            'is thereafter rescinded under this subdivision', note='the reinstatement route the cure needs')
q('C13', 2, 'to retire as required by subsection F', note='D 7 carve-out, as pass 17 verified')

# ============================================================ C14 — the reversal duty
q('C14', 1, 'the Board shall restore or credit service credit as this subdivision provides, and, '
            'where the determination as reversed or modified is such that the certified subsidy '
            'falls to be settled under subdivision 1 or under this subdivision, shall recertify '
            'and settle it accordingly, no later than 60 days after the reversal or modification',
  note='the duty AS CURED — the conditioning clause AND the referent correction, both enacted')
q('C14', 0, 'restore or credit service credit as this subdivision provides, and shall recertify '
            'and settle the certified subsidy as this subdivision requires, no later than 60 days '
            'after the reversal or modification',
  note='the duty as pass 17 quoted it — SUPERSEDED. Not quotable at revision 70')

# ============================================================ C15 — the arrears formula
q('C15', 1, "the next payment of the member's retirement allowance shall include every amount by "
            'which the amounts paid to the member fall short of the amounts that would have been '
            'payable to the member had the determination, as reversed or modified, taken effect '
            'on the date on which the determination took effect, or, where the determination is '
            'reversed in its entirety, had no determination been made',
  note='the formula AS CURED — net, plus the entirety limb. Both of pass 17’s limbs enacted')
q('C15', 0, "the next payment of the member's retirement allowance shall include every amount "
            'that would have been payable to the member had the determination, as reversed or '
            'modified, taken effect on the date on which the determination took effect',
  note='the gross formula as pass 17 quoted it — SUPERSEDED. Not quotable at revision 70')
q('C15', 0, 'no amount shall be collected, offset, or withheld from any member, retiree, '
            'survivor, beneficiary, or estate of a member on account of an involuntary '
            'separation, of a rescission or restoration under this subdivision, or of any other '
            'event to which this subdivision applies',
  note='G 4’s no-collection sentence as pass 17 quoted it — not quotable in these words')
q('C15', 1, 'no amount payable to the member or to any survivor, beneficiary, or estate of the '
            'member shall be reduced by reason of any such deferral or application',
  note='the live no-reduction limb, verified by the Director at revision 70 (MOO-206 §1.3)')

# ============================================================ C16 — the disability carve-out
q('C16', 1, 'A determination under subdivision 2 or 3 that has taken effect is not affected by an '
            'approval of the member for a disability retirement allowance upon an application '
            'filed after the date on which the determination took effect, except as this '
            'subdivision provides for the rescission of the determination',
  note='the saving sentence, live — and it now carries an express exception for the rescission, '
       'which pass 17’s quotation did not have')
q('C16', 0, 'approval of the member for a disability retirement allowance under this chapter upon '
            'an application filed after the date on which the determination took effect',
  note='the saving sentence as pass 17 quoted it — SUPERSEDED. Not quotable at revision 70')
q('C16', 0, 'as to which the Board was required by subsection H of § 51.1-156 to waive the '
            'ninety-day notification period',
  note='the counterfactual trigger pass 17 found — GONE. Replaced by the Medical Board anchor')
q('C16', 2, 'ninety-day notification period', where='code:51.1-156')

# ============================================================ C17 — the hardship branch
q('C17', 1, 'if the member retires in a qualifying retirement no later than 90 days after the '
            'date of the involuntary separation')
q('C17', 1, 'or, where this sentence is applied otherwise than in the determination of the '
            "member's unreduced retirement eligibility date, on or before the member's effective "
            'date of retirement',
  note='pass 17’s drafted cure for item 119, ENACTED. This is what releases the laid-off member')
q('C17', 1, 'Where this section does not state a date as of which the member’s unreduced '
            'retirement eligibility date is determined, that date is, for the purposes of the '
            'preceding sentence, the date on which the Board makes the certification, '
            'recertification, determination, statement, or other decision in which that date is '
            'applied', note='the residual sentence, live and unchanged')

# ============================================================ C18 — the settlement count
q('C18', 1, 'Where a determination under subdivision 2 or 3 has taken effect, a member may file '
            'with the Board written evidence that the member was unable to retire in a qualifying '
            'retirement by reason of an error of the Board',
  note='the error route — NO period is stated for the member’s filing. C18’s open limb')
q('C18', 2, 'is reversed or modified on reconsideration under subsection M or on judicial review',
  note='the judicial-review route — two sites: the reinstatement sentence and the reversal duty')
q('C18', 0, 'interest', note='zero at 69 and 70; re-counted here rather than taken from MOO-206')
q('C18', 27, 'refund', note='the refund vehicle the money statement omits')

# ============================================================ C19 — classification evidence only
q('C19', 1, 'except that the aggregate of all such non-running by reason of such requests and by '
            'reason of applications for a disability retirement allowance filed after the first '
            'such application shall not exceed 120 days',
  note='the FIRST application’s pendency is still uncapped — C19 holds at revision 70')
q('C19', 1, 'The Board shall not make a determination under subdivision 2, and shall not give the '
            'notice required by subdivision 2, while an application of the member for a '
            'disability retirement allowance under this chapter is pending')

# ============================================================ C20–C23 — the MOO-141 patch, unapplied
q('C20', 2, 'no later than 15 days after it acts upon the request',
  note="Edit 2's FIND. TWO sites: the definition's backstop notice (Edit 2's target) and M 2's "
       'application duty (Edit 2 does not reach it). A bare count of 2 is not a defect')
q('C20', 0, 'no later than 15 days after it gives its decision upon the request',
  note="Edit 2's READ — applied nowhere")
q('C21', 1, 'The Board shall act upon a request for reconsideration within 90 days',
  note='the duty to ACT; there is still no duty to give a decision')
q('C22', 1, 'retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board '
            'acts upon the request', note="Edit 3's FIND, unmoved — the patch is applied nowhere")
q('C22', 0, 'until 120 days after the Board acts upon the request', note="Edit 3's READ — applied nowhere")
q('C22', 0, 'the Board is deemed to act upon that request, and to last act upon it, on the date '
            'on which the Board first acts upon it', note="Edit 1's operative clause — applied nowhere")
q('C23', 1, 'the aggregate of all tolling under this subsection shall not exceed 120 days, '
            'excluding any period after the expiration of the 90 days allowed by this subsection '
            'and before the Board acts upon the request, provided that the aggregate of all '
            'periods so excluded shall not exceed 90 days',
  note="clause (ii), live — and the 90-day post-tolling window of C23 precision 8 is IN the text")

# ============================================================ C3 — the language hold
q('C3', 0, 'exception path')
q('C3', 0, 'backstop')
q('C3', 0, 'rare')

# ============================================================ print
w = max(len(r[0]) for r in rows)
print()
for entry, s, where, n, want, ok, note in rows:
    exp = '' if want is None else f'  [asserted {want}]'
    lbl = s if len(s) <= 76 else s[:73] + '...'
    print(f'{"    " if ok else "FAIL"} {entry:<{w}} {where:<15} {n:>3}  {lbl}{exp}')
    if note:
        print(f'{"":>{w + 26}}- {note}')

print()
if fails:
    print(f'== {len(fails)} assertion(s) FAILED — do not print the entry until it is repaired:')
    for f in fails:
        print('   ', f)
else:
    print('== every asserted count holds on the live text at store revision 72')
sys.exit(1 if fails else 0)
