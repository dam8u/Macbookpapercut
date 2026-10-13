"""
MOO-217 — assumption register for the subdivision D 1 extension channel that the
MOO-141 revision 9 patch opens, and for the Edit 4 notice.

EVERY number the model uses appears in this file, once, with a unit, a source and a
direction of error. There are no magic numbers in moo217_d1_channel.py.

The MOO-163 register is IMPORTED UNCHANGED (section B below re-exports it). Nothing in
`../moo163-retention-endpoint/moo163_inputs.py` is edited, and nothing is written to the
MOO-163 or MOO-170 directories.

Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.
No figure here is a VRS actuarial result.
Nothing is reliable beyond two significant figures (MOO-46 Decision 4).

Retrieval date for every Paperclip-internal source below: 12 October 2026.
"""

import os
import sys

# ---------------------------------------------------------------------------
# A. PATHS AND VINTAGE
# ---------------------------------------------------------------------------

_HERE = os.path.dirname(os.path.abspath(__file__))

BILL_TEXT_PATH = os.path.join(_HERE, '..', 'moo141-rev72', 's1.txt')
BILL_TEXT_CHARS = 134_012
BILL_DOC_CHARS = 502_586
# source: the ENACTED §1 EXTRACT (134,012 characters) of document key `bill-text-s8`
#   at store revision 72 (502,586 characters whole), which is the cut MOO-141 revision 9
#   is written against. Record: `moo141-rev72/live-meta.json`, latestRevisionId
#   368f5e41-56ab-4138-8bda-8553ae8eab04. The extract carries the whole of the new
#   § 51.1-142.4, which is where every provision this issue touches lives.
# NOTE ON NAMING, because two issues in this project use the label "G 4" for different
#   things: every reference below to G 1, G 2, G 4 or clause (iii) is to a subdivision of
#   subsection G of the NEW § 51.1-142.4. MOO-204's "G 4 aggregate, 120 days" is the
#   non-running proviso in a later part of that same subdivision, not clause (iii).
# direction of error: none. It is text. If the store moves, BILL_TEXT_CHARS fails the
#   §0 assertion and the screens in §4 are string tests, so they fail loudly not quietly.

BILL_STORE_REVISION = 72
PATCH_REVISION = 9
PATCH_EDIT_COUNT = 4
PATCH_CHARS_ADDED = 1_716
# source: MOO-141 record `moo141-rev72-revision9`, §1 and §6.

sys.path.insert(0, os.path.join(_HERE, '..', 'moo163-retention-endpoint'))
import moo163_inputs as R163  # noqa: E402  imported unchanged, never written to

# ---------------------------------------------------------------------------
# B. IMPORTED UNCHANGED FROM MOO-163 — re-exported here so the reader can see
#    exactly which MOO-163 levers this issue leans on, without copying values.
# ---------------------------------------------------------------------------

AGGREGATE_CAP_USD = R163.AGGREGATE_CAP_USD                   # $3,000,000, D 2
PER_ELECTION_CEILING_USD = R163.PER_ELECTION_CEILING_USD     # $170,000, D 2
CONTINGENCY_RATE = R163.CONTINGENCY_RATE                     # [20]%, D 3
PILOT_LENGTH_MONTHS = R163.PILOT_LENGTH_MONTHS               # 48 months
BOARD_DECISION_DEADLINE_DAYS = R163.BOARD_DECISION_DEADLINE_DAYS  # 90 days, M 2
PARTICIPANTS_ADMITTED_FUNDED = R163.PARTICIPANTS_ADMITTED_FUNDED   # 8.97/17.93/29.89
STATUTORY_REFUSALS_CENTRAL = R163.STATUTORY_REFUSALS_CENTRAL
RECONSIDERATION_SEEK_RATE = R163.RECONSIDERATION_SEEK_RATE   # 0.15/0.35/0.60, judgment
CAP_UTILISATION_STATED = R163.CAP_UTILISATION_STATED
RETIREMENT_WINDOW_RUNG_RATIO = R163.RETIREMENT_WINDOW_RUNG_RATIO

