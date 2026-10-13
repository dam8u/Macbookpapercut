# -*- coding: utf-8 -*-
"""MOO-141 — Edit 2 re-cut as **revision 8**, verified at store revision 71 on the combined text.

Why this exists. The Drafting Specialist's 01:20 report on 13 October 2026 was counted at store
revision 70 and found a defect in the **combined** text: after MOO-164's Edit 164-7 is applied, the
Board is deemed to act in two no-act classes, and 164-7's express exception makes that deeming date
R-6's notice duty — but MOO-141's Edit 2 re-keys R-6's fifteen days to the *giving of a decision*,
and in the deemed classes no decision is ever given. The duty is then keyed to an event that never
occurs. The cure is in MOO-141's provision, so it is drafted here.

The base has moved again: store revision 71, document revision 90. Every count below is taken
there. Nothing is written to the store.

MOO-164's thirteen substitutions are not re-typed. They are lifted out of
`moo164-act-versus-notice/verify_r70_v7.py` by executing its prefix, so that a divergence between
that kit and this one is impossible rather than merely unlikely.

Run: python3 verify_r71.py live.md
"""
import contextlib
import hashlib
import io
import os
import re
import sys

fail = 0


def chk(label, got, want):
    global fail
    ok = got == want
    if not ok:
        fail += 1
    print(f'   [{"ok" if ok else "FAIL"}] {label}: {got} (expected {want})')


HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'live.md')
doc = open(SRC, encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
print(f'== base: whole document {len(doc)}; enacted §1 {len(S1)}; §1 sha256 '
      f'{hashlib.sha256(S1.encode()).hexdigest()[:16]}')
print('   store revision 71, document revision 90. Revision 69 sha was 83a10b74… only if unchanged.')

# ---------------------------------------------------------------- MOO-164's kit, lifted not re-typed
KIT = os.path.join(HERE, '..', 'moo164-act-versus-notice', 'verify_r70_v7.py')
src = open(KIT, encoding='utf-8').read()
prefix = src[:src.index('\nHELD = {')]
ns = {'__name__': 'kit'}
argv = sys.argv
sys.argv = ['kit', SRC]
try:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(prefix, KIT, 'exec'), ns)
finally:
    sys.argv = argv
EDITS = ns['EDITS']
SAVING = ns['SAVING']
E164_7_EXC = ns['E164_7_EXC']
E1_EXC = ns['E1_EXC']
E1_F = ns['E1_F_R68']
E1_R = ns['E1_R']
E3_F = ns['E3_F']
E3_R = ns['E3_R6']          # the board's figure, 120 days, answered 14:15 on 12 October 2026
print(f'   lifted from the MOO-164 kit: {len(EDITS)} substitutions, saving body {len(SAVING)} chars')

# ---------------------------------------------------------------- Edit 2, revision 8
E2_F = ("it shall give the member written notice of that date no later than 15 days after it acts "
        "upon the request.")
# Revision 6's Edit 2 — card (g), the board's answer of 13:13 on 12 October 2026. Kept so that the
# change is visible and so that the fallback form is in the record rather than in prose.
E2_R6 = ("it shall give the member written notice of that date no later than 15 days after it gives "
         "its decision upon the request.")
# Revision 8. The first limb is revision 6's, unchanged, so the board's decided effect is untouched
# in the class the board was shown. The second limb is residual and is confined on its face to the
# two classes in which no decision upon the request is ever given.
E2_LIMB2 = ("except that where the request is denied otherwise than by a decision of the Board upon "
            "it, or where the period allowed by this section for acting upon the request expires "
            "without the Board's acting upon it, it shall give that notice no later than 15 days "
            "after the date on which the Board acts upon the request.")
E2_R = E2_R6[:-1] + ', ' + E2_LIMB2

print('\n== anchors at store revision 71 — §1-scoped, which is the only valid uniqueness test')
DEAD = ("every period within which a person may or must act that runs from the giving of that "
        "statement or notice is extended by three days.</u>")
