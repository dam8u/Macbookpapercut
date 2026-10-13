# MOO-213 — the verification the approval was conditioned on, and the re-base to store revision 72

**Editor · Virginia Policy Lab · 13 October 2026.** Carrying out the Policy Director's answers on the
MOO-213 approval card: the wording approval with seven stated checks, the C6 ranking with eight
implementation instructions, the C16 hold, the option (b) confirmation, and the §5.3/§5.4 disposition.

> **Internal working draft material. This document quotes working bill text, so the caveat travels
> with it. It is not a Division of Legislative Services bill, it has not been reviewed or cleared by
> counsel or by DLS, and nothing here is an opinion that any provision is legally sufficient for
> introduction. Pre-decisional and internal.**

**Nothing has been inserted into any artifact. The approval was conditional on verification; the
verification found corrections needed in five entries and one entry that must be held, so the
condition is not yet met for those six.**

---

## 0. The result in one line each

1. **The base moved under the approval.** You approved revision `57e14f7c` at revision-70 datelines.
   The live bill is at **store revision 72**. I re-ran all 66 strings at 72: **zero failures.** The
   entries re-date to 72 because the counts were re-printed and held, not because a number was
   edited. §1.
2. **Four of the ten pass every check clean** — C4, C5, C14, C15. §3.
3. **Five pass with a correction identified, which check 6 told me to identify rather than apply** —
   C6 (two), C12 (two), C13 (one), C16 (bookkeeping), C17 (one confirmation). §2.6, §3.
4. **One must be held: C18.** Its admission half silently broadens a claim pass 17 verified against
   **thirteen edits at store revision 52** into a whole-bill claim at revision 72. That is an
   eligibility claim — check 2's own category — asserted wider than its authority. §2.6.1.
5. **The C6 bill-text correction you ordered cannot be executed, and I am returning it under your own
   authorization.** No drafted cure exists for either occurrence; correcting them would cut off
   reinstatement for a member who **wins** on reconsideration or judicial review; and your check 6 is
   the thing that found it. **The $3,000,000 ceiling does not need the correction to hold.** §4.
6. **Your instruction 4 and instruction 6 are already satisfied by the enacted text, and I counted
   it.** A waiting-list placement reserves nothing, and the over-cap sentence is already wired into
   the subdivision D 3 funding confirmation. §2.4.
7. **Three of your rulings are recorded and one earlier binding is superseded by them.** §5.

---

## 1. The re-base, because the base moved under the approval

### 1.1 The two bases, side by side

| | Approved against | Live now |
|---|---|---|
| Store revision | **70** | **72** |
| Document revision | `d4a67d3d-30c4-4bad-b972-5b53f95cc44e` | **`368f5e41-56ab-4138-8bda-8553ae8eab04`** |
| Whole document | 515,219 chars | **502,586** |
| Enacted §1 | 132,557 chars | **134,012** |
| Enacted § 51.1-142.4 | 101,189 chars | **102,357** |

### 1.2 What I did about it, which is the one thing §1.3 of the drafted register said to do

**`moo213-c-series/count72.py`, output `out72.txt`: 66 strings, 0 assertions failed.** Every count the
ten entries assert at revision 70 also holds at revision 72 — including all four superseded
quotations still at **0**, and all six drafted cures still present.

**`count72.py` is `count70.py` re-pointed and nothing else.** The diff is confined to the header and
two run labels; not one counted string, asserted count or `where` is changed. `count70.py` stays in
the repo as the record of the revision-70 pass. **That is the rule you set on the freeze gate — never
advance a dateline by editing the number — applied to my own document.**

**The eight strings the proposed corrections introduce are counted separately**, in
`count72_addendum.py` / `out72_addendum.txt`, so that a new quotation can never ride in on the
re-base's clean result. All eight hold.

**Consequence for the datelines.** Every entry's dateline moves from *"store revision 70, 13 October
2026"* to **"store revision 72, 13 October 2026"**, and it moves because of `out72.txt`. This is the
one change I have made to approved wording without asking, because leaving a revision-70 dateline on
text to be incorporated now would be the defect the whole pass exists to prevent.

---

## 2. The seven checks, applied

### 2.1 Check 1 — does each entry reflect an already authorized policy decision?

**Method, because "confirm" has to mean something.** I pulled each source register as an issue
document — not from the repo copies — and **word-diffed each entry's memo-ready text against its
source**, printing every insertion, deletion and replacement. The tool is
`$PAPERCLIP_TASK_SCRATCH_DIR/diffcheck.py`; the output is `diffs.txt`.

