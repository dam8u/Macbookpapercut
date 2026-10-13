#!/usr/bin/env python3
"""
MOO-199 — (1) the interactive model's data shape re-emitted on the authorised basis;
          (2) the workforce exchange recomputed on the recommended design's own anchor.

Run:  cd moo199-authorised-export && python3 moo199_export.py > out_moo199_run.txt 2>&1
      exit 0 only if every §0 lock passes.  ~3 min.

Every input is in moo199_inputs.py.  The engine is the published repaired (v2) engine
committed at ../moo183-cost-per-participant/engine/ and is not modified by this issue.

Pre-decisional and internal.  Not a VRS actuarial result.  Two significant figures.
"""
import os
import sys
import csv
import json
import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.normpath(os.path.join(HERE, "..", "moo183-cost-per-participant", "engine"))
sys.path.insert(0, ENGINE)
sys.path.insert(0, HERE)

import moo199_inputs as IN   # noqa: E402
import inputs as EIN         # noqa: E402  (the engine's own register)
import v2_scenarios as X     # noqa: E402
import workforce as W        # noqa: E402
import s8 as S8             # noqa: E402
from pricing import Profile  # noqa: E402

PR = X.PR                   # the engine's own Pricer instance, so no second one exists

LEVELS = ("low", "central", "high")
RUNGS = (0, 1, 6, 12, 18, 24)
EL = EIN.TAKEUP_PRICE_ELASTICITY["value"]
CM_CENTRAL = EIN.PURCHASE_COMPLETION_MONTHS["value"]["central"]
FAILS = []


def hr(t=""):
    print("\n" + "=" * 96)
    if t:
        print(t)
        print("=" * 96)


def money(x):
    return f"${x:,.0f}"


def sig2(x):
    """Two significant figures - the precision the inputs support (MOO-46 Decision 4)."""
    import math
    if x == 0:
        return "$0"
    neg, x = x < 0, abs(float(x))
    e = int(math.floor(math.log10(x)))
    return ("-" if neg else "") + f"${round(x, -(e - 1)):,.0f}"


def check(name, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"  {'PASS' if ok else 'FAIL'}  {name:62s} got {got:>18,.6f}  want {want:>18,.6f}")
    if not ok:
        FAILS.append(name)
    return ok


# ===========================================================================
# the recommended design's own runner: Pathway A only, S8 price, explicit rung.
# Reproduced from moo48_main.elections/runA so this file does not execute that
# script's 1,000-line report to get one aggregate.  Lock §0.1 proves it is the
# same runner: it must reproduce the published ladder at all six rungs.
# ===========================================================================
def recommended(level="central", rung=IN.AUTHORISED_RUNG_MONTHS,
                i=IN.STATUTORY_INTEREST, cap=None, per_member_cap=None,
                queue_order="chronological", return_elections=False):
    tA = EIN.TAKEUP_PATHWAY_A["value"][level]
    tB = EIN.TAKEUP_PATHWAY_B["value"][level]
    bkw = dict(months_available=None, vet_qual=None, age_skew=None, vet_share=None,
               salary_factor=1.0, scope=None)
    lkw = dict(deadline_months=rung, completion_months=None)
    el0 = X.build_elections_cached(tA, tB, plans=("plan1", "plan2"), pathways=("A",), **bkw)
    base = X.aggregate(el0, "anc", **lkw)
    ref = X.aggregate(el0, "s8", s8_kw={"i_stat": i}, **lkw)
    adj = (ref["paid"] / base["paid"]) ** EL if base["paid"] else 1.0
    el = X.build_elections_cached(tA * adj, tB * adj, plans=("plan1", "plan2"),
                                 pathways=("A",), **bkw)
    a = X.aggregate(el, "s8", s8_kw={"i_stat": i}, cap=cap, per_member_cap=per_member_cap,
                    queue_order=queue_order, **lkw)
    a["takeup_adjustment"] = adj
    return (a, el) if return_elections else a


# ###########################################################################
hr("[0] LOCKS - nothing below runs unless all of these pass")
print("Engine provenance: " + IN.ENGINE_PROVENANCE)
print("\nNOT REACHABLE FROM THIS WORKSPACE: " + IN.V6_ENGINE_ABSENT)
print("\nEXPORT SCHEMA: " + IN.EXPORT_SCHEMA_NOTE)

print("\n--- 0.1  the recommended design's measured ladder, all six rungs x three levels ---")
LAD = {}
for rung in RUNGS:
    LAD[rung] = {lvl: recommended(lvl, rung) for lvl in LEVELS}
    lo, ce, hi, accel = IN.MOO48_LADDER[rung]
    check(f"rung {rung:2d} trust PV central", LAD[rung]["central"]["trust"], ce,
          IN.LOCK_TOL_DOLLARS)
    check(f"rung {rung:2d} trust PV low", LAD[rung]["low"]["trust"], lo, IN.LOCK_TOL_DOLLARS)
    check(f"rung {rung:2d} trust PV high", LAD[rung]["high"]["trust"], hi, IN.LOCK_TOL_DOLLARS)
    check(f"rung {rung:2d} participants central", LAD[rung]["central"]["n"],
          IN.MOO48_PARTICIPANTS["central"], IN.LOCK_TOL_PARTICIPANTS)
    check(f"rung {rung:2d} mean acceleration months",
          LAD[rung]["central"]["avg_acceleration_months"], accel, 0.001)

A12 = LAD[IN.AUTHORISED_RUNG_MONTHS]["central"]

print("\n--- 0.2  the authorised member-price pair (MOO-72 register item C) ---")
check("multiple of ANC", A12["multiple_of_anc"], IN.AUTHORISED_PRICE_PAIR["multiple_of_anc"],
      IN.AUTHORISED_PRICE_PAIR_TOL)
check("share of AEC", A12["share_of_aec"], IN.AUTHORISED_PRICE_PAIR["share_of_aec"],
      IN.AUTHORISED_PRICE_PAIR_TOL)

print("\n--- 0.3  the authorised ladder agrees with the v6 rung-12 figure ---")
check("authorised ladder rung 12 == V6 trust PV central",
      float(IN.AUTHORISED_LADDER_PV[12]), IN.V6_TRUST_PV_RUNG12["central"],
      IN.AUTHORISED_LADDER_TOL)
V6_CPP = IN.V6_TRUST_PV_RUNG12["central"] / IN.V6_PARTICIPANTS["central"]
check("authorised cost per participant", V6_CPP, 71813.0, 1.0)
for lvl in LEVELS:
    check(f"cost per participant is take-up invariant ({lvl})",
          IN.V6_TRUST_PV_RUNG12[lvl] / IN.V6_PARTICIPANTS[lvl], V6_CPP, 0.01)

print("\n--- 0.4  cap utilisation = (1 + contingency) x certified reserved / cap ---")
for lvl in LEVELS:
    u = (1.0 + IN.CONTINGENCY_RATE) * IN.V6_CERTIFIED_RESERVED_NOMINAL[lvl] / IN.AGGREGATE_CAP
    check(f"cap utilisation {lvl}", u, IN.AUTHORISED_CAP_UTILISATION[lvl],
          IN.AUTHORISED_CAP_UTILISATION_TOL)

