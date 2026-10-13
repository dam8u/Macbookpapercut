# -*- coding: utf-8 -*-
"""MOO-164 — the Policy Director's disposition of revision 8, verified at store revision 72.

This script does the one thing neither kit can do on its own: it lifts the CURRENT fixtures out of
BOTH kits and counts the cross-patch invariants between them.

  MOO-164 revision 8   moo164-act-versus-notice/verify_r72_v8.py   (thirteen substitutions, +4,210)
  MOO-141 revision 9   moo141-rev72/verify_r72.py                  (four edits, +1,716)

Why it exists. Each kit holds a FIXTURE of the other patch, and each fixture is one revision stale
right now: MOO-164's holds MOO-141 revision 8, and MOO-141's lifts MOO-164 revision 7. Both kits
report 0 failures while testing a superseded other half. That is MOO-141 F11's coupling and
MOO-209 F19's lesson — `verbatim` is a counted claim — applied to the pair rather than to either.

What it proves, and every one of these is a count:

  1. The two saving bodies DIVERGED at MOO-141 revision 9, and the repair is not a pure insertion:
     the series' "or" moves. Derived mechanically from MOO-141's own body, not re-typed.
  2. The two exceptions now differ in MORE than the two locators that must differ, because MOO-164
     revision 8 re-cut the R-6 descriptor on MOO-214 S3 and MOO-141 revision 9 adopted the
     SUPERSEDED paraphrase. MOO-141 §3.3's symmetry claim is false as of 02:05 on 13 October 2026.
  3. The §3.3 cross-reference as drafted at MOO-164 §18.5 contains both characterisations that
     MOO-141 §3.4's requirement 1 withdraws. The Director's replacement sentence contains neither,
     contains requirement 2's fact, and contains no date formula.
  4. The combined text applies in either order, byte-identically, at store revision 72.
  5. With the three repairs the saving bodies read (2, 0) — MOO-141's own expected-to-change line.
  6. The three candidates the Director takes (164-14, 164-15, 164-17) all resolve exactly once in
     the repaired applied text and 0 times in the base, and 164-18 — declined — still resolves once
     in the base and 0 times applied.

Run: python3 verify_xpatch_r72.py [live.md]
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
SHA = hashlib.sha256(S1.encode()).hexdigest()
print(f'== base: whole document {len(doc)}; enacted §1 {len(S1)}; §1 sha256 {SHA[:16]}')
chk('the base has NOT moved since revision 8 — §1 sha asserted, not inferred', SHA[:16], '83a10b74950b5272')
chk('§1 length', len(S1), 134012)


def lift(path, cut):
    """Execute a kit's prefix up to `cut` and return its namespace. Nothing is re-typed."""
    src = open(path, encoding='utf-8').read()
    ns = {'__name__': 'kit', '__file__': path}
    argv = sys.argv
    sys.argv = ['kit', SRC]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src[:src.index(cut)], path, 'exec'), ns)
    finally:
        sys.argv = argv
    return ns


K164 = lift(os.path.join(HERE, '..', 'moo164-act-versus-notice', 'verify_r72_v8.py'), '\nHELD = {')
K141 = lift(os.path.join(HERE, '..', 'moo141-rev72', 'verify_r72.py'),
            "\nprint('\\n== anchors at store revision 72")

EDITS164 = K164['EDITS']                 # thirteen substitutions, revision 8
SAVING_164 = K164['SAVING']              # the saving body as 164-7 carries it
EXC_164_7 = K164['E164_7_EXC']           # 164-7's exception, revision 8, with the S3 descriptor
R6_DESC = K164['R6_DESCRIPTOR']          # the determinate descriptor this cut coined
XREF_V8 = K164['XREF']                   # the cross-reference as drafted at §18.5
SAVING_141 = K141['SAVING_R9']           # the saving body as Edit 1 carries it after F7
EXC_141_E1 = K141['E1_EXC_R9']           # Edit 1's exception, revision 9, with the PARAPHRASE
E1_F, E1_R = K141['E1_F'], K141['E1_R']
print(f'   lifted: MOO-164 {len(EDITS164)} substitutions; MOO-141 saving body {len(SAVING_141)} chars')