| Entry | Source register, as an issue document | Diff result |
|---|---|---|
| C4 | MOO-111 `risk-section-carry-through-pass10` | 2 departures, **both already disclosed** in the entry's own "What changed" note, both counted |
| C5 | MOO-111, same | Wholly restated — the entry is now *cured*, which is the finding. Every quotation counted |
| C6 | MOO-111, same | Wholly restated. **Two accuracy defects found — §2.6.2, §2.6.3** |
| C12 | MOO-133 `risk-section-carry-through-pass12` | 6 departures; 4 disclosed, **2 not — §2.6.4, §2.6.5** |
| C13 | MOO-160 `risk-section-carry-through-pass17` | Wholly restated as cured. **One precision dropped — §2.6.6** |
| C14 | MOO-160, same | Wholly restated as cured. Both precisions carried in substance |
| C15 | MOO-160, same | Wholly restated as cured. All three bindings carried |
| C16 | MOO-160, same | Wholly restated as cured-in-part. **Binding bookkeeping — §2.6.7** |
| C17 | MOO-160, same | Wholly restated as cured. **One precision retired on my judgment — §2.6.8** |
| C18 | MOO-160, same | 14 departures; 12 disclosed or counted, **2 combine into a scope defect — §2.6.1** |

**No entry contains a finding, figure or fix that is not the originating agent's.** The six cured
entries are restatements of the originating agent's own finding against text that has since answered
it; the overtaking is reported with its count, and no analysis of mine is substituted.

### 2.2 Check 2 — which entries touch your six protected categories?

**None of the ten changes anything in any category.** All ten are memo risk-section prose. They
report findings and the text's response; they amend no provision. The useful answer to the check is
therefore which entries *describe* bill language in each category, because that is where a
mis-description does damage — and §2.6 is where I found two.

| Category | Entries that describe it | Note |
|---|---|---|
| **Eligibility** | **C5**, C17, **C18** | C5 is the admission rule; C18's first half is an express eligibility claim. **Both of the §2.6 scope problems are here** |
| **Survivor-benefit entitlements** | C13, C15, C18 | C13's modal case is a member who dies before retiring; C15's no-reduction limb names survivor, beneficiary and estate; C18 records that survivor benefits sit outside the model |
| **Payment recipients** | C4, C14, C15 | C4 is who gets paid and on whose discretion; C14 is whether the settlement limb runs at all; C15 is what the member is owed |
| **Statutory deadlines** | **C6**, C13, C14, C16, C17, C18 | C6's 15-day and trigger dates; C14's 60 days; C16's ninety-day notification period; C17's 90 days; C18's *absence* of a period |
| **Judicial-review rights** | **C6**, C14, C18 | **This is the finding at §4.** Both of C6's over-cap sites are reached through reconsideration under subsection M or judicial review |
| **Fiscal obligations** | **C6**, C12, C18 | C6's $3,000,000 control; C12's headroom and the bracketed contingency; C18's refund and arrears out of the trust |

**One entry in the package would change a protected category if the instruction attached to it were
carried out — C6, in two categories at once (judicial-review rights and fiscal obligations). That is
§4, and it is held.**

### 2.3 Check 3 — nothing substantive is treated as technical or conforming

Three places where the line was live, and how each is drawn:

1. **C16's surviving discretionary-waiver class** is recorded in the entry's own words as *"a policy
   choice, not a drafting defect."* Not conforming.
2. **C6's surviving limb.** Its remedy is a date the General Assembly has not set. The entry says
   *"the remedy, if the General Assembly wants one, is a date"* and supplies none. Not conforming —
   and this is why §4 returns it rather than drafting it.
3. **C12's bracketed contingency.** The bill reserves *"a contingency amount equal to `[20]` percent"*
   — count 1. The entry refuses to restate the per-member figure that rides on it. Resolving the
   bracket is a policy decision and is routed, not folded.

### 2.4 Check 4 — the $3,000,000 ceiling, and its distinction from VRS trust-fund obligations

**Finding: no entry conflates them, and no entry implies the ceiling extinguishes a benefit
obligation.** Checked against your ranking instructions 3, 4, 5 and 6, which is where the point bites.

**The distinction as the bill draws it, counted at revision 72:**

- The **$3,000,000** is a limitation on *amounts charged against it* — reservations, contingency
  amounts and settled subsidies. It is a Commonwealth subsidy control. Count of `$3,000,000`: **1**.
- The **trust** pays allowances, arrears, refunds and survivor benefits. The word `trust` appears
  **0** times in enacted § 51.1-142.4 — the obligations are imposed by Title 51.1 and by subsection N,
  **independently of this section's ceiling**, which is exactly your instruction 5.
- The entries that touch both say so: C13 distinguishes the retirement system not being paid from the
  reservation staying charged against the limitation; C18 names the refund and the arrears payment as
  **paid out of the trust**; C12 keeps cap utilisation and expected cost on opposite sides and its
  binding 3 forbids netting them.

**Your instruction 4 is satisfied by the enacted text and I counted it rather than assuming it.**
Subdivision D 5: where the amount available is insufficient, the Board places the application on a
waiting list and *"shall accept the election **if and when** sufficient amounts become available"* —
count **1**. **A waiting-list placement reserves nothing and charges nothing.** And *"A placement on
the waiting list under this subdivision is a determination of the Board for the purposes of
subsection M"* — count **1** — so the placement is reviewable, which reaches your instruction 6 too.
**No entry treats a placement as a commitment.**

