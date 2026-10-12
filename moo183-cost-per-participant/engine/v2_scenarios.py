"""
v2 - S0 through S9 on the repaired basis.

Repairs implemented here, each tied to the finding that forced it:

  F1  retirement dates are explicit monthly dates (v2_liability), and the counterfactual is VRS's
      own decrement assumption rather than an analyst lag.
  F2  the cohort is advanced monthly from the 6/30/2025 census through the end of the pilot, is
      plan-specific, assigns tier on membership tenure, and makes Pathway A and B mutually
      exclusive with one election per member (v2_cohort).
  F3  the aggregate cap is an ADMISSION RULE: VRS certifies the subsidy, the appropriation is
      reserved, and applicants are denied once it is exhausted.  S4's member / agency / trust
      ledgers are reported separately and reconciled; nothing is set to zero by assignment.
  F6  the workforce offset is NOT netted into any scenario headline.
  F7  selected-cohort tests (salary selection, longevity selection) are run on the repaired base
      and reported, and a per-member subsidy ceiling is tested alongside the aggregate cap.

Liabilities are PV at each election month and then discounted to the 6/30/2025 valuation date, so
elections made in different pilot years are never added at face value.
"""
import inputs as IN
import s8
import s9 as S9M
import v2_cohort as C
import v2_liability as L
from pricing import Pricer, Profile

PR = Pricer()
EL = IN.TAKEUP_PRICE_ELASTICITY["value"]
PILOT_FY = IN.PILOT_FY["value"]
PHASING = IN.PILOT_PHASING["value"]
PRE_PILOT_MONTHS = 24          # 2025-06-30 valuation date -> 2027-07-01 pilot open
PILOT_MONTHS = 48
I_NOM = IN.DISCOUNT_RATE["value"]

_LEDGER_CACHE = {}


# ---------------------------------------------------------------------------
# election schedule
# ---------------------------------------------------------------------------
def election_schedule():
    """(month_index, fiscal_year, share_of_total_elections) for each of the 48 pilot months."""
    out = []
    for k, (fy, share) in enumerate(zip(PILOT_FY, PHASING)):
        for j in range(12):
            out.append((PRE_PILOT_MONTHS + 12 * k + j, fy, share / 12.0))
    return out


# ---------------------------------------------------------------------------
# the eligible, veteran-filtered, take-up-adjusted election flow
# ---------------------------------------------------------------------------
def build_elections(takeup_A=None, takeup_B=None, months_available=None, vet_qual=None,
                    age_skew=None, vet_share=None, plans=("plan1", "plan2", "hybrid"),
                    pathways=("A", "B"), salary_factor=1.0, service_match_cap=False,
                    scope=None):
    """One list of candidate elections across the whole pilot, as expected weights.

    The stock is projected monthly once and reused; take-up is applied as a per-month hazard so the
    four-year pilot does not enrol the same member twice (one election per member, red team F12).
    """
    snaps = _stock(months_available is None)
    tA = IN.TAKEUP_PATHWAY_A["value"]["central"] if takeup_A is None else takeup_A
    tB = IN.TAKEUP_PATHWAY_B["value"]["central"] if takeup_B is None else takeup_B
    sched = election_schedule()
    out = []
    # convert the pilot-total take-up into a per-month share using the phasing
    for midx, fy, share in sched:
        if midx >= len(snaps):
            break
        for c in snaps[midx]:
            if c["plan"] not in plans:
                continue
            path, yrs, t_elig = C.classify(c["plan"], c["age"], c["service"], months_available,
                                           scope)
            if path is None or path not in pathways:
                continue
            if service_match_cap and yrs > c["service"]:
                yrs = c["service"]
            if yrs <= 0:
                continue
            t = tA if path == "A" else tB
            vet = _vet(c["weight"], age_skew, vet_qual, vet_share)
            w = vet * t * share       # `share` sums to 1.0 across the 48 pilot months
            if w <= 1e-12:
                continue
            # the cell salary is an age-band average at the 6/30/2025 valuation date; project it to
            # the election month on VRS's own individual salary scale
            sal = L.salary_at(c["cell_salary"] * (1.0 + IN.LONG_SERVICE_PREMIUM["value"]),
                              c["service_at_valuation"], c["service"]) * salary_factor
            out.append({"plan": c["plan"], "sex": c["sex"], "age": c["age"],
                        "service": c["service"], "salary": sal, "years": yrs,
                        "pathway": path, "weight": w, "month": midx, "fy": fy,
                        "months_to_eligibility": t_elig * 12.0})
    return out


_ELECTIONS = {}


