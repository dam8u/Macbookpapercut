"""Builds the VaLORS pre-score annex. Figures come from valors_model.py, so the
annex and the model cannot drift."""
import os
from pathlib import Path

import render
import valors_model as M

HERE = Path(__file__).parent
SCRATCH = os.environ.get("PAPERCLIP_RUN_SCRATCH_DIR") or os.environ.get("PAPERCLIP_SCRATCH_DIR") or "/tmp"

inc, br = M.cohorts()
inc_p, br_p = M.cohorts(allow_vesting_route=True)
pool = inc["n"] + br["n"]
f1 = inc["p1"] / inc["n"]
rate_inc = f1 * M.ANC["p1"] + (1 - f1) * M.ANC["p2"]
per_inc = rate_inc * inc["salary"]
per_br = 2.0 * M.ANC["p1"] * br["salary"]

low = M.funnel(0.06, 0.35, 0.05)
mid = M.funnel(0.08, 0.50, 0.12)
high = M.funnel(0.10, 0.65, 0.25)
t5, t12, t25 = (M.funnel(0.08, 0.50, t) for t in (0.05, 0.12, 0.25))
rf2 = M.roll_forward(2.0)
rf4 = M.roll_forward(4.0)

mid_sal = (mid["inc_parts"] * mid["inc_salary"] + mid["br_parts"] * mid["br_salary"]) / mid["participants"]

D = lambda x: f"${x:,.0f}"
N1 = lambda x: f"{x:,.1f}"

# ------------------------------------------------------------------ SPORS
SPORS_TABLE = {
    "Under 20": ([0] * 7, 0, 0),
    "20-24": ([129, 0, 0, 0, 0, 0, 0], 129, 8_124_027),
    "25-29": ([168, 88, 0, 0, 0, 0, 0], 256, 18_251_963),
    "30-34": ([72, 138, 63, 0, 0, 0, 0], 273, 21_799_044),
    "35-39": ([43, 59, 166, 12, 0, 0, 0], 280, 24_526_548),
    "40-44": ([20, 24, 68, 104, 70, 0, 0], 286, 28_963_359),
    "45-49": ([18, 12, 24, 37, 115, 47, 1], 254, 28_112_303),
    "50-54": ([5, 4, 22, 13, 57, 100, 13], 214, 26_015_540),
    "55-59": ([2, 2, 12, 18, 18, 32, 52], 136, 17_398_368),
    "60": ([2, 0, 1, 2, 2, 3, 6], 16, 1_839_634),
    "61": ([0, 0, 0, 1, 2, 1, 3], 7, 835_785),
    "62": ([1, 1, 0, 1, 1, 1, 6], 11, 1_431_911),
    "63": ([0, 1, 3, 4, 0, 0, 3], 11, 1_275_451),
    "64": ([0, 0, 1, 1, 0, 0, 10], 12, 1_618_600),
    "65": ([0, 0, 0, 0, 1, 1, 4], 6, 896_410),
    "66": ([0, 0, 0, 0, 0, 0, 3], 3, 424_941),
    "67": ([0, 0, 0, 0, 0, 1, 5], 6, 926_280),
    "68": ([0, 0, 0, 0, 0, 1, 1], 2, 285_971),
    "69": ([0] * 7, 0, 0), "70 & Over": ([0] * 7, 0, 0),
}
_saved = M.VALORS
M.VALORS = SPORS_TABLE
s_inc, s_br = M.cohorts()
s_low, s_mid, s_high = (M.funnel(v, q, t) for v, q, t in
                        ((0.06, 0.35, 0.05), (0.08, 0.50, 0.12), (0.10, 0.65, 0.25)))
s_f1 = s_inc["p1"] / s_inc["n"]
s_per_inc = (s_f1 * M.ANC["p1"] + (1 - s_f1) * M.ANC["p2"]) * s_inc["salary"]
s_per_br = 2.0 * M.ANC["p1"] * s_br["salary"]
M.VALORS = _saved

# State Employees figures, carried from V2-fiscal-model (not recomputed here)
ST = {"parts_mid": 41.5, "pay_mid": 554_922, "per_inc": 10_514, "per_br": 20_806,
      "pool": 8_650, "denom": 28_994, "parts_low": 17.3, "parts_high": 86.5,
      "pay_low": 231_218, "pay_high": 1_156_088}

B = []
A = B.append

A(("title", "Annex — Virginia Law Officers (VaLORS) pre-score"))
A(("sub", "A priced amendment held in reserve · Policy Director · MOO-100 · 12 October 2026 · "
          "internal, pre-decisional"))
