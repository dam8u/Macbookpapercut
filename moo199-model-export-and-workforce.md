# MOO-199 — the authorised-basis model export, and the workforce exchange on the recommended design's own anchor

**Fiscal & Impact Modeler, 12 October 2026.** Two products, both model runs. Model at
`moo199-authorised-export/`; register `moo199_inputs.py`; transcript `out_moo199_run.txt`;
export `out_moo199_model_data.json`. Rerun in 90 seconds, exit 0 only if all 42 locks pass.

**Internal working draft material. Pre-decisional and internal. Not a VRS actuarial result.
Nothing reliable beyond two significant figures. Release is the Policy Director's decision.**

---

## 0. Read this first — the headline, the surprise, and the one thing I could not reach

**The surprise, stated before anything else, because it contradicts text the Editor has
already cut.** The ten documents now say the workforce exchange's `$64,678` anchor is wrong
and that the error *"runs against the proposal — the real exchange is worse than the
documents show."* **On a consistent recomputation the coverage ratio is better, not worse:
about 88% rather than the printed 71%.** The documents reached "worse" by looking at the
denominator alone. Both legs of the exchange scale with months of acceleration, and the
recommended design accelerates retirement by **44.9 months** against repaired S1's **34.1**
— so when the anchor rose 11.0%, the workforce leg rose 38.0%. **The v2.1 pass has to change
the direction sentence, not just the figure.** §2.3.

**The headline.**

> On the recommended design's own anchor — **$71,813** of net trust cost per participant on
> the authorised basis — the workforce effect covers about **88%** of the pension cost in the
> central case (**−18% to 213%** across the three replacement-differential cases), not the
> **71%** the documents print against repaired S1's `$64,678`; the exchange breaks even at
> **50 months** of acceleration against the **45 months** this design measures, so on the
> central case it **does not** clear; and the coverage ratio is nearly invariant to the
> retirement rung — **77% to 98%** across the whole ladder — even though the pension leg
> alone moves **49%**.

**The sensitivity that controls it, flagged in the first paragraph as my standard requires.**
No 10% move in any single input swings the coverage figure by more than 25% (the largest is
13.2%, on the replacement differential). What controls the answer is three **choices of
basis**, and two of them are bigger than the correction this issue was raised to make:

1. **PV or nominal.** The pension leg is a present value at 6/30/2025; the workforce leg out
   of the engine is an **undiscounted** flow starting years later. The printed exchange made
   that comparison and so does my primary table. On a PV-consistent comparison the central
   case covers **54%**, not 88%. **The nominal convention flatters the bill.** §2.6.
2. **The replacement differential is not anchored.** The only published salary gap available
   is 10.9%, not the judged 18%. At 10.9% coverage is **42%**. §5.
3. **Which rung the exchange is printed on** — the one place the two legs move *together*,
   which is why this is the sturdy finding rather than a risk. §4.

**What I could not reach, and it bounds product 1.**
`AgentCreated/v2.0/05-model-code-and-data/model-current-12-october/moo32_v6_engine.py` is
**not in this workspace** — not in the repository, not in any `workspaces/*` tree, and a
filesystem-wide search for a directory named `AgentCreated` returns no match. Nor is
`make_model.py`. This is the same absence MOO-193 recorded for
`AgentCreated/_review-MOO-32-charts-v6/`. I did not block on it. Four of the five blocks are
authorised or measured without it; one is not; and every row in the export carries a quality
label saying which. §1.7.

---

## 1. Product 1 — the interactive model's data shape, on the authorised basis

**The export is `moo199-authorised-export/out_moo199_model_data.json`** (63 KB): `meta`,
`headline`, the five blocks, and `sensitivity`. Each block is also a CSV.

### 1.1 Block 1 — the retirement-deadline ladder *(authorised)*

The only block that is authorised outright. Participants are rung-invariant, so the
per-participant column is one constant division.

