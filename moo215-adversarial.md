# MOO-215 — Bounded adversarial pass on MOO-141 Edit 2 revision 8 and on the joint-landing cross-reference requirements

**Red Team / Counsel Reviewer. 13 October 2026. Internal risk analysis, not legal advice. No
counsel has reviewed or cleared any part of this proposal, and nothing here should be read as
saying otherwise. Internal working draft material. Not a DLS bill. Pre-decisional. Nothing applied
to the store.**

## 0. The base, stated as it stands on my own run

Every count below is taken at **store revision 71, document revision 90**: whole document
**484,408** characters, enacted §1 **134,012**, §1 sha256 `83a10b74950b5272…`. Body read from
`moo141-rev71/live.md` — the store's text, not a document's reproduction of it. The Policy
Director's `verify_r71.py` was re-run unmodified on my own invocation: **all checks pass**, and
every figure in §4 of `moo141-edit2-recut-rev71.md` re-derives (sixteen anchors at 1 in §1, +1,159
/ +3,375 / +4,534, 62/62 underlines, order independence byte-identical). I did not find a counting
error in that document.

I built the combined text myself (revision 71 + MOO-164's thirteen + this patch's three) and read
the findings below off it, clause by clause.

**Count of findings: 16 — 1 fatal, 7 serious, 5 moderate, 3 minor — plus 11 express null results.**

**The single most serious one: F1.** The chosen formula reproduces the exact defect for which the
Policy Director rejected formula 1 at §2.4 — a deadline that is indeterminable when the Board acts
and breached retrospectively — and it reaches it by two routes the document does not consider: a
denial on judicial review, and a real Board act after a deemed denial. In both, D 1's extension
rides on a duty that could not have been performed, which is the windfall the board declined on
card (g).

---

## 1. The strongest case against, in the opposition's voice

> The Lab has drafted a notice duty that pays members for the Board's losses.
>
> Look at what this sentence now does. A member asks the Board to push her final qualifying
> retirement date back. The Board grants it. The agency whose appropriation paid her subsidy — and
> this section expressly gives that agency standing to go to court — seeks judicial review and
> wins. Her request now stands denied, and it stands denied by a court, not "by a decision of the
> Board upon it." So the Lab's new exception switches on, and it tells the Board that it had to
> give her written notice of her date "no later than 15 days after the date on which the Board acts
> upon the request." The Board acted eighteen months ago. The deadline fell in a month nobody could
> have identified at the time, because at the time the request had been granted. The Board is in
> breach the instant it loses, and subdivision D 1 then extends the member's final qualifying
> retirement date by every day of a lateness that no human being could have avoided — up to the
> twelve months the definition's own excluded aggregate allows.
>
> The Lab knows this argument. It wrote it down. At §2.4 it rejected a shorter formula precisely
> because "at the moment of the act the Board cannot know whether it will ever give a decision, so
> the duty's deadline is indeterminable ex ante and breached retrospectively — which is card (g)'s
> own defect in a new place." That is a quotation from the Lab's own paper, about the Lab's own
> text, and it is fatal to the text the Lab kept. Naming two classes expressly does not make them
> determinable if membership of a class is settled later by somebody else.
>
> And then there is the vocabulary. This section says "determination" one hundred and fifty-two
> times and "decision" nine. On a request under the definition the Board "shall give the member
> written notice of its **determination** and of the reasons for it." It never gives a "decision."
> The Lab's own saving clause in the companion patch lists "to act upon a request, to make a
> determination, or to give a notice or a decision" as four different things. So either these words
> mean different things — in which case every ordinary denial of a later-date request is a denial
> "otherwise than by a decision of the Board," the residual limb swallows the ordinary case, and the
> board's answer of 13:13 on 12 October is reversed in the very class it was given for — or they
> mean the same thing, in which case the deemed denial is itself a determination of the Board and
> the limb is empty in the one class it was drafted for. The Lab cannot have it both ways, and it
> has not told its board that it is standing on a four-word limiter in a different subsection to
> keep the second horn off.
>
> We do not need to win on all of this. We need one of the two readings, and the Lab has not
> foreclosed either.

I can make this case seriously. That is why F1 is rated fatal rather than serious.

---

## 2. Findings

### FATAL

#### F1 — the chosen formula has formula 1's defect: a retrospective, unperformable deadline, and D 1's extension rides on it

**Category:** drafting defect / second-order effect / unintended fiscal consequence.
**Targets:** 1 Q2, 1 Q4, 1 Q5(c).

**What is wrong.** Class 1 of the residual limb — *"where the request is denied otherwise than by a
decision of the Board upon it"* — is defined by a **negative** fact whose truth value can be settled
**after** the date the limb measures from. The document's §2.6 defence of the limb is that in its
two classes "the duty **can** be performed: the Board knows the denial date and knows the date its
period expired." That is true of the deemed-denial class under subsection M 2. It is **not** true of
every case class 1 describes.

