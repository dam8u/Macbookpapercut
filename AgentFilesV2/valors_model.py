"""VaLORS pre-score model — MOO-100 V2 annex.

Source of record: VRS Annual Actuarial Valuation, June 30, 2025.
  p. 49  Active Participant Detail (VaLORS 7,459 / $432,703,326 / avg $58,011 / avg age 39.6 / avg total svc 8.3)
  p. 54  Active Participants by Age and Total Service - Virginia Law Officers
  p. 16  Results Summary - Virginia Law Officers (UAAL, employer rate development)
  p. 18  Employer Contribution Rate Detail (VaLORS normal cost 9.30%, admin 0.26%, amortization 13.04%)
Retrieved 12 October 2026.

Method mirrors V2-fiscal-model.docx exactly. Only the plan changes.
"""

# ---------------------------------------------------------------- Stage A data
# p. 54 table. Service bands: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30+
SVC_BANDS = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30+"]
SVC_LO = {"0-4": 0.0, "5-9": 5.0, "10-14": 10.0, "15-19": 15.0,
          "20-24": 20.0, "25-29": 25.0, "30+": 30.0}
SVC_HI = {"0-4": 5.0, "5-9": 10.0, "10-14": 15.0, "15-19": 20.0,
          "20-24": 25.0, "25-29": 30.0, "30+": 40.0}

# age label -> (counts by service band, total count, total payroll)
VALORS = {
    "Under 20": ([82, 0, 0, 0, 0, 0, 0], 82, 3_974_979),
    "20-24":    ([802, 7, 0, 0, 0, 0, 0], 809, 40_113_816),
    "25-29":    ([887, 181, 1, 0, 0, 0, 0], 1069, 56_162_653),
    "30-34":    ([680, 338, 78, 0, 0, 0, 0], 1096, 60_747_100),
    "35-39":    ([503, 256, 162, 58, 2, 0, 0], 981, 57_341_458),
    "40-44":    ([373, 163, 111, 190, 41, 1, 0], 879, 53_383_777),
    "45-49":    ([269, 151, 106, 135, 131, 74, 3], 869, 54_017_228),
    "50-54":    ([198, 99, 109, 141, 110, 64, 5], 726, 46_464_231),
    "55-59":    ([147, 92, 72, 102, 77, 26, 23], 539, 34_490_504),
    "60":       ([20, 22, 10, 20, 12, 4, 7], 95, 5_871_985),
    "61":       ([14, 12, 14, 12, 17, 7, 4], 80, 4_958_375),
    "62":       ([23, 6, 5, 13, 6, 4, 2], 59, 3_832_639),
    "63":       ([6, 5, 6, 13, 5, 10, 5], 50, 3_218_482),
    "64":       ([10, 9, 5, 7, 1, 5, 3], 40, 2_618_079),
    "65":       ([5, 4, 4, 4, 3, 1, 0], 21, 1_234_247),
    "66":       ([6, 1, 2, 6, 1, 5, 1], 22, 1_311_091),
    "67":       ([4, 1, 1, 2, 1, 0, 2], 11, 692_761),
    "68":       ([1, 1, 1, 1, 0, 3, 2], 9, 675_209),
    "69":       ([2, 1, 1, 0, 0, 1, 2], 7, 474_363),
    "70 & Over":([3, 2, 1, 0, 1, 4, 4], 15, 1_120_351),
}
AGE_LO = {"Under 20": 18, "20-24": 20, "25-29": 25, "30-34": 30, "35-39": 35,
          "40-44": 40, "45-49": 45, "50-54": 50, "55-59": 55, "60": 60, "61": 61,
          "62": 62, "63": 63, "64": 64, "65": 65, "66": 66, "67": 67, "68": 68,
          "69": 69, "70 & Over": 70}