| rung (months) | authorised trust PV | $/participant | mean accel. months | vs rung 12 | v6 ÷ MOO-48 | |
|---:|---:|---:|---:|---:|---:|---|
| 0 | $1,567,024 | $85,181 | 56.85 | +18.6% | 0.94296 | what the superseded documents printed |
| 1 | $1,547,336 | $84,110 | 55.85 | +17.1% | 0.94245 | the drafted text |
| 6 | $1,446,675 | $78,639 | 50.85 | +9.5% | 0.93966 | |
| **12** | **$1,321,112** | **$71,813** | **44.85** | — | 0.93564 | **the authorised rung** |
| 18 | $1,190,510 | $64,714 | 38.85 | −9.9% | 0.93064 | |
| 24 | $1,055,048 | $57,350 | 32.89 | −20.1% | 0.92427 | |

**Internal check on the authorised ladder's shape — it passes.** The v6/MOO-48 ratio falls
**monotonically** from 0.94296 at rung 0 to 0.92427 at rung 24: the two bases diverge *more*
the longer the permitted delay. That is the expected sign, and it is not a free parameter —
the no-advance bar refuses the least-accelerated members, and the longer the window the
larger the share of cost that is acceleration. The ladder as stated in the issue is
internally consistent with the v6 figure set, and rung 12 agrees with it to 50 cents.

Low and high columns in the export are the central figure scaled by the participant ratio.
Cost per participant is take-up invariant: **locked** directly on the authorised basis at
rung 12 and **measured** on the MOO-48 ladder at all six rungs. Applying it to the authorised
basis away from rung 12 is an inference from those two facts, labelled as such in the export.

### 1.2 Block 2 — the member-price grid *(measured, and basis-invariant)*

56 cells: the S8 earned-service price and price per year over age × completed service, for
Plan 1 and Plan 2, beside the ANC and full-AEC references and the resulting multiple and
share. Held at the measured mean participating salary **$104,181** and the measured mean
**1.6114** years purchased, over the cohort's own support (ages 50–67, service 20–30).

**Why this block does not move with the authorised basis, stated because it is the
load-bearing claim here.** §7 item 22 option (c) measures subsection C clause (ii) — the
**certified subsidy** — at the filing date, and clause (vii)'s no-advance bar is an
**eligibility** screen. Neither is a term of the member price. So option (c) and the bar move
*who* is in the cohort and *what the Commonwealth certifies*; they do not move the price
function. The cohort-weighted **mean** does move with the cohort, and the authorised mean is
not available here. What *is* available is the authorised **pair**, and the run reproduces it:
**1.4166× ANC and 42.51% of AEC**, which prints as the authorised 1.42× / 43%.

The structural result the grid shows, which is the sponsor question it exists to answer: the
S8 price rises with time since hire at roughly `(1 + i) / (1 + salary growth) − 1` per year,
so the basis is calendar-neutral only where the statutory rate equals the member's own salary
growth. At 6.00% it sits above it, so **S8 re-creates a calendar penalty** — smaller than the
full-AEC one it replaces, and not zero.

### 1.3 Block 3 — the statutory-interest dial *(measured on the MOO-48 cohort; authorised only at 6.00%)*

| rate | participants | trust PV (MOO-48 cohort) | $/participant | member paid/participant | × ANC | tag |
|---:|---:|---:|---:|---:|---:|---|
| 4.00% | 25.0955 | $2,094,569 | $83,464 | $14,553 | 0.884 | **restricted** |
| 4.50% | 23.3690 | $1,907,562 | $81,628 | $16,388 | 0.995 | **restricted** |
| 5.00% | 21.7681 | $1,732,101 | $79,570 | $18,446 | 1.120 | **restricted** |
| 5.50% | 20.2834 | $1,567,211 | $77,266 | $20,751 | 1.260 | **restricted** |
| **6.00%** | **18.9059** | **$1,411,988** | **$74,685** | **$23,331** | **1.417** | **authorised (measured)** |
| 6.50% | 17.6275 | $1,265,601 | $71,797 | $26,219 | 1.592 | **restricted** |
| 6.75% | 17.0230 | $1,195,478 | $70,227 | $27,789 | 1.687 | **restricted** |
| 7.00% | 16.4405 | $1,127,280 | $68,567 | $29,449 | 1.788 | **restricted** |

**This is the one block that needs the v6 engine and does not have it.** The authorised PV at
6.00% is the measured v6 figure; the off-6.00% authorised PVs in the export are **derived by
anchored rescaling** at the ratio 0.935639, and that is an assumption, not a measurement. The
no-advance bar and the zero-month bar screen on quantities the member price enters, so the
share of the cohort they refuse moves with the rate. Direction: a higher rate prices more
members out of a positive clause (ii) solution, so the authorised cohort shrinks *faster* than
the MOO-48 cohort as the rate rises — the derived figures above 6.00% are an **upper** bound
on cost and those below a **lower** bound. **This block, and only this block, must be
re-measured in the v2.1 pass.**

