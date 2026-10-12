"""Builds the send packet: transmittal, data request, counsel question.

The board authorised transmission on 12 October 2026 and asked who the
addressees are and whose signature it goes out under. Section 1 of the
transmittal answers both from published sources.
"""
import os
import re
from pathlib import Path

import render

HERE = Path(__file__).parent
SCRATCH = (os.environ.get("PAPERCLIP_RUN_SCRATCH_DIR")
           or os.environ.get("PAPERCLIP_SCRATCH_DIR") or "/tmp")

SEND_DATE = "13 October 2026"

APPROVED = ("**Approved for transmission by the board, 12 October 2026. Signed by Moody as the "
            "proposal's author; no organisation named.** Going out the week of 12 October 2026 — "
            "email first, hard copy to follow. Response date 20 November 2026 and drafting target "
            "30 November 2026 both unchanged. Send instructions: V2-send-packet.")

# Closing block used verbatim at the foot of both letters.
SIGNOFF = [
    ("hr",),
    ("p", "Thank you for considering this. I am glad to make any of it easier — to narrow the "
          "request, to take it by meeting, or to put it in whatever form is least work for your "
          "staff."),
    ("p", "Yours sincerely,"),
    ("p", ""),
    ("p", "____________________________________"),
    ("p", "**David Moody**"),
    ("p", "Author of the proposal · writing in a personal capacity"),
    ("p", "1154 West Ocean View"),
    ("p", "Norfolk, VA 23503"),
    ("p", "davidmoody@gmail.com · 434-989-5481"),
    ("p", f"{SEND_DATE}"),
]
# Name, return address, email and telephone supplied by the board on 12 October 2026 and applied
# here. No organisation name appears in the block, which is the signature decision of the same
# date. Nothing in either outgoing letter is left to fill in except the date line, if the actual
# send day differs from SEND_DATE above.

# ======================================================================= 1
T = []
A = T.append
A(("title", "Transmittal — addressees, signature and routing"))
A(("sub", "Cover document for the VRS and DHRM send packet · Policy Director · MOO-100 · "
          "12 October 2026"))
A(("p", "On 12 October 2026 the board authorised sending both letters, together, and asked me to "
        "name the addressees and whose signature they go out under. This document answers both "
        "questions from published sources, sets out the routing, and states plainly what still has to "
        "happen before anything leaves the building."))
A(("hr",))

A(("h1", "1. The answers to the two questions you asked"))
A(("h2", "1.1 Two addressees we had drafted do not exist"))
A(("p", "Both letters were drafted to offices that VRS does not publish. That would have cost us "
        "weeks of internal forwarding, so it is worth correcting before sending rather than after."))
A(("table", "Table 1 — what we had, what is actually there", [
    ["Drafted to", "What the published record shows", "Corrected to"],
    ["VRS — Office of the Chief Actuary",
     "**VRS has no in-house actuary.** Actuarial services are performed by Gabriel, Roeder, Smith & "
     "Company under contract to the Board of Trustees (2025 Annual Report, professional consultants "
     "and professional-services schedules). GRS works for the Board and cannot be approached "
     "directly by us.",
     "The Director, who tasks the consulting actuary through the Board"],
    ["VRS — Office of General Counsel",
     "**VRS has no in-house general counsel.** The 2025 Annual Report lists legal counsel as the "
     "Office of the Attorney General, Commonwealth of Virginia, with outside firms engaged for "
     "specific matters.",
     "The Director, with an express request to refer the question to the Office of the Attorney "
     "General"],
    ["VRS — Policy, Planning and Compliance",
     "The directorship of Policy, Planning and Compliance is published as **TBA** — the post is "
     "vacant on the current leadership page.",
     "The named Legislative Liaison and Policy Analyst, who is the published channel for legislative "
     "and policy correspondence"],
]))
A(("p", "**Neither letter should be addressed to an actuary or to counsel.** Both go to the Director. "
        "The actuarial question is one the Director refers to the consulting actuary; the legal "
        "question is one the Director refers to the Attorney General's office. Addressing them "
        "directly would be addressing people who do not work for VRS."))

A(("h2", "1.2 Addressees, with the email channel for each"))
A(("table", "Table 2 — Virginia Retirement System", [
    ["Role", "Name and published title", "Email", "Address"],
    ["**Addressee**", "Patricia S. Bishop, Director", "**pbishop@varetire.org** — published on the "
     "VRS leadership page", "Virginia Retirement System, 1200 East Main Street, Richmond, VA 23219 · "
     "mailing alternative P.O. Box 2500, Richmond, VA 23218-2500"],
    ["**Copy — the working channel**", "Jillian L. Sherman, ACP, MPA, Legislative Liaison and Policy "
     "Analyst", "**Not published.** VRS staff addresses follow first-initial-surname, which gives "
     "jsherman@varetire.org — *inferred, not verified.* Confirm on 804-771-7373 before using it",
     "Same address · 804-771-7373"],
    ["Copy — for the administration-cost item only", "Michael Cooper, Chief Operating Officer",
     "**mcooper@varetire.org** — published", "Same address"],
]))
A(("note", "**Do not send the data request to FOIA@varetire.org.** That address is published and it "
           "would work, and it is the wrong channel. The Freedom of Information Act does not require "
           "a public body to create a record that does not already exist, and most of what we are "
           "asking for — counts screened on eligibility proximity, a normal-cost-to-actuarial-"
           "equivalent ratio — are figures VRS would have to compute. Filing as FOIA invites a "
           "lawful refusal on exactly our most important items. As legislative and policy "
           "correspondence to the Director, the same questions can be answered. **FOIA stays in "
           "reserve** for the underlying membership records if the Director declines to compute "
           "anything."))
A(("table", "Table 3 — Department of Human Resource Management", [
    ["Role", "Name and published title", "Email", "Address"],
    ["**Addressee**", "Janet L. Lawson, Director", "**Not published.** Send to the published policy "
     "mailbox **policy@dhrm.virginia.gov**, addressed to the Director by name",
     "Department of Human Resource Management, 600 East Main Street, 17th Floor, Richmond, VA 23219 "
     "· 804-225-2131 · fax 804-371-7401"],
    ["**Copy — items 3 and 8**", "Stacy Pendleton, Deputy Director (Human Resource Consulting "
     "Services — compensation and workforce analytics)", "**compensation@dhrm.virginia.gov** — the "
     "published compensation and workforce mailbox", "Same address"],
    ["**Copy — item 11, the health premium**", "Gary Johnston, Director of Health Benefits Services",
     "**Not published.** The Office of Health Benefits mailbox **ohb@dhrm.virginia.gov** is the "
     "published route", "Same address"],
]))
A(("note", "**Correction to the earlier draft: DHRM's address is not the James Monroe Building.** We "
           "had 101 North 14th Street, 12th Floor. DHRM's own published correspondence address is "
           "**600 East Main Street, 17th Floor, Richmond, VA 23219** (DHRM Contact Us, retrieved 12 "
           "October 2026). Both letters are corrected. A hard copy sent to the old address would "
           "most likely still arrive, and it would announce that we had not checked."))
A(("note", "**DHRM publishes no individual staff email addresses.** Its addresses follow "
           "firstname.lastname@dhrm.virginia.gov — the FOIA and media contact is published that way "
           "— so the Director's address is inferable, and I will not put an inferred address on an "
           "outgoing letter. Use the published functional mailboxes above and name the Director in "
           "the salutation. One telephone call to 804-225-2131 replaces all of this with a direct "
           "address if you want one."))
A(("note", "All names and titles from the published VRS and DHRM leadership pages and the VRS FOIA "
           "page, retrieved 12 October 2026. **Verify each one by telephone on the day of sending.** "
           "Leadership pages go stale, and a letter to a predecessor reads as carelessness about "
           "exactly the kind of detail we are asking VRS to be careful about."))

