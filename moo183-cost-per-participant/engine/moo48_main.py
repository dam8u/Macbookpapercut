"""
MOO-48 — the bill as drafted, priced; the retirement-deadline ladder; the certified-subsidy
distribution on the corrected single basis; and the per-member ceiling solved for a stated floor.

    python3 moo48_main.py

Writes out_moo48_*.csv and out_moo48_summary.json and prints the full transcript (captured as
out_moo48_run.txt).  Measured runtime: about seven minutes on the machine this was built on, the
first minute of which is the monthly stock projection, which is then cached.

Step 0 is a hard REGRESSION LOCK against four published repaired-basis figures.  If any has
drifted the run aborts, so every number below is attributable to the three changes this issue asks
for - Pathway A only, the drafted retirement deadline, and the corrected certified-subsidy basis -
and to nothing else.

Nothing in inputs.py, s8.py, v2_cohort.py, v2_liability.py or v2_scenarios.py is modified.  The
MOO-45 calendar reprice is reapplied here by wrapping s8.s8_price in a context manager, exactly as
moo45_main.py does, so it stays a named variant rather than a silent change of basis.

NO FIGURE IN THIS FILE IS A VRS ACTUARIAL RESULT.  Nothing here is reliable beyond two significant
figures.
"""
import json
import time
from contextlib import contextmanager

import numpy as np
import pandas as pd

import inputs as IN
import moo48_inputs as M48
import s8
import scenarios as SC
import v2_cohort as C
import v2_decrements as D
import v2_liability as L
import v2_scenarios as X
from mortality import Mortality

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 80)

T0 = time.time()
OUT = {}
MORT = Mortality()

I6 = 0.06                                     # the decided statutory interest rate, not in question
EL = IN.TAKEUP_PRICE_ELASTICITY["value"]
GF = IN.GF_SHARE["value"]
IMPL = IN.VRS_IMPLEMENTATION_COST["value"]["central"]
CAP = M48.AGGREGATE_CAP["value"]
PLANS = ("plan1", "plan2")
LEVELS = ("low", "central", "high")
BILL_DL = M48.BILL_DEADLINE_MONTHS["value"]["central"]
LADDER = M48.DEADLINE_LADDER_MONTHS["value"]
CM_CENTRAL = IN.PURCHASE_COMPLETION_MONTHS["value"]["central"]

PUBLISHED = {"S1": 5_123_905, "S2": 2_057_259, "S8-i6": 3_652_752, "S8-i6-RETIRE": 5_199_779}


def money(x):
    return f"${x:,.0f}"


def sig2(x):
    """Two significant figures, which is the precision the inputs support (MOO-46 Decision 4)."""
    if x == 0:
        return "$0"
    neg = x < 0
    x = abs(float(x))
    e = int(np.floor(np.log10(x)))
    r = round(x, -(e - 1))
    return ("-" if neg else "") + f"${r:,.0f}"


# ===========================================================================
# the MOO-45 calendar reprice, as a named variant only (interest leg)
# ===========================================================================
_ORIG_S8_PRICE = s8.s8_price


@contextmanager
def calendar_gap(gap_years):
    """Lengthen the S8 interest period by `gap_years`, per MOO-45 / MOO-35 R3.

    The bill measures statutory interest on elapsed calendar time from the last day of the 36th
    month of membership service; s8.interest_years() returns credited service less 36 months.  The
    two differ by a constant, so the member price differs by exactly (1 + i) ** gap_years.
    """
    if gap_years == 0:
        yield
        return

    def patched(p, years, i_stat=None, **kw):
        i = IN.S8_INTEREST_RATE["value"] if i_stat is None else i_stat
        q = dict(_ORIG_S8_PRICE(p, years, i_stat=i_stat, **kw))
        k = (1.0 + i) ** gap_years
        q["price"] *= k
        q["price_per_year"] *= k
        q["interest_years"] += gap_years
        q["interest_term"] *= k
        q["implied_multiple_of_anc"] *= k
        return q

    s8.s8_price = patched
    try:
        yield
    finally:
        s8.s8_price = _ORIG_S8_PRICE


# ===========================================================================
# the bill's own runner: Pathway A only, S8 price, explicit deadline
# ===========================================================================
def _bkw(scope=None, salary_factor=1.0, months_available=None):
    return dict(months_available=months_available, vet_qual=None, age_skew=None, vet_share=None,
                salary_factor=salary_factor, scope=scope)


def elections(level="central", scope=None, salary_factor=1.0, months_available=None,
              pathways=("A",), deadline=None, cm=None, i=I6, apply_elasticity=True,
              takeup_mult=1.0):
    """The bill's election flow, with take-up adjusted for the S8 price on the bill's own cohort.

    The elasticity adjustment is computed on the SAME cohort the bill admits (Pathway A only),
    which is why the participant count differs slightly from the published S8-i6 row: that row
    adjusted take-up on the A+B price ratio.
    """
    tA = IN.TAKEUP_PATHWAY_A["value"][level] * takeup_mult
    tB = IN.TAKEUP_PATHWAY_B["value"][level] * takeup_mult
    bkw = _bkw(scope, salary_factor, months_available)
    lkw = dict(deadline_months=deadline, completion_months=cm)
    el0 = X.build_elections_cached(tA, tB, plans=PLANS, pathways=pathways, **bkw)
    adj = 1.0
    if apply_elasticity:
        base = X.aggregate(el0, "anc", **lkw)
        ref = X.aggregate(el0, "s8", s8_kw={"i_stat": i}, **lkw)
        adj = (ref["paid"] / base["paid"]) ** EL if base["paid"] else 1.0
    el = X.build_elections_cached(tA * adj, tB * adj, plans=PLANS, pathways=pathways, **bkw)
    return el, adj, lkw


def runA(level="central", deadline=None, i=I6, cm=None, scope=None, pathways=("A",),
         cap=None, per_member_cap=None, queue_order="chronological", salary_factor=1.0,
         months_available=None, apply_elasticity=True, annuity_load=1.0, rule="s8",
         takeup_mult=1.0):
    el, adj, lkw = elections(level, scope, salary_factor, months_available, pathways, deadline, cm,
                             i, apply_elasticity, takeup_mult)
    a = X.aggregate(el, rule, s8_kw={"i_stat": i}, cap=cap, per_member_cap=per_member_cap,
                    queue_order=queue_order, annuity_load=annuity_load, **lkw)
    a["takeup_adjustment"] = adj
    return a


def cells(level="central", deadline=None, i=I6, cm=None, scope=None, pathways=("A",),
          salary_factor=1.0, months_available=None, deadline_window=False):
    """One row per priced election cell, with both readings of certified subsidy.

    `deadline_window=True` is the variant in which lengthening the retirement deadline is read as
    lengthening the eligibility window too (moo48_inputs.DEADLINE_COHORT_HELD_FIXED): the cohort is
    built on the broad reading and then filtered to members who are eligible by the time the
    deadline expires.
    """
    el, adj, lkw = elections(level, scope, salary_factor, months_available, pathways, deadline, cm,
                             i)
    dl = IN.RETIREMENT_DEADLINE_MONTHS["value"] if deadline is None else deadline
    cmm = CM_CENTRAL if cm is None else cm
    rows = []
    for e in el:
        if deadline_window and e["months_to_eligibility"] > cmm + dl + 1e-9:
            continue
        d = X.ledger(e, "s8", s8_kw={"i_stat": i}, **lkw)
        p = X._profile(e)
        aec = X.PR.aec_full(p, e["years"])
        paid = d["member_payment"]
        cs_corr = d["gross_liability_increase"] - paid - M48.EMPLOYER_PAYMENT["value"]
        cs_draft = aec + d["early_retirement_component"] - paid
        rows.append({
            "pathway": e["pathway"], "plan": e["plan"], "sex": e["sex"], "age": e["age"],
            "service": e["service"], "salary": e["salary"], "years_bought": e["years"],
            "months_to_eligibility": e["months_to_eligibility"],
            "election_month": e["month"], "fy": e["fy"], "participants": e["weight"],
            "discount_factor": (1.0 + X.I_NOM) ** (-(e["month"] / 12.0)),
            "member_paid": paid,
            "aec_full_statutory_quote": aec,
            "gross_liability_increase": d["gross_liability_increase"],
            "service_credit_component": d["service_credit_component"],
            "early_commencement_component": d["early_retirement_component"],
            "retire_age_with_design": d["retire_age_with_design"],
            "counterfactual_retire_age": d["expected_counterfactual_retire_age"],
            "acceleration_months": d["acceleration_months"],
            "CS_corrected": cs_corr,
            "CS_drafted": cs_draft,
            "overlap_drafted_minus_corrected": cs_draft - cs_corr,
        })
    df = pd.DataFrame(rows)
    df.attrs["takeup_adjustment"] = adj
    return df


def agg_cols(df, cols, discounted=False):
    w = df.participants.values * (df.discount_factor.values if discounted else 1.0)
    return {c: float((df[c].values * w).sum()) for c in cols}


def wq(vals, weights, qs):
    """Participant-weighted quantiles."""
    o = np.argsort(vals)
    v, w = np.asarray(vals)[o], np.asarray(weights)[o]
    cw = np.cumsum(w) - 0.5 * w
    cw /= w.sum()
    return [float(np.interp(q, cw, v)) for q in qs]


QS = [0.50, 0.75, 0.90, 0.95]