A(("p", "**Status: reserve document. Not part of the bill, not part of the fiscal note, not for "
        "circulation.** The board decided on 12 October 2026 to exclude the State Police Officers', "
        "Virginia Law Officers' and Judicial Retirement Systems from the pilot, expressly in the bill "
        "text. On 12 October 2026 the board further decided to price a VaLORS amendment now, before it "
        "is offered on the floor, rather than after. This annex is that price. It is produced so that "
        "the answer to “what would it cost to add law officers?” is a number we already hold, "
        "not a number the other side supplies."))
A(("p", "Built on the same method as V2-fiscal-model, from the same source of record, with the same "
        "three dials at the same settings. Only the plan changes. Figures are computed by the same "
        "code, so this annex and the model cannot drift apart."))
A(("hr",))

A(("h1", "0. The answer in four lines"))
A(("table", None, [
    ["", "Low", "Mid", "High"],
    ["VaLORS participants added over the four-year pilot", N1(low["participants"]),
     f"**{N1(mid['participants'])}**", N1(high["participants"])],
    ["Member payments into the trust fund", D(low["member_payments"]),
     f"**{D(mid['member_payments'])}**", D(high["member_payments"])],
    ["Trust-fund subsidy at k = 2.0", D(low["member_payments"]),
     f"**{D(mid['member_payments'])}**", D(high["member_payments"])],
    ["Increase over the bill as scoped — participants",
     f"+{100*low['participants']/ST['parts_low']:.1f}%",
     f"**+{100*mid['participants']/ST['parts_mid']:.1f}%**",
     f"+{100*high['participants']/ST['parts_high']:.1f}%"],
    ["Increase over the bill as scoped — member payments",
     f"+{100*low['member_payments']/ST['pay_low']:.1f}%",
     f"**+{100*mid['member_payments']/ST['pay_mid']:.1f}%**",
     f"+{100*high['member_payments']/ST['pay_high']:.1f}%"],
]))
A(("p", "**The amendment is small, and the reason is the plan's own eligibility rules, not our "
        "drafting.** VaLORS is a young, high-turnover workforce — average age 39.6, average total "
        "service 8.3 years — and its unreduced-retirement rules are age 60 with five years or age 50 "
        "with 25 years. Only " + f"{pool:,.0f} of 7,459 members ({100*pool/7459:.1f}%)" + " sit in "
        "either pathway. The comparable figure for the State Employees plan is "
        f"{ST['pool']:,} of {ST['denom']:,} ({100*ST['pool']/ST['denom']:.1f}%)" + " — nearly four "
        "times the rate."))
A(("p", "**So the sympathetic amendment is also an affordable one, and that is the single most useful "
        "sentence in this annex.** At mid take-up, adding 7,459 law officers to the pilot adds about "
        f"{mid['participants']:.0f} participants and about {D(mid['member_payments'])} of member "
        "payments over four years. We should be able to say that in a committee room without "
        "reaching for a calculator."))
A(("p", "What we cannot say is what it costs the trust fund, for the same reason we cannot say that "
        "for the bill as scoped: the actuarial-equivalent-to-approximate-normal-cost ratio, k, is "
        "unknown and only VRS can supply it. Everything below is expressed in member payments and "
        "in k."))
A(("hr",))

A(("h1", "1. Why VaLORS is structurally different from the plan we scoped"))
A(("h2", "1.1 There is no VaLORS Hybrid — the whole plan is in scope"))
A(("p", "This is the finding that most changes how a VaLORS amendment should be read. Hazardous-duty "
        "positions are not eligible for the Hybrid Retirement Plan. A VaLORS member whose membership "
        "date is on or after 1 July 2010 is in **Plan 2**, even if the date is after 31 December 2013. "
        "So all 7,459 active VaLORS members are Plan 1 or Plan 2, and a bill naming Plan 1 and Plan 2 "
        "reaches every one of them."))
A(("p", "In the State Employees plan the Hybrid tier absorbs 52,280 of 81,274 members — 64% — and the "
        "Plan 1/Plan 2 denominator is only 28,994. **A reader who assumes the same 36% in-scope "
        "fraction applies to VaLORS will understate the VaLORS denominator by about 2.8×.** It does "
        "not change the answer in section 0, because the binding constraint is eligibility and not "
        "tier, but it is the kind of error that gets made out loud."))
A(("table", "Table 1 — plan-tier split, derived. Hazardous duty has no Hybrid tier, so one cut at "
            "15.0 years of total service separates the tiers and it falls exactly on a published "
            "band boundary. No band has to be split.", [
    ["Tier", "Members", "Average salary", "Basis"],
    ["VaLORS Plan 1", f"{M.tier_split()[0]:,.0f}", D(M.tier_split()[1]),
     "Hired before 1 July 2010 → total service ≥ 15.0 yr at 30 June 2025"],
    ["VaLORS Plan 2", f"{M.tier_split()[2]:,.0f}", D(M.tier_split()[3]),
     "Everyone else. No Hybrid tier exists for hazardous duty"],
    ["Total — the whole plan is in scope", "**7,459**", "$58,011", "VRS valuation, p. 49"],
]))