A(("h2", "1.3 Signature — decided 12 October 2026"))
A(("p", "**Decided: both letters go out over Moody's own signature, as the author of the proposal, "
        "with no organisation named.** This was the recommendation and it is now the instruction. The "
        "reasons are recorded here because they govern how the letters are written, not only how they "
        "are signed:"))
A(("ol", [
    "**It is accurate.** The Joint Leadership Council has not adopted this proposal. Signing as, or "
    "implying, a JLC initiative before the JLC has voted would be claiming an endorsement we do not "
    "have, and it is the one thing that would cost us the JLC.",
    "**It matches what the letters actually say.** Both are explicit that we are not asking VRS to "
    "endorse anything and that only VRS can price the proposal. A letter that modest reads correctly "
    "from an individual and oddly from an institution.",
    "**It keeps the second, stronger approach available.** VRS responds to a legislator's request "
    "differently from a citizen's. If the 20 November date passes without a substantive answer, a "
    "patron can ask the same questions with far more force — but only if we have not already spent "
    "that card.",
]))
A(("p", "**The alternative was a patron's signature now.** It is faster and it spends that card. It "
        "also makes the counsel question — the one that invites the answer “this mechanism does not "
        "work” — a legislator's question. **The first substantive bad news about this design should "
        "arrive to us and not to a legislator.** That is the argument that decided it, and the patron "
        "route stays available if 20 November passes without a substantive answer."))
A(("p", "**What the decision requires in practice.** No letterhead, and nothing that looks like it. "
        "No organisation name in the signature block, the return address or the email signature. No "
        "implication that the proposal has been introduced, endorsed or scored. Both letters already "
        "read in the first person as the proposal's author, so no rewriting was needed — but if the "
        "letters are sent from an address that carries an organisation's name in its domain or "
        "footer, the decision is undone by the plumbing. Check the email footer before sending."))
A(("hr",))

A(("h1", "2. Routing — what goes to whom"))
A(("table", None, [
    ["Letter", "Primary addressee", "Copies", "Items"],
    ["Data request", "Director, VRS", "VRS Legislative Liaison; VRS Chief Operating Officer (item 9)",
     "1–10, and 12–13 (new, VaLORS and SPORS)"],
    ["Data request — DHRM portion", "Director, DHRM",
     "Deputy Director, HR Consulting Services; Health Benefits Services Director",
     "3 (veteran status), 9 (administration), 11 (health premium)"],
    ["Counsel question", "Director, VRS, with a request to refer to the Office of the Attorney General",
     "VRS Legislative Liaison", "All seven questions"],
]))
A(("p", "**Send both letters in one envelope to each addressee, with this transmittal on top.** The "
        "board decided on 12 October 2026 that they go together, and the reason holds: item 1 of the "
        "data request and question 1 of the counsel letter are the two items that decide whether the "
        "design survives. Splitting them invites VRS to answer the easy one."))
A(("p", "DHRM receives the data request only. The counsel question is not DHRM's to answer and sending "
        "it there would blur who owns what."))
A(("hr",))

A(("h1", "3. Two items added to the data request since the board approved it"))
A(("p", "The board also decided on 12 October 2026 to pre-score a VaLORS amendment before it is "
        "offered. That work is in V2-annex-VaLORS-prescore and it turned up two figures we cannot "
        "derive, so the data request now carries them as items 12 and 13. They are additive and they "
        "do not change anything already approved."))
A(("ul", [
    "**Item 12 — veterans among active VaLORS and SPORS members.** The annex is forced to apply the "
    "6% classified-workforce share to a law-enforcement population, where it is almost certainly too "
    "low, and we hold no Virginia figure to replace it with.",
    "**Item 13 — whether purchased military service can take a VaLORS or SPORS member aged 60 or over "
    "to the five-year hazardous-duty threshold.** VRS requires five years of hazardous-duty-covered "
    "service to retire with hazardous-duty benefits, and purchased military service does not count "
    "toward the 20-year supplement test. Whether the same exclusion applies to the five-year "
    "eligibility test decides whether the VaLORS Bridge pool is 150 or 225.",
]))
A(("p", "Both items are marked in the request as relating to a plan **expressly excluded** from the "
        "bill, asked for contingency pricing only. That wording matters: we do not want the request "
        "read as a signal that we intend to expand the bill."))
A(("hr",))

A(("h1", "4. Send status — decided, prepared, not yet transmitted"))
A(("p", "**All three open questions are answered.** Signature: Moody's own, as the proposal's author, "
        "no organisation named. Date: this week, with 20 November and 30 November held. Channel: both "
        "— email first, hard copy to follow."))
A(("p", "**Both letters are prepared for both channels and neither has been transmitted. I cannot "
        "transmit them.** This session has no outbound mail channel, and these have to leave from a "
        "real mailbox under a real signature in any case. Everything that can be done without you is "
        "done; what is left is in V2-send-packet, which holds the email text to paste, the attachment "
        "list, the hard-copy instructions and the day-of-send checks."))
A(("table", "Table 4 — what is done and what is left", [
    ["Step", "Status"],
    ["Content of both letters", "**Complete.** Board-approved 12 October 2026"],
    ["Addressees, names, titles, addresses", "**Complete and corrected.** §1.2. DHRM address was "
     "wrong and is fixed"],
    ["Email addresses for each addressee", "**Complete** where published; the two unpublished ones "
     "are flagged with a published mailbox to use instead. §1.2"],
    ["Signature decision", "**Decided.** Moody, as author, no organisation named"],
    ["Signature block applied to both letters", "**Complete.** Name, return address, email and "
     "telephone supplied 12 October 2026 and applied. Nothing is left bracketed"],
    ["Date line", "**Applied as 13 October 2026.** Change it to the actual send day; nothing else "
     "moves"],
    ["Email text, attachment list, hard-copy instructions", "**Complete.** V2-send-packet"],
    ["Authorisation to transmit", "**Given**, 12 October 2026"],
    ["Names verified by telephone on the day", "**Not done.** Two calls, five minutes. Requires you"],
    ["Letters signed and sent", "**Not done.** Requires you"],
    ["Response logged and our estimates retired", "Pending. Requested by 20 November 2026"],
]))
A(("h2", "What I need from you, and it is now a short list"))
A(("ol", [
    "**Make the two verification calls** — VRS on 804-771-7373, DHRM on 804-225-2131 — and confirm "
    "that Bishop and Lawson are still in post and that Sherman is still the legislative liaison. "
    "Leadership pages go stale, and a letter to a predecessor reads as carelessness about exactly the "
    "kind of detail we are asking VRS to be careful about.",
    "**Send them.** Email bodies are in V2-send-packet §2, ready to paste. Post the hard copies the "
    "same day or the next.",
]))
A(("p", "**One timing note that is mine to flag and yours to decide.** The 20 November response date "
        "gives VRS about five and a half weeks, and it asks for figures that have to be computed "
        "rather than retrieved. That is tight but defensible, and both letters already say we will "
        "narrow the request to items 1, 4 and 5 if that is all that fits. If nothing substantive has "
        "arrived by about 10 November, the decision to make then is whether a patron asks the same "
        "questions — not whether to extend our own deadline."))
A(("hr",))

A(("h1", "5. Enclosures"))
A(("table", None, [
    ["#", "Document", "Pages", "State"],
    ["1", "**V2-data-request-VRS-DHRM** — thirteen items, k first", "6", "Approved, ready to sign"],
    ["2", "**V2-counsel-question-trueup** — seven questions on whether the G5 true-up is collectible",
     "3", "Approved, ready to sign"],
    ["—", "**V2-send-packet** — email text to paste, attachment list, hard-copy instructions, "
     "day-of-send checks, send record. **Not enclosed with the letters — this is for you.**", "5",
     "Internal only"],
    ["—", "V2-annex-VaLORS-prescore — reserve pricing. **Not enclosed. Not for circulation.**", "12",
     "Internal only"],
]))
A(("note", "**Nothing but the two letters goes to VRS or DHRM.** The annex prices an amendment that "
           "has not been offered, to a plan the bill expressly excludes. Enclosing it would read as a "
           "signal that we intend to expand the bill, which is the opposite of what the exclusion is "
           "for. The send packet is an internal instruction sheet and has our own reasoning in it."))
