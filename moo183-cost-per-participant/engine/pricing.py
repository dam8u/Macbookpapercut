"""
Part 2 - pricing a member purchase and the plan's cost.

ONE liability formula, applied twice:

    PV(x | retire_age, purchased_years) =
        mult * service_at_retirement * AFC(retire_age) * annuity(retire_age)
        * v^(retire_age - x) * (retire_age - x)p_x

    GROSS LIABILITY INCREASE = PV(x | R1, years) - PV(x | R0, 0)

where R1 is when the member actually retires under the design and R0 is when they would have
retired absent it.  This single difference is correct whether or not the design moves the
retirement date, and it avoids double-counting the service effect and the timing effect.

Two named special cases:

  AEC_full   - the price under CURRENT LAW after the 24-month window.  Va. Code 51.1-142.2 and the
               VRS employer manual (p.11) define actuarial equivalent cost as "the amount of money
               needed in today's dollars to pay for the total value of the increase in the
               employee's future retirement benefit OR EARLIER RETIREMENT ELIGIBILITY DATE".  So
               AEC_full = PV(x | earliest-eligible-WITH-purchase, years)
                        - PV(x | earliest-eligible-WITHOUT-purchase, 0).
               This is the headline price the bill would reduce.

  AEC_svc    - the same calculation with the retirement date held CONSTANT, i.e. the value of the
               extra service credit alone with no eligibility acceleration.  Reported separately
               because it is the whole cost for a Pathway B participant who was leaving anyway.

Caveat flagged in the write-up: this model values the basic single-life benefit only.  It excludes
the retiree Health Insurance Credit, Group Life, and any survivor-option loading, all of which VRS
would include.  Direction of error: UNDERSTATES both the actuarial-equivalent price and the plan's
cost, by an amount this model does not quantify.
"""
from dataclasses import dataclass

import inputs as IN
from mortality import Mortality

I_NOM = IN.DISCOUNT_RATE["value"]
G_SAL = IN.PAYROLL_GROWTH["value"]


def v(n):
    return (1.0 + I_NOM) ** (-n)


@dataclass
class Profile:
    plan: str          # "plan1" | "plan2" | "hybrid"
    age: float
    service: float     # completed years of creditable service now
    salary: float      # current annual creditable compensation
    label: str = ""

    @property
    def mult(self):
        return {"plan1": IN.MULT_PLAN1, "plan2": IN.MULT_PLAN2,
                "hybrid": IN.MULT_HYBRID}[self.plan]["value"]

    @property
    def anc_rate(self):
        return {"plan1": IN.ANC_PLAN1, "plan2": IN.ANC_PLAN2,
                "hybrid": IN.ANC_HYBRID}[self.plan]["value"]

    @property
    def afc_months(self):
        return {"plan1": IN.AFC_MONTHS_PLAN1, "plan2": IN.AFC_MONTHS_PLAN2,
                "hybrid": IN.AFC_MONTHS_PLAN2}[self.plan]["value"]

    def afc_at(self, retire_age):
        """Projected AFC if the member retires at `retire_age` (salary grows at payroll growth)."""
        t_ret = max(0.0, retire_age - self.age)
        m = int(round(self.afc_months))
        tot = sum(self.salary * (1.0 + G_SAL) ** (t_ret - j / 12.0) for j in range(1, m + 1))
        return tot / m

    def unreduced_age(self, purchased=0.0):
        """Earliest age at which an unreduced benefit is available, given `purchased` years."""
        s = self.service + purchased
        if self.plan == "plan1":
            # age 65 with 5 yrs, or age 50 with 30 yrs
            by_service = self.age + max(0.0, 30.0 - s)
            return min(65.0, max(50.0, by_service))
        # Plan 2 / Hybrid: normal SSRA (67) with 5 yrs, or age + service = 90
        by_rule90 = self.age + max(0.0, (90.0 - self.age - s) / 2.0)
        return min(67.0, by_rule90)

    def hybrid_like(self):
        return self.plan == "hybrid"


