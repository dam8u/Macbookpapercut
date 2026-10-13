#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 2 — MOO-199's workforce recomputation, MOO-202's C1 and C3,
and the registers that have to record what moved.

ADDITIVE: reads the current state of v2.1/08-markdown-sources and edits in place. It does
NOT re-copy from v2.0, because a second, unlocked run of this agent is writing the same ten
files and re-copying would destroy its work. Every edit is an exact-match assertion, so a
collision shows up as a MISS rather than as a silent overwrite.

Run part 1 first (it owns the ceiling, the bill-text re-transcription and the version surface).
"""
import os, sys

DST = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
DOCS = ["00-cover-and-contents.md", "01-one-page-summary.md", "02-policy-brief.md",
        "03-decision-memo.md", "04-fiscal-analysis.md", "05-bill-drafting-request.md",
        "06-questions-and-answers.md", "07-risk-register.md", "08-source-appendix.md",
        "09-sponsor-and-advocacy-plan.md"]

buf = {d: open(os.path.join(DST, d), encoding="utf-8").read() for d in DOCS}
applied = []


def rep(doc, old, new, count=1, tag=""):
    n = buf[doc].count(old)
    if n != count:
        sys.exit(f"MISS [{tag}] in {doc}: expected {count}, found {n}\n---\n{old[:300]}\n---")
    buf[doc] = buf[doc].replace(old, new)
    applied.append((tag, doc))


def save():
    for d in DOCS:
        open(os.path.join(DST, d), "w", encoding="utf-8").write(buf[d])


# ============================================================ MOO-199, the workforce exchange
# 02 §6 — the table and the direction sentence, on the recommended design's own anchor.
rep("02-policy-brief.md",
"""| Per participant | Conservative | **Central** | Optimistic |
|---|---:|---:|---:|
| Replacement salary differential | 8% | **18%** | 30% |
| Gross saving | $39,838 | **$72,437** | $111,555 |
| Recruitment and productivity ramp | −$29,010 | **−$26,400** | −$23,268 |
| **Net workforce effect** | **+$10,829** | **+$46,037** | **+$88,287** |
| Net cost to the trust per participating member — **repaired S1, not the recommended design** | −$64,678 | −$64,678 | −$64,678 |
| **Net effect on the Commonwealth** | **−$53,849** | **−$18,641** | **+$23,609** |

**At central assumptions the workforce effect covers about 71% of that cost, and no case we
regard as central covers all of it.** Break-even would need about 45 months of genuine
acceleration at an 18% differential.

**Two corrections travel with the $64,678, and the second makes this table less favourable, not
more.** It is **not** the pension cost of the purchased service: it is the net cost to the trust of
the whole election, of which only **28%** ($21,860) is service-credit content and **72%** ($54,891)
is the member commencing earlier. And it is **repaired S1's** anchor, not the recommended design's —
the recommended design costs **$71,813** per participant on the authorised basis, $7,135 more — so
**the exchange on the design this package actually recommends is worse than the rows above show.**
The recomputation on that anchor has not been produced by any source and is not attempted here.
Document 04 §9 carries the decomposition.""",
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
10.9% the workforce effect covers **42%**.

**And the correction to the figure this document printed before, stated plainly, because its
direction was wrong.** The 71% was measured against the original draft's **$64,678** anchor, not
this design's. On a consistent single-design recomputation the coverage **ratio is higher, not
lower** — about 88% against 71% — because both legs scale with acceleration and this design
accelerates 31% more of it. What is genuinely worse is the **pension cost per participant**, by the
**$7,135** between $64,678 and $71,813. Document 04 §10 carries the decomposition, the rung table
and the sources.""",
tag="02-s6-workforce")

# 00 §3, the no-savings-claim paragraph.
rep("00-cover-and-contents.md",
"""workforce value of an earlier, orderly retirement is real, it is quantified in document 04, and at
central assumptions it does **not** cover the pension cost.""",
"""workforce value of an earlier, orderly retirement is real, it is quantified in document 04, and at
central assumptions it does **not** cover the pension cost — about **88%** of it on the undiscounted
comparison this package has always made, **54% or less** when the workforce flow is discounted to
the same date, and **negative** in the conservative case.""",
tag="00-s3-coverage")

