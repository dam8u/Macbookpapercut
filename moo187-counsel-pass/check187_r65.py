# -*- coding: utf-8 -*-
"""MOO-187 re-check at **store revision 65** — the twelfth base move, and the first since
store revision 62 that lands inside a provision this cut amends.

Store revision 65 (MOO-191) makes **one insertion in subdivision D 1**: 137 characters added to the
Board's certification-contents sentence, a designation-of-beneficiary review advisory. D 1 is the
site of Edit 164-5, of candidate 164-8, and of the ordinal cross-reference *"the second sentence of
subdivision M 2"* that §13.9 warns about — so the move is material and is verified rather than
assumed.

This script:

  0. Isolates the change. Asserts enacted §1 at store revision 65 differs from store revision 64 in
     **exactly one line**, that the line is D 1, and that the whole of the difference is the single
     MOO-191 insertion (so no other word of §1 moved).
  1. Re-runs the cut's own invariants on the new base: twelve anchors each exactly once across three
     bases (bare, + MOO-141 patch rev 5, + rev 6), the +490 delta, the 21-occurrence classification,
     the four U+2019.
  2. Re-tests the textual predicate of every live MOO-187 finding that could be disturbed by an
     insertion in D 1 — F1, F3, F6, F12, F19, F20, F22, F23, F24, F25, F26 — plus the null results
     that are about D 1 (§13.4's "first required", §13.5's vehicle gap, §13.9's ordinals).
  3. Checks finding F21 against the new base: whether the committed verify_r6.py's whole-document
     counts now fail by even more than they did at store revision 63.

Requires head65.md (bill-text-s8 as fetched live) and head64.md (from the addendum run), both as
enacted-§1-bearing full documents. Reads only; writes nothing and modifies no team file.

Internal risk analysis. Not legal advice. Pre-decisional and internal.
"""
import re
import sys

fail = 0


def check(label, got, want):
    global fail
    ok = got == want
    print(f'   [{"ok " if ok else "FAIL"}] {label}: {got!r}' + ('' if ok else f'  expected {want!r}'))
    if not ok:
        fail += 1
    return ok


def sec1(doc):
    i = doc.index('\n## 1.')
    m = re.search(r'\n## (?!1\.)', doc[i + 5:])
    return doc[i:i + 5 + m.start()]


def subdivisions(body):
    """Map 'D 1', 'G 4', 'M 2', ... -> that subdivision's text.

    Enacted §1 puts each subsection or subdivision on its own line: the first subdivision of a
    lettered subsection carries '**X. n.**', later ones carry a bare '<u>n.' continuation.
    """
    out, letter = {}, None
    for line in body.split('\n'):
        m = re.match(r'\s*(?:<u>)?\*\*([A-Z])\.(?:\s*(\d+)\.)?\*\*', line)
        if m:
            letter = m.group(1)
            out[f'{letter} {m.group(2)}' if m.group(2) else letter] = line
            continue
        m = re.match(r'\s*(?:<u>)?(\d+)\.\s', line)
        if m and letter:
            out[f'{letter} {m.group(1)}'] = line
    return out


D64 = open('head64.md', encoding='utf-8').read()
D65 = open('head65.md', encoding='utf-8').read()
B64 = sec1(D64)
BILL = sec1(D65)

MOO191 = ("that the member is advised to review the member's designation of beneficiary under "
          "subsection A of § 51.1-162 before completing payment; ")

# ===================================================================== 0. isolate the change
print('== 0. what store revision 65 did to enacted §1')
print(f'   whole document: rev 64 = {len(D64)}, rev 65 = {len(D65)} ({len(D65)-len(D64):+d})')
print(f'   enacted §1:     rev 64 = {len(B64)}, rev 65 = {len(BILL)} ({len(BILL)-len(B64):+d})')
check('§1 delta is MOO-191 insertion length', len(BILL) - len(B64), len(MOO191))

L64, L65 = B64.split('\n'), BILL.split('\n')
check('§1 line count unchanged', len(L65), len(L64))
diff = [i for i, (x, y) in enumerate(zip(L64, L65)) if x != y]
check('exactly one §1 line changed', len(diff), 1)
if len(diff) == 1:
    i = diff[0]
    check('the changed line is subdivision D 1', L65[i].startswith('<u>**D. 1.**'), True)
    check('the changed line, minus the insertion, is byte-identical to rev 64',
          L65[i].replace(MOO191, '', 1), L64[i])
check('the insertion occurs exactly once in §1', BILL.count(MOO191), 1)
check('the insertion is not in rev 64', B64.count(MOO191), 0)