**And a product finding, not a note. A live interest dial cannot ship in a sponsor-facing
model.** Every row away from 6.00% carries the board's standing publication restriction on the
S8 family's comparative dollar cells — the restriction MOO-183 §9 invoked over its 4.00% and
5.00% rows. A model with a live dial exposes those figures to anyone who moves it. **The dial
ships as a static 6.00% column, or the restriction is lifted first.** Every restricted row is
tagged `publication_restricted = true` in the export and in the CSV.

The dial's shape, for the record: from 4.00% to 7.00% the member pays **2.02×** more per
participant and the count falls **34.5%**. It is the strongest single lever in the model on
the aggregate, and it moves the price and the count in the same direction.

### 1.4 Block 4 — the cap sweep

**Unit discipline first, because the package has made this error once already** (MOO-72 repair
register item B): § 51.1-142.4 D 2 caps **certified subsidy plus its mandatory 20 percent
contingency**. It does **not** cap trust cost. Those are different quantities and the ratio
between them is not 1.

**4a. Utilisation against the cap dial — exact on the authorised basis**, because utilisation
is a ratio and both terms are in the authorised figure set. The formula
`(1 + 20%) × certified reserved ÷ cap` reproduces the authorised 78.1872% central and 130.31%
high to five decimals, which is the lock that lets this table be published without a new run.

| cap | low | central | high | binds at |
|---:|---:|---:|---:|---|
| $1,500,000 | 78.2% | 156.4% | 260.6% | central, high |
| $2,000,000 | 58.6% | 117.3% | 195.5% | central, high |
| $2,500,000 | 46.9% | 93.8% | 156.4% | high |
| **$3,000,000** | **39.1%** | **78.2%** | **130.3%** | **high — the drafted value** |
| $3,500,000 | 33.5% | 67.0% | 111.7% | high |
| $4,000,000 | 29.3% | 58.6% | 97.7% | never |
| $5,000,000 | 23.5% | 46.9% | 78.2% | never |
| $6,000,000 | 19.5% | 39.1% | 65.2% | never |

- reservation aggregate including contingency: central **$2,345,616**, high **$3,909,360**
- the cap that just clears high take-up: **$3,909,360**, i.e. **$909,360** above the drafted figure
- the take-up multiple at which $3,000,000 binds: **1.279×** central
- the per-election ceiling $170,000 plus contingency = **$204,000** against the cap

**And the thing the dial must not imply: the retirement rung does not move this table.** D 2
meters the **reservation**, certified on the anticipated *earliest* qualifying retirement date,
which the window does not move. A cap tab wired to the rung dial would be wrong.

**4b. The cap as an admission rule — and the two tables disagree, which is the finding.**
Applied to **trust cost**, the cap stops denying anyone at $2,500,000; at the drafted
$3,000,000 it denies nobody even at high take-up, because trust cost PV there is $2,353,313.
Applied to the **reservation** aggregate — what D 2 actually meters — the same $3,000,000 sits
at 130% at high take-up and binds. **So an interactive model that caps the trust-cost ledger
tells a sponsor the cap never binds, when on the drafted figures and the drafted quantity it
binds at high take-up.** 4a is the table to wire the cap tab to; 4b is in the export to show
what the wrong wiring says. (4b is measured on the MOO-48 cohort, because admission is a run;
it is published as a shape, not a level.)

### 1.5 Block 5 — the workforce break-even

In the export as `workforce_exchange`: the three cases, the break-even months and
differential, a 30-cell months × differential grid, the exchange at all six rungs, the
PV-consistent variant, and the printed figures beside them for comparison. The substance is
product 2, §2.

### 1.6 What the locks prove

42 assertions, all pass, printed in §0 of the transcript.

- **§0.1** — the runner reproduces the published MOO-48 deadline ladder at **all six rungs ×
  three take-up levels**: trust cost PV to the cent, participants, and mean acceleration to
  three decimals. 30 assertions.