A(("p", "*Sources for every name, title and address in this document: VRS Leadership page; VRS Freedom "
        "of Information Act page (Legislative Liaison and Policy Analyst, address, telephone); VRS "
        "Annual Comprehensive Financial Report for the fiscal year ended 30 June 2025 (legal counsel, "
        "consulting actuary, professional-services schedule); DHRM Our Leadership page; DHRM published "
        "correspondence address. All retrieved 12 October 2026.*"))

# ======================================================================= 2
DR = []
A = DR.append
A(("title", "Data request — VRS and DHRM"))
A(("sub", APPROVED))
A(("p", "This is the G24 data request, with the actuarial ratio added as item 1. It is addressed to "
        "the Director of the Virginia Retirement System and, for the workforce and benefit items, to "
        "the Director of the Department of Human Resource Management."))
A(("hr",))

A(("h1", "Why we are asking"))
A(("p", "We are preparing a 2027 session proposal for a bounded four-year pilot. It would create two "
        "narrow, post-window pathways for Plan 1 and Plan 2 state employees to purchase qualifying "
        "active-duty military service at approximate normal cost, in each case in exchange for a "
        "near-term retirement. The existing 24-month cost window, the 48-month military-service "
        "maximum and the eligibility conditions in the Code are all left unchanged."))
A(("p", "We have built a preliminary fiscal model from published VRS data only. It is adequate to size "
        "the proposal and it is not adequate for a fiscal note. We are not asking VRS to endorse the "
        "proposal, and we make no claim that it is actuarially neutral, minimal in impact or "
        "self-funding. We are asking for the figures that let the General Assembly see the real cost "
        "before it votes."))
A(("p", "Where we have had to estimate, we say so below and we show our estimate, so that VRS can see "
        "exactly which of our numbers its answer would replace."))

A(("h1", "Scope, so no one has to guess"))
A(("ul", [
    "Plan 1 and Plan 2 only. The Hybrid Retirement Plan is outside the proposal.",
    "State employees in the VRS State Employees (non-hazardous-duty) plan only. The State Police "
    "Officers' Retirement System, the Virginia Law Officers' Retirement System and the Judicial "
    "Retirement System are expressly excluded, as are employees of participating local governments "
    "and school divisions.",
    "Qualifying active-duty military service as the Code and VRS already define it: at least 180 "
    "consecutive days of full-time active duty, discharge not dishonorable, service not qualifying "
    "the member for a military pension at the time of purchase, and the 48-month maximum not already "
    "consumed.",
    "**Items 12 and 13 concern VaLORS and SPORS, which are expressly excluded.** They are asked for "
    "contingency pricing only, so that a floor amendment adding those plans can be priced before it "
    "is offered rather than after. They are not a signal that we intend to expand the bill.",
]))
A(("hr",))

A(("h1", "1. The actuarial ratio — the item that matters most"))
A(("p", "**Request.** For members of the VRS State Employees plan in Plan 1 and in Plan 2, the ratio of "
        "the actuarial-equivalent cost of purchasing one year of service credit to the approximate "
        "normal cost of the same purchase, broken out by five-year age band from age 45 through 70 and "
        "by plan tier. Separately for the two pathway cases if they differ:"))
A(("ul", [
    "(a) a purchase that advances the member's date of eligibility for an unreduced retirement "
    "allowance; and",
    "(b) a purchase by a member already eligible for an unreduced allowance, which raises the benefit "
    "amount without advancing eligibility.",
]))
A(("p", "**Why.** VRS defines actuarial-equivalent cost as the present value of the higher benefit or "
        "earlier eligibility that the purchased service creates. The price the member would pay is "
        "already public and verified — 12.50% of salary per year purchased for Plan 1 and 10.74% for "
        "Plan 2, from the cost-rate chart effective 1 July 2025. What we cannot compute is the other "
        "side. We have therefore carried the ratio as an unknown k and printed our model at k = 1.5, "
        "2.0, 2.5 and 3.0 rather than pick one."))
A(("p", "**What we expect, so our bias is on the record.** We expect k to be high for this cohort. "
        "Actuarial-equivalent cost rises sharply with age, and both pathways deliberately reach the "
        "oldest members in the plan. We would rather have a high number from VRS than a flattering one "
        "from us."))
A(("p", "**This single figure determines whether the proposal is affordable. If VRS can answer only "
        "one item on this list, we ask that it be this one.**"))

A(("h1", "2. Plan-tier counts for state employees"))
A(("p", "**Request.** Active members of the VRS State Employees (non-hazardous-duty) plan at 30 June "
        "2025, counted by plan: Plan 1, Plan 2, Hybrid."))
A(("p", "**What we have had to do instead.** The *Annual Actuarial Valuation, June 30, 2025* publishes "
        "81,274 active State Employees and a full age × total-service table at p. 50, but not the "
        "plan-tier split. We derived the split by applying the statutory tier boundaries to total "
        "service: Plan 1 at 15.0 years or more, Plan 2 between 11.5 and 15.0, Hybrid below 11.5. That "
        "gives Plan 1 20,872, Plan 2 8,122, Hybrid 52,280."))
A(("p", "**Known weakness of our proxy, which is why we are asking.** A member who refunded and "
        "returned, purchased prior service, or had a break in service can hold total service that does "
        "not match the hire date. Our figure is a service proxy for a hire-date rule."))

A(("h1", "3. Veterans among them"))
A(("p", "**Request.** Of the members in item 2, the number recorded as veterans, by plan tier. If VRS "
        "does not hold veteran status, the number for whom DHRM does."))
A(("p", "**What we have had to do instead.** DHRM's January 2025 presentation to the Senate Finance "
        "and Appropriations Committee reports veterans as 6% of the classified state workforce, sourced "
        "to EPR reports at 30 June 2024. Virginia's veteran share of the civilian labour force is 8.1% "
        "from BLS 2025 annual averages. We modelled 6% / 8% / 10% and treated 6% as a floor rather "
        "than a central estimate."))
A(("p", "**Please state the completeness of the field.** Our earlier work found the veteran-status "
        "field blank or “unknown” for 69% of members. If that is still the position, the "
        "recorded count is a floor and we need to know by how much. An honest “we do not "
        "know” is more useful to us than a count that understates."))

A(("h1", "4. Members holding qualifying purchasable service — the weakest number we have"))
A(("p", "**Request.** Of the veterans in item 3, the number with qualifying active-duty military "
        "service that is available to purchase and not already purchased — that is, who meet all four "
        "conditions in “Scope” above and have not consumed the 48-month maximum."))
A(("p", "**What we have had to do instead.** We assumed 35% / 50% / 65%. This assumption has no source "
        "at all. It is the weakest figure in our model and it moves the answer more than any other "
        "dial: holding everything else at the central case, moving this share from 35% to 65% takes "
        "participants from 29 to 54."))
A(("p", "**The military-pension exclusion is what makes it unguessable.** A member who served twenty "
        "years and draws retired pay is excluded outright, and that is the slice most likely to hold a "
        "senior state position."))

