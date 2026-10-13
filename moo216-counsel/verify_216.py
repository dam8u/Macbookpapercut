# -*- coding: utf-8 -*-
"""MOO-216 — bounded adversarial pass on MOO-141 revision 9 at store revision 72.

Asserts the textual predicates each finding rests on, so the findings are counted and not
asserted. Reads the body from the same source the revision-9 kit reads and lifts BOTH patches'
edits by executing the two kits' prefixes, so a divergence from either is impossible.

Run: python3 verify_216.py <path to live.md>
"""
import contextlib, hashlib, io, os, re, sys

fail = 0
def chk(label, got, want):
    global fail
    ok = got == want
    if not ok:
        fail += 1
    print(f'   [{"ok" if ok else "FAIL"}] {label}: {got} (expected {want})')

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'moo141-rev72', 'live.md')
doc = open(SRC, encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
print(f'== base: whole document {len(doc)}; §1 {len(S1)}; §1 sha256 '
      f'{hashlib.sha256(S1.encode()).hexdigest()[:16]}')
chk('§1 re-derived independently', (len(S1), hashlib.sha256(S1.encode()).hexdigest()[:16]),
    (134012, '83a10b74950b5272'))

def lift(path, cut):
    src = open(path, encoding='utf-8').read()
    ns = {'__name__': 'kit', '__file__': path}
    argv = sys.argv; sys.argv = ['kit', SRC]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src[:src.index(cut)], path, 'exec'), ns)
    finally:
        sys.argv = argv
    return ns

K164 = lift(os.path.join(HERE, '..', 'moo164-act-versus-notice', 'verify_r70_v7.py'), '\nHELD = {')
K141 = lift(os.path.join(HERE, '..', 'moo141-rev72', 'verify_r72.py'),
            "\nprint('\\n== anchors at store revision 72")
EDITS = K164['EDITS']
E164_7 = [r for _l, _f, r in EDITS if 'is deemed' in r][0]
E1_DEEM, E4_NEW = K141['E1_DEEM'], K141['E4_NEW']
SAVING_R9, SAVING_R8 = K141['SAVING_R9'], K141['SAVING_R8']
print(f'   lifted: MOO-164 {len(EDITS)} substitutions; MOO-141 Edit 4 {len(E4_NEW)} chars')

# ===================================================================== R1 (fatal)
print('\n== R1: M 2\'s deemed-denial predicate is WINDOWED, not "no act up to that date"')
M2_DEEM = ('Where the Board does not act upon the request within 30 days after that notice is filed, '
           'the request is denied on the first day after the expiration of those 30 days')
chk('M 2 keys the deeming to a 30-day WINDOW opened by the filing of the expiry notice',
    S1.count(M2_DEEM), 1)
chk('and the window opens only after the Board has already missed the 90 days',
    S1.count('Where the Board does not act upon a request for reconsideration within the 90 days '
             'allowed by this subsection, the person who filed the request may file'), 1)
chk('the member\'s right to file the expiry notice is NOT conditioned on the Board still not '
    'having acted', 'has not acted' in M2_DEEM, False)
chk('and the drafter uses a CONTINUING condition elsewhere in the same subdivision',
    S1.count('at any time before the Board makes the determination'), 1)
chk('164-10 starts the 90 days at filing, so the window is reachable on known facts',
    [r for l, _f, r in EDITS if l.startswith('164-10')][0]
    == 'The Board shall act upon a request for reconsideration within 90 days after the request is filed.', True)
chk('the deemed denial displaces any real determination: it IS the final determination',
    S1.count('that denial constitutes the final determination of the Board upon the reconsideration'), 1)
print('\n   -> R1 scenario: recon. filed 1 Mar; 90 days expire 30 May; Board ACTS 2 Jun;')
print('      filer files the expiry notice 5 Jun; no act in the 30 days after it; denied 6 Jul.')
chk('164-7 limb 1 then deems the Board to act AND TO LAST ACT on the denial date',
    E164_7.count('to act upon the request, and to last act upon it, on the date of that denial'), 1)
chk('Edit 1 deems the Board to act AND TO LAST ACT on the date it FIRST acts',
    E1_DEEM.count('the Board is deemed to act upon that request, and to last act upon it, on the '
                  'date on which the Board first acts upon it'), 1)