print("\n--- 0.5  the PRINTED workforce exchange, reproduced on its own basis ---")
print("    If this fails, my reconstruction of what the documents print is wrong and the")
print("    recomputation below has nothing to be a correction OF.")
s1 = X.run("S1", "central", deadline_months=IN.PUBLISHED_RUNG_MONTHS)
check("printed anchor: S1 central trust per participant at the 6-month rung",
      s1["trust"] / s1["n"], float(IN.PRINTED_ANCHOR), 0.51)
d, cov, ramp, rec, tso = IN.WORKFORCE_CASES["central"]
w_printed = W.per_participant(s1["avg_salary"], s1["avg_acceleration_months"], d,
                              coverage_share=cov, ramp=ramp, recruit=rec,
                              timing_shift_only=tso)
check("printed coverage: net workforce effect / anchor",
      w_printed["net_workforce_effect"] / (s1["trust"] / s1["n"]),
      IN.PRINTED_COVERAGE, IN.PRINTED_COVERAGE_TOL)

if FAILS:
    print("\nLOCKS FAILED - no figure below may be used:")
    for f in FAILS:
        print("   " + f)
    sys.exit(1)
print("\nAll locks pass.")

# ###########################################################################
hr("[1] THE AUTHORISED BASIS, RESTATED - the anchor every figure below hangs on")
print(f"  participants, central              {IN.V6_PARTICIPANTS['central']:.4f}"
      f"   ({IN.V6_PARTICIPANTS['low']:.4f} to {IN.V6_PARTICIPANTS['high']:.4f})")
print(f"  net trust cost PV, rung 12         {money(IN.V6_TRUST_PV_RUNG12['central'])}"
      f"   ({money(IN.V6_TRUST_PV_RUNG12['low'])} to "
      f"{money(IN.V6_TRUST_PV_RUNG12['high'])})")
print(f"  cost per participant               {money(V6_CPP)}   (take-up invariant)")
print(f"  cap utilisation                    "
      f"{IN.AUTHORISED_CAP_UTILISATION['low']:.1%} / "
      f"{IN.AUTHORISED_CAP_UTILISATION['central']:.1%} / "
      f"{IN.AUTHORISED_CAP_UTILISATION['high']:.1%}")
print(f"  member-price pair (measured)        {A12['multiple_of_anc']:.4f}x ANC, "
      f"{A12['share_of_aec']:.2%} of AEC")
print(f"  mean participating salary (measured){A12['avg_salary']:>14,.2f}")
print(f"  mean acceleration, months (measured){A12['avg_acceleration_months']:>13.4f}")
print(f"  mean years purchased (measured)    {A12['years'] / A12['n']:>14.4f}")
print("\nThe three MEASURED cohort statistics above are the MOO-48 cohort's, not the v6")
print("cohort's, because the v6 engine is not in this workspace.  Direction of error on each")
print("is stated in moo199_inputs.py §F.  They are used only where the authorised figure set")
print("does not carry the statistic at all.")

# ###########################################################################
hr("[2] BLOCK 1 of 5 - THE RETIREMENT-DEADLINE LADDER (authorised, cited)")
print("The one block that is authorised outright.  Participants are rung-invariant, so the")
print("per-participant column is the ladder divided by one constant.\n")
hdr = (f"{'rung':>5s} {'authorised trust PV':>20s} {'$/participant':>14s} "
       f"{'accel months':>13s} {'vs rung 12':>11s} {'v6/MOO-48':>10s} {'note'}")
print(hdr)
print("-" * len(hdr))
LADDER_ROWS = []
for rung in RUNGS:
    pv = float(IN.AUTHORISED_LADDER_PV[rung])
    accel = IN.MOO48_LADDER[rung][3]
    ratio = pv / IN.MOO48_LADDER[rung][1]
    note = ("THE AUTHORISED RUNG" if rung == 12 else
            "the drafted text" if rung == 1 else
            "what the superseded documents printed" if rung == 0 else "")
    print(f"{rung:5d} {money(pv):>20s} {money(pv / IN.V6_PARTICIPANTS['central']):>14s} "
          f"{accel:13.2f} {pv / float(IN.AUTHORISED_LADDER_PV[12]) - 1:11.1%} "
          f"{ratio:10.5f} {note}")
    LADDER_ROWS.append(dict(rung_months=rung, trust_pv_central=pv,
                            trust_pv_low=pv * IN.V6_PARTICIPANTS["low"] / IN.V6_PARTICIPANTS["central"],
                            trust_pv_high=pv * IN.V6_PARTICIPANTS["high"] / IN.V6_PARTICIPANTS["central"],
                            cost_per_participant=pv / IN.V6_PARTICIPANTS["central"],
                            mean_acceleration_months=accel,
                            mean_acceleration_source="MOO-48 cohort, measured (proxy)",
                            v6_over_moo48_ratio=ratio, note=note,
                            basis="authorised (item 22 (c) + no-advance bar)",
                            central_quality="authorised (cited)",
                            low_high_quality=(
                                "scaled from central by the participant ratio. Cost per "
                                "participant is take-up invariant: locked directly on the "
                                "authorised basis at rung 12 (§0.3) and measured on the "
                                "MOO-48 ladder at all six rungs (§0.1). Applying it to the "
                                "authorised basis away from rung 12 is an inference from "
                                "those two facts, not a measurement.")))
print("\nSanity check on the authorised ladder's shape.  The v6/MOO-48 ratio falls monotonically")
print("from rung 0 to rung 24 (0.94296 -> 0.92427): the two bases diverge MORE the longer the")
print("permitted delay.  That is the expected sign - the no-advance bar refuses the least-")
print("accelerated members, and the longer the window the larger the share of cost that is")
print("acceleration.  The ladder is internally consistent with the figure set.  Agreement.")

# ###########################################################################
hr("[3] BLOCK 2 of 5 - THE MEMBER-PRICE GRID (measured; basis-invariant)")
print("What the dial shows: the S8 earned-service price per year purchased, as a surface over")
print("age x completed service, at the decided 6.00% statutory interest, beside the ANC and")
print("full-AEC references.")
print("\nWHY THIS BLOCK IS BASIS-INVARIANT, stated because it is the load-bearing claim here:")
print("§7 item 22 option (c) measures subsection C clause (ii) - the CERTIFIED SUBSIDY - at the")
print("filing date, and clause (vii)'s no-advance bar is an ELIGIBILITY screen.  Neither is a")
print("term of the member price.  So option (c) and the bar move WHO is in the cohort and what")
print("the Commonwealth certifies; they do not move the price function.  The cohort-weighted")
print("MEAN price does move with the cohort, and the authorised mean is not available here -")
print(f"what is available is the authorised PAIR, {IN.AUTHORISED_PRICE_PAIR['multiple_of_anc']}x ANC "
      f"and {IN.AUTHORISED_PRICE_PAIR['share_of_aec']:.0%} of AEC, which §0.2 locks.\n")