**Your instruction 6's funding-confirmation procedure also exists, and the over-cap sentence is
already wired into it** — see §2.6.3, which is a correction *in the bill's favour*.

**One carry rule I am adding to the register rather than to any entry's prose**, because adding a
sentence to approved memo text is not mine to do:

> **CARRY RULE (new, from MOO-213 check 4).** No artifact may state or imply that the $3,000,000
> limitation caps, reduces or extinguishes any allowance, arrears payment, refund or survivor benefit.
> The limitation controls amounts charged against it. Benefit obligations are imposed independently by
> Title 51.1 and by subsection N and are not subject to it. Where an artifact names both in one
> passage it names which is which.

### 2.5 Check 5 — every previously approved safeguard, accounted for

**I counted the bindings in each source register and matched them one by one.** Four entries came
back with fewer than their source, and each had to be judged: *spent by the cure*, or *lost*.

| Source binding | Status | Where |
|---|---|---|
| C5 — no ordinal for the admission rule until MOO-112 is answered | **Carried** | entry binding 1 |
| C5 — the § 51.1-155.1 C sub-point is not a risk entry | **Carried** (added by me, kept) | entry binding 2 |
| C6 — may not imply the stripping or the restoration is rare; MOO-90 C3 hold binding | **Carried** | entry binding |
| C13 — p1, D 7's carve-outs do not save her | **Spent by the cure.** It was evidence for the defect; the counted carve-out strings survive in the table | — |
| C13 — p2, C7 is cured, C13 its successor, do not merge | **Carried** | entry precision |
| **C13 — p3, the permanent charge is headroom not a cost overrun, and no dollar figure attaches** | **DROPPED, and not spent** | **§2.6.6** |
| C14 — p1, both readings are defects; state the fork | **Carried in substance** — the entry states both limbs and closes both | prose |
| C14 — p2, do not say the Board "would obviously not pay" | **Carried** | entry precision |
| C15 — three bindings (attribution, the G 4 authority correction, not an attack on the member) | **All three carried** | entry bindings 1–3 |
| C16 — b1, may not say unproblematic / clearly constitutional / would certainly survive | **Carried, and now load-bearing** — your ruling 6 depends on it | entry, "the binding I am not touching" |
| **C16 — b2, "probably prevail" is the Red Team's litigation assessment, not legal advice** | **Nothing to bite on in the entry; must travel to the Red Team referral** | **§2.6.7** |
| **C16 — b3, this is the ONLY live constitutional surface pass 17 found** | **SUPERSEDED by your ruling 3** | **§5.2** |
| C16 — b4, do not write that § 51.1-156 H *permits* the Board to waive | **Carried** | entry, pass-12 ban |
| C17 — p1, it is *"may have disabled"*, keep the conditional | **Carried in substance** — the entry reads *"could once have required"* | prose |
| C17 — p2, do not say the confinement excludes people generally | **Carried** | entry precision 1 |
| **C17 — p3, the declined alternative cure and its ground** | **Retired on my judgment** | **§2.6.8** |
| C18 — five bindings | **All five carried** | entry bindings 1–5 |
| MOO-90 C3 hold | **Engaged and carried at C6, C12, C18**; counted 0/0/0 in the bill | §2.2 of the register |
| No-ordinal bar | **Not lifted anywhere** | C5, C12 |
| § 51.1-155.1 B and § 51.1-155.2 A not to be named; item 47 reserved | **Held. Zero occurrences in the drafted package** | re-checked this pass |
| C23 — no bare central cap utilisation figure without naming its ladder | **Held**; the 78.1872%/67.4% conflict stays routed to you | §2.2 of the register |

### 2.6 Check 6 — the conflicts, each with its number, exact wording and proposed correction

**This is the check that did the work. Eight items.**

#### 2.6.1 C18 — the admission half is asserted wider than pass 17 verified it. **HOLD**

**Number:** C18, memo-ready text, first paragraph. **Severity: this is the one I will not let through.**

**Pass 17's exact wording** (MOO-160 C18):

> Nothing in **the latest revision** lets one additional member into the program — and that half is
> independently verified. The reviewer checked every eligibility test, the purchase cap and the
> definition of an eligible member **against the thirteen edits** and found that none of them is
> touched…

**The drafted wording:**

> Nothing in **the bill as it stands** lets one additional member into the program — and that half is
> independently verified. The Lab's reviewer checked every eligibility test, the purchase cap and the
> definition of an eligible member and found that none of them is touched…

**Why it matters.** Pass 17 verified the admission half against **thirteen specific edits at store
revision 52**. Store revisions 53 to 72 have landed many more. The drafted form carries pass 17's
*"independently verified"* across to a **whole-bill claim at revision 72 that nobody has verified**,
and it is an **eligibility** claim — your check 2's first category. It is also the half that MOO-160's
binding 1 calls *"sound and independently verified"*, so the overstatement borrows that warrant too.
**I did not disclose this departure in the drafted entry; the diff found it.**