A(("h2", "1.2 The eligibility rules are different, and they are what makes the amendment small"))
A(("p", "VaLORS Plan 1 and Plan 2 share one rule set: an unreduced allowance at **age 60 with at "
        "least five years of service credit, or at age 50 with at least 25 years of service credit**. "
        "That is materially more generous than the State Employees rules, and it cuts in an unexpected "
        "direction for this bill."))
A(("ul", [
    "**The age-60 route cannot be purchased into.** Once a member has five years, buying service does "
    "nothing for eligibility; before five years, the hazardous-duty rule requires five years of "
    "VaLORS, SPORS or enhanced hazardous-duty service, which purchased military service does not "
    "supply. Section 1.3 treats this as the governing reading.",
    "**The age-50-with-25-years route can be purchased into**, and it is the only Bridge route in "
    "VaLORS. It reaches members already aged 50 or over who hold 21 to just under 25 years of "
    "service.",
    "**Almost nobody is in that box.** A workforce averaging 8.3 years of service has very few "
    "members with 21 to 25 years and age 50 or more. The published table gives "
    f"{br['n']:,.0f}.",
]))
A(("table", "Table 2 — the two pathway pools, derived cell by cell from the published VaLORS age × "
            "total-service table", [
    ["Pool", "Count", "Average salary", "Composition"],
    ["Retirement Incentive — already eligible for an unreduced allowance",
     f"{inc['n']:,.0f}", D(inc["salary"]),
     f"Plan 1 {inc['p1']:,.0f} ({100*f1:.1f}%) · Plan 2 {inc['p2']:,.0f}"],
    ["Retirement Bridge — reaches the threshold with ≤ 48 months purchased",
     f"{br['n']:,.0f}", D(br["salary"]),
     f"Plan 1 {br['p1']:,.0f} · Plan 2 {br['p2']:,.0f}"],
    ["Combined pathway-eligible", f"**{pool:,.0f}**", D((inc['pay']+br['pay'])/pool),
     f"**{100*pool/7459:.1f}% of 7,459** — against 29.8% for State Employees"],
]))
A(("note", f"Bridge members need an average of **{br['avg_months']:.1f} months**, the same figure the "
           "State Employees model produces and for the same reason: the whole Bridge pool sits inside "
           "one published service band, so a uniform assumption inside that band yields a uniform "
           "months-needed distribution by construction. The average is robust. The shape is an "
           "artefact and we do not defend it."))

A(("h2", "1.3 The VaLORS Bridge is Plan 1 only, and the strict screen governs"))
A(("p", "**Expected VaLORS Plan 2 Bridge participation is zero for the whole pilot**, by exactly the "
        "argument the board adopted for the State Employees plan on 12 October 2026. A VaLORS Plan 2 "
        "member holds at most 15 years of service at 30 June 2025 and at most about 20 by 2031, so "
        "the 25-year route is out of reach even with 48 months purchased. Plan 2 should stay legally "
        "eligible in the drafting and be scored at zero in the note."))
A(("p", "There is a second, wider reading of the Bridge that we are **not** adopting. Members aged 60 "
        "or over with one to just under five years of service could in principle buy their way to the "
        "five-year threshold and retire unreduced at once. That reading adds "
        f"{br_p['n'] - br['n']:,.0f} members and would take the Bridge pool to {br_p['n']:,.0f}."))
A(("table", "Table 3 — the two VaLORS Bridge screens", [
    ["Screen", "Plan 1", "Plan 2", "Total", "Status"],
    ["Strict — service-route only (age 50 + 25 years)", f"{br['p1']:,.0f}", "0",
     f"**{br['n']:,.0f}**", "**Governs this annex**"],
    ["Wider — also allows buying to the five-year vesting threshold at age 60+",
     f"{br_p['p1']:,.0f}", f"{br_p['p2']:,.0f}", f"{br_p['n']:,.0f}",
     "Not adopted. Open question for VRS"],
]))
A(("p", "We take the strict screen for a stated reason: VRS requires five years of service **as a "
        "VaLORS, SPORS or enhanced hazardous-duty member** to retire with hazardous-duty benefits, and "
        "purchased military service does not count toward that requirement. A member who bought their "
        "way to five years of total creditable service would still not have five years of "
        "hazardous-duty service, and so would not reach the age-60 hazardous-duty rule. We are "
        "confident of the rule and not certain of its interaction with a purchase, so we take the "
        "smaller pool and put the question to VRS. **If VRS says the wider reading is right, the "
        f"Bridge pool rises by {100*(br_p['n']-br['n'])/br['n']:.0f}% and total VaLORS participants "
        f"rise by about {100*(br_p['n']-br['n'])/pool:.0f}%.** That is the sensitivity, and it does not "
        "change the order of magnitude."))
