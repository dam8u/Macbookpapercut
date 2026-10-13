# MOO-141 — revision 9: all sixteen MOO-215 findings disposed of, the asymmetry ruling reversed, and a fourth edit

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared
by counsel. Pre-decisional. Nothing applied to the store and nothing in this document authorises
applying anything.**

Policy Director · 13 October 2026 · cut and verified at **bill store revision 72**

---

## 0. The disposition in one table

MOO-215 reported 1 fatal, 7 serious, 5 moderate, 3 minor and 11 express null results. **All sixteen
findings are disposed of. Nine are cured in the text. Five are routed. Two are accepted as record
corrections. None is carried forward undisposed.**

| # | Severity | Disposition |
|---|---|---|
| **F1** | fatal | **Accepted and cured.** Edit 2 class 1 redefined by an affirmative fact |
| F2 | serious | **Accepted in part and cured in part.** The class test loses the word "decision"; the first limb keeps it, on R-7's own wording and because it is the board's decided text |
| F3 | serious | **Accepted in substance, rejected in direction.** Not a stranded duty — a missing duty. Cured by Edit 4. The 164-7 half is **no longer load-bearing** for this patch |
| **F4** | serious | **Accepted. My 01:32 asymmetry ruling is reversed.** Edit 1's exception takes R-6's duty |
| **F5** | serious | **Accepted. My three cross-reference requirements are withdrawn and replaced by four** |
| **F6** | serious | **Accepted, and the class is wider than the finding states.** Cured by Edit 4 — a new, fourth edit |
| F7 | serious | **Accepted and cured.** Edit 1's saving enumeration takes the three duty families. **My 17:26 finding of 12 October now closes** |
| **F8** | serious | **Accepted. My "nothing to re-price" ground is withdrawn and the fiscal issue is opened** |
| F9 | moderate | **Accepted.** "Harmless" withdrawn. It argues for the joint landing, which is decided |
| F10 | moderate | **Accepted and designed out.** F1's cure does not depend on M 2's limiter |
| F11 | moderate | **Routed** to the Drafting Specialist, with one new coupling: Edit 1 now uses the same descriptor |
| F12 | moderate | **Accepted.** §2.5's second ordering reason is withdrawn |
| F13 | moderate | **Routed**, and it does not bite while R-6's chapeau gates the limb |
| F14 | minor | **Answered by 164-4**, which chose "this section" deliberately. Standalone-only, and the joint landing is decided |
| F15 | minor | **Accepted.** Counted correction taken |
| F16 | minor | **Accepted.** Consequential on F3 and F6; the table is superseded by §4 below |
| N1–N11 | nulls | **All eleven accepted.** N8 re-derived independently at a new base |

**And one finding of my own, against my own record, found by a check I wrote to prove the opposite —
at §6.1. The claim "no word of the bill is deleted" is false and has been false since revision 5.**

---

## 1. The base: store revision 72 is record only, and this is the first time that is provable

`bill-text-s8`, document revision `368f5e41`, **whole document 502,586 characters**, enacted §1
**134,012**, §1 **sha256 `83a10b74950b5272…`**.

> **Enacted §1 is byte-identical to store revision 71.** Same length, same hash. So every count the
> MOO-215 pass took at revision 71 carries to revision 72, and `verify_r72.py` **asserts the hash**
> rather than inferring identity from a character count. This is the payoff of starting to hash §1 at
> `moo141-gate3-rev64`: the base has moved **ten** times under this item, and this is the first move
> that could be dismissed in one line with proof.

All four anchors resolve **exactly once in §1**. Edit 1's FIND still reads **2** whole-document,
because §5's own sweep quotes it — so the §1-scoped rule stands and the whole-document figure is
reported for the applier rather than used as a test.

---

## 2. Revision 9: four edits, **+1,716** in §1

| Edit | What it is | Δ | Change from revision 8 |
|---|---|---|---|
| **1** | the pendency / tolling re-key, its exception and its saving | **+1,116** | exception gains R-6's duty (F4); saving gains three duty families (F7) |
| **2** | card (g), the 15-day date-notice backstop, with the residual limb | **+317** | class 1 redefined (F1, F2, F10) |
| **3** | card (k-ii), the D 4 / D 5 retention at the board's **120 days** | **+15** | **unchanged** |
| **4** | **NEW** — a notice duty on the definition's expiry sentence | **+268** | new (F6, F3) |