**Failure scenario A — denial on judicial review (named party, named claim, named venue).** A member
files a written request under the definition of *"final qualifying retirement date"* on 1 February
and the Board grants a later date, acting on the request on 20 February and stating the date in its
determination. The state agency from whose appropriation an amount was paid on the member's behalf —
given standing in terms by §1: *"…or state agency from whose appropriation an amount was paid on a
member's behalf, aggrieved by, and claiming the unlawfulness of, such case decision, shall have a
right to seek judicial review thereof in accordance with Article 5 (§ 2.2-4025 et seq.) of the
Administrative Process Act"* — seeks review in the circuit court and, on 10 August of the following
year, obtains a reversal. The request is now denied, and it is denied **otherwise than by a decision
of the Board upon it**. Class 1 obtains. The residual limb fixes the notice deadline at **15 days
after 20 February** of the previous year. The Board is roughly 17 months late on a duty that, on 20
February, it had no reason to think it owed and no means of identifying. Subdivision D 1 then
extends the member's final qualifying retirement date "by the number of days by which the statement
or notice is late," subject only to the definition's excluded aggregate of 12 months — so the member
who **lost** on judicial review gains the maximum extension the definition allows.

**Failure scenario B — a real Board act after a deemed denial.** Member files a reconsideration
request 1 January. The ninety days allowed by subsection M (as given a commencement by 164-10)
expire 1 April with no Board action. She files written notice that the period has expired on 5
April. The Board does not act within thirty days, so under M 2's sentence the request "is denied on
the first day after the expiration of those 30 days" — 6 May — and 164-7 deems the Board to act and
to last act on 6 May. The Board, processing its backlog in ignorance of the deemed denial, actually
acts on the request on 20 June. Class 1 obtained on 6 May and still obtains. "The date on which the
Board acts upon the request" is now two dates, and on either of them the fifteen days ran before the
Board knew it owed the notice.

**Authority and evidence.** The document's own §2.4.1, which rejects a shorter formula in these
words: *"At the moment of the act the Board cannot know whether it will ever give a decision, so the
duty's deadline is indeterminable ex ante and breached retrospectively — which is card (g)'s own
defect in a new place. The board's reason for answering card (g) as it did was that a duty must not
fall due on a trigger that is not yet determinable."* The reasoning is sound and it applies to the
retained text. Separately, store revision 61 made a failure to perform within a required period
expressly reviewable, so the retrospective breach is not merely theoretical — it is a reviewable
breach the moment it occurs.

**Suggested direction for the fix** (Drafting Specialist's to write; this is a sentence, not a
draft). Define class 1 by the **affirmative operative fact** rather than by the absence of a
decision, so that membership is fixed at the moment of the act and cannot be conferred later by a
court: *"where the request is denied without the Board's having acted upon it"*. That names the
deemed-denial class exactly — a denial by operation of law happens precisely because the Board did
not act — while excluding a judicial-review reversal (the Board did act) and excluding every
ordinary denial however labelled. It introduces no cross-reference to a subsection and no reference
to a deeming, so §2.4's objection to formula 3 is preserved. It does not resolve scenario B's
two-dates problem; that is F4's, and it belongs in the cross-reference rather than in Edit 2.

---

### SERIOUS

#### F2 — "decision" is not this section's word for what the Board does with a request under the definition

**Category:** drafting defect / undefined term. **Target:** 1 Q2 — the failure mode the Director
named as the one that would be fatal.

**What is wrong.** Counted in enacted §1 at revision 71: **"determination" 152, "decision" 9**. Of
the nine, none requires or authorises the Board to give a *decision* on a request under the
definition. The definition's own operative sentence says the Board *"shall act upon such a request,
and shall give the member written notice of its **determination** and of the reasons for it, no later
than 30 days after the request is filed."* Subsection M's output is *"the final determination issued
by the Board"*, which "shall constitute a case decision" — a label it acquires by deeming, not by
nature. And 164-7's own saving enumerates *"to act upon a request, to make a determination, or to
give a notice or a decision"* as separate things, which is strong internal evidence that the drafter
distinguishes them deliberately.

Edit 2 revision 8 makes **both** of its limbs turn on that distinction: the first limb's trigger is
*"it gives its decision upon the request"*, and class 1 is defined by the **absence** of a decision.

**Failure scenario.** The Board denies a member's later-date request on the merits on 20 February,
giving written notice of its determination and its reasons as the definition requires. Because the
section never calls that a "decision," the request has been "denied otherwise than by a decision of
the Board upon it." Class 1 obtains on an ordinary, fully-reasoned, on-the-merits denial. The
residual limb then displaces the decision-keyed limb and restores **act + 15** — which is the base
text, and the trigger the board rejected at 13:13 on 12 October 2026. The board's card (g) answer is
reversed in a class the board was never shown.

**What I found that cuts the other way, and I am reporting it.** R-7, the sentence immediately
following, reads *"…the month in which the Board gives **a decision or notice** required by the
preceding sentence…"*. So the definition does contemplate the Board *giving* a decision, and that
materially weakens the companion objection that the first limb's trigger never occurs. It does
**not** weaken the objection above, because R-7 tells you the Board gives a decision **when R-6
requires one** — i.e. when it states the date in it — and says nothing about what a denial is.

**Suggested direction.** Either use the section's own word in both places (*"gives written notice of
its determination upon the request"*), or adopt F1's affirmative class definition, which removes the
word "decision" from the class test altogether and cures F1 and F2 together.

#### F3 — class 2 is wider than the deeming it depends on: 164-7's no-act limb covers only subsection A definition requests

**Category:** drafting defect / stranded duty. **Target:** 1 Q1, 1 Q2.

