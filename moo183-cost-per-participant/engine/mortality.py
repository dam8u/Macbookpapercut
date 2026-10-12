"""
Mortality and annuity factors.

VRS values the State Employee plan on PubG-2010 amount-weighted General Healthy Retiree rates
(100% of the male table, 110% of the female table) with 75% of the MP-2021 projection scale,
generational.  VRS does not publish the resulting q(x) vector, and the SOA does not publish the
Pub-2010 rate tables in a machine-readable form inside its report.

Rather than invent rates, this module FITS a Gompertz-Makeham force of mortality
    mu(x) = A + B * exp(k * x)
to the SOA's own published PubG-2010 annuity values (Table D.3, flat 7.00% interest, generational
with MP-2017) at ages 65, 75 and 85, separately for males and females.  The fit is then checked
OUT OF SAMPLE against the same table's deferred-to-62 values at ages 45 and 55.

This gives annuity factors that reproduce the published PubG-2010 annuity values at the one
interest rate the SOA published, and can then be re-evaluated at the VRS discount rate net of
the VRS COLA assumption.  The fit quality is reported so a reviewer can judge it.
"""
import math
import numpy as np
from scipy.optimize import least_squares

import inputs as IN

MONTHS = 12


def survival_curve(A, B, k, x0, x1=120.0, step=1.0 / MONTHS):
    """Monthly survival probabilities S(x0+t)/S(x0) under mu(x)=A+B*exp(kx).

    Integral of mu from x0 to x: A*(x-x0) + (B/k)*(exp(kx)-exp(k*x0)).
    """
    ts = np.arange(0.0, x1 - x0 + 1e-9, step)
    xs = x0 + ts
    H = A * (xs - x0) + (B / k) * (np.exp(k * xs) - np.exp(k * x0))
    return ts, np.exp(-H)


def annuity_due_monthly(A, B, k, age, i, cap_age=120.0):
    """Value of $1 per year paid monthly in advance, first payment now, at annual rate i."""
    ts, S = survival_curve(A, B, k, age, cap_age)
    v = (1.0 + i) ** (-ts)
    return float(np.sum(S * v) / MONTHS)


def deferred_annuity_due(A, B, k, age, defer_to, i):
    """Value at `age` of $1/yr paid monthly in advance starting at `defer_to`."""
    if defer_to <= age:
        return annuity_due_monthly(A, B, k, age, i)
    n = defer_to - age
    _, S = survival_curve(A, B, k, age, defer_to)
    S_n = float(S[-1])
    return S_n * (1.0 + i) ** (-n) * annuity_due_monthly(A, B, k, defer_to, i)


def fit_gompertz(targets, i=0.07):
    """Fit (A,B,k) to {age: immediate monthly annuity-due value} at interest i."""
    ages = sorted(targets)
    tgt = np.array([targets[a] for a in ages])

    def resid(p):
        A, logB, k = p
        B = math.exp(logB)
        got = np.array([annuity_due_monthly(A, B, k, a, i) for a in ages])
        return (got - tgt) / tgt

    sol = least_squares(resid, x0=[0.0005, math.log(2.5e-5), 0.098],
                        bounds=([0.0, math.log(1e-8), 0.03], [0.02, math.log(1e-2), 0.20]),
                        xtol=1e-14, ftol=1e-14)
    A, logB, k = sol.x
    return A, math.exp(logB), k, sol