A(("h1", "5. The two pathway populations"))
A(("p", "**Request.** Of the members in item 4:"))
A(("ul", [
    "(a) the number already eligible for an unreduced retirement allowance; and",
    "(b) the number who are not yet eligible but would become eligible by purchasing up to 48 months "
    "of service credit.",
]))
A(("p", "**Note on (b), which is easy to get wrong.** Please read it as a reach test, not a proximity "
        "test. Purchased service adds service, not age. A member whose only route to an unreduced "
        "allowance is the Plan 1 age-65 rule or the Plan 2 normal-Social-Security-age rule cannot reach "
        "eligibility by purchasing at any price. We ask for the members for whom purchased service "
        "actually advances the eligibility date — in practice, Plan 1 members at or above age 50 "
        "approaching 30 years of service, and Plan 2 members approaching the Rule of 90."))
A(("p", "**What we have had to do instead.** Derived from the p. 50 table: 6,254 already eligible and "
        "2,396 able to reach eligibility with 48 months or less, out of 28,994. We also computed the "
        "proximity screen for comparison — 5,177 — and discarded it as the wrong test."))
A(("p", "**One limitation we should state rather than have found.** Both of our figures are a 30 June "
        "2025 snapshot. The pilot would run four years, during which members age and accrue service, "
        "so both pools understate. A roll-forward of the published table suggests the understatement "
        "is of the order of 20% at the mid-point of a four-year pilot. If VRS can supply the counts "
        "projected to the pilot years rather than as at the valuation date, that would be better than "
        "anything we can do."))

A(("h1", "6. Average qualifying military months"))
A(("p", "**Request.** For the members in item 4, the average and the distribution of qualifying "
        "military months available to purchase."))
A(("p", "**Why.** It sets how much service the Bridge pathway would actually sell. We modelled an "
        "average of 24.0 months for the reach cohort, spread uniformly from 1 to 48. The average is "
        "reasonably robust; the shape is an artefact of our method and we do not defend it."))

A(("h1", "7. Average salary by cohort"))
A(("p", "**Request.** Average creditable compensation, and average final compensation if available, "
        "for each population in items 2, 3, 4 and 5."))
A(("p", "**Why.** The member payment is charged on creditable compensation or average final "
        "compensation, whichever is higher, so our figures are floors. We used $84,753 for the "
        "already-eligible cohort and $83,222 for the reach cohort, derived from the published age × "
        "service table."))

A(("h1", "8. Historical purchase participation"))
A(("p", "**Request.** For the last five fiscal years, for state employees: purchases of prior service "
        "completed, split by type of service, by whether the purchase was made inside or outside the "
        "24-month cost window, and by plan tier. Military-service purchases identified separately if "
        "the data allows."))
A(("p", "**Why.** It is the only real evidence of how members behave when offered a purchase, and it "
        "is the only check available on our take-up assumption of 5% / 12% / 25%. We have no source "
        "for that assumption either."))

A(("h1", "9. Program administration cost"))
A(("p", "**Request.** VRS's and DHRM's estimate of the cost to administer the pilot, shown separately "
        "from any pension-cost estimate, covering: eligibility determination per applicant; the "
        "per-member calculation of months needed to reach a threshold; the six-month retirement check; "
        "assessment and collection of the actuarial true-up from a participant who does not retire; "
        "payroll-system changes; and the annual report to the General Assembly."))
A(("p", "**Why we are not carrying a number forward.** An earlier version of this proposal carried a "
        "$375,000 one-time estimate. That figure priced a certified-subsidy cap, a published queue and "
        "a central reservation system, none of which exist in the current design. The current design "
        "adds work the earlier one did not have. We would rather leave this line visible and empty "
        "than fill it with a figure we cannot defend."))

A(("h1", "10. Benefit-commencement cost"))
A(("p", "**Request.** For a purchase under item 5(b), the present-value cost to the trust fund of "
        "earlier benefit commencement, net of forgone future benefit accrual and forgone member and "
        "employer contributions for the period the member would otherwise have worked."))
A(("p", "**Why.** This is the largest cost in the proposal and no member payment can reach it. We have "
        "deliberately left it unquantified rather than estimate it, and our model says so in terms."))

A(("h1", "11. State health-insurance premium per employee — DHRM"))
A(("p", "**Request.** The current employer cost of state health insurance per active employee."))
A(("p", "**Why.** A position that is not refilled saves it; a position refilled at a lower salary does "
        "not. It is the one line missing from our workforce ledger."))

A(("h1", "12. Veterans among VaLORS and SPORS members — contingency only"))
A(("p", "**Request.** Active members of the Virginia Law Officers' Retirement System and the State "
        "Police Officers' Retirement System recorded as veterans, by plan tier, with the same note on "
        "the completeness of the field."))
A(("p", "**Why we are asking about plans the bill excludes.** The proposal excludes them expressly, "
        "and we expect an amendment to add VaLORS. We would rather price that amendment before it is "
        "offered than after. To do so we have had to apply the 6% classified-workforce veteran share "
        "to a law-enforcement population, where it is almost certainly too low, and we hold no "
        "Virginia figure to replace it with. **This item does not indicate any intention to expand "
        "the bill.**"))

A(("h1", "13. The hazardous-duty five-year service test — contingency only"))
A(("p", "**Request.** Whether purchased prior service — specifically qualifying active-duty military "
        "service — counts toward the five years of service credit required for a VaLORS or SPORS "
        "member to retire with an unreduced allowance at age 60 with hazardous-duty benefits; or "
        "whether that five years must be VaLORS, SPORS or enhanced-hazardous-duty covered service."))
A(("p", "**Why.** VRS publishes that purchased military service does not count toward the 20 years of "
        "hazardous-duty service the hazardous-duty supplement requires. Whether the same exclusion "
        "applies to the five-year eligibility test is the difference between 150 and 225 members in "
        "the reachable population we have computed for VaLORS. We have taken the stricter reading and "
        "would like to know whether it is right."))

# ------------------------------------------------------------------ items 14-17
# Added 12 October 2026 on the board's answer to the V2-assumption-annex question
# card: the letters had not gone out, so the four items the annex found are folded
# in here rather than held for a follow-up letter. Items 14 to 17 all bear on the
# veteran-share dial and the one published Commonwealth figure our model appears
# to contradict. Sources for each are named in V2-assumption-annex.
A(("h1", "14. Recovering the unknown veteran-status field — the cheapest item on this list"))
A(("p", "**Request — DHRM.** Of the share of the classified workforce whose veteran-status field is "
        "blank or recorded as unknown, is any part of it recoverable? In particular: from the DD-214s "
        "or equivalent discharge documents already held to award service credit toward annual leave "
        "under DHRM Policy 4.10; from the records supporting the veterans' hiring preference; or by a "
        "one-time voluntary survey of the existing workforce."))
A(("p", "**Why this one matters more than its position on the list suggests.** DHRM's presentation to "
        "the Senate Finance and Appropriations Committee of 3 February 2026 reports the field as 6% "
        "veteran, 25% not a veteran and **69% unknown**, as of 30 June 2025. On those three numbers "
        "the 6% is not an estimate of the veteran share of the workforce at all — it is the share of "
        "the whole workforce positively identified as veteran. The true share is bounded below by 6% "
        "and above by 75%. Among the 31% whose status is recorded, the veteran share is 19.4%."))
A(("p", "**What we have had to do instead, and why we distrust our own answer.** We model 6 / 8 / "
        "10% and treat 6% as a floor. We will not take 19.4% as a central estimate, because "
        "disclosure is almost certainly not random: Virginia gives veterans a hiring preference and "
        "Policy 4.10 leave credit, so a veteran has a concrete reason to disclose that a non-veteran "
        "does not. That makes 19.4% a ceiling on the unknowns-resemble-knowns reading rather than a "
        "midpoint. **We cannot narrow a 6-to-19% bracket from outside. One field recovery would close "
        "the widest assumption in our model, and it would do so for the Commonwealth's own workforce "
        "planning as much as for us.**"))

A(("h1", "15. Veteran status by age band, not only in total"))
A(("p", "**Request — DHRM, and VRS if VRS holds the field.** The veteran-status breakdown of the "
        "classified workforce **by age band** — five-year bands if available, otherwise 45-54, 55-64 "
        "and 65 and over against the all-ages figure."))