**§1 +1,716; whole-document +1,716, so no edit lands outside §1. `<u>` 62/62. `first acts upon`
2 → 3. Combined with MOO-164 revision 7: +5,091 = 3,375 + 1,716, order-independent and
byte-identical in either order — a seventh base at which that holds.**

### 2.1 Edit 2 — F1's cure is four characters shorter than the defect

**Before (revision 8):** *"…except that where the request is **denied otherwise than by a decision of
the Board upon it**, or where the period allowed by this section for acting upon the request expires
without the Board's acting upon it, it shall give that notice no later than 15 days after the date on
which the Board acts upon the request."*

**After (revision 9):** *"…except that where the request is **denied without the Board's having acted
upon it**, or where the period allowed by this section for acting upon the request expires without the
Board's acting upon it, it shall give that notice no later than 15 days after the date on which the
Board acts upon the request."*

**The reviewer's fatal finding was right, and it was right on the ground I had myself stated at §2.4.1
when rejecting a different formula.** Class 1 was defined by a **negative** fact, and a negative fact
can be made true after the date the limb measures from. Their scenario A is the proof: the Board acts
and grants; a state agency with express standing obtains a reversal on judicial review seventeen
months later; the request is then denied, and denied otherwise than by a decision — so the deadline
was fixed fifteen days after an act that nobody could then have known created a duty, and subdivision
D 1 would have extended the date of the member who **lost** in court by up to the full 12 months the
definition allows.

**The affirmative formula takes the class's membership out of the future.** Counted:

- **Scenario A no longer reaches it.** The Board had acted, so the request is not denied *without the
  Board's having acted upon it*. **Class 1 does not obtain.**
- **The deemed-denial class still reaches it exactly.** A denial by operation of M 2 happens
  *because* the Board did not act, so the class is satisfied on the facts that produce it and is
  satisfied **at the moment the denial occurs**.
- **F2 is cured in the same stroke.** The word *"decision"* now appears **nowhere** in the class test.
  So the F2 scenario — an ordinary, fully-reasoned, on-the-merits denial of a later-date request,
  which this section calls a *determination* and not a *decision* — cannot fall into class 1. That
  was the one reversal of the board's card (g) answer I had called fatal if true, and it was true.
- **F10 is designed out.** The cure no longer turns on whether M 2's deemed denial is a *"decision"*,
  so it no longer rests on the four-word limiter *"for the purposes of this subsection"* in another
  subsection. That limiter was load-bearing and undisclosed; it is now neither.

**What I did not change, and why.** The **first limb's** trigger stays *"it gives its decision upon the
request"* — revision 6's text, character for character, the board's answer of 13:13 on 12 October 2026.
Two reasons, and the second is the reviewer's own. It is the board's decided text. And R-7, the very
next sentence, reads *"the month in which the Board gives **a decision or notice** required by the
preceding sentence"* — so the definition does contemplate the Board giving a decision required by
R-6, which is the trigger the first limb uses. **The register question is still live and is routed**
(F2, to the Statutory Researcher): if *"determination"* is the right word in R-6's deadline, that is a
change to the board's decided text and it comes back to the board, not to me.

**Class 2 is unchanged**, and §3 says why.

### 2.2 Edit 1 — two changes, and both make the two patches more alike rather than less

**(a) The exception takes R-6's duty.** It now reads:

> *"**Except for the purposes of the duty of the Board under subsection M to act upon an application no
> later than 15 days after it acts upon the request and the duty of the Board under the definition of
> "final qualifying retirement date" in this subsection to give the member written notice of the
> member's final qualifying retirement date,** nothing in the preceding sentence determines…"*

**(b) The saving's enumeration takes three duty families** (F7):

> *"…nothing in the preceding sentence determines the date by which the Board is required to act upon a
> request, to make a determination, to give a notice or a decision, **to restore or credit service
> credit, to recertify or settle a certified subsidy, or to pay or include any amount**, or whether the
> Board has performed such a duty within a period required by this section."*

**+111 characters to the saving body, all of it in the main clause, no exception added** — so it does
not collide with the §3.3 constraint I imposed on the cross-reference.

---

## 3. F4 and F5: the ruling I reverse, and the specification I withdraw

### 3.1 The premise did fail, and the reviewer found the case

My 01:32 ruling was that Edit 1's exception must name M 2's duty **alone**, because *"Edit 1's deeming
addresses the Board that acts more than once; in that class R-6's deadline is decision-keyed and the
residual limb cannot reach it."* The test I set was whether any case exists in which the Board acts
more than once **and** a residual class obtains.

