"""
v2 - the cohort, rebuilt to answer red team F2.

What was wrong in MOO-7, and what each fix is:

  (a) `build_participants` defaulted to Plan 1, so Plan 2 members who can qualify were absent.
      FIX: every pathway test is plan-specific and all three tiers are carried.

  (b) Pathway A applied a universal `30 - service` rule.  Plan 2 and Hybrid have no 30-year gate;
      they use the Rule of 90.  A Plan 2 member aged 65 with 21 years reaches an unreduced benefit
      by buying 4 years.
      FIX: years-needed is computed from each plan's own unreduced-eligibility rule.

  (c) Tier was inferred from TOTAL service, which includes purchased and ported service and
      therefore does not establish a first membership date.
      FIX: tier is assigned on membership TENURE = total service - purchased service, integrated
      over a stated distribution of purchased service, producing tier SHARES per cell.  The
      boundaries are also corrected: Plan 1 needs tenure >= 17.5 years (the 1/1/2013 vesting test
      binds, not the 7/1/2010 membership date), not the 15.0 MOO-7 used.

  (d) Pathways A and B overlapped: 7.711 expected A participants were already unreduced-eligible.
      FIX: the two pathways are mutually exclusive by construction - already eligible => B,
      made eligible by the purchase => A, otherwise not in the pilot.  One election per member.

  (e) "No aging/inflow simulation advances the stock of active members through the pilot. A small
      current stock is not a binding four-year enrollment limit."
      FIX: the 6/30/2025 stock is advanced MONTHLY, with VRS's own retirement and termination
      decrements and fitted mortality, from the valuation date through the end of the pilot.
      Members roll into eligibility as they age and accrue service, which is the whole point.

Everything here is expected weights on a cell grid, not simulated people.  No individual-level data
is used anywhere in this model.
"""
import inputs as IN
import population as POP
import v2_decrements as D
from mortality import Mortality

MORT = Mortality()
BOUNDS = IN.TIER_TENURE_BOUNDS["value"]
PSD = IN.PURCHASED_SERVICE_DIST["value"]
MIX = IN.PARTICIPANT_GENDER_MIX["value"]
SSRA = 67.0           # Plan 2 / Hybrid normal retirement age, as in pricing.Profile
MAXY = IN.MAX_MILITARY_YEARS["value"]


# ---------------------------------------------------------------------------
# (c) tier shares from membership tenure
# ---------------------------------------------------------------------------
def tier_shares(total_service, n_steps=40):
    """Split one cell's headcount across Plan 1 / Plan 2 / Hybrid on membership TENURE.

    tenure = total_service - X, where X is purchased/ported/granted service.
    X = 0 with probability `share_with_none`; otherwise uniform on (0, max_years_if_any].
    """
    out = {"plan1": 0.0, "plan2": 0.0, "hybrid": 0.0}

    def assign(tenure, w):
        if tenure >= BOUNDS["plan1_min_tenure"]:
            out["plan1"] += w
        elif tenure >= BOUNDS["plan2_min_tenure"]:
            out["plan2"] += w
        else:
            out["hybrid"] += w

    assign(total_service, PSD["share_with_none"])
    rest = 1.0 - PSD["share_with_none"]
    if rest > 0:
        hi = PSD["max_years_if_any"]
        for j in range(n_steps):
            x = hi * (j + 0.5) / n_steps
            assign(max(0.0, total_service - x), rest / n_steps)
    return out


# ---------------------------------------------------------------------------
# (b) plan-specific eligibility
# ---------------------------------------------------------------------------
AGE_BAND_AGES = {"Under 20": [19], "20-24": [20, 21, 22, 23, 24], "25-29": [25, 26, 27, 28, 29],
                 "30-34": [30, 31, 32, 33, 34], "35-39": [35, 36, 37, 38, 39],
                 "40-44": [40, 41, 42, 43, 44], "45-49": [45, 46, 47, 48, 49],
                 "50-54": [50, 51, 52, 53, 54], "55-59": [55, 56, 57, 58, 59],
                 "60": [60], "61": [61], "62": [62], "63": [63], "64": [64], "65": [65],
                 "66": [66], "67": [67], "68": [68], "69": [69],
                 "70+": [70, 71, 72, 73, 74, 75]}