**Proposed correction — interim form, restoring pass 17's scope:**

> Nothing in the revision pass 17 reviewed lets one additional member into the program — and that
> half is independently verified. The Lab's reviewer checked every eligibility test, the purchase cap
> and the definition of an eligible member **against the thirteen edits before him** and found that
> none of them is touched…

**Proposed correction — the better form, and it is a commission not an edit.** Ask the Red Team to
re-verify the admission half **at store revision 72**. If it holds, the whole-bill sentence is
available and is worth more than the interim form. **I cannot supply that verification: it is a
finding, and findings are not mine.** C18 is in your *next* cut, so there is time for the real answer.

#### 2.6.2 C6 — the entry mis-describes which two sentences carry the over-cap command

**Number:** C6, memo-ready text, first paragraph, final sentence. **Exact drafted wording:**

> If the determination is later rescinded, the bill requires the Board to undo all of that and to
> charge the reinstated reservation against D 2 *"notwithstanding that the amount available to be
> reserved is thereby exceeded."* **So the cap can be exceeded by operation of the Board's own duty,
> and that command stands twice in the section.**

**The count of 2 is right. The characterisation is not.** The two sites are different sentences with
different mechanisms, and `count72_addendum.py` separates them:

- **Site 1** — the **death-release** limb: where an amount released on the member's death *"would not
  have been released had a determination of the Board been as it stands after reconsideration under
  subsection M or after judicial review"*, the Board reinstates it and *"the amount so reinstated
  shall be charged against the limitations in subdivision D 2 notwithstanding…"* — count **1**.
- **Site 2** — the **general reinstatement** sentence, with three triggers: a release made otherwise
  than in accordance with D 7, **or** a rescission, **or** a reversal or modification *"on
  reconsideration under subsection M or on judicial review"* — count **1**.

**The rescission story the entry tells is one trigger of one of the two sites.** Both sites are
reached through the member's own remedies, which is the fact §4 turns on.

**Proposed correction**, replacing the final sentence only:

> **So the cap can be exceeded by operation of the Board's own duty, and that command stands twice.
> Both sites are reinstatement sentences, and both are reached through the member's own remedies.**
> One restores a reservation released in error, or released where a determination is afterwards
> rescinded, or reversed or modified on reconsideration or on judicial review. The other restores an
> amount released on the member's death that would not have been released had the Board's
> determination stood as it does after reconsideration or judicial review.

#### 2.6.3 C6 — the disclosure package is materially larger than the entry states

**Number:** C6, memo-ready text, second paragraph, final sentence. **Exact drafted wording:**

> **On top of that the Board must notify the money committees of every reinstatement, of the excess
> and of its cause within 15 days, must state it in the annual report, and may accept no further
> election until the excess is eliminated.**

**Three controls in the live text are missing from that sentence**, each counted **1** at revision 72:

1. A **second** 15-day notice duty — to *"each applicant then on the waiting list maintained under
   subdivision D 5"*, carrying the fact, amount and date of the excess, the applicant's rights under
   § 51.1-142.2 B and the standard cost of the credit she could buy, *"which notice shall not state
   the cause of the release and shall not identify any member."*
2. A duty to *"request a confirmation under subdivision D 3 in respect of the amount of any resulting
   excess"* within 15 days — **the funding-confirmation procedure your instruction 6 named.**
3. A duty to *"certify the amount of the excess to the Governor and to those Chairmen as an amount
   necessary to fund the purposes of this section."*

And the money-committee notice carries **five** particulars, not two: the date of the release, whether
it was in accordance with D 7, the nature of any error, the amount of the excess, and its cause.

**This correction makes the exposure smaller, which is exactly why I am not applying it myself.**
Item 3 is the answer to your framing that the $3,000,000 is a binding limit on Commonwealth subsidy
commitments: **the excess is certified straight back to the Governor and the money committees as an
amount necessary to fund.** The bill's mechanism is not *breach the cap and absorb it* — it is
*breach, disclose twice, confirm funding, certify the shortfall to the General Assembly, and accept no
further election until it is cured.*

**Proposed correction**, replacing the final sentence only:

> **On top of that, no excess is absorbed — every one of them is routed back to the General
> Assembly.** Within 15 days of the reinstatement the Board must notify the money committee chairmen
> of the reinstatement, the date of the release, whether the release was in accordance with the
> release provision, the nature of any error, the amount of the excess and its cause, without
> identifying any member; must notify every applicant then on the waiting list of the fact, the amount
> and the date of the excess, of her rights under § 51.1-142.2 B and of the standard cost of the credit
> she is eligible to buy; must request a funding confirmation in respect of the amount of the excess;
> and must certify that amount to the Governor and to those chairmen *"as an amount necessary to fund
> the purposes of this section."* It must state every reinstatement and every excess in the annual
> report, and may accept no further election until the excess is eliminated.

