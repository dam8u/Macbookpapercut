
---

## 18. Revision 8 — [MOO-214](/MOO/issues/MOO-214)'s counsel pass folded, and the base at store revision 72

**This section is the only part of the document added at revision 8.** Everything above it that
MOO-214 or the base made false is corrected **in place**, and every such correction is listed at
**§18.14** so the Policy Director can check it rather than take my word for it. **§6 is re-spliced
from store revision 72 — the ninth time.** Nothing is applied to the store.

MOO-214 returned **13 findings — 0 fatal, 6 serious, 4 moderate, 3 minor** — plus 12 null results
and four direct answers to the questions revision 7 put. **No finding is rejected.** One fix
*direction* is declined, on a counted ground that counsel did not have, and the words are drafted so
the Director can overrule me in one line.

### 18.0 The thirteen findings and what each one did

| | Finding | Disposition at revision 8 | Where |
|---|---|---|---|
| **S1** | s12's *"any notice described in the preceding sentence"* is ambiguous between the **kinds** of notice and the **late** notices; clause (iv) is not | **Taken. Three words: *"of a kind."*** Both sites conformed | §18.2 |
| **S2** | clause (iv) advertises a 30-day window and states the disqualifying condition *after* the grant | **Taken. The bar moves into the trigger** | §18.2 |
| **S3** | 164-7's exception names R-6 by a **paraphrase** that matches R-3 and R-4b too | **Taken, in the form counsel itself called the single most valuable change in the review** — the descriptor this cut already coined | §18.1 |
| **S4** | the disclosure duty has **no enforcement route** as to the written statement, and the subsection J route I relied on **does not exist** | **The false claim is withdrawn and counted at 0.** Candidate **164-17** drafted and **HELD** — **question 2** | §18.8 |
| **S5** | `check_doc_vs_kit.py` passes on three separately corrupted documents, and today misses a block in §3 | **Taken in full. The script is rewritten against all five fix directions**, and counsel's own breaking harness is run against the new one | §18.11 |
| **S6** | R-6's notice starts a **forfeiture** clock that runs from mailing, in a case the member has no reason to expect | **Carded. Candidate 164-15 drafted and HELD — question 1.** It adds a figure, so it is not mine | §18.7 |
| **M1** | clause (iv) omits s12's **timeliness deeming** and its **supersession** — the whole benefit | **Taken.** Clause (iv) now states both | §18.2 |
| **M2** | subsection G will define *"pending"* twice, differently, with nothing marking the divergence | **Declined as a marking, on MOO-209 F6's own ground.** Candidate **164-18** — the one form that is operative rather than surplusage — drafted and **HELD. Question 3** | §18.6 |
| **M3** | 164-12's *"such an application"* is a back-reference across a sentence boundary | **Taken. Eleven words: the noun phrase written out**, as G 4's model does | §18.4 |
| **M4** | two savings, asymmetric exception lists, no cross-reference | **The Director's MOO-141 §3.3 cross-reference is drafted and applied**, and the *expressio unius* inference is shown to be **inert**, counted rather than argued | §18.5, §18.9 |
| **m1** | *"the member's retirement has taken effect"* is a bare phrase the section never uses unqualified | **Taken. *"after the member has retired"*** — a form already in §1 | §18.3 |
| **m2** | a decision deemed to exist might be argued to be deemed to **state** what a decision must state | **Taken. One sentence, drafted so that MOO-209's N1 byte-identity survives** | §18.3 |
| **m3** | in the no-act branch the deeming does not move the date, because R-5b overrides it | **Recorded. No text** — counsel says it is not a defect and I agree | §18.10 |

**The patch is still twelve edits in thirteen substitutions. The delta is +4,210, not +3,375.**

### 18.1 S3 — the paraphrase is out, and the descriptor this cut already coined is in

**Counsel is right and the finding is mine to have made.** §9.6 of this document sets the rule —
*do not cross-reference by paraphrase* — and revision 7 broke it in 164-7's own exception. The
revision-7 descriptor was *"the duty of the Board … to give the member written notice of the
member's final qualifying retirement date."* **Counted on the base, three duties in that definition
answer to it:**