A(("p", "This is the same discipline the board applied to the State Employees Bridge screen: take the "
        "smaller defensible pool, state the larger one, and name the question that resolves it."))

A(("h2", "1.4 One piece of good news that belongs in the fiscal note"))
A(("p", "**Purchased military service does not create hazardous-duty supplement eligibility.** VRS is "
        "explicit: other types of prior service, including active-duty military service, do not count "
        "toward the 20 years of hazardous-duty service the supplement requires. So a VaLORS amendment "
        "cannot manufacture a supplement obligation, and the supplement — a dollar amount paid monthly "
        "from retirement to age 65, available only to pre-1 July 2001 members on the 1.7% multiplier — "
        "is outside this amendment's cost entirely. Say that before VRS has to ask."))
A(("hr",))

A(("h1", "2. Price — the 1.9× headline is wrong, and the real multiple is about 1.4×"))
A(("p", "The approximate-normal-cost rate for hazardous-duty positions is 23.78% of salary for Plan 1 "
        "and 19.15% for Plan 2, against 12.50% and 10.74% for non-hazardous state positions, all "
        "effective 1 July 2025. That is where the “roughly 1.9× the price per year purchased” "
        "line in V2-fiscal-model comes from, and as a statement about **rates** it is right."))
A(("p", "As a statement about **cost per participant** it is wrong, because VaLORS salaries are lower. "
        "Average VaLORS compensation is $58,011 against $77,215 for State Employees — 25% lower — and "
        "the member payment is charged on salary. The two effects partly cancel."))
A(("table", "Table 4 — member payment per participant, VaLORS against the plan we scoped", [
    ["Pathway", "Years purchased at ANC", "Rate", "Average salary", "Member pays",
     "State Employees", "Multiple"],
    ["Retirement Incentive (12-month cap, G3/G18)", "1.00", f"{100*rate_inc:.2f}% blended",
     D(inc["salary"]), f"**{D(per_inc)}**", D(ST["per_inc"]), f"{per_inc/ST['per_inc']:.2f}×"],
    ["Retirement Bridge (months needed only, G2/G18)", f"{br['avg_months']/12:.2f}", "23.78%",
     D(br["salary"]), f"**{D(per_br)}**", D(ST["per_br"]), f"{per_br/ST['per_br']:.2f}×"],
]))
A(("p", "**Correct the 1.9× line wherever it appears as a cost statement.** Per year of service "
        "purchased the hazardous-duty rate is 1.90× the Plan 1 non-hazardous rate. Per participant the "
        f"cost runs about {per_inc/ST['per_inc']:.2f}× on the Incentive and "
        f"{per_br/ST['per_br']:.2f}× on the Bridge. Anyone who argues “nearly twice as expensive "
        "per veteran” is overstating it by about a third, and that is an argument we will be on "
        "the wrong side of if we make it ourselves first."))
A(("table", "Table 5 — trust-fund subsidy at four values of k, mid case "
            f"({mid['participants']:.1f} VaLORS participants)", [
    ["k", "Actuarial-equivalent value of service granted", "Member pays", "Trust-fund subsidy"],
] + [[f"{k:.1f}", D(k * mid["member_payments"]), D(mid["member_payments"]),
      D((k - 1) * mid["member_payments"])] for k in (1.5, 2.0, 2.5, 3.0)]))
A(("p", "**k is probably higher for VaLORS than for the plan we scoped, and in the one direction we "
        "cannot measure.** Hazardous-duty members reach an unreduced allowance up to five years "
        "earlier, and the actuarial-equivalent cost of a purchase rises with how early the resulting "
        "allowance starts. VaLORS total normal cost is 14.30% of payroll against 8.73% for State "
        "Employees, which is the same fact seen from the employer side. We do not have a VaLORS k and "
        "we are not going to invent one. **If a VaLORS amendment is offered, k for VaLORS becomes a "
        "second actuarial question, not a scaling of the first.**"))
A(("hr",))

A(("h1", "3. Reach — the same three dials, at the same settings"))
A(("p", "Veteran share, share holding qualifying purchasable service, and take-up, exactly as in "
        "V2-fiscal-model. The dials are held at the same values deliberately, so the VaLORS column is "
        "comparable with the State Employees column rather than being argued separately."))
