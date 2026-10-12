"""
Affected population: from the VRS age x service table to a count of likely participants.

Plan tier is inferred from TOTAL SERVICE as of 6/30/2025, because VRS does not publish the
age x service table split by tier:
    Plan 1  = membership before 7/1/2010 and vested by 1/1/2013  -> service >= ~15.0 years
    Plan 2  = membership 7/1/2010 - 12/31/2013                   -> service ~11.5 to 15.0 years
    Hybrid  = membership on/after 1/1/2014                       -> service < ~11.5 years
Direction of error: the table's "total service" includes purchased and prior service, so a few
members with long total service have a later membership date and are actually Plan 2 or Hybrid.
That makes the Plan 1 counts here a slight OVERSTATEMENT.

STRUCTURAL CONSEQUENCE, and it is a finding in its own right: every State Employee with 25+ years
of total service on 6/30/2025 has a pre-2000 membership date and is therefore Plan 1.  The most
service any Plan 2 member can have by the end of a FY2028-FY2031 pilot is roughly 15 + 6 = 21
years.  Pathway A (buy the months needed to reach the 30-year unreduced threshold) is therefore an
effectively Plan 1-only programme for the whole pilot, and S6 (extend to Hybrid) reaches a
population that is further still from any unreduced threshold.
"""
import inputs as IN

T = IN.AGE_SERVICE_TABLE["value"]
BANDS = IN.SERVICE_BANDS["value"]
BAND_IX = {b: i for i, b in enumerate(BANDS)}

AGE_MID = {"Under 20": 19, "20-24": 22, "25-29": 27, "30-34": 32, "35-39": 37, "40-44": 42,
           "45-49": 47, "50-54": 52, "55-59": 57, "60": 60, "61": 61, "62": 62, "63": 63,
           "64": 64, "65": 65, "66": 66, "67": 67, "68": 68, "69": 69, "70+": 72}
SVC_MID = {"0-4": 2.5, "5-9": 7.0, "10-14": 12.0, "15-19": 17.0, "20-24": 22.0,
           "25-29": 27.0, "30+": 32.0}


def cells():
    """Yield (age_label, svc_label, age_mid, svc_mid, count, age_band_avg_salary)."""
    for a, row in T.items():
        avg_sal = row[8] / row[7] if row[7] else 0.0
        for b in BANDS:
            yield a, b, AGE_MID[a], SVC_MID[b], row[BAND_IX[b]], avg_sal


def tier(svc_mid):
    if svc_mid >= 15.0:
        return "plan1"
    if svc_mid >= 11.5:
        return "plan2"
    return "hybrid"


def cohort(min_age=None, max_age=None, svc_bands=None, tiers=None):
    """Count and average salary for a slice of the table."""
    n, pay = 0, 0.0
    for a, b, am, sm, c, sal in cells():
        if c == 0:
            continue
        if min_age is not None and am < min_age:
            continue
        if max_age is not None and am > max_age:
            continue
        if svc_bands is not None and b not in svc_bands:
            continue
        if tiers is not None and tier(sm) not in tiers:
            continue
        n += c
        pay += c * sal
    return {"count": n, "avg_age_band_salary": (pay / n if n else 0.0)}


# ---------------------------------------------------------------------------------
# Eligibility pools, as drafted
# ---------------------------------------------------------------------------------
def pool_pathway_A():
    """Plan 1, 25-29 years of service, age 50+ : reaching 30 years makes them unreduced-eligible."""
    return cohort(min_age=50, svc_bands=["25-29"], tiers=["plan1"])


def pool_pathway_A_within12mo():
    """Age 45-49 with 25-29 years: become age-eligible soon; only ~1/5 of the band turns 50 within 12 months."""
    c = cohort(min_age=45, max_age=49, svc_bands=["25-29"], tiers=["plan1"])
    c["count"] = round(c["count"] / 5.0)
    c["note"] = "45-49 band scaled by 1/5 to approximate those turning 50 within 12 months"
    return c


