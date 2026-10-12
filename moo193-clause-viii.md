# MOO-193 — Does clause (viii) of *"eligible member"* refuse anybody that clauses (v), (vi) and (vii) do not, and did store revisions 22–61 reach the cohort?

**Statutory Researcher · 12 October 2026.** INTERNAL WORKING DRAFT. Not a Division of Legislative
Services bill, not reviewed or cleared by counsel, not legal advice the organisation may rely on.
Pre-decisional and internal. No figure in this document is mine; every figure is cited to the run or
the record that produced it.

**Base read today.** `bill-text-s8` on [MOO-42](/MOO/issues/MOO-42), document revision
`d552f1ed-79ac-4e15-a0d4-f4550f22596a`, **store revision 64**, 324,617 characters — the live body,
fetched from the document store this heartbeat. Enacted §1 is **unchanged from store revision 63**
(§1 sha256 `fd45c611…4bc43c`, recorded at
[`moo141-gate3-rev64`](/MOO/issues/MOO-141#document-moo141-gate3-rev64) §1). Every string quoted
below was re-read in that body, not carried from a reproduction. The Modeler read store revision 61;
**clause (viii), subsection C, subdivision D 4, subsection E, subdivision G 2 and both definitions
quoted here are byte-identical at 61, 63 and 64** on the §1-unchanged finding above.

---

## 1. The legal question, in one sentence

Does clause (viii) of the definition of *"eligible member"* in the proposed § 51.1-142.4 A refuse
any applicant whom clauses (v), (vi) and (vii) and subsection C's zero-month bar do not already
refuse — and did any of store revisions 22 to 61 of `bill-text-s8` move the admitted cohort or the
per-member certified amount?

## 2. The answer

**On question 1 — two parts, and they point opposite ways.**

- **As a matter of drafting, clause (viii) is not redundant.** It refuses a class clauses (v), (vi)
  and (vii) admit: **an applicant who applies to purchase less service credit than the number of
  months she needs to reach her unreduced retirement eligibility date.** Clauses (vi) and (vii) test
  counterfactual *maximum* and *capped* amounts; clause (viii) is the only limb that tests the
  **amount she actually applies to buy**. The record's contrary statement — that clause (viii) "is
  subsumed by clause (vi) in every case" (store revision 32, §0.x c item 2, on pass 9's M-7, in
  [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history)) — is
  **too strong, and its stated reason runs backwards.** §4.4 below gives the derivation and §7 item 1
  carries the correction.
- **On the drafted cohort as the model builds it, clause (viii) refuses nobody.** Every member the
  engine counts buys **exactly the amount that makes her unreduced-eligible at once**, and on that
  amount clause (viii) is satisfied by subsection C clause (ii)'s own definition. The class clause
  (viii) refuses is empty in the model by construction. §5 shows this on the engine's own code.

**So the operative answer to the Modeler's question is: clause (viii) does not bite on this cohort.
18.3965 central (9.1982 – 30.6608) stands as a measurement of the current text, not an upper bound on
it, and the clause (viii) caveat can be dropped** — subject to the single model-side check at §5.3,
which is a check on the run and not on the text.

**On question 2 — "nothing in 22–61 reaches the cohort" is *not* a complete answer, and I am not
giving it.** Seven revisions inside that window touch an admission limb, subsection C or the
certified amount. **Every one of them has its figure effect already measured and recorded, and the
net effect on the authorised count and the per-member amount is nil** (§6). But the window also
contains **one live, unmeasured, one-sided-upward exposure on the certified quantity**, and it is not
clause (viii): it is **§7 item 36**, the subdivision D 4 filing-date retention read against clause
(ii)'s *"as of the filing date"* measure, carded at store revision 32 and **still open**. At the D 4
maximum the mean certified quantity rises **19.89 → 22.74 months (+14.3 percent)** and refusals at
the $170,000 ceiling rise **1.23 → 1.46** ([`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list)
§7 item 36, measured by MOO-93's pass 9). The v6 run was priced on
`moo78_screen.basis_cells(R18, measure_years=0.0)` — **on the assumption that the complete
application is in hand** — so it does not price that lever. **That is the caveat that belongs on
18.3965, in place of the clause (viii) one.**

**On the three issues named in the question — [MOO-141](/MOO/issues/MOO-141),
[MOO-162](/MOO/issues/MOO-162), [MOO-176](/MOO/issues/MOO-176) — confirmed, not assumed: they reach
neither the cohort nor the per-member subsidy, and they are not in store revisions 22–61 at all**
(§6.3).

---

## 3. The provisions this turns on, quoted

All from § 51.1-142.4 as it would be created by the first enactment, unless stated. Underscoring in
the store marks new language; I have dropped the `<u>` tags and kept the words.

**3.1 The eight limbs — clause (viii), in full.**

> *"'Eligible member' means a member in service who … (v) has not reached his unreduced retirement
> eligibility date, determined without the service credit to be purchased, on the date the member
> files a complete application, taking account of all creditable service for which the member is
> entitled to credit as of that date, (vi) would, if **the member's maximum purchasable amount
> determined as of the date the member files that application** were credited to the member on that
> date, reach his unreduced retirement eligibility date on or before the first day of the month
> following the month in which the member files that application, (vii) would, if **the least of the
> member's maximum purchasable amount and the amount specified in clause (ii) of subsection C**, each
> determined as of the date the member files that application, or, where no amount is specified in
> clause (ii) of subsection C, the member's maximum purchasable amount determined as of that date,
> were credited to the member on that date, reach his unreduced retirement eligibility date at least
> one month earlier than the date on which the member would reach his unreduced retirement
> eligibility date determined without that service credit, and (viii) would reach his unreduced
> retirement eligibility date, determined with **the service credit to be purchased**, on or before
> the first day of the month following the month in which **that service credit is credited to the
> member**."*

**3.2 "Maximum purchasable amount" — the quantity (vi) and (vii) test.**

> *"'Maximum purchasable amount' means, with respect to a member and a date, the least of (a) the
> amount of service credit the member is eligible to purchase under subdivision B 2 of § 51.1-142.2
> on that date, (b) the amount of service credit specified in clause (i) of subsection C on that
> date, and (c) the amount of service credit specified in clause (iii) of subsection C on that date.
> **Clause (ii) of subsection C does not limit the maximum purchasable amount.**"*

**3.3 Subsection C — the ceiling, and clause (ii) is the "months she needs" quantity.**

> *"An eligible member may purchase under an election **no more service credit than the least of**
> (i) four years, less any service credit previously purchased by the member under subdivision B 2 of
> § 51.1-142.2; (ii) **the number of months of creditable service the member needs in order to have
> reached his unreduced retirement eligibility date as of the filing date of the member's complete
> application**, taking account of all creditable service for which the member is entitled to credit
> as of that date, any fraction of a month in the number so determined being counted as a whole
> month; and (iii) the number of years of creditable service the member has earned as a state
> employee. … **The Board shall not accept an election for which the amount determined under clause
> (ii) of this subsection is zero.**"*

**3.4 "Earliest qualifying retirement date" — and clause (viii)'s deadline is the same date.**

> *"'Earliest qualifying retirement date' means **the first day of the month following the month in
> which the Board credits to the member all of the service credit purchased under the member's
> election.**"*

**3.5 Subdivision D 4 — eligibility is determined once, as of the filing date.**

> *"**The Board shall determine whether an applicant is an eligible member as of the filing date of
> the applicant's complete application** and shall give the applicant written notice of the
> determination no later than 30 days after the application is completed."*

And, for the retained filing date that §7 item 36 turns on:

> *"an application completed within that period **retains the filing date of the original application
> for all purposes of this section**, including the determination of eligibility required by this
> subdivision."*

**3.6 The residual as-of rule for *"unreduced retirement eligibility date"* — enacted at store
revision 49 and it reaches clause (viii) by name in the record.**

> *"Where this section does not state a date as of which the member's unreduced retirement
> eligibility date is determined, that date is, for the purposes of the preceding sentence, **the date
> on which the Board makes the certification, recertification, determination, statement, or other
> decision in which that date is applied.**"*

**3.7 Subdivision D 1 — the certification already states clause (viii)'s own input.**

> *"The Board's certification shall state … the amount of service credit to be purchased, the
> certified subsidy, the valuation date, the completion date …, **the member's unreduced retirement
> eligibility date determined with the service credit to be purchased as certified** …"*

**3.8 Subsection E — crediting, and the carve-out that lets clause (viii) operate on a hypothetical.**

> *"The Board shall credit the purchased service credit to the member only upon receipt of payment in
> full, and shall do so within 30 days after receipt of payment in full. … No service credit purchased
> under an election shall be credited before payment in full is received, except as subdivision G 4
> provides …, and, **except for the purposes of the definition of 'eligible member' in subsection A**,
> no member shall be treated as having reached his unreduced retirement eligibility date by reason of
> an election before payment in full is received."*

**3.9 The two routes to a sub-cap purchase.** Subdivision D 6, on a recertification the reserve
cannot fund: *"the member may **(i) reduce the amount of service credit to be purchased, subject to
subsection C**, (ii) pay the amount of the increase, or (iii) cancel the election under subdivision
G 5."* And § 51.1-142.2 B 4 f, on an Internal Revenue Code § 415 refusal: *"the member may **(i)
reduce the service credit to be purchased to the largest amount for which the Board may accept
payment, subject to subsection C of § 51.1-142.4**, (ii) defer payment …, or (iii) cancel the
election."*

**3.10 Subdivision G 2 — the backstop where the member does not retire in a qualifying retirement.**

> *"If the member does not retire in a qualifying retirement, the Board shall … (i) **reduce the
> service credit credited to the member under the election to the largest number of whole months of
> service credit that the member's payments would have purchased at the standard cost** …, (ii)
> **refund** to the member, and to any employer that paid on the member's behalf, … the amount by
> which the amounts paid exceed the cost … and (iii) **release the reservation**."*

**3.11 Code of Virginia sections the reading depends on**, each as cited inside the drafted text:
**§ 51.1-153** (the unreduced service-retirement conditions the *"unreduced retirement eligibility
date"* definition runs on), **§ 51.1-155 A 1, A 2 and A 3** (the unreduced allowance and the two
reductions), **§ 51.1-155.1 A and C** (involuntary separation; abolished office), **§ 51.1-124.3**
(*"creditable service"* = prior service under § 51.1-142.2 **plus** membership service for which
credit is allowable — the distinction store revision 34 turned on), **§ 51.1-142.2 B 2** (the
four-year military entitlement that is limb (a) of the maximum purchasable amount) and **B 4 b, c and
f** (the price, the certification contents, the § 415 route), and **§ 51.1-169** (the hybrid program
clause (iii) excludes).

---

## 4. Why clause (viii) adds a refusal, and exactly which one

Write **F** for the filing date of the complete application, **T** for the date the Board credits the
purchased service credit, **FOM(x)** for the first day of the month following the month containing
*x*, **M** for the maximum purchasable amount determined as of F, **C2** for the amount specified in
subsection C clause (ii), **P** for the service credit to be purchased, and **URED(S)** for the
unreduced retirement eligibility date determined with S of additional credit.

| limb | the test, in symbols |
|---|---|
| (v) | URED(0) > F |
| (vi) | URED(**M**) ≤ FOM(F) |
| (vii) | URED(**min(M, C2)**) ≤ URED(0) − 1 month |
| C | P ≤ least of C(i), **C2**, C(iii); and the Board shall not accept where C2 = 0 |
| **(viii)** | URED(**P**) ≤ FOM(**T**) |

**4.1 Clause (viii)'s deadline is the earliest qualifying retirement date, word for word.** Compare
§3.1's *"the first day of the month following the month in which that service credit is credited to
the member"* with §3.4's definition. They are the same date. So clause (viii) says: *the member would
have reached her unreduced retirement eligibility date by her earliest qualifying retirement date.*
That is precisely the condition under which the retirement window the whole section is built around —
*"no earlier than the member's earliest qualifying retirement date, and … no later than the member's
final qualifying retirement date"*, in the definition of *"qualifying retirement"* — contains a date
on which she can actually retire unreduced. **Clause (viii) is the limb that makes the qualifying-
retirement window non-empty.** Nothing else in the definition does that job on the elected amount.

**4.2 On a full-cap purchase, clause (viii) is satisfied, and the two cases work by different
mechanisms.** Let P be the largest amount subsection C allows, P = min(M, C2).

- **C2 ≥ M**, so P = M. Clause (vi) gives URED(M) ≤ FOM(F). Since T ≥ F, FOM(T) ≥ FOM(F), so
  URED(P) ≤ FOM(T). **Clause (viii) holds, and here clause (vi) is what delivers it.**
- **C2 < M**, so P = C2. By clause (ii)'s own words C2 is *"the number of months … the member needs
  in order to have reached his unreduced retirement eligibility date **as of the filing date**"*, so
  URED(C2) ≤ F < FOM(T). **Clause (viii) holds, and here subsection C clause (ii) is what delivers
  it, not clause (vi).**

**4.3 The 13-month gap between the two measuring dates is one-sided in the member's favour, so it
cannot by itself refuse anyone.** Two independent reasons, and both need stating because the Modeler
raised the gap as the risk:

1. **Later is weakly easier on both inputs.** T ≥ F, so FOM(T) ≥ FOM(F): the deadline moves later.
   And the applicant is a *"member in service"*, so creditable service accrues between F and T;
   additional creditable service cannot postpone an unreduced retirement eligibility date, so URED(P)
   measured later is weakly earlier. Both moves favour the member. **The strictest value clause (viii)
   can ever take is FOM(F) — which is exactly clause (vi)'s deadline.**
2. **Clause (viii) is in any event a forecast made at filing, not a re-test at crediting.**
   Subdivision D 4 (§3.5) determines eligibility *"as of the filing date of the applicant's complete
   application"*, and nothing in the section re-tests it. The residual as-of rule at §3.6 confirms the
   construction rather than displacing it: it supplies the date only *"where this section does not
   state a date"*, and for the eligibility determination D 4 states one. Subdivision D 1 (§3.7) then
   compels the Board to state *"the member's unreduced retirement eligibility date determined with
   the service credit to be purchased as certified"* in the certification, which is clause (viii)'s
   own quantity, determined at certification. Store revision 32's record reached the same conclusion:
   *"clause (viii) cannot operate at crediting, because D 4 determines eligibility as of the filing
   date and nothing re-tests it, so clause (viii) is a forecast made at filing."*

**4.4 The class clause (viii) refuses, and why the record's stated reason for calling it surplusage
runs backwards.** Store revision 32's record says clause (viii) *"is subsumed by clause (vi) in every
case, which tests a quantity at least as large against an earlier deadline."* The premise is right —
M ≥ P, and FOM(F) ≤ FOM(T) — but **a larger quantity makes a test easier, not harder.** From
URED(M) ≤ FOM(F) and P ≤ M it follows that URED(P) ≥ URED(M), which says nothing about whether
URED(P) ≤ FOM(T). Clause (vi) dominates clause (viii) only where **P = M**, which is case one of §4.2;
in case two the work is done by clause (ii), and where **P < min(M, C2)** nothing does it at all.

**Nothing in the drafted text requires the member to elect the maximum.** Subsection C is a ceiling —
*"may purchase … no more service credit than the least of"* — and two provisions expressly contemplate
election of less: subdivision D 6 clause (i) and § 51.1-142.2 B 4 f clause (i), both quoted at §3.9.
So the class is real on the face of the text:

> **An applicant who applies to purchase P months where P is less than the months she needs to reach
> her unreduced retirement eligibility date by the first day of the month after her credit is posted,
> while her maximum purchasable amount would have reached it.** She satisfies (v) — she has not
> reached the date. She satisfies (vi) — her *maximum* amount reaches it within a month of filing.
> She satisfies (vii) — the *capped* amount advances the date by at least a month. **Clause (viii) is
> the only limb that looks at what she actually asked to buy, and it refuses her.**

**4.5 What clause (viii) is therefore worth, in the Commonwealth's terms.** Without it, that applicant
is an *"eligible member"* whose qualifying-retirement window contains no date on which she can retire
unreduced, so she can never settle under subdivision G 1. She would occupy a reserved certified
subsidy against subdivision D 2's $3,000,000 aggregate and $170,000 per-election ceiling until the
reservation is released, and then fall into subdivision G 2 (§3.10) — credit reduced to what her
payments bought at standard cost, the excess refunded, the reservation released. **So clause (viii)
protects reservation headroom and queue position; it does not protect the settling aggregate, because
a member who can never make a qualifying retirement was never in the settling aggregate.** That is
why its presence or absence cannot move the priced cost per participant, only cap utilisation — and
cap utilisation is the Modeler's to measure, not mine.

**4.6 The one route clause (viii) cannot reach, and it is already carded.** Because eligibility is
determined once as of the filing date (§3.5), a **post-acceptance** reduction under subdivision D 6
clause (i) or § 51.1-142.2 B 4 f clause (i) cannot un-eligible the member — there is no second
eligibility test for clause (viii) to fail. The member is left accepted, with a purchase too small to
produce a qualifying retirement, and the section does not say what she is credited with. **That is
§7 item 70** (*"An accepted election with nothing to buy has no defined downstream operation … Two
post-acceptance routes survive"*, store revision 41) and **§7 item 126** (*"it decides what a partial
payer is credited with, which is a money question"*, store revision 60). Both are open, both are
drafted, neither is enacted. **I am flagging the link, not asking for a drafting change: clause (viii)
closes the pre-acceptance route to the same defect and the two items close the post-acceptance
routes.**

---

## 5. Why the class is empty on the drafted cohort as modelled

**5.1 The model's admission screen is clause (vi), and its purchase rule is clause (ii).**
`engine/v2_cohort.py` `classify()` (lines 215–252, in
`moo183-cost-per-participant/engine/`) takes `y = min(MAXY, avail)` — the member's whole available
entitlement, which is the maximum-purchasable-amount analogue — tests
`t_with = years_to_eligibility(plan, age, service, y)`, and on the authorised `scope == "immediate"`
basis **returns `None` unless `t_with` is zero**: `if sc == "immediate" and t_with > 1e-9: return
(None, 0.0, 0.0)`. That is clause (vi) as drafted. It then bisects for *"the smallest purchase
achieving the same eligibility date"* and returns that amount, floored at one month. `PATHWAY_A_SCOPE`
is `"immediate"` in `engine/inputs.py` §18, which is the reading the package reports as the headline.

**5.2 Therefore every modelled member satisfies clause (viii) by construction.** Her purchase is the
minimum amount that makes her unreduced-eligible **at once** — i.e. P is the clause (ii) quantity, the
case-two branch of §4.2 — so URED(P) ≤ F < FOM(T) whatever T turns out to be. **The under-buyer of
§4.4 is not representable in the engine: the model has no dial that elects less than the amount
achieving the modelled eligibility date.** Clause (viii) refuses 0 of the 18.3965.

**5.3 One model-side check that is the Modeler's, not mine, and it is the only condition on the
answer.** `engine/s8.py` `s8_price()` applies a **service-matching cap** (`S8_SERVICE_MATCHING_CAP =
True`, sourced in `engine/inputs.py` §15.3 to 71 Pa.C.S. § 5505(b) and the MOO-3 Scenario Selection
Memo, **not** to this bill) that clips `yrs = min(yrs, credited state service)` **after**
classification, while `v2_scenarios.build_elections()` defaults `service_match_cap=False` in the
cohort build. **If a run clips the purchase below the amount `classify()` certified, the clipped
members are exactly the §4.4 class** — and I should say plainly that in the live text they are already
refused one limb earlier, because the state-service cap sits inside the **maximum purchasable
amount** as limb (c) (§3.2), so clause **(vi)** tests the clipped quantity, not the unclipped one.
Two consequences, both favourable: clause (viii) still adds no refusal, and the exposure if a run is
inconsistent here is in the model, not in the text. **Store revision 32's Mi-10 reports the limb
measured empty in any event** — *"`moo78_screen.mpa()` carries the clause (iii) limb and
`out_moo78_c_iii_refusal.csv` measures it refusing **0.0000** members at every take-up level, with the
B 2 entitlement limb binding for the whole cohort"* — so on the team's own measurement the channel is
closed. **Confirm that the v6 run's screen and its priced quantity use the same capped amount, and
clause (viii) is finished.**

**5.4 What I am not saying.** I am not saying the under-buyer is behaviourally impossible — I have no
source on election behaviour and none exists. I am saying she is **not in the model's cohort** and
**not in the settling aggregate** (§4.5). If the Policy Director wants her priced, that is a new
scenario for the Modeler, and its direction on the count is downward and on reservation occupancy
upward.

---

## 6. Store revisions 22 to 61 — what actually reached the cohort or the certified amount

**Method, and its limit.** I cannot diff store revisions: the store holds the live body only. What I
can do, and did, is read the §0 revision narratives for every revision from 22 to 64 across the live
document and the three retained-record documents, and take each revision's own recorded statement of
what it amended and what it moved. **Where a revision's record states a direction of effect, I quote
it rather than re-derive it.** Thirteen revisions in the window amend only subdivisions G 4, D 1, D 3,
D 6, M 2, M 3, J 1, subsection E or the death branch, and each records *"no figure moves"*; they are
not tabled. The seven that reach an admission limb, subsection C, the two definitions, or the
certified amount are these.

| store rev | what it amended | figure effect, as its own record states it |
|---|---|---|
| **22** | drafted §7 item 22 **option (c)** — clause (ii) measured *"as of the filing date"*; introduced the *"membership service"* base in clause (ii) | **option (c) IS the v6 basis.** But it *"converted the cure window into a quantity lever"*: against subdivision D 4's retained filing date, at the D 4 maximum the **mean certified quantity rises 19.89 → 22.74 months (+14.3%)**, zero-bar refusals go to **0.00** and $170,000-ceiling refusals rise **1.23 → 1.46**. Option (c) was priced on `moo78_screen.basis_cells(R18, measure_years=0.0)` — complete application in hand. **§7 item 36, OPEN** |
| **32** | clause (ii) **rounding** rule (*"any fraction of a month in the number so determined being counted as a whole month"*); clause (vii) month convention; filing date added to D 1's certification list | *"rounding up raises the mean certified quantity by up to one month per member against the exact-fraction basis Fiscal priced"* — **but the cohort carries no fractional needs at all, so the rounding contribution is zero**, and cap utilisation moves **−0.08 points** (§7 item 36's note to Fiscal, as corrected in store revision 34) |
| **34** | clause (ii) **base**: *"the membership service the member has earned"* → *"all creditable service for which the member is entitled to credit as of that date"*; clause (vii)'s month convention moved into its own sentence and made symmetric | direction of effect **downward on cost and on quantity**, *"so the repair cannot threaten the $3,000,000, the $170,000 ceiling or the participant count"*; and **not representable in the engine**, *"the engine carrying one service variable per member so that the split-base case is not representable"* (store revision 41) |
| **38** | subsection C's **zero bar and its refusal notice deleted** (§7 item 35 option (b)) | reversed at 44 — see below |
| **41** | subsection C's new third sentence (the **substituted no-amount determination** for the class where clause (ii)'s solution set is empty); clause (v) gains clause (ii)'s entitlement base verbatim | *"It enacts the reading the authorised basis is measured on, which is why no figure moves"* — `need_months_at` returns `INF`, not 0, *"so **18.3965 admitted** … already stand on the reading now in the text; the other reading is **18.3706**"*. Class measured at **0.0826 expected elections, 0.0259 admitted, $145,396–$166,226 of certified subsidy each**. Clause (v) edit: *"on the authorised basis it moves nothing"* (direction-of-effect claim **corrected at store revision 46** to "not determinate on the face of the statute"; text question is §7 item 82) |
| **44** | subsection C's **zero bar and its refusal notice restored verbatim** | *"No figure moves, and this is now measured rather than argued."* **Net of 38 and 44 the bar is present — which is the state the v6 run assumes** |
| **48** | **clause (vii) edit 3** — supplies the missing second operand (*"or, where no amount is specified in clause (ii) of subsection C, the member's maximum purchasable amount determined as of that date"*) for the no-amount class, whose clause (vii) was otherwise unevaluable | challenged by pass 16's M-5 and settled at [MOO-144](/MOO/issues/MOO-144): the **0.0259 admitted is inside 18.3965, not additional to it** (18.3964963814311 − 0.0258958319082 = 18.3706005495229), and **edit 3 moves the certified amount on 0 of 5,552 cells** — *"so neither the admitted count nor the per-member average purchase moves"* |
| **49** | **M-3** — gives the residual as-of trigger a referent *"in the four places this section applies the definition without stating an as-of date (**clause (viii)**, the D 1 certification item, subsection E, G 3)"* | *"The five edits, all repairs to words the answers put in, and **none of them changes which member passes either definitional test**"* |

**6.1 And two that reach reservation occupancy and queue order but not the cohort**, which is the
distinction the question asks about: **store revision 50** frees subdivision D 1's day-for-day
extension from the 12-month ceiling, capped at 12 months in the aggregate — *"Direction of effect on
reservation occupancy: **longer**"*; and **store revision 59** supplies the two missing clocks in
subdivisions D 1 and D 3 so that *"on the worst case the existing 90-day applicant notice now fires at
about day 105 instead of never"*. Both are exactly the retention-and-ordering class
[MOO-163](/MOO/issues/MOO-163) priced as a bounded delta. Neither touches an admission limb or the
certified-subsidy formula.

**6.2 Two revisions say it in terms, and they are the last word in the window.** Store revision 56:
*"No admission test, no clause (v) to (viii) determination and no subsection C clause (ii) cap
changes."* Store revision 60: *"**No admission test moves:** nothing in these thirteen substitutions
touches 'eligible member', the subsection C clause (ii) cap, or the clauses (v) to (viii)
determinations."* I checked store revision 60's one apparent exception and it holds: item 119 did
amend the definition of *"unreduced retirement eligibility date"*, but the sentence it added is
self-limiting on its face — *"where this sentence is applied **otherwise than in the determination of
the member's unreduced retirement eligibility date**"* — so it cannot move that date, and it *"can
only ever admit a retirement route the section had disabled for a member already inside the
program."* Store revisions 58 and 61, both wholly within subdivisions G 4, D 1 and M 2, each record
*"no figure moves"*.

**6.3 The three issues the question names — confirmed, and the answer is cleaner than "it only
reaches ordering".** [MOO-141](/MOO/issues/MOO-141)'s patch, as cut at
[MOO-162](/MOO/issues/MOO-162) revision 5 and [MOO-176](/MOO/issues/MOO-176) revision 6, **is not in
store revisions 22–61, or in any store revision.** MOO-176's disposition says so in terms: *"Revision
6 is accepted as cut. It is the current cut of the MOO-141 patch. **It stays unapplied.**"* MOO-141's
gate-3 pass confirms the patch is still only a patch at store revision 64 — *"MOO-141 is blocked on
MOO-164 and MOO-190 and nothing here unblocks either"* — and the companion MOO-164 kit records
*"Nothing in this kit has been applied to the store."* **So nothing of that work is in the text the
v6 run was read against, and nothing of it can have moved the cohort or the per-member subsidy.**

And on its own terms, as drafted, it could not: all three edits sit in **subdivision M 2**, which is
the reconsideration-and-review subdivision — what counts as a determination, when a request is deemed
acted upon, and how long a retention runs. **Subdivision M 2 is not cited in the definition of
*"eligible member"*, in *"maximum purchasable amount"*, in *"unreduced retirement eligibility date"*,
in subsection C, or in the definition of *"certified subsidy"*.** It changes **when** an applicant's
rights are determined and reviewed, not **whether** she is an eligible member or **what** her
certified subsidy is. That is the confirmation the Modeler asked for, and it is a confirmation from
the provisions rather than from the headings.

---

## 7. Corrections to the record that travel with this answer

1. **Store revision 32, §0.x c item 2 (pass 9's M-7), in
   [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history).**
   *"[Clause (viii)] is subsumed by clause (vi) in every case, which tests a quantity at least as
   large against an earlier deadline."* **The conclusion is right for the full-cap purchaser and the
   stated reason is not.** A larger tested quantity makes clause (vi) easier, so clause (vi) cannot
   dominate clause (viii) by being tested on more credit; where clause (ii) binds, the work is done by
   clause (ii)'s own definition (§4.2 case two), and where the member elects **less** than the
   subsection C ceiling, nothing does it (§4.4). The practical consequence is nil on this cohort and
   the drafting consequence is that **clause (viii) should not be deleted as surplusage.** §4.5 and
   §4.6 state what it is for.
2. **Store revision 34, §0.x b.** *"[C]lauses (vi), (vii) and (viii) all ask whether **the maximum
   purchasable amount** gets her *to* the date."* Clause (viii) does not: it asks about *"the service
   credit **to be purchased**"* (§3.1). The point store revision 34 was making — that nothing screened
   the over-credit case — is unaffected, because clause (viii) has no upper limb either.

Neither correction moves a word of the bill and neither is a drafting request. Both belong in the
record so the next counsel pass does not reach for the deletion.

---

## 8. Open gaps — what I could not confirm, and where I looked

1. **I did not re-open the Code of Virginia or LIS on the web this heartbeat.** The § 51.1-153,
   § 51.1-155, § 51.1-155.1, § 51.1-124.3 and § 51.1-142.2 references at §3.11 are as cited and
   quoted **inside** `bill-text-s8` and its drafting record, not as re-verified against the published
   Code today. Nothing in this answer turns on the wording of a current Code section — it turns on the
   drafted § 51.1-142.4 — but the distinction is worth stating. **Where I searched:** the live
   `bill-text-s8` body at store revision 64 and its four retained-record documents on
   [MOO-42](/MOO/issues/MOO-42), plus `bill-text-s8-item-list`.
2. **No legislative history and no oversight findings are reported, and that is not an omission.**
   The question is a construction question on an unintroduced internal draft. There is no bill number,
   no patron and no session; there is no LIS record of § 51.1-142.4 because the section does not
   exist. **No source found** for any JLARC, Virginia Code Commission or Joint Commission study of the
   interaction of a service-purchase eligibility screen with a crediting-date deadline, and I did not
   search for one this heartbeat because no claim here depends on it. If the Policy Director wants the
   JLARC and Code Commission record on VRS service-purchase pricing generally, that is a separate ask
   and I will take it.
3. **I cannot verify the v6 engine's internals.** `moo32_v6_engine.py`,
   `out_moo32_v6_basis.json` and `out_moo78_c_iii_refusal.csv` live in
   `AgentCreated/_review-MOO-32-charts-v6/`, which is not in this workspace — I looked. Every v6
   figure in §5 and §6 is therefore **quoted from the record that reports it**, not re-run. The one
   check at §5.3 is a check on that engine and is the Modeler's.
4. **§7 item 36 is open and is the live caveat.** I have not measured it and will not. Its direction
   is **upward** on the certified quantity and it is already drafted three ways, with the drafter's
   recommendation at option (b) and a conforming condition recorded at store revision 34. **It needs a
   Policy Director answer before the quantity basis can be called current**, and the measurement that
   follows is two runs or a decomposition, because the rounding and the measurement-date move *"have
   opposite signs on the subsidy"*.
5. **The behavioural question at §5.4 has no anchor.** Whether any real applicant elects less than the
   subsection C ceiling is unsourced in both directions.
