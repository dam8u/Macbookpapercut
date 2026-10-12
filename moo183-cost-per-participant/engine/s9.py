"""
S9 - buy a WAIVER of the early-retirement reduction instead of service credit.
South Carolina's 2000 buy-down device, via the MOO-8 comparative work.

Nothing is added to the benefit formula.  Service credit is unchanged.  The member pays to have
the early-retirement reduction factor set to 1.000.

The reduction factor is DERIVED, not quoted, because VRS does not publish one.  VRS's employer
manual (service retirement, p.6) says only that "a member's benefit is actuarially reduced to
calculate the reduced Basic Benefit".  Taking that at its word:

    RF(R) = [ v^(U-R) * (U-R)p_R * a(U) ] / a(R)

for a member retiring at age R with service frozen at R, where U is the age at which that frozen
service first produces an unreduced benefit, a(.) is the COLA-indexed annuity-due factor already
used everywhere else in this model, and RF = 1.000 when R >= U.  This is the factor that makes
commencing early exactly equivalent to deferring to U - i.e. no subsidy either way.

CONSEQUENCE, and it is the whole S9 result: if the reduction really is actuarially equivalent,
then the waiver's full present value is what the member pays under the "actuarial" price rule, and
the trust is made whole on the waiver by construction.  What is left on the trust's books is only
the ordinary effect of the member stopping work earlier - fewer years of accrual and a lower AFC -
which is a SAVING to the pension fund, not a cost.  S9's fiscal problem therefore is not the trust;
it is the agency payroll (handled in workforce.py) and the member's willingness to pay.

Direction of error, stated plainly: public-plan reduction factors are frequently MORE generous than
strict actuarial equivalence.  If VRS's unpublished factors are more generous, the waiver is worth
less than computed here, the member price below is OVERSTATED, and the trust cost is UNDERSTATED.
Pulling the other way, VRS applies "an additional reduction factor ... under the 50/10 reduced
retirement provision" (same page), which makes the reduction harsher than actuarial for that
cohort and the waiver worth MORE than computed here.  Neither adjustment can be quantified from
public data.

MOO-38 CORRECTION, 2026-10-11.  The premise of the paragraph above is FALSE and the method is
therefore wrong.  VRS does publish the factors (Employer Manual, Service Retirement, July 2026, p.4
"Reduction by Type"; Benefits & Actuarial Committee, 17 June 2026, "Early Retirement Factors Study",
pp.14-21) and VRS does NOT use actuarial equivalence - it uses FIXED-RATE reductions that sit above
actuarial equivalence at every age by 3.59%-17.48% on VRS's own measurement.  The published rule is
implemented in `vrs_erf.py`, which reproduces all 35 published rows exactly, and is now the default.
The derived actuarial-equivalence factor is retained behind
`IN.ERF_METHOD_BASIS = "actuarial_equivalent_derived"` solely so MOO-31's published S9 numbers stay
regenerable as a regression lock.  See MOO-38 and `README_MOO38.md`.
"""
import inputs as IN
import vrs_erf as ERF
from pricing import Pricer, Profile, v

PR = Pricer()


def service_at(p: Profile, retire_age):
    """Credited service the member actually holds at `retire_age` (no purchase: S9 adds none)."""
    return p.service + max(0.0, retire_age - p.age)


def unreduced_age_frozen(p: Profile, retire_age, basis=None):
    """The age the reduction is measured back FROM, for service held at `retire_age`.

    Despite the name this has always PROJECTED service past `retire_age` (plan 1: `+ (30 - svc)`;
    plan 2: `/2`, i.e. one year of age and one of service per year worked).  MOO-38 keeps that as
    the central basis - it is the only reading either VRS source states explicitly, via the 60/5
    rule's "the first date on which the member WOULD HAVE completed 30 years of service" - and
    exposes the frozen-service alternative through `vrs_erf.ERF_UNREDUCED_BASIS`.
    """
    return ERF.unreduced_age(p.plan, retire_age, service_at(p, retire_age), basis=basis)


def reduction_factor(p: Profile, retire_age, mort=None, method=None, basis=None,
                     composition=None):
    """VRS's early-retirement reduction factor at `retire_age`.

    method="fixed_rate_published"        -> VRS's published fixed-rate rule (`vrs_erf`).  DEFAULT.
    method="actuarial_equivalent_derived" -> MOO-31's derived actuarially equivalent factor,
                                            RF = v^(U-R) * (U-R)p_R * a(U)/a(R).  Regression only.
    """
    method = IN.ERF_METHOD_BASIS["value"] if method is None else method
    if method == "fixed_rate_published":
        return ERF.erf(p.plan, retire_age, service_at(p, retire_age), basis=basis,
                       composition=composition)
    if method != "actuarial_equivalent_derived":
        raise ValueError(method)
    m = mort or PR.m
    U = unreduced_age_frozen(p, retire_age, basis=basis)
    if U <= retire_age:
        return 1.0
    n = U - retire_age
    return (v(n) * m.survive(retire_age, U) * m.annuity(U, p.plan)) / m.annuity(retire_age, p.plan)