- **§0.2** — the same run reproduces the **authorised member-price pair**, 1.42× / 43%.
- **§0.3** — the authorised ladder's rung 12 equals the v6 trust PV to 50 cents, and cost per
  participant is $71,813 at low, central and high alike.
- **§0.4** — the cap-utilisation formula reproduces the authorised 78.1872% / 130.31%.
- **§0.5** — the model reproduces **the exchange the documents actually print**: repaired S1
  at the 6-month rung, $64,678 per participant, 71% coverage. Without this lock the
  recomputation in §2 would have nothing to be a correction *of*.

### 1.7 What the export is not, and the mechanical step left for the v2.1 pass

`make_model.py` is inside the same unreadable tree, so **the exact key names it consumes could
not be verified.** The export carries `meta.key_binding_verified = false` and a
`meta.key_binding_table` mapping each block to the model tab and the dial it feeds. Binding
the keys is a ten-minute mechanical check for whoever has the folder; **no figure in the
export depends on it.** I would rather ship the data with the binding named as unverified than
assert a binding I could not test.

---

## 2. Product 2 — the workforce exchange, recomputed

### 2.1 The numerator convention, chosen and stated

**Convention T, trust-only: the denominator is net trust cost per participant, `$71,813`,
excluding the `$375,000` one-time nongeneral-fund implementation allowance.** MOO-183 §6 asked
for one convention, named. Three reasons:

1. **It makes this a one-driver change.** The printed `$64,678` was a trust-only figure. Hold
   the convention and the only thing that moves is the design anchor, which is what the issue
   asked for and what a reader can audit.
2. **It does not pair a fixed cost with a per-participant flow.** The allowance is a one-time
   administrative cost that does not scale with participants; the workforce effect is a
   per-participant flow over an acceleration window. Mixing units is the error this role
   exists to prevent, and it is the same error §2.3 identifies in the printed figure.
3. **It changes no ranking** (MOO-183 §6) — only the level, and the level is reported both ways.

| | per participant |
|---|---:|
| **convention T anchor** | **$71,813** |
| convention A anchor (all-in) | $92,198 *(= T + $20,384, the allowance over 18.3965 participants)* |
| the printed anchor | $64,678 *(repaired S1, 6-month rung)* |
| **T less printed** | **+$7,135, +11.0%** |

Convention A appears beside every headline below.

### 2.2 The three differential cases

Both legs come from the **same run**: incumbent salary **$104,181** and acceleration
**44.8516 months**, measured on the recommended design's own rung-12 run — not the engine's
`MONTHS_ACCELERATION` default of 2/6/14 months. That is what makes the exchange internally
consistent, and §0.5 confirms it is what the printed exchange did for S1.

| case | diff. | accel. mo | gross saving | frictions | net workforce | covers (T) | covers (A) | net state / participant (T) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| conservative | 8% | 44.85 | $33,613 | $46,338 | **−$12,725** | **−17.7%** | −13.8% | $84,538 |
| **central** | **18%** | **44.85** | **$89,888** | **$26,357** | **$63,531** | **88.5%** | **68.9%** | **$8,283** |
| optimistic | 30% | 44.85 | $153,250 | $0 | **$153,250** | **213.4%** | 166.2% | −$81,436 |

**The conservative case is negative.** At an 8% replacement differential the recruitment cost
and productivity ramp exceed the salary saving and the workforce leg makes the Commonwealth's
position *worse*, not better. That is a real cell of this model and it belongs in any artifact
that prints the central one. **Never report the point estimate without the range.**

Both the salary and the acceleration are the **MOO-48 cohort's**, because the v6 cohort's own
statistics are not in the cited figure set. On acceleration the direction of error is
one-sided and favourable to the result: the no-advance bar refuses members whose purchase
advances eligibility by less than a month — the **least-accelerated** band — so the authorised
cohort's own mean is **at or above** 44.85 months and **every coverage figure here is a lower
bound** on the authorised figure.

### 2.3 The revised "covers X%" — and why the documents' stated direction is wrong

There are two different questions the phrase can answer, and they give different answers.

**(i) Denominator-only swap — what the documents' wording implies.** Keep the printed
workforce effect of **$46,037** (which is S1's, at S1's 34.1 months) and divide by the
recommended design's anchor: **64.1%**, against the printed 71%. *This is the figure that makes
the exchange worse, and it is the one the documents now point at.* **It is also the one I will
not print**, because it divides one design's workforce effect by another design's pension cost.