class Mortality:
    """Fitted PubG-2010-calibrated mortality, with VRS's State/General table adjustments."""

    def __init__(self):
        self.i_fit = 0.07
        tgt = IN.SOA_D3_IMMEDIATE["value"]
        self.params = {}
        self.fit_report = {}
        for sex in ("male", "female"):
            A, B, k, sol = fit_gompertz(tgt[sex], self.i_fit)
            self.params[sex] = (A, B, k)
            fitted = {a: annuity_due_monthly(A, B, k, a, self.i_fit) for a in tgt[sex]}
            self.fit_report[sex] = {
                "params": {"A": A, "B": B, "k": k},
                "in_sample": {a: {"target": tgt[sex][a], "fitted": fitted[a],
                                  "pct_err": 100 * (fitted[a] / tgt[sex][a] - 1)} for a in tgt[sex]},
            }
        # out-of-sample check: deferred-to-62 values at 45 and 55
        d62 = IN.SOA_D3_DEFERRED62["value"]
        for sex in ("male", "female"):
            A, B, k = self.params[sex]
            oos = {}
            for a, t in d62[sex].items():
                got = deferred_annuity_due(A, B, k, a, 62, self.i_fit)
                oos[a] = {"target": t, "fitted": got, "pct_err": 100 * (got / t - 1)}
            self.fit_report[sex]["out_of_sample_deferred_to_62"] = oos

    # ---- VRS table adjustment: 100% male table, 110% female table -------------
    def _adj_params(self, sex):
        A, B, k = self.params[sex]
        if sex == "female":
            load = IN.VRS_FEMALE_LOAD["value"]
            return A * load, B * load, k
        return A, B, k

    def net_rate(self, plan):
        """Discount rate net of the VRS COLA assumption -> values a COLA-indexed benefit."""
        i = IN.DISCOUNT_RATE["value"]
        c = IN.COLA_PLAN1["value"] if plan == "plan1" else IN.COLA_PLAN2["value"]
        return (1.0 + i) / (1.0 + c) - 1.0

    def annuity(self, age, plan, sex=None, i=None):
        """Annuity-due factor for a COLA-indexed life annuity of $1/yr starting at `age`."""
        if i is None:
            i = self.net_rate(plan)
        if sex is not None:
            A, B, k = self._adj_params(sex)
            return annuity_due_monthly(A, B, k, age, i)
        mix = IN.PARTICIPANT_GENDER_MIX["value"]
        return sum(w * self.annuity(age, plan, sex=s, i=i) for s, w in mix.items())

    def survive(self, frm, to, sex=None):
        """Probability of surviving from age `frm` to age `to`."""
        if to <= frm:
            return 1.0
        if sex is not None:
            A, B, k = self._adj_params(sex)
            _, S = survival_curve(A, B, k, frm, to)
            return float(S[-1])
        mix = IN.PARTICIPANT_GENDER_MIX["value"]
        return sum(w * self.survive(frm, to, sex=s) for s, w in mix.items())

    def life_expectancy(self, age, sex):
        A, B, k = self._adj_params(sex)
        ts, S = survival_curve(A, B, k, age)
        return float(np.sum(S) / MONTHS)


if __name__ == "__main__":
    m = Mortality()
    for sex in ("male", "female"):
        r = m.fit_report[sex]
        p = r["params"]
        print(f"\n{sex.upper()}  Gompertz-Makeham  A={p['A']:.6g}  B={p['B']:.6g}  k={p['k']:.6g}")
        print("  in-sample (immediate annuity-due, 7.00% flat, SOA Table D.3):")
        for a, d in r["in_sample"].items():
            print(f"    age {a}: target {d['target']:.4f}  fitted {d['fitted']:.4f}  err {d['pct_err']:+.2f}%")
        print("  OUT OF SAMPLE (deferred-to-62, same table, NOT fitted):")
        for a, d in r["out_of_sample_deferred_to_62"].items():
            print(f"    age {a}: target {d['target']:.4f}  fitted {d['fitted']:.4f}  err {d['pct_err']:+.2f}%")
        print(f"  implied life expectancy (VRS-adjusted): age 55 {m.life_expectancy(55,sex):.1f}y, "
              f"age 65 {m.life_expectancy(65,sex):.1f}y")
    print(f"\nnet (real) discount rate: plan1 {m.net_rate('plan1'):.4%}, plan2 {m.net_rate('plan2'):.4%}")
    print("\nCOLA-indexed annuity-due factors (blended 75M/25F, VRS-adjusted):")
    for age in (50, 55, 60, 62, 65):
        print(f"  age {age}: plan1 {m.annuity(age,'plan1'):6.3f}   plan2 {m.annuity(age,'plan2'):6.3f}")
