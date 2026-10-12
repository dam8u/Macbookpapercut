"""
MOO-38: VRS's PUBLISHED fixed-rate early-retirement reduction factors (ERFs).

This module replaces the derived actuarial-equivalence factor MOO-31 used in s9.py.  VRS does
publish its factors, and it does not use actuarial equivalence.

PRIMARY SOURCES (both retrieved and text-extracted 2026-10-11; see README_MOO38.md)
--------------------------------------------------------------------------------------
[EM]  VRS Employer Manual, Service Retirement, July 2026.
      https://employers.varetire.org/media/shared/pdf/er-manual-service-retirement.pdf
      p.3  Unreduced Retirement:
             Plan 1          - "Age 65 with at least 5 years of service or Age 50 with at least
                                30 years of service"
             Plan 2/Hybrid   - "Age and service equal 90 or Normal Social Security retirement age
                                with at least 5 years of service"
      p.4  Reduced Retirement:
             Plan 1          - "Age 55 with at least 5 years or service or Age 50 with at least
                                10 years of service"
             Plan 2/Hybrid   - "Age 60 with at least 5 years of service."
                                >>> THERE IS NO 50/10 REDUCED RETIREMENT FOR PLAN 2 OR HYBRID. <<<
      p.4  "Reduction by Type":
             55/5  - "A 0.5% reduction is applied for the first 60 months, and 4/10 of 1% for any
                      additional months the member needs to meet age or service requirements for an
                      unreduced benefit."
             50/10 - "The amount determined based on service credit and average final compensation
                      (AFC), reduced by 0.5% for the first 60 months.  Plus 4/10 of 1% for any
                      additional months the member needs to meet age and service requirements for an
                      unreduced benefit.  Plus An additional reduction of 6/10 of 1% for each month
                      the member is younger than 55."
             60/5  - "The reduction is based on whether the member is closer to: Full Social
                      Security retirement age; or The first date on which the member would have
                      completed 30 years of service and the age plus service equal 90."

[BA]  VRS Benefits and Actuarial Committee, 17 June 2026, "Early Retirement Factors Study".
      https://www.varetire.org/media/members/pdf/board/materials/2026/bac-06-17-26.pdf
      p.14 "VRS currently uses fixed-rate reductions."
      p.15 "Fixed rate reduction factors often include a subsidy or provide a slightly more
            valuable benefit than a true actuarial equivalent, meaning the employer covers some of
            the cost of the earlier retirement."
      p.16 "Flat percentage reduction from Normal Retirement age to age of early commencement."
      p.19 Plan 1 method, verbatim and load-bearing:
             "Reduction of 0.5% for each month prior to unreduced retirement age for the first 60
              months, 0.4% reduction for the NEXT 60 MONTHS."
             "From age 55: 0.6% reduction for each month prior to age 55 back to age 50."
           + the 16-row Plan 1 general-employee factor table with VRS's own A.E. and subsidy.
      p.20 Enhanced Hazardous Duty, 11 rows (validation only; out of scope for a State pilot).
      p.21 Plan 2 & Hybrid method ("0.4% reduction THEREAFTER") + the 8-row table.

TWO AMBIGUITIES, AND WHAT THE TABLES DO AND DO NOT SETTLE
--------------------------------------------------------------------------------------
A. ORDER OF OPERATIONS for the Plan 1 50/10 extra 6/10 of 1% (MOO-37 records-request question A2).
   SETTLED by [BA] p.19 against the Employer Manual read literally.  Two things fall out of the
   published table, and only one combination reproduces it:
     (i)  the 0.5%/0.4% ladder is CAPPED at 120 months ("the next 60 months"), so the deepest
          55/5-style reduction is 30% + 24% = 54%, i.e. a floor factor of 0.4600; and
     (ii) the 0.6%-per-month-under-55 term is MULTIPLICATIVE on that factor, not additive on the
          reduction.
   Age 54, unreduced age 65:   capped ladder 0.4600 x (1 - 12 x 0.006) = 0.42688 -> 0.4269  MATCHES
                               additive, uncapped: 1 - (0.30 + 0.288 + 0.072)  = 0.3400  FAILS
                               additive, capped:   1 - (0.54 + 0.072)          = 0.3880  FAILS
                               multiplicative, uncapped: 0.4120 x 0.928        = 0.3823  FAILS
   The published ages 50-54 factors fall on an exact straight line (constant -0.03312/yr =
   -0.4600 x 0.072), which is the multiplicative form and nothing else.  `composition="ba_2026"`
   is therefore the central case and `composition="manual_literal"` is kept only to price the
   alternative reading the Employer Manual text would support on its own.

B. WHETHER THE UNREDUCED AGE IS FOUND ON PROJECTED OR FROZEN SERVICE.  **NOT SETTLED** by either
   source, and for the S9 cohort it dominates A by an order of magnitude.  Every row of all three
   published tables sits on the diagonal service = age - 35 (Plan 1), service = 23 (Plan 2),
   service = age - 35 (Haz Duty), where the two readings give the SAME unreduced age, so the tables
   cannot discriminate.  The only explicit textual signal is the 60/5 rule's "the first date on
   which the member WOULD HAVE completed 30 years of service", which is projected.
     basis="projected" (CENTRAL) - the unreduced date is the first date the member WOULD have met
                                   the test had they kept working.  Plan 1: min(65, age at 30 yrs).
     basis="frozen"              - service stops at retirement, so a Plan 1 member with under 30
                                   years can only ever satisfy 65/5, and the unreduced age is 65.
   For a Plan 1 member aged 52 with 27 years the factor is 0.6429 projected and 0.3606 frozen.
   This is raised as a NEW open item for MOO-37; it is not resolved here and both are priced.

CONVENTION NOTE.  basis="projected" reproduces exactly the unreduced-age arithmetic MOO-31 already
used (s9.unreduced_age_frozen, despite its name, projected service).  Choosing it as central keeps
this reprice to ONE change - the factor - so the move in the headline is attributable.
"""
import inputs as IN