**(ii) Consistent single-design recomputation — both legs from the recommended design on the
authorised rung: 88.5% on convention T, 68.9% on convention A.** **This is the figure to
print.** It is higher than the printed 71%, not lower.

**Why (ii) rises even though the anchor rose.** Both legs scale with acceleration. The
recommended design accelerates **44.9** months against S1's **34.1**, **+31%**. The pension
leg rose **+11.0%**; the workforce leg rose **+38.0%**, because the workforce saving is close
to linear in the window while the frictions are fixed per hire.

**So this is a finding against text the Editor has already cut.** `04-fiscal-analysis.md` §9
and `02-policy-brief.md` §6 now say the error *runs against the proposal* and that the real
exchange is worse. On a consistent recomputation the coverage **ratio** is better. What is
genuinely worse is the **pension cost per participant**, by the **$7,135** the documents
correctly name. **The v2.1 pass has to change the direction sentence, not just the figure**,
and §2.6 is the one qualification that can reverse this again.

### 2.4 The revised break-even

| | |
|---|---:|
| break-even months, convention T | **49.90** — against a measured 44.85, it falls **5.05 months short** |
| break-even months, convention A | 62.33 — falls 17.48 months short |
| break-even months as printed | 45.47 *(on S1's salary and the $64,678 anchor)* |
| break-even replacement differential at 44.85 months, convention T | **19.77%** *(central assumption: 18%)* |

**So the central case does not clear.** It covers 88.5% and needs 100%. The two ways it
clears, both inside the model's own stated ranges: five more months of acceleration, or a
replacement differential above **19.8%** rather than 18%. Both are inside the register's
defensible ranges, and neither is anchored — which is the honest reading of "the exchange is
close to break-even and the model cannot tell you which side of it you are on."

**The break-even grid** (net workforce effect less the convention-T anchor, per participant; a
positive cell pays for itself on the workforce leg alone):

| accel. months | 8% | 13% | 18% | 24% | 30% |
|---:|---:|---:|---:|---:|---:|
| 12 | −$73,409 | −$67,786 | −$62,164 | −$55,417 | −$48,671 |
| 24 | −$66,687 | −$54,585 | −$42,482 | −$27,959 | −$13,437 |
| 33 | −$61,646 | −$44,683 | −$27,721 | −$7,366 | $12,989 |
| **45** *(measured)* | −$54,924 | −$31,481 | **−$8,039** | $20,092 | $48,223 |
| 57 | −$48,202 | −$18,280 | $11,643 | $47,550 | $83,456 |
| 69 | −$41,480 | −$5,078 | $31,324 | $75,007 | $118,690 |

### 2.5 The aggregate exchange

| | |
|---|---:|
| pension cost PV, authorised | $1,321,112 |
| implementation allowance, FY2029 NGF | $375,000 |
| net workforce effect, central case | $1,168,742 *(= $63,531 × 18.3965, undiscounted)* |
| **net state effect, convention T** | **$152,369** |
| net state effect, convention A | $527,369 |

Range across the three cases, convention T:

| case | aggregate workforce effect | net state effect | covers |
|---|---:|---:|---:|
| conservative | −$234,096 | $1,555,208 | −17.7% |
| **central** | **$1,168,742** | **$152,369** | **88.5%** |
| optimistic | $2,819,257 | −$1,498,146 | 213.4% |

At reportable precision: **about $150,000 net, on a range from about $1.6 million to about
−$1.5 million.** The range crosses zero. Any artifact that prints the central figure without
it is asserting a precision four assumptions in the register do not support.

### 2.6 The PV / nominal mismatch — inherited, larger than this issue's correction, and it reverses the direction

The pension leg is a **present value at 6/30/2025**. The workforce leg out of
`engine/workforce.py` is an **undiscounted nominal flow** over an acceleration window that
opens years later — mean election month 43.5, plus a 12-month completion window, plus the
12-month rung, with a window midpoint 1.87 years beyond that. Discounting each election's
saving at the engine's own 6.75% back to the valuation date:

| case | PV workforce effect / participant | covers (T) | covers (A) |
|---|---:|---:|---:|
| conservative | −$7,813 | −10.9% | −8.5% |
| **central** | **$38,927** | **54.2%** | **42.2%** |
| optimistic | $93,922 | 130.8% | 101.9% |

**On a PV-consistent comparison the central case covers 54%, not 88%.** A stated approximation,
not a measurement: the engine does not expose a per-election retirement date, and the true
window opening is at or after the date I used — so this is an **upper bound** on the
PV-consistent leg, and the true coverage is at or below 54%.

**The printed exchange has the same flaw**, so this is not a defect of the recomputation; it is
a defect of a comparison the package has always made. It is also **larger than the
design-anchor correction this issue was raised to make.** I am not folding it into the headline
— one driver at a time, and the issue asked for the anchor — but **the v2.1 pass cannot print a
coverage percentage without deciding which convention it is on**, and it should be a separate,
named decision for the Policy Director. Direction: **the nominal convention overstates the
workforce leg, so it flatters the bill.**

---

## 3. Sensitivity

**No 10% move in any single input swings the coverage figure by more than 25%.** The tornado,
on the central case's 88.5%:

| input | −10% | base | +10% | swing |
|---|---:|---:|---:|---:|
| replacement differential | 76.8% | 88.5% | 100.2% | 13.2% |
| months of acceleration | 78.2% | 88.5% | 98.7% | 11.6% |
| pension anchor | 98.3% | 88.5% | 80.4% | 11.1% |
| incumbent salary | 78.9% | 88.5% | 98.0% | 10.8% |

What controls the answer is three **choices of basis**, which is a bigger source of movement
than any 10% move and is why they are reported as bases and not as tornado bars:

1. **Which rung the exchange is printed on** — §4, and it comes out *in the model's favour*.
2. **PV or nominal** — §2.6. It moves the central coverage from 88% to 54%, more than anything
   else on this page.
3. **The acceleration is unsourced as a behavioural quantity.** The model measures how much
   earlier the design *permits* retirement. Nobody has measured how much earlier members
   actually retire, and there is no published distribution of chosen retirement dates inside a
   VRS window anywhere. Analyst judgment, no anchor, **and it is the single biggest unevidenced
   input in the exchange** — the same item MOO-183 §5 flagged second.

---

## 4. The sturdy finding: the exchange ratio is nearly rung-invariant

The retirement rung moves both legs, and it moves them together.

| rung | $/participant | accel. mo | net workforce / participant | covers (T) | net state / participant |
|---:|---:|---:|---:|---:|---:|
| 0 | $85,181 | 56.85 | $83,212 | 97.7% | $1,968 |
| 1 | $84,110 | 55.85 | $81,572 | 97.0% | $2,538 |
| 6 | $78,639 | 50.85 | $73,372 | 93.3% | $5,267 |
| **12** | **$71,813** | **44.85** | **$63,531** | **88.5%** | **$8,283** |
| 18 | $64,714 | 38.85 | $53,690 | 83.0% | $11,024 |
| 24 | $57,350 | 32.89 | $43,905 | 76.6% | $13,446 |

**Coverage runs 77% to 98% across the whole ladder while the pension leg alone moves 49%.**
That is the result two printed figures — one design's ratio at one rung — could never have
shown, and it is the one answer in this document that is robust to the basis choice MOO-183
named as its dominant item. It also has a plain reading for a sponsor: **a longer permitted
retirement window is cheaper for the trust and worth proportionately less on the workforce
side, so the exchange does not improve by lengthening the window.** Note the direction: net
state cost per participant is *lowest* at rung 0 and *highest* at rung 24, the opposite of the
pension leg alone.

---

## 5. External sanity check — two disagreements and one agreement

**Check 1 — the replacement differential, against the only published salary gap. DISAGREEMENT,
and it is material.** The engine's register records the central 18% as *judgment* between two
published anchors. The lower anchor is the only one that is a measured salary gap: VRS
valuation p.50, average salary at age 35–39 ($74,012) against age 55–59 ($83,081) = **10.9%**
lower. Run the exchange at 10.9%: net workforce effect **$30,430** per participant, covering
**42.4%** — the published figure cuts the coverage by **52%**. The register's own reasoning for
why 10.9% is a floor rather than the answer is sound (it is cross-sectional — two age bands in
one year — so it understates an incumbent-versus-new-hire gap, and DHRM publishes no
incumbent/new-hire salary pairs by role), and I am not overturning it. What the check
establishes is that **the 18% is not anchored**, that the distance between the anchored floor
and the judged central moves the headline by half, and that a hostile reader who insists on
published figures only gets **42%**, not 88%. Print the range, never the point.

**Check 2 — the sign of the tier effect on the agency's books. AGREEMENT, and it is the one
structural check that comes out in the model's favour.** At 18% on a $104,181 incumbent the
annual salary differential is $18,752 and the annual *loaded* differential is $19,682 — but had
the successor carried the incumbent's own load rate it would be $22,672. The tier change
destroys **$2,990 a year** of the saving, because the Hybrid successor pays up to 3.5% of pay
in DC contributions the Plan 1 incumbent does not, on top of the same blended employer DB rate.
**On the agency's own books, replacing a Plan 1 incumbent with a Hybrid hire at the same salary
costs more**, so every dollar of agency-level saving has to come out of the salary gap alone.
The model has that sign right, against the direction a "turnover savings pay for it" claim
usually assumes.

**Check 3 — against the engine's own default. DISAGREEMENT, and it is the disagreement that
matters most.** The published engine's central acceleration assumption is **6 months**; this
design **measures 44.9** — **7.5×** the assumption. The engine's 2/6/14-month ladder was set
for a *general* early-retirement offset; this bill's Pathway A cohort buys an average 1.61
years of credit that advances unreduced eligibility by nearly four years. Those are not the
same quantity, and anyone who reads the 6-month default as a bound on the measured 44.9 will
conclude the workforce leg is seven times smaller than the model says. **The measured figure
is the right one for this cohort**; the gap is a reason to distrust the *level* of the
workforce leg, not its sign, and it is why §2.2 reports −18% to 213% rather than a point.

**Not checkable at all, and all three are data requests to VRS and DHRM:** every participant
count here (no published count of § 51.1-142.2 purchases exists); the retirement-date
distribution inside a VRS window; and the actual salary of the actual replacement for an
actual accelerated retiree.

---

## 6. Assumption register

Every figure above traces to a row here, to a lock in §1.6, or to a cited authorised figure.
Full register, with each item's source text and defensible range, is `moo199_inputs.py`.

| # | assumption | value | unit | source | direction of error |
|---|---|---|---|---|---|
| 1 | authorised participants | 18.3965 (9.1982–30.6608) | elections over the 48-month pilot | MOO-32 v6 figure set, cited | **upper bound** — clause (viii) is in the live text and in no run, and can only refuse more |
| 2 | authorised net trust cost, rung 12 | $1,321,112 ($660,556–$2,201,853) | dollars, PV at 6/30/2025 | MOO-32 v6, cited | rung 12 is the **cheap end**: +7.5% uniform, +16.3% all-at-earliest (MOO-85 §4) |
| 3 | authorised ladder, six rungs | $1,567,024 … $1,055,048 | dollars, PV, central | MOO-199 description = v6 deadline ladder | as #2; rung 12 cross-checks to 50 cents |
| 4 | certified subsidy reserved | $1,954,680 central, nominal | dollars over the pilot | MOO-32 v6, cited | pre-contingency; it is **not** trust cost |
| 5 | contingency inside the cap | 20% | fraction of certified subsidy | live bill text D 2/D 3, quoted in the live register | none — a drafted figure. It is why utilisation is 1.20× subsidy |
| 6 | aggregate cap | $3,000,000 | dollars, cumulative | § 51.1-142.4 D 2, doc revision 76 | none, unless the text moves |
| 7 | statutory interest | 6.00% | per annum, compounded annually | live text; verified at MOO-183 | none — a decided dial |
| 8 | mean participating salary | $104,181 | dollars per year | **measured**, MOO-48 rung-12 run | MOO-48 cohort, not v6's; the authorised mean is unavailable |
| 9 | mean acceleration | 44.8516 | months per participant | **measured**, same run | MOO-48 cohort; one-sided **favourable** — the no-advance bar removes the least-accelerated band, so coverage here is a **lower bound** |
| 10 | mean years purchased | 1.6114 | years | **measured**, same run | as #8 |
| 11 | replacement differential | 8% / 18% / 30% | fraction below incumbent salary | engine register: **judgment** between two published anchors | **not anchored.** Only published gap is 10.9%; at 10.9% coverage is 42% (§5) |
| 12 | vacancy length | 4.0 | months | DHRM 78-day hire cycle + judgment for the rest | longer vacancy → larger salary saving, larger coverage cost |
| 13 | vacancy coverage cost share | 0.90 / 0.55 / 0.25 | fraction of vacant salary | **judgment**, defensible 25%–90%; Virginia publishes nothing | higher → smaller net saving. Cuts against the offset |
| 14 | recruitment cost per hire | $8,000 / $5,000 / $3,000 | dollars | **judgment**; not published by DHRM or JLARC | cuts against the offset |
| 15 | productivity ramp loss | 0.40 / 0.25 / 0.10 | fraction of replacement first-year salary | **judgment**, defensible 10%–40% | cuts against the offset. Omitting it would bias the answer optimistic |
| 16 | implementation allowance | $375,000 | dollars, one-time, NGF, FY2029 | **analyst judgment**, defensible $150,000–$750,000; no position count modelled | two-sided and wide. 28% of the per-participant anchor once spread; same in every design, so it moves levels never rankings |
| 17 | discount rate | 6.75% | per annum | engine `DISCOUNT_RATE` | applies to the pension leg; the workforce leg is nominal — §2.6 |
| 18 | general-fund share | 47% | fraction of amortisation | engine register | applies to trust-cost amortisation only; the allowance is wholly NGF |
| 19 | numerator convention | T (trust-only) | — | **my choice**, §2.1 | convention A is +$20,384 per participant; changes levels, not rankings |
| 20 | PV adjustment of the workforce leg | window opens at election month + 12 + rung; midpoint discounting | — | **stated approximation** | **upper bound** on the PV leg — the true opening is at or after this date |

**Carried on every figure, from the engine family:** single-life basic pension only — no health
insurance credit, group life, survivor loading, disability or death-in-service, which
**understates** cost. Expected weights on a cell grid, not simulated people, so there is no
within-cell salary dispersion. Cap utilisation measured gross, every reservation live at once.

---

## 7. Fiscal years, fund split, local cost, administration

Unchanged from MOO-183 §8 and restated so this document stands alone. The pilot runs FY2028–31
in the engine's own layout; the 47% general-fund share applies to the **amortisation of trust
cost only**; the $375,000 implementation allowance is wholly **nongeneral fund**, one-time, in
the first pilot year. **No local cost and no unfunded local mandate:** the programme runs
between VRS, state agencies as employers, and state agency employees in Plan 1 and Plan 2.
Nothing in it places a duty on a locality. **Administration:** the $375,000 is an allowance,
not a costed position count — if the Policy Director needs positions and systems split into
one-time and ongoing, that is a separate run and a data request to VRS, and it has no bearing
on any figure above.

---

## 8. What is not mine, and who owns it

- **Whether clause (viii) refuses anybody** that clauses (v), (vi) and (vii) do not — Statutory
  Researcher. Until it is measured, 18.4 is a ceiling. MOO-193 addressed the reading; no
  committed run has the screen in it.
- **Whether the no-advance bar's effect on mean acceleration** is as I have reasoned in §2.2 —
  Statutory Researcher on the reading, me on the arithmetic once the reading is settled. My
  direction-of-error claim is a one-line inference and a reviewer should attack it, because the
  whole "lower bound" framing of §2.2 rests on it.
- **Whether the exchange should be printed in PV or nominal** — the Policy Director. §2.6 gives
  both and the direction. It is a bigger decision than the one this issue was raised to make.
- **Whether a live interest dial may ship** — the Policy Director, because it is a publication
  question about the S8 restriction, not a modelling one. §1.3.
- **The document rebuild** — the Editor. Nothing in this document writes to MOO-72 or to the
  `v2.0` folder. Both products travel in the `v2.1` pass already recorded in `VERSIONS.md`.

---

## 9. How to rerun

```bash
cd moo199-authorised-export
python3 moo199_export.py > out_moo199_run.txt 2>&1   # ~90s, exit 0 only if all 42 locks pass
```

Register `moo199_inputs.py`; inventory `README_MOO199.md`; export
`out_moo199_model_data.json`; eight CSVs beside it. Python 3.11, no third-party packages,
deterministic. The engine is imported from `../moo183-cost-per-participant/engine/` and is not
modified.
