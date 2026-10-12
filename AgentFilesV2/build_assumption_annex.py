"""V2 assumption-bounding annex.

Replaces the three sourceless dials in the fiscal model with published figures
where published figures exist, and says plainly where they still do not.
Sources: DHRM presentation to Senate Finance and Appropriations, 3 Feb 2026
(data as of 30 June 2025); BLS Employment Situation of Veterans, 2025 annual
averages; VRS Purchase of Prior Service pages; VRS Annual Actuarial Valuation
June 30 2025. All retrieved 12 October 2026.
"""
import render

# ---------------------------------------------------------------- source facts
# DHRM, 3 Feb 2026 presentation, slide 11 - classified workforce veteran field
DHRM_VET = 0.06
DHRM_NOT_VET = 0.25
DHRM_UNKNOWN = 0.69
DHRM_KNOWN = DHRM_VET + DHRM_NOT_VET                      # 0.31
VET_OF_KNOWN = DHRM_VET / DHRM_KNOWN                      # 0.19355

# BLS Employment Situation of Veterans, 2025 annual averages, Table 2A
# employed, thousands
BLS = {
    "18 and over": (8_042, 153_469),
    "45 to 54":    (1_830, 30_474),
    "55 to 64":    (2_085, 24_520),
    "65 and over": (1_120, 10_254),
}
share = {k: v / (v + nv) for k, (v, nv) in BLS.items()}
BASE_SHARE = share["18 and over"]
factor = {k: s / BASE_SHARE for k, s in share.items()}

F5564 = factor["55 to 64"]
F4554 = factor["45 to 54"]

# Age-adjusted cohort veteran share, applied to the DHRM bracket
FLOOR_ADJ = DHRM_VET * F5564
CEIL_ADJ = VET_OF_KNOWN * F5564
FLOOR_ADJ_CONS = DHRM_VET * F4554

# Published model figures (V2-fiscal-model, unchanged by this annex)
MODEL_LOW, MODEL_MID, MODEL_HIGH = 0.06, 0.08, 0.10
PARTS_LOW, PARTS_MID, PARTS_HIGH = 17, 42, 86

def rescale(share_value):
    """Participants scale linearly in veteran share, all else at mid."""
    return PARTS_MID * share_value / MODEL_MID

# VRS Annual Actuarial Valuation June 30 2025, p.50 - derived in V2-fiscal-model
ACTIVE_STATE = 81_274
PLAN1, PLAN2 = 20_872, 8_122
IN_SCOPE = PLAN1 + PLAN2                                  # 28,994
BEYOND_P1, BEYOND_P2 = 0.284, 0.040
BEYOND = PLAN1 * BEYOND_P1 + PLAN2 * BEYOND_P2            # ~6,253
BEYOND_OF_SCOPE = BEYOND / IN_SCOPE
BEYOND_OF_ACTIVE = BEYOND / ACTIVE_STATE
PURCHASABLE = 2_396
PURCHASABLE_OF_ACTIVE = PURCHASABLE / ACTIVE_STATE

# DHRM, slide 12 - FY25 retention measures
DHRM_ELIG_TODAY = 0.051
DHRM_ELIG_2YR = 0.090
DHRM_RET_RATE = 0.009
DHRM_TURNOVER = 0.128
DHRM_VACANCY = 0.130

ELIG_RATIO = BEYOND_OF_ACTIVE / DHRM_ELIG_TODAY

# DHRM, slide 11 - ages
AGE_WORKFORCE = 46.1
AGE_NEW_HIRE = 39.1
SERVICE_AVG = 8.5
AGE_GAP = AGE_WORKFORCE - AGE_NEW_HIRE

# Virginia Military Factbook (Secretary of Veterans and Defense Affairs) and
# ACS 2020-2024 - both dated, both flagged in the text
VA_RETIREES = 158_280
VA_VETERANS = 629_500
RETIREE_SHARE = VA_RETIREES / VA_VETERANS

pc = lambda x, d=1: f"{100*x:.{d}f}%"