# ======================================================================= 1. the saving bodies
print('\n== 1. the saving bodies diverged at MOO-141 revision 9, and the repair is not an insertion')
chk('the two bodies are NOT byte-identical today', SAVING_164 == SAVING_141, False)
chk('MOO-164 revision 8 body', len(SAVING_164), 256)
chk('MOO-141 revision 9 body', len(SAVING_141), 367)
chk('the divergence MOO-141 F7 published', len(SAVING_141) - len(SAVING_164), 111)
FAMILIES = ('to restore or credit service credit, to recertify or settle a certified subsidy, or to '
            'pay or include any amount, ')
chk('the three duty families stand once in MOO-141\'s body', SAVING_141.count(FAMILIES), 1)
chk('and 0 times in MOO-164\'s', SAVING_164.count(FAMILIES), 0)
# The naive repair — insert the families — does NOT reproduce MOO-141's body, because the series'
# "or" moves off "to give" and onto the new last item. Counted both ways so the drafter cannot
# take the insertion on its own.
NAIVE = SAVING_164.replace('or whether the Board has performed', FAMILIES + 'or whether the Board has performed')
chk('insertion ALONE does not reproduce MOO-141\'s body', NAIVE == SAVING_141, False)
REPAIRED = SAVING_164.replace(', or to give a notice or a decision,', ', to give a notice or a decision,')
REPAIRED = REPAIRED.replace('or whether the Board has performed', FAMILIES + 'or whether the Board has performed')
chk('insertion + the series repair reproduces it BYTE FOR BYTE', REPAIRED == SAVING_141, True)
chk('the series repair alone is the four characters MOO-141 did not spend',
    len(SAVING_141) - len(NAIVE), -3)

# ======================================================================= 2. the two exceptions
print('\n== 2. the two exceptions differ in MORE than the locators — MOO-214 S3 against MOO-141 F11')
LOCATORS = (('under this subsection', 'under subsection M'),
            ('in subsection A', 'in this subsection'))
swapped = EXC_164_7
for a, b in LOCATORS:
    chk(f'164-7\'s exception carries the locator "{a}" once', swapped.count(a), 1)
    swapped = swapped.replace(a, b)
chk('after the locator swap the two exceptions are STILL not equal', swapped == EXC_141_E1, False)
PARAPHRASE = "give the member written notice of the member's final qualifying retirement date,"
chk('MOO-141 Edit 1 carries the SUPERSEDED paraphrase, once', EXC_141_E1.count(PARAPHRASE), 1)
chk('MOO-164 164-7 carries the determinate descriptor, once', EXC_164_7.count(R6_DESC), 1)
chk('and the paraphrase 0 times', EXC_164_7.count(PARAPHRASE), 0)
E1_EXC_REPAIRED = EXC_141_E1.replace(PARAPHRASE, 'give ' + R6_DESC + ',')
chk('substituting the descriptor into Edit 1 makes the two equal MODULO THE TWO LOCATORS',
    swapped == E1_EXC_REPAIRED, True)
chk('so the repair is the descriptor and nothing else', len(E1_EXC_REPAIRED) - len(EXC_141_E1), 19)

# ======================================================================= 3. the cross-reference
print('\n== 3. the §18.5 cross-reference against MOO-141 §3.4\'s FOUR requirements')
SIGNPOST = 'which applies where the Board acts upon a request more than once'
OWN_SCOPE = 'applies where the Board does not act upon the request'
chk('§18.5 characterises Edit 1\'s scope — requirement 1 forbids it', XREF_V8.count(SIGNPOST), 1)
chk('§18.5 characterises 164-7\'s own scope — requirement 1 forbids that too',
    XREF_V8.count(OWN_SCOPE), 1)
# The Director's replacement. It states requirement 2's fact and nothing else, and it names the
# other deeming by its CONTENT, so with MOO-141 absent the class is empty and the sentence is inert.
XREF_NEW = ('A date on which the Board is deemed by this subsection to act upon a request is a date '
            'on which the Board acts upon the request for the purposes of any provision of this '
            'section deeming the Board to act upon a request, and to last act upon it, on the date '
            'on which the Board first acts upon it.')
chk('the replacement characterises neither scope (requirement 1)',
    XREF_NEW.count(SIGNPOST) + XREF_NEW.count(OWN_SCOPE) + XREF_NEW.count('applies where'), 0)
chk('it supplies requirement 2\'s fact, once',
    XREF_NEW.count('is a date on which the Board acts upon the request for the purposes of'), 1)
