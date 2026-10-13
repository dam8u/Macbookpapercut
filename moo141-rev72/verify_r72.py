# -*- coding: utf-8 -*-
"""MOO-141 — revision 9, cut and verified at store revision 72 on MOO-215's sixteen findings.

What changed from revision 8, and why.

  Edit 1  exception gains R-6's notice duty (F4 — my 01:32 asymmetry ruling is REVERSED), and the
          saving's enumeration gains the three duty families F7 found outside it.
  Edit 2  class 1 is redefined by an AFFIRMATIVE fact (F1 fatal, F2, F10). Class 2 and the
          decision-keyed first limb are unchanged — the first limb is still the board's 13:13
          answer of 12 October 2026, character for character.
  Edit 3  unchanged. 120 days, the board's answer of 14:15 on 12 October 2026.
  Edit 4  NEW (F6, and F3's class). A notice duty attached to the definition's expiry sentence,
          keyed to the expiry. No deeming, no cross-reference, no exception, and — counted below —
          outside subdivision D 1's lateness descriptor on both its pre- and post-164-5 wording.

Base: store revision 72 is RECORD ONLY. Enacted §1 is byte-identical to store revision 71 —
same length, same sha256 — so every count the MOO-215 pass took at revision 71 carries, and this
kit proves it rather than assuming it.

MOO-164's thirteen substitutions are lifted out of `verify_r70_v7.py` by executing its prefix, not
re-typed, so a divergence between the two kits is impossible rather than merely unlikely.

Run: python3 verify_r72.py live.md
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
chk('§1 is byte-identical to store revision 71 (sha asserted, not inferred)',
    SHA[:16], '83a10b74950b5272')
chk('§1 length unchanged from revision 71', len(S1), 134012)

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
SAVING_R8 = ns['SAVING']
E164_7_EXC = ns['E164_7_EXC']
E1_EXC_R8 = ns['E1_EXC']
E1_F = ns['E1_F_R68']
E3_F = ns['E3_F']
E3_R = ns['E3_R6']          # the board's figure, 120 days, answered 14:15 on 12 October 2026
print(f'   lifted from the MOO-164 kit: {len(EDITS)} substitutions, revision-8 saving body '
      f'{len(SAVING_R8)} chars')

# ================================================================ revision 9's four edits
# ---- Edit 1 -----------------------------------------------------------------------------------
# F7. The saving protected a closed list. A duty to restore or credit service credit, to recertify
# and settle a certified subsidy, or to pay an amount was in neither the enumeration nor the
# exception, and store revision 61 makes a failure to perform within a required period expressly
# reviewable. Three duty families are added to the MAIN CLAUSE, which extends what the deeming does
# NOT determine. It adds no exception, so it does not collide with the §3.3 constraint.
SAVING_R9 = ("nothing in the preceding sentence determines the date by which the Board is required to "
             "act upon a request, to make a determination, to give a notice or a decision, to restore "
             "or credit service credit, to recertify or settle a certified subsidy, or to pay or "
             "include any amount, or whether the Board has performed such a duty within a period "
             "required by this section.")
# F4. My 01:32 ruling was that Edit 1's exception must name M 2's duty alone. The premise failed:
# the Board can act more than once upon a request AND be in one of the residual limb's classes, and
# in that case the residual limb measures R-6's deadline from the Board's act, which Edit 1's
# deeming does reach. So the exception is operative, not surplusage, and it is added. The two
# exceptions now differ ONLY in the locators that must differ, because Edit 1 sits in subsection A
# and 164-7 sits in subsection M.
E1_EXC_R9 = ('Except for the purposes of the duty of the Board under subsection M to act upon an '
             'application no later than 15 days after it acts upon the request and the duty of the '
             'Board under the definition of "final qualifying retirement date" in this subsection to '
             "give the member written notice of the member's final qualifying retirement date,")
E1_DEEM = (" For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period "
           "begins or ends upon, or is measured from, the Board's acting, or last acting, upon a "
           "request, or where a date is fixed by reference to the month in which the Board acts, or "
           "last acts, upon a request, the Board is deemed to act upon that request, and to last act "
           "upon it, on the date on which the Board first acts upon it. ")
E1_R = E1_F[:-len('</u>')] + E1_DEEM + E1_EXC_R9 + " " + SAVING_R9 + "</u>"
E1_R8 = E1_F[:-len('</u>')] + E1_DEEM + E1_EXC_R8 + " " + SAVING_R8 + "</u>"

# ---- Edit 2 -----------------------------------------------------------------------------------
E2_F = ("it shall give the member written notice of that date no later than 15 days after it acts "
        "upon the request.")
# Revision 6 — card (g), the board's answer of 13:13 on 12 October 2026. Kept so the change stays
# visible and the decided text is in the record rather than in prose.
E2_R6 = ("it shall give the member written notice of that date no later than 15 days after it gives "
         "its decision upon the request.")
# Revision 8's residual limb. KEPT so F1's defect stays visible rather than being quietly fixed.
E2_LIMB2_R8 = ("except that where the request is denied otherwise than by a decision of the Board upon "
               "it, or where the period allowed by this section for acting upon the request expires "
               "without the Board's acting upon it, it shall give that notice no later than 15 days "
               "after the date on which the Board acts upon the request.")
# Revision 9. ONE change: class 1 is defined by the affirmative operative fact — a denial that
# happened WITHOUT an act — instead of by the absence of a decision. Membership is then fixed at the
# moment of the act and cannot be conferred afterwards by a court (F1), the class test no longer
# uses a word this section does not use for what the Board does with a request (F2), and the cure no
# longer depends on M 2's four-word "for the purposes of this subsection" limiter (F10).
E2_LIMB2 = ("except that where the request is denied without the Board's having acted upon it, or "
            "where the period allowed by this section for acting upon the request expires without "
            "the Board's acting upon it, it shall give that notice no later than 15 days after the "
            "date on which the Board acts upon the request.")
E2_R = E2_R6[:-1] + ', ' + E2_LIMB2
E2_R8 = E2_R6[:-1] + ', ' + E2_LIMB2_R8

# ---- Edit 4, new ------------------------------------------------------------------------------
# F6, and F3's class. The definition's expiry sentence fixes the member's final qualifying
# retirement date "notwithstanding any other provision of this definition" when the Board does not
# act. R-6's chapeau requires that "the Board's ACTION upon a request determines" the date, so in
# that class R-6 is not engaged at all and she is never told the date she has acquired. The cure is
# a notice duty attached to the expiry sentence and keyed to the expiry — not a widening of R-6's
# chapeau, which would collide with R-6's "state that date in its decision" branch.
E4_F = ("in which that period expired, the member's final qualifying retirement date is, "
        "notwithstanding any other provision of this definition, that first day.")
E4_NEW = (" Where the member's final qualifying retirement date is determined by the preceding "
          "sentence, the Board shall give the member written notice of that date no later than 15 "
          "days after the expiration of the period for acting upon the request referred to in that "
          "sentence.")
E4_R = E4_F + E4_NEW

print('\n== anchors at store revision 72 — §1-scoped, which is the only valid uniqueness test')
DEAD = ("every period within which a person may or must act that runs from the giving of that "
        "statement or notice is extended by three days.</u>")
chk('E1 FIND as written for store rev 65 (DEAD, kept visible)', S1.count(DEAD), 0)
chk('E1 FIND as re-cut at revision 69', S1.count(E1_F), 1)
chk('E2 FIND', S1.count(E2_F), 1)
chk('E3 FIND', S1.count(E3_F), 1)
chk('E4 FIND (new at revision 9)', S1.count(E4_F), 1)
print(f'   whole-document: E1 {doc.count(E1_F)}, E2 {doc.count(E2_F)}, E3 {doc.count(E3_F)}, '
      f'E4 {doc.count(E4_F)}')
chk('E2 revision 6 REPLACE not in the base', S1.count(E2_R6), 0)
chk('revision 8 residual limb not in the base', S1.count(E2_LIMB2_R8), 0)
chk('revision 9 residual limb not in the base', S1.count(E2_LIMB2), 0)
chk('neither saving body is in the base — MOO-164 is unapplied',
    (S1.count(SAVING_R8), S1.count(SAVING_R9)), (0, 0))

print('\n== F1 counted: why the affirmative class is not the old class in new words')
chk('revision 8 class 1 is keyed to the ABSENCE of a decision',
    'denied otherwise than by a decision' in E2_LIMB2_R8, True)
chk('revision 9 class 1 is keyed to a denial WITHOUT an act',
    "denied without the Board's having acted upon it" in E2_LIMB2, True)
chk('revision 9 class 1 uses the word "decision" nowhere',
    'decision' in E2_LIMB2, False)
chk('the decision-keyed FIRST limb is untouched — the board\'s decided text survives exactly once',
    E2_R.count(E2_R6[:-1]), 1)
chk('and it is ordered first, so the board\'s class is reached first',
    E2_R.index(E2_R6[:-1]) < E2_R.index(E2_LIMB2), True)
chk('class 2 is unchanged from revision 8',
    E2_LIMB2_R8[E2_LIMB2_R8.index(', or where'):] == E2_LIMB2[E2_LIMB2.index(', or where'):], True)
# F10: M 2's limiter is no longer load-bearing for the cure, because class 1 no longer asks whether
# the deemed denial is a "decision".
chk("M 2's four-word limiter is live in the base", S1.count('a case decision as defined in § 2.2-4001 for the purposes of this subsection'), 1)
chk('revision 9 does not depend on it: the class test asks only whether the Board acted',
    'case decision' in E2_LIMB2 or 'decision' in E2_LIMB2, False)

print('\n== F7 counted: the three duty families, and the enumeration that did not reach them')
for d in ('restore or credit service credit', 'recertify and settle', 'no later than 60 days after the reversal or modification'):
    chk('duty family present in the base: ' + d[:46], S1.count(d) >= 1, True)
for d in ('to restore or credit service credit', 'to recertify or settle a certified subsidy', 'to pay or include any amount'):
    chk('revision 8 saving did NOT enumerate: ' + d[:44], d in SAVING_R8, False)
    chk('revision 9 saving enumerates: ' + d[:44], d in SAVING_R9, True)
chk('revision 9 adds to the MAIN CLAUSE and adds no exception',
    SAVING_R9.count('Except') + SAVING_R9.count('except'), 0)
chk('the second branch\'s "such a duty" is unchanged, so it carries the longer list',
    SAVING_R9.endswith('or whether the Board has performed such a duty within a period required by this section.'), True)
chk('saving body grows by', len(SAVING_R9) - len(SAVING_R8), 111)

print('\n== F4 counted: the premise that failed, and why the reversal moves no date')
# 164-7's two deeming predicates are BOTH no-act predicates, so the date 164-7 deems necessarily
# precedes any real act of the Board upon the same request. Edit 1 selects the FIRST act. The two
# deemings therefore agree by construction, not by chance — which is why naming R-6's duty in
# Edit 1's exception moves no date.
E164_7 = [r for _l, _f, r in EDITS if 'is deemed' in r][0]
chk("164-7 limb 1's predicate is a denial by operation of M 2's no-act sentence",
    E164_7.count('Where a request is denied by operation of the preceding sentence'), 1)
chk("and M 2's sentence is itself predicated on the Board's NOT acting",
    S1.count('Where the Board does not act upon the request within 30 days after that notice is filed'), 1)
chk("164-7 limb 2's predicate is the Board's NOT acting within the period",
    E164_7.count('where the Board does not act upon a request under the definition'), 1)
chk('164-7 deems the act on the denial date or the day after expiry — both before any real act',
    E164_7.count('on the date of that denial or, as the case may be, on the day after the expiration of that period'), 1)
chk("Edit 1 selects the FIRST act, so it selects 164-7's deemed date",
    E1_R.count('on the date on which the Board first acts upon it'), 1)
chk("revision 8: Edit 1's exception named ONE duty", E1_EXC_R8.count('the duty of the Board'), 1)
chk("revision 9: it names TWO", E1_EXC_R9.count('the duty of the Board'), 2)
chk("and it names R-6's duty in 164-7's own words",
    "give the member written notice of the member's final qualifying retirement date," in E1_EXC_R9
    and "give the member written notice of the member's final qualifying retirement date," in E164_7_EXC, True)
# The two exceptions can never be byte-identical: each must locate the other subsection. What must
# be identical is the SAVING body, and after revision 9 the exceptions differ only in the locators.
chk('the two exceptions are not byte-identical, and cannot be', E1_EXC_R9 == E164_7_EXC, False)
chk('they differ ONLY in the two locators that must differ',
    E1_EXC_R9.replace('under subsection M', 'under this subsection').replace('in this subsection', 'in subsection A')
    == E164_7_EXC, True)
chk('revision 9 breaks byte-identity of the SAVING bodies — visible, not silent',
    SAVING_R9 == SAVING_R8, False)
print('   ^ this is the one thing revision 9 asks of MOO-164: 164-7\'s saving must take the same')
print('     three duty families, byte for byte, in the joint cut. F7 scopes the exposure to Edit 1')
print('     alone, so the words are inoperative in 164-7 — byte-identity is what they buy.')

print('\n== F6 counted: the class in which R-6 is never engaged, and Edit 4')
chk("R-6's chapeau requires the Board's ACTION to determine the date",
    S1.count("Where the Board's action upon a request determines a member's final qualifying retirement date under this definition"), 1)
chk('the expiry sentence fixes the date notwithstanding every other provision of the definition',
    S1.count('the member\'s final qualifying retirement date is, notwithstanding any other provision of this definition, that first day'), 2)
chk("the expiry sentence's class is a request that tolled under subsection M",
    S1.count('Where the Board does not act upon a request the filing of which tolled the running of the member\'s final qualifying retirement date under subsection M'), 1)
chk("164-7's no-act limb is confined to a request under the definition, so it does not deem there",
    E164_7.count('a request under the definition of "final qualifying retirement date" in subsection A'), 1)
chk('Edit 4 adds a duty and no deeming', 'deem' in E4_NEW, False)
chk('Edit 4 names no subsection and no subdivision', re.search(r'subsection|subdivision', E4_NEW) is None, True)
chk('Edit 4 keys the deadline to the expiry, not to an act', 'expiration of the period' in E4_NEW, True)
chk('Edit 4 does not repeat the period formula 164-4 re-cuts, so it is 164-4-proof',
    ('this definition allows' in E4_NEW) or ('allowed by this section' in E4_NEW), False)
# Edit 4 is fiscally inert on the D 1 channel: D 1's lateness extension reaches a notice required
# "upon"/"by reason of" the Board's ACTION. Edit 4's notice is required by reason of its NOT acting.
D1_PRE = "any notice of a date required by that definition upon the Board's action upon a request"
D1_POST = "any notice of a date required by that definition by reason of the Board's action upon a request"
chk("D 1's pre-164-5 descriptor is in the base", S1.count(D1_PRE), 1)
chk("Edit 4's notice is not required by reason of the Board's action, so D 1 does not reach it",
    ('action upon a request' in E4_NEW), False)

print('\n== Edit 4: the "preceding sentence" referents, which no earlier pass had to check')
PS = 'the preceding sentence'
base_ps = S1.count(PS)
print(f'   "{PS}" in the base: {base_ps}')


def apply(body, pairs, scope='§1'):
    out = body
    for f, r in pairs:
        assert out.count(f) == 1, f'FIND not unique in {scope}: ' + f[:60]
        out = out.replace(f, r, 1)
    return out


MOO141 = [(E1_F, E1_R), (E2_F, E2_R), (E3_F, E3_R), (E4_F, E4_R)]
MOO141_R8 = [(E1_F, E1_R8), (E2_F, E2_R8), (E3_F, E3_R)]
MOO164 = [(f, r) for _l, f, r in EDITS]

P9 = apply(S1, MOO141)
P8 = apply(S1, MOO141_R8)
# Two, not one: Edit 1's saving has carried "the preceding sentence" since revision 2 — it is how
# the saving refers to the deeming — and Edit 4 adds the second. Both are self-referring: each
# points at the sentence immediately before it inside its own REPLACE.
chk('the patch adds two "the preceding sentence" — Edit 1\'s saving and Edit 4\'s',
    P9.count(PS) - base_ps, 2)
chk("Edit 1's was already there at revision 8, so Edit 4 adds exactly one",
    P9.count(PS) - P8.count(PS), 1)
chk("Edit 1's refers to its own deeming sentence, which immediately precedes it",
    E1_R.index(E1_DEEM.strip()) < E1_R.index('nothing in ' + PS), True)
# R-7 must still point at R-6. Edit 4 is inserted BEFORE R-6, so R-7's referent is unmoved.
R7 = 'in which the Board gives a decision or notice required by the preceding sentence'
chk("R-7 still points at R-6 (N4 re-run for the new insertion point)", P9.count(R7), 1)
chk("and Edit 4 sits between the expiry sentence and R-6, not after R-6",
    P9.index(E4_NEW.strip()) < P9.index("Where the Board's action upon a request determines"), True)
chk('"Notwithstanding the two preceding sentences" is untouched and still earlier',
    P9.count('Notwithstanding the two preceding sentences'), 1)

print('\n== applied to a copy: MOO-141 revision 9 alone')
chk('revision 8 §1 delta (published +1159)', len(P8) - len(S1), 1159)
chk("Edit 1 delta = revision 8's, plus the exception's second duty, plus the saving's three families",
    len(E1_R) - len(E1_F),
    (len(E1_R8) - len(E1_F)) + (len(E1_EXC_R9) - len(E1_EXC_R8)) + (len(SAVING_R9) - len(SAVING_R8)))
chk("Edit 2 delta = revision 8's, less the four characters class 1 sheds",
    len(E2_R) - len(E2_F), (len(E2_R8) - len(E2_F)) + (len(E2_LIMB2) - len(E2_LIMB2_R8)))
chk('Edit 3 delta unchanged — the board\'s 120 days', len(E3_R) - len(E3_F), 15)
chk('revision 9 §1 delta', len(P9) - len(S1),
    (len(E1_R) - len(E1_F)) + (len(E2_R) - len(E2_F)) + (len(E3_R) - len(E3_F)) + len(E4_NEW))
print(f'   revision 8 +1159  ->  revision 9 +{len(P9) - len(S1)}  '
      f'(Edit 1 +{len(E1_R) - len(E1_F)}, Edit 2 +{len(E2_R) - len(E2_F)}, '
      f'Edit 3 +{len(E3_R) - len(E3_F)}, Edit 4 +{len(E4_NEW)})')
# E1's FIND reads 2 whole-document, because §5's own sweep quotes it. So the document-level check is
# done by splicing the amended §1 back in, which is the only valid form of it.
DOC9 = doc[:i] + P9 + doc[i + len(S1):]
chk('whole-document delta equals the §1 delta, so no edit lands outside §1',
    len(DOC9) - len(doc), len(P9) - len(S1))
chk("§5's sweep copy of Edit 1's FIND is untouched by the patch", DOC9.count(E1_F), 1)
# CORRECTION, found by this check failing. The claim "no word of the bill is deleted", made at
# 00:36 and again at 01:32, is FALSE and has been false since revision 5. Edits 1, 3 and 4 are pure
# insertions — each FIND survives verbatim inside its REPLACE. Edit 2 is not: card (g)'s re-key
# strikes three words. The revision-8 kit's check was labelled "no word of the bill is deleted by
# Edit 2" but only proved that revision 6's text survives inside revision 8, which is a different
# proposition. The deletion is the board's own decision of 13:13 on 12 October 2026, so the text is
# right and the claim about it was wrong.
chk('Edit 1 inserts inside the closing tag — every word of the FIND survives, in order',
    E1_F[:-len('</u>')] in E1_R and E1_R.endswith('</u>'), True)
chk('Edit 3 inserts four words — removing them recovers the FIND exactly',
    E3_R.replace('120 days after ', '', 1), E3_F)
chk('Edit 4 appends one sentence — removing it recovers the FIND exactly',
    E4_R.replace(E4_NEW, '', 1), E4_F)
chk('Edit 1 inserts one block before the closing tag — removing it recovers the FIND exactly',
    E1_R.replace(E1_DEEM + E1_EXC_R9 + ' ' + SAVING_R9, '', 1), E1_F)
chk('Edit 2 is the ONE edit that strikes words, and it strikes exactly three',
    E2_R6.replace('gives its decision upon', 'acts upon', 1), E2_F)
chk("and revision 9's own addition to Edit 2 strikes nothing",
    E2_R.replace(', ' + E2_LIMB2, '.', 1), E2_R6)
chk('<u>/</u> balance in §1 unchanged', (P9.count('<u>'), P9.count('</u>')),
    (S1.count('<u>'), S1.count('</u>')))
chk('one saving body, revision 9\'s', (P9.count(SAVING_R9), P9.count(SAVING_R8)), (1, 0))
chk('first acts upon', P9.count('first acts upon'), 3)

print('\n== the combined text: MOO-164 revision 7 + MOO-141 revision 9')
C = apply(apply(S1, MOO164), MOO141)
chk('order independence — MOO-164 then MOO-141 == MOO-141 then MOO-164',
    C == apply(apply(S1, MOO141), MOO164), True)
chk("MOO-164's published delta, re-derived at a base they have not seen",
    len(apply(S1, MOO164)) - len(S1), 3375)
chk('combined §1 delta', len(C) - len(S1), 3375 + (len(P9) - len(S1)))
chk("both deemings are in the combined text", (C.count(E1_DEEM.strip()), C.count('to act upon the request, and to last act upon it, on the date of that denial')), (1, 1))
chk("both exceptions name R-6's duty — the symmetry F4 asked for",
    C.count("give the member written notice of the member's final qualifying retirement date,"), 2)
chk('the two saving bodies in the combined text: 164-7 still carries revision 8\'s',
    (C.count(SAVING_R9), C.count(SAVING_R8)), (1, 1))
print('   ^ EXPECTED TO CHANGE: when MOO-164 takes the three duty families this reads (2, 0).')
chk('Edit 4 survives the combined application', C.count(E4_NEW.strip()), 1)
chk('R-7 still points at R-6 in the combined text', C.count(R7), 1)
chk('<u>/</u> balanced in the combined text', C.count('<u>') - C.count('</u>'), 0)
for s in ('that denial constitutes the final determination of the Board upon the reconsideration',
          'shall not extend that aggregate',
          'the aggregate of all extensions so excluded shall not exceed 12 months',
          'An applicant who is denied or wait-listed retains every right to purchase service credit'):
    chk('saved provision intact: ' + s[:50], C.count(s), 1)

print('\n== free result for MOO-164: their thirteen FINDs at store revision 72')
for label, f, _r in EDITS:
    chk(label.split(' ')[0], S1.count(f), 1)
chk('and none of them is disturbed by revision 9',
    all(P9.count(f) == 1 for _l, f, _r in EDITS), True)

print('\n' + ('ALL CHECKS PASS' if not fail else f'{fail} CHECK(S) FAILED'))
sys.exit(1 if fail else 0)
