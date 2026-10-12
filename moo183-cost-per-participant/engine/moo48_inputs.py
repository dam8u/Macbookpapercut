"""
MOO-48 input block — the bill as drafted, the deadline ladder, the corrected certified-subsidy
basis, and the per-member ceiling solved for a stated floor.

ADDITIVE ONLY.  `inputs.py`, `moo45_inputs.py`, `v2_*.py`, `s8.py` are all untouched, so
`python3 main.py`, `python3 s8s9_main.py`, `python3 v2_main.py`, `python3 moo38_main.py` and
`python3 moo45_main.py` still reproduce their published tables.  Every assumption introduced for
MOO-48 lives here with a value, a unit, a source or an explicit JUDGMENT label, and a direction of
error.

Retrieval date for every source cited below: 2026-10-11.
Primary legal source throughout: `bill-text-s8` (MOO-42), the drafted § 51.1-142.4 and the
conforming amendments to § 51.1-142.2.  Quoted clause text is copied from that document verbatim.
"""

def I(value, unit, source, note="", direction=""):
    return {"value": value, "unit": unit, "source": source, "note": note, "direction": direction}


# ============================================================================
# 1.  THE COHORT THE BILL ADMITS
# ============================================================================
PATHWAY_SET = I(("A",), "tuple of pathway labels",
    'PRIMARY: § 51.1-142.4 A, "eligible member" clause (v) — a member who "is not eligible, on the '
    'date the member files a complete application, for an unreduced service retirement allowance '
    'under § 51.1-153 without the service credit to be purchased". A member who is already '
    "unreduced-eligible is Pathway B by construction in v2_cohort.classify, so clause (v) removes "
    "Pathway B from the bill entirely.",
    "Every published S8 figure prices Pathways A and B together. This is the single largest "
    "difference between the published figures and the bill: Pathway B is 43.9 of the 62.2 "
    "modelled S8-at-6% participants (70%).",
    "Dropping Pathway B LOWERS cost. It is already drafted, so this is a correction to the "
    "published figures, not a policy option.")

PATHWAY_A_SCOPE_BILL = I("immediate", "rule",
    'PRIMARY: § 51.1-142.4 A, "eligible member" clause (vi) — the member "would be eligible for an '
    'unreduced service retirement allowance under § 51.1-153 on the first day of the month '
    'following the month in which the service credit to be purchased is credited". A member whose '
    "eligibility date merely moves forward is not eligible on that date. Reinforced by subsection "
    "C clause (ii), which caps the purchase at the credit the member NEEDS to be eligible. "
    "ADOPTED as policy intent by MOO-46 Decision 3.1 (narrow reading).",
    "Confirmation that clause (vi) forecloses the broad reading against the live text of "
    "§ 51.1-153 is MOO-49, assigned to Statutory Researcher. This model does not interpret the "
    "statute; it prices the reading the Policy Director has adopted and prices the broad reading "
    "alongside it as drafting exposure, every time.",
    "The broad ('advance') reading is 3.7x on the repaired S1 basis ($19.05M against $5.12M, "
    "v2 out_v2_pathwayA_scope.csv). The exposure is one-sided and large.")


