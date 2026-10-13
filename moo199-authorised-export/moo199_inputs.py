"""
MOO-199 — assumption register and lock set.

Two products:
  (1) the interactive model's full data shape, re-emitted on the AUTHORISED basis;
  (2) the workforce exchange recomputed on the RECOMMENDED design's own anchor.

EVERY number this model treats as given appears in this file, once, with a unit, a
source, a vintage and a direction of error. `moo199_export.py` contains no magic
numbers.

Pre-decisional and internal. No figure here is a VRS actuarial result. Nothing is
reliable beyond two significant figures (MOO-46 Decision 4).

Retrieval date for every Paperclip-internal source below: 13 October 2026.
"""

# ===========================================================================
# A. WHAT IS MEASURED IN THIS RUN, WHAT IS CITED, AND WHAT COULD NOT BE REACHED
# ===========================================================================
#
# MEASURED here, by re-running the published repaired (v2) engine that is committed
# in this repository at moo183-cost-per-participant/engine/:
#   - the recommended design's run on the authorised 12-month rung: participants,
#     net trust cost PV, mean acceleration, mean participating salary, mean years
#     purchased, member-price pair (multiple of ANC / share of AEC);
#   - the statutory-interest dial, 4.00% to 7.00%, on that design's own cohort;
#   - the S8 member-price surface over an age x service grid;
#   - the cap as an admission rule (aggregate-cap sweep) on that cohort;
#   - the whole workforce exchange, from engine/workforce.py.
#
# CITED, not re-derived:
#   - the authorised retirement-deadline ladder (MOO-32 v6 basis, six rungs);
#   - the MOO-32 v6 figure set: participants, trust PV and nominal at rung 12,
#     certified subsidy reserved nominal;
#   - the authorised cap-utilisation percentages.
#
# COULD NOT BE REACHED FROM THIS WORKSPACE, and this is stated in the deliverable:
#   - `AgentCreated/v2.0/05-model-code-and-data/model-current-12-october/
#      moo32_v6_engine.py` — the engine that computes the authorised basis. The
#      `AgentCreated` tree is not in this repository or in any workspace this agent
#      can read (the same absence MOO-193 recorded for
#      `AgentCreated/_review-MOO-32-charts-v6/`). So every block of the export that
#      needs a NEW v6 cohort run is produced on the MOO-48 cohort and carried to the
#      authorised anchor by a stated transformation, labelled `derived`, never
#      `measured`.
#   - `make_model.py` — the consumer. Its key names could not be read, so the export
#      ships a documented schema plus a key-binding table instead of an asserted
#      binding. See EXPORT_SCHEMA_NOTE.

ENGINE_PROVENANCE = (
    "moo183-cost-per-participant/engine/ — the published repaired (v2) engine as "
    "shipped with sponsor package v1.0 (AgentCreated/v1.0/05-model-code-and-data/"
    "python), copied byte-for-byte at MOO-183 and not modified since. This issue "
    "modifies no line of it."
)

V6_ENGINE_ABSENT = (
    "AgentCreated/v2.0/05-model-code-and-data/model-current-12-october/"
    "moo32_v6_engine.py is not present in this repository or in any workspace "
    "readable by this agent. Checked: the project repository, every "
    "instances/default/workspaces/* tree, and a filesystem-wide search for a "
    "directory named AgentCreated. Result: no match."
)

EXPORT_SCHEMA_NOTE = (
    "make_model.py is inside the same unreadable AgentCreated tree, so the exact key "
    "names it consumes could not be verified. out_moo199_model_data.json therefore "
    "carries meta.key_binding_verified = false and a meta.key_binding_table mapping "
    "each block to the model tab and the dial it feeds. Binding the keys is a "
    "mechanical check for whoever runs the v2.1 pass with the folder in hand; no "
    "figure in the export depends on it."
)

# ===========================================================================
# B. LOCKS — figures this run must reproduce before any number below is usable.
#    Direction of error: none. These are locks, not inputs. A mismatch means the
#    engine or its inputs moved and the run must stop.
# ===========================================================================

LOCK_TOL_DOLLARS = 0.51       # the source CSVs carry full precision
LOCK_TOL_PARTICIPANTS = 0.51
LOCK_TOL_RATIO = 0.0001