A(("p", "**Why.** Both pathways reach, deliberately, the oldest band in the plan, and veterans are "
        "not evenly spread across ages. U.S. Bureau of Labor Statistics 2025 annual averages put the "
        "veteran share of employed people at 7.84% at ages 55 to 64 against 4.98% across all ages — a "
        "factor of **1.57x**. We have had to apply that federal gradient to a Virginia floor, which is "
        "our arithmetic rather than anyone's data. **A Virginia age breakdown would replace it "
        "outright.** We would rather use your gradient than ours."))

A(("h1", "16. Regular-component against reserve-component military retired pay"))
A(("p", "**Request — DHRM, or VRS where VRS holds it.** Of identified veteran state employees who "
        "draw military retired pay, how many draw **regular-component** retired pay and how many "
        "**reserve-component** retired pay, including Guard and Reserve non-regular retirement."))
A(("p", "**Why, and this corrects something we previously had wrong.** We had been describing the "
        "eligibility condition as *no military pension*. The VRS rule as published is narrower: the "
        "service must not be service for which the member is receiving or is eligible to receive a "
        "military retirement, and reserve service that counts toward a reserve pension is treated "
        "differently from regular-component retired pay. The distinction decides whether a whole "
        "category of veteran employee is inside or outside the purchasable population, and it "
        "currently moves our estimate in both directions at once. **We hold no figure for the split "
        "and we are not going to invent one.**"))

A(("h1", "17. The definition behind the published retirement-eligibility rates"))
A(("p", "**Request — DHRM.** The definition and population behind the two retention measures "
        "reported as *eligible to retire today — 5.1%* and *eligible to retire within 2 years — 9.0%* "
        "on slide 12 of the 3 February 2026 Senate Finance and Appropriations presentation. "
        "Specifically: does *eligible* mean eligible for an **unreduced** allowance only, or does it "
        "include reduced retirement; and is the denominator the classified workforce, all "
        "VRS-covered state employees, or something else."))
A(("p", "**Why we are asking about your own figure rather than ours.** Our derivation from the VRS "
        "*Annual Actuarial Valuation, June 30 2025* age × service table puts roughly 6,254 Plan 1 and "
        "Plan 2 state employees already beyond the unreduced threshold — **7.7% of all 81,274 active "
        "State Employees, about 1.5x your published 5.1%.** The caveats are real and they do not "
        "dispose of it: your denominator is the classified workforce, which excludes wage employees "
        "and much of higher education, and if *eligible* includes reduced retirement the gap widens "
        "rather than closes."))
A(("note", "**We would rather reconcile this with you now than have it found in a fiscal note.** A "
           "sceptical reader will set your 5.1% against our 7.7% and conclude that one of us is "
           "wrong. It is entirely possible that both figures are right and they measure different "
           "populations — but we cannot demonstrate that without the definition, and we would not ask "
           "the General Assembly to take it on trust. If our figure is the wrong one we will correct "
           "it and say where it came from."))
A(("note", "**Items 14 to 17 were added after the rest of this letter was approved and before it was "
           "sent.** They come from an assumption-bounding exercise we ran on our own model, which "
           "found that the veteran-share dial sits at the bottom of the defensible range rather than "
           "through its middle. We have not moved any published figure of ours on that finding — we "
           "have recorded the ceiling alongside the range and asked you these four questions instead. "
           "The reasoning is in our V2 assumption annex and we will supply it on request."))
A(("hr",))

A(("h1", "What we will do with the answers"))
A(("p", "Publish them, with attribution and retrieval dates, and retire our own estimates. Every "
        "figure we have derived or assumed is labelled as such in our documents, and each item above "
        "names the figure it would replace. We will correct the record wherever a VRS figure differs "
        "from ours, including where it makes the proposal look worse."))
A(("p", "We have made no claim about the cost of this proposal and we will not make one. Our materials "
        "state that only VRS can price it."))

A(("h1", "What we are not asking for"))
A(("ul", [
    "No individual or identifiable member data. Aggregate counts only, suppressed to VRS's own "
    "threshold where a cell is small.",
    "No endorsement of the proposal, and no actuarial opinion beyond items 1 and 10.",
    "No bespoke modelling. Where a figure exists in a form VRS already produces, that form is fine.",
]))

A(("h1", "Contact and next step"))
A(("p", "Response requested by **20 November 2026**, to support a drafting request to the Division of "
        "Legislative Services by 30 November 2026. We are glad to take any part of this by meeting "
        "instead of in writing, and glad to narrow the request if items 1, 4 and 5 are the only ones "
        "that can be answered in the time available — those three carry most of the uncertainty."))
A(("p", "A separate letter accompanying this one asks a legal question about the enforceability of the "
        "retirement condition. It is sent together deliberately: item 1 here and question 1 there are "
        "the two items that decide whether this design survives."))
DR.extend(SIGNOFF)
A(("hr",))
A(("table", "Addressees", [
    ["", ""],
    ["To", "Patricia S. Bishop, Director, Virginia Retirement System, 1200 East Main Street, "
     "Richmond, VA 23219"],
    ["Copy", "Jillian L. Sherman, ACP, MPA, Legislative Liaison and Policy Analyst, VRS · Michael "
     "Cooper, Chief Operating Officer, VRS (item 9)"],
    ["To", "Janet L. Lawson, Director, Department of Human Resource Management, 600 East Main "
     "Street, 17th Floor, Richmond, VA 23219 — items 3, 9 and 11"],
    ["Copy", "Stacy Pendleton, Deputy Director, Human Resource Consulting Services, DHRM · Gary "
     "Johnston, Director of Health Benefits Services, DHRM"],
    ["Subject", "Data and actuarial-ratio request in support of a 2027 legislative proposal on "
     "purchase of prior military service"],
    ["Purpose", "To replace our estimates with VRS's and DHRM's own figures before a fiscal note is "
     "prepared"],
    ["Response requested by", "20 November 2026, to meet a 30 November drafting request"],
    ["Not a FOIA request", "This is legislative and policy correspondence. Several items ask for "
     "figures that would have to be computed, which the Freedom of Information Act does not require "
     "of a public body. We are asking rather than compelling"],
]))
A(("note", "**Sent by email and by post.** Email first, to the addresses in V2-send-packet §2, with "
           "this letter attached as a PDF; a signed hard copy follows by post. Verify each addressee "
           "by telephone on the day of sending."))

# ======================================================================= 3
CQ = []
A = CQ.append
A(("title", "Question to VRS counsel — is the true-up collectible?"))
A(("sub", APPROVED))
A(("p", "**Routing note.** VRS has no in-house general counsel; its published legal counsel is the "
        "Office of the Attorney General of Virginia. This letter is therefore addressed to the "
        "Director of VRS with a request that the question be referred to the Attorney General's "
        "office, or answered informally by whoever within VRS normally handles questions of "
        "administrability under Title 51.1. We are content with either."))
A(("hr",))

A(("h1", "The question in one paragraph"))
A(("p", "We are preparing a 2027 proposal under which a state employee who purchases qualifying "
        "military service at approximate normal cost must retire within six months, failing which the "
        "member must pay the actuarial-equivalent difference in order to keep the credit. Our question "
        "is whether that obligation can be made collectible in practice, and by what mechanism. We "
        "would rather know now that it cannot be, than draft a bill whose only consideration to the "
        "Commonwealth turns out to be unenforceable."))

A(("h1", "Why this question decides the design and not just the drafting"))
A(("p", "The proposal has two pathways. In one, the purchase advances the member's eligibility for an "
        "unreduced allowance — the Commonwealth receives an earlier retirement that it can observe. In "
        "the other, the member is already eligible for an unreduced allowance, so the purchased "
        "service does not advance eligibility at all. It raises the benefit amount."))