TOTAL_N = sum(v[1] for v in VALORS.values())
TOTAL_PAY = sum(v[2] for v in VALORS.values())
assert TOTAL_N == 7459, TOTAL_N
# Published total is $432,703,326; the age rows sum to $432,703,328. A $2
# rounding difference in VRS's own table, carried forward rather than forced.
assert abs(TOTAL_PAY - 432_703_326) <= 5, TOTAL_PAY
for age, (counts, n, pay) in VALORS.items():
    assert sum(counts) == n, (age, sum(counts), n)
_COLS = [4035, 1351, 689, 704, 408, 209, 63]
for j, b in enumerate(SVC_BANDS):
    got = sum(v[0][j] for v in VALORS.values())
    assert got == _COLS[j], (b, got, _COLS[j])

def row_salary(age):
    c, n, pay = VALORS[age]
    return pay / n if n else 0.0

# ------------------------------------------------- Stage A: plan tier proxy
# Hazardous duty positions are NOT eligible for the Hybrid plan. A VaLORS member
# whose membership date is on or after 1 July 2010 is in Plan 2 regardless of
# whether it is after 31 December 2013. So the tier boundary is a single cut:
#   Plan 1  = hired before 1 July 2010  -> total service >= 15.0 yr at 30 Jun 2025
#   Plan 2  = everyone else
# 15.0 falls exactly on a published band boundary, so no band has to be split.
def tier_split(boundary=15.0):
    p1 = p2 = 0
    p1_pay = p2_pay = 0.0
    for age, (counts, n, pay) in VALORS.items():
        s = row_salary(age)
        for b, c in zip(SVC_BANDS, counts):
            if not c:
                continue
            lo, hi = SVC_LO[b], SVC_HI[b]
            if lo >= boundary:
                frac1 = 1.0
            elif hi <= boundary:
                frac1 = 0.0
            else:
                frac1 = (hi - boundary) / (hi - lo)
            p1 += c * frac1
            p1_pay += c * frac1 * s
            p2 += c * (1 - frac1)
            p2_pay += c * (1 - frac1) * s
    return p1, p1_pay / p1 if p1 else 0, p2, p2_pay / p2 if p2 else 0

# ----------------------------------------- Stage B: who each pathway reaches
# VaLORS unreduced service retirement eligibility (Plan 1 and Plan 2, identical):
#   age 60 with at least 5 years of service credit, OR
#   age 50 with at least 25 years of service credit.
#   -- VaLORS Plan 1 Overview and Plan 2 Overview, 04-2026; Hazardous Duty
#      Benefits FAQ for Members, April 2026.
PURCHASE_MAX_YR = 4.0   # 48-month active-duty maximum, unchanged by G6

def eligible_now(age_lo, svc):
    return (age_lo >= 60 and svc >= 5.0) or (age_lo >= 50 and svc >= 25.0)

