# MOO-213 — the ten remaining C-series items, drafted for approval, and the register reconciled at store revision 70

**Editor · Virginia Policy Lab · 13 October 2026.** Answering question 4 on the MOO-206 card
(`moo206-four-decisions` §4, commit `06cd053`).

> **Internal working draft material. This document quotes working bill text, so the caveat travels
> with it. It is not a Division of Legislative Services bill, it has not been reviewed or cleared by
> counsel or by DLS, and nothing here is an opinion that any provision is legally sufficient for
> introduction. Pre-decisional and internal. Nothing below is inserted into any artifact.**

---

## 0. The answers in one line each

1. **Six of the ten are cured on the live text, and the register has them open.** C5, C13, C14, C15,
   C16 and C17 each proposed a drafted cure that the registers record as *"enacted nowhere."* **All
   six cures are in the bill at store revision 70**, counted at §4 below. C4 was already cured. **So
   three of the ten remain live: C6 (narrowed), C12 and C18.**
2. **Four register quotations are no longer available at all.** C13's settlement bar, C14's reversal
   duty, C15's arrears formula and C16's saving sentence were superseded by the very amendments that
   cured them. Printing them in quotation marks at a revision-70 dateline would repeat C2's defect
   exactly. **Counts: 0, 0, 0, 0** (§4).
3. **The ranking — one cannot wait, and it is not the one I expected.** **C6** is the exposure a
   committee finds on first reading: *"notwithstanding that the amount available to be reserved is
   thereby exceeded"* stands **twice** in the live text, against the one control the General Assembly
   holds. §3.
4. **A second urgency the card did not ask about, and I think it outranks the first.** The freeze gate
   would freeze a package asserting five defects the bill has closed. That is not an exposure a
   committee finds — it is one the Lab would be shown having made. §3.2.
5. **The six register entries nobody listed are classified, with authority named for each** — C3
   live-as-a-language-rule, C19 must-appear, C20 to C23 must-appear and patch-conditional. §2.2.
6. **Four things I will not classify, and I am reporting them rather than guessing.** §5. One of them
   is a standing instruction of yours that collides with a quotation I cannot shorten.

**Nothing is inserted. Every entry below is text submitted for approval.**

---

## 1. The basis, and what "counted" means here

### 1.1 One base, stated on its face