chk('it names the other deeming by content, not by citation', XREF_NEW.count('subsection A'), 0)
for tok in ('no later than', ' days', 'month', 'date of', 'except'):
    chk(f'requirement 3 — no "{tok}" in the replacement', XREF_NEW.count(tok), 0)
chk('and it is shorter than the sentence it replaces', len(XREF_NEW) < len(XREF_V8), True)

# ======================================================================= the repaired patches
print('\n== the three repairs, applied to 164-7 and to Edit 1')
E164_7_V8 = EDITS164[6][2]
chk('164-7 as cut at revision 8 carries the short saving once', E164_7_V8.count(SAVING_164), 1)
chk('   and the §18.5 cross-reference once', E164_7_V8.count(XREF_V8), 1)
E164_7_R9 = E164_7_V8.replace(SAVING_164, SAVING_141).replace(XREF_V8, XREF_NEW)
# F4's residue, routed to this issue by MOO-141 §3.2: 164-7 deems a LAST act, and a real act can
# follow it. Edit 1 answers it when both land ("first acts" controls); this sentence answers it when
# MOO-164 lands alone, in Edit 1's own policy, and adds nothing when Edit 1 is present.
F4_RESIDUE = (' A subsequent act of the Board upon the request does not affect the date on which the '
              'Board is deemed by this subsection to act, or to last act, upon it.')
chk('164-7 deems a LAST act — F4\'s residue is in its own words',
    E164_7_V8.count('to act upon the request, and to last act upon it,'), 1)
E164_7_R9 = E164_7_R9.replace(XREF_NEW, XREF_NEW + F4_RESIDUE)
chk('the repaired 164-7 carries MOO-141\'s saving body once', E164_7_R9.count(SAVING_141), 1)
chk('   and the short body 0 times', E164_7_R9.count(SAVING_164), 0)
chk('   and the withdrawn signpost 0 times', E164_7_R9.count(SIGNPOST), 0)
print(f'   164-7: +{len(E164_7_R9) - len(E164_7_V8)} characters over revision 8 '
      f'({len(SAVING_141) - len(SAVING_164)} saving, {len(XREF_NEW) - len(XREF_V8)} cross-reference, '
      f'{len(F4_RESIDUE)} F4 residue)')

E1_R_REPAIRED = E1_R.replace(EXC_141_E1, E1_EXC_REPAIRED)
chk('Edit 1 repaired: the descriptor once', E1_R_REPAIRED.count(R6_DESC), 1)
chk('   the paraphrase 0 times', E1_R_REPAIRED.count(PARAPHRASE), 0)
chk('   the saving body unchanged, once', E1_R_REPAIRED.count(SAVING_141), 1)

# ======================================================================= 4. both orders
print('\n== 4. the combined text at store revision 72, in both orders')
PAIRS164 = [(f, r) for _l, f, r in EDITS164]
PAIRS164_R9 = [(f, E164_7_R9 if r == E164_7_V8 else r) for f, r in PAIRS164]
PAIRS141 = [(E1_F, E1_R), (K141['E2_F'], K141['E2_R']), (K141['E3_F'], K141['E3_R']),
            (K141['E4_F'], K141['E4_R'])]
PAIRS141_R = [(f, E1_R_REPAIRED if f == E1_F else r) for f, r in PAIRS141]


def apply(body, pairs):
    out = body
    for f, r in pairs:
        n = out.count(f)
        assert n == 1, f'FIND resolves {n} times: {f[:60]!r}'
        out = out.replace(f, r, 1)
    return out


only164 = apply(S1, PAIRS164)
only141 = apply(S1, PAIRS141)
chk('MOO-164 revision 8 alone: the published delta', len(only164) - len(S1), 4210)
chk('MOO-141 revision 9 alone: the published delta', len(only141) - len(S1), 1716)
ab = apply(only164, PAIRS141)
ba = apply(only141, PAIRS164)
chk('revision 8 + revision 9 is byte-identical in either order', ab == ba, True)
chk('combined delta', len(ab) - len(S1), 5926)
chk('MOO-164\'s thirteen FINDs all resolve exactly once in the base',
    all(S1.count(f) == 1 for f, _r in PAIRS164), True)
chk('   and none is disturbed by MOO-141 revision 9',
    all(only141.count(f) == 1 for f, _r in PAIRS164), True)
