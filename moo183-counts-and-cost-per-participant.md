# MOO-183 — the five counts, the recommended row's aggregate, and the $64,678 identity

**Fiscal & Impact Modeler · 12 October 2026 · pre-decisional and internal.**
**No figure here is a VRS actuarial result. Nothing is reliable beyond two significant figures.**
Model: `moo183-cost-per-participant/moo183_cpp.py`, register `moo183_inputs.py`, transcript
`out_moo183_run.txt`, CSVs `out_moo183_rows.csv` and `out_moo183_recommended_ladder.csv`.

---

## 0. The costing question, and the horizon

> For each of the five scoreboard rows that print a cost and carry no authorised participant
> count, and for the recommended row, how many member elections does the design produce over
> the pilot, and what is the net cost to the trust per electing member — on a basis that is the
> same basis as the cost figure printed beside it?

**Unit of analysis:** one member election. **Horizon:** the four-year pilot, present value at
the 6/30/2025 valuation date. **Denominator for every per-participant figure below:** expected
member elections over the whole 48-month pilot — *not* per year.

---

## 1. Headline — and the sentence the Editor asked for

**All five counts can be produced, and they did not have to be estimated. They were already
inside the runs that produced the five cost figures the package prints; nobody had divided.**
The locks in §7 re-run the published engine and reproduce all seven published scoreboard costs
to the cent, and the method reproduces **six of the seven** per-participant figures §3b already
prints **to the dollar**.

> **One sentence for the Editor.** On the basis the scoreboard's cost figures are printed on,
> S3 reaches about **59 members at $57,000 each**, S5 about **23 at $55,000**, S6 about **91 at
> $57,000**, S8 at 4.00% about **85 at $66,000** and S8 at 5.00% about **73 at $63,000** — and
> the recommended design, on the board's authorised 12-month rung, costs **$1.4 million (range
> $0.71M–$2.4M) over 18.9 members, $75,000 each**, which falls to **$1.3 million over 18.4
> members, $72,000 each** once the bill's own option (c) and no-advance bar are in the cohort.

**Read the first paragraph of §2 before using any of the five.** There is a basis mismatch in
the question as put, it is not mine to resolve, and it moves the five per-participant figures by
13–15%.

---

## 2. Deliverable 1 — the five rows

### The basis mismatch, stated first because it controls the answer

The issue asks for these five **"on the authorised 12-month retirement rung."** They cannot be
delivered there and left beside their printed cost figures, because **no cost figure in the §3
scoreboard or the §3b coverage table is on the 12-month rung.** Every one of them — including
S1's $5,123,905 and the $64,678 anchor — is on the repaired engine's **6-month** retirement
deadline (`inputs.RETIREMENT_DEADLINE_MONTHS = 6`). The 12-month rung was priced for the
**recommended design only**, on a different cohort, by MOO-48 and MOO-85.

So I have produced the five **both ways** and I will not mix them in a row:

- **Table A** — on the basis the printed cost sits on. Numerator and denominator come out of one
  row of one run. **This is the set that satisfies §3b Decision 3 for those five cells**, because
  Decision 3 requires the count and the per-participant figure to sit *beside that cost figure*.
- **Table B** — the same five re-run with the retirement dial moved from 6 to 12 months and
  nothing else changed. **This set is only usable if the whole §3b table moves to the 12-month
  rung at once**, which means re-cutting all seven authorised rows and all twelve printed costs.
  That is a Policy Director decision, not a modelling result.

### Table A — on the basis each printed cost sits on *(recommended for v2.0)*

Repaired (v2) basis: Pathways A+B, 6-month retirement deadline, statutory interest as each row
defines it, four-year pilot, PV at 6/30/2025. Numerator = **net trust cost**: increase in
retirement-system liability attributable to the elections, **less member payments**, and
**excluding** the $375,000 one-time nongeneral-fund implementation allowance.

