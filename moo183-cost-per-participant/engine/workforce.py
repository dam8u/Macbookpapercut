"""
Part 4 - the workforce / early-retirement offset, and the break-even.

Two views are reported because they are NOT the same number and conflating them is the commonest
error in "turnover savings pay for it" claims:

  AGENCY BUDGET VIEW.  What shows up in an appropriation.  The employing agency pays the SAME
  blended employer DB rate (11.07% for FY2027-28) whatever tier the employee is in, PLUS up to 3.5%
  of pay in Hybrid DC contributions for a post-2014 hire.  So on the agency's books, replacing a
  Plan 1 incumbent with a Hybrid hire at the SAME salary costs MORE, not less.  All agency-level
  saving therefore has to come out of the salary differential.

  COMMONWEALTH / TRUST VIEW.  The plan's tier-specific normal cost falls when a Plan 1 member is
  replaced by a Hybrid member (12.50% -> 6.68% + up to 3.5% DC).  That saving is real but it accrues
  to the trust fund and only reaches budgets years later through a lower certified rate.  It cannot
  be appropriated against in the biennium the pilot runs.

Conservative choices, stated:
  * The employer share of health insurance is a FLAT per-position premium, so a lower-paid
    replacement produces NO health-premium saving.  Excluded.
  * The full recruitment cost and productivity-ramp loss are charged against EVERY participant,
    even though a pure timing shift would merely re-time costs the Commonwealth would have borne
    at the later retirement date anyway.  The "timing shift only" variant is reported as the
    optimistic bound.
  * Savings are counted only over the acceleration period, not in perpetuity.
"""
import inputs as IN

L_VARIABLE = (IN.ER_DB_RATE["value"] + IN.ER_GLI["value"] + IN.ER_HIC["value"]
              + IN.ER_VSDP["value"] + IN.ER_FICA["value"])          # 20.90%
L_REPLACEMENT = L_VARIABLE + IN.HYBRID_ER_DC["value"]                # + 3.5% hybrid DC

# Commonwealth/trust view components
NC_PLAN1 = IN.ANC_PLAN1["value"]        # 12.50%, used as the Plan 1 tier normal cost proxy
NC_HYBRID = IN.ANC_HYBRID["value"]      # 6.68%
UAAL_RATE = 0.0649                      # VRS_VAL p.18, applies to payroll regardless of tier
ADMIN_RATE = 0.0024


def per_participant(incumbent_salary, months_accel, differential, vacancy_months=None,
                    coverage_share=None, recruit=None, ramp=None, timing_shift_only=False):
    """Net workforce effect for ONE participant, agency budget view, over the acceleration period."""
    vac = IN.VACANCY_MONTHS["value"] if vacancy_months is None else vacancy_months
    cov = IN.VACANCY_COVERAGE_COST_SHARE["value"] if coverage_share is None else coverage_share
    rec = IN.RECRUITMENT_COST_PER_HIRE["value"] if recruit is None else recruit
    rmp = IN.PRODUCTIVITY_RAMP_LOSS["value"] if ramp is None else ramp

    S_i = incumbent_salary
    S_r = S_i * (1.0 - differential)
    m = max(0.0, months_accel)

    cost_incumbent = S_i * (1.0 + L_VARIABLE) * m / 12.0
    vac_m = min(vac, m)
    rep_m = max(0.0, m - vac)
    cost_successor = (S_i * cov) * vac_m / 12.0 + S_r * (1.0 + L_REPLACEMENT) * rep_m / 12.0

    gross_saving = cost_incumbent - cost_successor
    frictions = 0.0 if timing_shift_only else (rec + rmp * S_r)
    net = gross_saving - frictions

    # Commonwealth/trust view: tier-mix effect over the same window
    trust_inc = S_i * (NC_PLAN1 + UAAL_RATE + ADMIN_RATE) * m / 12.0
    trust_rep = S_r * (NC_HYBRID + IN.HYBRID_ER_DC["value"] + UAAL_RATE + ADMIN_RATE) * rep_m / 12.0
    tier_mix = trust_inc - trust_rep - S_i * 0.0 * vac_m

    return {
        "incumbent_salary": S_i, "replacement_salary": S_r,
        "months_accelerated": m,
        "annual_salary_differential": S_i - S_r,
        "annual_loaded_differential": S_i * (1 + L_VARIABLE) - S_r * (1 + L_REPLACEMENT),
        "incumbent_cost_over_window": cost_incumbent,
        "successor_cost_over_window": cost_successor,
        "gross_saving": gross_saving,
        "recruitment_and_ramp": frictions,
        "net_workforce_effect": net,
        "trust_tier_mix_effect": tier_mix,
    }