B = [
 ("title", "V2 assumption annex — bounding the three dials that have no source"),
 ("sub", "Prepared 12 October 2026 · Policy Director · companion to V2-fiscal-model · "
         "primary sources only, all retrieved 12 October 2026 · "
         "INTERNAL — no figure in the published model is changed by this annex"),

 ("h1", "0. Why this annex exists"),
 ("p", "The V2 fiscal model publishes participant counts of **"
       f"{PARTS_LOW} / {PARTS_MID} / {PARTS_HIGH}** over the four-year pilot. Those counts are the "
       "product of three dials. Two of the three had no published source at all, and I said so in "
       "the model: the **veteran share** of the eligible population and the **qualifying-service "
       "share**. The third, **take-up**, you set by decision at 5 / 12 / 25%."),
 ("p", "I have now found published Commonwealth and federal figures that bound the veteran-share "
       "dial on both sides, and that cross-check two other things the model asserts. **The finding "
       "is not that the model is wrong in method. It is that the model's veteran-share range sits "
       "at the very bottom of the defensible range, and the published mid of "
       f"{PARTS_MID} participants is more likely a floor than a central estimate.**"),
 ("note", "**Nothing in this annex changes a published figure.** The model, the scenario tables and "
          "the slider page all still read "
          f"{PARTS_LOW} / {PARTS_MID} / {PARTS_HIGH}. Rebasing them moves every headline number in "
          "material that has already gone out, so it is a decision for you, not a correction I make "
          "quietly. Section 7 states the decision."),

 ("h1", "1. The sources, and what each one is"),
 ("table", "Table 1 — Every source used in this annex", [
    ["Source", "What it is", "Date of data"],
    ["DHRM, *State Employee Workforce, Compensation, Health Benefits* — presentation to "
     "Senate Finance and Appropriations", "Primary Commonwealth source. Slide 11 demographics, "
     "slide 12 FY25 retention measures", "30 June 2025 (presented 3 Feb 2026)"],
    ["BLS, *Employment Situation of Veterans*, Table 2A", "Primary federal source. Employment by "
     "veteran status and age", "2025 annual averages"],
    ["BLS, same release, Table 8", "Employed veterans by class of worker", "August 2025"],
    ["VRS, *Purchase of Prior Service — Types of Service*", "The eligibility rule for active duty "
     "military service", "Retrieved 12 Oct 2026"],
    ["VRS, *Annual Actuarial Valuation, June 30 2025*, p.50", "Age x service table for active State "
     "Employees — the model's own denominator", "30 June 2025"],
    ["Virginia Military Factbook, Secretary of Veterans and Defense Affairs",
     "Military retiree count. **Dated — c.2018 data** and used only for order of magnitude",
     "c. 2018"],
 ]),
 ("p", "The Census ACS API now requires a registered key, which I did not create. Every figure "
       "below comes from the sources in Table 1, none of which needed an account."),

 ("h1", "2. Finding 1 — DHRM's 6% is a floor, not a veteran share"),
 ("p", "DHRM publishes the veteran composition of the classified state workforce as of 30 June 2025 "
       "as three numbers, and the third one is the story:"),
 ("table", None, [
    ["Veteran status field", "Share of classified workforce"],
    ["Veteran", f"**{pc(DHRM_VET,0)}**"],
    ["Not a veteran", pc(DHRM_NOT_VET, 0)],
    ["**Unknown**", f"**{pc(DHRM_UNKNOWN,0)}**"],
 ]),
 ("p", f"**{pc(DHRM_UNKNOWN,0)} of the field is unknown.** So {pc(DHRM_VET,0)} is not an estimate of "
       "the veteran share of the state workforce. It is the share of the *whole* workforce that has "
       "been positively identified as veteran. The veteran share of the workforce is bounded below "
       f"by {pc(DHRM_VET,0)} and above by {pc(DHRM_VET + DHRM_UNKNOWN,0)}."),
 ("p", "The useful middle reading is to assume the unknowns resemble the knowns. Among the "
       f"{pc(DHRM_KNOWN,0)} whose status is recorded, the veteran share is "
       f"{DHRM_VET:.0%} / {DHRM_KNOWN:.0%} = **{pc(VET_OF_KNOWN)}**."),
 ("note", "**I would not take 19.4% as the central estimate, and here is the reason against my own "
          "argument.** Virginia gives veterans a hiring preference and, under DHRM Policy 4.10, "
          "service credit toward annual leave for military service. Both give a veteran a concrete "
          "reason to disclose that a non-veteran does not have. Disclosure is therefore almost "
          "certainly not random — veterans are over-represented among those who answered. That makes "
          f"{pc(VET_OF_KNOWN)} a **ceiling** on the unknowns-resemble-knowns reading, not a midpoint."),
 ("p", f"**Defensible bracket for the whole classified workforce: {pc(DHRM_VET,0)} to "
       f"{pc(VET_OF_KNOWN)}.** The model's dial runs 6 / 8 / 10%. Its *high* case is barely above "
       "the floor."),

 ("h1", "3. Finding 2 — the pathways target the one age band where veterans are most concentrated"),
 ("p", "The Retirement Bridge and the Retirement Incentive both aim at members at or near unreduced "
       "retirement. That is, deliberately, the oldest band in the plan. Veterans are not evenly "
       "spread across ages, and BLS publishes the gradient."),
 ("table", "Table 2 — Veteran share of the employed population by age, 2025 annual averages "
           "(BLS Table 2A, thousands)", [
    ["Age band", "Employed veterans", "Employed nonveterans", "Veteran share",
     "Ratio to all ages"],
 ] + [[k, f"{BLS[k][0]:,}", f"{BLS[k][1]:,}", pc(share[k], 2),
       f"**{factor[k]:.2f}x**" if k != "18 and over" else "1.00x"]
      for k in ["18 and over", "45 to 54", "55 to 64", "65 and over"]]),
 ("p", f"At ages 55 to 64 the veteran share of employed people is **{pc(share['55 to 64'],2)}** "
       f"against **{pc(BASE_SHARE,2)}** across all ages — a factor of **{F5564:.2f}x**. At 65 and "
       f"over it is {factor['65 and over']:.2f}x. The effect is a cohort one, not a Virginia one, "
       "and it runs in the same direction as Finding 1."),
 ("note", "BLS Table 8 also reports that **12.9% of employed veterans work in state or local "
          "government** and 13.9% in federal government, against 67.2% in the private sector "
          "(August 2025). Veterans are over-represented in public employment relative to the "
          "workforce as a whole. I have not quantified that effect because the comparable nonveteran "
          "class-of-worker distribution is not in the same table, and I will not estimate it."),

 ("h1", "4. The two findings combined — and what they do to the published counts"),
 ("p", "Applying the age factor to the DHRM bracket gives the veteran share of the cohort the "
       "pathways actually reach:"),
 ("table", "Table 3 — Age-adjusted veteran share of the target cohort", [
    ["Reading", "Workforce share", "Age factor", "Cohort veteran share",
     "Participants at mid take-up"],
    ["Model low", pc(MODEL_LOW, 0), "none applied", pc(MODEL_LOW, 1),
     f"{rescale(MODEL_LOW):.0f}"],
    ["Model mid *(published)*", pc(MODEL_MID, 0), "none applied", pc(MODEL_MID, 1),
     f"**{PARTS_MID}**"],
    ["Model high", pc(MODEL_HIGH, 0), "none applied", pc(MODEL_HIGH, 1),
     f"{rescale(MODEL_HIGH):.0f}"],
    ["DHRM floor, conservative age band (45-54)", pc(DHRM_VET, 0), f"{F4554:.2f}x",
     pc(FLOOR_ADJ_CONS), f"{rescale(FLOOR_ADJ_CONS):.0f}"],
    ["**DHRM floor, 55-64 band**", f"**{pc(DHRM_VET,0)}**", f"**{F5564:.2f}x**",
     f"**{pc(FLOOR_ADJ)}**", f"**{rescale(FLOOR_ADJ):.0f}**"],
    ["Unknowns resemble knowns, no age factor", pc(VET_OF_KNOWN), "none applied",
     pc(VET_OF_KNOWN), f"{rescale(VET_OF_KNOWN):.0f}"],
    ["**Unknowns resemble knowns, 55-64 band — ceiling**", f"**{pc(VET_OF_KNOWN)}**",
     f"**{F5564:.2f}x**", f"**{pc(CEIL_ADJ)}**", f"**{rescale(CEIL_ADJ):.0f}**"],
 ]),
 ("p", "Participants scale linearly in the veteran share, so the rightmost column is simple "
       f"rescaling of the published mid of {PARTS_MID} with take-up and qualifying-service held at "
       "mid. Read the table as a range, not as seven estimates."),
 ("note", f"**The single sentence that matters: the model's high case of {pc(MODEL_HIGH,0)} is "
          f"almost exactly the DHRM floor once the age band is accounted for ({pc(FLOOR_ADJ)}).** "
          "Everything above that line in Table 3 is outside the range the model currently shows. "
          f"The published mid of {PARTS_MID} is, on these sources, between "
          f"{rescale(FLOOR_ADJ)/PARTS_MID:.1f}x and {rescale(CEIL_ADJ)/PARTS_MID:.1f}x too low."),

 ("h1", "5. Finding 3 — I had the VRS military-pension rule wrong, in two ways"),
 ("p", "I have been describing the eligibility condition as *no military pension*. The VRS rule as "
       "published says something narrower and more useful. Quoting the Types of Service page:"),
 ("note", "*The service must be full-time service of at least 180 consecutive days, and at the time "
          "of purchase it must not* **qualify you for a military pension** *in any federally "
          "established branch of the armed services or reserve components.* **Exception:** *if you "
          "were in the U.S. Armed Forces Reserves or the National Guard, you may purchase up to 48 "
          "months of active duty military service* **even if it will be used to qualify you for a "
          "military pension.**"),
 ("p", "Two corrections follow, and they point in opposite directions."),
 ("ul", [
    "**The test is about the service, not the person.** It asks whether the months being purchased "
    "qualify the member for a military pension — not whether the member happens to draw one. "
    "A veteran with a military pension earned on *other* service is not automatically barred.",
    "**Reserve and National Guard service is expressly carved out of the test.** A Reserve or Guard "
    "member may purchase active-duty periods even where those periods count toward a reserve "
    "pension. So the rule does not exclude reserve-component retirees at all.",
 ]),
 ("p", "The practical effect is that the exclusion bites on **regular-component retirees** — the "
       "twenty-year active-duty career, whose active service is precisely what earned the pension. "
       "Virginia has an unusually large retiree population: the Virginia Military Factbook puts "
       f"military retirees at **{VA_RETIREES:,}** against roughly **{VA_VETERANS:,}** veterans, "
       f"about **{pc(RETIREE_SHARE,0)}**. The Factbook figure is c.2018 and I use it only for order "
       "of magnitude."),
 ("note", "**I will not put a number on this adjustment.** It removes regular-component retirees and "
          "only those, and we hold no figure for the regular/reserve split inside the Virginia state "
          "workforce. It is a real downward pressure on Findings 1 and 2 and it is unquantified. "
          "It is now a data-request item."),

 ("h1", "6. Two cross-checks the model has to survive, and one it currently fails"),

 ("h2", "6.1 DHRM publishes a retirement-eligibility rate, and ours is about 1.5x it"),
 ("p", "DHRM slide 12 reports, for the classified workforce in FY25:"),
 ("table", None, [
    ["DHRM FY25 retention measure", "Published"],
    ["Eligible to retire today", f"**{pc(DHRM_ELIG_TODAY)}**"],
    ["Eligible to retire within 2 years", f"**{pc(DHRM_ELIG_2YR)}**"],
    ["Retirement rate", pc(DHRM_RET_RATE)],
    ["Turnover rate", pc(DHRM_TURNOVER)],
    ["Vacancy rate", pc(DHRM_VACANCY)],
 ]),
 ("p", "The model's own derivation says "
       f"**{BEYOND:,.0f}** Plan 1 and Plan 2 state employees are already beyond the unreduced "
       f"threshold. That is {pc(BEYOND_OF_SCOPE)} of the {IN_SCOPE:,} in-scope members, and "
       f"**{pc(BEYOND_OF_ACTIVE)}** of all {ACTIVE_STATE:,} active State Employees. DHRM publishes "
       f"{pc(DHRM_ELIG_TODAY)}. **Ours is {ELIG_RATIO:.2f}x the Commonwealth's own published "
       "figure.**"),
 ("p", "The caveats are genuine and they do not dispose of it. DHRM's denominator is the *classified* "
       "workforce, which is not the same set as VRS-covered active State Employees — it excludes "
       "wage employees and much of higher education. DHRM does not publish whether *eligible* means "
       "unreduced or includes reduced retirement; if it includes reduced, the gap is worse, not "
       "better. Either way:"),
 ("note", "**A hostile fiscal-note reader will find 5.1% in a Senate Finance presentation and set it "
          "against our 7.7%.** This has to be reconciled with DHRM before the fiscal note, not "
          "after. It is the one number in the model that a published Commonwealth source appears to "
          "contradict."),
 ("p", "The *combined* reach figure survives the same test much better. Already beyond "
       f"({pc(BEYOND_OF_ACTIVE)}) plus the purchasable Bridge pool of {PURCHASABLE:,} "
       f"({pc(PURCHASABLE_OF_ACTIVE)}) is {pc(BEYOND_OF_ACTIVE + PURCHASABLE_OF_ACTIVE)} reachable "
       f"within four years, against DHRM's {pc(DHRM_ELIG_2YR)} within two. Those are consistent. "
       "The problem is specific to the already-eligible component."),

 ("h2", "6.2 DHRM's average service corroborates the derived denominator"),
 ("p", f"DHRM reports average years of service of **{SERVICE_AVG} years** and average age "
       f"**{AGE_WORKFORCE}**. The Hybrid plan opened on 1 July 2014, so a Hybrid member holds at "
       "most about eleven years of service. An average of 8.5 years across the whole classified "
       "workforce is only possible if the workforce is heavily Hybrid-weighted."),
 ("p", f"That is independent support for the derived in-scope count of **{IN_SCOPE:,}** Plan 1 and "
       "Plan 2 state employees over the earlier pro-rata estimate of about 39,000, and for the "
       "finding that state service is more Hybrid-weighted than the system as a whole. Two "
       "unrelated sources now agree."),

 ("h1", "7. Three Virginia figures that replace guesses in Ledger 3"),
 ("p", "The workforce ledger used assumed replacement salaries of 80 / 85 / 90% and assumed 1 / 3 / "
       "5% of vacated posts not refilled. DHRM publishes figures that bear directly on both."),
 ("table", "Table 4 — What DHRM's published figures do to Ledger 3", [
    ["DHRM figure", "Value", "What it does to the ledger"],
    ["Average age of the classified workforce", f"{AGE_WORKFORCE} years",
     "Baseline for the departing participant"],
    ["**Average age of new hires and rehires**", f"**{AGE_NEW_HIRE} years**",
     f"A replacement is on average **{AGE_GAP:.1f} years younger** than the person leaving. This is "
     "a Virginia source for the replacement-salary assumption, which until now was a judgment. "
     "80-90% of the departing salary is consistent with a 7-year-younger hire; it is not generous."],
    ["**Vacancy rate**", f"**{pc(DHRM_VACANCY,0)}**",
     "Agencies already cannot fill 13% of posts. Against that, assuming only 1-5% of *vacated* "
     "posts go unfilled is strongly conservative. The ledger understates this line."],
    ["Turnover rate FY25", pc(DHRM_TURNOVER),
     "Down from 15.6% in FY21. The workforce is stabilising, so the pilot's retirements would not "
     "be lost in noise — they are measurable, which G22 needs"],
    ["Retirement rate FY25", pc(DHRM_RET_RATE),
     f"About {ACTIVE_STATE*DHRM_RET_RATE:,.0f} retirements a year at this scale. A pilot of "
     f"{PARTS_MID} over four years is roughly {PARTS_MID/4/(ACTIVE_STATE*DHRM_RET_RATE):.1%} of "
     "annual retirements — small enough that VRS cannot call it a demographic shock"],
 ]),

 ("h1", "8. The hardest thing in this annex, and it is not a number"),
 ("p", "DHRM's own key messages, on the same slides, are these. I quote them because they are the "
       "argument against our bill and they come from the agency we have just written to:"),
 ("note", "*Attracting and retaining talent is critical, ongoing focus.* · *Service retirements "
          "continue to be above average.* · *Mid-level to higher level professionals and managers.* "
          "· *Workforce planning and knowledge transfer critical.*"),
 ("p", "DHRM is on record that it is already losing more senior people than it wants to, that the "
       "losses are concentrated in exactly the mid-to-senior professional grades our two pathways "
       "target, and that knowledge transfer is its stated worry. **A bill whose declared purpose is "
       "to accelerate senior retirements runs straight into the Commonwealth's own published "
       "workforce concern.**"),
 ("p", "That is worth knowing before the DHRM reply arrives rather than after. Three consequences:"),
 ("ol", [
    "**Stop describing the workforce effect as a saving first.** Led with, it reads as headcount "
    "reduction dressed as veteran policy, and DHRM has already said that is its problem, not its "
    "goal. Ledger 3 stays in the model and stops being a selling point.",
    "**Lead on succession instead.** The pilot converts unplanned, unpredictable senior attrition "
    "into a *dated, voluntary, six-month-notice* transition. A known retirement date is worth more "
    "to a workforce planner than an avoided one, and it is the only thing in this bill DHRM "
    "actually needs. G22's reporting is what proves it.",
    "**Expect DHRM to be the sceptical reader, not VRS.** We built this expecting the pension cost "
    "to be the fight. On DHRM's published position, the workforce argument is the softer flank.",
 ]),
 ("p", "This does not change a goal and it does not change a figure. It changes the order of the "
       "argument in the one-pager and the advocacy brief, and both were written before I had read "
       "this slide deck."),

 ("h1", "9. The dial that still has no source at all"),
 ("p", "The **qualifying-service share** — of veterans in the state workforce, what fraction hold at "
       "least some active-duty service of 180+ consecutive days that is purchasable and not already "
       "purchased. The model runs it at 35 / 50 / 65%."),
 ("p", "Nothing in this annex touches it. It remains the weakest number in the model, and as the "
       "scenario tables showed, it moves the answer more than take-up does: holding take-up at mid "
       "and sweeping this dial alone takes participants from 29 to 54. **There is no published "
       "figure, federal or Commonwealth, that bounds it.** Only VRS's own records can close it, "
       "which is why it is in the data request."),
 ("p", "Two things now press on it in opposite directions. The 180-consecutive-day rule and the "
       "regular-component pension exclusion push it down. The Reserve and Guard carve-out in "
       "Finding 3 pushes it up, because reserve service that counts toward a reserve pension is "
       "still purchasable — a category I had wrongly assumed was excluded."),

 ("h1", "10. Four items for the data request, and the decision I need from you"),
 ("p", "The letters to VRS and DHRM carry thirteen items. These findings add four. The letters have "
       "not been reissued — if they have not yet gone out, say so and I will fold these in; if they "
       "have, these go in the follow-up."),
 ("table", "Table 5 — New data-request items", [
    ["#", "Item", "Which finding it closes"],
    ["14", "Of the 69% of the classified workforce whose veteran-status field is unknown, is any "
           "part recoverable — from DD-214s already held for the Policy 4.10 annual-leave service "
           "credit, from the hiring-preference record, or from a one-time voluntary survey?",
     "Finding 1. This is the single cheapest way to replace the widest assumption in the model"],
    ["15", "The veteran-status breakdown **by age band**, not just in total, for the classified "
           "workforce",
     "Finding 2. Would replace the national age factor with a Virginia one"],
    ["16", "Of identified veteran state employees, how many hold **regular-component** military "
           "retired pay, and how many **reserve-component**? The VRS rule treats them differently",
     "Finding 3. Currently unquantified in both directions"],
    ["17", "The definition behind *eligible to retire today — 5.1%* and *within 2 years — 9.0%*: "
           "unreduced only or including reduced, and over which population",
     "Finding 6.1. Without it we cannot tell whether our 7.7% contradicts DHRM or merely measures "
     "something else"],
 ]),

 ("h1", "11. The decision"),
 ("p", "On these sources the model's veteran-share dial of 6 / 8 / 10% is anchored at the floor of "
       "the defensible range rather than through its middle. Three ways to handle that, and they "
       "are genuinely different bets:"),
 ("table", "Table 6 — What to do about the veteran-share dial", [
    ["Option", "What changes", "The argument for it", "The argument against"],
    ["**(a) Leave every published figure alone.** Carry this annex as the stated limitation and let "
     "VRS's answer rebase the model once",
     "Nothing. 17 / 42 / 86 stand",
     "Figures that have already gone out stay stable. One rebase, on VRS's data, not two on ours. "
     "The direction of the error is conservative, which is the right direction for an advocacy "
     "model to err",
     "We are publishing a mid case we now believe is low. If a fiscal note is built on 42 and the "
     "real number is 100, the pilot's cap and administrative estimate are both wrong"],
    ["**(b) Rebase the dial** to roughly 9 / 15 / 30% and republish the model and scenario tables",
     f"Every headline moves. Mid goes from {PARTS_MID} to about {rescale(0.15):.0f}",
     "The published range would then actually contain the answer",
     "It moves figures the letters already reference, and it rests on a national age factor applied "
     "to a Virginia floor — defensible, but it is our arithmetic, not anyone's data"],
    ["**(c) Keep the published range and add a fourth *sourced ceiling* column** alongside it",
     "Nothing moves. One column is added everywhere",
     "Honest about the width without destabilising anything. Shows a reader we found the ceiling "
     "ourselves",
     "A four-case model is harder to carry into a meeting than a three-case one"],
 ]),
 ("note", "**My recommendation is (c).** The reason is G16 — one basis per figure. Option (b) would "
          "replace a stated assumption with a different assumption of our own construction and "
          "present it as an improvement; the age factor is real but it is federal, and the floor it "
          "multiplies is a Virginia artefact of a 69% unknown field. Option (a) leaves us publishing "
          "a number we no longer believe. Option (c) publishes both and names which is which, which "
          "is what G23 and G25 actually ask of us."),
 ("hr",),
 ("p", "*Sources, all retrieved 12 October 2026. DHRM, State Employee Workforce, Compensation, "
       "Health Benefits — presentation to the Senate Finance and Appropriations Committee, "
       "3 February 2026, slides 10-13 (data as of 30 June 2025). U.S. Bureau of Labor Statistics, "
       "Employment Situation of Veterans — 2025, Tables 2A and 8. Virginia Retirement System, "
       "Purchase of Prior Service: Types of Service, and Cost Windows. Virginia Retirement System, "
       "Annual Actuarial Valuation, June 30 2025, p.50. Virginia Military Factbook, Secretary of "
       "Veterans and Defense Affairs (c.2018 data, used for order of magnitude only). "
       "DHRM Policy 4.10 policy guide, Veteran's Service Credit for Annual Leave.*"),
]

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    scratch = os.environ.get("PAPERCLIP_RUN_SCRATCH_DIR", "/tmp")
    render.to_docx(B, os.path.join(here, "V2-assumption-annex.docx"))
    render.to_pdf(B, os.path.join(here, "V2-assumption-annex.pdf"), scratch)
    print("built V2-assumption-annex .docx + .pdf")
    print(f"  vet of known           {VET_OF_KNOWN:.4%}")
    print(f"  age factor 55-64       {F5564:.4f}x")
    print(f"  floor adjusted         {FLOOR_ADJ:.4%}  -> {rescale(FLOOR_ADJ):.1f} participants")
    print(f"  ceiling adjusted       {CEIL_ADJ:.4%}  -> {rescale(CEIL_ADJ):.1f} participants")
    print(f"  beyond threshold       {BEYOND:,.0f} = {BEYOND_OF_ACTIVE:.4%} of active")
    print(f"  vs DHRM 5.1%           {ELIG_RATIO:.3f}x")
