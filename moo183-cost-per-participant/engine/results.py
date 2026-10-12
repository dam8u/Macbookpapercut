"""Assemble the full result set: pension cost, workforce offset, fiscal-year layout, break-even."""
import inputs as IN
import scenarios as SC
import workforce as W


def net_state_cost(level="central", overrides=None, friction="charged",
                   scenario="S1", months_accel=None, workforce_level="central"):
    """One scalar: PV net cost to the Commonwealth of `scenario` over the pilot.

    = net incremental pension liability (gross liability less member payments)
      + VRS one-time implementation cost
      - aggregate net workforce effect
    """
    o = dict(overrides or {})
    ma = IN.MONTHS_ACCELERATION["value"][workforce_level] if months_accel is None else months_accel
    agg, parts = SC.run_scenario(scenario, level, months_accel=ma, overrides=o)

    pension_net = agg["net"]
    n = agg["n"]
    avg_sal = (agg["payroll"] / n) if n else 0.0
    diff = o.get("differential", IN.REPLACEMENT_DIFFERENTIAL["value"][workforce_level])
    wf_per = W.per_participant(avg_sal, ma, diff,
                               timing_shift_only=(friction == "timing_only"))
    wf_total = wf_per["net_workforce_effect"] * n
    impl = o.get("implementation", IN.VRS_IMPLEMENTATION_COST["value"]["central"])

    return {
        "scenario": scenario, "level": level, "friction": friction,
        "participants": n,
        "avg_participant_salary": avg_sal,
        "gross_liability": agg["gross"],
        "member_payments": agg["paid"],
        "pension_net_liability": pension_net,
        "pension_net_per_participant": (pension_net / n) if n else 0.0,
        "service_credit_component": agg["svc"],
        "early_retirement_subsidy_component": agg["accel"],
        "workforce_net_per_participant": wf_per["net_workforce_effect"],
        "workforce_net_total": wf_total,
        "trust_tier_mix_total": wf_per["trust_tier_mix_effect"] * n,
        "vrs_implementation": impl,
        "net_state_cost_pv": pension_net + impl - wf_total,
        "gf_share": IN.GF_SHARE["value"],
        "net_gf_cost_pv": (pension_net + impl - wf_total) * IN.GF_SHARE["value"],
        "_agg": agg,
    }


def fiscal_layout(pension_net_liability, impl=None):
    """Pilot-year liability layers, 20-year amortisation, and GF/NGF annual cost by FY."""
    impl = IN.VRS_IMPLEMENTATION_COST["value"]["central"] if impl is None else impl
    layers, annual = SC.pilot_layout(pension_net_liability, 0.0)
    gf = IN.GF_SHARE["value"]
    rows = []
    fys = sorted(set(list(annual) + IN.PILOT_FY["value"]))
    for fy in fys:
        amort = annual.get(fy, 0.0)
        one_off = impl if fy == IN.PILOT_FY["value"][0] else 0.0
        rows.append({"FY": fy, "amortisation_total": amort,
                     "amortisation_GF": amort * gf, "amortisation_NGF": amort * (1 - gf),
                     "vrs_implementation_NGF": one_off,
                     "total": amort + one_off,
                     "total_GF": amort * gf, "total_NGF": amort * (1 - gf) + one_off})
    total_20yr = sum(r["amortisation_total"] for r in rows)
    return rows, layers, total_20yr