chk('MOO-141\'s four FINDs all resolve exactly once in the base',
    all(S1.count(f) == 1 for f, _r in PAIRS141), True)
chk('   and none is disturbed by MOO-164 revision 8',
    all(only164.count(f) == 1 for f, _r in PAIRS141), True)

print('\n== the same, with the three repairs — order independence must survive them')
only164r = apply(S1, PAIRS164_R9)
only141r = apply(S1, PAIRS141_R)
abr = apply(only164r, PAIRS141_R)
bar = apply(only141r, PAIRS164_R9)
chk('repaired: byte-identical in either order', abr == bar, True)
chk('repaired MOO-164 delta', len(only164r) - len(S1), 4210 + (len(E164_7_R9) - len(E164_7_V8)))
chk('repaired MOO-141 delta', len(only141r) - len(S1), 1716 + 19)
chk('<u>/</u> balanced in the combined repaired text', abr.count('<u>') - abr.count('</u>'), 0)

# ======================================================================= 5. (2, 0)
print('\n== 5. MOO-141\'s expected-to-change line: the saving bodies read (2, 0) after the repair')
chk('today, on the combined text', (ab.count(SAVING_141), ab.count(SAVING_164)), (1, 1))
chk('after the repair', (abr.count(SAVING_141), abr.count(SAVING_164)), (2, 0))
swapped_pair = abr.count(EXC_164_7), abr.count(E1_EXC_REPAIRED)
chk('and the two exceptions each stand once, differing only in the two locators', swapped_pair, (1, 1))
chk('the superseded paraphrase is gone from the whole combined text', abr.count(PARAPHRASE), 0)
# The descriptor stands at four sites after both patches, but only two of them carry the determiner
# "a": 164-5 and 164-13(a) read "any notice …" and "every notice …". Counted on the core phrase, so
# the four-site claim is a count and not a guess.
CORE = R6_DESC[len('a '):]
chk('the descriptor\'s core phrase stands at four sites after both patches', abr.count(CORE), 4)
chk('   two of them with the determiner "a" — the two exceptions', abr.count(R6_DESC), 2)
chk('   and the two others are 164-5\'s "any" and 164-13(a)\'s "every"',
    (abr.count('any notice of a date required by that definition by reason of'),
     abr.count('every notice of a date required by that definition by reason of')), (1, 1))

# ======================================================================= 6. the candidates
print('\n== 6. the four candidates, as the Policy Director would have disposed of them')
print('   (the board answered at 02:08 on 13 October 2026 and took 164-18 as well — section 7)')
TAKEN = [
 ('164-14 (MOO-209 F10) — "or the application is otherwise disposed of"',
  'until the date on which the Board grants or denies it.',
  'until the date on which the Board grants or denies it or the application is otherwise disposed of.'),
 ('164-15 (MOO-214 S6) — the non-receipt saving',
  'no later than 30 days after the Board gives the notice; and a notice so filed',
  'no later than 30 days after the Board gives the notice or, where the Board mails the notice and '
  'the member does not receive it within that period, no later than 30 days after the member '
  'receives it and in no case later than 90 days after the Board gives the notice; and a notice so filed'),
]
C17_FIND = 'and supersedes any notice of retirement previously filed by the member.'
C17 = ('A failure to state in the written statement required by that definition, or in any notice of a '
       'kind described in the preceding sentence, every matter this subdivision requires to be stated '
       'in it is a failure of the Board to state in a certification a matter this section requires to '
       'be stated in it for the purposes of subsection M; a person adversely affected by it may seek '
       'review under subsection M no later than 30 days after the date on which the written statement '
       'or notice is given to the member; and the Board shall state every such failure in the report '
       'required by subsection J.')
for lbl, f, r in TAKEN:
    chk(f'{lbl} — FIND in the base (must be 0: it amends this cut\'s own text)', S1.count(f), 0)
    chk(f'{"":6} — FIND in the repaired applied text', only164r.count(f), 1)
chk('164-17 — FIND in the base', S1.count(C17_FIND), 0)
chk('164-17 — FIND in the repaired applied text', only164r.count(C17_FIND), 1)
withall = only164r
for _l, f, r in TAKEN:
    withall = withall.replace(f, r, 1)