# ---- the published rates, from [EM] p.4 and [BA] pp.19-21 -------------------------------
TIER1_RATE = IN.ERF_TIER1_RATE["value"]              # 0.005 per month, first 60 months
TIER2_RATE = IN.ERF_TIER2_RATE["value"]              # 0.004 per month
TIER1_MONTHS = IN.ERF_TIER1_MONTHS["value"]          # 60
TIER2_MONTHS = IN.ERF_TIER2_MONTHS["value"]          # 60  ("the next 60 months")
SUB55_RATE = IN.ERF_SUB55_RATE["value"]              # 0.006 per month under age 55, Plan 1 50/10
SSNRA = IN.SSNRA["value"]                            # 67 for anyone born 1960 or later


# ---------------------------------------------------------------------------- eligibility
def retirement_eligible(plan, retire_age, service):
    """Is the member eligible to commence ANY service-retirement benefit at `retire_age`?

    [EM] p.3-4.  Returns (eligible, provision).  Disability retirement is out of scope.
    """
    if plan == "plan1":
        if retire_age >= 65.0 and service >= 5.0:
            return True, "unreduced 65/5"
        if retire_age >= 50.0 and service >= 30.0:
            return True, "unreduced 50/30"
        if retire_age >= 55.0 and service >= 5.0:
            return True, "reduced 55/5"
        if retire_age >= 50.0 and service >= 10.0:
            return True, "reduced 50/10"
        return False, "not eligible"
    # Plan 2 and Hybrid
    if retire_age >= SSNRA and service >= 5.0:
        return True, "unreduced SSNRA/5"
    if retire_age + service >= 90.0:
        return True, "unreduced rule of 90"
    if retire_age >= 60.0 and service >= 5.0:
        return True, "reduced 60/5"
    return False, "not eligible"


def is_unreduced(plan, retire_age, service):
    ok, prov = retirement_eligible(plan, retire_age, service)
    return ok and prov.startswith("unreduced")


# ------------------------------------------------------------------ the unreduced-age target
def unreduced_age(plan, retire_age, service, basis=None):
    """The age the ERF measures back FROM.  See ambiguity B in the module docstring."""
    basis = IN.ERF_UNREDUCED_BASIS["value"] if basis is None else basis
    if is_unreduced(plan, retire_age, service):
        return retire_age

    if plan == "plan1":
        # min(age-65 date, 30-years-of-service date), the 30-year date floored at age 50
        if basis == "projected":
            at_30 = max(50.0, retire_age + max(0.0, 30.0 - service))
        elif basis == "frozen":
            at_30 = float("inf") if service < 30.0 else max(50.0, retire_age)
        else:
            raise ValueError(basis)
        return min(65.0, at_30)

    # Plan 2 / Hybrid: nearer of SSNRA, or the first date BOTH 30 yrs and age+service=90 hold
    if basis == "projected":
        t30 = max(0.0, 30.0 - service)                              # 1 yr of service per yr worked
        t90 = max(0.0, (90.0 - retire_age - service) / 2.0)         # age and service both +1
    elif basis == "frozen":
        t30 = float("inf") if service < 30.0 else 0.0
        t90 = max(0.0, 90.0 - retire_age - service)                 # age only
    else:
        raise ValueError(basis)
    return min(SSNRA, retire_age + max(t30, t90))


