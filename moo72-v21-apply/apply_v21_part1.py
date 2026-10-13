#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 1 — the bill text moved, so these edits carry the text.

Run from this directory. Idempotent: it re-copies the ten markdown sources from v2.0
and applies every edit by exact-match assertion, so a silent miss is impossible.

Part 1 covers:
  1. The per-member ceiling is now IN the bill text at $170,000 (store revision 69);
     the `[$100,000]` bracket is gone. Ten lead blocks plus eight document sites.
  2. The mandated cohort phrase, swept verbatim into all ten through the shared lead block.
  3. The bill's section set: it now amends BOTH 51.1-142.2 and 51.1-162.
  4. Document 05 §4 re-transcribed whole from store revision 69.
  5. The store-revision numbering correction (there is no bill "revision 76").
  6. The version surface: 2.0 -> 2.1, 12 October -> 13 October 2026.
"""
import os, re, shutil, sys

SRC = "/Users/davidmoody/AgentCreated/v2.0/08-markdown-sources"
DST = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.join(HERE, "live-bill-rev69-working-draft.md")

DOCS = ["00-cover-and-contents.md", "01-one-page-summary.md", "02-policy-brief.md",
        "03-decision-memo.md", "04-fiscal-analysis.md", "05-bill-drafting-request.md",
        "06-questions-and-answers.md", "07-risk-register.md", "08-source-appendix.md",
        "09-sponsor-and-advocacy-plan.md"]

buf = {}
applied = []


def load():
    for d in DOCS:
        shutil.copy2(os.path.join(SRC, d), os.path.join(DST, d))
        buf[d] = open(os.path.join(DST, d), encoding="utf-8").read()


def rep(doc, old, new, count=1, tag=""):
    """Exact-match replacement. Dies if the old text is not present exactly `count` times."""
    n = buf[doc].count(old)
    if n != count:
        sys.exit(f"MISS [{tag}] in {doc}: expected {count} occurrence(s), found {n}\n---\n{old[:300]}\n---")
    buf[doc] = buf[doc].replace(old, new)
    applied.append((tag, doc, count))


def rep_all(old, new, tag="", docs=None):
    for d in (docs or DOCS):
        rep(d, old, new, 1, tag)


# The shared lead block is in nine documents. The one-pager carries only the
# recommendation sentence, so it takes the same two corrections at its own sites.
NINE = [d for d in DOCS if d != "01-one-page-summary.md"]


def save():
    for d in DOCS:
        open(os.path.join(DST, d), "w", encoding="utf-8").write(buf[d])


load()

# ---------------------------------------------------------------- 1 + 2
# The shared lead block, byte-identical in all ten. Two changes in one edit:
# the ceiling is in the text, and the mandated cohort phrase lands verbatim in all ten.
rep_all(
"""> would not advance the member's unreduced retirement eligibility date, and a **$170,000** per-member
> ceiling refuses the most expensive 4.74% of the cohort — and the bill still brackets `[$100,000]`,
> so the ceiling figure is directed but not yet in the text. On modelled demand, at the central""",
"""> would not advance the member's unreduced retirement eligibility date, and a **$170,000** per-member
> ceiling refuses the most expensive 4.74% of the cohort. **That ceiling is now in the bill text:**
> § 51.1-142.4 D 2 states it twice at store revision 69 of 13 October 2026, where the draft
> previously bracketed `[$100,000]`. The cohort behind every figure in this package is the unreduced
> subdivision A 1 cohort, reached through § 51.1-153 A, B 2 or B 3. On modelled demand, at the central""",
tag="lead-block-ceiling-and-cohort-phrase", docs=NINE)

# The one-pager's own cohort site, so the mandated phrase is verbatim in all ten.
rep("01-one-page-summary.md",
"""**18.4 elections** over the four years, range **9.2 – 30.7** — an **upper bound**, because a
further eligibility screen in the live draft is in no model run —""",
"""**18.4 elections** over the four years, range **9.2 – 30.7**, from the unreduced subdivision A 1
cohort reached through § 51.1-153 A, B 2 or B 3 — an **upper bound**, because a further eligibility
screen in the live draft is in no model run —""",
tag="01-cohort-phrase")

# ---------------------------------------------------------------- 1, document sites
rep("00-cover-and-contents.md",
"""| The per-member subsidy ceiling and the definition it is written on | **Decided at $170,000, and not yet in the text.** The board confirmed $170,000 on the reservation basis subsection D 2 certifies; the draft still brackets `[$100,000]` and the replacement is directed.""",
"""| The per-member subsidy ceiling and the definition it is written on | **Closed on the figure: $170,000 is in the bill text**, stated twice in § 51.1-142.4 D 2 at store revision 69 of 13 October 2026, on the reservation basis D 2 certifies. The `[$100,000]` bracket is gone. **What is still open is the "certified subsidy" definition the figure is written on** — document 07 at R-F.""",
tag="00-ceiling-open-item")

rep("01-one-page-summary.md",
"""  **$9,147** of excess, a factor of twenty. The bill still brackets `[$100,000]`; $170,000 is
  directed and not yet in the text.""",
"""  **$9,147** of excess, a factor of twenty. **The ceiling is now in the bill text** — § 51.1-142.4
  D 2, store revision 69 — where the draft previously bracketed `[$100,000]`.""",
tag="01-ceiling")

rep("02-policy-brief.md",
"""The bill still brackets `[$100,000]`; $170,000 is directed and not yet in the text. |""",
"""**The ceiling is now in the bill text** — § 51.1-142.4 D 2, store revision 69 of 13 October 2026 — where the draft previously bracketed `[$100,000]`. |""",
tag="02-ceiling")

rep("03-decision-memo.md",
"""| 2 | **Getting $170,000 into the text.** The ceiling figure is **decided: $170,000**, on the reservation basis subsection D 2 certifies, refusing the most expensive 4.74% of the cohort. The draft still brackets `[$100,000]`.""",
"""| 2 | ~~**Getting $170,000 into the text.**~~ **Closed: $170,000 is in the bill text**, stated twice in § 51.1-142.4 D 2 at store revision 69 of 13 October 2026, on the reservation basis D 2 certifies, refusing the most expensive 4.74% of the cohort. The `[$100,000]` bracket is gone. **What is still open is the definition the figure is written on** — document 07 at R-F.""",
tag="03-ceiling")

rep("04-fiscal-analysis.md",
"""the most expensive **4.74%** of it. Two caveats travel with that figure and both are required. First,
**the bill still brackets `[$100,000]`**; the replacement is directed and is not yet in the text.
Second, **a refusal is not a trim.**""",
"""the most expensive **4.74%** of it. Two things travel with that figure and both are required. First,
**the ceiling is now in the bill text:** § 51.1-142.4 D 2 states $170,000 twice at store revision 69
of 13 October 2026, where the draft previously bracketed `[$100,000]`. What is still open is the
*"certified subsidy"* definition the figure is written on, not the figure.
Second, **a refusal is not a trim.**""",
tag="04-ceiling-s7")

rep("04-fiscal-analysis.md",
"""2. **Getting $170,000 into the bill text** (§7). The figure is decided; the draft still brackets
   `[$100,000]`.""",
"""2. ~~**Getting $170,000 into the bill text**~~ **(§7) — closed.** § 51.1-142.4 D 2 states $170,000
   twice at store revision 69 of 13 October 2026 and the `[$100,000]` bracket is gone. The
   *"certified subsidy"* definition it is written on is still open.""",
tag="04-ceiling-s13")

rep("05-bill-drafting-request.md",
"""**The draft still brackets `[$100,000]`; replacing it is a drafting action that has not happened yet.**""",
"""**The draft now states $170,000 in the text** — § 51.1-142.4 D 2, twice, at store revision 69 of 13 October 2026 — and the `[$100,000]` bracket is gone.""",
tag="05-ceiling-element9")

rep("05-bill-drafting-request.md",
"""| 2 | **Writing $170,000 into the draft.** The draft reads `$[per-member subsidy ceiling]` and brackets `[$100,000]`. The figure is **decided: $170,000**, on the reservation basis subsection D 2 certifies. **$80,000 is withdrawn** — it excludes 100% of the cohort the bill admits. What is still open is the definition the figure is written on, which has three identified defects: a double count, no statutory standard for measuring acceleration, and no named obligor. | The figure is settled; the definition is not, and they have to be consistent. | Policy lead with counsel, at drafting |""",
"""| 2 | ~~**Writing $170,000 into the draft.**~~ **Closed on the figure.** § 51.1-142.4 D 2 states $170,000 twice at store revision 69 of 13 October 2026; neither the `$[per-member subsidy ceiling]` placeholder nor the `[$100,000]` bracket survives. **$80,000 remains withdrawn** — it excludes 100% of the cohort the bill admits. **What is still open is the definition the figure is written on**, which has three identified defects: a double count, no statutory standard for measuring acceleration, and no named obligor. | The figure is settled; the definition is not, and they have to be consistent. | Policy lead with counsel, at drafting |""",
tag="05-ceiling-open-decision")

rep("07-risk-register.md",
"""| **R-F** | **The per-member ceiling figure is decided at $170,000 and is not in the text.** What is still open is the "certified subsidy" definition it is written on: the definition carries a double count, no statutory standard for measuring acceleration, and""",
"""| **R-F** | **The ceiling figure is in the text; the definition it is written on is not settled.** § 51.1-142.4 D 2 states $170,000 twice at store revision 69 of 13 October 2026. What is still open is the "certified subsidy" definition it is written on: the definition carries a double count, no statutory standard for measuring acceleration, and""",
tag="07-RF-head")

rep("07-risk-register.md",
"""The figure is settled on the reservation basis subsection D 2 certifies — it refuses the most expensive 4.74% of the cohort. The draft still brackets `[$100,000]`; **$80,000 is withdrawn**""",
"""The figure is settled on the reservation basis subsection D 2 certifies — it refuses the most expensive 4.74% of the cohort — and it is now in the text; the `[$100,000]` bracket is gone. **$80,000 is withdrawn**""",
tag="07-RF-body")

# ---------------------------------------------------------------- 3, the section set
rep("00-cover-and-contents.md",
"subtitle: A sponsor package for the 2027 and 2028 sessions — amending Va. Code § 51.1-142.2",
"subtitle: A sponsor package for the 2027 and 2028 sessions — amending Va. Code §§ 51.1-142.2 and 51.1-162 and adding § 51.1-142.4",
tag="00-subtitle-section-set")

rep("01-one-page-summary.md",
"subtitle: A four-year capped pilot amending Va. Code § 51.1-142.2 for state agency employees",
"subtitle: A four-year capped pilot amending Va. Code §§ 51.1-142.2 and 51.1-162 for state agency employees",
tag="01-subtitle-section-set")

rep("05-bill-drafting-request.md",
"""An amendment to **Va. Code § 51.1-142.2**, plus a new **§ 51.1-142.4**, confined to prior
active-duty military service purchased by **state agency employees** in Plan 1 and Plan 2, that:""",
"""An amendment to **Va. Code § 51.1-142.2**, a conforming amendment to **§ 51.1-162** (death before
retirement), and a new **§ 51.1-142.4**, confined to prior active-duty military service purchased by
**state agency employees** in Plan 1 and Plan 2, that:""",
tag="05-requested-section-set")

# ---------------------------------------------------------------- 4 + 5, document 05 §4
live = open(LIVE, encoding="utf-8").read().rstrip() + "\n"
for must in ["### Title", "### Enacting clause", "### § 51.1-142.2.",
             "### <u>§ 51.1-142.4.", "### § 51.1-162.", "### Remaining enactment clauses"]:
    assert must in live, must
assert "[$100,000]" not in live
assert live.count("$170,000") == 2

NOTE = """> **This whole section is a transcription, not a draft produced here.** Everything below is
> reproduced verbatim from the drafting team's working bill text as it stands at **store revision 69
> of 13 October 2026** — the title, the enacting clause, both amended sections, the new section and
> all five enactment clauses. It supersedes the transcription carried in v2.0 of this package, which
> was taken from an earlier state of that document and is superseded in four ways a reader of v2.0
> needs to know about: the bill now also **amends § 51.1-162** (death before retirement), which v2.0
> did not carry at all; the **per-member ceiling of $170,000 is now in the text** at subdivision D 2,
> where the draft previously bracketed `[$100,000]`; the total normal cost rate is now the rate in
> effect **on the date the member filed the complete application** rather than on the date the Board
> accepts the election; and § 51.1-142.2's subdivision B 4 now carries a redetermination right, a
> no-accrual-after-the-valuation-date rule and a state agency payment policy that v2.0's text did
> not. **The contingency inside the cap is still bracketed** — `[20]` percent — and is an open
> figure.
>
> **One numbering correction, because v2.0 got it wrong.** v2.0 described its transcription as
> *"store revision 76"*. There is no bill store revision 76. That figure was the **Paperclip
> document revision number** of the bill-text document, which is a different counter from the bill's
> own *"store revision"* byline; the document counter stood at **88** when this transcription was
> taken and the bill's own byline read **store revision 69**. Everything in this version is dated to
> the bill's own counter. The authorised participant count was measured on the cohort machinery, not
> on a bill revision; what is still open about it is clause (viii) of *"eligible member"*, which is
> in this text and in no committed model run — see document 04 §13.
>
> **This remains an internal working draft and not a bill: it has not been reviewed or cleared by
> counsel outside this Lab or by the Division of Legislative Services, and only DLS drafts official
> Virginia bills.**