def cohorts(allow_vesting_route=False, boundary=15.0):
    """Returns (incentive, bridge) each as dict with n, salary, p1, p2."""
    inc = {"n": 0.0, "pay": 0.0, "p1": 0.0, "p2": 0.0}
    br  = {"n": 0.0, "pay": 0.0, "p1": 0.0, "p2": 0.0, "months": 0.0}
    for age, (counts, n, pay) in VALORS.items():
        a = AGE_LO[age]
        s = row_salary(age)
        for b, c in zip(SVC_BANDS, counts):
            if not c:
                continue
            lo, hi = SVC_LO[b], SVC_HI[b]
            width = hi - lo
            # ---- already eligible
            if a >= 60:
                thr = 5.0
            elif a >= 50:
                thr = 25.0
            else:
                thr = None
            if thr is not None:
                f_elig = min(1.0, max(0.0, (hi - thr) / width))
            else:
                f_elig = 0.0
            # ---- bridgeable: not eligible, but reaches threshold with <=48 months
            if thr is None:
                f_br = 0.0
            else:
                # service in [thr - 4, thr)
                lo_b, hi_b = max(lo, thr - PURCHASE_MAX_YR), min(hi, thr)
                f_br = max(0.0, (hi_b - lo_b) / width)
                if a >= 60 and not allow_vesting_route:
                    # The 60/5 rule is the hazardous-duty rule, and VRS requires
                    # 5 years of VaLORS/SPORS/enhanced hazardous-duty service to
                    # retire with hazardous duty benefits. Purchased military
                    # service does not supply that. Strict screen drops it.
                    f_br = 0.0
            # mean months still needed, for the bridgeable slice
            if f_br > 0:
                lo_b, hi_b = max(lo, thr - PURCHASE_MAX_YR), min(hi, thr)
                mean_need = thr - (lo_b + hi_b) / 2.0
            else:
                mean_need = 0.0
            p1f = 1.0 if lo >= boundary else (0.0 if hi <= boundary
                                              else (hi - boundary) / width)
            for d, f in ((inc, f_elig), (br, f_br)):
                if f <= 0:
                    continue
                d["n"] += c * f
                d["pay"] += c * f * s
                d["p1"] += c * f * p1f
                d["p2"] += c * f * (1 - p1f)
                if d is br:
                    d["months"] += c * f * mean_need * 12.0
    for d in (inc, br):
        d["salary"] = d["pay"] / d["n"] if d["n"] else 0.0
    br["avg_months"] = br["months"] / br["n"] if br["n"] else 0.0
    return inc, br

def roll_forward(years=2.0):
    """Mid-pilot view. Both screens above are 'eligible at 30 June 2025'. The
    pilot runs four years, so age and service both advance. Shift the table by
    `years` on both axes and recompute. Nothing leaves VaLORS in this view, so
    it is an upper bound on the dynamic effect, not a projection."""
    global VALORS, AGE_LO
    saved_v, saved_a = VALORS, AGE_LO
    newv, newa = {}, {}
    for age, (counts, n, pay) in saved_v.items():
        key = f"{age}+{years:g}"
        shifted = [0.0] * len(SVC_BANDS)
        for j, c in enumerate(counts):
            if not c:
                continue
            lo, hi = SVC_LO[SVC_BANDS[j]] + years, SVC_HI[SVC_BANDS[j]] + years
            for k, b2 in enumerate(SVC_BANDS):
                ov = max(0.0, min(hi, SVC_HI[b2]) - max(lo, SVC_LO[b2]))
                if ov > 0:
                    shifted[k] += c * ov / (hi - lo)
        newv[key] = (shifted, n, pay)
        newa[key] = saved_a[age] + years
    VALORS, AGE_LO = newv, newa
    try:
        return cohorts()
    finally:
        VALORS, AGE_LO = saved_v, saved_a

# ----------------------------------------------------- Stage C/D/E: the funnel
ANC = {"p1": 0.2378, "p2": 0.1915}       # VaLORS / hazardous duty, eff. 1 Jul 2025
ANC_STATE = {"p1": 0.1250, "p2": 0.1074}  # non-hazardous, for the multiple
INCENTIVE_YEARS = 1.0                     # G3 / G18 cap

def funnel(vet=0.08, qual=0.50, takeup=0.12, strict=True):
    inc, br = cohorts(allow_vesting_route=not strict)
    pool = inc["n"] + br["n"]
    parts = pool * vet * qual * takeup
    inc_p = inc["n"] / pool * parts
    br_p = br["n"] / pool * parts
    # member payments
    def pay(d, years, n_parts):
        if d["n"] == 0:
            return 0.0
        f1 = d["p1"] / d["n"]
        rate = f1 * ANC["p1"] + (1 - f1) * ANC["p2"]
        return n_parts * years * rate * d["salary"]
    m_inc = pay(inc, INCENTIVE_YEARS, inc_p)
    m_br = pay(br, br["avg_months"] / 12.0, br_p)
    return {
        "pool": pool, "inc_pool": inc["n"], "br_pool": br["n"],
        "participants": parts, "inc_parts": inc_p, "br_parts": br_p,
        "member_payments": m_inc + m_br, "m_inc": m_inc, "m_br": m_br,
        "inc_salary": inc["salary"], "br_salary": br["salary"],
        "br_months": br["avg_months"],
    }

