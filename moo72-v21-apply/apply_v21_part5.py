#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 5 — the workforce exchange goes back behind a marker.

Why this part exists. Part 2 printed MOO-199's recomputation. Checking it against the
chart set that ships in the same folder found that the two authorised artifacts disagree
on the quantity, and on one input in a way that matters:

  * MOO-199 measures the exchange at 44.8516 months of acceleration, taken from the MOO-48
    cohort because "the v6 cohort's own statistics are not in the cited figure set", and
    reasons that the authorised cohort's own mean must be AT OR ABOVE that, which makes
    every coverage figure in it a lower bound.
  * The authorised chart set measures the authorised cohort's own mean acceleration at
    42.8910 months (`out_moo32_v6_basis.json`, `member_price.mean_acceleration_months`),
    which is BELOW 44.85. The chart page built on it prints a different per-case split.

That is two authorised measurements of one quantity, and the reasoning in one of them is
contradicted by the other. Reconciling them is a model decision and not the Editor's, so
the per-case figures go behind a marker that names both, and the statements the two
measurements agree on stay in the text.

Additive; run after part 4.
"""
import os, sys

DST = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
DOCS = ["00-cover-and-contents.md", "02-policy-brief.md", "04-fiscal-analysis.md",
        "06-questions-and-answers.md"]
buf = {d: open(os.path.join(DST, d), encoding="utf-8").read() for d in DOCS}
applied = []


def rep(doc, old, new, tag):
    n = buf[doc].count(old)
    if n != 1:
        sys.exit(f"MISS [{tag}] in {doc}: found {n}\n---\n{old[:300]}\n---")
    buf[doc] = buf[doc].replace(old, new)
    applied.append((tag, doc))


MARKER = "`[WITHHELD — two authorised measurements disagree; referred to the Policy Director]`"

# ----------------------------------------------------------------- 04 §10
rep("04-fiscal-analysis.md",
"""first. **This table is measured on the recommended design at the authorised 12-month rung, with both
legs taken from the same run:** mean participating salary **$104,181** and mean acceleration
**44.85 months**.

| Case | Replacement differential | Gross saving | Recruitment + ramp | **Net workforce effect** | **Covers** |
|---|---:|---:|---:|---:|---:|
| Conservative *(leads)* | 8% | $33,613 | −$46,338 | **−$12,725** | **−17.7%** |
| **Central** | **18%** | **$89,888** | **−$26,357** | **+$63,531** | **88.5%** |
| Optimistic | 30% | $153,250 | $0 | **+$153,250** | **213.4%** |

*(Coverage is the net workforce effect over the trust's own net cost per participant on the
authorised basis, **$71,813**. On the all-in convention, which adds the one-time $375,000 allowance
across 18.3965 participants, the anchor is $92,198 and the central case covers **68.9%**. Rows are
rounded to the dollar from unrounded model output.)*

**The conservative case is negative, and it belongs in every artifact that prints the central one.**
At an 8% differential the recruitment cost and the productivity ramp exceed the salary saving and
the workforce leg makes the Commonwealth's position worse. In aggregate the central case is about
**$150,000** of net cost to the Commonwealth, on a range running from about **$1.6 million** of net
cost to about **$1.5 million** of net benefit. **The range crosses zero**, and no artifact in this
package prints the central figure without it.

**Break-even.** The exchange breaks even at **49.90 months** of acceleration against the **44.85**
this design measures — **5.05 months short** — or at a replacement differential of **19.77%**
against the 18% assumed. Both are inside the model's defensible ranges and neither is anchored,
which is the honest reading: the exchange is close to break-even and the model cannot tell you
which side of it you are on.""",
"""first. **The per-case figures are withheld in this version, and the reason is a disagreement
between two authorised measurements of the same quantity.**

| | the recomputation on the recommended design | the authorised chart set |
|---|---:|---:|
| mean acceleration | **44.8516 months** | **42.8910 months** |
| net workforce effect, conservative (8%) | −$12,725 | about +$16,000 |
| net workforce effect, central (18%) | +$63,531 | about +$61,000 |
| net workforce effect, optimistic (30%) | +$153,250 | about +$113,000 |
| covers, central | 88.5% | about 85% |
| covers, conservative | **−17.7%** | about **+22%** |
| break-even acceleration | 49.90 months | not stated |