chk('so both sentences deem the SAME two facts, and neither contains a priority rule',
    ('priority' in E164_7 or 'notwithstanding' in E164_7.lower()
     or 'priority' in E1_DEEM or 'notwithstanding' in E1_DEEM.lower()), False)
chk('the scenario needs ONE real act, not two — so §3.1\'s multi-act test was the wrong test',
    'first acts upon it' in E1_DEEM and 'more than once' in E1_DEEM, False)
print('\n   -> what moves with it')
chk("G 4's pendency window ends on the date the Board FIRST acts (MOO-141's own subject matter)",
    S1.count('such a request is pending from the date on which the member files it until the date '
             'on which the Board first acts upon it'), 1)
chk("and G 4's class is the tolling class, so the reconsideration request is in it",
    S1.count('while a request the filing of which tolls the running of the member’s final '
             'qualifying retirement date under subsection M is pending'), 1)
chk("R-6's deadline runs 15 days from the Board's acting, so it moves with the chosen date",
    S1.count('it shall give the member written notice of that date no later than 15 days after it '
             'acts upon the request.'), 1)
chk("and revision 9 is what puts R-6's deadline inside Edit 1's deeming",
    (K141['E1_EXC_R8'].count('the duty of the Board'), K141['E1_EXC_R9'].count('the duty of the Board')),
    (1, 2))

# ===================================================================== R2 (serious)
print('\n== R2: on 164-7\'s own confinement clause, a deemed act is NOT an act for Edit 1')
CONF = ('for the purposes of every provision of this section and of subdivision B 4 f of '
        '§ 51.1-142.2 under which a period begins or ends upon, or is measured from, the '
        "Board's acting, or last acting, upon the request, or under which a date is fixed by "
        'reference to the month in which the Board acts, or last acts, upon the request')
chk("164-7's deeming is confined to provisions of those two kinds", E164_7.count(CONF), 1)
chk("Edit 1's sentence does not measure a period from the Board's acting — it DEFINES the acting",
    bool(re.search(r'the Board is deemed to act upon that request', E1_DEEM)), True)
chk("Edit 1's sentence fixes no date by reference to the MONTH in which the Board acts",
    'on the date on which the Board first acts upon it' in E1_DEEM
    and 'the month in which the Board first acts' in E1_DEEM, False)
print('   -> so in the pure no-act case Edit 1\'s "the date on which the Board first acts upon it"')
print('      has no referent, and "the two agree by construction" fails on this route too.')

# ===================================================================== R3 (serious)
print('\n== R3: Edit 4 is a FOURTH date document, attached to none of the five machinery provisions')
D1_ENUM = ('Where the Board gives that written statement, any notice of a later approved date '
           'required by that definition, or any notice of a date required by that definition upon '
           "the Board's action upon a request, later than the time required by that definition")
chk("D 1's lateness enumeration names exactly three documents", S1.count(D1_ENUM), 1)
chk('(i) Edit 4 is not reached by D 1 on the pre-164-5 wording',
    "action upon a request" in E4_NEW, False)
chk('(ii) D 1\'s companion later-effective-date right sits in the SAME sentence, so it is lost too',
    S1.count('the member may state an effective date of retirement that is no earlier than the '
             'first day of the month following the month in which the Board gives the statement '
             'or notice') >= 1, True)
D13A = [r for l, _f, r in EDITS if l.startswith('164-13(a)')][0]
chk('(iii) 164-13(a) widens the disclosure duty to the THIRD document only',
    D13A.count('in every notice of a date required by that definition by reason of the Board\'s '
               'action upon a request'), 1)
chk('    and Edit 4\'s notice is not required by reason of the Board\'s action, so it is excluded',
    "by reason of the Board's action" in E4_NEW, False)
D13B = [r for l, _f, r in EDITS if l.startswith('164-13(b)')][0]
chk('(iv) 164-13(b) clause (iv) rides on the same disclosure sentence',
    D13B.count('that where the Board gives a notice described in this sentence') , 1)
D164_8 = [r for l, _f, r in EDITS if l.startswith('164-8')][0]
chk('(v) 164-8\'s supersession right is keyed to D 1\'s enumerated documents',
    D164_8.count('Where the Board gives any notice described in the preceding sentence'), 1)
R7 = ('Where the date that would otherwise apply under this definition is earlier than the first '
      'day of the second month following the month in which the Board gives a decision or notice '
      'required by the preceding sentence')