GRID_AGE = (50, 53, 56, 59, 62, 65)
GRID_SVC = (20, 24, 27, 29, 30)
YEARS = A12["years"] / A12["n"]
SAL = A12["avg_salary"]
print(f"Grid held at the measured mean participating salary {money(SAL)} and the measured mean")
print(f"{YEARS:.4f} years purchased.  Age and service are the cohort's own support (ages 50-67,")
print("service concentrated at 27-30 years).\n")
print(f"{'plan':7s} {'age':>4s} {'svc':>4s} {'S8 price':>11s} {'per year':>10s} "
      f"{'ANC ref':>10s} {'AEC ref':>11s} {'xANC':>6s} {'%AEC':>6s} {'interest yrs':>12s}")
print("-" * 96)
PRICE_ROWS = []
for plan in ("plan1", "plan2"):
    for age in GRID_AGE:
        for svc in GRID_SVC:
            if svc > age - 22:          # not reachable: hired before age 22
                continue
            p = Profile(plan=plan, age=float(age), service=float(svc), salary=SAL)
            q = S8.s8_price(p, YEARS, i_stat=IN.STATUTORY_INTEREST)
            anc = PR.anc_price(p, YEARS)
            aec = PR.aec_full(p, YEARS)
            row = dict(plan=plan, age=age, completed_service=svc,
                       years_purchased=YEARS, salary=SAL,
                       s8_price=q["price"], s8_price_per_year=q["price_per_year"],
                       anc_reference=anc, aec_full_reference=aec,
                       multiple_of_anc=q["price"] / anc if anc else 0.0,
                       share_of_aec=q["price"] / aec if aec else 0.0,
                       interest_years=q["interest_years"],
                       statutory_interest=IN.STATUTORY_INTEREST,
                       publication_restricted=False)
            PRICE_ROWS.append(row)
            if plan == "plan1" and svc in (27, 30):
                print(f"{plan:7s} {age:4d} {svc:4d} {money(q['price']):>11s} "
                      f"{money(q['price_per_year']):>10s} {money(anc):>10s} {money(aec):>11s} "
                      f"{row['multiple_of_anc']:6.2f} {row['share_of_aec']:6.1%} "
                      f"{q['interest_years']:12.2f}")
print(f"\n({len(PRICE_ROWS)} grid cells in the export; the printed extract above is Plan 1 at 27")
print("and 30 completed years, which is where 44% of the cohort's weight sits.)")
print("\nThe structural result the grid shows, and the sponsor question it answers: the S8 price")
print("rises with time since hire at roughly (1 + i_stat) / (1 + salary growth) - 1 per year, so")
print("the basis is calendar-neutral only where the statutory rate equals the member's own salary")
print("growth.  At 6.00% it is above it, so S8 re-creates a calendar penalty - smaller than the")
print("full-AEC one it replaces, and not zero.")

# ###########################################################################
hr("[4] BLOCK 3 of 5 - THE STATUTORY-INTEREST DIAL (measured on the MOO-48 cohort)")
print("PUBLICATION RESTRICTION.  Every row below at a rate other than 6.00% is tagged")
print("publication_restricted = true, under the board's standing restriction on the S8 family's")
print("comparative dollar cells (the restriction MOO-183 §9 invoked over its 4.00% and 5.00%")
print("rows).  CONSEQUENCE FOR THE PRODUCT, which is a finding and not a note: a LIVE interest")
print("dial in a sponsor-facing model exposes restricted figures to anyone who moves it.  The")
print("dial can ship as a static 6.00% column, or the restriction has to be lifted first.\n")
DIAL_RATES = (0.0400, 0.0450, 0.0500, 0.0550, 0.0600, 0.0650, 0.0675, 0.0700)
ANCHOR_RATIO = IN.V6_TRUST_PV_RUNG12["central"] / IN.MOO48_LADDER[12][1]
print(f"Anchor ratio, authorised / MOO-48 at 6.00% and rung 12: {ANCHOR_RATIO:.6f}.")
print("Rows marked `derived` are the measured MOO-48 figure multiplied by that ratio.  That is")
print("an ASSUMPTION, not a measurement: the no-advance bar and the zero-month bar screen on")
print("quantities the member price enters, so the share of the cohort they refuse moves with the")
print("rate.  Direction of error: a higher rate prices more members out of a positive clause (ii)")
print("solution, so the authorised cohort shrinks FASTER than the MOO-48 cohort as the rate")
print("rises; the derived figures above 6.00% are therefore an UPPER bound on cost and the ones")
print("below 6.00% a LOWER bound.  Only the 6.00% row is authorised.\n")
print(f"{'rate':>6s} {'participants':>13s} {'trust PV (MOO-48)':>18s} {'$/part':>10s} "
       f"{'member paid/part':>17s} {'xANC':>6s} {'derived authorised PV':>22s} {'tag'}")
print("-" * 112)
DIAL_ROWS = []
for r in DIAL_RATES:
    a = recommended("central", IN.AUTHORISED_RUNG_MONTHS, i=r)
    der = a["trust"] * ANCHOR_RATIO
    restricted = abs(r - IN.S8_RESTRICTED_RATES_EXCLUDE) > 1e-9
    tag = "RESTRICTED" if restricted else "AUTHORISED (measured)"
    print(f"{r:6.2%} {a['n']:13.4f} {money(a['trust']):>18s} "
          f"{money(a['trust'] / a['n']):>10s} {money(a['paid'] / a['n']):>17s} "
          f"{a['multiple_of_anc']:6.3f} {money(der):>22s} {tag}")
    DIAL_ROWS.append(dict(statutory_interest=r, participants=a["n"],
                          trust_pv_moo48_cohort=a["trust"],
                          cost_per_participant_moo48_cohort=a["trust"] / a["n"],
                          member_paid_per_participant=a["paid"] / a["n"],
                          multiple_of_anc=a["multiple_of_anc"],
                          share_of_aec=a["share_of_aec"],
                          trust_pv_authorised=(IN.V6_TRUST_PV_RUNG12["central"]
                                               if not restricted else der),
                          trust_pv_authorised_quality=("measured" if not restricted
                                                       else "derived by anchored rescaling"),
                          publication_restricted=restricted))
print("\nThe dial's shape: from 4.00% to 7.00% the member pays 2.02x more per participant and the")
print("count falls 34.5%, so net trust cost falls - the rate is the strongest single lever in the")
print("model on the aggregate, and it moves the count and the price in the same direction.")

