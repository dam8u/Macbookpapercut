"""
MOO-7 — VRS Military Service Purchase: model inputs.
EVERY number in the model comes from this file. No magic numbers in the logic files.

Each input is a dict:
  value / unit / source / retrieved / note / direction_of_error
"source" = "PRIMARY: <url>"  -> published primary figure
           "DERIVED: <...>"  -> arithmetic on primary figures (shown)
           "JUDGMENT: <...>" -> analyst judgment, defensible range stated
Retrieval date for all web sources: 2026-10-11.
"""
RETRIEVED = "2026-10-11"

VRS_VAL = "https://employers.varetire.org/media/employers/pdf/financial-reporting/valuations/valuation-report-vrs.pdf"
VRS_PPS = "https://www.varetire.org/am/media/shared/pdf/publications/pps-rate-charts.pdf"
VRS_BAC = "https://www.varetire.org/media/members/pdf/board/materials/2025/bac-06-09-25.pdf"
VRS_EXP = "https://employers.varetire.org/media/shared/pdf/publications/vrs-experience-study.pdf"
VRS_HB1 = "https://www.varetire.org/media/shared/pdf/publications/handbook-plan-1.pdf"
VRS_HB2 = "https://www.varetire.org/media/shared/pdf/publications/handbook-plan-2.pdf"
VRS_ERM = "https://employers.varetire.org/media/shared/pdf/er-manual-purchase-of-prior-service-credit.pdf"
VRS_RATES = ("https://employers.varetire.org/employer-update/2025/november/"
             "board-certifies-fy-2027-2028-rates-for-statewide-plans-and-opebs.html")
DHRM_SFAC = "https://sfac.virginia.gov/pdf/General%20Gov/2025/01212025_No1_DHRM.pdf"
HAC_COMP = "https://hac.virginia.gov/subtopics/state-employees-and-operations/compensation/"
CODE_142 = "https://law.lis.virginia.gov/vacode/title51.1/chapter1/section51.1-142.2/"
SOA_PUB = "https://www.soa.org/globalassets/assets/files/resources/research-report/2019/pub-2010-mort-report.pdf"
FIS_SB419 = "https://lis.blob.core.windows.net/files/1098992.PDF"


def I(value, unit, source, note="", direction_of_error=""):
    return dict(value=value, unit=unit, source=source, note=note,
                direction_of_error=direction_of_error, retrieved=RETRIEVED)


# ----------------------------------------------------------------------------
# 1. VRS ACTUARIAL / ECONOMIC ASSUMPTIONS  (June 30, 2025 valuation)
# ----------------------------------------------------------------------------
DISCOUNT_RATE = I(0.0675, "per year", f"PRIMARY: {VRS_VAL} p.37 (and p.12 asset recon., 'Assumed Rate 6.75%')",
    "Investment return = discount rate. Also the statutory interest rate used for refunded-service purchases.",
    "Lower discount rate -> higher actuarial-equivalent price and higher plan cost. Dominant driver.")
INFLATION = I(0.0250, "per year", f"PRIMARY: {VRS_VAL} p.9 ('2.50% assumption' for Plan 1 COLA); 2020-24 experience study",
    "Long-term price inflation.", "")
PAYROLL_GROWTH = I(0.0300, "per year", f"PRIMARY: {VRS_EXP} (total payroll growth 3.00% for State Employees)",
    "Used for salary projection beyond 20 years of service (merit/longevity scale applies only to the first 20 "
    "years for non-judicial members) and for level-percent-of-pay amortization.",
    "Higher growth -> higher projected AFC -> higher plan cost and higher ANC price.")
COLA_PLAN1 = I(0.0250, "per year", f"PRIMARY: {VRS_VAL} p.9 ('actual COLA of 2.95% for Plan 1 recipients compared to a 2.50% assumption')",
    "Plan 1 COLA = first 3% of CPI-U + half of next 4%, max 5% (handbook p.57).",
    "Higher assumed COLA -> higher PV of benefit -> higher plan cost.")
COLA_PLAN2 = I(0.0225, "per year", f"PRIMARY: {VRS_VAL} p.9 ('actual COLA of 2.48% for Plan 2 / Hybrid recipients compared to a 2.25% assumption')",
    "Plan 2 COLA = first 2% of CPI-U + half of next 2%, max 3% (Plan 2 handbook p.57).", "")
AMORT_PERIOD = I(20, "years", f"PRIMARY: {VRS_VAL} p.19 ('2025 (Gain)/Loss ... 20 years')",
    "New gain/loss layers in the State Employee plan are amortized over a closed 20-year period, "
    "level percent of pay, with a timing adjustment factor of 1.018041.",
    "Shorter period -> higher annual GF cost, same total.")
AMORT_TIMING_ADJ = I(1.018041, "factor", f"PRIMARY: {VRS_VAL} p.18 footnote 1 ('Includes a timing adjustment factor of 1.018041')", "", "")

MORTALITY_BASIS = I("PubG-2010 amount-weighted General Healthy Retiree, generational, 75% of MP-2021; "
                    "State General post-retirement adjustment 100% of male table / 110% of female table",
    "table", f"PRIMARY: {VRS_EXP} pp. B-9 to B-10 (adjustment tables) and p.1753",
    "VRS does not publish the resulting q(x) vector. This model fits a Gompertz-Makeham law to the "
    "SOA-published PubG-2010 annuity values (see mortality.py) rather than guessing rates.",
    "Lighter mortality -> larger annuity factor -> higher plan cost.")

# ----------------------------------------------------------------------------
# 2. PLAN DESIGN (benefit formula / eligibility)
# ----------------------------------------------------------------------------
MULT_PLAN1 = I(0.017, "of AFC per year of service", f"PRIMARY: {VRS_HB1} p.18 ('Under VRS Plan 1, the retirement multiplier is 1.7%')", "", "")
MULT_HYBRID = I(0.0100, "of AFC per year of service (DB component)",
    "PRIMARY: https://www.varetire.org/media/shared/pdf/publications/hybrid-handbook.pdf",
    "Hybrid DB multiplier 1.00%; AFC = highest 60 consecutive months; unreduced at normal SSRA w/ 5 yrs "
    "or age + service = 90. The Hybrid DC component is unaffected by a service purchase.", "")
MULT_PLAN2 = I(0.0165, "of AFC per year of service", f"PRIMARY: {VRS_HB2} p.18 ('the retirement multiplier for service retirement is 1.65%')", "", "")
AFC_MONTHS_PLAN1 = I(36, "months", f"PRIMARY: {VRS_HB1} p.18", "Highest 36 consecutive months.", "")
AFC_MONTHS_PLAN2 = I(60, "months", f"PRIMARY: {VRS_HB2} p.18", "Highest 60 consecutive months.", "")
UNREDUCED_PLAN1 = I("age 65 w/ 5 yrs, or age 50 w/ 30 yrs", "rule", f"PRIMARY: {VRS_HB1} p.16", "", "")
UNREDUCED_PLAN2 = I("normal Social Security retirement age w/ 5 yrs, or age + service = 90 (Rule of 90)",
    "rule", f"PRIMARY: {VRS_HB2} p.16", "", "")
MAX_MILITARY_YEARS = I(4, "years", f"PRIMARY: {CODE_142}; {VRS_ERM} p.5",
    "Up to four years of prior active-duty U.S. military service; >=180 consecutive days; "
    "cannot qualify the member for a benefit from another retirement system (Reserve/Guard excepted); "
    "discharge not dishonorable.", "")
ANC_WINDOW_MONTHS = I(24, "months", f"PRIMARY: {CODE_142}; {VRS_BAC} p.7",
    "Approximate-normal-cost rate applies for 24 months after first date of hire in a covered position "
    "(or end of eligible leave); after that the price becomes actuarial equivalent cost.", "")

# ----------------------------------------------------------------------------
# 3. APPROXIMATE NORMAL COST RATES (purchase price inside the window)
# ----------------------------------------------------------------------------
ANC_PLAN1 = I(0.1250, "of creditable comp per year purchased",
    f"PRIMARY: {VRS_PPS} p.2; approved {VRS_BAC} p.6 (RBA 2025-06), effective 2025-07-01",
    "Regular VRS (State, Teacher, PS non-hazardous). Prior rate 12.54%.", "")
ANC_PLAN2 = I(0.1074, "of creditable comp per year purchased",
    f"PRIMARY: {VRS_PPS} p.3; approved {VRS_BAC} p.6", "Prior rate 10.89%.", "")
ANC_HYBRID = I(0.0668, "of creditable comp per year purchased",
    f"PRIMARY: {VRS_PPS} p.1; approved {VRS_BAC} p.6", "Hybrid window is 2 years as well.", "")
ANC_BASIS = I("higher of current creditable compensation or AFC at time of purchase", "rule",
    f"PRIMARY: {VRS_ERM} p.11; {VRS_HB1} p.27", "", "")