# --- B1. the recommended design's measured ladder -------------------------------
# source: out_moo48_deadline_ladder.csv / out_moo48_summary.json (sponsor package
#   v1.0), locked rung-by-rung by MOO-85 §0, reproduced to the dollar at MOO-48 §2
#   and byte-identically again at MOO-183 §7.
# basis: Pathway A only, S8 earned-service price, statutory interest 6.00%, narrow
#   clause (vi) reading, WITHOUT §7 item 22 option (c) and WITHOUT the no-advance bar.
MOO48_PARTICIPANTS = {"low": 9.452951873201249,
                      "central": 18.905903746402497,
                      "high": 31.509839577337704}
# unit: member elections over the 48-month pilot. Rung-INVARIANT (MOO-48 §3,
#   MOO-85 §1: "the window admits no one new"); re-verified in this run.
# direction of error: modeled demand, not observed take-up. No external anchor.

MOO48_LADDER = {
    # rung (months): (trust PV low, central, high, mean acceleration months)
    0:  (830909.35148502, 1661818.70297004, 2769697.8382834056, 56.85161523952638),
    1:  (820911.8936185322, 1641823.7872370644, 2736372.978728435, 55.85161523952625),
    6:  (769788.0481337646, 1539576.0962675293, 2565960.1604458787, 50.851615239526225),
    12: (705994.0462162767, 1411988.0924325534, 2353313.487387581, 44.85161523952625),
    18: (639617.403410847, 1279234.806821694, 2132058.011369493, 38.85161523952607),
    24: (570747.8378511794, 1141495.6757023588, 1902492.7928372638, 32.88554063420059),
}

# --- B2. the authorised member-price pair ---------------------------------------
# source: MOO-72 repair register item C — "the member-price pair 1.50x / 61% to
#   1.42x / 43%". The 1.42x / 43% pair is the authorised one.
# unit: dimensionless ratios (member payment / ANC reference; member payment / AEC
#   reference), cohort-weighted, PV.
AUTHORISED_PRICE_PAIR = {"multiple_of_anc": 1.42, "share_of_aec": 0.43}
AUTHORISED_PRICE_PAIR_TOL = 0.005   # the authorised figures are printed to 2 s.f.

# --- B3. the printed workforce exchange, which this issue replaces --------------
# source: 04-fiscal-analysis.md §9 and 02-policy-brief.md §6, sponsor package v1.0.
# The printed pairing is repaired S1 (Pathways A+B at approximate normal cost), at
#   the published 6-month retirement rung, central take-up: net trust cost per
#   participant $64,678 against a central net workforce effect per participant, and
#   the sentence "the workforce effect covers about 71% of the pension cost".
PRINTED_ANCHOR = 64678          # unit: dollars per participant, PV at 6/30/2025
PRINTED_COVERAGE = 0.71         # unit: fraction of the pension cost, as printed
PRINTED_COVERAGE_TOL = 0.005
PRINTED_ANCHOR_DESIGN = "S1"
PRINTED_ANCHOR_RUNG = 6         # months
# MOO-183 §4 established that $64,678 is agg['trust'] / agg['n'] on the S1 central
#   row, identical to the tenth of a cent, and that its printed LABEL ("pension cost
#   of the purchased service") names the 28% service-credit line while the figure is
#   the 100%-less-member-payment line. The figure was never wrong; the design and the
#   rung were.

# --- B4. the authorised cap-utilisation percentages -----------------------------
# source: MOO-32 v6, carried into the live register and quoted verbatim at
#   moo191-rev64/live-body.md — "MOO-32 v6's authorised 78.1872 percent central and
#   130.31 percent high on 18.3965 participants", "each including the mandatory 20
#   percent contingency". MOO-183 §3 prints the set as 39% / 78% / 130%.
AUTHORISED_CAP_UTILISATION = {"low": 0.390936, "central": 0.781872, "high": 1.303120}
AUTHORISED_CAP_UTILISATION_TOL = 0.00005

# ===========================================================================
# C. THE AUTHORISED BASIS — cited. This is the basis the ten documents print.
#    § 51.1-142.4 C item 22 as option (c) measured at the filing date, PLUS the
#    no-advance bar of clause (vii) of "eligible member"; 12-month retirement rung;
#    6.00% statutory interest; state agency employees in Plan 1 and Plan 2;
#    four-year pilot from 1 July 2029; PV at 6/30/2025.
#    source: the MOO-32 v6 figure set (out_moo32_v6_basis.json /
#    out_moo32_v6_funnel_C6.csv / out_moo32_v6_deadline_ladder.csv), carried into
#    this issue by its own description and by moo183_inputs.py §E.
# ===========================================================================