**Neither set is adopted here.** The recomputation takes its salary and acceleration from the
earlier cohort, because the authorised cohort's own statistics were not available to it, and
reasons that the authorised cohort's mean acceleration must be **at or above** 44.85 months — which
would make every coverage figure in it a lower bound. The authorised chart set measures that same
mean at **42.8910 months**, which is **below** it. So the one-sided reasoning that supports the
recomputation's figures is contradicted by the artifact that ships beside them, and the two sets
differ most in exactly the case a hostile reader will quote: the conservative one, where one makes
the workforce leg **negative** and the other does not. **Reconciling them is a model decision and is
not made in this document.** The conflict is referred to the Policy Director; the chart page built
on the second measurement is held out of the published chart set for the same reason, at
`04-charts/held-pending-reconciliation/`.

**What the two measurements agree on, which is what this package asserts:**

- **At central assumptions the workforce effect does not cover the pension cost.** Both put the
  central coverage between about 85% and about 89%, against the **$71,813** per-participant anchor.
- **The exchange is close to break-even and the model cannot tell you which side of it you are on.**
- **The optimistic replacement-salary case is the only one that covers the cost**, and that
  differential is analyst judgment.
- **The frictions can swallow the saving.** How far they do is the quantity in dispute.
- **The coverage ratio is higher than the 71% this package printed before**, which was measured
  against a different design's anchor. Both measurements put it higher.""",
    tag="04-s10-withhold")

# The rung table: keep the direction, drop the disputed absolutes.
rep("04-fiscal-analysis.md",
"""**The one robust result: the exchange ratio is nearly invariant to the retirement rung**, because
the rung moves both legs together.

| Retirement rung | Trust cost per participant | Mean acceleration | Net workforce effect | **Covers** |
|---:|---:|---:|---:|---:|
| 0 months | $85,181 | 56.85 mo | $83,212 | 97.7% |
| 1 month *(the drafted text)* | $84,110 | 55.85 mo | $81,572 | 97.0% |
| 6 months | $78,639 | 50.85 mo | $73,372 | 93.3% |
| **12 months — authorised** | **$71,813** | **44.85 mo** | **$63,531** | **88.5%** |
| 18 months | $64,714 | 38.85 mo | $53,690 | 83.0% |
| 24 months | $57,350 | 32.89 mo | $43,905 | 76.6% |

**Coverage runs 77% to 98% across the whole ladder while the pension leg alone moves 49%.** So
**the exchange does not improve by lengthening the retirement window**: net cost to the Commonwealth
per participant is *lowest* at the shortest rung and highest at the longest, the opposite of the
pension leg taken alone. This is the one figure in this section that is robust to the basis choice
in qualification 1.""",
"""**One result survives the disagreement, because it is a ratio rather than a level: the exchange is
nearly invariant to the retirement rung.** The rung moves both legs together — a longer permitted
window is cheaper for the trust *and* worth proportionately less on the workforce side — so
**lengthening the retirement window does not improve the exchange**, and net cost to the
Commonwealth per participant is lowest at the shortest rung and highest at the longest, the opposite
of the pension leg taken alone. On the recomputation's own basis the coverage ratio moves only
between about 77% and 98% across the whole ladder while the pension leg alone moves 49%. The
*direction* is what this package relies on; the levels are inside the marker above. The trust-cost
column of that ladder is not in dispute and is printed in §6.""",
    tag="04-s10-rung")

rep("04-fiscal-analysis.md",
"""**And the honest conclusion, which is why no savings claim appears anywhere in this package:** on
either convention the central case does not cover the pension cost, and the only case that covers it
is the optimistic one.""",
"""**And the honest conclusion, which is why no savings claim appears anywhere in this package:** on
either convention, and on either measurement, the central case does not cover the pension cost, and
the only case that covers it is the optimistic one.""",
    tag="04-s10-conclusion")

rep("04-fiscal-analysis.md",
"""**The superseded 71%, the superseded net effect of
+$46,037 and the superseded 45-month break-even are listed in §13 and must not be reprinted.**""",
"""**The superseded 71%, the superseded net effect of
+$46,037 and the superseded 45-month break-even are listed in §13 and must not be reprinted**, and
the figures that would replace them are behind the marker above until the two measurements are
reconciled.""",
    tag="04-s10-direction-marker")

# ----------------------------------------------------------------- 04 §13
rep("04-fiscal-analysis.md",
"""| The workforce exchange printed on repaired S1's anchor — net effect **+$10,829 / +$46,037 / +$88,287** per participant, coverage **71%**, break-even about **45 months** | Withdrawn. The exchange is now measured on the recommended design's own anchor and its own acceleration (§10): **−$12,725 / +$63,531 / +$153,250**, coverage **88.5%**, break-even **49.90 months**. The two sets are not comparable — S1 accelerates 34.1 months and this design 44.85. |""",
"""| The workforce exchange printed on repaired S1's anchor — net effect **+$10,829 / +$46,037 / +$88,287** per participant, coverage **71%**, break-even about **45 months** | **Withdrawn, and not replaced in this version.** It was measured against a design this package does not recommend. Two authorised measurements of the exchange on the design it does recommend disagree, and §10 states both rather than choosing between them. |""",
    tag="04-s13-register-marker")