**It exists.** Request denied by operation of M 2 on 6 May with no Board act; the Board, working its
backlog, actually acts on 20 June and again on 10 July. **The Board has acted more than once and class
1 obtains** — on revision 8's wording and on revision 9's alike, because the denial happened without a
prior act and a later act does not unmake that. In that case the residual limb measures R-6's deadline
**from the Board's act**, which is precisely what Edit 1's deeming reaches. **So the exception is
operative, not surplusage, and the *Forst* reasoning I gave for omitting it does not apply.**

### 3.2 But the cure the reviewer recommends is right for a reason they did not give, and the reason matters

Their framing is that two deemings then fix *"different dates — 6 May and 20 June — with no priority
rule."* **I do not think they can fix different dates, and the reason is structural rather than
fortunate.**

**Both of 164-7's deeming predicates are no-act predicates.** Limb 1 fires on a denial by operation of
M 2's sentence, which is itself predicated on *"the Board does not act upon the request within 30 days
after that notice is filed."* Limb 2 fires *"where the Board does not act upon a request … within the
period allowed by this section for acting upon it."* And 164-7 deems the act *"on the date of that
denial or, as the case may be, on the day after the expiration of that period."*

> **So in every case where both deemings operate, the date 164-7 deems necessarily precedes any real
> act of the Board upon the same request — because the deeming's own trigger is the absence of such an
> act up to that date. Edit 1 selects the date on which the Board *first* acts. A deemed act is an act
> for Edit 1's purposes, because 164-7's confinement clause makes the deeming operate for every
> provision measuring a period from the Board's acting, and Edit 1's sentence is such a provision.
> Edit 1 therefore selects 164-7's deemed date. The two agree by construction.**

**That is why adding R-6's duty to Edit 1's exception moves no date**, which was the condition I set
on myself at §3.3 and the only reason I had for hesitating. All four counts are in `verify_r72.py`.

**One wrinkle that is the drafter's, not mine, and I am naming it rather than fixing it.** 164-7 deems
the Board *"to act upon the request, and to **last** act upon it"* on the deemed date. A real act on 20
June is then an act **after** the deemed last act. That is a conflict inside 164-7's own words, not
between the two patches, and it is **F4's residue after my cure**. Routed.

### 3.3 The symmetry, stated precisely, because "byte-identical" has been claimed falsely three times on this bill

- **The saving bodies must be byte-identical.** After revision 9 they are **not** — Edit 1's carries
  the three duty families and 164-7's does not. **This is the one thing revision 9 asks of MOO-164.**
- **The two exceptions can never be byte-identical**, and claiming it would be the fourth false claim
  of its kind. Each must locate the other subsection: Edit 1 sits in subsection A and says *"under
  subsection M"* and *"in this subsection"*; 164-7 sits in subsection M and says *"under this
  subsection"* and *"in subsection A"*. **After revision 9 they differ in those two locators and in
  nothing else**, and `verify_r72.py` proves it by substituting the locators and asserting equality.

### 3.4 My three cross-reference requirements are withdrawn. Here are four

The reviewer's answer to target 3 was: no, the three are not sufficient, and requirements 1 and 3
cannot both be met. **I accept all of it, including the part that says requirement 1 misdescribed my
own Edit 1.** Edit 1's deeming is not confined to the multi-act case; it operates wherever a period is
measured from the Board's acting, and a signpost saying it *"governs the case where the Board acts more
than once"* would narrow it by implication — a substantive amendment in a signpost's clothes. That was
my error and it is withdrawn.

> **The specification, replacing §3.3's three requirements:**
>
> 1. **Characterise neither deeming's scope.** No *"governs the case where…"*. Nothing that could be
>    read as confining either sentence to a class.
> 2. **Make them cumulative by supplying the one fact that makes them cumulative**: that a date on
>    which the Board is deemed under subdivision M 2 to act upon a request is a date on which the
>    Board acts upon it for the purposes of subsection A's deeming. On §3.2 that states what both
>    texts already produce, so it resolves no priority and chooses no date.
> 3. **Move no date and add no exception.** Now achievable, because requirement 1 is gone and the
>    exceptions are symmetric.
> 4. **If it cannot be drafted without resolving a priority or touching an exception, that is a
>    finding and it comes back to me.** Unchanged, and it is how this specification arrived.

**It goes in 164-7, not in Edit 1** — subsection A comes first, so the later sentence refers back
without a forward reference. Unchanged from 01:32.

---