# ============================================================================
# 2.  THE RETIREMENT DEADLINE — what the bill actually requires
# ============================================================================
# § 51.1-142.4 A, "qualifying retirement":
#   "a service retirement under § 51.1-153 with an effective date of retirement that is the first
#    day of the month following the month in which the Board credits to the member all of the
#    service credit purchased under the member's election, except that the Board may approve a
#    later effective date of retirement, not more than 90 days after that date, where the Board's
#    own processing requirements make the earlier date impracticable."
# § 51.1-142.4 E:
#   payment must be complete "no later than 12 months after the date the Board accepts the
#   election"; the Board "shall credit the purchased service credit to the member only upon receipt
#   of payment in full, and shall do so within 30 days after receipt of payment in full."
#
# So the chain is: election -> payment complete (<= 12 months, inputs.PURCHASE_COMPLETION_MONTHS)
#                           -> credit posted (<= 1 month)
#                           -> retire the first of the NEXT month
#                           -> plus up to 90 days of Board processing discretion.
#
# The v2 liability engine takes the deadline as months AFTER the later of completion and
# eligibility (v2_liability.pv_with_design), which is exactly the bill's structure once the
# crediting lag and the month-boundary rule are collapsed into one number.
BILL_DEADLINE_MONTHS = I({"low": 0, "central": 1, "high": 4}, "months after purchase completion",
    "DERIVED from the three drafted clauses quoted above. Central 1 month = the crediting lag "
    "(up to 30 days, § 51.1-142.4 E) plus the month-boundary rule, collapsed to one month. Low 0 "
    "months = credit posts and retirement takes effect inside the same month, the fastest the "
    "drafted text permits. High 4 months = 1 month plus the 90 days of Board discretion the "
    '"qualifying retirement" definition grants.',
    "MOO-46 Decision 1.5 calls the bill's requirement 'effectively 0 months, the most expensive "
    "setting on the ladder'. That is right to within one rung: the bill is rung 1, its own "
    "drafted range is rungs 0 to 4, and rung 0 is reported here so the Director's reading is "
    "priced as well as mine. The difference between rung 0 and rung 1 is small and is reported.",
    "A SHORTER deadline RAISES cost. Rung 0 is the dearest cell the bill can produce.")

DEADLINE_LADDER_MONTHS = I([0, 1, 6, 12, 18, 24], "months after purchase completion",
    "REQUESTED: MOO-46 Decision 1.5 and the MOO-48 assignment ask for 0 / 6 / 12 / 18 / 24. Rung "
    "1 is added because it is the bill as drafted (BILL_DEADLINE_MONTHS) and the ladder is "
    "useless to the decision if it does not contain the status quo.",
    "The ladder moves the retirement deadline ONLY. Clause (vi) and subsection C clause (ii) are "
    "held as drafted, so the cohort does not change across the ladder. That is the right way to "
    "read a deadline amendment: a patron who lengthens the deadline does not thereby admit "
    "members who are not eligible when the credit posts. If clause (vi) were relaxed in the same "
    "motion the cohort moves to the broad reading and the ladder does not apply - priced "
    "separately and flagged.",
    "Monotone and large: longer deadline -> more service accrued, later commencement, less "
    "acceleration -> LOWER cost.")

DEADLINE_COHORT_HELD_FIXED = I(True, "boolean",
    "SCOPE DECISION, stated so it can be attacked. The ladder holds the eligible-member "
    "definition at the drafted narrow reading for every rung.",
    "The alternative - that a longer retirement deadline implies a longer eligibility window, so "
    "that members who become eligible within the deadline may elect - is the broad reading by "
    "another route. It is priced as a named variant (the 'deadline window' variant) rather than "
    "left silent, because a drafter who lengthens the deadline without touching clause (vi) and a "
    "drafter who lengthens both produce very different bills.",
    "The window variant is DEARER at every rung beyond 0 and the gap grows with the rung.")


# ============================================================================
# 3.  CERTIFIED SUBSIDY — the drafted definition and the corrected one
# ============================================================================
# § 51.1-142.4 A, "certified subsidy", as drafted:
#   "the full actuarial equivalent cost, determined under subdivision B 3 of § 51.1-142.2, of the
#    service credit to be purchased, PLUS the actuarial cost to the retirement system of the
#    earlier commencement of the retirement allowance that the Board determines will result from
#    the election, LESS the amount payable by the member and by any employer under subdivision
#    B 4 of § 51.1-142.2."
CERTIFIED_SUBSIDY_BASIS = I("corrected_single_basis", "label",
    "ADOPTED: MOO-46 Decision 2(d) — the definition 'must be a single-basis measure of the "
    "increase in liability to the retirement system attributable to the election, less member and "
    "employer payments.'",
    "On this model's ledger that quantity is exactly\n"
    "    CS_corrected = gross_liability_increase - member_payment - employer_payment\n"
    "               where gross_liability_increase = PV(benefit | the election)\n"
    "                                              - PV(benefit | VRS's own decrements, no election)\n"
    "and employer_payment = 0 in S8 by construction (there is no employer differential; that is "
    "S4). It carries NO double count: the service-credit component and the early-commencement "
    "component are measured against the same counterfactual and sum to the gross increase "
    "(v2_liability.participant_ledger).\n"
    "The drafted definition is also computed, as\n"
    "    CS_drafted = aec_full(§ 51.1-142.2 B 3 quote) + early_commencement_component - paid\n"
    "and the difference between the two is reported per member and in aggregate. The overlap is "
    "the eligibility-acceleration term that the B 3 quote already contains (VRS employer manual, "
    "purchase of prior service, p.11: the quote buys 'the increase in the employee's future "
    "retirement benefit OR EARLIER RETIREMENT ELIGIBILITY DATE') and that the second drafted term "
    "then adds a second time.",
    "CS_drafted >= CS_corrected for every cell in this cohort, so the corrected basis is the "
    "LOOSER ceiling basis for a given dollar figure. A ceiling figure carried over from the "
    "drafted basis without redrafting the definition would bind on fewer members than intended - "
    "the error MOO-45 §2.5 warned about, now quantified on the bill's own cohort.")