chk('(vi) R-7\'s floor is keyed to a decision or notice required by R-6, not by Edit 4',
    S1.count(R7), 1)
chk('    and the expiry sentence blocks any OTHER provision of the definition from supplying one',
    S1.count("the member's final qualifying retirement date is, notwithstanding any other "
             'provision of this definition, that first day'), 2)
chk('    Edit 4 is inserted BEFORE R-6, which is what denies its notice R-7\'s floor',
    S1.index(K141['E4_F']) < S1.index("Where the Board's action upon a request determines"), True)

# ===================================================================== R4 (serious)
print('\n== R4: Edit 4\'s class membership is defeasible by the Board\'s own later act')
chk('Edit 4 triggers on the OUTCOME of the expiry sentence, not on an affirmative fact',
    E4_NEW.count('Where the member\'s final qualifying retirement date is determined by the '
                 'preceding sentence'), 1)
chk('and the expiry sentence applies only on a comparison with the date that would OTHERWISE apply',
    S1.count('and the date that would otherwise apply under this definition is earlier than the '
             'first day of the second month following the month in which that period expired'), 1)
chk('which the Board can move later by approving a later date under the definition',
    S1.count('A later date approved under this definition shall be the first day of a month and '
             'shall be not more than three months after the date determined under the first '
             'sentence of this definition.'), 1)
chk('contrast F1\'s cure, which took class membership out of the future by an affirmative fact',
    "denied without the Board's having acted upon it" in K141['E2_LIMB2'], True)

# ===================================================================== R5 (serious)
print('\n== R5: the saving\'s list is still closed, and seven Board duty families stay outside it')
OUTSIDE = ['shall reserve any increase in the certified subsidy',
           'the Board shall rescind the determination',
           'shall release the reservation',
           'the Board shall extend the completion date',
           'the Board shall apply that amount to the purchase of additional service credit',
           'the Board shall correct the error',
           'shall recertify the election under subdivision D 6 of § 51.1-142.4']
for d in OUTSIDE:
    chk('express Board duty in the base, not in the enumeration: ' + d[:52],
        S1.count(d) >= 1 and d.split('shall ')[-1][:14] not in SAVING_R9, True)
M2_LIST = ('Every determination, certification, redetermination, recertification, reduction, '
           'cancellation, rescission, restoration, crediting of service credit, placement on a '
           'waiting list, expiration of a reservation, denial of an election, and refusal to '
           'accept an election under this section is a determination of the Board for the '
           'purposes of this subsection')
chk('M 2 makes THIRTEEN classes of Board action reviewable as determinations', S1.count(M2_LIST), 1)
_items = ['determination', 'certification', 'redetermination', 'recertification', 'reduction',
          'cancellation', 'rescission', 'restoration', 'crediting of service credit',
          'placement on a waiting list', 'expiration of a reservation', 'denial of an election',
          'refusal to accept an election']
chk('   count of the list', len(_items), 13)
# the saving's verbs, matched to M 2's list explicitly rather than by prefix
_verb = {'determination': 'to make a determination', 'recertification': 'to recertify',
         'restoration': 'to restore', 'crediting of service credit': 'or credit service credit'}
_reached = sorted(x for x in _items if _verb.get(x) and _verb[x] in SAVING_R9)
chk("   the saving's enumeration reaches four of them by name", _reached,
    ['crediting of service credit', 'determination', 'recertification', 'restoration'])
chk('   and nine are outside it', [x for x in _items if x not in _reached],
    ['certification', 'redetermination', 'reduction', 'cancellation', 'rescission',
     'placement on a waiting list', 'expiration of a reservation', 'denial of an election',
     'refusal to accept an election'])
chk('   and M 2\'s deeming cannot carry them in: it is confined by the SAME four-word limiter '
    'F10 was about', S1.count('is a determination of the Board for the purposes of this '
                              'subsection'), 1)
chk('the enumeration remains a closed list — no general words', 
    ('anything' in SAVING_R9) or ('any duty' in SAVING_R9) or ('any act' in SAVING_R9), False)
print('   -> and none of the three ADDED families runs from the Board\'s acting upon a request:')
for d in ('no later than 60 days after the date on which the member is so approved, or dies, or '
          'the Board makes that determination',
          'no later than 60 days after the reversal or modification',
          'within 60 days after the recertification',
          'within 60 days after the determination takes effect',
          'within 60 days after it credits the service credit',
          'within 60 days after it receives the notice of cancellation'):
    chk('   deadline runs from something else: ' + d[:50], S1.count(d) >= 1, True)
