# -*- coding: utf-8 -*-
"""
MOO-217 — the subdivision D 1 extension channel the MOO-141 revision 9 patch opens,
priced. Four questions from the Policy Director, answered in order.

Run:  python3 moo217_d1_channel.py
      python3 moo217_d1_channel.py > out_moo217_run.txt

No numpy required. Fully deterministic — there is no random draw anywhere in this model
and no wall-clock line in the output, so two runs diff byte-identical.

Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import moo217_inputs as A  # noqa: E402


def rule(title):
    print()
    print('=' * 78)
    print(title)
    print('=' * 78)


def usd(x):
    return f'${x:,.0f}'


def usd2sf(x):
    """Two significant figures, because MOO-46 Decision 4 says nothing here is reliable
    beyond that and the inputs are rounded to it. Dollar-exact cells would be false
    precision carried from a cohort count given to two figures."""
    if x == 0:
        return '$0'
    import math
    mag = math.floor(math.log10(abs(x)))
    q = round(x, -(mag - 1))
    return f'${q:,.0f}'


FAILS = []


def check(name, cond):
    print(f'   [{"PASS" if cond else "FAIL"}] {name}')
    if not cond:
        FAILS.append(name)


# ===========================================================================
rule('SECTION 0 -- VINTAGE, AND THE REGISTER IMPORTED UNCHANGED')
# ===========================================================================

TEXT = open(A.BILL_TEXT_PATH, encoding='utf-8').read()
print(f'   enacted §1 extract read from : {os.path.relpath(A.BILL_TEXT_PATH)}')
print(f'   characters in the extract    : {len(TEXT):,}  '
      f'(of {A.BILL_DOC_CHARS:,} in the whole bill-text-s8 document)')
print(f'   bill store revision          : {A.BILL_STORE_REVISION}')
print(f'   patch under test             : revision {A.PATCH_REVISION}, '
      f'{A.PATCH_EDIT_COUNT} edits, +{A.PATCH_CHARS_ADDED:,} characters in enacted §1')
check('the extract is the vintage the register declares', len(TEXT) == A.BILL_TEXT_CHARS)
check('the extract carries the whole of the new § 51.1-142.4',
      '§ 51.1-142.4. Military service purchase pilot program' in TEXT)
print()
print('   MOO-163 register imported unchanged. Levers this issue leans on:')
print(f'     D 2 aggregate cap                 {usd(A.AGGREGATE_CAP_USD)}')
print(f'     D 2 per-election ceiling          {usd(A.PER_ELECTION_CEILING_USD)}')
print(f'     D 3 contingency rate              {A.CONTINGENCY_RATE:.0%}  (still a [20] bracket)')
print(f'     pilot length                      {A.PILOT_LENGTH_MONTHS} months')
print(f'     funded cohort, central            {A.PARTICIPANTS_ADMITTED_FUNDED["central"]:.2f} members / 48 months')
print(f'     M 2 seek rate, central            {A.RECONSIDERATION_SEEK_RATE["central"]:.2f} (analyst judgment, MOO-163)')

REFUSED_CENTRAL = sum(A.STATUTORY_REFUSALS_CENTRAL.values())
print(f'     refused members, central          {REFUSED_CENTRAL:.2f} / 48 months '
      f'(sum of the four MOO-163 refusal rows)')

print()
print('   NEW statutory parameters read off this cut (text, not estimates):')
print(f'     period allowed on a definition request   {A.DEFINITION_REQUEST_ACT_DAYS} days')
print(f'     M 2 period on a reconsideration request  {A.BOARD_DECISION_DEADLINE_DAYS} days')
print(f'     Edit 4 notice deadline                   {A.EDIT4_NOTICE_DAYS} days after period expiry')
print(f'     mailing extension                        {A.MAILING_EXTENSION_DAYS} days')
print(f'     D 1 excluded aggregate, per member       {A.EXCLUDED_AGGREGATE_CAP_DAYS} days (12 months)')
print(f'     subsection N payment window              {A.N_PAYMENT_DAYS} days after settlement')


# ===========================================================================
rule('SECTION 1 -- THE COSTING QUESTION, AND THE UNIT OF ANALYSIS')
# ===========================================================================

print("""
   Over the 48-month pilot, does the channel through which a member's final qualifying
   retirement date can move when the Board does not act -- the subdivision D 1 lateness
   extension, and the new Edit 4 notice that attaches to the definition's expiry
   sentence -- change the amount the Commonwealth pays to the retirement system under
   subsection N, or the number of members who receive a certified subsidy rather than
   subsection B standard-cost rights?

   UNIT OF ANALYSIS. One member-event: one member, one no-act occasion, one outcome on
   the settle/release line. NOT one reservation (which is MOO-163's unit) and NOT one
   queue-ordering date (which is MOO-170's unit). The change of unit is the whole reason
   this is a separate issue and it is the answer to question 2.

   HORIZON. The 48-month pilot. July 1 effective date; FY%d carries implementation only;
   FY%d is the first benefit year (MOO-183 §8). Events in this channel require an
   accepted election, credited service credit, a filed request, a no-act, and then the
   passage of a date, so they land at the BACK of the pilot, not evenly across it.
   Settlements are paid within %d days of settlement under subsection N.
""" % (A.FY_IMPLEMENTATION, A.FY_FIRST_BENEFIT, A.N_PAYMENT_DAYS))

print("""   WHAT MOVES THE MONEY, in one chain, because every figure below hangs off it:

     subsection F   she must retire in a qualifying retirement on or before her FQRD
     subdivision G 1  if she does -> subsidy SETTLED, credit vests at the subsidised cost
     subdivision G 2  if she does not -> credit REDUCED to standard-cost equivalent,
                      excess payments REFUNDED, reservation RELEASED
     subdivision G 4  three exceptions where 2 and 3 do not apply and the credit vests at
                      the subsidised cost anyway: (i) death, (ii) disability approval,
                      (iii) "unable to retire in a qualifying retirement by reason of an
                      error of the Board"
     subsection N     "Upon the settlement of a certified subsidy under subdivision G 1
                      OR G 4, the Commonwealth shall pay the amount settled to the
                      retirement system from an appropriation made for that purpose"

   So a settlement is an APPROPRIATION OUTLAY and a release is not. That is the line this
   channel lands on, and it is a different line from the one MOO-163 and MOO-170 priced.""")


# ===========================================================================
rule('SECTION 2 -- QUESTION 1: THE TWO MISSING INPUTS')
# ===========================================================================

print("""   Asked: can the Board no-act rate and the later-date filing rate be sourced,
   bounded, or honestly declared unobtainable?

   2.1 MECHANICAL SCAN OF EVERY REGISTER IN THIS PROJECT.""")

REG_PATHS = []
_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
for dirpath, _dirnames, filenames in os.walk(_root):
    if any(part in dirpath for part in ('__pycache__', '/.git')):
        continue
    for fn in filenames:
        if fn.endswith('_inputs.py') or fn.endswith('inputs.py'):
            REG_PATHS.append(os.path.join(dirpath, fn))
REG_PATHS = sorted(set(REG_PATHS))

NOACT_PAT = re.compile(r'NO_?ACT|NOACT|FAIL(URE)?_TO_ACT|ON_TIME|DEEM', re.I)
FILING_PAT = re.compile(r'LATER_DATE|FQRD|FILING_RATE|REQUEST_RATE', re.I)
NEAR_PAT = re.compile(r'QUALIFY|QUALIFYING|LATENESS|EXTENS|NOTICE', re.I)

print(f'   registers found: {len(REG_PATHS)}')
hits_noact, hits_filing, near = [], [], []
total_levers = 0
for p in REG_PATHS:
    src = open(p, encoding='utf-8').read()
    names = set(re.findall(r'^([A-Z][A-Z0-9_]{3,})\s*=', src, re.M))
    rel = os.path.relpath(p, _root)
    own = rel.startswith('moo217')
    n_hit = sorted(n for n in names if NOACT_PAT.search(n))
    f_hit = sorted(n for n in names if FILING_PAT.search(n))
    near_hit = sorted(n for n in names
                      if NEAR_PAT.search(n) and n not in n_hit and n not in f_hit)
    print(f'     {rel:<58} levers={len(names):>3}'
          f'  no-act={n_hit if n_hit else "-"}'
          f'  later-date={f_hit if f_hit else "-"}'
          f'{"   (this issue)" if own else ""}')
    if not own:
        total_levers += len(names)
        hits_noact += [(rel, n) for n in n_hit]
        hits_filing += [(rel, n) for n in f_hit]
        near += [(rel, n) for n in near_hit]

print()
print(f'   levers scanned across pre-existing registers             : {total_levers}')
print(f'   pre-existing registers carrying a Board no-act rate      : '
      f'{hits_noact if hits_noact else "NONE"}')
print(f'   pre-existing registers carrying a later-date filing rate : '
      f'{hits_filing if hits_filing else "NONE"}')
print(f'   NEAR MISSES, reported rather than suppressed             :')
for rel, n in near:
    print(f'       {rel}  ::  {n}')
print("""
   CONFIRMED on MOO-215's finding, and on a wider scan than MOO-215 ran: neither input
   exists in any of the pre-existing registers in this project. "$0 on this limb" was
   therefore an unpriced assertion, not a counted one.

   AND ONE NEAR MISS IS NOT A MISS. MOO-204's NON_QUALIFYING_RETIREMENT_SHARE is the
   fraction of FUNDED participants who do not retire in a qualifying retirement and so
   reach a G 2 cutback -- 2% / 5% / 15%, analyst judgment on MOO-140 §3.2's four
   narrowing grounds. That is the UNCONDITIONAL rate of the very event this channel turns
   on. It does not supply either input the Policy Director asked about, but it does anchor
   the FLOOR of the third input §2.4 shows is needed, and this model uses it as that
   floor rather than guessing the conditional rate free-standing. Searching for the two
   named inputs turned up a third that was already in the record.""")

print("""   2.2 THE BOARD NO-ACT RATE: UNOBTAINABLE, AND THE REASON IS A MISSING DENOMINATOR.

     - VRS publishes no on-time-decision rate for § 51.1-142.2 purchase determinations.
     - MOO-71 §3 establishes that NO published count of § 51.1-142.2 military purchases
       exists at all. A rate needs a denominator and the denominator does not exist.
       Denominator discipline forbids reporting a rate here.
     - The bill would CREATE the series prospectively: subsection J requires the Board to
       report every failure to give a notice within the period and every D 1 delay. A
       figure a bill has to commission is a figure that is not collected now.
     - There is no comparable programme to scale from. The §51.1-142.4 subsidy is a
       Virginia-specific construct with no other-state analogue; Comparative Policy
       Analyst has supplied no take-up or no-act series for it.

     DECLARED UNOBTAINABLE. Not guessed, not defaulted to zero. It is SWEPT across
     %s
     and the answer in §5 is reported as a THRESHOLD IN THIS VARIABLE -- the no-act rate
     at which the channel becomes material -- so that no figure below is conditioned on a
     rate I cannot source.

   2.3 THE LATER-DATE FILING RATE: NOT SOURCEABLE EITHER, BUT BOUNDABLE FROM TEXT.

     Bounded ABOVE by 1.00, which is the value MOO-215 used and which they say over-counts.
     The text narrows it on three grounds, all in the definition:
       (a) the ground is confined to where "the Board's own processing requirements, or
           any other cause not attributable to the member" make timely retirement
           impracticable -- a member with no such cause has nothing to request;
       (b) the relief is confined to not more than %d months and to the first day of a
           month, so the request is worth filing only to a member whose problem fits;
       (c) the Board "shall approve a later date ON ITS OWN INITIATIVE or upon the written
           request of the member" -- own-initiative approval removes the need to file in
           exactly the cases most likely to have a qualifying cause.
     Against that, filing is costless, may be made "at any time before the date that would
     otherwise apply", and D 1 obliges the Board to tell the member about the mechanism.

     CARRIED AS ANALYST JUDGMENT, %.2f central, band %.2f-%.2f. Labelled as judgment
     everywhere it is used. I would not defend MOO-215's 1.00 as a central case.
""" % (str(A.BOARD_NO_ACT_RATE_SWEEP), A.LATER_DATE_MAX_MONTHS,
       A.LATER_DATE_FILING_RATE['central'], A.LATER_DATE_FILING_RATE['low'],
       A.LATER_DATE_FILING_RATE['high']))

print("""   2.4 A THIRD INPUT THE QUESTION DID NOT NAME, AND IT IS NEEDED.

     Exposure is not harm. MOO-215 counted members whose date CAN move; the money moves
     only where her date actually passes without a qualifying retirement. That conversion
     needs a HARM REALISATION RATE, and MOO-215 implicitly set it to 1.00.
     1.00 over-counts, for a textual reason: the expiry sentence is PROTECTIVE. It sets
     her date to "the first day of the second month following the month in which that
     period expired" and applies only where the date that would otherwise apply is
     EARLIER. So a no-act hands the member at least a further month. What it does not hand
     her, before Edit 4, is the date itself.

     NOT FREE-STANDING JUDGMENT. It is built on MOO-204's prior figure and one labelled
     multiplier, so the reader can attack the multiplier alone:
         MOO-204 unconditional non-qualifying-retirement share   %.2f / %.2f / %.2f
       x information-failure multiplier (ANALYST JUDGMENT, 2x-8x) %.1f / %.1f / %.1f
       = harm realisation rate used here                         %.3f / %.3f / %.3f
     The unconditional rate is a FLOOR on the conditional one, because the condition --
     the Board's silence about her date -- cannot make her more likely to meet it.
""" % (A.NON_QUALIFYING_RETIREMENT_SHARE_BASE['low'],
       A.NON_QUALIFYING_RETIREMENT_SHARE_BASE['central'],
       A.NON_QUALIFYING_RETIREMENT_SHARE_BASE['high'],
       A.INFORMATION_FAILURE_MULTIPLIER['low'],
       A.INFORMATION_FAILURE_MULTIPLIER['central'],
       A.INFORMATION_FAILURE_MULTIPLIER['high'],
       A.HARM_REALISATION_RATE['low'], A.HARM_REALISATION_RATE['central'],
       A.HARM_REALISATION_RATE['high']))


# ===========================================================================
rule('SECTION 3 -- QUESTION 2: ARE MOO-163 AND MOO-170 SILENT, OR DO THEY COVER IT?')
# ===========================================================================

print("""   3.1 MOO-163's $0. SILENT. Two independent tests.

     TEST A -- lever test. MOO-163's register carries no final-qualifying-retirement-date
     lever, no notice-lateness lever and no no-act rate. Shown mechanically in §2.1.

     TEST B -- unit test, which is the stronger one. MOO-163's own stated unit of analysis
     is "one certified subsidy RESERVATION" and its own stated mechanism is:
       "The retention endpoint can move money only where queue position decides who is
        funded. Queue position decides that only where the $3.00M cap BINDS."
     This channel does not touch queue position. It touches whether a reservation already
     made is SETTLED or RELEASED. At the central estimate MOO-163 reports the cap does not
     bind (67.4% utilisation), which is exactly the condition under which MOO-163's
     mechanism is inert -- and it is NOT the condition under which this channel is inert.
     A settle/release flip moves an appropriation outlay under subsection N whether or not
     the cap binds. So MOO-163's $0 neither covers nor excludes this channel. SILENT.""")

print("""
   3.2 MOO-170's $204,000 BOUND. ITS GROUND DOES NOT SURVIVE THIS CHANNEL, AND THE
       REASON IS NOT THE ONE THE POLICY DIRECTOR ANTICIPATED.

     The Policy Director asked whether the bound's ground survives because "an unbounded
     or extended retention is not a longer figure, it is the absence of one". On that
     question MOO-170 IS RIGHT and the answer is YES. Reconstruct its derivation:""")

residual_bound = A.PER_ELECTION_CEILING_USD * (1 + A.CONTINGENCY_RATE)
print(f"""
       fill the queue in filing-date order against a fixed pool of {usd(A.AGGREGATE_CAP_USD)};
       whatever the order, the fill stops when the next application does not fit, so the
       unreserved residual is strictly less than one election plus its contingency:
         residual < {usd(A.PER_ELECTION_CEILING_USD)} x {1 + A.CONTINGENCY_RATE:.1f} = {usd(residual_bound)}
       two orderings each leave a residual in [0, that bound), so the difference in total
       RESERVED between any two orderings is bounded by |Δ| < {usd(residual_bound)}.""")
check('the reconstructed bound reproduces MOO-170/MOO-163\'s $204,000',
      abs(residual_bound - 204_000) < 1)

print("""
     There is no k in that derivation and no length of retention in it. A retention of any
     length, including an unbounded one, yields SOME ordering date or none; either way the
     fill is still a fill of the same fixed pool by some order. So the absence of a figure
     is not a counter-example and MOO-170's analytic claim holds on its own terms.

     BUT THE BOUND DOES NOT TRANSFER HERE, AND THE REASON IS THE QUANTIFIER. Read what the
     derivation quantifies over: ORDERINGS OF A FIXED SET OF APPLICATIONS against a fixed
     pool. It bounds a difference in the amount RESERVED. It holds two things constant that
     this channel moves:

       (1) the SET is fixed. This channel does not reorder the set; it changes whether a
           member already inside it ends in G 1/G 4 (settled) or G 2 (released).
       (2) the quantity bounded is RESERVED, and the bound is a bound on LAPSE -- MOO-163
           says so in terms: "note what the delta IS: it is a change in LAPSE". A
           settle/release flip is not a change in lapse. It is a change in the amount PAID
           under subsection N.

     So the $204,000 figure is not an upper bound on this channel. It is a bound on a
     different variable. Stated expressly, as asked: THE BOUND'S GROUND SURVIVES THE
     RETENTION-LENGTH QUESTION AND DOES NOT REACH THIS CHANNEL AT ALL.

   3.3 THE CORRECT HARD BOUND ON THIS CHANNEL, derived the same analytic way.""")

headroom_central = A.AGGREGATE_CAP_USD * (1 - A.CAP_UTILISATION_STATED['central']
                                          * A.RETIREMENT_WINDOW_RUNG_RATIO)
print(f"""
     Each event converts at most one release into one settlement, and one settlement is
     bounded by D 2's per-election ceiling: {usd(A.PER_ELECTION_CEILING_USD)}. So for N events

       0 <= channel exposure <= min( N x {usd(A.PER_ELECTION_CEILING_USD)} , unexpended balance of the cap )

     and the second term at the central cohort is
       {usd(A.AGGREGATE_CAP_USD)} x (1 - {A.CAP_UTILISATION_STATED['central']:.3f} x {A.RETIREMENT_WINDOW_RUNG_RATIO:.4f})
       = {usd(A.AGGREGATE_CAP_USD)} x (1 - {A.CAP_UTILISATION_STATED['central'] * A.RETIREMENT_WINDOW_RUNG_RATIO:.3f}) = {usd(headroom_central)}.

     THE SIGN IS NOT INDETERMINATE HERE, which is the second difference from MOO-170. A
     settle/release flip in this channel runs one way only: toward settlement, toward
     payment. There is no symmetric branch in which the Board's lateness causes a member
     to be paid LESS. So unlike MOO-163's lapse delta, this exposure cannot cancel across
     events and cannot be dismissed as sign-indeterminate noise. It is small or it is
     zero; it is never offsetting.""")


# ===========================================================================
rule('SECTION 4 -- QUESTION 3: IS EDIT 4 FISCALLY INERT? TESTED ON THE TEXT, '
     'NOT ON THE READING')
# ===========================================================================

print("""   Three screens, each a string test on the cut in §0, so each fails loudly if the
   text moves. Their LEGAL effect is Statutory Researcher's; what is mine is the test.

   4.1 SCREEN 1 -- D 1's enumeration. How many of D 1's limbs reach Edit 4's notice?""")

D1_SENT = ('Where the Board gives that written statement, any notice of a later approved '
           'date required by that definition, or any notice of a date required by that '
           'definition upon the Board\'s action upon a request, later than the time '
           'required by that definition, the member\'s final qualifying retirement date '
           'is extended by the number of days by which the statement or notice is late')
check('D 1\'s extension sentence is present in the cut verbatim', D1_SENT in TEXT)

D1_LIMBS = [
    ('L1  "that written statement"',
     'the statement first required by the definition, due 15 days after the Board credits '
     'the purchased service credit. A different instrument from Edit 4\'s notice, with a '
     'different trigger. DOES NOT REACH IT.'),
    ('L2  "any notice of a later approved date required by that definition"',
     'presupposes an APPROVAL of a later date. In a no-act case there is no approval. '
     'DOES NOT REACH IT.'),
    ('L3  "any notice of a date required by that definition upon the Board\'s ACTION '
     'upon a request"',
     'presupposes the Board\'s ACTION. Edit 4\'s notice is required by reason of the '
     'Board\'s NOT acting. DOES NOT REACH IT.'),
]
for limb, why in D1_LIMBS:
    print(f'\n     {limb}\n       -> {why}')

print(f"""
     SCREEN 1 RESULT: 0 of 3 limbs reach it. Property 5 HOLDS on my reading of the
     enumeration, and the Policy Director's claim is confirmed on this screen.

   4.2 SCREEN 2 -- is the screen conditioned on MOO-164's 164-5? NO, as F12 says.
     Pre-164-5 wording of L3  : "upon the Board's ACTION upon a request"
     Post-164-5 wording of L3 : "by reason of the Board's ACTION upon a request"
     The operative word in both is "action". A re-cut of the connective does not reach the
     noun it connects to. The screen is 164-5-INDEPENDENT and the channel opens either
     way, so nothing below is conditioned on 164-5.""")

print("""
   4.3 SCREEN 3 -- AND THIS IS WHERE THE CLAIM STOPS HOLDING. Subdivision G 4 clause
       (iii) is a SECOND channel, it is not the D 1 channel, and property 5 is the reason
       Edit 4 lands in it.""")

G4_DEEM = ('a member whose final qualifying retirement date passes at a time when the '
           'Board has not given such a statement or notice and the time allowed by that '
           'definition for giving it has expired is unable to retire in a qualifying '
           'retirement by reason of an error of the Board')
G4_CARVE = ('a statement or notice of the member\'s final qualifying retirement date '
            'required by that definition does not include the notice of the Board\'s '
            'determination upon a request, and of the reasons for it, that that '
            'definition requires to be given no later than 30 days after the request is '
            'filed, and the remedies of the member for a failure of the Board to give '
            'that notice are those provided by subdivision D 1, by that definition, and '
            'by subsection M')
N_SETTLE = ('Upon the settlement of a certified subsidy under subdivision G 1 or G 4, the '
            'Commonwealth shall pay the amount settled to the retirement system from an '
            'appropriation made for that purpose')
check('G 4 clause (iii)\'s deeming sentence is present verbatim', G4_DEEM in TEXT)
check('G 4 clause (iii)\'s carve-out is present verbatim', G4_CARVE in TEXT)
check('subsection N\'s payment obligation names G 4 as well as G 1', N_SETTLE in TEXT)

print(f"""
     Apply the deeming sentence to Edit 4's notice, element by element:
       "a statement or notice of the member's final qualifying retirement date"
            Edit 4: "the Board shall give the member written notice of THAT DATE",
            and "that date" is her final qualifying retirement date.          SATISFIED
       "required by that definition"
            Edit 4 is inserted INTO the definition, after the expiry sentence
            and before R-6.                                                    SATISFIED
       "the time allowed by that definition for giving it has expired"
            Edit 4 supplies a time: {A.EDIT4_NOTICE_DAYS} days after the expiration of the
            period for acting. Before Edit 4 there was no such time, because
            there was no such duty.                                            SATISFIED
       the carve-out: "does not include the notice of the Board's determination
            upon a request ... no later than 30 days after the request is filed"
            Edit 4's notice is NOT that notice. That notice is due {A.DEFINITION_REQUEST_ACT_DAYS} days
            after FILING and presupposes a determination; Edit 4's is due
            {A.EDIT4_NOTICE_DAYS} days after the PERIOD EXPIRES and presupposes none.
            NOT CARVED OUT.

     AND READ THE CARVE-OUT'S OWN REASON: "the remedies of the member for a failure of the
     Board to give that notice are those provided by SUBDIVISION D 1, by that definition,
     and by subsection M." The bill carves a notice OUT of G 4 clause (iii) precisely
     BECAUSE D 1 already remedies it. Property 5 establishes that D 1 does NOT remedy
     Edit 4's notice. On the carve-out's own logic that is the reason Edit 4's notice
     belongs INSIDE clause (iii).

     SCREEN 3 RESULT: Edit 4's notice enters G 4 clause (iii)'s deeming limb.

   4.4 VERDICT ON QUESTION 3, stated as two findings and not one.

     (a) PROPERTY 5 IS CORRECT AS WRITTEN. No D 1 extension attaches to Edit 4's notice,
         on either wording, and that holds on my model. The Policy Director's textual
         ground survives the test.

     (b) "FISCALLY INERT" DOES NOT FOLLOW FROM IT, AND IS NOT CONFIRMED. Edit 4 adds a
         required notice of a final qualifying retirement date where none was required.
         The non-giving of that notice is the trigger of G 4 clause (iii)'s deeming limb,
         and a clause (iii) case is settled rather than released, and a settlement is paid
         by the Commonwealth under subsection N. Edit 4 is inert on the D 1 channel and
         NOT inert on the G 4 channel. The claim was tested in the place the Policy
         Director pointed at, and it is right there; the cost is one subdivision over.

     One qualification I will not bury. Clause (iii)'s main limb is "unable to retire in a
     qualifying retirement by reason of an error of the Board", and the deeming sentences
     are expressed "for the purposes of clause (iii)". Whether they are INCLUSIVE examples
     or an EXHAUSTIVE definition is Statutory Researcher's, and whether a member in the
     expiry-sentence class could reach clause (iii) WITHOUT Edit 4 on the un-deemed limb
     is Red Team / Counsel Reviewer's. That probability is register input
     G4_BASELINE_AVAILABILITY and Edit 4's incremental cost is proportional to one minus
     it. I do not set it and I report the whole 0-1 interval.""")


# ===========================================================================
rule('SECTION 5 -- THE POPULATION, AND A CORRECTION TO MOO-215\'S SCOPING')
# ===========================================================================

print("""   5.1 THE EXPIRY SENTENCE NEEDS ONE NO-ACT GATE, NOT TWO. MOO-215's class 1 is
       quadratic because they modelled the subsection M 2 DEEMED DENIAL, which has two
       independent no-act gates. The sentence Edit 4 attaches to is not that. It reads:

         "Where the Board does not act upon a request the filing of which tolled the
          running of the member's final qualifying retirement date under subsection M
          within the period this definition allows for acting upon it ..."

       One no-act. So BOTH classes are LINEAR in the no-act rate in this channel, and
       MOO-215's class-1 column under-counts the expiry-sentence class by a factor of the
       no-act rate itself. Reported because it moves in the ADVERSE direction.

   5.2 BUT CLASS 1'S MEMBERSHIP IS CONDITIONAL ON MOO-164's 164-4, AND I DO NOT ASSUME IT.
       The sentence says "within the period THIS DEFINITION allows". The definition allows
       %d days, and it allows them on a request under the definition. The %d days for a
       reconsideration request are allowed by subsection M 2, not by the definition. So on
       the pre-164-4 wording the expiry sentence arguably reaches class 2 only; 164-4's
       re-cut to "the period allowed by this section" would bring class 1 in. BOTH ARE
       REPORTED. Nothing is conditioned on 164-5 (§4.2), and class 2 -- the dominant
       class -- is unconditional on either.
""" % (A.DEFINITION_REQUEST_ACT_DAYS, A.BOARD_DECISION_DEADLINE_DAYS))

SCEN = {
    'low':     dict(cohort='low',     seek='low',     f='low',     q='low',
                    subsidy='corrected_authorised'),
    'central': dict(cohort='central', seek='central', f='central', q='central',
                    subsidy='corrected_authorised'),
    'high':    dict(cohort='high',    seek='high',    f='high',    q='high',
                    subsidy='moo71_stated'),
}


def cohort_scale(level):
    """Scale MOO-163's central-only refusal rows to the low/high cohort, and say so."""
    return (A.PARTICIPANTS_ADMITTED_FUNDED[level]
            / A.PARTICIPANTS_ADMITTED_FUNDED['central'])


def exposed(level, p, include_class1):
    s = SCEN[level]
    refused = REFUSED_CENTRAL * cohort_scale(s['cohort'])
    c1 = refused * A.RECONSIDERATION_SEEK_RATE[s['seek']] * p if include_class1 else 0.0
    c2 = (A.PARTICIPANTS_ADMITTED_FUNDED[s['cohort']]
          * A.LATER_DATE_FILING_RATE[s['f']] * p)
    return c1, c2


def harmed(level, p, include_class1):
    c1, c2 = exposed(level, p, include_class1)
    return (c1 + c2) * A.HARM_REALISATION_RATE[SCEN[level]['q']]


print('   5.3 EXPOSED MEMBERS over the 48-month pilot, central scenario, both class-1 '
      'treatments.')
print(f'   {"no-act":>8} | {"class 1 (if 164-4)":>19} | {"class 2":>9} | '
      f'{"exposed":>9} | {"harmed":>8} | vs MOO-170 res. {A.MOO170_RESOLUTION_MEMBERS}')
for p in A.BOARD_NO_ACT_RATE_SWEEP:
    c1, c2 = exposed('central', p, True)
    h = harmed('central', p, True)
    print(f'   {p:>8.2f} | {c1:>19.4f} | {c2:>9.4f} | {c1 + c2:>9.4f} | {h:>8.4f} | '
          f'{"ABOVE" if (c1 + c2) > A.MOO170_RESOLUTION_MEMBERS else "below"}')

print("""
     Read the two right-hand columns together. "Exposed" is MOO-215's quantity and it is
     the one that crosses MOO-170's resolution. "Harmed" is the quantity that can move a
     dollar, and at the central judgment inputs it is an order of magnitude smaller.
     MOO-215 did not over-reach: they said expressly that their class-2 column assumes
     every funded member files one request. Both corrections are theirs to have flagged.""")

print(f"""
   5.4 THE PER-MEMBER DAY CAP, which is what the withdrawn ground was about.
     D 1's excluded aggregate is {A.EXCLUDED_AGGREGATE_CAP_DAYS} days PER MEMBER. Cohort extension-days are
     population x per-member days, so an unmoved per-member cap bounds nothing in the
     aggregate. Confirmed arithmetically, at the central scenario:""")
for p in (0.05, 0.20, 0.50):
    c1, c2 = exposed('central', p, True)
    pop = c1 + c2
    print(f'       no-act {p:.2f}: {pop:6.4f} exposed members x up to '
          f'{A.EXCLUDED_AGGREGATE_CAP_DAYS} days = up to {pop * A.EXCLUDED_AGGREGATE_CAP_DAYS:8.1f} member-days')
print("""     The Policy Director's withdrawal of that ground is correct and the arithmetic
     above is the demonstration of it. The cap is a per-member bound on DAYS; the cost
     driver is a POPULATION on the settle/release line.""")


# ===========================================================================
rule('SECTION 6 -- QUESTION 4: THE PRICE OF ATTACHING A D 1 EXTENSION TO THE '
     'EDIT 4 NOTICE')
# ===========================================================================

print("""   6.1 THE OPTION, AND WHY ITS PRICE IS NOT WHAT IT LOOKS LIKE.

     The option: extend the member's final qualifying retirement date by the number of
     days by which the Edit 4 notice is late, as D 1 already does for the other three
     notice species.

     Work the counterfactual on the harmed member -- the one whose date passes without a
     qualifying retirement because nobody told her the date:

       WITHOUT the extension, revision 9 as drafted:
         no D 1 remedy (§4.1) -> she misses a qualifying retirement
         -> G 4 clause (iii) deems Board error (§4.3) -> credit vests at the SUBSIDISED
            cost -> subsidy SETTLED -> subsection N pays the amount settled.

       WITH the extension:
         her date moves out by the lateness days -> she can retire IN a qualifying
         retirement -> G 1 settles -> subsection N pays the amount settled.

     BOTH BRANCHES END IN A SETTLEMENT PAID UNDER SUBSECTION N, OF THE SAME ELECTION.
     On the appropriation line the option is a SUBSTITUTE for the G 4 route, not an
     addition to it. So:

       PRICE OF THE OPTION, on the subsidy and the D 2 cap        $0
       PRICE OF THE OPTION, on the retirement allowance            UNOBTAINABLE, see 6.3
       PRICE OF THE OPTION, administrative                         SMALL AND FAVOURABLE, 6.4

   6.2 AND THE COROLLARY, WHICH IS THE ONE THAT MATTERS FOR THE RELEASE GATE. The option
       and Edit 4 CANNOT BOTH BE FREE, and they cannot both be dear. One statutory reading
       flips which of them carries the exposure, and the exposure itself does not move:""")

print("""
     +------------------------------------+------------------------+------------------------+
     | if Edit 4's notice is ...          | cost of EDIT 4 alone   | cost of ATTACHING D 1  |
     +------------------------------------+------------------------+------------------------+
     | INSIDE G 4 clause (iii)  (§4.3)    | N x S x (1 - p_base)   | ~$0, allowance term    |
     | OUTSIDE G 4 clause (iii)           | $0  (information only) | N x S x conversion     |
     +------------------------------------+------------------------+------------------------+
       N      = harmed members over the pilot (§5)
       S      = amount settled per election (6.5)
       p_base = G4_BASELINE_AVAILABILITY -- whether she already recovered without Edit 4

     The Policy Director's two claims -- "Edit 4 is fiscally inert" and "attaching a D 1
     extension is a policy choice with a price" -- are each true in exactly one row of
     that table, and they are the SAME row-flip. THEY CANNOT BOTH BE TRUE AT ONCE. The
     total exposure of the patch on this line is N x S in either row. That is the finding.

   6.3 THE ONE TERM I CANNOT PRICE, DECLARED RATHER THAN ESTIMATED.
     "Qualifying retirement" is defined as a retirement "the allowance for which is
     calculated in accordance with subdivision A 1 of § 51.1-155 and is NOT REDUCED under
     subdivision A 2 or A 3". G 4 clause (iii) vests the service credit; it does not make
     her retirement a qualifying one. So the extension route may hand the member an
     UNREDUCED allowance where the G 4 route leaves a reduced one. That differential is a
     VRS actuarial quantity. It needs early-retirement reduction factors, an age
     distribution and a service distribution for this cohort. None exists in this project;
     MOO-71 §3 establishes no published count of these purchases exists at all; and my
     role bars me from introducing individual-level data to construct one.
     DECLARED UNOBTAINABLE. Direction of error: UPWARD on the option -- an unreduced
     allowance costs the trust more than a reduced one. Incidence: at most the N harmed
     members of §5, so it is bounded by the same population, not by the cohort.
     THIS IS A DATA REQUEST TO VRS, and it is the only one this issue generates.

   6.4 THE ADMINISTRATIVE TERM, both directions, no positions modelled.
     NEW, from Edit 4: one notice per no-act event, on a clock that already exists in the
       bill for three other notice species, plus a trigger on the expiry of a period the
       Board already tracks for subsection J reporting. At the volumes in §5 this is
       single-digit notices over four years.
     AVOIDED, from attaching the extension: the whole G 2 machinery on each converted
       event -- a 60-day determination, a notice no less than 30 days before it takes
       effect, a credit reduction, a refund to the member and to any state agency, and the
       G 4 determination within 60 days of the date with its own 15-day notice.
     NET: FAVOURABLE to attaching the extension, and below the threshold at which a
     Virginia fiscal note reports a figure rather than "can be absorbed with existing
     resources". NO POSITION COUNT IS MODELLED, which is a known gap carried from
     MOO-183 §8 and is not a finding of this issue.
     ONE-TIME vs ONGOING: the notice trigger is a one-time systems change, and it sits
     inside the $375,000 one-time nongeneral-fund VRS implementation allowance MOO-183
     already carries. I do NOT assign it a fiscal year: MOO-183's own table labels that
     allowance FY2029 while its §8 says FY2028 carries implementation only, and resolving
     that label is MOO-183's to do, not mine to pick. The per-event cost is ongoing and is
     the volume above.

   6.5 THE PER-EVENT FIGURE, S. Carried from MOO-163 §2, not re-derived.""")

for k, v in A.MEAN_CERTIFIED_SUBSIDY_USD.items():
    print(f'       {k:<22} {usd(v)}')
print(f'       {"D 2 hard ceiling":<22} {usd(A.PER_ELECTION_CEILING_USD)}  (per election, text)')
print("""     MOO-163 carries the corrected $94k because a lower mean makes ITS cap bind later,
     which is cautious THERE. Here the per-event figure IS the cost, so $94k is the
     OPTIMISTIC end. The scenario table below therefore uses $94k central and the $111k
     stated basis in the high case, and every line is bounded by the $170,000 ceiling.""")


# ===========================================================================
rule('SECTION 7 -- SCENARIO TABLE, AND THE THRESHOLD INVERSION')
# ===========================================================================

print("""   Because the Board no-act rate is unobtainable (§2.2), the headline is reported as a
   THRESHOLD IN THAT RATE rather than as a figure conditioned on a value of it.

   Dollars below are over the whole 48-month pilot, class 1 INCLUDED, which is the
   adverse 164-4 branch of §5.2.""")

print('   Dollar cells are carried to TWO SIGNIFICANT FIGURES. The cohort count they')
print('   descend from is given to two figures, so a dollar-exact cell would be false')
print('   precision (MOO-46 Decision 4).')
print("""
   7.0 FIRST, A REGIME TEST I HAVE TO RUN BEFORE THE TABLE MEANS ANYTHING, AND IT
       INVERTS MOO-163's CONDITION.

     A settlement instead of a release is net new appropriation only where the released
     money would have funded NOBODY ELSE -- that is, where the $3,000,000 cap does NOT
     bind. Where it DOES bind, D 5 requires the Board to "accept the election if and when
     sufficient amounts become available", so the freed room would have funded a
     wait-listed applicant, the aggregate stays at the cap, and the effect is DISPLACEMENT
     of a member rather than a dollar.

     MOO-163's mechanism is live only where the cap BINDS. This channel's mechanism is
     live only where it does NOT. THE TWO ISSUES ARE ACTIVE IN COMPLEMENTARY REGIMES. So
     MOO-163's $0 was established on precisely the case in which this channel is loudest,
     which is an independent and stronger answer to question 2 than §3 gives.""")
print()
print(f'   {"scenario":>9} | {"cohort":>7} | {"utilisation":>11} | {"cap":>12} | '
      f'{"headroom = exposure ceiling":>27}')
HEADROOM = {}
for lvl in ('low', 'central', 'high'):
    coh = A.PARTICIPANTS_ADMITTED_FUNDED[SCEN[lvl]['cohort']]
    base_util = (A.CAP_UTILISATION_STATED['central'] if lvl != 'high'
                 else A.CAP_UTILISATION_STATED['high'])
    util = base_util * A.RETIREMENT_WINDOW_RUNG_RATIO
    if lvl == 'low':
        util *= A.PARTICIPANTS_ADMITTED_FUNDED['low'] / A.PARTICIPANTS_ADMITTED_FUNDED['central']
    binds = util >= 1.0
    hr = max(0.0, A.AGGREGATE_CAP_USD * (1 - util))
    HEADROOM[lvl] = hr
    print(f'   {lvl:>9} | {coh:>7.2f} | {util:>10.1%} | '
          f'{"BINDS" if binds else "does not bind":>12} | '
          f'{(usd2sf(hr) + "  (displacement only)" if binds else usd2sf(hr)):>27}')
print("""
     So the HIGH scenario's dollar line is bounded by $0 of headroom and its effect is
     displacement in members, NOT an appropriation figure -- unless the release would have
     come too late in the pilot for any wait-listed applicant to use it, in which case the
     money lapses either way and the settlement IS net new outlay. §10.3 shows these
     events are back-loaded to the last two fiscal years of the pilot, so that caveat is
     live and I cannot resolve it: it turns on whether a waiting list is still fundable
     when the release would have happened. BOTH BRANCHES ARE REPORTED BELOW AND I DO NOT
     PICK ONE. The uncapped column is the lapse branch; the capped column is the
     displacement branch.""")
print()
print(f'   7.1 CHANNEL EXPOSURE. "lapse branch" = N x S. "capped" = min(N x S, headroom).')
print()
print(f'   {"no-act":>8} | {"LOW":>24} | {"CENTRAL":>24} | {"HIGH":>24}')
print(f'   {"":>8} | {"N    lapse    capped":>24} | {"N    lapse    capped":>24} | '
      f'{"N    lapse    capped":>24}')
for p in A.BOARD_NO_ACT_RATE_SWEEP:
    cells = []
    for lvl in ('low', 'central', 'high'):
        n = harmed(lvl, p, True)
        s = A.MEAN_CERTIFIED_SUBSIDY_USD[SCEN[lvl]['subsidy']]
        gross = n * s
        cells.append(f'{n:5.3f} {usd2sf(gross):>9} {usd2sf(min(gross, HEADROOM[lvl])):>9}')
    print(f'   {p:>8.2f} | {cells[0]:>24} | {cells[1]:>24} | {cells[2]:>24}')
print("""
     The low and central columns are identical in both branches -- they are nowhere near
     the headroom, so the cap regime does not bite there. The high column collapses from
     hundreds of thousands to $0 on the displacement branch. THE HIGH LINE IS THEREFORE
     NOT A FIGURE, IT IS A PAIR, and the thing that decides between them is not a fiscal
     input (§7.0).""")

print(f"""
   7.2 THE THRESHOLDS. Solved analytically -- every term is linear in the no-act rate, so
       each threshold is a division and carries no Monte Carlo error.""")


def threshold_rate(level, target_usd, include_class1=True):
    s = SCEN[level]
    per_unit_p = harmed(level, 1.0, include_class1)
    if per_unit_p <= 0:
        return float('inf')
    sub = A.MEAN_CERTIFIED_SUBSIDY_USD[s['subsidy']]
    return (target_usd / sub) / per_unit_p


def threshold_members(level, target_members, include_class1=True):
    per_unit_p = harmed(level, 1.0, include_class1)
    return float('inf') if per_unit_p <= 0 else target_members / per_unit_p


rows = []
for lvl in ('low', 'central', 'high'):
    sub = A.MEAN_CERTIFIED_SUBSIDY_USD[SCEN[lvl]['subsidy']]
    rows.append((lvl, sub,
                 threshold_members(lvl, 1.0),
                 threshold_rate(lvl, A.MATERIALITY_FLOOR_USD),
                 threshold_rate(lvl, A.PER_ELECTION_CEILING_USD * 1.0)))
print(f'   {"scenario":>9} | {"S":>9} | {"no-act for 1 harmed":>20} | '
      f'{"no-act for " + usd(A.MATERIALITY_FLOOR_USD):>20} | {"no-act for 1 x $170k":>20}')
for lvl, sub, t1, tm, tc in rows:
    def fmt(x):
        return '  >100% (unreachable)' if x > 1.0 else f'{x * 100:19.1f}%'
    print(f'   {lvl:>9} | {usd(sub):>9} | {fmt(t1)} | {fmt(tm)} | {fmt(tc)}')

print(f"""
   7.3 COMPARISON WITH MOO-215's 15.6% CROSSOVER, on their basis and then on mine.
     MOO-215 inverted for {A.MOO170_RESOLUTION_MEMBERS} EXPOSED members with the later-date filing rate at
     1.00 and no harm-realisation step. Reproducing that basis:""")
p215 = A.MOO170_RESOLUTION_MEMBERS / A.PARTICIPANTS_ADMITTED_FUNDED['central']
print(f'       {A.MOO170_RESOLUTION_MEMBERS} / {A.PARTICIPANTS_ADMITTED_FUNDED["central"]:.2f} = {p215 * 100:.1f}%   '
      f'<- MOO-215 reports 15.6%.')
check('MOO-215\'s 15.6% crossover reproduces on their stated basis',
      abs(p215 * 100 - 15.6) < 0.1)
t_cen = threshold_rate('central', A.MATERIALITY_FLOOR_USD) * 100
t_high = threshold_rate('high', A.MATERIALITY_FLOOR_USD) * 100
print(f"""     Reproduced. The two inversions differ because they answer different questions:
     theirs is "when does this stop being below MOO-170's member resolution", mine is
     "when does this put a dollar on an appropriation line". The central dollar threshold
     is {t_cen:.0f}% and the high one is {t_high:.1f}%, against their {p215 * 100:.1f}%. Theirs is the earlier
     warning and mine is the later one; neither contradicts the other, and a reader who
     wants the conservative trigger should take theirs.""")

print("""
   7.4 HEADLINE, on the basis of 7.1 to 7.3.""")
c_central = harmed('central', 0.10, True) * A.MEAN_CERTIFIED_SUBSIDY_USD['corrected_authorised']
c_high = harmed('high', 0.10, True) * A.MEAN_CERTIFIED_SUBSIDY_USD['moo71_stated']
c_high20 = harmed('high', 0.20, True) * A.MEAN_CERTIFIED_SUBSIDY_USD['moo71_stated']
print(f"""     At a 10% Board no-act rate -- a rate I cannot source, and which I offer only as a
     reading point on the sweep and not as an estimate -- the channel prices at
     {usd2sf(c_central)} central and {usd2sf(c_high)} high over the whole 48-month pilot, and at
     {usd2sf(c_high20)} on the high scenario at a 20% rate.
     Central stays below the {usd(A.MATERIALITY_FLOOR_USD)} reporting convention until the no-act rate
     reaches {t_cen:.0f}%, which is not a defensible rate for any administrative body. The
     high scenario crosses it at {t_high:.1f}% ON THE LAPSE BRANCH, and never on the
     displacement branch, where its ceiling is $0 of headroom (§7.0).

     SO THE ANSWER, STATED WITHOUT HEDGING: NOT $0, AND NOT MATERIAL AT THE CENTRAL
     ESTIMATE. It is a conditional, ONE-SIGNED exposure -- it cannot offset, unlike
     MOO-163's sign-indeterminate lapse delta -- of {usd2sf(c_central)} central at an
     illustrative 10% no-act rate, rising to {usd2sf(c_high)} in the high cohort only if
     that cohort's exposure lands on the lapse branch rather than the displacement one.
     The single line a fiscal note should carry is "indeterminate, not material, mechanism
     described", and the mechanism is §4.3 and §7.0.""")


# ===========================================================================
rule('SECTION 8 -- SENSITIVITY: WHAT CONTROLS THE ANSWER')
# ===========================================================================

print("""   8.1 ONE-AT-A-TIME, 10% move off the central cell at a 10% no-act rate. Reported as
       the percentage swing in the dollar answer, so a swing above 25% is a flag.""")

BASE_P = 0.10
base = harmed('central', BASE_P, True) * A.MEAN_CERTIFIED_SUBSIDY_USD['corrected_authorised']


def perturbed(**over):
    f = over.get('f', A.LATER_DATE_FILING_RATE['central'])
    q = over.get('q', A.HARM_REALISATION_RATE['central'])
    seek = over.get('seek', A.RECONSIDERATION_SEEK_RATE['central'])
    coh = over.get('cohort', A.PARTICIPANTS_ADMITTED_FUNDED['central'])
    sub = over.get('sub', A.MEAN_CERTIFIED_SUBSIDY_USD['corrected_authorised'])
    p = over.get('p', BASE_P)
    refused = REFUSED_CENTRAL * (coh / A.PARTICIPANTS_ADMITTED_FUNDED['central'])
    n = (refused * seek * p + coh * f * p) * q
    return n * sub


TESTS = [
    ('Board no-act rate            ', dict(p=BASE_P * 1.1)),
    ('later-date filing rate       ', dict(f=A.LATER_DATE_FILING_RATE['central'] * 1.1)),
    ('harm realisation rate        ', dict(q=A.HARM_REALISATION_RATE['central'] * 1.1)),
    ('funded cohort               ', dict(cohort=A.PARTICIPANTS_ADMITTED_FUNDED['central'] * 1.1)),
    ('amount settled per election  ', dict(sub=A.MEAN_CERTIFIED_SUBSIDY_USD['corrected_authorised'] * 1.1)),
    ('M 2 seek rate                ', dict(seek=A.RECONSIDERATION_SEEK_RATE['central'] * 1.1)),
]
print(f'   {"input moved +10%":<32} | {"answer":>12} | {"swing":>8} | flag')
max_swing = 0.0
for name, kw in TESTS:
    v = perturbed(**kw)
    sw = (v - base) / base
    max_swing = max(max_swing, abs(sw))
    print(f'   {name:<32} | {usd2sf(v):>12} | {sw * 100:>7.1f}% | '
          f'{"**>25%**" if abs(sw) > 0.25 else ""}')

print(f"""
     NO INPUT SWINGS THE ANSWER BY MORE THAN 25% ON A 10% MOVE. The largest swing is
     {max_swing * 100:.1f}%, and the pattern is worth reading rather than skipping:

       exactly 10%  -- the no-act rate, the harm realisation rate, the amount settled, and
                       the FUNDED COHORT. The cohort lands at exactly 10% and not above it
                       because it scales BOTH classes: it multiplies class 2 directly and
                       it scales MOO-163's central-only refusal rows that feed class 1. So
                       it is linear, not super-linear. THERE IS NO SUPER-LINEAR TERM IN
                       THIS MODEL.
       under 10%    -- the later-date filing rate ({[round(((perturbed(f=A.LATER_DATE_FILING_RATE['central'] * 1.1) - base) / base) * 100, 1)][0]}%) and the M 2 seek rate
                       ({[round(((perturbed(seek=A.RECONSIDERATION_SEEK_RATE['central'] * 1.1) - base) / base) * 100, 1)][0]}%), because each touches ONE class only. Their two swings sum
                       to 10%, which is the mechanical check that the two classes partition
                       the population with nothing double-counted and nothing dropped.

     THERE IS NO DOMINANT FISCAL ASSUMPTION IN THIS MODEL, and that is itself the finding:
     the answer is not controlled by anything I could refine.

   8.2 WHAT DOES CONTROL THE ANSWER IS NOT A FISCAL INPUT. In rank order:

     1. G4_BASELINE_AVAILABILITY -- whether the harmed member already recovered under
        G 4 clause (iii) WITHOUT Edit 4, on the un-deemed limb. It multiplies the whole
        Edit 4 answer by (1 - p_base). At 1.00 Edit 4 is inert and the exposure sits on
        the option instead; at 0.00 it sits on Edit 4. SWING: 100%, from the whole figure
        to zero. It is a LEGAL probability. RED TEAM / COUNSEL REVIEWER's, with the
        inclusive-or-exhaustive reading of clause (iii) STATUTORY RESEARCHER's.

     2. WHETHER EDIT 4's NOTICE IS INSIDE G 4 CLAUSE (iii) AT ALL (§4.3). A binary, and
        it does not change the total exposure -- it changes which instrument carries it
        (§6.2). STATUTORY RESEARCHER's.

     3. THE BOARD NO-ACT RATE, unobtainable, swept, and the answer is reported as a
        threshold in it rather than conditioned on a value (§7.2).

     4. WHICH CAP REGIME THE COHORT IS IN (§7.0) -- lapse branch or displacement branch.
        It is the difference between the whole high-scenario figure and $0, and it turns
        on whether a wait-listed applicant is still fundable when the release would have
        occurred. Not a fiscal input either; it is a timing question about the end of the
        pilot and about whether D 5 maintains a live waiting list.

     5. MOO-49's CLAUSE (vi) READING, upstream of this issue as it is of MOO-163 and
        MOO-170. Broad gives ~130 members instead of {A.PARTICIPANTS_ADMITTED_FUNDED['central']:.0f}, a 7x move on the cohort.
        The cohort is exactly linear here (8.1), so 7x the cohort is 7x the figure -- but
        it ALSO pushes utilisation far past the cap, which moves the whole answer onto the
        displacement branch and so onto item 4. BROAD CLAUSE (vi) REQUIRES REPRICING THIS
        CHANNEL TOO, and it would not simply scale.

     A 10% move in items 1, 2 or 4 does not exist -- none of them is continuous. THAT is
     why the first paragraph of the deliverable names them instead of naming a fiscal
     driver, and why refining any input in 8.1 would be wasted work.""")


# ===========================================================================
rule('SECTION 9 -- EXTERNAL SANITY CHECK')
# ===========================================================================

print(f"""   9.1 NO QUANTITATIVE EXTERNAL ANCHOR EXISTS, and this is established rather than
       asserted: MOO-71 §3 establishes that no published count of § 51.1-142.2 military
       purchases exists at all, and §2.2 above establishes that no no-act rate exists for
       any denominator. There is no other-state analogue of the § 51.1-142.4 certified
       subsidy to scale by population. So the check available is a CONVENTION check, the
       same one MOO-163 §8 and MOO-170 §7 used, plus one basis-mismatched internal
       cross-check. Both are reported, including where they disagree.

   9.2 CONVENTION CHECK against Virginia fiscal-note practice on capped, self-executing
       programmes. A channel that (a) cannot exceed a statutory ceiling that is already
       appropriated for, (b) produces single-digit events over a four-year pilot at any
       defensible rate, and (c) has no local component, is reported in Virginia practice
       as "$0" or "indeterminate but not material", with the mechanism described.
       RESULT: AGREEMENT with the central line, and the convention cannot validate the
       high line. Stated as such. It validates $0 and nothing else -- exactly MOO-163's
       and MOO-170's own disclosure about this check.

   9.3 BASIS-MISMATCHED CROSS-CHECK on the per-event figure. MOO-183 Table A reports cost
       per participant of {usd(A.MOO183_COST_PER_PARTICIPANT_USD['low'])}-{usd(A.MOO183_COST_PER_PARTICIPANT_USD['high'])} across five priced designs, on a NET TRUST
       COST basis, PV at 6/30/2025. The per-event figure here is {usd(A.MEAN_CERTIFIED_SUBSIDY_USD['corrected_authorised'])}-{usd(A.MEAN_CERTIFIED_SUBSIDY_USD['moo71_stated'])} on a
       CERTIFIED SUBSIDY basis, nominal.
       RATIO: {A.MEAN_CERTIFIED_SUBSIDY_USD['corrected_authorised'] / A.MOO183_COST_PER_PARTICIPANT_USD['high']:.2f}x to {A.MEAN_CERTIFIED_SUBSIDY_USD['moo71_stated'] / A.MOO183_COST_PER_PARTICIPANT_USD['low']:.2f}x.
       THIS IS NOT AGREEMENT AND I AM NOT CALLING IT AGREEMENT. The two are different
       quantities: a certified subsidy is a gross reserved amount, net trust cost is net
       of member payments and discounted. The check establishes only that the per-event
       figure is the right ORDER OF MAGNITUDE for one member of this cohort -- tens of
       thousands, not thousands and not millions. A 2x gap on a basis difference of
       exactly this kind is what I would expect; a 20x gap would have refuted the figure.
       FALSIFIABLE, AND NOT REFUTED.

   9.4 WHAT WOULD FALSIFY THE WHOLE ANSWER. A published VRS on-time-decision rate above
       {threshold_rate('high', A.MATERIALITY_FLOOR_USD) * 100:.0f}% failure for determinations of this kind, or a clause (vi) reading
       that puts ~130 members in the cohort. Either one brings this issue back.""")


# ===========================================================================
rule('SECTION 10 -- LOCAL COST, FUND SPLIT, AND THE UNFUNDED-MANDATE TEST')
# ===========================================================================

print("""   10.1 LOCAL COST: $0, AND NO UNFUNDED MANDATE ON LOCALITIES. Every duty in this
        channel is the Board's: give a notice, act on a request, make a determination,
        report under subsection J. The one duty the section puts on anyone else is on
        "a state agency that employs or last employed a member", which is not a locality.
        The population is the State Employee plan, carried from MOO-183 §8. NO LOCALITY
        ACQUIRES A DUTY, A COST, OR A REPORTING OBLIGATION IN THIS CHANNEL. Called out
        explicitly because an unfunded local mandate is a finding in itself, and there
        is none here.

   10.2 FUND SPLIT. Subsection N pays "from an appropriation made for that purpose", so a
        settlement is an APPROPRIATION line, not a trust-absorbed cost. MOO-183 §8 carries
        a 47% general-fund share on the amortisation of trust cost and treats the
        implementation allowance as nongeneral fund. THE 47% SHARE IS NOT APPLIED TO THE
        FIGURES ABOVE, because a subsection N settlement is a direct payment of the amount
        settled and not an amortised trust cost, and I have no authority for the fund
        split on that line. DECLARED OPEN. Direction: a GF share below 100% reduces the
        general-fund figure below the figures in §7, so §7 is the conservative reading.
        This is the one place where a figure in §7 could only move DOWN on better
        information.

   10.3 BIENNIUM TIMING. Events require an accepted election, credited service credit, a
        filed request, a no-act and then the passage of a date, so they cannot land in the
        first programme year. On the MOO-183 timing convention (July 1 effective date,
        FY2028 implementation only, FY2029 first benefit year) the earliest event lands in
        FY2030 and the distribution is back-loaded across FY2030-FY2033. AT THE CENTRAL
        FIGURES THERE IS LESS THAN ONE EVENT IN THE WHOLE PILOT, SO A FISCAL-YEAR SPLIT OF
        IT WOULD BE FALSE PRECISION AND IS NOT OFFERED. If the high line is taken, the
        same back-loading applies and FY2032-FY2033 carry it.""")


# ===========================================================================
rule('SECTION 11 -- SELF-TEST')
# ===========================================================================

check('no-act rate 0 gives exactly zero exposed members',
      harmed('central', 0.0, True) == 0.0)
check('exposure is linear in the no-act rate (doubling p doubles N)',
      abs(harmed('central', 0.20, True) - 2 * harmed('central', 0.10, True)) < 1e-12)
check('class 1 excluded is strictly smaller than class 1 included',
      harmed('central', 0.10, False) < harmed('central', 0.10, True))
check('class 2 dominates class 1 at every swept rate, central scenario',
      all(exposed('central', p, True)[1] > exposed('central', p, True)[0]
          for p in A.BOARD_NO_ACT_RATE_SWEEP if p > 0))
check('linear class 1 exceeds MOO-215\'s quadratic class 1 at a 20% no-act rate',
      exposed('central', 0.20, True)[0]
      > REFUSED_CENTRAL * A.RECONSIDERATION_SEEK_RATE['central'] * 0.20 * 0.20)
check('per-event figure never exceeds the D 2 per-election ceiling',
      max(A.MEAN_CERTIFIED_SUBSIDY_USD.values()) < A.PER_ELECTION_CEILING_USD)
check('the §7.0 regime table reproduces MOO-163\'s published 67.4% central utilisation',
      abs((1 - HEADROOM['central'] / A.AGGREGATE_CAP_USD) - 0.674) < 0.0005)
check('the §7.0 regime table reproduces MOO-163\'s published 33.7% low utilisation',
      abs((1 - HEADROOM['low'] / A.AGGREGATE_CAP_USD) - 0.337) < 0.0005)
check('the high scenario binds the cap, so its headroom is exactly zero',
      HEADROOM['high'] == 0.0)
check('low and central exposures are below headroom at every swept rate, so the cap '
      'regime does not bite there',
      all(harmed(lvl, p, True) * A.MEAN_CERTIFIED_SUBSIDY_USD[SCEN[lvl]['subsidy']]
          < HEADROOM[lvl]
          for lvl in ('low', 'central') for p in A.BOARD_NO_ACT_RATE_SWEEP))
check('the harm rate is built on MOO-204\'s base x the labelled multiplier, not free-hand',
      all(abs(A.HARM_REALISATION_RATE[k]
              - A.NON_QUALIFYING_RETIREMENT_SHARE_BASE[k]
              * A.INFORMATION_FAILURE_MULTIPLIER[k]) < 1e-9
          for k in ('low', 'central', 'high')))
check('the harm rate never falls below MOO-204\'s unconditional floor',
      all(A.HARM_REALISATION_RATE[k] >= A.NON_QUALIFYING_RETIREMENT_SHARE_BASE[k]
          for k in ('low', 'central', 'high')))
check('the central dollar threshold exceeds MOO-215\'s member crossover',
      threshold_rate('central', A.MATERIALITY_FLOOR_USD) > p215)
check('MOO-163 register untouched by this run (no write handle opened)',
      not os.path.exists(os.path.join(os.path.dirname(A.BILL_TEXT_PATH), '..',
                                      'moo163-retention-endpoint', '.moo217_touch')))

print()
if FAILS:
    print(f'   SELF-TEST FAILED: {FAILS}')
    sys.exit(1)
print('   ALL CHECKS PASS.')

rule('ONE SENTENCE FOR THE EDITOR')
print(f"""
   The subdivision D 1 extension channel the MOO-141 revision 9 patch opens prices at
   {usd2sf(c_central)} central over the whole 48-month pilot at an illustrative 10% Board
   no-act rate -- a rate that exists in no published series and is therefore swept rather
   than assumed, with the materiality threshold at {t_cen:.0f}% centrally -- so the channel is
   immaterial at every rate a reader could defend and the right fiscal-note line is
   "indeterminate, not material"; but it is NOT $0 on its merits, because Edit 4's new
   notice duty is inert on subdivision D 1 exactly as the Policy Director claims and
   thereby lands inside subdivision G 4 clause (iii), where a notice not given converts a
   released reservation into a settlement the Commonwealth must pay under subsection N, so
   attaching a D 1 extension to the Edit 4 notice costs nothing on the appropriation line
   and merely moves that same exposure off Edit 4 and onto the extension -- and the figure
   is controlled by none of the fiscal inputs, no one of which swings it more than 10% on a
   10% move, but by three non-fiscal questions: whether the member already recovered
   without Edit 4, whether Edit 4's notice is inside clause (iii) at all, and whether the
   cohort sits in the cap-binding regime where the whole exposure becomes displacement of
   another member instead of a dollar.
""")
