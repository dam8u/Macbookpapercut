"""
MOO-183 — assumption register and lock set for the five uncovered scoreboard rows,
the recommended row's aggregate on the authorised 12-month rung, and the $64,678
identity.

EVERY number this model treats as given appears in this file, once, with a unit, a
source, a vintage and a direction of error. `moo183_cpp.py` contains no magic numbers.

Pre-decisional and internal. No figure here is a VRS actuarial result. Nothing is
reliable beyond two significant figures (MOO-46 Decision 4).

Retrieval date for every Paperclip-internal source below: 12 October 2026.
"""

# ---------------------------------------------------------------------------
# A. WHAT IS MEASURED IN THIS RUN, AND WHAT IS CITED
#
# Measured here, by re-running the published repaired (v2) engine:
#   - participant counts and net trust cost for S1, S3, S5, S6, S8-i4, S8-i5, S8-i6
#     at low / central / high take-up, on the published basis;
#   - the same seven at a 12-month retirement rung (deadline_months=12), which is the
#     only number in this issue that did not already exist anywhere;
#   - repaired S1's trust cost per participant, which is the $64,678 question.
#
# Cited, not re-derived:
#   - the MOO-48 retirement-deadline ladder for the recommended design (its own engine
#     run, locked by MOO-85 §0 at every rung);
#   - the MOO-32 v6 figure set, which is the only run on the current statutory basis.
# ---------------------------------------------------------------------------

ENGINE_PROVENANCE = (
    "AgentCreated/v1.0/05-model-code-and-data/python — the published repaired (v2) "
    "engine as shipped with sponsor package v1.0. Copied into ./engine/ byte-for-byte; "
    "no line of it is modified by this issue. Its own transcript is "
    "AgentCreated/v1.0/05-model-code-and-data/run-logs/out_v2_run.txt."
)

# ---------------------------------------------------------------------------
# B. LOCKS — the published repaired figures this run must reproduce exactly.
#    Source: out_v2_scenarios.csv (sponsor package v1.0, outputs-csv-json/), which is
#    the file §5 of `model-s8-s9-repaired` (MOO-31) prints and §3 of the Scenario
#    Selection Memo scores on. Direction of error: none — these are locks, not inputs.
#    A mismatch means the engine or its inputs moved and the run must stop.
# ---------------------------------------------------------------------------

LOCK_TOL = 0.51  # dollars / hundredths of a participant; the CSV carries full precision

PUBLISHED = {
    # code: (participants low, central, high, trust low, trust central, trust high)
    "S1": (37.06883916255061, 79.22147132166214, 140.50877386370297,
           2422559.711247316, 5123905.434065103, 9004485.742726222),
    "S3": (27.481676848227554, 59.183087237594236, 105.6993233880104,
           1579219.5612339978, 3380695.0762184807, 6006055.233442513),
    "S5": (10.13491894238333, 22.803567620362156, 45.60713524072431,
           557976.2422062634, 1255446.544964066, 2510893.089928132),
    "S6": (42.31019836648359, 90.49988500673598, 160.6322888008416,
           2433775.685580768, 5149487.641893239, 9052373.187708512),
    "S8-i4": (39.71293788298184, 84.85416907107385, 150.47022830932562,
              2647914.1305173743, 5599029.809243501, 9837053.582976677),
    "S8-i5": (34.02331739439338, 72.66181452991162, 128.79356591417582,
              2159778.1203703103, 4563715.279251739, 8013135.529812243),
    "S8-i6": (29.15365777822701, 62.22963986729717, 110.251307593205,
              1730197.2533036307, 3652752.090836663, 6408546.45080553),
}

# The decomposition of repaired S1's gross liability, same CSV, same row. Used only to
# test the words "pension cost of the purchased service" against the quantity.
S1_GROSS = 6080336.7557684975          # unit: dollars, PV at 6/30/2025
S1_MEMBER_PAID = 956431.3217033731     # unit: dollars, PV
S1_SVC_COMPONENT = 1731760.9088353347  # unit: dollars, PV — service-credit content
S1_ACCEL_COMPONENT = 4348575.84693318  # unit: dollars, PV — earlier-commencement content