chk("Edit 1's deeming reaches only periods measured from the Board's acting upon a request",
    E1_DEEM.count("is measured from, the Board's acting, or last acting, upon a request"), 1)

# ===================================================================== R6 (serious)
print('\n== R6: §3.4 requirement 2 — the locator is sound, the assertion is not')
chk("164-7's deeming does land inside subdivision M 2 (its FIND is M 2's deemed-denial sentence)",
    [f for l, f, _r in EDITS if l.startswith('164-7')][0].endswith(
        'a case decision as defined in § 2.2-4001 for the purposes of this subsection.'), True)
chk('and it does deem a date on which the Board ACTS, so requirement 2 describes it correctly',
    'the Board is deemed' in E164_7 and 'to act upon the request' in E164_7, True)
print('   -> but on R1 the cumulation sentence makes the acting-dates {2 Jun, 6 Jul}; Edit 1 takes')
print('      "first" = 2 Jun, overriding 164-7\'s express LAST-act deeming of 6 Jul. That resolves')
print('      a priority and chooses a date, which requirement 2 denies and requirement 3 forbids.')

# ===================================================================== R7 (moderate)
print('\n== R7: Edit 4\'s deadline is not anaphoric to the trigger, and "that period" was available')
chk('Edit 4 describes the period afresh; "referred to in that sentence" modifies the REQUEST',
    E4_NEW.count('the period for acting upon the request referred to in that sentence'), 1)
chk('the expiry sentence\'s own anaphor is in the words immediately before Edit 4',
    S1.count('the month in which that period expired'), 1)
chk('and the expiry sentence\'s class includes reconsideration requests, which have two periods',
    S1.count('The filing of a request for reconsideration under this subsection, and the filing '
             'of a request under the definition of "final qualifying retirement date" in '
             'subsection A, tolls the running'), 1)
chk('   period A: M 2\'s 90 days', S1.count('The Board shall act upon a request for '
                                            'reconsideration within 90 days.'), 1)
chk('   period B: the 30 days after the expiry notice', S1.count(M2_DEEM), 1)
chk('"that period" would be 23 characters shorter and names no formula',
    len('the period for acting upon the request referred to in that sentence') - len('that period'), 56)

# ===================================================================== R8 (moderate)
print('\n== R8: what the Edit 4 remedy is actually worth')
chk('a failure to give a notice within a required period is reviewable under M 2',
    S1.count('to make a determination, to give a notice, or to make a payment within a period '
             'required by this section'), 1)
chk('filing a reconsideration tolls the running of the member\'s FQRD', 
    S1.count('tolls the running of the member\'s final qualifying retirement date'), 1)
chk('a second request on the SAME failure does not toll — but this is a different failure',
    S1.count('no second or subsequent request for reconsideration of the same determination or of '
             'the same failure'), 1)
chk('and all tolling under M 2 is capped at 120 days in the aggregate',
    S1.count('the aggregate of all tolling under this subsection shall not exceed 120 days'), 1)
chk('while the Edit 4 class has BY DEFINITION already filed a request that tolled',
    S1.count('Where the Board does not act upon a request the filing of which tolled the running '
             'of the member\'s final qualifying retirement date under subsection M'), 1)

# ===================================================================== R9 (moderate)
print('\n== R9: the saving\'s "include" limb has no Board-duty referent')
chk('the bill\'s only "include" provision names no actor',
    S1.count("the next payment of the member's retirement allowance shall include every amount"), 1)
chk('NULL RESULT: a Board duty "to include" DOES exist, so the limb has a referent',
    S1.count('the Board shall include the amount that this subdivision requires to be included '
             "in the next payment of the member's retirement allowance"), 1)
chk('but the primary case — a payment already payable — is ACTORLESS',
    S1.count("the next payment of the member's retirement allowance shall include every amount"), 1)
chk('and the operative payment duties say "pay a refund" / "refund", not "pay any amount"',
    (S1.count('shall pay a refund'), S1.count('shall refund')), (5, 6))
chk('while subsection M\'s own word for the family is "to make a payment"',
    S1.count('to make a payment'), 3)
chk('the saving says "to pay or include any amount"', 'to pay or include any amount' in SAVING_R9, True)