# 00's withheld table — the exchange is no longer withheld, and its direction is corrected.
rep("00-cover-and-contents.md",
"""| **The workforce exchange in document 04 §9** | Measured against the *original draft's* $64,678 per participant, not the recommended design's $71,813, so it **overstates** the exchange. | Fiscal & Impact Modeler |""",
"""| **The workforce exchange in document 04 §10** | **Released, and the earlier statement of its direction is withdrawn.** Recomputed on the recommended design's own anchor and its own acceleration, the central case covers about **88%** — *higher* than the 71% printed before, not lower, because both legs scale with acceleration. What is worse is the pension cost per participant, by $7,135. Range **−18% to 213%**; **54% or less** on a discounted comparison. | — |""",
tag="00-withheld-exchange")

# 04 §10 — the whole exchange section, restated.
rep("04-fiscal-analysis.md",
"""A participant who retires earlier is replaced by a less senior hire. The loaded salary differential
is real money; so is the cost of recruiting and ramping the replacement, and that cost is paid
first. Per participant, on the full-cohort acceleration of 34 months:

| Case | Replacement differential | Gross saving | Recruitment + ramp | **Net workforce effect** |
|---|---:|---:|---:|---:|
| Conservative *(leads)* | 8% | $39,838 | −$29,010 | **+$10,829** |
| **Central** | **18%** | **$72,437** | **−$26,400** | **+$46,037** |
| Optimistic | 30% | $111,555 | −$23,268 | **+$88,287** |

**And the honest conclusion, which is why no savings claim appears anywhere in this package:** the
cost set against the workforce effect on the same basis is **$64,678 per participant**, and its
identity is now **confirmed** — it is the same quantity as the scoreboard's cost per participant for
repaired S1, from the same run and the same field, reproducing to a tenth of a cent.""",
"""A participant who retires earlier is replaced by a less senior hire. The loaded salary differential
is real money; so is the cost of recruiting and ramping the replacement, and that cost is paid
first. **This table is measured on the recommended design at the authorised 12-month rung, with both
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
which side of it you are on.

**Three qualifications, each of which moves the answer further than any 10% move in any single
input.** (The largest single-input swing is 13.2%, on the replacement differential.)

1. **Undiscounted against present value.** The pension leg is a present value at 6/30/2025; the
   workforce leg is an **undiscounted** flow over a window that opens years later. Discounted at the
   model's own 6.75%, the central case covers **54.2%** rather than 88.5% — and that is an **upper
   bound**, because the true window opening is at or after the date used, so the discounted coverage
   is at or below 54%. **The undiscounted convention flatters the bill.** Every version of this
   package has made the undiscounted comparison, including the 71% printed before; which convention
   the package standardises on is a Policy Director decision and is not settled here.
2. **The 18% replacement differential is not anchored.** The only published salary gap available is
   **10.9%** — VRS valuation p. 50, average salary at ages 35–39 against ages 55–59 — and at 10.9%
   coverage is **42.4%**. The 18% is analyst judgment between two published anchors, and a reader
   who insists on published figures only gets 42%, not 88%.
3. **The acceleration is unsourced as a behavioural quantity.** The model measures how much earlier
   the design *permits* retirement. No published distribution of chosen retirement dates inside a
   VRS window exists, and the engine's own general-purpose default is **6 months** against the 44.9
   this cohort measures — 7.5× apart. The measured figure is the right one for this cohort; the gap
   is a reason to distrust the *level* of the workforce leg, not its sign.

**The one robust result: the exchange ratio is nearly invariant to the retirement rung**, because
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
in qualification 1.

**And the honest conclusion, which is why no savings claim appears anywhere in this package:** on
either convention the central case does not cover the pension cost, and the only case that covers it
is the optimistic one.

**What this section printed before, and why it changed.** The cost previously set against the
workforce effect was **$64,678 per participant**, and its identity is **confirmed** — it is the same
quantity as the scoreboard's cost per participant for repaired S1, from the same run and the same
field, reproducing to a tenth of a cent.""",
tag="04-s10-workforce")