class Pricer:
    def __init__(self, mort=None):
        self.m = mort or Mortality()

    # ---- the single liability formula -------------------------------------------------
    def pv_benefit(self, p: Profile, retire_age: float, purchased: float):
        retire_age = max(retire_age, p.age)
        service = p.service + (retire_age - p.age) + purchased
        afc = p.afc_at(retire_age)
        annual = p.mult * service * afc
        n = retire_age - p.age
        return annual * self.m.annuity(retire_age, p.plan) * v(n) * self.m.survive(p.age, retire_age)

    def anc_price(self, p: Profile, years: float):
        """Price inside the window: rate x higher of current comp or AFC, x years purchased."""
        basis = max(p.salary, p.afc_at(p.age))
        return p.anc_rate * basis * years

    # ---- the two named actuarial-equivalent measures -----------------------------------
    def aec_full(self, p: Profile, years: float):
        """Current-law price: value of extra benefit AND earlier eligibility date."""
        r_with = p.unreduced_age(years)
        r_without = p.unreduced_age(0.0)
        return self.pv_benefit(p, r_with, years) - self.pv_benefit(p, r_without, 0.0)

    def aec_service_only(self, p: Profile, years: float, retire_age: float = None):
        """Value of the extra service credit with the retirement date held constant."""
        if retire_age is None:
            retire_age = p.unreduced_age(years)
        return self.pv_benefit(p, retire_age, years) - self.pv_benefit(p, retire_age, 0.0)

    # ---- what the design actually costs the plan ---------------------------------------
    def baseline_retire_age(self, p: Profile):
        return p.unreduced_age(0.0) + IN.BASELINE_EXTRA_YEARS_WORKED["value"]

    def design_cost(self, p: Profile, years: float, months_accel: float,
                    member_payment: float = None, baseline_extra: float = None,
                    purchase_loads_afc: bool = True):
        """Gross liability increase and net plan cost for one participant under the design."""
        extra = IN.BASELINE_EXTRA_YEARS_WORKED["value"] if baseline_extra is None else baseline_extra
        r0 = p.unreduced_age(0.0) + extra
        r1 = max(p.unreduced_age(years), r0 - months_accel / 12.0, p.age)
        pv1 = self.pv_benefit(p, r1, years)
        pv0 = self.pv_benefit(p, r0, 0.0)
        gross = pv1 - pv0
        pay = self.anc_price(p, years) if member_payment is None else member_payment
        svc_only = self.aec_service_only(p, years, retire_age=r0)
        return {
            "years": years, "baseline_retire_age": r0, "actual_retire_age": r1,
            "months_accelerated": max(0.0, (r0 - r1) * 12.0),
            "pv_with_design": pv1, "pv_counterfactual": pv0,
            "gross_liability_increase": gross,
            "service_credit_component": svc_only,
            "early_retirement_subsidy_component": gross - svc_only,
            "member_payment": pay,
            "net_plan_cost": gross - pay,
        }

    # ---- member-side payoff -------------------------------------------------------------
    def member_payoff(self, p: Profile, years: float, member_payment: float = None):
        r_with = p.unreduced_age(years)
        r_without = p.unreduced_age(0.0)
        pay = self.anc_price(p, years) if member_payment is None else member_payment
        afc = p.afc_at(r_with)
        d_annual_service = p.mult * afc * years        # extra annual benefit from extra service
        value = self.aec_full(p, years)                # total PV of what the purchase buys
        cola = IN.COLA_PLAN1["value"] if p.plan == "plan1" else IN.COLA_PLAN2["value"]
        a_undisc = self.m.annuity(r_with, p.plan, i=(1.0 / (1.0 + cola)) - 1.0)
        lifetime_nominal = d_annual_service * a_undisc * self.m.survive(p.age, r_with)
        # years of retirement needed to recover the cash outlay from the benefit uplift
        payback = pay / d_annual_service if d_annual_service else float("nan")
        return {
            "member_payment": pay,
            "earliest_retire_with": r_with, "earliest_retire_without": r_without,
            "eligibility_accelerated_years": r_without - r_with,
            "annual_benefit_increase": d_annual_service,
            "lifetime_nominal_benefit_increase": lifetime_nominal,
            "pv_value_to_member": value,
            "value_per_dollar_paid": value / pay if pay else float("nan"),
            "simple_payback_years": payback,
        }