# ----------------------------------------------------------------------------
# 4. EMPLOYER CONTRIBUTION / LOADING RATES  (FY2027-2028 Board-certified)
# ----------------------------------------------------------------------------
ER_DB_RATE = I(0.1107, "of payroll", f"PRIMARY: {VRS_RATES}; {VRS_VAL} p.18 (4.34% NC + 0.24% admin + 6.49% UAAL)", "", "")
ER_GLI = I(0.0106, "of payroll", f"PRIMARY: {VRS_RATES}", "Group Life Insurance.", "")
ER_HIC = I(0.0070, "of payroll", f"PRIMARY: {VRS_RATES}", "State retiree Health Insurance Credit.", "")
ER_VSDP = I(0.0042, "of payroll", f"PRIMARY: {VRS_RATES}", "Virginia Sickness and Disability Program.", "")
ER_FICA = I(0.0765, "of payroll", "PRIMARY: 26 U.S.C. 3111 (OASDI 6.2% + HI 1.45%)",
    "OASDI applies only up to the wage base; at the salaries modelled here the full 7.65% applies.", "")
HYBRID_ER_DC = I(0.035, "of payroll", f"PRIMARY: {VRS_RATES} ('1.0%-3.5% based on member elections')",
    "Modelled at the maximum (1% mandatory + 2.5% match) to avoid overstating the tier-mix saving.",
    "Lower actual match -> larger tier-mix saving than modelled (conservative).")
ER_HEALTH_FLAT = I(0, "dollars per year", "JUDGMENT: treated as NOT salary-scaled and therefore NOT a source of savings",
    "The employer share of state health insurance is a flat per-employee premium, not a percentage of pay. "
    "Replacing a high-salary incumbent with a lower-salary hire produces ZERO health-premium saving. "
    "Excluded from the salary-differential loading on purpose.",
    "Including it would overstate workforce savings.")

# ----------------------------------------------------------------------------
# 5. HEADCOUNT AND PAYROLL  (State Employee plan, June 30, 2025)
# ----------------------------------------------------------------------------
ACTIVE_STATE = I(81274, "members", f"PRIMARY: {VRS_VAL} p.12", "Active State Employee plan members.", "")
COVERED_PAYROLL_STATE = I(6_275_603_114, "dollars", f"PRIMARY: {VRS_VAL} p.50 (table total)", "", "")
# Active participants tabulated by age and total service, State Employees, 6/30/2025 (VRS_VAL p.50).
# rows: age band label -> {service band -> count}, plus total count and total payroll for the age band.
AGE_SERVICE_TABLE = I({
 #  age label      : (  0-4,  5-9, 10-14, 15-19, 20-24, 25-29, 30+ ,  total,      payroll)
 "Under 20": (  107,    0,     0,     0,     0,     0,     0,    107,     4_357_105),
 "20-24"   : ( 2505,   11,     0,     0,     0,     0,     0,   2516,   122_954_249),
 "25-29"   : ( 5985,  627,     4,     0,     0,     0,     0,   6616,   384_424_727),
 "30-34"   : ( 5547, 2244,   299,     0,     0,     0,     0,   8090,   537_371_988),
 "35-39"   : ( 4772, 2651,  1520,   289,     5,     0,     0,   9237,   683_642_180),
 "40-44"   : ( 3916, 2414,  1789,  1186,   368,    10,     0,   9683,   775_140_818),
 "45-49"   : ( 3371, 2110,  1596,  1362,   968,   342,    10,   9759,   813_314_096),
 "50-54"   : ( 3017, 1975,  1560,  1333,  1165,   892,   238,  10180,   862_780_498),
 "55-59"   : ( 2590, 1816,  1450,  1374,  1230,  1061,  1008,  10529,   874_767_645),
 "60"      : (  468,  302,   313,   231,   226,   231,   329,   2100,   170_788_873),
 "61"      : (  416,  339,   266,   286,   248,   214,   327,   2096,   173_035_222),
 "62"      : (  326,  285,   270,   241,   224,   225,   349,   1920,   156_481_463),
 "63"      : (  300,  269,   202,   224,   211,   211,   315,   1732,   143_187_368),
 "64"      : (  224,  248,   206,   210,   206,   161,   325,   1580,   130_192_505),
 "65"      : (  154,  165,   144,   166,   157,   108,   229,   1123,    94_393_368),
 "66"      : (  140,  141,   126,   117,   105,    77,   228,    934,    80_275_667),
 "67"      : (  100,  102,   101,    87,    82,    61,   127,    660,    57_045_695),
 "68"      : (   64,   88,    75,    87,    53,    66,   132,    565,    48_317_294),
 "69"      : (   54,   66,    60,    57,    51,    32,    89,    409,    34_661_885),
 "70+"     : (  191,  149,   172,   183,   167,   132,   444,   1438,   128_470_467),
}, "counts and dollars", f"PRIMARY: {VRS_VAL} p.50 'Active Participants - Tabulated by Age and Total Service, State Employees'",
 "Service bands are COMPLETED years of TOTAL service. Payroll is for the whole age row, not by service band.",
 "")
SERVICE_BANDS = I(["0-4","5-9","10-14","15-19","20-24","25-29","30+"], "labels", "DERIVED: column headers of AGE_SERVICE_TABLE", "", "")

# ----------------------------------------------------------------------------
# 6. SALARY  (DHRM classified, 6/30/2024)
# ----------------------------------------------------------------------------
DHRM_SAL_MEAN   = I(69865, "dollars", f"PRIMARY: {DHRM_SFAC} p.14 (All Pay Areas, n=56,728)", "", "")
DHRM_SAL_MEDIAN = I(61305, "dollars", f"PRIMARY: {DHRM_SFAC} p.14", "", "")
DHRM_SAL_P25    = I(48538, "dollars", f"PRIMARY: {DHRM_SFAC} p.14", "", "")
DHRM_SAL_P75    = I(82735, "dollars", f"PRIMARY: {DHRM_SFAC} p.14", "", "")
LONG_SERVICE_PREMIUM = I(0.10, "fraction", "JUDGMENT: central 10%, defensible range 0% to 20%",
    "Premium of a 25+ year employee's salary over the average for their AGE band. The VRS table gives payroll "
    "by age only, not by age x service, so the within-age seniority gradient is not public. 10% is the "
    "midpoint between no gradient and the gradient implied by DHRM pay-band progression.",
    "Higher premium -> higher ANC price, higher plan cost, and higher workforce differential (partly offsetting).")
SALARY_DISPERSION = I({"p25": 48538/61305, "p50": 1.0, "p75": 82735/61305}, "ratio to median",
    f"DERIVED: {DHRM_SFAC} p.14 percentile ratios applied to the long-service median", "", "")

# ----------------------------------------------------------------------------
# 7. VETERAN SHARE AND ELIGIBILITY FUNNEL
# ----------------------------------------------------------------------------
VETERAN_SHARE_WORKFORCE = I(0.06, "fraction of classified employees",
    f"PRIMARY: {DHRM_SFAC} p.8 ('Veterans 6% / Non-Veterans 94%')",
    "Self-identified, classified executive-branch workforce, 6/30/2024. The VRS State Employee plan "
    "(81,274 actives) is a different and broader denominator than DHRM classified (56,917).",
    "Self-identification UNDERSTATES veteran share -> understates eligible population and cost.")
VETERAN_AGE_SKEW = I(1.5, "multiplier", "JUDGMENT: central 1.5x, defensible range 1.0x to 2.0x",
    "Veteran share among employees aged 50+ with 25+ years of service, relative to the 6% all-ages share. "
    "Veterans in the state workforce are older on average (prior military service delays state entry), so the "
    "share in a 25+ year, age-50+ cohort exceeds the overall share. VRS/DHRM publish no cross-tab.",
    "Higher skew -> larger eligible pool -> higher cost. One of the top-3 sensitivities.")
QUALIFYING_SERVICE_SHARE = I(0.60, "fraction of veterans",
    "JUDGMENT: central 60%, defensible range 40% to 75%",
    "Share of veteran employees holding prior active-duty service that is actually purchasable: >=180 "
    "consecutive days of active duty, not already credited in the VRS record, not used to qualify for a "
    "benefit from another retirement system (so active-duty military retirees are excluded; Reserve/Guard "
    "are not), and not already purchased inside the 24-month window.",
    "Not published by VRS. Lower share -> lower cost. Second-largest population uncertainty.")
AVG_MONTHS_AVAILABLE = I(36, "months", "JUDGMENT: central 36 months, defensible range 24 to 48",
    "Average months of qualifying active-duty service a participating veteran holds, capped at the statutory "
    "48. A single 4-year enlistment net of training/terminal leave typically credits 36-48 months; many hold "
    "a shorter single tour.",
    "Higher -> higher cost per participant, roughly linear.")