withall = withall.replace(C17_FIND, C17_FIND + ' ' + C17, 1)
chk('all three applied together: no FIND collision', withall.count(C17), 1)
# §17.10 published 164-14 at "+39 characters". The words as drafted there are +44 with the space
# they need. Counted here so the figure is corrected rather than carried.
chk('164-14 as drafted at §17.10 is +44, not the published +39',
    len(TAKEN[0][2]) - len(TAKEN[0][1]), 44)
print(f'   the three taken candidates add +{len(withall) - len(only164r)} characters '
      f'(164-14 +{len(TAKEN[0][2]) - len(TAKEN[0][1])}, 164-15 +{len(TAKEN[1][2]) - len(TAKEN[1][1])}, '
      f'164-17 +{len(C17) + 1})')
# 164-15 is taken, so clause (iv) must be conformed in the SAME cut. Counted so it cannot be
# forgotten: s12 and clause (iv) share the 30-day formula today and must share the new one.
NONRECEIPT = 'where the Board mails the notice and the member does not receive it within that period'
chk('the non-receipt limb is 0 in the base', S1.count(NONRECEIPT), 0)
chk('   0 in the applied text before 164-15', only164r.count(NONRECEIPT), 0)
chk('   and 1 after it — in s12 ONLY', withall.count(NONRECEIPT), 1)
print('   ^ THE CONFORMANCE OWED, counted: 164-15 puts the non-receipt limb in s12 and clause (iv)')
print('     still states the bare 30 days. 1 against 0 is the mismatch M1 was about, one revision on.')
print('     Clause (iv) must carry the same two limbs in the SAME cut.')
C18_F = ('Nothing in this subdivision prevents the payment of a retirement allowance to a member while '
         'an application of the member for a disability retirement allowance under this chapter is '
         'pending, and the determination required by this subdivision shall take effect notwithstanding '
         'that a retirement allowance has been paid to the member while such an application was pending.')
chk('164-18 — recommended for declining; TAKEN by the board. Its FIND is in the base, once',
    S1.count(C18_F), 1)
chk('   164-12\'s own FIND is inside 164-18\'s', C18_F.count(EDITS164[12][1]), 1)
# §18.6 says the containment makes the two "mutually exclusive". Counted, the exclusivity is
# ONE-DIRECTIONAL: 164-12 is an INSERTION whose REPLACE opens with its own FIND, so 164-18's FIND
# SURVIVES 164-12 and a careless applier can take both. The other order does block.
chk('   164-18\'s FIND survives 164-12 — so the containment is NOT exclusivity',
    only164r.count(C18_F), 1)
chk('   the block runs the other way: after 164-18, 164-12\'s FIND is gone',
    S1.replace(C18_F, 'X', 1).count(EDITS164[12][1]), 0)
print('   ^ RECORD CORRECTION, and it now bites, because the board took 164-18: the containment does')
print('     not make the two exclusive, so "drop 164-12" has to be done by the applier, not by the')
print('     text. The substantive exclusivity does hold — 164-18 removes "pending" from G 2, which')
print('     would orphan 164-12\'s definition of it.')
chk('164-9 stays HELD — its FIND is 164-1\'s own new cap, 0 in the base',
    S1.count('and in no case later than 48 days after the Board acts upon the request'), 0)
chk('   and 1 in the repaired applied text, so MOO-204 still has its insertion point',
    only164r.count('and in no case later than 48 days after the Board acts upon the request'), 1)

# ======================================================================= 7. the board's answers
# The board answered the three questions at 02:08:17 UTC on 13 October 2026 (interaction
# b4f375e1-49db-4875-8110-85817b235c90, resolved by local-board):
#   164-15  take as drafted, with the 90-day outer bound     -> option 1
#   164-17  take into THIS cut                               -> option 1
#   164-18  TAKE IT AND DROP EDIT 164-12                     -> option 1  (against my recommendation)
# The third answer is the one with consequences, and they are counted here rather than described.
print('\n== 7. the board\'s answers of 02:08 on 13 October 2026, applied and counted')
C18_R = ('Nothing in this subdivision prevents the payment of a retirement allowance to a member at any '
         'time after the member has filed an application for a disability retirement allowance under this '
         'chapter and before the Board has granted or denied it, and the determination required by this '
         'subdivision shall take effect notwithstanding that a retirement allowance has been paid to the '
         'member during that time.')