EMPLOYER_PAYMENT = I(0.0, "dollars per election",
    "PRIMARY: § 51.1-142.4 and the conforming § 51.1-142.2 B 4 create no employer contribution. "
    "An employer MAY pay on the member's behalf (§ 51.1-142.4 G 2 (ii) refers to 'any employer "
    "that paid on the member's behalf'), but nothing requires it and no appropriation funds it.",
    "So 'less the amount payable by the member and by any employer' = less the member's S8 price. "
    "If agencies did pay, the certified subsidy falls dollar for dollar and the appropriation "
    "stretches further; that is S4, which is not this bill.",
    "Any employer payment LOWERS certified subsidy and raises the number of elections the "
    "appropriation funds. Zero is the conservative (dearest) assumption.")


# ============================================================================
# 4.  THE CAP, THE CEILING AND THE FLOOR RULE
# ============================================================================
AGGREGATE_CAP = I(3_000_000, "dollars of certified subsidy reserved over the pilot",
    "PRIMARY: § 51.1-142.4 D 2 as drafted — 'The aggregate of all certified subsidies reserved "
    "under this section shall not exceed $3,000,000.' CONFIRMED at this figure by MOO-46 "
    "Decision 2(b), whose meaning is 'the appropriation the Commonwealth is asked to make, not a "
    "prediction of cost'.", "", "")

CEILING_FLOOR_RULE = I({"elections": 30, "order": "dearest_first", "cap": 3_000_000},
    "elections; queue order; dollars",
    "ADOPTED: MOO-46 Decision 2(e) — 'the lowest round figure that guarantees the appropriation "
    "funds at least 30 elections in the adverse (dearest-first) order, and that touches no "
    "Pathway B election' (second limb moot while Pathway B is out of the bill).",
    "TWO PROBLEMS WITH THE RULE AS WRITTEN, both reported rather than silently resolved:\n"
    " (1) Direction. A LOWER ceiling funds MORE elections, so the set of ceilings satisfying the "
    "     floor is an interval running down from a maximum, and 'the lowest round figure' "
    "     satisfying it is $0. The figure the rule is reaching for is the HIGHEST round figure "
    "     that still meets the floor - the least intrusive ceiling consistent with 30 elections. "
    "     That is what is solved for, and both readings are shown in the sweep.\n"
    " (2) Feasibility. 30 elections is compared below against the size of the modelled cohort. "
    "     If the cohort is smaller than 30 at the relevant take-up, no ceiling can satisfy the "
    "     floor and the rule returns nothing; the deliverable then has to restate the floor. The "
    "     answer is reported either way and the Director decides.",
    "A HIGHER ceiling is better for the member and worse for the election count. The two limbs of "
    "the rule pull in opposite directions by construction.")