def case_table(incumbent_salary, pension_net_cost_per_participant):
    """Conservative / central / optimistic net workforce effect, and the backfill cases."""
    out = {}
    for lvl in ("conservative", "central", "optimistic"):
        m = IN.MONTHS_ACCELERATION["value"][lvl]
        d = IN.REPLACEMENT_DIFFERENTIAL["value"][lvl]
        r = per_participant(incumbent_salary, m, d,
                            coverage_share={"conservative": 0.90, "central": 0.55,
                                            "optimistic": 0.25}[lvl],
                            ramp={"conservative": 0.40, "central": 0.25, "optimistic": 0.10}[lvl],
                            recruit={"conservative": 8000, "central": 5000, "optimistic": 3000}[lvl],
                            timing_shift_only=(lvl == "optimistic"))
        r["pension_net_cost"] = pension_net_cost_per_participant
        r["net_state_effect"] = r["net_workforce_effect"] - pension_net_cost_per_participant
        out[lvl] = r

    # the three backfill behaviours, at central acceleration
    m = IN.MONTHS_ACCELERATION["value"]["central"]
    bf = {}
    bf["lower_cost_backfill"] = per_participant(
        incumbent_salary, m, IN.REPLACEMENT_DIFFERENTIAL["value"]["central"])
    bf["equal_cost_backfill"] = per_participant(incumbent_salary, m, 0.0)
    left = per_participant(incumbent_salary, m, 0.0, vacancy_months=m,
                           recruit=0.0, ramp=0.0)
    bf["left_vacant"] = left
    out["backfill_cases"] = bf
    mix = IN.BACKFILL_BEHAVIOUR["value"]
    out["blended_backfill_net"] = sum(mix[k] * bf[k]["net_workforce_effect"] for k in mix)
    return out


# ---------------------------------------------------------------------------------
# break-even
# ---------------------------------------------------------------------------------
def breakeven_months(incumbent_salary, pension_net_cost, differential=None, **kw):
    d = IN.REPLACEMENT_DIFFERENTIAL["value"]["central"] if differential is None else differential
    lo, hi = 0.0, 240.0
    f = lambda m: per_participant(incumbent_salary, m, d, **kw)["net_workforce_effect"] - pension_net_cost
    if f(hi) < 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return hi


def breakeven_differential(incumbent_salary, pension_net_cost, months=None, **kw):
    m = IN.MONTHS_ACCELERATION["value"]["central"] if months is None else months
    lo, hi = 0.0, 0.95
    f = lambda d: per_participant(incumbent_salary, m, d, **kw)["net_workforce_effect"] - pension_net_cost
    if f(hi) < 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return hi


def breakeven_grid(incumbent_salary, pension_net_cost,
                   months_list=(3, 6, 9, 12, 18, 24), diff_list=(0.08, 0.13, 0.18, 0.24, 0.30)):
    grid = {}
    for m in months_list:
        grid[m] = {}
        for d in diff_list:
            r = per_participant(incumbent_salary, m, d)
            grid[m][d] = r["net_workforce_effect"] - pension_net_cost
    return grid
