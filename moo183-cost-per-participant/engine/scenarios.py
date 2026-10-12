"""
Part 3 - price S0 through S7.

Participants are built CELL BY CELL from the VRS age x service table so the aggregate carries the
real age distribution, not a single average member.  For each cell:
    weight = cell count x veteran funnel x take-up
    years purchased = Pathway A: min(30 - service, 4, months_available/12)
                      Pathway B: min(1, months_available/12)
                      S5/S6:     min(4, months_available/12)
    member payment  = per scenario
    plan cost       = Pricer.design_cost(...)["net_plan_cost"]
"""
from dataclasses import dataclass

import inputs as IN
import population as POP
from pricing import Pricer, Profile

PR = Pricer()
MAXY = IN.MAX_MILITARY_YEARS["value"]


def salary_for_cell(age_band_avg):
    return age_band_avg * (1.0 + IN.LONG_SERVICE_PREMIUM["value"])


@dataclass
class Participant:
    profile: Profile
    years: float
    weight: float
    pathway: str


def _cells(min_age=None, max_age=None, svc_bands=None, tiers=None):
    for a, b, am, sm, c, sal in POP.cells():
        if c == 0:
            continue
        if min_age is not None and am < min_age:
            continue
        if max_age is not None and am > max_age:
            continue
        if svc_bands is not None and b not in svc_bands:
            continue
        if tiers is not None and POP.tier(sm) not in tiers:
            continue
        yield am, sm, c, sal


def build_participants(pathway, takeup, months_available=None, age_skew=None,
                       vet_qual=None, vet_share=None, tiers=("plan1",)):
    mav = IN.AVG_MONTHS_AVAILABLE["value"] if months_available is None else months_available
    avail_y = mav / 12.0
    out = []
    if pathway == "A":
        sel = _cells(min_age=50, svc_bands=["25-29"], tiers=tiers)
    elif pathway == "B":
        sel = list(_cells(min_age=50, svc_bands=["30+"], tiers=tiers)) + \
              list(_cells(min_age=65, svc_bands=["15-19", "20-24", "25-29"], tiers=tiers))
    elif pathway == "OPEN":          # S5 / S6: whole active population of the given tiers
        sel = _cells(tiers=tiers)
    else:
        raise ValueError(pathway)

    for am, sm, c, sal in sel:
        plan = POP.tier(sm)
        p = Profile(plan=plan, age=float(am), service=float(sm),
                    salary=salary_for_cell(sal), label=f"{plan}/a{am}/s{sm}")
        if pathway == "A":
            yrs = min(max(0.0, 30.0 - sm), MAXY, avail_y)
        elif pathway == "B":
            yrs = min(1.0, avail_y)
        else:
            yrs = min(MAXY, avail_y)
        if yrs <= 0:
            continue
        w = POP.veteran_filter(c, age_skew=age_skew, qual=vet_qual, vet_share=vet_share) * takeup
        out.append(Participant(p, yrs, w, pathway))
    return out


def price_cohort(parts, payment_rule="anc", months_accel=None, baseline_extra=None):
    """Aggregate gross liability, member payments and net plan cost for a participant list."""
    ma = IN.MONTHS_ACCELERATION["value"]["central"] if months_accel is None else months_accel
    agg = dict(n=0.0, gross=0.0, paid=0.0, net=0.0, svc=0.0, accel=0.0,
               anc_ref=0.0, aec_ref=0.0, payroll=0.0)
    for pt in parts:
        p, y, w = pt.profile, pt.years, pt.weight
        anc = PR.anc_price(p, y)
        aec = PR.aec_full(p, y)
        if payment_rule == "anc":
            pay = anc
        elif payment_rule == "aec":
            pay = aec
        elif payment_rule == "sliding":
            share = IN.S3_GAP_SHARE["value"]["30plus_yrs_state_service"] if p.service >= 30 \
                else IN.S3_GAP_SHARE["value"]["25-29_yrs_state_service"]
            pay = anc + share * max(0.0, aec - anc)
        elif payment_rule == "employer_funded":
            pay = aec                      # member pays ANC, agency pays the gap -> plan made whole
        else:
            raise ValueError(payment_rule)
        d = PR.design_cost(p, y, ma, member_payment=pay, baseline_extra=baseline_extra)
        agg["n"] += w
        agg["gross"] += w * d["gross_liability_increase"]
        agg["paid"] += w * pay
        agg["net"] += w * d["net_plan_cost"]
        agg["svc"] += w * d["service_credit_component"]
        agg["accel"] += w * d["early_retirement_subsidy_component"]
        agg["anc_ref"] += w * anc
        agg["aec_ref"] += w * aec
        agg["payroll"] += w * p.salary
    return agg


# ---------------------------------------------------------------------------------
# amortisation and fiscal-year layout
# ---------------------------------------------------------------------------------
def amort_schedule(uaal, years=None, i=None, g=None, timing=None):
    """Level-percent-of-pay amortisation payments, VRS State Employee convention."""
    years = IN.AMORT_PERIOD["value"] if years is None else years
    i = IN.DISCOUNT_RATE["value"] if i is None else i
    g = IN.PAYROLL_GROWTH["value"] if g is None else g
    timing = IN.AMORT_TIMING_ADJ["value"] if timing is None else timing
    r = (1.0 + g) / (1.0 + i)
    factor = (1.0 - r ** years) / (1.0 - r)
    first = uaal * timing / factor
    return [first * (1.0 + g) ** t for t in range(years)]