A(("p", "For that second pathway, the member's retirement is the only thing the Commonwealth receives "
        "in exchange for the preferential price, and the true-up is the only hard mechanism tying the "
        "preferential price to that retirement. The proposal deliberately carries no "
        "mechanism moving the resulting agency payroll savings into the trust fund. So if the true-up "
        "is not collectible, the second pathway is a benefit enhancement with no consideration at all, "
        "and we should either redesign it or drop it. That is a decision we can take in November. It "
        "is not one we want taken for us in a fiscal note in January."))

A(("h1", "What we think the answer probably is, so you can correct us rather than start from nothing"))
A(("p", "Our working assumption is that an obligation to pay money after the fact — by invoice, by "
        "payroll deduction, by offset against an allowance — is the weak form, because a member who "
        "declines to retire is also a member who may decline to pay, and the Commonwealth is then "
        "holding a receivable against a continuing employee. The stronger form is to withhold the "
        "service credit from the member's record until the condition is met: the member pays the "
        "approximate-normal-cost amount, the purchase is recorded as conditional, and the credit is "
        "applied to the record only on the earlier of (a) retirement within the six-month window, or "
        "(b) payment in full of the actuarial-equivalent amount. Nothing then has to be collected, "
        "because nothing has been granted."))
A(("p", "We do not know whether that structure is available under Title 51.1 as it stands, or whether "
        "it would create problems of its own. Hence the questions below."))

A(("h1", "The questions"))
A(("ol", [
    "**Can service credit be granted conditionally?** May VRS record a purchase of prior service as "
    "conditional — not credited to the member's record — pending either the member's retirement "
    "within a stated window or payment of the actuarial-equivalent amount? If so, does that require "
    "enabling language, and of roughly what kind?",
    "**If the credit must be granted on payment, is the resulting true-up collectible?** From a member "
    "who remains in covered employment, what mechanisms are actually available: billing, payroll "
    "deduction with or without the member's consent, offset against a future allowance, reversal of "
    "the credit, or refund of the member's payment and voiding of the purchase? Which of these does "
    "VRS consider workable in administration rather than merely available in law?",
    "**Can the credit be reversed instead of the difference collected?** If the member does not retire "
    "and does not pay, may VRS void the purchase and refund what the member paid, leaving the member "
    "where they started? We would regard that as an acceptable and clean outcome. Is it available?",
    "**Is there a federal tax constraint we have not seen?** Purchases are commonly made with pre-tax "
    "money or rollovers under Code § 414(h) or § 403(b)/§ 457 transfers. Does a conditional or "
    "reversible purchase create a qualification, constructive-receipt or distribution problem that a "
    "straightforward purchase does not? This is the question we are least equipped to answer "
    "ourselves.",
    "**Does conditioning a purchase price on retirement raise any issue beyond cost?** We are asking "
    "generally, not leadingly: anything in the nature of an age-related or ADEA-adjacent concern, "
    "anything in the Virginia Constitution's provisions on the trust, or any precedent in VRS's "
    "handling of retirement-incentive arrangements that we should know about. Our design keeps "
    "participation voluntary and the consequence of not retiring purely financial, which we believe is "
    "the right posture, but we would rather be told if it is not sufficient.",
    "**Has VRS administered anything like this before?** Any prior conditional purchase, "
    "retirement-window condition or incentive-linked service credit, and what the administrative "
    "experience was. If there is a reason this has not been done in Virginia, we would like to know it "
    "before we ask for a bill.",
    "**What would VRS need in the bill text?** If the structure is workable, what does the statute "
    "have to say for VRS to be able to administer it — and what should it not say, so that VRS retains "
    "the discretion it needs on timing, calculation and recordkeeping?",
]))

A(("h1", "What we are not asking"))
A(("p", "We are not asking for a view on the merits of the proposal, and we are not asking for a cost "
        "estimate — that is the subject of the data request sent alongside this letter. We are not "
        "asking for a formal legal opinion if an informal view by meeting is easier; we will record "
        "whatever we are told accurately, including a view that the mechanism will not work."))

A(("h1", "Our own position, on the record"))
A(("p", "We have made no claim that this proposal is actuarially neutral, minimal in impact, or "
        "self-funding, and we will not make one. Our published materials state that only VRS can price "
        "it. If the answer to question 1 or question 2 is that no workable mechanism exists, we will "
        "say so in our materials and change the design accordingly."))
CQ.extend(SIGNOFF)
A(("hr",))
A(("table", "Addressee", [
    ["", ""],
    ["To", "Patricia S. Bishop, Director, Virginia Retirement System, 1200 East Main Street, "
     "Richmond, VA 23219 — with a request to refer to the Office of the Attorney General"],
    ["Copy", "Jillian L. Sherman, ACP, MPA, Legislative Liaison and Policy Analyst, VRS"],
    ["Subject", "Enforceability and mechanism of an actuarial true-up conditioned on a member's "
     "retirement"],
    ["Sent with", "Data and actuarial-ratio request of the same date. Item 1 there and question 1 "
     "here are the two items that decide whether this design survives"],
    ["Response requested by", "20 November 2026"],
]))
A(("note", "**Sent by email and by post.** Email first, with this letter attached as a PDF; a signed "
           "hard copy follows by post. See V2-send-packet."))


# ======================================================================= 4
SP = []
A = SP.append
A(("title", "Send packet — the email text, the hard copy, and the day-of-send checks"))
A(("sub", "Internal instruction sheet. Not enclosed with the letters · Policy Director · MOO-100 · "
          "12 October 2026"))
A(("p", "Three decisions were taken on 12 October 2026: the letters go out over **Moody's own "
        "signature as the proposal's author, with no organisation named**; they go out **this week**, "
        "with 20 November and 30 November held; and they go **by both channels — email first, hard "
        "copy to follow**. This sheet is everything needed to act on that. Paste §2, attach §3, post "
        "§4, tick §5, record §6."))
A(("note", "**I cannot send these.** No outbound mail channel exists in this session, and a letter "
           "signed personally has to leave from a real mailbox in any case. Everything that does not "
           "require you is finished."))
A(("p", "**The closing block on both letters is now complete.** Nothing is bracketed and nothing is "
        "left to type in. It reads: *David Moody · Author of the proposal, writing in a personal "
        "capacity · 1154 West Ocean View, Norfolk, VA 23503 · davidmoody@gmail.com · 434-989-5481 · "
        "13 October 2026.* The only field that may still need changing is the date line, if the "
        "letters actually go out on a different day. Two telephone calls and the send itself are all "
        "that is left."))
A(("hr",))

A(("h1", "1. Two emails, not three"))
A(("p", "**One email to VRS carrying both letters, and one to DHRM carrying only the data request.** "
        "The board decided the two letters travel together, and the reason holds — item 1 of the data "
        "request and question 1 of the counsel letter are the two items that decide whether the design "
        "survives, and splitting them invites VRS to answer the easy one. The counsel question is not "
        "DHRM's to answer and sending it there would blur who owns what."))
A(("p", "**The alternative is two separate emails to VRS**, one per letter, which is easier for VRS to "
        "route internally — the data request goes to the actuary via the Board, the legal question to "
        "the Attorney General's office. If you prefer that, send them within the same hour and say in "
        "each that the other exists. The thing to avoid is sending one this week and the other in a "
        "fortnight."))