SVC_POINTS = IN.SUBCELL_SERVICE_POINTS["value"]
MIN_ENTRY = IN.SUBCELL_MIN_ENTRY_AGE["value"]


def subcells(age_label, svc_label, count):
    """Spread one published cell over integer ages and within-band service points.

    The cell total is preserved exactly: sub-cells that would imply entry before age
    SUBCELL_MIN_ENTRY_AGE are dropped and the remaining weights are renormalised.
    """
    ages = AGE_BAND_AGES[age_label]
    pts = SVC_POINTS[svc_label]
    raw = []
    for a in ages:
        for sv, sw in pts:
            if sv <= (a - MIN_ENTRY):
                raw.append((float(a), float(sv), sw / len(ages)))
    tot = sum(r[2] for r in raw)
    if tot <= 0:
        return []
    return [(a, sv, count * w / tot) for a, sv, w in raw]


def is_unreduced_eligible(plan, age, service):
    if plan == "plan1":
        return (age >= 65.0 and service >= 5.0) or (age >= 50.0 and service >= 30.0)
    return (age >= SSRA and service >= 5.0) or (age + service >= 90.0 and service >= 5.0)


def years_needed_for_eligibility(plan, age, service):
    """Years of purchased credit that make the member unreduced-eligible IMMEDIATELY.

    Returns None if no purchase up to the 4-year statutory maximum can do it.
    Purchased credit adds to SERVICE only; it does not add to age.  That is why the Rule of 90
    requirement here is (90 - age - service) and not the halved form used when both age and
    service grow with calendar time.
    """
    if plan == "plan1":
        if age >= 65.0:
            need = max(0.0, 5.0 - service)
        elif age >= 50.0:
            need = max(0.0, 30.0 - service)
        else:
            return None                      # under 50 and under 30 yrs: no purchase helps now
    else:
        if age >= SSRA:
            need = max(0.0, 5.0 - service)
        else:
            need = max(0.0, 90.0 - age - service)
            if service + need < 5.0:
                need = 5.0 - service
    return need if 0.0 < need <= MAXY else None


def years_to_eligibility(plan, age, service, purchased=0.0):
    """Years from now until the member is unreduced-eligible, counting `purchased` credit.

    Both age and service advance with calendar time; purchased credit advances SERVICE only.
    Returns the earliest of the plan's alternative routes.  0.0 if already eligible.
    """
    s = service + purchased
    if is_unreduced_eligible(plan, age, s):
        return 0.0
    if plan == "plan1":
        by_service = max(max(0.0, 50.0 - age), max(0.0, 30.0 - s))   # age 50 AND 30 years
        by_age = max(0.0, 65.0 - age) if s + max(0.0, 65.0 - age) >= 5.0 else float("inf")
        return min(by_service, by_age)
    by_r90 = max(0.0, (90.0 - age - s) / 2.0)                        # age + service = 90
    if s + by_r90 < 5.0:
        by_r90 = float("inf")
    by_age = max(0.0, SSRA - age) if s + max(0.0, SSRA - age) >= 5.0 else float("inf")
    return min(by_r90, by_age)