A(("table", "Table 6 — take-up only, veteran share 8% and qualifying share 50%", [
    ["Take-up", "Incentive", "Bridge", "Total", "Member payments", "Subsidy at k = 2.0"],
] + [[f"{t:.0%}", N1(r["inc_parts"]), N1(r["br_parts"]), N1(r["participants"]),
      D(r["member_payments"]), D(r["member_payments"])]
     for t, r in ((0.05, t5), (0.12, t12), (0.25, t25))]))
A(("table", "Table 7 — all 27 cells. Participants added over the four-year pilot.", [
    ["Veteran share", "Qualifying share", "Take-up 5%", "Take-up 12%", "Take-up 25%"],
] + [[f"{v:.0%}" if q == 0.35 else "", f"{q:.0%}"]
     + [N1(M.funnel(v, q, t)["participants"]) for t in (0.05, 0.12, 0.25)]
     for v in (0.06, 0.08, 0.10) for q in (0.35, 0.50, 0.65)]))
A(("p", f"**Honest full range: {low['participants']:.1f} to {high['participants']:.1f} VaLORS "
        f"participants over four years, {D(low['member_payments'])} to "
        f"{D(high['member_payments'])} in member payments.** Two of the three dials are data requests "
        "and not judgments. The VaLORS-specific versions of both are now added to the G24 request."))

A(("h2", "3.1 The one dial that should probably be set higher for VaLORS"))
A(("p", "**Veteran share is almost certainly higher among law officers than across the classified "
        "state workforce, and we hold no Virginia figure for it.** The 6% we use as a floor comes from "
        "DHRM's January 2025 presentation and covers the classified workforce as a whole. Corrections "
        "and law-enforcement roles draw disproportionately from people with military service. We will "
        "not put a number on that from a secondary source, so the table below is labelled as what it "
        "is: arithmetic on a judgment, offered so the sensitivity is visible rather than hidden."))
A(("table", "Table 8 — veteran-share sensitivity. Qualifying share 50%, take-up 12%. "
            "**The multipliers are judgment with no source. Do not quote them as findings.**", [
    ["Veteran share", "Basis", "VaLORS participants", "Member payments"],
] + [[f"{v:.0%}", basis, N1(M.funnel(v, 0.50, 0.12)["participants"]),
      D(M.funnel(v, 0.50, 0.12)["member_payments"])]
     for v, basis in ((0.08, "Base — same as the State Employees model"),
                      (0.12, "1.5× the base. Judgment, no source"),
                      (0.16, "2.0× the base. Judgment, no source"),
                      (0.20, "2.5× the base. Judgment, no source"))]))
A(("p", "**Even at 2.5× the veteran share, a VaLORS amendment adds about "
        f"{M.funnel(0.20, 0.50, 0.12)['participants']:.0f} participants at mid take-up.** That is the "
        "robust point. The amendment is small across every setting of the dial we are least sure "
        "about, because the binding constraint is eligibility and not veteran status."))

A(("h2", "3.2 Where this annex is conservative, stated plainly"))
A(("p", "Both screens ask who is eligible, or reachable, **at 30 June 2025**. The pilot would run four "
        "years. Members age and accrue service throughout. Rolling the published table forward on "
        "both axes gives the scale of what the static screens leave out."))
A(("table", "Table 9 — roll-forward. Nothing leaves VaLORS in this view, so these are upper bounds on "
            "the dynamic effect, not projections.", [
    ["View", "Incentive pool", "Bridge pool", "Combined", "Against the static screen"],
    ["Static — 30 June 2025 (governs this annex)", f"{inc['n']:,.0f}", f"{br['n']:,.0f}",
     f"{pool:,.0f}", "—"],
    ["+2 years — mid-pilot", f"{rf2[0]['n']:,.0f}", f"{rf2[1]['n']:,.0f}",
     f"{rf2[0]['n']+rf2[1]['n']:,.0f}", f"+{100*((rf2[0]['n']+rf2[1]['n'])/pool-1):.0f}%"],
    ["+4 years — end of pilot", f"{rf4[0]['n']:,.0f}", f"{rf4[1]['n']:,.0f}",
     f"{rf4[0]['n']+rf4[1]['n']:,.0f}", f"+{100*((rf4[0]['n']+rf4[1]['n'])/pool-1):.0f}%"],
]))
A(("p", "**This conservatism applies to the State Employees model too, where it had not been "
        "stated.** Our published pools of 6,254 and 2,396 are also a 30 June 2025 snapshot. The "
        "direction of the error is known — we understate — and the size is of this order. It belongs "
        "in the fiscal note as a stated limitation rather than as something a reviewer finds. It is "
        "now carried in three places: **§6.1 of V2-fiscal-model**, added as amendment 1 of 12 October "
        "2026; **item 5 of the data request**, which states it to VRS and asks for the counts "
        "projected to the pilot years; and open item 7 in §7 below."))