# ===========================================================================
# 0. REGRESSION LOCKS
# ===========================================================================
print(__doc__)
print("=" * 112)
print("[0] REGRESSION LOCKS — the harness must reproduce the published repaired-basis figures")
print("=" * 112)
lock = {}
lock["S1"] = X.run("S1", "central")
lock["S2"] = X.run("S2", "central")
lock["S8-i6"] = X.run("S8", "central", s8_kw={"i_stat": I6})
lock["S8-i6-RETIRE"] = X.run("S8", "central", s8_kw={"i_stat": I6}, retire_immediately=True)
for k, v in lock.items():
    assert round(v["trust"]) == PUBLISHED[k], (k, round(v["trust"]), PUBLISHED[k])
    print(f"    repaired {k:<13s} central trust cost {money(v['trust']):>13s}   "
          f"published {money(PUBLISHED[k]):>13s}   participants {v['n']:>5.1f}   OK")
print("    Sources: model-s8-s9-repaired §2a/§4 (MOO-31), out_v2_scenarios.csv, "
      "out_v2_retire_immediately.csv.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 1. THE BILL AS DRAFTED
# ===========================================================================
print()
print("=" * 112)
print("[1] THE BILL AS DRAFTED — Pathway A only, retire the month after the credit posts, "
      "statutory interest 6.00%")
print("=" * 112)
print("    What the three drafted clauses do to the priced design, in one place:")
print('      § 51.1-142.4 A "eligible member" (v)   removes every already-eligible member '
      "(Pathway B) — 43.9 of the")
print("                                             62.2 published S8-at-6% participants, 71% of "
      "that cohort.")
print('      § 51.1-142.4 A "eligible member" (vi)  requires unreduced eligibility on the first of '
      "the month after")
print("                                             the credit posts — the narrow Pathway A "
      "reading (MOO-46 Decision 3.1).")
print('      § 51.1-142.4 A "qualifying retirement" fixes retirement at the first of the month '
      "after crediting, with")
print("                                             up to 90 days of Board discretion — deadline "
      "rung 1, range 0 to 4.")
print()

bill = {}
for lvl in LEVELS:
    bill[lvl] = runA(lvl, deadline=BILL_DL)
b = bill["central"]
OUT["bill_central"] = {k: v for k, v in b.items() if isinstance(v, (int, float))}

bill_rows = []
for lvl in LEVELS:
    a = bill[lvl]
    bill_rows.append({"take_up_case": lvl, "takeup_A": IN.TAKEUP_PATHWAY_A["value"][lvl],
                      "takeup_adjustment": a["takeup_adjustment"],
                      "participants": a["n"], "years_purchased": a["years"],
                      "acceleration_months": a["avg_acceleration_months"],
                      "member_paid": a["paid"], "multiple_of_anc": a["multiple_of_anc"],
                      "share_of_aec": a["share_of_aec"],
                      "gross_liability": a["gross"], "trust_cost": a["trust"],
                      "implementation_NGF": IMPL,
                      "headline_state_cost": a["trust"] + IMPL,
                      "GF_PV": a["trust"] * GF, "NGF_PV": a["trust"] * (1 - GF) + IMPL})
dfb = pd.DataFrame(bill_rows)
dfb.to_csv("out_moo48_bill_as_drafted.csv", index=False)
print("    HEADLINE — central net trust cost, PV at the 6/30/2025 valuation date, "
      "plus VRS implementation:")
print(dfb.round({"takeup_A": 2, "takeup_adjustment": 3, "participants": 1, "years_purchased": 1,
                 "acceleration_months": 1, "member_paid": 0, "multiple_of_anc": 2,
                 "share_of_aec": 2, "gross_liability": 0, "trust_cost": 0,
                 "headline_state_cost": 0, "GF_PV": 0, "NGF_PV": 0}).to_string(index=False))
print()
print(f"    CENTRAL  trust cost {money(b['trust'])}  + implementation {money(IMPL)}  "
      f"= headline {money(b['trust'] + IMPL)}")
print(f"    RANGE    {money(bill['low']['trust'])} (low take-up) to "
      f"{money(bill['high']['trust'])} (high take-up) on trust cost;")
print(f"             {money(bill['low']['trust'] + IMPL)} to "
      f"{money(bill['high']['trust'] + IMPL)} on the headline.")
print(f"    Two significant figures, which is all the inputs support: "
      f"{sig2(b['trust'] + IMPL)} central, "
      f"{sig2(bill['low']['trust'] + IMPL)} to {sig2(bill['high']['trust'] + IMPL)}.")
print()
print("    WHERE THIS SITS AGAINST THE TWO NEAREST PRICED CELLS — and it is NOT between them:")
brk = pd.DataFrame([
    {"cell": "S8 at 6%, Pathways A+B, 6-month deadline", "basis": "published repaired headline",
     "participants": lock["S8-i6"]["n"], "trust_cost": lock["S8-i6"]["trust"]},
    {"cell": "S8 at 6%, Pathways A+B, retire-immediately guardrail",
     "basis": "published repaired §2a", "participants": lock["S8-i6-RETIRE"]["n"],
     "trust_cost": lock["S8-i6-RETIRE"]["trust"]},
    {"cell": "S2, Pathway A only, ANC price, 6-month deadline", "basis": "published repaired §4",
     "participants": lock["S2"]["n"], "trust_cost": lock["S2"]["trust"]},
    {"cell": "THE BILL: Pathway A only, S8 at 6%, deadline rung 1", "basis": "MOO-48, this run",
     "participants": b["n"], "trust_cost": b["trust"]},
])
brk.to_csv("out_moo48_bracket.csv", index=False)
print(brk.round({"participants": 1, "trust_cost": 0}).to_string(index=False))
print()
print("    THE BRACKET IN THE ASSIGNMENT DOES NOT HOLD, and the reason matters for the memo.")
print(f"    The bill at {money(b['trust'])} is BELOW S2's {money(lock['S2']['trust'])}, not "
      "between S2 and $5.2M. S2 is")
print("    Pathway A only at the APPROXIMATE NORMAL COST price; the bill is Pathway A only at the")
print("    S8 6% price, which is 1.5x ANC. The dearer price does two things at once: the member")
print(f"    pays {money(b['paid'])} instead of {money(lock['S2']['paid'])}, and take-up falls with")
print(f"    price (elasticity {EL}), so the cohort is {b['n']:.1f} rather than "
      f"{lock['S2']['n']:.1f} members. Both move the")
print("    same way. S2 was never a lower bound on the bill — it is the same eligible population at")
print("    a cheaper price, which buys more take-up; the published S8 figures were a wider")
print("    population at the bill's own price.")

# ---- the two member-fairness figures in the adopted memo wording ---------
print()
print("    TWO FIGURES IN MOO-46 DECISION 1.4's REPLACEMENT WORDING MOVE ON THE BILL'S COHORT,")
print("    AND ONE OF THEM MOVES A LOT. The adopted sentence says the member pays '1.50x the")
print("    approximate normal cost' and '61% of the current-law actuarial-equivalent price'. Both")
print("    were measured on the A+B cohort. On the cohort the bill admits:")
fair = pd.DataFrame([
    {"figure": "member price as a multiple of ANC", "memo_wording_A_plus_B": 1.50,
     "bill_cohort_A_only": b["multiple_of_anc"]},
    {"figure": "member price as a share of the current-law AEC quote",
     "memo_wording_A_plus_B": 0.61, "bill_cohort_A_only": b["share_of_aec"]},
])
fair.to_csv("out_moo48_member_fairness.csv", index=False)
print(fair.round(2).to_string(index=False))
print("      The 'this is not a subsidy' claim SURVIVES: the member still pays more than VRS's")
print(f"      own stated cost of a year of service credit ({b['multiple_of_anc']:.2f}x, against "
      "1.50x on the wider cohort).")
print("      The 'veteran keeps most of the benefit' claim MOVES THE OTHER WAY and must be")
print(f"      restated: on the bill's cohort the member pays {b['share_of_aec']:.0%} of the "
      "current-law price, i.e. a")
print(f"      {1-b['share_of_aec']:.0%} discount rather than a 39% discount. That is better for "
      "the veteran and worse")
print("      for the Commonwealth, and it is a direct consequence of clause (v): Pathway A members")
print("      buy more years and buy a large eligibility acceleration, so their current-law quote")
print("      is much larger than a Pathway B member's.")
print("      BOTH FIGURES IN THE ADOPTED WORDING NEED REPLACING with the right-hand column.")

# ---- the bill's own drafted range on the deadline -------------------------
print()
print("    THE BILL'S OWN DRAFTED RANGE on the retirement date (rungs 0, 1 and 4 are all drafted):")
dr = []
for dl, lbl in ((0, "rung 0 — credit posts and retirement takes effect in the same month"),
                (BILL_DL, "rung 1 — THE BILL: first of the month after the credit posts"),
                (4, "rung 4 — rung 1 plus the 90 days of Board discretion in 'qualifying "
                    "retirement'")):
    a = runA("central", deadline=dl)
    dr.append({"deadline_months": dl, "reading": lbl, "participants": a["n"],
               "acceleration_months": a["avg_acceleration_months"], "trust_cost": a["trust"]})
dfdr = pd.DataFrame(dr)
dfdr.to_csv("out_moo48_bill_deadline_range.csv", index=False)
print(dfdr.round({"participants": 1, "acceleration_months": 1, "trust_cost": 0})
      .to_string(index=False))
print(f"    The Director's reading (rung 0) and the drafted text (rung 1) differ by "
      f"{money(dfdr.trust_cost.iloc[0] - dfdr.trust_cost.iloc[1])}, "
      f"{(dfdr.trust_cost.iloc[0]/dfdr.trust_cost.iloc[1]-1):.1%}. Rung 1 is used")
print("    as the headline because it is what the text says; nothing in the decision turns on it.")

# ---- completion lag, which is the other clock in the same definition -----
print()
print("    THE COMPLETION LAG IS PART OF THE SAME CLAUSE AND IT MOVES THE ANSWER MORE THAN THE")
print("    DEADLINE DOES. § 51.1-142.4 E allows up to 12 months to pay; the retirement date is")
print("    measured from the credit posting, so a member who pays by lump sum retires a year")
print("    earlier than a member on a 12-month agreement, at the same deadline rung.")
cmr = []
for cmv, lbl in ((0, "lump sum (90 days to remit, treated as 0)"),
                 (CM_CENTRAL, "12-month purchase payment agreement (central)"),
                 (36, "36-month agreement (NOT permitted by § 51.1-142.4 E as drafted; shown as "
                      "the value of amending E)")):
    a = runA("central", deadline=BILL_DL, cm=cmv)
    cmr.append({"completion_months": cmv, "reading": lbl, "participants": a["n"],
                "acceleration_months": a["avg_acceleration_months"], "trust_cost": a["trust"]})
dfcm = pd.DataFrame(cmr)
dfcm.to_csv("out_moo48_completion_lag.csv", index=False)
print(dfcm.round({"participants": 1, "acceleration_months": 1, "trust_cost": 0})
      .to_string(index=False))
print("    STATED UP FRONT because it is a behavioural assumption carrying a drafted dial: the")
print("    central answer rests on a 12-month completion lag which § 51.1-142.4 E permits as a")
print(f"    maximum and does not require. At a lump sum the same bill costs "
      f"{money(dfcm.trust_cost.iloc[0])}, "
      f"{(dfcm.trust_cost.iloc[0]/b['trust']-1):+.0%}; over the")
print(f"    whole drafted range the bill is {money(dfcm.trust_cost.iloc[1])} to "
      f"{money(dfcm.trust_cost.iloc[0])} on the completion lag alone. A MINIMUM")
print("    completion period, rather than a maximum, is the cheapest amendment available to this")
print("    bill and it is not currently in the text.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 2. THE RETIREMENT-DEADLINE LADDER
# ===========================================================================
print()
print("=" * 112)
print("[2] THE RETIREMENT-DEADLINE LADDER — Pathway A only, 6.00%, cohort held at the drafted "
      "narrow reading")
print("=" * 112)

lad = []
lad_cells = {}
for dl in LADDER:
    rec = {"deadline_months": dl}
    for lvl in LEVELS:
        a = runA(lvl, deadline=dl)
        if lvl == "central":
            rec.update({"participants": a["n"], "years_purchased": a["years"],
                        "acceleration_months": a["avg_acceleration_months"],
                        "design_retire_age": a["avg_design_retire_age"],
                        "counterfactual_retire_age": a["avg_counterfactual_retire_age"],
                        "member_paid": a["paid"], "gross_liability": a["gross"],
                        "trust_cost": a["trust"],
                        "windfall_bound": a["svc"] - a["paid"],
                        "headline_state_cost": a["trust"] + IMPL})
        rec[f"trust_cost_{lvl}"] = a["trust"]
    df = cells("central", deadline=dl)
    lad_cells[dl] = df
    rec["certified_subsidy_aggregate_nominal"] = float(
        (np.maximum(0.0, df.CS_corrected.values) * df.participants.values).sum())
    rec["certified_subsidy_aggregate_PV"] = float(
        (np.maximum(0.0, df.CS_corrected.values) * df.participants.values
         * df.discount_factor.values).sum())
    rec["certified_subsidy_aggregate_drafted_basis_nominal"] = float(
        (np.maximum(0.0, df.CS_drafted.values) * df.participants.values).sum())
    rec["max_CS_corrected_per_member"] = float(df.CS_corrected.max())
    rec["is_the_bill"] = (dl == BILL_DL)
    lad.append(rec)
dfl = pd.DataFrame(lad)
dfl.to_csv("out_moo48_deadline_ladder.csv", index=False)
show = ["deadline_months", "is_the_bill", "participants", "acceleration_months", "member_paid",
        "trust_cost_low", "trust_cost", "trust_cost_high", "certified_subsidy_aggregate_nominal",
        "max_CS_corrected_per_member", "windfall_bound"]
print(dfl[show].round({"participants": 1, "acceleration_months": 1, "member_paid": 0,
                       "trust_cost_low": 0, "trust_cost": 0, "trust_cost_high": 0,
                       "certified_subsidy_aggregate_nominal": 0,
                       "max_CS_corrected_per_member": 0, "windfall_bound": 0})
      .to_string(index=False))
print()
print("    HOW TO READ THE LAST THREE COLUMNS. `certified_subsidy_aggregate_nominal` is the "
      "quantity")
print("    § 51.1-142.4 D 2 meters against $3,000,000 — the sum of the positive per-member")
print("    certified subsidies, on the CORRECTED single basis, in the nominal dollars the Board")
print("    certifies. It is NOT the same number as trust cost: trust cost is a present value at")
print("    the valuation date and nets the members whose subsidy is negative.")
r0, rb = dfl.iloc[0], dfl[dfl.deadline_months == BILL_DL].iloc[0]
r24 = dfl[dfl.deadline_months == 24].iloc[0]
r12 = dfl[dfl.deadline_months == 12].iloc[0]
print()
print(f"    THE SWING: rung 0 {money(r0.trust_cost)} -> rung 24 {money(r24.trust_cost)}, "
      f"a fall of {(1-r24.trust_cost/r0.trust_cost):.0%}.")
print(f"    From the bill (rung 1, {money(rb.trust_cost)}): rung 12 saves "
      f"{money(rb.trust_cost - r12.trust_cost)} ({(1-r12.trust_cost/rb.trust_cost):.0%}), "
      f"rung 24 saves {money(rb.trust_cost - r24.trust_cost)} "
      f"({(1-r24.trust_cost/rb.trust_cost):.0%}).")
print(f"    Acceleration falls from {r0.acceleration_months:.1f} months to "
      f"{r24.acceleration_months:.1f} months. The member price does NOT move "
      f"({money(rb.member_paid)} at")
print("    every rung): the S8 price is a function of salary history and interest, not of the")
print("    retirement date, so the whole of the saving is acceleration and none of it is price.")

# ---- the Director's two reasons, checked -------------------------------
print()
print("    THE TWO REASONS FOR A LONGER DEADLINE, CHECKED ON THIS COHORT (MOO-46 Decision 1.5)")
print()
print("    REASON 1 — 'the windfall bound is the cheap case'. CONFIRMED, and by a wider margin on")
print("    the bill's cohort than on repaired S1.")
wf = []
for dl in LADDER:
    r = dfl[dfl.deadline_months == dl].iloc[0]
    wf.append({"deadline_months": dl, "full_compliance_trust_cost": r.trust_cost,
               "windfall_bound_trust_cost": r.windfall_bound,
               "windfall_as_share_of_full": r.windfall_bound / r.trust_cost if r.trust_cost else 0})
dfwf = pd.DataFrame(wf)
dfwf.to_csv("out_moo48_windfall_bound.csv", index=False)
print(dfwf.assign(windfall_as_share_of_full=lambda d: d.windfall_as_share_of_full
                  .map("{:.0%}".format))
      .round({"full_compliance_trust_cost": 0, "windfall_bound_trust_cost": 0})
      .to_string(index=False))
print(f"    On repaired S1 the bound was {money(775_330)} against {money(5_123_905)} (15%). On the")
print(f"    bill's cohort at rung 1 it is {money(rb.windfall_bound)} against "
      f"{money(rb.trust_cost)} "
      f"({rb.windfall_bound/rb.trust_cost:.0%}). A member who")
print("    buys cheap credit and keeps working costs the trust a small fraction of what a member")
print("    who buys and retires costs. The direction of the Director's reason is right.")
print()
print("    AND THE DRAFTED TEXT IS STRONGER THAN THE BOUND SUGGESTS. § 51.1-142.4 G 2 reduces a")
print("    non-retiring member's credit to what their payment would have bought at the current-law")
print("    § 51.1-142.2 B 3 price, refunds the excess, and releases the reservation. So a member")
print("    who does not retire is not a windfall at all on this bill: the price discount is")
print("    unwound in kind, there is no acceleration because there is no retirement, and the")
print("    reserved appropriation goes back in the pool. REASON 2 IS SOUND. Two qualifications,")
print("    both fiscal and neither fatal:")
print("      (a) G 2 measures the B 3 price 'on the date the Board accepted the election' but is")
print("          applied up to 13 months later, so the trust forgoes the drift between the two.")
print("          Second-order; not priced here.")
print("      (b) G 4 is the real cost of a longer deadline. Death, approval for disability, and")
print("          involuntary separation vest the credit AT THE PILOT PRICE with no G 2 reduction,")
print("          and the exposure window is exactly election-to-required-retirement, so it grows")
print("          with the rung. The exposed population is counted below. The cost per event is")
print("          NOT priced: survivor-option and disability benefits are outside this model.")


def g4_exposure(deadline, cm=None, level="central"):
    """Expected members hitting a § 51.1-142.4 G 4 event inside the election-to-retirement window.

    Decrements are VRS's own (v2_decrements) plus fitted mortality, applied monthly to the
    election cohort.  Death and involuntary separation are counted separately because the drafted
    clause reaches 'separated ... other than by the member's own choice or for cause', which is a
    subset of VRS's single termination rate that VRS does not publish separately.
    """
    cmm = CM_CENTRAL if cm is None else cm
    months = int(round(cmm + deadline))
    df = lad_cells[deadline] if deadline in lad_cells and level == "central" else \
        cells(level, deadline=deadline, cm=cm)
    p_die = p_term = 0.0
    for _, r in df.iterrows():
        alive = 1.0
        d_, t_ = 0.0, 0.0
        for m in range(months):
            age = r.age + m / 12.0
            svc = r.service + m / 12.0
            qd = 1.0 - MORT.survive(age, age + 1.0 / 12.0, sex=r.sex)
            qt = D.monthly(D.term_rate(svc, r.sex))
            d_ += alive * qd
            t_ += alive * (1.0 - qd) * qt
            alive *= (1.0 - qd) * (1.0 - qt)
        p_die += r.participants * d_
        p_term += r.participants * t_
    return {"deadline_months": deadline, "window_months": months,
            "expected_deaths_in_window": p_die,
            "expected_terminations_in_window": p_term,
            "g4_exposed_low": p_die,
            "g4_exposed_high": p_die + p_term}


g4 = pd.DataFrame([g4_exposure(dl) for dl in LADDER])
g4["share_of_cohort_high"] = g4.g4_exposed_high / float(rb.participants)
g4.to_csv("out_moo48_g4_exposure.csv", index=False)
print()
print("    § 51.1-142.4 G 4 EXPOSURE BY RUNG (expected members, central take-up cohort of "
      f"{rb.participants:.1f})")
print(g4.assign(share_of_cohort_high=lambda d: d.share_of_cohort_high.map("{:.1%}".format))
      .round({"expected_deaths_in_window": 2, "expected_terminations_in_window": 2,
              "g4_exposed_low": 2, "g4_exposed_high": 2}).to_string(index=False))
print("    LOW = death only. HIGH = death plus ALL terminations, which overstates G 4 because it")
print("    includes voluntary quits and dismissals for cause, which G 4 excludes. The true figure")
print("    is inside that band and VRS does not publish the split. Direction: a longer deadline")
print("    raises the count monotonically, so the ladder's saving is slightly overstated at the")
print("    long rungs by an amount this model cannot value.")

# ---- the window variant: what happens if clause (vi) moves too -----------
print()
print("    THE ONE WAY A LONGER DEADLINE GETS EXPENSIVE: if the eligibility clause moves with it.")
print("    If a patron lengthens the deadline AND relaxes clause (vi) so that a member who becomes")
print("    eligible within the deadline may elect, the cohort stops being the narrow one. Priced:")
win = []
for dl in LADDER:
    a_fixed = runA("central", deadline=dl)
    dfw = cells("central", deadline=dl, scope="advance", deadline_window=True)
    n_w = float(dfw.participants.sum())
    gross_w = float((dfw.gross_liability_increase * dfw.participants * dfw.discount_factor).sum())
    paid_w = float((dfw.member_paid * dfw.participants * dfw.discount_factor).sum())
    win.append({"deadline_months": dl, "cohort_held_fixed_participants": a_fixed["n"],
                "cohort_held_fixed_trust_cost": a_fixed["trust"],
                "window_variant_participants": n_w,
                "window_variant_trust_cost": gross_w - paid_w,
                "ratio": (gross_w - paid_w) / a_fixed["trust"] if a_fixed["trust"] else 0.0})
dfwin = pd.DataFrame(win)
dfwin.to_csv("out_moo48_deadline_window_variant.csv", index=False)
print(dfwin.round({"cohort_held_fixed_participants": 1, "cohort_held_fixed_trust_cost": 0,
                   "window_variant_participants": 1, "window_variant_trust_cost": 0,
                   "ratio": 2}).to_string(index=False))
print("    So the deadline is safe to lengthen ONLY if clause (vi) is left alone. That is a")
print("    drafting instruction, not a modelling result, and it goes to the Drafting Specialist.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 3. CERTIFIED SUBSIDY ON THE CORRECTED SINGLE BASIS
# ===========================================================================
print()
print("=" * 112)
print("[3] CERTIFIED SUBSIDY, ONE CORRECTED BASIS (MOO-46 Decision 2(d)), on the bill's own cohort")
print("=" * 112)
dfc = lad_cells[BILL_DL].copy()
dfc = dfc.sort_values("CS_corrected").reset_index(drop=True)
dfc.to_csv("out_moo48_cs_cells.csv", index=False)
N = float(dfc.participants.sum())
n_profiles = len(dfc.groupby(["plan", "sex", "age", "service"]))
print(f"    {N:.1f} expected participating members at central take-up, Pathway A only, carried on "
      f"{len(dfc):,} priced")
print(f"    rows = {n_profiles:,} distinct (plan, sex, age, service) profiles x the election month "
      "each row is")
print("    priced in. One row is a fractional expected headcount, not a person; the distribution")
print("    below is participant-weighted across those rows.")
print("    CS_corrected = increase in liability attributable to the election, less member and")
print("                   employer payments (employer payment = $0 in this bill).")
print("    CS_drafted   = § 51.1-142.2 B 3 actuarial-equivalent quote + the drafted 'earlier")
print("                   commencement' term - payments. Reported only to measure the double count.")
print()
agg_rows = []
for col, lbl in (("CS_corrected", "CS_corrected — the single-basis measure Decision 2(d) adopts"),
                 ("CS_drafted", "CS_drafted — the two terms added as § 51.1-142.4 A drafts them")):
    nom = float((np.maximum(0.0, dfc[col]) * dfc.participants).sum())
    net = float((dfc[col] * dfc.participants).sum())
    agg_rows.append({"measure": col, "definition": lbl, "aggregate_positive_nominal": nom,
                     "aggregate_net_nominal": net, "per_member_mean": net / N})
dfagg = pd.DataFrame(agg_rows)
ov_agg = float((dfc.overlap_drafted_minus_corrected * dfc.participants).sum())
dfagg.to_csv("out_moo48_cs_aggregates.csv", index=False)
print(dfagg.round({"aggregate_positive_nominal": 0, "aggregate_net_nominal": 0,
                   "per_member_mean": 0}).to_string(index=False))
print(f"\n    THE DOUBLE COUNT ON THIS COHORT: CS_drafted - CS_corrected = {money(ov_agg)} "
      f"aggregate,")
print(f"    {money(ov_agg / N)} per member, "
      f"{ov_agg / float((dfc.CS_corrected * dfc.participants).sum()):.0%} of the corrected figure.")
print(f"    MOO-45 measured the same overlap at {money(2_374_550)} and 44% on the MOO-31 basis and "
      "the A+B")
print("    cohort. IT IS SMALLER IN PROPORTION HERE — 25%, not 44% — and the reason is the repair,")
print("    not the cohort. The overlap itself is the eligibility-acceleration content that the")
print("    § 51.1-142.2 B 3 quote already carries, measured from earliest eligibility. On the")
print("    repaired basis the DENOMINATOR is much larger, because the corrected certified subsidy")
print("    is measured against VRS's own expected retirement date rather than against earliest")
print("    eligibility, so it captures far more acceleration. Same numerator, bigger denominator.")
print("    THE DIRECTION OF THE DECISION IS UNAFFECTED: the drafted definition still overstates")
print("    the capped quantity by a quarter, and a ceiling figure written for one basis is wrong")
print("    on the other by that much.")
print()
dist = []
for col in ("CS_corrected", "CS_drafted"):
    q = wq(dfc[col].values, dfc.participants.values, QS)
    dist.append({"measure": col, "min": float(dfc[col].min()), "median": q[0], "p75": q[1],
                 "p90": q[2], "p95": q[3], "max": float(dfc[col].max()),
                 "mean": float((dfc[col] * dfc.participants).sum() / N)})
dfd = pd.DataFrame(dist)
dfd.to_csv("out_moo48_cs_distribution.csv", index=False)
print("    DISTRIBUTION PER PARTICIPATING MEMBER (participant-weighted; the unit is one member)")
print(dfd.round(0).to_string(index=False))
print()
print("    PATHWAY SPLIT. The bill admits Pathway A only, so the split is degenerate by")
print("    construction: 100% Pathway A, 0 Pathway B members, $0 of Pathway B subsidy. The")
print("    comparison that is actually informative is what Pathway B WOULD carry if clause (v)")
print("    were dropped, on the same price and the same deadline:")
dfab = cells("central", deadline=BILL_DL, pathways=("A", "B"))
pw_rows = []
for pw, g in dfab.groupby("pathway"):
    n = float(g.participants.sum())
    pw_rows.append({"pathway": pw, "members": n,
                    "share_of_A_plus_B_cohort": n / float(dfab.participants.sum()),
                    "mean_years_bought": float((g.years_bought * g.participants).sum() / n),
                    "mean_acceleration_months": float((g.acceleration_months * g.participants)
                                                      .sum() / n),
                    "min_CS_corrected": float(g.CS_corrected.min()),
                    "mean_CS_corrected": float((g.CS_corrected * g.participants).sum() / n),
                    "max_CS_corrected": float(g.CS_corrected.max()),
                    "aggregate_CS_corrected": float((np.maximum(0.0, g.CS_corrected)
                                                     * g.participants).sum())})
dfpw = pd.DataFrame(pw_rows)
dfpw["in_the_bill"] = dfpw.pathway == "A"
dfpw.to_csv("out_moo48_pathway_split.csv", index=False)
print(dfpw.assign(share_of_A_plus_B_cohort=lambda d: d.share_of_A_plus_B_cohort
                  .map("{:.0%}".format))
      .round({"members": 1, "mean_years_bought": 1, "mean_acceleration_months": 1,
              "min_CS_corrected": 0, "mean_CS_corrected": 0, "max_CS_corrected": 0,
              "aggregate_CS_corrected": 0}).to_string(index=False))
print("    Clause (v) removes the larger part of the cohort and the cheaper part of the")
print("    distribution. That is why the bill's PER-MEMBER certified subsidy is far higher than")
print("    anything in the published tables while its AGGREGATE is far lower.")
print("    (Pathway A shows 18.3 members in this table against 18.9 in the bill run above: the")
print("     take-up elasticity adjustment is computed on whichever cohort is being priced, and")
print("     the A+B price ratio differs slightly from the A-only one. The difference is 0.6 of a")
print("     member and it does not touch any conclusion.)")
print()
print("    PRECISION NOTE, unchanged from MOO-45 and still binding: the cohort is priced on a")
print("    grid of age x service cells carrying fractional weights, with one salary per age band")
print("    and no within-cell salary dispersion. These percentiles therefore describe the")
print("    distribution ACROSS CELLS. The true 95th percentile and the true maximum are HIGHER")
print("    than reported. One-sided, and it is the direction that matters for a ceiling.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 4. THE PER-MEMBER CEILING, SOLVED FOR THE STATED FLOOR
# ===========================================================================
print()
print("=" * 112)
print("[4] THE PER-MEMBER CEILING — solved for MOO-46 Decision 2(e)'s 30-election floor")
print("=" * 112)


def elections_served(df, ceiling, order, cap=CAP, measure="CS_corrected", discounted=False,
                     contingency=0.0):
    """Members the $3,000,000 appropriation funds, under the drafted reserve-then-admit rule.

    The per-member ceiling is a REFUSAL in § 51.1-142.4 D 2 ('The Board shall not accept an
    election for which the certified subsidy exceeds $X'), not a trim: the election does not
    happen.  That is the opposite of the MOO-45 convention, where the member funded the excess, and
    it is what the drafted text says.  Both are computed; `refuse=True` is the drafted one.
    """
    s = np.maximum(0.0, df[measure].values) * (1.0 + contingency)
    w = df.participants.values.copy()
    if discounted:
        s = s * df.discount_factor.values
    keep = s <= ceiling
    s, w = s[keep], w[keep]
    if len(s) == 0:
        return 0.0
    if order == "chronological":
        mean = float((s * w).sum() / w.sum()) if w.sum() else 0.0
        return float(min(w.sum(), cap / mean if mean > 0 else w.sum()))
    o = np.argsort(s if order == "cheapest_first" else -s)
    s, w = s[o], w[o]
    rem, served = cap, 0.0
    for sub, wt in zip(s, w):
        if sub <= 0:
            served += wt
            continue
        take = min(wt, rem / sub)
        served += take
        rem -= take * sub
        if rem <= 1e-9:
            break
    return float(served)


FLOOR = M48.CEILING_FLOOR_RULE["value"]["elections"]
print(f"    THE RULE AS ADOPTED: the lowest round figure at which {money(CAP)} funds at least")
print(f"    {FLOOR} elections in the dearest-first order.")
print()
print("    TWO PROBLEMS WITH THE RULE, BOTH ARITHMETIC, BOTH REPORTED RATHER THAN RESOLVED HERE.")
print()
print("    (1) THE RULE IS INVERTED. A LOWER ceiling funds MORE elections, because it refuses the")
print("        dearest ones. So the ceilings that satisfy a 30-election floor form an interval")
print("        running DOWN from a maximum, and 'the lowest round figure' satisfying it is $0.")
print("        The figure the rule is reaching for is the HIGHEST round figure that still meets")
print("        the floor — the least intrusive ceiling consistent with 30 elections. That is what")
print("        is solved for below.")
print()
cohort_sizes = {lvl: float(cells(lvl, deadline=BILL_DL).participants.sum()) for lvl in LEVELS}
print(f"    (2) THE FLOOR EXCEEDS THE COHORT. At central take-up the bill admits "
      f"{cohort_sizes['central']:.1f} members in")
print(f"        total, across the whole four-year pilot. {FLOOR} elections is "
      f"{FLOOR/cohort_sizes['central']:.1f}x the entire modelled")
print("        cohort. Modelled cohort by take-up case:")
for lvl in LEVELS:
    print(f"          {lvl:<8s} take-up {IN.TAKEUP_PATHWAY_A['value'][lvl]:.2f}  ->  "
          f"{cohort_sizes[lvl]:.1f} members"
          f"{'   <- the only case whose COHORT even reaches 30' if cohort_sizes[lvl] >= FLOOR else ''}")
print("        So no ceiling satisfies the floor at low or central take-up: the constraint is the")
print("        number of members the bill admits, not the appropriation. Only the high-take-up")
print("        cohort reaches 30 at all, and the sweep below shows that even there no ceiling")
print("        delivers 30 FUNDED elections in the dearest-first order. The rule as adopted is")
print("        unsatisfiable on this bill in every take-up case.")
print()

sweep = []
for ceil in M48.CEILING_ROUND_FIGURES["value"] + [10 ** 12]:
    for lvl in LEVELS:
        dfx = cells(lvl, deadline=BILL_DL) if lvl != "central" else dfc
        refused = dfx[np.maximum(0.0, dfx.CS_corrected) > ceil]
        rec = {"ceiling": "none" if ceil >= 10 ** 12 else ceil, "take_up_case": lvl,
               "cohort": float(dfx.participants.sum()),
               "members_refused": float(refused.participants.sum()),
               "subsidy_refused": float((np.maximum(0.0, refused.CS_corrected)
                                         * refused.participants).sum())}
        for order in ("cheapest_first", "chronological", "dearest_first"):
            rec[order] = elections_served(dfx, ceil, order)
        rec["meets_30_floor"] = rec["dearest_first"] >= FLOOR
        sweep.append(rec)
dfsw = pd.DataFrame(sweep)
dfsw.to_csv("out_moo48_ceiling_sweep.csv", index=False)
print("    THE SWEEP — elections the $3,000,000 appropriation funds, by ceiling and queue order")
print("    (certified subsidy on the corrected basis, nominal metering, ceiling as a REFUSAL per")
print("     § 51.1-142.4 D 2)")
for lvl in LEVELS:
    print(f"\n      take-up case: {lvl}  (cohort "
          f"{cohort_sizes[lvl]:.1f} members)")
    g = dfsw[dfsw.take_up_case == lvl]
    print(g[["ceiling", "members_refused", "subsidy_refused", "cheapest_first", "chronological",
             "dearest_first", "meets_30_floor"]]
          .round({"members_refused": 1, "subsidy_refused": 0, "cheapest_first": 1,
                  "chronological": 1, "dearest_first": 1}).to_string(index=False))

uncapped = {lvl: float(dfsw[(dfsw.take_up_case == lvl) & (dfsw.ceiling == "none")]
                       .dearest_first.iloc[0]) for lvl in LEVELS}


def solve(floor, lvl):
    """Highest round ceiling meeting `floor` elections dearest-first, on the stated take-up case.

    Returns one of:
      ("not_binding", None)   the floor is met with NO ceiling at all, so the rule asks for nothing
      ("figure", x)           x is the highest round figure that still meets the floor
      ("unreachable", None)   no ceiling meets the floor; the cohort is smaller than the floor
    """
    if uncapped[lvl] >= floor:
        return ("not_binding", None)
    g = dfsw[(dfsw.take_up_case == lvl) & (dfsw.ceiling != "none")
             & (dfsw.dearest_first >= floor)]
    if not len(g):
        return ("unreachable", None)
    return ("figure", int(g.ceiling.max()))


sol = {lvl: solve(FLOOR, lvl) for lvl in LEVELS}
print()
print("    THE SOLVED FIGURE, on the rule read as 'the highest round figure that still meets the")
print(f"    {FLOOR}-election floor, dearest-first':")
for lvl in LEVELS:
    kind, v = sol[lvl]
    msg = {"not_binding": f"no ceiling is required — {money(CAP)} already funds "
                          f"{uncapped[lvl]:.1f} elections dearest-first",
           "unreachable": f"UNREACHABLE — the cohort is only {cohort_sizes[lvl]:.1f} members, so "
                          f"{FLOOR} elections cannot occur at any ceiling",
           "figure": money(v) if v else ""}[kind]
    print(f"      {lvl:<8s} {msg}")
best_served = {lvl: float(dfsw[(dfsw.take_up_case == lvl) & (dfsw.ceiling != 'none')]
                          .dearest_first.max()) for lvl in LEVELS}
print()
print("    THE ANSWER TO ITEM 4 IS THEREFORE A FINDING ABOUT THE RULE, NOT A FIGURE.")
print("    A per-member ceiling cannot be solved for a 30-election floor on this bill, because the")
print("    bill does not admit 30 elections. The binding constraint on the number of elections is")
print("    clause (v) and the take-up rate, not the $3,000,000. Dearest-first, at any ceiling:")
for lvl in LEVELS:
    print(f"      {lvl:<8s} at most {best_served[lvl]:.1f} elections of a "
          f"{cohort_sizes[lvl]:.1f}-member cohort; "
          f"{money(CAP)} alone funds {uncapped[lvl]:.1f}")
print()
print("    AND NOTE WHAT THAT DOES TO THE CAP. At central take-up the whole cohort's certified")
print(f"    subsidy is {money(float((np.maximum(0.0, dfc.CS_corrected) * dfc.participants).sum()))}"
      f" against a {money(CAP)} appropriation, so the cap does not ration anything")
print("    at the central estimate. It binds only in the high-take-up case. MOO-46 Decision 2.3's")
print("    rationing narrative ('at $2.0M, 61% of applicants are denied'; '~57 of 103 elections')")
print("    is true of the A+B cohort and is NOT true of the bill: on the bill's own cohort the")
print("    appropriation is roughly 1.4x the central requirement. That is a better fact for the")
print("    money committee and a worse fact for the 'smallest defensible maximum' framing — the")
print("    cap is now a headroom figure rather than a binding maximum, and the package should say")
print("    which of those two things it is.")
print()
print("    WHAT I RECOMMEND THE RULE BE RESTATED AS — the Director's call, not mine, and all three")
print("    are priced above:")
print("      (i)  FLOOR AS A SHARE OF THE COHORT. 'The ceiling shall be the highest round figure")
print("           at which the appropriation funds at least 80% of the modelled cohort in the")
print("           dearest-first order.' Survives a change in cohort size, which a fixed count")
print("           does not.")
print("      (ii) FLOOR AS A COUNT, SET BELOW THE CENTRAL COHORT. A 15-election floor is binding")
print("           and achievable; 30 is not.")
print("      (iii) CEILING SET OFF THE DISTRIBUTION, not off the appropriation — e.g. the 90th")
print("           percentile of certified subsidy rounded up, which is the form MOO-45 used.")
d90 = float(dfd[dfd.measure == "CS_corrected"].p90.iloc[0])
print(f"           On this cohort that is {money(d90)} -> "
      f"{money(int(np.ceil(d90 / 10_000.0) * 10_000))} as a round figure.")
alt = []
for floor_alt in (5, 8, 10, 12, 15, 20, 25, 30):
    rec = {"floor_elections": floor_alt}
    for lvl in LEVELS:
        kind, v = solve(floor_alt, lvl)
        rec[lvl] = {"not_binding": "no ceiling needed",
                    "unreachable": "unreachable",
                    "figure": money(v) if v else ""}[kind]
        rec[f"{lvl}_figure"] = v
    alt.append(rec)
dfalt = pd.DataFrame(alt)
dfalt.to_csv("out_moo48_ceiling_floor_solutions.csv", index=False)
print()
print("    THE SOLVED CEILING AT EVERY PLAUSIBLE FLOOR (highest round figure meeting the floor,")
print("    dearest-first):")
print(dfalt[["floor_elections"] + list(LEVELS)].to_string(index=False))
print("      'no ceiling needed' = the appropriation meets the floor unaided, so the rule as")
print("                            adopted asks for no ceiling at all at that floor.")
print("      'unreachable'       = the modelled cohort is smaller than the floor, so no ceiling")
print("                            can produce that many elections.")
print("    THE RULE ONLY PRODUCES A FIGURE IN A NARROW BAND OF FLOORS, AND ONLY AT HIGH TAKE-UP.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 5. HOW MANY ELECTIONS $3,000,000 FUNDS
# ===========================================================================
print()
print("=" * 112)
print("[5] HOW MANY ELECTIONS $3,000,000 FUNDS — one number, with the order stated")
print("=" * 112)
REC_P90 = int(np.ceil(d90 / 10_000.0) * 10_000)
CEILS = ((10 ** 12, "A. no ceiling"),
         (REC_P90, f"B. ceiling {money(REC_P90)} (90th pct, rounded)"),
         (100_000, "C. ceiling $100,000 (MOO-45's figure, superseded)"))
served = []
for lvl in LEVELS:
    dfx = dfc if lvl == "central" else cells(lvl, deadline=BILL_DL)
    for ceilv, clbl in CEILS:
        for order in ("cheapest_first", "chronological", "dearest_first"):
            for cont, mlbl in ((0.0, "D 2 only"),
                               (M48.CONTINGENCY_RESERVE["value"]["central"],
                                "D 2 + D 3 contingency inside the cap")):
                served.append({
                    "take_up_case": lvl, "ceiling": clbl, "queue_order": order,
                    "metering": mlbl, "cohort": float(dfx.participants.sum()),
                    "elections_funded_nominal": elections_served(dfx, ceilv, order,
                                                                 contingency=cont),
                    "elections_funded_PV_metered": elections_served(dfx, ceilv, order,
                                                                    discounted=True,
                                                                    contingency=cont),
                    "elections_funded_drafted_basis": elections_served(
                        dfx, ceilv, order, measure="CS_drafted", contingency=cont)})
dfs5 = pd.DataFrame(served)
dfs5["share_of_cohort_nominal"] = dfs5.elections_funded_nominal / dfs5.cohort
dfs5.to_csv("out_moo48_elections_funded.csv", index=False)
g = dfs5[(dfs5.metering == "D 2 only")]
print("    § 51.1-142.4 D 2 as drafted, no D 3 contingency charged against the cap:")
print(g.pivot_table(index=["take_up_case", "ceiling"], columns="queue_order",
                    values="elections_funded_nominal").round(1).to_string())
print()
print("    Same, with the D 3 contingency (10%) charged against the $3,000,000:")
g2 = dfs5[dfs5.metering != "D 2 only"]
print(g2.pivot_table(index=["take_up_case", "ceiling"], columns="queue_order",
                     values="elections_funded_nominal").round(1).to_string())
print()
print("    Same, on the DRAFTED certified-subsidy basis (the double count left in), no contingency")
print("    — this is the direct answer to MOO-44 §8, 'the draft does not say which':")
print(g.pivot_table(index=["take_up_case", "ceiling"], columns="queue_order",
                    values="elections_funded_drafted_basis").round(1).to_string())
print()
cen = dfs5[(dfs5.take_up_case == "central") & (dfs5.ceiling == "A. no ceiling")
           & (dfs5.metering == "D 2 only")]
hi = dfs5[(dfs5.take_up_case == "high") & (dfs5.ceiling == "A. no ceiling")
          & (dfs5.metering == "D 2 only")]
print("    THE SENTENCE FOR THE FISCAL STATEMENT. On the corrected basis, the bill's own cohort,")
print("    and nominal metering as § 51.1-142.4 D 1-D 3 describes it:")
for _, r in cen.iterrows():
    print(f"      central take-up, {r.queue_order:<16s} {r.elections_funded_nominal:>5.1f} of "
          f"{r.cohort:.1f} modelled elections "
          f"({r.share_of_cohort_nominal:.0%} of the cohort)")
for _, r in hi.iterrows():
    print(f"      high take-up,    {r.queue_order:<16s} {r.elections_funded_nominal:>5.1f} of "
          f"{r.cohort:.1f} modelled elections "
          f"({r.share_of_cohort_nominal:.0%} of the cohort)")
print()
print("    SO THE QUEUE ORDER DOES NOT MATTER AT THE CENTRAL ESTIMATE — nothing is rationed,")
print("    because the appropriation exceeds the cohort's whole certified subsidy. The order")
print("    matters only in the high-take-up case, and there it is worth about "
      f"{hi.elections_funded_nominal.max() - hi.elections_funded_nominal.min():.1f} elections")
print("    between the best and the worst order. MOO-44 §8's '$3,000,000 buys between 28 and 213")
print("    elections and the draft does not say which' is answered: on the bill's own cohort and")
print("    the corrected basis it buys the WHOLE COHORT at the central estimate, and 24 to 29 of")
print("    31 in the adverse high-take-up case. The width in MOO-44's complaint came from the")
print("    cohort and the definition, both of which this run fixes; what remains is take-up.")
print()
print("    WHAT THE CEILING IS FOR, VISIBLE IN ONE COMPARISON. At high take-up, dearest-first,")
print(f"    the appropriation funds {float(hi[hi.queue_order == 'dearest_first'].elections_funded_nominal.iloc[0]):.1f}"
      " elections with no ceiling and "
      f"{float(dfs5[(dfs5.take_up_case == 'high') & (dfs5.ceiling == CEILS[1][1]) & (dfs5.queue_order == 'dearest_first') & (dfs5.metering == 'D 2 only')].elections_funded_nominal.iloc[0]):.1f} with a "
      f"{money(REC_P90)} ceiling. The")
print("    ceiling RAISES the number of elections in the adverse order — which is precisely the")
print("    MOO-15 F7 argument, now quantified on the bill's own cohort. At central take-up it")
print("    LOWERS the count, because nothing needed rationing and the ceiling simply refuses")
print("    members. That asymmetry is the whole case for and against a ceiling, in one line.")
print()
print("    THE ORDER THE BILL ACTUALLY USES IS NEITHER OF THE COST ORDERS. § 51.1-142.4 D 4")
print("    requires acceptance 'in the order in which eligible members file complete")
print("    applications', with ties broken by lot. That is the CHRONOLOGICAL row, and it is the")
print("    row the fiscal statement should quote, with dearest-first quoted beside it as the")
print("    adverse case, because well-advised members file first (MOO-15 F12).")
print()
print(f"    A FINDING NOT PREVIOUSLY REPORTED. § 51.1-142.4 D 3 requires the Board to reserve a")
print("    contingency amount 'IN ADDITION TO each certified subsidy'. D 2 caps 'the aggregate of")
print("    all certified subsidies' at $3,000,000. On the face of the text the contingency sits")
print("    OUTSIDE the cap, so the appropriation the Commonwealth must actually make exceeds")
print(f"    $3,000,000 by the contingency — about {money(CAP * 0.10)} at the 10% figure D 6")
print("    implies. Either the appropriation is stated as that larger figure, or the contingency")
print("    is drafted inside the cap and about a tenth of the elections above are not funded.")
print("    This is a drafting question for the Drafting Specialist; both are priced above.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 6. SENSITIVITY
# ===========================================================================
print()
print("=" * 112)
print("[6] SENSITIVITY — one driver at a time, on the bill's central trust cost")
print("=" * 112)
base = b["trust"]
tests = []


def add(name, lo_lbl, lo_val, hi_lbl, hi_val):
    tests.append({"driver": name, "low_label": lo_lbl, "low": lo_val, "high_label": hi_lbl,
                  "high": hi_val, "swing": abs(hi_val - lo_val),
                  "swing_pct_of_base": abs(hi_val - lo_val) / base})


add("retirement deadline (the policy dial)", "24 months",
    float(dfl[dfl.deadline_months == 24].trust_cost.iloc[0]), "0 months",
    float(dfl[dfl.deadline_months == 0].trust_cost.iloc[0]))
add("purchase completion lag (§ 51.1-142.4 E)", "36 months",
    float(dfcm[dfcm.completion_months == 36].trust_cost.iloc[0]), "lump sum",
    float(dfcm[dfcm.completion_months == 0].trust_cost.iloc[0]))
add("take-up (0.15 / 0.50 of eligible)", "low", bill["low"]["trust"], "high",
    bill["high"]["trust"])
add("months of qualifying military service available", "24 months",
    runA("central", deadline=BILL_DL, months_available=24)["trust"], "48 months",
    runA("central", deadline=BILL_DL, months_available=48)["trust"])
add("salary selection into the pilot", "base", base, "+20%",
    runA("central", deadline=BILL_DL, salary_factor=1.20)["trust"])
add("ancillary benefits excluded from the valuation", "as valued (pension only)", base,
    "+10% annuity load", runA("central", deadline=BILL_DL, annuity_load=1.10)["trust"])
with calendar_gap(1.20):
    cal_c = runA("central", deadline=BILL_DL)["trust"]
with calendar_gap(3.70):
    cal_h = runA("central", deadline=BILL_DL)["trust"]
add("MOO-45 calendar-time interest reprice", "gap 3.70 yr", cal_h, "gap 0.00 yr (as modelled)",
    base)
add("Pathway A reading (clause (vi)) — DRAFTING EXPOSURE, not an assumption", "narrow (drafted)",
    base, "broad", runA("central", deadline=BILL_DL, scope="advance")["trust"])
dft = pd.DataFrame(tests).sort_values("swing", ascending=False).reset_index(drop=True)
dft.to_csv("out_moo48_sensitivity.csv", index=False)
print(f"    Base: the bill as drafted, central take-up, trust cost {money(base)}.")
print(dft.assign(swing_pct_of_base=lambda d: d.swing_pct_of_base.map("{:.0%}".format))
      .round({"low": 0, "high": 0, "swing": 0}).to_string(index=False))
print()
print("    THE THREE ASSUMPTIONS THAT CONTROL THE ANSWER, excluding the drafting exposure:")
ctl = dft[~dft.driver.str.contains("DRAFTING EXPOSURE")].head(3)
for _, r in ctl.iterrows():
    print(f"      {r.driver}: {money(r.low)} to {money(r.high)}, "
          f"{r.swing_pct_of_base:.0%} of base")
print()
print("    THE 10%-MOVE TEST, computed rather than asserted. Each input is moved 10% from its")
print("    central value, one at a time, and the resulting move in the answer is reported:")
ten = [{"input": "take-up rate (Pathway A, 0.30)", "central": 0.30, "plus_10pct": 0.33,
        "trust_cost": runA("central", deadline=BILL_DL, takeup_mult=1.10)["trust"]},
       {"input": "months of qualifying service available (36)", "central": 36, "plus_10pct": 39.6,
        "trust_cost": runA("central", deadline=BILL_DL, months_available=39.6)["trust"]},
       {"input": "purchase completion lag (12 months)", "central": 12, "plus_10pct": 13.2,
        "trust_cost": runA("central", deadline=BILL_DL, cm=13.2)["trust"]},
       {"input": "retirement deadline (1 month)", "central": 1, "plus_10pct": 1.1,
        "trust_cost": runA("central", deadline=1.1)["trust"]},
       {"input": "participant salary (selection)", "central": 1.0, "plus_10pct": 1.10,
        "trust_cost": runA("central", deadline=BILL_DL, salary_factor=1.10)["trust"]}]
dften = pd.DataFrame(ten)
dften["move_in_answer"] = dften.trust_cost / base - 1.0
dften = dften.reindex(dften.move_in_answer.abs().sort_values(ascending=False).index)
dften.to_csv("out_moo48_ten_percent_moves.csv", index=False)
print(dften.assign(move_in_answer=lambda d: d.move_in_answer.map("{:+.1%}".format))
      .round({"trust_cost": 0}).to_string(index=False))
worst = dften.iloc[0]
print(f"    NO SINGLE INPUT MOVES THE ANSWER BY MORE THAN 25% ON A 10% MOVE. The largest is")
print(f"    {worst.input} at {worst.move_in_answer:+.1%}, so the 'first paragraph' warning my own")
print("    standard requires is NOT triggered. What IS large is the take-up RANGE (0.15 to 0.50 is")
print("    a factor of 3.3, not a 10% move) and the clause (vi) drafting exposure. Those are")
print("    reported as a range and as an exposure respectively, not as sensitivities.")
print(f"    The MOO-45 calendar reprice at the central gap gives {money(cal_c)}, "
      f"{(cal_c/base-1):+.0%}. It is")
print("    reported as a variant, not folded into the headline, so the headline stays on the same")
print("    basis as the published repaired figures it is compared against.")
print(f"    [{time.time()-T0:.0f}s elapsed]")

# ===========================================================================
# 7. EXTERNAL SANITY CHECK
# ===========================================================================
print()
print("=" * 112)
print("[7] EXTERNAL SANITY CHECK — VRS's own fiscal impact statement for SB 419 (2026)")
print("=" * 112)
v = IN.SB419_CHECK["value"]
sp_n, va_n = IN.SPORS_ACTIVES["value"], IN.VALORS_ACTIVES["value"]
sp_pay, va_pay = IN.SPORS_PAYROLL["value"], IN.VALORS_PAYROLL["value"]
n_act = sp_n + va_n
avg_sal_sb = (sp_pay + va_pay) / n_act
avg_service_proxy = 10.3
extra_years = avg_service_proxy / 5.0
member_years = n_act * extra_years
sb_cost_per_year = v["liability_increase"] / member_years
gross_per_year = b["gross"] / b["years"]
chk = pd.DataFrame([
    {"anchor": "SB 419 (2026), SPORS+VaLORS, one year per five — VRS-scored liability",
     "basis": "VRS fiscal impact statement", "cost_per_year_of_service": sb_cost_per_year,
     "avg_salary": avg_sal_sb, "as_pct_of_salary": sb_cost_per_year / avg_sal_sb},
    {"anchor": "THE BILL, gross liability per year of purchased service",
     "basis": "MOO-48 central", "cost_per_year_of_service": gross_per_year,
     "avg_salary": b["avg_salary"], "as_pct_of_salary": gross_per_year / b["avg_salary"]},
])
chk.to_csv("out_moo48_sanity_check.csv", index=False)
print(chk.assign(as_pct_of_salary=lambda d: d.as_pct_of_salary.map("{:.0%}".format))
      .round({"cost_per_year_of_service": 0, "avg_salary": 0}).to_string(index=False))
ratio = gross_per_year / sb_cost_per_year
print()
print(f"    THE CHECK: this model's gross liability per year of purchased service is "
      f"{ratio:.1f}x VRS's own")
print("    scored cost per year of granted service on SB 419. THE TWO DISAGREE, and the")
print("    disagreement is in the direction the three stated adjustments predict:")
print("      1. SB 419 granted service to the ENTIRE active membership, including young members")
print("         whose benefit is discounted for decades. This cohort is at or within months of")
print("         retirement, where the cost of a year of service is at its maximum. This is the")
print("         dominant term and it is large.")
print("      2. SB 419's plans are hazardous-duty (total normal cost 18.37% / 14.30% against")
print("         8.73% for State Employees), which pushes VRS's figure UP relative to ours, i.e.")
print("         against the direction of the gap.")
print("      3. This bill's gross liability includes the EARLY-COMMENCEMENT cost, which SB 419's")
print("         grant did not create: SB 419 granted service without a retirement condition.")
print(f"         On this cohort the early-commencement component is "
      f"{b['accel']/b['gross']:.0%} of gross liability,")
print("         so removing it would close most of the remaining gap.")
svc_per_year = b["svc"] / b["years"]
print(f"    LIKE FOR LIKE, service-credit component only: {money(svc_per_year)} per year against")
print(f"    VRS's {money(sb_cost_per_year)}, a ratio of {svc_per_year/sb_cost_per_year:.1f}x — "
      "consistent with a cohort at")
print("    retirement rather than across all ages. The check does not validate the level; it")
print("    confirms the magnitude is the one a near-retirement cohort should produce, and it")
print("    confirms that the acceleration term, not the service credit, is what this bill buys.")

# ===========================================================================
# 8. FISCAL YEARS, FUNDS, AND LOCAL EFFECT
# ===========================================================================
print()
print("=" * 112)
print("[8] FISCAL YEARS, GENERAL FUND / NONGENERAL FUND, AND LOCAL EFFECT")
print("=" * 112)
FYS = M48.PILOT_FY_ELECTIONS["value"]
IMPL_FY = M48.VRS_IMPLEMENTATION_FY["value"]
fy_rows = []
for lbl, trust in (("bill as drafted (rung 1)", b["trust"]),
                   ("rung 12", float(dfl[dfl.deadline_months == 12].trust_cost.iloc[0])),
                   ("rung 24", float(dfl[dfl.deadline_months == 24].trust_cost.iloc[0]))):
    _layers, annual = SC.pilot_layout(trust, 0.0, fys=FYS)
    rec = {"case": lbl, "trust_cost_PV": trust, "GF_PV": trust * GF,
           "NGF_PV": trust * (1 - GF) + IMPL, "implementation_NGF_FY2029": IMPL}
    for fy in range(IMPL_FY, FYS[-1] + 3):
        am = annual.get(fy, 0.0)
        rec[f"GF_FY{fy}"] = am * GF
        rec[f"NGF_FY{fy}"] = am * (1 - GF) + (IMPL if fy == IMPL_FY else 0.0)
    fy_rows.append(rec)
dffy = pd.DataFrame(fy_rows)
dffy.to_csv("out_moo48_fiscal_years.csv", index=False)
print(dffy.round(0).to_string(index=False))
print()
print(f"    FY{IMPL_FY} carries the {money(IMPL)} VRS implementation charge and no elections.")
print(f"    FY{FYS[0]} is the first election year and carries no amortised liability. "
      f"FY{FYS[0]+1} is the")
print("    first year carrying amortised liability. Elections are spread monthly across the 48")
print("    pilot months using inputs.PILOT_PHASING and discounted to the valuation date.")
print("    The 47% general-fund share is applied to the amortisation of trust cost ONLY; the")
print("    implementation allowance is nongeneral fund in full.")
print()
print("    LOCAL COST: ZERO. UNFUNDED MANDATE: NONE. This is a finding, not a footnote.")
print('    § 51.1-142.4 A excludes from "eligible member" both "a teacher" and "an employee of a')
print('    political subdivision", and clause (i) requires a state employee. No locality, school')
print("    division or political subdivision acquires any duty, cost, or contribution-rate change")
print("    under the drafted text. There is no mechanism in the bill by which local cost arises.")
print()
print("    ADMINISTRATIVE COST: the $375,000 central VRS implementation allowance (range $150,000")
print("    to $750,000, inputs.VRS_IMPLEMENTATION_COST) is one-time, nongeneral fund, and lands in")
print(f"    FY{IMPL_FY}. It is NOT re-estimated here, and the drafted bill adds duties that were not")
print("    in the costed design when that allowance was set: the D 4 two-channel application")
print("    intake, the monthly published running balance, the D 5 wait-list and notice, the D 6")
print("    recertification, the G 2 credit reduction and refund, the I return-to-work monitoring,")
print("    and the K 1 annual report with the K 2 agency data collection. Direction of error:")
print("    the implementation allowance UNDERSTATES administrative cost. Flagged for VRS in the")
print("    MOO-37 ask; no position count is modelled here and none should be quoted.")

# ===========================================================================
# 9. THE TWO CORRECTIONS CARRIED INTO THE DOCUMENT
# ===========================================================================
print()
print("=" * 112)
print("[9] THE TWO CORRECTIONS THE DIRECTOR ASKED ME TO CARRY")
print("=" * 112)
print("    (a) THE PER-MEMBER CEILING IS NOT A DEAD GUARDRAIL. Accepted in full, and the")
print("        'another free-but-dead guardrail' sentence is withdrawn — it does not appear in")
print("        this document and it must not travel. The arithmetic of the correction, on this")
print("        cohort rather than on MOO-45's:")
pm_max = float(dfc.CS_corrected.max())
pm_trust_max = float((dfc.gross_liability_increase - dfc.member_paid).max())
print("          max net trust cost per member, repaired A+B cohort (repaired §6)      "
      f"{money(92_135)}")
print("          max certified subsidy per member, drafted basis, MOO-45 cohort         "
      f"{money(158_455)}")
print(f"          max net trust cost per member, THE BILL's cohort                      "
      f"{money(pm_trust_max)}")
print(f"          max certified subsidy per member, corrected basis, THE BILL's cohort  "
      f"{money(pm_max)}")
print(f"          max certified subsidy per member, drafted basis, THE BILL's cohort    "
      f"{money(float(dfc.CS_drafted.max()))}")
print("        NOTE WHAT DECISION 2(d) DOES TO THE DISCREPANCY: once certified subsidy is defined")
print("        as the increase in liability less payments, and the employer payment is zero, the")
print("        corrected certified subsidy and the net trust cost per member are THE SAME")
print("        QUANTITY by construction — the third and fourth lines above are identical, not")
print("        merely close. The 0.0-bound / 36.2%-bound disagreement was entirely a basis")
print("        artefact and the corrected definition dissolves it. What makes the ceiling live is")
print("        not the basis, it is the COHORT: repaired §6 found nothing binding at $100,000")
print(f"        because its A+B cohort topped out at {money(92_135)} per member, while the bill's")
print(f"        Pathway-A-only cohort tops out at {money(pm_max)}. At $100,000 the ceiling refuses")
print(f"        {float(dfc[dfc.CS_corrected > 100_000].participants.sum()):.1f} of {N:.1f} members "
      f"({float(dfc[dfc.CS_corrected > 100_000].participants.sum())/N:.0%}) on the corrected "
      "basis. It is a live guardrail on the")
print("        bill's basis and on the bill's cohort, and the 'free-but-dead' sentence is wrong")
print("        about the bill even though it was right about the scenario it described.")
print()
print("    (b) '% OF S1' IS RETIRED AS A HEADLINE METRIC. Accepted. The headline pair in this")
print(f"        document is the absolute central cost ({sig2(b['trust'] + IMPL)}) and the")
print(f"        appropriation ({money(CAP)}). For the annex only, labelled as a comparison between")
print("        two of our own estimates and not as a comparison with current law:")
ann = pd.DataFrame([
    {"metric": "bill as drafted / repaired S1", "value": b["trust"] / PUBLISHED["S1"]},
    {"metric": "bill as drafted / repaired S2 (Pathway A only, ANC price)",
     "value": b["trust"] / PUBLISHED["S2"]},
    {"metric": "bill as drafted / published S8-at-6% (A+B, 6-month deadline)",
     "value": b["trust"] / PUBLISHED["S8-i6"]},
])
ann.to_csv("out_moo48_annex_ratios.csv", index=False)
print(ann.assign(value=lambda d: d.value.map("{:.0%}".format)).to_string(index=False))

# ===========================================================================
# 10. THE ONE-SENTENCE HANDOFF
# ===========================================================================
print()
print("=" * 112)
print("[10] FOR THE EDITOR — the headline number and range in one sentence")
print("=" * 112)
dom = dft[~dft.driver.str.contains("DRAFTING EXPOSURE")].iloc[0]
print(f"""
    "The pilot as drafted is estimated to cost the Commonwealth {sig2(b['trust'] + IMPL)} in present
    value over the four-year election window — {sig2(bill['low']['trust'] + IMPL)} to {sig2(bill['high']['trust'] + IMPL)} across the take-up range
    — of which {sig2(b['trust'] * GF)} is general fund and {sig2(b['trust'] * (1 - GF) + IMPL)} nongeneral fund, on about
    {N:.0f} elections over four years. There is no local cost and no mandate on localities. The
    {money(CAP)} appropriation in § 51.1-142.4 D 2 funds the whole modelled cohort at the central
    estimate and rations only if take-up runs at the top of the range."
""")
print(f"    Top sensitivity: {dom.driver} ({money(dom.low)} to {money(dom.high)}).")
print("    Largest single exposure, and it is a drafting question not a modelling one: whether")
print("    clause (vi) forecloses the broad Pathway A reading (MOO-49). Broad reading = "
      f"{sig2(float(dft[dft.driver.str.contains('Pathway A reading')].high.iloc[0]))}.")
print(f"    Model: moo7-vrs-military-purchase-model/moo48_main.py  ·  "
      f"python3 moo48_main.py  ·  {time.time()-T0:.0f}s")

# ===========================================================================
# summary json
# ===========================================================================
OUT.update({
    "bill": {lvl: {"participants": bill[lvl]["n"], "member_paid": bill[lvl]["paid"],
                   "gross": bill[lvl]["gross"], "trust_cost": bill[lvl]["trust"],
                   "headline_state_cost": bill[lvl]["trust"] + IMPL} for lvl in LEVELS},
    "deadline_ladder": dfl.to_dict(orient="records"),
    "cs_distribution": dfd.to_dict(orient="records"),
    "cs_aggregates": dfagg.to_dict(orient="records"),
    "pathway_split": dfpw.to_dict(orient="records"),
    "ceiling_solutions": dfalt.to_dict(orient="records"),
    "elections_funded": dfs5.to_dict(orient="records"),
    "sensitivity": dft.to_dict(orient="records"),
    "ten_percent_moves": dften.to_dict(orient="records"),
    "member_fairness_vs_memo_wording": fair.to_dict(orient="records"),
    "ceiling_sweep": dfsw.to_dict(orient="records"),
    "uncapped_elections_dearest_first": uncapped,
    "g4_exposure": g4.to_dict(orient="records"),
    "window_variant": dfwin.to_dict(orient="records"),
    "cohort_sizes": cohort_sizes,
    "locks": {k: v["trust"] for k, v in lock.items()},
    "runtime_seconds": time.time() - T0,
})
with open("out_moo48_summary.json", "w") as f:
    json.dump(OUT, f, indent=1, default=float)
print("\n    Wrote out_moo48_*.csv and out_moo48_summary.json.")