# --------------------------------------------------------------------------- hazardous duty
def unreduced_age_hazduty(retire_age, service):
    """Enhanced Hazardous Duty: unreduced at 60, or 50 with 25 years.  Validation only."""
    if retire_age >= 60.0 or (retire_age >= 50.0 and service >= 25.0):
        return retire_age
    return min(60.0, max(50.0, retire_age + max(0.0, 25.0 - service)))


# ----------------------------------------------------------------------------- the factor
def erf(plan, retire_age, service, basis=None, composition=None, hazduty=False):
    """VRS's published fixed-rate early-retirement reduction factor.

    plan        "plan1" | "plan2" | "hybrid"
    retire_age  age at commencement
    service     CREDITED service at commencement (years)
    basis       "projected" | "frozen"           - ambiguity B
    composition "ba_2026" | "manual_literal"     - ambiguity A
    """
    composition = IN.ERF_COMPOSITION["value"] if composition is None else composition

    U = unreduced_age_hazduty(retire_age, service) if hazduty \
        else unreduced_age(plan, retire_age, service, basis=basis)
    if U <= retire_age:
        return 1.0
    months = (U - retire_age) * 12.0

    t1 = min(months, TIER1_MONTHS)
    rest = max(0.0, months - TIER1_MONTHS)
    t2 = min(rest, TIER2_MONTHS) if composition == "ba_2026" else rest
    reduction = TIER1_RATE * t1 + TIER2_RATE * t2
    factor = 1.0 - reduction

    # the 50/10 extra: Plan 1 only, and only below age 55 ([EM] p.4; [BA] p.19 "back to age 50")
    sub55 = 0.0
    if plan == "plan1" and not hazduty and retire_age < 55.0:
        sub55 = min(60.0, (55.0 - retire_age) * 12.0)
    if sub55:
        if composition == "ba_2026":
            factor *= (1.0 - SUB55_RATE * sub55)        # multiplicative - reproduces [BA] p.19
        elif composition == "manual_literal":
            factor = 1.0 - reduction - SUB55_RATE * sub55
        else:
            raise ValueError(composition)
    return max(0.0, factor)


def detail(plan, retire_age, service, basis=None, composition=None, hazduty=False):
    U = unreduced_age_hazduty(retire_age, service) if hazduty \
        else unreduced_age(plan, retire_age, service, basis=basis)
    ok, prov = retirement_eligible(plan, retire_age, service)
    return {"plan": plan, "retire_age": retire_age, "service": service,
            "eligible": ok, "provision": prov,
            "unreduced_age": U, "months_early": max(0.0, (U - retire_age) * 12.0),
            "erf": erf(plan, retire_age, service, basis=basis, composition=composition,
                       hazduty=hazduty)}


# =========================================================================================
# VALIDATION against all 35 published rows.  Imported by moo38_main.py and run by __main__.
# =========================================================================================
# [BA] p.19 - Plan 1 general employees.  (age, service, ERF, VRS's A.E., VRS's subsidy)
# Ages 50-54 print no service in the slide; the service that puts the row on the published
# diagonal is age - 35, which is what is used here and what makes the unreduced age 65.
BA_P19_PLAN1 = [
    (65, 30, 1.0000, 1.0000, 0.0000), (64, 29, 0.9400, 0.9074, 0.0359),
    (63, 28, 0.8800, 0.8248, 0.0669), (62, 27, 0.8200, 0.7509, 0.0920),
    (61, 26, 0.7600, 0.6847, 0.1100), (60, 25, 0.7000, 0.6252, 0.1197),
    (59, 24, 0.6520, 0.5716, 0.1407), (58, 23, 0.6040, 0.5233, 0.1543),
    (57, 22, 0.5560, 0.4795, 0.1594), (56, 21, 0.5080, 0.4400, 0.1547),
    (55, 20, 0.4600, 0.4041, 0.1385), (54, 19, 0.4269, 0.3714, 0.1493),
    (53, 18, 0.3938, 0.3417, 0.1522), (52, 17, 0.3606, 0.3147, 0.1460),
    (51, 16, 0.3275, 0.2900, 0.1293), (50, 15, 0.2944, 0.2675, 0.1006),
]