chk('164-18 delta, as the question put it to the board', len(C18_R) - len(C18_F), 33)
chk('"pending" in enacted §1 today', S1.count('pending'), 9)
chk('   two of the nine are in subdivision G 2, and both are in 164-18\'s one sentence',
    C18_F.count('pending'), 2)
AFTER18 = S1.replace(C18_F, C18_R, 1)
chk('   so 164-18 does remove "pending" from G 2 entirely — §18.6\'s claim, counted',
    AFTER18.count('pending'), 7)
chk('and Edit 164-12 can no longer apply, which is why the board was asked to drop it',
    AFTER18.count(EDITS164[12][1]), 0)

# 164-14 was drafted against Edit 164-12's OWN new sentence. Dropping 164-12 destroys its insertion
# point: the words "until the date on which the Board grants or denies it." never come into being.
# It has to be re-cut against 164-18's words, and the defect F10 found survives into them unchanged.
chk('164-14\'s revision-8 FIND is 0 in the base', S1.count(TAKEN[0][1]), 0)
chk('   and 0 in the text as the board has now settled it — it has NO insertion point',
    AFTER18.count(TAKEN[0][1]), 0)
C14_F = 'and before the Board has granted or denied it,'
C14_R = 'and before the Board has granted or denied it or the application has otherwise been disposed of,'
chk('F10\'s open end survives into 164-18\'s words, once', AFTER18.count(C14_F), 1)
chk('   and the re-cut 164-14 is +50 there, not the +44 of the revision-8 wording',
    len(C14_R) - len(C14_F), 50)

PAIRS_BOARD = [(f, r) for f, r in PAIRS164_R9 if f != EDITS164[12][1]]
PAIRS_BOARD.append((C18_F, C18_R))
PAIRS_BOARD.append((C14_F, C14_R))
PAIRS_BOARD.append((TAKEN[1][1], TAKEN[1][2]))
PAIRS_BOARD.append((C17_FIND, C17_FIND + ' ' + C17))
board164 = apply(S1, PAIRS_BOARD)
chk('the revision-9 target: twelve substitutions + four, every FIND exactly once',
    len(PAIRS_BOARD), 16)
chk('   Edit 164-12\'s inserted definition sentence is absent — it is DROPPED, not re-pointed',
    board164.count(EDITS164[12][2][len(EDITS164[12][1]):].strip()), 0)
chk('   (and G 4\'s own two "is pending from the date" phrases are untouched — they are not it)',
    board164.count('is pending from the date on which the member files it'), 2)
chk('   and 164-18\'s rewrite stands, carrying 164-14\'s words inside it',
    board164.count(C14_R), 1)
print(f'   revision-9 target delta over enacted §1: +{len(board164) - len(S1)}')
print(f'   (revision 8 was +4210; the 164-7 repairs are +{len(E164_7_R9) - len(E164_7_V8)}; '
      f'164-12 out is {len(EDITS164[12][1]) - len(EDITS164[12][2])}; '
      f'164-18 in is +{len(C18_R) - len(C18_F)}; 164-14 +{len(C14_R) - len(C14_F)}; '
      f'164-15 +{len(TAKEN[1][2]) - len(TAKEN[1][1])}; 164-17 +{len(C17) + 1})')
chk('the order independence of the two patches survives the board\'s answers',
    apply(board164, PAIRS141_R) == apply(only141r, PAIRS_BOARD), True)
chk('   combined delta', len(apply(board164, PAIRS141_R)) - len(S1),
    len(board164) - len(S1) + 1735)
chk('the saving bodies still read (2, 0) on the combined revision-9 text',
    (apply(board164, PAIRS141_R).count(SAVING_141), apply(board164, PAIRS141_R).count(SAVING_164)),
    (2, 0))
chk('164-9 still has its insertion point for MOO-204',
    board164.count('and in no case later than 48 days after the Board acts upon the request'), 1)
chk('the non-receipt limb stands once, in s12', board164.count(NONRECEIPT), 1)
chk('164-17\'s route stands once', board164.count(C17), 1)
chk('<u>/</u> balanced in the revision-9 target', board164.count('<u>') - board164.count('</u>'), 0)

print('\n' + ('ALL CHECKS PASS' if not fail else f'{fail} CHECK(S) FAILED'))
sys.exit(1 if fail else 0)
