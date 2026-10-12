"""Part 5 - one-at-a-time tornado on the net cost of S1 as drafted."""
import copy
import inputs as IN
import mortality, pricing, scenarios, results


def _reload_chain():
    """Re-instantiate the pricer so a changed discount-rate input is picked up."""
    import importlib
    importlib.reload(mortality)
    importlib.reload(pricing)
    importlib.reload(scenarios)
    importlib.reload(results)
    return results


def run_tornado(scenario="S1"):
    base = results.net_state_cost(scenario=scenario)["net_state_cost_pv"]

    drivers = []

    def add(name, low_setter, high_setter, low_label, high_label):
        drivers.append((name, low_setter, high_setter, low_label, high_label))

    # participation
    add("Participation (take-up)",
        lambda: dict(level="low"), lambda: dict(level="high"),
        "low (15% / 10%)", "high (50% / 40%)")
    # months of acceleration
    add("Months of retirement acceleration",
        lambda: dict(workforce_level="conservative"), lambda: dict(workforce_level="optimistic"),
        "2 months", "14 months")
    # replacement salary differential (held independent of months)
    add("Replacement salary differential",
        lambda: dict(overrides={"differential": 0.08}),
        lambda: dict(overrides={"differential": 0.30}),
        "8% below incumbent", "30% below incumbent")
    # average purchased months
    add("Average purchased months",
        lambda: dict(overrides={"months_available": 24}),
        lambda: dict(overrides={"months_available": 48}),
        "24 months", "48 months")
    # veteran funnel
    add("Veteran age/service skew",
        lambda: dict(overrides={"age_skew": 1.0}),
        lambda: dict(overrides={"age_skew": 2.0}),
        "1.0x (= 6% share)", "2.0x (= 12% share)")
    add("Qualifying-service share",
        lambda: dict(overrides={"vet_qual": 0.40}),
        lambda: dict(overrides={"vet_qual": 0.75}),
        "40%", "75%")
    # friction treatment
    add("Recruitment/ramp treatment",
        lambda: dict(friction="charged"), lambda: dict(friction="timing_only"),
        "charged in full", "timing shift only")

    rows = []
    for name, lo, hi, lol, hil in drivers:
        v_lo = results.net_state_cost(scenario=scenario, **lo())["net_state_cost_pv"]
        v_hi = results.net_state_cost(scenario=scenario, **hi())["net_state_cost_pv"]
        rows.append({"driver": name, "low_label": lol, "high_label": hil,
                     "low": v_lo, "high": v_hi, "base": base,
                     "swing": abs(v_hi - v_lo),
                     "pct_swing_vs_base": 100 * abs(v_hi - v_lo) / abs(base) if base else float("nan")})

    # discount rate needs the input mutated and the chain reloaded
    for lo_rate, hi_rate in [(0.0600, 0.0750)]:
        vals = {}
        orig = IN.DISCOUNT_RATE["value"]
        for tag, rate in (("low", lo_rate), ("high", hi_rate)):
            IN.DISCOUNT_RATE["value"] = rate
            R = _reload_chain()
            vals[tag] = R.net_state_cost(scenario=scenario)["net_state_cost_pv"]
        IN.DISCOUNT_RATE["value"] = orig
        _reload_chain()
        # NOTE: a lower discount rate RAISES the liability, so "low rate" is the high-cost end
        rows.append({"driver": "Discount rate", "low_label": "7.50%", "high_label": "6.00%",
                     "low": vals["high"], "high": vals["low"], "base": base,
                     "swing": abs(vals["low"] - vals["high"]),
                     "pct_swing_vs_base": 100 * abs(vals["low"] - vals["high"]) / abs(base) if base else float("nan")})

    rows.sort(key=lambda r: -r["swing"])
    return base, rows


def ten_percent_test(scenario="S1"):
    """Role standard: flag any input where a 10% move swings the answer by more than 25%."""
    base = results.net_state_cost(scenario=scenario)["net_state_cost_pv"]
    out = []

    def rec(name, val, detail=""):
        out.append({"input": name, "net_cost_at_+10pct": val,
                    "pct_change_in_answer": 100 * (val - base) / base,
                    "detail": detail})

    tA = IN.TAKEUP_PATHWAY_A["value"]["central"]
    tB = IN.TAKEUP_PATHWAY_B["value"]["central"]
    rec("Take-up rate", results.net_state_cost(
        scenario=scenario, overrides={"takeup_A": tA * 1.1, "takeup_B": tB * 1.1})["net_state_cost_pv"],
        "0.30/0.22 -> 0.33/0.242")
    rec("Months of acceleration", results.net_state_cost(
        scenario=scenario, months_accel=IN.MONTHS_ACCELERATION["value"]["central"] * 1.1
        )["net_state_cost_pv"], "6.0 -> 6.6 months")
    rec("Replacement differential", results.net_state_cost(
        scenario=scenario,
        overrides={"differential": IN.REPLACEMENT_DIFFERENTIAL["value"]["central"] * 1.1}
        )["net_state_cost_pv"], "18% -> 19.8%")
    rec("Veteran age/service skew", results.net_state_cost(
        scenario=scenario, overrides={"age_skew": IN.VETERAN_AGE_SKEW["value"] * 1.1}
        )["net_state_cost_pv"], "1.50 -> 1.65")
    rec("Qualifying-service share", results.net_state_cost(
        scenario=scenario, overrides={"vet_qual": IN.QUALIFYING_SERVICE_SHARE["value"] * 1.1}
        )["net_state_cost_pv"], "60% -> 66%")

    # discount rate needs the chain reloaded
    orig = IN.DISCOUNT_RATE["value"]
    IN.DISCOUNT_RATE["value"] = orig * 1.1
    R = _reload_chain()
    v = R.net_state_cost(scenario=scenario)["net_state_cost_pv"]
    IN.DISCOUNT_RATE["value"] = orig
    _reload_chain()
    out.append({"input": "Discount rate", "net_cost_at_+10pct": v,
                "pct_change_in_answer": 100 * (v - base) / base, "detail": "6.75% -> 7.425%"})

    out.sort(key=lambda r: -abs(r["pct_change_in_answer"]))
    return base, out