# ------------------------------------------------- Ledger 2: workforce (VaLORS)
# p.18: employer normal cost 9.30%, admin 0.26%, amortization 13.04% (NOT a
# saving - it is a charge against a fixed $717.570M UAAL), FICA 7.65%.
VALORS_SCALABLE = 1 + 0.0930 + 0.0026 + 0.0765
VALORS_AMORT = 0.1304

def workforce(n_retire, salary, replace=0.85, not_refilled=0.03):
    unfilled = n_retire * not_refilled
    refilled = n_retire - unfilled
    s_unfilled = unfilled * salary * VALORS_SCALABLE
    s_compress = refilled * salary * (1 - replace) * VALORS_SCALABLE
    amort_lost = (unfilled * salary + refilled * salary * (1 - replace)) * VALORS_AMORT
    return {"unfilled": s_unfilled, "compress": s_compress,
            "total": s_unfilled + s_compress, "amort_lost": amort_lost}


if __name__ == "__main__":
    p1, s1, p2, s2 = tier_split()
    print(f"TIER SPLIT  Plan 1 {p1:,.0f} (${s1:,.0f})  Plan 2 {p2:,.0f} (${s2:,.0f})"
          f"  total {p1+p2:,.0f}")
    for strict in (True, False):
        inc, br = cohorts(allow_vesting_route=not strict)
        tag = "STRICT" if strict else "PERMISSIVE"
        print(f"\n{tag}")
        print(f"  Incentive pool {inc['n']:,.1f}  avg sal ${inc['salary']:,.0f}"
              f"  P1 {inc['p1']:,.1f} / P2 {inc['p2']:,.1f}")
        print(f"  Bridge    pool {br['n']:,.1f}  avg sal ${br['salary']:,.0f}"
              f"  P1 {br['p1']:,.1f} / P2 {br['p2']:,.1f}"
              f"  avg months needed {br['avg_months']:.1f}")
    for y in (2.0, 4.0):
        i2, b2 = roll_forward(y)
        print(f"\nROLL-FORWARD +{y:g} yr  Incentive {i2['n']:,.0f}  "
              f"Bridge {b2['n']:,.0f}  combined {i2['n']+b2['n']:,.0f}")

    print("\nFUNNEL, same dials as the State Employees model")
    for name, v, q, t in (("Low", 0.06, 0.35, 0.05), ("Mid", 0.08, 0.50, 0.12),
                          ("High", 0.10, 0.65, 0.25)):
        r = funnel(v, q, t)
        print(f"  {name:5s} vet {v:.0%} qual {q:.0%} takeup {t:.0%} -> "
              f"{r['participants']:.1f} ({r['inc_parts']:.1f} inc / "
              f"{r['br_parts']:.1f} br)  member pays ${r['member_payments']:,.0f}")
    print("\nTAKE-UP ONLY (vet 8%, qual 50%)")
    for t in (0.05, 0.12, 0.25):
        r = funnel(0.08, 0.50, t)
        print(f"  {t:.0%}: {r['participants']:.1f}  inc {r['inc_parts']:.1f}"
              f"  br {r['br_parts']:.1f}  pays ${r['member_payments']:,.0f}")
        w = workforce(r['participants'],
                      (r['inc_parts'] * r['inc_salary'] + r['br_parts'] * r['br_salary'])
                      / r['participants'])
        print(f"        workforce ${w['total']:,.0f}/yr  (unfilled ${w['unfilled']:,.0f}"
              f" + compression ${w['compress']:,.0f})  amort lost ${w['amort_lost']:,.0f}")