## 4. F6 and F3 are one gap, it is bigger than either finding states, and Edit 4 closes it

### 4.1 What the two findings share

F6 says R-6's chapeau — *"Where the Board's **action** upon a request **determines** a member's final
qualifying retirement date under this definition"* — is false where the definition's **expiry
sentence** fixes her date, because there the date is fixed by the expiry of a period
*"notwithstanding any other provision of this definition"* and not by any action. F3 says class 2
reaches a request 164-7 does not deem. **Both are about the same hole: a member whose date is fixed by
the Board's not acting.**

### 4.2 Two corrections to the findings, and both widen the gap

**F6's class is misidentified, and the correct class is larger.** The expiry sentence applies to *"a
request **the filing of which tolled the running of the member's final qualifying retirement date under
subsection M**"* — that is a request that tolls under subsection M, not a request under the definition
as F6's scenario has it. **And 164-7's no-act limb is confined on its face to *"a request under the
definition of 'final qualifying retirement date' in subsection A"*.** So in the expiry sentence's own
class, 164-7 does not deem an act at all.

**F3's direction is wrong, and the truth is worse.** F3 reasons that class 2 obtains, R-6 is engaged,
and the duty is left with an unascertainable deadline. But in a no-act case there is no action, real or
deemed, so **R-6's chapeau is false and R-6 is not engaged at all.** There is no stranded duty, because
there is no duty.

> **The gap, stated once: a member whose final qualifying retirement date is fixed by the expiry
> sentence acquires a statutory retirement date by operation of law and the bill requires nobody to
> tell her what it is. No notice, no decision, no statement, and — because subdivision D 1's lateness
> extension reaches only a notice required by reason of the Board's *action* — no remedy either.**

That is the harm MOO-209's F1 identified in a different provision, and it is the reason MOO-164 took
route (c). It is in this patch's territory because it is the second half of the question this issue
exists to answer: what happens to the member's own clocks while the Board is late.

### 4.3 Edit 4

Inserted immediately after the expiry sentence and immediately before R-6:

> *"**Where the member's final qualifying retirement date is determined by the preceding sentence, the
> Board shall give the member written notice of that date no later than 15 days after the expiration of
> the period for acting upon the request referred to in that sentence.**"*

**+268 characters. Five properties, all counted:**

1. **It widens no chapeau.** I drafted the chapeau widening the reviewer suggested and dropped it: R-6's
   chapeau governs both a duty to *state the date in its decision* and the notice backstop, and in a
   no-act case there is no decision to state it in, so widening the chapeau puts the Board in breach of
   the first branch in order to engage the second. A separate sentence has no such collision.
2. **It contains no deeming and no cross-reference** — no *"subsection"*, no *"subdivision"*, no
   *"deemed"*. So it is fully operative applied alone, and it needs neither patch's deeming to work.
   **It is the only edit in this patch that does not depend on the joint landing.**
3. **It is 164-4-proof.** It does not repeat the period formula — *"the period for acting upon the
   request referred to in that sentence"* — so MOO-164's re-cut of *"the period this definition allows"*
   to *"the period allowed by this section"* cannot strand it, and F14's register point cannot bite it.
4. **R-7's referent does not move.** Edit 4 is inserted **before** R-6, so R-7's *"a decision or notice
   required by the preceding sentence"* still points at R-6. Asserted at a new insertion point that no
   earlier pass had to check, which is MOO-215's N4 re-run.
5. **It is fiscally inert on the D 1 channel, and that is a counted claim, not an assumption.**
   D 1 extends the member's date for *"any notice of a date required by that definition **upon**"* — or,
   after 164-5, *"**by reason of**"* — *"the Board's **action** upon a request"*. Edit 4's notice is
   required by reason of the Board's **not** acting. **So no extension attaches, on either wording.**

**And the consequence of property 5, disclosed rather than buried: Edit 4 gives her the information and
not the time.** If the Board is late with the Edit 4 notice she has no extension — only the
reviewability of a failure to act within a required period that store revision 61 supplies. **Attaching
a D 1 extension to the Edit 4 notice is a policy choice with a price, and it is the first question in
the fiscal ask at §5. I have not taken it and I have not carded it.**

---

## 5. F8: the ground is withdrawn, and the fiscal issue is opened

**My §2.6 ground was:** *"The 12-month aggregate cap is unmoved, so there is nothing to re-price."*
**It is withdrawn.** The reviewer's test is correct and the error is a category error of mine: the cap
is a **bound per member**, and what drives cost in MOO-163 is a **population** against a fixed
$3,000,000 pool. An unmoved per-member cap says nothing about how many members reach it.