# ----------------------------------------------------------------------------
# 8. TAKE-UP
# ----------------------------------------------------------------------------
TAKEUP_PATHWAY_A = I({"low": 0.15, "central": 0.30, "high": 0.50}, "fraction of eligible",
    "JUDGMENT: see note. Pending comparative figures from MOO-8.",
    "The purchase is strongly NPV-positive for the member (payback shown in results), can be funded pre-tax "
    "from a 457/403(b) rollover, and the pilot is time-limited and will be publicised. Against that: VRS's own "
    "experience is that most members do NOT purchase even inside the cheap 24-month window (that is the "
    "problem the bill addresses), and the purchase requires a four- to five-figure cash outlay. "
    "Low 15% = behaviour unchanged from today's revealed low purchase propensity. "
    "Central 30% = a publicised, time-limited, NPV-positive one-time window. "
    "High 50% = strong agency HR promotion plus employer payroll-deduction financing.",
    "Participation scales cost almost linearly. THE dominant sensitivity.")
TAKEUP_PATHWAY_B = I({"low": 0.10, "central": 0.22, "high": 0.40}, "fraction of eligible",
    "JUDGMENT: set 0.73x of Pathway A at each level; defensible range as shown.",
    "Lower than Pathway A because Pathway B requires the member to retire within six months of completing "
    "the purchase, which screens out everyone not already at the point of leaving.",
    "Same direction as Pathway A.")
TAKEUP_S5_OPEN_WINDOW = I({"low": 0.04, "central": 0.09, "high": 0.18}, "fraction of eligible",
    "JUDGMENT: central 9%; defensible range 4% to 18%.",
    "S5 reopens the window for the whole Plan 1/Plan 2 active population with no retirement proximity and no "
    "immediate benefit payoff, so take-up per eligible member is far lower than for members at the retirement "
    "cusp - but the eligible denominator is ~7x larger.",
    "")
PILOT_PHASING = I([0.35, 0.30, 0.20, 0.15], "fraction of total participants by pilot year",
    "JUDGMENT: front-loaded; defensible range 0.50/0.25/0.15/0.10 to 0.25/0.25/0.25/0.25",
    "A one-time election against a STOCK of eligible members front-loads. Year-1 share is damped by the "
    "12-month completion requirement and by VRS implementation lead time.", "")
PILOT_FY = I([2028, 2029, 2030, 2031], "fiscal years",
    "DERIVED: four-year pilot with a July 1, 2027 effective date (2027 session / JLC 2027 initiative cycle)",
    "FY2028 = 7/1/2027-6/30/2028. Virginia's FY boundary coincides with the effective date, so no program "
    "year is split; the 12-month completion requirement is what shifts cash across fiscal years.", "")

# ----------------------------------------------------------------------------
# 9. WORKFORCE / REPLACEMENT INPUTS
# ----------------------------------------------------------------------------
REPLACEMENT_DIFFERENTIAL = I({"conservative": 0.08, "central": 0.18, "optimistic": 0.30}, "fraction below incumbent salary",
    "JUDGMENT: anchored on two published figures; see note.",
    "Lower anchor: VRS p.50 average salary at age 35-39 ($74,012) vs age 55-59 ($83,081) = 10.9% lower, "
    "cross-sectional and therefore an understatement of the incumbent-vs-new-hire gap. Upper anchor: DHRM "
    f"p.14 pay-band structure - a band-3 minimum ($32,843) is 64% below the band-3 maximum ($90,832), so a "
    "replacement hired near band minimum for a role whose incumbent sits near midpoint implies a much larger "
    "gap. Central 18% is between them. DHRM does not publish incumbent-vs-new-hire salary pairs by role.",
    "Higher differential -> larger workforce saving. Top-3 sensitivity for the offset.")
MONTHS_ACCELERATION = I({"conservative": 2.0, "central": 6.0, "optimistic": 14.0}, "months per participant",
    "JUDGMENT: see note. No Virginia or other-state measurement of this exists for this design.",
    "Averaged over ALL participants, including those who would have retired anyway (zero acceleration). "
    "DHRM p.10: 5.2% of classified employees are retirement-eligible today and 8.5% within two years, but the "
    "annual retirement rate is only 1.4% - i.e. eligibility alone does not trigger retirement, so there is a "
    "large stock of eligible-but-staying employees for a design to move. Conservative 2 months assumes most "
    "participants are pure windfall. Central 6 months assumes roughly half are windfall and the rest move "
    "~12 months. Optimistic 14 months assumes the six-month retirement condition genuinely binds.",
    "Directly proportional to the workforce saving. THE dominant sensitivity for the offset.")
VACANCY_MONTHS = I(4.0, "months", f"PRIMARY (component): {DHRM_SFAC} p.10 average time to hire 78 days; "
    "JUDGMENT for the rest of the cycle (posting, approval, offer, notice period): total 4.0 months, range 2.6-7.0",
    "DHRM also reports a 22.4% classified vacancy rate, i.e. positions routinely stay open well past the "
    "78-day hire cycle.", "Longer vacancy -> larger salary saving but larger overtime/coverage cost.")
VACANCY_COVERAGE_COST_SHARE = I(0.55, "fraction of vacant-position salary",
    "JUDGMENT: central 55%, defensible range 25% to 90%",
    "Share of the vacant incumbent's salary cost that comes back as overtime, wage/temporary staff, contractor "
    "coverage or service degradation during the vacancy. Virginia does not publish coverage cost per vacancy.",
    "Higher share -> smaller net vacancy saving. CUTS AGAINST the offset.")
RECRUITMENT_COST_PER_HIRE = I(5000, "dollars",
    "JUDGMENT: central $5,000, defensible range $3,000 to $8,000. NOT PUBLISHED by DHRM or JLARC.",
    "DHRM reports 16,088 FY24 recruitments and a 78-day average time to hire but no cost per hire; JLARC's "
    "workforce reports do not publish a per-hire cost either. $5,000 is the midpoint of commonly cited "
    "public-sector cost-per-hire benchmarks and is used only as a labelled estimate.",
    "CUTS AGAINST the offset.")
PRODUCTIVITY_RAMP_LOSS = I(0.25, "fraction of replacement first-year salary",
    "JUDGMENT: central 25%, defensible range 10% to 40%",
    "Output forgone while a replacement reaches the incumbent's productivity, plus incumbent-time spent "
    "training. Not published for Virginia.",
    "CUTS AGAINST the offset. Often omitted from turnover-savings claims; omitting it would bias the "
    "answer optimistic.")
BACKFILL_BEHAVIOUR = I({"lower_cost_backfill": 0.70, "left_vacant": 0.10, "equal_cost_backfill": 0.20},
    "fractions, sum to 1", "JUDGMENT: central mix; the 'equal cost' branch is the one that destroys the saving",
    "If a position is backfilled at the SAME cost (market-rate hire, hard-to-fill role, or a promotion that "
    "simply moves the vacancy) there is no salary saving at all and the design is a pure cost. "
    "Agencies facing a 22.4% vacancy rate often backfill hard-to-fill roles at or above the incumbent rate.",
    "A larger equal-cost share eliminates the offset. Reported explicitly as its own case.")

# ----------------------------------------------------------------------------
# 10. FUND SPLIT
# ----------------------------------------------------------------------------
GF_SHARE = I(0.47, "fraction of state employee payroll",
    f"PRIMARY (qualitative): {HAC_COMP} - nongeneral funds 'represent a little over half of the cost of "
    "across the broad pay increases for state employees'; JUDGMENT: central 47%, range 40%-55%",
    "Virginia does not publish a single GF/NGF payroll percentage for the State Employee plan; the HAC "
    "statement bounds NGF just above 50%, so GF is just under 50%.",
    "Higher GF share -> higher general fund cost, same total cost.")

# ----------------------------------------------------------------------------
# 11. EXTERNAL SANITY CHECK ANCHOR
# ----------------------------------------------------------------------------
SB419_CHECK = I({"liability_increase": 258_000_000, "sports_valors_actives": None,
                 "gf_annual": 26_256_000, "ngf_annual": 4_155_000,
                 "vrs_implementation_cost": 374_500},
    "dollars", f"PRIMARY: {FIS_SB419} (VRS Fiscal Impact Statement, SB 419, 2026 session, published 1/28/2026)",
    "SB 419 awarded 1 extra year of creditable service per 5 full years to SPORS/VaLORS members. VRS scored "
    "it at ~$258M of added liability across the two plans and ~$30.4M/yr of added employer contributions "
    "beginning FY2028, plus $374,500 of VRS implementation cost. Used in sanity_check.py as a "
    "cost-per-added-year-of-service-credit benchmark and as the benchmark for VRS implementation cost.", "")
VALORS_ACTIVES = I(9865, "members", f"PRIMARY: {VRS_VAL} p.16 (Virginia Law Officers, active)", "", "")
SPORS_ACTIVES = I(1879, "members", f"PRIMARY: {VRS_VAL} p.14 (State Police Officers, active)", "", "")
VALORS_PAYROLL = I(432_703_000, "dollars", f"PRIMARY: {VRS_VAL} p.16", "", "")
SPORS_PAYROLL = I(182_726_000, "dollars", f"PRIMARY: {VRS_VAL} p.14", "", "")