# 04 §10, the S1 anchor paragraph: the direction correction.
rep("04-fiscal-analysis.md",
"""Second, **it is S1's anchor, not the bill's.** S1 is the drafted-at-approximate-normal-cost design
this package does **not** recommend. The recommended design's figure is **$71,813** per participant
on the authorised basis, and $64,678 is also a **6-month-deadline** figure where the authorised rung
is 12 months. **So the 71% below is measured against S1's cost, not against the recommended design's,
and the exchange on the recommended design is worse than this table shows** — the per-participant
cost is $7,135 higher. The recomputation on the recommended design's own anchor has not been
produced by any source and is not attempted here. At the central differential the workforce effect
covers about **71%** of S1's cost and no case covers all of it. Break-even would need about
**45 months** of genuine acceleration at an 18% differential.""",
"""Second, **it was S1's anchor, not the bill's.** S1 is the drafted-at-approximate-normal-cost design
this package does **not** recommend, and $64,678 is also a **6-month-deadline** figure where the
authorised rung is 12 months. The recommended design's figure is **$71,813** per participant on the
authorised basis. **The recomputation on that anchor has now been produced and is the table above.**

**One statement in the previous version of this package is withdrawn as to its direction.** It said
that the anchor error ran *against* the proposal and that the real exchange was *worse* than the
documents showed. On a consistent single-design recomputation the coverage **ratio is higher** —
88.5% against the 71% printed on S1's anchor — because both legs scale with acceleration: this
design accelerates **44.85** months against S1's **34.1**, so when the anchor rose 11.0% the
workforce leg rose 38.0%. What is genuinely worse is the **pension cost per participant**, by the
**$7,135** this document correctly named. **The superseded 71%, the superseded net effect of
+$46,037 and the superseded 45-month break-even are listed in §13 and must not be reprinted.**
**And one figure must never be printed at all:** dividing S1's workforce effect by this design's
anchor gives 64%, which pairs one design's workforce effect with another design's pension cost.""",
tag="04-s10-direction")

# The §13 withdrawal register.
rep("04-fiscal-analysis.md",
"""**What is withheld rather than withdrawn, and who closes it.**""",
"""| The workforce exchange printed on repaired S1's anchor — net effect **+$10,829 / +$46,037 / +$88,287** per participant, coverage **71%**, break-even about **45 months** | Withdrawn. The exchange is now measured on the recommended design's own anchor and its own acceleration (§10): **−$12,725 / +$63,531 / +$153,250**, coverage **88.5%**, break-even **49.90 months**. The two sets are not comparable — S1 accelerates 34.1 months and this design 44.85. |
| The statement that the $64,678 anchor error *"runs against the proposal"* and that the real exchange is *"worse than the documents show"* | **Withdrawn as to direction.** The coverage *ratio* is higher on a consistent recomputation, not lower. What is worse is the pension cost per participant, by $7,135. §10. |
| A coverage figure of **64%** — S1's workforce effect over this design's anchor | **Never printed and not printable.** It divides one design's workforce effect by another design's pension cost. §10. |

**What is withheld rather than withdrawn, and who closes it.**""",
tag="04-s13-register")

rep("04-fiscal-analysis.md",
"""| **The cost per participant for the recommended design used in the workforce exchange (§9)** | The exchange is still measured against **repaired S1's** $64,678 rather than the recommended design's $71,813, so it **overstates** the exchange. Not recomputed here. | Fiscal & Impact Modeler |""",
"""| **The cost per participant for the recommended design used in the workforce exchange (§10)** | **Released.** The exchange is recomputed on the recommended design's own anchor, $71,813, and its own acceleration; the earlier statement of the error's direction is withdrawn. §10 and §13. | — |""",
tag="04-withheld-exchange")