**And my own trigger fired on its own terms.** §2.6 said the limb re-opens MOO-163 and the declined
F-6 cap *"if the bounded pass widens the limb beyond the two named classes."* F1, F2 and F3 each widen
it, on three independent grounds. **I wrote the trigger, the pass met it, and I am honouring it.**

**What I accept and what I do not.** I accept that the screen **cannot be performed** on the inputs
that exist: no register in this project carries a Board no-act rate or a rate at which funded members
file later-date requests, so *"$0 on this limb"* was an unpriced assertion. I accept their scoping —
the exposure is in **class 2**, which §2.6 did not discuss, and class 1 is quadratic in a small number
and negligible. I note with them that the channel is **probably immaterial** at a plausible no-act
rate. **The finding is that the ground was wrong, not that the figure is wrong, and that distinction is
why this does not disturb the board's 120 days or the declined F-6 cap.**

**Routed, not assumed:** a child issue to the Fiscal & Impact Modeler with four questions — the two
missing inputs; whether MOO-163's $0 and MOO-170's $204,000 bound are silent on this channel rather
than covering it; whether Edit 4's §4.3 property-5 neutrality holds on their model; and the price of
attaching a D 1 extension to the Edit 4 notice. **F12 feeds it:** the D 1 channel opens whether or not
164-5 lands, so their scoping must not be conditioned on it.

**Nothing re-opens on my own motion.** MOO-163 and the F-6 cap re-open **if** the modeller comes back
non-zero, on the same footing as the MOO-49 trigger. **The board's 120 days are not reopened and
nothing in this document bears on the figure.**

---

## 6. Four things found on my own side of the line

### 6.1 "No word of the bill is deleted" is false, and has been since revision 5

I wrote a check to prove the claim and the check failed. **Edit 2 strikes three words.** Card (g)'s
re-key replaces *"no later than 15 days after it **acts upon** the request"* with *"…after it **gives
its decision upon** the request."* Edits 1, 3 and 4 are pure insertions — removing the inserted block
recovers each FIND exactly, and `verify_r72.py` asserts that for all three. Edit 2 does not.

**Where the claim came from.** It was true at revision 3, when the patch was Edit 1 alone and Edit 2
had been dropped on pass 17's F-1. Edit 2 came back at revision 5 as card (g) and the claim came with
it, unexamined, into 00:36 and again into 01:32. **And the revision-8 kit's own check was mislabelled**
— it was headed *"no word of the bill is deleted by Edit 2"* but asserted only that revision 6's text
survives inside revision 8, which is a different proposition. **The text is right: the deletion is the
board's own decision of 13:13 on 12 October 2026. The claim about the text was wrong, and a verifier
label was doing work a verifier check was not.**

### 6.2 F9's "harmless" is withdrawn, and the joint landing is the answer

Standalone, M 2's deemed-denial sentence is live in the base, so class 1 **does** obtain and the
residual limb **does** engage R-6's duty with a deadline that can never arrive where the Board never
acts. That is not *"the same position as the base."* **It is a reason the joint landing is mandatory
rather than preferable, and the joint landing is decided.** Edit 4 is unaffected — §4.3 property 2.

### 6.3 F12 — the second of my two ordering reasons is withdrawn

D 1's **pre-164-5** descriptor already tracks R-6's chapeau nearly word for word, so the channel does
not depend on 164-5. **§2.5's second reason is withdrawn; the first stands; the joint landing makes the
constraint moot in any case.** It matters to §5's scoping and nowhere else.

### 6.4 F15 and F16 — taken

The *"denied"* count is **two** others, not three; the conclusion it supported is unaffected. The §2.3
table's single no-act row is wrong for two classes and is **superseded by §4 of this document**, not
repaired — a table that needs three rows to be true should not survive into a briefing as one.

---

## 7. Verification

`moo141-rev72/verify_r72.py`, run against the body read **from the store** at document revision
`368f5e41`. **ALL CHECKS PASS.**

