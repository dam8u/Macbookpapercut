# AgentFilesV2 — index

*VRS Plan 1 / Plan 2 legislation, version 2 · Policy Director · MOO-100 · updated 12 October 2026 · internal, pre-decisional*

All V2 files live in this folder. **Every deliverable is a .docx and a .pdf.** Nothing you need to read, file, edit or send exists only as a web page.

---

## Read in this order

| # | File | What it is |
|---|---|---|
| 1 | **V2-decisions-adopted** | **The board decisions of 12 October 2026. The authoritative record.** Where any other document appears to differ, this one controls. **Start here.** |
| 2 | V2-goal-set | The governing 25-goal set, the amendment register at §7, the verification section, and the findings from building the model |
| 3 | V2-fiscal-model | The model written out — method, sources, three ledgers, sensitivity. **Amendment 1 of 12 October 2026 adds §6.1**, the snapshot limitation |
| 4 | V2-fiscal-model-scenarios | **The model on paper.** Every number the sliders produce, printed across the full range of each slider |

## The send packet — signed by Moody, going out the week of 12 October 2026

| File | What it is | Status |
|---|---|---|
| **V2-send-packet** | **New. The email text to paste, the attachment list, the hard-copy instructions, six day-of-send checks and a send record.** Internal. **Start here when you are ready to send** | Ready |
| V2-transmittal-VRS-DHRM | Cover document. Every addressee with the email channel for each, the signature decision and the reasoning, the routing, and §4's done-and-left table | Updated — signature now recorded as decided and the closing block complete |
| **V2-data-request-VRS-DHRM-SEND** | **The copy that actually goes.** Thirteen items, k first. No internal banner, no internal notes, first person throughout | **Attach this one. Not yet sent** |
| **V2-counsel-question-trueup-SEND** | **The copy that actually goes.** Seven questions on whether the true-up is collectible, addressed to the Director with a request to refer to the Attorney General | **Attach this one. Not yet sent** |
| V2-data-request-VRS-DHRM · V2-counsel-question-trueup | The working copies, with the “approved for transmission” banner and the internal notes. **Our record of what was approved** | Internal. **Do not send** |

**There are two versions of each letter and only one can leave the building.** The working copies carry an internal banner under the title that reads “Approved for transmission by the board.” On a letter signed personally, with no organisation named, that sentence contradicts the signature. The **-SEND** files are identical in substance with the banner and the internal notes removed.

**Both letters also had to be rewritten into the first person.** They said “we” 111 times between them, and a letter signed “writing in a personal capacity” that says “our board has decided” names an organisation by implication. Every instance is converted and the one sentence that named a board is gone. The internal documents still say “we”; the two outgoing letters do not.

**Signature: Moody's own, as the proposal's author, with no organisation named.** Decided 12 October 2026. The patron route stays in reserve for 10 November, if nothing substantive has come back by then.

**Three corrections to the addressees, all found from published sources.** Two offices we had drafted to do not exist — VRS has no in-house actuary (Gabriel, Roeder, Smith & Company is the consulting actuary, under contract to the Board) and no in-house general counsel (its published legal counsel is the Office of the Attorney General). And **DHRM is not in the James Monroe Building**: its published address is 600 East Main Street, 17th Floor. Both letters now go to the respective Directors at the corrected addresses.

**Do not send the data request to FOIA@varetire.org.** FOIA does not require a public body to create a record that does not exist, and most of our items would have to be computed. Filing as FOIA invites a lawful refusal on the items that matter most. Send-packet §1 has the reasoning; FOIA stays in reserve for the underlying records.

**The signature block on both letters is complete.** Name, return address, email and telephone were supplied on 12 October 2026 and are applied: *David Moody · Author of the proposal, writing in a personal capacity · 1154 West Ocean View, Norfolk, VA 23503 · davidmoody@gmail.com · 434-989-5481.* No organisation is named anywhere in the block, which is the signature decision of the same date. Nothing in either outgoing letter is bracketed. The only field that may still need changing is the date line, if the send day moves.

## Assumptions and sourcing

| File | What it is | Status |
|---|---|---|
| **V2-assumption-annex** | **New. 8 pages.** Bounds the model's three dials against published DHRM and BLS figures. Finds that DHRM's 6% veteran share is a floor on a field that is **69% unknown**, that the pathways target the one age band where veterans run **1.57x** their all-ages share, and that our 7.7% already-eligible figure is **1.51x** DHRM's published 5.1%. Also corrects the VRS military-pension rule — Reserve and Guard service is expressly carved out of it | **Internal. Changes no published figure — section 11 holds the decision** |

**Headline: the model's veteran-share range of 6 / 8 / 10% sits at the bottom of the defensible range, not through its middle.** The high case of 10% is roughly the DHRM floor once the age band is accounted for. On these sources the published mid of 42 participants is between 1.2x and 3.8x too low. Four items added for the data request.

## Reserve — not for circulation

| File | What it is | Status |
|---|---|---|
| **V2-annex-VaLORS-prescore** | **New. 12 pages.** The VaLORS amendment priced before it is offered, per the board's decision of 12 October 2026. Includes a SPORS pre-score and says why JRS is deliberately unscored | **Reserve. Not attached to the bill, the fiscal note, the one-pager or the brief** |

