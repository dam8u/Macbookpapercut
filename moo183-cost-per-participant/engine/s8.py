"""
S8 - Earned-Service Repricing, modelled on 71 Pa.C.S. 5505(b).

    member price = TNC_rate
                 x  (average annual creditable compensation over the FIRST `m` months of service)
                 x  years purchased
                 x  (1 + i_stat) ** (service_now - m/12)

The three terms in words:

  TNC_rate          VRS's published approximate-normal-cost rate for the plan.  VRS defines that
                    rate as "the average cost of one year of VRS service credit" (employer manual,
                    purchase of prior service, p.11), i.e. the total member-plus-employer cost -
                    exactly what 5505(b) charges.  So S8 and ANC use the SAME rate, and the whole
                    S8/ANC multiple collapses to

                        S8 / ANC  =  (first-m-month comp / ANC salary basis) x (1+i)^n

                    which is why this file reports that decomposition directly: the reader can see
                    the salary term and the interest term separately and watch which one wins.

  salary basis      Reconstructed from the member's CURRENT salary by walking VRS's own
                    service-based individual salary-increase scale BACKWARDS to date of hire.
                    (inputs.VRS_SALARY_SCALE_STATE - PRIMARY, valuation appendix p.57.)

  interest term     Compounded annually from the END of the averaging period to the date of
                    purchase, per 5505(b) ("together with statutory interest during all periods of
                    subsequent State and school service to date of purchase").

STRUCTURAL RESULT, derived here rather than asserted: the price moves with time-since-hire at
roughly (1 + i_stat) / (1 + g_salary) - 1 per year.  The basis is calendar-NEUTRAL only when the
statutory interest rate equals the member's own salary-growth rate.  Above that the interest term
dominates and S8 re-creates a calendar penalty; below it, S8 rewards long service.  See
`crossover_interest_rate` and `calendar_slope`.
"""
import inputs as IN
from pricing import Pricer, Profile

SCALE = IN.VRS_SALARY_SCALE_STATE["value"]
_MAX_KEY = max(SCALE)


def salary_increase_rate(completed_service_years, shift=0.0):
    """VRS individual salary-increase rate applying over the year of service [s, s+1)."""
    k = int(completed_service_years)
    if k < 0:
        k = 0
    if k > _MAX_KEY:
        k = _MAX_KEY
    return SCALE[k] + shift


def salary_path_backcast(current_salary, service_now, shift=0.0):
    """Salary at each completed year of service from 0 to int(service_now), walking the scale back.

    Returns a list `sal` where sal[k] is the annual rate of compensation at completed service k.
    sal[int(service_now)] is anchored to the member's current salary.
    """
    n = int(round(service_now))
    sal = [0.0] * (n + 1)
    sal[n] = current_salary
    for k in range(n - 1, -1, -1):
        sal[k] = sal[k + 1] / (1.0 + salary_increase_rate(k, shift))
    return sal


def first_months_avg_comp(current_salary, service_now, months=None, shift=0.0):
    """Average annual RATE of compensation over the first `months` of VRS service.

    Evaluated monthly: within service year k the annual rate is interpolated geometrically from
    sal[k] to sal[k+1], which is how a salary that steps once a year but is measured monthly
    actually behaves.  The result is the mean of the 12*`months`/12 monthly annual-rate readings.
    """
    m = int(IN.S8_AVERAGING_MONTHS["value"] if months is None else months)
    sal = salary_path_backcast(current_salary, service_now, shift)
    if service_now * 12.0 < m:
        m = max(1, int(service_now * 12.0))
    tot, cnt = 0.0, 0
    for j in range(m):
        t = j / 12.0
        k = int(t)
        frac = t - k
        if k + 1 < len(sal):
            rate = sal[k] * (sal[k + 1] / sal[k]) ** frac if sal[k] > 0 else 0.0
        else:
            rate = sal[-1]
        tot += rate
        cnt += 1
    return tot / cnt