| | |
|---|---|
| Anchors | **4 at exactly 1 in §1.** Whole-document: E1 **2** (§5's sweep), E2 1, E3 1, E4 1 |
| §1 | 134,012, sha256 `83a10b74950b5272…` — **asserted equal to revision 71** |
| Patch | **+1,716** in §1 and **+1,716** whole-document |
| Per edit | 1 **+1,116**, 2 **+317**, 3 **+15**, 4 **+268** |
| Markup | `<u>` 62/62 in §1; balance 0 in the combined text |
| `first acts upon` | 2 → **3** |
| Combined | MOO-164 +3,375 (re-derived at a base they had not seen) + 1,716 = **+5,091**, **order-independent and byte-identical in either order** |
| MOO-164's 13 anchors | **all 1 at revision 72, and all still 1 after revision 9** |
| Deliberately failing-later | the two saving bodies read **(1, 1)** in the combined text today and **must read (2, 0)** once MOO-164 takes the three duty families |

**Revision 8's defective class-1 wording is kept in the kit as a live assertion at 0**, so F1's defect
stays visible in the record rather than being quietly fixed.

### 7.1 For whoever applies

1. **Four anchors now, not three.** Resolve all of them **within §1** and require a §1 count of
   exactly 1. **A whole-document count is not a valid uniqueness test for Edit 1.**
2. **Edit 2 must be applied in the same cut as Edit 1.** Unchanged from 00:36: Edit 1's exception
   describes M 2's duty by words that resolve twice in §1 until Edit 2 consumes the second.
3. **Edit 4 is the exception to the joint landing in one direction only** — it is fully operative alone
   — but it ships with the rest.
4. **Re-verify at the base as it stands at the moment of application.** The base has moved **ten**
   times under this item; four of those moves rewrote a provision this patch reaches without an anchor
   moving, and one killed an anchor outright.

---

## 8. What is routed, and to whom

**To the Drafting Specialist, as part of the joint cut:**

1. **164-7's saving must take Edit 1's three duty families, byte for byte.** F7 scopes the exposure to
   Edit 1 alone, so the words are inoperative in 164-7 — **byte-identity of the two saving bodies is
   what they buy**, and it is worth more than two spare phrases cost. **If you judge the divergence
   safer than the surplusage, that is a finding and it comes back to me.**
2. **The cross-reference, to the four-requirement specification at §3.4.**
3. **F4's residue (§3.2):** 164-7 deems the Board to *"last act"* on the deemed date, and a real act
   can follow it.
4. **F11**, with one new coupling: **Edit 1 now uses your R-6 descriptor verbatim**, so if you re-cut
   it on F11, Edit 1's exception moves with it in the same cut.
5. **F3's 164-7 half and F13** — your calls on your own grounds. **Neither is load-bearing for this
   patch any more**: Edit 4 closes the harm without widening 164-7's no-act limb.

**To the Statutory Researcher:** F2's register question — *decision* against *determination* in R-6's
deadline. **If *determination* is right, it changes the board's decided text and comes back to the
board, not to me.** And F13.

**To the Fiscal & Impact Modeler:** §5, as a child issue of this one.

**To the Editor, for the memo's risk section:** F1 and F2 **as cured** — the drafting history is the
risk disclosure, not the current text; **F4/F5 as the live construction question**; **§4.2's gap and
Edit 4**; and **§5's unpriced channel**. **F6/F3's gap is the one new memo item.**

**To the Stakeholder Analyst:** the reviewer is right that the **state agency from whose appropriation
an amount was paid on a member's behalf** has express standing in §1 and is the litigant in F1's
scenario. It should be on the map. **Note that F1's cure removes that scenario from the patch** — the
standing point survives it and the fiscal consequence does not.

---

## 9. Where this stands

**Revision 9 is cut, verified and unapplied. Nothing is applied to the store.**

| Gate | Issue | What clears it |
|---|---|---|
| 1 | **MOO-164** | The *"acts upon"* cut, carrying F-9, the §3.4 cross-reference, and §8's five items |
| 2 | **MOO-197** | Store revision 66's four edits — F1's Rule 2A:2 cure and the rest |
| 3 | **new** | One bounded pass over revision 9's new text — Edit 4, §3.2's structural claim, and the §3.4 specification. **Nothing in revision 9 has been read adversarially: MOO-215 named the defects and I drafted the cures, which is exactly the condition that made MOO-214 necessary** |
| 4 | whoever applies | §7.1 |

**No card to the board.** Nothing in revision 9 moves a figure the board decided, reverses an answer it
gave, or puts a question it has not been asked. The two items that touch its answers are **disclosed
and unchanged**: card (g)'s first limb survives character for character, and card (k-ii)'s 120 days are
untouched.

**Internal working draft material. Not a DLS bill. Not reviewed or cleared by counsel. Pre-decisional.**
