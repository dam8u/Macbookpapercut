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

**Price, and which way it cuts.** The member gains a filing window she does not have today; the Board
gains no duty it does not have today (it is already required to give the notices, already required to
report every delay under subsection J, and already bound by the extension). **Against today's text it
costs the Commonwealth nothing except in the case where the member uses the window to retire later than
she otherwise could have — which is the case the extension already decided in her favour.** It is in
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

**Candidate 164-7 — insert two sentences in M 2, immediately after the enacted denial sentence. 106 words,
+583 characters. Not applied.**

> **FIND** (count = **1** at store revision 63):
>
> ```
> the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.
> ```
>
> **READ:**
>
> ```
> the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. Where a request is denied by operation of the preceding sentence, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, to act upon the request, and to last act upon it, on the date of that denial. Nothing in the preceding sentence relieves the Board of the duty to act upon a request for reconsideration, or determines whether the Board has acted upon a request within the period allowed by this section.
> ```

**Four things to see in it, because each is a drafting choice I made rather than a word I found.**

1. **It is Decision 1's method, not its opposite.** It does **not** define *"act upon"* and it does not
   touch any of the 21 occurrences. It supplies a **date** for one event the section creates and leaves
   the verb alone — which is what §1.2 recommended and why option (f-4) beat the verb definition.
2. **Its form is the bill's own.** The confinement to provisions *"under which a period begins or ends
   upon, or is measured from, the Board's acting, or last acting, upon the request"* is lifted **word for
   word** from the MOO-141 patch's Edit 1, which is already in front of the Director; and the second
   sentence is Edit 1's own saving clause, so the deemed denial **cannot** discharge the Board's 90-day
   duty or make its breach disappear. Two words for one concept is the defect §3.6 exists to prevent, and
   this candidate avoids it by using Edit 1's words.
3. **It makes Edit 164-1's cap work in the only case where that cap currently fails.** With 164-7 the
   deemed act date exists, so the tolling ends at **denial + 48 days** at the outside, by Edit 164-1's own
   cap and with no new number.
4. **It reaches endpoint 4, the Board's 15-day duty on the application, and I did not carve that out.**
   That is deliberate and it is the one limb a reviewer should press on. Carving it out would leave the
   member whose retention has ended with no decision on her application; reaching it means a duty on the
   Board is triggered by the Board's own inaction, 15 days after the deemed denial. **I think reaching it
   is right and I am flagging it rather than burying it.**

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
reference**, and nothing in the text warns a drafter of it. I am not amending it — an ordinal reference
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

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by counsel,
and nothing here states or implies that it has been. Pre-decisional and internal.**
