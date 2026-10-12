# Memo risk section — carry-through register, revision 5 of the MOO-141 patch (MOO-172)

**Editor · 12 October 2026 · INTERNAL WORKING DRAFT — pre-decisional. Contains bill text; do not
circulate outside the Lab.**

This is the editorial carry-through record for the **four** things revision 5 of the MOO-141 patch
requires in the memo's risk section, the **one argument that is withdrawn**, the **one phrase that is
now banned**, and the **three-sentence plain-language statement of what the patch does**, which is
released.

It **continues** the MOO-90 register (C1–C3), the [MOO-111](/MOO/issues/MOO-111) register (C4–C6), the
[MOO-133](/MOO/issues/MOO-133) register (C7–C12) and the [MOO-160](/MOO/issues/MOO-160) register
(C13–C18), as amended by [MOO-165](/MOO/issues/MOO-165) (C19 added, C8 retired). Every earlier entry is
still live except where §5 below says in terms that something moved it. New entries are numbered
**C20 to C23**.

It is an **input register**, not an artifact. Nothing here is a new finding, and every entry keeps the
citation the originating agent gave it.

**Sources.** The Policy Director's disposition of revision 5
([`moo162-policy-director-disposition`](/MOO/issues/MOO-162#document-moo162-policy-director-disposition)),
which is where the instruction that **all four items must appear** comes from; the Drafting
Specialist's revision 5 ([`moo162-edits-2-and-3`](/MOO/issues/MOO-162#document-moo162-edits-2-and-3),
document revision `38d9caf0`, cut against `bill-text-s8` **store revision 60**); pass 18 on the patch
([MOO-166](/MOO/issues/MOO-166)), as reported through that revision and that disposition; and the
released price at [MOO-163](/MOO/issues/MOO-163), which is the whole of entry C23's condition.

**All four entries describe a patch that is applied nowhere.** Three gates stand between revision 5 and
application (§7), and the memo must not describe the patch as enacted. **The 30-day figure in Edit 3 is
also itself an open question in front of the board** — gate 4 on [MOO-141](/MOO/issues/MOO-141) — so
C22's number can change.

---

## 1. What I verified, and what I did not

### Verified — the operative strings every entry quotes

I read revision 5 in full and checked every string these four entries put in quotation marks against
its §1 (the anchored edits) and §3 (the provisions reproduced in full as amended). **The quoted text in
C20 to C23 is the drafter's, at revision 5, word for word.**

| Claim | Provision, as revision 5 has it | Verified |
| --- | --- | --- |
| The patch is three edits, +697 characters | §1: Edit 1 **+669**, Edit 2 **+14**, Edit 3 **+14** | Yes — the three parts sum to the stated total |
| Edit 1's operative clause deems one date | *"the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it"* | Yes — §1.1 READ string and §3.1 |
| Edit 1's saving sentence disclaims the Board's own due dates | *"Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section."* | Yes — and *"or an application"* is **deleted** from it, which is F-1 |
| Edit 2 re-keys the backstop notice | FIND *"no later than 15 days after it acts upon the request"* → READ *"no later than 15 days after it gives its decision upon the request"* | Yes — §1.2, and §3.2 shows it in the definition's penultimate sentence |
| Edit 2's condition precedent is untouched | *"Where the Board's action upon a request determines a member's final qualifying retirement date under this definition, the Board shall state that date in its decision upon the request, and where the Board does not do so …"* | Yes — nothing else in the sentence moves |
| Edit 3 extends the D 4 / D 5 retention | FIND *"retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"* → READ *"… until **30 days after** the Board acts upon the request"* | Yes — §1.3, and §3.3 shows it in M 2 |
| The retention and the application duty are **one sentence** | M 2: *"An application that is the subject of a request for reconsideration under this subsection retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request, **and the Board shall act upon the application no later than 15 days after it acts upon the request.**"* | Yes — this is what makes C22's self-defeat point exact |
| The tolling sentence carries two limits and the retention sentence carries neither | M 2: *"… tolls the running of the member's final qualifying retirement date … until 30 days after the Board acts upon the request, **except that** (i) no second or subsequent request … tolls any period …, and (ii) the aggregate of all tolling under this subsection shall not exceed 120 days …"* — both limbs hang off *"except that"* on the **tolling** sentence and speak only of *"tolling"* | Yes — this is the whole of C23's uncapped-and-chainable limb |
| D 1's extension runs on days of lateness and can escape the ceiling | D 1: *"the member's final qualifying retirement date is extended by the number of days by which the statement or notice is late"*; definition: *"except that this sentence does not apply to an extension under subdivision D 1 by reason of a statement or notice given later than the time required by this definition, and the aggregate of all extensions so excluded shall not exceed 12 months"* | Yes — §3.5 and §3.2. **This is the mechanism C20 is about, and the 12-month figure is the text's own** |
| The decision-keyed floor runs off a notice *required by* the preceding sentence | definition, final sentence: *"Where the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which the Board gives a decision or notice **required by the preceding sentence**, the member's final qualifying retirement date is … that first day."* | Yes — and this is why C21's switch-off works the way it does |
| M 2's reconsideration deadline is 90 days, and it is a duty to **act** | M 2: *"The Board shall act upon a request for reconsideration within 90 days."* | Yes — there is no duty to *give a decision* in it |
| D 3's parallel duty is keyed to the confirmation, not to the Board's acting on a request | D 3: *"the Board shall act upon the application no later than 15 days after the confirmation is obtained"* | Yes — §3.6 and §5.4. This is why day 22 is **one** site and not two |
| D 2's cumulative limitation is **$3,000,000** | relied on, unchanged across the register | Yes — carried from C13's verification at store revision 57 |

### Verified — the arithmetic each entry states, on the facts the drafting assumes

The ordinary facts are the drafter's and pass 18's, not mine: **first act F = day 7, decision D = day
85.** On those facts every figure in C20 to C22 reproduces:

| Figure | Reproduces as | Where it is used |
| --- | --- | --- |
| **day 22** | F + 15 = 7 + 15 | C20 (the foreclosed start date), C21, C22 |
| **day 100** | D + 15 = 85 + 15 | C20 (Edit 2's new start date) |
| **78 days** | D − F = 85 − 7 | C22 (what Edit 1 takes) |
| **day 37** | F + 30 = 7 + 30 | C22 (where the retention now ends) |
| **net −48** | 78 − 30 | C22, and sentence 3 of the plain-language summary |
| **48 days before** | 85 − 37 | C22 (priority gone before the reconsideration is decided) |
| **15 days** | the retention's live endpoint against the application duty at that endpoint + 15 | C22 (the self-defeat gap Edit 3 cures) |
| **63 days** | 100 − 37, on the undeleted reading | C22's precision 2 — **counterfactual only** |
| **day 106** | the 91st-day deemed denial + 15 | C21 (what item 124 buys), Drafting Specialist's figure |
| **day 105** | 90-day decision limb + 15 | C21 (what pass 18's card C buys), Drafting Specialist's figure |

**I did not derive any of these and I am not their author.** Each is the drafter's or pass 18's, stated
in revision 5 §5.1 to §5.4 and §6.4 and in the disposition §5. I checked that they are internally
consistent and that no two of them contradict.

### Verified — no figure conflict among the four entries

Every repeated number across revision 5, the disposition, the released price and the plain-language
summary matches: **$3,000,000**, **30 days**, **15 days**, **90 days**, **120 days**, the **12-month**
D 1 ceiling and its **further 12 months**, **78**, **30**, **48**, **+697 characters**, **67.4%**,
**112.3%**, **$204,000**, **48 months**, **$0**. One number is held — see §2 — and it is not in any of
the four entries.

### Not verified here

- **The live bill text.** Revision 5 was cut against **store revision 60** and I read the patch
  document, not the store. Every quotation above is cited to revision 5, which is the correct authority
  for a patch that is applied nowhere. **If the base has moved again, the drafter's gate 3 is what
  catches it, not this register.**
- **MOO-163's model.** I did not run or replicate it. C23 carries its figures as released, with its own
  conditions attached, and §2 holds the one place its basis collides with the package's published
  figure.
- **Pass 18's findings in their own words.** I have them through revision 5 and the disposition, both of
  which quote and dispose of them. **Where either reports a finding I have cited that report, not the
  pass**, and C21's and C23's substance is pass 18's on the drafter's and the Director's account of it.
- **The three gates.** [MOO-42](/MOO/issues/MOO-42) §7 item 124, [MOO-164](/MOO/issues/MOO-164)'s cut
  and the re-verification at application are all open on other issues. I checked none of them.
- **Whether the board keeps 30 days.** Gate 4 on [MOO-141](/MOO/issues/MOO-141) is live. **C22 is
  written against 30 days because 30 days is the decided number today.**

---

## 2. One thing held, not resolved, and routed to the Policy Director

**None of the four entries is held. All four are written and ready.** What is held is a
number-consistency question that C23 walks into, and it is held because reconciling it is not mine.

### 2.1 Central cap utilisation appears in the package as **78.1872%** and in C23's source as **67.4%**

C23's condition — the whole of it — is that D 2's cap does not bind at the central estimate, and
[MOO-163](/MOO/issues/MOO-163) puts that at **67.4%** utilisation. The package's authorised central cap
utilisation, recorded in the [MOO-160](/MOO/issues/MOO-160) register §2.1 and reproducible from the
authorised participation figure (18.3965 × $106,253 × 1.20 ÷ $3,000,000 = **78.19%**), is a different
number for the same quantity: utilisation of the same $3,000,000 cumulative limitation at the same
central estimate.

**It is not a contradiction, and I am not calling it one.** MOO-163 states the relationship on its own
record: it carries MOO-71's **corrected** mean certified subsidy of **$94k** rather than the stated
$110,042, because the corrected mean is the authorised ladder, and it says in terms that the 14.6% gap
*"is the correction working, not a conflict."* It also says the conclusion is unchanged on the stated
figure — **79.3% still does not bind.**

**But two different percentages for one quantity cannot both appear in three artifacts, and choosing
between them is a basis decision, not an edit.** So it is held and routed.

**Standing rule until the Policy Director answers.** C23's sentence uses **67.4%** and attributes it —
*"MOO-163's corrected central-estimate utilisation"* — and **no artifact states a bare central cap
utilisation figure without naming which ladder it sits on.** The substance C23 needs survives either
way, because the cap does not bind on either figure, and C23 is written so that the percentage is
evidence for the non-binding claim rather than a headline number of its own.

**No other conflict found**, in revision 5, the disposition, the released price or the summary.

---

## 3. The four entries

**All four are "must appear" on the Policy Director's instruction** (disposition §5), not the Red
Team's. Only the Policy Director can change that.

### C20 — Edit 2 forecloses the up-to-12-month D 1 extension. **A trade, not a clarification** — the patch is applied nowhere

Memo §8 (Risks and objections). **Must appear.** It is **the one item in the patch that trades against
the member**, and it goes in as a trade in its own first clause.

Memo-ready text:

> **The patch takes something from the member, and it is the only place in the patch that does.** The
> bill gives a member a backstop: where the Board's action on her request sets her final qualifying
> retirement date and the Board does not state that date in its decision, it must give her written
> notice of the date — and subdivision D 1 then extends her retirement deadline *"by the number of days
> by which the statement or notice is late."* That extension is one of the few that escapes the bill's
> own 12-month ceiling, up to a further 12 months.
>
> **The question was when the notice falls due, and the answer the patch gives costs the member the
> extension.** Before the patch, one available reading put the notice at 15 days after the Board's first
> action on the request — **day 22** on the facts the drafting assumes. Edit 2 re-keys it to 15 days
> after the Board *"gives its decision upon the request"* — **day 100** on the same facts. The member
> who would have been owed notice on day 22 and received it on day 100 had, on the earlier reading, an
> extension of up to 12 months. **After Edit 2 she has none, because the notice is not late.**
>
> **That is the trade the Lab recommends making, and the reason is that the earlier reading was not
> stable.** The condition the backstop hangs on — that the Board did *not* state the date in its
> decision — is a bare negative with no time index, so on the first-action reading its truth value can
> flip after the due date has passed: the Board fails to notify by day 22, states the date in its
> decision on day 85, and whether a duty ever arose, or whether a breach was cured after the fact,
> is genuinely unclear. Edit 2 moves the due date past the last moment at which the condition can
> change state. **The member gets a notice date that cannot shift behind her; she gives up an extension
> of up to 12 months.**

Citation to carry: § 51.1-142.4, the definition of *"final qualifying retirement date"* in subsection A
(penultimate sentence, and the ceiling sentence with its *"further 12 months"* carve-out) and
subdivision D 1's extension sentence, as reproduced in
[`moo162-edits-2-and-3`](/MOO/issues/MOO-162#document-moo162-edits-2-and-3) revision 5 §3.2 and §3.5;
the trade, the day-22 and day-100 figures and the temporally-unanchored ground, Drafting Specialist
revision 5 §5.1 on pass 18's **F-3**; the Policy Director's withdrawal of the contrary argument,
disposition §4. **The ordinary facts (F = 7, D = 85) travel with the two day figures in every
artifact.**

Response column, where the memo gives one: the defect Edit 2 cures is real and the cure is the right
one; the cost is a remedy the member loses, it is disclosed, and it is not netted against anything.

**Three precisions, because this is the entry most likely to be softened in editing.**

1. **The word *"clarification"* may not be used of Edit 2, in any artifact.** See §4. The argument that
   made Edit 2 look near-costless is withdrawn by its own author.
2. **Do not write that the first-action reading was wrong or absurd.** The drafter's own statement is
   that it *"was available, it was not absurd, and it produced a member-favourable rule."* An artifact
   that dismisses it has deleted the cost.
3. **The vocabulary point is worth a clause and is not a cost argument.** No syllable of Edit 2 is new
   to the definition: the next sentence already says *"gives a decision or notice"* and the amended
   sentence already says *"its decision upon the request."* It answers *"is this a new event?"* — not
   *"what does it cost?"* Revision 4 let the two run together and that is what F-3 killed. Keep them in
   separate sentences.

---

### C21 — Edit 2 keys the member's only deadline to an event the section never commands, and switches off the floor that was supposed to protect her. **Conditional: real unless MOO-42 §7 item 124 is enacted**

Memo §8. **Must appear**, and it **corrects** what the Lab said at revision 4 about where the member's
protection against a slow Board comes from.

Memo-ready text:

> **Edit 2's new deadline starts when the Board gives a decision — and nothing in the section requires
> the Board ever to give one.** *"Decision"* is not defined. Every Board duty in the section is a duty
> to **act**, to **make a determination**, to **certify**, or to **give a notice**; the reconsideration
> provision says only that *"[t]he Board shall act upon a request for reconsideration within 90
> days."* The patch's own saving sentence lists *"a determination"* and *"a notice or a decision"* as
> separate things, which is a reason to read them as separate. **So the member's only deadline under
> this backstop starts on an event the section never commands, controlled by the actor whose lateness
> the backstop exists to police.**
>
> **It also switches off the fallback.** The definition's floor — which pulls the member's retirement
> deadline forward to the first day of the second month after the Board gives its decision or notice —
> operates only on a decision or notice *"required by the preceding sentence."* If no decision is given
> and the notice is never *required*, because its 15 days never start, **neither limb triggers.** At
> revision 4 the Lab told the board the member's protection here was the decision-keyed floor, *"which
> Edit 1 cannot move."* Edit 1 cannot. **Edit 2 can switch it off, and that correction is on this
> record because the Lab made it against itself.**
>
> **The member in that case has little else.** A reconsideration the Board never completes produces no
> case decision — the bill makes the final determination a case decision only *"[u]pon completion of a
> reconsideration"*, disapplies the hearing articles, and disapplies the Administrative Process Act's
> deemed-decision sentences in terms — so there is no deemed decision and no judicial review either.
>
> **There is a cure, it is already drafted for an unrelated reason, and the Lab will not apply this
> patch without it.** A deemed denial on the 91st day gives Edit 2's 15 days a guaranteed start —
> **day 106** at the latest — and the floor a guaranteed trigger, without adding a duty to the 90-day
> sentence, and it can never pull the notice forward of an actual decision, because it arises only
> where the Board has not completed the reconsideration. **If it is enacted, this risk closes. It is
> not enacted.**

Citation to carry: § 51.1-142.4 M 2 (the 90-day sentence, the case-decision sentence and the Articles 3
and 4 disapplication), M 3, and the definition's final sentence, as reproduced at revision 5 §3.2 and
§3.3; the undefined-*"decision"* sweep of every Board duty in §1 and the *Forst* presumption, pass 18's
**F-2 / F-4**, through revision 5 §6.4; the correction against revision 4, Drafting Specialist, same
section; the no-judicial-review consequence of store revision 59, same section; the cure, **[MOO-42]
(/MOO/issues/MOO-42) §7 item 124** (deemed denial on the 91st day, drafted and recommended) with pass
18's card C as the fallback, and the day-106 and day-105 figures, Drafting Specialist revision 5 §6.4
and §9 card 1; **the gate**, Policy Director, disposition §3.1 and §6.

Response column: the cure is small, already drafted, recommended on independent grounds, and the Lab
has made it a condition of applying the patch rather than a recommendation.

**Four precisions.**

1. **Write it conditionally and state the condition in the same sentence as the risk.** The honest form
   is *"real unless the deemed-denial cure is enacted"*, and the cure is **not enacted** — it is a
   question on the Policy Director's card. **An artifact that states the risk flat is wrong, and one
   that states the cure as done is worse.**
2. **The two cure figures are different cures.** **Day 106** is item 124's deemed denial on the 91st
   day plus 15. **Day 105** is pass 18's card C — a decision limb in the 90-day sentence — plus 15.
   Card C is the fallback and fires only if item 124 is declined. Do not merge them or average them.
3. **Do not offer "the Board will obviously give a decision" as the response.** The drafter looked for
   a right-sized drafting fallback and reports there is none: any fallback keyed to the acting period
   fires in the ordinary case, and the one revision 4 proposed would have restored the very extension
   Edit 2 was adopted to foreclose. **The honest response is the cure, not an assurance about
   practice.**
4. **This is a correction, not a new finding, and the memo gains from saying so.** The register's
   earlier account of the member's protection was wrong and the Lab's own drafter said so. A risk
   section that shows its own correction reads as a review; one that quietly swaps the sentence does
   not.

---

### C22 — Edit 3 gives back 30 of the 78 days Edit 1 takes. **Net −48, and it cures a self-defeat gap without delivering the retention's purpose**

Memo §8. **Must appear.** It is the number in front of the board as the single open question on the
patch, and the memo states it as it stands today.

Memo-ready text:

> **The patch's member-favourable edit is smaller than it looks, and the Lab's own arithmetic says
> so.** When a member asks the Board to reconsider, her application keeps its filing date — its place
> in the subsidised queue — while the request is pending. The bill currently says it keeps that date
> *"until the Board acts upon the request"*, and does not say whether that means the Board's first
> action or its last. **Edit 1 fixes it at the first action. Edit 3 then adds 30 days.** On the facts
> the drafting assumes — first action on day 7, decision on day 85 — Edit 1 shortens the retention by
> **78 days** and Edit 3 gives back **30**: **net −48**. The retention ends on **day 37**, against a
> reconsideration decided on **day 85**, so the filing-date priority is gone **48 days before** the
> decision whose outcome it exists to preserve.
>
> **What Edit 3 does fix is real, and it is a provision that currently defeats itself.** The retention
> and the deadline for acting on the application are halves of one sentence: the application keeps its
> date until the Board acts on the request, and the Board may act on the *application* as late as 15
> days after that. **So on the live text the protection can expire up to 15 days before the duty it
> exists to protect falls due.** Edit 3's 30 days cover that window with 15 days to spare. That is a
> defect repaired.
>
> **It is not the same thing as delivering the protection.** The retention exists so that a member who
> wins her reconsideration still has her place in the queue. On these facts she does not. **Edit 3
> cures the self-defeat gap; it does not deliver the retention's purpose**, and the Lab has put the
> 30-day figure back in front of the decision-maker rather than defending it.

Citation to carry: § 51.1-142.4 M 2's retention-and-application sentence, quoted in full, as reproduced
at revision 5 §3.3; Edit 1's deeming clause at §3.1; the **78 / 30 / −48** arithmetic and the day-37
and day-85 facts, Drafting Specialist revision 5 §5.2 and §5.3 on pass 18's **card A, confirmed**; the
self-defeat gap and that Edit 3 strictly covers it, §5.3; the open question on the figure, Policy
Director, disposition §5 and **gate 4 on [MOO-141](/MOO/issues/MOO-141)**.

Response column: the 30 days was chosen before two facts were on the record, the Lab has asked the
decision-maker to look again, and a longer retention is priced at **$0** at the central estimate — see
C23 — so the response is an open question, not a defence.

**Four precisions.**

1. **The 78 days are a cost of Edit 1, not of Edit 3, and the patch is uniformly member-adverse on
   tolling.** An artifact that presents Edit 3 as a gift without Edit 1's subtraction has reversed the
   sign of the patch's effect here.
2. **The 63-day figure is a counterfactual and must never appear as the patch's effect.** Without
   Edit 1's three-word deletion the application duty fell on the open reading at day 100 against a
   retention ending day 37, and **Edit 3 would have enlarged the self-defeat gap from 15 days to 63.**
   That is the reason the deletion was kept. It describes a rejected alternative.
3. **The 30 days is the board's decided number and it is live.** Gate 4 can change it; the Policy
   Director's own recommendation on the record is **120 days keyed to the first act**. **No artifact
   may describe 30 days as settled**, and if the figure moves, this entry, sentence 3 of the
   plain-language summary, and every artifact that carries −48 all move with it.
4. **Say "one event with two endpoints", not "both clocks now restart on the same day."** See §4. After
   Edit 1 and Edit 3, G 4's pendency ends at the first act and M 2's tolling and retention run to first
   act + 30. The two clocks are keyed to one event and end on different days, and that is the decided
   design.

---

### C23 — The third-party limb: Edit 3's retention is uncapped and chainable, and the cost falls on other wait-listed applicants. **At the central estimate that cost is zero, and the condition is the whole of the item**

Memo §8. **Must appear**, and **it may not appear without its condition.** Unconditioned it is
misleading in the opposite direction from C20 to C22 — it would read as an unpriced third-party cost
when the released price says it is zero.

Memo-ready text:

> **One part of the patch can cost somebody other than the member who benefits, and the Lab priced
> it.** The filing-date retention Edit 3 extends operates in a priority queue for a capped pool: the
> bill lets the Board reserve no more than **$3,000,000** in total, and applications are funded in
> filing-date order with a waiting list behind them. A member who holds her filing date for an extra
> 30 days holds a place other applicants want. **And the extension carries no limit.** The two limits
> in the surrounding provision — that a second or subsequent request about the same determination does
> not count, and that the total may not exceed 120 days — are attached to the *tolling* sentence and
> speak only of tolling. **The retention sentence carries neither, so successive requests about
> successive waiting-list placements can chain.**
>
> **At the Lab's central estimate the cost of that is zero, and the reason is that there is no
> money-rationed queue to be at the front of.** On the authorised participation basis the
> $3,000,000 cap is not reached — **67.4%** of it is used, on the corrected central-estimate ladder —
> so every election the bill admits is funded whatever the order, and **queue position decides nothing
> for anyone.** The effect on the appropriation line is **$0 exactly**, as an identity, under all three
> readings the model priced. Order can matter only at high take-up, where utilisation reaches
> **112.3%** and the cap does bind; even there the whole effect is bounded by **under $204,000 over
> 48 months**, it is **lapse rather than cost**, and the displacement is **0.11 to 0.14 members on
> average** across the pilot. **And an applicant who loses priority keeps every standard-cost right the
> bill gives her** — she loses her place, not her purchase.
>
> **Two things would bring this back.** The price covered one retention endpoint, not an unbounded
> chain of them, and a bounded addendum on the chaining limb has been commissioned. And the whole
> count rests on the narrower of two readings of an eligibility clause that is still open; on the
> broader reading the programme reaches roughly **130** members, **the cap binds in every scenario**,
> and the queue becomes real. **On the record as it stands, this is a disclosed third-party exposure
> priced at zero, not an unpriced one.**

Citation to carry: § 51.1-142.4 M 2's tolling sentence with its clause (i) and clause (ii) limits and
its retention sentence, and D 2's $3,000,000 limitation, D 3's contingency and D 4 / D 5's order and
waiting list, as reproduced at revision 5 §3.3 and §3.6; the uncapped-and-chainable finding, pass 18's
**F-6**, through revision 5 §1.3 and §9 card 4; **every figure in the second paragraph**,
[MOO-163](/MOO/issues/MOO-163) as released 12 October 2026 — **67.4%** central and **112.3%** high
corrected cap utilisation, **$0** on the appropriation line under all three readings, the **$204,000 /
48-month** lapse bound, the **0.11–0.14** mean displacement, and D 5's preservation of the subsection B
standard-cost rights; the decision not to cap, and the two re-opening triggers, Policy Director,
disposition §3.4; the chaining addendum, disposition §3.5; the broad-reading trigger,
[MOO-49](/MOO/issues/MOO-49), flagged by MOO-163 itself.

Response column: the exposure is real in shape and zero in amount on the authorised basis; the Lab
declined to cap the retention because a cap would narrow a member protection to prevent a cost that is
nil at the central estimate, and it named the two events that would reverse that.

**Five precisions, and the first is the one that matters.**

1. **Never write this item without its condition in the same sentence.** *"Uncapped and chainable"* on
   its own is a serious-sounding unpriced liability. The required shape is **the mechanism, then the
   condition, then the bound** — and the condition is *at the central estimate, where the cap does not
   bind.*
2. **Two caveats travel with every figure here, into the one-pager too.** The figures are conditional
   on **the narrow reading of the eligibility clause**, open at [MOO-49](/MOO/issues/MOO-49), and the
   price covers **one endpoint, not an unbounded chain.** Neither may be dropped to shorten a line.
3. **Use 67.4% with its attribution, and see §2.** It is MOO-163's corrected central-estimate
   utilisation. The package's published figure for the same quantity is 78.1872%, the basis question is
   held, and no artifact may state a bare utilisation figure without naming the ladder.
4. **$204,000 is lapse, not cost, and it is a bound, not an estimate.** MOO-163's own words: seven of
   eight high-scenario cells are not distinguishable from zero, and a quantity whose sign flipped on a
   fresh draw is zero. **Do not convert the bound into a point estimate and do not call it a cost to
   the Commonwealth.**
5. **The displaced applicant is in the stakeholder map already; the pathway is not.**
   [MOO-125](/MOO/issues/MOO-125) maps the subdivision D 5 waiting-list applicant as a cost-bearer on
   the zero-credit election route. **Edit 3's retention is a second route onto the same party, not a new
   group**, so no artifact may present them as a stakeholder the Lab had missed.

---

## 4. Style rules — one argument withdrawn, one phrase banned

### Withdrawn, and it was the Policy Director's own: Edit 2 as a **clarification**

**Revision 4's condition-precedent argument for Edit 2 is withdrawn by its author.** It said Edit 2 was
a near-costless clarification because the backstop duty was already conditional on the decision on its
own face. **It does not hold:** *"where the Board does not do so"* is a bare negative, and a negative is
satisfied by the non-occurrence of the positive — at day 22, with no decision in existence, *"has the
Board stated that date in its decision?"* has the determinate answer **no**.

**The argument was the Policy Director's, from the disposition of revision 3, not the Drafting
Specialist's.** The record should say so.

**The rule, and it reaches every artifact, chart label and slide title.** Edit 2 may not be called a
**clarification**, and no paraphrase of that claim may be used either — *"tidies up"*, *"makes
explicit"*, *"confirms"*, *"near-costless"*, *"technical fix"* and *"no substantive change"* are the
same claim in other clothes. **If any draft of mine calls Edit 2 a clarification, that wording comes
out.** The required frame is **a trade**: C20's first clause.

**What survives, and it is worth a clause and not a paragraph:** the condition is **temporally
unanchored**, so its truth value can flip after the due date has passed; Edit 1's saving sentence
already disclaims that notice's due date, so Edit 2 resolves an ambiguity Edit 1 deliberately left; and
**the vocabulary point stands untouched** — no syllable of Edit 2 is new to the definition, the next
sentence already saying *"gives a decision or notice"* and the same sentence *"its decision upon the
request."* **The vocabulary point answers whether the event is new, never what the edit costs.**

Source: Policy Director, disposition §4, withdrawing their own argument; Drafting Specialist revision 5
§5.1 on pass 18's **F-3**.

### Banned from here on: *"Both clocks now restart on the same day"*

**It is false after Edit 1 and Edit 3.** G 4's pendency ends at the Board's **first act**; M 2's tolling
and the D 4 / D 5 retention run to **first act + 30**. The patch does not make the two clocks end
together — it makes them **one event with two endpoints**, and that is the decided design, not a
residual defect.

The replacement, verbatim:

> **The patch gives the two clocks one starting event with two endpoints: G 4's pendency ends when the
> Board first acts, and M 2's tolling and filing-date retention run to 30 days after that.**

Applies to all three artifacts and to any chart label or slide title. **Also banned:** *"the clocks are
aligned"*, *"the two clocks now match"* and *"the 30-day mismatch is closed"* — the last is the worst of
them, because the 30 days is now the deliberate interval, not the error.

Source: Policy Director on this issue.

### Still binding from earlier passes

- **Everything in the [MOO-160](/MOO/issues/MOO-160) register §4**, as amended by
  [MOO-165](/MOO/issues/MOO-165): the replacement fiscal sentence in both halves (*"No admission
  quantity moves; the settlement count moves upward by an amount the current engine cannot value"*),
  the fourth-time ban on *"the § 51.1-153 B normal-retirement cohort"* in favour of **the unreduced
  subdivision A 1 cohort, reached through § 51.1-153 A, B 2 or B 3**, the ban on saying § 51.1-156 H
  *permits* a waiver, no ordinal for the admission rule among the model's drivers, MOO-90's C3 hold,
  and the MOO-140 replacement form of the zero-allowance window rule with its *"where the Board meets
  each of its own deadlines"* requirement.
- **From MOO-165: no per-year participation rate.** The authorised form is *"about nineteen state
  employees **in all**"*, and a per-year rate is impossible on D 2's own cap.
- **From MOO-165: the $3,000,000 is never an appropriation.** *"A $3,000,000 cap on the Commonwealth's
  share"* is available. **This bears directly on C23**, whose second paragraph says *"$0 exactly on the
  appropriation line"* — that phrase is MOO-163's description of a **fiscal-note line**, and an artifact
  must not let it imply the bill appropriates anything.
- **No artifact uses 18.9059 participants.** The authorised figure is **18.3965**.
- **New on this pass, from §2 above:** no bare central cap utilisation figure without naming the ladder
  it sits on, until the Policy Director answers.
- **New on this pass, from C22:** **no artifact may describe 30 days as settled**, and none may state
  the −48 without the ordinary facts (first act day 7, decision day 85) on the same page.
- **New on this pass, from C21:** the risk is written **conditionally** on the deemed-denial cure, and
  the cure is **enacted nowhere**.
- **New on this pass, standing over all four:** **no artifact may describe this patch as enacted,
  applied or in the bill.** Three gates stand before application and the board's figure question is a
  fourth. The patch is a recommendation.

---

## 5. Carry-through — where the earlier entries stand after revision 5

**Recorded because an artifact that carries a cured entry is as wrong as one that drops a live one.**
Every status below is the originating agent's, not mine.

| Entry | State before revision 5 | State now | Authority |
| --- | --- | --- | --- |
| **C1, C3–C6** | live | **Live, untouched.** Revision 5 does not reach them | MOO-90, MOO-111 |
| **C2** | released in MOO-140 replacement form | **Live, unchanged** | Policy Director, MOO-140 |
| **C7** | cured, successor is C13 | **Unchanged** | pass 17 |
| **C8** | held | **Retired.** Replaced by C19 | Policy Director, MOO-165 |
| **C9** | cured, replaced by C16 | **Unchanged** | pass 17 |
| **C10** | cured in principle, defective in execution | **Unchanged** | pass 17 |
| **C11** | cured and verified | **Unchanged** | my own check at store revision 57 |
| **C12** | live | **Live and unchanged as a finding.** Edit 3's retention is a second route onto the D 5 waiting-list applicant, which is C23's limb, not a change to C12 | pass 12; MOO-163; disposition §7 |
| **C13–C18** | five open legal entries plus the fixed fiscal statement | **Live and unchanged.** None of the three edits reaches any of them | MOO-160 |
| **C19** | new, must-appear | **Live.** Carry its four bindings verbatim from MOO-165 §3.2 | Policy Director, MOO-165 |

**The risk-section inventory becomes:** C1, C2 (MOO-140 form), C4, C5, C6, C12, C13, C14, C15, C16,
C17, C18, C19 and **C20, C21, C22, C23**, with C3's open question in §9, §3.7's null results in the
opening or closing paragraph, and **C8 retired**.

**Two consequences for §8 as it now stands.** The four new entries are about **a patch, not the bill** —
they describe a proposed amendment to three provisions and must be grouped and labelled as such, or a
reader will take them for defects in enacted text alongside C13 to C19. And **C21 is the only entry in
the whole register whose risk is written conditionally on a cure**; every other open entry states its
cure as drafted and enacted nowhere. That asymmetry is deliberate: the Policy Director made the cure a
gate on applying the patch, so the patch and the cure travel together.

---

## 6. Logged for use — the three-sentence plain-language statement of what the patch does

**Released by the Drafting Specialist on this issue, the hold having been lifted by the Policy
Director's disposition §5.** Source:
[`moo162-edits-2-and-3`](/MOO/issues/MOO-162#document-moo162-edits-2-and-3) revision 5, document
revision `38d9caf0`. **To be used as given and not paraphrased**, subject to the four bindings below.

> Where this bill measures a deadline from the day the Board "acts upon" a member's request, it does not
> say whether that means the Board's first action on the request or its last; the patch answers that
> once — it means the first action — so the pendency clock in subdivision G 4 and the tolling clock in
> subdivision M 2 are counted from the same event instead of restarting on different days.
>
> The patch also requires the Board to notify a member of their final qualifying retirement date within
> 15 days after it **gives its decision** on the request, rather than within 15 days after it acts on
> the request, which gives the member a notice date that cannot shift after the fact but gives up an
> extension of up to 12 months that the earlier reading made available when the Board notifies late.
>
> And it lets an application keep its filing date for the subdivision D 4 and D 5 purposes for **30 days
> after** the Board acts on the request, instead of losing it the moment the Board acts — repairing a
> provision that today can expire up to 15 days before the duty it exists to protect falls due, though
> on the facts the drafting assumes the patch still leaves that protection 48 days shorter than it is
> now.

**Where it goes: memo §5 (Recommended approach), as the paragraph that introduces the patch**, and the
one-pager's *"what the proposal does"* bullets **only if the patch is in the recommendation at all.** It
is the fifth plain-language statement in the register and the five are **not** alternatives:

| Statement | Describes | Belongs in |
| --- | --- | --- |
| MOO-90's | **what the bill does**, in mechanism terms | memo §2 opening; one-pager bullets |
| MOO-111's | what the **pass-10 edits** did | memo §5 |
| MOO-133's | what the **pass-12 edits** did | memo §5 |
| MOO-160's, as answered by MOO-165 | **what the bill does**, in scale-and-promise terms. Supersedes MOO-90's for the opening | memo §2 opening; one-pager bullets |
| **this one** | **what the revision-5 patch does** — the three edits on the MOO-141 clock problem | memo §5, with the patch |

**Four bindings.**

1. **It is a summary of the patch, not of S8.** Three edits on one clock problem. **It may not be used
   as a summary of the bill, and it does not replace MOO-160's.** If the memo needs a three-sentence
   summary of S8 as a whole, that is a separate ask of the Drafting Specialist and they have offered to
   write it.
2. **Sentence 2's second half is the cost, and it does not come out.** The Drafting Specialist's
   instruction, on the record: if the sentence must be shortened, **cut the first clause, not the
   second.** The sentence is deliberately a trade, which is C20 and §4.
3. **Sentence 3's "48 days shorter" is the net and it is the number that matters** — 78 taken by Edit 1,
   30 given back by Edit 3, retention ending day 37 against a reconsideration decided day 85. It is
   C22, and the ordinary facts travel with it.
4. **Three things the summary deliberately does not say, so place them yourself and not by omission.**
   It does not mention a **cap** on the retention, because there is none in the patch — card F-6 is
   declined on MOO-163's released price, and it returns only on the chaining addendum or on
   [MOO-49](/MOO/issues/MOO-49) landing broad, at which point sentence 3 is re-cut. It does not mention
   **day 22** — the Board deciding the application before the reconsideration — because that is a
   consequence of the patch rather than something the patch does; it is a confirmed structural
   sequencing defect and **it belongs in the risk section.** And it does not describe the **no-decision
   cure**, because MOO-42 §7 item 124 is a **gate on applying the patch**, not part of it; if item 124
   is declined the fallback changes and the Drafting Specialist re-cuts these sentences.

**Day 22, placed.** It is not a fifth must-appear item and the Policy Director did not make it one. It
goes into the memo's risk section **inside C21**, as the sequencing consequence of the deletion that
makes Edit 3 work: on the ordinary facts the Board must act on the **application** by day 22 while the
**reconsideration** whose outcome the application's retained filing date exists to preserve is not
decided until day 85. **One site in the bill** — D 3's parallel duty is keyed to the confirmation and
does not move by a day — **and it is not cured by a longer retention.** Source: pass 18's **card B,
confirmed**, through the Policy Director's disposition §1, where it is accepted and disclosed; the
one-site finding, revision 5 §5.4.

---

## 7. What this register does not resolve

- **The patch is applied nowhere, and three gates stand before it is.** [MOO-164](/MOO/issues/MOO-164)'s
  cut must carry F-9; the no-decision residual must be cured ([MOO-42](/MOO/issues/MOO-42) §7 item 124,
  or pass 18's card C if item 124 is declined); and whoever applies it must re-verify against the base
  as it stands at that moment, not against store revision 60. **An answer to any gate rewrites part of
  this register**, and item 124's answer rewrites C21.
- **Gate 4 is the one that can change the text.** The board's question on Edit 3's figure is live on
  [MOO-162](/MOO/issues/MOO-162) and recorded as gate 4 on [MOO-141](/MOO/issues/MOO-141), with three
  costed options and the Policy Director's recommendation of **120 days keyed to the first act**. **If
  the figure moves, C22 moves, sentence 3 of the summary moves, and the 120-day option puts the
  declined cap back on the table as a paired item.**
- **One number is held and routed to the Policy Director** — which central cap utilisation figure the
  package states. See §2. **Until it is answered the standing rule in §4 binds every artifact.**
- **The chaining price does not exist yet.** MOO-163 priced one retention endpoint; the bounded
  addendum on Edit 3's uncapped, chainable limb is commissioned of the Fiscal & Impact Modeler and has
  not reported. **C23's figures cover the endpoint, not the chain**, and that caveat is one of the two
  that travel with them.
- **[MOO-49](/MOO/issues/MOO-49) is the dominant open driver and it is not mine.** Narrow gives the
  counts C23 uses; broad gives roughly 130 members, the cap binds in every scenario, and **C23 and
  MOO-163 both re-open.**
- **Three cards from this pass are not entries here.** F-9 (card 2), F-5 (card 3) and D 3's event
  mismatch (card 6) are drafting and research items on other issues and the Policy Director did not
  mark any of them must-appear. **If he wants one in §8, that is his instruction to give.**
- **Card (l) is closed and is not a risk entry.** The corrected figure is **129 against 128** —
  first-action is worse by one day, not better by seven, pass 17's F-6 having been an arithmetic slip —
  and the disposition's own frame is that this was a precision question, not a risk question. **It is
  recorded so that nobody promotes it into §8, and the correction stands unsoftened.**
- **I verified revision 5, not the store.** See §1. No claim here is a check of the live bill text.
- **Nothing here authorises drafting of the memo to begin**, and nothing here changes the fiscal
  statement, which is unchanged at **$0** and carried by [MOO-163](/MOO/issues/MOO-163). This register
  is what §8 is built from when the basis is released.

---

**Standing caveat.** Internal working draft. Pre-decisional. Contains bill text. **Not a Division of
Legislative Services bill; not reviewed by counsel or by DLS** — the passes cited are the Lab's own
adversarial reviews and are expressly not legal advice. Nothing in it is cleared for external use.
**Saving a file is not sending it.**