rep("04-fiscal-analysis.md",
"""| **The cost per participant for the recommended design used in the workforce exchange (§10)** | **Released.** The exchange is recomputed on the recommended design's own anchor, $71,813, and its own acceleration; the earlier statement of the error's direction is withdrawn. §10 and §13. | — |""",
"""| **The per-case figures of the workforce exchange (§10)** | `[WITHHELD — two authorised measurements disagree]` — they differ on the authorised cohort's mean acceleration (44.8516 against **42.8910** months) and most in the conservative case, where one makes the workforce leg negative and the other does not. What both support is in §10 and is asserted; the split is not. | Policy Director, with the Fiscal & Impact Modeler |""",
    tag="04-withheld-exchange-marker")

# ----------------------------------------------------------------- 02 §6
rep("02-policy-brief.md",
"""**This table is now measured on the design this package recommends, on its own anchor and its own
acceleration — 44.9 months against the original draft's 34.1 — so both legs come from one run.**

| Per participant, recommended design | Conservative | **Central** | Optimistic |
|---|---:|---:|---:|
| Replacement salary differential | 8% | **18%** | 30% |
| Gross saving | $33,613 | **$89,888** | $153,250 |
| Recruitment and productivity ramp | −$46,338 | **−$26,357** | $0 |
| **Net workforce effect** | **−$12,725** | **+$63,531** | **+$153,250** |
| Net cost to the trust per participating member, authorised basis | −$71,813 | −$71,813 | −$71,813 |
| **Net effect on the Commonwealth** | **−$84,538** | **−$8,283** | **+$81,436** |

*(Rows are rounded to the dollar from unrounded model output, so the last row can differ by $1 from
the difference of the two rows above it.)*

**At central assumptions the workforce effect covers about 88% of that cost; the conservative case
is negative.** At an 8% differential the recruitment cost and the productivity ramp exceed the
salary saving, and the workforce leg makes the Commonwealth's position worse rather than better. The
range is **−18% to 213%** and it crosses zero. Break-even needs **49.9 months** of acceleration
against the **44.9** this design measures, or a replacement differential above **19.8%** rather than
18% — so on the central case the exchange does **not** clear.

**Two things travel with the 88% and both are required.** First, **it compares an undiscounted
workforce flow with a present-value pension cost.** Discounted to the same date, the central case
covers **54% or less**. That nominal comparison is the one every version of this package has made,
including the 71% it printed before, and it **flatters the bill**; which convention the package
standardises on is a Policy Director decision and is not settled here. Second, **the 18%
replacement differential is not anchored** — the only published salary gap is **10.9%**, and at
10.9% the workforce effect covers **42%**.""",
"""**The per-case figures are withheld in this version.** Two authorised measurements of this exchange
on the design we recommend disagree — on the cohort's mean acceleration (44.8516 months against
**42.8910**) and, most, on the conservative case, where one makes the workforce leg negative and the
other leaves it positive. Reconciling them is a model decision and it has not been made. Document 04
§10 states both sets side by side and names the quantity in dispute. **What both measurements
support is asserted here:**

| Per participant, recommended design | |
|---|---:|
| Net cost to the trust per participating member, authorised basis | **$71,813** |
| Share of it the workforce effect covers at central assumptions | **about 85% to 89%** |
| The case that covers all of it | the optimistic one only |
| Per-case gross saving, frictions and net effect | """ + MARKER + """ |

**At central assumptions the workforce effect does not cover the pension cost on either
measurement**, and the exchange sits close enough to break-even that the model cannot tell you which
side of it you are on. **Two things travel with that and both are required.** First, **it compares
an undiscounted workforce flow with a present-value pension cost.** Discounted to the same date the
central case covers **54% or less**; the undiscounted comparison is the one every version of this
package has made, including the 71% it printed before, and it **flatters the bill.** Which
convention the package standardises on is a Policy Director decision and is not settled here.
Second, **the 18% replacement differential is not anchored** — the only published salary gap is
**10.9%**, and at 10.9% the workforce effect covers about **42%**.""",
    tag="02-s6-withhold")