def build_elections_cached(takeup_A, takeup_B, **kw):
    """Elections scale LINEARLY in take-up, so the structure is built once per (filter set) and
    the weights are rescaled.  Cheap, exact, and it is what keeps the dial sweeps rerunnable."""
    key = (tuple(sorted((k, (tuple(v) if isinstance(v, (list, tuple)) else v))
                        for k, v in kw.items())),)
    base = _ELECTIONS.get(key)
    if base is None:
        base = build_elections(1.0, 1.0, **kw)
        _ELECTIONS[key] = base
    out = []
    for e in base:
        d = dict(e)
        d["weight"] = e["weight"] * (takeup_A if e["pathway"] == "A" else takeup_B)
        out.append(d)
    return out


_STOCK = {}


def _stock(default=True):
    key = "default"
    if key not in _STOCK:
        _STOCK[key] = C.project_stock(PRE_PILOT_MONTHS + PILOT_MONTHS)
    return _STOCK[key]


def _vet(count, age_skew=None, qual=None, vet_share=None):
    vs = IN.VETERAN_SHARE_WORKFORCE["value"] if vet_share is None else vet_share
    sk = IN.VETERAN_AGE_SKEW["value"] if age_skew is None else age_skew
    q = IN.QUALIFYING_SERVICE_SHARE["value"] if qual is None else qual
    return count * vs * sk * q


# ---------------------------------------------------------------------------
# prices
# ---------------------------------------------------------------------------
def _profile(e):
    return Profile(plan=e["plan"], age=e["age"], service=e["service"], salary=e["salary"])


def member_price(e, rule, s8_kw=None):
    p = _profile(e)
    y = e["years"]
    if rule == "anc":
        return PR.anc_price(p, y)
    if rule == "aec":
        return PR.aec_full(p, y)
    if rule == "sliding":
        anc, aec = PR.anc_price(p, y), PR.aec_full(p, y)
        share = (IN.S3_GAP_SHARE["value"]["30plus_yrs_state_service"] if e["service"] >= 30
                 else IN.S3_GAP_SHARE["value"]["25-29_yrs_state_service"])
        return anc + share * max(0.0, aec - anc)
    if rule == "employer_funded":
        return PR.aec_full(p, y)                 # member ANC + agency gap = plan made whole
    if rule == "s8":
        return s8.s8_price(p, y, **(s8_kw or {}))["price"]
    if rule == "s9_actuarial":
        return S9M.waiver_value(p, p.age)["waiver_value"]
    if rule == "s9_anc_parity":
        return PR.anc_price(p, y)
    raise ValueError(rule)


def ledger(e, rule, s8_kw=None, completion_months=None, deadline_months=None,
           retire_immediately=False, shift=0.0, annuity_load=1.0):
    pay = member_price(e, rule, s8_kw)
    # EVERY present value in v2_liability is strictly LINEAR in salary (benefit = multiplier x
    # service x AFC, and AFC is a weighted mean of salary).  So the ledger is computed once at a
    # unit salary and scaled.  That is exact, not an approximation, and it is what makes the
    # repaired monthly model rerunnable in seconds instead of hours.
    key = (e["plan"], e["sex"], L._m(e["age"]), L._m(e["service"]),
           L._m(e["years"]), completion_months, deadline_months, retire_immediately,
           round(shift, 8), round(annuity_load, 6), L._m(e["months_to_eligibility"] / 12.0))
    d = _LEDGER_CACHE.get(key)
    if d is None:
        d = L.participant_ledger(e["plan"], e["sex"], e["age"], e["service"], 1.0,
                                 e["years"], 0.0, completion_months, deadline_months, shift,
                                 retire_immediately, e["months_to_eligibility"])
        if annuity_load != 1.0:
            for k in ("pv_with_design", "pv_counterfactual", "gross_liability_increase",
                      "service_credit_component", "early_retirement_component"):
                d[k] = d[k] * annuity_load
        _LEDGER_CACHE[key] = d
    sal = e["salary"]
    out = dict(d)
    for k in ("pv_with_design", "pv_counterfactual", "gross_liability_increase",
              "service_credit_component", "early_retirement_component"):
        out[k] = d[k] * sal
    out["member_payment"] = pay
    out["trust_cost"] = out["gross_liability_increase"] - pay
    return out