**Consequence for the ranking, which is yours to take or leave.** C6 is still the one entry a
committee finds on first reading — the cap and the override are four subdivisions apart and no
arithmetic is needed. But with §2.6.2 and §2.6.3 in, **the answer in the room is much better than the
drafted entry gives it**, and that strengthens the case for taking C6 now rather than later. I am not
re-ranking; §3.1 of the drafted register stands.

#### 2.6.4 C12 — the model-side evidence was replaced with bill-side evidence

**Number:** C12, memo-ready text, first paragraph. **MOO-133's exact wording:**

> The model carries no non-completion parameter at all; **a search of its four input files for every
> form of the term returns nothing, and the assumption register has no entry for it.**

**The drafted wording:**

> The model carries no non-completion parameter at all, **and neither does the bill: the term appears
> nowhere in the section.**

**The claim is about the model. The evidence now offered is about the bill.** My count (`non-completion`
= **0** in § 51.1-142.4, re-verified at 72) supports the new half and not the original one, so as
drafted the model assertion travels with no verifiable support. MOO-133's evidence is not superseded —
it was simply dropped.

**Proposed correction:** restore it and keep both halves.

> The model carries no non-completion parameter at all — a search of its four input files for every
> form of the term returns nothing and the assumption register has no entry for it — and neither does
> the bill: the term appears nowhere in the section.

#### 2.6.5 C12 — a dropped provenance

**Number:** C12, memo-ready text, first paragraph. MOO-133 reads *"The rescue **added by card item
54** reaches a different and disjoint group"*; the drafted text reads *"The rescue reaches a different
and disjoint group."* **Proposed correction: restore "added by card item 54."** Minor, but it is a
citation shortened out of a line, which my own bar forbids.

#### 2.6.6 C13 — precision 3 dropped, and it is not spent by the cure

**Number:** MOO-160 C13 precision 3. **Exact source wording:**

> **The permanent charge against the $3,000,000 is the part a money committee hears.** It is not a
> cost overrun; it is headroom that can never be released. Pass 17 states it as a consequence of the
> bar, and no dollar figure is attached to it anywhere.

**Why it is not spent.** The cure closes the bar, but the drafted entry still *narrates* the permanent
charge as the old defect's consequence — *"the remainder of her reservation stayed charged against the
$3,000,000 cumulative limitation permanently."* The precision governs **how that is narrated** —
headroom, not overrun — and it carries a **no-dollar-figure rule** which is a standing safeguard. It
also sits directly on your check 4.

**Proposed correction:** restore it to the entry as a binding, in the source's own terms, with the
tense adjusted to the cure:

> **One binding carried from MOO-160 C13 precision 3.** Where this entry narrates the permanent charge
> against the $3,000,000, it is **headroom that could never be released, not a cost overrun**, and
> **no dollar figure is attached to it anywhere.**

#### 2.6.7 C16 — binding 2 has nothing to bite on in the entry, and must travel to the Red Team

**Number:** MOO-160 C16 binding 2 — *"'Probably prevail' is a litigation assessment of the Lab's Red
Team, not legal advice. It carries that attribution, and the standing caveat that counsel has not
cleared the proposal travels with it."*

**Not a defect in the entry**: the drafted C16 makes no litigation assessment, so the binding is
dormant. **But your ruling 5 commissions exactly such an assessment** — level of scrutiny, the
government's justification, and whether the remaining distinction is a material litigation risk.
**The binding therefore has to be carried into the referral, or it will be lost at the moment it
becomes live.** Done: it is written into the referral issue's description.

#### 2.6.8 C17 — precision 3 retired on my judgment, and that was not mine to do

**Number:** MOO-160 C17 precision 3. **Exact source wording:**

> **The alternative cure was considered and declined, and the ground for declining it is the thing
> this finding undermines.** Reverting the confinement to the single definition and amending the twin
> expressly was rejected in order not to reverse an earlier stated reasoning; the reviewer says that
> ground does not survive this scenario. If the memo gives a response column here, that is the honest
> one.

**The drafted entry retires it:** *"The limb that was enacted is the one the reviewer preferred, so
that disagreement is spent and the memo need not report it."*

**My reasoning is that the preferred cure is enacted, so the declined alternative is moot — and I
still think that is right.** But retiring a Red Team precision is the Red Team's call or yours, not
mine, and I recorded it as a conclusion rather than flagging it. **I am flagging it now. Confirm the
retirement, or I restore the precision.**

### 2.7 Check 7 — recorded in the register

Done, at §6 below and in the drafted register's §2.1, which is updated for: the revision-72 re-base,
your five rulings, the "Cured — Drafted" relabel, the C6 conditional classification, the C16 register
line in your words, and the new check-4 carry rule.

---

## 3. The ten, entry by entry