# ---------------------------------------------------------------------------
# C. NEW STATUTORY PARAMETERS — read off BILL_TEXT_PATH directly. These are text,
#    not estimates. Direction of error: none, unless the text moves again.
# ---------------------------------------------------------------------------

DEFINITION_REQUEST_ACT_DAYS = 30
# unit: days from the filing of a request under the definition of "final qualifying
#   retirement date".
# source: the definition, subsection A — "the Board shall act upon such a request, and
#   shall give the member written notice of its determination and of the reasons for it,
#   no later than 30 days after the request is filed".
# NOTE: this is the "period allowed" that Edit 4's notice clock hangs off. It is 30 days,
#   NOT the 90 days of M 2. The two classes have different periods.

EDIT4_NOTICE_DAYS = 15
# unit: days after the expiration of the period for acting upon the request.
# source: MOO-141 revision 9 Edit 4 — "no later than 15 days after the expiration of the
#   period for acting upon the request referred to in that sentence". Drafted, not enacted.

MAILING_EXTENSION_DAYS = 3
# unit: days. source: subdivision D 1 — "where the Board mails the statement or notice,
#   every period that runs from the giving of it is extended by three days".
# direction of error: none; it lengthens every downstream period by three days and is
#   carried so the day arithmetic is not optimistic.

EXCLUDED_AGGREGATE_CAP_DAYS = 365
# unit: days per member (12 months).
# source: the definition — "this sentence does not apply to an extension under subdivision
#   D 1 by reason of a statement or notice given later than the time required by this
#   definition, and the aggregate of all extensions so excluded shall not exceed 12
#   months". THIS IS THE CAP THE POLICY DIRECTOR'S WITHDRAWN GROUND RELIED ON. It is per
#   member. It bounds days, not members, and not dollars.

LATER_DATE_MAX_MONTHS = 3
# unit: months after the first-sentence date. source: the definition — "shall be not more
#   than three months after the date determined under the first sentence".

G2_DETERMINATION_DAYS = 60
G2_NOTICE_MIN_DAYS = 30
# unit: days. source: subdivision G 2 — the 60-day determination period and the "no less
#   than 30 days ... before the determination takes effect" notice.

N_PAYMENT_DAYS = 60
# unit: days after settlement. source: subsection N — "the Commonwealth shall pay the
#   amount settled to the retirement system from an appropriation made for that purpose,
#   no later than 60 days after the settlement".
# THIS IS THE LINE THE CHANNEL LANDS ON. A G 1 or G 4 settlement is an appropriation
#   outlay. A G 2 release is not.

# ---------------------------------------------------------------------------
# D. PER-EVENT MONEY — the value of one conversion of a release into a settlement.
#    Carried from MOO-163's own derivation, not re-derived.
# ---------------------------------------------------------------------------

MEAN_CERTIFIED_SUBSIDY_USD = {
    "corrected_authorised": 94_000,   # $3.00M x 0.674 / 1.2 / 17.93, MOO-163 §2
    "moo71_stated": 111_000,          # $3.00M x 0.793 / 1.2 / 17.93, MOO-163 §2
    "moo48_pathway_a": 110_042,       # MOO-48 Pathway A mean, MOO-163 §2 cross-check
}
# unit: dollars per election.
# source: MOO-163 Section 2, carried as given. MOO-163 carries the corrected $94k because
#   it is the authorised 12-month rung; the $111k line is the stated basis and the
#   $110,042 is the independent MOO-48 figure the $111k line validates to 0.5%.
# direction of error: the corrected figure is the LOW end of the three. Carrying it is the
#   cautious direction for MOO-163 (a lower mean lets more members fit, so the cap binds
#   later) but it is the OPTIMISTIC direction here, because here the per-event figure is
#   the cost itself. So this model reports the band $94k-$111k and bounds it at $170k.

# ---------------------------------------------------------------------------
# E. THE TWO MISSING INPUTS — question 1. Neither exists in any register in this
#    project. Neither is assumed. Both are SWEPT, and the model inverts for the
#    threshold instead of guessing a value.
# ---------------------------------------------------------------------------