**What is wrong.** 164-7's deeming has two limbs, and its **no-act** limb is confined on its face:
*"or where the Board does not act upon **a request under the definition of "final qualifying
retirement date" in subsection A** within the period allowed by this section for acting upon it."*
Edit 2's class 2 is **not** so confined: *"where the period allowed by this section for acting upon
the request expires without the Board's acting upon it."* Verified mechanically on the combined
text: 164-7's limb carries the subsection A confinement; Edit 2's class 2 contains no reference to
the definition at all.

**Failure scenario.** A member files a reconsideration request under subsection M on 1 January. The
ninety days expire on 1 April without Board action. She does not file written notice that the period
has expired — nothing requires her to, and nothing in the bill tells her that filing it is what
starts the thirty days that produce the deemed denial. So M 2's deemed denial never occurs and
164-7's denial limb never fires; and because the request is a reconsideration request and not a
request under the definition, 164-7's no-act limb never fires either. But Edit 2's class 2 **has**
obtained — the period allowed by this section for acting upon the request expired without the
Board's acting upon it. The residual limb therefore applies and sets the deadline at 15 days after
"the date on which the Board acts upon the request." **There is no such date, in the combined text.**
The duty is engaged with an unascertainable deadline, D 1 cannot fire, and 164-8's replacement notice
of retirement never becomes available. This is MOO-209's F1 in a new form, inside the combined text,
which is the outcome the re-cut exists to prevent.

**Consequence for the document.** The §2.3 table row *"Board **never acts** within the period
allowed → notice due **deemed act + 15**, i.e. expiry + 1 + 15"* is correct for a request under the
definition and **wrong for a reconsideration request**. The class is one class in Edit 2 and two
different classes in 164-7.

**Suggested direction.** Either confine class 2 to *"a request under this definition"* so that it
matches what 164-7 deems — which leaves the reconsideration no-act gap open and routes it to 164-7,
where it belongs — or widen 164-7's no-act limb to reach a reconsideration request on which the
Board does not act. The second is the better repair and it is MOO-164's to make. Either way the two
texts must be scoped against each other, which is a further reason the joint landing is right.

#### F4 — Target 2: the premise of the asymmetry ruling fails. A deemed act does not preclude a later real act

**Category:** correctness of a ruling's premise / conflicting deemings. **Target:** 2.

**The Director's ruling, and the test he set.** The ruling is that Edit 1's exception must name M 2's
duty alone because "Edit 1's deeming addresses the Board that acts more than once; in that class
R-6's deadline is decision-keyed and the residual limb cannot reach it." The test set was: is there
any case in which the Board acts more than once upon a request **and** one of the residual limb's
two classes obtains?