# ---------------------------------------------------------------------------
# aggregation, with discounting to the valuation date and FY layers
# ---------------------------------------------------------------------------
def aggregate(elections, rule, s8_kw=None, cap=None, per_member_cap=None,
              queue_order="chronological", **lkw):
    """Aggregate one scenario.  `cap` turns the aggregate dollar limit into an admission rule."""
    rows = []
    for e in elections:
        d = ledger(e, rule, s8_kw, **lkw)
        rows.append((e, d))

    if queue_order == "cheapest_first":
        rows.sort(key=lambda r: (r[0]["month"], max(0.0, r[1]["trust_cost"])))
    elif queue_order == "dearest_first":
        rows.sort(key=lambda r: (r[0]["month"], -max(0.0, r[1]["trust_cost"])))
    else:
        rows.sort(key=lambda r: r[0]["month"])

    agg = dict(n=0.0, denied=0.0, gross=0.0, paid=0.0, trust=0.0, svc=0.0, accel=0.0,
               anc_ref=0.0, aec_ref=0.0, payroll=0.0, years=0.0, pv_design=0.0,
               accel_months_w=0.0, cf_age_w=0.0, ret_age_w=0.0, by_fy={},
               plans={}, pathways={}, per_member_capped=0.0)
    remaining = float("inf") if cap is None else float(cap)
    for e, d in rows:
        w = e["weight"]
        disc = (1.0 + I_NOM) ** (-(e["month"] / 12.0))
        subsidy = max(0.0, d["trust_cost"])
        pay = d["member_payment"]
        if per_member_cap is not None and subsidy > per_member_cap:
            # per-member subsidy ceiling (red team F7): the member funds the excess
            pay += subsidy - per_member_cap
            subsidy = per_member_cap
            agg["per_member_capped"] += w
        if cap is not None:
            if subsidy * w * disc > remaining:
                admitted = max(0.0, remaining / (subsidy * disc)) if subsidy > 0 else w
                admitted = min(w, admitted)
                agg["denied"] += (w - admitted)
                w = admitted
                if w <= 1e-12:
                    continue
            remaining -= subsidy * w * disc
        agg["n"] += w
        agg["gross"] += w * d["gross_liability_increase"] * disc
        agg["pv_design"] += w * d["pv_with_design"] * disc
        agg["paid"] += w * pay * disc
        agg["trust"] += w * (d["gross_liability_increase"] - pay) * disc
        agg["svc"] += w * d["service_credit_component"] * disc
        agg["accel"] += w * d["early_retirement_component"] * disc
        agg["anc_ref"] += w * PR.anc_price(_profile(e), e["years"]) * disc
        agg["aec_ref"] += w * PR.aec_full(_profile(e), e["years"]) * disc
        agg["payroll"] += w * e["salary"]
        agg["years"] += w * e["years"]
        agg["accel_months_w"] += w * d["acceleration_months"]
        agg["cf_age_w"] += w * d["expected_counterfactual_retire_age"]
        agg["ret_age_w"] += w * d["retire_age_with_design"]
        fy = e["fy"]
        f = agg["by_fy"].setdefault(fy, dict(n=0.0, gross=0.0, paid=0.0, trust=0.0))
        f["n"] += w
        f["gross"] += w * d["gross_liability_increase"] * disc
        f["paid"] += w * pay * disc
        f["trust"] += w * (d["gross_liability_increase"] - pay) * disc
        agg["plans"][e["plan"]] = agg["plans"].get(e["plan"], 0.0) + w
        agg["pathways"][e["pathway"]] = agg["pathways"].get(e["pathway"], 0.0) + w
    if agg["n"]:
        agg["avg_acceleration_months"] = agg["accel_months_w"] / agg["n"]
        agg["avg_counterfactual_retire_age"] = agg["cf_age_w"] / agg["n"]
        agg["avg_design_retire_age"] = agg["ret_age_w"] / agg["n"]
        agg["avg_salary"] = agg["payroll"] / agg["n"]
        agg["trust_per_participant"] = agg["trust"] / agg["n"]
    agg["multiple_of_anc"] = agg["paid"] / agg["anc_ref"] if agg["anc_ref"] else 0.0
    agg["share_of_aec"] = agg["paid"] / agg["aec_ref"] if agg["aec_ref"] else 0.0
    return agg


# ---------------------------------------------------------------------------
# the scenarios
# ---------------------------------------------------------------------------
SCEN = {
    "S0": "Status quo - actuarial-equivalent price after the 24-month window",
    "S1": "As drafted - Pathway A + Pathway B at approximate normal cost",
    "S2": "Pathway A only",
    "S3": "Sliding scale (member pays ANC + 25/50% of the gap)",
    "S4": "Employer-funded differential (member ANC, agency pays the gap); agency opt-in",
    "S5": "Reopened 60-month window, all tiers, no retirement condition",
    "S6": "S1 plus Hybrid members",
    "S7": "S1 with a binding aggregate dollar cap, enforced as an admission rule",
    "S8": "Earned-service repricing on 71 Pa.C.S. 5505(b)",
    "S9": "Waiver of the early-retirement reduction; no service credit added",
}


