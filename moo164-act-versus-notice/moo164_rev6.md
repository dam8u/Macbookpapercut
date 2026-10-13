# MOO-164 — "acts upon" and act-versus-notice, decided once: **two decisions, ELEVEN anchored edits at revision 6, one candidate still held, and one candidate retired**

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared
by counsel — [MOO-187](/MOO/issues/MOO-187) is an internal adversarial pass by a colleague and is
expressly not legal advice. Nothing here states or implies that counsel or Division of Legislative
Services has cleared it, and no part of it is legally sufficient for introduction. Pre-decisional and
internal.**

**Drafting Specialist · 12–13 October 2026 · cut against `bill-text-s8` [MOO-42](/MOO/issues/MOO-42).**

> ## REVISION 6 — the Policy Director's disposition, folded in
>
> **[`moo164-policy-director-disposition`](/MOO/issues/MOO-164#document-moo164-policy-director-disposition)
> answered all eleven questions and sent none back.** Revision 6 does the six things it asked for and
> nothing else. **§16 is the only part of this document added at revision 6**, and every statement in
> §0 to §15 that the disposition or the base made false is corrected **in place** and listed in a table
> at **§16.7**.
>
> | | Folded in at revision 6 | Where |
> |---|---|---|
> | 1 | **Candidate (c-2) applied** as **Edit 164-12**; (c-1) and its pricing retired to the record | §3.11, §4 |
> | 2 | **164-7 (with F19's limb (B)), 164-7-B, 164-8, 164-10 and 164-11 promoted** from held to applied | §3.7–§3.10 |
> | 3 | **164-9 stays held**, cross-referenced to [MOO-204](/MOO/issues/MOO-204) | §16.4 |
> | 4 | **§6 re-spliced from store revision 68, by content** — the sixth stale reproduction | §6 |
> | 5 | **§3.1's derivation of the 48-day cap re-cut**; clause (ii)'s bound restated as **300 days, unconditionally** | §16.2, §16.3 |
> | 6 | **Question 5's item and the case-decision asymmetry routed** to [MOO-42](/MOO/issues/MOO-42)'s §7; [MOO-141](/MOO/issues/MOO-141) told its Edit 1 FIND is dead | §16.5 |
>
> **The patch is now eleven edits and the delta is +2,551 characters, not +642.** Every figure in §16 is
> **counted** by `verify_r68_v6.py`, which reports **0 failures** at store revision 68.

**History of the cut.** Revisions 1 and 2 cut six edits against **store revision 61**; **§13** re-verified
at store revisions 62 and 63 and decided F-9's narrow side; **§14** took **§7 item 130's residual** with
all three limbs in front of it on the Policy Director's decision of 17:57; **§15** answered
[MOO-187](/MOO/issues/MOO-187)'s **26 counsel findings**, re-cut Edits 164-1 and 164-2 and revised
candidate 164-7 at **store revision 65**; **§16** is revision 6 at **store revision 68**. **The base has
moved thirteen times under this cut.** Disposes of the six MOO-141 residual cards (b), (c), (f), (h),
(i), (j); carries pass 18's **F-9** (card (k)) and **F-5** (card (l)) as the Policy Director directed on
[MOO-162](/MOO/issues/MOO-162); and performs the §6.7 apostrophe normalisation as a recorded
non-substantive item.

---

## ⚠ APPLICATION ORDER — ON THE FACE OF THIS DOCUMENT

**Application of the MOO-141 patch does not precede this cut carrying F-9.** This cut carries it. That
condition is satisfied by this document.

**RESTATED AT REVISION 6 for eleven edits at store revision 68.** Every one of the eleven FIND strings
below resolves **exactly once** in enacted §1 in each of **three** bases, with the **identical +2,551
delta** in all three:

| Base | Eleven FINDs | Delta |
|---|---|---|
| `bill-text-s8` store revision 68 as it stands | all 1 | **+2,551** |
| store revision 68 + MOO-141 patch **revision 5** (Edit 3 at 30 days) | all 1 | **+2,551** |
| store revision 68 + MOO-141 patch **revision 6** (Edit 3 at 120 days) | all 1 | **+2,551** |

**So this cut is order-independent of the MOO-141 patch and indifferent to the 30/120 answer.** That has
now held across **five** base moves and two patch revisions. Either patch may be applied first, and
nothing here needs a re-cut if the figure moves again. §11 carries the original run and **§16.6** the
revision-6 one.

> **⚠ THE MOO-141 PATCH ITSELF HAS A BROKEN ANCHOR AND IT IS NOT THIS CUT'S.** Store revision 68 re-cast
> subsection A's three-day sentence — it is now confined to **mailing** and the triplet *"statement,
> notice, or certification"* replaces *"that statement or notice."* **MOO-141 Edit 1's FIND string
> resolves 0 times.** `verify_r68_v6.py` keeps the dead string and asserts it at **0** so the break stays
> visible, and carries a working repair **solely** so the order-independence test above can be run.
> **MOO-141 must re-cut its own Edit 1; this cut does not do it for them.** Edits 2 and 3 still resolve
> exactly once. §16.5.

**One fact the applier needs: apply every FIND inside enacted §1 only.** Five of the eleven FIND strings
also occur in the §0 revision narrative of the store document — 164-10's resolves **four** times
whole-document — so a whole-document find-and-replace would edit the **record** as well as the bill.
`apply164.py` slices §1 before substituting and asserts byte-identity outside it. This is
[MOO-187](/MOO/issues/MOO-187) finding **F21**.

---

## 0. In one page

**The shape the Policy Director asked for: two decisions, then the drafting falls out.** Both questions
are answered once, in one place, and every one of the eight items is disposed of against those two
answers and against nothing else.

### 0.1 Decision 1 — what it is to "act upon" a request

**Do not define the verb. Repair the endpoints where a token action costs the member something.**
Cards (f) and (i). Four options priced at §1.1; option **(f-4)** recommended.

The reason is arithmetic, not taste. I classified **all 19** `act/acts/acting/action upon` occurrences in
enacted §1 (§7.1). A substantive definition of the verb would move **every** one of them, and three closed
decisions are priced on the first-action event: MOO-141's patch direction (78 days at `F = 7`, `D = 85`),
[MOO-140](/MOO/issues/MOO-140)'s settled C2 answer, and [MOO-163](/MOO/issues/MOO-163)'s **$0** on Edit 3.
It would also lengthen every link in the uncapped chain pass 18 found at F-6 — **firing card 4's first
trigger by drafting rather than by pricing**, which is the one thing the Director's disposition of F-6
says not to do.

**CORRECTED AT REVISION 5 — [MOO-187](/MOO/issues/MOO-187) F1.** Revisions 1 to 4 said here that
*"exactly one act-keyed endpoint remains where a token action can still cost anybody anything."*
**That was false and it was the headline Decision 1's recommendation was argued on. Two remain.**

1. **Edit 3's D 4 / D 5 retention** — queue position only, with D 5 preserving every subsection B
   standard-cost right.
2. **Edit 164-1's own 48-day cap**, which is measured from the Board's **acting** and is therefore
   reached by the MOO-141 patch's Edit 1 exactly as the floor is. On MOO-141's facts (`F = 7`, `D = 85`)
   the cap fixes the tolling endpoint at **day 55**, thirty days before the Board tells her anything.

**So Edit 164-1 repairs 18 of card (f)'s 78 days and leaves 60.** That is a **disclosed policy choice**
— §9.3 said so in terms, and §2.2 prices the movement at +18 days precisely because the cap holds it
there — but it is not a closed endpoint, and this document must not say it is. **Candidate 164-9 at
§15.4 is the five-word change that would close the remaining 60 days, and it is question 7.** The cost
of being wrong on Decision 1 is the retention row **plus** up to 60 days of tolling per request at the
M 2 endpoint that the cap declines to restore.

**The figure for that row is live and I am not going to quote a stale one.**
[MOO-163](/MOO/issues/MOO-163) released **$0 at the central estimate** for the retention at **30 days**.
The board has since answered **120 days** ([MOO-176](/MOO/issues/MOO-176)), and
[MOO-177](/MOO/issues/MOO-177) and [MOO-180](/MOO/issues/MOO-180) own what that does to the register and
to the price. **Nothing in Decision 1 turns on which figure it is**: the row is queue position in both
cases, D 5 preserves the standard-cost right in both, and the recommendation would be the same at $0 or
at MOO-163's high-take-up bound of `|Δ| < $204,000` of lapse. **What would change the recommendation is a
finding that the retention costs a member her purchase, and D 5 is why it does not.**

### 0.2 Decision 2 — does a clock run from the act or from notice of it

**From the act, except where the period is one within which a person must act — then from notice. That is
already the bill's own rule, in three places, and I am conforming three stragglers to it rather than
inventing a rule.** Cards (b) and (h), and card (c) sits next to both.

The bill's rule, as enacted: M 2's own 30 days to seek reconsideration run *"after the notice of the
determination is given"*; the definition's two floors run from the month in which the Board **gives** a
statement, a decision or a notice; and subsection A's mailing extension reaches *"every period within
which a person may or must act that runs **from the giving of** that statement, notice, or
certification."* **Card (b)'s defect is that the one period that does not run from the giving of a notice
is thereby the one period the mailing extension cannot reach.** That is not a policy gap. It is a
straggler.

**CORRECTED AT REVISION 6 — the quotation, not the argument.** Store revision 68 re-cast that sentence:
the extension is now confined to **mailing**, and a new express giving rule in the same paragraph covers
statements, notices **and certifications**, with a 5:00 p.m. electronic cut-off. **Decision 2 now has
six sites in the bill, not three**, and the two newest — D 1's certification-failure clock and G 4's
§ 51.1-162 C waiver floor, both added by store revision 62 — were drafted by somebody else. §16.3.

### 0.3 The eight items, disposed — and the five promotions at revision 6

**REVISION 6: the patch is eleven edits.** The eight items below are unchanged; what changed is that
five things this document carried as **candidates** are now **applied text**, on the Policy Director's
disposition. The disposition's own table is at §16.1 and the new edits at §3.7–§3.11.

| | Promoted at revision 6 | Now | Words | Chars |
|---|---|---|---|---|
| **164-7 + 164-7-B** | item 130's residual, route (c) — the deemed act, two triggers | **Edit 164-7** | 217 | **+1,153** |
| **164-8** | D 1's filing vehicle | **Edit 164-8** | 81 | **+485** |
| **164-10** | M 2's 90-day duty gets a commencement | **Edit 164-10** | 5 | **+27** |
| **164-11** | M 2's expiry-notice sentence conformed | **Edit 164-11** | — | **+24** |
| **(c-2)** | G 2's own pendency endpoint | **Edit 164-12** | 38 | **+220** |
| **164-9** | the 48-day cap's remaining 60 days | **still held** — [MOO-204](/MOO/issues/MOO-204) | 0 | 0 |
| **(c-1)** | G 4's definition extended to the subsection | **retired to the record** | 0 | 0 |

| | Item | Disposition | Words |
|---|---|---|---|
| **(f)** | Token action ending a period | **Option (f-4): no definition; endpoint repair.** §1.1–§1.2 | 0 |
| **(i)** | Is *"acts"* too thin a verb for M 2's 90-day duty | **Closed on the merits, no text.** The confirming sentence is drafted at §1.3 and I recommend against it, for item 123's reason | 0 |
| **(b)** | M 2's 30 days run from the act, not from notice | **Cured, Edit 164-1**, re-cut at revision 5 on F8, F18 and F23; bounded at **+18 days** and priced | 46 |
| **(h)** | G 2's notice floor — worse off the faster the Board moves | **Cured, Edit 164-2**, re-cut at revision 5 on F3, which showed the 38-word version was a no-op. The irreconcilable pair is identified at §2.3 | 59 |
| **(j)** | M 2's stranded *"the 90 days allowed by this subsection"* | **Cured, Edit 164-3**, on G 4's own precedent | 11 for 7 |
| **(l) / F-5** | R-5's period | **Cured, Edit 164-4.** And it is the answer to the no-decision residual, §2.4 | 5 |
| **(k) / F-9** | D 1's descriptor | **Cured, Edit 164-5**, as the Director worded it | 4 |
| **(c)** | G 2's two uses of *"pending"* are undefined | **CURED AT REVISION 6, Edit 164-12 = candidate (c-2).** (c-1) is retired. **No item-46 card goes to the board**, and §16.1 says why that is a decision and not an omission | 38 |
| — | **Conforming amendment** | **Edit 164-6**, so one concept has one formula at all three sites | 4 |
| — | §6.7's four apostrophes | **Normalised, recorded, folded into no amendment.** §8 | n/a |

**+2,551 characters of amendment across eleven edits at revision 6.** It was **+642** across six at
revision 5 and **+490** before Edits 164-1 and 164-2 were re-cut. The per-edit arithmetic is at §16.6,
and every figure there is counted by `verify_r68_v6.py` rather than predicted. **Nothing applied to the
store.**

### 0.4 What I did not do

- **Card C is not drafted.** The no-decision residual is disposed to [MOO-42](/MOO/issues/MOO-42) §7
  item 124 and is not mine to re-decide. I hold card C as the fallback only. **But §2.4 shows F-5's five
  words give the member a floor in the no-decision case whether or not item 124 is enacted**, which is the
  one answer the Director asked F-5 and the residual to share.
- **No cap on Edit 3's retention.** F-6 declined on the released price. No cap text, on either named
  trigger, until a trigger fires and the Director says so.
- **The old lettering's card (l)** — the F-6 sign flip, closed at 129 against 128 — is not reopened.
- **No argument anywhere in this document rests on "where the Board does not do so."** The
  condition-precedent argument is withdrawn and I have not rebuilt it. Cards (f) and (i) are decided on
  the 19-occurrence classification and on the three released prices, and on nothing else.
- **The §0.2 call is not reopened.** One pendency event, two endpoints. Decision 1 keeps the event where
  the Director put it; Decision 2 repairs endpoints, which is what *"two endpoints"* reserves to each
  provision.
- **No enactment clause, no effective date, no sunset, no severability.** §5.

---

## 1. Decision 1 — what it is to "act upon" a request. Cards (f) and (i)

### 1.1 The four options, priced against each other

**The question.** Edit 1 stops a token action **discharging a duty** — its saving sentence does that in two
limbs, and both passes confirmed the limbs hold. It does **not** stop a token action **ending a period**.
Does a bare acknowledgment count as the Board's acting upon a request?

**Option (f-1) — nothing. Leave Edit 1 as drafted and leave every endpoint act-keyed.**
*Price:* the member loses `D − F` days at every endpoint that runs in her favour — 78 days on MOO-141's
own facts (`F = 7`, `D = 85`) at M 2's tolling endpoint, which is the endpoint that carries her retirement
deadline and every period within which she must act. **Rejected.** 78 days is not a rounding error, and
the defect is curable in 44 words at one site.

**Option (f-2) — define the verb substantively, once, in subsection A's interpretation paragraph.**
Drafted, and I am not recommending it:

> <u>For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, the Board acts upon a
> request when it makes a determination granting or denying the request in whole or in part, and no
> acknowledgment of the receipt of a request, no request by the Board for further information, and no
> other action of the Board that does not determine a request in whole or in part is an acting upon the
> request.</u>

*Price, and this is why it loses.* It moves **all 19** occurrences, not the one that hurts:

1. **It reverses the direction of effect the MOO-141 patch was priced on.** The patch moves the tolling
   endpoint from the decision to the first action. Making the event substantive moves it back. Three
   closed decisions are priced on the first-action event — MOO-141's 78 days, MOO-140's C2, and
   MOO-163's **$0** on Edit 3 — and all three would need re-pricing.
2. **It fires card 4's first trigger by drafting.** Pass 18's F-6 found Edit 3's retention carries
   **neither** of the tolling sentence's two limits and chains without bound. A substantive event
   lengthens **every link** in that chain. The Director declined the cap on the released price; a verb
   definition would make the thing the cap was declined for larger.
3. **It lengthens G 4's non-running** of the Board's own 60-day and effect-date periods, which is adverse
   to the member at G 2, bounded at 120 days by G 4's own aggregate.
4. **It would need the word *"application"* as well as *"request"* to reach G 4's pendency definition**,
   and §0.3 of the MOO-162 disposition has just decided that *"or an application"* stays deleted. Adding
   it back on the event side, one revision later, is how a record stops being readable.

**Option (f-3) — define the verb substantively for duties only.** *Price: zero, because it is already
done.* Edit 1's saving sentence is exactly this, in two limbs. Option (f-3) is a re-draft of enacted text.
**Rejected as redundant** — and the redundancy is card (i), which §1.3 closes.

**Option (f-4) — leave the verb alone; repair the endpoints at which a token action costs the member
something. RECOMMENDED.**

*Price: 44 words at one site, +18 days of exposure, and a residual of $0.* The classification at §7.1 is
what makes this a finite claim rather than a hope. Of the 19 occurrences, **five** are endpoints a token
action can move. After Edit 164-1 they stand as follows:

| Endpoint | Act-keyed after this cut? | Who it moves against | Residual |
|---|---|---|---|
| M 2 tolling endpoint (#15) | **Partly — CORRECTED at revision 5, F1.** Edit 164-1's floor **and** its 48-day cap are both measured from the Board's acting | the member | **18 of 78 days repaired; 60 days of residual, disclosed.** Candidate 164-9 at §15.4 closes it; question 7 |
| The definition's reset, *"the month in which the Board last acts"* (#2) | Yes | the member | **neutralised downstream** by the decision-keyed floor (the Director's own §2.3 finding), and in the no-decision case by R-5 as cured by Edit 164-4 — §2.4 |
| G 4's pendency, *"first acts upon it"* (#12, #13) | Yes | **the Board** — its periods resume earlier | favourable; no repair wanted |
| M 2's 15-day application-duty **trigger** (#19) | Yes | the applicant, favourably — day 37 rather than day 100 | decided at MOO-162 §0.3; not mine |
| Edit 3's D 4 / D 5 retention (#17) | Yes | the applicant, in queue position | **queue position only**; D 5 preserves standard-cost rights. Figure live at [MOO-177](/MOO/issues/MOO-177) / [MOO-180](/MOO/issues/MOO-180) after the 120-day answer |

**So the cost of being wrong on Decision 1 is the last row.**
[MOO-163](/MOO/issues/MOO-163)'s released price for it, at Edit 3's **30-day** retention, was zero at the
central estimate, `|Δ| < $204,000` of lapse over 48 months at 112.3% take-up, and displacement of
0.11–0.14 members mean. **At 120 days the figure is being re-examined on
[MOO-177](/MOO/issues/MOO-177) and [MOO-180](/MOO/issues/MOO-180) and I do not restate it as though it
still applied.** If MOO-49 lands broad, that row re-opens as well — and it re-opens as card 4, which is
already recorded, not as a new finding.

**One point about (f-4) and the *Forst* identity, re-stated for revision 6.** Pass 18 relied on an
identity between M 2's two endpoints: *"under Forst the identity is what secures the same meaning for
both."* **That identity is already gone, and not by anything in this cut.** The board's 120-day answer
makes Edit 3's retention read *"until 120 days after the Board acts upon the request"* against the
tolling sentence's 30, and [MOO-176](/MOO/issues/MOO-176) records the identity as gone with **Edit 1's
express deeming** named as what carries Edit 3 instead.

**What Edit 164-1 does about that is preserve the limb the deeming attaches to.** Clause (a) keeps
*"30 days after the Board acts upon the request"* word for word, so Edit 1's deeming still reaches the
tolling endpoint exactly as it reaches the retention; the notice limb and the 48-day cap are added
**around** it, not in place of it. **Verified on the revision-6 base**: the phrase
*"120 days after the Board acts upon the request"* appears once and
*"30 days after the Board acts upon the request"* appears once, each in its own sentence, and each still
inside Edit 1's trigger.

**The principled distinction, if anyone asks for one:** the retention protects a **queue position**,
where every applicant needs the same certain date, and the tolling protects a person who **must act**,
who needs to know. That is the distinction the bill already draws — see §0.2 — and it is the distinction
the board's own 30/120 divergence now rests on.

### 1.2 Decision 1, recommended, with the cost of being wrong in one line

**Recommend (f-4), and the recommendation survives F1 because neither of F1's two reasons for rejecting
(f-2) depends on the row that was wrong.** (f-2) still re-prices three closed decisions and still fires
card 4's first trigger by drafting.

**Cost of being wrong, restated truthfully at revision 5.** It is **two** rows and not one:

- **the retention** — queue position only; **$0** at MOO-163's central estimate for the 30-day version,
  with the 120-day figure live at [MOO-177](/MOO/issues/MOO-177) / [MOO-180](/MOO/issues/MOO-180); **and**
- **the M 2 tolling endpoint** — **up to 60 days per request** that Edit 164-1's 48-day cap declines to
  restore, bounded, disclosed, and closable by candidate 164-9 if the Director wants it closed.

Cost of being wrong on (f-2) instead: the re-pricing of three closed decisions and an unbounded chain the
Director has already declined to cap.

### 1.3 Card (i) — closed on the merits, and the text I am not recommending

**It can be closed, and it is closed, and the closing does not need a word of new text.** The Director
asked me to close it or to say plainly that drafting cannot. Drafting can — and does not need to.

Three things hold M 2's 90-day duty against a token action, and the third is the one neither pass named:

1. **Edit 1's saving, limb 1** — nothing in the deeming determines *"the date by which the Board is
   required to act upon a request."*
2. **Edit 1's saving, limb 2** — nor *"whether the Board has performed such a duty within a period
   required by this section."*
3. **M 2's own first sentence names the object of the duty.** What the person may obtain is *"written
   reconsideration by the Board **stating the reasons for its decision**."* The 90-day sentence requires
   the Board to *"act upon"* that request; the thing it is required to do is supply the written
   reconsideration the first sentence defines. **A letter acknowledging receipt states no reasons and
   decides nothing.** That is not a saving construction — it is the subsection's own object, and it is why
   both passes could conclude the limbs hold without being able to say why they held.

**The confirming sentence, drafted and recommended against:**

> <u>The Board does not act upon a request for reconsideration for the purposes of the preceding sentence
> unless it gives the person who filed the request its written reconsideration stating the reasons for its
> decision.</u>

**Why I recommend against it.** It is item 123's problem, bought for free. M 2's 90-day duty would become
the one duty in a section carrying **74** *"no later than"* periods and **five** *"shall act upon"*
duties (**74**, not the 72 revisions 1 to 4 quoted — F15; `shall act upon` was right at five) that says what discharges it, and a reader would ask why the others do not — and answer that a token action discharges those. **It also disturbs item 124**,
whose drafted text keys to *"does not act upon a request for reconsideration within the 90 days allowed by
this subsection"*; a confirming sentence here invites the argument that item 124's deemed denial is
triggered by the absence of a **reasoned decision** rather than by the absence of **action**, which is a
larger change than either item intends.

**Card (i) is closed. If the Director wants belt-and-braces, the text above is the text, it is 33 words,
and it goes in after M 2's 90-day sentence and before item 124's new sentence.**

---

## 2. Decision 2 — does a clock run from the act, or from notice of it. Cards (b) and (h)

### 2.1 The rule, and where the bill already has it

**Answer: from the act, except where the period is one within which a person must act — then from
notice of it.** I did not choose that rule. The bill has it in three places already:

- **M 2's own first sentence.** The 30 days to seek reconsideration run *"within 30 days after **the
  notice of the determination is given**."*
- **The definition's two floors.** Both run from *"the month in which the Board **gives** the statement"*
  and *"the month in which the Board **gives** a decision or notice."* Edit 2 moves the backstop onto the
  same formula, which is the Director's own reason for taking card (g): *"the vocabulary is already
  there."*
- **Subsection A's mailing extension.** It reaches *"every period within which a person may or must act
  that runs **from the giving of** that statement or notice."*

**And that third one is card (b), stated exactly.** The period in M 2 that runs from the Board's *acting*
is, for that reason alone, the one period in the section that **the mailing extension cannot reach** — not
because anyone decided she should not have the three days, but because the extension is drafted against
notices and this period is not. **Cards (b) and (h) are stragglers from a rule the bill already applies.
Conforming them is the smallest change that answers the question, and it needs no new concept.**

### 2.2 Card (b) — the 18 days, what the cure costs, and the option I am not recommending

**The defect.** M 2 tolls her final qualifying retirement date and every period within which she must act
*"until 30 days after the Board acts upon the request."* Two gaps run inside those 30 days:

- **Gap (i) — the token action.** Under Edit 1's deeming, *"the Board acts upon the request"* is the date
  it **first** acts. On MOO-141's own facts the 30 days can begin on day 7 and expire on day 37, with the
  decision landing on day 85. **That gap is card (f)'s and Decision 1 answers it** — see below.
- **Gap (ii) — the carded 18 days.** Even keyed to the decision, nothing requires the Board to tell her
  the decision has reset her final qualifying retirement date until **15 days** after it gives the
  decision (Edit 2's backstop) and, where it mails, **3 days** more. **18 of her 30 days can run before
  she can know the date she is now required to retire by.**

**The cure, Edit 164-1, and it closes both gaps at one site in 41 words.** The endpoint becomes the
**later** of 30 days after the act and 30 days after written notice of the decision, **capped at 48 days
after the act**. The cap is not invented: every number in it is already in the section.

> **THE DERIVATION, RE-CUT AT REVISION 6. The figure is right and the old sentence explaining it is now
> wrong.** Revisions 1 to 5 wrote `48 = 15 (Edit 2's backstop) + 3 (subsection A's mailing) + 30` and
> called the 3 an unconditional extension. **Store revision 68 confined the three days to mailing** and
> added an express giving rule with a 5:00 p.m. electronic cut-off, so the derivation has to be done case
> by case. **It still comes to 48, and 48 is still the worst case:**
>
> | How the Board gives the notice | Given on | + 30 | Outer day |
> |---|---|---|---|
> | **Mails** on the fifteenth day — the worst case | day 15 | — | **day 48** (15 + 3 + 30) |
> | Transmits electronically before 5:00 p.m. on the fifteenth day | day 15 | no mailing extension | day 45 |
> | Transmits electronically **after** 5:00 p.m. on the fifteenth day — already a breach of the 15-day duty | day 16 | no mailing extension | day 46 |
>
> **Mailing is the only route that reaches 48, and nothing reaches past it.** The 15 is the definition's
> own notice backstop — *"no later than 15 days after it acts upon the request"* — asserted at count 1
> in `verify_r68_v6.py`, which also asserts the mailing confinement, the giving rule and the 5:00 p.m.
> rule at 1 each. **A notice given late is a breach of the 15-day duty, not an extension of the cap**;
> the cap is precisely what stops the Board's breach from lengthening the member's clock without limit.

**What it is worth, in days, and this is the answer to "say how much before recommending."**

| Case | Tolling ends today | Tolling ends after Edit 164-1 | Movement |
|---|---|---|---|
| Decision and notice together on the day of the act | act + 30 | act + 30 | **0** |
| Notice 18 days after the act (the carded case) | act + 30 | act + 48 | **+18 days** |
| Token act day 7, decision day 85, notice day 85 (gap (i)) | day 37 | day 55 | **+18 days** |
| Board never gives notice | act + 30 | act + 48 | **+18 days, capped.** F23 showed the revision-4 wording (*"the later of (a) … and (b) …"*) did not actually say this — where limb (b) never occurs, *"the later of"* is at least as naturally read as resolving to limb (a), i.e. act + 30. **The revision-5 re-cut at §15.2 states the cap as a freestanding outer limit, so this row is now what the words say.** |

**Maximum movement is +18 days per request, in every case, and clause (ii)'s 120-day aggregate still
binds on top of it.** There is no case in which Edit 164-1 moves the endpoint by more than 18 days.

**What that costs on MOO-140's settled C2 exposure, stated plainly.** The route is G 2's notice floor: a
longer tolling lengthens *"the period allowed to the member by subsection M within which to request
reconsideration"*, the floor is keyed to that period, and so the G 2 determination may not take effect for
18 days longer — and **no retirement allowance is paid until that determination takes effect.** So:
**the zero-allowance window lengthens by up to 18 days, once per request, bounded by clause (ii)'s
120-day aggregate.** G 2's arrears sentence then pays her **every amount** that would have been payable
from her effective date of retirement, so the loss is the time value of 18 days of allowance and the
liquidity, not the benefit.

**Recommend the cure.** She is exchanging **up to 18 days of deferred-but-not-forfeited allowance** for
**up to 18 of the 30 days she has to challenge a determination that cuts her service credit**. The
challenge window is the thing she cannot get back; the allowance is paid either way.

**Cost of being wrong:** 18 days of first-payment deferral for a member who did not need the notice
because the Board had already told her — the top row of the table, where the movement is zero. **The
asymmetry runs in her favour and the cap makes the downside finite.**

**Option (b-2), drafted and recommended against.** Make the endpoint simply notice-keyed — *"until 30
days after the Board gives … written notice of its decision upon the request"* — with no cap and no
retention of the act limb. **Price: it restores the full `D − F` difference, 78 days on MOO-141's facts,
reverses the direction of effect the patch was priced on, re-opens MOO-140's C2 and the retention's
price, and — the point that survives revision 6 — it removes the act limb altogether, so Edit 1's
deeming would no longer reach the tolling endpoint at all.** Rejected for the same reason as (f-2): a
cure the size of the patch is not a cure.

### 2.3 Card (h) — the clearest write-up: the member's protection survives only where the Board breaches

**This is the most counter-intuitive item in the set, so here it is as a pair of mandatory sentences that
cannot both be obeyed.** Both are in G 2 today.

> **The floor.** *"The Board shall give the member written notice of the determination … **no less than 30
> days, and in no case less than the period allowed to the member by subsection M within which to request
> reconsideration of the determination**, before the determination takes effect …"*
>
> **The outer limit.** *"A determination under this subdivision shall take effect no later than 60 days
> after the Board gives the notice required by this subdivision, and **in no event later than 120 days
> after the determination date**, except that where the Board gives that notice **later than** 60 days
> after the determination date, or has not given it within 60 days after the determination date, the
> determination takes effect on the first day on which it may take effect under [the floor], and in that
> case the limit of 120 days … does not apply."*

**The period allowed to her by subsection M is tolled by subsection M.** M 2 tolls *"any period within
which the member or applicant must act under this section"*, and her 30 days to seek reconsideration is
such a period. So the floor is **as long as her tolled window**, and clause (ii) expressly permits
aggregate tolling of **120 days**.

**Worked case. Determination date day 0; aggregate tolling 100 days, which clause (ii) permits.** Her
tolled 30-day window ends on day 130 at the earliest, so the floor forbids the determination taking
effect before day 130.

| The Board gives G 2 notice on | Is the 120-day limit lifted? | Effect date | Outcome |
|---|---|---|---|
| **day 55 — on time** | **No.** The exception needs notice *later than* 60 days | floor says ≥ 130; limit says ≤ 120 | **Irreconcilable** |
| **day 65 — late** | **Yes** | day 130 | **Floor honoured in full** |

**So the member's floor stands only where the Board has breached its own 60-day notice duty, and is
stranded where the Board has complied.** That is the sentence to put in front of anyone who asks why this
matters: **a protection that switches on the agency's breach is not a protection.** And the
opposition's reading is the easy one — a specific outer limit beats a general floor, so cut the floor down
to 120 days. The member's answer is G 2's own self-correction clause (*"a determination that takes effect
in contravention of this sentence takes effect instead on the first day on which it may take effect under
this sentence"*), and she should not have to reach for it.

**The arithmetic of when it bites — CORRECTED AT REVISION 5, [MOO-187](/MOO/issues/MOO-187) F4.**
Revisions 1 to 4 stated the condition as *"wherever `notice day + 30 + T > 120` and `notice day ≤ 60`."*
**That overstates the conflict twice**, and a reviewer who re-runs it gets a different answer from the
document's. Two terms were missing:

- **`T` should be `T_after`** — only tolling that falls **after** notice lengthens her remaining window.
- **G 4's suspension `S` is missing from the right-hand side.** Subdivision G 4's second sentence provides
  that *"[n]o period stated in subdivision 2 … whether it is a period within which the Board is required
  to act or **a period within which a determination is required to take effect**, runs while such an
  application is pending or while a request the filing of which tolls … is pending,"* capped at 120.
  **G 2's 120-day outer limit is such a period**, so it does not run during pendency. §7.3 and §6.5 both
  quote that sentence; §2.3's arithmetic proceeded as though the 120 were a calendar figure.

**Corrected condition: conflict wherever `notice_day + 30 + T_after > 120 + S` and `notice_day ≤ 60`.**

**The worked case above still reproduces** — with tolling on days 0–100 and notice on day 55, `T_after`
is 45, the floor is day 130, and the irreconcilable pair is real. **But it reproduces only where `S` is
small, which is the prompt-token-action class.** `S` is driven by **pendency** (filing → first action);
`T` by **tolling** (filing → the endpoint). Where the Board does not act promptly, `S ≈ T` and the pair
is reconcilable: tolling on days 10–110 with notice on day 55 gives a floor of day 140 against a limit,
as suspended, of day 220.

**So the honest statement of card (h) is narrower than the one revisions 1 to 4 made**, and it is this:
*the member's floor is stranded wherever the Board acts promptly on her request and gives the G 2 notice
on time.* That is the prompt-first-action class — which is [MOO-141](/MOO/issues/MOO-141)'s own class,
and the class this whole issue exists for. **Edit 164-2 needs no change for this finding; the claim did.**

**The cure, Edit 164-2: one more limb on an exception that already exists, 38 words, and the consequence
is already drafted.** The 120-day limit lifts where the floor makes compliance with it impossible — which
is precisely what the limit already does when notice is late. **I am extending an existing exception from
one impossibility to the other, not writing a new rule.**

**Price — CORRECTED AT REVISION 5, [MOO-187](/MOO/issues/MOO-187) F5. The 210 is not an absolute bound
and must not go to the board as one.** Revisions 1 to 4 gave `60 (notice) + 30 (her window) + 120 (clause
(ii)'s aggregate) = 210 days`. **Clause (ii)'s 120 is not a bound on `T`**: the clause excludes from the
aggregate *"any period after the expiration of the [period allowed] … and before the Board acts upon the
request"* — that is, the Board's **own lateness is taken out of its own cap**, and tolling runs through
the excluded interval without consuming it.

**True bound at store revision 65: `60 + 30 + 120 + the Board's lateness in first acting`, and the last
term was unbounded on the face of the text.** Counsel's worked case reached **460 days** on a first
action at day 400, and 4,060 on a first action at day 4,000.

> **CLOSED AT REVISION 6, AND NOT BY ANYTHING IN THIS CUT. THE BOUND IS 300 DAYS, UNCONDITIONALLY.**
> **m8-a is *enacted*.** At store revision 68 clause (ii) closes *"provided that the aggregate of all
> periods so excluded shall not exceed 90 days"* — one occurrence in enacted §1, counted, and it
> **survives Edit 164-3**, which is also counted. So the last term is capped at 90 and
> **`60 + 30 + 120 + 90 = 300 days`, with no condition attached.**
>
> **Everywhere this document previously wrote *"300 days if m8-a lands, unbounded if it does not"* the
> conditional is now stale in the member's favour**, and the Policy Director counted it rather than
> taking my recommendation to wait for it. The places are listed at §16.7. **Question 8 is discharged:
> there is no second instrument to draft here, and I am not drafting one.**

**Three things to say about that, in order of importance.**

1. **The unbounded term is pre-existing and is not created by this cut.** Clause (ii)'s exclusion is in
   the enacted base. **Edit 164-3 does widen its reach**, from one class of request to two — §3.3 says so
   approvingly — so this cut makes an existing unbounded term bite more often. That is the honest
   statement.
2. **Bounding it means touching clause (ii)'s exclusion, which is a larger change than this cut**, and
   I have not drafted it. **CORRECTED AT REVISION 6: question 8 is discharged, because m8-a is no longer
   approved-and-pending — it is enacted.** At store revision 68 clause (ii) itself carries *"provided
   that the aggregate of all periods so excluded shall not exceed 90 days"*, one occurrence in enacted
   §1, counted, and it survives Edit 164-3. **The true bound is `60 + 30 + 120 + 90 = 300 days`,
   unconditionally, and the term is closed by the base rather than by this cut.**
3. **Which way it cuts is unchanged.** The window is already unbounded today in the late-notice case,
   because G 2's existing exception already lifts the limit there. The class this cure adds is the one
   bounded by the same arithmetic as the existing class.

**Recommend the cure. Cost of being wrong:** deferred first payment of `60 + 30 + 120 + 90` days in the
rare case of near-maximal tolling — **300 days, unconditionally, at store revision 68** (RESTATED AT
REVISION 6; revision 5 said *"300 if m8-a is applied, unbounded if it is not"*) — instead of a floor cut
to 120 days by a court. **The alternative cure — computing
the floor *"without regard to any tolling under subsection M"* — is 7 words, keeps the 120-day discipline,
and lets the determination take effect while her tolled right to be heard is still open.** I have not
drafted it as the recommendation because it makes the hearing right nominal in exactly the cases where
tolling exists, and G 4's rescission route restores service credit only **after** she wins.

### 2.4 F-5 and the no-decision residual — one question, one answer, and it holds whether or not item 124 is enacted

**The Director's instruction was to decide F-5 and the no-decision residual in one place with one answer,
and also that the residual is disposed to [MOO-42](/MOO/issues/MOO-42) §7 item 124 and is not mine. Those
two are reconcilable, and here is how.**

**R-5, as it stands, gives the M 2 class nothing.** It reads:

> *Where the Board does not act upon a request the filing of which tolled the running of the member's
> final qualifying retirement date under subsection M **within the period this definition allows for
> acting upon it** …*

**and the definition allows no period at all for an M 2 reconsideration request.** The definition's own
30-day period is for a request to approve a later date. The 90 days for a reconsideration request are
M 2's. So R-5 — the no-action backstop that gives the member a floor at *"the first day of the second month
following the month in which that period expired"* — **misses the entire class of request that M 2's
tolling is mostly about.**

**Edit 164-4's five words fix that**: *"within the period **allowed by this section** for acting upon it."*
This section allows 90 days for a reconsideration request and 30 for a definition request, so R-5 now
reaches both.

**Why that is the same answer as the residual's.** The residual is: Edit 2 keys the member's only deadline
to a *decision*, and nothing requires the Board ever to give one. Item 124 answers it by **deeming the
request denied on the 91st day**. R-5 as cured answers it by **giving her a floor measured from the expiry
of the same 90 days**. The two key to the **identical date** — the expiry of M 2's 90-day period — so:

- **If item 124 is enacted**, she has a reviewable determination on day 91 *and* a floor at the first day
  of the second month after the month in which day 91 falls. The two agree.
- **If item 124 is declined**, she still has the floor. **F-5 is therefore the fallback for the residual,
  and it is a better fallback than card C**, because it is five words in text that already exists and it
  adds no duty to M 2's 90-day sentence.

**That is one answer to one question, and it does not re-decide the residual.** Item 124 remains the
Director's disposition and the gate. **The one thing I would ask the Director to note: F-5 removes the
need to treat card C as the fallback at all.**

---

## 3. The patch — **eleven** anchored edits at revision 6, verified at store revision 68 and on an applied copy

**Whoever applies this must use the FIND strings verbatim, and must apply every one of them inside
enacted §1 only.** Each is counted over §1 of store revision 68, and each is counted **three times** —
on the base as it stands, on the base with the MOO-141 patch at **revision 5**, and on it with the patch
at **revision 6** (Edit 3 at 120 days). **All thirty-three counts are 1, and the delta is +2,551 on all
three bases.** `verify_r68_v6.py` reports **0 failures**; `apply164.py` applies all eleven to a copy and
asserts that everything outside §1 is byte-identical.

| Edit | Site | Card / finding | Chars |
|---|---|---|---|
| **164-1** | M 2, the tolling endpoint | card (b); re-cut on F8, F18, F23 | +233 |
| **164-2** | G 2, the 120-day exception | card (h); re-cut on F3 | +366 |
| **164-3** | M 2 clause (ii) | card (j) | +24 |
| **164-4** | the definition, R-5 | card (l) / F-5 | +1 |
| **164-5** | D 1, the lateness descriptor | card (k) / F-9 | +8 |
| **164-6** | G 4, the period formula | the conforming amendment | +10 |
| **164-7** | M 2, after the enacted denial sentence | item 130, route (c), in 164-7-B's two-trigger form | **+1,153** |
| **164-8** | D 1, the lateness-extension sentence | the filing vehicle | +485 |
| **164-10** | M 2's 90-day duty | F6 — the commencement | +27 |
| **164-11** | M 2's expiry-notice sentence | F12 — the conformed formula | +24 |
| **164-12** | G 2, item 46's carve-out | card (c), candidate **(c-2)** | +220 |
| | | **total** | **+2,551** |

**There is no Edit 164-9.** Candidate 164-9 is **held** for [MOO-204](/MOO/issues/MOO-204) and the number
is reserved for it, so that if the Fiscal & Impact Modeler's pricing comes back and the Policy Director
takes it, the edit arrives under the number this document and the counsel pass already use for it.
**§16.4** states the one thing the applier needs about it: it amends **Edit 164-1's own new text**, so it
cannot be applied to the base, and its FIND resolves exactly once in the **applied** text — counted.

### 3.1 Edit 164-1 — subsection M 2, the tolling endpoint. Card (b)

> **FIND** (count = **1** on both bases):
>
> ```
> tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request
> ```
>
> **READ:**
>
> ```
> tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the Board acts upon the request
> ```

**RE-CUT AT REVISION 5** on [MOO-187](/MOO/issues/MOO-187)'s **F8**, **F18** and **F23**. The
revision-1-to-4 text was:

> ```
> … until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after the Board gives the person who filed the request written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request
> ```

**Three defects, one re-cut, and the endpoint arithmetic is unchanged in every case the old text
actually reached.**

- **F8 — limb (b) keyed the *member's* clock to notice given to *the filer*, who need not be the
  member.** M 2's tolling sentence is unconditional on who files, and M 2's standing list carries
  **eight** classes, including an employer that paid on the member's behalf. On the old text an employer
  could file, be told the decision on day 20, and end the **member's** tolling on day 50 without her
  being told anything — buying her 18 days for someone else. The re-cut requires notice **to the member
  and to the person who filed the request**; where the filer is the member that is one notice, and where
  it is not, the 48-day cap carries the case.
- **F23 — the no-notice endpoint was ambiguous between act + 30 and act + 48**, and after item 124's
  enactment every deemed-denial case is a no-notice case. *"The later of (a) X and (b) Y"* where Y never
  occurs is at least as naturally read as resolving to X. **The cap is now a freestanding outer limit**
  — *"in no case later than 48 days after the Board acts upon the request"* — which operates whether or
  not notice is ever given, and the floor is a freestanding minimum.
- **F18 — four enumerated items in two series plus an unlettered limit.** The re-cut has **no clause
  lettering at all**: one endpoint, one floor, one cap. The question §9.4 answered about `(a)`/`(b)`
  against `(i)`/`(ii)` no longer arises.

**+233 characters. 46 words added, none struck.**

**The property §9.11 item 1 exists to preserve is preserved and I checked it rather than assuming it.**
*"30 days after the Board acts upon the request"* survives in the floor and *"48 days after the Board
acts upon the request"* in the cap, so **both** are periods measured from the Board's acting and the
MOO-141 patch's Edit 1 reaches both, exactly as it reached clause (a). That is also **why F1 is live**:
the cap is act-keyed by design, and §0.1 as corrected says so. The FIND must be the full clause and not the short form
*"until 30 days after the Board acts upon the request."* **At the MOO-141 patch's revision 5 that short
form became non-unique**, because Edit 3 at 30 days made M 2's retention sentence read identically;
at revision 6, with Edit 3 at 120 days, it is unique again. **The full clause resolves exactly once on
all three bases, which is why it is the anchor and why the 30/120 answer cannot strand it.**

**Clause lettering.** `(a)` and `(b)`, not `(i)` and `(ii)`, because the same sentence already carries
clauses `(i)` and `(ii)` for its two tolling exceptions. G 2's determination-date clauses use `(a)`,
`(b)`, `(c)`, so the form is the chapter's own.

**Who, what, by when, or else.** The actor is named — *"the Board gives written notice"*; the
recipients are **the member and the person who filed the request**, which covers both classes of tolling
request and the case where the filer is not the member; the outer date is fixed at act + 48; and the
consequence of the Board not giving notice is that the tolling runs the full 48 days, which is the
*"or else."* **The limb creates no new notice duty on the Board** — it is a clock trigger, and the
Board's notice duties are elsewhere; the 48-day cap is what happens if the Board never gives it.

### 3.2 Edit 164-2 — subdivision G 2, the exception to the 120-day outer limit. Card (h)

> **FIND** (count = **1** on both bases):
>
> ```
> or has not given it within 60 days after the determination date, the determination takes effect on the first day
> ```
>
> **READ:**
>
> ```
> or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect, the determination takes effect on the first day
> ```

**RE-CUT AT REVISION 5** on [MOO-187](/MOO/issues/MOO-187)'s **F3**, which showed that the 38-word
version **was a no-op and did not cure card (h) at all.** This is the most consequential repair in
revision 5 and the finding I should have caught myself.

**What went wrong.** G 2's floor sentence imposes **two** requirements: notice no less than 30 days,
*"and in no case less than the period allowed to the member by subsection M within which to request
reconsideration of the determination,"* before the determination takes effect. The old limb's condition
was that the determination could not take effect within 120 days *"consistently with **the sentence** of
this subdivision that requires notice to be given **no less than 30 days** before the determination
takes effect."* A reader takes the words after *"consistently with"* as naming **the requirement being
tested** — and tested against the 30-day limb alone the condition is satisfied almost never, because
notice on day 60 plus 30 days is day 90, inside the 120. **The limb would have lifted nothing and card
(h) would have stayed uncured.**

**Why §3.2's old defence was wrong.** It was right about the **consequence** clause, where the same
descriptor only **identifies** a sentence and the operative words — *"the first day on which it may take
effect under"* it — import the whole sentence, both limbs. It was wrong about the **new limb**, where the
descriptor is **load-bearing as a substantive test**. Borrowing a descriptor built for identification and
using it for a test is the defect. **The consequence clause is unchanged and needs no change.**

**The re-cut names the requirement, in the floor sentence's own words, both limbs.** *"[C]onsistently
with the requirement of this subdivision that notice be given no less than 30 days, and in no case less
than the period allowed to the member by subsection M within which to request reconsideration of the
determination, before the determination takes effect."* It is longer, and it is the only version that
reaches the case. **+366 characters. 59 words added, none struck.**

**On the words *"the period allowed to the member by subsection M"*.** They are G 2's own and they are
**not** the concept Edit 164-6 unifies — that is the **member's** period, not the Board's — so repeating
them here creates no second formula for one concept. §7.3 said so before this re-cut and it is still
true.

### 3.3 Edit 164-3 — subsection M 2, clause (ii). Card (j)

> **FIND** (count = **1** on both bases):
>
> ```
> excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request
> ```
>
> **READ:**
>
> ```
> excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request
> ```

**+24 characters. Seven words struck, eleven added.** **G 4's own cure is the precedent and the source of
the words** — see Edit 164-6. The defect: clause (ii) excludes the Board's late period from the 120-day
aggregate by reference to *"the 90 days allowed by **this subsection**"*, but the tolling sentence it
qualifies covers **two** classes of request, and this subsection allows no 90 days for a request under the
definition of *"final qualifying retirement date."* **For that class the exclusion has no referent and
does nothing.** Pass 17's F-5 makes it bite more often.

**The FIND is the full clause and not the bare phrase, deliberately.** If
[MOO-42](/MOO/issues/MOO-42) §7 item 124 is enacted it will introduce *"the 90 days allowed by this
subsection"* a second time, correctly — item 124's sentence is expressly about a request **for
reconsideration**, which this subsection does allow 90 days for. **The two are compatible and the order of
application does not matter, because this FIND cannot match item 124's sentence.**

### 3.4 Edit 164-4 — the definition of *"final qualifying retirement date"*, R-5. Card (l) / pass 18's F-5

> **FIND** (count = **1** on both bases):
>
> ```
> within the period this definition allows for acting upon it
> ```
>
> **READ:**
>
> ```
> within the period allowed by this section for acting upon it
> ```

**+1 character. Three words struck, four added — the Director's own wording.** §2.4 is why it is the
answer to the no-decision residual as well.

### 3.5 Edit 164-5 — subdivision D 1, the lateness descriptor. Card (k) / pass 18's F-9

> **FIND** (count = **1** on both bases):
>
> ```
> any notice of a date required by that definition upon the Board's action upon a request
> ```
>
> **READ:**
>
> ```
> any notice of a date required by that definition by reason of the Board's action upon a request
> ```

**+8 characters. One word struck, three added — the Director's own wording.** The descriptor identifies
which notice D 1's lateness extension attaches to. Reading *"upon"* as the temporal preposition it also is
makes the descriptor say the notice is required **at the moment of** the Board's action — which Edit 2 has
just made false, because the notice is now due 15 days after the Board **gives its decision**. *"By reason
of"* says what the descriptor means: the notice required **because** the Board acted. **My cross-reference
analysis still holds that D 1's reference is not stranded and that no conforming amendment is required**;
the Director takes the four words anyway to foreclose the looser reading, and I agree the four words are
cheaper than the argument.

### 3.6 Edit 164-6 — subdivision G 4, the period formula. **Conforming amendment, and the only one required**

> **FIND** (count = **1** on both bases):
>
> ```
> a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate
> ```
>
> **READ:**
>
> ```
> a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate
> ```

**+10 characters. Three words struck, four added. No change of meaning whatever.**

**Why it is required and not optional.** Edits 164-3 and 164-4 introduce *"the period allowed by this
section for acting upon the request"* at two sites. G 4 already carries the same concept in different
words at the third. **Three sites, one concept, two formulas is the defect the rule against two words for
one concept exists to prevent** — and it is the defect card (j) is a case of, so leaving it would cure the
disease and keep the symptom. After this edit the phrase appears **three times and the variant none**
(§7.2).

**It does not touch either of G 4's express *"first"*s**, which is the condition on which revision 2's
withdrawn G 4 edit stays withdrawn. I re-checked both at store revision 61: intact.

**I chased every other *"the period allowed…"* in enacted §1 before claiming one concept — and
CORRECTED AT REVISION 5, [MOO-187](/MOO/issues/MOO-187) F13 and F24: there are six, not three, and
*"the time allowed by that definition"* occurs twice, not once.** The conclusion survives unchanged; the
sweep as stated did not, and a reviewer who checks a checkable figure and finds it wrong discounts the
rest. Counted mechanically over §1 at store revision 65: `the period allowed` **7** (one of which is the
site Edit 164-6 amends), `the time allowed` **2**.

| # | Phrase | Provision | Concept | Amended? |
|---|---|---|---|---|
| 1 | *the period allowed by this subdivision for making an election under clause (i), (ii), or (iii)* | subsection D, completion dates | an **election-making** period | no |
| 2 | *A notice filed within the period allowed by this subdivision satisfies § 51.1-153* | D 1 | the member's **§ 51.1-153 filing** period | no |
| 3 | *The Board shall state the period allowed by this subdivision in the written statement* | D 1 | the same filing period | no |
| 4 | *the period allowed by that subdivision for making such an election* | → § 51.1-142.2 B 4 f | an **election-making** period | no |
| 5 | *the period allowed to the member by subsection M* | G 2 floor | the **member's** reconsideration period | no — and Edit 164-2 now repeats it, correctly |
| 6 | *the period allowed to it by this subdivision* | D 6 | the 60 days for determining **whether clause (iii) applies**, which the redetermination period then runs from — **F17: revisions 1 to 4 called this the redetermination period itself** | no |
| 7 | *the period allowed to it for acting upon the request* | **G 4 — the site Edit 164-6 amends** | **the Board's period for acting upon a request** | **yes** |
| 8–9 | *the time allowed by that definition for giving that statement or notice* · *the time allowed by that definition for giving it* | G 4, **two** instances | the Board's period for **giving a statement or notice** | no |

**None of the eight others is the concept Edit 164-6 conforms. One conforming amendment, and it is in
the patch.**

### 3.7 Edit 164-7 — subsection M 2, the deemed act. **PROMOTED AT REVISION 6**, item 130's residual, route (c), in candidate 164-7-B's two-trigger form

**The Policy Director took route (c) at question 2 and took 164-7-B at question 9.** They are one
sentence in the applied text, because 164-7-B was always drafted as a **replacement** for 164-7's
deeming sentence and not as an addition to it. **What is applied below is 164-7-B's deeming sentence,
carrying F19's limb (B), followed by 164-7's saving sentence, carrying F20's verbatim form and its one
express exception.** The reasoning is at §13.7, §14.1 to §14.4 and §15.4; this is the text.

> **FIND** (count = **1** in enacted §1 at store revision 68; **2** whole-document — F21):
>
> ```
> and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.
> ```
>
> **READ:**
>
> ```
> and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of "final qualifying retirement date" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. Except for the purposes of the duty of the Board under this subsection to act upon an application no later than 15 days after it acts upon the request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.
> ```

**217 words, +1,153 characters** — 141 words and 743 characters in the deeming sentence, 76 words and
408 in the saving. **Revision 5 priced 164-7 alone at 170 words and +898; 164-7-B's second trigger is
the difference**, and §16.7 records that the earlier figure is superseded rather than wrong.

**Five things about the applied text, each of which is a drafting choice and not a word I found.**

1. **It still defines no verb, and it still touches none of the 21 occurrences.** It supplies a **date**
   for events the section creates. That is Decision 1's method — option (f-4) — applied to the one case
   where no act exists to key to.
2. **Both triggers key to a date the section already fixes.** Trigger one is *"denied by operation of the
   preceding sentence"*, which is store revision 63's own enacted denial. Trigger two is the expiry of
   *"the period allowed by this section for acting upon it"* — **the identical formula Edit 164-4 puts
   into R-5**, and the identical date R-5's floor keys to. **No new number enters the section.**
3. **"The preceding sentence" appears twice and both references are verified, not assumed.**
   `verify_r68_v6.py` asserts, against the applied text, that the deeming sentence immediately follows
   the enacted denial sentence, that the saving sentence immediately follows the deeming sentence, and
   that nothing sits between them. **This is the trap §14.6 recorded against itself and it is now a
   counted assertion.** Anything a future pass inserts between those sentences strands a reference
   silently — §16.5 routes that to [MOO-42](/MOO/issues/MOO-42)'s §7 with D 1's ordinal reference.
4. **It does not move item 131's antecedent, and that is counted too.** The two sentences sit **before**
   M 2's completion sentence, so the nearest antecedent of *"such case decision"* is unmoved; and the
   applied text of 164-7 contains **no** *"case decision"* of its own, so there is no competing
   antecedent. Both are assertions in the verifier.
5. **The saving carries one express exception and it is the limb a reviewer should press on.** The
   deeming **does** reach the Board's 15-day duty on the application — limb 3 — because that period is
   *"measured from"* the Board's acting, which is the third form in the confinement clause. Reaching it
   means a duty on the Board is triggered by the Board's own inaction. **I think that is right** — the
   alternative leaves the member whose retention has ended with no decision on her application — and the
   Policy Director can decline that one limb by striking the exception without re-drafting the sentence.

**What it does and does not cure, stated as the disposition left it.** With it, all three of item 130's
limbs are reached for a reconsideration request where a denial date exists, and the definition-request
class is reached unconditionally by trigger two. **The one case still open is the member who files a
reconsideration request and never files the expiry notice**: there is no denial date, so trigger one
supplies nothing. That is **not** cured here and it is not elective to cure — the only instrument that
would reach it is an automatic denial on the 91st day, which the board considered and declined when it
took option (d). **It is recorded, not drafted, and §16.5 routes it.**

### 3.8 Edit 164-8 — subdivision D 1, the filing vehicle. **PROMOTED AT REVISION 6**

**The Policy Director took it at question 3, knowing from §13.5 that the candidate is wider than the
sentence it appends to.** D 1 gives the member **one** 30-day filing window running from the **first**
written statement, and then tells her that where any of three documents is late she *"may state an
effective date of retirement"* later. For the second and third documents that permission can arrive
after her only window has closed, and **D 1 contains no power to amend, replace or withdraw a filed
notice** — `amend`, `withdraw`, `replacing`, `substitute` each **0** occurrences in the subdivision —
and **§ 51.1-153 is silent**. She may state a date and has nothing to state it in.

> **FIND** (count = **1** in enacted §1 at store revision 68):
>
> ```
> the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.
> ```
>
> **READ:**
>
> ```
> the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. Where the Board gives any notice described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice already filed, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes any notice previously filed.
> ```

**81 words, +485 characters.** *Who, what, by when, or else:* the **member** may file **that notice or a
replacement**, **no later than 30 days after the Board gives the late notice**, and the consequence is
stated — the notice **is** one filed within the period D 1 allows, so it carries D 1's existing
retroactivity sentence and § 51.1-153's satisfaction with it, and it **supersedes** the earlier notice so
the Board never holds two.

**Two ordering facts, both counted.** Edit 164-5's FIND sits in the **same sentence** as this one and
**precedes** it; the verifier asserts the order, and the two substitutions are applied front to back so
neither disturbs the other. And this edit inserts **after** D 1's lateness-extension sentence and
**before** its *"The Board shall state, in the written statement … (i) … (ii) … (iii)"* sentence, which
makes no *"preceding sentence"* reference and is therefore undisturbed.

### 3.9 Edit 164-10 — subsection M 2, the 90-day duty's commencement. **PROMOTED AT REVISION 6**, counsel's F6

> **FIND** (count = **1** in enacted §1 at store revision 68; **4** whole-document — F21, and this is the
> string most likely to be mis-applied):
>
> ```
> The Board shall act upon a request for reconsideration within 90 days.
> ```
>
> **READ:**
>
> ```
> The Board shall act upon a request for reconsideration within 90 days after the request is filed.
> ```

**Five words, +27 characters, and it is the only one of the section's five *"shall act upon"* duties that
did not state a commencement.** The count of *"shall act upon"* is **5** in the base and **5** in the
applied text, counted — **this edit adds no duty; it dates one that exists.** Four things in this cut
depend on the expiry of that period being determinate: Edit 164-3's exclusion, Edit 164-4's floor,
Edit 164-7's second trigger, and Edit 164-11's conformed formula. **Since store revision 63 the member's
route into a case decision, and therefore into court, depends on it too.**

### 3.10 Edit 164-11 — subsection M 2, the expiry-notice sentence's period formula. **PROMOTED AT REVISION 6**, counsel's F12. Conforming

> **FIND** (count = **1** in enacted §1 at store revision 68; **2** whole-document):
>
> ```
> Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file
> ```
>
> **READ:**
>
> ```
> Where the Board does not act upon a request for reconsideration within the period allowed by this section for acting upon the request, the person who filed the request may file
> ```

**+24 characters, no change of meaning** — the sentence is expressly about a request **for
reconsideration**, for which this section allows 90 days, and Edit 164-10 now says from when.
**CORRECTED AT REVISION 6: §15.4 priced this at +23. The substitution is 38 characters for 62, so it is
+24** — the identical arithmetic as Edit 164-3, which is the same substitution at the other site.

**This is card (j)'s defect at its second site and Edit 164-6's cure in its third application.** At store
revision 68 *"the 90 days allowed by this subsection"* occurs **twice** in enacted §1 — clause (ii) and
this sentence. Edit 164-3 removes one and this removes the other, so the count goes **2 → 0** and the
conformed formula stands at **five** sites and the variants at none. All counted.

**It is [MOO-42](/MOO/issues/MOO-42)'s enacted sentence, not mine**, and the Policy Director's question 11
disposed it *"take it, and MOO-42 is told, not asked."* §16.5 tells them.

### 3.11 Edit 164-12 — subdivision G 2, item 46's carve-out gets its own pendency endpoint. **PROMOTED AT REVISION 6**; this is candidate **(c-2)**

**The Policy Director took (c-2) at question 1 and retired (c-1).** The full comparison, including who
loses what in days under (c-1), stays at §4 as the record of the choice.

> **FIND** (count = **1** in enacted §1 at store revision 68; **1** whole-document):
>
> ```
> and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.
> ```
>
> **READ:**
>
> ```
> and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. Notwithstanding the definition in subdivision 4, and for the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which the Board grants or denies it.
> ```

**38 words, +220 characters. CORRECTED AT REVISION 6: §4.2 called it *"twenty words"* and then
*"twenty-eight"*; counted, the new sentence is 38 words and 219 characters, +220 with the space.**

**Who loses what: nobody, against today's ordinary-meaning reading.** It forecloses the argument that
G 4's definition travels into G 2, confirms item 46 exactly as the board enacted it, and leaves the
Commonwealth bearing the cost item 46 priced and the no-recovery limb absorbs. ***"Grants or denies"***
rather than *"determines"*, because G 2 uses *"the determination"* and *"determines"* some twenty times
for the **G 2 reduction determination** and the collision would have made the carve-out circular — F10.
***"Notwithstanding the definition in subdivision 4"*** makes the divergence deliberate on the face of
the text, because without it subsection G would define *"pending"* for a disability application twice,
differently, in adjacent subdivisions, and the natural judicial move on a word defined twice in one
subsection is to **harmonise**, with the drafter no longer choosing which gives way.

**It does not touch G 4**, and the verifier asserts that: (c-1)'s FIND — G 4's confined definition — still
resolves **exactly once, unamended**, in the applied text. **G 4's own first-action pendency runs in the
member's favour there, by resuming the Board's clock earlier, and it is unchanged.**

**The board is told, not asked.** The Policy Director decided at question 1 that no item-46 card goes to
the board, because (c-2) confirms what they already decided and a card reading *"do you still want the
thing you decided?"* invites a reopening nobody asked for. **What they must be told, in the
designation-review read-through, is the deliberate divergence: subsection G will define *"pending"*
twice, differently, in adjacent subdivisions, on purpose.**

---

## 4. Card (c) — G 2's two uses of *"pending"*. **(c-2) is applied at revision 6 as Edit 164-12**; this section is the record of the choice

**The Director's instruction was: do not draft without saying exactly who loses what, and the item-46
question comes to the Policy Director. Both candidates were drafted so the choice was visible.**

> **DISPOSED AT REVISION 6.** The Policy Director answered question 1: **(c-2)**, which is now
> **Edit 164-12** at §3.11, **and no item-46 card goes to the board** — the question was contingent on
> (c-1), and counsel's **F9** makes (c-1) defective rather than merely impolitic. **(c-1) and the pricing
> at §4.1 are retired to the record.** They are kept in full below, unedited, because the price of the
> option that was *not* taken is the only way to check that the one that was taken is better.

**The defect.** G 2 uses *"pending"* twice, in the carve-out item 46 put there:

> *Nothing in this subdivision prevents the payment of a retirement allowance to a member while an
> application of the member for a disability retirement allowance under this chapter **is pending**, and
> the determination required by this subdivision shall take effect notwithstanding that a retirement
> allowance has been paid to the member while such an application **was pending**.*

**Neither is defined.** G 4 defines *"pending"* for a disability application — *"from the date on which the
member files it until the date on which the Board **first acts upon it**"* — but confines the definition
*"[f]or the purposes of **this subdivision**."* So G 2's two uses fall to ordinary meaning, which is
**pending until determined**, and a reader can argue either way from the same bill.

### 4.1 Candidate (c-1) — one word. Extend G 4's definition to the subsection. **RETIRED AT REVISION 6 — record only, not applied, not to be applied**

> **FIND** `For the purposes of this subdivision an application for a disability retirement allowance is pending`
> → **READ** `For the purposes of this subsection an application for a disability retirement allowance is pending`

**One word. And it narrows item 46's carve-out. Here is exactly who loses what.**

- **Who:** a member whose election has not been settled, who does not retire in a qualifying retirement,
  and who has a disability retirement application on file when the G 2 determination falls due.
- **What she loses:** the retirement allowance for the period **from the Board's first action on her
  disability application until the G 2 determination takes effect**. Today, on the ordinary-meaning
  reading, item 46's carve-out pays her throughout. Under (c-1) the carve-out ends at the Board's first
  action — an acknowledgment, a request for records — and G 2's third sentence then bars any allowance
  until the determination takes effect.
- **How much:** bounded by G 2's own limits at **120 days after the determination date**, and **unbounded**
  in the late-notice case, where G 2's exception already lifts that limit — and, after Edit 164-2, in the
  tolled-floor case too, where the bound is `60 + 30 + 120 + the Board's lateness` — §2.3 as corrected at
  revision 5, **not** the 210 days revisions 1 to 4 stated. **Pass 10's worked case for item 46 was
  14 months with no allowance**; (c-1) does not restore 14 months, because G 4's bar on **making** the
  determination also lifts at first action, but it does hand back the window between the two events.
- **What item 46 was decided on:** *"the no-recovery limb absorbs any overpayment, so the Commonwealth
  bears the cost either way and paying her is strictly better."* **(c-1) re-takes part of what that
  answer gave, for a drafting tidiness reason.**

### 4.2 Candidate (c-2) — 38 words. Give G 2 its own endpoint, keyed to the disposal of the application. **APPLIED AT REVISION 6 as Edit 164-12 — see §3.11 for the applied text**

> **FIND** `and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.`
> → **READ (REVISED AT REVISION 5 on F10)** `and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. Notwithstanding the definition in subdivision 4, and for the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which the Board grants or denies it.`

**Two repairs, both from [MOO-187](/MOO/issues/MOO-187) F10, and both are the price of taking (c-2).**

- ***"[D]etermines it"* collided with G 2's most overloaded verb.** G 2 uses *"the determination"* and
  *"determines"* about twenty times for the **G 2 reduction determination**, so *"until the date on
  which the Board determines it"* invited the reading that the endpoint is the G 2 determination — which
  would make the carve-out circular, since the allowance may be paid **until** the determination and the
  determination is the thing the carve-out is an exception **to**. ***"[G]rants or denies it"*** is
  unambiguous and is the ordinary vocabulary for disposing of an application.
- **One word, two definitions, one subsection.** Without an express non-application, subsection G would
  define *"pending"* for a disability application twice, differently, in adjacent subdivisions. It is
  operationally coherent and deliberate — the Board may **make** the G 2 determination once it first
  acts (G 4), while it must keep **paying** until it grants or denies (G 2) — but it reads as an error,
  and the natural judicial move on a word defined twice in one subsection is to **harmonise**, with the
  drafter no longer choosing which gives way. ***"Notwithstanding the definition in subdivision 4"***
  makes the divergence deliberate on the face of the text.

**Who loses what: nobody, against today's ordinary-meaning reading.** It forecloses the argument that
G 4's definition travels, confirms item 46 as the board enacted it, and leaves the Commonwealth bearing
the cost item 46 priced and the no-recovery limb absorbs. **It does not touch G 4**, so G 4's own
first-action pendency — which runs in the member's favour there, by resuming the Board's clock earlier —
is unchanged.

**A second, independent reason for (c-2), found by counsel and not by me — F9.** (c-1) narrows **both**
of G 2's uses, and §4.1 prices only the first. The second is the **validating** limb: *"the determination
… shall take effect notwithstanding that a retirement allowance has been paid to the member while such
an application **was pending**."* Narrowed to first-action pendency, **an allowance paid after the
Board's first action is no longer covered by the notwithstanding** — and G 2's third sentence requires
that the determination take effect **before** the first payment. Worked case: application day 0,
acknowledgment day 5, allowance paid day 40, determination effective day 90. The payment on day 40 was
not made *"while such an application was pending,"* so the validation does not reach it, **G 2's own
self-correction clause is attached to the floor sentence and not to this one**, and a litigant on either
side can argue the determination is of no effect or the payment was unlawful. **That is a worse outcome
than the carve-out narrowing §4.1 prices, and it is a drafting consequence of a one-word change.**

**Why (c-2) and not (c-1).** (c-1) is one word and (c-2) is now twenty-eight, and on minimal footprint
(c-1) should win. It loses because **the footprint that matters is the policy footprint**: (c-1) reverses part of an
enacted board decision as a side effect of defining a word, and a clarifying patch should not reprice
anybody. That is the Director's own reason for taking (k-ii) over the first-action result, applied to the
same facts.

**SUPERSEDED AT REVISION 6: (c-2) *is* in the patch at §3, as Edit 164-12. (c-1) is not and will not
be.** The sentence this replaced read *"Neither is in the patch at §3, and neither will be applied until
the Policy Director answers §10.1."* §10.1 is answered.

---

## 5. Title line, enacting clause and enactment clauses

**Unchanged by this patch**, and reproduced so this document is readable without `bill-text-s8`:

> A BILL to amend and reenact §§ 51.1-142.2 and 51.1-162 of the Code of Virginia and to amend the Code
> of Virginia by adding a section numbered 51.1-142.4, relating to the Virginia Retirement System;
> purchase of prior active duty military service credit by state employees; cost; pilot program;
> post-retirement employment; reports.
>
> Be it enacted by the General Assembly of Virginia:
>
> 1. That §§ 51.1-142.2 and 51.1-162 of the Code of Virginia are amended and reenacted and that the
>    Code of Virginia is amended by adding a section numbered 51.1-142.4 as follows:

**RE-TAKEN FROM THE BASE AT REVISION 6.** Revisions 1 to 5 reproduced the title line and the first
enactment as they read at store revision 61 — **one** amended section. The act now amends **two**:
§ 51.1-162 was added to the amended sections, and the editorial note in enacted §1 records the removal
of § 51.1-155 by the Policy Director's direction. **Nothing in this cut touches either the title line or
any enactment clause**; the reproduction was simply stale, for the same reason §6 was.

**This patch adds no enactment clause, no effective date, no sunset and no severability clause.** All
**eleven** edits are repairs inside a section whose effective-date mechanics already carry them — the second
enactment's 1 July 2029 date and the third enactment's 1 July 2033 expiration with its clause (i) to (iv)
savings — and none is severable from the provision it amends. **The §6.7 question is recorded as settled on
[MOO-162](/MOO/issues/MOO-162) and I am not re-raising it**; if a reviewer puts it in writing that the
third enactment's clause (i) savings are insufficient, it comes back as a card.

---

## 6. The provisions, in full, as amended

**Markup convention, the same one the MOO-141 patch's own cuts use.** The whole of subsection A, subdivision D 1,
subdivision G 2, subdivision G 4 and subsection M is **new language in the bill** — each is already
wrapped in `<u>…</u>` in `bill-text-s8` — so **every word reproduced below is underlined new text in the
bill as it stands**, and nesting a second `<u>` inside it would be ambiguous markup rather than clearer
markup. Inside that wrapper:

- words **this patch adds** are **bolded**;
- words this patch removes are ~~struck through~~;
- words the **MOO-141 patch** adds are ***bold italic*** — at its current cut, [MOO-176](/MOO/issues/MOO-176)'s **revision 6**, with Edit 3 at **120 days** — and
  the words it removes are ~~struck~~ with its text shown next to them — so that a reader can see both
  patches at once at the provisions where they overlap.

> **RE-SPLICED AT REVISION 6, AND THIS IS THE SIXTH TIME. Every reproduction below was spliced
> programmatically from the live `bill-text-s8` at store revision 68 by `repro68.py`, locating each
> provision by content and not by line index. None is carried forward from any earlier revision.**
>
> **Store revisions 66, 67 and 68 grew enacted §1 from 121,576 to 131,066 characters** — nearly ten
> thousand characters into provisions this cut reproduces in full — **and every one of the thirteen
> anchors still resolved exactly once throughout.** That is the whole lesson of the six stale splices:
> *an anchor that still resolves tells you nothing about whether the surrounding text has moved.*
>
> **What store revision 68 changed inside these reproductions:** subsection A's interpretation paragraph
> was re-cast (§6.1), which is what killed MOO-141 Edit 1's anchor; subdivision D 1 gained the
> *"where the person adversely affected is the member"* qualification on its certification-failure
> sentence and now keys that clock to the **certification given to the member**; subdivision G 2's
> clause (ii) refund limb now names *"any state agency from whose appropriation an amount was paid"*
> rather than *"any employer that paid"*; and **subsection M 2 gained m8-a's 90-day proviso in clause
> (ii)** — the instrument that makes §2.3's bound 300 days unconditionally — along with the same
> state-agency wording in its two standing lists. **None of those was mine, three of them strengthen
> §2.1's argument, and all four moved text sitting behind an anchor that still resolved once.**
>
> **The reproductions below carry all eleven edits**, including the five promoted at revision 6. The
> apostrophes in the G 4 extract at §6.5 are shown **normalised** per §8; all four are still inside G 4
> at store revision 68, and the verifier asserts both the count and the confinement.

### 6.1 Subsection A, final interpretation paragraph — **not amended by this patch**, and this is the provision Decision 1 declines to amend

Reproduced in full because Decision 1 is a decision about it, and because store revision 68 re-cast it.
**Two things changed:** the giving rule is now express and reaches **certifications** as well as
statements and notices, with a 5:00 p.m. electronic cut-off; and the three-day extension is **confined
to mailing**. §16.2 re-cuts Edit 164-1's derivation of its 48-day cap on that footing, and §16.3 records
that Decision 2 gains a site from it.

**The bold italic text is the MOO-141 patch's Edit 1, shown at its REPAIRED anchor.** Edit 1's FIND as
MOO-141 wrote it resolves **0** times at store revision 68. **The repair below is shown so this document
is readable and so the order-independence test can be run; it is MOO-141's to cut, not mine, and I have
not cut it for them.** Option (f-2) at §1.1 would have added a further sentence here and does not.

<u>For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, a written statement, notice, or certification required of the Board is given on the date the Board mails it to the person to whom it is required to be given or transmits it electronically to an address that person has provided to the Board for that purpose, except that an electronic transmission completed after 5:00 p.m. is given on the following day. For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where the Board mails a written statement, notice, or certification, every period within which a person may or must act that runs from the giving of that statement, notice, or certification is extended by three days. ***For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.***</u>

### 6.2 The definition of *"final qualifying retirement date"* in subsection A — in full, as amended by **Edit 164-4** and by the MOO-141 patch's **Edit 2**

**Edit 164-7's second trigger keys to the period this definition allows**, through the formula Edit 164-4
puts into R-5, so the definition and M 2 now compute from one date. Candidate **164-9** at §15.4 would
not touch this provision.

<u>"Final qualifying retirement date" means the date that is 12 months after the member's earliest qualifying retirement date, except that the Board shall approve a later date where the Board's own processing requirements, or any other cause not attributable to the member, make the member's retirement on or before the date that would otherwise apply under this definition impracticable. A later date approved under this definition shall be the first day of a month and shall be not more than three months after the date determined under the first sentence of this definition. The Board shall approve a later date on its own initiative or upon the written request of the member, which the member may file at any time before the date that would otherwise apply under this definition or before any later date approved under this definition; the Board shall act upon such a request, and shall give the member written notice of its determination and of the reasons for it, no later than 30 days after the request is filed; and the member may seek review of the determination under subsection M. The Board shall determine the member's earliest qualifying retirement date and final qualifying retirement date, and shall state both of them and the reasons for any later date approved under this definition, in writing to the member no later than 15 days after the Board credits to the member the service credit purchased under the member's election, and shall give the member written notice of any later date approved after that statement no later than 15 days after the approval. Where the member's final qualifying retirement date as extended under subdivision D 1 or as tolled under subsection M is not the first day of a month, the member's final qualifying retirement date is the first day of the next month. In no event shall a member's final qualifying retirement date, as extended under subdivision D 1 or as tolled under subsection M, be later than 12 months after the date that applies under the first sentence of this definition or, where a later date has been approved under this definition, after that later date, except that this sentence does not apply to an extension under subdivision D 1 by reason of a statement or notice given later than the time required by this definition, and the aggregate of all extensions so excluded shall not exceed 12 months. Where the running of a period has been tolled under subsection M and the member is prevented by the preceding sentence from retiring in a qualifying retirement after that tolling ends, the member's final qualifying retirement date is, notwithstanding the preceding sentence, the first day of the second month following the month in which the Board last acts upon a request the filing of which tolled that period, and in no event later than 12 months after the latest date the preceding sentence permits. Notwithstanding the two preceding sentences, where the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which the Board gives the statement required by this definition, the member's final qualifying retirement date is that first day. Where the Board does not act upon a request the filing of which tolled the running of the member's final qualifying retirement date under subsection M within the period ~~this definition allows~~ **allowed by this section** for acting upon it, and the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which that period expired, the member's final qualifying retirement date is, notwithstanding any other provision of this definition, that first day. Where the Board's action upon a request determines a member's final qualifying retirement date under this definition, the Board shall state that date in its decision upon the request, and where the Board does not do so it shall give the member written notice of that date no later than 15 days after ~~it acts upon~~ ***it gives its decision upon*** the request. Where the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which the Board gives a decision or notice required by the preceding sentence, the member's final qualifying retirement date is, notwithstanding any other provision of this definition, that first day.</u>

### 6.3 Subdivision D 1 — in full, as amended by **Edit 164-5** and, newly at revision 6, by **Edit 164-8**

The two edits sit in **one sentence** — 164-5 in its opening descriptor, 164-8 appended after it — and
the verifier asserts that order. **D 1's ordinal reference into M 2** — *"the second sentence of
subdivision M 2"* — appears in the certification-failure sentence below; §16.6 proves that no edit or
candidate in this cut inserts before the sentence it points at.

<u>**D. 1.** The Board shall not accept an election until the Board has, in writing, certified to the member and reserved the certified subsidy for that election under this subsection. The Board shall determine the certified subsidy for an election no later than 30 days after the member's application is completed. The Board shall give the certification required by this subsection no later than 15 days after the confirmation required by subdivision 3 is obtained. The Board's certification shall state the matters required by subdivision B 4 c of § 51.1-142.2, the filing date of the member's complete application, the amount of service credit to be purchased, the certified subsidy, the valuation date, the completion date by which the member must complete payment, the member's anticipated earliest qualifying retirement date and anticipated final qualifying retirement date, the member's unreduced retirement eligibility date determined with the service credit to be purchased as certified, the member's right to cancel the election under subdivision G 5 at any time before completing payment, and the member's obligations under subsections E, F, and G. The Board shall not accept an election until the member has filed with the Board a written acknowledgment of the member's obligations under subsections E, F, and G. The Board's certification shall also state that, where a member whose election the Board has accepted dies without having retired, the benefit payable on the member's death is determined under subdivision G 4 and under § 51.1-162 as on the death of a member in service and not under the provisions of subdivision C 1 of § 51.1-165 or of subsection F of § 51.1-165.01 that require benefits to be paid in accordance with § 51.1-163; that where the member dies while in service and subdivision C 2 of § 51.1-165 otherwise applies, that subdivision provides for the payment of benefits in accordance with § 51.1-163, except that where the contingent annuitant or annuitants under the option elected are the same person or persons who would receive a monthly benefit under subsection B of § 51.1-162 and that monthly benefit would be greater, that subdivision provides for the payment of benefits in accordance with that subsection, and that the Board shall pay the benefit that subdivision provides or the benefit determined under subdivision G 4, whichever is greater; that no option elected under § 51.1-165.01, and no option elected under subdivision A 2 or A 3 of § 51.1-165, limits that benefit, but that the straight life option under subdivision A 1 of § 51.1-165 is an election to receive an increased retirement allowance in lieu of any death benefits and, where that election is not rendered null and void by subdivision C 1 of § 51.1-165, may leave no benefit payable on the member's death; that, to the extent required by § 401(a)(37) of the Internal Revenue Code, as amended or renumbered, and the regulations thereunder applicable to governmental plans, subsection B of § 51.1-162 provides a retirement allowance on the death of a member in service only where no benefit is payable under subsection C of that section and only to a surviving spouse, minor child, or parent whom the member has designated under subsection A of that section or who is entitled in the order of precedence that subsection B of that section states where the member has made no designation or the person designated has predeceased the member and no other designation has been made; that the member is advised to review the member's designation of beneficiary under subsection A of § 51.1-162 before completing payment; that subsection C of § 51.1-162 provides a retirement allowance, where the member dies in service from a cause compensable under the Virginia Workers' Compensation Act (§ 65.2-100 et seq.), to the member's surviving spouse, minor children, or parents as that subsection provides; and that where no benefit is payable under subsection B of § 51.1-162, subsection A of that section provides for the payment of the member's accumulated contributions, reduced by the amount of any retirement allowance previously received by the member, to the person the member has designated or, where the member has made no designation or the person designated has predeceased the member and no other designation has been made, to a surviving relative in the order of precedence that section states. A failure to state in the Board's certification every matter this subdivision requires to be stated in it is a failure of the Board to state in a certification a matter this section requires to be stated in it for the purposes of subsection M; a person adversely affected by it may seek review under subsection M no later than 30 days after the date on which the certification is given to the member or, where that person is not the member, no later than 30 days after the date on which the notice required by subdivision G 4 is given to that person; the second sentence of subdivision M 2 does not apply to such a failure where the person adversely affected is the member; and the Board shall state every such failure in the report required by subsection J. The member shall file the notice of retirement required by § 51.1-153, stating as the effective date of retirement a date on which the member will retire in a qualifying retirement, no later than 30 days after the date on which the Board gives the member the written statement of the member's earliest qualifying retirement date and final qualifying retirement date first required by the definition of "final qualifying retirement date" in subsection A. Nothing in this subdivision requires the member to file that notice any period before the effective date of retirement stated in it. A notice filed within the period allowed by this subdivision satisfies § 51.1-153 notwithstanding that it is filed after the effective date of retirement stated in it; and where such a notice is filed after that effective date, the member's retirement shall take effect on that date and the retirement allowance shall be payable retroactively to that date, subject to subsection E of § 51.1-153 and provided that the effective date stated is on or after the day following the member's last day of service. The Board shall state the period allowed by this subdivision in the written statement required by that definition. Where the Board gives that written statement, any notice of a later approved date required by that definition, or any notice of a date required by that definition ~~upon~~ **by reason of** the Board's action upon a request, later than the time required by that definition, the member's final qualifying retirement date is extended by the number of days by which the statement or notice is late, the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. **Where the Board gives any notice described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice already filed, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes any notice previously filed.** The Board shall state, in the written statement required by that definition and in every notice of a later approved date required by that definition, (i) that where the Board gives the statement or notice later than the time required by that definition the member's final qualifying retirement date is extended by the number of days by which the statement or notice is late, that the date so extended is subject to the limits stated in that definition, and that where the date so extended is not the first day of a month it is the first day of the next month; (ii) that the member may state as the effective date of retirement a date no earlier than the first day of the month following the month in which the Board gives the statement or notice, and that nothing in this subdivision prevents the member from stating an earlier effective date of retirement to which the member is otherwise entitled, subject to subsection E of § 51.1-153; and (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days.</u>

### 6.4 Subdivision G 2 — in full, as amended by **Edit 164-2** and, newly at revision 6, by **Edit 164-12**

Edit 164-12 is candidate **(c-2)**, applied on the Policy Director's answer to question 1. It appends one
sentence to item 46's carve-out. **Candidate (c-1) is retired and is not shown**, because it is not in
the patch and will not be.

<u>2. If the member does not retire in a qualifying retirement, the Board shall, except as subdivision 4 provides, within 60 days after the earlier of (a) the member's final qualifying retirement date, if any, and (b) the date on which the member retires in a retirement that is not a qualifying retirement, (i) reduce the service credit credited to the member under the election to the largest number of whole months of service credit that the member's payments would have purchased at the standard cost determined as of the date the Board accepted the election, (ii) refund to the member, and to any state agency from whose appropriation an amount was paid on the member's behalf, in proportion to the amounts each paid, the amount by which the amounts paid exceed the cost, at that standard cost, of the service credit credited under clause (i), and (iii) release the reservation. The Board shall give the member written notice of the determination, of the service credit retained, and of the reasons for the determination, no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect, and a determination that takes effect in contravention of this sentence takes effect instead on the first day on which it may take effect under this sentence; and the member may seek review of the determination under subsection M. The Board shall not pay any retirement allowance to a member whose election has not been settled under subdivision 1 or 4 until the Board has made the determination required by this subdivision, and the determination shall take effect before the first payment of any retirement allowance to the member; and the first payment of the retirement allowance shall include every amount that would have been payable to the member from the effective date of retirement had the determination been made before the effective date of retirement. Nothing in this subdivision prevents the payment of a retirement allowance to a member while an application of the member for a disability retirement allowance under this chapter is pending, and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. **Notwithstanding the definition in subdivision 4, and for the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which the Board grants or denies it.** No determination under this subdivision is required in respect of an election that has been cancelled under subdivision D 6 or under subdivision 5 of this subsection, in respect of an election under which the member has been credited with service credit under subdivision 3 or 5 of this subsection, or in respect of an election under which the reservation has been released under subdivision D 7 without any service credit having been credited to the member, and no retirement allowance shall be withheld by reason of this subdivision on account of any such election. For the purposes of this subdivision, "the determination date" means the date from which the 60-day period within which the Board must make the determination required by this subdivision runs, whether that period runs under the first sentence of this subdivision or under subdivision 4. The Board shall give the notice required by this subdivision no later than 60 days after the determination date, and shall state in the report required by subsection J every failure to give that notice within that period. A determination under this subdivision shall take effect no later than 60 days after the Board gives the notice required by this subdivision, and in no event later than 120 days after the determination date, except that where the Board gives that notice later than 60 days after the determination date, or has not given it within 60 days after the determination date, **or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect,** the determination takes effect on the first day on which it may take effect under the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect, and in that case the limit of 120 days stated in this sentence does not apply. Where the member dies before the first payment of the retirement allowance, the Board shall pay the amount that would have been included in that payment under this subdivision to the person entitled to any benefit payable on the member's death or, if there is none, to the member's estate. The Board shall pay a refund required by this subdivision within 60 days after the determination takes effect, except that to the extent a refund may not be paid to the member without adverse federal tax consequence to the member, the Board shall apply that amount to the purchase of additional service credit for the member at the standard cost and shall notify the member in writing of the amount so applied.</u>

### 6.5 Subdivision G 4 — the suspension and pendency passage, in full, as amended by **Edit 164-6**

**Convention for this provision, stated because it is the one place I am not reproducing a whole
provision.** Subdivision G 4 is **31,872 characters** at store revision 68 and this patch amends three
words in one sentence of it. The extract below is the three consecutive sentences that carry the
suspension, the aggregate, and the pendency definition — every sentence this patch touches, every
sentence the retired candidate (c-1) would have touched, and the context needed to read either.
**Both of G 4's express *"first"*s appear in it and both are intact, and Edit 164-12 does not touch this
definition** — the verifier asserts that (c-1)'s FIND still resolves exactly once, unamended, in the
applied text.

> The Board shall not make a determination under subdivision 2, and shall not give the notice required by subdivision 2, while an application of the member for a disability retirement allowance under this chapter is pending, and a determination made in contravention of this sentence is of no effect. No period stated in subdivision 2 or in this subdivision, whether it is a period within which the Board is required to act or a period within which a determination is required to take effect, runs while such an application is pending or while a request the filing of which tolls the running of the member's final qualifying retirement date under subsection M is pending, except that the aggregate of all such non-running by reason of such requests and by reason of applications for a disability retirement allowance filed after the first such application shall not exceed 120 days, and a failure of the Board to act upon such a request within the period ~~allowed to it~~ **allowed by this section** for acting upon the request shall not extend that aggregate. For the purposes of this subdivision an application for a disability retirement allowance is pending from the date on which the member files it until the date on which the Board first acts upon it, and such a request is pending from the date on which the member files it until the date on which the Board first acts upon it.

### 6.6 Subsection M — subdivisions 1, 2 and 3 in full, as amended by **Edits 164-1, 164-3, 164-7, 164-10 and 164-11** and by the MOO-141 patch's **Edit 3**

**Five of the eleven edits are in M 2, and the sentence order below is the whole of question 4's
answer.** Reading forward: M 2's **second** sentence is the one D 1's ordinal reference points at and is
**unamended**; the **third** carries Edit 164-10; the **fourth** carries Edit 164-11; the **fifth** is
item 124's enacted denial sentence, **unamended**, and Edit 164-7's two sentences follow it immediately;
then the tolling sentence with Edits 164-1 and 164-3 and **m8-a's enacted 90-day proviso**; then the
retention and 15-day-duty sentence, which is **one sentence and not two**, carrying the MOO-141 patch's
Edit 3 at revision 6's 120 days. The confirming sentence at §1.3, which I recommend against and the
Policy Director declined, is **not** shown.

<u>**M. 1.** The Board shall adopt and publish, no later than July 1, 2029, procedures for administering this section, which shall address the content of a complete application, the channels through which an application may be filed, the determination of initial average compensation where records are incomplete, the determination and reservation of certified subsidies and contingency amounts, the waiting list, recertification, the crediting of service, settlement, cancellation, refunds, and the review of the Board's determinations. The Board shall publish the procedures on its website and shall make them available to any person on request.</u>

<u>2. A member, retiree, beneficiary, applicant, personal representative of a deceased member's estate, person who has claimed any benefit payable on the death of a member, person to whom this section requires a notice to be given in respect of a benefit payable on the death of a member, or state agency from whose appropriation an amount was paid on a member's behalf, adversely affected by a determination of the Board under this section, or by a failure of the Board to make a determination, to give a notice, or to make a payment within a period required by this section, or by a failure of the Board to state in a certification or notice a matter this section requires to be stated in it, may obtain, upon written request filed within 30 days after the notice of the determination is given or, in the case of a failure to make a determination, to give a notice, or to make a payment, at any time before the Board makes the determination, gives the notice, or makes the payment or, where the Board has made the determination, given the notice, or made the payment late, within 30 days after the notice of the determination is given or, in the case of a failure to give a notice or to make a payment, within 30 days after the Board gives the notice or makes the payment, or, in the case of a failure to state a matter, within 30 days after the certification or notice is given or, where the provision that requires the matter to be stated provides a longer or later period, within that period, written reconsideration by the Board stating the reasons for its decision. Every determination, certification, redetermination, recertification, reduction, cancellation, rescission, restoration, crediting of service credit, placement on a waiting list, expiration of a reservation, denial of an election, and refusal to accept an election under this section is a determination of the Board for the purposes of this subsection, whether or not another provision of this section expressly provides for review of it. The Board shall act upon a request for reconsideration within 90 days **after the request is filed**. Where the Board does not act upon a request for reconsideration within ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request**, the person who filed the request may file with the Board written notice that the period has expired. Where the Board does not act upon the request within 30 days after that notice is filed, the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. **Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of "final qualifying retirement date" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. Except for the purposes of the duty of the Board under this subsection to act upon an application no later than 15 days after it acts upon the request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.** The filing of a request for reconsideration under this subsection, and the filing of a request under the definition of "final qualifying retirement date" in subsection A, tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board **gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board** acts upon the request **and in no case later than 48 days after the Board acts upon the request**, except that (i) no second or subsequent request for reconsideration of the same determination or of the same failure, and no second or subsequent request under that definition, tolls any period under this section or under subdivision B 4 f of § 51.1-142.2, and (ii) the aggregate of all tolling under this subsection shall not exceed 120 days, excluding any period after the expiration of ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request** and before the Board acts upon the request, provided that the aggregate of all periods so excluded shall not exceed 90 days. An application that is the subject of a request for reconsideration under this subsection retains its filing date for the purposes of subdivisions D 4 and D 5 until ***120 days after*** the Board acts upon the request, and the Board shall act upon the application no later than 15 days after it acts upon the request. Upon completion of a reconsideration under this subsection, the final determination issued by the Board shall constitute a case decision as defined in § 2.2-4001. A member, retiree, beneficiary, applicant, personal representative of a deceased member's estate, person who has claimed any benefit payable on the death of a member, person to whom this section requires a notice to be given in respect of a benefit payable on the death of a member, or state agency from whose appropriation an amount was paid on a member's behalf, aggrieved by, and claiming the unlawfulness of, such case decision, shall have a right to seek judicial review thereof in accordance with Article 5 (§ 2.2-4025 et seq.) of the Administrative Process Act. Nothing in this subsection limits the right of any person under § 2.2-4026 to seek judicial review of a case decision. Articles 3 (§ 2.2-4018 et seq.) and 4 (§ 2.2-4024) of the Administrative Process Act shall not apply to a reconsideration under this subsection.</u>

<u>3. The sentence of subsection B of § 2.2-4021 providing that a decision shall be deemed to be in favor of the named party, and the corresponding sentence of subsection C of that section, shall not apply to a determination of the Board under this section or to a reconsideration under subdivision 2.</u>

---

## 7. Cross-reference check — performed on store revision 61, with results

> **RE-RUN AT REVISION 6 and the result is restated at §16.6.** The classification below is the
> revision-1 run over **19** occurrences; §13.3 re-ran it at **21** and the claim survived verbatim;
> §16.6 re-runs it at store revision 68 and reports what the eleven edits do to the census. **The
> conclusion has not changed at any of the three counts: one conforming amendment is required outside
> the cards, and it is Edit 164-6.** Edit 164-11, promoted at revision 6, is the **same** repair at a
> second site inside M 2 — counsel's F12 — and is carried as an edit rather than as a conforming
> amendment because it is inside a provision this cut already amends.

**Re-performed at store revision 63 at §13.9: same result, plus one new ordinal reference into M 2 that every future edit to that subsection has to respect.**

**Performed twice: on store revision 61, and on store revision 61 with the three MOO-162 edits applied.
Identical results on both.**

### 7.1 Every `act / acts / acting / action upon` in enacted §1 — **19 occurrences**, classified

**At store revision 63 this is 21, not 19.** Store revision 63 added two, both express negatives and neither an endpoint; they are classified at §13.3 and **Decision 1's claim is unchanged**.

The count matches MOO-141 §4.1's 19. The classification is what Decision 1 rests on.

| # | Provision | What it is | Act-keyed endpoint? | Touched by this patch |
|---|---|---|---|---|
| 1 | definition, later-date request | **duty**, 30 days | no | no |
| 2 | definition, tolling reset | **date fixed by a month** | yes — moves against the member | **no — neutralised downstream**, §1.1 |
| 3 | definition, R-5 trigger | condition | — | no |
| 4 | definition, R-5 period | **period** | — | **Edit 164-4** |
| 5 | definition, condition precedent | condition | — | no (Edit 2 preserves it) |
| 6 | definition, the backstop notice | **duty**, 15 days | — | no (the MOO-141 patch's Edit 2) |
| 7 | subdivision D 1, the descriptor | descriptor | — | **Edit 164-5** |
| 8 | subdivision D 3, DPB Director | **duty**, 30 days, **and not the Board's** | no | no |
| 9 | subdivision D 3, the application | **duty**, 15 days | no | no |
| 10 | subdivision G 4, the aggregate | **failure** | no | **Edit 164-6** |
| 11 | subdivision G 4, the period | **period** | — | **Edit 164-6** |
| 12 | subdivision G 4, pendency of an application | **period** | yes — moves **in** the member's favour | no |
| 13 | subdivision G 4, pendency of a request | **period** | yes — moves **in** the member's favour | no |
| 14 | subsection M 2, the 90 days | **duty** | no | no — card (i), §1.3 |
| 15 | subsection M 2, the tolling endpoint | **period** | yes — moved against the member | **Edit 164-1** |
| 16 | subsection M 2, clause (ii) | **exclusion** | — | **Edit 164-3** |
| 17 | subsection M 2, the D 4 / D 5 retention | **period** | **yes — the one residual.** Queue position only | no (the MOO-141 patch's Edit 3, now 120 days) |
| 18 | subsection M 2, the application duty | **duty**, 15 days | no | no |
| 19 | subsection M 2, that duty's trigger | **trigger** | yes — moves **in** the applicant's favour | no |

**Five endpoints, of which one moved against the member and is now repaired, three move in her or the
applicant's favour, and one — #17 — is the residual priced at $0.** #2 is the fifth and is neutralised,
twice over: by the decision-keyed floor where there is a decision, and by R-5 as cured by Edit 164-4 where
there is not (§2.4).

### 7.2 Counts, every one re-run today on the live base and on an applied copy

**SUPERSEDED IN PART AT REVISION 5. Read §15.8 instead; this table is left standing because
[MOO-187](/MOO/issues/MOO-187) F2 is about it and deleting it would hide the finding.** Three things
were wrong with it and all three are corrected at §15.8:

1. **The `acts upon` row predicted 7 and the true count is 9** (F2). Edit 164-1's READ contains
   *"acts upon"* **twice**, not once — in revisions 1 to 4 it was clause (a) and the cap; at revision 5
   it is the floor and the cap. `8 + 1 (Edit 1) + 1 (Edit 164-1 net) − 1 (Edit 2) = 9`. **The drafter
   did not notice that Edit 164-1 adds a second act-keyed term — in the count or in the
   classification — and that is the same root as F1.**
2. **These were whole-document counts.** From store revision 62 the §0 narrative quotes three of these
   anchor strings, so a whole-document count returns 2 for them. **§1-only is the right basis** and
   §13.1 adopted it; §15.8 is on that basis throughout.
3. **A predicted count is not a count.** The kit's own rule, set at `bill-text-s8` §5.37, was not
   applied here. Every figure at §15.8 is produced by `verify_r65.py`, which fails rather than prints
   if a count moves.

| Phrase | Store rev 61 | After both patches | Expected — **as predicted in revisions 1 to 4; see §15.8 for the counted figures** |
|---|---|---|---|
| `acts upon` | 8 | 7 | **WRONG — it is 9.** F2 |
| `act upon` | 8 | 11 | **11** — Edit 1 adds three |
| `last acts upon` | 1 | 1 | **1** |
| `first acts upon` | 2 | 3 | **3** — Edit 1 adds one |
| `acting upon` | 3 | 4 | **4** whole-document — **2 → 3 in enacted §1**; the third occurrence is in §6's commentary, not in the bill |
| `action upon` | 2 | 2 | **2** — Edit 164-5 moves one word before it, not the phrase |
| `30 days after the Board acts upon the request` | 1 | **1** at revision 6; **2** at revision 5 | Edit 164-1's clause (a), plus Edit 3's retention only while it read 30 days. **The identity pass 18 relied on is gone by the board's 120-day answer, not by this cut** — §1.1 |
| `48 days after the Board acts upon the request` | 0 | 1 | **1** |
| `120 days after the Board acts upon the request` | 0 | 1 | **1** — the MOO-141 patch's Edit 3 at revision 6; untouched by this cut |
| `the period allowed by this section for acting upon` | 0 | **3** | **3** — one concept, one formula, three sites |
| `the period allowed to it for acting upon` | 1 | **0** | **0** |
| `the 90 days allowed by this subsection` | 1 | **0** | **0** — item 124 would restore it once, correctly |
| `this definition allows for acting upon it` | 1 | **0** | **0** |
| `upon the Board's action upon a request` | 1 | **0** | **0** |
| `by reason of the Board's action upon a request` | 0 | 1 | **1** |
| `written notice of its decision upon the request` | 0 | 1 | **1** |
| `is pending` / `was pending` | 8 / 1 | 8 / 1 | **unchanged** — card (c) is not in the patch |
| typographic apostrophe `’` | **4** | **0** | **0** — §8 |

### 7.3 Conforming amendments — **one required, and it is in the patch**

**Edit 164-6.** It is the only one. The reasons, provision by provision:

- **Subdivision D 1 → the definition.** D 1 imports *"the time required by that definition"* and the
  descriptor that identifies which notice. Edit 164-5 repairs the descriptor; nothing else in D 1 refers to
  the words any of these edits changes. **No further amendment.**
- **The definition → subsection M.** The definition refers to tolling *"under subsection M"* generically
  and never to M 2's clause (ii) or to its tolling endpoint by its words. **No amendment.**
- **Subsection M 2 → subdivisions D 4 and D 5.** The retention sentence is untouched by this patch.
  **No amendment.**
- **Subdivision G 2 → subsection M.** G 2's floor refers to *"the period allowed to the member by
  subsection M"* — the **member's** period, not the Board's, and a different concept from the one Edit
  164-6 conforms. Edit 164-2 does not change that phrase. **No amendment.**
- **Subdivision G 4 → subdivision G 2.** G 4 suspends *"[n]o period stated in subdivision 2 or in this
  subdivision."* Edit 164-2 adds no new period to G 2; it lifts an existing limit in a new case. **No
  amendment.**
- **Subdivision J 1 and subsection C's reporting sentences.** Both report failures *"to make a
  determination, to give a notice, or to make a payment within a period required by this section."* None of
  the six edits creates or removes a duty, so neither report line moves. **No amendment.** (The J 1 gap
  item 127 identifies is pre-existing and is not mine.)
  **RE-RUN AT REVISION 6 for the five promotions, because this is the one item in §9 that an added duty
  would move. The answer is still no amendment, and here is each one.** **164-10** dates an existing duty
  and creates none. **164-11** and **164-12** create no duty — one conforms a formula, the other defines a
  word. **164-8** creates a **member's power** to file, not a Board duty; the Board's existing duty to
  report *"every such delay"* under subsection J is untouched and already covers the late notice that
  triggers it. **164-7** creates no duty either, and its saving sentence is drafted so that it cannot: it
  expressly does not determine *"the date by which the Board is required to act … or whether the Board has
  performed such a duty within a period required by this section."* **Its one express exception — the
  15-day duty on the application — supplies a date on which an existing duty falls due; it does not create
  the duty.** So a failure to meet it is reportable under J 1 and subsection C **by the words those
  provisions already have**, which is the result route (c) was taken to produce. **No amendment, and the
  reason is in the text rather than in this note.**
- **Subdivision B 4 f of § 51.1-142.2.** Reached by Edits 164-1 and 164-3 only through M 2's existing
  *"under this section or under subdivision B 4 f of § 51.1-142.2"*, which both edits preserve verbatim.
  **No amendment.**
- **§ 51.1-153, § 51.1-162, § 51.1-165, § 2.2-4001, § 2.2-4021, § 2.2-4025 et seq.** None refers to any
  word changed. **No amendment.**

**Ten referring provisions chased in both directions. One conforming amendment, in the patch.** This is
the fifth consecutive cut at which the answer has been *"none required"* on the Code side; it is the first
at which one is required **inside** enacted §1, and that is because this is the first cut that introduces
a formula a second provision already had in different words.

---

## 8. §6.7's four apostrophes — normalised, recorded, folded into no amendment

**Performed as a non-substantive normalisation, exactly as the Policy Director directed, and it is not
part of any of the eleven edits.**

> **RE-COUNTED AT REVISION 6 AND IT IS NOW TWO ASSERTIONS, NOT ONE.** At store revision 68 there are
> still **four** typographic apostrophes in enacted §1, and `verify_r68_v6.py` now asserts not only the
> count but the **confinement** — zero typographic apostrophes anywhere in §1 outside subdivision G 4's
> own character range. Revisions 1 to 5 asserted the count and stated the confinement; at revision 6 the
> confinement is counted too. The straight-apostrophe count has moved with the base and is **201** in
> §1 at store revision 68.

- **Count verified at store revision 61: four typographic apostrophes (U+2019) against 637 straight
  ones.** All four are inside subdivision G 4. Three are in *"the member's final qualifying retirement
  date"* or *"the member's behalf"*; the fourth is in the same subdivision's rescission passage.
- **It changes no meaning and it silently breaks exact-string anchoring**, which is why it is being done.
- **Applied as a whole-document substitution `’` → `'`, net character delta 0**, verified on both bases.
  After it, the typographic count is **0** and the straight count is **641**.
- **Recorded as a non-substantive normalisation and folded into no amendment.** It does not appear in any
  FIND or READ at §3, it carries no markup in §6, and it must be recorded in `bill-text-s8` §0 as a
  normalisation and not as an edit.
- **Order note for the applier: run the normalisation after the eleven substitutions, not before.** None
  of the eleven FIND strings contains a typographic apostrophe — checked again at revision 6, and
  `apply164.py` performs the normalisation only after all eleven substitutions have been made — so either
  order works, but running it last keeps the eleven counts reproducible against the stored base.

---

## 9. Drafter's note — every ambiguity I resolved, and how

**9.1 Why there are two decisions and not eight answers.** The Director's framing was right and it held
all the way through: cards (f) and (i) are one question, cards (b) and (h) are one question, and (c) sits
between them. **The proof that it held is §7.1** — once all 19 occurrences are classified, card (f) stops
being a judgment call and becomes a count: one endpoint moves against the member, and repairing it is 41
words. I did not know that when I started; I expected to recommend the verb definition.

**9.2 The ambiguity in "decide F-5 and the residual in one place, with one answer."** The Director also
said the residual is disposed to item 124 and is not mine to re-decide. I resolved the two as: **F-5 must
be drafted so that R-5 keys to the same date item 124 keys to** — the expiry of M 2's 90 days — **so that
the two agree if both are enacted and F-5 still answers if item 124 is declined.** §2.4. That is the only
reading on which one answer exists. **If the Director meant something else, Edit 164-4 is one word and I
will re-cut it; nothing else in the patch depends on it.**

**9.3 Why the 48-day cap, and why 48.** A bare notice-keyed endpoint is unbounded if the Board gives no
notice, which is the F-6 shape of defect and I am not going to introduce one while F-6 is open. The cap
uses the section's own numbers — Edit 2's 15 days, subsection A's 3, and the existing 30 — so it invents
no period. **The cap is also what holds Edit 164-1 to the carded 18 days** rather than to card (f)'s 78.

**9.4 Clause lettering, and why `(a)` and `(b)`.** M 2's tolling sentence already carries `(i)` and `(ii)`.
G 2's determination-date clauses use `(a)`, `(b)`, `(c)`. Using `(a)` and `(b)` inside a sentence that
already uses `(i)` and `(ii)` for a different purpose is the chapter's own practice and avoids a sentence
with two clause `(i)`s.

**9.5 "The person who filed the request", and why not "the member."** M 2's standing list has seven
classes and the tolling sentence speaks of *"the member or applicant."* Either class can file. **Naming the
filer names the actor and the recipient in one phrase** and covers both classes of tolling request without
reciting the list a third time.

**9.6 Why Edit 164-2's new limb repeats a 25-word cross-reference instead of saying "that sentence."**
Because the antecedent appears **after** the new limb. The section does not cross-refer by paraphrase, and
*"that sentence"* with a forward antecedent is worse than a repetition.

**9.7 What I resolved against myself.** I expected card (b)'s cure to be the simple notice-keyed endpoint,
and I drafted it that way first. It is option (b-2) at §2.2 and I recommend against my own first draft:
it restores 78 days, re-opens MOO-140's C2 and the retention's price, and **removes the act limb that
Edit 1's deeming attaches to.** The capped form keeps the limb and delivers the carded 18 days.

**9.8 What I did not resolve, and will not by drafting choice.** Card (c). Both candidates are drafted; the
choice between them moves an enacted board answer; it is at §10.1 and it is not mine.

**9.9 One thing I checked because the last six cuts have taught me to.** All three MOO-141-patch FIND
strings still resolve exactly once at store revision 61, after a seventh base move that landed in all
three of the provisions that patch reaches. **The patch does not need a re-cut for that move**, at either
revision 5 or revision 6. I would rather report that unasked than have it discovered at application.

**9.10 The patch moved under me mid-cut, and what I did about it.** This cut was built against the
MOO-141 patch at **revision 5**. [MOO-176](/MOO/issues/MOO-176) landed revision 6 — Edit 3 at **120
days** — while I was assembling it. **I re-ran every anchor and every count against the revision-6 base
rather than shipping against a superseded one**, and corrected every statement in this document that
depended on Edit 3's figure. There are four, and they are listed at §9.11 so a reviewer can check them
rather than take my word.

**9.11 The four places the 30/120 answer touched this cut, and what each now says.**

1. **§1.1's *Forst* paragraph.** It said the identity survives. **It does not** — the board's answer
   removed it. The point that survives is that Edit 164-1's clause (a) **keeps the act limb**, so Edit 1's
   deeming still reaches the tolling endpoint.
2. **§3.1's anchor note.** The short-form FIND was non-unique at revision 5 and is unique again at
   revision 6. **The full clause is the anchor on all three bases**, so neither answer strands it.
3. **§2.2's option (b-2) and §9.7.** The rejection no longer rests on the identity; it rests on the 78
   days, on MOO-140's C2, and on (b-2) removing the limb the deeming attaches to.
4. **Every price for the retention row.** MOO-163's $0 was for the 30-day retention.
   **[MOO-177](/MOO/issues/MOO-177) and [MOO-180](/MOO/issues/MOO-180) own the 120-day figure and I do not
   restate the old one as current.** Nothing in either decision turns on which figure it is.

**9.12 The standing caveat, in terms.** This is an internal working draft. It is not a Division of
Legislative Services bill, it has not been reviewed by counsel, and nothing in it states or implies that
it has been or that it is legally sufficient for introduction.

---

## 10. Open questions for the Policy Director — **all answered; this section is the record**

> **DISPOSED AT REVISION 6.** The two questions below became eleven at §15.9, and the Policy Director's
> disposition answered **all eleven and sent none back**. §16.1 carries the dispositions in one table.
> **§10.1's item-46 question is answered twice over: (c-2) is taken, and no item-46 card goes to the
> board.** §10.2's confirming sentence is declined. Nothing in this section is open.

**Three more were opened by store revisions 62 and 63, after this cut. They are at §13.12, none of them blocks the six edits, and §10.1 below is question 1 of the four.**

### 10.1 Card (c) — which candidate, and the item-46 question

**(c-1)** narrows item 46's carve-out and costs the identified member her allowance for the window between
the Board's first action on her disability application and the G 2 determination taking effect — bounded at
120 days after the determination date, unbounded in the late-notice case, 210 days in the tolled-floor
case after Edit 164-2. **(c-2)** confirms item 46 as enacted and costs nobody anything against today's
reading. **I recommend (c-2).** Neither is in the patch and neither will be applied until this is answered.
**This is the item-46 question the Director said would go to the board.**

### 10.2 Card (i) — belt-and-braces or not

**I recommend not.** The 33-word confirming sentence is drafted at §1.3. It buys certainty on M 2's 90-day
duty and it buys item 123's negative-implication argument against the section's other 72 *"no later than"*
periods, and it complicates item 124's trigger. **Not a blocker: card (i) is closed either way.**

### 10.3 Not a question — two things I am flagging so they are not rediscovered

- **Edit 3's retention could be conformed to notice as well**, which would put both of M 2's endpoints on
  the same footing at the endpoint level rather than at the phrase level. **I have not drafted it**: Edit 3
  is a board decision, now at 120 days on the board's own answer, and it is [MOO-176](/MOO/issues/MOO-176)'s
  to re-cut and not mine. If the Director wants it, it is 29 words at a FIND this patch does not touch.
- **F-5 removes the need for card C as the residual's fallback** (§2.4). Item 124 remains the Director's
  disposition; the fallback is now five words of already-existing text rather than a new sentence.

---

## 11. Verification at store revision 61

**Superseded as the current check by §13.1, which re-runs every count at store revision 63. The run below is retained as the record of what was verified at the time of the cut.**

### 11.1 The base

`bill-text-s8` on [MOO-42](/MOO/issues/MOO-42), document revision `3efccfe2-8332-4f4a-82ba-a9347141287f`,
revision number **3**, **271,611 characters**, fetched today. The §1 region I counted in — title line through the enactment clauses — spans **117,964 characters**.
`bill-text-s8-item-list`, revision number **3**, **323,866 characters**, read for items 46 and 124.

### 11.2 Anchors — eighteen counts, all 1

Every one of the six FIND strings counted in the **whole document** on each of three bases:

| Edit | Store rev 61 | + MOO-141 patch **rev 5** | + MOO-141 patch **rev 6** | Delta |
|---|---|---|---|---|
| 164-1 | 1 | 1 | 1 | +209 |
| 164-2 | 1 | 1 | 1 | +238 |
| 164-3 | 1 | 1 | 1 | +24 |
| 164-4 | 1 | 1 | 1 | +1 |
| 164-5 | 1 | 1 | 1 | +8 |
| 164-6 | 1 | 1 | 1 | +10 |
| **total** | | | | **+490** |

**The totals are identical on all three bases, which is the test of order-independence** — had any edit
overlapped an anchor of the MOO-141 patch at either revision, the count or the delta would have differed.

**The two candidate texts at §4 and the confirming sentence at §1.3 were counted too**: (c-1)'s FIND = 1,
(c-2)'s FIND = 1, and card (i)'s insertion point = 1, on all three bases. **None is applied.**

### 11.3 Post-application invariants — applied to a **copy**, every one checked

Applied to a copy of each base: final length **272,101** characters on store revision 61 alone,
**272,798** with the MOO-141 patch at revision 5, and **272,799** with it at revision 6; ~~every count in
§7.2 confirmed~~ — **struck at revision 5. [MOO-187](/MOO/issues/MOO-187) F2 is right that this claim
cannot stand: the `acts upon` row of §7.2 was a prediction, not a count, and the prediction was wrong.
A verification whose failure mode is to confirm the thing it failed to count is worse than no
verification, and that is the defect, not the row.** The remaining invariants were checked and hold:
**no FIND re-resolved after its own edit**; both of G 4's express *"first"*s intact; `is pending` and
`was pending` unchanged at 8 and 1. **§15.8 replaces this paragraph at store revision 65 on a counted
basis.**

### 11.4 What I did not verify, stated as a limit

- **I did not verify that the MOO-141 patch's three edits produce the document the Director approved**, at
  either revision 5 or revision 6 — only that their FIND strings still resolve once at store revision 61 and
  that my six are independent of them on both. That patch's own verification is its own.
- **I did not re-read [MOO-176](/MOO/issues/MOO-176)'s revision-6 document in full.** I took Edit 3's new
  READ from its cut script and re-derived the base from it; I did not audit its reproductions, its
  four-limb day-37-to-day-127 pricing, or its answer to the 120/120 collision. **If any of those moved an
  anchor I rely on, the counts at §11.2 would have caught it, and they did not.**
- **I did not re-price anything.** The 78 days, the $0, the $204,000 and the 67.4% are MOO-141's and
  MOO-163's figures, cited and not recomputed.
- **I did not read § 51.1-156, § 51.1-162 or § 51.1-165 at source this heartbeat.** The claims at §7.3 that
  they refer to no changed word are from the text of enacted §1's references to them, not from those
  sections.
- **The 14-month figure at §4.1 is pass 10's**, from item 46 as written, and I have not reconstructed it.

### 11.5 Not applied to the store

**Nothing in this document has been written to `bill-text-s8` or to the §7 item list.** The apostrophe
normalisation at §8 is **drafted and verified, not applied**; it is to be performed as part of the next
store revision carrying these edits, and recorded in §0 as a non-substantive normalisation.

---

## 12. Status and next step

> **SUPERSEDED AT REVISION 6 — the current status and next step are at §16.8.** The counsel pass this
> section was written for is [MOO-187](/MOO/issues/MOO-187), which is `done`; its 26 findings are
> disposed at §15; and §10.1 is answered. **What remains is a counsel pass on the five promotions and
> the eleven-edit interactions, and then application.** §16.8.

**Ready for the Red Team / Counsel Reviewer.** Then back to the Policy Director with the §10.1 answer.

1. **Counsel pass** on the six edits, the two decisions, and the two candidates at §4. **§13 was added
   after that pass began** and carries two further candidates — 164-7 and 164-8 — plus the F-9 narrow-side
   decision at §13.4; the reviewer should treat §13.4, §13.5 and §13.7 as in scope and the six edits as
   unchanged from what they received.
2. **The §10.1 answer** — card (c), which is the item-46 question for the board — and the three further
   questions at §13.12.
3. **Application**, in either order with the MOO-141 patch, with the three MOO-162 gates and the apostrophe
   normalisation performed in the same store revision. **Verified at store revision 63 at §13.1: nothing
   needs a re-cut for the eighth, ninth or tenth base move.**

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by counsel,
and nothing here states or implies that it has been. Pre-decisional and internal.**

---

## 13. Re-verification at store revisions 62 and 63 — the base moved twice *after* this cut, and what it changes

**Why this section exists.** Revisions 1 and 2 of this document were cut and verified against
`bill-text-s8` at **store revision 61** (document revision 76, 271,611 characters). Within four minutes
of the delivery comment the base moved twice more:

| Document revision | Written | Store revision | Characters | §1 characters | What it did |
|---|---|---|---|---|---|
| 76 | 13:54 | **61** | 271,611 | 117,980 | the base this cut was verified against |
| 77 | 17:39 | **62** | 306,404 | 120,888 | [MOO-169](/MOO/issues/MOO-169)'s counsel pass disposed and seven Director answers enacted — **twenty-one substitutions** in D 1, G 4, L, M 2 and N |
| 78 / 79 | 17:43 / 17:44 | **63** | 320,665 | 121,439 | **§7 item 124 answered by the board as option (d)** and enacted — **two sentences inserted in M 2**, the member-triggered deemed denial |

**The eighth, ninth and tenth base moves. Both revisions touched provisions this cut amends.** Store
revision 62 rewrote **D 1** (Edit 164-5's provision), **G 4** (Edit 164-6's provision) and **M 2** (Edits
164-1 and 164-3' provision); store revision 63 inserted two sentences into **M 2** again. **Five lines of
§1 differ between store revision 61 and store revision 63** — M 2, G 4, D 1, subsection L and subsection
N — and three of the five are provisions reproduced at §6.

**The headline: the cut stands, unchanged, with every FIND still unique.** No edit text is altered by this
section. What is new is at §13.3 (the classification moves from 19 to 21), §13.4–13.5 (F-9's narrow side,
decided, and the one real consequence of it), §13.6–13.7 (what item 124's enactment does to F-5, to card
C, and to the endpoints), §13.9 (a new ordinal cross-reference into M 2 that constrains every future edit
to that subsection), and §13.11 (corrections).

### 13.1 Anchors re-counted at store revision 63 — twelve, on three bases, every one exactly 1

`verify_r63.py` in the apply kit reproduces the run below from a fetched `bill-text-s8`.

| | store rev 63 | + MOO-141 patch rev 5 | + MOO-141 patch rev 6 |
|---|---|---|---|
| Edit **164-1** card (b) | 1 | 1 | 1 |
| Edit **164-2** card (h) | 1 | 1 | 1 |
| Edit **164-3** card (j) | 1 | 1 | 1 |
| Edit **164-4** F-5 | 1 | 1 | 1 |
| Edit **164-5** F-9 | 1 | 1 | 1 |
| Edit **164-6** conforming | 1 | 1 | 1 |
| held candidate **(c-1)** | 1 | 1 | 1 |
| held candidate **(c-2)** | 1 | 1 | 1 |
| card **(i)** insertion point | 1 | 1 | 1 |
| **Amendment delta** | **+490** | **+490** | **+490** |
| Apostrophes normalised | 4 | 4 | 4 |

**And the MOO-141 patch's own three FINDs still resolve exactly once at store revision 63** — `E1 = 1,
E2 = 1, E3 = 1` — so that patch does not need a re-cut for the ninth or tenth base move either. **The
order-independence claim in the header holds at store revision 63 on all three bases**, with the identical
+490 delta. Nothing in this cut needs re-cutting for these two moves.

**One scope change in the check itself, and it would have produced a false alarm if I had not made it.**
Every count above is taken over **enacted §1 only**. Store revisions 62 and 63 **quote three of these
anchor strings in the §0 revision narrative and in the §5 sweep** — the G 4 period formula, the D 4 / D 5
retention and M 2's 90-day sentence — so a whole-document count now returns **2, 2 and 3** for those three
and 1 for the rest. §1 is the text that is amended; the narrative is commentary that is not. The apply kit
has always counted §1 only; this is the first base at which the distinction is load-bearing, and
`verify_r63.py` states it at the top rather than leaving it to be rediscovered.

**A second anchoring lesson, from this section's own drafting.** My first anchor for candidate 164-8 was
*"and the Board shall state every such delay in the report required by subsection J."* — which **resolves
twice**, in D 1's lateness sentence and in D 4's incomplete-application sentence. It is replaced by a span
long enough to be unique and the count is asserted at 1. **A short anchor that reads as if it could only
mean one thing is not evidence that it does.**

### 13.2 The §6 reproductions are re-spliced from store revision 63, because three of them were stale

**Every reproduction at §6 is now spliced programmatically from the live body at store revision 63** by
`repro63.py`, which supersedes `repro.py` and locates each provision **by content rather than by line
index** — line indices moved when store revision 62 rewrote five lines of §1. D 1, G 4 and M 2 as
reproduced in revisions 1 and 2 of this document were **stale behind anchors that still resolved exactly
once**, which is the fourth time on this file that has happened and the reason the splice is programmatic.

**The apostrophes are re-checked and the §8 record is unchanged: four typographic apostrophes in §1,
all four still inside subdivision G 4**, at the same four phrases, against 637 straight ones. Store
revisions 62 and 63 introduced none and removed none.

### 13.3 The classification moves from **19 to 21** — and Decision 1's claim is re-tested and survives verbatim

Store revision 63's two inserted sentences add two occurrences of `act upon` to §1. Counts over §1 at
store revision 63: `acts upon` **8**, `act upon` **9**, `acting upon` **2**, `action upon` **2** —
**21** in total, where §7.1 classified **19**.

**Both new occurrences are negatives, and neither is an endpoint:**

| | The occurrence | What it does | Class |
|---|---|---|---|
| **20** | *"Where the Board **does not act upon** a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file with the Board written notice that the period has expired"* | condition on the Board's **non**-action; confers a power on the person | **not an endpoint** — nothing begins, ends or is measured from an act |
| **21** | *"Where the Board **does not act upon** the request within 30 days after that notice is filed, the request is denied on the first day after the expiration of those 30 days"* | condition on the Board's **non**-action; fixes a date by reference to the member's notice | **not an endpoint** — the date is measured from the member's filing, not from any act of the Board |

**So the claim §1.2 rests Decision 1 on is unchanged at store revision 63: after this cut exactly one
act-keyed endpoint remains where a token action can cost anybody anything** — Edit 3's D 4 / D 5
retention, queue position only. A verb definition would now have had to move **21** occurrences rather
than 19, and the two new ones are precisely the kind a definition of *"act upon"* would have reached
without being needed there: defining the verb would have put content into two express negatives whose
whole function is to describe the Board doing nothing.

### 13.4 F-9's narrow side, decided — ***"first required"* does not narrow Edit 164-5, and Edit 164-5 stands as drafted**

**The Policy Director's ask, in terms: store revision 61 made D 1's descriptor read *"first required"*,
which *"on its face selects the opening statement and not the backstop notice — the narrow side of F-9. I
am not deciding it; you are."*** Decided: **the narrow reading is right about the sentence it is in, and
it has no purchase on the sentence Edit 164-5 amends.** Three grounds, in order of weight.

**1. They are different sentences doing different work.** *"First required"* sits in D 1's **filing-duty**
sentence:

> The member shall file the notice of retirement required by § 51.1-153 … no later than 30 days after the
> date on which the Board gives the member the written statement of the member's earliest qualifying
> retirement date and final qualifying retirement date **first required** by the definition of *"final
> qualifying retirement date"* in subsection A.

Edit 164-5's descriptor sits in D 1's **lateness-extension** sentence, four sentences later, and qualifies
a different noun — *"any notice of a date"*, not *"the written statement"*.

**2. The descriptor's own words are open, and *"any"* cannot be narrowed by a *"first"* in another
sentence.** The lateness sentence lists **three** documents in parallel: *"that written statement, any
notice of a later approved date required by that definition, or any notice of a date required by that
definition [by reason of] the Board's action upon a request."* Reading the third limb to mean the opening
statement would make it **duplicate the first limb** and leave the action-keyed notice unreached.

**3. The action-keyed notice is the one the MOO-141 patch's Edit 2 re-timed.** Edit 2 moves that notice
from *"15 days after it acts upon"* to *"15 days after it gives its decision upon"* the request. A
descriptor that selected only the opening statement would strand the limb that Edit 2 is about — which is
the whole reason the Policy Director took F-9 as a gate on applying the patch.

**Consequence for the patch: none. Edit 164-5 is unchanged, its FIND still resolves once at store
revision 63, and the four words still do exactly what §3.5 says they do.** What the narrow reading **is**
right about is the filing-duty sentence, and that has a consequence of its own, which is next.

### 13.5 The real consequence of *"first required"* — D 1 grants the member a permission she has no vehicle to exercise. **Candidate 164-8, not applied**

**The defect, in four lines.** D 1's filing-duty sentence gives the member **one** 30-day window, running
from the **first** statement. D 1's lateness-extension sentence then says that where **any** of the three
documents is late, *"the member **may state** an effective date of retirement that is no earlier than the
first day of the month following the month in which the Board gives the statement or notice."* For the
**second and third** documents — a later-approved-date notice, and the action-keyed notice — that
permission can arrive **after** the member's single window has closed. **She may state a date, and she has
nothing to state it in.**

**I checked whether the vehicle exists elsewhere, because the defect only bites if it does not.**
Subdivision D 1 contains no power to amend, replace or withdraw a filed notice of retirement — `amend`,
`withdraw`, `replacing`, `substitute` each **0** occurrences in the subdivision. **§ 51.1-153 is silent
too**, read at source today at `law.lis.virginia.gov`: subsection A requires *"written notification to
the Board setting forth the date the retirement is to become effective"* and says nothing about
modification; subsection E bounds only how far **back** a stated date may be. **So the permission is
unexercisable in exactly the case the extension exists for.**

**Candidate 164-8 — append one sentence to D 1's lateness-extension sentence. 81 words, +485 characters.
Not applied.**

> **FIND** (count = **1** at store revision 63; the short form of this anchor resolves twice — §13.1):
>
> ```
> the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.
> ```
>
> **READ:**
>
> ```
> the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. Where the Board gives any notice described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice already filed, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes any notice previously filed.
> ```

**Who, what, by when, or else:** the **member** may file **that notice or a replacement**, **no later than
30 days after the Board gives the late notice**, and the consequence is stated — it **is** a notice filed
within the period D 1 allows, so it carries D 1's existing retroactivity sentence and § 51.1-153's
satisfaction with it, and it **supersedes** the earlier notice so the Board is never holding two.

**Why the one-word alternative is not a cure, so the Director is not offered a false cheap option.**
Striking *"first"* from the filing-duty sentence — one word — **does not reach the problem**: the later
documents are not *"the written statement"* at all, they are *"notice of a later approved date"* and
*"notice of a date … by reason of the Board's action"*, so deleting *"first"* leaves them outside the
sentence and merely reinstates the ambiguity store revision 61 removed deliberately. **There is one
candidate here, not two, and it is take-it-or-leave-it.**

**Price, and which way it cuts. CORRECTED AT REVISION 5 — [MOO-187](/MOO/issues/MOO-187) F26: the
candidate is wider than the sentence it appends to, and the price statement below covered only part of
what it reaches.** The member gains a filing window she does not have today; the Board gains no duty it
does not have today (it is already required to give the notices, already required to report every delay
under subsection J, and already bound by the extension). **Against today's text it costs the
Commonwealth nothing in the class the extension already decided in her favour — the member who uses the
window to retire later than she otherwise could have.**

**The class the price statement did not cover.** 164-8's condition is keyed to when the notice
**arrives** — *"after the expiration of the period allowed by this subdivision for filing the notice of
retirement"* — and not to whether the notice is **late**. A later date can be approved, and notice of it
given perfectly on time, long after the member's single 30-day window has closed: the definition lets
her request a later date *"at any time before the date that would otherwise apply"*, and the Board must
give notice of an approval *"no later than 15 days after the approval."* First statement 1 February,
window closes 3 March, later date approved 1 September, notice given 10 September — **on time, and
164-8 fires.** D 1's lateness extension never reached that case, so it never decided it in her favour.

**I am not narrowing the candidate, and the Director should know why.** A member who has just been given
a later retirement date and has no vehicle to file for it has the same problem whether the notice was
late or timely; reaching both is the better rule, and keying the cure to **lateness** would leave the
on-time case with a permission and no vehicle — which is the defect 164-8 exists to cure. **But the
Director is approving a candidate wider than the sentence it appends to, and §13.12 question 3 now says
so.** It is in
scope of neither of this issue's two decisions and I have therefore not applied it: **§13.12 question 3.**

### 13.6 §7 item 124 is enacted — what it does to F-5, to card C, and to one claim I made

**Store revision 63 enacted item 124 as the board's option (d), the member-triggered denial**, inserting
two sentences in M 2:

> <u>Where the Board does not act upon a request for reconsideration within the 90 days allowed by this
> subsection, the person who filed the request may file with the Board written notice that the period has
> expired. Where the Board does not act upon the request within 30 days after that notice is filed, the
> request is denied on the first day after the expiration of those 30 days, and that denial constitutes
> the final determination of the Board upon the reconsideration and a case decision as defined in
> § 2.2-4001 for the purposes of this subsection.</u>

**Correction to §2.4, and it matters.** I wrote that R-5, once Edit 164-4 points it at the section, *"keys
to the expiry of M 2's 90 days — the identical date item 124's deemed denial keys to."* **On the enacted
words that identity does not hold**, because the board took option (d) rather than the carded (b): the
denial falls **30 days after the member files an expiry notice**, not on the 91st day after the request.
The two dates are now **different**, and they can be separated without limit, because the member may file
the expiry notice at any time or never.

**That makes Edit 164-4 more useful than §2.4 claimed, not less, and this is the corrected statement.**
R-5's limb keys to the **expiry of the period allowed for acting** — day 90 — which happens **whether or
not the member ever files an expiry notice**. So:

- the member who files the expiry notice gets a dated denial **and** the floor;
- **the member who does not file it gets the floor anyway**, and she is the member the deemed denial does
  nothing for.

**Card C is now dead rather than held.** It was held as the fallback if item 124 were declined; item 124
is enacted, and the enacted sentences occupy the ground card C was drafted for. I am not holding it and I
am not re-drafting it. The gate the Policy Director set on item 124 is **discharged**.

### 13.7 New §7 item 130 — the endpoints the deemed denial does not reach. **Candidate 164-7, not applied, and the trade stated both ways**

**The drafter of store revision 63 declined to deem the denial an act and recorded why: *"that verb is the
subject of MOO-164."* It is therefore mine to put to the Director, and here it is.** The enacted sentences
fix a **date** but do not make that date an act of the Board. **Four endpoints in this section are keyed to
the Board's act, and on the text as it now stands none of them arrives where the Board never acts:**

| | The endpoint | Where | Consequence where the Board never acts |
|---|---|---|---|
| 1 | *"tolls … **until 30 days after the Board acts upon the request**"* | M 2, Edit 164-1's sentence | the member's tolling **never ends** |
| 2 | *"excluding any period after the expiration of the 90 days … **and before the Board acts upon the request**"* | M 2 clause (ii), Edit 164-3's site | the exclusion from the 120-day aggregate is **unbounded** |
| 3 | *"retains its filing date for the purposes of subdivisions D 4 and D 5 **until the Board acts upon the request**"* | M 2, the MOO-141 patch's Edit 3 | queue position retained **without end** |
| 4 | *"the Board shall act upon the application **no later than 15 days after it acts upon the request**"* | M 2 | the duty **never triggers** |

**Edit 164-1 does not cure this and does not purport to. Say so plainly.** Its cap reads *"in no case later
than **48 days after the Board acts upon the request**"* — keyed to the act. Where the Board acts but gives
no notice, the cap binds and that is what it is for. **Where the Board never acts, neither limb (a) nor
limb (b) nor the cap engages**, because there is no act and there is no notice of a decision: store
revision 63's own record states that a denial by operation of these sentences *"carries no writing, no
reasons and no notice."*

**Candidate 164-7 — insert two sentences in M 2, immediately after the enacted denial sentence.
REVISED AT REVISION 5: 170 words, +898 characters. Not applied.**

> **FIND** (count = **1** at store revision 63):
>
> ```
> the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.
> ```
>
> **READ:**
>
> ```
> the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. Where a request is denied by operation of the preceding sentence, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial. Except for the purposes of the duty of the Board under this subsection to act upon an application no later than 15 days after it acts upon the request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.
> ```

**REVISED AT REVISION 5 on [MOO-187](/MOO/issues/MOO-187)'s F19 and F20. Both were serious, both were
mine, and the first of them would have hurt the member the candidate exists to protect.**

**Four things to see in it, because each is a drafting choice I made rather than a word I found.**

1. **It is Decision 1's method, not its opposite.** It does **not** define *"act upon"* and it does not
   touch any of the 21 occurrences. It supplies a **date** for one event the section creates and leaves
   the verb alone — which is what §1.2 recommended and why option (f-4) beat the verb definition.
2. **Its form is the bill's own — and at revisions 3 and 4 it was not, in two places. F19 and F20.**

   **F19 — the confinement carried one of Edit 1's two trigger limbs, not both.** Edit 1 triggers where
   **(A)** *"a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon
   a request"* **or** where **(B)** *"a date is fixed by reference to the month in which the Board acts,
   or last acts, upon a request."* The revision-3 and revision-4 text carried **(A) only**, and §13.7 and
   §14.1 both described it as lifted *"word for word."* **It was not.** Limb (B) is the limb that reaches
   **occurrence #2** — the definition's reset, *"the first day of the second month following the month in
   which the Board **last acts** upon a request the filing of which tolled that period"* — **the sentence
   whose entire function is to give the member a usable retirement date once her tolling ends.** Without
   limb (B), 164-7 **ended her tolling and removed her reset in the same move**: on counsel's facts,
   tolling ends 19 September, R-5's floor as cured by Edit 164-4 keys to April and gives 1 June, three
   and a half months in the past, and the definition's 12-month cap then binds with no reset. **She can
   be left unable to retire in a qualifying retirement at all — which is the injury the reset exists to
   prevent, and she is not in that position without 164-7.** Limb (B) is now in, in Edit 1's own words,
   and it cannot cut against her: the deemed date is the denial date, which is later than the nothing she
   has today.

   **F20 — the second sentence was *not* Edit 1's saving clause, and describing it as one was the best
   evidence for the argument it invited.** Edit 1's saving reads *"Nothing in the preceding sentence
   determines **the date by which the Board is required to act upon a request, to make a determination,
   or to give a notice or a decision**, or whether the Board has **performed such a duty within a period
   required by** this section."* The old 164-7 saving read *"Nothing in the preceding sentence **relieves
   the Board of the duty to act upon a request for reconsideration**, or determines whether the Board has
   **acted upon a request within the period allowed by** this section."* Different in both limbs — a
   **second, differently-worded saving clause for the same deeming mechanism**, which is the very defect
   §3.6 exists to prevent, created in the paragraph that asserted it away. And the difference was
   **substantive**: Edit 1's dropped first limb is what keeps the deeming out of the Board's **duty
   dates**, and dropping it silently is how the old draft reached endpoint 4.

   **The revision-5 saving is Edit 1's, verbatim, with one express exception.** *"Except for the purposes
   of the duty of the Board under this subsection to act upon an application no later than 15 days after
   it acts upon the request, nothing in the preceding sentence determines …"* **One formula for one
   concept, and the carve-out that reaches limb 3 is now visible on the face of the text instead of
   hidden in a 30-word difference.** A Board arguing that the two savings must mean the same thing now
   loses on the words.
3. **It makes Edit 164-1's cap work in the only case where that cap currently fails.** With 164-7 the
   deemed act date exists, so the tolling ends at **denial + 48 days** at the outside, by Edit 164-1's own
   cap and with no new number.
4. **It reaches endpoint 4, the Board's 15-day duty on the application, and at revision 5 it says so
   expressly.** Reaching it is deliberate and it is the one limb a reviewer should press on. Carving it
   out would leave the member whose retention has ended with no decision on her application; reaching it
   means a duty on the Board is triggered by the Board's own inaction, 15 days after the deemed denial.
   **I think reaching it is right. At revisions 3 and 4 it was reached by omitting a limb of the saving
   clause; at revision 5 it is reached by an express exception that names the duty** — same effect, and
   the Director can now decline that one limb without re-drafting the sentence.

**The trade, stated both ways, because it is a genuine one and not mine to resolve.** Unbounded tolling is
**not** simply an exposure: it extends the member's final qualifying retirement date without limit, which
**favours the member** and defers settlement, which is a cost exposure the Fiscal & Impact Modeler owns and
I have not priced. Bounding it at denial + 48 days **cuts against the member** in the one case where the
Board has wholly failed to act. **Candidate 164-7 is therefore not applied: §13.12 question 2.**

### 13.8 Decision 2 is now supported by **five** sites in the bill, not three

§2.1 rested Decision 2 — *from the act, except where the period is one within which a person must act;
then from notice* — on **three** places where the bill already has the rule. **Store revision 62 added two
more, neither of them mine, both enacting the same rule on the Director's answers:**

- **D 1, the certification-failure clock.** Now runs *"no later than 30 days after the date on which the
  **certification is given to the member** or, where that person is not the member, no later than 30 days
  after the date on which the notice required by subdivision G 4 is given to that person."* A period within
  which a person must act, keyed to **notice**, with a separate limb for the person who gets a different
  notice.
- **G 4, the § 51.1-162 C waiver floor.** *"Where the Board gives a notice required by this subdivision on
  the death of a member later than 30 days after the death, the period stated in subsection C of
  § 51.1-162 within which a waiver must be made **does not expire before the thirtieth day after the
  notice is given** to the person entitled to make it."* A period within which a person must act, keyed to
  notice, **with a floor** — which is structurally the same instrument as card (h)'s floor and Edit 164-2's
  exception limb.

**Cards (b) and (h) are stragglers from a rule the bill now applies in five places. That is a stronger
statement of §2.1's argument than the one I made, and it was made by someone else's revision.**

### 13.9 Cross-reference re-check at store revision 63 — one new reference into M 2, and it constrains every future edit to that subsection

**The result first: no conforming amendment beyond Edit 164-6 is required at store revision 63, and the
cut and both new candidates are safe against the new reference.**

**What is new, and it is a trap for the next drafter.** Store revision 62 put an **ordinal**
cross-reference into D 1: *"**the second sentence of subdivision M 2** does not apply to such a failure."*
M 2's second sentence is the deeming sentence — *"Every determination, certification, redetermination …
is a determination of the Board for the purposes of this subsection."*

**Verified against the file as it now stands and as this cut and both candidates would leave it:**

| Change | Where it inserts | Does it disturb *"the second sentence of subdivision M 2"*? |
|---|---|---|
| Edit **164-1** | rewrites M 2's **sixth** sentence in place | **No** — no sentence added |
| Edit **164-3** | rewrites clause (ii) of the same sentence | **No** |
| Item 124's enacted sentences | after M 2's **third** | **No** — already in the base and already after it |
| Candidate **164-7** | after M 2's **fifth** | **No** |
| Card **(i)**'s confirming sentence, recommended against at §1.3 | after M 2's **third** | **No** |

**But any future edit that inserts a sentence into M 2 *before* the deeming sentence silently strands that
reference**, and nothing in the text warns a drafter of it. **Widened at revision 5 on
[MOO-187](/MOO/issues/MOO-187) F25: insertion is not the only way. Any edit that *splits* M 2's first
sentence into two strands it just as silently** — and M 2's first sentence is a 1,300-character sentence
carrying eight standing classes and three review windows, which store revision 62 has already rewritten
once and which is the likeliest sentence in the subsection to be broken up. **The same warning now
applies to candidate 164-7's own two uses of *"the preceding sentence"*** (§14.7). I am not amending it — an ordinal reference
that is currently correct is not a defect, and converting it to a quoted-phrase reference is a change
nobody has agreed. **It is recorded here, and it is §13.12 question 4: whether the Director wants that
reference converted on the next pass that touches D 1.**

**Ten referring provisions re-chased in both directions at store revision 63**, as at §7.3: same result,
**no amendment required outside §1**, and the three other *"the period allowed…"* phrases in §1 remain
three different concepts, none of them the one Edit 164-6 unifies.

### 13.10 Corrections to statements in revisions 1 and 2 of this document

Listed so the reviewer can check them rather than take my word, in the same form as §9.11.

| | Statement as it stood | Corrected statement |
|---|---|---|
| 1 | §2.4: R-5's date is *"the identical date item 124's deemed denial keys to"* | **Not identical.** Option (d) keys the denial to the member's expiry notice + 30 days; R-5 keys to the expiry of the allowed period. §13.6 |
| 2 | Card C is *"held as the fallback"* if item 124 is declined | **Dead.** Item 124 is enacted at store revision 63; the gate is discharged. §13.6 |
| 3 | §7.1: *"19 occurrences, classified"* | **21** at store revision 63; both new ones classified, and Decision 1's claim unchanged. §13.3 |
| 4 | §2.1: the bill has Decision 2's rule *"in three places"* | **Five**, two added by store revision 62. §13.8 |
| 5 | §6: *"spliced programmatically from the live `bill-text-s8` at store revision 61 today"* | re-spliced from **store revision 63** by `repro63.py`; D 1, G 4 and M 2 as previously reproduced were stale. §13.2 |
| 6 | §11's base, counts and deltas | re-run at store revision 63; **same counts, same +490**. §13.1 |

**Nothing in the six edits, the two decisions, the (c-1)/(c-2) candidates or the card (i) analysis is
changed by any of these corrections.**

### 13.11 What I did not verify at store revision 63, stated as a limit

- **I did not re-read the whole of store revisions 62 and 63.** I read both §0 narratives in full, and I
  diffed **§1 line by line** between store revisions 61 and 63 — five lines differ, and I read all five.
  Subsections **L** and **N** changed and are **not** reproduced here, because this cut does not touch
  them and no anchor or cross-reference of mine reaches them.
- **I did not price anything.** Item 130's trade at §13.7 and candidate 164-8's at §13.5 are stated in
  days and in direction only. Costing belongs to Fiscal & Impact Modeler.
- **I did not retrieve Rule 2A:2**, and store revision 63's record says it has not been retrieved — so
  whether an Article 5 period can run from a silent decision remains open on [MOO-186](/MOO/issues/MOO-186).
  It does not bear on any of the six edits or on either candidate.
- **Nothing is applied to the store.** Still true at store revision 63, for the six edits, the apostrophe
  normalisation and both new candidates.

### 13.12 Questions for the Policy Director — now four

**Question 1 is §10.1 unchanged: card (c), which candidate, and the item-46 question.** The three below
are new, and **none of them blocks the six edits**, which are verified and ready at store revision 63.

| | Question | My recommendation | If you say nothing |
|---|---|---|---|
| **2** | **Item 130** — apply candidate **164-7**, deeming a request denied by operation of M 2 to be acted upon on the date of the denial, for period purposes only? | **Apply it.** It is Decision 1's method, it uses Edit 1's own words, and it is what makes Edit 164-1's cap work where the Board never acts. But it bounds a window that currently runs in the member's favour, so it is a trade and it is yours. | the four endpoints at §13.7 stay unbounded in the no-act case and the residual stays open on [MOO-97](/MOO/issues/MOO-97) |
| **3** | **D 1's vehicle gap** — apply candidate **164-8**, giving the member 30 days to file or replace her § 51.1-153 notice where a later notice is late? | **Apply it.** The permission D 1 already grants is otherwise unexercisable, and § 51.1-153 does not supply the vehicle. | D 1 keeps a permission the member cannot use in the second and third of its three cases |
| **4** | **The ordinal reference** — convert *"the second sentence of subdivision M 2"* to a quoted-phrase reference on the next pass that touches D 1? | **Yes, but not in this cut.** It is correct today; it is fragile tomorrow. | the next insertion into M 2 before the deeming sentence strands it, with no warning in the text |

---

## 14. The Policy Director's decision of 17:57 — §7 item 130's residual, taken here, with all three limbs

**This section answers the Director's comment of 12 October, 17:57:50. It changes no decision, no edit and
no markup above it.** It does four things: it records that the limb the Director describes as *"in nobody's
record before today"* was delivered seven seconds earlier as **§13.7 endpoint 4** and is already reached by
candidate 164-7; it **answers the open question** the Director left open about whether subsection A's
late-Board backstop protects limb 1; it **recommends route (c)** and gives the cost of being wrong; and it
reports **one case no route on the table reaches**, which is new and which I am carding rather than curing.

**Base: store revision 64.** It is **record only** — enacted §1 is **byte-identical** to store revision 63,
proved rather than asserted at §14.6. **Nothing in this cut needs a re-cut for it.**

### 14.1 The three limbs against my four endpoints — the same text, counted twice, and they agree

The Director enumerates **three limbs with no backstop**; §13.7 enumerated **four endpoints keyed to the
Board's act**. They are the same text:

| Director's limb | §13.7 endpoint | The keying words in §1 at store revision 64 | Reached by 164-7 because the period… |
|---|---|---|---|
| **1** — M 2's tolling of *"any period within which the member or applicant must act"* | **1** — *"until 30 days after the Board acts upon the request"* | 1 occurrence | **ends upon** the act |
| **1** (same limb, second site) | **2** — clause (ii)'s *"and before the Board acts upon the request"* | 1 occurrence | **ends upon** the act |
| **2** — the D 4 / D 5 filing-date retention. *The only one with a third-party cost* | **3** — *"retains its filing date … until the Board acts upon the request"* | 1 occurrence | **ends upon** the act |
| **3** — **NEW to the Director** — *"the Board shall act upon the application no later than 15 days after it acts upon the request"* | **4** — the 15-day duty | 1 occurrence | **is measured from** the act |

**Limb 3 is §13.7's endpoint 4, and candidate 164-7 already reaches it as drafted.** §13.7 point 4 says so
in terms: *"It reaches endpoint 4, the Board's 15-day duty on the application, and I did not carve that out.
That is deliberate and it is the one limb a reviewer should press on."* The Director's comment and document
revision 3 crossed — 17:57:43 against 17:57:50 — so this is parallel discovery, not a gap. **No new text is
needed for limb 3.** The textual reason it is caught is in the table above and verified at §14.6: the
15 days is a period ***measured from*** the Board's acting, and 164-7's confinement clause — lifted word for
word from the MOO-141 patch's Edit 1 — reaches periods that *"begin or end upon, **or are measured from**,
the Board's acting."* A limb keyed by *"measured from"* needs that third form; a cure drafted only for
*"begins or ends upon"* would have missed it.

**One fact worth having, because it is an independent reason clause (ii) cannot reach limbs 2 and 3.** The
D 4 / D 5 retention and the 15-day duty are **not two sentences. They are one.** 112 characters apart, no
full stop between them, verified at §14.6 group A. So the Director's reason — *"neither the retention nor
the 15-day duty is tolling"* — is right, and there is a second: route (b) amends **clause (ii) of the
tolling sentence**, and both limbs live in **the sentence after it**. No amendment confined to clause (ii)
can reach either, on any reading.

### 14.2 The open question, answered: subsection A's backstop does **not** protect limb 1, and the *"notwithstanding"* fight is immaterial to it

The Director records this as *"probably protected … open question, not a finding,"* and notes that both
experts' arguments turn on it. **I can close it, and not by winning the priority argument — by showing the
priority argument does not matter.** The sentence, in full, from §1 at store revision 64 (1 occurrence, and
it is **Edit 164-4's own site**, which is why the two must be read together):

> Where the Board does not act upon a request the filing of which tolled the running of the member's final
> qualifying retirement date under subsection M within the period this definition allows for acting upon it,
> **and the date that would otherwise apply under this definition is earlier than** the first day of the
> second month following the month in which that period expired, the member's final qualifying retirement
> date **is**, notwithstanding any other provision of this definition, **that first day**.

**It is a floor, not a cap, and it operates in the same direction as the defect.**

1. **Its trigger is a one-way comparison.** It engages only where the otherwise-applicable date is
   ***earlier*** than the computed day. It has no limb that engages where that date is *later*.
2. **Its consequent raises an early date to a fixed day.** *"is … that first day."* It contains no
   *"in no event later than"* and no *"in no case later than"* — verified; the two cap formulas in this
   definition are in other sentences.
3. **A later final qualifying retirement date is more time for the member, not less.** The definition's
   first sentence fixes it at *"12 months after the member's earliest qualifying retirement date"* — the
   **outer** date by which she must retire to qualify. So the backstop is **member-protective against an
   early date**, and that is all it is.
4. **The defect in limb 1 is the opposite direction.** Unbounded tolling pushes the date **later** without
   limit. The backstop never engages against it, and where it does engage it moves the date **later still**.

**So whichever way the *"notwithstanding"* question is resolved, limb 1 is unaffected by it.** If the
*"notwithstanding"* is confined to the definition, the backstop does not reach M 2's tolling. If it beats
M 2's tolling outright, it still only raises a date that is too early. **Either way it cannot bound a date
that is too late. Route (a) — do nothing — therefore leaves all three limbs open, not two.**

**And one correction to how my own work was characterised, stated plainly.** The Director names my
revision-6 **§6.2(c)** as turning on this limb. It does not. §6.2(c) is about the Board that **acts late**:
tolling ends 30 days after it acts, the retention runs 120, and the member's own clocks run in the gap
between. It concerns the **tolling endpoint**, not subsection A's backstop, and it assumes an act that
arrives. **The limb here is the Board that never acts at all.** Different case, different provision — so
§6.2(c) is not authority for *"probably protected,"* in either direction. I have not read counsel's
MOO-169 M8 and I am not characterising it.

### 14.3 Route (c) is recommended — candidate 164-7, unchanged — and here is the cost of being wrong

**Recommendation: route (c). Adopt candidate 164-7 as drafted at §13.7. No new words, no new number.**
§13.7 held it unrecommended because the bounded-versus-unbounded trade is a policy call. **Two things have
changed since, and both point the same way:**

- **§14.2 removes the alternative.** Route (a) was defensible while limb 1 might already be protected. It is
  not protected, so route (a) leaves an **unenforceable duty** in the bill — limb 3 is a duty with an actor,
  an object and a deadline, and **no date on which the deadline falls**. *Who, what, by when, or else*: limb
  3 fails *by when* on its own text, and that is a defect rather than a trade.
- **The Director's incidence warning cuts against route (b) harder than the comment puts it.** I accept the
  warning in full and add the drafting reason. G 4's sentence — *"a failure of the Board to act upon such a
  request … shall not extend that aggregate"* — sits where the aggregate is a cap **on the Board's own
  clocks**, so the words make the Board bear its delay. M 2 clause (ii)'s aggregate caps **the member's
  tolling**, so the identical words make the **member** bear it. **Same words, reversed incidence**, which
  is exactly the trap §3.6 and Decision 1 exist to avoid. Route (b) is a policy choice wearing the clothes
  of a conforming amendment, and I would not sign it as a conforming amendment.

**The cost of being wrong, both ways, in one line each.**

- **If 164-7 is adopted and that is wrong:** the member whose Board wholly failed to act has her tolling
  bounded at **denial + 48 days** (Edit 164-1's existing cap, no new figure) and her D 4 / D 5 retention at
  **denial + 120 days** (Edit 3 at revision 6). She keeps the deemed denial, which store revision 63 makes a
  case decision, and her judicial review with it. **Bounded, computable, and nothing is forfeited** —
  G 2's arrears sentence still pays in full.
- **If 164-7 is declined and that is wrong:** tolling runs without end; clause (ii)'s 120-day aggregate
  never binds; the queue position is held without end **at third-party cost — the one limb with a priced
  exposure**; and the 15-day duty never falls due, so the member who has won nothing also gets no decision
  on her application. **Three open limbs and one unenforceable duty.**

**What I still do not own, and am not asserting.** Unbounded tolling defers settlement, which is a cost
exposure the **Fiscal & Impact Modeler** owns; I have not priced it and §14.3 does not. If the Director
wants the deferred-settlement side before deciding, that is MOO-170's class of question, not mine.

### 14.4 The one case **no** route on the table reaches — new, carded, not cured

**Route (c) buys all three limbs only for the member who files the expiry notice.** Store revision 63 took
the board's **option (d)**, the member-triggered denial, and its first sentence reads *"the person who filed
the request **may** file with the Board written notice that the period has expired."* ***May* is a power,
not a duty.** So where the Board never acts **and** the member never files that notice, **there is no denial
date**, and candidate 164-7 — which fixes the deemed act *"on the date of that denial"* — supplies nothing.

**This corrects one cell of the Director's table, and in route (b)'s favour.**

| | Limb 1 (tolling) | Limb 2 (retention, priced) | Limb 3 (15-day duty) |
|---|---|---|---|
| **(c)** reconsideration request, she files the expiry notice | cured | cured | cured |
| **(c)** reconsideration request, she does **not** | **open** | **open** | **open** |
| **(c)** request **under the definition** — ADDED AT REVISION 5, F22 | **open, unconditionally** | n/a — the retention sentence reaches only reconsideration requests | n/a |
| **(b)** either way | cured | open | open |

**ADDED AT REVISION 5 — [MOO-187](/MOO/issues/MOO-187) F22, and it corrects the framing of this
section and not only a cell.** Revision 4 attributed the uncured case to the member's **choice** —
*"**may** is a power, not a duty"* — and its two rows were *"where she files"* and *"where she does
not."* **For a request under the definition of *"final qualifying retirement date"* there is no row she
can be in.** M 2 tolls on **two** classes of request; store revision 63's expiry-notice and
deemed-denial machinery opens *"Where the Board does not act upon **a request for reconsideration**,"*
and is confined to that class. **So for a definition request there is no expiry notice to file, no
denial date, and nothing for 164-7's *"on the date of that denial"* to attach to. The gap is
structural, not elective, and this document must not describe it as elective.**

Worked: she files a definition request on 1 January for approval of a later retirement date; the
definition's 30 days expire 31 January; the Board never acts. Her final qualifying retirement date and
every period within which she must act are tolled **indefinitely**; clause (ii)'s 120-day aggregate
never binds, because Edit 164-3's exclusion takes the Board's lateness out of it; and there is no notice
she can file. **Edit 164-4's five words are her only protection — R-5 keys to the expiry of the allowed
period whether or not anyone files anything — which is why Edit 164-4 matters more than §2.4 said and
why §13.10 correction 1 was the right correction to make.**

**Candidate 164-7-B closes it, and it is a policy choice I am not making.** One sentence replacing
164-7's deeming sentence, with two triggers and one formula:

> ```
> Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of "final qualifying retirement date" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period.
> ```

**It is the same trade as route (c)'s and it runs the other way for this class.** Unbounded tolling on a
definition request **favours** the member in the sense that it moves her final qualifying retirement
date later; bounding it at *"the day after the expiration of that period"* + 30 (or + 48 under Edit
164-1's cap) **cuts against her** where the Board has wholly failed to act on a request she made to be
allowed to retire **later**. **I have drafted it and not applied it: question 9.**

**Route (b) is unconditional and route (c) is not.** That is a real difference in reach and it was not in
front of the Director. It does **not** change my recommendation, for three reasons:

1. **In the never-notifies case limb 1 favours the member.** Unbounded tolling gives her more time, and
   **Edit 164-4 already protects her floor without any notice from anyone** — §13.6: R-5 keys to the expiry
   of the allowed period whether or not she ever files. So the limb route (b) uniquely reaches is the limb
   that, in that case, hurts her.
2. **The limbs that bite in that case are 2 and 3, and route (b) reaches neither** — §14.1: they are in the
   sentence after clause (ii).
3. **The only thing that would reach them is an automatic denial on the 91st day, and the board has already
   declined it.** It chose option (d) over the deemed denial on the 91st day. **I will not draft round that
   choice**, and §13.6 is why card C is dead rather than held.

**So the elective case is carded, not cured, and the structural case has a candidate. New item for the
Director's list: the member who files a request, never files
the expiry notice, and has an application pending holds a D 4 / D 5 queue position with no end and gets no
decision on her application — at third-party cost, in the one limb that is priced.** It belongs with §7
item 130, it is in nobody's record before this document, and **MOO-190** is reviewing store revision 63 now.
**§14.8 question 5.**

### 14.5 What this does to MOO-97's held route (b)

**Nothing I am asking for.** The Director has held MOO-97's route (b) until this lands, and on my
recommendation it should be **declined rather than held**, for §14.3's incidence reason and because route (c)
makes it redundant for limb 1 in every case where the denial date exists. **But the §14.4 column is a reason
to decide that consciously rather than by implication:** route (b) is the only thing on the table that
bounds tolling where no denial date is ever fixed. If the Director wants that case covered at all, (b) + (c)
is the only combination that does it — and then clause (ii) would be bounded twice, once by G 4's words and
once by the deemed date, which is two instruments for one concept and would need the second to be drafted
as an exception to the first. **I am not drafting that combination. It is a policy choice and it is
question 6.**

### 14.6 Verification at store revision 64 — `verify_r64.py`, 0 failures

**Store revision 64 is record only, and the proof is byte-identity rather than my word for it.**

| | Store rev 63 | Store rev 64 |
|---|---|---|
| whole document | 320,665 characters | 324,617 characters |
| **enacted §1** | **121,439** | **121,439 — byte-identical** |
| `act/acts/acting/action upon` in §1 | 21 | **21**, unchanged |

What revision 64 added is **§7 item 131** and two record edits: M 2's Article 5 grant is keyed to *"such
case decision"* whose nearest antecedent is the completion sentence, and the enacted characterisation is
bounded *"for the purposes of this subsection"* while § 2.2-4026 sits outside it. **That is not a defect
this cut creates or cures, and §14.7 reports what 164-7 does to it.**

`verify_r64.py` re-runs **every** count from `verify_r63.py` on the revision-64 body — it does not rely on
the byte-identity it proves — and adds three new groups. **0 failures.**

- **Twelve anchors, three bases, every one exactly 1 in enacted §1.** Store revision 64; + the MOO-141 patch
  at revision 5 (Edit 3 at 30 days); + at revision 6 (120 days). **Amendment delta +490 on all three**, the
  same figure as at store revisions 61, 62 and 63. **So this cut remains order-independent of the MOO-141
  patch and indifferent to the 30/120 answer — now across four base moves.**
- **Group A — limb reach.** Each of the four keying phrases occurs exactly once; limbs 2 and 3 are proved to
  be one sentence (0 full stops between them); and 164-7's confinement clause is checked to contain both
  *"begins or ends upon"* and *"is measured from"*, and to be Edit 1's formula verbatim.
- **Group B — the backstop.** The late-Board sentence located and counted at 1, its trigger checked to be
  the *"is earlier than"* comparison, its consequent checked to be *"is … that first day"*, and the absence
  of any cap formula in it checked explicitly. **§14.2 stands on these four checks, not on reading.**
- **Group C — antecedent and ordinal integrity.** §14.7.
- **The apostrophes: still four, still all inside G 4**, at store revision 64. §8 stands.

### 14.7 What candidate 164-7 does to item 131 and to D 1's ordinal reference — checked, and the answer is nothing

**Both were worth checking because both are the kind of thing that breaks silently, and §13.9 exists
because one of them nearly did.**

**Item 131 — *"such case decision"*. Unaffected.** M 2's sentence order at store revision 64, verified:

| # | Sentence | |
|---|---|---|
| 1 | the reconsideration right | |
| 2 | *"Every determination, certification, …"* | ← **D 1's ordinal reference points here** |
| 3 | *"The Board shall act upon a request for reconsideration within 90 days."* | |
| 4 | the member's expiry notice | store rev 63 |
| 5 | the deemed denial — *"… and a case decision as defined in § 2.2-4001 for the purposes of this subsection."* | store rev 63 |
| **5a** | **candidate 164-7's two sentences would insert here** | **not applied** |
| 6 | the tolling sentence, with clause (ii) | limb 1 |
| 7 | the retention **and** the 15-day duty | limbs 2 and 3, one sentence |
| 8 | *"Upon completion of a reconsideration … shall constitute a case decision as defined in § 2.2-4001."* | ← **nearest antecedent of *"such case decision"*** |
| 9 | the Article 5 judicial-review grant — *"such case decision"* | item 131 |

164-7 attaches to the **end of sentence 5**, which is **before** sentence 8, so the nearest antecedent of
*"such case decision"* **remains sentence 8** — unmoved. And **164-7's own text contains no *"case
decision"***, so it introduces no competing antecedent. **It neither cures nor worsens item 131.** The one
honest qualification: it puts 583 more characters between sentence 5's characterisation and sentence 9, so a
proximity argument *for* sentence 5 gets marginally weaker. Item 131 does not rest on proximity and
**MOO-190** owns it.

**D 1's ordinal reference — *"the second sentence of subdivision M 2"*. Unaffected, and re-proved.** It
points at sentence 2. Store revision 63 inserted at 4 and 5; 164-7 inserts at 5a. **The ordinal is unmoved
at store revision 64**, as §13.9 reported at 63. The designator *"2."* is not a sentence and the count above
does not treat it as one.

**One thing 164-7 adds to that trap, and I am recording it against myself.** Its first sentence opens *"Where
a request is denied by operation of **the preceding sentence**"*, and its second opens *"Nothing in **the
preceding sentence**."* Those are ordinal references of the same family as the one §13.9 warns about. They
are correct as drafted and at the insertion point verified above. **Anything later inserted between the
enacted denial sentence and 164-7's first sentence strands the first; anything inserted between 164-7's two
sentences strands the second.** The form is the bill's own — Edit 1 uses *"the preceding sentence"* twice for
the same reason — so I have not changed it, but the applier and the next drafter should have it in writing.
**§14.8 question 4 now covers both references, not one.**

### 14.8 Questions for the Policy Director — six at revision 4; **eleven at revision 5, and the full list is at §15.9**

| | Question | My recommendation | What turns on it |
|---|---|---|---|
| **1** | **Card (c)** — candidate (c-1) or (c-2), and the item-46 question | **(c-2)**, twenty words, costs nobody anything against today's reading. §4, §10.1 | **unchanged, still yours, still the one that goes to the board** |
| **2** | **§7 item 130's residual — route (a), (b) or (c)** | **route (c): adopt candidate 164-7 as drafted.** §14.3 | all three limbs; limb 3 is an unenforceable duty without it |
| **3** | **Card (i)** — the 33-word confirming sentence | **against.** §1.3, §10.2 | unchanged |
| **4** | Convert D 1's **ordinal reference** on the next pass that touches D 1, and note that 164-7 adds two of its own | **yes, but not in this cut** | correct today, fragile tomorrow. §14.7 |
| **5** | **NEW — the member who never files the expiry notice**, holding a D 4 / D 5 place with no end and no decision on her application | **card it to MOO-190 with item 130.** I am not drafting round the board's option-(d) choice | the priced limb, in the one case no route reaches. §14.4 |
| **6** | **NEW — MOO-97's route (b): decline, or keep as (b) + (c)?** | **decline.** §14.3, §14.5 | (b) is the only thing that bounds tolling with no denial date — decide it knowingly |

### 14.9 What I have not done

- **Nothing is applied to the store.** Candidate 164-7 remains **not applied**: the Director's comment says
  *"nothing in this comment is a drafting instruction,"* and I have treated it as one.
- **I have not re-cut any of the six edits.** Enacted §1 did not move. §14.6.
- **I have not drafted route (b), the (b) + (c) combination, an automatic 91st-day denial, or a cure for
  §14.4.** Each is a policy choice and each is a question above.
- **I have not priced deferred settlement.** Fiscal & Impact Modeler.
- **[MOO-187](/MOO/issues/MOO-187)'s counsel pass has since landed** — 26 findings across two passes.
  **§15 disposes of every one of them**, re-cuts two of the six edits, and revises candidate 164-7.

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by counsel,
and nothing here states or implies that it has been. Pre-decisional and internal.**

---

## 15. The counsel pass is in — [MOO-187](/MOO/issues/MOO-187)'s 26 findings, every one disposed of, and what changed in the text

**[MOO-187](/MOO/issues/MOO-187) ran two passes: 18 findings on document revision 2 against store
revision 62, and 8 more on document revision 4 against store revision 64. Running total 26 — 0 fatal,
11 serious, 8 moderate, 7 minor — and 19 null results. No finding is rejected. Two edits are re-cut,
one candidate is substantially revised, four new candidates are drafted, nine statements in this
document are corrected in place, and the apply kit is repaired.**

**The three that changed the substance, in one line each.**

- **F3 — Edit 164-2 as drafted was a no-op.** Its new limb tested the determination against the one limb
  of G 2's floor that never conflicts. Card (h) would have stayed uncured and the document would have
  said it was cured. **Re-cut at §3.2.**
- **F19 — candidate 164-7 carried one of MOO-141 Edit 1's two trigger limbs and I described it as lifted
  word for word.** It ended the member's tolling and removed the reset that gives her a retirement date
  when tolling ends, in the same move. **Revised at §13.7.**
- **F1 — Edit 164-1's 48-day cap is itself act-keyed, so M 2's tolling endpoint is not closed**, and
  §0.1's headline claim and §1.1's classification row were false. The 18 days are real; the *"closed"*
  was not. **Corrected in place; the recommendation survives on reasons that do not depend on it.**

### 15.1 Every finding, with its disposition

**Pass 1 — document revision 2, store revision 62.**

| | Finding | Disposition |
|---|---|---|
| **F1** | the 48-day cap is act-keyed; endpoint #15 is not closed; §0.1's headline is false | **ACCEPTED. §0.1, §1.1's table row and §1.2 corrected in place.** The cap is **not** changed — holding it at 48 is what keeps card (b) at +18 days and keeps MOO-140's C2 and three closed decisions where they are. **Candidate 164-9 at §15.4 is the version that closes the remaining 60 days, drafted and not applied: question 7** |
| **F2** | §7.2 predicts `acts upon` = 7; it is 9 | **ACCEPTED. §7.2 marked superseded, §11.3's "every count confirmed" struck, §15.8 replaces both on a counted, §1-only basis.** `verify_r65.py` now **counts** it and fails if it moves |
| **F3** | Edit 164-2's limb names only the 30-day limb of a two-limb requirement; the 38 words are a no-op | **ACCEPTED IN FULL. Edit 164-2 re-cut at §3.2**, naming the requirement in the floor sentence's own words, both limbs. 38 words → 59, +238 → +366 characters |
| **F4** | §2.3's arithmetic omits G 4's suspension `S` of G 2's own 120-day limit | **ACCEPTED. §2.3's condition restated as `notice_day + 30 + T_after > 120 + S`**, and the class the cure is for is now named: the prompt-first-action class, which is MOO-141's class. **No text change to Edit 164-2.** In the memo's risk section |
| **F5** | the 210-day bound fails; clause (ii) excludes the Board's lateness from its own cap | **ACCEPTED. §2.3 restated: the true bound is `60 + 30 + 120 + the Board's lateness`, unbounded on the face of the text.** The term is pre-existing; **Edit 164-3 widens its reach and this document now says so.** Bounding it is **question 8**, and the board's already-approved **m8-a** on [MOO-97](/MOO/issues/MOO-97) is the instrument I recommend over a second one here |
| **F6** | M 2's *"within 90 days"* states no commencement — the only one of five *"shall act upon"* duties that does not | **ACCEPTED. Candidate 164-10 at §15.4 — five words, *"after the request is filed"*, not applied: question 10.** Escalated since the pass: store revision 63 keys **the member's route into court** to the same unfixed date |
| **F7** | §6.3 and §6.6 stale against the live base | **DISCHARGED at revision 3, and re-discharged at revision 5** — store revision 65 moved D 1 again (+137) and §6 is re-spliced by `repro65.py` |
| **F8** | limb (b) keys the **member's** clock to notice given to **the filer** | **ACCEPTED. Edit 164-1 re-cut at §3.1** — notice **to the member and to the person who filed the request** |
| **F9** | candidate (c-1) also narrows G 2's *"was pending"* validating limb, and §4.1 prices only the first | **ACCEPTED. §4.2 records it as a second, independent reason to prefer (c-2).** No change to (c-1), which is not recommended |
| **F10** | candidate (c-2) defines *"pending"* twice in one subsection and borrows G 2's most overloaded verb | **ACCEPTED. (c-2) redrafted at §4.2**: *"grants or denies it"* for *"determines it"*, and an express *"Notwithstanding the definition in subdivision 4"* opener. 20 words → 28 |
| **F11** | R-6's *"determines"* condition is a route by which occurrence #2's classification fails | **ACCEPTED AS A CARD, not drafted.** Counsel's own view is that it is strained and would not win; the fix is one clause in a sentence this cut does not touch. **Recorded at §15.5 for the next pass that opens the definition** |
| **F12** | item 124 would re-create two formulas for one concept inside M 2 — **now realised in enacted text** | **ACCEPTED. Candidate 164-11 at §15.4**, conforming the enacted expiry-notice sentence to the same formula. Not applied: **question 11**, and it is as much [MOO-42](/MOO/issues/MOO-42)'s as mine |
| **F13** | §7.3's *"period allowed"* sweep names three others; there are six, plus a second *"time allowed"* | **ACCEPTED. §3.6's sweep replaced with the full nine-row table, counted mechanically.** The conclusion — one conforming amendment — is unchanged |
| **F14** | §2.4 keys R-5's floor to the wrong month in the boundary case | **SUPERSEDED** by §13.10 correction 1, which counsel agrees goes further and is right |
| **F15** | *"72 'no later than' periods"* is 74 | **ACCEPTED. §1.3 corrected.** Counted at store revision 65: **74**, and `shall act upon` is **5**, which the document had right |
| **F16** | §6.4 calls item 46 the fifth-from-last sentence of G 2; it is the seventh | **ACCEPTED and verified independently** — I split the live subdivision and counted: eleven sentences, item 46 is seventh from the end. §6.4 corrected |
| **F17** | §7.3 mis-describes D 6's phrase | **ACCEPTED. Corrected in the new §3.6 table**, row 6 |
| **F18** | the amended tolling sentence carries four enumerated items in two series plus an unlettered limit | **ACCEPTED, and cured rather than noted.** The re-cut at §3.1 has **no clause lettering at all** |

**Pass 2 — document revision 4, store revision 64.**

| | Finding | Disposition |
|---|---|---|
| **F19** | 164-7's confinement carries Edit 1's limb (A) only, so it ends tolling and removes the member's reset | **ACCEPTED IN FULL. Limb (B) added verbatim at §13.7**, and the *"word for word"* claim at §13.7 and §14.1 is withdrawn and replaced with what the two texts actually say |
| **F20** | 164-7's second sentence is not Edit 1's saving clause, and calling it one is the best evidence for the argument it invites | **ACCEPTED. The saving is now Edit 1's, verbatim, with one express exception naming the 15-day duty.** One formula for one concept; the carve-out that reaches limb 3 is visible instead of hidden in a 30-word difference |
| **F21** | the apply kit hard-fails on the current base; README names two different scripts as current; two of this cut's FINDs resolve twice whole-document | **ACCEPTED. §15.7 and the kit itself.** `verify_r6.py` and `verify.py` retired, README corrected, **the §1-only scope moved into the apply instructions, not only the scripts' docstrings** — because the thing that goes wrong is a replace, not a count |
| **F22** | the definition-request class is uncured **structurally**, not electively, and §14.4's table says otherwise | **ACCEPTED. §14.4's table and framing corrected, and candidate 164-7-B drafted there** — one sentence, two triggers, one formula. Not applied: **question 9** |
| **F23** | Edit 164-1's no-notice endpoint is ambiguous between act + 30 and act + 48, and the cut assumes the second | **ACCEPTED and cured rather than put to the Director.** The re-cut at §3.1 states the cap as a freestanding outer limit, so act + 48 is what the words say. §2.2's table row 4 annotated |
| **F24** | §13.9 repeats §7.3's *"three others"* | **ACCEPTED** — carried from F13; the new §3.6 table is the single place the sweep now lives, and §13.9 points at it |
| **F25** | §13.9's fragility note is narrower than the fragility — splitting M 2's first sentence strands the ordinal too | **ACCEPTED. §13.9 widened**, and extended to 164-7's own two uses of *"the preceding sentence"* |
| **F26** | candidate 164-8 is keyed to **arrival**, not **lateness**, so it reaches a class D 1's extension never decided | **ACCEPTED as a disclosure, not a narrowing. §13.5 now states the uncovered class and says why I am not narrowing the candidate**, so the Director approves it knowing it is wider than the sentence it appends to |

**The 19 null results are not restated here.** Two are worth one line because they are load-bearing:
**N1** — the occurrence classification was independently re-enumerated and holds, with a twentieth
occurrence hunted under six alternative forms and not found; and **N18** — counsel reached §14.2's
answer on the subsection A backstop independently before revision 4 existed, and agrees it is a floor
and not a cap.

### 15.2 The two edits re-cut, side by side

| | Revisions 1–4 | Revision 5 | Why |
|---|---|---|---|
| **164-1** | *"until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after the Board gives **the person who filed the request** written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request"* — 41 words, +209 | *"until 30 days after the Board gives written notice of its decision upon the request **to the member and to the person who filed the request**, but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the Board acts upon the request"* — 46 words, +233 | **F8** (whose clock), **F23** (no-notice endpoint), **F18** (lettering) |
| **164-2** | *"consistently with **the sentence** of this subdivision that requires notice to be given **no less than 30 days** before the determination takes effect"* — 38 words, +238 | *"consistently with **the requirement** of this subdivision that notice be given **no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination**, before the determination takes effect"* — 59 words, +366 | **F3** — the old limb tested the one requirement that never conflicts |

**Neither re-cut changes a figure, a designator, a defined term or a recommendation.** Edit 164-1's
endpoint arithmetic is identical in every case the old text actually reached: 0 where decision and
notice land together, +18 in the carded case, +18 in the gap-(i) case, +18 capped where no notice is
given. **What changed is that the words now say it.**

### 15.3 What I did not change, and why — three places where I am declining counsel's fix direction

1. **F1 — I did not give the 48-day cap a second limb.** Counsel's suggested *"48 days after the later
   of (i) the Board's acting and (ii) the expiration of the period allowed … for acting upon the
   request"* closes the 60-day residual, and on MOO-141's facts it moves the endpoint from day 55 to
   day 115. **That is card (f)'s full 78 days, which is the movement option (b-2) was rejected for at
   §2.2 and option (f-2) at §1.1** — it reverses the direction of effect the MOO-141 patch was priced
   on, re-opens MOO-140's settled C2 exposure and MOO-163's and MOO-177's figures. **That is a policy
   decision with a price, and it is the Director's, not a repair I make inside a counsel pass.** The
   words are drafted as **candidate 164-9** and the claim they falsify is corrected. **Question 7.**
2. **F6 — I did not put the five words into the patch.** *"[A]fter the request is filed"* is new text in
   a sentence no card in this issue reaches, and it now carries the member's route into court. The
   drafting rule is to propose it in the note, not to add it. **Candidate 164-10. Question 10, and I
   recommend taking it.**
3. **F11 — I did not open the definition's penultimate sentence.** One clause would close it, counsel's
   own view is that the argument it guards against is strained, and this cut has no card in that
   sentence. **Recorded at §15.5 for the next pass that opens the definition.**

### 15.4 The three new candidates, drafted and not applied

**Candidate 164-9 — F1. Close the remaining 60 days at M 2's tolling endpoint. Five words into Edit
164-1's cap.**

> **Edit 164-1's READ as it stands at §3.1**, with its final clause replaced:
>
> ```
> … but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the later of the Board's acting upon the request and the expiration of the period allowed by this section for acting upon the request
> ```

*What it does.* On MOO-141's facts (`F = 7`, `D = 85`) the endpoint moves from **day 55** to **day
115** — limb (b), the notice limb — with an outer bound at day 138. **It closes endpoint #15 and makes
§0.1's original claim true.** *What it costs.* It is the full 78 days of card (f), so MOO-140's C2
exposure, MOO-163's and MOO-177's retention figures and the MOO-141 patch's own direction of effect all
have to be re-read against it. **It uses the formula Edits 164-3, 164-4 and 164-6 introduce, so it adds
no concept.** *My recommendation:* **not in this cut.** If the Director wants the 60 days, take it as a
separate decision with the Fiscal & Impact Modeler in the room.

**Candidate 164-10 — F6. Give M 2's 90-day duty a commencement. Five words.**

> **FIND** (count = **1** in §1 at store revision 65; **4** whole-document — F21)
>
> ```
> The Board shall act upon a request for reconsideration within 90 days.
> ```
>
> **READ**
>
> ```
> The Board shall act upon a request for reconsideration within 90 days after the request is filed.
> ```

**+27 characters.** It is the only one of the section's **five** *"shall act upon"* duties with no
stated commencement; the other four all state one. **Three things in this document now depend on the
expiry of that period being determinate** — Edit 164-3's exclusion, Edit 164-4's floor, and §2.4's
agreement claim — **and since store revision 63 the member's power to file the expiry notice, which is
her route into a case decision and therefore into court, depends on it too.** *My recommendation:*
**take it.** It moves no figure, states no new duty, and it is the kind of thing Legislative Services
returns a draft over. **Question 10.**

**Candidate 164-11 — F12. One concept, one formula, inside M 2. Conforming.**

> **FIND** (count = **1** in §1 at store revision 65)
>
> ```
> Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file with the Board written notice that the period has expired.
> ```
>
> **READ**
>
> ```
> Where the Board does not act upon a request for reconsideration within the period allowed by this section for acting upon the request, the person who filed the request may file with the Board written notice that the period has expired.
> ```

**+23 characters. No change of meaning:** the sentence is expressly about a request **for
reconsideration**, for which this section allows 90 days. **This is the same defect card (j) was a case
of and the same cure Edit 164-6 is.** At store revision 65 *"the 90 days allowed by this subsection"*
occurs **twice** in §1 — this sentence and clause (ii); Edit 164-3 removes the clause (ii) one and
leaves this one standing against **three** instances of the conformed formula. *My recommendation:*
**take it, and route it to [MOO-42](/MOO/issues/MOO-42) as well**, because it is their enacted sentence
and the applier should not be surprised by it. **Question 11.**

### 15.5 Carried forward, not drafted — F11

**The definition's penultimate sentence** opens *"Where the Board's action upon a request determines a
member's final qualifying retirement date under this definition, the Board shall state that date in its
decision upon the request."* R-6's floor then keys to *"a decision or notice required by the preceding
sentence."* **A Board arguing that its *action* did not *determine* the date — the statute did —
defeats the duty in the first sentence and leaves R-6 with nothing to key to**, and R-5 does not rescue
that case because the Board **did** act within the period. One clause closes it: *"Where a member's
final qualifying retirement date is determined under this definition by reference to the Board's action
upon a request"*. **Not drafted into this cut, no card in this issue reaches that sentence, and counsel
agrees the argument is strained. Recorded so the next pass that opens the definition has it.**

### 15.6 Every statement in §0 to §14 that is corrected in place, so a reviewer can check them rather than take my word

| | Where | Was | Is |
|---|---|---|---|
| 1 | **§0.1** | *"exactly one act-keyed endpoint remains where a token action can still cost anybody anything"* | **two**, and the second is Edit 164-1's own cap. 18 of 78 days repaired, 60 disclosed |
| 2 | **§1.1 table, row 1** | endpoint #15 *"closed"* | **partly** — floor and cap both act-keyed; residual 60 days; candidate 164-9 closes it |
| 3 | **§1.2** | cost of being wrong *"$0 at the central estimate … at the one endpoint"* | **two rows** — the retention **and** up to 60 days of tolling per request |
| 4 | **§1.3** | *"72 'no later than' periods"* | **74** |
| 5 | **§2.3** | conflict wherever `notice day + 30 + T > 120` | `notice_day + 30 + T_after > 120 + S`, and the class named |
| 6 | **§2.3** | *"absolute outer bound … 210 days"* | `60 + 30 + 120 + the Board's lateness`; **300 if m8-a lands, unbounded if not** |
| 7 | **§3.6** | *"Three others exist"* | **eight others**, in a nine-row table, counted |
| 8 | **§6.4** | item 46 is the *"fifth-from-last"* sentence of G 2 | **seventh-from-last** |
| 9 | **§7.2 / §11.3** | `acts upon` after both patches = 7; *"every count in §7.2 confirmed"* | **9**, counted; the confirmation claim struck |
| 10 | **§13.7 point 2 / §14.1** | 164-7's confinement *"lifted word for word"* from Edit 1 | **it carried one of two limbs**; limb (B) now added and the claim withdrawn |
| 11 | **§13.7 point 2** | 164-7's second sentence is *"Edit 1's own saving clause"* | **it was not**; it is now, verbatim, with one express exception |
| 12 | **§14.4** | the uncured case is the member's **choice** | **elective for reconsideration requests, structural for definition requests** |
| 13 | **§4.2** | (c-2) *"until the date on which the Board determines it"*, 20 words | *"grants or denies it"*, with an express non-application, 28 words |
| 14 | **§13.5** | 164-8 costs nothing *"except in the case the extension already decided in her favour"* | **plus a class the extension never reached** — on-time notice after the window closes |

**Three further figures move because the text moved, not because they were wrong:** the patch delta
**+490 → +642**, Edit 164-1 **41 → 46** words, Edit 164-2 **38 → 59** words.

### 15.7 The apply kit, repaired — F21, the finding most likely to cause actual damage

**What was wrong.** `verify_r6.py`, as committed, read the whole document and asserted `count == 1`. It
**hard-fails** on store revisions 63, 64 and 65, because the §0 revision narrative quotes anchor strings.
And `README.md` said *"`verify_r63.py` is the current check"* at line 3 and *"`verify_r6.py` — **the
current check**"* at line 28, naming the script that fails. §13.1's claim that *"the apply kit has
always counted §1 only"* was not true of `verify_r6.py`.

**Measured at store revision 65, §1 against whole document:**

| String | §1 | Whole document |
|---|---|---|
| **Edit 164-6's FIND** (the G 4 period formula) | 1 | **2** |
| **Candidate 164-7's FIND** (the enacted denial sentence) | 1 | **2** |
| MOO-141 Edit 3's FIND (the D 4 / D 5 retention) | 1 | **2** |
| **Candidate 164-10's FIND** (M 2's 90-day sentence) | 1 | **4** |
| Edits 164-1 to 164-5, 164-8, 164-11, both card (c) candidates | 1 | 1 |

**Two of them are this cut's own strings.** A whole-document find-and-replace on Edit 164-6 — which is
what the FIND/READ form invites — **edits the §0 revision narrative as well as the bill**, corrupting
the record of store revision 62, 63 or 65.

**Repairs made.**

1. `verify_r6.py` and `verify.py` **deleted**, not retained as *"the record of what was run"* — a script
   that fails is not a record, and leaving it next to a README that calls it current is how it gets run.
2. `README.md` rewritten: **one** current check (`verify_r65.py`), **one** current splicer
   (`repro65.py`), and the superseded `verify_r63.py` / `verify_r64.py` / `repro63.py` named as
   superseded in one place.
3. **The §1-only scope is now in the apply instructions in capitals, not only in a docstring:**
   *"Apply every FIND inside enacted §1 only. Three of these strings occur in the §0 narrative. A
   whole-document replace will corrupt the revision record."*
4. `apply164.py` rewritten to slice §1 before substituting and to **assert the §0 narrative is
   byte-identical after application.**

### 15.8 Verification at store revision 65 — `verify_r65.py`, 0 failures, every figure counted

**The base has moved twelve times under this cut. Store revision 65** (document revision `bc0576f5`,
whole document **346,114** characters; **enacted §1 121,576**) added 137 characters to subdivision D 1 —
[MOO-191](/MOO/issues/MOO-191)'s designation-review advisory. **Every count below is over enacted §1.**

**Anchors — thirteen strings, three bases, every one exactly 1.** Store revision 65; store revision 65
with the MOO-141 patch at **revision 5**; and with it at **revision 6**. The six edits, candidates
164-7, 164-8, 164-10, 164-11, both card (c) candidates, and card (i)'s insertion point. **The seventh
base move at which no anchor has shifted, and the third consecutive one at which the cut is
order-independent of the MOO-141 patch and indifferent to the 30/120 answer.**

**Delta of the six edits: +642 on all three bases** (it was +490 before the two re-cuts). Per edit:

| Edit | FIND | READ | Delta | Words added |
|---|---|---|---|---|
| 164-1 | 245 | 478 | **+233** | 46 |
| 164-2 | 112 | 478 | **+366** | 59 |
| 164-3 | 126 | 150 | +24 | 11 for 7 |
| 164-4 | 59 | 60 | +1 | 4 for 3 |
| 164-5 | 87 | 95 | +8 | 3 for 1 |
| 164-6 | 141 | 151 | +10 | 4 for 3 |
| | | | **+642** | |

**The verb, counted and not predicted — F2's row, done properly.**

| Phrase | §1 at store rev 65 | + this cut | + MOO-141 patch rev 6 | + both |
|---|---|---|---|---|
| `acts upon` | 8 | **9** | 8 | **9** — *not the 7 §7.2 predicted* |
| `act upon` | 9 | 9 | 12 | **12** |
| `acting upon` | 2 | 3 | 2 | **3** |
| `action upon` | 2 | 2 | 2 | **2** |
| **all four forms** | **21** | 23 | 24 | **26** |

**21 at base confirms §13.3's classification unchanged at store revision 65.**

**The formula, after the cut:** `the period allowed by this section for acting upon` **3** — two
*"… the request"* (Edits 164-3 and 164-6) and one *"… it"* (Edit 164-4, whose antecedent is a request).
`the period allowed to it for acting upon the request` **0**. `the period this definition allows`
**0**. **One concept, one formula, three sites — and §3.6's claim of "three times" is true of the
formula's stem, which is what §15.8 now says rather than leaving it to be mis-read as three identical
strings.**

**Figures the document quotes, re-counted:** `no later than` **74** (F15), `shall act upon` **5**,
`the 90 days allowed by this subsection` **2** (F12, realised in enacted text), `the period allowed`
**7**, `the time allowed` **2** (F13/F24), `is pending` **7** / `was pending` **1**, typographic
apostrophes **4** and all four still inside G 4 (§8).

**`verify_r65.py` asserts every figure above and exits non-zero if any moves.** 0 failures today.

### 15.9 Questions for the Policy Director — eleven

| | Question | My recommendation | What turns on it |
|---|---|---|---|
| **1** | **Card (c)** — (c-1) or (c-2), and the item-46 question | **(c-2) as redrafted at §4.2.** Counsel's F9 adds a second, independent reason | unchanged, still yours, still the one that goes to the board |
| **2** | **§7 item 130's residual — route (a), (b) or (c)** | **route (c): adopt candidate 164-7 as revised at §13.7.** Counsel concurs, *"with F19's clause"*, which is in | all three limbs; limb 3 is a duty that never falls due without it |
| **3** | **Candidate 164-8** — D 1's missing filing vehicle | **take it**, knowing from F26 that it reaches a class D 1's extension never decided | the member with a permission and no vehicle |
| **4** | Convert D 1's **ordinal reference** on the next pass that touches D 1 | **yes, but not in this cut** | correct today, fragile tomorrow. §13.9 as widened by F25 |
| **5** | The member who **never files the expiry notice** | **card it to [MOO-190](/MOO/issues/MOO-190) with item 130** | the priced limb, in the elective gap |
| **6** | **[MOO-97](/MOO/issues/MOO-97)'s route (b): decline, or keep as (b) + (c)?** | **decline** | §14.3, §14.5 |
| **7** | **NEW — F1. Candidate 164-9: close the remaining 60 days at M 2's tolling endpoint, or keep the 48-day cap?** | **keep the cap in this cut.** It is the full 78 days and it re-opens MOO-140's C2 and two live figures — a priced decision, not a repair | whether endpoint #15 is closed or disclosed. §15.4 |
| **8** | **NEW — F5. Bound clause (ii)'s exclusion of the Board's lateness, or take the board's already-approved m8-a?** | **take m8-a** on [MOO-97](/MOO/issues/MOO-97) rather than draft a second instrument here | whether the zero-allowance window has any bound at all. §2.3 |
| **9** | **NEW — F22. Candidate 164-7-B: extend the deeming to the definition-request class?** | **no recommendation.** It is the same trade as route (c) and it runs against the member in the class that asked to retire **later** | the only limb no route on the table reaches. §14.4 |
| **10** | **NEW — F6. Candidate 164-10: give M 2's 90-day duty a commencement?** | **take it.** Five words, no figure moves, and the member's route into court now depends on it | §15.4 |
| **11** | **NEW — F12. Candidate 164-11: conform the enacted expiry-notice sentence's formula?** | **take it, and route it to [MOO-42](/MOO/issues/MOO-42)** | one concept, one formula, inside M 2. §15.4 |

*(Questions 1 to 6 are the six from revision 4, unchanged in substance; 7 to 11 are new and all five come out of the counsel pass.)*

### 15.10 What revision 5 does not do

- **Nothing is applied to the store.** Not the six edits, not the apostrophe normalisation, not one of
  the five candidates.
- **No recommendation is reversed.** Decision 1 is still (f-4); Decision 2 is still *from the act,
  except where a person must act, then from notice*; card (i) is still closed with the confirming
  sentence recommended against; (c-2) is still preferred to (c-1); route (c) is still recommended.
- **No finding is rejected**, and where I decline counsel's **fix direction** — F1, F6, F11 — the
  reason is at §15.3 and the words are drafted so the Director can overrule me in one line.
- **I have not priced anything.** F1's 60 days, F5's unbounded term, F19's reset and F22's class are
  stated in days and direction only. **Deferred settlement is the Fiscal & Impact Modeler's**, and
  question 7 in particular should not be answered without them.
- **I have not re-read § 51.1-153 at source on this pass** — §13.5's reading of it stands from
  revision 3, read that day.
- **I have not read [MOO-190](/MOO/issues/MOO-190), [MOO-186](/MOO/issues/MOO-186) or
  [MOO-195](/MOO/issues/MOO-195)**, and F6 touches item 131's territory; counsel's note that F6 should
  be read alongside MOO-190 is passed on rather than acted on.

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by counsel
in the sense of legal clearance — [MOO-187](/MOO/issues/MOO-187) is an internal adversarial pass by a
colleague and is expressly not legal advice — and nothing here states or implies that Division of
Legislative Services has seen it. Pre-decisional and internal.**

---

## 16. Revision 6 — the Policy Director's disposition, folded in

**[`moo164-policy-director-disposition`](/MOO/issues/MOO-164#document-moo164-policy-director-disposition)
answered all eleven questions at §15.9 and sent none back.** Nine of the eleven recommendations were
taken as written; one was answered the other way; one was discharged by the base. **This section does the
six things the disposition's §14 asked for and nothing else. No decision in §0 to §15 is reopened, and
nothing is applied to the store.**

### 16.1 The eleven answers, and what each one did to the text

| | Question | Disposition | What revision 6 did |
|---|---|---|---|
| 1 | Card (c) — (c-1) or (c-2) | **(c-2)**, and **no item-46 card to the board** | **(c-2) applied as Edit 164-12**, §3.11. §4 kept as the record; (c-1) marked retired at §4.1 |
| 2 | Item 130's residual — route (a), (b) or (c) | **Route (c)** | **164-7 applied**, §3.7, carrying F19's limb (B) |
| 3 | Candidate 164-8 | **Take it** | **Applied as Edit 164-8**, §3.8 |
| 4 | D 1's ordinal reference | **Convert on the next pass that opens D 1 — not here** | Not converted. **Routed to [MOO-42](/MOO/issues/MOO-42)'s §7 at §16.5**, together with 164-7's two *"preceding sentence"* references, which are the same class of trap |
| 5 | The member who never files the expiry notice | **Carded — and to MOO-42's §7, because MOO-190 is `done`** | **Routed at §16.5.** Not drafted |
| 6 | MOO-97's route (b) | **Declined.** Not (b) + (c) | Nothing to do here. The Director posted it on [MOO-97](/MOO/issues/MOO-97) |
| 7 | Candidate 164-9 | **Keep the cap. The 60 days becomes [MOO-204](/MOO/issues/MOO-204)** | **164-9 stays held**, cross-referenced at §16.4. The edit number is reserved and not reused |
| 8 | F5's bound | **Discharged by the base — m8-a is enacted** | **§2.3 restated: 300 days, unconditionally.** Three places, §16.3 |
| 9 | Candidate 164-7-B | **Take it** | **Folded into Edit 164-7** as its deeming sentence, §3.7 |
| 10 | Candidate 164-10 | **Take it** | **Applied as Edit 164-10**, §3.9 |
| 11 | Candidate 164-11 | **Take it. MOO-42 is told, not asked** | **Applied as Edit 164-11**, §3.10, and MOO-42 is told at §16.5 |

**Two of the eleven are worth one line each, because they went against what I recommended or stated.**

- **Question 9 — I gave no recommendation and the Director decided it.** Their reason is the one I had
  not put in those words: *the tolled thing is her **final qualifying retirement date**, the outer date
  by which she must retire to qualify, so tolled without end it is not **later**, it is
  **indeterminate** — and she cannot plan a retirement against a date that never fixes.* **That reading
  is right and it resolves the trade I left open**, because 164-7-B's second trigger invents no bound: it
  fixes the deemed act *"on the day after the expiration of that period"*, **the identical date Edit
  164-4 already keys R-5's floor to**. Two provisions about one date now agree, which is the character of
  the whole cut.
- **Question 8 — I recommended waiting for m8-a and the Director counted it instead.** m8-a is not
  approved-and-pending; it is **enacted** in clause (ii) at store revision 68. **My withdrawal of the
  210-day bound at revision 5 was right; my statement of what replaced it was conditional and the
  condition is already satisfied.** §16.3.

**On question 1, so the omission is not read as an oversight.** No board card is created for item 46.
(c-2) confirms item 46 exactly as enacted and costs nobody anything against today's reading; the card
would have read *"do you still want the thing you decided?"* **What the board must be told, in the
designation-review read-through, is the deliberate divergence — subsection G will define *"pending"*
twice, differently, in adjacent subdivisions, on purpose.** §3.11 states it in those terms so whoever
writes that read-through can lift it.

### 16.2 The 48-day cap's derivation, re-cut — the figure is right and the old sentence was wrong

**Re-cut in place at §2.2.** Revisions 1 to 5 derived the cap as `48 = 15 + 3 + 30` and called the 3
*"subsection A's mailing"* extension as though it were unconditional. **Store revision 68 confined the
three days to mailing and added an express giving rule with a 5:00 p.m. electronic cut-off**, so the
derivation is now case by case — and **mailing is still the worst case, and 48 is still the outer bound.**
The table at §2.2 works all three routes: mailing on the fifteenth day reaches **day 48**; electronic
transmission before 5:00 p.m. reaches **day 45**; electronic transmission after 5:00 p.m. reaches **day
46** and is already a breach of the 15-day duty. **Nothing reaches past 48.**

**Four facts behind that table are counted, not asserted** — the mailing confinement, the giving rule,
the 5:00 p.m. rule and the definition's 15-day notice backstop each resolve **exactly once** in enacted
§1 at store revision 68, in `verify_r68_v6.py`.

**The point the Director made and I am recording in the document rather than in a comment: the figure was
right and the sentence explaining it was wrong.** A derivation that no longer matches the base is a
defect even when its answer is still correct, because the next person re-derives it from the sentence.

### 16.3 Clause (ii)'s bound is 300 days, unconditionally — and Decision 2 gains a sixth site

**m8-a is enacted.** At store revision 68 clause (ii) closes *"provided that the aggregate of all periods
so excluded shall not exceed 90 days"* — **one occurrence in enacted §1, counted, and it survives Edit
164-3**, which is also counted. So the term counsel's **F5** showed to be unbounded is capped at 90, and
**`60 + 30 + 120 + 90 = 300 days`, with no condition attached.**

**Restated in three places, all in the member's favour:** §2.3's true-bound paragraph, §2.3's
three-numbered-points list, and §2.3's cost-of-being-wrong line. **Every form of the words *"300 if m8-a
lands, unbounded if not"* is gone from §0 to §14.** The revision-5 corrections table at §15.6 keeps the
conditional form as the record of what revision 5 said, which is what that table is for.

**Decision 2 now has six sites in the bill and three of them are somebody else's work.** The three
original sites are at §2.1. Store revision 62 added two — D 1's certification-failure clock, keyed to the
**certification given to the member**, and G 4's § 51.1-162 C waiver **floor**, keyed to notice, which is
structurally the same instrument as card (h)'s floor and Edit 164-2's exception limb. **Store revision 68
adds the sixth: the new giving rule is keyed to *certifications* as well as statements and notices**,
which is precisely the rule §2.1 argues the bill already applies. **§2.1's argument is stronger than I
made it, three times over, and each time somebody else's revision made it.**

### 16.4 Candidate 164-9 stays held — and the one thing the applier needs about it

**Question 7: keep Edit 164-1's 48-day cap as drafted; the remaining 60 days at M 2's tolling endpoint
becomes [MOO-204](/MOO/issues/MOO-204), priced by the Fiscal & Impact Modeler.** The disposition's reason
is one I accept against my own framing: **a 60-day residual at a tolling endpoint, correctly disclosed,
is how something gets forgotten.** My drafting call — that a counsel pass is not where a priced decision
gets taken — stands; the Director's addition is that disclosure is not a disposition.

**The candidate is unchanged and is at §15.4.** Two facts the applier needs, both counted:

1. **164-9 cannot be applied to the base.** It amends **Edit 164-1's own new text** — the final clause
   *"and in no case later than 48 days after the Board acts upon the request"* — which resolves **0**
   times in store revision 68 and **exactly once** in the applied text. `verify_r68_v6.py` asserts both.
   **So 164-9 is applied after Edit 164-1 or not at all.**
2. **The edit number 164-9 is reserved and is not reused.** There is no Edit 164-9 in the patch; the
   promoted candidates took 164-7, 164-8, 164-10, 164-11 and the new number 164-12. If MOO-204 comes
   back and the Director takes it, the edit arrives under the number this document, the counsel pass and
   MOO-204 already use for it.

**It uses the formula Edits 164-3, 164-4, 164-6 and 164-11 introduce, so it adds no concept** — which is
why it is five words and why holding it costs nothing in drafting terms. **What it costs in policy terms
is card (f)'s full 78 days, and that is MOO-204's question and not mine.**

### 16.5 What leaves this document — four routings, none of them a question

**1. To [MOO-42](/MOO/issues/MOO-42)'s §7 — two record items and one trap, per questions 4, 5 and 11.**

- **Question 5's item.** *The member who files a reconsideration request, never files the expiry notice,
  and has an application pending holds a D 4 / D 5 queue position with no end and gets no decision on her
  application — at third-party cost, in the one limb that is priced.* Edit 164-7's trigger one needs a
  **denial date**, and the enacted expiry notice is a **power** — *"may file"* — so where she never files
  it there is no date to deem. **The only instrument that reaches it is an automatic denial on the 91st
  day, which the board considered and declined when it took option (d). I will not draft round that
  choice.** It belongs with §7 item 130.
- **The case-decision asymmetry.** **After Edit 164-7 the definition-request class has a determinate
  date and still has no deemed denial — so still no case decision, and no route into court under M 2's
  own judicial-review sentence.** 164-7's second trigger fixes the **date**; store revision 63's
  denial-and-case-decision machinery is confined to *"a request for reconsideration"*. **That asymmetry
  is now narrower than it was and it is not closed**, and it is MOO-42's sentence, not mine.
- **Edit 164-11 is MOO-42's enacted sentence.** Question 11's disposition is *"take it, and MOO-42 is
  told, not asked."* The edit is at §3.10, +24 characters, no change of meaning.
- **The ordinal-reference trap, now two of them.** D 1 points at *"the second sentence of subdivision
  M 2"*, and Edit 164-7 contains **two** *"the preceding sentence"* references. **All three are safe as
  cut and all three are counted** — §16.6. **Any future insertion into M 2 before its second sentence
  strands D 1's reference; anything inserted between the enacted denial sentence and 164-7's first
  sentence, or between 164-7's two sentences, strands one of its references.** Question 4's disposition
  is to convert the ordinal on the next pass that opens D 1; this is the record for that pass.

**2. To [MOO-141](/MOO/issues/MOO-141) — its Edit 1 FIND string is dead.** Store revision 68 re-cast
subsection A's three-day sentence: it is confined to **mailing** and the triplet *"statement, notice, or
certification"* replaces *"that statement or notice."* **MOO-141 Edit 1's FIND resolves 0 times.** This
kit keeps the dead string and asserts it at **0** so the break stays visible, and carries a working
repair **solely** so the order-independence test can be run. **MOO-141 must re-cut its own Edit 1. I have
not cut it for them, and the repair in this kit is not an amendment of theirs.** Edits 2 and 3 still
resolve exactly once.

**3. To [MOO-204](/MOO/issues/MOO-204) — candidate 164-9**, §16.4.

**4. Nothing to [MOO-97](/MOO/issues/MOO-97).** Route (b) is declined and the Director posted the
decision there. **It is declined and not held, and not (b) + (c)** — which is the answer I recommended,
for the incidence reason at §14.5: G 4's aggregate caps the **Board's** clocks, so *"a failure of the
Board to act … shall not extend that aggregate"* makes the Board bear its delay, while M 2 clause (ii)'s
aggregate caps the **member's** tolling, so the identical words make the **member** bear it. **Route (b)
is a policy choice wearing the clothes of a conforming amendment and I would not sign it as one.**

### 16.6 Verification at store revision 68 — `verify_r68_v6.py`, 0 failures, every figure counted

**Base: whole document 449,196 characters; enacted §1 131,066. The base has moved thirteen times under
this cut.** The check is new, not an edit of the old one: `verify_r68.py` checks the **six**-edit cut and
is kept as the record of the Director's own run; `verify_r68_v6.py` is the **current** check and covers
eleven.

**The eleven edits, per-edit delta, counted by `apply164.py` on an applied copy:**

| Edit | §1 FIND | Whole-doc FIND | Delta |
|---|---|---|---|
| 164-1 | 1 | 1 | +233 |
| 164-2 | 1 | 1 | +366 |
| 164-3 | 1 | 1 | +24 |
| 164-4 | 1 | 1 | +1 |
| 164-5 | 1 | 1 | +8 |
| 164-6 | 1 | **2** | +10 |
| 164-7 | 1 | **2** | **+1,153** |
| 164-8 | 1 | 1 | +485 |
| 164-10 | 1 | **4** | +27 |
| 164-11 | 1 | **2** | +24 |
| 164-12 | 1 | 1 | +220 |
| **total** | **11 of 11** | — | **+2,551** |

**Five of the eleven resolve more than once whole-document, because the §0 revision narrative quotes
them.** `apply164.py` slices §1, substitutes, and then asserts that the head and the tail are
**byte-identical**; it aborts otherwise. This is F21, and 164-10's four whole-document occurrences are why
it is the finding most likely to cause actual damage.

**Order-independence, on three bases:**

| Base | Eleven FINDs | Delta |
|---|---|---|
| store revision 68 | all 1 | **+2,551** |
| + MOO-141 patch **revision 5** (Edit 3 at 30 days) | all 1 | **+2,551** |
| + MOO-141 patch **revision 6** (Edit 3 at 120 days) | all 1 | **+2,551** |

**Thirty-three counts, all 1; one delta, identical on all three. Still order-independent of the MOO-141
patch and still indifferent to the 30/120 answer** — which has now held across five base moves, and now
holds for eleven edits rather than six.

**The ordering invariants the five promotions create — all counted, none assumed:**

| Invariant | Result |
|---|---|
| Edit 164-5's FIND precedes Edit 164-8's, inside one sentence of D 1 | **true** |
| In the applied text, 164-7's deeming sentence immediately follows the enacted denial sentence | **true** |
| In the applied text, 164-7's saving sentence immediately follows its deeming sentence | **true** |
| Nothing sits between 164-7's two sentences | **true** |
| *"The preceding sentence"* occurrences inside 164-7's two sentences | **2** |
| M 2's first five sentences are in order 1 < 2 < 3 < 4 < 5 | **true** |
| D 1's ordinal reference *"the second sentence of subdivision M 2"* | **1 occurrence** |
| No applied edit inserts into M 2 before its second sentence | **true** |
| Item 131: M 2's completion sentence still present, once, **after** 164-7's two sentences | **true** |
| Edit 164-7 introduces no competing *"case decision"* | **0 occurrences** |
| Candidate 164-9's FIND, against the **applied** text / against the base | **1 / 0** |
| Candidate (c-1)'s FIND — G 4 must be untouched by Edit 164-12 | **1, unamended** |

**The verb census — counted, never predicted, which is F2's lesson:**

| | `acts upon` | `act upon` | `acting upon` | `action upon` | census |
|---|---|---|---|---|---|
| store revision 68 §1 | 8 | 9 | 2 | 2 | **21** |
| + this cut at revision 6 | 10 | 14 | 5 | 2 | **31** |
| + MOO-141 patch revision 6 | 8 | 12 | 2 | 2 | **24** |
| + both | 10 | 17 | 5 | 2 | **34** |

**The census goes from 21 to 31, and that is not a retreat from Decision 1.** Decision 1 is that the cut
does not **define** the verb and does not **move** any existing occurrence's meaning. **The ten new
occurrences, attributed:**

| Edit | New occurrences | What they are |
|---|---|---|
| **164-7** | **7** | 4 in the deeming sentence, 3 in the saving. They supply a **date** for events the section creates |
| 164-1 | 1 | the cap repeats the floor's own *"after the Board acts upon the request"* |
| 164-3 | 1 | the conformed formula's *"for acting upon the request"* |
| 164-11 | 1 | the same formula at the second site |
| 164-4, 164-5, 164-6, 164-8, 164-10, 164-12 | **0 each** | — |

**None of the 21 existing occurrences is amended and none changes meaning.** Edits 164-4 and 164-6
replace the words **around** an occurrence and leave the occurrence itself intact; 164-5 replaces
*"upon"* with *"by reason of"* in a descriptor and leaves D 1's *"action upon a request"* standing, which
is the whole point of card (k). **Counted, not reasoned: the attribution above is computed by substitution
and the totals reconcile to the census table exactly.**

**The formula, after Edits 164-3, 164-4, 164-6, 164-7 and 164-11:**

| | Count |
|---|---|
| *the period allowed by this section for acting upon* | **5** |
| of which *"… the request"* | 3 |
| of which *"… it"* | 2 |
| *the period allowed to it for acting upon the request* — the variant Edit 164-6 removes | **0** |
| *the period this definition allows* — the variant Edit 164-4 removes | **0** |
| *the 90 days allowed by this subsection* — **2 in the base**, removed by Edits 164-3 and 164-11 | **0** |

**One concept, one formula, five sites, and every variant at zero. Card (j)'s defect is now cured at both
of its sites**, which it was not at revision 5.

**Other counted figures:** `no later than` **74** in the base; `shall act upon` **5** in the base and
**5** in the applied text, so Edit 164-10 adds no duty and dates one that exists; m8-a's proviso **1**
before and **1** after Edit 164-3; clause (ii)'s 120-day aggregate **1**; typographic apostrophes **4**,
with **0** anywhere in §1 outside subdivision G 4 — the confinement is now counted and not merely
stated; straight apostrophes **201**.

**`repro68.py` re-spliced all eight §6 reproductions by content.** Store revisions 66, 67 and 68 grew
enacted §1 from 121,576 to **131,066** characters, and **every anchor still resolved exactly once
throughout.** That is the sixth stale splice behind sound anchors, and §6's banner now states the lesson
rather than the incident.

### 16.7 Every statement in §0 to §15 corrected in place at revision 6

**Fifteen. Listed so a reviewer can check them rather than take my word for it.**

| | Where | Said | Now says |
|---|---|---|---|
| 1 | **title block, §3, ⚠ banner** | *"six anchored edits"*, *"+490"*, *"eighteen counts"* | **eleven edits, +2,551, thirty-three counts** |
| 2 | **§0.2** | the mailing extension reaches *"that statement or notice"*, unconditionally | *"that statement, notice, or certification"*, and **confined to mailing** |
| 3 | **§2.2** | `48 = 15 + 3 + 30`, the 3 unconditional | the same **48**, derived route by route; mailing is the worst case. §16.2 |
| 4 | **§2.3**, three places | *"300 if m8-a lands, unbounded if not"* | **300 days, unconditionally.** m8-a is enacted. §16.3 |
| 5 | **§4, §4.1, §4.2** | *"neither is applied"*; (c-2) is a recommendation | **(c-2) is Edit 164-12**; (c-1) is **retired** |
| 6 | **§4.2** | (c-2) is *"twenty words"*, then *"twenty-eight"* | **38 words, +220 characters**, counted |
| 7 | **§15.4** | Edit 164-11 is **+23** | **+24** — 38 characters for 62, the same arithmetic as Edit 164-3 |
| 8 | **§13.7, §15.4** | candidate 164-7 is *"170 words, +898"* | **as applied with 164-7-B's trigger, 217 words, +1,153.** The earlier figure is superseded, not wrong |
| 9 | **§5** | the act amends **one** section | it amends **two** — § 51.1-162 was added |
| 10 | **§6**, six provisions | spliced at store revision 65 | **re-spliced at store revision 68** by `repro68.py` |
| 11 | **§6.5** | subdivision G 4 is **29,648** characters | **31,872** at store revision 68 |
| 12 | **§8** | **637** straight apostrophes, **641** after | **201** in §1 at store revision 68; and the **confinement** is now counted too |
| 13 | **§7** | the census is **19** | **21** in the base, **31** after this cut. The conclusion is unchanged at all three counts |
| 14 | **§10** | two open questions | **all eleven answered**, none sent back |
| 15 | **§12** | ready for the counsel pass that became MOO-187 | **superseded** — the current step is §16.8 |

**None of these changes a recommendation.** Items 3, 6, 7, 8, 11, 12 and 13 are figures; items 1, 2, 9
and 10 are the base moving under the document; items 4, 5, 14 and 15 are the disposition landing.

### 16.8 Status and next step

**Revision 6 is complete as the Policy Director specified it, and it has not been reviewed.** Five edits
in this patch have never been reviewed **as applied text** — counsel read them as **candidates** in
[MOO-187](/MOO/issues/MOO-187), one at a time, and what they could not read then is how the eleven sit
together: the formula now standing at **five** sites rather than three, Edit 164-5 and Edit 164-8 sharing
one sentence of D 1, Edit 164-7's two *"preceding sentence"* references in applied text, and the verb
census at **31**. **My own gate is that counsel reviews every draft before it goes to the Editor, so the
next step is a bounded pass and not application.**

1. **A counsel pass scoped to the five promotions and the eleven-edit interactions** — §3.7 to §3.11,
   §16.2 to §16.4, §16.6's ordering invariants, and the one case §3.7 states as uncured. **The six edits
   and the two decisions are unchanged from what MOO-187 cleared and are out of scope.**
2. **Then application**, in either order with the MOO-141 patch, with the apostrophe normalisation
   performed in the same store revision and recorded in §0 as a non-substantive normalisation —
   **after** the eleven substitutions, not before.
3. **Not in this cut:** candidate 164-9, held for [MOO-204](/MOO/issues/MOO-204); card (i)'s confirming
   sentence, declined; candidate (c-1), retired; **F11**, carried forward at §15.5 for the next pass that
   opens the definition.

**One housekeeping item is still outstanding and it needs a board action.** The stray document created in
error at 18:07 on 12 October is still on this issue, retitled **SUPERSEDED — created in error**.
`DELETE /api/issues/:issueId/documents/:key` is **board-only and returns 403 to an agent**, so deleting
it is a board action. **Harmless, and visible.**

### 16.9 What revision 6 does not do

- **Nothing is applied to the store.** Not the eleven edits, not the apostrophe normalisation.
- **No decision or recommendation is reversed.** Decision 1 is still **(f-4)** — do not define the verb,
  repair the endpoints. Decision 2 is still **from the act, except where the period is one within which a
  person must act, then from notice**. Card (i) stays closed with the confirming sentence declined. The
  §0.2 call — one pendency event, two endpoints — is not reopened, nor is MOO-140's C2 text, nor F-6's
  declined cap at [MOO-179](/MOO/issues/MOO-179).
- **I have priced nothing.** The eleven-edit delta is a character count, not a cost. **The 60 days at
  MOO-204, the deferred settlement route (c) bounds, and the retention figure are the Fiscal & Impact
  Modeler's**, and this revision adds no estimate of any of them.
- **I have not re-read store revisions 66 and 67 for substance.** The verifier proves that nothing in
  them moved an anchor, a count or a figure this document quotes. **It does not prove that nothing in
  them bears on the two decisions** — [MOO-200](/MOO/issues/MOO-200)'s pass over store revision 67 is the
  right place for that, and the Policy Director said the same thing about their own run.
- **I have not re-read § 51.1-153 at source on this pass.** §13.5's reading of it stands from revision 3,
  read that day; it is the authority for candidate 164-8's premise that no filing vehicle exists, and
  Edit 164-8 is now applied text resting on it. **A reviewer who wants that premise re-checked should say
  so and I will re-read it.**
- **I have not converted D 1's ordinal reference.** Question 4's disposition is that it waits for the
  next pass that opens D 1, and this cut does open D 1 — at Edits 164-5 and 164-8. **I am following the
  disposition rather than my own view that it could have gone in here**, and §16.5 records it so the next
  pass has it.

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared
by counsel — [MOO-187](/MOO/issues/MOO-187) is an internal adversarial pass by a colleague and is
expressly not legal advice, and the five edits promoted at revision 6 have not been reviewed as applied
text at all. Nothing here states or implies that counsel or Division of Legislative Services has cleared
it, and no part of it is legally sufficient for introduction. Pre-decisional and internal.**