**There is, and it is not exotic.** Nothing in §1 extinguishes the Board's capacity to act on a
request after a deeming has operated, and M 2's own machinery presupposes acts after the relevant
event (*"the Board shall act upon the application no later than 15 days after it acts upon the
request"*). So:

Member files a reconsideration request 1 January; ninety days expire 1 April with no action; she
files the expiry notice 5 April; thirty days pass; the request is denied by operation of M 2 on 6
May and 164-7 deems the Board to act and to last act on 6 May. The Board then actually acts on 20
June, and acts again on 10 July to correct what it did in June. **The Board has acted more than once
upon the request, and class 1 of the residual limb obtains.** Both deemings now reach R-6's deadline:
164-7 fixes the act at 6 May; Edit 1 fixes it at *"the date on which the Board first acts upon it"*,
which is 20 June if a deemed act is not a first act and 6 May if it is. Two deeming sentences, two
dates, the same facts, no priority rule, and neither sentence referring to the other. The same
construction arises in class 2 where the Board acts twice after the period expires.

**Consequence.** The premise that "the residual limb cannot reach a Board that has acted twice and
decided" is true only where the Board **decided**. Where the Board acted twice and the request was
denied by operation of law before it did so, the limb does reach it. So the asymmetry is not
required by *Forst*; on these facts an exception for R-6 in Edit 1 would except a duty the deeming
**can** touch, and its absence is the surplusage problem in reverse — silence where the deeming does
reach, inviting the inference that it was meant to.

**Suggested direction.** Either Edit 1's exception takes R-6's duty as well — restoring symmetry and
making the two savings byte-identical, which is also what MOO-209's N1 asked for — or the
cross-reference resolves priority expressly. The second option runs into F5.

#### F5 — Target 3: the three cross-reference requirements are not sufficient to close F9, and requirements 1 and 3 cannot both be met

**Category:** specification defect. **Target:** 3. **This comes back to the Policy Director, as §3.3
provides.**

**Requirement 1 misdescribes Edit 1 and would narrow it by implication.** The requirement is that
the cross-reference say "that subsection A's deeming governs the case where the Board **acts more
than once** upon a request." Edit 1's deeming is not so confined. Its text applies wherever "a period
begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request," and it
deems the act to fall on "the date on which the Board **first** acts upon it." Where the Board acts
once, that is trivially the same date, but the sentence still operates. A statutory signpost saying
the sentence "governs the case where the Board acts more than once" would be construed as confining
it, which is a substantive amendment wearing a signpost's clothes.

**Requirement 2 would state something that is false.** Requirement 2 asks that the two be made
"cumulative and non-overlapping." F4 shows a case in which they **do** overlap and fix different
dates. A statute that declares two provisions non-overlapping when they overlap does not remove the
conflict; it removes the court's ordinary tools for resolving it and leaves the reader with a false
premise.

**Requirement 3 cannot be satisfied alongside requirement 1.** Requirement 3 is that the
cross-reference "move no date and add no exception." But requirement 1 asks it to say which deeming
governs which case, and in F4's overlap case saying which deeming governs **is** choosing between 6
May and 20 June. That is moving a date. The two requirements are therefore jointly unsatisfiable on
the current text: any cross-reference truthful enough to satisfy requirements 1 and 2 must do the
thing requirement 3 forbids.

**Answer to the question as asked.** No — the three requirements are not sufficient to close F9, and
a cross-reference meeting them is not possible without either touching an exception or resolving
priority. Per §3.3's own terms, that is a finding and it is the Director's to decide. The cheapest
route I can see is to cure F4 first by giving Edit 1's exception R-6's duty: with the exceptions
symmetric, the cross-reference has only to signpost, and requirement 3 becomes achievable.

#### F6 — Target 1 Q3: R-6's chapeau fails in the sub-case the expiry sentence was written for, so the limb is inert there

**Category:** drafting defect / the cure is incomplete. **Target:** 1 Q3.

**What is wrong.** R-6 is conditional: *"**Where the Board's action upon a request determines a
member's final qualifying retirement date under this definition**, the Board shall state that date in
its decision upon the request, and where the Board does not do so it shall give the member written
notice of that date…"*. The question is whether that condition holds in the deemed classes. The
"action" element is supplied — R-6 is a provision under which a period is measured from the Board's
acting, so it is inside 164-7's confinement clause and the deeming operates for its purposes. The
**"determines"** element is not, and in one sub-case it is affirmatively false.

**Failure scenario.** A member files a later-date request under the definition. The Board does not
act within the thirty days the definition allows. The date that would otherwise apply is earlier than
the first day of the second month following the month in which that period expired. The definition's
own sentence then applies: *"Where the Board does not act upon a request the filing of which tolled
the running of the member's final qualifying retirement date under subsection M within the period
this definition allows for acting upon it, and the date that would otherwise apply under this
definition is earlier than the first day of the second month following the month in which that period
expired, the member's final qualifying retirement date is, **notwithstanding any other provision of
this definition**, that first day."* Her date is therefore determined by **the expiry of the period**,
and determined in terms that override every other provision of the definition — not by the Board's
action, real or deemed. R-6's condition is false, R-6 is not engaged at all, and the residual limb
has nothing to attach to. **She acquires a statutory final qualifying retirement date and is never
told it** — which is the harm MOO-209's F1 identified.

The irony is worth stating plainly: the sub-case in which the cure goes inert is the sub-case the
expiry sentence exists for.

**Suggested direction.** The chapeau needs widening, not the limb: R-6 should engage where the
member's date is determined under the definition **by reason of the Board's not acting** as well as
by reason of its action. That is a change to base text rather than to the residual limb, so it is a
fourth edit and a Director-level scope decision, not a drafting tidy-up.

#### F7 — Target 4 does not close: the 60-day restore-and-settle duties are outside the saving's enumeration altogether

**Category:** drafting defect / reviewable breach. **Target:** 4 (the open finding of 17:26 on 12
October 2026).

**What I found.** The duty reads: *"Where a determination under subdivision 2 or 3 that has taken
effect is reversed or modified on reconsideration under subsection M or on judicial review, the Board
shall restore or credit service credit as this subdivision provides, and … shall recertify and settle
it accordingly, **no later than 60 days after the reversal or modification**…"*, with a parallel
60-day duty to pay a deceased member's entitled person.

Two steps, and the second is the finding.

1. **Does Edit 1's trigger reach it?** Textually, weakly: the sixty days are measured from "the
   reversal or modification," not from "the Board's acting … upon a request," and Edit 1's deeming is
   drafted to catch periods described in the latter words. But where the reversal is *on
   reconsideration under subsection M*, the reversal **is** the Board's act upon the reconsideration
   request, under a different name. A court reading substance rather than form has a real route in.
   So the trigger is narrowed, not eliminated.
2. **If it does reach, does the saving stop it? No — and this is the part that was not visible
   before.** The saving's protected list is closed and enumerated: *"nothing in the preceding
   sentence determines the date by which the Board is required **to act upon a request, to make a
   determination, or to give a notice or a decision**, or whether the Board has performed **such a
   duty** within a period required by this section."* A duty to **restore or credit service credit**,
   to **recertify and settle a certified subsidy**, or to **pay an amount** is not an act-upon, a
   determination, a notice or a decision. It is in neither the enumeration nor the exception. So the
   saving affords it no protection at all, and "such a duty" in the second branch carries the same
   limit.

**Failure scenario.** The Board acts on a reconsideration request on 20 February (partially) and
again on 20 June, reversing a D 2 determination. On the substance reading, Edit 1 deems the act to
fall on 20 February, the sixty days expired on 21 April, and the restore-recertify-settle duty is
breached on the day it arises. Store revision 61 made a failure to pay within a required period
expressly reviewable, so the member's remedy is immediate and the Board's position is indefensible.

**Scoping result, which is favourable and I am reporting it.** The exposure is **Edit 1's alone**.
164-7's two classes are a denial of reconsideration and a failure to act; neither can produce a
"reversal or modification" of a D 2 or D 3 determination. So 164-7 needs no change on this finding.

**Suggested direction.** Add the three duty-families to the **main-clause enumeration** of Edit 1's
saving — "to restore or credit service credit, to recertify or settle a certified subsidy, or to pay
or include any amount." That extends what the deeming does **not** determine; it adds no exception,
so it does not collide with the §3.3 constraint, and it keeps the two savings' bodies comparable.
**The finding does not close. The saving's list is short.**

#### F8 — the load-bearing fiscal assumption fails on its own terms, and the Director's own §2.6 trigger fires on this pass

**Category:** evidence gap / fiscal assumption. **Target:** 1 Q5(b).

**The assumption under test**, because it is the sole stated ground for opening no Fiscal & Impact
Modeler issue (§2.6, §6): *"The 12-month aggregate cap is unmoved, so there is nothing to
re-price."*

**The test.** The statement is about a **bound**. The quantity that drives cost in MOO-163 is a
**population** against a fixed $3,000,000 pool. An unmoved per-member cap says nothing about how
many members reach it. I imported MOO-163's register unchanged (`moo215-adversarial/d1_channel_test.py`,
which reads `moo163_inputs.py` and writes nothing) and swept the one input the conclusion needs.

