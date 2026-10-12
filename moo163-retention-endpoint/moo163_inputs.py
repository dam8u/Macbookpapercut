"""
MOO-163 — assumption register for the D 4 / D 5 filing-date retention endpoint.

EVERY number the model uses appears in this file, once, with a unit, a source and a
direction of error. There are no magic numbers in moo163_retention.py.

Pre-decisional and internal. No figure here is a VRS actuarial result.
Nothing is reliable beyond two significant figures (MOO-46 Decision 4).

Retrieval date for every Paperclip-internal source below: 12 October 2026.
"""

# ---------------------------------------------------------------------------
# A. STATUTORY PARAMETERS — read off bill-text-s8 (MOO-42) document revision 73,
#    506,992 characters. These are text, not estimates. Direction of error: none,
#    unless the text moves again.
# ---------------------------------------------------------------------------

AGGREGATE_CAP_USD = 3_000_000
# unit: dollars, cumulative over the life of the section (not per year).
# source: subdivision D 2, revision 73 — "together with all certified subsidies and
#   all contingency amounts previously reserved under this subsection and not
#   released, would exceed $3,000,000". D 2 also states the limitation is
#   "self-executing and require[s] no further act of the General Assembly".
# direction of error: none. It is a hard ceiling.

PER_ELECTION_CEILING_USD = 170_000
# unit: dollars per election.
# source: subdivision D 2, revision 73 — "The Board shall not accept an election for
#   which the certified subsidy exceeds $170,000."
# direction of error: none. This ceiling is what bounds the aggregate delta in §3.

CONTINGENCY_RATE = 0.20
# unit: fraction of each certified subsidy, reserved alongside it.
# source: subdivision D 3, revision 73 — "a contingency amount equal to `[20]` percent
#   of that certified subsidy", and "charged against the limitation in subdivision 2".
#   NOTE the bracket: `[20]` is still a drafting dial in the live text.
# direction of error: the bracket could move either way; a higher rate makes the cap
#   bind sooner, which makes the retention endpoint matter MORE. Tested in §5.

BOARD_DECISION_DEADLINE_DAYS = 90
# unit: days from filing of the reconsideration request.
# source: subsection M 2, revision 73 — "The Board shall act upon a request for
#   reconsideration within 90 days."

RETENTION_KII_OFFSET_DAYS = 30
# unit: days after the Board's first action on the request.
# source: the board's decision of 12 October 2026, card (k-ii), MOO-141 revision 3
#   §5.3 — "until 30 days after the Board acts upon the request". Drafted as Edit 3
#   on MOO-162. This is the endpoint being priced, not an estimate.

PILOT_LENGTH_MONTHS = 48
# unit: months. source: MOO-71 authorised-participant-count §1 — "over the 48-month
#   pilot". The unit of analysis for every count below is "members over 48 months",
#   NOT members per year.

# ---------------------------------------------------------------------------
# B. AUTHORISED COUNTS — transcribed from MOO-71 "authorised-participant-count"
#    document revision 2, released by the Policy Director 12 October 2026.
#    I am NOT re-deriving these. They are an input to this issue, cited as given.
#    Basis: bill-text-s8 store revision 21, §7 item 22 = option (c) + no-advance bar.
#    Conditional on the NARROW clause (vi) reading (open at MOO-49).
# ---------------------------------------------------------------------------

ELIGIBLE_MEMBERS = {"low": 9.82, "central": 19.63, "high": 32.72}
# unit: members over 48 months. source: MOO-71 §1 row "eligible members,
#   clauses (v)+(vi), with the no-advance bar".
# direction of error: the clause (vi) reading is the dominant unresolved driver —
#   broad gives ~130, a 6.9x move (MOO-71 comment). Conditional, and the condition
#   travels with the number.

PARTICIPANTS_ADMITTED_FUNDED = {"low": 8.97, "central": 17.93, "high": 29.89}
# unit: members over 48 months, net of take-up and of all three statutory refusals.
# source: MOO-71 §1 row "participants — admitted and funded". Carried as 18 (9 to 30).
# direction of error: MOO-71 §3 — true central is between 17.93 and 18.49; rounds to
#   18 either way.

CAP_UTILISATION_STATED = {"central": 0.793, "high": 1.322}
# unit: fraction of the $3,000,000, with the 20% contingency charged inside it.
# source: MOO-71 §1 note. BOTH ARE UPPER BOUNDS (MOO-71 §3).

RETIREMENT_WINDOW_RUNG_RATIO = 1_411_988 / 1_661_819
# unit: dimensionless. The factor by which the move to the 12-month retirement-window
#   rung lowers per-member subsidy.
# source: MOO-71 §3 — "net trust cost falls $1,661,819 -> $1,411,988 on the authorised
#   ladder". Applying it to CAP_UTILISATION_STATED reproduces MOO-71's own corrected
#   high figure of "near 112%", which is the model's internal bridge check (§2).
# direction of error: downward on utilisation, i.e. makes the cap LESS likely to bind.