V6_PARTICIPANTS = {"low": 9.19824819071555,
                   "central": 18.3964963814311,
                   "high": 30.66082730238517}
# unit: member elections over the 48-month pilot. Rung-invariant on this basis too.
# direction of error: UPPER BOUND. Clause (viii) of "eligible member" is in the live
#   draft at document revision 76 and in no committed run; it is an additional
#   screen, so it can only refuse more. 18.4 is a ceiling, not a measurement.

V6_TRUST_PV_RUNG12 = {"low": 660555.7514886515,
                      "central": 1321111.502977303,
                      "high": 2201852.504962172}
# unit: dollars, net cost to the trust, PV at 6/30/2025.
# direction of error: the 12-month rung is the CHEAP END of the retirement window.
#   Measured bounds from MOO-85 §4: uniform across the permissible dates +7.5%,
#   front-loaded 2:1 +8.6%, all at the earliest permissible date +16.3%. Every
#   deviation is dearer; the exposure is one-sided.

V6_TRUST_NOMINAL_RUNG12 = {"low": 834339.2430846596,
                           "central": 1668678.4861693191,
                           "high": 2781130.8102821987}
# unit: dollars, undiscounted.

V6_CERTIFIED_RESERVED_NOMINAL = {"low": 977339.9642755161,
                                 "central": 1954679.9285510322,
                                 "high": 3257799.8809183873}
# unit: dollars of certified subsidy reserved over the pilot, nominal, BEFORE the
#   mandatory contingency. This is the quantity § 51.1-142.4 D 2 meters, and it is
#   NOT the trust cost. Certification is on the anticipated EARLIEST qualifying
#   retirement date, which the retirement window does not move — so the 12-month
#   rung does not ease the $3,000,000 (MOO-183 §3).

AUTHORISED_LADDER_PV = {
    # rung (months): trust cost PV, central take-up, dollars
    0:  1567024,
    1:  1547336,
    6:  1446675,
    12: 1321112,
    18: 1190510,
    24: 1055048,
}
# source: the authorised ladder as stated in the MOO-199 description, which is the
#   MOO-32 v6 deadline ladder. Rung 12 agrees with V6_TRUST_PV_RUNG12['central'] to
#   50 cents, which is the only cross-check available on it.
# unit: dollars, PV at 6/30/2025, central take-up.
# direction of error: as V6_TRUST_PV_RUNG12 — rung 12 is the cheap end.
AUTHORISED_LADDER_TOL = 0.51

AUTHORISED_RUNG_MONTHS = 12
# unit: months. source: the board's controlling basis (MOO-85, MOO-71 §3).
# direction of error: none; a choice of basis, not an estimate.

PUBLISHED_RUNG_MONTHS = 6
# unit: months. source: inputs.RETIREMENT_DEADLINE_MONTHS in the published engine.
#   The basis every §3 scoreboard cost figure, and the printed $64,678, sits on.

STATUTORY_INTEREST = 0.0600
# unit: fraction per annum, compounded annually. source: live bill text, document
#   revision 76 — "six percent per annum, compounded annually". Verified at MOO-183.
# direction of error: none; it is a decided dial, not an estimate.

# ===========================================================================
# D. THE CAP, AND THE CONTINGENCY THAT RIDES INSIDE IT
# ===========================================================================

AGGREGATE_CAP = 3_000_000
# unit: dollars of certified subsidy reserved over the pilot, cumulative.
# source: § 51.1-142.4 D 2, live text at document revision 76. Verified at MOO-183.

CONTINGENCY_RATE = 0.20
# unit: fraction of certified subsidy, reserved IN ADDITION to each subsidy and
#   counted INSIDE the $3,000,000 (MOO-72 register item E; bill-text-s8 D 2 and D 3).
# source: live bill text — "the mandatory 20 percent contingency", quoted in the
#   live register at moo191-rev64/live-body.md and moo97-rev69/live.md.
# direction of error: none; a drafted figure. It is the reason cap utilisation is
#   1.20 x certified subsidy and not 1.00 x, and it is why the cap binds at high
#   take-up on a reservation aggregate that is below $3,000,000.