A(("hr",))

A(("h1", "4. The workforce ledger (G11 Ledger 2) — and the amortization trap is worse here"))
A(("p", "Separate ledger, agency appropriations, never netted against the pension cost. Decision 6 of "
        "12 October 2026 holds without exception and a VaLORS amendment does not reopen it."))
A(("table", "Table 10 — the VaLORS employer rate, and which parts are a real saving when payroll falls",
   [
    ["Component", "VaLORS", "State Employees", "A saving when payroll falls?"],
    ["Employer normal cost", "9.30%", "4.34%", "Yes"],
    ["Administrative expense", "0.26%", "0.24%", "Yes"],
    ["Amortization of unfunded liability", "**13.04%**", "6.49%", "**No** — see below"],
    ["Employer DB contribution rate", "22.60%", "11.07%", ""],
    ["FICA", "7.65%", "7.65%", "Yes"],
    ["Honest scalable multiplier", f"**{M.VALORS_SCALABLE:.4f}**", "1.1223", ""],
]))
A(("p", "**For VaLORS, 13.04 of the 22.60 points — 58% of the employer rate — is amortization of a "
        "fixed $717.570 million unfunded liability, and none of it is a saving.** Cutting VaLORS "
        "payroll does not reduce that liability by a cent; it reduces the dollars collected against it "
        "and the rate must rise later. The trap is the same one the State Employees ledger carries, "
        "and it is twice as large as a share of the rate. Anyone presenting 22.60% as avoided employer "
        "cost would be booking a timing cost as a saving."))
A(("table", f"Table 11 — VaLORS agency payroll saving, annual run-rate at mid take-up "
            f"({mid['participants']:.1f} retirements, blended salary {D(mid_sal)})", [
    ["Positions not refilled", "Replacement at 80%", "at 85%", "at 90%"],
] + [[f"{nf:.0%}"] + [D(M.workforce(mid["participants"], mid_sal, rep, nf)["total"])
                      for rep in (0.80, 0.85, 0.90)] for nf in (0.01, 0.03, 0.05)]))
A(("table", "Table 12 — where the mid-cell saving comes from (85% replacement, 3% not refilled)", [
    ["Source", "Annual", "Share"],
    ["Salary compression on replacement",
     D(M.workforce(mid["participants"], mid_sal)["compress"]),
     f"{100*M.workforce(mid['participants'], mid_sal)['compress']/M.workforce(mid['participants'], mid_sal)['total']:.1f}%"],
    ["Positions not refilled", D(M.workforce(mid["participants"], mid_sal)["unfilled"]),
     f"{100*M.workforce(mid['participants'], mid_sal)['unfilled']/M.workforce(mid['participants'], mid_sal)['total']:.1f}%"],
    ["Total", f"**{D(M.workforce(mid['participants'], mid_sal)['total'])}**", ""],
    ["Memo — amortization dollars no longer collected. A timing cost, not a saving.",
     D(M.workforce(mid["participants"], mid_sal)["amort_lost"]), ""],
]))
A(("p", "Not modelled, and the same gaps as the main ledger: state health insurance per head, leave "
        "payout at separation, vacancy and training cost during transition. For VaLORS there is a "
        "further one that matters more than it does elsewhere — **a corrections or law-enforcement post "
        "that is not refilled may not be a saving at all** if it is backfilled with overtime. We hold "
        "no figure for that and it would cut against us. It belongs in the note."))
A(("hr",))

A(("h1", "5. State Police (SPORS) — the amendment that usually travels with it"))
A(("p", "Scored here for the same reason, at the same settings. SPORS shares the VaLORS eligibility "
        "rules — age 60 with five years or age 50 with 25 years — and the same hazardous-duty "
        "approximate-normal-cost rates. It is a much smaller plan with much higher salaries, and those "
        "two facts almost cancel in the dollars."))