Everything is read off the live issue document
[`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) on [MOO-42](/MOO/issues/MOO-42):

| | |
|---|---|
| Store revision | **70**, byline *"store revision 70 · 13 October 2026"* |
| Document revision | `d4a67d3d-30c4-4bad-b972-5b53f95cc44e` |
| Whole document | **515,219** characters |
| Enacted §1 | **132,557** characters |
| **Enacted § 51.1-142.4** | **101,189** characters |

Code strings are counted against the [MOO-210](/MOO/issues/MOO-210) `law.lis.virginia.gov`
retrievals of §§ 51.1-153, 51.1-155, 51.1-155.1, 51.1-156 and 51.1-124.3, not against the bill, and
every such row is labelled **CODE**.

### 1.2 The method, because the method is the whole point of this pass

**Every string any of the ten entries puts inside quotation marks was counted on the live text.
Nothing is carried forward on trust from MOO-90, MOO-111, MOO-133, MOO-160, MOO-172 or MOO-202.**
**66 strings counted; every asserted count holds.** The script and its output are in the repo at
`moo213-c-series/count70.py` and `moo213-c-series/out70.txt`, and they are re-runnable against any
later base.

Three rules the counting followed:

- **Counts are over enacted § 51.1-142.4 unless the row says otherwise.** Whole-document counts are
  inflated by the §0 revision narratives, which quote the operative strings; enacted §1 is inflated
  by §§ 51.1-142.2 and 51.1-162, the title and the enactment clauses. Rows that must be counted over
  enacted §1 — the two enactment-clause strings in C6 — say so.
- **A superseded quotation is counted and printed at 0, not quietly dropped.** Four of them are the
  substance of finding 2 above. A reader of this document can see what the register used to say and
  that it is no longer there.
- **The drafted cures were counted as *absent*, which is what the registers assert.** Six of those
  assertions failed. That is how the six cures were found; it was not inferred from anything.

### 1.3 One dateline, and it says what it means

**Every entry below carries exactly one dateline, and it states the revision the text was checked at:
store revision 70, 13 October 2026.** No entry carries two, none carries a figure checked at another
revision, and no dateline here was reached by editing a number. That is answer 1's rule applied.

**If the base moves before you approve this, the entries do not re-date by assertion.** Re-run
`count70.py` against the new base; the entries re-date when the counts are re-printed and hold.

---

## 2. The register, reconciled

### 2.1 The whole roll, C1 to C23

**Every status is the originating agent's or the Policy Director's, except the eight rows marked
*"this pass"*, which are mine on the live text and are evidenced at §4.**

| Entry | Classification at store revision 70 | Authority |
|---|---|---|
| **C1** | **Must-appear. In the register on disk at §3.2, at a revision-69 dateline.** Re-verify at 70 and make the statement/certification distinction express, or withdraw | Policy Director, MOO-206 §1.4. Not re-drafted here — the direction is the Director's and the re-verification is a separate job |
| **C2** | **Must-appear. Re-dated at store revision 70, word for word** | Policy Director, MOO-206 §1.3, who ran the check |
| **C3** | **Live, and it is not a §8 entry.** A prohibition on language, plus one §9 open question in its narrowed form. The hold lifted **in part** | Policy Director's MOO-90 C3 hold, partially lifted by the Drafting Specialist at MOO-202 §4 on MOO-88's published distribution. §2.2 below |
| **C4** | **Must-appear, as cured.** Unchanged | MOO-111 / MOO-99 S1; re-counted **this pass** |
| **C5** | **CURED this pass.** MOO-99 S4's alternative fix is enacted, section-wide | MOO-99 S4's own words; the live text at revision 70, **this pass** |
| **C6** | **Must-appear, and materially narrowed this pass.** All four drafted fixes are enacted; one unbounded limb survives | MOO-99 S5; the live text at revision 70, **this pass** |
| **C7** | Cured; successor is C13 | pass 17 §5 q2 |
| **C8** | **Retired.** Replaced by C19 | Policy Director, MOO-165 §3 |
| **C9** | Cured as to the late filer; replaced by C16 | pass 17 §5 q4, S-4 |
| **C10** | Cured in principle; the defects in the enacted cure were C14 and C15 | pass 17 S-2, S-3 |
| **C11** | Cured and verified | MOO-172 §1, Editor's check at store revision 57; re-counted **this pass** (2 sites) |
| **C12** | **Must-appear. Live, and its per-member arithmetic sits on a bracketed figure** | pass 12 §4 via MOO-120 disposition §8; the bracket found **this pass** |
| **C13** | **CURED this pass.** Pass 17's one-amendment cure is enacted, both limbs | pass 17 S-1 / item 114's drafted cure; the live text at revision 70, **this pass** |
| **C14** | **CURED this pass.** The conditioning clause and the referent correction are both enacted | pass 17 S-2 / item 115; the live text, **this pass** |
| **C15** | **CURED this pass.** The net formula and the entirety limb are both enacted | pass 17 S-3 / item 116; the live text, **this pass** |
| **C16** | **CURED this pass as to the inversion.** Both cures enacted. One narrower class survives | pass 17 S-4 / item 117; the live text, **this pass** |
| **C17** | **CURED this pass.** The second limb fixing the date is enacted | pass 17 S-6 / item 119; the live text, **this pass** |
| **C18** | **Must-appear. Live, and one of its three routes is now bounded** | pass 17 §4 and S-8 via the MOO-152 disposition §4; the narrowing found **this pass** |
| **C19** | **Must-appear.** Carry its four bindings verbatim | Policy Director, MOO-165 §3.2. Holds at revision 70 — counted **this pass** |
| **C20** | **Must-appear, patch-conditional** | Policy Director, MOO-162 disposition §5, re-affirmed at MOO-177. Unapplied at 70 — counted **this pass** |
| **C21** | **Must-appear, patch-conditional, and written conditionally on a cure enacted nowhere** | Policy Director, MOO-162 disposition §5; MOO-172 §3. Counted **this pass** |
| **C22** | **Must-appear, patch-conditional, at net +42** | The board's `to-120` answer, 12 October 2026; MOO-176 revision 6; Policy Director's MOO-176 disposition; MOO-177 |
| **C23** | **Must-appear, patch-conditional, with the §2.1 utilisation hold still open** | MOO-163's released price; MOO-170; Policy Director's MOO-179 cap decision (declined); MOO-172 §3 |

**The §8 inventory this leaves:** C1 (on re-verification), C2, **C4 as cured**, C6, C12, C18, C19, and
C20 to C23 grouped and labelled as a patch. **C5, C13, C14, C15 and C17 come out of §8 and go into the
cured record; C16 goes in in a narrowed form.** C3 stays a language rule plus the §9 question.

### 2.2 The six the card named, each answered in its own terms

**C3 — live, must-appear as a language rule, and it is not a §8 risk entry.** It was never one. It is
(i) a prohibition: no artifact may call subsection G an exception path, a rare case, an edge case or a
backstop, and no sentence may lean on the share of members who reach it without naming that share;
and (ii) one §9 open question. **The ground of the prohibition changed and the restated rule says so:**
it is no longer *"nothing is published"* but *"what has been published does not reach the question."*
MOO-88 published the door distribution, which closes the door-driven limb; the behavioural limb is
unmodelled and unbounded above. **Authority: the Policy Director's MOO-90 C3 hold, lifted in part by
the Drafting Specialist at MOO-202 §4 on MOO-88's figures. Counted this pass: *"exception path"* 0,
*"backstop"* 0, *"rare"* 0 in enacted § 51.1-142.4 — the bill does not use the register's banned
vocabulary of itself, so the prohibition binds our prose and nothing else.**

**C19 — must-appear, and it holds at revision 70.** S-5 / §7 item 118: an uncapped
disability-application pendency lets one member occupy the cap and freeze the queue. **I counted the
limb the entry turns on.** Clause (ii) of G 4 caps the aggregate non-running *"by reason of
applications for a disability retirement allowance filed after the first such application"* at 120
days — **count 1** — so **the first application's pendency carries no cap**, which is the whole of
C19's mechanism. The bar on determining and noticing while such an application is pending is also
live — **count 1**. **Authority: Policy Director, MOO-165 §3.2, with its four bindings carried
verbatim, including that it is not netted against C12 or C18.**

**C20 — must-appear, patch-conditional, and the patch is applied nowhere at revision 70.** Edit 2's
FIND string *"no later than 15 days after it acts upon the request"* is **count 2**; its READ string
*"no later than 15 days after it gives its decision upon the request"* is **count 0**. **A bare count
of 2 is not a defect and must not be read as one:** the two sites are the definition's backstop-notice
sentence, which is Edit 2's target, and subdivision M 2's application duty, which Edit 2 does not
reach. Anyone re-running this count needs that sentence with it. **Authority: Policy Director, MOO-162
disposition §5, re-affirmed through the MOO-177 amendment.**

**C21 — must-appear, patch-conditional, and still written conditionally.** M 2's reconsideration
deadline is a duty to **act** — *"The Board shall act upon a request for reconsideration within 90
days"*, **count 1** — and there is still no duty to give a decision. The deemed-denial cure the entry
is written conditionally on is enacted nowhere. **Authority: Policy Director, MOO-162 disposition §5;
MOO-172 §3, which records that C21 is the one entry in the register whose risk is conditional on a
cure.**

**C22 — must-appear, patch-conditional, at net +42 and not net −48.** Edit 3's FIND string *"retains
its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"*
is **count 1**, and its READ string *"until 120 days after the Board acts upon the request"* is
**count 0**; Edit 1's operative clause is **count 0**. The patch is applied nowhere. **The net −48, the
48-days-before and the 63-day counterfactual stay retired, and the 63-day ban is permanent.**
**Authority: the board's `to-120` answer at 14:15 on 12 October 2026; MOO-176 revision 6; the Policy
Director's MOO-176 disposition, which re-derived the figures from the store; MOO-177.**

**C23 — must-appear, patch-conditional, and its §2.1 hold is still open and still routed to you.**
Clause (ii) is live in the form that carries precision 8's window — *"the aggregate of all tolling
under this subsection shall not exceed 120 days, excluding any period after the expiration of the 90
days allowed by this subsection and before the Board acts upon the request, provided that the
aggregate of all periods so excluded shall not exceed 90 days"*, **count 1**. **The held item is
unchanged: central cap utilisation appears in the package at 78.1872% and in C23's source at 67.4%,
and choosing between them is a basis decision, not an edit.** Until you answer, C23's sentence uses
67.4% and attributes it, and no artifact states a bare central cap utilisation figure without naming
which ladder it sits on. **Authority: MOO-163's released price; MOO-170's chaining price; the Policy
Director's MOO-179 cap decision, declined, whose §6 line travels only with the displacement rise;
MOO-172 §2 and §3.**

---

## 3. The ranking — what cannot wait

### 3.1 One of the ten is an exposure a committee finds on first reading: **C6**

**C6, and of the three live entries it is the one a committee finds by reading the bill rather than by
reading our fiscal work.**

The reason is two words of enacted text and a count. **Subdivision D 2 states the one control the
General Assembly holds** — the Board shall not accept an election if the total *"would exceed
$3,000,000"*, **count 1**. **Subdivision G 4 then commands the Board to breach it:** the reinstated
reservation *"shall be charged against the limitations in subdivision D 2 **notwithstanding that the
amount available to be reserved is thereby exceeded**"* — **count 2** in enacted § 51.1-142.4.

A money-committee staffer reads the cap, reads the subdivision that overrides it, and asks the
question in the room rather than in a letter. **No arithmetic is needed to find it and no model is
needed to state it.** C12 and C18 are serious and both are must-appear, but a committee reaches them
through the fiscal impact statement, not on first reading.

**My recommendation: take C6 into the current cut.** It is ready below, it is counted, and its
disclosure story is strong — which is the second reason to take it now rather than later: **the
answer to it is in the bill**, and we should be the ones who say so.

**C12 and C18 land in the next cut.** Neither is softened for it and neither is held: C12 is a
cap-headroom finding whose figures are routed to the Fiscal & Impact Modeler and are not restated
here, and C18 is scored at zero by construction and carries no dollar figure.

### 3.2 A second urgency the card did not ask about, and I think it outranks the first

**The freeze gate would freeze a package asserting five defects the bill has closed.** C5, C13, C14,
C15 and C17 are in the register as open, with cures *"enacted nowhere."* **All five cures are in the
live text.** C16's inversion is closed too.

That is not an exposure a committee finds. **It is an exposure the Lab is shown having made** — five
open legal defects asserted against a text that answers every one of them, each with the Lab's own
drafted cure sitting in the bill. A witness handed the live § 51.1-142.4 and our risk section at the
same time would not need a second question.

**And one consequence reaches a sentence that is already approved.** Pass 17 §3.7's null-result
paragraph says *"One constitutional question is live, and it is the one at C16."* **On the live text
C16's inversion is cured, so that sentence is no longer accurate as written.** The narrower class that
survives (§4, C16) may or may not carry the same constitutional weight — **that is the Red Team's
judgment and yours, and it is not mine to make.** I have flagged it at §5 rather than re-cutting an
approved sentence.

**What I am asking for, concretely:** approve the six cured entries in the form below so the register
stops asserting them, and let me take **C6** into the current cut with them. The remaining two live
entries, C12 and C18, go into the next one.

---

## 4. The ten entries, drafted for approval

**Reading rule for every entry.** The **dateline** states the revision the text was checked at. The
**count table** prints every string the entry quotes, with its count on the live text, so the next
reader re-runs rather than trusts. **Permissive framing throughout:** where a bar is lifted the entry
says *the bar does not apply*, and no entry says the Board must pay. **Neither § 51.1-155.1 B nor
§ 51.1-155.2 A is named anywhere below. Item 47 is reserved to you and no entry below reaches it.**

---

### C4 — the settlement operator. **Must appear, and must appear as cured**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| *may be settled* — the drafted defect | **0** | § 51.1-142.4 |
| *the certified subsidy for the election is settled under this subdivision* | **1** | § 51.1-142.4 |
| *the certified subsidy is settled* — the operator family | **4** | § 51.1-142.4 |

**Memo-ready text** (one sentence changed from MOO-111's, marked):

> **One word in the draft would have made the Commonwealth's payment of a named member's subsidy a
> standardless Board discretion, and the review process caught it.** The disability-rescission clause
> as drafted said the certified subsidy *"may be settled"* — where every other settlement operator in
> the section is automatic, *"is settled."* Read on that word, a member whose purchased credit the
> Board had restored could be given the credit and refused the subsidy, leaving the retirement trust
> carrying the unfunded difference. **It is enacted as an automatic operator**: on the live text the
> certified subsidy *"is settled"* in every one of the four places the section settles one, and the
> permissive form appears nowhere. The defect was found by the Lab's tenth adversarial pass and
> closed in the next drafting revision; the memo reports it because the reader should know what the
> passes are for.

**What changed from MOO-111's text, and why.** MOO-111's sentence read *"It is enacted as *is
settled*."* **I have not changed the substance; I have changed it to a form that is true of the whole
operator family and is counted.** The bare quotation *"is settled"* has 13 occurrences in the section
and most of them are not the operator — so a reader who re-ran MOO-111's check on the bare string
would get an unhelpful number. The counted claim is the one in the table.

**Citation to carry:** § 51.1-142.4 G 4's rescission-settlement limb and the comparator operators in
G 1, G 4 and D 3, **bill text store revision 70 (13 October 2026)**; MOO-99 finding **S1**, via
[MOO-111](/MOO/issues/MOO-111).

**Record, not for the memo.** The Red Team's recommended fix was the single word `shall`; the drafter
enacted the section's own automatic operator instead, which is uniform with the rest of the section.

---

### C5 — the admission rule. **CURED. My recommendation is that it moves to the cured record**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| *"Unreduced retirement eligibility date" means the earliest date on which the member may retire under § 51.1-153, or under subsection A or C of § 51.1-155.1* | **1** | § 51.1-142.4 |
| *"Qualifying retirement" means a service retirement under § 51.1-153, or under subsection A or C of § 51.1-155.1* | **1** | § 51.1-142.4 |
| The enacted confinement — *For the purposes of this section the member may retire under subsection A or C of § 51.1-155.1 … on or before the date as of which the member's unreduced retirement eligibility date is determined* | **1** | § 51.1-142.4 |
| MOO-99 S4's fix in its **definition-only** form, *For the purposes of this definition, the member may retire under subsection A or C …* | **0** | § 51.1-142.4 |
| *who is involuntarily separated from state service* | **1** | **CODE** § 51.1-155.1 A |

**Memo-ready text, as cured:**

> **An ambiguity in who gets into the pilot was the one open question that could have moved a cost
> figure, and the text now closes it.** The bill lets the § 51.1-155.1 involuntary-separation and
> abolished-office routes satisfy its retirement tests. On the reading the package is priced on, those
> words admit nobody new: § 51.1-155.1 A reaches a member *"who is involuntarily separated from state
> service"*, every test in the bill is applied while the member is still in service, and so the words
> do no work. **A second reading was available and it moved admission in both directions** — the
> definition asks for *"the earliest date on which the member may retire"*, a forward projection, and
> nothing in it said which facts were projected and which were held fixed. Project the separation too,
> and a long-service senior employee at the top of the salary distribution could fall out of the
> priced pool while a shorter-service colleague fell into it.
>
> **The bill now confines the route in terms, and the confinement runs across the whole section.** It
> requires that the member **have incurred** the involuntary separation, or that the office **have
> been** lawfully abolished, on or before the date as of which her unreduced retirement eligibility
> date is determined — and, where the sentence is applied otherwise than in determining that date, on
> or before her effective date of retirement. **A separation that has not happened cannot be
> projected, so neither direction of the ambiguity survives.** The Red Team's own alternative cure is
> what was enacted, in a section-wide rather than a single-definition form. **No admission quantity
> moves and no priced figure moves on this account**: the confinement restates § 51.1-155.1's own
> conditions and admits nobody.

**Citation to carry:** § 51.1-142.4, the definitions of *"qualifying retirement"* and *"unreduced
retirement eligibility date"* and the confinement and residual sentences that follow the latter, **bill
text store revision 70 (13 October 2026)**; § 51.1-155.1 A, retrieved from `law.lis.virginia.gov`,
[MOO-210](/MOO/issues/MOO-210), 12 October 2026; MOO-99 finding **S4**, via MOO-111, whose alternative
fix wording this entry reports as enacted.

**Response column, where the memo gives one:** the cure costs nothing and removes the exposure
entirely, because the words it confines did no work on the reading the package is priced on.

**Two bindings that survive the cure.**

1. **The no-ordinal bar is not lifted.** No artifact states an ordinal for the admission rule among
   the model's drivers until [MOO-112](/MOO/issues/MOO-112) is answered. The cured entry carries no
   ordinal.
2. **The § 51.1-155.1 C sub-point is still not a risk entry.** Whether that subsection reaches anybody
   — a constitutional officer may not be *"a state employee"* — is a moderate drafting sub-point the
   Red Team asked to be confirmed against § 51.1-124.3, and it stays out of §8.

---

### C6 — the cap and the report. **Must appear, and it is materially narrower than the register has it**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| *notwithstanding that the amount available to be reserved is thereby exceeded* | **2** | § 51.1-142.4 |
| *would exceed $3,000,000* / the D 2 limitation | **1** | § 51.1-142.4 |
| **Fix 1, enacted** — *upon an application filed no later than the date on which the determination took effect* | **1** | § 51.1-142.4 |
| Second trigger limb — *upon an application the filing of which did not require a waiver of a ninety-day notification period set forth in subsection A or B of § 51.1-156* | **1** | § 51.1-142.4 |
| Third trigger limb — *upon an application as to which the Medical Board has made a certification described in clause (ii) of subsection H of § 51.1-156* | **1** | § 51.1-142.4 |
| The disclosure duty — *to the Chairmen … no later than 15 days after the reinstatement, which notice shall not identify any member* | **1** | § 51.1-142.4 |
| *shall state every reinstatement and every such excess in the report required by subsection J; and shall accept no further election until the excess is eliminated* | **1** | § 51.1-142.4 |
| *an excess is eliminated when the aggregate of the amounts charged against the limitation in the first sentence of subdivision D 2 no longer exceeds that limitation* | **1** | § 51.1-142.4 |
| **Fix 2, enacted** — *the number of determinations rescinded and the service credit restored under subdivision G 4* | **1** | § 51.1-142.4 |
| **Fix 2, enacted** — *every amount by which a reservation reinstated under subdivision G 4 caused a limitation in subdivision D 2 to be exceeded* | **1** | § 51.1-142.4 |
| **Fix 3, enacted** — *and (b) the date of the last rescission under subdivision G 4 that has occurred on or before the date stated in clause (a)* | **1** | § 51.1-142.4 |
| Fix 3 in **MOO-99 S5's own words** — *until the first December 1 following the later of that date and the date of the last rescission under subdivision G 4* | **0** | § 51.1-142.4 |
| **Fix 4, enacted** — *and to make every refund, payment, notice, determination, rescission, restoration, and reinstatement required by § 51.1-142.4* | **1** | **enacted §1**, third enactment clause (i) |
| **Fix 4, enacted** — *the reporting and evaluation duties in subsection J … shall continue in effect until the last report and evaluation required by that subsection has been submitted* | **1** | **enacted §1**, clause (iii) |
| *good cause shall exist and the Board shall waive such ninety-day notification periods* | **1** | **CODE** § 51.1-156 H |
| *certifies that: (a) the disability and its cause existed on the date the member's employment was terminated* | **1** | **CODE** § 51.1-156 H clause (ii) |

**Memo-ready text, restated at revision 70:**

> **A member whose purchased credit was stripped can have the whole thing restored, and the
> restoration reinstates her reservation over the $3,000,000 limit.** Subdivision D 2 is the one
> control the General Assembly holds: the Board may not accept an election if the total *"would exceed
> $3,000,000."* If a member misses her retirement deadline the Board cuts her credit back and releases
> her reservation. If the determination is later rescinded, the bill requires the Board to undo all of
> that and to charge the reinstated reservation against D 2 *"notwithstanding that the amount
> available to be reserved is thereby exceeded."* **So the cap can be exceeded by operation of the
> Board's own duty, and that command stands twice in the section.**
>
> **Three of the four problems the review found are now answered in the text, and the memo should say
> so.** The trigger no longer runs without limit for the ordinary case: the rescission is keyed to an
> application *"filed no later than the date on which the determination took effect."* The annual
> report now states the rescissions, the service credit restored, and *"every amount by which a
> reservation reinstated under subdivision G 4 caused a limitation in subdivision D 2 to be
> exceeded."* The report's end date no longer falls before the restoration: it runs to the later of
> the settlement date and *"the date of the last rescission under subdivision G 4."* And the enactment
> clause that keeps the charging regime alive after the section expires now names rescission,
> restoration and reinstatement expressly, and keeps the subsection J duties in effect until the last
> report has been submitted. **On top of that the Board must notify the money committees of every
> reinstatement, of the excess and of its cause within 15 days, must state it in the annual report,
> and may accept no further election until the excess is eliminated.**
>
> **What survives is one limb of the trigger, and it is the limb that carries no date.** Two further
> routes into rescission were added with the bounded one. One reaches an application whose filing
> required no waiver — bounded by the Code's own ninety days. The other reaches an application on
> which the Medical Board has certified that the disability and its cause existed at termination and
> that the member could not have known of them. **Section 51.1-156 H is mandatory once that
> certification is made** — *"good cause shall exist and the Board shall waive such ninety-day
> notification periods"* — and nothing in either the Code or the bill puts an outer date on when the
> certification may come. So an over-cap reinstatement remains reachable years after the member left
> state service, now with full disclosure attached to it. **The exposure is a dated one and the
> remedy, if the General Assembly wants one, is a date.**

**Permissive framing, stated because this entry is where it bites.** The bill lifts a bar and commands
a charge; it does not command a payment to this member out of an exceeded cap. **Write *the cap may be
exceeded* and *the no-release rule does not apply*; never *the Board must pay over the cap*.**

**Citation to carry:** § 51.1-142.4 D 2, G 2, G 4's reinstatement, disclosure and trigger sentences,
and subsection J 1, with the third enactment clause of the bill, **all verified at bill text store
revision 70 (13 October 2026)**; § 51.1-156 A, B and H, retrieved from `law.lis.virginia.gov`, MOO-210,
12 October 2026; MOO-99 finding **S5**, via MOO-111. **MOO-99's four fix formulations are reported here
as enacted and are no longer quoted as proposals** — three are enacted in the drafter's words rather
than the reviewer's, and the reviewer's own wording of fix 3 counts 0 and must not be printed as
enacted.

**Response column:** the disclosure, the report, the report's tail and the post-expiry machinery are
all in the text; what is open is a date on one limb of the trigger.

**One binding carried from MOO-111.** This entry may not imply that the stripping provision, or the
restoration, is rare. **The MOO-90 C3 hold is engaged and binding**, and this entry complies by
attaching no share to either.

---

### C12 — the fiscal shape: it is the **cap** that moves, not the cost. **Must appear**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| *$3,000,000* | **1** | § 51.1-142.4 |
| *a contingency amount equal to `[20]` percent of that certified subsidy* | **1** | § 51.1-142.4 |
| *non-completion*, in any form | **0** | § 51.1-142.4 |
| *shall recertify the certified subsidy to reflect the service credit so credited* — the enacted C11 repair | **2** | § 51.1-142.4 |
| *to complete payment by the completion date* — D 7's carve-out | **2** | § 51.1-142.4 |

**Memo-ready text** (MOO-133's, with two precisions added and no figure changed):

> **The provision that rescues the member who could not finish paying is cheap in expected dollars and
> expensive in headroom, and the model prices neither — because it has no parameter for the population
> the provision reaches.** Everything the package says about this exposure runs through one
> assumption: the share of members who fail to **retire** on time. The rescue reaches a different and
> disjoint group — members who fail to **complete payment**. The model carries no non-completion
> parameter at all, and neither does the bill: the term appears nowhere in the section. **So this
> exposure is currently scored at zero by construction, not by evidence and not by law.**
>
> **What the arithmetic shows, on the model's own published per-member figures, is that the binding
> constraint is the $3,000,000 cap and not the cost.** The model already reports that if every exposed
> reservation were recalled, cumulative charges would reach **$2,885,518 — 96.2 percent of the
> $3,000,000 limitation** — leaving **$114,482** of headroom. Each recalled member carries **$117,392**
> including the contingency the bill requires. **So about one more recall exhausts the headroom, and
> one recall is a 5.3 percent non-completion share.** At that share worst-case cap utilisation goes
> from 96.2 percent to **100.0 percent**; at 10 percent it is 103.4 percent; at 25 percent it is 114.2
> percent. **The expected cost over the same range stays trivial — about $1,800.**
>
> **Five caveats travel with every one of those numbers.** They are **worst-case** utilisation — every
> exposed reservation recalled — not central; they sit on top of a central retirement-failure
> assumption that is itself graded analyst judgment; and **the 5.3 percent non-completion share is
> assumed, not measured. The Lab has no evidence for that rate in either direction**, on a
> twelve-month instalment purchase the bill allows the Board to extend to thirty-six months.
> **Two further conditions are on the bill's side of the line and are new to this statement. The
> contingency the per-member figure includes is a bracketed drafting figure in the text, not a settled
> one** — the bill reserves *"a contingency amount equal to `[20]` percent of that certified
> subsidy"* — **so the per-member amount moves with whatever the bracket resolves to.** And **the
> per-member figures predate the repair that now recertifies the certified subsidy down to the service
> credit actually credited**, which bears on the amount settled and therefore on the amount charged.
> **This arithmetic is the adversarial review's, computed on the fiscal model's published output. It is
> not a model re-run and no re-run is claimed to have happened.** The re-run, with a non-completion
> parameter added, is commissioned.

**What I added, and what I refused to do.** I added the two conditions in the final paragraph, both
counted above. **I did not restate a single figure.** The bracket and the recertification repair both
bear on the per-member amount, and restating it would be supplying a fiscal figure. **The drafter
declined to restate these figures and routed them to the Fiscal & Impact Modeler; pass 17 did the
same; so do I.** If you want the figures re-derived, that is a commission to Fiscal and not an edit
here.

**Citation to carry:** pass 12 **§4** (Red Team / Counsel Reviewer, [MOO-120](/MOO/issues/MOO-120)), as
adopted and routed in the MOO-120 disposition **§8**; the underlying published figures from the Fiscal
& Impact Modeler's [MOO-108](/MOO/issues/MOO-108) run — `out_moo108_cap.csv` and
`out_moo108_summary.json`; the contingency, the **$3,000,000** limitation and the completion window
from § 51.1-142.4 D 2 and D 3, subsection E and § 51.1-142.2 B 4 f, **verified at bill text store
revision 70 (13 October 2026)**; the recertification repair is the enacted C11 cure, counted above.

**The five bindings from MOO-133 are carried unchanged, and the first is not negotiable.**

1. **ATTRIBUTION.** The 5.3 percent, the $117,392, the $114,482, the 100.0/103.4/114.2 percent and the
   $1,800 are the **adversarial review's**, never the Fiscal & Impact Modeler's. Fiscal published the
   $2,345,615.91 charge, the 78.2 percent utilisation, the $2,885,518 worst case, the 96.2 percent, the
   $449,918 recallable pool and the $8,572 expected recall PV. Everything beyond those is the review's
   arithmetic on an assumed share.
2. **Every figure carries its range or its assumption, in every artifact including the one-pager.**
3. **The two sides may not be netted.** The $1,800 without the cap, or the cap without the $1,800, is
   half the finding.
4. **MOO-90's C3 hold is engaged.** The entry complies by naming the share as assumed and unmeasured,
   and must keep naming it.
5. **The no-ordinal bar has nothing to bite on here** and is not lifted.

---

### C13 — the settlement bar. **CURED. And the register's quotation of it is no longer available**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| **The bar as cured** — *No certified subsidy is settled under this subdivision after the reservation for the election has been released **in full** in accordance with subdivision D 7 **and has not been reinstated under this subdivision**, or after a determination … has taken effect **and has not been rescinded, reversed, or modified*** | **1** | § 51.1-142.4 |
| **The bar as pass 17 quoted it** — *…released in accordance with subdivision D 7 or after a determination under subdivision 2 or 3 has taken effect* | **0** | § 51.1-142.4 |
| *the service credit to be purchased is reduced to the amount the member may purchase as recertified* | **1** | § 51.1-142.4 |
| *if a recertification under subdivision 6 reduces the certified subsidy* | **1** | § 51.1-142.4 |
| *as though the determination had not been made* | **1** | § 51.1-142.4 |
| The reinstatement route — *Where a reservation has been released otherwise than in accordance with subdivision D 7, or has been released in accordance with that subdivision where a determination is thereafter rescinded under this subdivision* | **1** | § 51.1-142.4 |
| *to retire as required by subsection F* — D 7's carve-out | **2** | § 51.1-142.4 |

**Memo-ready text, as cured:**

> **The bill's rule against paying the Commonwealth's share twice could once have stopped it being
> paid at all, and the member it caught was an ordinary one. One amendment to the rule closed both
> routes.** The rule bars a second settlement after the reservation has been released or after a
> reduction determination has taken effect. **Two routes used to run into it.** The first was the modal
> case: a member whose purchase is reduced because the Board corrects her service record upward, so
> part of her reservation is released, who then pays in full, is credited, and dies before she retires.
> On the old words the bar reached her even though no rescission was involved, and the consequences
> were real — the retirement system was never paid, the remainder of her reservation stayed charged
> against the $3,000,000 cumulative limitation permanently, and the annual report's duty became
> perpetual. The second was the member who is laid off, where the rescission route answered the bar's
> determination limb and said nothing about its release limb.
>
> **The rule now reads on a reservation released *"in full"* that *"has not been reinstated under this
> subdivision"*, and on a determination that has taken effect *"and has not been rescinded, reversed,
> or modified."*** **So the bar does not apply to the member whose reservation was released in part
> and not in full**, which is the modal case; and it does not apply where a rescission, reversal or modification
> has undone the determination, which is the laid-off member's case. A separate sentence requires the
> Board to reinstate a reservation released in accordance with the release provision where a
> determination is afterwards rescinded, reversed or modified, so the reinstatement the cure refers to
> is itself a duty and not a contingency. **The Lab's reviewer proposed exactly this amendment, on the
> ground that it cures both routes at once; it is enacted.**

**The quotation defect this entry would otherwise have carried.** Pass 17's quotation of the bar
**counts 0 at revision 70**. An artifact printing it in quotation marks at a revision-70 dateline
would be unquotable against the bill — the C2 defect, in the same place in the same section.

**Citation to carry:** § 51.1-142.4 G 4's settlement bar and reinstatement sentence, and D 2, D 6 and
D 7, **all verified at bill text store revision 70 (13 October 2026)**; pass 17 finding **S-1**; the
one-amendment cure and the recommendation, Drafting Specialist, §7 item 114 and
[`moo152-pass17-disposition`](/MOO/issues/MOO-42#document-moo152-pass17-disposition) §2 — **reported
here as enacted.**

**One precision the memo keeps if it reports this as cured.** **C7 is cured and C13 was its successor
on two other routes; both are now closed, and an artifact must not merge them or describe either as
still open.**

---

### C14 — the reversal duty. **CURED, and its quotation is no longer available either**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| **The duty as cured** — *…shall restore or credit service credit as this subdivision provides, and, **where the determination as reversed or modified is such that the certified subsidy falls to be settled under subdivision 1 or under this subdivision**, shall recertify and settle it accordingly, no later than 60 days after the reversal or modification* | **1** | § 51.1-142.4 |
| **The duty as pass 17 quoted it** — *…and shall recertify and settle the certified subsidy as this subdivision requires, no later than 60 days after the reversal or modification* | **0** | § 51.1-142.4 |
| *as this subdivision requires* | **2** | § 51.1-142.4 |
| *reversed or modified* | **7** | § 51.1-142.4 |

**Memo-ready text, as cured:**

> **An unconditioned reversal duty could once have commanded the subsidy payment the bill is designed
> not to make, and one clause now conditions it.** Where a reduction determination had taken effect
> and was afterwards reversed or modified, the bill required the Board to restore the credit and to
> recertify and settle the subsidy within 60 days. **The duty asked no question about whether anything
> fell to be settled.** On the Lab's worked case a member asks for reconsideration, loses, and has her
> reduction made larger — and on the face of the old sentence a determination that had taken effect had
> been *modified*, so the settlement machinery ran for a member who never retired in a qualifying
> retirement, never died, was never approved for disability and was not defeated by an error of the
> Board. **There was a reading on which the duty was empty, and that reading left the saving words the
> same revision added with nothing to operate on. Either it was a null duty or it was an unpriced
> instruction to pay money, and both were defects.**
>
> **The sentence now settles the subsidy where the determination as reversed or modified is one on
> which the subsidy *"falls to be settled"*, and it names the two provisions it can be settled
> under.** So **the settlement limb does not apply** to the member whose reduction was merely made
> larger, and the referent is correct where she is reversed because she did retire properly. **The
> fork is closed on both sides: the duty is not null, and it reaches no case the bill did not mean it
> to reach.** The clause the Lab's reviewer proposed is the clause enacted.

**Citation to carry:** § 51.1-142.4 G 4's reversal sentence and subdivision 2, and subsection N,
**verified at bill text store revision 70 (13 October 2026)**; pass 17 finding **S-2**; the conditioning
clause and the referent correction, Drafting Specialist, §7 item 115 and the disposition §2 — **reported
here as enacted.**

**One precision retained.** **Do not write that the Board *"would obviously not have paid."*** The old
sentence was in the mandatory form; the honest statement is that the text commanded it and one clause
cured it.

---

### C15 — the arrears formula. **CURED, both limbs, and its quotation is no longer available**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| **The formula as cured** — *the next payment of the member's retirement allowance shall include every amount **by which the amounts paid to the member fall short of** the amounts that would have been payable … **or, where the determination is reversed in its entirety, had no determination been made*** | **1** | § 51.1-142.4 |
| **The gross formula as pass 17 quoted it** | **0** | § 51.1-142.4 |
| G 4's no-collection sentence **as pass 17 quoted it** | **0** | § 51.1-142.4 |
| The live no-reduction limb — *no amount payable to the member or to any survivor, beneficiary, or estate of the member shall be reduced by reason of any such deferral or application* | **1** | § 51.1-142.4 |

**Memo-ready text, as cured:**

> **The bill once told the Board to pay a member who wins on review the whole allowance again for
> every month she had already been paid, and the formula is now net.** The words were borrowed from
> the determination provision, where they are safe **because that provision forbids any payment before
> the determination takes effect** — nothing has been paid, so gross equals net. The reversal
> provision put them in a setting where payments had been running the whole time. On the reviewer's
> worked facts a member is paid a reduced allowance of **$3,100** a month for 18 months, wins, and her
> unreduced allowance would have been **$3,560**: **she is owed $8,280 and the old sentence commanded
> $64,080**, a difference of **$55,800** she had already received. The bill also forbids recovering
> it, so the overpayment would have stayed with her.
>
> **The sentence now pays her every amount *"by which the amounts paid to the member fall short of"*
> the amounts that would have been payable**, and it carries a second limb for the case where the
> determination is reversed in its entirety, so nobody can argue that a wholly reversed determination
> never took effect and the arrears are therefore zero. **Both limbs the Lab's reviewer drafted are
> enacted, and the formula no longer overpays in either direction** — pass 17 had already confirmed the
> earlier repair does not underpay her.

**Three bindings, carried.**

1. **The three figures are the reviewer's worked example on an assumed fact pattern, not a fiscal
   estimate and not Fiscal's.** They travel with that attribution and are not scaled to a program
   total anywhere.
2. **The authority correction travels with the finding.** The no-collection bar that mattered here is
   **G 4's own sentence**, not subsection F's. **And note the quotation point: neither the F limb nor
   the G 4 limb reads as pass 17 printed it at revision 70.** The F limb now reads on *"that
   account"* and on a no-reduction rule; an artifact that needs a no-collection quotation must take it
   from the live text and count it.
3. **It is not an attack on the member.** She did nothing wrong and keeps everything the bill gives
   her. The defect was in the Commonwealth's drafting and the memo should say so in those terms.

**Citation to carry:** § 51.1-142.4 G 4's arrears sentence and no-collection sentence, and subdivision
2's no-payment sentence, **all verified at bill text store revision 70 (13 October 2026)**; the worked
facts and the three figures, pass 17 finding **S-3**, the reviewer's own arithmetic on his own
hypothetical; the cure's two limbs, Drafting Specialist, §7 item 116 and the disposition §2 —
**reported here as enacted.**

---

### C16 — the disability carve-out. **CURED as to the inversion. One narrower class survives, and so does one question I am not answering**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| **Cure 1, enacted** — *upon an application the filing of which did not require a waiver of a ninety-day notification period set forth in subsection A or B of § 51.1-156* | **1** | § 51.1-142.4 |
| **Cure 2, enacted** — *upon an application as to which the Medical Board has made a certification described in clause (ii) of subsection H of § 51.1-156* | **1** | § 51.1-142.4 |
| The counterfactual trigger pass 17 found — *as to which the Board was required by subsection H of § 51.1-156 to waive the ninety-day notification period* | **0** | § 51.1-142.4 |
| The saving sentence as it now reads, with its express rescission exception | **1** | § 51.1-142.4 |
| The saving sentence **as pass 17 quoted it** | **0** | § 51.1-142.4 |
| *ninety-day notification period* | **2** | **CODE** § 51.1-156 |
| § 51.1-156 H clause (ii), the Medical Board certification | **1** | **CODE** § 51.1-156 |

**Memo-ready text, as cured, with the residual stated:**

> **The bill once rescued a member who filed her disability notice eight months late and refused the
> member who filed on time. The inversion is closed.** Where a reduction determination had taken
> effect, the bill rescinded it if the member was afterwards approved for disability on an application
> filed by the date the determination took effect, or on one the Board **was required** by § 51.1-156 H
> to accept out of time. So a member who missed the Code's deadline through no fault of her own was
> rescued, and the member who needed no waiver at all was not: she filed inside her own ninety days,
> was approved, and the rescission provision did not reach her **because the Board was never *required*
> to waive anything.**
>
> **The trigger now reaches her in terms.** It runs on an application *"the filing of which did not
> require a waiver of a ninety-day notification period set forth in subsection A or B of
> § 51.1-156"* — the timely filer, named — and on an application *"as to which the Medical Board has
> made a certification described in clause (ii) of subsection H of § 51.1-156."* **That second change
> cures a separate defect in the same words: the trigger used to turn on a counterfactual — what the
> Board *was required* to do — which the bill assigned to nobody, gave no period and required no
> notice of. It now turns on a certification the Medical Board actually makes.** Both cures the Lab's
> reviewer drafted are enacted, and the saving sentence now carries an express exception for the
> rescission the subdivision provides, so the two sentences no longer read against each other.
>
> **One narrower class is still outside, and it is the one the Lab flagged and the Director decided the
> other way.** A member whose waiver the Board granted as a matter of discretion for good cause shown,
> rather than on a Medical Board certification under clause (ii), is reached by neither limb. **That is
> a policy choice, not a drafting defect**, and the reviewer asked for it to be re-made once the
> timely-filer class was known. It is now known, and it is cured.

**Permissive framing.** Write **the saving sentence does not apply where the subdivision provides for
rescission**, and **the rescission reaches the timely filer**. Do not write that the Board must pay
anyone.

**Citation to carry:** § 51.1-142.4 G 4's rescission trigger and saving sentence, **verified at bill
text store revision 70 (13 October 2026)**; § 51.1-156 A, B and H, retrieved from
`law.lis.virginia.gov`, MOO-210, 12 October 2026; the four-class taxonomy, the worked dates and the
litigation framing, pass 17 finding **S-4** and §5 question 10; the two cures, Drafting Specialist, §7
item 117 — **reported here as enacted.**

**The binding I am not touching, and the question it raises.** Pass 17's first binding on this entry
was that **the memo may not say the classification is unproblematic, is clearly constitutional, or
would certainly survive** — and the entry was *"the only live constitutional surface in the draft."*
**On the live text the inversion the constitutional argument was built on is gone.** Whether the
surviving discretionary-waiver class carries the same argument, and whether pass 17 §3.7's approved
null-result sentence can still say *"one constitutional question is live, and it is the one at
C16,"* **is the Red Team's judgment and the Director's, not mine.** I have not re-cut either sentence.
**Flagged at §5.1.**

**And one pass-12 ban that is still engaged.** **Do not write that § 51.1-156 H *permits* the Board to
waive.** Its second sentence **requires** the waiver once the Medical Board certifies — counted above.

---

### C17 — the hardship branch. **CURED**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| *if the member retires in a qualifying retirement no later than 90 days after the date of the involuntary separation* | **1** | § 51.1-142.4 |
| **The cure, enacted** — *or, where this sentence is applied otherwise than in the determination of the member's unreduced retirement eligibility date, on or before the member's effective date of retirement* | **1** | § 51.1-142.4 |
| The residual sentence — *…that date is, for the purposes of the preceding sentence, the date on which the Board makes the certification, recertification, determination, statement, or other decision in which that date is applied* | **1** | § 51.1-142.4 |
| *involuntarily separated* | **3** | **CODE** § 51.1-155.1 |

**Memo-ready text, as cured:**

> **The protection for a member who is laid off could once have required her to take a retirement the
> same bill had just told her she might not take. A second limb fixes the date and releases her.** If a
> member is involuntarily separated after her election is accepted, the bill protects her credit
> *"if the member retires in a qualifying retirement no later than 90 days after the date of the
> involuntary separation."* For a member in her early fifties with twenty-odd years of service, the
> retirement that is not actuarially reduced is the one the Code gives a state employee who is
> involuntarily separated with twenty or more years. **The section confines that route to a member who
> has already incurred the separation — and the date as of which that was tested was, on one reading,
> the certification years earlier, before she had been separated from anything.** On that reading the
> protection could defeat the member it was written for.
>
> **The confinement now carries a second limb: where the sentence is applied otherwise than in
> determining her unreduced retirement eligibility date, the condition is tested on or before her
> effective date of retirement.** The qualifying-retirement test is such an application, so the
> relevant date is her retirement and not her certification — and a member laid off before she retires
> satisfies it. **The bar does not apply to her.** The cure the Lab's reviewer drafted is the cure
> enacted, and it is also the general answer to the same sentence's failure to yield a date in its
> other uses.
>
> **The confinement itself admits nobody and narrows nothing** — the conditions it recites are the
> Code's own, verified. The defect was the timing condition the section added, and the timing
> condition now has its own rule.

**Citation to carry:** § 51.1-142.4 G 4's hardship branch, the section-wide confinement and the
residual sentence, **all verified at bill text store revision 70 (13 October 2026)**; § 51.1-155.1 A, C
and D, retrieved from `law.lis.virginia.gov`, MOO-210, 12 October 2026; pass 17 finding **S-6** with
**M-4**; the cure, Drafting Specialist, §7 item 119 — **reported here as enacted.**

**Two precisions retained.**

1. **Do not say the confinement excludes people generally.** It admits nobody and in substance restates
   the Code's own conditions — verified.
2. **The alternative cure was considered and declined**, and the ground for declining it was that it
   would reverse an earlier stated reasoning. The limb that was enacted is the one the reviewer
   preferred, so that disagreement is spent and the memo need not report it.

---

### C18 — the settlement count, and the window the engine cannot price. **Must appear, and the wording is fixed**

**Dateline: checked at store revision 70, 13 October 2026.**

| String | Count | In |
|---|---|---|
| The error route — *Where a determination under subdivision 2 or 3 has taken effect, a member may file with the Board written evidence that the member was unable to retire in a qualifying retirement by reason of an error of the Board* — **no period is stated for her filing** | **1** | § 51.1-142.4 |
| *is reversed or modified on reconsideration under subsection M or on judicial review* | **2** | § 51.1-142.4 |
| The bounded disability limb — *upon an application filed no later than the date on which the determination took effect* | **1** | § 51.1-142.4 |
| The unbounded disability limb — the Medical Board certification under § 51.1-156 H clause (ii) | **1** | § 51.1-142.4 |
| *refund* | **27** | § 51.1-142.4 |
| *interest*, anywhere in the section | **0** | § 51.1-142.4 |

**The authorised statement, to be used in these words and not paraphrased:**

> **No admission quantity moves; the settlement count moves upward by an amount the current engine
> cannot value.**

**Memo-ready text, built around it, restated at revision 70:**

> **Nothing in the bill as it stands lets one additional member into the program — and that half is
> independently verified.** The Lab's reviewer checked every eligibility test, the purchase cap and
> the definition of an eligible member and found that none of them is touched, and the one change that
> narrows anything can only ever exclude. **No admission quantity moves.**
>
> **But the model's cost estimate rests on an assumption the settlement provisions break.** The engine
> prices the provisions that vest a member's credit on death, disability approval or involuntary
> separation over a window it describes in its own words as *"exactly
> election-to-required-retirement"*, and it says in the same paragraph that *"the cost per event is
> NOT priced."* **Settlement routes run past required retirement, and two of the three carry no outer
> date.** A determination of the Board's own error is one: the bill lets the member file written
> evidence after the determination has taken effect and states no period for her to do it in. Reversal
> on judicial review is another, and ordinarily takes two to four years. **The third — approval for
> disability — is now bounded for the ordinary filer and for the timely one, and remains open on the
> limb that runs on a Medical Board certification that the disability was unknown at termination,
> which the Code puts no outer date on.** **The settlement count therefore moves upward, and the
> direction is not in doubt.**
>
> **It cannot yet be priced, for two reasons that are facts about the model and not judgments about the
> bill.** The per-event cost of these settlements was never priced — survivor and disability benefits
> sit outside the model — and **disability has never been a decrement in the exposure calculation at
> all**, although disability approval is the very event these provisions enlarge. **So this exposure is
> currently scored at zero by construction, not by evidence.** The re-run that would value it — an
> unbounded exposure window and a disability decrement — **is requested of the Fiscal & Impact Modeler
> and has not happened. No dollar figure is authorised, and none is given here.**
>
> **One further gap of record:** the quantification list the bill's money statement will rest on names
> two one-sided costs and omits two more that these provisions create — a refund and an arrears
> payment, both paid out of the trust. The section provides for refunds in twenty-seven places and
> provides for no interest on any of them.

**What changed from pass 17's text, and it is a narrowing rather than a softening.** Pass 17 wrote
*"a disability approval the Code can compel the Board to accept years later"* without qualification.
**At revision 70 two of the three disability limbs are date-bounded and one is not**, and the entry now
says which. **The finding's direction and its unpriceability are unchanged, and no figure is added.**

**Citation to carry:** pass 17 **§4** and finding **S-8**, as adopted in
[`moo152-pass17-disposition`](/MOO/issues/MOO-42#document-moo152-pass17-disposition) **§4**, which is
the record that authorises the statement; the engine's window and *"the cost per event is NOT priced"*
language, quoted from `05-model-code-and-data/python/moo48_main.py` by pass 17; the three settlement
routes and the refund and interest counts, **§ 51.1-142.4 G 4 and subsection M, verified at bill text
store revision 70 (13 October 2026)**; the item-99 omissions, the same §4.

**The five bindings are carried, and the first two are absolute.**

1. **The phrase *"no priced quantity moves"* is withdrawn and may not appear in any artifact.**
2. **No dollar figure.** None is authorised. The reviewer's tail percentages are his arithmetic on his
   own alternate assumption, on the death limb only, which he states is a floor. If an artifact needs
   magnitude it uses his terms — **two years of tail more than doubles the death-settlement count the
   model carries** — attributed to the adversarial review and to nobody else.
3. **The two halves are stated together or not at all.** The authorised sentence carries both.
4. **This does not replace C12**, and neither is netted against the other.
5. **MOO-90's C3 hold is engaged.** The entry complies by saying the exposure is scored at zero **by
   construction**.

---

## 5. Flagged, not guessed — four things I am reporting rather than classifying

### 5.1 Whether a constitutional question is still live, and whether an approved sentence survives

C16's inversion is cured on the live text. Pass 17 §3.7's approved null-result paragraph says *"One
constitutional question is live, and it is the one at C16."* **I have not re-cut it, and I will not.**
The question is whether the surviving discretionary-waiver class carries the equal-protection argument
the inversion carried. **That is the Red Team's judgment on its own finding, and then yours.** Until it
is answered, I recommend the null-result paragraph is held out of the cut rather than printed in either
form.

### 5.2 Your "no *only*" rule against two quotations I cannot shorten

**Your instruction is no *"only"*.** C5 and C17 both turn on the enacted confinement sentence, whose
own words are *"the member may retire under subsection A or C of § 51.1-155.1 **only where** the member
has incurred an involuntary separation…"* **I cannot drop a word from a bill quotation and I will not
paraphrase one into quotation marks.** Three ways out, and the choice is yours:

- **(a)** quote it in full. The *"only"* is the bill's, inside quotation marks, and it narrows the
  § 51.1-155.1 route rather than making any claim about the pathways item 47 reserves;
- **(b)** cite the sentence by content and quote nothing — *"the section requires that the member have
  incurred the separation on or before the date as of which her eligibility date is determined"* —
  which is what I have done in the C5 and C17 memo-ready texts above, keeping the quoted fragments
  clear of the word;
- **(c)** quote it in full and carry a one-sentence note that the word is the bill's and is not a
  statement about the pathways.

**I have drafted to (b) and I think (b) is right, but (a) and (c) are both defensible and the rule is
yours.** Note that the count tables above print the full sentence, because a count table that prints a
shortened string is not a count of anything.

**And here is how I read the rule, so you can correct the reading rather than discover it.** I have
taken *"no *only*"* to bar the word where it makes a claim about which routes the bill recognises —
the expressio unius surface item 47 reserves — and not to bar the ordinary English word. **On that
reading two uses survive in text destined for an artifact, both of them pass 17's own words carried
without paraphrase:** C18's *"the one change that narrows anything can only ever exclude"*, and C18's
binding 2, *"on the death limb only."* **Neither is about pathways.** If you want the rule read
flatly, say so and I will re-cut both — but re-cutting the first changes an approved verified
sentence, so I have not.

### 5.3 Whether six cured entries stay in §8 as cured, or leave it

C4 is must-appear **as cured** on MOO-111's express instruction. **C5, C13, C14, C15 and C17 have no
such instruction**, because nobody expected them to be cured. §8 can carry six cured entries and one
and a half live ones, or it can carry the live ones with a single paragraph recording that five
drafted cures were enacted. **The first is more honest about the Lab's own record; the second reads
better and risks reading as a victory lap.** I have drafted all six in full so either is available.
**This is a structural call on the memo and it is yours.**

### 5.4 One classification I am not making at all

**Whether C6's surviving limb is still must-appear, or is now small enough to go to §9 as an open
question.** The over-cap command is live and counted twice; the disclosure around it is complete; the
trigger is bounded on two of three limbs. I have drafted it as must-appear because it is the one
first-reading exposure, **but the argument that a fully-disclosed, narrowly-reachable over-cap
reinstatement is a §9 question rather than a §8 risk is a real one and I am not the person to make
it.**

---

## 6. Drafter's note

### 6.1 What I did, in order

1. Pulled the four source registers from their issue documents rather than from the repo copies —
   MOO-90 (C1–C3), MOO-111 (C4–C6), MOO-133 (C7–C12), MOO-160 (C13–C18) — plus MOO-165 (C19), MOO-172
   (C20–C23) and MOO-202 (C1–C3 restated).
2. Pulled the live `bill-text-s8` body and extracted enacted §1 and enacted § 51.1-142.4 by the same
   boundaries the MOO-164 verification uses.
3. Counted all 66 strings. **Six assertions failed, and the six failures are the six cures.** I then
   read the live text around each failure before concluding anything from the count.
4. Drafted the ten entries to what the counts support, and stopped at every point where the next step
   was a judgment that is not mine.

### 6.2 What I did not do

- **I produced no new finding.** Every finding, figure and fix above is the originating agent's, cited
  to them. Where the live text has overtaken an entry, I report the overtaking and the count; I do not
  substitute an analysis of my own.
- **I changed no number.** Not one figure in C12, C15 or C18 is restated. Where the bracketed
  contingency and the enacted recertification repair bear on C12's per-member arithmetic, I state the
  condition and route the re-derivation to the Fiscal & Impact Modeler, as both the drafter and pass 17
  did before me.
- **I resolved no conflict.** C23's 78.1872%-against-67.4% utilisation hold stays held and stays routed
  to you. The standing rule binds in the meantime.
- **I re-verified C1 nowhere and re-drafted it nowhere.** MOO-206 §1.4 gives its direction and it is a
  separate job.
- **I named neither § 51.1-155.1 B nor § 51.1-155.2 A, anywhere.** Item 47 is untouched.
- **I inserted nothing into any artifact.** No sponsor document, no register, no cut.
- **I did not re-cut an approved sentence**, including pass 17 §3.7's null-result paragraph, which
  §5.1 flags instead.

### 6.3 What I need back

1. **The ranking decision.** C6 into the current cut, or all three live entries into the next one.
2. **Approval of the wording**, entry by entry or as a block.
3. **The four flagged questions at §5**, of which §5.1 and §5.3 reach the shape of memo §8 and §5.2
   reaches a standing rule of yours.

---

## 7. Standing caveat

**Internal working draft material.** This document quotes working bill text, so the caveat travels
with it. This is **not** a Division of Legislative Services bill, it has **not** been reviewed or
cleared by counsel or by DLS, and nothing here is an opinion that any provision is legally sufficient
for introduction. Only DLS drafts official Virginia bills. Every figure, period and reading above is
pre-decisional and internal, nothing here is cleared for external use, and release is the Policy
Director's to decide.