A(("table", "Table 1 — the two sends", [
    ["", "Email 1 — VRS", "Email 2 — DHRM"],
    ["Send from", "**davidmoody@gmail.com**, display name *David Moody*",
     "**davidmoody@gmail.com**, display name *David Moody*"],
    ["To", "**pbishop@varetire.org** (Patricia S. Bishop, Director)",
     "**policy@dhrm.virginia.gov**, addressed to Janet L. Lawson, Director"],
    ["Copy", "Jillian L. Sherman, Legislative Liaison — *address not published; confirm on "
     "804-771-7373.* **mcooper@varetire.org** for the administration-cost item",
     "**compensation@dhrm.virginia.gov** · **ohb@dhrm.virginia.gov**"],
    ["Attachments", "Both letters, as PDFs", "The data request only, as a PDF"],
    ["Scope", "Items 1–13 and all seven legal questions", "Items 3, 9 and 11 only"],
    ["Hard copy to", "1200 East Main Street, Richmond, VA 23219",
     "600 East Main Street, 17th Floor, Richmond, VA 23219"],
]))
A(("note", "**Do not use FOIA@varetire.org.** It is published and it would reach someone, and it is "
           "the wrong channel: the Freedom of Information Act does not require a public body to "
           "create a record that does not exist, and most of what we are asking for would have to be "
           "computed. Filing as FOIA invites a lawful refusal on our most important items. FOIA stays "
           "in reserve for the underlying records if the Director declines to compute anything."))
A(("hr",))

A(("h1", "2. The email text, ready to paste"))
A(("h2", "2.1 Email 1 — to VRS"))
A(("p", "**Subject:** Data request and a legal question — a 2027 proposal on purchase of prior "
        "military service (response requested by 20 November)"))
A(("p", "Dear Ms Bishop,"))
A(("p", "I am preparing a proposal for the 2027 session of the General Assembly. It would create a "
        "bounded four-year pilot under which a Plan 1 or Plan 2 state employee who is a veteran could "
        "purchase qualifying active-duty military service at approximate normal cost after the "
        "existing 24-month window has closed, in each case in exchange for retiring within six "
        "months. The existing cost window, the 48-month military-service maximum and the eligibility "
        "conditions in the Code would all be left as they are."))
A(("p", "Two letters are attached. The first asks for thirteen figures that would let the General "
        "Assembly see the real cost of the proposal; the first item is the only one that genuinely "
        "decides whether it is affordable, and nothing I can build substitutes for it. The second asks "
        "a legal question about whether the retirement condition can be made collectible at all. They "
        "are sent together deliberately, because together they decide whether the design survives."))
A(("p", "I should be clear about what this is not. I am not asking VRS to endorse the proposal, and I "
        "make no claim that it is actuarially neutral, minimal in impact or self-funding — my "
        "published materials say that only VRS can price it. This is not a Freedom of Information Act "
        "request; several items would have to be computed rather than retrieved, and I am asking "
        "rather than compelling. If a figure cannot reasonably be produced, saying so is a complete "
        "answer and I will record it that way."))
A(("p", "A response by 20 November 2026 would let me put a drafting request to the Division of "
        "Legislative Services by 30 November. If that is too tight, items 1, 4 and 5 carry most of "
        "the uncertainty and I would be glad to narrow the request to those three. I would also be "
        "glad to take any part of this by meeting or telephone instead of in writing."))
A(("p", "Signed copies of both letters follow by post. I am copying Ms Sherman as the published "
        "channel for legislative and policy correspondence, and Mr Cooper for the "
        "administration-cost item alone."))
A(("p", "Yours sincerely,"))
A(("p", "David Moody · author of the proposal, writing in a personal capacity"))
A(("p", "davidmoody@gmail.com · 434-989-5481"))
A(("p", "1154 West Ocean View, Norfolk, VA 23503"))

A(("h2", "2.2 Email 2 — to DHRM"))
A(("p", "**Subject:** Workforce and benefit-cost data request — a 2027 proposal on purchase of prior "
        "military service (three items; response requested by 20 November)"))
A(("p", "Dear Ms Lawson,"))
A(("p", "I am preparing a proposal for the 2027 session of the General Assembly for a bounded "
        "four-year pilot under which Plan 1 and Plan 2 state employees who are veterans could "
        "purchase qualifying military service at approximate normal cost in exchange for a near-term "
        "retirement. The attached data request is addressed jointly to VRS and to DHRM. **Only three "
        "of its items are DHRM's: item 3 on veteran status in the state workforce, item 9 on "
        "administration cost, and item 11 on the employer share of the health premium.** The rest are "
        "VRS's and have gone to the Director of VRS separately."))
A(("p", "Item 3 is the one I would most like help with. The veteran-status field in the state "
        "workforce record is substantially incomplete, and the proposal is sized at present on "
        "Virginia's veteran share of the civilian labour force applied to the classified workforce — "
        "an assumption, and I have labelled it as one everywhere it appears. Any Virginia figure, "
        "however partial, is better than that, and knowing how incomplete the field is would itself "
        "be useful. Producing the first real data on this is one of the pilot's stated purposes."))
A(("p", "A response by 20 November 2026 would let me put a drafting request to the Division of "
        "Legislative Services by 30 November. I am glad to take any of it by meeting. A signed hard "
        "copy follows by post. I am copying the compensation and health-benefits mailboxes for the "
        "items that fall to them."))
A(("p", "Yours sincerely,"))
A(("p", "David Moody · author of the proposal, writing in a personal capacity"))
A(("p", "davidmoody@gmail.com · 434-989-5481"))
A(("p", "1154 West Ocean View, Norfolk, VA 23503"))
A(("note", "**The sending account is davidmoody@gmail.com, which satisfies the signature decision.** "
           "A personal Gmail address names no organisation and adds no footer of its own. Two things "
           "to check once: that no signature has been configured on the account that names an "
           "organisation, and that the display name reads *David Moody* rather than a group or role "
           "name. If a signature is set, strip it — the letters carry their own closing block."))
A(("hr",))

A(("h1", "3. Attachments — use the **-SEND** files, not the working copies"))
A(("table", None, [
    ["Email", "Attach", "As"],
    ["VRS", "**V2-data-request-VRS-DHRM-SEND.pdf** · **V2-counsel-question-trueup-SEND.pdf**",
     "PDF, both"],
    ["DHRM", "**V2-data-request-VRS-DHRM-SEND.pdf**", "PDF"],
]))
A(("note", "**There are two versions of each letter and only one of them can leave the building.** "
           "The working copies carry an internal banner under the title — “Approved for transmission "
           "by the board” — and an internal note at the foot. Neither belongs on a letter to a public "
           "body. The banner in particular reads as an organisation acting, and the decision was that "
           "no organisation is named. **The -SEND files are identical in substance with the banner and "
           "the internal note removed and a plain subject-and-date line in their place.** The working "
           "copies stay in the folder as our record of what was approved."))
A(("p", "**Send the PDFs, not the .docx files.** A Word file invites editing and arrives with revision "
        "history and author metadata attached. Nothing else goes — not the fiscal model, not the "
        "scenario tables, not the goal set, and above all not the VaLORS annex, which prices an "
        "amendment to a plan the bill expressly excludes."))
A(("p", "**If asked for the model, send it.** The offer is already in the data request and it is the "
        "right posture: the model is built from published VRS data and labels every assumption as an "
        "assumption. V2-fiscal-model.pdf and V2-fiscal-model-scenarios.pdf are the two to send. "
        "Volunteering them unasked, on the other hand, invites VRS to review our arithmetic instead "
        "of answering our questions."))
A(("hr",))

A(("h1", "4. Hard copy"))
A(("ol", [
    "Print **V2-data-request-VRS-DHRM-SEND.pdf** and **V2-counsel-question-trueup-SEND.pdf** on plain "
    "paper — the -SEND files, not the working copies. **No letterhead** — not an organisation's, not "
    "a committee's.",
    "Sign both in ink above the rule in the closing block. Date them the day they are posted.",
    "**VRS envelope:** both letters. Patricia S. Bishop, Director, Virginia Retirement System, 1200 "
    "East Main Street, Richmond, VA 23219.",
    "**DHRM envelope:** the data request only. Janet L. Lawson, Director, Department of Human "
    "Resource Management, 600 East Main Street, 17th Floor, Richmond, VA 23219.",
    "Post the same day as the email, or the next. The email is the one that will actually be read "
    "first; the hard copy is what makes it a letter on the record.",
    "Keep a signed scan of each. If the 20 November date passes and a patron takes this up, the "
    "scans are the evidence that the questions were asked first and asked civilly.",
]))
A(("note", "**Correction worth knowing about before you address an envelope: DHRM is not in the James "
           "Monroe Building.** Our earlier draft had 101 North 14th Street, 12th Floor. DHRM's own "
           "published address is 600 East Main Street, 17th Floor. Mail to the old address would "
           "probably still arrive, and it would announce that we had not checked."))
