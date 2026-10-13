"""
MOO-204 — assumption register for pricing candidate 164-9.

Candidate 164-9 replaces the final clause of Edit 164-1's READ (MOO-164 §3.1) so that
subsection M 2's tolling endpoint is capped at 48 days after the LATER of the Board's
acting upon the request and the expiration of the period allowed by this section for
acting upon the request, instead of 48 days after the Board's acting.

EVERY number this model uses appears in this file, once, with a unit, a source and a
direction of error. There are no magic numbers in moo204_164_9.py.

Sections:
  A. STATUTORY / DRAFTED PARAMETERS — read off the cut and the enacted base. Text, not
     estimates. Direction of error: none unless the text moves again.
  B. LIVE FIGURES INHERITED — cited as given from released issues. NOT re-derived here.
  C. ALLOWANCE AND RATE INPUTS — sourced where a source exists, labelled ANALYST
     JUDGMENT where none does.
  D. POPULATION — the C2 class. No authorised count exists; the bound and the judgment
     are both stated.
  E. MODEL CONTROLS.

Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.
No figure here is a VRS actuarial result. Nothing is reliable beyond two significant
figures (MOO-46 Decision 4).

Retrieval date for every Paperclip-internal source: 12 October 2026.
Retrieval date for every external source: 12 October 2026.
"""

# ---------------------------------------------------------------------------
# A. STATUTORY AND DRAFTED PARAMETERS
# ---------------------------------------------------------------------------

M2_PERIOD_RECONSIDERATION_DAYS = 90
# unit: days allowed to the Board for acting upon a request for reconsideration.
# source: subsection M 2 — "The Board shall act upon a request for reconsideration
#   within 90 days." Quoted at MOO-164 §15.4 (candidate 164-10's FIND).
# direction of error: none. It is the figure candidate 164-9's new cap keys to.
# CONDITION: the period has no stated COMMENCEMENT in the enacted text. Candidate
#   164-10 ("... after the request is filed") supplies one and the Policy Director's
#   disposition §10 takes it. This model assumes 164-10 is applied; §9 prices the
#   case where it is not.

M2_PERIOD_DEFINITION_DAYS = 30
# unit: days allowed by this section for acting upon a request under the definition of
#   "final qualifying retirement date".
# source: MOO-164 §2.4 — "the definition's own 30-day period is for a request to
#   approve a later date ... This section allows 90 days for a reconsideration request
#   and 30 for a definition request."
# direction of error: none. M 2's tolling sentence covers BOTH classes, so candidate
#   164-9's cap resolves to two different outer bounds. Both are reported.

EDIT_164_1_FLOOR_DAYS = 30
# unit: days after the Board acts upon the request.
# source: MOO-164 §3.1 READ, revision-5 re-cut — "in no case earlier than 30 days
#   after the Board acts upon the request". A freestanding minimum (F23).

EDIT_164_1_NOTICE_OFFSET_DAYS = 30
# unit: days after the Board gives written notice of its decision.
# source: MOO-164 §3.1 READ — "until 30 days after the Board gives written notice of
#   its decision upon the request to the member and to the person who filed the
#   request".

EDIT_164_1_CAP_DAYS = 48
# unit: days. The outer limit in Edit 164-1 as the cut stands.
# source: MOO-164 §3.1 READ — "in no case later than 48 days after the Board acts upon
#   the request". Derived at §2.2 as 15 (notice backstop) + 3 (mailing) + 30.
#   NOTE the Policy Director's disposition §12.2: at store revision 68 the 3-day
#   extension is available only where the Board MAILS, so mailing remains the worst
#   case and 48 remains the outer bound, but §3.1's derivation sentence is now stale.
#   The FIGURE is unaffected, which is all this model uses.
# direction of error: none. Candidate 164-9 does not change the 48; it changes what
#   the 48 is measured from.

NOTICE_BACKSTOP_DAYS = 15
# unit: days after the Board gives its decision, by which it must tell the member the
#   decision has reset her final qualifying retirement date.
# source: MOO-164 §2.2 — "nothing requires the Board to tell her ... until 15 days
#   after it gives the decision (Edit 2's backstop)".

MAILING_EXTENSION_DAYS = 3
# unit: days. Extension of every period running from the giving of a mailed statement
#   or notice.
# source: the final interpretation paragraph of subsection A, as corrected at MOO-140
#   §0.1 item 1 (it is NOT subsection L). Verified there against bill-text-s8 document
#   revision 73.
# direction of error: at store revision 68 this is available only on the mailing route;
#   electronic transmission carries the 5:00 p.m. rule instead and cannot push the
#   given date past the backstop. Mailing is the worst case, so using it is cautious.

