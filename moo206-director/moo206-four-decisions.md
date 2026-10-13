# MOO-206 — the four decisions on the `v2.1` pass, and three defects the live folder has that the report does not

**Policy Director, Virginia Policy Lab, 12 October 2026.** Answering the four questions on the
MOO-206 card. **Internal working draft. Pre-decisional. Not reviewed by counsel or by the Division of
Legislative Services.**

---

## 0. The four answers in one line each

1. **The dateline — re-date, and not to 69.** The bill is at **store revision 70**. A dateline states
   the revision at which the text was checked, so the package may not carry a revision it has not
   been checked at, and it may not carry two. **C2 is verified at 70 and holds, word for word — I ran
   the check myself** (§1). C2 re-dates at 70. **C1 may not**, until it is re-checked, because
   revision 70's only enacted change is inside the one subdivision C1 is about.
2. **The back-reference rule — confirmed, with one guard.** The 14-word phrase at all 88 sites would
   not be English and I am not asking for it. **But a back-reference may not be used in anything that
   can be lifted out alone.** I swept for those: **eleven occurrences in nine table rows** (§2).
3. **The lead-in — keep a lead-in, change these four words.** *"which the bill defines as"* is not
   accurate: the bill's definitions cite **§ 51.1-153 whole**, not *"A, B 2 or B 3"*. Replace with
   *"under the bill, reached through"* and carry a one-sentence note of the bill's actual words (§3).
4. **The remaining C-series — queued, commissioned, and not holding the freeze.** Ten items, drafted
   for approval the way C2 was, targeted at the next cut and not at this one (§4).

**And three things the live folder has that the report does not** (§5). The most serious: **document
05 reproduces bill text that revision 70 superseded**, so *"0 of 58 blocks divergent"* is no longer
true. **It is 2 of 58 at revision 70, and I have named both.**

---

## 1. Answer 1 — the dateline. Re-date at the live revision, after a check, and never carry two

### 1.1 The bill is at store revision 70, not 69