def run(code, level="central", overrides=None, s8_kw=None, cap=None, per_member_cap=None,
        queue_order="chronological", apply_elasticity=True, **lkw):
    o = dict(overrides or {})
    tA = o.get("takeup_A", IN.TAKEUP_PATHWAY_A["value"][level])
    tB = o.get("takeup_B", IN.TAKEUP_PATHWAY_B["value"][level])
    t5 = o.get("takeup_5", IN.TAKEUP_S5_OPEN_WINDOW["value"][level])
    bkw = dict(months_available=o.get("months_available"), vet_qual=o.get("vet_qual"),
               age_skew=o.get("age_skew"), vet_share=o.get("vet_share"),
               salary_factor=o.get("salary_factor", 1.0), scope=o.get("scope"))

    if code == "S0":
        t0 = IN.S0_TAKEUP["value"]
        el = build_elections_cached(t0, t0, plans=("plan1", "plan2"), **bkw)
        a = aggregate(el, "aec", **lkw)
        return a
    if code == "S1":
        el = build_elections_cached(tA, tB, plans=("plan1", "plan2"), **bkw)
        return aggregate(el, "anc", **lkw)
    if code == "S2":
        el = build_elections_cached(tA, tB, plans=("plan1", "plan2"), pathways=("A",), **bkw)
        return aggregate(el, "anc", **lkw)
    if code == "S3":
        el0 = build_elections_cached(tA, tB, plans=("plan1", "plan2"), **bkw)
        base = aggregate(el0, "anc", **lkw)
        ref = aggregate(el0, "sliding", **lkw)
        adj = ((ref["paid"] / base["paid"]) ** EL) if (base["paid"] and apply_elasticity) else 1.0
        el = build_elections_cached(tA * adj, tB * adj, plans=("plan1", "plan2"), **bkw)
        a = aggregate(el, "sliding", **lkw)
        a["takeup_adjustment"] = adj
        return a
    if code == "S4":
        opt = o.get("agency_optin", IN.S4_AGENCY_OPTIN["value"])
        el = build_elections_cached(tA * opt, tB * opt, plans=("plan1", "plan2"), **bkw)
        a = aggregate(el, "employer_funded", **lkw)
        a["member_paid_anc"] = a["anc_ref"]
        a["agency_appropriation"] = a["paid"] - a["anc_ref"]
        return a
    if code == "S5":
        el = build_elections_cached(t5, t5, plans=("plan1", "plan2", "hybrid"),
                                    months_available=o.get("months_available"),
                                    vet_qual=o.get("vet_qual"), age_skew=o.get("age_skew", 1.0),
                                    vet_share=o.get("vet_share"),
                                    salary_factor=o.get("salary_factor", 1.0),
                                    scope=o.get("scope"))
        return aggregate(el, "anc", **lkw)
    if code == "S6":
        el = build_elections_cached(tA, tB, plans=("plan1", "plan2", "hybrid"), **bkw)
        return aggregate(el, "anc", **lkw)
    if code == "S7":
        el = build_elections_cached(tA, tB, plans=("plan1", "plan2"), **bkw)
        return aggregate(el, "anc", cap=cap, per_member_cap=per_member_cap,
                         queue_order=queue_order, **lkw)
    if code == "S8":
        el0 = build_elections_cached(tA, tB, plans=("plan1", "plan2"), **bkw)
        adj = 1.0
        if apply_elasticity:
            base = aggregate(el0, "anc", **lkw)
            ref = aggregate(el0, "s8", s8_kw=s8_kw, **lkw)
            adj = (ref["paid"] / base["paid"]) ** EL if base["paid"] else 1.0
        el = build_elections_cached(tA * adj, tB * adj, plans=("plan1", "plan2"), **bkw)
        a = aggregate(el, "s8", s8_kw=s8_kw, cap=cap, per_member_cap=per_member_cap,
                      queue_order=queue_order, **lkw)
        a["takeup_adjustment"] = adj
        return a
    if code in ("S9", "S9-actuarial", "S9-anc_parity"):
        rule = "s9_actuarial" if code != "S9-anc_parity" else "s9_anc_parity"
        kw = dict(lkw)
        kw["retire_immediately"] = True
        el0 = build_elections_cached(tA, tB, plans=("plan1", "plan2"), pathways=("A",), **bkw)
        adj = 1.0
        if apply_elasticity:
            s2 = aggregate(el0, "anc", **kw)
            ref = aggregate(el0, rule, **kw)
            # the member responds to price PER UNIT OF VALUE: S9 adds no service credit, so the
            # same price buys less than S2's.  value proxy = PV of the benefit under the design.
            pr_ratio = (ref["paid"] / s2["paid"]) if s2["paid"] else 1.0
            val_ratio = (ref["pv_design"] / s2["pv_design"]) if s2["pv_design"] else 1.0
            adj = ((pr_ratio / val_ratio) ** EL) if val_ratio else pr_ratio ** EL
        el = build_elections_cached(tA * adj, tB * adj, plans=("plan1", "plan2"), pathways=("A",), **bkw)
        a = aggregate(el, rule, **kw)
        a["takeup_adjustment"] = adj
        return a
    raise ValueError(code)