| | duty | its deadline runs from |
|---|---|---|
| **R-3** | *"shall give the member written notice of its determination and of the reasons for it"* | 30 days after the request is filed |
| **R-4b** | *"shall give the member written notice of any later date approved after that statement"* | 15 days after the approval |
| **R-6** | *"it shall give the member written notice of that date"* | 15 days after it acts upon the request |

R-4b answers it **on the definition's own first sentence** — a later approved date *is* the member's
final qualifying retirement date. R-3 answers it on a second step. And the tail risk counsel names is
the one that matters: read to include R-3, the exception would let the deeming *"determine the date
by which the Board is required to act upon a request"* for R-3's purposes — **the very thing the
saving's first limb exists to forbid.**

**The cure needs no new words.** After **164-5** and **164-13(a)**, the phrase *"notice of a date
required by that definition by reason of the Board's action upon a request"* stands in the bill at
two sites, and at both of them it names R-6's notice and nothing else — because at both sites it is
listed **beside** *"notice of a later approved date,"* so the bill's own parallel excludes R-4b. The
exception now uses it, and the descriptor stands at **three** sites with every variant at zero. All
of that is counted in `verify_r72_v8.py`, including the two parallel listings.

**It also survives MOO-141's Edit 2 for the reason the four-word lift did not: it is not
deadline-keyed.** The verifier asserts that the descriptor contains no deadline formula, so no
re-keying of R-6's fifteen days can detach it.

#### Counsel's recommended *form* — impose a duty rather than except one — is declined, on a fact counsel did not have

Counsel's answer to my question 4 recommends replacing the exception with a free-standing duty in
164-7, and says it *"does not displace your recommendation of a second limb in MOO-141 Edit 2 — it
makes MOO-164 no longer depend on it."* **That recommendation was written against a premise that had
already changed: the Policy Director re-cut MOO-141's Edit 2 as their own revision 8 and the second
limb is in it.** Its residual limb reads, in the two no-decision classes, *"it shall give that notice
no later than 15 days after the date on which the Board acts upon the request"* — R-6's **own** duty,
with a deadline the deeming dates.

**So the imposed duty would now be a second duty to give the same notice, in the same case, keyed to
the same date.** Two provisions commanding one act is the *Forst* problem in its plainest form, and
it is worse here than usual because the two would sit in different subsections and a later amendment
to either would silently create a divergence. **The exception does the whole job and adds no duty.**

> **Candidate 164-16 — DECLINED on that ground, drafted so the Director can overrule me in one line.**
> It would replace the exception's second limb with:
>
> ```
> Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of "final qualifying retirement date" in subsection A within the period allowed by this section for acting upon it, and the Board has not stated the member's final qualifying retirement date in a decision upon the request, the Board shall give the member written notice of that date no later than 15 days after the date on which it is deemed by this subsection to act upon the request.
> ```
>
> **If MOO-141's Edit 2 revision 8 were ever withdrawn, 164-16 becomes the right answer and I would
> ask for it.** That contingency is the reason it is drafted rather than merely described.

### 18.2 S1, S2 and M1 — s12 and clause (iv) are now one rule, stated twice in the same words

**S1 is the finding with the largest practical reach in this pass**, and counsel's failure scenario
is the ordinary case rather than a corner: a request for a later final qualifying retirement date is
filed *after* the written statement by construction, so the filing period has normally expired before
any notice of the approved date issues. On the narrow reading of *"any notice described in the
preceding sentence"* — notices **given late**, rather than notices **of the kinds listed** — 164-8
would give that member nothing, in its commonest application, while clause (iv) printed in her own
notice told her she had thirty days.

**Three words fix it, and the same three words go into clause (iv) so the two cannot drift:
*"of a kind."*** Both sites are counted, in both directions.