| Row | cost printed | participants, central | range (low–high take-up) | **cost per participant** | at 2 s.f. |
|---|---|---|---|---|---|
| **S3** sliding scale | $3.38M | **59.2** | 27.5 – 105.7 | **$57,123** | **$57,000** |
| **S5** reopen/extend the window | $1.26M | **22.8** | 10.1 – 45.6 | **$55,055** | **$55,000** |
| **S6** add Hybrid members | $5.15M | **90.5** | 42.3 – 160.6 | **$56,900** | **$57,000** |
| **S8 at 4.00%** *(internal)* | $5.60M | **84.9** | 39.7 – 150.5 | **$65,984** | **$66,000** |
| **S8 at 5.00%** *(internal)* | $4.56M | **72.7** | 34.0 – 128.8 | **$62,808** | **$63,000** |
| *S1 as drafted, for calibration* | $5.12M | 79.2 | 37.1 – 140.5 | $64,678 | $65,000 |
| *S8 at 6.00%, for calibration* | $3.65M | 62.2 | 29.2 – 110.3 | $58,698 | $59,000 |

The per-participant figure's own range across the take-up cases is **about ±1%** (S3
$56,822–$57,464; S5 exactly flat; S6 $56,355–$57,522; S8-i4 $65,375–$66,676; S8-i5
$62,217–$63,479). Take-up scales the cohort and the cost together, so it very nearly cancels in
the ratio. **That is the whole case for Decision 3's column: the ratio is robust exactly where
the aggregate is not** — the same structure as the ratio rule in §3.

### Table B — the same five on the authorised 12-month rung

One driver moved, nothing else. Participant counts are **identical** to Table A (see the
invariance check below), so only the cost and the ratio move.

| Row | trust cost @ 6 mo | **trust cost @ 12 mo** | move | **$/participant @ 12 mo** | mean acceleration |
|---|---|---|---|---|---|
| **S3** | $3,380,695 | **$2,858,888** | −15.4% | **$48,306** | 34.1 → 28.2 mo |
| **S5** | $1,255,447 | **$1,079,283** | −14.0% | **$47,330** | 30.9 → 25.0 mo |
| **S6** | $5,149,488 | **$4,463,297** | −13.3% | **$49,318** | 32.2 → 26.3 mo |
| **S8 at 4.00%** | $5,599,030 | **$4,850,885** | −13.4% | **$57,167** | 34.1 → 28.2 mo |
| **S8 at 5.00%** | $4,563,715 | **$3,923,069** | −14.0% | **$53,991** | 34.1 → 28.2 mo |
| *S1 as drafted* | $5,123,905 | *$4,425,424* | −13.6% | *$55,861* | 34.1 → 28.2 mo |
| *S8 at 6.00%* | $3,652,752 | *$3,104,084* | −15.0% | *$49,881* | 34.1 → 28.2 mo |

**The count is rung-invariant, measured not assumed.** Largest difference in any participant
count between the two rungs, over 7 designs × 3 take-up cases: **0.0000000000**. The retirement
deadline moves what the trust pays and not who elects — the same finding MOO-48 §3 and MOO-85 §1
report on the drafted cohort, now confirmed on the repaired cohort. **So the five counts in
Table A are also the five counts on the 12-month rung**; it is only the cost and the ratio that
need a basis label.

### Every count above is modeled demand

**These are modeled demand, not actual cap utilization.** They are elasticity-adjusted take-up
extrapolations on a cell grid of expected weights, not simulated people and not observed
elections. **No participant count in this package has an external anchor**: no published count
of purchases actually made under § 51.1-142.2 per year exists, and getting one is a data request
to VRS. S3 and S8 carry one further modelled step the others do not — a price-elasticity
adjustment to take-up (−0.6) — so their counts are one inference further from the data than
S1's, S5's or S6's.

### Two rankings you cannot draw from Table A