# 06 Q5.
rep("06-questions-and-answers.md",
"""**No, and the package does not claim it does.** At central assumptions the workforce effect is
worth **+$46,037** per participant after recruitment and ramp-up cost — a real number — against a
**net cost to the trust of $64,678 per participant**. That figure's identity is confirmed: it is the
same quantity as the scoreboard's cost per participant for the original draft. But it is **not** the
pension cost of the purchased service — only **28%** of it is service credit, and **72%** is the
member retiring earlier — and it is the **original draft's** figure, not the recommended design's.
The recommended design costs **$71,813** per participant, $7,135 more, **so the exchange on the
design we recommend is worse than the 71% suggests.** It covers about **71%** of the original
draft's cost and no case we regard as central covers all of it. Break-even would need about 45
months of genuine acceleration at an 18% replacement differential.""",
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
the only published salary gap is 10.9%, where coverage is **42%**.

**An earlier version of this answer printed 71% and said the exchange was worse than that on the
recommended design. The figure is superseded and the direction was wrong.** The 71% was measured
against the original draft's **$64,678** per participant — a confirmed figure, but that design's,
and only **28%** of it is service credit while **72%** is the member retiring earlier. On a
consistent recomputation the coverage ratio is **higher**, because both legs scale with acceleration
and this design accelerates 31% more. What is genuinely worse is the pension cost per participant,
by **$7,135**.""",
tag="06-q5-workforce")

# ============================================================ MOO-202 C1
rep("07-risk-register.md",
"""## 4. Resolved items, and how""",
"""### 3.2 C1 — a Board delay can reach credit the member bought with her own money

**Carry-through item C1, re-verified at store revision 69 (13 October 2026).** The mechanism and the
cure both hold at that revision; three citations in the previous statement of this item pointed at
the wrong text and are corrected here; and the residual has changed, so the old one is not reprinted.

Subdivision D 1 requires the member to file the § 51.1-153 notice of retirement no later than 30
days after the date on which the Board gives her the written statement of her earliest and final
qualifying retirement dates, and it provides that a notice filed after the effective date stated in
it is still good, *"subject to subsection E of § 51.1-153"* — which allows an effective date of
retirement no more than 90 days before the notice is filed. Read on that sentence alone, a Board
statement that arrives late enough could leave her unable to reach back to any effective date on or
before her final qualifying retirement date. Her retirement would then fail the definition of
*"qualifying retirement,"* and subdivision G 2 would cut her purchased credit back to what her own
payments would have bought at the ordinary price.

**The section cures it, in three parts.** D 1 extends her final qualifying retirement date by the
number of days by which the Board's statement or notice is late; it lets her state an effective date
no earlier than the first day of the month following the month in which the Board gives it; and it
requires the Board to state every such delay in the report required by subsection J. D 1 further
requires the Board to tell her, in the statement itself, that the extension operates, that she may
name the later effective date, that nothing prevents her from naming an earlier date to which she is
otherwise entitled, and that a mailed statement adds three days to every period that runs from it.
No case can be constructed in which a late statement alone defeats the definition.

**The residual is that the Board's notice duty carries no consequence.** Nothing in the section
attaches to a statement that omits those matters: an incomplete statement is not a reviewable
determination, and the extension keys on the statement being **late** rather than on its being
**incomplete**. That residual is open in the drafting file, with one self-enforcing sentence drafted
and not enacted.

**Two notes on citation, because the previous statement of this item got them wrong.** The 30-day
filing window is a free-standing sentence of **subdivision D 1**, not clause (ii) of D 1 — clause
(ii) is now part of the Board's statement-content duty, so the old citation points at the wrong
text. And the words *"the limitation in subsection E of § 51.1-153"* do not occur in the bill: the
text reads *"subject to subsection E of § 51.1-153."* The substance is unchanged and the 90-day
bound still binds, but the quotation is not available and is not printed. The extension is also no
longer in D 1's last sentence; it is cited here by content rather than by position.

**The subsection J limb is correct as written.** The subsection J that the board deleted on 11
October 2026 was the *backfill* provision; the renumbering that followed moved the Board's annual
report into subsection J, and *"the report required by subsection J"* occurs **14 times** in
§ 51.1-142.4 at store revision 69, twice inside D 1. Subsection J is the Board's annual report to
the Governor, the Department of Planning and Budget and the money committees, and it must state
every failure of the Board to make a determination, or to give a notice, within a period required by
the section, stated separately for each provision. That is the line this cure relies on.

**Sources.** § 51.1-142.4 D 1 and § 51.1-153 E, bill text **store revision 69** (13 October 2026);
red-team finding S-2. Every quotation above was re-checked against the live § 51.1-142.4 at that
revision, and the one quotation that failed the check is the one withdrawn in the paragraph above.

## 4. Resolved items, and how""",
tag="07-c1")