M2_CLAUSE_II_AGGREGATE_DAYS = 120
# unit: days. The aggregate ceiling on tolling under M 2's tolling sentence.
# source: M 2 clause (ii), via pass 18's F-6 as recorded in MOO-170's register
#   section E — "the aggregate of all [tolling] shall not exceed 120 days". MOO-164
#   §2.2 states it operates on top of Edit 164-1: "clause (ii)'s 120-day aggregate
#   still binds on top of it."
# direction of error: WHETHER clause (ii) clips a SINGLE request's endpoint, as
#   against capping only the aggregate across requests, is a construction question and
#   it is STATUTORY RESEARCHER'S. Both branches are reported (CLAUSE_II_BRANCHES).

M8A_EXCLUSION_CAP_DAYS = 90
# unit: days. Ceiling on the aggregate of periods excluded from clause (ii)'s cap.
# source: ENACTED at store revision 68 — subdivision M 2 clause (ii) now closes
#   "provided that the aggregate of all periods so excluded shall not exceed 90 days."
#   Counted in enacted §1 by the Policy Director, disposition §8.
# direction of error: none. This is what closes the formerly unbounded term and makes
#   the card (h) bound 300 days rather than unbounded. Earlier MOO-164 revisions'
#   "300 if m8-a lands, unbounded if not" is stale.

CARD_H_BOUND_COMPONENTS = {
    "g2_notice_days": 60,
    "member_window_days": 30,
    "clause_ii_aggregate_days": 120,
    "m8a_exclusion_cap_days": 90,
}
# unit: days. The four terms of the card (h) outer bound on the zero-allowance window.
# source: MOO-164 §2.3 as corrected at revision 5 — "60 + 30 + 120 + the Board's
#   lateness in first acting", with the last term closed at 90 by m8-a. Sums to 300.
# direction of error: none. Candidate 164-9 touches no term in it; §3 proves that.

G2_DETERMINATION_DAYS = 60
G2_NOTICE_DAYS = 60
G2_EFFECT_FLOOR_DAYS = 30
G2_OUTER_LIMIT_DAYS = 120
# unit: days, all measured from the determination date (G 2's own day 0 — "the date
#   from which the 60-day period within which the Board must make the determination
#   required by this subdivision runs").
# source: MOO-140 §2.1's sentence-by-sentence table, read off bill-text-s8 store
#   revision 47. Determination within 60; notice no later than 60 after the
#   determination date; effect no less than 30 days (33 where mailed) after notice;
#   effect no later than 60 after notice and in no event later than 120 after the
#   determination date.
# direction of error: none. These are MOO-140's settled figures and this model does
#   not re-derive them.

G4_AGGREGATE_DAYS = 120
# unit: days. Ceiling on the non-running of G 2's clocks by reason of M 2 requests.
# source: subdivision G 4, quoted at MOO-140 §2.3(b) — "the aggregate of all such
#   non-running by reason of such requests shall not exceed 120 days". MOO-140 §2.3
#   concludes "the ceiling is 240 days, and the member has no allowance throughout".
# direction of error: none. This is the clip that bounds candidate 164-9's effect on
#   C2 regardless of which clause (ii) branch obtains.

RETENTION_DAYS = 120
# unit: days after the Board acts upon the request, for which the D 4 / D 5 filing date
#   is retained.
# source: the BOARD's card on MOO-176 revision 5, 14:15 on 12 October 2026, recorded
#   at MOO-177 §1 ("Edit 3 retention: 30 days after the Board acts -> 120 days after
#   the Board acts") and owned by MOO-177 / MOO-180.
#   THIS SUPERSEDES MOO-163's RETENTION_KII_OFFSET_DAYS = 30. MOO-163's $0 is NOT
#   restated as current anywhere in this model.
# direction of error: none. It is a board figure, not an estimate.

WORKED_FIRST_ACTION_DAY = 7
WORKED_DECISION_DAY = 85
# unit: days from the filing of the request.
# source: MOO-141's worked facts (files 1 April, acknowledged 8 April, decided
#   25 June), carried as the ordinary facts at MOO-177 §1 and used by MOO-164 §15.4 to
#   state candidate 164-9's movement.
# direction of error: none. They are the published comparison facts, not estimates.

CARD_F_DAYS = 78
# unit: days. The full act-versus-decision difference on the worked facts (85 - 7).
# source: MOO-164 §2.2 option (b-2) — "it restores the full D - F difference, 78 days
#   on MOO-141's facts". MOO-177 §1 uses the same 78 in "net +42 = 120 - 78".

MOO177_NET_DAYS = 42
# unit: days of retention to spare against the decision day.
# source: MOO-177 §1 — "Net: +42", derived as 120 - 78 and as 127 - 85.
# Used as a LOCK, not as an input: §0 re-derives it and stops if it does not reproduce.

