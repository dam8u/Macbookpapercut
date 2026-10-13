# -*- coding: utf-8 -*-
"""MOO-213 addendum — the eight strings the PROPOSED corrections introduce, counted at store revision 72.

Kept separate from `count72.py` on purpose. `count72.py` is the re-base of the approved
revision-70 pass and its diff against `count70.py` is confined to the header and two labels.
Every string a *proposed correction* puts inside quotation marks is new, so it is counted here
rather than smuggled into the re-base. Same discipline, same base, separate file.

Base: `bill-text-s8` on MOO-42, document revision 368f5e41-56ab-4138-8bda-8553ae8eab04,
store revision 72 (13 October 2026). Counts over enacted § 51.1-142.4 (102,357 chars).

Run:  python3 count72_addendum.py     (reads $PAPERCLIP_TASK_SCRATCH_DIR/bill.md)
"""
import os
import re
import sys

SCRATCH = os.environ.get('PAPERCLIP_TASK_SCRATCH_DIR', '.')
doc = open(os.path.join(SCRATCH, 'bill.md'), encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
SEC = S1[S1.index('### <u>§ 51.1-142.4.'):S1.index('### § 51.1-162.')]


def norm(s):
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    s = s.replace('—', '--').replace('–', '-')
    s = re.sub(r'</?u>', '', s)
    s = s.replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', s)


B = norm(SEC)
print(f'== live base, store revision 72: enacted § 51.1-142.4 {len(SEC)} chars')
print()

ROWS = [
    # --- C6 correction 1: the two over-cap sites are DISTINCT sentences, and both are reached
    #     through the member's own remedies. This is what the drafted entry mis-describes.
    ('C6 fix 1', 1, 'the amount so reinstated shall be charged against the limitations in '
                    'subdivision D 2 notwithstanding that the amount available to be reserved is '
                    'thereby exceeded',
     'SITE 1 — the death-release limb: an amount released on death that would not have been '
     'released had the determination stood as it does after reconsideration or judicial review'),
    ('C6 fix 1', 1, 'and the reinstated reservation and contingency amount shall be charged '
                    'against the limitations in subdivision D 2 notwithstanding that the amount '
                    'available to be reserved is thereby exceeded',
     'SITE 2 — the general reinstatement sentence: release in error, OR rescission, OR reversal '
     'or modification on reconsideration under subsection M or on judicial review'),
    # --- C6 correction 2: the disclosure package is larger than the drafted entry states
    ('C6 fix 2', 1, 'of the date of the release, of whether the release was in accordance with '
                    'subdivision D 7, of the nature of any error, of the amount of any resulting '
                    'excess, and of the cause of the release',
     'the money-committee notice carries five particulars, not two'),
    ('C6 fix 2', 1, 'to each applicant then on the waiting list maintained under subdivision D 5 '
                    'no later than 15 days after the reinstatement, which notice shall not state '
                    'the cause of the release and shall not identify any member',
     'a SECOND 15-day notice duty, to every waiting-list applicant — absent from the drafted entry'),
    ('C6 fix 2', 1, 'shall request a confirmation under subdivision D 3 in respect of the amount '
                    'of any resulting excess no later than 15 days after the reinstatement',
     'the funding-confirmation procedure the Director named in ranking instruction 6 — it exists, '
     'and the over-cap sentence is already wired into it'),
    ('C6 fix 2', 1, 'and shall certify the amount of the excess to the Governor and to those '
                    'Chairmen as an amount necessary to fund the purposes of this section',
     'the excess is certified back to the Governor and the money committees as an amount '
     'necessary to fund — the $3,000,000 control is not escaped, it is re-asserted'),
    # --- Director ranking instruction 4: waiting-list placement is NOT a commitment
    ('rank 4', 1, 'shall accept the election if and when sufficient amounts become available '
                  'before the expiration of this section',
     'D 5: a waiting-list placement reserves nothing; the election is accepted only if and when '
     'amounts become available. Instruction 4 is satisfied by the enacted text'),
    ('rank 4', 1, 'A placement on the waiting list under this subdivision is a determination of '
                  'the Board for the purposes of subsection M',
     'and the placement is reviewable, so instruction 6\'s reconsideration procedure reaches it'),
]

fails = []
w = max(len(r[0]) for r in ROWS)
for entry, want, s, note in ROWS:
    n = B.count(norm(s))
    ok = n == want
    if not ok:
        fails.append((entry, want, n, s[:72]))
    lbl = s if len(s) <= 72 else s[:69] + '...'
    print(f'{"    " if ok else "FAIL"} {entry:<{w}} {n:>3}  {lbl}  [asserted {want}]')
    print(f'{"":>{w + 10}}- {note}')
    print()

if fails:
    print(f'== {len(fails)} assertion(s) FAILED:')
    for f in fails:
        print('   ', f)
else:
    print('== all 8 strings the proposed corrections introduce hold at store revision 72')
sys.exit(1 if fails else 0)