BOARD_NO_ACT_RATE_SWEEP = (0.00, 0.01, 0.02, 0.05, 0.10, 0.20, 0.35, 0.50)
# unit: fraction of requests on which the Board does not act within the period allowed.
# source: NONE. UNOBTAINABLE on existing inputs, and declared as such in §2:
#   - VRS publishes no on-time-decision rate for § 51.1-142.2 purchase determinations.
#   - MOO-71 §3 establishes that NO published count of § 51.1-142.2 military purchases
#     exists at all, so the denominator of such a rate does not exist either.
#   - The bill itself would create the data prospectively (subsection J requires the Board
#     to report every failure to act and every delay), which is evidence that the figure
#     is not currently collected.
#   - No prior Virginia fiscal impact statement in this project's record carries a VRS
#     no-act rate, and no register in this project carries one (verified mechanically
#     in §2 by scanning the MOO-163 and MOO-170 registers).
# direction of error: not applicable. It is swept, and the answer is reported as a
#   threshold in this variable rather than as a point estimate conditioned on it.

LATER_DATE_FILING_RATE = {"low": 0.05, "central": 0.20, "high": 0.60}
# unit: fraction of the funded cohort who file at least one written request for a later
#   final qualifying retirement date under the definition, over the 48-month pilot.
# source: ANALYST JUDGMENT, and the judgment is bounded on one side by text, not data:
#   - UPPER structural bound is 1.00 and MOO-215 used exactly 1.00. That assumption says
#     every funded member files one such request, which over-counts and MOO-215 says so.
#   - The definition confines the ground to where "the Board's own processing
#     requirements, or any other cause not attributable to the member, make the member's
#     retirement on or before the date that would otherwise apply ... impracticable", and
#     confines the relief to not more than three months. A member with no such cause has
#     nothing to ask for. The Board may also approve a later date "on its own initiative",
#     which removes the need to file in the very cases most likely to have a cause.
#   - Against that, filing is costless, may be done "at any time before the date that
#     would otherwise apply", and D 1 requires the Board to tell the member about the
#     mechanism in the written statement, which is strong prompting.
#   I would defend 5%-60%. I would not defend MOO-215's 1.00 as a central case, and I
#   would not defend 0.
# direction of error: symmetric, and the result is LINEAR in it, so a 10% move in this
#   input moves the answer 10%. It is the second-ranked driver.

NON_QUALIFYING_RETIREMENT_SHARE_BASE = {"low": 0.02, "central": 0.05, "high": 0.15}
# unit: fraction of FUNDED participants who do not retire in a qualifying retirement and
#   so reach a subdivision G 2 cutback determination. UNCONDITIONAL base rate.
# source: MOO-204 register `moo204-164-9/moo204_inputs.py`, NON_QUALIFYING_RETIREMENT_SHARE,
#   carried as given and NOT re-derived. MOO-204 labels it analyst judgment grounded on
#   MOO-140 §3.2's four narrowing grounds, with the hard bound that the class cannot
#   exceed the funded participant count.
# WHY IT IS HERE: this issue's harm rate is the SAME event conditioned on the Board's
#   silence. An unconditional base rate is a floor on a conditional rate whose condition
#   can only make the event more likely. So this anchors the floor and the figure below is
#   a MULTIPLIER on a prior analyst-judgment figure, not a free-standing guess.

INFORMATION_FAILURE_MULTIPLIER = {"low": 5.0, "central": 5.0, "high": 3.3}
# unit: dimensionless, applied to NON_QUALIFYING_RETIREMENT_SHARE_BASE.
# source: ANALYST JUDGMENT, and this is the only free parameter in the harm rate. It is
#   the factor by which not being told your statutory retirement date raises the chance
#   you miss it. I would defend 2x to 8x and I have no source for any value in that band.
#   The high case uses the SMALLER multiplier because the base it multiplies is already
#   3x the central base; using 5.0 there would carry the high case to 75%, which I would
#   not defend against the two mitigating textual facts below.
# direction of error: symmetric. A 10% move here moves the answer 10%.