Store revision 70 landed on 13 October 2026 — the MOO-208 composite. The question as asked (*"keep 68
or re-date at 69?"*) was already out of date when it was asked, and the folder on disk already answers
it differently from the report: **`07-risk-register.md` §3.1 prints C2 at store revision 69**, not at
68, and the package carries **28** separate *"store revision 69"* datelines and **no** *"store
revision 68"* dateline at all.

### 1.2 The rule, which is the part worth keeping

**A dateline is a statement that the text was checked at that revision. It is not a label.** Three
consequences, and they are the standing rule from here:

- **The package speaks at one revision.** Mixed datelines in one package tell a witness that some of
  it was checked and some of it was not. That is worse than an old date.
- **Re-dating requires a re-check, not a find-and-replace.** Nobody may advance a dateline by editing
  the number.
- **The re-check belongs at the freeze, not at every revision.** Do not chase the bill mid-pass. The
  bill-dependent surface is re-verified **once**, at the moment the folder is frozen, against whatever
  is live then — and the frozen folder carries that revision.

### 1.3 C2 at revision 70 — checked, and it holds

I ran this rather than asking for it. Every string C2 quotes, counted over § 51.1-142.4 at store
revision 70:

| String as printed in C2 | at rev 69 | at rev 70 |
|---|---|---|
| *no amount shall be collected, offset, or withheld from any member, retiree, or beneficiary on that account* | 1 | **1** |
| *Nothing required or permitted by subdivision G 2* | 1 | **1** |
| *including any deferral of payment of a retirement allowance that subdivision G 2 requires until a determination under that subdivision takes effect* | 1 | **1** |
| *is a collection, offset, or withholding for the purposes of this section* | 1 | **1** |
| *no amount payable to the member or to any survivor, beneficiary, or estate of the member shall be reduced by reason of any such deferral or application* | 1 | **1** |
| **the struck string** — *is not a collection, offset, or withholding for the purposes of this section* | 0 | **0** |
| G 2's refund sentence — *shall pay a refund required by this subdivision within 60 days after the determination takes effect* | 1 | **1** |
| *interest*, anywhere in § 51.1-142.4 | 0 | **0** |

**And I checked what the two revisions actually changed, rather than inferring it from the quotation
counts.** Section 1 of the bill, diffed end to end:

- **68 → 69:** subsection A's exclusion sentence (the subsection L move), and three substitutions in
  **subdivision G 4's death branch** — Edit 1's *"the effective date of which the Board determines"*
  and Edit 3's confinement of the greater-of to coincident payees. **None of them touches the
  deferral clock, the 60/60/30/33 periods, subsection F, G 2's refund sentence, subdivision M 2, or
  subsection A's final interpretation paragraph.** G 4 is in C2's sources line, but what changed in
  G 4 is the death branch, and C2 does not state the death branch.
- **69 → 70:** the **title line**, and **subdivision D 1** — the beneficiary-designation advisory out
  of MOO-195 F9 and F4. Nothing else in the enacted text moved.

**So C2 re-dates at store revision 70.** No word of it changes.

### 1.4 C1 may not re-date until it is re-checked, and this is the reason the rule exists

**Revision 70's only enacted change is inside subdivision D 1. C1 is the item about subdivision D 1.**
C1 is in the register on disk at a revision-69 dateline, and revision 70 then:

- added four new matters to D 1's statement-content duty;
- added a carve-out to D 1's consequence sentence — *"other than a failure to state that the Board
  advises the member to review the member's designation of beneficiary"*; and
- extended D 1's subsection J reporting limb to the new failure.

C1's residual paragraph says *"nothing in the section attaches to a statement that omits those
matters."* **That survives at 70, but only on a distinction C1 does not draw**: D 1's consequence
sentence runs on the Board's **certification**, and C1's residual runs on the Board's **statement** of
qualifying retirement dates. A reader who has just read the new consequence sentence will challenge
the residual, and the entry has to answer that in its own words. The counts C1 prints do hold at 70 —
*"the report required by subsection J"* is still **14** in § 51.1-142.4, and *"for the purposes of
subsection M"* still **6** — so this is a completeness repair, not a correction.

**Direction.** C2 → **store revision 70**. C1 → re-verify at 70, make the statement/certification
distinction express, then date at 70. **If C1 cannot be re-verified before the freeze, it comes out
rather than going out at a stale date.**

---

## 2. Answer 2 — the back-reference rule. Confirmed, with a liftability guard

**Confirmed as written.** The phrase in full at the first class-1 site in each document, at any
class-1 site beside a differently-labelled cohort, and at any class-1 site carrying a headline figure;
a back-reference elsewhere. *"Cohort"* occurs 88 times and the 14-word phrase at all of them would not
be English. The judgment was right.

**One guard, and it is the whole of the change.** A back-reference is permitted **only where the full
phrase stands earlier in the same block or section, and that block always travels with it.** A
back-reference is **not** permitted in anything that can be lifted out alone — a table row or cell, a
caption, a chart or axis label, a slide title, or a line of an executive summary. These documents get
quoted a row at a time, and a row that reads *"refuses the most expensive 4.74% of the cohort"* on its
own names no cohort at all.

**Where it does not fit, the minimum is the identifier and not the routes:** *"the unreduced
subdivision A 1 cohort"*. **Never a bare *"the cohort"* or *"that cohort"* in a liftable site.**

**The sites this names — I swept for them rather than describing the rule and leaving it. Eleven
occurrences, in nine table rows, across six documents:**

| Site | As it reads now |
|---|---|
| `00-cover-and-contents.md` withheld-figures row | *"on **the cohort's** mean acceleration (44.8516 against 42.8910 months)"* |
| `00-cover-and-contents.md` ceiling row | *"it excludes 100% of **the cohort** the bill admits"* |
| `02-policy-brief.md` $170,000 ceiling row | *"Refuses the most expensive 4.74% of **the cohort** — about 1.2 of 20.65 members"* |
| `03-decision-memo.md` closed-item row **(two)** | *"refusing the most expensive 4.74% of **the cohort**"*; *"excludes 100% of **the cohort** the bill admits"* |
| `04-fiscal-analysis.md` row withdrawing $80,000 | *"$80,000 excludes 100% of **the cohort** the bill admits"* |
| `04-fiscal-analysis.md` row withdrawing the Plan 2 claim | *"Plan 2 members are 7% of **the cohort**"* |
| `05-bill-drafting-request.md` element 9 | *"it excludes 100% of **the cohort** the bill admits"* |
| `05-bill-drafting-request.md` closed-item row | *"it excludes 100% of **the cohort** the bill admits"* |
| `07-risk-register.md` **R-F** **(two)** | *"it refuses the most expensive 4.74% of **the cohort**"*; *"excludes 100% of **the cohort** the bill admits"* |

**One site I will not classify for you, because I am not sure and the register says say so.**
`07-risk-register.md` R1/F1/F2 reads *"the cohort was rebuilt monthly from membership histories"*. It
describes how the model's cohort was constructed rather than naming the cohort behind a figure, so it
may be no class at all. **Report it; do not guess it.**

**Two sites that are right as they are, and must not be swept with the others.** The shared headline
block's *"4.74% of that cohort"* back-references the full phrase eight lines above **in the same
quote-block, which never travels in halves** — leave it. And `04-fiscal-analysis.md` §13's *"$1,641,824
on that cohort"* back-references the **superseded** cohort named in its own row: putting the phrase
there would attach the authorised cohort's name to a figure that was not measured on it. **Leave it,
and do not let a sweep touch it.**

---

## 3. Answer 3 — the lead-in. Keep one; these four words are not accurate

**The reason for having a lead-in is right and I am keeping it.** Three of the five sites sit beside
the pre-existing words *"One pathway only"*, and without a lead-in the row reads as *only* those
routes — which is the expressio unius argument I reserved at item 47. **The lead-in stays.**

**But *"which the bill defines as"* says something the bill does not.** I read the two definitions at
revision 70:

> *"Qualifying retirement" means a service retirement **under § 51.1-153, or under subsection A or C of
> § 51.1-155.1**, …*
>
> *"Unreduced retirement eligibility date" means the earliest date on which the member may retire
> **under § 51.1-153, or under subsection A or C of § 51.1-155.1**, and receive a service retirement
> allowance that is calculated in accordance with **subdivision A 1 of § 51.1-155** and is not reduced
> under subdivision A 2 or A 3 of that section …*

**The bill cites § 51.1-153 whole. It never writes *"A, B 2 or B 3."*** That breakdown is our reading
of which routes inside § 51.1-153 can yield an allowance calculated under subdivision A 1 and not
reduced under A 2 or A 3. It is a good reading and I am not withdrawing it — but it is ours, and
*"which the bill defines as"* hands it to the bill. A witness asked *"where does the bill say B 2 or
B 3?"* would have to answer *"it does not."* **That is the one answer this package must never be made
to give.**

The § 51.1-155.1 limb is different and is safe: the bill's own definition carries the
involuntary-separation and lawfully-abolished-office condition in terms, so that part of the extended
form is the bill speaking.

**Direction — change four words at all five sites, and nothing else:**

> ~~which the bill defines as~~ **under the bill,** reached through § 51.1-153 A, B 2 or B 3, or, on an
> involuntary separation or a lawfully abolished office, through subsection A or C of § 51.1-155.1

The adopted words after the lead-in are untouched, no *"only"* appears, and neither § 51.1-155.1 B nor
§ 51.1-155.2 A is named. **Item 47 stays reserved to me.**

**And carry this note once per document, at the first extended-form site:**

> *The bill's definitions cite § 51.1-153 as a whole, and subsection A or C of § 51.1-155.1. The
> subdivisions of § 51.1-153 named here are the routes within that section that reach an allowance
> calculated under subdivision A 1 of § 51.1-155 and not reduced under subdivision A 2 or A 3.*

---

## 4. Answer 4 — the remaining C-series. Commissioned, and not holding the freeze

**They do not hold `v2.1`.** The published register is the R-series, which is complete in itself;
adding R-H for C2 is not a claim that the C-series is exhausted. Freezing with C2 and C1 in and the
rest queued misleads nobody.

**And they do not sit idle either.** C2 took a full approval cycle and the cycle earned its keep — the
register text that came in was **not quotable** against the bill. Ten more cannot be poured in on
trust. **Commissioned as a separate drafting pass, to the C2 discipline:**

- **The ten:** C4, C5, C6, C12, C13, C14, C15, C16, C17, C18.
- **Reconcile the register first.** C1 is now in, against a report that said it was not. **C3, C19,
  C20, C21, C22 and C23 are in the register and are not on anyone's list** — say for each whether it
  is must-appear, cured, retired or superseded, and name the authority. **Do not guess.**
- **Every quotation counted against the live bill** at the revision the entry is dated at, with the
  count printed. Not carried forward on trust.
- **Permissive framing throughout** — *the bar does not apply*, never *the Board must pay*.
- **Rank them, and tell me which cannot wait.** If any one of the ten is an exposure a committee finds
  on first reading, say so and I will take it into this cut. Otherwise they land in the next one.
- **Nothing is inserted before I approve the text.**

---

## 5. Three things the live folder has that the report does not — and one is a defect

The report is dated before the folder's last write. I checked the folder rather than the report.

### 5.1 Already done, and reported as open

- **C2 is at a revision-69 dateline on disk, with an expanded verification note** — not at 68 as
  reported. The dateline question had already been answered on disk, which is exactly why answer 1 is
  a rule and not a number.
- **C1 is in the register at §3.2** — reported as *"in no artifact."*
- **The two MOO-199 items are in.** 71% is printed only as what the package *"printed before"*, 88% is
  in document 04, and the direction sentence is expressly **withdrawn as to direction**. Reported as
  *"not mine to write"* and open.

**No criticism in any of that** — two passes were writing one folder. But it means the open list has
to be re-derived from the folder before the freeze, not from the report.

### 5.2 The defect: document 05 reproduces bill text that revision 70 superseded

The claim that document 05 is *"0 of 58 blocks divergent"* was true at revision 69 and **is not true at
revision 70**. Two blocks, both found by reading the file:

1. **The reproduced subdivision D 1 still carries *"that the member is advised to review the member's
   designation of beneficiary"*.** Revision 70 replaced that with *"that the Board advises the member
   to review…"*, added three further matters, and added the consequence carve-out. **The new wording
   appears nowhere in document 05.**
2. **The reproduced title line reads *"…pilot program; post-retirement employment; reports."*** Revision
   70's title line reads *"…pilot program; **death benefits; designation of beneficiary;**
   post-retirement employment; reports."*

**This is the standing cost of reproducing bill text, and it is why answer 1 puts the re-verification
at the freeze.** Re-transcribe both blocks at the live revision and re-run the full block comparison
before `VERSION.md` is written.

### 5.3 What the freeze gate is, then

**`v2.1` does not freeze until all five are done:**

1. the bill-dependent surface re-verified at one live revision, and every dateline set to it;
2. C1 re-verified at that revision or withdrawn;
3. document 05's reproduced blocks re-transcribed and the block comparison re-run to zero;
4. the nine liftable rows at §2 cured, and the one unclassified site reported;
5. the five lead-ins at §3 changed and the note carried.

Then `VERSION.md`, the `VERSIONS.md` row, and `CURRENT`. **The freeze is one pass's job and it is the
pass that owns the folder.**

---

## 6. Housekeeping I owe, from the report

**MOO-205 §0 points at §2.5 for its own approved text, which is at §2.4.** The report is right and the
error is mine. §2.4 was always the intent — the task description says §2.4 three times — and §2.4 is
what was applied. Corrected in my own document; no artifact read the wrong section.

**The departure from verbatim in C2 was correct.** *"and the memo should say so"* is an instruction to
the Editor, not a statement about the bill, and it has no business in a sponsor document. **Approved as
applied.** The same goes for narrowing the global cohort sentence to the figures it is actually true
of: the register's rule is per-site, 1.50× / 61% is labelled on the Pathways A + B cohort, and a global
claim that is false of four figures is worse than no claim. **Approved.**

---

## 7. Standing caveat

**Internal working draft material.** This document quotes working bill text, so the caveat travels with
it. This is **not** a Division of Legislative Services bill, it has **not** been reviewed or cleared by
counsel or by DLS, and nothing here is an opinion that any provision is legally sufficient for
introduction. Every figure, period and reading above is pre-decisional and internal, nothing here is
cleared for external use, and release is mine to decide.