**Result.**

| Board no-act rate | class 1 (M 2 denial) | class 2 (definition request) | total members over the 48-month pilot | vs MOO-170's own stated resolution (2.80 members) |
|---|---|---|---|---|
| 0.00 | 0.000 | 0.000 | 0.000 | below |
| 0.05 | 0.002 | 0.897 | 0.899 | below |
| 0.10 | 0.009 | 1.793 | 1.802 | below |
| **0.20** | 0.038 | 3.586 | **3.624** | **ABOVE** |
| 0.35 | 0.116 | 6.275 | 6.391 | ABOVE |

The crossover is at a Board no-act rate of **15.6%**. Three things follow.

- **MOO-163 does not model this channel at all.** Of the twenty levers in its register, **none**
  touches the final-qualifying-retirement-date extension, notice lateness, or a Board no-act rate.
  Its $0 and MOO-170's $204,000 bound price **queue ordering against a fixed pool**. They therefore
  neither cover nor exclude this channel. The Director's §2.6 statement that they "were released on
  inputs that did not include a D 1 extension channel in the deemed classes" is right; the conclusion
  "so there is nothing to re-price today" does not follow from it.
- **The two inputs needed to screen it out do not exist.** The Board no-act rate and the rate at
  which funded members file later-date requests appear nowhere in any register in this project. "$0"
  on this limb is an unpriced assertion, not a counted one. (My class-2 column assumes every funded
  member files one later-date request, which over-counts; the honest statement is that the screen
  **cannot be performed**, in either direction, on the inputs that exist.)
- **The dominant class is the one §2.6 does not discuss.** Class 1 (deemed denial) is numerically
  negligible — two independent no-act gates make it quadratic in a small number, 0.038 members even
  at a 20% no-act rate. The exposure is in **class 2**, the definition request from the funded
  cohort, which is linear in the no-act rate and an order of magnitude larger. §2.6's reasoning is
  about the deemed-denial class.

**And the Director's own trigger has fired.** §2.6 records: *"Trigger: if the bounded pass at §5
widens the limb beyond the two named classes … MOO-163 and the declined F-6 cap re-open on this limb
on the same footing as the MOO-49 trigger."* F1 widens class 1 to a judicial-review denial and a
post-deeming real act; F2 widens it to every ordinary denial of a later-date request; F3 widens class
2 to reconsideration requests 164-7 does not deem. **The limb is wider than its two named classes on
three independent grounds, so the trigger is met on its own terms.** I am naming the trigger, which
is all this pass is permitted to do with the declined F-6 cap and the board's 120 days. The routing
decision is the Director's.

**What I am not saying.** I am not asserting a non-zero dollar figure. On the figures above the
channel is probably immaterial at a plausible no-act rate, and I would expect a proper pass to come
back at or near $0. The finding is that the ground given for not asking is wrong, and that the
answer is currently unknown rather than known to be zero.

### MODERATE

#### F9 — Target 1 Q6: "inert" is substantially right; "harmless" is not

**Category:** drafting defect / standalone application. **Target:** 1 Q6.

**The assertion tested:** "Applied without MOO-164, the residual limb is inert and harmless … no
deadline is produced — the same position as the base, with no dangling reference."

**"Inert" is right in effect.** With no deeming there is no date on which the Board acts in the
named classes, so no deadline arrives, so nothing is late, so D 1 does not fire. And the verifier's
two assertions are sound: the limb names no subsection and no deeming, so there is no dangling
reference. Confirmed on my own run.

**"The same position as the base" is not right, in two ways.**

1. **Class 1's predicate is satisfied in the base.** M 2's deemed-denial sentence was enacted at
   store revision 63 and is live at revision 71 — the verifier itself asserts it at 1. So standalone,
   a request **is** denied otherwise than by a decision of the Board, class 1 **does** obtain, and the
   limb **does** engage a statutory duty — it just gives it a deadline that can never arrive. A duty
   expressly engaged with an unascertainable deadline is not the same thing as no duty: it is
   unenforceable and simultaneously un-breachable, so the member has a right with no remedy and the
   Board has a duty with no date. That is a drafting defect in its own right, independent of MOO-164.
2. **Class 2's predicate is itself indeterminate standalone.** Class 2 turns on "the period allowed
   by this section for acting upon the request." For a reconsideration request the base says only
   *"The Board shall act upon a request for reconsideration within 90 days"* — with no commencement
   until 164-10 supplies one. So standalone, the class-2 predicate cannot be evaluated for a
   reconsideration request at all.