HARM_REALISATION_RATE = {
    k: round(NON_QUALIFYING_RETIREMENT_SHARE_BASE[k] * INFORMATION_FAILURE_MULTIPLIER[k], 4)
    for k in ("low", "central", "high")
}
# unit: fraction of no-act events in which the member's final qualifying retirement date
#   actually passes without a qualifying retirement, GIVEN that the Board did not act and
#   did not give the notice. DERIVED: base x multiplier = 0.10 / 0.25 / 0.495.
# MOO-215 implicitly set this to 1.00 by counting exposed members rather than harmed
#   members. 1.00 over-counts for two textual reasons:
#   - the expiry sentence is PROTECTIVE. It moves the member's date to "the first day of
#     the second month following the month in which that period expired", and applies only
#     where the date that would otherwise apply is EARLIER. So the no-act case hands the
#     member at least a further month and a fraction, counted in §5.
#   - a member who has filed a request and heard nothing by the end of the period has both
#     notice that something is wrong and a live route to the Board.
#   What she does not have, before Edit 4, is the DATE. So the harm is informational and
#   partial, not automatic. I would not defend 1.00 and I would not defend 0.
# direction of error: symmetric, result LINEAR in it. Tied second-ranked driver with
#   LATER_DATE_FILING_RATE; the two enter the product identically.

G4_BASELINE_AVAILABILITY = {"low": 0.00, "central": 0.50, "high": 1.00}
# unit: probability that, WITHOUT Edit 4, a member in the expiry-sentence class who loses
#   her qualifying retirement because nobody told her her date is nonetheless held
#   harmless under subdivision G 4 clause (iii) as "unable to retire in a qualifying
#   retirement by reason of an error of the Board" on the UN-DEEMED limb of that clause.
# source: ANALYST JUDGMENT, and it is a LEGAL probability I am not competent to set.
#   It is in the register because the incremental cost of Edit 4 is proportional to
#   (1 - this). It is RED TEAM / COUNSEL REVIEWER's to replace, and STATUTORY RESEARCHER's
#   to say whether clause (iii)'s deeming sentences are inclusive or exhaustive.
#   - If 1.00, Edit 4 is fiscally inert on this line, because she already recovers.
#   - If 0.00, Edit 4's incremental cost is the whole conversion value.
#   The whole 0-1 interval is reported; the central 0.50 is a placeholder that carries no
#   information and is labelled as such everywhere it is used.
# direction of error: this is the single largest unresolved term in the answer and it is
#   not a fiscal input. Named first in the sensitivity section for that reason.

# ---------------------------------------------------------------------------
# F. MODEL CONTROLS
# ---------------------------------------------------------------------------

MATERIALITY_FLOOR_USD = 100_000
# unit: dollars over the 48-month pilot. The threshold at which a Virginia fiscal impact
#   statement on a capped, self-executing programme would print a figure rather than "$0"
#   or "can be absorbed with existing resources".
# source: ANALYST JUDGMENT, same convention MOO-163 §8 and MOO-170 §7 used. It is a
#   reporting convention, not a legal threshold.

MOO170_RESOLUTION_MEMBERS = 2.80
# unit: members over 48 months. MOO-170's own stated resolution figure, used so the
#   member-count comparison is on MOO-170's terms and not on a threshold of my choosing.
# source: MOO-170 README headline and §3.

MOO183_COST_PER_PARTICIPANT_USD = {"low": 55_000, "high": 66_000}
# unit: dollars per participant, PV at 6/30/2025, net trust cost basis.
# source: MOO-183 Table A, range across the five priced designs ($55,000 to $66,000).
# USED ONLY as an order-of-magnitude cross-check on the per-event figure in §8, and the
#   BASIS DIFFERS (net trust cost per participant, not certified subsidy per election).
#   Reported as a basis-mismatched comparison, NOT as agreement.

FY_FIRST_BENEFIT = 2029
FY_IMPLEMENTATION = 2028
# source: MOO-183 §8 — a July 1 effective date splits the first programme year, FY2028
#   carries implementation only, FY2029 is the first benefit year.
# direction of error: none; it is the authorised timing convention in this project.