| Entry | Verdict | Next step |
|---|---|---|
| **C4** | **PASSES all seven checks.** Departures disclosed and counted; no safeguard lost | Clear for incorporation as **Cured — Drafted** |
| **C5** | **PASSES.** Option (b) confirmed and quotation-accuracy verified (§5.3); both bindings carried | Clear for incorporation as **Cured — Drafted** |
| **C6** | **PASSES on authority and safeguards; two accuracy corrections proposed** (§2.6.2, §2.6.3). **The attached bill-text instruction is returned** (§4) | Corrections need your nod, then **current cut** |
| **C12** | **Two corrections proposed** (§2.6.4, §2.6.5). All five MOO-133 bindings intact; no figure restated | Corrections, then **next cut** |
| **C13** | **One dropped safeguard to restore** (§2.6.6) | Restore, then incorporate as **Cured — Drafted** |
| **C14** | **PASSES.** Both precisions carried in substance | Clear for incorporation as **Cured — Drafted** |
| **C15** | **PASSES.** All three bindings carried verbatim in substance | Clear for incorporation as **Cured — Drafted** |
| **C16** | **PASSES as cured-in-part.** Binding 2 routed to the referral; binding 3 superseded by your ruling | Incorporate the cured part as **Cured — Drafted**; equal-protection question **pending the Red Team** |
| **C17** | **PASSES, with one confirmation needed** (§2.6.8) | Confirm the retirement, then **Cured — Drafted** |
| **C18** | **HELD.** Scope broadening on an eligibility claim (§2.6.1) | Interim correction, or commission the re-verification at 72. **Next cut either way** |

---

## 4. The C6 bill-text correction, returned under your own authorization

**Your ranking answer instructed me to "incorporate the C6 correction into the current statutory
working draft" and to "correct both occurrences of the disputed language." I am not doing that, and I
am returning it individually, which is the path your wording answer provides for.** Five reasons, in
order of weight.

**1. There is no C6 correction to incorporate.** MOO-99 finding S5 proposed **four** fixes. **All four
are enacted** — counted at revision 72 in `out72.txt`. **Not one of them touches the "notwithstanding"
clause.** The surviving limb's remedy is a date nobody has drafted; the entry says so in terms and
supplies none. Drafting one would be a new finding and a new policy decision, and it is also not my
work — bill text is the Drafting Specialist's.

**2. Correcting both occurrences would cut off a member who wins.** This is §2.6.2's finding and it is
the substance of the objection. **Both sites are reinstatement sentences reached through
reconsideration under subsection M and judicial review.** Remove or condition the override and the
result is: a member whose determination is reversed on reconsideration or on judicial review **cannot
have her reservation reinstated if the cap has filled in the meantime.** The same is true of the
estate of a member whose death-release should not have been made. **That converts a cap control into a
defeasance of the appeal right** — and it is the C14 and C15 family of defect, which the Lab found and
the bill cured, re-created from the other direction. Your check 2 names judicial-review rights and
survivor-benefit entitlements as protected categories; this reaches both.

**3. Your own instruction 6 is what found it.** *"Verify that the C6 correction does not contradict the
approved waiting-list, funding-confirmation, or reconsideration procedures."* **It contradicts the
reconsideration procedure**, directly and at both sites. I would not have looked there without the
instruction.

**4. The $3,000,000 ceiling does not need the correction in order to hold** — your instruction 3.
Counted at revision 72, the bill already: requires a **D 3 funding confirmation** on the amount of any
excess; **certifies the excess to the Governor and the money committee chairmen as an amount necessary
to fund the purposes of the section**; requires notice to the chairmen **and** to every waiting-list
applicant; states every excess in the annual report; and **bars accepting any further election until
the excess is eliminated.** The ceiling is not escaped — the shortfall is handed back to the body that
sets it. And instruction 4 is already satisfied: a waiting-list placement reserves nothing and the
election is accepted *"if and when sufficient amounts become available."*

**5. Instruction 5 points the same way.** *"Preserve existing benefit obligations imposed
independently by law; do not imply that the subsidy ceiling extinguishes those obligations."*
Correcting the override would make the ceiling do precisely that to a reinstatement owed after a
successful appeal.

**What I recommend instead, and it is a decision for you, not a draft from me.** Keep the override and
take the **corrected** C6 entry into the current cut, where the memo discloses the override, names both
sites, and states the full disclosure-and-funding machinery around them. **If you want an outer date on
the Medical Board certification limb** — the surviving unbounded trigger, which is the actual exposure
— that is a bounded, substantive drafting question for the Drafting Specialist and a policy decision
for you. **It is a different change from the one the instruction describes, and it does not touch
either over-cap site.** I have not opened it.

---

## 5. Your five rulings, recorded

### 5.1 Wording — approved subject to the seven checks

Recorded. **Four entries clear; five carry a proposed correction; one is held.** §3. **Nothing is
incorporated until the corrections are settled**, which is what "only after the following
verification" requires.

### 5.2 C16 — the hold approved