# ----------------------------------------------------------------------------
# 12. SOA MORTALITY CALIBRATION TARGETS
# ----------------------------------------------------------------------------
# Table D.3 "Amount-Weighted General at Flat 7.0% Interest": monthly annuity-due values,
# PubG-2010 base with MP-2017, generational @ July 1, 2018. Ages 65/75/85 are IMMEDIATE
# annuities; ages 25/35/45/55 are DEFERRED-to-62 values.
SOA_D3_IMMEDIATE = I({"male": {65: 11.2288, 75: 8.8082, 85: 5.7558},
                      "female": {65: 10.6096, 75: 8.0934, 85: 5.1212}},
    "annuity-due value per $1/yr paid monthly, 7.00% flat",
    f"PRIMARY: {SOA_PUB} Table D.3 (p.83)", "", "")
SOA_D3_DEFERRED62 = I({"male": {45: 3.7330, 55: 7.3051}, "female": {45: 3.5270, 55: 6.9103}},
    "deferred-to-62 annuity-due value, 7.00% flat", f"PRIMARY: {SOA_PUB} Table D.3 (p.83)",
    "Used as an OUT-OF-SAMPLE check on the fitted mortality law, not as a fitting target.", "")
VRS_FEMALE_LOAD = I(1.10, "multiplier on female q(x)",
    f"PRIMARY: {VRS_EXP} p. B-10 'Healthy Post-Retirement Mortality Rate Adjustments', State/General: "
    "100% of male table, 110% of female table", "", "")
PARTICIPANT_GENDER_MIX = I({"male": 0.75, "female": 0.25}, "fractions",
    "JUDGMENT: central 75/25, defensible range 60/40 to 90/10",
    "DHRM p.8 reports the classified workforce as 45% male / 55% female, but the participating population is "
    "VETERANS, who are predominantly male. Nationally ~90% of the living veteran population is male, skewing "
    "less so in younger cohorts. 75/25 is deliberately between the two.",
    "A higher male share LOWERS the annuity factor and therefore lowers plan cost, because male mortality is "
    "heavier. Modest effect (~3%).")


# ----------------------------------------------------------------------------
# 13. BASELINE RETIREMENT BEHAVIOUR (counterfactual)
# ----------------------------------------------------------------------------
BASELINE_EXTRA_YEARS_WORKED = I(2.0, "years past first unreduced eligibility",
    "JUDGMENT: central 2.0 years, defensible range 0.0 to 4.0",
    f"PRIMARY support: {DHRM_SFAC} p.10 - 5.2% of the classified workforce is retirement-eligible TODAY and "
    "8.5% within two years, against an annual retirement rate of only 1.4%. If everyone retired at first "
    "eligibility the retirement rate would have to be several times higher. 2.0 years is the implied average "
    "lag, rounded. VRS/DHRM do not publish an age-at-retirement-minus-age-at-first-eligibility distribution.",
    "A LONGER baseline lag makes the counterfactual benefit larger, which RAISES the early-retirement "
    "subsidy per month of acceleration. Also raises the headroom for acceleration to be real.")


# ----------------------------------------------------------------------------
# 14. SCENARIO-SPECIFIC INPUTS
# ----------------------------------------------------------------------------
TAKEUP_PRICE_ELASTICITY = I(-0.6, "elasticity of take-up w.r.t. member price",
    "JUDGMENT: central -0.6, defensible range -0.3 to -1.0",
    "Used only to move take-up between scenarios that change the member's price (S3 sliding scale, "
    "S0 status quo). A 1% higher member price reduces take-up by 0.6%. No Virginia purchase-price "
    "elasticity is published; this is a stated judgment, not data.",
    "A larger magnitude makes S3 cheaper and S0 participation closer to zero.")
S0_TAKEUP = I(0.02, "fraction of eligible", "JUDGMENT: central 2%, range 0%-5%",
    "Status quo: eligible out-of-window members pay full actuarial equivalent cost. Participation is "
    "not zero (some members do pay it) but is very low; this is the revealed behaviour the bill addresses.",
    "")
S3_GAP_SHARE = I({"25-29_yrs_state_service": 0.50, "30plus_yrs_state_service": 0.25}, "share of the ANC-to-AEC gap paid by the member",
    "DESIGN PARAMETER from the MOO-7 scenario set (S3: 25/50/75%, share falling with state service)",
    "The 75% tier would apply to members with under 25 years of state service, who are not in the "
    "Pathway A/B eligible pool, so it never binds for S1/S2-style eligibility.", "")
S4_AGENCY_OPTIN = I(0.35, "fraction of eligible members at opting-in agencies",
    "JUDGMENT: central 35%, defensible range 15% to 60%",
    "S4 makes the employing agency pay the ANC-to-AEC differential out of turnover savings, and is "
    "opt-in. Agencies with a 22.4% vacancy rate (DHRM p.10) and no appropriated offset have a weak "
    "incentive to spend cash now for a saving they cannot bank.",
    "")
S7_CAPS = I([2_000_000, 5_000_000, 10_000_000], "dollars of aggregate incremental liability",
    "DESIGN PARAMETER: candidate hard caps to test for S7", "", "")
DOUBLE_PARTICIPATION_FACTOR = I(2.0, "multiplier", "REQUIREMENT of the MOO-7 assignment",
    "Explicitly requested stress case: participation at double the central estimate.", "")
VRS_IMPLEMENTATION_COST = I({"low": 150_000, "central": 375_000, "high": 750_000}, "dollars, one-time",
    "PRIMARY anchor: VRS scored its own implementation cost for SB 419 (2026) at $374,500 in FY2027 "
    "(https://lis.blob.core.windows.net/files/1098992.PDF); JUDGMENT for the range.",
    "A pilot with two pathways, a clawback, an annual report and a sunset needs myVRS Navigator and "
    "benefit-calculation changes plus counselling material. Nongeneral fund (VRS administrative).",
    "A clawback and a six-month retirement condition are system-heavy; the high case is plausible.")


# ============================================================================
# 15. MOO-31 ADDITIONS — S8 (Pennsylvania earned-service repricing) and
#     S9 (South Carolina early-retirement reduction waiver).
#     Purely ADDITIVE: nothing above this line is changed, so every MOO-7
#     number still reproduces.
# ============================================================================
PA_5505 = "https://law.justia.com/codes/pennsylvania/2010/title-71/chapter-55/5505"
PA_5102 = "https://codes.findlaw.com/pa/title-71-pacsa-state-government/pa-csa-sect-71-5102"
VRS_ERM_SR = "https://employers.varetire.org/media/shared/pdf/er-manual-service-retirement.pdf"
VRS_VAL_APX = VRS_EXP  # the document served at this URL contains the Appendix to the
                       # June 30, 2025 Annual Actuarial Valuation Reports (salary scale, p.57)

# ---- 15.1 the S8 price basis -----------------------------------------------
S8_STATUTORY_BASIS = I(
    "total normal cost rate x average annual creditable compensation over the first 36 months of "
    "VRS service x years purchased x (1 + statutory interest)^(years from end of that period to "
    "date of purchase)", "rule",
    f"PRIMARY: 71 Pa.C.S. 5505(b) ({PA_5505}) — 'applying the member's basic contribution rate, "
    "the additional contribution rate plus the Commonwealth normal contribution rate ... to his "
    "average annual rate of compensation as a member of the system over the first three years of "
    "such subsequent State service and multiplying the result by the number of years ... being "
    "purchased together with statutory interest during all periods of subsequent State and school "
    "service to date of purchase'",
    "Modelled exactly as drafted in Pennsylvania, with the Virginia analogues substituted for each "
    "Pennsylvania rate. No election window.", "")

S8_TNC_RATE_SOURCE = I("VRS published approximate-normal-cost rate for the plan", "rule",
    f"PRIMARY: {VRS_ERM} p.11 — 'The approximate normal cost rate is the average cost of one year "
    "of VRS service credit.' That is, by VRS's own words, the TOTAL (member + employer) cost of a "
    "year of service credit for the plan, which is what 71 Pa.C.S. 5505(b) charges.",
    "So S8 uses the SAME rate as the ANC price (12.50% Plan 1 / 10.74% Plan 2). The entire S8-to-ANC "
    "multiple is therefore driven by the salary basis and the interest term, not by the rate. That "
    "makes the comparison exact rather than approximate.",
    "If VRS instead certified a plan-specific total normal cost built from the valuation "
    "(member 5.00% + employer normal cost 4.34% = 9.34%), the S8 price falls by a factor of 0.747. "
    "Tested as S8_TNC_NARROW below.")