# The three printed sites of $64,678 in sponsor package v1.0 (08-markdown-sources/).
# Transcribed, not computed. Direction of error: none; this is the text.
PRINTED_64678 = 64678
PRINTED_64678_SITES = (
    ("04-fiscal-analysis.md", 250, "pension cost of the purchased service on the same basis"),
    ("02-policy-brief.md", 170, "Pension cost of the purchased service"),
    ("06-questions-and-answers.md", 62, "pension cost of $64,678 per participant on the same basis"),
)
SSM_3B_64678_LABEL = "S1 as drafted — cost per participant, §3b coverage table"

# ---------------------------------------------------------------------------
# C. THE RETIREMENT RUNG — the dial this issue turns on.
# ---------------------------------------------------------------------------

PUBLISHED_DEADLINE_MONTHS = 6
# unit: months after the later of purchase completion and eligibility.
# source: `inputs.RETIREMENT_DEADLINE_MONTHS` in the published engine, value 6. This is
#   the basis EVERY cost figure in the §3 scoreboard and the §3b coverage table sits on.
# direction of error: a LONGER permitted delay lowers cost (measured, not assumed).

AUTHORISED_RUNG_MONTHS = 12
# unit: months, same dial.
# source: the board's controlling basis — MOO-85 (the 12-month rung priced for the
#   recommended design) and MOO-71 §3. Carried into this issue by its own description.
# direction of error: none; it is a choice of basis, not an estimate.

# ---------------------------------------------------------------------------
# D. THE RECOMMENDED ROW — cited from the MOO-48 engine run, not re-derived here.
#    Source: out_moo48_deadline_ladder.csv and out_moo48_summary.json, sponsor package
#    v1.0; locked rung-by-rung by MOO-85 §0 and reproduced to the dollar in MOO-48 §2.
#    Basis: Pathway A only, narrow clause (vi) reading, statutory interest 6.00%,
#    bill-text-s8 store revision 21 read for subsection C, WITHOUT §7 item 22 option (c)
#    and WITHOUT the no-advance bar.
# ---------------------------------------------------------------------------

MOO48_PARTICIPANTS = {"low": 9.452951873201249,
                      "central": 18.905903746402497,
                      "high": 31.509839577337704}
# unit: member elections over the 48-month pilot. Rung-INVARIANT: the same value at
#   every rung of the ladder, because the retirement deadline does not change who the
#   bill admits (MOO-48 §3; MOO-85 §1 "the window admits no one new").
# direction of error: modeled demand, not observed take-up. No external anchor exists.

MOO48_LADDER = {
    # rung (months): (trust cost PV low, central, high, mean acceleration months,
    #                 certified subsidy aggregate nominal)
    0:  (830909.35148502, 1661818.70297004, 2769697.8382834056, 56.85161523952638, 2105762.745331074),
    1:  (820911.8936185322, 1641823.7872370644, 2736372.978728435, 55.85161523952625, 2080445.921957173),
    6:  (769788.0481337646, 1539576.0962675293, 2565960.1604458787, 50.851615239526225, 1950979.0724016451),
    12: (705994.0462162767, 1411988.0924325534, 2353313.487387581, 44.85161523952625, 1789416.5780305462),
    18: (639617.403410847, 1279234.806821694, 2132058.011369493, 38.85161523952607, 1621303.956316947),
    24: (570747.8378511794, 1141495.6757023588, 1902492.7928372638, 32.88554063420059, 1447059.4517007023),
}
MOO48_BILL_RUNG = 1
# source: MOO-48 §2 — "You labelled rung 0 'as drafted'. The drafted text is rung 1."