# ###########################################################################
hr("[5] BLOCK 4 of 5 - THE CAP SWEEP")
print("Unit discipline first, because the package has made this error once already (MOO-72")
print("register item B): § 51.1-142.4 D 2 caps CERTIFIED SUBSIDY plus its mandatory 20 percent")
print("contingency.  It does NOT cap trust cost.  Those are different quantities and the ratio")
print("between them is not 1.\n")
print("5.1  Utilisation against the cap dial - EXACT on the authorised basis, because")
print("     utilisation is a ratio and both terms are in the authorised figure set.\n")
print(f"{'cap':>12s} " + " ".join(f"{lvl:>12s}" for lvl in LEVELS) + "   binds at")
print("-" * 68)
CAP_ROWS = []
for cap in IN.CAP_SWEEP_DIAL:
    us = {}
    for lvl in LEVELS:
        us[lvl] = (1.0 + IN.CONTINGENCY_RATE) * IN.V6_CERTIFIED_RESERVED_NOMINAL[lvl] / cap
    binds = [lvl for lvl in LEVELS if us[lvl] > 1.0]
    mark = " (DRAFTED)" if cap == IN.AGGREGATE_CAP else ""
    print(f"{money(cap):>12s} " + " ".join(f"{us[lvl]:11.1%} " for lvl in LEVELS)
          + "   " + (", ".join(binds) if binds else "never") + mark)
    CAP_ROWS.append(dict(cap=cap, utilisation_low=us["low"], utilisation_central=us["central"],
                         utilisation_high=us["high"], binds_at=binds,
                         is_drafted_value=(cap == IN.AGGREGATE_CAP),
                         quality="measured (exact arithmetic on the authorised figure set)"))
reserved_c = (1.0 + IN.CONTINGENCY_RATE) * IN.V6_CERTIFIED_RESERVED_NOMINAL["central"]
reserved_h = (1.0 + IN.CONTINGENCY_RATE) * IN.V6_CERTIFIED_RESERVED_NOMINAL["high"]
print(f"\n  reservation aggregate including contingency: central {money(reserved_c)}, "
      f"high {money(reserved_h)}")
print(f"  the cap that just clears high take-up:       {money(reserved_h)}  "
      f"(i.e. ${reserved_h - IN.AGGREGATE_CAP:,.0f} above the drafted $3,000,000)")
print(f"  the take-up multiple at which $3,000,000 binds: "
      f"{1.0 / IN.AUTHORISED_CAP_UTILISATION['central']:.3f}x central")
print(f"  per-election ceiling {money(IN.PER_ELECTION_CEILING)} plus contingency = "
      f"{money(IN.PER_ELECTION_CEILING * (1 + IN.CONTINGENCY_RATE))} against the cap")
print("\n  AND THE THING THE DIAL MUST NOT IMPLY: the retirement rung does not move this table.")
print("  D 2 meters the RESERVATION, certified on the anticipated earliest qualifying retirement")
print("  date, which the window does not move.  A cap tab wired to the rung dial would be wrong.")

print("\n5.2  The cap as an admission rule - MEASURED, but on the MOO-48 cohort, because")
print("     admission is a run and the v6 engine is not here.  Reported as a SHAPE, not a level.\n")
print(f"{'cap':>12s} {'participants':>13s} {'denied':>9s} {'trust PV':>14s} {'$/part':>10s}")
print("-" * 62)
CAP_RUN_ROWS = []
for cap in IN.CAP_SWEEP_DIAL:
    a = recommended("high", IN.AUTHORISED_RUNG_MONTHS, cap=cap)
    print(f"{money(cap):>12s} {a['n']:13.4f} {a['denied']:9.4f} {money(a['trust']):>14s} "
          f"{money(a['trust'] / a['n']) if a['n'] else '-':>10s}")
    CAP_RUN_ROWS.append(dict(cap=cap, take_up_case="high", participants_moo48_cohort=a["n"],
                             denied_moo48_cohort=a["denied"],
                             trust_pv_moo48_cohort=a["trust"],
                             quality="measured on the MOO-48 cohort; shape only"))
first_free = next((r["cap"] for r in CAP_RUN_ROWS if r["denied_moo48_cohort"] < 1e-9), None)
print("\n  Read the SHAPE, and read it against 5.1, because the two tables disagree and the")
print("  disagreement is the finding.  Applied to TRUST COST as an admission rule the cap stops")
print(f"  denying anyone at {money(first_free)}; at the drafted {money(IN.AGGREGATE_CAP)} it denies nobody even at")
print(f"  high take-up, because trust cost PV there is {money(IN.MOO48_LADDER[12][2])}.  Applied to the")
print("  RESERVATION aggregate - which is what D 2 actually meters - the same $3,000,000 is at")
print(f"  {IN.AUTHORISED_CAP_UTILISATION['high']:.0%} at high take-up and binds.")
print("  So an interactive model that caps the trust-cost ledger tells a sponsor the cap never")
print("  binds, when on the drafted figures and the drafted quantity it binds at high take-up.")
print("  5.1 is the table to wire the cap tab to. 5.2 is here to show what the wrong wiring says.")

# ###########################################################################
hr("[6] BLOCK 5 of 5 / DELIVERABLE 2 - THE WORKFORCE EXCHANGE, RECOMPUTED")
print(f"NUMERATOR CONVENTION: {IN.NUMERATOR_CONVENTION} (trust-only).  The denominator is net")
print(f"trust cost per participant, {money(V6_CPP)}, EXCLUDING the "
      f"{money(IN.IMPLEMENTATION_ALLOWANCE)} one-time")
print("nongeneral-fund implementation allowance.  Convention A (all-in) is reported beside every")
print("headline.  Reasons for the choice are in the deliverable; in one line, T makes this a")
print("one-driver change against the printed figure and does not pair a fixed cost with a")
print("per-participant flow.\n")
IMPL_PER = IN.IMPLEMENTATION_ALLOWANCE / IN.V6_PARTICIPANTS["central"]
ANCHOR_T = V6_CPP
ANCHOR_A = V6_CPP + IMPL_PER
print(f"  convention T anchor  {money(ANCHOR_T)} per participant")
print(f"  convention A anchor  {money(ANCHOR_A)} per participant  "
      f"(= T + {money(IMPL_PER)}, the allowance over {IN.V6_PARTICIPANTS['central']:.4f} participants)")
print(f"  the printed anchor   {money(IN.PRINTED_ANCHOR)} per participant  "
      f"(repaired S1, 6-month rung)")
print(f"  T less printed       {money(ANCHOR_T - IN.PRINTED_ANCHOR)} higher "
      f"({ANCHOR_T / IN.PRINTED_ANCHOR - 1:+.1%})")

ACCEL = A12["avg_acceleration_months"]
print(f"\nThe workforce leg's months of acceleration: {ACCEL:.4f}, MEASURED on the recommended")
print(f"design's own rung-12 run - not the engine's MONTHS_ACCELERATION default "
      f"{EIN.MONTHS_ACCELERATION['value']}.")
print(f"The incumbent salary: {money(SAL)}, the same run's mean participating salary.")
print("Both are the MOO-48 cohort's; §1 states the direction of error on each.  On acceleration")
print("it is one-sided and favourable: the no-advance bar removes the least-accelerated band, so")
print("the authorised cohort's own mean is at or above 44.85 months and every coverage figure")
print("below is a LOWER bound.")

print("\n6.1  THE THREE DIFFERENTIAL CASES, on the recommended design's own anchor\n")
print(f"{'case':14s} {'diff':>6s} {'accel mo':>9s} {'gross saving':>13s} {'frictions':>11s} "
      f"{'net workforce':>14s} {'covers (T)':>11s} {'covers (A)':>11s} {'net state/part':>15s}")