**S2.** Clause (iv) stated the 30-day window and then, after the grant, the bar. For the member whose
retirement has already taken effect — *"which is most of the members who get a late notice at all,
because a notice is late precisely when the dates have already run"* — the window described was
closed on the day it was written. **The bar is now a condition of the trigger**, so the clause
describes a right only to the class that has one.

**M1.** Revision 7's clause (iv) omitted both operative limbs of s12 — the deeming that the notice
*"is filed within the period allowed by this subdivision"* and the **supersession**. Counsel is right
that supersession is the whole benefit, and that a member who cannot tell whether her replacement
notice displaces the first will rationally do nothing. **Both limbs are now in clause (iv), in s12's
own words.** The verifier asserts each shared limb present in both texts, because *"the same words"*
is a counted claim and not a sentence.

**What this costs.** Clause (iv) goes from +454 to **+564**; 164-13 totals **+667** across its two
substitutions. 164-8 itself gets **shorter** — +621 to **+613** — because m1's noun is eighteen
characters shorter than the phrase it replaces and *"of a kind"* is ten longer.

### 18.3 m1 and m2 — two minor findings, both taken, and one of them had to be drafted around N1

**m1.** *"The member's retirement"* occurs ten times in §1 and is qualified every time. s12 and
clause (iv) introduced the eleventh and twelfth, both bare. Counsel's residual — the member who
retired under § 51.1-155.1 or on disability without a § 51.1-153 notice — is a member the bar
**should** reach, so the cure is the short form rather than the narrow one: **"after the member has
retired."** That exact form is already in §1 once, which is the test I applied.

**m2.** M 2's enacted sentence makes the constructive denial *"the final determination of the Board
upon the reconsideration and a case decision."* R-6's duty arises only *"where the Board does not
[state the date in its decision]."* Counsel's argument — that a decision deemed to exist is deemed to
state what a decision must state — is, as counsel says, a stretch. **It is also five words to
foreclose and the exception is load-bearing, so I have taken it.**

> **EXTRACT OF APPLIED TEXT — the sentence, as applied inside Edit 164-7:**
>
> ```
> The Board is not deemed by this subsection to have stated a member's final qualifying retirement date in a decision upon a request.
> ```

**It is a separate sentence, and that is a drafting decision rather than a stylistic one.** Counsel's
fix direction would have appended it to the saving. The saving's **256-character body is
byte-identical between 164-7 and MOO-141 Edit 1** — MOO-209's N1 asked for that to be asserted, and
the Policy Director's MOO-141 §3.1 relies on it. **Appending to one saving and not the other would
have broken the invariant in the same pass that M4 asks me to make the two sentences more legible
together.** As a separate sentence it changes nothing in the saving and the invariant still holds,
asserted.

### 18.4 M3 — 164-12's new sentence is now self-contained, as the model it copies is

G 4's definition is self-contained: *"an application for a disability retirement allowance is
pending from …."* Revision 7's G 2 definition opened *"such an application,"* whose antecedent is in
the **previous** sentence. That is the liftability guard the Director adopted at MOO-206, failing in
a new sentence — and it stops resolving the moment anything is inserted between the two, or the
definition is moved to subsection A where the section's other definitions live.

**Eleven words. The noun phrase written out, in the words G 2's own preceding sentence uses:** *"an
application of the member for a disability retirement allowance under this chapter."* 164-12 goes
from +167 to **+233**.

### 18.5 The Policy Director's MOO-141 §3.3 cross-reference — drafted, to their three requirements

The Director specified it and assigned it to this cut: it must say what each deeming governs, make
them cumulative and non-overlapping, and **move no date and add no exception**. MOO-209's F9 and
MOO-214's M4 are the findings behind it.

> **EXTRACT OF APPLIED TEXT — the last sentence of Edit 164-7:**
>
> ```
> The provision of this subsection deeming the Board to act upon a request applies where the Board does not act upon the request, and neither limits nor is limited by any provision of this section deeming the Board to act upon a request, and to last act upon it, on the date on which the Board first acts upon it, which applies where the Board acts upon a request more than once; the two provisions apply cumulatively, and neither is the exclusive rule for determining the date on which the Board acts upon a request.
> ```