A(("table", "Table 13 — SPORS pre-score", [
    ["", "SPORS", "VaLORS"],
    ["Active members", "1,902", "7,459"],
    ["Average compensation", "$96,071", "$58,011"],
    ["Incentive pool", f"{s_inc['n']:,.0f}", f"{inc['n']:,.0f}"],
    ["Bridge pool (strict screen)", f"{s_br['n']:,.0f}", f"{br['n']:,.0f}"],
    ["Pathway-eligible share of the plan", f"{100*(s_inc['n']+s_br['n'])/1902:.1f}%",
     f"{100*pool/7459:.1f}%"],
    ["Member pays — Incentive, per participant", D(s_per_inc), D(per_inc)],
    ["Member pays — Bridge, per participant", D(s_per_br), D(per_br)],
    ["Participants, mid take-up", N1(s_mid["participants"]), N1(mid["participants"])],
    ["Member payments, mid take-up", f"**{D(s_mid['member_payments'])}**",
     f"**{D(mid['member_payments'])}**"],
    ["Participants, full range", f"{s_low['participants']:.1f} – {s_high['participants']:.1f}",
     f"{low['participants']:.1f} – {high['participants']:.1f}"],
    ["Employer amortization share of the DB rate", "17.96% of 31.67% — 57%",
     "13.04% of 22.60% — 58%"],
]))
A(("p", "**SPORS is a quarter of the size of VaLORS and costs about the same, because the salaries are "
        f"double.** Pathway-eligibility runs at {100*(s_inc['n']+s_br['n'])/1902:.1f}% against "
        f"{100*pool/7459:.1f}% for VaLORS — state police serve longer careers — so the eligible "
        "fraction is higher even though the plan is far smaller. One more fact worth holding: SPORS "
        "members must retire within 60 days of age 70, and no active SPORS member is aged 69 or over "
        "in the published table. The Incentive pathway cannot reach anyone the mandatory-retirement "
        "rule would have reached anyway."))
A(("table", "Table 14 — what each amendment adds at mid take-up", [
    ["Scope", "Participants", "Member payments", "Against the bill as scoped"],
    ["Bill as scoped — State Employees Plan 1/Plan 2 only", N1(ST["parts_mid"]), D(ST["pay_mid"]),
     "—"],
    ["+ VaLORS", N1(ST["parts_mid"] + mid["participants"]),
     D(ST["pay_mid"] + mid["member_payments"]),
     f"+{100*mid['participants']/ST['parts_mid']:.1f}% participants, "
     f"+{100*mid['member_payments']/ST['pay_mid']:.1f}% payments"],
    ["+ VaLORS and SPORS",
     N1(ST["parts_mid"] + mid["participants"] + s_mid["participants"]),
     D(ST["pay_mid"] + mid["member_payments"] + s_mid["member_payments"]),
     f"+{100*(mid['participants']+s_mid['participants'])/ST['parts_mid']:.1f}% participants, "
     f"+{100*(mid['member_payments']+s_mid['member_payments'])/ST['pay_mid']:.1f}% payments"],
]))

A(("h2", "5.1 Judicial (JRS) is deliberately not scored"))
A(("p", "**We should not put a number on JRS and this annex does not.** The Judicial Retirement System "
        "applies weighted service credit at rates that depend on the date of appointment, which means "
        "“years of service credit” in the JRS eligibility rules is not the same quantity as "
        "the total service published in the valuation table. Applying the VaLORS method to the JRS "
        "table would produce a confident-looking figure built on the wrong variable."))
A(("p", "What we can say: JRS has 473 active members, the oldest average age in the system at 57.3, and "
        "an approximate-normal-cost rate of 31.97% for Plan 1 and 29.67% for Plan 2 — about 2.6× the "
        "Plan 1 non-hazardous rate — on an average compensation of $208,551. **Per participant, a "
        "judicial purchase is by far the most expensive in the system.** If a JRS amendment is "
        "actually offered, the weighted-service rules have to be verified first. That is a day of work "
        "and it is listed as an open item rather than guessed at here."))
A(("hr",))

A(("h1", "6. How to use this annex"))
A(("ol", [
    "**It stays in reserve.** It is not attached to the bill, the fiscal note, the one-pager or the "
    "advocacy brief. The bill as drafted expressly excludes SPORS, VaLORS and JRS, and that remains "
    "the position.",
    "**If a VaLORS amendment is offered, the answer is a number and not a flinch.** At mid take-up it "
    f"adds about {mid['participants']:.0f} participants and about {D(mid['member_payments'])} in "
    "member payments over four years — roughly "
    f"{100*mid['member_payments']/ST['pay_mid']:.0f}% on top of the bill as scoped.",
    "**Lead with why we excluded them, not with the cost.** The reason is sequencing: prove the "
    "mechanism on the one plan we can model from published data, then extend. The cost is modest and "
    "saying so first makes the sequencing argument sound like a pretext.",
    "**Do not accept a floor amendment that adds a plan without adding k for that plan.** A VaLORS "
    "amendment needs its own actuarial ratio. Accepting one without it converts a bounded, priced "
    "pilot into an unpriced one, which is the specific failure mode G13 exists to prevent.",
    "**If the board wants VaLORS in the bill from the start, say so before 30 November 2026.** It is a "
    "different bill with a different fiscal note, and the data request would need a VaLORS section "
    "that it does not currently have. Adding it at the drafting request is cheap; adding it in "
    "February is not.",
]))
A(("hr",))