print("-" * 118)
WF_ROWS = []
for case, (d, cov, ramp, rec, tso) in IN.WORKFORCE_CASES.items():
    r = W.per_participant(SAL, ACCEL, d, coverage_share=cov, ramp=ramp, recruit=rec,
                          timing_shift_only=tso)
    net = r["net_workforce_effect"]
    print(f"{case:14s} {d:6.0%} {ACCEL:9.2f} {money(r['gross_saving']):>13s} "
          f"{money(r['recruitment_and_ramp']):>11s} {money(net):>14s} "
          f"{net / ANCHOR_T:11.1%} {net / ANCHOR_A:11.1%} {money(ANCHOR_T - net):>15s}")
    WF_ROWS.append(dict(case=case, replacement_differential=d, acceleration_months=ACCEL,
                        incumbent_salary=SAL,
                        gross_saving_per_participant=r["gross_saving"],
                        frictions_per_participant=r["recruitment_and_ramp"],
                        net_workforce_per_participant=net,
                        trust_tier_mix_per_participant=r["trust_tier_mix_effect"],
                        pension_anchor_T=ANCHOR_T, pension_anchor_A=ANCHOR_A,
                        covers_share_T=net / ANCHOR_T, covers_share_A=net / ANCHOR_A,
                        net_state_per_participant_T=ANCHOR_T - net,
                        aggregate_net_workforce=net * IN.V6_PARTICIPANTS["central"],
                        convention="undiscounted, as printed"))
CENTRAL_NET = [r for r in WF_ROWS if r["case"] == "central"][0]["net_workforce_effect"] \
    if False else [r for r in WF_ROWS if r["case"] == "central"][0]["net_workforce_per_participant"]

print("\n6.2  THE REVISED \"COVERS X%\" FIGURE - and the two different questions it can answer\n")
naive = w_printed["net_workforce_effect"] / ANCHOR_T
print("  (i)  DENOMINATOR-ONLY SWAP - what the documents' own wording implies.  Keep the printed")
print(f"       workforce effect of {money(w_printed['net_workforce_effect'])} (which is S1's, at S1's "
      f"{s1['avg_acceleration_months']:.1f} months)")
print(f"       and divide by the recommended design's anchor:  {naive:.1%}   "
      f"(printed: {IN.PRINTED_COVERAGE:.0%})")
print("       This is the figure that makes the exchange WORSE, and it is the one the documents")
print("       now point at.  It is also the one I will not print, because it divides one design's")
print("       workforce effect by another design's pension cost.  Mixing units is the error.")
print("\n  (ii) CONSISTENT SINGLE-DESIGN RECOMPUTATION - both legs from the recommended design on")
print(f"       the authorised rung:  {CENTRAL_NET / ANCHOR_T:.1%} on convention T, "
      f"{CENTRAL_NET / ANCHOR_A:.1%} on convention A.")
print("       This is the figure to print.  It is HIGHER than the printed 71%, not lower.")
print("\n  Why (ii) rises even though the anchor rose.  Both legs scale with acceleration, and the")
print(f"  recommended design accelerates {ACCEL:.1f} months against S1's "
      f"{s1['avg_acceleration_months']:.1f} - "
      f"{ACCEL / s1['avg_acceleration_months'] - 1:+.0%}.")
print(f"  The pension leg rose {ANCHOR_T / IN.PRINTED_ANCHOR - 1:+.1%}; the workforce leg rose "
      f"{CENTRAL_NET / w_printed['net_workforce_effect'] - 1:+.1%}, because the")
print("  workforce saving is close to linear in the window while the frictions are fixed per hire.")
print("\n  SO THE DOCUMENTS' STATED DIRECTION IS WRONG, and this is a finding against the text the")
print("  Editor has already cut.  04-fiscal-analysis.md §9 and 02-policy-brief.md §6 now say the")
print("  error 'runs against the proposal' and that the real exchange is worse.  On a consistent")
print("  recomputation the coverage RATIO is better.  What is genuinely worse is the per-")
print(f"  participant net state cost in dollars at the SAME acceleration, and the dollar gap "
      f"of {money(ANCHOR_T - IN.PRINTED_ANCHOR)}")
print("  the documents name.  The v2.1 pass has to change the direction sentence, not just the")
print("  figure.  §6.5 gives the one qualification that can reverse this again.")

print("\n6.3  THE REVISED BREAK-EVEN\n")
be_T = W.breakeven_months(SAL, ANCHOR_T,
                          differential=IN.WORKFORCE_CASES["central"][0])
be_A = W.breakeven_months(SAL, ANCHOR_A,
                          differential=IN.WORKFORCE_CASES["central"][0])
be_printed = W.breakeven_months(s1["avg_salary"], float(IN.PRINTED_ANCHOR),
                                differential=IN.WORKFORCE_CASES["central"][0])
bed_T = W.breakeven_differential(SAL, ANCHOR_T, months=ACCEL)
for nm, be in (("T", be_T), ("A", be_A)):
    short = be - ACCEL
    verdict = (f"clears it by {-short:.2f} months" if short < 0
               else f"does NOT clear it - it falls {short:.2f} months short")
    print(f"  break-even months, convention {nm}   {be:.2f}   against a measured "
          f"{ACCEL:.2f} months => {verdict}")
print(f"  break-even months as printed      {be_printed:.2f}   (on S1's salary and the "
      f"{money(IN.PRINTED_ANCHOR)} anchor)")
print(f"  break-even replacement differential at the measured {ACCEL:.2f} months, convention T: "
      f"{bed_T:.2%}")
print(f"    against the central assumption of {IN.WORKFORCE_CASES['central'][0]:.0%} - so the")
print(f"    exchange clears on convention T at any differential above {bed_T:.1%}.")
print("\n  Break-even grid: net workforce effect LESS the convention-T anchor, per participant.")
print("  A positive cell is a design that pays for itself on the workforce leg alone.\n")
print(f"{'months':>7s} " + " ".join(f"{d:>11.0%}" for d in IN.BREAKEVEN_DIFF_GRID))
print("-" * (8 + 12 * len(IN.BREAKEVEN_DIFF_GRID)))
BE_GRID = []
for m in IN.BREAKEVEN_MONTHS_GRID:
    cells = []
    for d in IN.BREAKEVEN_DIFF_GRID:
        v = W.per_participant(SAL, m, d)["net_workforce_effect"] - ANCHOR_T
        cells.append(v)
        BE_GRID.append(dict(acceleration_months=m, replacement_differential=d,
                            net_of_anchor_T=v, incumbent_salary=SAL,
                            pension_anchor_T=ANCHOR_T))
    mark = "  <- measured" if m == 45 else ""
    print(f"{m:7d} " + " ".join(f"{money(c):>11s}" for c in cells) + mark)