# ===================================================================== 1. the cut's invariants
E1_F = ("every period within which a person may or must act that runs from the giving of that "
        "statement or notice is extended by three days.</u>")
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


BASES = [("store rev 65", BILL),
         ("store rev 65 + MOO-141 patch rev 5", build(E3_R5)),
         ("store rev 65 + MOO-141 patch rev 6", build(E3_R6))]

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
 ("164-5 F-9  (in D 1 — the moved subdivision)",
  "any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition by reason of the Board's action upon a request"),
 ("164-6 conforming",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
  "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
]

DENIAL = ("the request is denied on the first day after the expiration of those 30 days, and that denial "
          "constitutes the final determination of the Board upon the reconsideration and a case decision "
          "as defined in § 2.2-4001 for the purposes of this subsection.")

HELD = [
 ("c-1", "For the purposes of this subdivision an application for a disability retirement allowance is pending"),
 ("c-2", "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending."),
 ("card (i) insertion point", "The Board shall act upon a request for reconsideration within 90 days."),
 ("164-7 anchor (item 130)", DENIAL),
 ("164-8 anchor (in D 1 — the moved subdivision)",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J."),
]

for name, base in BASES:
    out, delta = base, 0
    print(f"\n== 1. {name}  ({len(base)} chars)")
    for tag, f, r in EDITS:
        c = out.count(f)
        print(f"   {tag:44s} FIND count {c}  delta {len(r)-len(f):+d}")
        if c != 1:
            fail += 1
        else:
            out = out.replace(f, r, 1)
            delta += len(r) - len(f)
    for tag, f in HELD:
        c = base.count(f)
        print(f"   held: {tag:46s} FIND count {c}   (not applied)")
        if c != 1:
            fail += 1
    n = out.count('’')
    print(f"   amendment delta {delta:+d} | U+2019 normalised {n} | final length {len(out)}")
    if delta != 490:
        fail += 1
    if n != 4:
        fail += 1

print('\n== 1b. the 21-occurrence classification on the new base')
counts = {p: BILL.count(p) for p in ('acts upon', 'act upon', 'acting upon', 'action upon')}
for p, c in counts.items():
    print(f'   {p!r:14s} {c}')
check('total act/acts/acting/action upon in §1', sum(counts.values()), 21)
check("'acts upon' (§13.3)", counts['acts upon'], 8)
check("'act upon' (§13.3)", counts['act upon'], 9)
check("'acting upon' (§13.3)", counts['acting upon'], 2)
check("'action upon' (§13.3)", counts['action upon'], 2)
# MOO-191 inserted no occurrence of the family
check('MOO-191 insertion contains no act/acts/acting/action upon',
      sum(MOO191.count(p) for p in counts), 0)

print('\n== 1c. the four U+2019, and where they are')
SUB = subdivisions(BILL)
check('U+2019 in §1', BILL.count('’'), 4)
check('U+2019 inside subdivision G 4', SUB['G 4'].count('’'), 4)
check('U+2019 anywhere else in §1', BILL.count('’') - SUB['G 4'].count('’'), 0)
check('MOO-191 insertion introduced no U+2019', MOO191.count('’'), 0)

# ===================================================================== 2. the live findings
print('\n== 2. textual predicate of each live MOO-187 finding, re-tested on store revision 65')

print(' -- F1 (serious, unanswered): Edit 164-1\'s 48-day cap is itself act-keyed')
after = BILL
for tag, f, r in EDITS:
    after = after.replace(f, r, 1)
after141 = after.replace(E1_F, E1_R, 1).replace(E2_F, E2_R, 1).replace(E3_F, E3_R6, 1)
check("'acts upon' after both patches (§7.2 predicts 7 — finding F2)",
      after141.count('acts upon'), 9)
read1 = EDITS[0][2]
check("occurrences of 'acts upon' inside Edit 164-1's READ", read1.count('acts upon'), 2)
check("Edit 164-1's READ still carries the act-keyed cap",
      'in no case later than 48 days after the Board acts upon the request' in read1, True)

print(' -- F3 (serious): Edit 164-2 tests against the 30-day limb, which never conflicts')
check("G 2 contains the 30-day notice floor limb",
      BILL.count('no less than 30 days before the determination takes effect'), 1)
check("Edit 164-2's new limb names that sentence, not the subsection M period",
      'requires notice to be given no less than 30 days before the determination takes effect' in EDITS[1][2], True)

print(' -- F6 (serious, escalated): the 90-day duty states no commencement')
check("'The Board shall act upon a request for reconsideration within 90 days.' occurs",
      BILL.count('The Board shall act upon a request for reconsideration within 90 days.'), 1)
shall = re.findall(r'[^.]*shall act upon[^.]*\.', BILL)
print(f'   the section\'s "shall act upon" duties: {len(shall)}')
nocommence = [s for s in shall if 'within 90 days.' in s]
check('exactly one of them states no commencement', len(nocommence), 1)

print(' -- F12 (moderate, realised): two formulas for one concept inside M 2')
# NOTE: this corrects the addendum's own F12 row, which said "three instances of 'the period
# allowed by this section for acting upon the request'". Three is the §1-wide count of the
# FORMULA; only two of the three read "the request" — the third is Edit 164-4's "...upon it", and
# it is in the subsection A definition, not in M 2. The defect is unaffected: inside M 2 it is one
# of each, which is what "two formulas for one concept in the same subsection" requires.
check("'the 90 days allowed by this subsection' in §1 as it stands",
      BILL.count('the 90 days allowed by this subsection'), 2)
m2_after = subdivisions(after)['M 2']
check("within M 2 after the cut: 'the 90 days allowed by this subsection'",
      m2_after.count('the 90 days allowed by this subsection'), 1)
check("within M 2 after the cut: 'the period allowed by this section for acting upon the request'",
      m2_after.count('the period allowed by this section for acting upon the request'), 1)
check("§1-wide, the formula 'the period allowed by this section for acting upon ...' after the cut",
      len(re.findall(r'the period allowed by this section for acting upon', after)), 3)
check("  of which read 'the request'",
      after.count('the period allowed by this section for acting upon the request'), 2)
check("  and 'it' (Edit 164-4's site, in the subsection A definition)",
      after.count('the period allowed by this section for acting upon it'), 1)

print(' -- F19 (serious): 164-7 carries only limb (A) of Edit 1\'s two triggers')
check("Edit 1 limb (B) present in Edit 1's READ",
      'where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request' in E1_R, True)
check("the reset sentence (occurrence #2) is still in §1 and keyed to limb (B)",
      BILL.count('the first day of the second month following the month in which the Board last acts upon a request the filing of which tolled that period'), 1)

print(' -- F22 (serious): the definition-request class has no denial mechanism')
m2 = SUB['M 2']
defreq = re.findall(r'a request under the definition of [^,;]*', m2)
print(f'   M 2 references to a request under the definition: {len(defreq)}')
for s in defreq:
    print(f'      {s[:120]}')
check('M 2 still tolls on a definition request as well as a reconsideration request',
      len(defreq) >= 1, True)
check("option (d)'s denial sentence is in M 2 and confined to 'this subsection'",
      m2.count(DENIAL), 1)
check("option (d) speaks of 'a request for reconsideration' only",
      'reconsideration' in m2[:m2.index(DENIAL)], True)

print(' -- F24 (minor): the "period allowed" family')
pa = re.findall(r'the (?:period|time) allowed[^,.;]*', BILL)
print(f'   "the period/time allowed..." phrases in §1: {len(pa)}')
for p in sorted(set(pa)):
    print(f'      {BILL.count(p)}x  {p[:110]}')

print(' -- F25 / §13.9 (minor): D 1\'s ordinal reference to M 2')
d1 = SUB['D 1']
check("'the second sentence of subdivision M 2' occurs in §1",
      BILL.count('the second sentence of subdivision M 2'), 1)
check('it is inside subdivision D 1 (the subdivision MOO-191 moved)',
      d1.count('the second sentence of subdivision M 2'), 1)
# MOO-191's insertion is in D 1 too — does it sit before or after the ordinal reference?
i_ord = d1.index('the second sentence of subdivision M 2')
i_ins = d1.index(MOO191)
print(f'   within D 1: MOO-191 insertion at {i_ins}, ordinal reference at {i_ord} — '
      f'insertion is {"BEFORE" if i_ins < i_ord else "AFTER"} the ordinal reference')
check('MOO-191 inserted nothing into M 2, so the ordinal reference\'s referent is unmoved',
      SUB['M 2'].count(MOO191), 0)
check("M 2's second sentence is unchanged from store revision 64",
      SUB['M 2'], subdivisions(B64)['M 2'])

print(' -- §13.4 null result: D 1\'s "first required"')
check("'first required' occurrences in §1", BILL.count('first required'), 1)
check("'first required' is in D 1's filing-duty sentence", d1.count('first required'), 1)

print(' -- §13.5 null result: no vehicle in D 1 to amend/withdraw a stated effective date')
print(f'   subdivision D 1 is now {len(d1)} characters (was 7214 at store revision 64)')
for w in ('amend', 'withdraw', 'replace', 'replacing', 'substitute', 'revoke', 'rescind'):
    c = d1.count(w)
    print(f'      {w:11s} {c}')
    if c:
        fail += 1

print(' -- F26 (moderate): 164-8 keys to arrival of the notice, not to its lateness')
check("D 1's lateness-extension sentence still carries 'by reason of'/'upon' the Board's action",
      BILL.count("any notice of a date required by that definition upon the Board's action upon a request"), 1)

# ------------------------------------------- F27: what MOO-191's advisory does to the M 2 machinery
print('\n -- F27 (new, minor): MOO-191\'s advisory is a "matter this subdivision requires to be '
      'stated", so omitting it is a reviewable failure that tolls under M 2')
check('the advisory is in the "The Board\'s certification shall also state that ..." series',
      d1.index("The Board's certification shall also state that") < d1.index(MOO191), True)
FAILSENT = ("A failure to state in the Board's certification every matter this subdivision requires "
            "to be stated in it is a failure of the Board to state in a certification a matter this "
            "section requires to be stated in it for the purposes of subsection M")
check("D 1's failure-to-state sentence is present and unchanged", d1.count(FAILSENT), 1)
check('it sweeps in EVERY matter the subdivision requires, with no carve-out for advisories',
      'every matter this subdivision requires' in FAILSENT and 'except' not in FAILSENT, True)
check('and the advisory precedes that sentence, so it is one of those matters',
      d1.index(MOO191) < d1.index(FAILSENT), True)
# subsection M review on such a failure is what M 2's tolling sentence attaches to
check("M 2 gives review for 'a failure of the Board to state in a certification or notice a matter'",
      SUB['M 2'].count('failure of the Board to state in a certification or notice a matter this '
                       'section requires to be stated in it'), 1)
# MOO-191 did NOT add the advisory to D 1's clause (i)/(ii)/(iii) "shall state" list
tail = d1[d1.index('The Board shall state, in the written statement required by that definition'):]
check('MOO-191 added nothing to D 1\'s clause (i)/(ii)/(iii) list', tail.count(MOO191), 0)

print('    F27 litigation-surface limb — who could plead the omission, and where')
check('D 1 gives review to "a person adversely affected by it", not only the member',
      d1.count('a person adversely affected by it may seek review under subsection M'), 1)
check('and expressly contemplates that person not being the member',
      d1.count('where that person is not the member'), 1)
check('M 2 lists a death-benefit claimant among those who may seek reconsideration',
      SUB['M 2'].count('person who has claimed any benefit payable on the death of a member'), 2)
check('and routes the resulting case decision to Article 5 of the APA',
      SUB['M 2'].count('Article 5 (§ 2.2-4025 et seq.) of the Administrative Process Act'), 1)
# the advisory adds exhortation, not information: D 1 already states the subsection A machinery
check('D 1 already described the § 51.1-162 subsection A designation machinery before MOO-191',
      subdivisions(B64)['D 1'].count('subsection A of that section provides for the payment of the '
                                     "member's accumulated contributions to the person the member "
                                     'has designated'), 1)
# and D 1 already knows how to switch a failure off, so the fix has a model in the same sentence
check('D 1 already carves one consequence out of one failure, in the same sentence',
      d1.count('the second sentence of subdivision M 2 does not apply to such a failure'), 1)

# ===================================================================== 3. F21 on the new base
print('\n== 3. F21 — whole-document counts on store revision 65')
WHOLE = [('164-6 FIND', EDITS[5][1]),
         ('164-7 FIND (item 130 denial)', DENIAL),
         ('MOO-141 Edit 3 FIND', E3_F),
         ("M 2's 90-day sentence", 'The Board shall act upon a request for reconsideration within 90 days.')]
worse = 0
for tag, s in WHOLE:
    w, o = D65.count(s), BILL.count(s)
    w64 = D64.count(s)
    print(f'   {tag:32s} whole-document {w} (was {w64} at rev 64) | enacted §1 {o}')
    if w != o:
        worse += 1
print(f'   anchors whose whole-document count differs from their §1 count: {worse}')
print('   F21 stands: a whole-document find-and-replace on any of these edits the §0 record too.')

print(f'\n{"ALL CHECKS PASS" if fail == 0 else str(fail) + " FAILURES"}')
sys.exit(1 if fail else 0)