chk('E1 FIND as written for store rev 65 (DEAD, kept visible)', S1.count(DEAD), 0)
chk('E1 FIND as re-cut at revision 69', S1.count(E1_F), 1)
chk('E2 FIND', S1.count(E2_F), 1)
chk('E3 FIND', S1.count(E3_F), 1)
chk('E2 revision 6 REPLACE not in the base', S1.count(E2_R6), 0)
chk('E2 revision 8 second limb not in the base', S1.count(E2_LIMB2), 0)
print(f'   whole-document: E1 {doc.count(E1_F)}, E2 {doc.count(E2_F)}, E3 {doc.count(E3_F)}')
chk('E1 FIND whole-document — a sweep now quotes IT, which is new at revision 71', doc.count(E1_F), 2)
print('   NOTE: E3 read 2 whole-document at revisions 63, 64 and 69 because a sweep quoted it.')
chk('E3 whole-document today — the sweep that quoted it is gone', doc.count(E3_F), 1)

print('\n== MOO-164 is still unapplied, so both patches still have work to do')
chk('164-7 / Edit 1 saving body not in the base', S1.count(SAVING), 0)
chk("164-1's act-keyed tolling endpoint still live", S1.count('until 30 days after the Board acts upon the request'), 1)
chk("M 2's deemed-denial sentence intact", S1.count('that denial constitutes the final determination of the Board upon the reconsideration'), 1)
chk("G 4's anti-delay sentence intact", S1.count('shall not extend that aggregate'), 1)
chk("both of G 4's express 'first's intact", S1.count('the Board first acts upon it'), 2)

print('\n== MOO-164\'s thirteen FINDs at a base they have not seen — free result for them')
for label, f, _r in EDITS:
    chk(label.split(' ')[0], S1.count(f), 1)

print('\n== the act-upon family in enacted §1 at revision 71')
for p, want in (('acts upon', 9), ('act upon', 9), ('acting upon', 2), ('action upon', 2),
                ('last acts upon', 1), ('first acts upon', 2)):
    chk(p, S1.count(p), want)
# 'acts upon' moved 8 -> 9 between revisions 69 and 71. The ninth is not the Board's act.
NEW = ('no later than 15 days after the Director of the Department of Planning and Budget or his '
       'designee acts upon the Board\'s request under subdivision 3')
chk("the ninth 'acts upon' is the DPB Director's, not the Board's", S1.count(NEW), 1)
chk("Edit 1's deeming is confined to the Board's own acting, so it does not reach it",
    "the Board's acting" in E1_R and 'Director' not in E1_R, True)


def apply(body, pairs, scope='§1'):
    out = body
    for f, r in pairs:
        assert out.count(f) == 1, f'FIND not unique in {scope}: ' + f[:60]
        out = out.replace(f, r, 1)
    return out


MOO141_R8 = [(E1_F, E1_R), (E2_F, E2_R), (E3_F, E3_R)]
MOO141_R6 = [(E1_F, E1_R), (E2_F, E2_R6), (E3_F, E3_R)]
MOO164 = [(f, r) for _l, f, r in EDITS]

print('\n== applied to a copy: MOO-141 alone')
P8 = apply(S1, MOO141_R8)
P6 = apply(S1, MOO141_R6)
chk('revision 6 §1 delta (published +847)', len(P6) - len(S1), 847)
chk('revision 8 second limb length', len(E2_LIMB2), 311)
chk('revision 8 §1 delta', len(P8) - len(S1), 847 + len(E2_LIMB2) + 1)
chk('revision 8 §1 delta is +1159', len(P8) - len(S1), 1159)
chk('no word of the bill is deleted by Edit 2 — revision 6 text survives inside revision 8',
    P8.count(E2_R6[:-1]), 1)
chk('<u>/</u> balance in §1 unchanged', (P8.count('<u>'), P8.count('</u>')),
    (S1.count('<u>'), S1.count('</u>')))
chk('one saving body, with one exception naming one duty', P8.count(SAVING), 1)
chk("Edit 1's exception still names M 2's duty alone", P8.count(E1_EXC), 1)
chk("and does not name R-6's duty", P8.count('give the member written notice of the member\'s final qualifying retirement date'), 0)

