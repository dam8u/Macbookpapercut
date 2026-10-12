"""
Step 6 - external sanity check.

Benchmark: VRS's OWN fiscal impact statement for SB 419 (2026 session), which awarded SPORS and
VaLORS members one extra year of creditable service per five full years of service.  VRS scored it
at ~$258M of added liability across the two plans.

That gives a published Virginia cost per EXTRA YEAR OF CREDITABLE SERVICE GRANTED, against which
this model's gross liability per year of purchased service can be compared.  The comparison must be
adjusted for three things, all stated:
  1. SPORS/VaLORS are hazardous-duty plans with much richer benefits (total normal cost 18.37% and
     14.30% vs 8.73% for State Employees), so their cost per year of service is structurally higher.
  2. SB 419 granted service to the ENTIRE active membership, including young members whose benefit
     is heavily discounted; this model's participants are at or near retirement, where the cost per
     year is highest.
  3. SB 419 granted the service FREE; this model's members pay the approximate normal cost, so the
     comparison is on GROSS liability, not net.
"""
import inputs as IN
import results
import scenarios as SC


def sb419_benchmark():
    v = IN.SB419_CHECK["value"]
    sp_n, va_n = IN.SPORS_ACTIVES["value"], IN.VALORS_ACTIVES["value"]
    sp_pay, va_pay = IN.SPORS_PAYROLL["value"], IN.VALORS_PAYROLL["value"]
    n = sp_n + va_n
    payroll = sp_pay + va_pay
    avg_sal = payroll / n
    # average extra service granted: 1 year per 5 full years. Average service is not published for
    # these plans in the valuation summary, so use the State Employee average service as a proxy and
    # flag it.
    avg_service_proxy = 10.3           # DHRM p.8, classified average years of service
    extra_years = avg_service_proxy / 5.0
    total_extra_year_members = n * extra_years
    cost_per_extra_year = v["liability_increase"] / total_extra_year_members
    return {
        "actives": n, "avg_salary": avg_sal,
        "assumed_avg_service_years": avg_service_proxy,
        "avg_extra_years_granted": extra_years,
        "member_years_granted": total_extra_year_members,
        "vrs_scored_liability": v["liability_increase"],
        "implied_cost_per_year_of_service": cost_per_extra_year,
        "implied_cost_as_pct_of_salary": cost_per_extra_year / avg_sal,
    }


def model_cost_per_year(scenario="S1"):
    r = results.net_state_cost(scenario=scenario)
    agg = r["_agg"]
    # total years purchased, weighted
    _, parts = SC.run_scenario(scenario, "central")
    years = sum(p.weight * p.years for p in parts)
    avg_sal = r["avg_participant_salary"]
    return {
        "gross_liability": agg["gross"], "years_purchased": years,
        "gross_per_year_of_service": agg["gross"] / years if years else float("nan"),
        "avg_participant_salary": avg_sal,
        "as_pct_of_salary": (agg["gross"] / years) / avg_sal if years and avg_sal else float("nan"),
    }


def plan_richness_ratio():
    """Hazardous-duty vs State Employee total normal cost, from the valuation (p.18)."""
    return {"state_employees_total_nc": 0.0873, "spors_total_nc": 0.1837,
            "valors_total_nc": 0.1430,
            "weighted_hazardous_total_nc": (0.1837 * IN.SPORS_ACTIVES["value"] +
                                            0.1430 * IN.VALORS_ACTIVES["value"]) /
                                           (IN.SPORS_ACTIVES["value"] + IN.VALORS_ACTIVES["value"])}


def report():
    b = sb419_benchmark()
    m = model_cost_per_year()
    rich = plan_richness_ratio()
    scale = rich["weighted_hazardous_total_nc"] / rich["state_employees_total_nc"]
    adjusted_benchmark_pct = b["implied_cost_as_pct_of_salary"] / scale
    return {"benchmark": b, "model": m, "richness": rich,
            "hazardous_to_state_richness_ratio": scale,
            "benchmark_adjusted_to_state_pct_of_salary": adjusted_benchmark_pct,
            "model_pct_of_salary": m["as_pct_of_salary"],
            "ratio_model_over_adjusted_benchmark":
                m["as_pct_of_salary"] / adjusted_benchmark_pct if adjusted_benchmark_pct else None}


def all_ages_cost_per_year():
    """Same model, applied to the WHOLE active Plan 1 + Plan 2 population.

    SB 419 granted service to every active member, most of whom are far from retirement, so the
    like-for-like comparison with VRS's score is the model run over an all-ages population, not
    over the near-retirement Pathway A/B pool.
    """
    import scenarios as SC
    from pricing import Pricer
    PR = Pricer()
    parts = SC.build_participants("OPEN", 1.0, tiers=("plan1", "plan2"),
                                  age_skew=1.0, vet_qual=1.0, vet_share=1.0)
    gross, years, payroll, n = 0.0, 0.0, 0.0, 0.0
    for pt in parts:
        # retirement date held constant at first eligibility; no acceleration, like SB 419
        d = PR.design_cost(pt.profile, pt.years, 0.0, member_payment=0.0)
        gross += pt.weight * d["gross_liability_increase"]
        years += pt.weight * pt.years
        payroll += pt.weight * pt.profile.salary
        n += pt.weight
    return {"members": n, "years_granted": years,
            "gross_liability": gross,
            "gross_per_year_of_service": gross / years,
            "avg_salary": payroll / n,
            "as_pct_of_salary": (gross / years) / (payroll / n)}


def full_report():
    r = report()
    r["all_ages_model"] = all_ages_cost_per_year()
    r["ratio_all_ages_model_over_adjusted_benchmark"] = (
        r["all_ages_model"]["as_pct_of_salary"] / r["benchmark_adjusted_to_state_pct_of_salary"])
    return r


def benchmark_service_sensitivity(service_years=(8.0, 10.3, 13.0, 16.0)):
    """The SPORS/VaLORS average-service figure is NOT published in the valuation summary.

    The implied cost per year of service in the SB 419 benchmark is inversely proportional to it,
    so the sanity check is reported across a range rather than at a point.
    """
    import inputs as IN
    v = IN.SB419_CHECK["value"]
    n = IN.SPORS_ACTIVES["value"] + IN.VALORS_ACTIVES["value"]
    payroll = IN.SPORS_PAYROLL["value"] + IN.VALORS_PAYROLL["value"]
    avg_sal = payroll / n
    rich = plan_richness_ratio()
    scale = rich["weighted_hazardous_total_nc"] / rich["state_employees_total_nc"]
    out = {}
    for s in service_years:
        member_years = n * (s / 5.0)
        pct = (v["liability_increase"] / member_years) / avg_sal
        out[s] = {"implied_pct_of_salary": pct, "state_equivalent_pct": pct / scale}
    return out