"""

c = buf["05-bill-drafting-request.md"]
i = c.index("### Title")
j = c.index("## 5. Open decisions in the draft")
buf["05-bill-drafting-request.md"] = c[:i] + NOTE + live + "\n---\n\n" + c[j:]
applied.append(("05-working-draft-retranscribed", "05-bill-drafting-request.md", 1))

# the old transcription note sat inside the block that was just replaced; prove it is gone
assert "working bill text at **store revision 76**" not in buf["05-bill-drafting-request.md"]
assert "whether it survives revision 76" not in buf["05-bill-drafting-request.md"]
# the only surviving mention is the numbering correction, which names the wrong figure to retire it
assert buf["05-bill-drafting-request.md"].count("store revision 76") == 2

rep("04-fiscal-analysis.md",
"""   which is in the live draft at revision 76 and in no committed model run. It is an additional""",
"""   which is in the live draft at store revision 69 of 13 October 2026 and in no committed model run.
   It is an additional""",
tag="04-revision-69")

# ---------------------------------------------------------------- 6, version surface
rep_all("· Version 2.0 · 12 October 2026", "· Version 2.1 · 13 October 2026", tag="version-surface")

save()
print(f"part 1 OK — {len(applied)} edits applied")
for tag, doc, n in applied:
    print(f"  {tag:40s} {doc}")