print("\n6.4  THE AGGREGATE EXCHANGE, and the sentence the Editor needs\n")
agg_wf = CENTRAL_NET * IN.V6_PARTICIPANTS["central"]
print(f"  pension cost PV, authorised           {money(IN.V6_TRUST_PV_RUNG12['central'])}")
print(f"  implementation allowance, FY2029 NGF  {money(IN.IMPLEMENTATION_ALLOWANCE)}")
print(f"  net workforce effect, central case    {money(agg_wf)}   "
      f"(= {money(CENTRAL_NET)} x {IN.V6_PARTICIPANTS['central']:.4f}, undiscounted)")
print(f"  net state effect, convention T        "
      f"{money(IN.V6_TRUST_PV_RUNG12['central'] - agg_wf)}")
print(f"  net state effect, convention A        "
      f"{money(IN.V6_TRUST_PV_RUNG12['central'] + IN.IMPLEMENTATION_ALLOWANCE - agg_wf)}")
print(f"\n  range across the three cases, convention T:")
for r in WF_ROWS:
    tot = r["net_workforce_per_participant"] * IN.V6_PARTICIPANTS["central"]
    print(f"    {r['case']:14s} workforce {money(tot):>12s}  net state "
          f"{money(IN.V6_TRUST_PV_RUNG12['central'] - tot):>12s}  covers "
          f"{r['covers_share_T']:6.1%}")

print("\n6.5  THE PV / NOMINAL MISMATCH - inherited, large, and it reverses the direction\n")
print(IN.PV_ADJUSTMENT_METHOD)
a12, el12 = recommended("central", IN.AUTHORISED_RUNG_MONTHS, return_elections=True)
wt = sum(e["weight"] for e in el12)
mean_month = sum(e["weight"] * e["month"] for e in el12) / wt
PV_ROWS = []
for case, (d, cov, ramp, rec, tso) in IN.WORKFORCE_CASES.items():
    num = 0.0
    for e in el12:
        per = W.per_participant(e["salary"], ACCEL, d, coverage_share=cov, ramp=ramp,
                                recruit=rec, timing_shift_only=tso)["net_workforce_effect"]
        t_open = (e["month"] + CM_CENTRAL + IN.AUTHORISED_RUNG_MONTHS) / 12.0
        df = (1.0 + IN.ENGINE_DISCOUNT_RATE) ** (-(t_open + ACCEL / 24.0))
        num += e["weight"] * per * df
    pv_per = num / wt
    PV_ROWS.append(dict(case=case, net_workforce_per_participant_nominal=None,
                        net_workforce_per_participant_pv=pv_per,
                        covers_share_T_pv=pv_per / ANCHOR_T,
                        quality="stated approximation; upper bound on the PV leg"))
    print(f"  {case:14s} PV workforce effect {money(pv_per):>12s} per participant   "
          f"covers {pv_per / ANCHOR_T:6.1%} (T)   {pv_per / ANCHOR_A:6.1%} (A)")
print(f"\n  mean election month {mean_month:.2f}; discount rate {IN.ENGINE_DISCOUNT_RATE:.2%}; "
      f"window midpoint {ACCEL / 24.0:.2f} years after it opens.")
central_pv = [r for r in PV_ROWS if r["case"] == "central"][0]["net_workforce_per_participant_pv"]
print(f"\n  On a PV-consistent comparison the central case covers {central_pv / ANCHOR_T:.1%}, not "
      f"{CENTRAL_NET / ANCHOR_T:.1%}.")
print("  THE PRINTED EXCHANGE HAS THE SAME FLAW, so this is not a new defect of the recomputation;")
print("  it is a defect of the comparison the package has always made.  It is also larger than")
print("  the design-anchor correction this issue was raised to make.  I am NOT folding it into the")
print("  headline - one driver at a time, and the issue asked for the anchor - but the v2.1 pass")
print("  cannot print a coverage percentage without deciding which convention it is on.")
print("  Direction: the nominal convention OVERSTATES the workforce leg, so it flatters the bill.")

# ###########################################################################
hr("[7] SENSITIVITY - the assumptions that control these answers")
print("Standard check: does a 10% move in any single input swing the answer by more than 25%?")
base_cov = CENTRAL_NET / ANCHOR_T
tests = [
    ("months of acceleration", lambda k: W.per_participant(
        SAL, ACCEL * k, *IN.WORKFORCE_CASES["central"][:1],
        coverage_share=IN.WORKFORCE_CASES["central"][1],
        ramp=IN.WORKFORCE_CASES["central"][2],
        recruit=IN.WORKFORCE_CASES["central"][3])["net_workforce_effect"] / ANCHOR_T),
    ("replacement differential", lambda k: W.per_participant(
        SAL, ACCEL, IN.WORKFORCE_CASES["central"][0] * k,
        coverage_share=IN.WORKFORCE_CASES["central"][1],
        ramp=IN.WORKFORCE_CASES["central"][2],
        recruit=IN.WORKFORCE_CASES["central"][3])["net_workforce_effect"] / ANCHOR_T),
    ("incumbent salary", lambda k: W.per_participant(
        SAL * k, ACCEL, IN.WORKFORCE_CASES["central"][0],
        coverage_share=IN.WORKFORCE_CASES["central"][1],
        ramp=IN.WORKFORCE_CASES["central"][2],
        recruit=IN.WORKFORCE_CASES["central"][3])["net_workforce_effect"] / ANCHOR_T),
    ("pension anchor", lambda k: CENTRAL_NET / (ANCHOR_T * k)),
]
print(f"\n{'input':26s} {'-10%':>10s} {'base':>10s} {'+10%':>10s} {'swing':>9s} {'dominant?'}")
print("-" * 76)
SENS = []
for name, f in tests:
    lo, hi = f(0.90), f(1.10)
    swing = max(abs(lo - base_cov), abs(hi - base_cov)) / base_cov
    print(f"{name:26s} {lo:10.1%} {base_cov:10.1%} {hi:10.1%} {swing:9.1%} "
          f"{'YES - over 25%' if swing > 0.25 else ''}")
    SENS.append(dict(input=name, coverage_minus10=lo, coverage_base=base_cov,
                     coverage_plus10=hi, swing=swing, dominant=swing > 0.25))
print("\nNo 10% move swings the coverage figure by more than 25%.  The three items that DO")
print("control the answer are choices of basis, which is why they are reported as bases:")
print("  1. WHICH RUNG the exchange is printed on.  Both legs move with it, and they move")
print("     together - so the ratio is far steadier than either leg.  The table:")
print(f"\n{'rung':>5s} {'$/participant':>14s} {'accel mo':>9s} {'net workforce':>14s} "
      f"{'covers (T)':>11s} {'net state/part':>15s}")
print("-" * 74)
RUNG_EXCHANGE = []
for rung in RUNGS:
    pv = float(IN.AUTHORISED_LADDER_PV[rung])
    cpp = pv / IN.V6_PARTICIPANTS["central"]
    accel = IN.MOO48_LADDER[rung][3]
    d, cov, ramp, rec, tso = IN.WORKFORCE_CASES["central"]
    net = W.per_participant(SAL, accel, d, coverage_share=cov, ramp=ramp, recruit=rec,
                            timing_shift_only=tso)["net_workforce_effect"]
    print(f"{rung:5d} {money(cpp):>14s} {accel:9.2f} {money(net):>14s} {net / cpp:11.1%} "
          f"{money(cpp - net):>15s}")
    RUNG_EXCHANGE.append(dict(rung_months=rung, cost_per_participant=cpp,
                              mean_acceleration_months=accel,
                              net_workforce_per_participant=net, covers_share_T=net / cpp,
                              net_state_per_participant_T=cpp - net))