# [BA] p.21 - Plan 2 & Hybrid, born 1960 or later.  Rule90 column = age + service, so service = 23.
BA_P21_PLAN2 = [
    (67, 1.0000, 1.0000, 0.0000), (66, 0.9400, 0.9045, 0.0393),
    (65, 0.8800, 0.8197, 0.0736), (64, 0.8200, 0.7443, 0.1017),
    (63, 0.7600, 0.6770, 0.1226), (62, 0.7000, 0.6167, 0.1350),
    (61, 0.6520, 0.5627, 0.1587), (60, 0.6040, 0.5141, 0.1748),
]
BA_P21_SERVICE = 23.0

# [BA] p.20 - Enhanced Hazardous Duty (age, service, ERF).  Independent check of the ladder.
BA_P20_HAZDUTY = [
    (60, 25, 1.0000), (59, 24, 0.9400), (58, 23, 0.8800), (57, 22, 0.8200),
    (56, 21, 0.7600), (55, 20, 0.7000), (54, 19, 0.6520), (53, 18, 0.6040),
    (52, 17, 0.5560), (51, 16, 0.5080), (50, 15, 0.4600),
]

TOL = 5e-5


def validate(basis="projected", composition="ba_2026", verbose=True):
    """Reproduce all 35 published rows.  Returns (n_rows, n_fail, rows)."""
    rows, fails = [], 0
    for age, svc, pub, ae, sub in BA_P19_PLAN1:
        got = erf("plan1", float(age), float(svc), basis=basis, composition=composition)
        bad = abs(got - pub) > TOL
        fails += bad
        rows.append(("[BA] p.19 Plan 1", age, svc, pub, got, bad))
    for age, pub, ae, sub in BA_P21_PLAN2:
        got = erf("plan2", float(age), BA_P21_SERVICE, basis=basis, composition=composition)
        bad = abs(got - pub) > TOL
        fails += bad
        rows.append(("[BA] p.21 Plan 2/Hybrid", age, BA_P21_SERVICE, pub, got, bad))
    for age, svc, pub in BA_P20_HAZDUTY:
        got = erf("plan1", float(age), float(svc), basis=basis, composition=composition,
                  hazduty=True)
        bad = abs(got - pub) > TOL
        fails += bad
        rows.append(("[BA] p.20 Enh. Haz Duty", age, svc, pub, got, bad))
    if verbose:
        print(f"    ERF implementation vs published tables  "
              f"(basis={basis}, composition={composition})")
        print(f"    {'table':26s} {'age':>4s} {'svc':>5s} {'published':>10s} {'model':>8s}  ok")
        for t, a, s, pub, got, bad in rows:
            print(f"    {t:26s} {a:>4} {s:>5.0f} {pub:>10.4f} {got:>8.4f}  "
                  f"{'FAIL' if bad else 'ok'}")
        print(f"    -> {len(rows) - fails}/{len(rows)} published rows reproduced exactly "
              f"(tolerance {TOL}).")
    return len(rows), fails, rows


def composition_comparison():
    """The age 50-54 Plan 1 rows under every candidate reading of the 50/10 rule (ambiguity A)."""
    out = []
    for age, svc, pub, _, _ in BA_P19_PLAN1:
        if age >= 55:
            continue
        U = 65.0
        m = (U - age) * 12.0
        capped = 1.0 - (TIER1_RATE * 60 + TIER2_RATE * 60)
        uncapped = 1.0 - (TIER1_RATE * 60 + TIER2_RATE * (m - 60))
        mu = (55.0 - age) * 12.0
        out.append({
            "age": age, "published": pub,
            "capped_multiplicative_BA": capped * (1 - SUB55_RATE * mu),
            "capped_additive": capped - SUB55_RATE * mu,
            "uncapped_multiplicative": uncapped * (1 - SUB55_RATE * mu),
            "uncapped_additive_EM_literal": uncapped - SUB55_RATE * mu,
        })
    return out


if __name__ == "__main__":
    validate()
    print()
    for r in composition_comparison():
        print("   ", r)