CEILING_ROUND_FIGURES = I([10_000, 20_000, 25_000, 30_000, 40_000, 50_000, 60_000, 70_000, 75_000,
                           80_000, 90_000, 100_000, 110_000, 120_000, 125_000, 130_000, 140_000,
                           150_000, 160_000, 175_000, 200_000, 250_000],
    "dollars per member",
    "JUDGMENT: 'round figure' is read as a figure a drafter would write into a Code section - "
    "multiples of $10,000, with the $25,000/$75,000/$125,000/$175,000 quarter points included.",
    "The solved figure is reported together with the full sweep so the Director can see how much "
    "the answer moves between adjacent round figures.", "")

CAP_METERING_BASIS = I("nominal_at_certification", "label",
    "PRIMARY: § 51.1-142.4 D 1-D 3. The Board certifies a dollar amount and RESERVES it against a "
    "$3,000,000 aggregate before accepting the election. A reservation is a nominal dollar "
    "commitment made on the certification date; nothing in the drafted text discounts it.",
    "This differs from the repaired model's own cap-admission rule (v2_scenarios.aggregate), "
    "which meters discounted dollars against the cap. Both are computed. The nominal basis is the "
    "one the clause describes and is used for every elections-funded figure reported here; the "
    "discounted basis is reported alongside it because it is what the published F3 table used.",
    "Nominal metering exhausts the appropriation FASTER than PV metering (elections late in the "
    "pilot are discounted by up to 6 years at 6.75%), so the nominal basis funds FEWER "
    "elections. Nominal is the conservative reading and it is also the drafted one.")

CONTINGENCY_RESERVE = I({"low": 0.0, "central": 0.10, "high": 0.10}, "fraction of certified subsidy",
    "PRIMARY: § 51.1-142.4 D 3 — the Board 'shall also reserve, IN ADDITION TO each certified "
    "subsidy, a contingency amount ... sufficient in the Board's judgment to fund the "
    "recertification required by subdivision 6.' D 6 triggers recertification when the certified "
    "subsidy would increase by more than 10 percent, so 10 percent is the figure the drafted text "
    "itself implies. JUDGMENT as to the amount; the clause leaves it to the Board.",
    "A DRAFTING EXPOSURE FOUND IN THIS RUN, not previously reported. D 2 caps 'the aggregate of "
    "all certified subsidies' at $3,000,000. The D 3 contingency is reserved IN ADDITION to each "
    "certified subsidy, so on the face of the text it sits OUTSIDE the $3,000,000 cap while still "
    "requiring the D 3 confirmation that appropriated funds are sufficient. Either the "
    "appropriation must exceed $3,000,000 by the contingency, or the contingency must be drafted "
    "inside the cap and the number of elections funded falls by about a tenth. Both are priced; "
    "the drafting choice belongs to the Drafting Specialist.",
    "A contingency inside the cap REDUCES elections funded by roughly the contingency rate. A "
    "contingency outside the cap RAISES the appropriation the fiscal statement must request.")


# ============================================================================
# 5.  THE NON-RETIREMENT MECHANISM — what § 51.1-142.4 G actually does
# ============================================================================
# G 2: if the member does not retire in a qualifying retirement the Board shall "(i) reduce the
#      service credit credited to the member under the election to the amount of service credit
#      that the member's payments would have purchased under subdivision B 3 of § 51.1-142.2 on
#      the date the Board accepted the election, (ii) refund ... any amount paid in excess ...,
#      and (iii) release the reservation."
# G 4: G 2 does NOT apply, and the credit vests at the pilot price, if the member "(i) dies,
#      (ii) is approved for a disability retirement allowance ..., or (iii) is separated from
#      employment other than by the member's own choice or for cause."
G2_NEUTRALISES_THE_WINDFALL = I(True, "boolean",
    "PRIMARY: § 51.1-142.4 G 2 as quoted above, read with F ('no other consequence shall attach').",
    "FISCAL READING of the mechanism, which is what this model can speak to: a member who does "
    "not retire keeps only the credit their payment buys at the current-law B 3 price, so the "
    "price discount is unwound in kind rather than collected as a debt, and no acceleration "
    "occurs because the member did not retire. Trust cost for that member is therefore "
    "approximately ZERO, and the reservation is released back into the $3,000,000 pool. The "
    "Policy Director's second reason for a longer deadline is sound on the drafted text, and "
    "stronger than stated: G 2 does not merely avoid a collection problem, it removes the "
    "windfall cost almost entirely. The residual is the drift between the B 3 price on the "
    "acceptance date and the B 3 price when the reduction is made up to 13 months later, which is "
    "second-order and is NOT priced here.\n"
    "THE EXCEPTION THAT IS NOT NEUTRALISED is G 4. Death, disability and involuntary separation "
    "vest the credit at the pilot price with no reduction, and the G-4 window is exactly the "
    "election-to-required-retirement window, so it GROWS with the deadline. The exposed "
    "population is counted at every rung of the ladder. The cost per G-4 event is not priced: "
    "survivor-option and disability benefits are outside this model's valuation (stated caveat, "
    "unchanged since MOO-7).",
    "G 2 makes non-retirement CHEAP. G 4 makes a longer deadline slightly DEARER than the ladder "
    "shows, by an amount this model cannot value.")

