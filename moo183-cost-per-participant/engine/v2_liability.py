"""
v2 - liability with explicit monthly dates, answering red team F1.

MOO-7 computed the design's retirement date as

    r1 = max( unreduced_age(purchased),  unreduced_age(0) + 2.0 - 0.5,  current_age )

which is not the proposal.  The brief requires retirement within six months of COMPLETING the
purchase, once eligibility is met.  For a Plan 1 member aged 57 with 27 years buying 3 years, the
brief's date is about 57.5 and MOO-7's was 61.5.  Those are different benefits.

What this file does instead:

  WITH the design, four explicit monthly dates:
      t_elect      the month the member elects, drawn from the pilot election schedule
      t_complete   t_elect + PURCHASE_COMPLETION_MONTHS
      t_eligible   the month the member is unreduced-eligible counting the purchased credit
      t_retire     max(t_complete, t_eligible) + RETIREMENT_DEADLINE_MONTHS
  The member's service at t_retire is actual service accrued to t_retire plus the purchase, and
  their AFC is computed on the salary path to t_retire.  This is a date, not a lag.

  WITHOUT the design, the counterfactual is NOT a lag at all.  It is the expectation over VRS's own
  published decrements: each future month the member either retires (VRS retirement rate),
  terminates (VRS termination rate, taking a deferred vested benefit commencing at their unreduced
  age on service accrued to termination), dies (fitted mortality, no retirement benefit modelled),
  or continues.  The counterfactual PV is the probability-weighted present value over that
  distribution, and the expected counterfactual retirement date is reported alongside it so the
  reader can see it rather than infer it.

Everything is discounted to the election month and then to the valuation date, so liabilities
created in different pilot years are not silently added at face value.

CAVEATS, unchanged and restated: this values the basic single-life pension benefit only. It
excludes the retiree Health Insurance Credit, Group Life, survivor-option loading, disability and
death-in-service. Direction of error: UNDERSTATES cost. No figure is a VRS actuarial result.
"""
import inputs as IN
import s8
import v2_decrements as D
from mortality import Mortality

MORT = Mortality()
I_NOM = IN.DISCOUNT_RATE["value"]
MIX = IN.PARTICIPANT_GENDER_MIX["value"]
DEADLINE = IN.RETIREMENT_DEADLINE_MONTHS["value"]
HORIZON_MONTHS = 12 * 35          # project the counterfactual to age ~100 at most
MULT = {"plan1": IN.MULT_PLAN1["value"], "plan2": IN.MULT_PLAN2["value"],
        "hybrid": IN.MULT_HYBRID["value"]}
AFC_M = {"plan1": int(IN.AFC_MONTHS_PLAN1["value"]),
         "plan2": int(IN.AFC_MONTHS_PLAN2["value"]),
         "hybrid": int(IN.AFC_MONTHS_PLAN2["value"])}


def v(n):
    return (1.0 + I_NOM) ** (-n)


# ---------------------------------------------------------------------------
# caches.  The monthly engine evaluates these millions of times; without the caches the repaired
# model is too slow to rerun, and a model nobody can rerun is not an estimate.
# ---------------------------------------------------------------------------
_PATH = {}          # (shift,) -> salary index relative to service 0, by service month
_ANN = {}           # (plan, sex, age_month) -> annuity-due factor
_SURV = {}          # (sex, a_month, b_month) -> survival probability
_MAX_SVC_M = 12 * 60