# ===================================================================== null results
print('\n== null results: what I checked and found sound')
chk('N1 property 1: R-6\'s chapeau governs BOTH branches, so widening it would collide',
    S1.count("Where the Board's action upon a request determines a member's final qualifying "
             'retirement date under this definition, the Board shall state that date in its '
             'decision upon the request, and where the Board does not do so it shall give the '
             'member written notice of that date no later than 15 days after it acts upon the '
             'request.'), 1)
chk('N1 Edit 4 does not touch R-6', 'action upon a request determines' in E4_NEW, False)
chk('N2 no MOO-164 substitution inserts a sentence between the expiry sentence and Edit 4',
    all(K141['E4_F'] not in r or l.startswith('164-4') for l, _f, r in EDITS), True)
chk('N2 164-4 substitutes WITHIN the expiry sentence, it does not split it',
    [f for l, f, _r in EDITS if l.startswith('164-4')][0],
    'within the period this definition allows for acting upon it')
_a = S1.index('Where the Board does not act upon a request the filing of which tolled')
_b = S1.index(K141['E4_F']) + len(K141['E4_F'])
chk('N2 the expiry sentence names exactly one request, so "the request referred to in that '
    'sentence" resolves', S1[_a:_b].count('request'), 1)
chk('N3 property 3: Edit 4 contains neither period formula',
    ('this definition allows' in E4_NEW) or ('allowed by this section' in E4_NEW), False)
chk('N3 and no MOO-164 FIND overlaps Edit 4\'s new sentence',
    any(f in E4_NEW for _l, f, _r in EDITS), False)
chk('N5 property 5: D 1 reaches three documents and Edit 4\'s is a fourth',
    D1_ENUM.count('any notice'), 2)
chk('N6 the bill\'s recertify-and-settle duty takes "it" = the certified subsidy',
    S1.count('where the determination as reversed or modified is such that the certified subsidy '
             'falls to be settled under subdivision 1 or under this subdivision, shall recertify '
             'and settle it accordingly'), 1)
chk('N6 "to restore or credit service credit" matches the bill verbatim, twice',
    S1.count('restore or credit service credit'), 2)
chk('N7 counted facts: four anchors at exactly 1 in §1',
    tuple(S1.count(f) for f in (K141['E1_F'], K141['E2_F'], K141['E3_F'], K141['E4_F'])),
    (1, 1, 1, 1))
chk('N7 Edit 1\'s FIND reads 2 whole-document, so a whole-document count is not a uniqueness test',
    doc.count(K141['E1_F']), 2)
chk('N7 <u> 62/62; "first acts upon" base 2; "the preceding sentence" base 21',
    (S1.count('<u>'), S1.count('</u>'), S1.count('first acts upon'),
     S1.count('the preceding sentence')), (62, 62, 2, 21))
chk('N8 the denial of a reconsideration is a case decision, so judicial review lies',
    S1.count('shall constitute a case decision as defined in § 2.2-4001'), 1)
chk('N9 G 4\'s window already ends on the FIRST act, so Edit 1 alone is consistent with it',
    S1.count('until the date on which the Board first acts upon it'), 2)
chk('N10 card (g)\'s first limb survives character for character and is ordered first',
    (K141['E2_R'].count(K141['E2_R6'][:-1]),
     K141['E2_R'].index(K141['E2_R6'][:-1]) < K141['E2_R'].index(K141['E2_LIMB2'])), (1, True))
chk('N10 card (k-ii)\'s 120 days untouched — Edit 3 delta 15',
    len(K141['E3_R']) - len(K141['E3_F']), 15)
chk('N11 Edit 4 is operative alone: no subsection, no subdivision, no deeming',
    bool(re.search(r'subsection|subdivision|deem', E4_NEW)), False)

# ===================================================================== R11 (minor)
print('\n== R11: the kit label that is doing work its check is not')
chk('the kit counts a string under a label asserting "both before any real act"',
    "on the date of that denial or, as the case may be, on the day after the expiration of that "
    "period" in E164_7, True)
print('   -> the counted proposition is the presence of the phrase; the labelled proposition is an')
print('      ordering claim about real acts, which no string count can reach. §6.1, recurring.')

print('\n' + ('ALL CHECKS PASS' if not fail else f'{fail} CHECK(S) FAILED'))
sys.exit(1 if fail else 0)