# ---------------------------------------------------------------------------
# B. LIVE FIGURES INHERITED — cited as given, NOT re-derived
# ---------------------------------------------------------------------------

LAPSE_BOUND_USD = 204_000
# unit: dollars, over the 48-month pilot, as LAPSE and not as cost.
# source: MOO-163 §4a, re-established analytically under chaining at MOO-170 §2 and
#   adopted at MOO-179 §2.1. It is the cap-fill residual argument and it quantifies
#   over ANY ordering of a fixed cohort against the fixed pool.
# direction of error: none that a days change can reach. The bound is
#   permutation-invariant; §5 states why candidate 164-9 is inside the quantifier.

DISPLACEMENT_MEMBERS_LIVE = {
    "removed_high_mean": 2.80,
    "removed_high_worst_draw": 11.0,
    "back_of_queue_gated_any": 0.00,
    "central": 0.00,
    "low": 0.00,
}
# unit: members of queue position moved, per 48 months.
# source: MOO-179 §2.2, on MOO-170's sweep at the board's 120-day retention —
#   "0.14 -> 2.80 members mean over the 48-month pilot, roughly 21x, with 11 members in
#   the worst draw", `back_of_queue_gated` "flat at 0.00 at every chain length
#   including unbounded", and $0 / 0.00 at central and low (MOO-170 §4).
#   THIS IS THE LIVE THIRD-PARTY FIGURE. MOO-163's 0.11-0.14 is superseded.
# direction of error: MOO-179 §2.2 records it as 8.0% of a high-cell cohort of 35
#   against a count known to roughly +/-9 members, i.e. inside the resolution of its
#   own denominator.

CAP_UTILISATION_CENTRAL = 0.674
# unit: fraction of D 2's $3,000,000.
# source: MOO-179 §2.1 — "67.4% utilisation", from MOO-163 §2 as corrected.
# direction of error: upper bound (MOO-71 §3). The cap does not bind at central, which
#   is why queue position decides nothing for anyone there.

DAYS_DIMENSION_HAS_NO_FISCAL_WARRANT = True
# unit: boolean, a released finding.
# source: MOO-179 §2.3 — "MOO-170 re-ran the saturated cell at the 33-day, 40-day and
#   120-day link and got IDENTICAL results ... Link length decides only how fast the
#   chain saturates, not what it saturates at. So the clause (ii) dimension —
#   aggregate days — has no fiscal warrant whatsoever, at any figure."
# This is the single most load-bearing inherited finding in this issue, because
#   candidate 164-9 is a DAYS change. §5 re-verifies it at 164-9's own day figures
#   rather than taking it on trust.

# ---------------------------------------------------------------------------
# C. ALLOWANCE AND RATE INPUTS
# ---------------------------------------------------------------------------

DHRM_SALARY = {"mean": 69_865, "median": 61_305, "p25": 48_538, "p75": 82_735}
# unit: dollars per year, DHRM classified workforce, 6/30/2024, All Pay Areas,
#   n = 56,728.
# source: PRIMARY — DHRM State Workforce Facts p.14, transcribed from the published
#   engine register `moo183-cost-per-participant/engine/inputs.py` (DHRM_SAL_MEAN,
#   DHRM_SAL_MEDIAN, DHRM_SAL_P25, DHRM_SAL_P75). Not re-derived here.
# direction of error: 2024 vintage against a 2027-session bill. Understates nominal
#   salary and therefore understates the allowance, which understates the dollar
#   movement priced here. Cautious direction for a $0 conclusion is OVERstatement, so
#   this input is used with the long-service premium and the high service rung below.

LONG_SERVICE_PREMIUM = 0.10
# unit: fraction. Premium of a 25+ year employee's salary over the age-band average.
# source: JUDGMENT, carried unchanged from the published engine register
#   (`inputs.py` LONG_SERVICE_PREMIUM, "central 10%, defensible range 0% to 20%").
# direction of error: higher premium raises the allowance and so raises the movement.

RETIREMENT_MULTIPLIER = {"plan1": 0.0170, "plan2": 0.0165, "hybrid_db": 0.0100}
# unit: fraction of AFC per year of service.
# source: PRIMARY — VRS Plan 1 / Plan 2 / Hybrid handbooks p.18, transcribed from the
#   published engine register (`inputs.py` MULT_PLAN1, MULT_PLAN2, MULT_HYBRID).
# direction of error: none in the figures. Which plan the affected member is in is a
#   composition question; plan 2 is used at the central estimate because the class is
#   long-service veterans and the hybrid DB rate would lower the allowance.