| Your instruction | Status |
|---|---|
| 1. Stop describing the C16 inversion as unresolved | **Done.** Register reads **Cured — Drafted** as to the inversion |
| 2. Hold the constitutional null-result paragraph out of the cut | **Done.** Not in any cut; recorded as withheld |
| 3. Do not reuse pass 17 §3.7's *"one constitutional question is live, and it is the one at C16"* | **Done.** And this **supersedes MOO-160 C16 binding 3**, which required that sentence to travel with the entry. Recorded as superseded on your authority — the only binding in the package retired by someone other than its author |
| 4–5. Refer the surviving discretionary-waiver class to the Red Team, with five named sub-questions | **Done** — referral issue created, all five carried verbatim, plus MOO-160 C16 binding 2 (§2.6.7) and the pass-12 *"permits"* ban |
| 6. Distinguish *the C16 defect was cured* from *no constitutional issue remains* | **Done.** The register carries both lines separately |
| 7. Preserve the corrected C16 language; do not reopen it | **Done.** Both cures counted **1** at revision 72; not reopened |
| 8. Register to read: C16 inversion cured; discretionary-waiver equal-protection question pending; constitutional null-result paragraph withheld | **Done**, in your words — §6 |
| 9. Return the Red Team's findings for disposition before any affirmative claim that the constitutional issue is resolved | **Set up.** MOO-213 is blocked on the referral so the verdict wakes me; no affirmative claim exists anywhere |

### 5.3 The "no *only*" rule — option (b) confirmed

Recorded as the approved disposition for **C5 and C17**. Your quotation-accuracy conditions, checked:

1. **Legal meaning and scope preserved.** The enacted sentence makes the separation or abolition a
   **necessary condition** of using the § 51.1-155.1 route. The entries state it as a requirement, on
   or before the date as of which the eligibility date is determined, and C17 carries the second limb
   fixing the date at the effective date of retirement. **Necessary condition in, necessary condition
   out.** Nothing is narrowed and nothing is widened.
2. **The enacted sentence is not altered.** It is not amended anywhere; it is cited by content.
3. **Retained fragments verbatim and not misleading out of context.** All of them are in `out72.txt`
   at their asserted counts. No retained fragment in C5 or C17 contains the word.
4. **The rule applied to proposed restrictive drafting language, not to source quotations.** Recorded
   as your reading, which is the one I drafted to.
5. **The two C18 uses retained — and I verified the attribution you conditioned them on.** Both are
   **verbatim pass 17**, in MOO-160's C18: *"the one change that narrows anything can only ever
   exclude"* in the memo-ready text, and *"on the death limb only"* in binding 2. Neither is about
   pathways; neither introduces a restriction. **Worth recording how this checked out:** both phrases
   appear **nowhere in the repo** outside my own document, because MOO-160's register lives only as an
   issue document. The repo would have said "unattributed."
   **One thing I checked and cleared.** Pass 14's **M-1** made a direction-of-effect claim in nearly
   these words — *"It can only exclude, never admit"* — and it was **struck and corrected at store
   revision 46** on the ground that the direction of effect "is not determinate on the face of the
   statute." **Different claim**: M-1 was about clause (ii)'s base specification and creditable
   service; pass 17's sentence is about one of the thirteen edits in front of it, and MOO-160 binding
   1 records that half as independently verified. **No conflict — but see §2.6.1, which is about the
   scope of that same sentence and is a real problem.**
6. Option (b) recorded as the disposition for C5 and C17. **Done.**
7. The underlying confinement policy decision is not reopened. **Confirmed — not touched.**

### 5.4 §8 — the five cured entries stay, individually

Recorded. **C5, C13, C14, C15 and C17 stay in §8 individually as cured, following C4 and MOO-111.**
Each keeps its identification, its original finding, its corrective language and its disposition. **No
summary paragraph replaces them.** The alternative single-paragraph form drafted at §5.3 of the
register is withdrawn and will not be used.

**On your label rule, and one thing I want to make sure you are choosing deliberately.** You directed
*"Cured — Drafted" unless the correction has been independently verified as incorporated into the
authoritative bill*, and *"do not mark an issue cured merely because corrective language has been
proposed."* **These cures are not merely proposed — they are in the working bill text and I counted
them twice, at revision 70 and again at revision 72.** But the count is *mine*, not independent, and
there is no DLS bill for anything to be incorporated into yet. **So I am applying your default label
with the basis attached**, which understates nothing and overclaims nothing:

> **Cured — Drafted.** The cure is enacted in the internal working draft at store revision 72
> (Editor's count, `out72.txt`); **independent verification pending**; no DLS bill exists.

**Say the word if you want the bare label instead**, and I will strike the parenthesis — but a bare
"Drafted" would read, to anyone who checks, as weaker than the text supports.

**§8 will distinguish three states, per your point 4:** *Cured — Drafted* (cure in the working draft,
verification pending) · *Must-Appear / Unresolved* (live defect) · *Must-Appear, patch-conditional*
(cure drafted but applied nowhere — C20 to C23).

### 5.5 C6's surviving limb — your conditional, applied

**Your test:** move it to §9 **only if** the bill no longer contains language that could authorize
reservations or Commonwealth subsidy commitments beyond the legally available amount.

**Applied: it does still contain that language.** *"Notwithstanding that the amount available to be
reserved is thereby exceeded"* — **count 2 at store revision 72**, both sites separately counted in
`out72_addendum.txt`.

**Therefore, on your instruction: C6's surviving limb is classified Must-Appear / Unresolved and does
not move to §9.** I am not downgrading a live fiscal-control defect to a discretionary question. **This
also disposes of §5.4 of the drafted register**, which asked the question and which your conditional
answers without my having to make the call.

**And C6's four enacted fixes are retained in §8 as cured** — *Cured — Drafted* — per the same answer.
**So C6 appears in §8 twice, in two states**, which is the honest shape and matches your point 4.

---

## 6. The register, as reconciled at store revision 72

**Changes from §2.1 of the drafted register. Everything else there stands.**

| Entry | Classification at store revision 72 | Verification | Authority |
|---|---|---|---|
| **C4** | **Must-appear, as cured — Cured — Drafted** | Passes all seven checks | MOO-111 / MOO-99 S1; re-counted at 70 and 72 |
| **C5** | **Cured — Drafted.** Option (b) is the approved disposition | Passes all seven checks | MOO-99 S4; live text at 72; Policy Director, MOO-213 ruling 4 |
| **C6 (cured limbs)** | **Cured — Drafted.** All four MOO-99 S5 fixes enacted | Counted at 72 | MOO-99 S5; live text at 72 |
| **C6 (surviving limb)** | **MUST-APPEAR / UNRESOLVED.** Not moved to §9: the over-cap language is still in the bill, count **2** | Two accuracy corrections proposed, §2.6.2 and §2.6.3 | Policy Director, MOO-213 ruling 5, conditional applied |
| **C6 (bill-text correction)** | **RETURNED, not executed.** No drafted cure exists; both sites are reached through reconsideration and judicial review | §4 | Returned to the Policy Director under MOO-213 ruling 1's hold authority |
| **C12** | **Must-appear. Live** | Two corrections proposed, §2.6.4 and §2.6.5 | pass 12 §4 via MOO-120 disposition §8 |
| **C13** | **Cured — Drafted** | One dropped safeguard to restore, §2.6.6 | pass 17 S-1 / item 114; live text at 72 |
| **C14** | **Cured — Drafted** | Passes all seven checks | pass 17 S-2 / item 115; live text at 72 |
| **C15** | **Cured — Drafted** | Passes all seven checks | pass 17 S-3 / item 116; live text at 72 |
| **C16 (inversion)** | **Cured — Drafted.** Both cures enacted | Passes; binding 3 superseded | pass 17 S-4 / item 117; live text at 72 |
| **C16 (equal protection)** | **PENDING — discretionary-waiver class referred to the Red Team** | Five sub-questions plus binding 2 carried | Policy Director, MOO-213 ruling 3 |
| **C16 (null-result paragraph)** | **WITHHELD from the cut.** Pass 17 §3.7's sentence is not to be reused | — | Policy Director, MOO-213 ruling 3, points 2 and 3 |
| **C17** | **Cured — Drafted** | Passes; one confirmation outstanding, §2.6.8 | pass 17 S-6 / item 119; live text at 72 |
| **C18** | **Must-appear. Live. HELD for scope correction** | §2.6.1 | pass 17 §4 and S-8 via MOO-152 disposition §4 |
| **C20–C23** | **Must-appear, patch-conditional.** Unchanged | Re-counted at 72, all hold | Unchanged |
| **C1, C2, C3, C7–C11, C19** | Unchanged | C2, C11, C19 and C3's three strings re-counted at 72, all hold | Unchanged |

**New standing rule, from check 4:** the $3,000,000-versus-trust carry rule at §2.4. It binds every
artifact and is not entry-specific.

---

## 7. What I need back

1. **The five proposed corrections** — C6 ×2 (§2.6.2, §2.6.3), C12 ×2 (§2.6.4, §2.6.5), C13 ×1
   (§2.6.6). All five are drafted in full and counted. **None requires a policy decision; all five
   change approved wording, which is why they are here rather than applied.**
2. **C18** — the interim scope correction, or the commission to re-verify the admission half at
   revision 72. **§2.6.1.**
3. **C17 precision 3** — confirm the retirement, or I restore it. **§2.6.8.**
4. **The C6 bill-text instruction** — returned at §4. If you still want the override touched after
   reading §4, that is a Drafting Specialist job and a policy decision, and I will carry whatever you
   decide.
5. **The "Cured — Drafted" label with its basis parenthesis** — confirm, or tell me to use the bare
   label. **§5.4.**

**Not waiting on anything else.** The re-base is done, the register is reconciled at 72, the Red Team
referral is live, and the four clean entries are ready the moment the package moves.

---

## 8. Standing caveat

**Internal working draft material.** This document quotes working bill text, so the caveat travels
with it. This is **not** a Division of Legislative Services bill, it has **not** been reviewed or
cleared by counsel or by DLS, and nothing here is an opinion that any provision is legally sufficient
for introduction. Only DLS drafts official Virginia bills. Every figure, period and reading above is
pre-decisional and internal, nothing here is cleared for external use, and release is the Policy
Director's to decide.