def pilot_layout(total_liability, total_member_paid, phasing=None, fys=None):
    """Spread the pilot's liability over the pilot fiscal years and amortise each year's layer."""
    phasing = IN.PILOT_PHASING["value"] if phasing is None else phasing
    fys = IN.PILOT_FY["value"] if fys is None else fys
    layers = []
    for k, (fy, share) in enumerate(zip(fys, phasing)):
        layers.append({"fy_created": fy, "liability": total_liability * share,
                       "member_paid": total_member_paid * share,
                       "schedule": amort_schedule(total_liability * share)})
    # annual employer contribution by fiscal year (amortisation starts the FY after creation)
    annual = {}
    for L in layers:
        for t, pmt in enumerate(L["schedule"]):
            fy = L["fy_created"] + 1 + t
            annual[fy] = annual.get(fy, 0.0) + pmt
    return layers, annual


SCENARIOS = {
    "S0": "Status quo - actuarial-equivalent price after the 24-month window",
    "S1": "Proposal as drafted - Pathway A + Pathway B at approximate normal cost",
    "S2": "Pathway A only",
    "S3": "Blended / sliding-scale price (member pays ANC + 25/50% of the gap)",
    "S4": "Employer-funded differential (member pays ANC, agency pays the gap); agency opt-in",
    "S5": "Reopened election window for all Plan 1 / Plan 2 actives, no retirement condition",
    "S6": "S1 plus Hybrid Retirement Plan members",
    "S7": "S1 with a binding aggregate dollar cap",
}


def run_scenario(code, level="central", months_accel=None, overrides=None):
    o = overrides or {}
    tA = o.get("takeup_A", IN.TAKEUP_PATHWAY_A["value"][level])
    tB = o.get("takeup_B", IN.TAKEUP_PATHWAY_B["value"][level])
    t5 = o.get("takeup_5", IN.TAKEUP_S5_OPEN_WINDOW["value"][level])
    mav = o.get("months_available")
    skew = o.get("age_skew")
    qual = o.get("vet_qual")
    ma = months_accel
    kw = dict(months_available=mav, age_skew=skew, vet_qual=qual)

    el = IN.TAKEUP_PRICE_ELASTICITY["value"]

    if code == "S0":
        # Status quo. Member pays full AEC, so the plan is made whole: no incremental liability.
        t0 = IN.S0_TAKEUP["value"]
        parts = build_participants("A", t0, **kw) + build_participants("B", t0, **kw)
        a = price_cohort(parts, "aec", months_accel=0.0)   # no design, no acceleration
        a["net"] = 0.0
        return a, parts

    if code == "S1":
        parts = build_participants("A", tA, **kw) + build_participants("B", tB, **kw)
        return price_cohort(parts, "anc", months_accel=ma), parts

    if code == "S2":
        parts = build_participants("A", tA, **kw)
        return price_cohort(parts, "anc", months_accel=ma), parts

    if code == "S3":
        # member price rises -> take-up falls, via the stated elasticity
        base, bparts = price_cohort(build_participants("A", tA, **kw) +
                                    build_participants("B", tB, **kw), "anc", months_accel=ma), None
        ref = price_cohort(build_participants("A", tA, **kw) + build_participants("B", tB, **kw),
                           "sliding", months_accel=ma)
        price_ratio = ref["paid"] / base["paid"] if base["paid"] else 1.0
        adj = price_ratio ** el
        parts = build_participants("A", tA * adj, **kw) + build_participants("B", tB * adj, **kw)
        a = price_cohort(parts, "sliding", months_accel=ma)
        a["takeup_adjustment"] = adj
        return a, parts

    if code == "S4":
        opt = o.get("agency_optin", IN.S4_AGENCY_OPTIN["value"])
        parts = build_participants("A", tA * opt, **kw) + build_participants("B", tB * opt, **kw)
        a = price_cohort(parts, "employer_funded", months_accel=ma)
        # plan made whole; cost lands on agency operating budgets instead
        a["agency_appropriation"] = a["paid"] - a["anc_ref"]
        a["net"] = 0.0
        return a, parts

    if code == "S5":
        parts = build_participants("OPEN", t5, tiers=("plan1", "plan2"),
                                   months_available=mav, age_skew=o.get("age_skew", 1.0),
                                   vet_qual=qual)
        return price_cohort(parts, "anc", months_accel=ma), parts

    if code == "S6":
        parts = build_participants("A", tA, **kw) + build_participants("B", tB, **kw) + \
                build_participants("OPEN", t5, tiers=("hybrid",), months_available=mav,
                                   age_skew=o.get("age_skew", 1.0), vet_qual=qual)
        return price_cohort(parts, "anc", months_accel=ma), parts

    if code == "S7":
        a, parts = run_scenario("S1", level, months_accel, overrides)
        a = dict(a)
        a["uncapped_net"] = a["net"]
        a["caps"] = {c: min(c, a["net"]) for c in IN.S7_CAPS["value"]}
        return a, parts

    raise ValueError(code)