SERVICE_YEARS_AT_RETIREMENT = {"low": 20, "central": 27, "high": 32}
# unit: years of creditable service at retirement.
# source: ANALYST JUDGMENT. No count of service at retirement for the § 51.1-142.2
#   military-purchase class is published; MOO-71 §3 records that no published count of
#   these purchases exists at all. 20-32 years is the band I would defend for a member
#   who is buying service credit in order to reach a qualifying retirement date.
# direction of error: symmetric. It scales the allowance linearly and therefore scales
#   the dollar movement linearly. Tested in §7.

MEMBER_DISCOUNT_RATE = {"low": 0.0400, "central": 0.0675, "high": 0.1000}
# unit: per year. The rate at which the member values money she receives later.
# source for the CENTRAL figure: PRIMARY — VRS June 30, 2025 valuation p.37, 6.75%
#   assumed rate, which is ALSO "the statutory interest rate used for refunded-service
#   purchases" (published engine register `inputs.py` DISCOUNT_RATE). Using the rate
#   the chapter itself uses avoids picking a household rate out of the air.
# source for LOW and HIGH: ANALYST JUDGMENT. 4% is a short-horizon risk-free saving
#   rate; 10% is an unsecured household borrowing rate for a member who has to bridge
#   the gap. I would defend 4-10%.
# direction of error: symmetric, and the result scales almost linearly in it.

# ---------------------------------------------------------------------------
# D. POPULATION — the C2 class
# ---------------------------------------------------------------------------

NON_QUALIFYING_RETIREMENT_SHARE = {"low": 0.02, "central": 0.05, "high": 0.15}
# unit: fraction of funded participants who reach a G 2 cutback determination, i.e.
#   whose election has not settled under subdivision 1 or 4 and who do not retire in a
#   qualifying retirement, with no disability application pending.
# source: ANALYST JUDGMENT. NO AUTHORISED COUNT OF THIS CLASS EXISTS IN THIS PROJECT.
#   MOO-71's funnel counts eligibility, take-up and the three statutory refusals; it
#   does not count members who elect, are funded and then fail to retire qualifying.
#   MOO-140 §3.2 establishes that the class is NARROWER than "a member who does not
#   retire in a qualifying retirement" on four separate grounds, so a share in the
#   single digits is the defensible region; 15% is the high case.
# direction of error: symmetric and it scales the aggregate linearly. THE HARD BOUND
#   is that the class cannot exceed the funded participant count (18, range 9 to 30
#   over 48 months), which is what §4 reports as the ceiling case.

# ---------------------------------------------------------------------------
# E. MODEL CONTROLS
# ---------------------------------------------------------------------------

CLAUSE_II_BRANCHES = ("clause_ii_clips_endpoint", "clause_ii_aggregate_only")
# The one construction question this model cannot resolve for itself, so it reports
# BOTH branches everywhere it matters.
#   clause_ii_clips_endpoint — M 2 clause (ii)'s 120-day aggregate operates as a hard
#       ceiling on a single request's tolling, net of the excluded period. This is the
#       branch MOO-164 §2.2 states ("clause (ii)'s 120-day aggregate still binds on
#       top of it").
#   clause_ii_aggregate_only — clause (ii) bounds only the sum across requests, and a
#       single request's endpoint runs to candidate 164-9's own cap.
# WHICH ONE THE TEXT REQUIRES IS A QUESTION FOR STATUTORY RESEARCHER, NOT FOR ME.

FIRST_ACTION_SCAN_DAYS = range(0, 121)
# Model control. The range of first-action days over which §2 scans the retention
# coverage margin, so the worst case is found rather than assumed.

FISCAL_YEARS = ("FY2027", "FY2028", "FY2029", "FY2030")
# Model control. The four fiscal years of the 48-month pilot, as MOO-170 §0 reports.

PILOT_LENGTH_MONTHS = 48
# unit: months. source: MOO-71 authorised-participant-count §1, via MOO-163's
#   register. THE UNIT OF ANALYSIS FOR EVERY COUNT HERE IS MEMBERS PER 48 MONTHS.

MONTH_DAYS = 30.44
# unit: days per month, for converting a day count into months of allowance.
# source: 365.25 / 12. Arithmetic, not an estimate.

DISPLAY_FLOOR_USD = 1_000
# Model control, carried from MOO-163 and MOO-170: a dollar delta below this is
# reported as $0 because the inputs do not support finer resolution.

MC_DRAWS_INVARIANCE_CHECK = 20_000
# Model control for the §6 re-run of MOO-170's sweep. The invariance check is an
# IDENTITY test across link lengths on a SHARED draw set and a fixed seed, so it would
# be decisive at far fewer draws. It is run at MOO-170's own 20,000 so that the same
# run also REPRODUCES MOO-179 §2.2's published 2.80 mean / 11 worst draw exactly.

RNG_SEED = 20261012
# Carried from MOO-163 / MOO-170 so the §5 re-run is comparable to theirs.