# The two aggregates the issue describes as "15% apart", exactly as it states them.
CIRCULATING_AGGREGATE = 1661819          # what the ten sponsor documents print
CIRCULATING_RANGE = (830909, 2769698)
AUTHORISED_LADDER_AGGREGATE = 1411988    # MOO-85, the 12-month rung

# ---------------------------------------------------------------------------
# E. THE CURRENT STATUTORY BASIS — the only run that exists on it.
#    Source: out_moo32_v6_basis.json / out_moo32_v6_funnel_C6.csv /
#    out_moo32_v6_deadline_ladder.csv, in AgentCreated/_review-MOO-32-charts-v6/
#    (a review copy, NOT a published version folder). Basis: §7 item 22 option (c) —
#    subsection C clause (ii) measured at the filing date — PLUS the no-advance bar;
#    retirement rung 12; interest 6.00%; bill-text-s8 revision 19 for the retirement
#    window, revision 21 read for subsection C and D 4.
# ---------------------------------------------------------------------------

V6_PARTICIPANTS = {"low": 9.19824819071555,
                   "central": 18.3964963814311,
                   "high": 30.66082730238517}
V6_TRUST_PV_RUNG12 = {"low": 660555.7514886515,
                      "central": 1321111.502977303,
                      "high": 2201852.504962172}
V6_TRUST_NOMINAL_RUNG12 = {"low": 834339.2430846596,
                           "central": 1668678.4861693191,
                           "high": 2781130.8102821987}
V6_CERTIFIED_RESERVED_NOMINAL = {"low": 977339.9642755161,
                                 "central": 1954679.9285510322,
                                 "high": 3257799.8809183873}
V6_IMPLEMENTATION_NGF = 375000
# unit: dollars, one-time, nongeneral fund, FY2029. ANALYST JUDGMENT, defensible
#   $150,000–$750,000; no position count is modelled. Same value in every scenario, so
#   it never changes a ranking, only a level.
V6_MOO71_ARITHMETIC_CENTRAL = 17.93
# The count MOO-71 authorised "by arithmetic rather than measurement" and asked to have
# confirmed or corrected. v6 corrects it to 18.3965: the 1.0148 no-advance band was
# subtracted from 18.9483, which had already removed 0.4631 of that band under the
# zero-month bar. At two significant figures the authorised headline (18, range 9 to 30)
# is unchanged.

# ---------------------------------------------------------------------------
# F. STATUTORY PARAMETERS VERIFIED AGAINST THE LIVE TEXT TODAY
#    bill-text-s8 (MOO-42) document revision 76 / store revision 61, 271,611 characters
#    (the same figures MOO-141 §2 verified from the document store on 12 October 2026).
#    These are presence-and-value checks on the dials this model uses. Whether each
#    provision still READS the way the model screens it is a question for Statutory
#    Researcher, not for me.
# ---------------------------------------------------------------------------

LIVE_TEXT_CHECKS = {
    "statutory interest": ("six percent per annum, compounded annually", "6.00% as modelled"),
    "aggregate cap (D 2)": ("$3,000,000", "unchanged"),
    "per-election ceiling (D 2)": ("$170,000", "unchanged"),
    "completion window (E)": ("no later than 12 months after the Board accepts the election",
                              "unchanged"),
    "earliest qualifying retirement date": ("first day of the month following the month in which "
                                            "the Board credits the service credit", "= ladder rung 1"),
    "final qualifying retirement date": ("12 months after the earliest qualifying retirement date, "
                                         "extendable", "= ladder rung 13, with extensions"),
    "clause (ii) of subsection C": ("as of the filing date of the member's complete application",
                                    "option (c) is IN the live text"),
    "zero-month bar (C)": ("the Board shall not accept an election for which the amount determined "
                           "under clause (ii) is zero", "present"),
    "no-advance bar": ("eligible member clause (vii) — 'at least one month earlier'", "present"),
    "a screen no run has measured": ("eligible member clause (viii)", "NOT in any committed run"),
}