**Headline: the amendment is small.** At mid take-up, adding all 7,459 law officers to the pilot adds about **2.8 participants and about $51,726** in member payments over four years — roughly **9% on top of the bill as scoped**. The reason is the plan's own eligibility rules: VaLORS averages 39.6 years of age and 8.3 years of service, and only **7.8%** of the plan sits in either pathway, against 29.8% of the State Employees plan.

## For advocacy

| File | What it is | Status |
|---|---|---|
| V2-JLC-one-pager | One page. The 2027 package ask | Rewritten on the V2 architecture, 12 October 2026 |
| V2-advocacy-brief | Two pages. The case, the five questions you will be asked, and what we are honest about | Rewritten on the V2 architecture, 12 October 2026 |

**The V1 one-pager and V1 brief must not be circulated.** Both argued that Virginia's 24-month purchase window should be repealed. That is no longer our position and it is now the wrong central claim.

## Optional, and working files

| File | What it is |
|---|---|
| vrs-v2-fiscal-model.html | The State Employees model with live sliders, for exploring between the printed cases. Double-click; any browser; no internet needed. It adds no figure the scenario tables omit |
| valors_model.py | The VaLORS and SPORS computation. Every figure in the annex comes from it, so the annex and the model cannot drift |
| render.py · docx_to_blocks.py · build_*.py · amend_fiscal_model.py | Document build scripts. One source per document, emitted as both .docx and .pdf |
| README.md | Plain-text source of this index. Can be ignored |

---

## The twelve decisions, in one table

| # | Decision | Applied as |
|---|---|---|
| 1 | **Denominator** | 177,807 is system-wide context only. The modeling denominator is **28,994**, derived from the VRS valuation age × service table. The earlier ~39,000 pro-rata estimate is superseded |
| 2 | **Reach bounds** | Take-up **5% / 12% / 25%**, giving **17 / 42 / 86** participants. Full three-dial range **9 to 141** |
| 3 | **Bridge screen** | The purchasable screen — **2,396**. G9's “within four years” screen (5,177) is retired as a Bridge figure |
| 4 | **Plan scope** | **State Employees (non-hazardous-duty) only**, with SPORS, VaLORS and JRS excluded **expressly in the bill** |
| 5 | **Plan 2** | Legally eligible for the Bridge, **scored at zero**. Proximity assumptions 12% and 13% **withdrawn**; derived 4.0% and 6.7% govern |
| 6 | **Payroll saving** | **No transfer mechanism.** It stays in agency appropriations and never nets against the pension cost |
| 7 | **Send the data request** | **Authorised.** Addressees corrected and email channels identified. Prepared, not yet transmitted |
| 8 | **Send the counsel question** | **Authorised, together with the data request.** One email to VRS carrying both letters; one envelope |
| 9 | **Pre-score a VaLORS amendment** | **Done.** V2-annex-VaLORS-prescore. Held in reserve |
| 10 | **Signature** | **Moody's own, as the proposal's author. No organisation named.** No letterhead, and check the sending account's footer |
| 11 | **Send date** | **The week of 12 October 2026.** 20 November response date and 30 November drafting target both unchanged. Letters dated 13 October; change to the actual day |
| 12 | **Channel** | **Both — email first, hard copy to follow.** Two emails: VRS with both letters, DHRM with the data request only. PDFs, not .docx |

## What to look at in the numbers

Open **V2-fiscal-model-scenarios.pdf** at **Table 4**, the reach grid, then **Table 7**, the subsidy at four values of k.

**k is the ratio of actuarial-equivalent cost to approximate normal cost, and it is the number that decides whether this bill is affordable.** Only VRS can supply it. It is item 1 of the data request.

One thing worth seeing in Table 4: take-up is the dial the board set, but it is not the strongest one. Holding take-up at mid and moving only the qualifying-service share from 35% to 65% takes participants from 29 to 54. **That dial has no source at all.** G24 closes it; nothing else can.

## One rule the model never breaks

The agency payroll saving is **agency appropriation, not VRS trust-fund money.** Nothing in the design moves it. No headline nets it against the pension cost. That is G11, reinforced by decision 6, and every ledger in every document keeps them apart.

## Still open, with owners

| # | Item | Owner |
|---|---|---|
| 1 | **k** — the actuarial-equivalent to approximate-normal-cost ratio, by age band and tier, both pathways | VRS, through its consulting actuary |
| 2 | The G24 counts — state Plan 1/Plan 2 members, veterans among them, members with qualifying purchasable service, average qualifying military months | VRS and DHRM |
| 3 | Is the G5 true-up collectible? | VRS, referred to the Office of the Attorney General |
| 4 | A V2 administrative-cost estimate. V1's $375,000 does not carry over | VRS and DHRM |
| 5 | State health-insurance premium per employee | DHRM |
| 6 | **The two verification calls and the act of sending.** The signature block is now complete | **The board.** Everything else on both letters is finished |
| 7 | Does purchased military service reach the VaLORS five-year hazardous-duty threshold? Worth 150 against 225 members in the reserve annex | VRS — item 13 of the data request |
| 8 | Pathway counts projected to the pilot years rather than the valuation date | VRS — item 5 of the data request, and §6.1 of the fiscal model |
| 9 | JRS weighted-service-credit rules, if a judicial amendment is ever offered | Policy Director |

**Drafting request target: 30 November 2026. Data-request response date: 20 November 2026.** The letters go out the week of 12 October, which gives VRS about five and a half weeks. **The date to watch is about 10 November** — if nothing substantive has arrived by then, the question is whether a patron asks the same questions, not whether to extend our own deadline.