def pv_unreduced_frozen(p: Profile, retire_age):
    """PV at the member's CURRENT age of an unreduced benefit on service accrued to `retire_age`."""
    return PR.pv_benefit(p, retire_age, 0.0)


def waiver_value(p: Profile, retire_age, method=None, basis=None, composition=None):
    """PV of waiving the reduction: (1 - RF) x PV of the unreduced benefit at `retire_age`."""
    rf = reduction_factor(p, retire_age, method=method, basis=basis, composition=composition)
    pv_unred = pv_unreduced_frozen(p, retire_age)
    return {
        "retire_age": retire_age,
        "unreduced_age_frozen": unreduced_age_frozen(p, retire_age, basis=basis),
        "years_early": max(0.0, unreduced_age_frozen(p, retire_age, basis=basis) - retire_age),
        "reduction_factor": rf,
        "pv_unreduced": pv_unred,
        "pv_reduced": rf * pv_unred,
        "waiver_value": (1.0 - rf) * pv_unred,
    }


def s9_member_price(p: Profile, retire_age, years_equivalent, rule="actuarial",
                    method=None, basis=None, composition=None):
    """Member price for the waiver.

    rule="actuarial"  -> the full PV of the waiver (the South Carolina device as described).
    rule="anc_parity" -> the same statutory formula S2 uses: ANC rate x salary basis x the number of
                         years of unreduced-eligibility the waiver advances.  Drafting-simplest, and
                         the apples-to-apples price comparison against S2.
    """
    w = waiver_value(p, retire_age, method=method, basis=basis, composition=composition)
    if rule == "actuarial":
        return w["waiver_value"], w
    if rule == "anc_parity":
        return PR.anc_price(p, years_equivalent), w
    raise ValueError(rule)


def s9_participant_cost(p: Profile, years_equivalent, months_accel=None,
                        retire_immediately=None, baseline_extra=None, rule="actuarial",
                        method=None, basis=None, composition=None):
    """One participant's gross liability, member payment and net plan cost under S9.

    The retirement date is the ONLY lever S9 pulls, so it is set explicitly:
      retire_immediately=True  -> R1 = the member's current age (the Utah-style guardrail in the
                                  MOO-3 memo 4.2, and the only case in which the waiver has value
                                  for this population).
      retire_immediately=False -> R1 = baseline retirement date pulled back by `months_accel`,
                                  i.e. exactly the S0-S7 convention.
    """
    extra = IN.BASELINE_EXTRA_YEARS_WORKED["value"] if baseline_extra is None else baseline_extra
    ma = IN.MONTHS_ACCELERATION["value"]["central"] if months_accel is None else months_accel
    ri = IN.S9_RETIRE_IMMEDIATELY["value"] if retire_immediately is None else retire_immediately

    r0 = p.unreduced_age(0.0) + extra
    r1 = p.age if ri else max(p.age, r0 - ma / 12.0)

    pv1 = pv_unreduced_frozen(p, r1)          # unreduced, actual service, retires at r1
    pv0 = PR.pv_benefit(p, r0, 0.0)           # counterfactual: works on, retires unreduced at r0
    pay, w = s9_member_price(p, r1, years_equivalent, rule=rule, method=method, basis=basis,
                             composition=composition)
    elig, prov = ERF.retirement_eligible(p.plan, r1, service_at(p, r1))
    return {
        "baseline_retire_age": r0, "actual_retire_age": r1,
        "months_accelerated": max(0.0, (r0 - r1) * 12.0),
        "retirement_eligible": elig, "eligibility_provision": prov,
        "reduction_factor": w["reduction_factor"],
        "years_early_vs_unreduced": w["years_early"],
        "waiver_value": w["waiver_value"],
        "pv_with_design": pv1, "pv_counterfactual": pv0,
        "gross_liability_increase": pv1 - pv0,
        "member_payment": pay,
        "net_plan_cost": (pv1 - pv0) - pay,
        "service_credit_component": 0.0,      # S9 adds none, by construction
        "early_retire_component": pv1 - pv0,
    }


def s2_same_outcome(p: Profile, years, months_accel=None, retire_immediately=None,
                    baseline_extra=None):
    """S2 (buy credit at ANC) forced onto the SAME retirement date, for a like-for-like comparison."""
    extra = IN.BASELINE_EXTRA_YEARS_WORKED["value"] if baseline_extra is None else baseline_extra
    ma = IN.MONTHS_ACCELERATION["value"]["central"] if months_accel is None else months_accel
    ri = IN.S9_RETIRE_IMMEDIATELY["value"] if retire_immediately is None else retire_immediately
    r0 = p.unreduced_age(0.0) + extra
    r1 = p.age if ri else max(p.age, r0 - ma / 12.0)
    pv1 = PR.pv_benefit(p, r1, years)
    pv0 = PR.pv_benefit(p, r0, 0.0)
    pay = PR.anc_price(p, years)
    return {
        "baseline_retire_age": r0, "actual_retire_age": r1,
        "pv_with_design": pv1, "pv_counterfactual": pv0,
        "gross_liability_increase": pv1 - pv0,
        "member_payment": pay,
        "net_plan_cost": (pv1 - pv0) - pay,
    }