rep("03-decision-memo.md",
"""## 8. Decisions still needed""",
"""**R-I (carry-through item C1). A Board delay in stating the member's retirement window can reach
credit she bought with her own money — and the section cures it.** Subdivision D 1 requires her
notice of retirement within 30 days of the Board's written statement of her retirement dates,
subject to § 51.1-153 E's 90-day limit on back-dating; read alone, a late enough statement could
cost her the definition of *"qualifying retirement"* and send her purchase to the subdivision G 2
cutback. **The cure is in the text in three parts:** her final qualifying retirement date is
extended by the days the statement is late, she may state a later effective date, and the Board must
report every such delay in the report required by subsection J — and must tell her, in the
statement, how all of that works. **The residual is that the notice duty carries no consequence:**
nothing attaches to a statement that omits those matters, because an incomplete statement is not a
reviewable determination and the extension keys on lateness rather than on incompleteness.
**Mitigation:** ask the drafter for the self-enforcing sentence, which is drafted and not enacted.
Full text, citations and sources: **document 07 §3.2**.

## 8. Decisions still needed""",
tag="03-c1")

# ============================================================ MOO-202 C3
rep("04-fiscal-analysis.md",
"""5. **The official VRS cost statement.** Ours is an independent estimate and no amount of modelling
   substitutes for it.""",
"""5. **The official VRS cost statement.** Ours is an independent estimate and no amount of modelling
   substitutes for it.
6. **What share of the admitted cohort fails to retire inside the window.** Subsection G cuts back
   and refunds the purchase of a member who does not retire in a qualifying retirement. The
   post-purchase door distribution has been published and it closes one half of this question:
   **100%** of the expected participants reach an unreduced subdivision A 1 door and none reaches a
   reduced door, so subsection G 2 cannot fire on account of an admitted member landing at the wrong
   door — and that conclusion does not rest on the design assumption, because **the same cohort is
   already 89.26% unreduced with no bill at all**, which makes the design's marginal effect about 11
   points rather than 100. What subsection G actually fires on is a member **working past** her
   final qualifying retirement date, **retiring before** her earliest, or **separating without
   retiring**. That share is behavioural, is not modelled, and is **not bounded above**. **What
   would resolve it:** a behavioural retirement-date distribution for the admitted cohort, which no
   artifact in this file carries.""",
tag="04-c3-open-question")

rep("07-risk-register.md",
"""### Missing evidence
No official VRS quote for any member; no implementation estimate from VRS for the reservation
queue; no count of VRS members who are veterans with purchasable service; and no verified
enactment provenance for the South Carolina provision the fallback design is modelled on.""",
"""### Missing evidence
No official VRS quote for any member; no implementation estimate from VRS for the reservation
queue; no count of VRS members who are veterans with purchasable service; and no verified
enactment provenance for the South Carolina provision the fallback design is modelled on.

**And one piece of missing evidence that governs how this package is written.** Subsection G cuts
back and refunds the purchase of a member who does not retire in a qualifying retirement. The
published door distribution shows **100%** of expected participants reaching an unreduced
subdivision A 1 door and none reaching a reduced door — never to be cited without the **89.26%**
no-bill counterfactual beside it, which is what makes the design's marginal effect about 11 points
rather than 100. But the events subsection G 2 actually fires on are behavioural: working past the
final qualifying retirement date, retiring before the earliest, or separating without retiring.
**That share is unmodelled and unbounded above.** What has been published does not reach the
question. **So no document in this package states or implies that subsection G is an exception path,
a rare case, an edge case or a backstop, and no sentence leans on the share without naming it** —
*"most members will never see subsection G"* is the same claim in other words and is barred too.
What a document may say is that subsection G 2 cannot fire on account of an admitted member landing
at the wrong door, though the share who fail to retire inside the window for behavioural reasons is
not modelled.""",
tag="07-c3-language-rule")