rep("02-policy-brief.md",
"""lower** — about 88% against 71% — because both legs scale with acceleration and this design
accelerates 31% more of it.""",
"""lower** — both measurements put it higher — because both legs scale with acceleration and this
design accelerates far more of it.""",
    tag="02-s6-direction")

# ----------------------------------------------------------------- 06 Q5
rep("06-questions-and-answers.md",
"""**No, and the package does not claim it does.** Measured on the design we recommend, with both legs
from the same run, the workforce effect is worth **+$63,531** per participant after recruitment and
ramp-up cost, against a **net cost to the trust of $71,813 per participant** on the authorised
basis. **That is about 88% of the cost at central assumptions — and the conservative case is
negative:** at an 8% replacement differential the recruitment cost and the productivity ramp exceed
the salary saving, so the workforce leg makes the Commonwealth's position worse. The range is
**−18% to 213%** and it crosses zero. Break-even needs **49.9 months** of acceleration against the
**44.9** this design measures, or a differential above **19.8%** rather than 18%.

Two things travel with the 88%. It compares an **undiscounted** workforce flow with a
**present-value** pension cost; discounted to the same date the central case covers **54% or less**,
and the undiscounted convention flatters the bill. And the 18% differential is **not anchored** —
the only published salary gap is 10.9%, where coverage is **42%**.""",
"""**No, and the package does not claim it does.** At central assumptions the workforce effect covers
**about 85% to 89%** of the **$71,813** the trust spends per participating member, and the only case
that covers all of it is the optimistic one. The exchange sits close enough to break-even that the
model cannot tell you which side of it you are on.

**The per-case figures are withheld in this version, and we would rather say so than pick one.** Two
authorised measurements of the exchange disagree — on the cohort's mean acceleration (44.8516 months
against 42.8910) and most in the conservative case, where one makes the workforce leg negative and
the other leaves it positive. Document 04 §10 states both. Reconciling them is a model decision and
it has not been made.

Two things travel with the coverage figure. It compares an **undiscounted** workforce flow with a
**present-value** pension cost; discounted to the same date the central case covers **54% or less**,
and the undiscounted convention flatters the bill. And the 18% replacement differential is **not
anchored** — the only published salary gap is 10.9%, where coverage is about **42%**.""",
    tag="06-q5-withhold")

rep("06-questions-and-answers.md",
"""On a
consistent recomputation the coverage ratio is **higher**, because both legs scale with acceleration
and this design accelerates 31% more.""",
"""On a
consistent recomputation the coverage ratio is **higher** on both measurements, because both legs
scale with acceleration and this design accelerates far more of it.""",
    tag="06-q5-direction")

# ----------------------------------------------------------------- 00
rep("00-cover-and-contents.md",
"""central assumptions it does **not** cover the pension cost — about **88%** of it on the undiscounted
comparison this package has always made, **54% or less** when the workforce flow is discounted to
the same date, and **negative** in the conservative case.""",
"""central assumptions it does **not** cover the pension cost — about **85% to 89%** of it on the
undiscounted comparison this package has always made, and **54% or less** when the workforce flow is
discounted to the same date. The per-case split is withheld in this version because two authorised
measurements of it disagree; document 04 §10 states both.""",
    tag="00-s3-withhold")

rep("00-cover-and-contents.md",
"""| **The workforce exchange in document 04 §10** | **Released, and the earlier statement of its direction is withdrawn.** Recomputed on the recommended design's own anchor and its own acceleration, the central case covers about **88%** — *higher* than the 71% printed before, not lower, because both legs scale with acceleration. What is worse is the pension cost per participant, by $7,135. Range **−18% to 213%**; **54% or less** on a discounted comparison. | — |""",
"""| **The per-case figures of the workforce exchange, document 04 §10** | `[WITHHELD — two authorised measurements disagree]`, on the cohort's mean acceleration (44.8516 against **42.8910** months) and most in the conservative case. **What both support is asserted:** central coverage of about **85% to 89%**, the optimistic case the only one that covers the cost, and **54% or less** on a discounted comparison. The earlier statement that the anchor error ran *against* the proposal is **withdrawn** — both measurements put the ratio *higher* than the 71% printed before; what is worse is the pension cost per participant, by $7,135. | Policy Director, with the Fiscal & Impact Modeler |""",
    tag="00-withheld-exchange-marker")

for d in DOCS:
    open(os.path.join(DST, d), "w", encoding="utf-8").write(buf[d])
print(f"part 5 OK — {len(applied)} edits applied")
for tag, doc in applied:
    print(f"  {tag:30s} {doc}")