S8_TNC_NARROW_RATE = I(0.0500 + 0.0434, "of creditable comp per year purchased",
    f"DERIVED: member contribution 5.00% ({VRS_HB1} p.14, 'You contribute 5% of your compensation "
    f"each month') + employer normal cost 4.34% ({VRS_VAL} p.18).",
    "Alternative, NARROWER reading of 'total normal cost'. It is the State Employee plan's BLENDED "
    "employer normal cost across Plan 1 / Plan 2 / Hybrid, so it understates the total normal cost "
    "of a Plan 1 benefit specifically. Reported as a drafting sensitivity, not as the central case.",
    "Using it UNDERSTATES the S8 price and therefore OVERSTATES the Commonwealth's cost.")

S8_INTEREST_RATE = I(0.0400, "per year, compounded annually",
    f"PRIMARY, and it agrees on both sides of the comparison: (a) Pennsylvania's 'statutory "
    f"interest' is defined at 71 Pa.C.S. 5102 as 'interest at 4% per annum, compounded annually' "
    f"({PA_5102}); (b) Virginia's own statutory member-account rate is also 4% — {VRS_HB1} p.14, "
    "'Your account accrues 4% interest, which is compounded annually on the balance as of the "
    "previous June 30.'",
    "4.00% is therefore the drafting default: it is what Pennsylvania actually charges AND what "
    "Virginia already pays on member contributions, so a Virginia bill can adopt it by reference to "
    "existing Virginia practice without inventing a rate.",
    "The DOMINANT driver of the S8 price. Every 100bp of interest raises the price of a 27-year "
    "member by roughly 27%. Higher rate -> higher member price -> lower Commonwealth cost AND lower "
    "take-up.")

S8_INTEREST_TEST = I([0.04, 0.05, 0.06, 0.0675], "per year",
    "REQUIREMENT of the MOO-31 assignment: test 4%, 5%, 6% and the assumed rate of return (6.75%).",
    "6.75% is the VRS assumed rate of return (DISCOUNT_RATE). Charging it would make the basis "
    "'actuarially whole on contributions' but, as the results show, re-creates a calendar penalty.", "")

S8_AVERAGING_MONTHS = I(36, "months",
    f"PRIMARY: 71 Pa.C.S. 5505(b) ({PA_5505}) — 'over the first three years of such subsequent "
    "State service'.",
    "Also coincides with the VRS Plan 1 AFC period (36 consecutive months), which is a drafting "
    "convenience: VRS already holds and uses a 36-month compensation average.",
    "A LONGER averaging period raises the salary base (later, higher-paid months enter) but SHORTENS "
    "the interest period. The two effects partly cancel; net direction depends on whether the "
    "interest rate exceeds individual salary growth.")

S8_AVERAGING_TEST = I([24, 36, 60], "months",
    "REQUIREMENT of the MOO-31 assignment. 60 months is also the VRS Plan 2 / Hybrid AFC period.",
    "", "")

# ---- 15.2 the salary back-cast — the second dominant driver -----------------
VRS_SALARY_SCALE_STATE = I(
    {0: 0.0585, 1: 0.0585, 2: 0.0585, 3: 0.0525, 4: 0.0495, 5: 0.0495, 6: 0.0495,
     7: 0.0485, 8: 0.0475, 9: 0.0450, 10: 0.0450,
     11: 0.0415, 12: 0.0415, 13: 0.0415, 14: 0.0415, 15: 0.0415, 16: 0.0415,
     17: 0.0415, 18: 0.0415, 19: 0.0415, 20: 0.0350},
    "annual rate of individual salary increase, by completed years of service",
    f"PRIMARY: {VRS_VAL_APX} — 'Salary Increase Rates ... State', Appendix to the June 30, 2025 "
    "Annual Actuarial Valuation Reports, p.57. Key 20 = '20+'. The published note reads 'the rates "
    "below include wage inflation of 3.5% per year'.",
    "This is VRS's own INDIVIDUAL salary-increase assumption (service-based), which is the right "
    "scale for reconstructing a member's own compensation history. It is NOT the same figure as "
    "PAYROLL_GROWTH (3.00%), which is aggregate total payroll growth and is used elsewhere in this "
    "model for projecting the plan's payroll, not an individual's pay.",
    "CRITICAL DIRECTION OF ERROR. This is a FORWARD-LOOKING assumption applied BACKWARD. Virginia "
    "granted no general salary increase to state employees in several years of the 1998-2025 period, "
    "so realised individual growth over a 25-year career was very probably LOWER than 4.15-5.85%. "
    "Lower realised growth means the member's first-36-month salary was HIGHER relative to today's "
    "salary than this back-cast implies, so the TRUE S8 price is HIGHER and the Commonwealth's cost "
    "LOWER than modelled. Tested in the tornado as SALARY_BACKCAST_SHIFT.")

S8_BACKCAST_SHIFT_TEST = I([-0.0100, 0.0, +0.0100], "additive shift to every rate in the scale",
    "JUDGMENT: +/-100bp on the whole scale, a defensible band given that the scale is an assumption "
    "applied to history.",
    "-100bp approximates a career with several Virginia salary-freeze years.",
    "A LOWER back-cast growth rate raises the first-36-month base and therefore the S8 price.")

# ---- 15.3 the service-matching cap ----------------------------------------
S8_SERVICE_MATCHING_CAP = I(True, "boolean",
    f"PRIMARY: 71 Pa.C.S. 5505(b) ({PA_5505}) and the MOO-3 Scenario Selection Memo 4.2 — the "
    "member may not purchase more military service than credited state service.",
    "Applied as years_purchased = min(years_purchased, credited_state_service).", "")

# ---- 15.4 S9: the South Carolina reduction waiver --------------------------
S9_DEVICE = I("member purchases a waiver of the early-retirement reduction factor; benefit stays "
    "computed on ACTUAL service, no credit is added", "rule",
    "DESIGN, from the MOO-8 comparative work (South Carolina 2000 buy-down) via the MOO-3 Scenario "
    "Selection Memo 3 (S9 / 'S2-SC').",
    "Nothing is added to the benefit formula. Only the reduction factor is bought off.", "")

VRS_REDUCTION_IS_ACTUARIAL = I("actuarial", "rule",
    f"PRIMARY: {VRS_ERM_SR} p.6 — \"A member's benefit is actuarially reduced to calculate the "
    "reduced Basic Benefit\"; and ibid. \"An additional reduction factor is applied to a VRS Plan 1 "
    f"member retiring under the 50/10 reduced retirement provision.\" See also {VRS_HB1} p.16.",
    "VRS does not publish a numeric early-retirement reduction factor table. Because the published "
    "rule is actuarial reduction, this model DERIVES the factor as the actuarially equivalent one on "
    "its own mortality and discount basis: "
    "RF(R) = v^(U-R) * (U-R)p_R * a(U) / a(R), with service frozen at R and U the member's "
    "unreduced age on that frozen service. RF = 1 when R >= U.",
    "CRITICAL. In practice public-plan reduction factors are often MORE GENEROUS than strict "
    "actuarial equivalence (a subsidy), and VRS's 50/10 provision carries an EXTRA reduction in the "
    "other direction. If VRS's real factors are more generous than actuarial equivalence, the waiver "
    "is worth LESS than modelled, so the member price here is OVERSTATED and the plan's cost "
    "UNDERSTATED. Only VRS can settle this; the factor table is not public.")

S9_PRICE_RULES = I(["actuarial", "anc_parity"], "labels",
    "DESIGN PARAMETER. 'actuarial' = member pays the full present value of the waiver (the South "
    "Carolina device as described). 'anc_parity' = member pays the SAME statutory formula as S2 "
    "(ANC rate x salary x years of eligibility advanced), which is the drafting-simplest option.",
    "", "")

S9_RETIRE_IMMEDIATELY = I(True, "boolean",
    "DESIGN, from the MOO-3 Scenario Selection Memo 4.2 ('Retirement immediately after purchase', "
    "modelled on Utah 49-12-409).",
    "This guardrail is not optional for S9: a reduction waiver has no value at all to a member who "
    "goes on working past their unreduced date, so S9 only exists as a design if purchase triggers "
    "retirement. Modelled as retirement at the member's current age.",
    "Without the condition the waiver is worth $0 at central assumptions — reported explicitly.")

S9_ACCEL_SWEEP = I([6.0, 12.0, 24.0, 36.0, 48.0, 60.0], "months of retirement acceleration",
    "DESIGN PARAMETER: swept because the waiver's value is zero until the retirement date is pulled "
    "back past the member's unreduced-eligibility date.", "", "")

# ---- 15.5 reference point for the headline ratio ---------------------------
S1_NET_LIABILITY_REFERENCE = I(2_903_252, "dollars, PV, four-year pilot, central",
    "DERIVED: the MOO-7 model's own S1 central net liability (out_part3_scenarios.csv, row S1). "
    "Recomputed live in this run and asserted equal, so the ratio can never drift from the table.",
    "The memo rounds this to $2.90M.", "")


# ============================================================================
# 16. MOO-31 REPAIR (Policy Director comment of 2026-10-11 16:09, acting on the
#     MOO-15 red team findings F1, F2, F3, F6, F7).
#     Still purely ADDITIVE: `python3 main.py` reproduces MOO-7 unchanged.
# ============================================================================