# ---------------------------------------------------------------------------
# (e) monthly stock projection
# ---------------------------------------------------------------------------
def project_stock(months, start_cells=None):
    """Advance the 6/30/2025 census forward `months` months, cell by cell, sex by sex.

    Yields the surviving-active stock at each month end as a dict
        (plan, sex) -> list of {age, service, weight, cell_salary}
    Decrements applied monthly: VRS retirement, VRS termination, fitted mortality.
    No new entrants are added - a new hire cannot have 25 years of service inside a four-year
    pilot, so inflow is irrelevant to this population and omitting it is exact, not an
    approximation.
    """
    if start_cells is None:
        start_cells = []
        for a, b, am, sm, c, sal in POP.cells():
            if c == 0:
                continue
            for age, svc, w0 in subcells(a, b, c):
                shares = tier_shares(svc)
                for plan, sh in shares.items():
                    if sh <= 0:
                        continue
                    for sex, sw in MIX.items():
                        start_cells.append({"plan": plan, "sex": sex, "age": age,
                                            "service": svc, "weight": w0 * sh * sw,
                                            "cell_salary": sal, "service_at_valuation": svc})
    stock = [dict(c) for c in start_cells]
    snapshots = [[dict(c) for c in stock]]
    for m in range(months):
        nxt = []
        for c in stock:
            qr = D.monthly(D.retire_rate(c["plan"], c["age"], c["service"], c["sex"]))
            qt = D.monthly(D.term_rate(c["service"], c["sex"]))
            qd = 1.0 - MORT.survive(c["age"], c["age"] + 1.0 / 12.0, sex=c["sex"])
            stay = max(0.0, (1.0 - qr) * (1.0 - qt) * (1.0 - qd))
            w = c["weight"] * stay
            if w <= 1e-9:
                continue
            d = dict(c)
            d["age"] = c["age"] + 1.0 / 12.0
            d["service"] = c["service"] + 1.0 / 12.0
            d["weight"] = w
            nxt.append(d)
        stock = nxt
        snapshots.append([dict(c) for c in stock])
    return snapshots


# ---------------------------------------------------------------------------
# (a)(b)(d) pathway assignment, mutually exclusive
# ---------------------------------------------------------------------------
ELIGIBILITY_HORIZON_YEARS = 10.0


def classify(plan, age, service, months_available=None, scope=None):
    """Return (pathway, years, years_to_eligibility_with_purchase).

    Mutually exclusive by construction (red team F2(d)): already unreduced-eligible => Pathway B,
    otherwise Pathway A if a purchase brings eligibility forward at all.  One election per member.

    Pathway A does NOT require the purchase to produce eligibility immediately.  A member whose
    gap is larger than the service they hold still buys what they have and reaches eligibility
    sooner than they otherwise would; the repaired liability engine then runs the retirement
    deadline from that later eligibility date rather than from today.  MOO-7 collapsed this to
    "eligible now", which is what made its retirement dates wrong in both directions.
    """
    avail = (IN.AVG_MONTHS_AVAILABLE["value"] if months_available is None
             else months_available) / 12.0
    sc = IN.PATHWAY_A_SCOPE["value"] if scope is None else scope
    if avail <= 0:
        return (None, 0.0, 0.0)
    if is_unreduced_eligible(plan, age, service):
        y = min(1.0, avail)                      # Pathway B as drafted: up to 1 year
        return ("B", y, 0.0) if y > 0 else (None, 0.0, 0.0)
    y = min(MAXY, avail)
    t_with = years_to_eligibility(plan, age, service, y)
    t_without = years_to_eligibility(plan, age, service, 0.0)
    if not (t_with < t_without - 1e-9):
        return (None, 0.0, 0.0)                  # the purchase buys no eligibility advance
    if sc == "immediate" and t_with > 1e-9:
        return (None, 0.0, 0.0)                  # narrow reading: must be eligible at once
    if t_with > ELIGIBILITY_HORIZON_YEARS:
        return (None, 0.0, 0.0)                  # too far out to be a pilot participant
    # buy only as much as is useful: the smallest purchase achieving the same eligibility date
    lo, hi = 0.0, y
    for _ in range(24):
        mid = (lo + hi) / 2.0
        if years_to_eligibility(plan, age, service, mid) <= t_with + 1e-9:
            hi = mid
        else:
            lo = mid
    return ("A", max(hi, 1.0 / 12.0), t_with)