def _salary_index(shift=0.0):
    """Cumulative salary index by service month, normalised to 1.0 at service 0.

    index[k] = salary at service month k / salary at service 0, on the VRS service-based scale.
    Also returns the prefix sums of the index so an AFC over any window is O(1).
    """
    key = round(shift, 8)
    if key in _PATH:
        return _PATH[key]
    idx = [1.0]
    for k in range(_MAX_SVC_M):
        g = s8.salary_increase_rate(k // 12, shift)
        idx.append(idx[-1] * (1.0 + g) ** (1.0 / 12.0))
    pre = [0.0]
    for x in idx:
        pre.append(pre[-1] + x)
    _PATH[key] = (idx, pre)
    return _PATH[key]


def _m(x):
    return int(round(x * 12.0))


def salary_at(salary_now, service_now, service_then, shift=0.0):
    """Project (or back-cast) an individual's salary on the VRS service-based scale."""
    idx, _ = _salary_index(shift)
    a = min(max(_m(service_now), 0), _MAX_SVC_M)
    b = min(max(_m(service_then), 0), _MAX_SVC_M)
    return salary_now * idx[b] / idx[a]


def afc_at(plan, salary_now, service_now, service_at_exit, shift=0.0):
    """AFC on the plan's own averaging period, measured on the salary path to exit.

    VRS defines AFC as the highest consecutive 36 (Plan 1) or 60 (Plan 2/Hybrid) months.  On a
    monotonically rising salary path the highest window is the last one, so this is the mean of the
    final AFC_M months before exit - computed from the prefix sums of the cached index.
    """
    idx, pre = _salary_index(shift)
    m = AFC_M[plan]
    a0 = min(max(_m(service_now), 0), _MAX_SVC_M)
    hi = min(max(_m(service_at_exit), 0), _MAX_SVC_M)
    lo = max(0, hi - m)
    n = hi - lo
    if n <= 0:
        return salary_now
    mean_idx = (pre[hi + 1] - pre[lo + 1]) / n
    return salary_now * mean_idx / idx[a0]


def annual_benefit(plan, salary_now, service_now, service_at_exit, purchased=0.0, shift=0.0):
    afc = afc_at(plan, salary_now, service_now, service_at_exit, shift)
    return MULT[plan] * (service_at_exit + purchased) * afc


def annuity(plan, sex, age):
    k = (plan, sex, _m(age))
    r = _ANN.get(k)
    if r is None:
        r = MORT.annuity(k[2] / 12.0, plan, sex=sex)
        _ANN[k] = r
    return r


def survive(sex, a, b):
    if b <= a:
        return 1.0
    k = (sex, _m(a), _m(b))
    r = _SURV.get(k)
    if r is None:
        r = MORT.survive(k[1] / 12.0, k[2] / 12.0, sex=sex)
        _SURV[k] = r
    return r


def pv_at_commencement(plan, sex, age_at_exit, age_at_commence, benefit, age_now):
    """PV at `age_now` of a benefit of `benefit`/yr commencing at `age_at_commence`.

    Survival to exit is NOT applied here: the caller supplies the probability of reaching the exit
    state.  Survival from exit to commencement IS applied, because a deferred vested member can
    die before commencing.
    """
    surv = survive(sex, age_at_exit, age_at_commence)
    a = annuity(plan, sex, age_at_commence)
    return benefit * a * surv * v(age_at_commence - age_now)


def unreduced_age_from(plan, age, service):
    """Age at which a member who STOPS accruing now first gets an unreduced benefit."""
    if plan == "plan1":
        if service >= 30.0:
            return max(age, 50.0)
        return max(age, 65.0) if service >= 5.0 else max(age, 65.0)
    if service < 5.0:
        return max(age, 67.0)
    return min(max(age, 67.0), max(age, 90.0 - service))


# ---------------------------------------------------------------------------
# WITH the design - explicit dates
# ---------------------------------------------------------------------------
def pv_with_design(plan, sex, age_elect, service_elect, salary_elect, purchased,
                   completion_months=None, deadline_months=None, shift=0.0,
                   retire_immediately=False, months_to_eligibility=0.0):
    """PV of the benefit under the design, on the brief's own four dates.

        t_elect     = 0 (this function values from the election month)
        t_complete  = PURCHASE_COMPLETION_MONTHS
        t_eligible  = months_to_eligibility, counting the purchased credit
        t_retire    = max(t_complete, t_eligible) + RETIREMENT_DEADLINE_MONTHS
    """
    cm = (IN.PURCHASE_COMPLETION_MONTHS["value"]["central"] if completion_months is None
          else completion_months)
    dl = DEADLINE if deadline_months is None else deadline_months
    if retire_immediately:
        t_ret_m = 0.0
    else:
        t_ret_m = max(float(cm), float(months_to_eligibility)) + float(dl)
    t = t_ret_m / 12.0
    age_exit = age_elect + t
    svc_exit = service_elect + t
    ben = annual_benefit(plan, salary_elect, service_elect, svc_exit, purchased, shift)
    surv = survive(sex, age_elect, age_exit)
    pv = surv * pv_at_commencement(plan, sex, age_exit, age_exit, ben, age_elect)
    return {"pv": pv, "retire_age": age_exit, "months_to_retirement": t_ret_m,
            "service_at_retirement": svc_exit + purchased, "annual_benefit": ben}


# ---------------------------------------------------------------------------
# WITHOUT the design - expectation over VRS's own decrements
# ---------------------------------------------------------------------------
_CF = {}


def pv_counterfactual(plan, sex, age_elect, service_elect, salary_elect, shift=0.0,
                      horizon_months=HORIZON_MONTHS):
    """Cached wrapper: the counterfactual depends on no design dial, so it is computed once per
    (plan, sex, age, service, salary, shift) and reused across every scenario and every dial."""
    k = (plan, sex, _m(age_elect), _m(service_elect), round(salary_elect, 2), round(shift, 8))
    r = _CF.get(k)
    if r is None:
        r = _pv_counterfactual(plan, sex, age_elect, service_elect, salary_elect, shift,
                               horizon_months)
        _CF[k] = r
    return r


def _pv_counterfactual(plan, sex, age_elect, service_elect, salary_elect, shift=0.0,
                       horizon_months=HORIZON_MONTHS):
    """Expected PV of the benefit absent the purchase, and the expected retirement date.

    Each month the active member faces VRS's retirement rate, VRS's termination rate and fitted
    mortality.  Retirement commences the benefit at that age.  Termination defers it to the
    member's unreduced age on service accrued to termination.
    """
    alive_active = 1.0
    pv = 0.0
    e_ret_age_num = 0.0
    e_ret_age_den = 0.0
    p_retire_total = 0.0
    p_terminate_total = 0.0
    for m in range(horizon_months):
        age = age_elect + m / 12.0
        svc = service_elect + m / 12.0
        qr = D.monthly(D.retire_rate(plan, age, svc, sex))
        qt = D.monthly(D.term_rate(svc, sex))
        qd = 1.0 - survive(sex, age, age + 1.0 / 12.0)
        # decrements in the month, applied to the start-of-month active population
        p_r = alive_active * qr
        p_t = alive_active * (1.0 - qr) * qt
        p_d = alive_active * (1.0 - qr) * (1.0 - qt) * qd
        if p_r > 0:
            ben = annual_benefit(plan, salary_elect, service_elect, svc, 0.0, shift)
            pv += p_r * pv_at_commencement(plan, sex, age, age, ben, age_elect)
            e_ret_age_num += p_r * age
            e_ret_age_den += p_r
            p_retire_total += p_r
        if p_t > 0:
            ben = annual_benefit(plan, salary_elect, service_elect, svc, 0.0, shift)
            u = unreduced_age_from(plan, age, svc)
            pv += p_t * pv_at_commencement(plan, sex, age, u, ben, age_elect)
            e_ret_age_num += p_t * u
            e_ret_age_den += p_t
            p_terminate_total += p_t
        alive_active -= (p_r + p_t + p_d)
        if alive_active <= 1e-9:
            break
    return {"pv": pv,
            "expected_retire_age": (e_ret_age_num / e_ret_age_den) if e_ret_age_den else age_elect,
            "p_retire": p_retire_total, "p_terminate": p_terminate_total,
            "p_die_active": max(0.0, 1.0 - p_retire_total - p_terminate_total)}


# ---------------------------------------------------------------------------
# one participant's ledger
# ---------------------------------------------------------------------------
def participant_ledger(plan, sex, age_elect, service_elect, salary_elect, purchased,
                       member_payment, completion_months=None, deadline_months=None,
                       shift=0.0, retire_immediately=False, months_to_eligibility=0.0):
    """Gross liability increase, member payment, trust cost - all at the election date."""
    w = pv_with_design(plan, sex, age_elect, service_elect, salary_elect, purchased,
                       completion_months, deadline_months, shift, retire_immediately,
                       months_to_eligibility)
    c = pv_counterfactual(plan, sex, age_elect, service_elect, salary_elect, shift)
    # service-credit component: the purchase valued at the DESIGN's own retirement date, holding
    # the date fixed, so the two components sum to gross without double counting.
    svc_only = w["pv"] - pv_with_design(plan, sex, age_elect, service_elect, salary_elect, 0.0,
                                        completion_months, deadline_months, shift,
                                        retire_immediately, months_to_eligibility)["pv"]
    gross = w["pv"] - c["pv"]
    return {
        "retire_age_with_design": w["retire_age"],
        "months_to_retirement": w["months_to_retirement"],
        "expected_counterfactual_retire_age": c["expected_retire_age"],
        "acceleration_months": max(0.0, (c["expected_retire_age"] - w["retire_age"]) * 12.0),
        "pv_with_design": w["pv"], "pv_counterfactual": c["pv"],
        "gross_liability_increase": gross,
        "service_credit_component": svc_only,
        "early_retirement_component": gross - svc_only,
        "member_payment": member_payment,
        "trust_cost": gross - member_payment,
        "p_counterfactual_retire": c["p_retire"], "p_counterfactual_terminate": c["p_terminate"],
    }
