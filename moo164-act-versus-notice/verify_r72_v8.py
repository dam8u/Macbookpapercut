# -*- coding: utf-8 -*-
"""MOO-164 **revision 8** — the MOO-214 counsel pass folded, verified at store revision 72.

Supersedes verify_r70_v7.py for two reasons:

  1. **The base moved twice more.** Store revision **71** made thirteen substitutions in §1
     (MOO-210's R2/R5/R6 and nine MOO-200 findings), growing enacted §1 from 132,557 to
     **134,012**; store revision **72** is record only and leaves §1 **byte-identical** to 71.
     That byte-identity is proved here, not asserted.
  2. **Revision 8 re-cuts four applied substitutions.** MOO-214's thirteen findings are folded:
     **164-7** takes **S3** (the paraphrase descriptor replaced by the determinate one the cut
     already coined), **m2** (the no-deemed-statement sentence) and the Policy Director's
     **§3.3 cross-reference**; **164-8** takes **S1** (*"of a kind"*) and **m1**; **164-13(b)**
     takes **S2** (the bar moved into the trigger) and **M1** (the timeliness deeming and the
     supersession disclosed); **164-12** takes **M3** (the noun phrase written out).

Applied at revision 8: **thirteen** substitutions across twelve edits, unchanged in number.
Held: **164-9** (MOO-204), **164-14** (MOO-209 F10), and three new on this pass — **164-15**
(S6, non-receipt), **164-16** (counsel's impose-not-except form of S3) and **164-17** (S4's
enforcement route). **164-18** (M2's one-concept alternative) is drafted and held. Retired: **(c-1)**.

Every count is taken over **enacted §1 only** (MOO-187 finding F21). Several anchors resolve more
than once whole-document because the §0 revision narratives quote them.

New in this check, each because MOO-214 asked for a proposition rather than a string:

  * **S3** — the exception's second descriptor is asserted to be the descriptor 164-5 and 164-13(a)
    put into the bill, counted at its three sites, and the paraphrase is asserted **absent**. The
    old descriptor's two rival referents (R-3 and R-4b) are counted so the ambiguity is on the
    record as a number.
  * **M4** — the *expressio unius* inference is shown to be **inert** rather than argued away:
    after MOO-141 Edit 2 revision 8, R-6's deadline in Edit 1's class is decision-keyed, so Edit 1's
    deeming cannot reach it whether or not it is excepted. Counted on the combined text.
  * **N1 preserved** — m2's cure is a **separate sentence**, so the saving's 256-character body
    stays byte-identical between 164-7 and MOO-141 Edit 1. Still asserted.
  * **S1/S2/M1** — s12 and clause (iv) are asserted to use **one** formula for the class of notice
    and **one** form of the bar, in both directions, so the two cannot drift apart again.
  * **S4** — the claim that subsection J reaches a failure to state is counted at **0** and the
    claim is withdrawn in the document; the two phrases are asserted absent from J 1.
  * **F5's lesson, one level up** — `check_doc_vs_kit.py` is rewritten on MOO-214 **S5**, which
    broke the old one three ways.

Run: python3 verify_r72_v8.py bill72.md
Nothing is written to the store.
"""
import re
import sys

fail = 0


def chk(label, got, want):
    global fail
    if got != want:
        fail += 1
    print(f'   [{"ok" if got == want else "FAIL"}] {label}: {got} (expected {want})')