- **S3 against S6** is $57,123 against $56,900 — **0.4% apart**, well inside the ±1% take-up
  spread on either figure. At two significant figures both print $57,000. **They are
  indistinguishable on this measure and the package must not rank them on it.**
- **S5's apparent cheapness per head** is an artefact of the numerator convention. Add the
  $375,000 implementation allowance, which every design incurs once, and S5 is the **dearest**
  of the five per participant ($71,500 against S6's $61,044), because it spreads a fixed cost
  over the smallest cohort. Pick one numerator and say which (§6).

---

## 3. Deliverable 2 — the recommended row on the authorised rung

### The answer

**On the authorised 12-month rung the recommended design's aggregate is $1,411,988 in present
value, range $705,994 to $2,353,313, and the cost per participant against 18.9059 participants
is $74,685.** At reportable precision: **$1.4 million, range $0.71M to $2.4M, about $75,000 per
member.** Add the one-time $375,000 nongeneral-fund implementation allowance and the headline
state cost is **$1,786,988**, i.e. **$1.8 million**.

The per-participant figure is **invariant to take-up** on this ladder — $74,685 at low, central
and high alike — because take-up scales the aggregate and the count by the same factor. Its real
range comes from the retirement-date assumption, not from take-up (§5).

### The two circulating aggregates: same quantity, two different retirement dates — and one is mislabelled

| figure | what it actually is |
|---|---|
| **$1,661,819**, range $830,909–$2,769,698 | the ladder at **rung 0** — credit posts and retirement takes effect in the same month |
| $1,641,824 | the ladder at **rung 1** — *the drafted text*: first of the month after the credit posts |
| **$1,411,988**, range $705,994–$2,353,313 | the ladder at **rung 12** — the authorised rung |

**The figure the ten sponsor documents print is rung 0, not rung 1.** MOO-48 §2 recorded this
correction when it verified the run; the ten documents carried the rung-0 figure with a rung-1
label. Rung 1 is $1,641,824, $19,995 (1.2%) below it. **So the issue's own description of the
circulating figure as "basis: rung 1" is itself the labelling error, and it should be corrected
wherever v2.0 describes the superseded figure.**

**Neither aggregate is wrong, and they are not two estimates of one quantity.** Both are net
trust cost in present value, on the same cohort, at the same member price, with the same 18.9059
participants. They are **two rungs of one measured ladder**. The whole of the difference is
retirement-date acceleration:

> $1,661,819 − $1,411,988 = **$249,831**, over **12.0 months** of acceleration removed (56.9 →
> 44.9 months) = **$20,819 per month**, which steps monotonically across the ladder. The member
> price does not move at any rung.

**So: the rung-0 figure is superseded as the publication basis, and it is not superseded as a
measurement.** It is the right number for the question "what if members retire as soon as the
credit posts", which is also the dearest honest answer (§5). **Nothing is averaged and nothing
is interpolated.** The "15% apart" in the issue and the "17.7% apart" in my transcript are the
same gap on two denominators — 15.0% of the rung-0 figure, 17.7% of the rung-12 figure.
Denominator discipline: say which.

### Does the result sit on the current bill text? No — and this is the most important thing in this document

**Both circulating figures, and the 18.9 count, are on the MOO-48 engine cohort, which predates
§7 item 22.** They were run on the narrow clause (vi) reading of `bill-text-s8` store revision 21
**without** option (c) and **without** the no-advance bar. MOO-87 has since put both into
§ 51.1-142.4, and I have verified clause (vii)'s no-advance bar and subsection C clause (ii)'s
filing-date measurement are in the live text at document revision 76 / store revision 61.

One run exists on that basis — the MOO-32 v6 basis run, a review copy, never published. On it:

| | low | **central** | high |
|---|---|---|---|
| participants | 9.1982 | **18.3965** | 30.6608 |
| net trust cost, rung 12, **PV** | $660,556 | **$1,321,112** | $2,201,853 |
| **cost per participant** | $71,813 | **$71,813** | $71,813 |
| plus implementation, FY2029, NGF | $375,000 | $375,000 | $375,000 |
| **total cost to the Commonwealth, PV** | $1,035,556 | **$1,696,112** | $2,576,853 |

**Against the MOO-48 cohort at the same rung: the count moves −2.7% (18.9059 → 18.3965), the
aggregate −6.4% ($1,411,988 → $1,321,112) and the cost per participant −3.8% ($74,685 →
$71,813).** At two significant figures the count is unchanged — 18, range 9 to 31 — and the
aggregate moves from $1.4M to $1.3M, i.e. **the second significant figure moves.**

That run also **corrects the count MOO-71 authorised by arithmetic**: 17.93 is a double
subtraction (the 1.0148 no-advance band was taken off 18.9483, which had already removed 0.4631
of that band under the zero-month bar; 18.9483 − 1.0148 + 0.4631 = 18.3965). The correction runs
in the member-favourable direction and does not move the authorised two-significant-figure
headline.

**And one thing the window does not do.** On the current basis the Commonwealth **reserves**
$1,954,680 nominal while the trust **pays** $1,668,678 nominal; the $286,001 difference is the
12-month window's entire effect. D 2 meters the reservation, certified on the anticipated
earliest qualifying retirement date, which the window does not move. **Any artifact that implies
the 12-month rung eases the $3,000,000 is wrong.** Cap utilisation on that basis is 39% / 78% /
130% — it binds at high take-up.

### What I am not telling you, and who owns it

I verified the **values of the dials** against the live text (interest six percent; $3,000,000;
$170,000; E's 12-month completion window; earliest qualifying retirement date = rung 1; final
qualifying retirement date = rung 13 with extensions). I did **not** re-read the eligibility
clauses and re-price on my own reading. Two items are for
[@Statutory Researcher](agent://705d4b07-92cb-4a50-80f8-fbfab9cccb27), and they are the reason
I will not call the figures above current:

1. **Clause (viii) of "eligible member"** — *"would reach his unreduced retirement eligibility
   date, determined with the service credit to be purchased, on or before the first day of the
   month following the month in which that service credit is credited"* — is in the live text and
   is **in no committed run**. It is an additional screen, so its direction is one-sided: the
   count can only come out at or below 18.3965. **18.4 is therefore an upper bound on the current
   text, not a measurement of it.**
2. Whether anything in store revisions 22–61 (the M 2 retention and notice work on
   [MOO-141](/MOO/issues/MOO-141), [MOO-162](/MOO/issues/MOO-162),
   [MOO-176](/MOO/issues/MOO-176)) reaches the cohort or the per-member subsidy. On its face it
   reaches queue order and retention, which [MOO-163](/MOO/issues/MOO-163) priced separately as a
   bounded delta, not the cohort — but that is a reading, and the reading is not mine.

---

## 4. Deliverable 3 — the $64,678 identity: **YES, the same quantity**

**They are the same number, from the same run, out of the same field, and the identity is
demonstrated in code rather than argued.**

- §3b's per-participant column is `agg["trust"] / agg["n"]` on repaired S1 at central take-up.
- The package's three printed sites trace to repaired §7's break-even line, which prints
  `a_base["trust"] / a_base["n"]` where `a_base = X.run("S1", "central")` — *the same
  expression on the same object*.
- Re-run today: $5,123,905.434065 / 79.22147132 = **$64,678.241247**, identical to the tenth of
  a cent, rounding to the printed $64,678.

**So the package already carries S1's per-participant anchor and the Decision 3 column can cite
it — with two corrections that have to travel with it.**

**Correction 1 — the label is wrong, and it is wrong in the direction that matters.** All three
sites call it *"pension cost of the purchased service per participant."* It is not that. It is
the **net cost to the trust per participating member of the whole election**, and only 28% of it
is purchased service:

| per participating member, repaired S1 | |
|---|---|
| gross liability increase | $76,751 |
| — of which service-credit content | **$21,860 (28%)** |
| — of which earlier-commencement content | **$54,891 (72%)** |
| less member payment | −$12,073 |
| **= net cost to the trust** | **$64,678** |

A reader who takes the label at face value concludes the Commonwealth is paying $64,678 for
four years of service credit. It is paying $21,860 for the credit and $54,891 for the member
retiring earlier, less what the member pays. The label should read: **"net cost to the trust per
participating member — repaired S1, Pathways A+B at approximate normal cost, four-year pilot, PV
at 6/30/2025, net of member payments, excluding implementation."**

**Correction 2 — it is S1's anchor, not the bill's.** S1 is the drafted-at-ANC design the package
does *not* recommend. The bill as drafted is **$74,685 per participant** on the authorised rung
(or $71,813 on the current statutory basis), and the recommended S8 cell is **$58,698** on the
scoreboard basis. $64,678 sits between them. If it is used as "the" per-participant anchor
without the scenario name attached, every comparison built on it is wrong by 9% to 16%.

**And one consequence for §3b as a whole.** $64,678 is a **6-month-deadline** figure. On the
board's controlling 12-month rung the same quantity is **$55,861**. The anchor is not on the
board's basis, and it is the fourth place in this document where that mismatch surfaces.

---

## 5. Sensitivity — the three that control these answers

**Flagged in the first paragraph as my standard requires: no 10% move in any single input swings
any answer here by more than 25%.** The items below are choices of basis and bounds, which is a
bigger source of movement than any 10% move, and that is why they are reported as bases and not
as tornado bars.

1. **Which retirement rung the table prints — the dominant item for Deliverable 1.** 6 months
   against 12 months moves all five costs and all five per-participant figures by **13–15%**,
   one-directionally. It changes **no** count and **no** ranking among the five.
2. **Who retires when inside the window — the dominant item for Deliverable 2, and it is
   unsourced.** The rung-12 figure prices *every* member retiring on the last permissible day.
   It is therefore the **cheap end** of the window, not a central estimate of it. Measured
   bounds, from MOO-85 §4: uniform across the permissible dates **+7.5%** ($1,517,644),
   front-loaded 2:1 **+8.6%**, all at the earliest date **+16.3%** ($1,641,824). **Every
   deviation is dearer — the exposure is one-sided**, and there is no published distribution of
   chosen retirement dates inside a VRS window anywhere. Analyst judgment, no anchor.
3. **Which cohort — item 22 (c) plus the no-advance bar.** −2.7% on the count, −6.4% on the
   aggregate, −3.8% per participant, and the count is an **upper bound** until clause (viii) is
   measured. Behind all of it sits the clause (vi) reading, which MOO-71 records as a 6.9×
   exposure on the count and the v6 register as $1.3M–$11.0M on the aggregate. **That is a
   drafting question, not modelling uncertainty, and it dwarfs everything in this document.**

**Take-up is the dominant driver of every aggregate (factor ~3.3) and very nearly cancels in
every ratio (±1%).** Any artifact that ranks designs on aggregate is reporting a take-up
assumption; one that ranks them per participant is reporting something sturdier. That is the
substantive reason Decision 3's column is worth the trouble.

---

## 6. The convention question — my view, since you asked

**Print the per-participant column to two significant figures, like every other figure in the
package, and add a no-ranking rule.**

Three reasons:

1. **The precision is not in the inputs.** Take-up alone moves each figure ±1% (±$600 on
   $58,698). The rung choice moves it 13–15%. The cohort basis moves it 3.8%. A figure printed to
   the dollar asserts a precision that four separate assumptions in the register do not support,
   and §3b printing to the dollar beside a scoreboard printing to two significant figures is the
   kind of inconsistency a hostile reader uses to argue the model is not understood.
2. **The cases where rounding "destroys" a comparison are cases where the comparison was never
   there.** $47,094 against $46,857 is a **0.5%** gap between two modeled-demand figures whose
   own take-up ranges are twice that wide. Rounding both to $47,000 does not lose information —
   it stops the table asserting a difference the model cannot see. The same is true of my S3
   ($57,123) against S6 ($56,900). The package already uses this test on aggregates, in §3a's
   sign-stability rule; the per-participant column should use it too.
3. **Audit precision belongs in the model, not in the memo.** Full precision is in
   `out_moo183_rows.csv` and in §3b's own source CSVs, where a reviewer can check the division.

**So, concretely:** per-participant to the nearest $1,000 (`$57,000`), aggregates to two
significant figures as now (`$3.38M`), counts to one decimal (`59.2`) with the range beside
them, **and a stated rule that two designs whose per-participant figures round to the same
$1,000 are not ranked against each other on that measure.** On the current §3b table that rule
binds on S0/S4 ($47,000 both) and, once the five rows land, on S3/S6 ($57,000 both).

---

## 7. Verification, and the external check

**Construction locks — all pass, in `out_moo183_run.txt` §0.** The engine reproduces
`out_v2_scenarios.csv` for all seven designs at all three take-up levels, on both the count and
the cost, to within 51 cents. The five counts are therefore not a new estimate; they are the
denominators that were always inside the published runs.

**Internal check on the method itself — it reproduces the authorised column.** Dividing published
trust cost by published participants reproduces **six of the seven** figures §3b already prints,
to the dollar: S0 $46,857, S4 $47,094, S8-6.75 $54,842, S8-6.00 $58,698, S1 $64,678, S2 $88,295.
(The seventh, S9's $71,580, is MOO-70's reprice and is not in this engine's scenario CSV.) The
same division on the MOO-48 engine reproduces that document's published $86,842 at rung 1. **So
the five new rows are produced by exactly the convention the seven authorised rows were produced
by, on both engines.**

**Independent reproduction of the ladder.** I re-ran `moo48_main.py` from a clean start today:
`out_moo48_deadline_ladder.csv` came back **byte-identical** to the published file, including
rung 0 at $1,661,818.70, rung 1 at $1,641,823.79 and rung 12 at $1,411,988.09, with participants
18.905903746402497 at every rung.

**External sanity check — it disagrees, and the disagreement is the finding.** The only external
anchor this programme has is SB 419 (2026) and VRS's own fiscal impact statement for it, which
scores a year of granted service at **$10,664**. On this engine family the bill's gross liability
per purchased year is **$86,660 at rung 1 and $77,108 at rung 12 — 8.1× and 7.2×**; the
like-for-like service-credit row is **$26,219 → $24,982, 2.5× → 2.3×** (MOO-85 §5; the v6 basis
run gets $75,260 per purchased year, 7.1×, on the option-(c) cohort).
**The check does not validate the level.** Most of the gap is the early-commencement component,
which SB 419 does not buy and which is 72% of what this bill buys — the same decomposition that
settles Deliverable 3. The residual 2.3× is not validated and stays the honest open item. **Not
checkable at all:** every participant count here, because no published count of § 51.1-142.2
purchases exists; and the retirement-date distribution inside the window. Both are data requests
to VRS.

---

## 8. Fiscal years, fund split, local cost, administration

Unchanged from the repaired basis and stated here so the five rows are not quoted without it.
The 47% general-fund share applies to the **amortisation of trust cost only**; the $375,000
implementation allowance is **nongeneral fund** and is never multiplied by 47%. FY2028 carries
implementation only — a July 1 effective date splits the first programme year, so FY2028 holds no
benefit cost. **No local cost in any row, and no unfunded mandate on localities in any row: the
State Employee plan only, and S6's Hybrid members and S5's reopened window are state employees
too.** Administration is the one-time implementation allowance; **no position count is modelled**
in any row, which is a known gap in every figure in this package, not a finding of this issue.

---

## 9. Assumption register

Everything the model treated as given. Full text, with sources and vintages, in
`moo183-cost-per-participant/moo183_inputs.py`.

| # | assumption | value | unit | source | direction of error |
|---|---|---|---|---|---|
| 1 | published scoreboard retirement deadline | 6 | months after the later of completion and eligibility | `inputs.RETIREMENT_DEADLINE_MONTHS`, published engine | a longer delay lowers cost; **measured**, not assumed |
| 2 | authorised rung | 12 | same dial | the board's controlling basis; MOO-85, MOO-71 §3 | none — a choice of basis |
| 3 | published counts and costs, 7 designs × 3 levels | see Table A | elections / dollars PV | `out_v2_scenarios.csv`, sponsor package v1.0 | **locks**, not inputs; a mismatch stops the run |
| 4 | take-up, Pathway A / B / S5 | low / central / high as published | fraction of the eligible pool | `inputs.TAKEUP_*` | dominant driver of every aggregate, factor ~3.3; cancels to ±1% in every ratio |
| 5 | price elasticity of take-up | −0.6 | dimensionless | published engine; applies to **S3 and S8 only** | puts S3's and S8's counts one inference further from data than S1's |
| 6 | recommended-row participants | 18.905903746 (9.4530–31.5098) | elections over 48 months | MOO-48 / MOO-85, reproduced byte-identical today | **modeled demand**; no external anchor; rung-invariant |
| 7 | recommended-row ladder, rungs 0–24 | $1,661,819 … $1,141,496 | dollars PV | MOO-48 §3, locked rung-by-rung by MOO-85 §0 | measured; the rung is a choice, not an error |
| 8 | who retires when inside the window | all on the last permissible day | — | **analyst judgment, no external anchor** | **one-sided dearer: +7.5% uniform, +16.3% all-earliest** |
| 9 | current-basis count and cost | 18.3965; $1,321,112 PV | elections; dollars | MOO-32 v6 basis run (review copy, unpublished) | **upper bound on the count** — clause (viii) unmeasured |
| 10 | VRS implementation allowance | $375,000 | dollars, one-time, NGF, FY2029 | **analyst judgment**, defensible $150,000–$750,000 | same in every design, so it moves levels and never rankings; no position count modelled |
| 11 | general-fund share of amortisation | 47% | fraction | repaired §8 | applies to trust-cost amortisation only |
| 12 | statutory dials in the live text | 6.00%; $3,000,000; $170,000; 12-month completion | — | `bill-text-s8` doc rev 76 / store rev 61, verified today | none, unless the text moves again |
| 13 | eligibility screens as modelled | clauses (v), (vi), (vii) + C's zero bar | — | v6 basis run on rev 19/21 | **clause (viii) is in the live text and in no run** — one-sided, reduces the count |

**Carried on every figure:** single-life basic pension only — no health insurance credit, group
life, survivor loading, disability or death-in-service, which **understates** cost. Expected
weights on a cell grid, not simulated people, so there is no within-cell salary dispersion.
Cap utilisation measured gross, every reservation live at once. Pre-decisional and internal;
release is the Policy Director's decision. **The two S8 rows above are internal under the
board's standing publication restriction and are not released by this document.**

---

## 10. How to rerun

```bash
cd moo183-cost-per-participant
python3 moo183_cpp.py > out_moo183_run.txt 2>&1   # ~11 min, exit 0 only if every §0 lock passes
```

Register `moo183_inputs.py`; inventory `README_MOO183.md`; outputs `out_moo183_rows.csv` (42
rows) and `out_moo183_recommended_ladder.csv`. The engine in `engine/` is the published repaired
engine copied byte-for-byte and unmodified. Python 3.11, no third-party packages, no RNG.