# ---- 16.1 VRS's own decrement assumptions ---------------------------------
# These replace BASELINE_EXTRA_YEARS_WORKED as the counterfactual.  Red team F1:
# "estimate the counterfactual retirement date separately and visibly rather than
# burying it in a lag assumption."  VRS publishes the assumption, so the repaired
# model uses VRS's assumption instead of an analyst lag.
RETIREMENT_RATES_PLAN1 = I({
    # attained age -> {service band -> rate}; bands as published: 0-4, 5-9, 10-29, 30+
    "male": {
        50: (0.000, 0.000, 0.030, 0.160), 51: (0.000, 0.000, 0.030, 0.080),
        52: (0.000, 0.000, 0.030, 0.090), 53: (0.000, 0.000, 0.030, 0.080),
        54: (0.000, 0.000, 0.030, 0.090), 55: (0.000, 0.030, 0.030, 0.090),
        56: (0.000, 0.040, 0.040, 0.080), 57: (0.000, 0.040, 0.040, 0.090),
        58: (0.000, 0.040, 0.040, 0.090), 59: (0.000, 0.040, 0.040, 0.090),
        60: (0.000, 0.050, 0.050, 0.100), 61: (0.000, 0.070, 0.070, 0.150),
        62: (0.000, 0.110, 0.110, 0.190), 63: (0.000, 0.090, 0.090, 0.170),
        64: (0.000, 0.140, 0.140, 0.180), 65: (0.000, 0.250, 0.250, 0.250),
        66: (0.000, 0.260, 0.260, 0.260), 67: (0.000, 0.230, 0.230, 0.230),
        68: (0.000, 0.220, 0.220, 0.220), 69: (0.000, 0.210, 0.210, 0.210),
        70: (0.000, 0.220, 0.220, 0.220), 71: (0.000, 0.210, 0.210, 0.210),
        72: (0.000, 0.210, 0.210, 0.210), 73: (0.000, 0.210, 0.210, 0.210),
        74: (0.000, 0.210, 0.210, 0.210), 75: (0.000, 0.230, 0.230, 0.230),
        76: (0.000, 0.200, 0.200, 0.200), 77: (0.000, 0.200, 0.200, 0.200),
        78: (0.000, 0.210, 0.210, 0.210), 79: (0.000, 0.250, 0.250, 0.250),
        80: (0.000, 1.000, 1.000, 1.000)},
    "female": {
        50: (0.000, 0.000, 0.040, 0.070), 51: (0.000, 0.000, 0.030, 0.070),
        52: (0.000, 0.000, 0.030, 0.070), 53: (0.000, 0.000, 0.030, 0.090),
        54: (0.000, 0.000, 0.030, 0.080), 55: (0.000, 0.040, 0.040, 0.070),
        56: (0.000, 0.040, 0.040, 0.080), 57: (0.000, 0.040, 0.040, 0.090),
        58: (0.000, 0.040, 0.040, 0.090), 59: (0.000, 0.050, 0.050, 0.090),
        60: (0.000, 0.060, 0.060, 0.120), 61: (0.000, 0.080, 0.080, 0.150),
        62: (0.000, 0.120, 0.120, 0.190), 63: (0.000, 0.110, 0.110, 0.170),
        64: (0.000, 0.160, 0.160, 0.190), 65: (0.000, 0.290, 0.290, 0.290),
        66: (0.000, 0.310, 0.310, 0.310), 67: (0.000, 0.260, 0.260, 0.260),
        68: (0.000, 0.250, 0.250, 0.250), 69: (0.000, 0.270, 0.270, 0.270),
        70: (0.000, 0.280, 0.280, 0.280), 71: (0.000, 0.250, 0.250, 0.250),
        72: (0.000, 0.230, 0.230, 0.230), 73: (0.000, 0.240, 0.240, 0.240),
        74: (0.000, 0.240, 0.240, 0.240), 75: (0.000, 0.260, 0.260, 0.260),
        76: (0.000, 0.250, 0.250, 0.250), 77: (0.000, 0.220, 0.220, 0.220),
        78: (0.000, 0.240, 0.240, 0.240), 79: (0.000, 0.240, 0.240, 0.240),
        80: (0.000, 1.000, 1.000, 1.000)}},
    "annual probability of retirement",
    f"PRIMARY: {VRS_VAL_APX} 'State Employees Retirement Rates, Plan 1 Members', Appendix to the "
    "June 30, 2025 Annual Actuarial Valuation Reports, p.53. Rates are 0.000 for all ages <= 49.",
    "Transcribed in full. Service bands are as published: 0-4, 5-9, 10-29, 30+.", "")

RETIREMENT_RATES_PLAN2_AGE60PLUS = I({
    "male": {60: 0.080, 61: 0.070, 62: 0.090, 63: 0.100, 64: 0.100, 65: 0.180, 66: 0.210,
             67: 0.200, 68: 0.210, 69: 0.220, 70: 0.210},
    "female": {60: 0.080, 61: 0.080, 62: 0.100, 63: 0.100, 64: 0.110, 65: 0.190, 66: 0.210,
               67: 0.210, 68: 0.200, 69: 0.200, 70: 0.200}},
    "annual probability of retirement, service >= 5",
    f"PRIMARY: {VRS_VAL_APX} 'State Employees Retirement Rates, Plan 2 and Hybrid Members', "
    "Appendix to the June 30, 2025 Annual Actuarial Valuation Reports, pp.54-55.",
    "The published Plan 2 / Hybrid table is age x exact years of service. Its structure is: zero "
    "below service 5; from age 60 the rate depends on age alone; below age 60 the rate is a flat "
    "8.0% once age + service reaches 89, i.e. the year in which the member crosses the Rule of 90. "
    "Encoded that way rather than as an 18-column grid, which is the same thing and auditable.",
    "")
RETIREMENT_RATE_PLAN2_RULE90 = I(0.080, "annual probability of retirement",
    f"PRIMARY: {VRS_VAL_APX} pp.54-55 — the single pre-age-60 rate in the Plan 2 / Hybrid table.",
    "Applies when service >= 5 and age + service >= 89.", "")
RETIREMENT_RATES_AGE71PLUS = I({"male": 0.210, "female": 0.200}, "annual probability",
    "DERIVED: the published Plan 2 / Hybrid table is truncated in the appendix extract at age 70. "
    "Extended flat from the age-70 rate, with 100% retirement assumed at 80, matching the published "
    "Plan 1 table's own structure (0.20-0.25 through the 70s, 1.000 at 80+).",
    "Affects only members already past 70, who are a negligible share of the eligible pool.",
    "Immaterial: fewer than 1% of the modelled pool.")

TERMINATION_RATES_STATE = I({
    "male": {0: 0.1860, 1: 0.1510, 2: 0.1240, 3: 0.1040, 4: 0.0970, 5: 0.0870, 6: 0.0780,
             7: 0.0710, 8: 0.0640, 9: 0.0550, 10: 0.0460, 11: 0.0460, 12: 0.0410, 13: 0.0390,
             14: 0.0390, 15: 0.0380, 16: 0.0350, 17: 0.0340, 18: 0.0310, 19: 0.0310, 20: 0.0310},
    "female": {0: 0.2120, 1: 0.1740, 2: 0.1450, 3: 0.1200, 4: 0.1070, 5: 0.0960, 6: 0.0870,
               7: 0.0800, 8: 0.0720, 9: 0.0640, 10: 0.0590, 11: 0.0560, 12: 0.0550, 13: 0.0500,
               14: 0.0480, 15: 0.0460, 16: 0.0400, 17: 0.0400, 18: 0.0380, 19: 0.0380,
               20: 0.0380}},
    "annual probability of termination, by completed years of service",
    f"PRIMARY: {VRS_VAL_APX} 'State Employees Termination Rates, Male & Female', Appendix to the "
    "June 30, 2025 Annual Actuarial Valuation Reports, p.56. Key 20 = '20+'.",
    "Used to project the active stock forward through the pilot (red team F2: 'no aging/inflow "
    "simulation advances the stock of active members through the pilot') and, in the "
    "counterfactual, to move a member to a deferred vested benefit rather than a service "
    "retirement.", "")

# ---- 16.2 plan tier from MEMBERSHIP TENURE, not total service --------------
# Red team F2: "total service includes purchased/ported service and does not establish first
# membership date."  So tenure = total service - purchased/ported service, and the tier boundaries
# are applied to TENURE.
TIER_TENURE_BOUNDS = I({"plan1_min_tenure": 17.5, "plan2_min_tenure": 11.5},
    "years of membership tenure at 2025-06-30",
    "DERIVED from statute and VRS plan definitions: Plan 1 requires membership before 7/1/2010 AND "
    "vesting (5 years) as of 1/1/2013, i.e. membership by 1/1/2008, i.e. tenure >= 17.5 years at "
    f"6/30/2025. Hybrid is membership on/after 1/1/2014, i.e. tenure < 11.5 years. See {VRS_HB1} "
    f"p.14 and {VRS_HB2} p.14.",
    "NOTE: this CORRECTS the MOO-7 model, which used a single 15.0-year cut on TOTAL service. The "
    "binding Plan 1 condition is the 1/1/2013 vesting test, not the 7/1/2010 membership date, so "
    "the Plan 1 floor is 17.5 years of tenure and not 15.0.",
    "The old 15.0 cut on total service OVERSTATED the Plan 1 population and, more importantly, "
    "hid the Plan 2 members the red team found in Pathway B.")