WINDFALL_BOUND_DEFINITION = I("svc_component_less_member_paid", "label",
    "CARRIED FORWARD from the repaired model (v2_main.windfall_bound): trust cost if the purchase "
    "induced no acceleration at all - the service-credit component alone, less what the member "
    "paid.",
    "This is the bound MOO-46 Decision 1.5 cites as $775,330 against $5,123,905 on repaired S1. "
    "It is recomputed here on the BILL's cohort, which is the comparison the deadline decision "
    "needs. NOTE that on the bill's own text the windfall bound OVERSTATES the windfall, because "
    "G 2 reduces the credit of a member who does not retire (see above). The bound is the right "
    "measure of 'the member keeps working and keeps cheap credit'; it is the wrong measure of "
    "'the member does not retire', which G 2 handles.", "")


# ============================================================================
# 6.  TIMING, FUNDS AND LOCAL EFFECT
# ============================================================================
PILOT_FY_ELECTIONS = I([2030, 2031, 2032, 2033], "fiscal years of election",
    "CARRIED FORWARD UNCHANGED from moo45_inputs.PILOT_FY_RELABELLED: delayed effective date of "
    "July 1, 2029 (MOO-6 Rule 4), expiry July 1, 2033.", "Pure re-label of the published layout.",
    "")

VRS_IMPLEMENTATION_FY = I(2029, "fiscal year",
    "CARRIED FORWARD UNCHANGED from moo45_inputs.VRS_IMPLEMENTATION_FY_RELABELLED.",
    "FY2029 carries the systems charge and no elections; FY2030 is the first election year; "
    "FY2031 is the first year carrying amortised liability.", "")

LOCAL_COST = I(0.0, "dollars",
    'PRIMARY: § 51.1-142.4 A — "Eligible member" expressly excludes "a teacher, or an employee of '
    'a political subdivision", and clause (i) requires a state employee. The bill reaches the '
    "State Employee plan only.",
    "NO LOCAL COST AND NO UNFUNDED MANDATE. No new duty is placed on any locality, school "
    "division or political subdivision, and no local employer contribution rate is affected. "
    "This finding is unchanged from the repaired model (v2_main §8) and is restated here because "
    "it is a finding in its own right, not a footnote.",
    "One-sided: there is no mechanism in the drafted text by which a locality incurs cost.")

GF_SHARE_APPLIES_TO = I("amortisation_only", "label",
    "CARRIED FORWARD from inputs.GF_SHARE (47%) and inputs.IMPLEMENTATION_IS_NGF (True).",
    "The 47% general-fund share is applied to the amortisation of trust cost only. The VRS "
    "implementation allowance is nongeneral fund in full and is never multiplied by 47% - the "
    "error the red team found in MOO-7's headline.", "")

PRECISION_RULE = I(2, "significant figures",
    "ADOPTED: MOO-46 Decision 4 (the four lower-stakes calls) — two significant figures on every "
    "dollar figure in anything leaving the team.",
    "Full decimals live in the CSVs for chart reproducibility only. The console transcript prints "
    "whole dollars so the CSVs can be checked against it; the DOCUMENT rounds to two significant "
    "figures.", "")