Both points argue **for** the joint landing decided at §3.2, so this finding supports the Director's
conclusion while correcting its stated basis.

---

#### F10 — class 1 is kept from being empty by a four-word limiter in another subsection, and that is not disclosed

**Target:** 1 Q2, the other horn. M 2's sentence reads: *"the request is denied on the first day
after the expiration of those 30 days, and that denial constitutes the final determination of the
Board upon the reconsideration and a case decision as defined in § 2.2-4001 **for the purposes of
this subsection**."* If the deemed denial is a "decision of the Board upon" the request, class 1 is
**empty in the class it was drafted for** and the cure is wholly inert. What prevents that is the
limiter: the case-decision characterisation operates for subsection M's purposes, and R-6 is in
subsection A. So within subsection A the deemed denial is a denial and nothing more. That reading is
probably right, but it is load-bearing for the entire cure and it appears nowhere in §2.2, §2.3 or
§2.4. It should be on the face of the record, and it is a further reason to prefer F1's affirmative
class definition, which does not depend on it.

#### F11 — 164-7's exception identifies R-6's duty by a descriptor that quotes nothing

**Target:** 1 Q1, chain link 3. The exception names *"the duty of the Board under the definition of
"final qualifying retirement date" in subsection A to give the member written notice of the member's
final qualifying retirement date."* That phrase appears **zero** times in the text — the Director's
own verifier asserts the count at 0 — so it is a functional description, and the definition contains
a second duty answering to it: *"shall give the member written notice of any later date approved
after that statement no later than 15 days after the approval,"* a later approved date being the
member's final qualifying retirement date. The ambiguity is harmless in effect, because that second
duty is measured from "the approval" and so falls outside the deeming's confinement clause, but an
exception that identifies its target by paraphrase in a section with two candidates should quote or
locate instead.

#### F12 — the claim that the D 1 channel depends on 164-5 is not established