PURCHASED_SERVICE_DIST = I({"share_with_none": 0.85, "max_years_if_any": 4.0},
    "distribution of purchased/ported/granted service included in reported total service",
    "JUDGMENT: central 85% of members hold none; conditional on holding some, uniform on (0, 4] "
    "years. Defensible range for share_with_none: 70% to 95%. VRS does not publish the "
    "distribution of purchased service across the active population.",
    "Used to convert each (age, total service) cell into TIER SHARES rather than a hard tier "
    "assignment, by integrating over this distribution. Mean purchased service = 0.30 years.",
    "A LARGER purchased-service allowance moves more members across the 11.5 and 17.5-year tenure "
    "boundaries from Plan 1 into Plan 2 and Hybrid. That ENLARGES the Plan 2 Pathway A population "
    "the red team identified and therefore RAISES modelled cost. Tested in the tornado.")

# ---- 16.3 the retirement condition actually in the brief (red team F1) -----
RETIREMENT_DEADLINE_MONTHS = I(6, "months after the later of purchase completion and eligibility",
    "PRIMARY: the two-page brief section 2, as quoted in the MOO-15 red team document F1 — "
    "'retirement within six months of completing the purchase, once eligibility is met'.",
    "This REPLACES the MOO-7 convention of (first eligibility without the purchase + 2 years - 6 "
    "months). The red team's rerun of the MOO-7 code with this deadline, holding the MOO-7 cohort "
    "fixed, moved S1 central net pension liability from $2.903m to $7.041m.",
    "The deadline is the single largest correction in this repair. A LONGER permitted delay lowers "
    "the liability, because the member accrues more service and commences later.")

PURCHASE_COMPLETION_MONTHS = I({"low": 0, "central": 12, "high": 36},
    "months from election to completion of payment",
    "JUDGMENT anchored on PRIMARY payment machinery: VRS permits a lump sum (90 days to remit) or "
    f"a purchase payment agreement by payroll deduction ({VRS_ERM} p.17). Central 12 months, "
    "defensible 0 (lump sum) to 36 (long agreement).",
    "A pro-rata credit on incomplete payment is assumed (memo 4.2, after N.Y. R.S.S.L. 1000(6)), so "
    "an incomplete purchase is not modelled as forfeiture.",
    "LONGER completion delays retirement and therefore LOWERS the liability. The low case (lump "
    "sum, immediate retirement) is the expensive one.")

PILOT_ELECTION_WINDOW = I({"open": "2027-07-01", "close": "2031-06-30"}, "dates",
    "DERIVED from PILOT_FY: elections may be made in any month of the four pilot fiscal years.",
    "Elections are spread across the 48 pilot months using PILOT_PHASING by fiscal year and "
    "uniformly within each fiscal year. This replaces the MOO-7 treatment, which priced every "
    "participant at the 6/30/2025 snapshot.", "")

VALUATION_DATE = I("2025-06-30", "date", f"PRIMARY: {VRS_VAL} p.12 and p.50 — the census date.",
    "All ages and service in AGE_SERVICE_TABLE are as of this date. The pilot opens 24 months "
    "later, so the stock must be advanced 24 months before the first election month.", "")

# ---- 16.4 workforce offset: zero in the headline (red team F6/F7) ---------
SCORE_WORKFORCE_OFFSET_IN_HEADLINE = I(False, "boolean",
    "DECISION TAKEN BY POLICY DIRECTOR, 2026-10-11 comment on MOO-31, acting on red team F6/F7: "
    "'Score zero assumed workforce savings in the headline for every scenario. Report the offset "
    "separately as a sensitivity, with the selected-cohort effects shown.'",
    "The repaired headline net state cost is therefore: net incremental pension liability + VRS "
    "implementation cost. No workforce term. The offset is reported in its own table and is never "
    "netted into a scenario headline.",
    "This RAISES every headline figure relative to MOO-7 and is the conservative direction.")

# ---- 16.5 the cap as an admission rule (red team F3) ----------------------
CAP_ADMISSION_RULE = I("reserve-then-admit", "rule",
    "DIRECTION from red team F3: 'For S7 reserve a VRS-certified subsidy before accepting an "
    "election; deny/wait-list when the remaining appropriation is insufficient.'",
    "Implemented as: elections arrive in month order; for each, VRS certifies the subsidy (gross "
    "liability increase less the member payment); if the remaining appropriation covers it the "
    "election is accepted and the appropriation is decremented, otherwise the applicant is denied "
    "and counted. The cap therefore binds on ADMISSIONS, and the reported liability is the "
    "liability of admitted elections only.",
    "")
CAP_QUEUE_ORDER = I(["chronological", "cheapest_first", "dearest_first"], "labels",
    "DESIGN PARAMETER. Red team F12 notes 'under S7 well-advised members reserve funds first', so "
    "the ordering is not neutral and all three are reported.",
    "'chronological' is the stated central case. 'dearest_first' is the adverse-selection case.",
    "'dearest_first' serves the fewest members for the same money; 'cheapest_first' the most.")

# ---- 16.6 GF allocation fix -----------------------------------------------
IMPLEMENTATION_IS_NGF = I(True, "boolean",
    "CORRECTION noted by the red team: the MOO-7 headline multiplied the nongeneral-fund-only "
    "$375,000 VRS implementation allowance by the 47% general fund share, unlike its own "
    "fiscal-year table. VRS administrative cost is nongeneral fund.",
    "Removing that allocation changes GF PV from about $1.584m to about $1.408m on MOO-7's own "
    "inputs. The repaired model never applies GF_SHARE to the implementation allowance.", "")


# ============================================================================
# 17. MOO-31 REPAIR, part 2 — sub-cell resolution.
#     The MOO-7 model put every member of a cell at the BAND MID-POINT (age 52,
#     service 27).  That makes eligibility flip for a whole band at once, and it
#     forces an all-or-nothing tier assignment at the 17.5-year tenure boundary.
#     Both are artefacts, and both matter for the repaired monthly cohort.
# ============================================================================
SUBCELL_AGE_STEP = I(1.0, "years",
    "DERIVED: the published age bands are 1 to 5 years wide; members are spread uniformly across "
    "the integer ages inside each band so that the band total is preserved exactly.",
    "'70+' is spread over ages 70-75.", "")

SUBCELL_SERVICE_POINTS = I({
    "0-4": [(0.5, 0.2), (1.5, 0.2), (2.5, 0.2), (3.5, 0.2), (4.5, 0.2)],
    "5-9": [(5.5, 0.2), (6.5, 0.2), (7.5, 0.2), (8.5, 0.2), (9.5, 0.2)],
    "10-14": [(10.5, 0.2), (11.5, 0.2), (12.5, 0.2), (13.5, 0.2), (14.5, 0.2)],
    "15-19": [(15.5, 0.2), (16.5, 0.2), (17.5, 0.2), (18.5, 0.2), (19.5, 0.2)],
    "20-24": [(20.5, 0.2), (21.5, 0.2), (22.5, 0.2), (23.5, 0.2), (24.5, 0.2)],
    "25-29": [(25.5, 0.2), (26.5, 0.2), (27.5, 0.2), (28.5, 0.2), (29.5, 0.2)],
    "30+": [(30.5, 0.40), (32.5, 0.25), (34.5, 0.16), (36.5, 0.11), (38.5, 0.08)]},
    "service value and share, within each published service band",
    "DERIVED for the five closed bands (uniform across the band, which preserves the band total "
    "exactly). JUDGMENT for the open '30+' band: a declining profile, because long-service counts "
    "thin out and VRS does not publish the shape above 30 years. Defensible alternatives run from "
    "uniform to a steeper decline.",
    "The 30+ shape matters only for Pathway B members, who buy 1 year each, so its effect on the "
    "answer is small; tested in the tornado.",
    "A FLATTER 30+ profile puts more weight on very long service, which raises the benefit base "
    "and therefore raises cost.")

SUBCELL_MIN_ENTRY_AGE = I(18.0, "years",
    "DERIVED: a member cannot have more years of service than (age - 18). Sub-cells violating "
    "that are dropped and the cell's weight is renormalised over the survivors, so every "
    "published cell total is still reproduced exactly.", "", "")