PER_ELECTION_CEILING = 170_000
# unit: dollars of certified subsidy per election. source: § 51.1-142.4 D 2, live
#   text, board-confirmed. With the contingency, $204,000 against the $3,000,000.

CAP_SWEEP_DIAL = (1_500_000, 2_000_000, 2_500_000, 3_000_000, 3_500_000,
                  4_000_000, 5_000_000, 6_000_000)
# unit: dollars. The dial positions the export publishes. Analyst choice of grid;
#   $3,000,000 is the drafted value and is marked as such.

# ===========================================================================
# E. THE IMPLEMENTATION ALLOWANCE, AND THE NUMERATOR CONVENTION
# ===========================================================================

IMPLEMENTATION_ALLOWANCE = 375_000
# unit: dollars, one-time, nongeneral fund, FY2029.
# source: ANALYST JUDGMENT, defensible $150,000-$750,000. No position count is
#   modelled. Same value in every design, so it moves levels and never rankings.
# direction of error: two-sided, and wide. It is 28% of the authorised per-
#   participant figure once spread over 18.3965 participants, which is why the
#   convention has to be stated rather than assumed.

NUMERATOR_CONVENTION = "T"
# "T" = trust-only: the denominator of the workforce exchange is net trust cost per
#       participant, EXCLUDING the implementation allowance.
# "A" = all-in: the allowance is spread over the participant count and added.
# CHOSEN: T, and the reasons are in the deliverable §2.1. In one line: the printed
#   $64,678 was a trust-only figure, so T makes the revision a ONE-DRIVER change
#   (the design anchor) that a reader can audit; and the allowance is a fixed cost
#   that does not scale with participants, so pairing it with a per-participant
#   flow mixes units. Convention A is reported as a stated alternative at every
#   headline so the level shift is visible. It changes no ranking (MOO-183 §6).

GF_SHARE = 0.47
# unit: fraction of trust-cost amortisation borne by the general fund.
# source: engine inputs.GF_SHARE. Applies to the amortisation of trust cost only;
#   the implementation allowance is wholly nongeneral fund (MOO-183 §8).

# ===========================================================================
# F. THE WORKFORCE EXCHANGE — the dials, and the three cases
# ===========================================================================
# Every component rate (employer DB, GLI, HIC, VSDP, FICA, Hybrid DC, Plan 1 and
# Hybrid normal cost, UAAL, admin) lives in engine/inputs.py and engine/workforce.py
# and is NOT restated here, because restating it would create a second source of
# truth for a number the engine already owns. The run transcript prints each one it
# uses, with the engine's own source string.

WORKFORCE_CASES = {
    # case: (replacement differential, vacancy coverage cost share, productivity
    #        ramp loss as a fraction of replacement salary, recruitment cost per
    #        hire, timing-shift-only)
    "conservative": (0.08, 0.90, 0.40, 8000, False),
    "central":      (0.18, 0.55, 0.25, 5000, False),
    "optimistic":   (0.30, 0.25, 0.10, 3000, True),
}
# source: engine/workforce.py case_table — the published case structure, reproduced
#   here verbatim so this run uses the same three cases the package printed.
#   REPLACEMENT_DIFFERENTIAL {0.08, 0.18, 0.30} is engine inputs; the coverage,
#   ramp and recruitment values are the case_table ladder.
# direction of error: the conservative case charges the full recruitment cost and
#   productivity ramp against every participant even where the retirement is a pure
#   timing shift; the optimistic case charges none. The truth is inside, and there is
#   no Virginia-specific anchor for where.

BREAKEVEN_DIFF_GRID = (0.08, 0.13, 0.18, 0.24, 0.30)
BREAKEVEN_MONTHS_GRID = (12, 24, 33, 45, 57, 69)
# unit: fraction below incumbent salary; months of acceleration. Analyst choice of
#   grid. The months grid is centred on the authorised design's own measured
#   acceleration rather than on the published engine's 6-month default, because the
#   authorised figure is 44.9 months and a grid topping out at 24 would not contain
#   the answer.