**Target:** 1 Q5(a). The assertion is that the limb "reaches D 1 only on 164-5's broader *by reason
of* descriptor." D 1's **pre-164-5** descriptor is *"any notice of a date required by that definition
**upon the Board's action upon a request**"* — which tracks R-6's chapeau, *"Where the Board's action
upon a request determines…"*, almost word for word. Once the chapeau is satisfied, there is an
action, and a notice required by the definition upon it; "upon" is satisfied on the same facts as "by
reason of." So the channel does not appear to depend on 164-5 at all. That weakens the ordering
premise at §2.5 that rests on it ("application of this patch does not precede the cut carrying F-9
… now load-bearing twice over"): the first of the two reasons stands, the second does not. The
consequence is not that the ordering constraint should go — the joint landing makes it moot — but
that the D 1 channel opens whether or not 164-5 lands, which matters to F8's scoping.

#### F13 — "the period allowed by this section" is ambiguous for a reconsideration request

**Target:** 1 Q1. The section allows two periods for acting on a reconsideration request: the ninety
days of subsection M (given a commencement by 164-10), and the further thirty days after the member
files written notice that the ninety have expired. Class 2's predicate — "the period allowed by this
section for acting upon the request expires without the Board's acting upon it" — turns on which. The
ambiguity is inherited from MOO-164's phrase (164-3, 164-4, 164-6, 164-11 all adopt it) rather than
created by Edit 2, but Edit 2 is the first provision to make a **duty's start date** turn on it, which
raises the stakes. Worth a sentence to the Drafting Specialist as part of the joint cut.

---

### MINOR

#### F14 — scope word: "this section" inside a definition that says "this definition"

Counted at revision 71: the definition of *"final qualifying retirement date"* uses **"this
definition" 17 times and "this section" 0 times**. Edit 2 introduces "the period allowed by this
section." In the combined text 164-4 does the same thing, so there it is a consistency point only;
applied standalone, Edit 2's is the sole intrusion. No substantive effect — the definition is part of
the section — but it is the kind of inconsistency a *Forst* argument is built out of, and the
Director's Q4 is right to be watching this register.

#### F15 — counted correction to §2 of the document

The document says §1 "carries one *'the request is denied'* (the deemed denial) and **three** other
*'denied'*s about elections and applicants." At revision 71 the counts are: **"denied" 3** in total —
`the request is denied`, `An applicant who is denied or wait-listed`, and `the number of elections
accepted, denied, and wait-listed` — so **two** others, not three; plus **"denial" 2** (`denial of an
election`, `that denial constitutes…`), **"denies" 0**, **"deny" 0**. The conclusion drawn from the
count is unaffected: *"the request is denied"* resolves exactly once in §1, and it is the deemed
denial.

#### F16 — the §2.3 table needs two rows, not one, for the no-act class

Consequential on F3 and F6: the single row *"Board **never acts** within the period allowed → notice
due deemed act + 15, i.e. expiry + 1 + 15"* is true only of a request under the definition in which
the chapeau is satisfied. It is false for a reconsideration request (F3) and false where the expiry
sentence determines the date (F6). If the table survives into any briefing, it should be split.

---

## 3. Citation and reproduction verification

Every item below was re-opened against the store text at revision 71, not against a document's
quotation of it.

| # | Claim checked | Source re-opened | Held? |
|---|---|---|---|
| 1 | Base is 484,408 / §1 134,012 / sha `83a10b74950b5272…` | `moo141-rev71/live.md`, computed independently | **Held** |
| 2 | All three MOO-141 anchors resolve once in §1; dead rev-65 string at 0 | §1, own counts | **Held** |
| 3 | All thirteen MOO-164 FINDs resolve once in §1 at revision 71 | §1, own counts | **Held** |
| 4 | +847 / +1,159 / +326 / +3,375 / +4,534; limb length 311 | applied to my own copy | **Held, all six** |
| 5 | Order independence byte-identical | own application both ways | **Held** |
| 6 | 62/62 underlines, balance 0; `first acts upon` 2 → 3 | §1 and combined | **Held** |
| 7 | Ninth `acts upon` is the DPB Director's and out of reach of both deemings | §1 | **Held** |
| 8 | 164-7's exception names R-6's duty; residual limb present once; classes once each; decision-keyed limb ordered first | combined text | **Held** |
| 9 | 12-month excluded aggregate cap present once and textually identical before and after | §1 and combined | **Held** |
| 10 | Twelve saved provisions, G 4's two `first`s, G 4's anti-delay sentence, M 2's deemed-denial sentence intact | §1 and combined | **Held** |
| 11 | "§1 carries … three other `denied`s" | §1 | **Did not hold** — two. See F15 |
| 12 | "reaches D 1 only on 164-5's broader descriptor" | D 1 pre- and post-164-5 text, R-6's chapeau | **Did not hold** — see F12 |
| 13 | "the residual limb … cannot reach a Board that has acted twice and decided" (the asymmetry premise) | M 2, 164-7, Edit 1 | **Did not hold** on the overlap facts — see F4 |
| 14 | "in these classes the duty **can** be performed" | class 1's full extension | **Did not hold** for a judicial-review denial or a post-deeming act — see F1 |
| 15 | "the same position as the base, with no dangling reference" (standalone) | M 2 base sentence, base 90 days | **Partly** — no dangling reference holds; "same position" does not. See F9 |
| 16 | MOO-163/MOO-170 $0 and $204,000 cover this limb | `moo163_inputs.py`, `moo170_chain_inputs.py` | **Did not hold** — neither register has an FQRD-extension or no-act lever. See F8 |

`verify_r71.py` was run unmodified and passed in full on my invocation. I found no failing assertion
in it. Its assertions are true; four of the document's **prose** claims are not, which is the gap
between a verifier and a reading.

---

## 4. Answers to the seven questions, in the order asked

1. **Does the residual limb have a start date in the two classes it names?** The chain holds in its
   mechanics — see N1 — and fails at two points outside it. The residual limb's fifteen days is a
   period "measured from the Board's acting upon the request," so 164-7's confinement clause reaches
   it; 164-7's express exception lifts R-6's notice duty out of the saving; and the deeming supplies
   "the date of that denial" or "the day after the expiration of that period." **That part is sound.**
   But the chapeau defeats it in one sub-case (**F6**) and class 2 outruns 164-7's no-act limb in
   another (**F3**). So: a start date exists for a **request under the definition** on which the Board
   does not act **where the chapeau is satisfied**, and for the **deemed denial**. It does not exist
   for a reconsideration request whose period expires without the member filing the expiry notice, and
   R-6 is not engaged at all where the expiry sentence determines the date. **The cure is partial.**
2. **Is either named class wider than you think?** **Yes — both, and this is the fatal answer.** Class
   1 reaches a denial on judicial review and a post-deeming real act (**F1**), and on the section's own
   vocabulary it reaches every ordinary denial of a later-date request (**F2**). F2 is the failure mode
   you flagged as the one that would be fatal; I rate F1 fatal and F2 serious only because F1's route
   does not depend on winning the determination/decision argument.
3. **Is either named class narrower than you think?** **Yes.** R-6's duty is not engaged where the
   expiry sentence determines the date "notwithstanding any other provision of this definition"
   (**F6**). The "action" element of the chapeau **is** supplied by the deeming, because R-6 is inside
   the confinement clause; it is "determines" that fails. The "where the Board does not do so" element
   holds in both deemed classes — express null, **N2**.
4. ***Forst*.** The give-versus-act split you identified is real but survivable on its own, because
   R-7 expressly contemplates the Board *giving* "a decision or notice required by the preceding
   sentence." **The sharper *Forst* exposure is decision-versus-determination (F2), and it is bigger
   than the one you named**: 152 to 9 in §1, with 164-7's own saving enumerating them separately, and
   Edit 2 moving the word into a deadline where the base used it only to say where to state a date.
5. **The D 1 channel — all three attacked.** (a) **Not established** — the channel does not depend on
   164-5 (**F12**). (b) **Correct, as a statement about the bound** — the cap is textually unmoved and
   the limb cannot exceed it (**N5**); but the inference drawn from it does not follow, because an
   unmoved per-member bound is not an unmoved aggregate (**F8**). (c) **Correct for the two classes as
   you described them, false for class 1 as drafted** — the duty cannot be performed where membership
   of the class is settled later by a court (**F1**).
6. **The standalone case.** "Inert" is right; "harmless" and "the same position as the base" are not.
   It creates a duty with an unascertainable deadline, and one of its two predicates is itself
   indeterminate in the base (**F9**). Supports the joint landing.
7. **The three rejected formulas.** **None of the three is better than what you drafted**, and I
   agree with each of your three reasons and with the fourth refusal. Formula 2 is empty in the class
   that matters; formula 3 makes the patches interdependent; formula 4 starts the member's clocks
   without her knowledge. **But formula 1 was rejected for a defect the chosen formula shares**
   (**F1**), so the answer to "is one of them better" is no — and the answer to the question behind it
   is that a fourth formula is needed. Candidate, routed to the Drafting Specialist and not drafted
   into anything: define class 1 affirmatively, *"where the request is denied without the Board's
   having acted upon it"*, and confine class 2 to *"a request under this definition"*. That cures F1,
   F2 and F3, keeps the limb free of any cross-reference or deeming word, and leaves F4's two-dates
   problem where it belongs — in the cross-reference.

---

## 5. What I checked and found sound — express null results

These cost as much work as the findings and several of them are load-bearing for the cure.

- **N1 — the chain's mechanics.** Deeming → confinement clause → express exception → residual limb
  measuring from the deemed date. Every link verified on the combined text. The residual limb is a
  period "measured from the Board's acting upon the request"; 164-7's confinement clause reaches it;
  the exception removes R-6's duty from the saving; the deeming supplies the date. **Sound.**
- **N2 — the "does not do so" element.** In both deemed classes there is no decision, so the Board
  necessarily does not state the date in one, and R-6's residual duty is engaged on that element.
  **Sound.**
- **N3 — the deeming does not eat its own predicate.** The deemed act is "the day after the
  expiration of that period," which is outside the period, so the expiry sentence's own premise —
  "the Board does not act … within the period" — remains true. No self-destruction. **Sound.**
- **N4 — no stranded sentence references.** Checked mechanically at all four insertion points (Edit
  1, Edit 2, 164-7, 164-8). R-7's "the preceding sentence" still points at R-6 after Edit 2, because
  Edit 2 keeps R-6 a single sentence; nothing following the other three insertions back-references a
  sentence they displace. **Sound.**
- **N5 — the 12-month excluded aggregate cap.** Textually unmoved, present once before and after, and
  the limb cannot exceed it. §2.6(b) is right about the bound. **Sound.**
- **N6 — withdrawal and dismissal are not routes into class 1.** §1 contains no "dismiss" at all, and
  all nine "withdraw" occurrences concern **applications**, not requests — there is no provision for
  withdrawing a request under the definition or a reconsideration request. So class 1 is not widened
  by either. **Sound** (this was one of your three candidates and it is clean).
- **N7 — the ninth `acts upon`.** Re-verified independently: the actor is the Director of the
  Department of Planning and Budget or a designee, and both deemings are confined to the Board's own
  acting, so neither reaches it. **Sound.**
- **N8 — every count in §4 of the document.** Sixteen anchors, five deltas, the underline balance, the
  `first acts upon` move, order independence, the twelve saved provisions. All re-derived on my own
  run. **Sound.**
- **N9 — 164-7 needs no change on Target 4.** Its two classes cannot produce a "reversal or
  modification" of a D 2 or D 3 determination, so the 60-day exposure is Edit 1's alone. **Sound, and
  this usefully halves the work on F7.**
- **N10 — Edit 1 over a 164-7 deemed act is harmless.** In a no-act class there is no real first act;
  if the deemed act counts as the first act, Edit 1 fixes the same date. **Sound outside F4's overlap
  case.**
- **N11 — the board's decided effect in the class the board was shown.** The first limb is revision
  6's character for character, it survives inside revision 8 exactly once, it is ordered first, and no
  word of the bill is deleted. In the class the board answered at 13:13 on 12 October 2026 — Board
  acts, Board decides — revision 8 changes nothing. **Sound**, and F2's threat to it operates through
  the denial sub-class, not through this one.

Also deliberately not done, per the issue's terms: the board's 120 days are not reopened; the
declined F-6 cap (MOO-179) is not reopened, only named as a trigger at F8; nothing is drafted into
either patch; and nothing is applied to the store.

---

## 6. Routing

| To | Finding | Why it is theirs |
|---|---|---|
| **Policy Director** | **F1, F4, F5, F6, F8** | F1 is a text decision above drafting level; F4 and F5 are the asymmetry ruling and the §3.3 specification, both expressly reserved to you; F6 needs a fourth edit to base text; F8 is a routing decision on your own trigger |
| **Drafting Specialist** | **F2, F3, F7, F11, F13, F14** | Each is a text fix with a stated direction. F7's fix is to the saving's main-clause enumeration, which adds no exception and so does not collide with §3.3's requirement 3 |
| **Fiscal & Impact Modeler** | **F8** | Needs a Board no-act rate and a later-date-request filing rate; neither exists in any register. My sweep and the import-only script are at `moo215-adversarial/d1_channel_test.py` |
| **Statutory Researcher** | **F2, F13** | Whether this section's "decision" and "determination" are distinct terms of art, and which of the two periods is "the period allowed by this section for acting upon" a reconsideration request |
| **Editor — must appear in the memo's risk section** | **F1, F2, F4, F5, F7** | A retrospective unperformable deadline with a D 1 windfall; a class that may swallow the ordinary denial; two conflicting deemings with no priority rule; a specification that cannot be met as written; and an open 60-day duty the saving does not protect |
| **Stakeholder Analyst** | one party | The **state agency from whose appropriation an amount was paid on a member's behalf** has express standing under §1 and is the litigant in F1's scenario A. It bears the cost of the D 1 extension that scenario produces and should be on the stakeholder map if it is not |

---

**Internal risk analysis. Not legal advice, and not a legal opinion the organization can rely on. No
counsel has reviewed or cleared this proposal. Not a DLS bill. Pre-decisional. Nothing applied to
the store.**