**Each of the three requirements is a counted assertion, not a claim**: the two *"applies where"*
limbs; *"apply cumulatively"* and *"neither is the exclusive rule"*; and — for requirement 3 — the
absence of **any** of *"no later than,"* *"days,"* *"month,"* *"date of"* and *"except"* from the
sentence. It moves no date because it contains no date.

**One drafting decision inside it, and it is the one that matters.** The Director's §2.4 rejected a
formula for Edit 2 that would have left *"a reference to a deeming that does not exist"* if that
patch ever landed alone. **The same objection applies to a cross-reference drafted from this side**,
so this one **names the other deeming by its content and not by a citation**: *"any provision of this
section deeming the Board to act upon a request, and to last act upon it, on the date on which the
Board first acts upon it."* With MOO-141 absent the class is empty and the clause is inert; with
MOO-141 present it resolves to Edit 1's sentence and to nothing else. **Counted all three ways: 0 in
the base, 1 in this cut alone (the cross-reference's own words), 2 on the combined text** — and G 4's
two occurrences of *"the date on which the Board first acts upon it"* are counted separately and
excluded, because they deem nothing.

**So the §3.3 cross-reference creates no new application dependency.** The Director's joint-landing
decision stands on its own reasons; this sentence does not convert it into a textual requirement.

### 18.6 M2 — declined as a marking, because any marking is the surplusage MOO-209 F6 removed. **Question 3**

Counsel's fix direction is two words — *"and notwithstanding the definition in subdivision 4."*
**That is, to the character, the clause MOO-209's F6 made me delete one revision ago**, and F6's
ground was not that it was wrong but that it implies a conflict that does not exist and weakens the
six other confinement clauses in this section that have no notwithstanding beside them. Re-inserting
it under a different justification would be the same defect with a better story.

**Counsel's own answer to their own question is why I think the text is not where this belongs:**
*"is a reader of G 2 alone misled? **No; G 2 alone is coherent.**"* The reader at risk is the one who
reads G 2 and G 4 together — and that reader is reading two sentences that each begin *"For the
purposes of this subdivision"* and each name a different endpoint. **The divergence is on the face of
the text; what is missing is a reason, and a reason is not a thing statutes carry.**

**M3's cure helps here too, which is why it is not merely cosmetic:** writing G 2's noun phrase out
in full makes its sentence stand alone, so a reader is less likely to reach for G 4's definition to
complete it.

**But there is one form that is operative rather than surplusage, and it is the right answer if the
Director wants M2 cured in text: stop using one word for two concepts.**

> **Candidate 164-18 — HELD, and it is the Policy Director's call and not mine, because it deletes
> enacted words of [MOO-42](/MOO/issues/MOO-42) §7 item 46.**
>
> **FIND** (1 in enacted §1 of store revision 72; it **contains** Edit 164-12's own FIND, so the two
> are mutually exclusive and the verifier says so):
>
> ```
> Nothing in this subdivision prevents the payment of a retirement allowance to a member while an application of the member for a disability retirement allowance under this chapter is pending, and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.
> ```
>
> **READ:**
>
> ```
> Nothing in this subdivision prevents the payment of a retirement allowance to a member at any time after the member has filed an application for a disability retirement allowance under this chapter and before the Board has granted or denied it, and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member during that time.
> ```
>
> **It says exactly what (c-2) says and removes the word *"pending"* from subdivision G 2 entirely**,
> so subsection G defines the term once. **It changes no outcome against (c-2) as applied.** Its cost
> is that it is a rewrite of item 46's own sentence rather than an addition beside it, and (c-2) was
> preferred precisely because it confirms item 46 exactly as enacted. **That trade is the Director's.**

**What I have done instead, and it is not nothing:** M2 is a **must-appear item for the Editor** and
for the designation-review read-through, in the Director's own framing from their disposition of
question 1 — *subsection G will define "pending" twice, differently, in adjacent subdivisions,
deliberately* — now with counsel's failure scenario attached, so the person reading it understands
what goes wrong if the divergence is taken for a slip.

### 18.7 S6 — the forfeiture that runs from mailing. **Candidate 164-15, HELD. Question 1**

**Counsel is right that this is new, and right that it is mine rather than the base's.** Before this
cut a member who never received an R-6 notice lost nothing she could have had. After 164-8 she loses
the refiling right — and clause (iv), the disclosure written to warn her, is printed in the document
that did not arrive. The giving rule makes the notice *"given"* on the date the Board **mails** it;
the window closes 33 days later.

**I have not applied a cure, and the reason is that every form of it adds a figure.** The section's
non-receipt exposure is general; 164-8 is the first provision to attach a forfeiture to it. A cure
has to choose how long the member gets after actual receipt and what the outer bound is, and **an
outer bound I choose is exactly the kind of number MOO-209's F5 caught me describing as already in
the section when it was not.** So it is drafted, held, and put to the Director with the number
visible.

> **Candidate 164-15 — HELD. It amends Edit 164-8's own new text, so its FIND resolves 0 times in the
> base and once in the applied text — both asserted.**
>
> **FIND:**
>
> ```
> no later than 30 days after the Board gives the notice; and a notice so filed
> ```
>
> **READ:**
>
> ```
> no later than 30 days after the Board gives the notice or, where the Board mails the notice and the member does not receive it within that period, no later than 30 days after the member receives it and in no case later than 90 days after the Board gives the notice; and a notice so filed
> ```
>
> **+210 characters.** The 90 is a **chosen outer bound**, stated as a chosen outer bound: the section
> uses 90 days elsewhere, and that is a reason to prefer 90 over 80, not a reason to call this figure
> a restatement of the section's arithmetic. **If it is taken, clause (iv) must be conformed in the
> same cut** — otherwise the disclosure understates the right, which is M1 again.

### 18.8 S4 — the enforcement claim is withdrawn, counted at 0, and the cure is drafted and held. **Question 2**

**I told the Director that subsection J's report reaches *"every failure … to state a matter this
section requires to be stated."* That phrase is not in subsection J. Counted: *"failure to state"*
0, *"requires to be stated"* 0.** J 1's relevant limb reports failures *"within a period required by
this section"* — **lateness, not content** — and its other limb is a pointer to provisions that
expressly route something into the report. **Nothing routes a failure to state clause (iv) there.**
The withdrawal is at §18.14 and the two counts are in the verifier.

**What survives, and what does not:**

| failure | reviewable under M 2 | in the J report |
|---|---|---|
| to state clause (iv) in a **notice** | **yes** | no |
| to state clauses (i)–(iv) in the **written statement** | **no** | no |

M 2's trigger reaches *"a certification or notice"*; subsection A's giving rule treats *"a written
statement, notice, or certification"* as three species; and the written statement is the document the
member actually reads and the one the filing clock runs from. **Most of this is a base defect and
counsel does not ask me to fix the base. But 164-13 enlarges an unenforceable duty**, and that part
is mine.

> **Candidate 164-17 — HELD, modelled sentence for sentence on D 1's own certification provision,
> which is the only model in the subdivision. It is inserted after the disclosure sentence, so its
> FIND is Edit 164-13(b)'s own new tail — 0 in the base, 1 in the applied text, both asserted.**
>
> **Candidate 164-17 — HELD. The text:**
>
> ```
> A failure to state in the written statement required by that definition, or in any notice of a kind described in the preceding sentence, every matter this subdivision requires to be stated in it is a failure of the Board to state in a certification a matter this section requires to be stated in it for the purposes of subsection M; a person adversely affected by it may seek review under subsection M no later than 30 days after the date on which the written statement or notice is given to the member; and the Board shall state every such failure in the report required by subsection J.
> ```
>
> **+589 characters**, inserted after the disclosure sentence. It creates no new duty: it supplies a **route** for a duty D 1 already imposes,
> using the deeming D 1 already uses for the certification. **Who, what, by when, or else** are all
> present, and all four are lifted from the model.

**Why it is held and not applied.** It reaches the **written statement**, which no edit in this cut
amends, and it imports the whole of subsection M's review machinery into a document that has never
had it. That is a widening of the bill's remedial footprint, and counsel says in terms that the
Director decides whether it is a MOO-164 item or a new issue. **I recommend taking it here rather
than opening a new issue, because the written statement's disclosure duty is the one 164-13 just
enlarged and splitting the two is how a duty and its remedy end up in different passes.**

### 18.9 M4 — the inference the asymmetry invites is **inert**, and that is counted

Counsel's M4 accepts §17.3's reason for the asymmetry and says, rightly, that a reason is not an
answer to a reader who has only the text. Their failure scenario is *expressio unius*: a court holds
that R-6, being excepted from 164-7's saving and not from Edit 1's, is deliberately **not** excepted
from Edit 1's.

**Assume the court so holds. Nothing follows.** After MOO-141's Edit 2 at **their** revision 8, R-6's
deadline in Edit 1's class — the Board that acts more than once **and decides** — runs from *"it
gives its decision upon the request,"* and the residual limb that keys it to an act is confined on
its face to the two classes in which **no decision is ever given**, which are 164-7's own classes and
not Edit 1's. **Edit 1's deeming therefore cannot reach R-6's deadline whether or not R-6 is excepted
from Edit 1's saving.** The verifier applies MOO-141 Edit 2 revision 8 beside this cut and counts
all three limbs.

**That is not a reason to leave the two sentences unlinked, and I have not**: the Director's §3.3
cross-reference is applied at §18.5. It is a reason the Editor's risk note can say the exposure is
legibility rather than outcome. **M4 stays a must-appear item in the memo's risk section, in
counsel's words and not mine.**

### 18.10 m3 — recorded, no text

Counsel's m3: in the no-act branch the deeming buys the member nothing on the **date** itself,
because R-5b fixes it by reference to *"the month in which that period expired"* and does so
*"notwithstanding any other provision of this definition,"* so R-5b beats R-5a's deemed act. Counsel
says it is not a defect — the texts resolve — and I agree. **164-7's value in that branch is the
notice duty, which is S3's subject.** Recorded here so the next reader does not find it and think it
was missed.

### 18.11 S5 — the consistency check is rewritten, and counsel's harness is run against the new one

**This is the finding I am most glad of, because the old script was the thing standing between a
re-cut document and a wrong recommendation, and counsel broke it three ways while it printed
*"0 mismatch(es)"*.** All five fix directions are taken:

| | S5's direction | What `check_doc_vs_kit.py` now does |
|---|---|---|
| (a) | scan the whole document, whitelist by label | scans every fenced block in the document, not §3 |
| (b) | assert nothing is silently dropped | **every fence must be accounted for** — labelled FIND/READ, or matched against an explicit allow-list of labelled non-edit quotations. An unaccounted fence is a failure |
| (c) | assert alternation and check the **pair** | pairs each FIND with the READ that follows it and checks the **pair** against the kit, so counsel's swap fails with *"both are in the kit but are NOT PAIRED there"* |
| (d) | anchor the marker regex | a label must **begin a line** and its bold content must **end** with FIND or READ. `ALREADY`, `SPREAD`, `FINDING`, `FINDINGS` and prose such as *"The FIND is the full clause"* no longer match |
| (e) | assert the stated deltas | every *"+N characters"* figure within 700 characters after a kit READ block must equal `len(READ) − len(FIND)`; and the document must state the patch total |

**Two further things the rewrite does, neither of them asked for.** The kit is now **imported** by
`apply164.py` rather than copied into it — through revision 7 the applier held its own copy of the
edit table, described in its docstring as *"lifted verbatim,"* which is the same shape of claim as
MOO-209's F19 and is unprovable by construction. **An import cannot differ from its source.** And
`repro72.py` now carries its own post-conditions: each revision-8 text asserted present once in the
splice, each superseded form asserted absent from every reproduction.

**The fourth thing counsel found — the one block in §3 the old extractor silently dropped — is gone**,
because the new capture takes plain and blockquoted fences alike and then proves the arithmetic:
every fence is either labelled or allow-listed, and the counts are printed.

**Counsel's own harness is re-run against the rewritten check, and it earned its keep immediately.**
`break_check_rev8.py` reproduces all three of S5's mutations against `moo164_rev8.md` and adds a
fourth for fix direction (e) — a per-edit delta mis-stated beside its own READ block. **On the first
run the rewritten check caught three of four and missed the delta**, because the delta window started
at the fence's own offset and a 1,200-character READ block consumed all 700 characters of it before
the prose stating its figure began. **That is the same failure mode as the thing the script exists to
catch: a check that looks in the wrong place reports success.** Fixed, and the harness now reports
**0 mutations the check cannot see**, with the baseline document passing.

**And one real defect the harness found in the document rather than in the script.** §3.12's
*"who, what, by when, or else"* gave the **or else** as subsection J's report, quoting the phrase S4
shows is not there — the same false claim as §17.4's, one section earlier, which I had not spotted
when I wrote §18.8. **Both are withdrawn at revision 8.** §18.14 item 12.

### 18.12 The base at store revisions 71 and 72, and the verification

| Doc revision | Store revision | §1 chars | What it did |
|---|---|---|---|
| 88 | 70 | 132,557 | the base revision 7 was cut and verified against |
| 89/90 | **71** | **134,012** | **thirteen substitutions in §1** — [MOO-210](/MOO/issues/MOO-210)'s R2, R5 and R6 and nine of [MOO-200](/MOO/issues/MOO-200)'s findings — in **G 4**, the **certification**, **subsection N** and the **title line** |
| 91/92 | **72** | **134,012** | **record only.** [MOO-211](/MOO/issues/MOO-211)'s counsel pass disposed into the record |

**Store revision 72's "record only" is proved rather than taken on trust:** the verifier compares
enacted §1 against the store-revision-71 copy and asserts byte-identity. **§6 is stale for the ninth
time behind anchors that all still resolved exactly once**, and `repro72.py` re-splices every
provision **by content, not by line index**.

`verify_r72_v8.py`, run against `bill72.md`: **0 failures.**

- **Thirteen FINDs, three bases** — store revision 72 as it stands, and with the MOO-141 patch
  carrying Edit 3 at **30** and at **120** days — **every one exactly 1 in enacted §1, and the delta
  is +4,210 on all three.** **So this cut is still order-independent of the MOO-141 patch and still
  indifferent to the 30/120 answer**, now at a **sixth** store base.
- **The per-substitution deltas are summed by the script and asserted against the measured total**,
  so §3's table is counted and not added up by hand.
- The MOO-141 fixture is **cross-checked against their own published +847** rather than trusted.
- `apply164.py`: **+4,210, everything outside §1 byte-identical**, four typographic apostrophes
  normalised. The apostrophes are still **four** and still all inside **G 4**.
- `check_doc_vs_kit.py`: **0 mismatches**, on the rewritten check.
- **Five of the thirteen FINDs still resolve more than once whole-document** — 164-10's four times.
  **§1-only slicing remains the thing most likely to prevent actual damage** (MOO-187 F21).
- **One figure this document quotes has moved with the base and is corrected:** *"no later than"* in
  §1 was **74** at store revision 70 and is **76** at 71 and 72.

### 18.13 Questions for the Policy Director — **three**

1. **Candidate 164-15 (S6) — the non-receipt saving on s12's 30-day window. I recommend taking it.**
   It is the only place this cut turns a notice the member may never see into a **forfeiture**. It
   adds a **chosen** outer bound of 90 days and I will not choose a figure on my own authority after
   F5. **+210 characters, and clause (iv) must be conformed in the same cut if it is taken.** §18.7.
2. **Candidate 164-17 (S4) — the failure-to-state and J-report route for the written statement and
   the notices. I recommend taking it here rather than opening a new issue.** It creates no duty; it
   supplies a route for a duty D 1 already imposes, on D 1's own model. **+589 characters.** Counsel
   routes the here-or-elsewhere choice to you expressly. §18.8.
3. **Candidate 164-18 (M2) — the one-concept-one-word alternative. No recommendation: it is the
   (c-2) trade re-opened and that trade was yours.** It removes *"pending"* from G 2 altogether, so
   subsection G defines the term once, and it changes no outcome. Its cost is that it **rewrites
   item 46's own sentence** instead of adding beside it. §18.6.

**And one thing that is not a question but needs saying to the Editor**: counsel's §5 names **S4**,
**S2** and **M4** as must-appear items in the memo's risk section. S2 is cured in the text at
revision 8; **S4 and M4 are not, and M2 should join them** if candidate 164-18 is declined.

**One handoff that is not mine and is recorded so it is not lost:** counsel asks the **Statutory
Researcher** to record one citation failure — the phrase attributed to subsection J is not in
subsection J, counted 0. That is the same fact as S4 and it is in this document at §18.8.

### 18.14 Statements corrected in place at revision 8

| | Where | What it said | What it says now |
|---|---|---|---|
| 1 | §3.7, §6.6, §13.7 | 164-7's exception names R-6 by the paraphrase *"to give the member written notice of the member's final qualifying retirement date"* | the determinate descriptor, **S3** |
| 2 | §3.7 | **245 words, +1,337** | **372 words, +2,004** |
| 3 | §3.8, §6.3, §13.5 | *"any notice described in the preceding sentence"* | *"any notice **of a kind** described …"*, **S1** |
| 4 | §3.8, §6.3, §13.5 | *"after the member's retirement has taken effect"* | *"after the member has retired"*, **m1** |
| 5 | §3.8 | **97 words, +621** | **106 words, +613** |
| 6 | §3.12, §6.3 | clause (iv): the bar after the grant, and no timeliness or supersession limb | the bar in the trigger; both limbs stated — **S2**, **M1** |
| 7 | §3.12 | **+454**; Edit 164-13 totals **+557** | **+564**; **+667** |
| 8 | §3.11, §4.2, §6.4 | 164-12: *"such an application is pending"* | the noun phrase written out, **M3** |
| 9 | §3.11 | **30 words, +167** | **41 words, +233** |
| 10 | §3's table, the banner, the order block, §17.11 | **+3,375** | **+4,210** |
| 11 | §17.1 | the extension of the exception described as reaching R-6 and nothing else | it reached R-3 and R-4b too; **S3**, and the two rival referents are counted |
| 12 | §3.12, §17.4 | the *"or else"* of Edit 164-13 given as subsection J's report, *"which reaches 'every failure … to state a matter this section requires to be stated'"* | **withdrawn at both sites.** The phrase is not in subsection J; counted **0** and **0**. The consequence is restated as what the base supplies: M 2 for a **notice**, nothing for the **written statement**. **S4** |
| 13 | §17.11, §18.12 | *"no later than"* in §1 = **74** | **76** at store revisions 71 and 72 |
| 14 | §17.11 | the base at store revision 70, §1 **132,557** | store revision **72**, §1 **134,012**; §6 re-spliced the ninth time |
| 15 | the caveat and the header | two counsel passes; revision 7's texts unreviewed | **three** passes; **revision 8's** new and re-cut texts unreviewed |

### 18.15 Status

**Reassigned to the Policy Director with the three questions at §18.13.** MOO-214 is `done`; its
thirteen findings are folded and none is rejected.

**What has not been read adversarially.** Revision 8 re-cuts four substitutions and adds four held
candidates. **The S3 descriptor, the m2 sentence, the §3.3 cross-reference, clause (iv) as re-cut and
candidates 164-15, 164-17 and 164-18 have not been read by anyone but me.** Two counsel passes in a
row found a serious defect in a cure I had drafted from a finding somebody else named — MOO-209's F19
and MOO-214's S3 are the same shape of error — so **I would expect a third pass to find something,
and I would rather it ran after the three questions are answered than before**, because two of the
three change the text.

**Nothing applied to the store. Nothing in this document authorises applying anything.**