STATUTORY_REFUSALS_CENTRAL = {
    "zero_month_bar": 0.46,       # subsection C zero bar, MOO-71 §4 row (c)
    "ceiling_170k": 1.23,         # D 2 $170,000 ceiling, MOO-71 §4 row (c)
    "no_advance_band": 1.01,      # MOO-71 §3 — 18.95 less 17.93
    "max_purchasable_amount": 0.00,  # MOO-71 §4 — refuses nobody, a structural finding
}
# unit: members over 48 months. These are the members who receive a refusal notice and
#   who therefore have something to ask the Board to reconsider under subsection M 2.
# direction of error: MOO-71 §4 marks the first two as "<=" under the authorised row,
#   so this over-counts the pool that can seek reconsideration. Over-counting is the
#   cautious direction here: it inflates the cohort this provision can touch.

# ---------------------------------------------------------------------------
# C. ANALYST JUDGMENT — no source exists for any of these. Each is labelled, with
#    the range I would defend. None of them is data.
# ---------------------------------------------------------------------------

RECONSIDERATION_SEEK_RATE = {"low": 0.15, "central": 0.35, "high": 0.60}
# unit: fraction of refused applicants who file an M 2 request.
# source: ANALYST JUDGMENT. No Virginia source. VRS publishes no reconsideration
#   volumes for § 51.1-142.2 purchases; MOO-71 §3 records that no published count of
#   these purchases exists at all. A defensible range is 15-60%: the refusal notice is
#   required by D 4 / D 5 / C to state the member's standard-cost rights and the
#   standard cost, which is unusually strong prompting toward a request, so I would
#   not defend a figure below 15%.
# direction of error: symmetric. The result is NOT sensitive to it (see §5).

SUBSIDY_CV = {"low": 0.15, "central": 0.25, "high": 0.40}
# unit: coefficient of variation of the certified subsidy across the funded cohort.
# source: ANALYST JUDGMENT. MOO-71 withdrew the per-member "agreement" from the record
#   and gives like-for-like Pathway A means 13.6% apart ($125,060 v $137,402), which is
#   a between-model spread, not a within-cohort spread. No within-cohort dispersion has
#   been published by any issue in this project.
# direction of error: higher CV widens the residual at exhaustion and so widens the
#   aggregate delta. This is the driver the binding-case answer is most sensitive to.

FIRST_ACTION_DAYS = {"low": 3, "central": 10, "high": 30}
# unit: days from filing of the request to the Board's first action (F).
# source: ANALYST JUDGMENT, anchored on the worked example in MOO-141 revision 3 §5.3
#   (files 1 April, acknowledged 8 April => F = 7) and on the 30-day completeness-notice
#   habit the bill imposes elsewhere (D 4). 3-30 days is the defensible band.

DECISION_DAYS = {"low": 30, "central": 60, "high": 90}
# unit: days from filing of the request to the Board's decision (D).
# source: ANALYST JUDGMENT, anchored on the same worked example (decided 25 June =>
#   D = 85) and capped by BOARD_DECISION_DEADLINE_DAYS. The statute allows 90.

# ---------------------------------------------------------------------------
# D. MODEL CONTROLS
# ---------------------------------------------------------------------------

RNG_SEED = 20261012
# Fixed so the run is byte-reproducible.

N_DRAWS = 20_000
# Monte Carlo draws per scenario per reading. 20,000 puts the Monte Carlo error on the
# reported dollar deltas well below $1,000, i.e. below the two-significant-figure
# precision the inputs support. Reported in the transcript.

QUEUE_DISCIPLINE = ("strict_stop", "skip_ahead")
# The one construction question this model cannot resolve for itself, so it reports
# BOTH. Subdivision D 5 says the Board "shall place the application on a waiting list
# ... and shall accept the election if and when sufficient amounts become available",
# while D 4 says the Board "shall accept elections in the order in which eligible
# members file complete applications".
#   strict_stop  — the Board stops at the first application that does not fit.
#   skip_ahead   — the Board wait-lists it and continues down the order, accepting any
#                  later application that does fit.
# WHICH ONE THE TEXT REQUIRES IS A QUESTION FOR STATUTORY RESEARCHER, NOT FOR ME.
# The headline bound in §3 holds under both; see the transcript.

READINGS = ("first_action", "kii_F_plus_30", "decision")
# The three endpoints the Policy Director handed me on MOO-163. I am pricing between
# them. I am NOT deciding which one the text produces.

DISPLACEMENT_MODELS = ("back_of_queue", "removed")
# What happens to the applicant once retention ends and the Board has not yet accepted
# her election.
#   back_of_queue — her effective ordering date becomes the retention end date.
#   removed       — she drops out of the subsidised queue and takes her subsection B
#                   standard-cost rights (MOO-141 §5.3 describes this outcome).
# Also a construction question. Both reported.