ACCELERATION_SOURCE = "measured_from_the_recommended_design_run"
# The workforce leg's months of acceleration is taken from the SAME run that
#   produces the pension leg, not from engine inputs.MONTHS_ACCELERATION
#   ({2, 6, 14} months). That is what makes the exchange internally consistent, and
#   it is what the printed exchange did for S1 (lock B3 reproduces it on that basis).
# direction of error on carrying the MOO-48 cohort's acceleration to the authorised
#   anchor: the no-advance bar of clause (vii) refuses members whose purchase
#   advances unreduced eligibility by less than one month, i.e. it removes the
#   LEAST-accelerated band. So the authorised cohort's own mean acceleration is at or
#   above the MOO-48 cohort's 44.85 months, and every coverage percentage this model
#   reports on that proxy is a LOWER BOUND on the authorised figure.

# ===========================================================================
# G. THE PV / NOMINAL MISMATCH IN THE EXCHANGE, AS INHERITED
# ===========================================================================

ENGINE_DISCOUNT_RATE = 0.0675
# unit: fraction per annum. source: engine inputs.DISCOUNT_RATE / v2_scenarios.I_NOM.
#   The rate every pension figure in this package is discounted at, to 6/30/2025.

WORKFORCE_LEG_IS_NOMINAL = True
# The pension leg is a PV at 6/30/2025. The workforce leg out of
#   engine/workforce.py is an UNDISCOUNTED nominal flow over the acceleration
#   window, which begins years after the valuation date. The printed exchange
#   compared the two directly. This run reports the exchange on the printed
#   (undiscounted) convention as the primary, because that is the one-driver
#   comparison the issue asks for, AND reports a PV-consistent variant, because the
#   mismatch is large enough to change the answer's direction.
# direction of error: comparing a nominal flow to a PV OVERSTATES the workforce leg.

PV_ADJUSTMENT_METHOD = (
    "Each election's workforce saving is discounted at ENGINE_DISCOUNT_RATE from the "
    "midpoint of its acceleration window back to 6/30/2025. The window is taken to "
    "open at the election month plus the central purchase-completion window plus the "
    "retirement rung, which is the earliest date the design permits the member to "
    "retire. STATED APPROXIMATION, not a measurement: the engine does not expose a "
    "per-election retirement date, and the true opening date is at or after this one "
    "for every election. Direction of error: this adjustment is therefore an upper "
    "bound on the PV-consistent workforce leg."
)

# ===========================================================================
# H. STANDING CAVEATS THAT TRAVEL WITH EVERY FIGURE IN THIS RUN
# ===========================================================================

CAVEATS = (
    "Two significant figures. No figure in this package is a VRS actuarial result.",
    "Participant counts are MODELED DEMAND, not actual cap utilisation. No "
    "participant count in this programme has an external anchor: no published count "
    "of purchases under § 51.1-142.2 exists.",
    "18.4 participants is an UPPER BOUND. Clause (viii) of \"eligible member\" is in "
    "the live draft at document revision 76 and in no committed run, and can only "
    "refuse more.",
    "The 12-month rung is the CHEAP END of the retirement window: +7.5% uniform "
    "across the permissible dates, +16.3% all at the earliest date (MOO-85 §4).",
    "S8 publication restriction: the S8 family's comparative dollar cells at statutory "
    "interest rates other than the decided 6.00% are internal under the board's "
    "standing restriction. Every such row in this run is tagged "
    "publication_restricted = true and must not reach a sponsor-facing artifact. "
    "Participant counts are not dollar figures.",
    "Pre-decisional and internal. Release is the Policy Director's decision.",
)

S8_RESTRICTED_RATES_EXCLUDE = 0.0600
# The board's standing publication restriction covers the S8 scenario family's
#   comparative dollar cells at statutory interest rates OTHER than the decided
#   6.00% — the restriction MOO-183 §9 invoked over its S8-at-4.00% and
#   S8-at-5.00% rows. The recommended design's own figures AT 6.00% are not
#   restricted: they are the bill's figures on the authorised basis, which is what
#   the ten sponsor documents print.
# Enforced in code: every interest-dial row at a rate other than 6.00% is tagged
#   publication_restricted = true in the export and in every CSV, and the
#   deliverable states the consequence for the interactive model — a LIVE interest
#   dial in a sponsor-facing artifact exposes restricted figures to anyone who moves
#   it. That is a design constraint on the product, not a note.