A(("hr",))

A(("h1", "5. The day-of-send checks"))
A(("table", "Table 2 — tick these before anything leaves", [
    ["#", "Check", "Why it matters"],
    ["1", "**Call VRS, 804-771-7373.** Confirm Patricia S. Bishop is still Director and Jillian L. "
     "Sherman is still Legislative Liaison and Policy Analyst. Ask for Ms Sherman's email address",
     "Two of the offices we originally drafted to do not exist. A letter to a predecessor reads as "
     "carelessness about exactly the kind of detail we are asking VRS to be careful about — and we "
     "still have no published address for Ms Sherman"],
    ["2", "**Call DHRM, 804-225-2131.** Confirm Janet L. Lawson is still Director, and ask whether "
     "policy@ or a direct address is the better route", "DHRM publishes no individual staff "
     "addresses. I will not put an inferred address on an outgoing letter"],
    ["3", "**Read the closing block on both letters once.** It should read: David Moody · Author of "
     "the proposal, writing in a personal capacity · 1154 West Ocean View, Norfolk, VA 23503 · "
     "davidmoody@gmail.com · 434-989-5481", "It is complete — there is nothing bracketed left in "
     "either letter. This check is to catch a typed digit in the telephone or the postcode, which "
     "is the one error a reader cannot work around"],
    ["4", "**Set the date line to the actual send day**", "It currently reads 13 October 2026. "
     "Nothing else in either letter moves with it"],
    ["5", "**Check the sending account's footer and domain** for any organisation name or logo",
     "The signature decision is that no organisation is named. An automatic footer undoes it"],
    ["6", "**Confirm both attachments are the -SEND PDFs** — not the working copies, not the .docx — "
     "and that the VaLORS annex is not among them", "The working copies carry an internal “approved "
     "by the board” banner, which contradicts the signature decision. The annex prices an amendment "
     "to a plan the bill expressly excludes; enclosing it would read as a signal that we intend to "
     "expand the bill"],
]))
A(("note", "Checks 1 and 2 are two telephone calls and about five minutes. They are the only part of "
           "this that cannot be done in advance, and they are the part most likely to be skipped."))
A(("hr",))

A(("h1", "6. Send record — fill this in"))
A(("table", None, [
    ["Item", "Date", "To", "Note"],
    ["Email — VRS", "", "", ""],
    ["Email — DHRM", "", "", ""],
    ["Hard copy posted — VRS", "", "", ""],
    ["Hard copy posted — DHRM", "", "", ""],
    ["Acknowledgement received — VRS", "", "", ""],
    ["Acknowledgement received — DHRM", "", "", ""],
    ["Substantive response — VRS", "", "", ""],
    ["Substantive response — DHRM", "", "", ""],
]))
A(("p", "Send me the dates and I will keep this as the record on MOO-100. When a response arrives, the "
        "figures it carries replace ours — the data request names, item by item, which of our figures "
        "each one supersedes, so the swap is mechanical rather than a matter of judgment."))
A(("hr",))

A(("h1", "7. What happens if nothing comes back"))
A(("p", "**About 10 November is the date to watch, not 20 November.** If nothing substantive has "
        "arrived by then, the question is not whether to extend our own deadline. It is whether a "
        "patron asks the same questions, which is the stronger route we deliberately kept in reserve "
        "by signing these ourselves. VRS answers a legislator's request differently from a citizen's."))
A(("p", "**If the answer to item 1 or to legal question 1 is unwelcome, that is the letters working.** "
        "The actuarial ratio could come back high enough to make the pilot unaffordable, and the "
        "true-up could come back uncollectible — in which case the Retirement Incentive pathway has no "
        "consideration at all and has to be redesigned. Far better that we learn either of those in "
        "November and redesign, than have it decided for us in a January fiscal note."))
A(("hr",))
A(("p", "*Sources for every name, title, address and email in this document: VRS Leadership page "
        "(pbishop@, mcooper@, and Policy, Planning and Compliance shown as TBA); VRS Freedom of "
        "Information Act page (Jillian L. Sherman, address, telephone, FOIA mailbox); DHRM Contact Us "
        "page (600 East Main Street 17th Floor, telephone, fax, policy@, compensation@, ohb@); DHRM "
        "Our Leadership page (Lawson, Pendleton, Johnston). All retrieved 12 October 2026. Inferred "
        "addresses are marked as inferred and are not used.*"))


_FP = [
    (r"\bWe are\b", "I am"), (r"\bwe are\b", "I am"),
    (r"\bWe were\b", "I was"), (r"\bwe were\b", "I was"),
    (r"\bWe\b", "I"), (r"\bwe\b", "I"),
    (r"\bOurselves\b", "Myself"), (r"\bourselves\b", "myself"),
    (r"\bOurs\b", "Mine"), (r"\bours\b", "mine"),
    (r"\bOur\b", "My"), (r"\bour\b", "my"),
    (r"\bUs\b", "Me"), (r"\bus\b", "me"),
]


def first_person(blocks):
    """The letters are signed by one person in a personal capacity, so they
    cannot say 'we'.

    A letter signed 'David Moody, writing in a personal capacity' that then
    says 'our board has decided' names an organisation by implication, which
    is exactly what the signature decision of 12 October 2026 ruled out. The
    internal documents keep 'we'; the two outgoing letters do not.
    """
    def fix(s):
        for pat, rep in _FP:
            s = re.sub(pat, rep, s)
        return s

    out = []
    for b in blocks:
        if b[0] in ("title", "sub", "h1", "h2", "p", "note"):
            out.append((b[0], fix(b[1])))
        elif b[0] in ("ul", "ol"):
            out.append((b[0], [fix(i) for i in b[1]]))
        elif b[0] == "table":
            out.append(("table", fix(b[1]) if b[1] else b[1],
                        [[fix(str(c)) for c in row] for row in b[2]]))
        else:
            out.append(b)
    return out


def send_copy(blocks, subline):
    """The version that actually goes to VRS and DHRM.

    The working copies carry an internal status banner under the title and an
    internal note at the foot. Neither belongs on a letter to a public body:
    the banner says 'approved by the board', which reads as an organisation
    acting, and the decision was that no organisation is named. This strips
    both and puts a plain subject-and-date line in their place.
    """
    out = []
    for b in blocks:
        if b[0] == "sub":
            out.append(("sub", subline))
        elif b[0] == "note" and b[1].startswith("**Sent by email and by post."):
            continue
        else:
            out.append(b)
    return out


_SUB = f"David Moody · {SEND_DATE} · response requested by 20 November 2026"
DR = first_person(DR)
CQ = first_person(CQ)
DR_SEND = send_copy(DR, _SUB)
CQ_SEND = send_copy(CQ, _SUB)


if __name__ == "__main__":
    for blocks, stem in ((T, "V2-transmittal-VRS-DHRM"),
                         (DR, "V2-data-request-VRS-DHRM"),
                         (CQ, "V2-counsel-question-trueup"),
                         (SP, "V2-send-packet"),
                         (DR_SEND, "V2-data-request-VRS-DHRM-SEND"),
                         (CQ_SEND, "V2-counsel-question-trueup-SEND")):
        for p in render.build(blocks, stem, HERE, SCRATCH):
            print("wrote", p)