# ============================================================ merge: the C2 dateline
# The concurrent run wrote §3.1 at store revision 68. Every quotation in it was re-checked
# against the live § 51.1-142.4 at store revision 69 in this run, so the dateline moves with
# the evidence rather than staying behind it.
rep("07-risk-register.md",
"""**Carry-through item C2, verified at store revision 68 (12 October 2026).** This is the text the
package prints for this item; it is reproduced from the Policy Director's approved wording.""",
"""**Carry-through item C2, re-verified at store revision 69 (13 October 2026).** This is the text the
package prints for this item; it is reproduced from the Policy Director's approved wording. Every
provision quoted below was re-checked against the live § 51.1-142.4 at store revision 69, including
subdivision G 4, which that revision amended in three places: every quotation holds verbatim, and
the word *"interest"* occurs **nowhere** in § 51.1-142.4, which is what makes the no-interest
statement a reading of the text rather than an inference.""",
tag="07-c2-dateline")

rep("07-risk-register.md",
"""*Periods stated here are read off the bill text at store revision 68 of 12 October 2026. The clock
convention in subdivision G 2 is under decision; the figure is anchored to a date the Board does not
choose and will not move, but the condition attached to it may change when that decision lands.*""",
"""*Periods stated here are read off the bill text at store revision 69 of 13 October 2026. The clock
convention in subdivision G 2 is under decision; the figure is anchored to a date the Board does not
choose and will not move, but the condition attached to it may change when that decision lands.*""",
tag="07-c2-footnote-dateline")

rep("07-risk-register.md",
"""paragraph of subsection A, bill text store revision 68 (12 October 2026); red-team findings m-2 and""",
"""paragraph of subsection A, bill text store revision 69 (13 October 2026); red-team findings m-2 and""",
tag="07-c2-sources-dateline")

# ============================================================ §14, the interactive model
rep("04-fiscal-analysis.md",
"""**It is withheld from this version, and the reason is the same rule that governs everything else
here.** Its data arrays are embedded at build time and they are the **superseded** family: the model
returns 18.9 participants and a $1,411,988 aggregate on every tab, against the 18.4 and $1,321,112
this document now prints. A reader moving its dials would get a second answer to every question the
documents answer. Re-emitting those arrays on the authorised basis is a model run, not an editorial
change, so it is commissioned rather than improvised. The file is kept, unaltered, at
`03-financial-model-interactive/superseded/`.""",
"""**It is withheld from this version too, and the reason has changed.** Its data arrays are embedded
at build time and they are the **superseded** family: the model returns 18.9 participants and a
$1,411,988 aggregate on every tab, against the 18.4 and $1,321,112 this document prints. A reader
moving its dials would get a second answer to every question the documents answer. **The authorised
data now exists** — the model's five data blocks were re-emitted on the authorised basis and are in
this folder at `05-model-code-and-data/` — but two things stop it being rebuilt in this version, and
neither is editorial. First, the **statutory-interest dial** is the one block that could not be
measured on the authorised basis: its figures away from 6.00% are derived by anchored rescaling, and
the modeller's own instruction is that this block must be re-measured before it ships. Second, every
row of that dial away from 6.00% carries the standing publication restriction on the S8 family's
comparative dollar figures, so **a live dial would publish restricted figures to anyone who moved
it** — it ships as a static 6.00% column or the restriction is lifted first, and that is a
publication decision, not a modelling one. The file is kept, unaltered, at
`03-financial-model-interactive/superseded/`.""",
tag="04-s14-interactive-model")

save()
print(f"part 2 OK — {len(applied)} edits applied")
for tag, doc in applied:
    print(f"  {tag:34s} {doc}")
