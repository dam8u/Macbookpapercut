"""Profile set for Part 2: age x service x salary percentile x plan."""
import inputs as IN
from pricing import Profile

AGES = [50, 55, 60, 62]
SERVICES = [25, 27, 29, 31]
PCTILES = ["p25", "p50", "p75"]


def long_service_median_salary():
    """Median salary of a state employee aged 50-64 with 25+ years of service.

    Base: payroll-weighted average salary for ages 50-64 from the VRS age/service table (primary),
    uplifted by the long-service premium (analyst judgment) because the VRS table gives payroll by
    AGE only, not by age x service.
    """
    t = IN.AGE_SERVICE_TABLE["value"]
    bands = ["50-54", "55-59", "60", "61", "62", "63", "64"]
    n = sum(t[b][7] for b in bands)
    pay = sum(t[b][8] for b in bands)
    base = pay / n
    return base * (1.0 + IN.LONG_SERVICE_PREMIUM["value"]), base, n


def salary_for(pctile):
    med, _, _ = long_service_median_salary()
    return round(med * IN.SALARY_DISPERSION["value"][pctile], -2)


def profile_set(plans=("plan1", "plan2")):
    out = []
    for plan in plans:
        for age in AGES:
            for svc in SERVICES:
                for pc in PCTILES:
                    out.append(Profile(plan=plan, age=float(age), service=float(svc),
                                       salary=salary_for(pc),
                                       label=f"{plan}/age{age}/svc{svc}/{pc}"))
    return out