print('\n== the defect, counted on the combined text — the whole point of this re-cut')
C_R6 = apply(apply(S1, MOO164), MOO141_R6)      # MOO-164 + MOO-141 revision 6: the defect
C_R8 = apply(apply(S1, MOO164), MOO141_R8)      # MOO-164 + MOO-141 revision 8: the cure
chk("164-7's deeming is in the combined text", C_R8.count("to act upon the request, and to last act upon it, on the date of that denial"), 1)
chk("164-7's exception names R-6's duty", C_R8.count(E164_7_EXC), 1)
chk('revision 6: R-6 has ONE deadline and it is decision-keyed only',
    (C_R6.count(E2_R6), C_R6.count(E2_LIMB2)), (1, 0))
chk('revision 8: R-6 has a residual deadline for the no-decision classes',
    C_R8.count(E2_LIMB2), 1)
chk('the residual limb names the deemed-denial class', C_R8.count('where the request is denied otherwise than by a decision of the Board upon it'), 1)
chk('the residual limb names the no-act class', C_R8.count("the period allowed by this section for acting upon the request expires without the Board's acting upon it"), 1)
chk('the residual limb measures from the act, which is what 164-7 deems',
    C_R8.count('it shall give that notice no later than 15 days after the date on which the Board acts upon the request'), 1)
chk('the ordinary two-act class is untouched: the decision-keyed limb is first and intact',
    C_R8.index(E2_R6[:-1]) < C_R8.index(E2_LIMB2), True)

print('\n== order independence of the two patches, on the combined text')
chk('MOO-164 then MOO-141 == MOO-141 then MOO-164',
    apply(apply(S1, MOO164), MOO141_R8) == apply(apply(S1, MOO141_R8), MOO164), True)
chk('combined §1 delta', len(C_R8) - len(S1), (len(apply(S1, MOO164)) - len(S1)) + 1159)
chk("MOO-164's own published delta, re-derived here at a base they have not seen", len(apply(S1, MOO164)) - len(S1), 3375)
print(f'   MOO-164 alone: +{len(apply(S1, MOO164)) - len(S1)};  MOO-141 revision 8: +1159;  '
      f'combined: +{len(C_R8) - len(S1)}')

print('\n== the standalone case: Edit 2 revision 8 applied without MOO-164')
# The residual limb measures from "the date on which the Board acts upon the request". Without
# 164-7 there is no such date in the two classes it names, so the limb is inert — it is no worse
# than the base and it leaves no dangling reference, because it names no deeming and no subsection.
chk('the residual limb contains no cross-reference to any subsection', re.search(r'subsection|subdivision', E2_LIMB2) is None, True)
chk('the residual limb contains no reference to a deeming', 'deem' in E2_LIMB2, False)

print('\n== the D 1 lateness channel, which is what makes the residual limb bite — and its cap')
chk('the 12-month aggregate cap on excluded D 1 extensions is intact and unmoved',
    C_R8.count('the aggregate of all extensions so excluded shall not exceed 12 months'), 1)
chk('it reads the same in the base', S1.count('the aggregate of all extensions so excluded shall not exceed 12 months'), 1)
chk("D 1's lateness sentence reaches R-6's notice only on 164-5's broader descriptor",
    C_R8.count('any notice of a date required by that definition by reason of the Board\'s action upon a request, later than the time required by that definition'), 1)
chk('the narrower pre-164-5 descriptor is gone from the combined text',
    C_R8.count("any notice of a date required by that definition upon the Board's action upon a request"), 0)
chk("'later than the time required by' occurrences unchanged by this patch",
    (S1.count('later than the time required by'), P8.count('later than the time required by')), (3, 3))

print('\n== invariants after the combined application')
chk('first acts upon', C_R8.count('first acts upon'), 3)
chk('<u>/</u> balanced', C_R8.count('<u>') - C_R8.count('</u>'), 0)
for s in ('that denial constitutes the final determination of the Board upon the reconsideration',
          'shall not extend that aggregate',
          'An applicant who is denied or wait-listed retains every right to purchase service credit'):
    chk('saved provision intact: ' + s[:48], C_R8.count(s), 1)

print('\n' + ('ALL CHECKS PASS' if not fail else f'{fail} CHECK(S) FAILED'))
sys.exit(1 if fail else 0)