# ============================================================================
# 18. MOO-31 REPAIR, part 3 — the drafting ambiguity the repair exposed.
# ============================================================================
PATHWAY_A_SCOPE = I("immediate", "rule",
    "DRAFTING AMBIGUITY, not an assumption. The two-page brief does not say which of these two "
    "readings of Pathway A it intends, and the answer changes the score by a factor of about four:\n"
    "  'immediate' - Pathway A is confined to members whom a purchase of available military "
    "service makes unreduced-eligible AT ONCE. The purchase is a bridge to retirement now.\n"
    "  'advance'   - any member whose unreduced-eligibility DATE the purchase brings forward at "
    "all may elect, buy now, and retire when that earlier date arrives. The brief's own deadline "
    "language ('within six months of completing the purchase, ONCE ELIGIBILITY IS MET') "
    "contemplates exactly this gap, so the broad reading is textually supported.",
    "The repaired model reports 'immediate' as the headline, because it is the reading that "
    "matches the brief's framing of a retirement bridge and the reading MOO-7 intended, so the "
    "comparison against the published S0-S7 table stays meaningful. 'advance' is reported "
    "alongside it as drafting exposure, every time.",
    "'advance' is far more expensive: it admits members a decade from eligibility, each buying the "
    "full four years. This is a question for Statutory Researcher and Drafting Specialist, not a "
    "number for the modeller to choose. It must be resolved in the bill text.")


# ============================================================================
# 19. MOO-38 — VRS's PUBLISHED FIXED-RATE EARLY-RETIREMENT REDUCTION FACTORS.
#     MOO-31 derived the reduction as the ACTUARIALLY EQUIVALENT one on the
#     model's own basis, on the stated ground that "VRS publishes no factor
#     table".  That ground was wrong.  VRS publishes the rule and the tables,
#     and VRS does not use actuarial equivalence.  Everything below is PRIMARY.
#     Purely ADDITIVE: `python3 main.py` and `python3 v2_main.py` are untouched.
# ============================================================================
VRS_EM_SR = "https://employers.varetire.org/media/shared/pdf/er-manual-service-retirement.pdf"
VRS_BAC26 = "https://www.varetire.org/media/members/pdf/board/materials/2026/bac-06-17-26.pdf"

ERF_METHOD_BASIS = I("fixed_rate_published", "rule",
    f"PRIMARY: {VRS_BAC26} p.14 — \"VRS currently uses fixed-rate reductions.\"  p.16 — \"VRS uses "
    "fixed-rate reductions. Three different fixed-rate tables are required... Flat percentage "
    "reduction from Normal Retirement age to age of early commencement.\"  p.15 — \"Fixed rate "
    "reduction factors often include a subsidy or provide a slightly more valuable benefit than a "
    "true actuarial equivalent, meaning the employer covers some of the cost of the earlier "
    "retirement.\"  GRS's review, same deck: the factors are \"well within common practice among "
    "State retirement systems both in terms of the use of simple factors and the subsidies "
    "provided.\"",
    "This REPLACES the MOO-31 assumption that the reduction is actuarially equivalent. The "
    "alternative label 'actuarial_equivalent_derived' is retained ONLY so MOO-31's published S9 "
    "numbers stay regenerable as a regression lock.",
    "Resolved against a published rule, so there is no remaining direction of error on the METHOD. "
    "The two residual ambiguities are ERF_UNREDUCED_BASIS (open) and ERF_COMPOSITION (settled by "
    "the published table).")

ERF_TIER1_RATE = I(0.005, "reduction per month, first 60 months",
    f"PRIMARY: {VRS_EM_SR} p.4 — \"A 0.5% reduction is applied for the first 60 months\"; "
    f"{VRS_BAC26} pp.19-21 — \"Reduction of 0.5% for each month prior to unreduced retirement age "
    "for the first 60 months\".", "Identical for Plan 1, Plan 2/Hybrid and Enhanced Hazardous Duty.", "")

ERF_TIER2_RATE = I(0.004, "reduction per month thereafter",
    f"PRIMARY: {VRS_EM_SR} p.4 — \"4/10 of 1% for any additional months the member needs to meet "
    f"age or service requirements for an unreduced benefit\"; {VRS_BAC26} p.19 — \"0.4% reduction "
    "for the next 60 months\", p.21 — \"0.4% reduction thereafter\".", "", "")

ERF_TIER1_MONTHS = I(60.0, "months", f"PRIMARY: {VRS_EM_SR} p.4; {VRS_BAC26} pp.19-21.", "", "")

ERF_TIER2_MONTHS = I(60.0, "months",
    f"PRIMARY: {VRS_BAC26} p.19 — \"0.4% reduction for the NEXT 60 MONTHS\", i.e. the ladder is "
    "capped at 120 months total and the deepest 55/5-style reduction is 30% + 24% = 54%, a floor "
    f"factor of 0.4600.  The Employer Manual's \"any additional months\" ({VRS_EM_SR} p.4) states "
    "no cap, but the cap is what reproduces the published ages 50-54 rows and the manual's own "
    "phrasing never binds for a 55/5 member (at most 120 months from 55 to 65).",
    "Binds only on Plan 1 members retiring under 50/10 who are more than 120 months from their "
    "unreduced age.", "Removing the cap makes the reduction deeper and the S9 waiver worth MORE.")

ERF_SUB55_RATE = I(0.006, "additional reduction per month under age 55, Plan 1 50/10 only",
    f"PRIMARY: {VRS_EM_SR} p.4, 50/10 — \"Plus An additional reduction of 6/10 of 1% for each month "
    f"the member is younger than 55\"; {VRS_BAC26} p.19 — \"From age 55: 0.6% reduction for each "
    "month prior to age 55 back to age 50\".",
    "This is the 50/10 additional factor MOO-31 §5.4 recorded as not quantifiable from public "
    "data. It is published, and it is quantified here.",
    "Applies to Plan 1 only. Plan 2 and Hybrid have no 50/10 reduced retirement at all "
    f"({VRS_EM_SR} p.4: \"Plan 2 and Hybrid  Age 60 with at least 5 years of service.\").")

ERF_COMPOSITION = I("ba_2026", "rule",
    f"PRIMARY, SETTLED: {VRS_BAC26} p.19.  'ba_2026' = the 0.5%/0.4% ladder capped at 120 months, "
    "then MULTIPLIED by (1 - 0.006 x months under 55).  This is the only candidate reading that "
    "reproduces the published ages 50-54 factors: at age 54, 0.4600 x (1 - 0.072) = 0.4269 "
    "(published 0.4269), against 0.3880 capped-additive, 0.3823 uncapped-multiplicative and "
    "0.3400 for the Employer Manual read literally (uncapped, additive).  The published 50-54 "
    "factors fall on an exact straight line of -0.03312 per year = -0.4600 x 0.072, which is the "
    "multiplicative form and nothing else.",
    "This ANSWERS MOO-37 records-request question A2 from public documents. The request is still "
    "worth sending for confirmation, but the reprice is not blocked on it.",
    "'manual_literal' (uncapped ladder, additive 0.6% term) is priced alongside as the alternative "
    "reading. It makes the reduction DEEPER, so the waiver is worth MORE and S9 dearer.")

ERF_UNREDUCED_BASIS = I("projected", "rule",
    "AMBIGUITY, OPEN — and for the S9 cohort it dominates ERF_COMPOSITION by an order of "
    "magnitude.  The ERF is measured back from 'the unreduced retirement age', and neither source "
    "says whether that age is found on PROJECTED service (what the member would have reached had "
    "they kept working) or FROZEN service (what they actually hold at commencement).  Every row of "
    f"all three published tables ({VRS_BAC26} pp.19-21) sits on a diagonal — service = age - 35 "
    "for Plan 1 and Haz Duty, service = 23 for Plan 2 — where the two readings give the SAME "
    "unreduced age, so the tables cannot discriminate.  The only explicit textual signal is the "
    f"60/5 rule ({VRS_EM_SR} p.4): \"the first date on which the member WOULD HAVE completed 30 "
    "years of service and the age plus service equal 90\" — projected.",
    "'projected' is central for two reasons: it is the only reading either source states "
    "explicitly, and it reproduces the unreduced-age arithmetic MOO-31 already used "
    "(s9.unreduced_age_frozen projected service despite its name), so this reprice changes ONE "
    "thing — the factor — and the move in the headline is attributable to it.",
    "DOMINANT UNRESOLVED DRIVER for S9. 'frozen' makes the reduction far deeper (Plan 1 aged 52 "
    "with 27 years: 0.3606 frozen against 0.6429 projected), so the waiver is worth MORE, the "
    "member price under the actuarial rule is HIGHER, and S9 is DEARER. Raised as a new open item "
    "for MOO-37; both are priced every time.")

SSNRA = I(67.0, "age",
    f"PRIMARY: {VRS_EM_SR} p.3 — \"1960 and later ... 67\"; {VRS_BAC26} p.21 header \"1960 or "
    "Later\".",
    "Every member of the S9 pilot cohort born 1960 or later retires on a 67 SSNRA. Plan 2 and "
    "Hybrid members in the pilot are all younger than that cohort boundary.", "")