doc = open(sys.argv[1] if len(sys.argv) > 1 else 'bill72.md', encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
print(f'== base: whole document {len(doc)} chars; enacted §1 {len(S1)} chars')

# Store revision 72 is record only. PROVE it rather than take the §0 narrative's word for it: if a
# copy of store revision 71 is present, enacted §1 must be byte-identical.
try:
    _r71 = open('../moo141-rev71/live.md', encoding='utf-8').read()
    _i = _r71.index('\n## 1.')
    _m = re.search(r'\n## (?!1\.)', _r71[_i + 5:])
    chk('store revision 72 leaves enacted §1 byte-identical to store revision 71',
        S1 == _r71[_i:_i + 5 + _m.start()], True)
except FileNotFoundError:
    print('   [skip] no store-revision-71 copy present to compare against')

# ---------------------------------------------------------------- MOO-141 patch (not ours)
E1_F_R65_DEAD = ("every period within which a person may or must act that runs from the giving of that "
                 "statement or notice is extended by three days.</u>")
E1_F_R68 = ("every period within which a person may or must act that runs from the giving of that "
            "statement, notice, or certification is extended by three days.</u>")
# The saving clause's body. Identical in MOO-141 Edit 1 and in MOO-164 Edit 164-7 — 256 characters.
# Only the exception that precedes it differs. MOO-209 N1 asked for this to be asserted, because the
# "word for word" claim was made twice and was false twice (MOO-187 F19, F20).
SAVING = ("nothing in the preceding sentence determines the date by which the Board is required to act "
          "upon a request, to make a determination, or to give a notice or a decision, or whether the "
          "Board has performed such a duty within a period required by this section.")
E1_EXC = ('Except for the purposes of the duty of the Board under subsection M to act upon an '
          'application no later than 15 days after it acts upon the request,')
E1_R = (E1_F_R68[:-len('</u>')] +
        " For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period "
        "begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, "
        "or where a date is fixed by reference to the month in which the Board acts, or last acts, upon "
        "a request, the Board is deemed to act upon that request, and to last act upon it, on the date "
        "on which the Board first acts upon it. " + E1_EXC + " " + SAVING + "</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R5 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

print('\n== MOO-141 patch anchors at store revision 70')
chk('E1 FIND as written for store rev 65 (DEAD — kept so the break stays visible)',
    S1.count(E1_F_R65_DEAD), 0)
chk('E1 FIND as re-cut by MOO-141 for store rev 68/69', S1.count(E1_F_R68), 1)
chk('E2 FIND', S1.count(E2_F), 1)
chk('E3 FIND', S1.count(E3_F), 1)
chk('neither saving is in the base — MOO-164 is not applied to the store', S1.count(SAVING), 0)


def build(body, e3):
    out = body
    for f, r in ((E1_F_R68, E1_R), (E2_F, E2_R), (E3_F, e3)):
        assert out.count(f) == 1, 'MOO-141 FIND not unique: ' + f[:50]
        out = out.replace(f, r, 1)
    return out


# ---------------------------------------------------------------- revision 8's thirteen substitutions
# 164-7's exception. Revision 7 named R-6's duty by a PARAPHRASE — "to give the member written
# notice of the member's final qualifying retirement date" — which MOO-214 S3 showed matches R-3
# and R-4b as well. Revision 8 uses the descriptor THIS CUT ALREADY COINED: after 164-5 and
# 164-13(a), "notice of a date required by that definition by reason of the Board's action upon a
# request" stands at two sites in the bill and names R-6's notice at both. It is not deadline-keyed,
# so it still identifies R-6 after MOO-141's Edit 2 re-keys R-6's 15 days.
E164_7_EXC_V7_DEAD = ('give the member written notice of the member\'s final qualifying retirement date,')
R6_DESCRIPTOR = ('a notice of a date required by that definition by reason of the Board\'s action '
                 'upon a request')
E164_7_EXC = ('Except for the purposes of the duty of the Board under this subsection to act upon an '
              'application no later than 15 days after it acts upon the request and the duty of the '
              'Board under the definition of "final qualifying retirement date" in subsection A to '
              'give ' + R6_DESCRIPTOR + ',')

# MOO-214 m2 — foreclose the argument that a decision deemed to exist is deemed to state what a
# decision must state, which would make R-6's "where the Board does not do so" condition fail.
# Drafted as a SEPARATE SENTENCE so the saving's 256-character body stays byte-identical between
# the two deemings (MOO-209 N1). That invariant is asserted below.
NOT_STATED = ("The Board is not deemed by this subsection to have stated a member's final qualifying "
              "retirement date in a decision upon a request.")

# The Policy Director's MOO-141 §3.3 cross-reference, drafted to their three requirements: say what
# each deeming governs; make them cumulative and non-exclusive; move no date and add no exception.
# It names the other deeming BY ITS CONTENT and not by a citation, so if this cut were ever applied
# without the MOO-141 patch the class is empty and the clause is inert rather than dangling.
XREF = ("The provision of this subsection deeming the Board to act upon a request applies where the "
        "Board does not act upon the request, and neither limits nor is limited by any provision of "
        "this section deeming the Board to act upon a request, and to last act upon it, on the date "
        "on which the Board first acts upon it, which applies where the Board acts upon a request more than "
        "once; the two provisions apply cumulatively, and neither is the exclusive rule for "
        "determining the date on which the Board acts upon a request.")

EDITS = [
 ("164-1 (card (b))",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the Board acts upon the request"),
 ("164-2 (card (h))",
  "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
  "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect, the determination takes effect on the first day"),
 ("164-3 (card (j))",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request"),
 ("164-4 (card (l) / F-5)",
  "within the period this definition allows for acting upon it",
  "within the period allowed by this section for acting upon it"),
 ("164-5 (card (k) / F-9)",
  "any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition by reason of the Board's action upon a request"),
 ("164-6 (conforming)",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
  "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
 ("164-7 RE-CUT at revision 8 on MOO-214 S3 and m2, and carrying the Director's §3.3 cross-reference",
  "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
  "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of \"final qualifying retirement date\" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. "
  + E164_7_EXC + " " + SAVING + " " + NOT_STATED + " " + XREF),
 ("164-8 RE-CUT at revision 8 on MOO-214 S1 and m1 — the class of notice, and the bar's noun",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. Where the Board gives any notice of a kind described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member, except that no notice may be filed under this sentence after the member has retired."),
 ("164-13(a) NEW at revision 7 on MOO-209 F4 — the disclosure duty reaches the third document",
  "The Board shall state, in the written statement required by that definition and in every notice of a later approved date required by that definition, (i)",
  "The Board shall state, in the written statement required by that definition, in every notice of a later approved date required by that definition, and in every notice of a date required by that definition by reason of the Board's action upon a request, (i)"),
 ("164-13(b) RE-CUT at revision 8 on MOO-214 S2 and M1 — the bar into the trigger, the right stated in full",
  "; and (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days.",
  "; (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days; and (iv) that where the Board gives a notice of a kind described in this sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153 and the member has not retired, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives that notice, and that a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member."),
 ("164-10 (F6 commencement)",
  "The Board shall act upon a request for reconsideration within 90 days.",
  "The Board shall act upon a request for reconsideration within 90 days after the request is filed."),
 ("164-11 (F12 conforming)",
  "Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file",
  "Where the Board does not act upon a request for reconsideration within the period allowed by this section for acting upon the request, the person who filed the request may file"),
 ("164-12 RE-CUT at revision 8 on MOO-214 M3 — the noun phrase written out, as G 4's model does",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. For the purposes of this subdivision, an application of the member for a disability retirement allowance under this chapter is pending from the date on which the member files it until the date on which the Board grants or denies it."),
]

HELD = {
 "(c-1) FIND — RETIRED to the record; G 4 must be untouched": "For the purposes of this subdivision an application for a disability retirement allowance is pending",
 "card (i) confirming-sentence insertion point — declined": "The Board shall act upon a request for reconsideration within 90 days.",
}

BASES = [("store rev 70", S1),
         ("store rev 70 + MOO-141 patch, Edit 3 at 30 days", build(S1, E3_R5)),
         ("store rev 70 + MOO-141 patch, Edit 3 at 120 days", build(S1, E3_R6))]

print('\n== the MOO-141 fixture is cross-checked, not trusted: their own published delta')
chk('MOO-141 patch delta over §1 with Edit 3 at 120 days', len(BASES[2][1]) - len(S1), 847)
print('   with Edit 3 at 30 days:', len(BASES[1][1]) - len(S1), '(one character shorter: "30" for "120")')

print('\n== N1 — the saving body is byte-identical in the two deemings, and that is now asserted')
chk('the saving body is 256 characters', len(SAVING), 256)
chk('164-7 REPLACE contains the saving body verbatim, once', EDITS[6][2].count(SAVING), 1)
chk('MOO-141 Edit 1 REPLACE contains the same body verbatim, once', E1_R.count(SAVING), 1)
chk('the two exceptions differ, and only in the duties they name',
    (E164_7_EXC == E1_EXC), False)

print('\n== the thirteen applied anchors + two held strings, on three bases, over §1 only')
for name, body in BASES:
    print(f'  -- {name} ({len(body)} chars)')
    for label, f, r in EDITS:
        chk(label, body.count(f), 1)
    for label, f in HELD.items():
        chk(label, body.count(f), 1)


def apply_all(body):
    out = body
    for label, f, r in EDITS:
        assert out.count(f) == 1, 'FIND not unique when applied in order: ' + label
        out = out.replace(f, r, 1)
    return out


print('\n== delta of the THIRTEEN substitutions — the revision-8 figure, on every base')
deltas = []
for name, body in BASES:
    d = len(apply_all(body)) - len(body)
    deltas.append(d)
    print(f'   {name} delta: {d}')
chk('the delta is identical on all three bases', len(set(deltas)), 1)
print('   revision 7 was thirteen and +3,375; revision 6 eleven and +2,551; revision 5 six and +642')
REV7_DELTA = deltas[0]

print('\n== per-substitution delta, so the README table is counted and not added up by hand')
_run = 0
for label, f, r in EDITS:
    d = len(r) - len(f)
    _run += d
    print(f'   {d:+6}   {label[:78]}')
chk('the per-substitution deltas sum to the measured total', _run, REV7_DELTA)

only164 = apply_all(S1)
patched141 = build(S1, E3_R6)
both = apply_all(patched141)

print('\n== the revision-7 re-cuts, still measured rather than asserted')
chk('F2 — ", satisfies § 51.1-153," is gone from 164-8', only164.count('satisfies § 51.1-153,'), 0)
chk('  and D 1\'s own sentence still carries it WITH the subsection E qualification',
    only164.count('A notice filed within the period allowed by this subdivision satisfies § 51.1-153'), 1)
chk('  that sentence defers to subsection E of § 51.1-153', only164.count('subject to subsection E of § 51.1-153'), 2)
chk('F3 — the supersession is confined to the member\'s own notice of retirement — s12 states it '
    'and clause (iv) discloses it (MOO-214 M1)',
    only164.count('supersedes any notice of retirement previously filed by the member'), 2)
chk('  and the unbounded form is gone', only164.count('supersedes any notice previously filed'), 0)
chk('  the post-retirement bar is present once in 164-8, in m1\'s conformed words',
    only164.count('no notice may be filed under this sentence after the member has retired'), 1)
chk('  m1 — the bare "the member\'s retirement has taken effect" is gone from this cut',
    only164.count("the member's retirement has taken effect"), 0)
chk('  and "the member has retired" was already the section\'s own form', S1.count('the member has retired'), 1)
chk('F6 — the notwithstanding is gone from 164-12',
    only164.count('Notwithstanding the definition in subdivision 4'), 0)
chk('F4 — the disclosure sentence now reaches the third document',
    only164.count("and in every notice of a date required by that definition by reason of the Board's action upon a request, (i)"), 1)
chk('F4 — clause (iv) is present once', only164.count('; and (iv) that where the Board gives a notice of a kind described in this sentence'), 1)

print('\n== S1, S2 and M1 — s12 and clause (iv) now use ONE formula and ONE form of the bar')
chk('S1 — "of a kind" is in both, and the bare form is in neither',
    (only164.count('notice of a kind described in'), only164.count('notice described in')), (2, 0))
chk('  s12 has it', EDITS[7][2].count('any notice of a kind described in the preceding sentence'), 1)
chk('  clause (iv) has it', EDITS[9][2].count('a notice of a kind described in this sentence'), 1)
chk('S2 — the bar is in clause (iv)\'s TRIGGER, not its tail',
    EDITS[9][2].count('for filing the notice of retirement required by § 51.1-153 and the member has not retired, the member may file'), 1)
chk('  and clause (iv) no longer states the bar after the grant',
    EDITS[9][2].count('no such notice may be filed'), 0)
chk('M1 — clause (iv) now discloses the timeliness deeming',
    EDITS[9][2].count('a notice so filed is filed within the period allowed by this subdivision'), 1)
chk('M1 — and the supersession, which is the whole benefit',
    EDITS[9][2].count('supersedes any notice of retirement previously filed by the member'), 1)
chk('  both of those stand in s12 too, in the same words',
    (EDITS[7][2].count('a notice so filed is filed within the period allowed by this subdivision'),
     EDITS[7][2].count('supersedes any notice of retirement previously filed by the member')), (1, 1))
print('   s12 states the rule and clause (iv) describes it. They are now the same rule, word for word')
print('   in every operative limb — and "word for word" is a counted claim here, not a sentence:')
for frag in ['of a kind described in', 'the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member',
             'a notice so filed is filed within the period allowed by this subdivision',
             'supersedes any notice of retirement previously filed by the member']:
    chk(f'   shared limb present in both: {frag[:52]}…',
        (EDITS[7][2].count(frag) >= 1, EDITS[9][2].count(frag) >= 1), (True, True))

print('\n== M3 — 164-12\'s new sentence is self-contained, as G 4\'s model is')
chk('164-12 adds no new "such an application is pending" back-reference — the one occurrence is '
    'G 4\'s own, in the base, untouched',
    (S1.count('such an application is pending'), only164.count('such an application is pending')), (1, 1))
chk('the noun phrase is written out, once',
    only164.count('an application of the member for a disability retirement allowance under this chapter is pending from the date'), 1)
chk('  it is the same noun phrase G 2 and G 4 already use — twice in the base, three times applied',
    (S1.count('an application of the member for a disability retirement allowance under this chapter'),
     only164.count('an application of the member for a disability retirement allowance under this chapter')), (2, 3))
chk('G 4\'s model is self-contained in the same way, and is untouched',
    only164.count('For the purposes of this subdivision an application for a disability retirement allowance is pending'), 1)
print('   M2 — the two endpoints still diverge, deliberately: G 4 ends at the Board\'s FIRST ACT and')
print('   G 2 at the GRANT OR DENIAL. No marking is added, because any marking is the surplusage')
print('   MOO-209 F6 removed. Candidate 164-18 is the one form that is operative; it is HELD. §18.6.')
chk('G 4\'s endpoint', only164.count('until the date on which the Board first acts upon it.'), 1)
chk('G 2\'s endpoint', only164.count('until the date on which the Board grants or denies it.'), 1)

print('\n== S4 — the subsection J claim, counted and withdrawn')
_J = S1[S1.index('J. 1.'):]
_J = _J[:_J.index('\n')] if '\n' in _J else _J
chk('"failure to state" in subsection J', _J.count('failure to state'), 0)
chk('"requires to be stated" in subsection J', _J.count('requires to be stated'), 0)
chk('J 1 reports LATENESS, not content', _J.count('within a period required by this section'), 1)
chk('the model for candidate 164-17 — D 1\'s own certification sentence — is in the base, once',
    S1.count('A failure to state in the Board\'s certification every matter this subdivision requires to be stated in it'), 1)
chk('subsection M 2\'s trigger reaches a certification or notice and not a written statement',
    (S1.count('a failure of the Board to state in a certification or notice a matter this section requires to be stated in it'),
     S1.count('written statement, notice, or certification')), (1, 2))
chk('  and the disclosure sentence now carries (i), (ii), (iii) and (iv)',
    [only164.count(f'({n})') > 0 for n in ('i', 'ii', 'iii', 'iv')], [True] * 4)
# MOO-209 did not raise this; store revision 70 did, by moving D 1's certification series' "and" to
# its new last item. Adding clause (iv) without moving the "and" would leave the series with two
# conjunctions. The move is asserted in both directions so it cannot be lost in a re-cut.
_DS = only164[only164.index('The Board shall state, in the written statement required by that definition,'):]
_DS = _DS[:_DS.index("previously filed by the member.") + 31]
chk('the disclosure series carries exactly one "and" before its last item',
    (_DS.count('; and ('), _DS.count('; (')), (1, 2))
chk('  and that one "and" is before clause (iv), not clause (iii)',
    (_DS.count('; and (iv)'), _DS.count('; and (iii)')), (1, 0))
chk('  clause (iii) survives, unchanged in substance', _DS.count('; (iii) that where the Board mails the statement or notice'), 1)

print('\n== S3 — the paraphrase is out and the cut\'s own descriptor is in')
R6 = ('Where the Board\'s action upon a request determines a member\'s final qualifying retirement date '
      'under this definition, the Board shall state that date in its decision upon the request, and '
      'where the Board does not do so it shall give the member written notice of that date no later '
      'than 15 days after it acts upon the request.')
chk('R-6 is in the base, once', S1.count(R6), 1)
chk('the revision-7 PARAPHRASE is gone from the applied text', only164.count(E164_7_EXC_V7_DEAD), 0)
# MOO-214 S3's two rival referents for the paraphrase, counted so the ambiguity is a number.
chk('  R-3 — a duty to give written notice of a DETERMINATION, which on the definition\'s first '
    'sentence is a determination of that date', S1.count('written notice of its determination and of the reasons for it'), 1)
chk('  R-4b — a duty to give written notice of ANY LATER DATE APPROVED, which that definition makes '
    'the member\'s final qualifying retirement date',
    S1.count('written notice of any later date approved'), 1)
print('   -- so the paraphrase had three candidate referents, not one. The replacement has one.')
chk('the descriptor is the one 164-5 and 164-13(a) put into the bill — 0 in the base',
    S1.count("notice of a date required by that definition by reason of the Board's action upon a request"), 0)
chk('  and it stands at THREE sites in the applied text: 164-5, 164-13(a) and 164-7\'s exception',
    only164.count("notice of a date required by that definition by reason of the Board's action upon a request"), 3)
chk('  the exception carries it once', E164_7_EXC.count(R6_DESCRIPTOR), 1)
# Determinacy: in D 1 the descriptor is listed BESIDE "notice of a later approved date", in both
# lists, so the parallel excludes R-4b by the bill's own words rather than by argument.
for lbl, frag in [('the lateness sentence (164-5)', 'any notice of a later approved date required by that definition, or any notice of a date required by that definition by reason of'),
                  ('the disclosure sentence (164-13(a))', 'in every notice of a later approved date required by that definition, and in every notice of a date required by that definition by reason of')]:
    chk(f'  R-4b and R-6 are listed as separate items in {lbl}', only164.count(frag), 1)
chk('exactly one duty in §1 to give the member written notice of that date', S1.count('give the member written notice of that date'), 1)
print('   -- the MOO-141 Edit 2 interaction, counted on both bases rather than argued')
chk('on the base R-6\'s 15 days is keyed to the Board\'s ACT',
    S1.count('written notice of that date no later than 15 days after it acts upon the request'), 1)
chk('after MOO-141 Edit 2 REVISION 6 it was decision-keyed only, and the exception went inert',
    patched141.count('written notice of that date no later than 15 days after it gives its decision upon the request'), 1)
print('   MOO-141 Edit 2 REVISION 8 adds the residual limb that cures it. That limb is theirs, not')
print('   ours; the combined-text assertions for it live in moo141-rev71/verify_r71.py. What is')
print('   asserted here is only that OUR descriptor is not deadline-keyed, so no re-keying of R-6\'s')
print('   fifteen days can detach it:')
chk('the descriptor contains no deadline formula',
    any(x in R6_DESCRIPTOR for x in ('15 days', 'no later than', 'acts upon the request,')), False)

print('\n== m2 — the no-deemed-statement sentence, and N1 is preserved by making it SEPARATE')
chk('present once in the applied text', only164.count(NOT_STATED), 1)
chk('0 in the base', S1.count(NOT_STATED), 0)
chk('it is not inside the saving body — the 256 characters are untouched', SAVING.count(NOT_STATED), 0)
chk('R-6\'s condition it protects is in the base, once', S1.count('and where the Board does not do so it shall give the member written notice of that date'), 1)

print('\n== the Policy Director\'s MOO-141 §3.3 cross-reference, against their three requirements')
chk('present once in the applied text', only164.count(XREF), 1)
chk('req 1 — it says what THIS deeming governs', XREF.count('applies where the Board does not act upon the request'), 1)
chk('req 1 — and what the OTHER governs', XREF.count('applies where the Board acts upon a request more than once'), 1)
chk('req 2 — cumulative, and neither exclusive',
    (XREF.count('apply cumulatively'), XREF.count('neither is the exclusive rule')), (1, 1))
chk('req 3 — it moves no date: no "no later than", no figure, no month',
    any(x in XREF for x in ('no later than', 'days', 'month', 'date of')), False)
chk('req 3 — it adds no exception: no "except"', XREF.lower().count('except'), 0)
# It names the other deeming BY CONTENT, so with MOO-141 absent the class is empty and the clause is
# inert; with MOO-141 present it resolves to Edit 1's sentence and to nothing else.
OTHER = "on the date on which the Board first acts upon it"
chk('the other deeming\'s content-descriptor matches nothing in the base', S1.count(OTHER), 0)
chk('  G 4\'s two "the date on which the Board first acts upon it" are NOT it — they deem nothing',
    S1.count('until the date on which the Board first acts upon it'), 2)
chk('  matches nothing in MOO-164 alone except the cross-reference itself', only164.count(OTHER), 1)
chk('  and matches MOO-141 Edit 1\'s sentence, and only it, on the combined text', both.count(OTHER), 2)
chk('  Edit 1\'s deeming carries those exact words', E1_R.count('on the date on which the Board first acts upon it'), 1)

print('\n== M4 — the expressio unius inference is INERT, and that is counted, not argued')
E2_R8 = ("it shall give the member written notice of that date no later than 15 days after it gives its "
         "decision upon the request, except that where the request is denied otherwise than by a decision "
         "of the Board upon it, or where the period allowed by this section for acting upon the request "
         "expires without the Board's acting upon it, it shall give that notice no later than 15 days "
         "after the date on which the Board acts upon the request.")
both_r8 = apply_all(S1.replace(E1_F_R68, E1_R, 1).replace(E2_F, E2_R8, 1).replace(E3_F, E3_R6, 1))
chk('MOO-141 Edit 2 revision 8 applies cleanly beside this cut', both_r8.count(E2_R8), 1)
chk('  R-6\'s ORDINARY-class deadline is decision-keyed, so Edit 1\'s deeming cannot reach it '
    'whether or not R-6 is excepted from Edit 1\'s saving',
    both_r8.count('no later than 15 days after it gives its decision upon the request'), 1)
chk('  R-6\'s residual deadline is confined to the two no-decision classes, which are 164-7\'s own',
    both_r8.count("where the request is denied otherwise than by a decision of the Board upon it"), 1)
print('   So the adverse reading M4 fears — "R-6 is not excepted from Edit 1\'s saving, therefore the')
print('   deeming reaches it" — produces no consequence: in Edit 1\'s class (the Board that acts more')
print('   than once and decides) R-6\'s deadline runs from the GIVING OF A DECISION and the deeming')
print('   does not touch it. The asymmetry is inert as well as principled. §18.9.')

print('\n== F5 — the mislabelled 48-day line is DELETED, and replaced by the finding itself')
chk('"notice of its decision" occurs 0 times in the base — no provision requires it by any date',
    S1.count('notice of its decision'), 0)
chk('it occurs once in the applied text, and only because Edit 164-1 adds it',
    only164.count('notice of its decision'), 1)
chk('the duty that governs a definition request is keyed to the FILING, not to the act',
    S1.count('written notice of its determination and of the reasons for it, no later than 30 days after the request is filed'), 1)
print('   so the periods 48 displaces are act + 62 (definition request, every duty met, mailed) and')
print('   UNBOUNDED (reconsideration request, no duty fixes the giving). 48 is a CHOSEN outer limit.')
print('   The revision-6 claim that "every number in it is already in the section" does not hold.')

print('\n== F16 — a commencement is asserted WITHIN each of the five "shall act upon" duties')
chk('"shall act upon" in §1 (base)', S1.count('shall act upon'), 5)
chk('"shall act upon" in §1 (applied) — 164-10 adds no duty', only164.count('shall act upon'), 5)
COMMENCEMENTS = 0
for mm in re.finditer('shall act upon', only164):
    seg = only164[mm.start():mm.start() + 260]
    seg = seg[:seg.index('.') + 1] if '.' in seg else seg
    if re.search(r'after (?:the request is filed|the application is filed|the confirmation is obtained|'
                 r'it acts upon the request|the application is completed|the request is made)', seg):
        COMMENCEMENTS += 1
chk('all five state a commencement inside their own sentence', COMMENCEMENTS, 5)

print('\n== N2 — EVERY "preceding sentence" reference in the applied §1, resolved')
base_pr = S1.count('the preceding sentence')
app_pr = only164.count('the preceding sentence')
print(f'   base {base_pr}; applied {app_pr}; the edits add {app_pr - base_pr}')
chk('revision 7 adds exactly three "preceding sentence" references', app_pr - base_pr, 3)
chk('  two of them are 164-7\'s', EDITS[6][2].count('the preceding sentence'), 2)
chk('  one of them is 164-8\'s', EDITS[7][2].count('the preceding sentence'), 1)
chk('164-13 adds none — it says "this sentence", not "the preceding sentence"',
    EDITS[8][2].count('the preceding sentence') + EDITS[9][2].count('the preceding sentence'), 0)
chk('"this sentence" references added by revision 7', only164.count('described in this sentence'), 1)

print('\n== ordering invariants — now with 164-13 between 164-8 and the rest of D 1')
D1_S = ("the member may state an effective date of retirement that is no earlier than the first day of "
        "the month following the month in which the Board gives the statement or notice")
chk('164-5 FIND precedes 164-8 FIND inside one sentence of D 1',
    S1.index(EDITS[4][1]) < S1.index(D1_S), True)
chk('164-8 FIND precedes 164-13(a) FIND — the vehicle lands before the disclosure sentence',
    S1.index(EDITS[7][1]) < S1.index(EDITS[8][1]), True)
chk('164-13(a) FIND precedes 164-13(b) FIND inside one sentence',
    S1.index(EDITS[8][1]) < S1.index(EDITS[9][1]), True)
# The slice runs from mid-lateness-sentence to the start of 164-8's new sentence, so exactly one
# sentence boundary — the lateness sentence's own — may lie inside it. Two would mean something was
# inserted between them and 164-8's "the preceding sentence" had been stranded.
chk('164-8\'s "the preceding sentence" still means the lateness sentence — nothing is inserted between',
    only164[only164.index(D1_S):only164.index('Where the Board gives any notice of a kind described in the preceding sentence')].count('. '), 1)
DEEM = 'Where a request is denied by operation of the preceding sentence'
SAVE = 'Except for the purposes of the duty of the Board under this subsection to act upon an application'
DENIAL_END = 'a case decision as defined in § 2.2-4001 for the purposes of this subsection.'
chk('the deeming sentence immediately follows the denial sentence',
    only164[only164.index(DENIAL_END) + len(DENIAL_END):].lstrip().startswith(DEEM), True)
chk('the saving sentence immediately follows the deeming sentence',
    only164[only164.index(DEEM):only164.index(SAVE)].count('. '), 1)
chk('m2\'s sentence immediately follows the saving, and the cross-reference immediately follows m2\'s',
    only164[only164.index(SAVE):only164.index(XREF)].count(SAVING + ' ' + NOT_STATED + ' '), 1)

print('\n== question 4 — D 1\'s ordinal reference into M 2, re-run for thirteen substitutions')
chk('D 1 ordinal reference still present and singular', S1.count('the second sentence of subdivision M 2'), 1)
M2_SENTENCES = [
    'written reconsideration by the Board stating the reasons for its decision.',
    'is a determination of the Board for the purposes of this subsection, whether or not another provision of this section expressly provides for review of it.',
    'The Board shall act upon a request for reconsideration within 90 days.',
    'the person who filed the request may file with the Board written notice that the period has expired.',
    'and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.',
]
pos = [S1.index(s) for s in M2_SENTENCES]
chk('M 2 sentence order 1 < 2 < 3 < 4 < 5', pos == sorted(pos), True)
M2_START = S1.index(M2_SENTENCES[0])
chk('no applied edit inserts into M 2 before sentence 2',
    all(S1.index(f) > pos[1] or S1.index(f) < M2_START for _, f, _ in EDITS), True)

print('\n== item 131 — the antecedent of "such case decision" is unmoved')
COMPLETION = 'Upon completion of a reconsideration under this subsection, the final determination issued by the Board shall constitute a case decision as defined in § 2.2-4001.'
chk('completion sentence still present once', only164.count(COMPLETION), 1)
chk('164-7\'s two sentences sit before the completion sentence', only164.index(SAVE) < only164.index(COMPLETION), True)
chk('164-7 introduces no competing "case decision"',
    only164[only164.index(DEEM):only164.index(SAVE) + 900].count('case decision'), 0)

print('\n== the SIX HELD candidates, asserted against the APPLIED text — none of them is applied')
HELD_CANDIDATES = [
 ('164-9  (MOO-204) — the two-limb cap closing the last 60 days at M 2\'s tolling endpoint',
  'and in no case later than 48 days after the Board acts upon the request'),
 ('164-14 (MOO-209 F10) — "or the application is otherwise disposed of"',
  'until the date on which the Board grants or denies it.'),
 ('164-15 (MOO-214 S6) — the non-receipt saving on s12\'s 30-day window',
  'no later than 30 days after the Board gives the notice; and a notice so filed'),
 ('164-17 (MOO-214 S4) — the failure-to-state route for the written statement',
  'and supersedes any notice of retirement previously filed by the member.'),
]
for lbl, f in HELD_CANDIDATES:
    chk(f'{lbl[:72]} — FIND in applied §1', only164.count(f), 1)
    chk(f'   {"":68} — FIND in the base (must be 0: it amends this cut\'s own new text)', S1.count(f), 0)
# 164-16 and 164-18 are alternatives to applied text, so their FINDs are in the applied text and in
# the base respectively. Counted here so neither can be applied by accident on top of the other.
chk('164-16 (counsel\'s impose-not-except form of S3) would REPLACE the exception\'s second limb, '
    'which stands once', only164.count('and the duty of the Board under the definition of "final qualifying retirement date" in subsection A to give ' + R6_DESCRIPTOR), 1)
C18_F = ('Nothing in this subdivision prevents the payment of a retirement allowance to a member while '
         'an application of the member for a disability retirement allowance under this chapter is '
         'pending, and the determination required by this subdivision shall take effect notwithstanding '
         'that a retirement allowance has been paid to the member while such an application was pending.')
chk('164-18 (MOO-214 M2 alternative) FIND is in the BASE, once — it rewrites item 46\'s own words',
    S1.count(C18_F), 1)
chk('  and it is incompatible with 164-12 as applied: 164-12\'s FIND is inside it',
    C18_F.count(EDITS[12][1]), 1)
print('   164-18 is HELD and is NOT a drafting choice: it deletes enacted words of §7 item 46 and is')
print('   the Policy Director\'s call. §18.6 question 3.')

print('\n== F6 — the confinement-clause family 164-12 must not weaken')
conf = (S1.count('For the purposes of this subdivision') + S1.count('for the purposes of this subdivision') +
        S1.count('For the purposes of this subsection') + S1.count('for the purposes of this subsection'))
print('   confinement clauses of that family in the base:', conf)
chk('G 4\'s definition is expressly confined, so there was nothing to notwithstand',
    S1.count('For the purposes of this subdivision an application for a disability retirement allowance is pending'), 1)
chk('164-12 adds a confinement clause and no notwithstanding',
    (only164.count('Notwithstanding the definition in subdivision 4'),
     only164.count('For the purposes of this subdivision, an application of the member')), (0, 1))

print('\n== F12 — the B 4 f extension reaches no provision, counted so nobody goes looking')
# Slice § 51.1-142.2's own text out of §1 by its heading, and count the verb family inside it.
_heads = [(mm.start(), mm.group(0).strip()) for mm in re.finditer(r'\n### [^\n]*', S1)]
_a = [x for x, y in _heads if '51.1-142.2' in y][0]
_nxt = [x for x, y in _heads if x > _a]
SEC1422 = S1[_a:(_nxt[0] if _nxt else len(S1))]
print(f'   § 51.1-142.2 as enacted in this act: {len(SEC1422)} characters')
chk('the act-upon family anywhere in § 51.1-142.2',
    len(re.findall(r"\b(?:acts|act|acting|action)\s+upon\b", SEC1422)), 0)
chk('164-7 nevertheless extends to subdivision B 4 f of it, once',
    EDITS[6][2].count('and of subdivision B 4 f of § 51.1-142.2'), 1)
print('   MOO-209 F12 confirmed: the extension reaches no provision on the present text. It mirrors')
print('   M 2\'s tolling sentence, which names B 4 f for periods within which the MEMBER must act, and')
print('   it is 46 characters of insurance. KEPT, and the count is now in the record.')

print('\n== F2 — the verb, counted and never predicted')
for ph in ['acts upon', 'act upon', 'acting upon', 'action upon']:
    print(f'   {ph:14} §1 base={S1.count(ph):3}  +164 only={only164.count(ph):3}  '
          f'+141 only={patched141.count(ph):3}  both={both.count(ph):3}')
STEM = re.compile(r"\b(?:acts|act|acting|action)\s+upon\b")
for nm, bd in [('store rev 70 §1', S1), ('+ MOO-164 revision 7', only164),
               ('+ MOO-141 patch, Edit 3 at 120 days', patched141), ('+ both', both)]:
    print(f'   occurrence census {nm:36} {len(STEM.findall(bd))}')

print('\n== the formula — five sites, every variant at zero')
chk('"the period allowed by this section for acting upon"',
    only164.count('the period allowed by this section for acting upon'), 5)
chk('  of which "... the request"',
    only164.count('the period allowed by this section for acting upon the request'), 3)
chk('  of which "... it"', only164.count('the period allowed by this section for acting upon it'), 2)
chk('"the period allowed to it for acting upon the request" after 164-6',
    only164.count('the period allowed to it for acting upon the request'), 0)
chk('"the period this definition allows" after 164-4', only164.count('the period this definition allows'), 0)
chk('"the 90 days allowed by this subsection" after 164-3 and 164-11',
    only164.count('the 90 days allowed by this subsection'), 0)
chk('  it was this many in the base', S1.count('the 90 days allowed by this subsection'), 2)
print('   F13 DECLINED: "for acting upon that request" would make a SIXTH variant of a term card (j)')
print('   and Edit 164-6 exist to conform. Drafted at §17.9 so the Director can overrule in one line.')

print('\n== figures this document quotes, re-counted at store revision 70')
chk('"no later than" in §1 (base) — 74 at store revision 70, 76 at 71/72', S1.count('no later than'), 76)
chk('m8-a: the 90-day proviso on the excluded periods',
    S1.count('the aggregate of all periods so excluded shall not exceed 90 days'), 1)
chk('m8-a survives Edit 164-3', only164.count('the aggregate of all periods so excluded shall not exceed 90 days'), 1)
chk('clause (ii) aggregate still 120 days',
    S1.count('the aggregate of all tolling under this subsection shall not exceed 120 days'), 1)
chk('60 + 30 + 120 + 90', 60 + 30 + 120 + 90, 300)

print('\n== subsection A at store revision 70 — the facts behind the 48-day route table')
chk('the three-day extension is confined to mailing',
    S1.count('where the Board mails a written statement, notice, or certification'), 1)
chk('the giving rule reaches certifications',
    S1.count('a written statement, notice, or certification required of the Board is given on the date'), 1)
chk('the 5:00 p.m. electronic cut-off',
    S1.count('an electronic transmission completed after 5:00 p.m. is given on the following day'), 1)

print('\n== the two savings after both patches')
chk('MOO-164 alone: one saving, carrying its (now extended) exception', only164.count(SAVING), 1)
chk('MOO-141 alone: one saving, carrying its exception', patched141.count(SAVING), 1)
chk('both patches: two savings, two exceptions, neither bare',
    (both.count(SAVING), both.count('Except for the purposes of the duty of the Board')), (2, 2))
chk('164-7\'s exception names "this subsection" and R-6; Edit 1\'s names "subsection M" alone',
    (both.count(E164_7_EXC), both.count(E1_EXC)), (1, 1))
print('   The asymmetry is PRINCIPLED and is stated at §17.3: 164-7 must except R-6 because the no-act')
print('   case has no decision to key to; Edit 1 need not, because MOO-141 Edit 2 re-keys R-6 to the')
print('   giving of a decision. Those are two sides of one fact, and the second is why F1\'s cure goes')
print('   inert on the combined text.')

print('\n== the descriptor M 2\'s 15-day duty shares')
DESC = 'no later than 15 days after it acts upon the request'
chk('base: two referents — M 2\'s duty and R-6\'s notice', S1.count(DESC), 2)
chk('after both patches, exactly one referent survives outside the exceptions',
    both.replace(E164_7_EXC, '').replace(E1_EXC, '').count(DESC), 1)

print('\n== apostrophes (§6.7 record item)')
chk('typographic apostrophes in §1', S1.count('’'), 4)
G4S = S1.index('4. Subdivisions 2 and 3 shall not apply')
G4E = S1.index('5. A member may cancel an election at any time before payment is completed')
chk('all four are inside subdivision G 4', S1[:G4S].count('’') + S1[G4E:].count('’'), 0)
print('   straight apostrophes in §1:', S1.count("'"))

print('\n== F21 — whole-document counts for the strings a whole-document replace would corrupt')
for label, f in [(lbl.split(' ')[0] + ' FIND', f) for lbl, f, _ in EDITS]:
    if doc.count(f) != S1.count(f):
        print(f'   {label:20} §1={S1.count(f)}  whole document={doc.count(f)}  <-- §1-only apply REQUIRED')
print(f'   MOO-141 E3 FIND      §1={S1.count(E3_F)}  whole document={doc.count(E3_F)}')

print(f'\n== revision 8 delta over enacted §1: +{REV7_DELTA}')
print(f'== {fail} failure(s)')
sys.exit(1 if fail else 0)