A(("h1", "7. Open items this annex creates"))
A(("table", None, [
    ["#", "Item", "Owner", "Why it matters"],
    ["1", "Does purchased military service let a VaLORS member aged 60+ reach the hazardous-duty "
          "five-year threshold, or does that threshold require five years of hazardous-duty-covered "
          "service?", "VRS",
     f"The wider Bridge screen. Worth +{br_p['n']-br['n']:.0f} members, "
     f"+{100*(br_p['n']-br['n'])/pool:.0f}% of VaLORS participants"],
    ["2", "k for VaLORS Plan 1 and Plan 2, by age band", "VRS actuary (GRS)",
     "Probably above the State Employees k. Cannot be scaled from it"],
    ["3", "Veterans among active VaLORS and SPORS members", "VRS / DHRM",
     "The dial we are least sure about and most likely understating"],
    ["4", "Members with qualifying purchasable military service, VaLORS and SPORS", "VRS",
     "Same weakest-link status as in the main model"],
    ["5", "Whether an unfilled corrections or law-enforcement post is backfilled with overtime",
     "DHRM / Department of Corrections", "Could reduce the Ledger 2 saving to near zero. Cuts "
     "against us"],
    ["6", "JRS weighted-service-credit rules by appointment date", "Policy Director",
     "Required before any JRS figure can be produced"],
    ["7", "Roll-forward limitation stated in the main fiscal note", "Policy Director",
     "Our State Employees pools are also a 30 June 2025 snapshot and understate by roughly this order"],
]))
A(("hr",))

A(("h1", "8. Sources"))
A(("p", "All retrieved 12 October 2026. Primary Commonwealth sources only, per G25."))
A(("table", None, [
    ["Source", "Used for"],
    ["VRS, *Annual Actuarial Valuation, June 30, 2025* — p. 49 Active Participant Detail; p. 54 "
     "Active Participants by Age and Total Service, Virginia Law Officers; p. 52 same table, State "
     "Police; p. 53 same table, Judicial; p. 16 Results Summary, Virginia Law Officers; p. 18 "
     "Employer Contribution Rate Detail",
     "Every count, salary, employer rate and the $717.570M VaLORS UAAL"],
    ["VRS, *Purchase of Prior Service Cost Rates for VRS Plan 1* and *for VRS Plan 2*, effective "
     "1 July 2025", "23.78% / 19.15% hazardous; 31.97% / 29.67% judicial; 12.50% / 10.74% "
     "non-hazardous"],
    ["VRS, *Plan 1: Virginia Law Officers' Retirement System* overview, 04-2026",
     "Unreduced eligibility age 60/5 and age 50/25; 1.7% and 2.0% multipliers; 36-month AFC; "
     "hazardous-duty supplement rules; prior service counts toward eligibility"],
    ["VRS, *Plan 2: Virginia Law Officers' Retirement System* overview, 04-2026",
     "Identical unreduced eligibility; 2.0% multiplier; 60-month AFC"],
    ["VRS, *Hazardous Duty Benefits FAQ for Members*, April 2026",
     "Eligibility rules confirmed for SPORS and VaLORS together; the five-years-of-hazardous-duty "
     "requirement; purchased military service excluded from the 20-year supplement test; SPORS "
     "mandatory retirement at 70"],
    ["VRS, Hybrid Retirement Plan eligibility — hazardous-duty exclusion",
     "No VaLORS or SPORS Hybrid tier; membership on or after 1 July 2010 is Plan 2 regardless of date"],
    ["DHRM, presentation to Senate Finance and Appropriations, 21 January 2025, slide 8",
     "Veterans 6% of the classified state workforce, as of 30 June 2024. Used as a floor"],
]))
A(("p", "**Derived, not published:** the plan-tier split; both pathway pools; all average salaries by "
        "cohort; the months-needed distribution; the roll-forward. **Assumptions, labelled per G23:** "
        "veteran share; qualifying-service share; take-up; uniform distribution within published age "
        "and service bands; salary as a proxy for average final compensation; k as a ratio rather than "
        "a value. **Judgment with no source, and marked as such in Table 8:** the veteran-share "
        "multipliers for law-enforcement cohorts."))
A(("p", "*Nothing in this annex is a VRS actuarial result, and it contains no claim that any part of "
        "the proposal is actuarially neutral, minimal in impact or self-funding.*"))

if __name__ == "__main__":
    paths = render.build(B, "V2-annex-VaLORS-prescore", HERE, SCRATCH)
    for p in paths:
        print("wrote", p)
