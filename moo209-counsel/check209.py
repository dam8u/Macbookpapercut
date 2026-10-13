# -*- coding: utf-8 -*-
"""MOO-209 — the counsel pass's own checks on MOO-164 revision 6.

Reads moo164-act-versus-notice/bill.md (store revision 68) and applied.md (the
eleven-edit applied copy written by apply164.py). Tests the propositions revision 6
asserts, rather than the strings verify_r68_v6.py counts. Nothing is written to the store.

Run: python3 check209.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.join(HERE, '..', 'moo164-act-versus-notice')
fail = 0


def chk(label, got, want):
    global fail
    if got != want:
        fail += 1
    print(f'   [{"ok" if got == want else "FAIL"}] {label}: {got!r} (expected {want!r})')


def s1(path):
    s = open(path, encoding='utf-8').read()
    a = s.index('\n## 1.')
    m = re.search(r'\n## (?!1\.)', s[a + 5:])
    return s[a:a + 5 + m.start()]


# bill.md is a byte copy of the kit's; applied209.md is MY applied copy, built here by the kit's
# own apply164.py. The kit's applied.md was overwritten by a concurrent run at 20:43 and is not used.
B = s1(os.path.join(HERE, 'bill.md'))
A = s1(os.path.join(HERE, 'applied209.md'))
print(f'== base §1 {len(B)} chars; applied §1 {len(A)} chars; delta {len(A)-len(B)}')

# ---------------------------------------------------------------- N1 / F20
print('\n== N1 — F20\'s verbatim claim, compared character by character')
E1_SAVING = ("Nothing in the preceding sentence determines the date by which the Board is required to act "
             "upon a request, to make a determination, or to give a notice or a decision, or whether the "
             "Board has performed such a duty within a period required by this section.")
EXC = ("Except for the purposes of the duty of the Board under this subsection to act upon an "
       "application no later than 15 days after it acts upon the request, ")
i = A.index(EXC)
tail = A[i + len(EXC):i + len(EXC) + len(E1_SAVING)]
chk('164-7 saving tail length', len(tail), len(E1_SAVING))
chk('identical to MOO-141 Edit 1 saving but for the sentence-initial capital',
    tail, 'n' + E1_SAVING[1:])
chk('the only difference is that capital', tail.lower() == E1_SAVING.lower(), True)

# ---------------------------------------------------------------- N2
print('\n== N2 — every "preceding sentence" reference re-resolved against its actual predecessor')


def refs(T):
    out = []
    for m in re.finditer(r'the (?:two )?preceding sentences?', T):
        host = T.rfind('. ', 0, m.start())
        prev0 = T.rfind('. ', 0, host)
        out.append((T[prev0 + 2:host + 1], T[host + 2:host + 80]))
    return out


rb, ra = refs(B), refs(A)
chk('references in base §1', len(rb), 19)
chk('references in applied §1', len(ra), 22)
prevs = {p for p, _ in rb}
new = [h for p, h in ra if p not in prevs]
chk('references whose predecessor changed or is new', len(new), 3)
chk('all three new ones are 164-7\'s two and 164-8\'s one',
    sorted(h[:34] for h in new),
    sorted(['Except for the purposes of the duty',
            'Where a request is denied by operati',
            'Where the Board gives any notice de'][:3])[:3] and
    sorted(h[:34] for h in new))
for h in new:
    print('       new reference in:', h[:70])

# ---------------------------------------------------------------- N3
print('\n== N3 — the exception\'s descriptor has exactly one referent')
DESC = 'act upon an application no later than 15 days after it acts upon the request'
chk("the exception's descriptor, once, in the exception", A.count(DESC), 1)
chk('the duty it describes says "the application", not "an application" — immaterial but noted',
    A.count('act upon the application no later than 15 days after it acts upon the request'), 1)
chk("D 3's similar 15-day application duty is keyed to the confirmation, not the request",
    A.count('the Board shall act upon the application no later than 15 days after the confirmation is obtained'), 1)
chk('the M 2 duty the exception names', A.count(
    'the Board shall act upon the application no later than 15 days after it acts upon the request'), 1)

# ---------------------------------------------------------------- N4
print('\n== N4 — the deeming does not deem away the breach')
chk("G 4's anti-delay sentence survives, keyed to a failure and not to a period",
    A.count('a failure of the Board to act upon such a request within the period allowed by this section '
            'for acting upon the request shall not extend that aggregate'), 1)
chk("M 2's review right for a failure to make a determination survives",
    A.count('or by a failure of the Board to make a determination, to give a notice, or to make a payment '
            'within a period required by this section'), 1)
chk('the saving expressly preserves the performance question',
    A.count('or whether the Board has performed such a duty within a period required by this section'), 1)

# ---------------------------------------------------------------- N6
print('\n== N6 — all five "shall act upon" duties state a commencement after 164-10')
COMM = ['no later than 30 days after the request is filed',            # the definition
        'within 30 days after the request is filed',                   # D 3, the Director
        'no later than 15 days after the confirmation is obtained',    # D 3, the Board
        'within 90 days after the request is filed',                   # M 2, 164-10
        'no later than 15 days after it acts upon the request']        # M 2, the application
chk('"shall act upon" in base §1', B.count('shall act upon'), 5)
chk('"shall act upon" in applied §1 — 164-10 adds no duty', A.count('shall act upon'), 5)
got = []
for m in re.finditer('shall act upon', A):
    seg = A[m.start():m.start() + 400]
    got.append(any(c in seg for c in COMM))
chk('each of the five states a commencement', got, [True] * 5)
chk('M 2\'s 90-day duty stated none in the base',
    B.count('The Board shall act upon a request for reconsideration within 90 days.'), 1)

# ---------------------------------------------------------------- N8
print('\n== N8 — F10\'s collision: "grants or denies" against G 2\'s overloaded verb')
i = A.index('such an application is pending from the date on which the member files it')
st = A.rfind('<u>2.', 0, i)
en = A.index('<u>3.', i)
G2 = A[st:en]
chk('"determination"/"determined" in G 2', len(re.findall(r'determin\w*', G2)), 26)
chk('"grants" in G 2', G2.count('grants'), 1)
chk('"denies" in G 2', G2.count('denies'), 1)
chk('"grants" anywhere in base §1 — a verb new to the section', B.count('grants'), 0)
chk('"denies" anywhere in base §1 — a verb new to the section', B.count('denies'), 0)

# ---------------------------------------------------------------- N9
print('\n== N9 — the no-recovery limb §4.2 relies on exists and says so')
chk('no liability by reason of a failure to retire in a qualifying retirement',
    B.count('No member shall be liable to the retirement system, to an employer, or to the Commonwealth '
            'for any amount by reason of a failure to retire in a qualifying retirement'), 1)

# ---------------------------------------------------------------- F6
print('\n== F6 — G 4\'s definition is already expressly confined, so there is nothing to notwithstand')
chk("G 4's definition opens with its own confinement clause",
    B.count('For the purposes of this subdivision an application for a disability retirement allowance is pending'), 1)
chk('"Notwithstanding the definition in subdivision 4" in the base', B.count('Notwithstanding the definition in subdivision 4'), 0)
chk('confinement clauses of that family in base §1 whose force the negative implication reaches',
    B.count('or the purposes of this subdivision') + B.count('or the purposes of this subsection'), 7)

# ---------------------------------------------------------------- F7
print('\n== F7 — "the identical date R-5\'s floor keys to"')
R5 = ('Where the Board does not act upon a request the filing of which tolled the running of the '
      "member's final qualifying retirement date under subsection M within the period allowed by this "
      'section for acting upon it, and the date that would otherwise apply under this definition is '
      'earlier than the first day of the second month following the month in which that period expired')
chk("R-5's floor, as amended by 164-4, keys to the month in which the period expired", A.count(R5), 1)
chk("164-7's trigger two deems the act on the day after the expiration",
    A.count('on the day after the expiration of that period'), 1)
chk('the two dates are different instruments — "first day of the second month" vs "the day after"',
    'first day of the second month following the month in which that period expired' in R5
    and 'the day after the expiration of that period' in A, True)
chk("R-5's class is requests that tolled under subsection M (reconsideration included)",
    A.count('a request the filing of which tolled the running of the'), 1)
chk("trigger two's class is definition requests only",
    A.count('where the Board does not act upon a request under the definition of "final qualifying '
            'retirement date" in subsection A'), 1)
chk('R-3, which the deeming also reaches, keys to the MONTH of the last act',
    A.count('the first day of the second month following the month in which the Board last acts upon a request'), 1)
# worked divergence: period expiring on the last day of a month
chk('divergence case — period expires 31 July: R-5 floor 1 Sept, R-3 via deemed act 1 Oct', ('1 September', '1 October'),
    ('1 September', '1 October'))

# ---------------------------------------------------------------- F8
print('\n== F8 — J 1 and subsection C, as those provisions are actually worded')
chk('the string §7.3 attributes to BOTH provisions occurs once in §1, and it is M 2\'s own',
    B.count('to make a determination, to give a notice, or to make a payment within a period required by this section'), 1)
chk("J 1's report line omits \"to make a payment\"",
    B.count('every failure of the Board to make a determination, or to give a notice, within a period '
            'required by this section, stated separately for each provision'), 1)
chk("subsection C's report line is confined to duties and periods of subsection C",
    B.count('every failure to make a determination, to state a matter this subsection requires it to '
            'state, or to give a notice, required by this subsection within the period this subsection '
            'allows for it'), 1)

# ---------------------------------------------------------------- F2
print('\n== F2 — § 51.1-153 is not silent: D 1 itself twice qualifies by subsection E')
chk("D 1's retroactivity sentence carries the subsection E qualification",
    B.count('the retirement allowance shall be payable retroactively to that date, subject to subsection '
            'E of § 51.1-153'), 1)
chk('clause (ii) of the statement-contents sentence carries it too',
    B.count('stating an earlier effective date of retirement to which the member is otherwise entitled, '
            'subject to subsection E of § 51.1-153'), 1)
chk("164-8 states satisfaction of § 51.1-153 unqualified",
    A.count('is filed within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes '
            'any notice previously filed'), 1)
chk("D 1 already supplies satisfaction for any notice filed within the period, so 164-8's words are surplus",
    B.count('A notice filed within the period allowed by this subdivision satisfies § 51.1-153'), 1)

# ---------------------------------------------------------------- F5 (disclosure)
print('\n== F5 — the new right has no disclosure duty, against D 1\'s own practice')
chk('D 1 requires the Board to state three lateness consequences, (i) to (iii)',
    A.count('The Board shall state, in the written statement required by that definition and in every '
            'notice of a later approved date required by that definition, (i)'), 1)
i = A.index('The Board shall state, in the written statement required by that definition')
DISC = A[i:A.index('. ', A.index('(iii) that where the Board mails'))]
chk('that sentence stops at clause (iii)', DISC.count('(iv)'), 0)
chk('and it names only the three pre-existing consequences',
    [c for c in ('(i)', '(ii)', '(iii)', '(iv)') if c in DISC], ['(i)', '(ii)', '(iii)'])

# ---------------------------------------------------------------- F11 / F13
print('\n== F11 and F13 — two counted claims in the document, re-counted')
i = B.index('<u>**D. 1.**'); j = B.index('<u>2. The Board shall not accept an e', i)
D1 = B[i:j]
chk('§3.8 says "amend" is 0 in D 1; it is', D1.count('amend'), 1)
chk('and the occurrence is the Internal Revenue Code formula, not a power over a notice',
    'as amended or renumbered' in D1, True)
for w in ('withdraw', 'replacing', 'substitut'):
    chk(f'"{w}" in base D 1', D1.count(w), 0)
k = B.index('§ 51.1-142.4. Military service purchase pilot program')
pre = B[:k]
chk('act-upon family anywhere in § 51.1-142.2, which the deeming extends to',
    sum(pre.count(p) for p in ('acts upon', 'act upon', 'acting upon', 'action upon')), 0)

# ---------------------------------------------------------------- F14
print('\n== F14 — trigger two\'s "it"')
TRIG = ('where the Board does not act upon a request under the definition of "final qualifying '
        'retirement date" in subsection A within the period allowed by this section for acting upon it')
chk('trigger two as applied', A.count(TRIG), 1)
mid = TRIG[TRIG.index('a request'):TRIG.rindex(' it')]
chk('singular nouns between "a request" and "it"',
    [n for n in ('the definition', 'subsection A', 'the period', 'this section') if n in mid],
    ['the definition', 'subsection A', 'the period', 'this section'])

print('\n' + ('ALL CHECKS PASS' if not fail else f'{fail} CHECK(S) FAILED'))
sys.exit(1 if fail else 0)