def interest_years(service_now, months=None):
    """Years from the END of the averaging period to the date of purchase (5505(b))."""
    m = IN.S8_AVERAGING_MONTHS["value"] if months is None else months
    return max(0.0, service_now - m / 12.0)


def tnc_rate(p: Profile, narrow=False):
    return IN.S8_TNC_NARROW_RATE["value"] if narrow else p.anc_rate


def s8_price(p: Profile, years, i_stat=None, months=None, shift=0.0, narrow=False,
             service_match_cap=True, extra_service_at_purchase=0.0):
    """S8 member price, plus the decomposition that explains it.

    `extra_service_at_purchase` lets the caller price a purchase that happens N years after the
    6/30/2025 snapshot (the pilot runs FY2028-FY2031).  It adds N years of salary growth AND N
    years of interest, which is the honest way to handle the timing rather than ignoring it.
    """
    i = IN.S8_INTEREST_RATE["value"] if i_stat is None else i_stat
    m = IN.S8_AVERAGING_MONTHS["value"] if months is None else months
    svc = p.service + extra_service_at_purchase
    sal_now = p.salary
    for k in range(int(round(p.service)), int(round(svc))):
        sal_now *= (1.0 + salary_increase_rate(k, shift))

    yrs = years
    capped_by_service_match = False
    if service_match_cap and IN.S8_SERVICE_MATCHING_CAP["value"] and yrs > svc:
        yrs = svc
        capped_by_service_match = True

    base = first_months_avg_comp(sal_now, svc, months=m, shift=shift)
    n = interest_years(svc, months=m)
    rate = tnc_rate(p, narrow)
    accum = (1.0 + i) ** n
    price = rate * base * yrs * accum

    anc_basis = max(sal_now, p.afc_at(p.age + extra_service_at_purchase))
    return {
        "price": price,
        "price_per_year": price / yrs if yrs else 0.0,
        "years_priced": yrs,
        "capped_by_service_match": capped_by_service_match,
        "tnc_rate": rate,
        "first_m_month_avg_comp": base,
        "salary_at_purchase": sal_now,
        "anc_salary_basis": anc_basis,
        "salary_term": base / anc_basis if anc_basis else 0.0,   # < 1: makes S8 cheaper than ANC
        "interest_years": n,
        "interest_term": accum,                                   # > 1: makes S8 dearer than ANC
        "implied_multiple_of_anc": (base / anc_basis) * accum * (rate / p.anc_rate)
                                   if anc_basis else 0.0,
    }


def calendar_slope(i_stat=None, service_years=27, shift=0.0):
    """d(ln price)/d(years since hire): the per-year calendar gradient the basis creates.

    Positive -> the basis PENALISES long service (interest term wins).
    Negative -> the basis REWARDS long service (salary term wins).
    Zero     -> the basis is calendar-neutral, which is the design intent.
    """
    i = IN.S8_INTEREST_RATE["value"] if i_stat is None else i_stat
    g = salary_increase_rate(service_years, shift)
    return (1.0 + i) / (1.0 + g) - 1.0


def crossover_interest_rate(p: Profile, years, pr: Pricer, target="aec_full",
                            months=None, shift=0.0, lo=0.0, hi=0.30, tol=1e-7):
    """Statutory interest rate at which the S8 price equals a reference price.

    target = "aec_full" -> the current-law actuarial-equivalent price.  Above this rate S8 is WORSE
                           for the veteran than doing nothing, which would be fatal to the design.
    target = "anc"      -> the approximate-normal-cost price (the S1 ask).
    """
    ref = pr.aec_full(p, years) if target == "aec_full" else pr.anc_price(p, years)

    def f(i):
        return s8_price(p, years, i_stat=i, months=months, shift=shift)["price"] - ref

    if f(lo) > 0:
        return None            # already dearer than the reference at zero interest
    if f(hi) < 0:
        return float("inf")    # never reaches the reference inside the bracket
    a, b = lo, hi
    while b - a > tol:
        mid = (a + b) / 2.0
        if f(mid) < 0:
            a = mid
        else:
            b = mid
    return (a + b) / 2.0