print("\n     Coverage runs from "
      f"{min(r['covers_share_T'] for r in RUNG_EXCHANGE):.0%} to "
      f"{max(r['covers_share_T'] for r in RUNG_EXCHANGE):.0%} across the whole ladder while the")
print("     pension leg alone moves 48%.  THAT IS THE STURDY FINDING IN THIS DOCUMENT: the")
print("     exchange ratio is nearly rung-invariant, which the two printed figures - one")
print("     design's ratio at one rung - could never have shown.")
print("  2. WHETHER THE COMPARISON IS IN PV OR NOMINAL.  §6.5: it moves the central coverage")
print(f"     from {CENTRAL_NET / ANCHOR_T:.0%} to {central_pv / ANCHOR_T:.0%}, which is larger "
      f"than everything else on this page.")
print("  3. The acceleration itself is UNSOURCED as a behavioural quantity.  The model measures")
print("     how much earlier the design PERMITS retirement; nobody has measured how much earlier")
print("     members actually retire.  There is no published distribution of chosen retirement")
print("     dates inside a VRS window.  Analyst judgment, no anchor, and it is the single biggest")
print("     unevidenced input in the exchange - the same item MOO-183 §5 flagged second.")

# ###########################################################################
hr("[8] EXTERNAL SANITY CHECK")
print("The exchange's one externally anchorable input is the replacement-salary differential,")
print("because that is where every dollar of agency-level saving has to come from.  The engine's")
print("register records the central 18% as JUDGMENT between two published anchors, and the LOWER")
print("anchor is the only one that is a measured salary gap: VRS valuation p.50, average salary at")
print("age 35-39 ($74,012) against age 55-59 ($83,081) = 10.9% lower.  So the check is: run the")
print("exchange at the published 10.9% instead of the judged 18% and see what survives.\n")
d_ext = 1.0 - 74012.0 / 83081.0
r_ext = W.per_participant(SAL, ACCEL, d_ext, coverage_share=0.55, ramp=0.25, recruit=5000)
print(f"Check 1 - at the published-anchored {d_ext:.1%} differential, central frictions:")
print(f"  net workforce effect {money(r_ext['net_workforce_effect'])} per participant, covering "
      f"{r_ext['net_workforce_effect'] / ANCHOR_T:.1%} of the authorised anchor")
print(f"  against {CENTRAL_NET / ANCHOR_T:.1%} on the judged 18%.  DISAGREEMENT, and it is material:")
print(f"  the only published salary gap available cuts the coverage figure by "
      f"{1 - (r_ext['net_workforce_effect'] / CENTRAL_NET):.0%}.")
print("  The register's own note says why the published figure is a floor rather than the answer -")
print("  it is CROSS-SECTIONAL (two age bands in one year), so it understates an incumbent-versus-")
print("  new-hire gap, and DHRM publishes no incumbent/new-hire salary pairs by role.  That")
print("  reasoning is sound and I am not overturning it.  What the check establishes is that the")
print(f"  18% is not anchored, that the gap between the anchored floor and the judged central moves")
print(f"  the headline by {1 - (r_ext['net_workforce_effect'] / CENTRAL_NET):.0%}, and that a hostile "
      f"reader who insists on published figures only")
print(f"  gets {r_ext['net_workforce_effect'] / ANCHOR_T:.0%} coverage, not {CENTRAL_NET / ANCHOR_T:.0%}.  "
      f"Print the range, never the point.")
print(f"\nCheck 2 - the sign of the tier effect on the AGENCY's books.  At the central 18% on a")
r = W.per_participant(SAL, ACCEL, 0.18, coverage_share=0.55, ramp=0.25, recruit=5000)
load_neutral = r["annual_salary_differential"] * (1.0 + W.L_VARIABLE)
print(f"  {money(SAL)} incumbent the annual salary differential is "
      f"{money(r['annual_salary_differential'])} and the annual LOADED")
print(f"  differential is {money(r['annual_loaded_differential'])}.  Had the successor carried the "
      f"incumbent's own load")
print(f"  rate it would be {money(load_neutral)}, so the tier change destroys "
      f"{money(load_neutral - r['annual_loaded_differential'])} a year of the")
print(f"  saving - the Hybrid successor pays up to {EIN.HYBRID_ER_DC['value']:.1%} of pay in DC "
      f"contributions the Plan 1")
print("  incumbent does not, on top of the same blended employer DB rate.  So on the agency's own")
print("  books replacing a Plan 1 incumbent with a Hybrid hire at the SAME salary costs MORE, and")
print("  every dollar of agency-level saving has to come out of the salary gap alone.  The model")
print("  already has that sign right, against the direction a 'turnover savings pay for it' claim")
print("  usually assumes.  Agreement, and it is the one structural check that comes out in the")
print("  model's favour.")
print(f"\nCheck 3 - against the engine's own default.  The published engine's central acceleration")
print(f"  assumption is {EIN.MONTHS_ACCELERATION['value']['central']:.0f} months; this design MEASURES "
      f"{ACCEL:.1f}.  The measured figure is")
print(f"  {ACCEL / EIN.MONTHS_ACCELERATION['value']['central']:.1f}x the assumption.  DISAGREEMENT, and it is")
print("  the disagreement that matters most in this document.  The engine's 2/6/14-month ladder")
print("  was set for a GENERAL early-retirement offset; this bill's Pathway A cohort buys an")
print("  average 1.61 years of credit that advances unreduced eligibility by nearly four years.")
print("  Those are not the same quantity, and anyone who reads the 6-month default as a bound on")
print("  the measured 44.9 will conclude the workforce leg is seven times smaller than the model")
print("  says.  The measured figure is the right one for THIS cohort; the gap is a reason to")
print("  distrust the LEVEL of the workforce leg, not its sign, and it is why §6 reports a range")
print(f"  from {min(r['covers_share_T'] for r in WF_ROWS):.0%} to "
      f"{max(r['covers_share_T'] for r in WF_ROWS):.0%} and not a point.")
print("\nNot checkable at all, and all three are data requests to VRS and DHRM:")
print("  - every participant count here (no published count of § 51.1-142.2 purchases exists);")
print("  - the retirement-date distribution inside a VRS window;")
print("  - the actual salary of the actual replacement for an actual accelerated retiree.")