def pool_pathway_B():
    """Plan 1, already unreduced-eligible: age 50+ with 30+ years, or age 65+ with 5+ years."""
    a = cohort(min_age=50, svc_bands=["30+"], tiers=["plan1"])
    b = cohort(min_age=65, svc_bands=["15-19", "20-24", "25-29"], tiers=["plan1"])
    n = a["count"] + b["count"]
    sal = (a["count"] * a["avg_age_band_salary"] + b["count"] * b["avg_age_band_salary"]) / n
    return {"count": n, "avg_age_band_salary": sal,
            "detail": {"age50+_30yrs": a["count"], "age65+_5to29yrs_plan1": b["count"]}}


def pool_s5_reopened_window():
    """S5: all active Plan 1 and Plan 2 members, any age, no retirement condition."""
    return cohort(tiers=["plan1", "plan2"])


def pool_s6_hybrid_added():
    return cohort(tiers=["hybrid"])


def veteran_filter(count, age_skew=None, qual=None, vet_share=None):
    """Apply the veteran funnel: workforce veteran share x age/service skew x qualifying-service share."""
    vs = IN.VETERAN_SHARE_WORKFORCE["value"] if vet_share is None else vet_share
    sk = IN.VETERAN_AGE_SKEW["value"] if age_skew is None else age_skew
    q = IN.QUALIFYING_SERVICE_SHARE["value"] if qual is None else qual
    return count * vs * sk * q


def summary():
    out = {}
    out["plan1_actives"] = cohort(tiers=["plan1"])
    out["plan2_actives"] = cohort(tiers=["plan2"])
    out["hybrid_actives"] = cohort(tiers=["hybrid"])
    out["svc25plus_all_ages"] = cohort(svc_bands=["25-29", "30+"])
    out["svc25plus_age50plus"] = cohort(min_age=50, svc_bands=["25-29", "30+"])
    out["pathway_A"] = pool_pathway_A()
    out["pathway_A_within12mo"] = pool_pathway_A_within12mo()
    out["pathway_B"] = pool_pathway_B()
    out["s5_pool"] = pool_s5_reopened_window()
    out["s6_pool"] = pool_s6_hybrid_added()
    return out


if __name__ == "__main__":
    s = summary()
    print("STATE EMPLOYEE PLAN, 6/30/2025 (VRS valuation p.50), tier inferred from total service\n")
    for k in ("plan1_actives", "plan2_actives", "hybrid_actives"):
        print(f"  {k:28s} {s[k]['count']:>7,}   avg age-band salary ${s[k]['avg_age_band_salary']:,.0f}")
    print(f"\n  {'25+ yrs service, all ages':28s} {s['svc25plus_all_ages']['count']:>7,}")
    print(f"  {'25+ yrs service, age 50+':28s} {s['svc25plus_age50plus']['count']:>7,}")
    print("\nELIGIBILITY POOLS (before the veteran funnel):")
    print(f"  Pathway A (P1, 25-29 yrs, age 50+)        {s['pathway_A']['count']:>7,}")
    print(f"  Pathway A, turning 50 within 12 months    {s['pathway_A_within12mo']['count']:>7,}")
    print(f"  Pathway B (P1, already unreduced-eligible) {s['pathway_B']['count']:>6,}   {s['pathway_B']['detail']}")
    print(f"  S5 reopened window (all P1 + P2 actives)  {s['s5_pool']['count']:>7,}")
    print(f"  S6 adds Hybrid actives                    {s['s6_pool']['count']:>7,}")
    print("\nVETERAN FUNNEL (6% workforce share x 1.5 age/service skew x 60% qualifying service = 5.4%):")
    for k in ("pathway_A", "pathway_A_within12mo", "pathway_B", "s5_pool", "s6_pool"):
        print(f"  {k:28s} {s[k]['count']:>7,} -> {veteran_filter(s[k]['count']):>8,.0f} veteran-eligible")
