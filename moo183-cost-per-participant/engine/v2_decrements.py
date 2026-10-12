"""
v2 - VRS's own published decrements, applied monthly.

This file exists to answer red team F1: "estimate the counterfactual retirement date separately
and visibly rather than burying it in a lag assumption."  MOO-7 used
BASELINE_EXTRA_YEARS_WORKED = 2.0 years, an analyst judgment.  VRS publishes the assumption, so
the repaired model uses VRS's.

Three decrements, all PRIMARY from the Appendix to the June 30, 2025 Annual Actuarial Valuation
Reports:

  retirement   p.53 (Plan 1), pp.54-55 (Plan 2 / Hybrid)
  termination  p.56
  mortality    already fitted in mortality.py from the SOA PubG-2010 tables VRS uses

Annual rates are converted to monthly by 1 - (1 - q)^(1/12), which is the standard uniform-force
conversion and is what keeps a 16% annual Plan 1 age-50 retirement rate from being applied twelve
times over.
"""
import inputs as IN

RR1 = IN.RETIREMENT_RATES_PLAN1["value"]
RR2 = IN.RETIREMENT_RATES_PLAN2_AGE60PLUS["value"]
RR2_R90 = IN.RETIREMENT_RATE_PLAN2_RULE90["value"]
RR_OLD = IN.RETIREMENT_RATES_AGE71PLUS["value"]
TR = IN.TERMINATION_RATES_STATE["value"]
MIX = IN.PARTICIPANT_GENDER_MIX["value"]


def _p1_band(service):
    if service < 5:
        return 0
    if service < 10:
        return 1
    if service < 30:
        return 2
    return 3


def retire_rate(plan, age, service, sex):
    """Annual probability of service retirement, VRS State Employee assumption."""
    a = int(age)
    if plan == "plan1":
        if a < 50:
            return 0.0
        if a >= 80:
            return 1.0
        return RR1[sex][min(a, 79)][_p1_band(service)]
    # Plan 2 and Hybrid
    if service < 5:
        return 0.0
    if a >= 80:
        return 1.0
    if a >= 71:
        return RR_OLD[sex]
    if a >= 60:
        return RR2[sex][a]
    return RR2_R90 if (age + service) >= 89.0 else 0.0


def term_rate(service, sex):
    """Annual probability of termination (withdrawal), VRS State Employee assumption."""
    k = int(service)
    return TR[sex][min(max(k, 0), 20)]


def monthly(q):
    """Annual decrement probability -> monthly, uniform force of decrement."""
    if q <= 0.0:
        return 0.0
    if q >= 1.0:
        return 1.0
    return 1.0 - (1.0 - q) ** (1.0 / 12.0)


def blend(fn):
    """Weight a sex-specific rate function by the modelled participant gender mix."""
    return lambda *a: sum(w * fn(*a, s) for s, w in MIX.items())