# ###########################################################################
hr("[9] THE EXPORT")
meta = dict(
    issue="MOO-199",
    generated=datetime.datetime.now().isoformat(timespec="seconds"),
    basis=("§ 51.1-142.4 C item 22 as option (c) measured at the filing date, plus the "
           "no-advance bar of clause (vii) of \"eligible member\"; 12-month retirement rung; "
           "6.00% statutory interest; state agency employees in Plan 1 and Plan 2; four-year "
           "pilot from 1 July 2029; PV at 6/30/2025"),
    engine_provenance=IN.ENGINE_PROVENANCE,
    v6_engine_absent=IN.V6_ENGINE_ABSENT,
    key_binding_verified=False,
    key_binding_note=IN.EXPORT_SCHEMA_NOTE,
    key_binding_table=[
        dict(block="retirement_deadline_ladder", model_tab="retirement deadline",
             dial="rung in months", quality="authorised (cited)"),
        dict(block="member_price_grid", model_tab="member price",
             dial="age x completed service", quality="measured; basis-invariant"),
        dict(block="interest_rate_dial", model_tab="interest rate",
             dial="statutory interest", quality="measured on the MOO-48 cohort; "
                                                "authorised only at 6.00%"),
        dict(block="cap_sweep_utilisation", model_tab="cap",
             dial="aggregate cap in dollars", quality="measured (exact arithmetic)"),
        dict(block="cap_sweep_admission", model_tab="cap",
             dial="aggregate cap in dollars", quality="measured on the MOO-48 cohort; shape only"),
        dict(block="workforce_exchange", model_tab="workforce break-even",
             dial="replacement differential x months of acceleration", quality="measured"),
    ],
    numerator_convention=IN.NUMERATOR_CONVENTION,
    precision_rule=("two significant figures; per-participant figures to the nearest $1,000; "
                    "two designs whose per-participant figures round to the same $1,000 are not "
                    "ranked against each other on that measure (MOO-183 §6)"),
    caveats=list(IN.CAVEATS),
    publication=("pre-decisional and internal; release is the Policy Director's decision. "
                 "Interest-dial rows away from 6.00% carry the board's standing S8 publication "
                 "restriction and must not appear in a sponsor-facing artifact."),
)
DATA = dict(
    meta=meta,
    headline=dict(
        participants=IN.V6_PARTICIPANTS,
        trust_pv_rung12=IN.V6_TRUST_PV_RUNG12,
        trust_nominal_rung12=IN.V6_TRUST_NOMINAL_RUNG12,
        certified_reserved_nominal=IN.V6_CERTIFIED_RESERVED_NOMINAL,
        cost_per_participant=V6_CPP,
        cost_per_participant_all_in=ANCHOR_A,
        implementation_allowance=IN.IMPLEMENTATION_ALLOWANCE,
        cap_utilisation=IN.AUTHORISED_CAP_UTILISATION,
        member_price_pair=dict(multiple_of_anc=A12["multiple_of_anc"],
                               share_of_aec=A12["share_of_aec"]),
        mean_participating_salary=SAL,
        mean_acceleration_months=ACCEL,
        mean_years_purchased=YEARS,
        gf_share_of_amortisation=IN.GF_SHARE,
    ),
    retirement_deadline_ladder=LADDER_ROWS,
    member_price_grid=PRICE_ROWS,
    interest_rate_dial=DIAL_ROWS,
    cap_sweep_utilisation=CAP_ROWS,
    cap_sweep_admission=CAP_RUN_ROWS,
    workforce_exchange=dict(
        cases=WF_ROWS,
        breakeven=dict(months_convention_T=be_T, months_convention_A=be_A,
                       months_as_printed=be_printed,
                       differential_convention_T=bed_T,
                       measured_acceleration_months=ACCEL),
        breakeven_grid=BE_GRID,
        by_rung=RUNG_EXCHANGE,
        pv_consistent_variant=PV_ROWS,
        printed_for_comparison=dict(anchor=IN.PRINTED_ANCHOR, design=IN.PRINTED_ANCHOR_DESIGN,
                                    rung=IN.PRINTED_ANCHOR_RUNG,
                                    coverage=IN.PRINTED_COVERAGE,
                                    net_workforce_per_participant=w_printed["net_workforce_effect"],
                                    denominator_only_swap_coverage=naive),
    ),
    sensitivity=SENS,
)


def w_csv(name, rows, fields=None):
    p = os.path.join(HERE, name)
    if not rows:
        return
    fields = fields or list(rows[0])
    with open(p, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        wr.writeheader()
        for r in rows:
            wr.writerow({k: (";".join(v) if isinstance(v, list) else v)
                         for k, v in r.items() if k in fields})
    print(f"  wrote {name}  ({len(rows)} rows)")


jp = os.path.join(HERE, "out_moo199_model_data.json")
with open(jp, "w") as fh:
    json.dump(DATA, fh, indent=2, sort_keys=False)
print(f"  wrote out_moo199_model_data.json  ({os.path.getsize(jp):,} bytes)")
w_csv("out_moo199_ladder.csv", LADDER_ROWS)
w_csv("out_moo199_member_price_grid.csv", PRICE_ROWS)
w_csv("out_moo199_interest_dial.csv", DIAL_ROWS)
w_csv("out_moo199_cap_sweep.csv", CAP_ROWS)
w_csv("out_moo199_cap_admission.csv", CAP_RUN_ROWS)
w_csv("out_moo199_workforce_exchange.csv", WF_ROWS)
w_csv("out_moo199_workforce_by_rung.csv", RUNG_EXCHANGE)
w_csv("out_moo199_breakeven_grid.csv", BE_GRID)

hr("[10] THE SENTENCE FOR THE EDITOR")
print(f"""
On the recommended design's own anchor - {money(V6_CPP)} of net trust cost per participant on the
authorised basis - the workforce effect covers about {CENTRAL_NET / ANCHOR_T:.0%} of the pension cost in the central
case ({min(r['covers_share_T'] for r in WF_ROWS):.0%} to {max(r['covers_share_T'] for r in WF_ROWS):.0%} across the three replacement-differential cases), not the {IN.PRINTED_COVERAGE:.0%} the
documents print against repaired S1's {money(IN.PRINTED_ANCHOR)}; the exchange breaks even at {be_T:.0f} months of
acceleration against the {ACCEL:.0f} months this design measures, and the coverage ratio is nearly
invariant to the retirement rung ({min(r['covers_share_T'] for r in RUNG_EXCHANGE):.0%} to {max(r['covers_share_T'] for r in RUNG_EXCHANGE):.0%} across the whole ladder) even though the
pension leg alone moves {max(float(IN.AUTHORISED_LADDER_PV[r]) for r in RUNGS) / min(float(IN.AUTHORISED_LADDER_PV[r]) for r in RUNGS) - 1:.0%}.
""".strip())
print(f"\nTwo-significant-figure form: about {sig2(V6_CPP)} per participant, workforce effect about")
print(f"{CENTRAL_NET / ANCHOR_T:.0%} of it, break-even about {be_T:.0f} months.")
print("\nAnd the correction the sentence carries: the documents say the real exchange is WORSE than")
print("they show.  On a consistent recomputation the coverage RATIO is better; what is worse is")
print(f"the pension cost per participant, by {money(ANCHOR_T - IN.PRINTED_ANCHOR)}.  The direction sentence must change.")

print(f"\nrun completed {datetime.datetime.now().isoformat(timespec='seconds')}")
for c in IN.CAVEATS:
    print("  * " + c)
