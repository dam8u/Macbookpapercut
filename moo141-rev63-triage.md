# MOO-141 — store revision 63 triage: gate 2's cure, its non-existent fallback, and who bears the Board's delay

**Policy Director. 12 October 2026. Internal working draft material. Not a DLS bill. Not reviewed or
cleared by counsel. Pre-decisional.**

**Why this document exists.** MOO-141 woke on the Drafting Specialist's comment reporting that gate 2's
cure is enacted as store revision 63 and that gate 2's named fallback does not exist. All three of their
claims check out against the live text. This document records the verification, the one correction it
forces in a document of mine, and **three findings of my own that none of the four comments on this
issue carries** — including that the recommended cure for the residual they raised buys one limb of
three and spends a date movement to do it.

**What I did not do.** I did not draft, I did not touch the store, I did not reopen the board's
120 days, and I did not put a card to the board. §6 says why in each case.

---

## 1. The Drafting Specialist's three claims — all three confirmed against the live text

Fetched the live body, not a reproduction. `bill-text-s8` is at **document revision
`37a5426c-a7fd-4454-917a-1790a4dcdd1b`, document revision number 79, store revision 63, 320,665
characters.** That is the revision id and the character count MOO-190's brief states, so the brief and
the body agree.

**Claim 1 — the two sentences are enacted in subdivision M 2.** Confirmed, spliced from the live body:

> Where the Board does not act upon a request for reconsideration within the 90 days allowed by this
> subsection, the person who filed the request may file with the Board written notice that the period
> has expired. Where the Board does not act upon the request within 30 days after that notice is filed,
> the request is denied on the first day after the expiration of those 30 days, and that denial
> constitutes the final determination of the Board upon the reconsideration and a case decision as
> defined in § 2.2-4001 for the purposes of this subsection.

They sit immediately after *"The Board shall act upon a request for reconsideration within 90 days"* and
immediately before the tolling sentence. **One occurrence each in §1 and nothing else in the subsection
moved.**

**Claim 2 — *"the 90 days allowed by this subsection"* now reads 2 in §1.** Confirmed: **2**, both in
M 2, both referring to the same 90-day duty — one in the new first sentence, one in clause (ii) of the
tolling sentence. So **card (j), if it re-keys that phrase, moves the new sentence with it.** One edit
either way, as the Drafting Specialist says; MOO-164 owns it and no action of mine is needed.

**Claim 3 — pass 18 carries no card C.** Confirmed by reading the document, not by inference. Pass 18 is
**MOO-156**, `done`; its only document is `moo156-pass18-review`, **57,166 characters**. A regex for a
lettered card in any letter returns **zero matches**. *"§ 2.2-4021"* does not appear. *"Article 5"*
appears **twice**, both times as § 2.2-4025 et seq. in the venue lines of S18-2 and S18-3 — the
judicial-review article M 2 already cites, not this residual. The card this issue sent to pass 18 was
**(l)**. This issue's own **card (c)** is G 2's undefined *"pending"*, a different defect.

**My error, stated plainly.** `moo141-base-recheck-rev61` §7 offered gate 2 two cures. There was one.
Corrected at that document's new **§7.1**, which also carries the narrow lesson: **a named fallback is
only a gate if someone has resolved the name.** I did not resolve it when I wrote the row.

---

## 2. The base, the anchors, and one new instruction for whoever applies

**The eighth base.** §1 — on the store's own convention, `## 1. The bill` to `## 2. Section-by-section`
— is **121,439 characters**, against 117,980 at store revision 61. **+3,459 over two store revisions**,
of which revision 63's two sentences are about 540. The rest is revision 62. Reported so the next
re-count has a figure to reconcile against rather than a surprise.

**All three anchors still resolve exactly once in §1.**

| Edit | §1 | Whole document |
|---|---|---|
| **1** — the pendency / tolling re-key | **1** | 1 |
| **2** — the 15-day date-notice backstop | **1** | 1 |
| **3** — the D 4 / D 5 retention | **1** | **2** |

**That last cell is new and it is a trap.** Edit 3's FIND string now appears **twice in the document** —
once in §1 at the operative sentence, and once at document offset 226,409, inside **§5, the
cross-reference check**, where a sweep quoted it. **An applier who resolves Edit 3 over the whole
document gets two hits and will either stop, thinking the anchor has gone ambiguous, or patch the
record.** Neither is what gate 3 asks for.

> **Gate 3 instruction, refined: resolve all three anchors *within §1*, not over the document, and
> require a §1 count of exactly 1. A whole-document count is no longer a valid uniqueness test for
> Edit 3.**

**Counts in §1 at revision 63**, for the next reconciliation: `acts upon` **8**, `act upon` **9**,
`acting upon` **2**, `action upon` **2**, `last acts upon` **1**, `first acts upon` **2**, `pending`
**9**. `act upon` moved **7 → 9** and the two new sentences each contain it, so the delta is fully
accounted for. Both of G 4's express *"first"*s are intact, which is the standing condition on which
revision 2's withdrawn G 4 edit stays withdrawn. `<u>` balance **60/60 in §1 and 61/61 whole-document**.

---

## 3. Finding 1 — G 4 and M 2 now take **opposite** positions on who bears the Board's delay, and the words that look like a conforming amendment are not one

This is the sharpest form this issue's subject has taken, and it is the reason the issue is still open.

Both provisions cap at **120 days**. They do opposite things with Board delay. Both spliced from the
live body:

**Subdivision G 4** — the cap on non-running of the Board's own periods, as it reads after store
revision 62:

> …except that the aggregate of all such non-running by reason of such requests and by reason of
> applications for a disability retirement allowance filed after the first such application shall not
> exceed 120 days, **and a failure of the Board to act upon such a request within the period allowed to
> it for acting upon the request shall not extend that aggregate.**

**Subdivision M 2, clause (ii)** — the cap on tolling of the member's own periods:

> …and (ii) the aggregate of all tolling under this subsection shall not exceed 120 days, **excluding
> any period after the expiration of the 90 days allowed by this subsection and before the Board acts
> upon the request.**

**G 4 says Board delay does not extend the aggregate. M 2 says Board delay is taken out of the
aggregate — which is to say it extends it without limit.** Same bill, same figure, adjacent provisions,
opposite rules, and the divergence is express on both faces rather than inferred.

### Why this is useful, and the trap in it

**The useful half.** My 17:42 comment paired the Drafting Specialist's §6.2(c) (let the member's clock
stop for *longer*) against counsel's M8 (make it *run again* once the Board's 90 days expire) and
recorded them as one question with two live expert answers and no priced option. **The bill now answers
that question for the Board's own clocks, and answers it against the Board.** G 4's sentence is in-bill
precedent for M8's direction. That matters: M8 stops being a novel policy proposal and becomes the
extension of a rule the drafters have already adopted once.

**The trap, and it is mine to name because both halves of the argument are in front of me.** The
symmetry is in the words and not in the incidence. **In G 4 the cap protects the Board's clocks against
the member's filings, so "delay does not extend the aggregate" makes the Board bear its own delay. In
M 2 the cap limits the member's tolling, so the identical words make the *member* bear the Board's
delay.** Identical text, opposite party burdened.

> **So giving M 2 clause (ii) G 4's words is not a conforming amendment. It is M8's policy choice,
> wearing a conforming amendment's clothes.** It is still very possibly the right choice. It is not a
> repair, and it must not be written up or carded as one.

This is the same discipline as card (g), where the re-key was defensible precisely *because* *"gives a
decision"* was the formula the very next sentence already used. Here the formula is adjacent but its
effect reverses. **Card (g) was a clarification of an unworkable reading. This would be a choice against
the member.** The distinction is the whole of the difference and it survives into the memo.

---

## 4. Finding 2 — revision 63 creates a request that is **disposed of and permanently un-acted-upon**, and three clocks have no backstop

The Drafting Specialist raised this and §7 item 130 states it. I verified it, and the enumeration moves
it on in two ways.

**The mechanism.** The deemed denial disposes of the request but is **not** an act of the Board — and
deliberately not, because that verb is MOO-164's. So the request is simultaneously **finally determined**
and, for the purposes of every clock keyed to the Board's act, **still not acted upon.** M 2 clause (ii)
then excludes from its cap *"any period … before the Board acts upon the request"*, a window that on
these facts never closes.

**What I did that item 130 does not.** I enumerated **all 21** occurrences of *"act(s) upon"*,
*"acting upon"* and *"action upon"* in §1 and sorted the clocks keyed to the Board's act into protected
and unprotected.

### Protected

- **G 4's pendency** (occurrences 12 and 13) — the Board first acting. Never acting leaves pendency
  open, **but revision 62's anti-delay clause caps the aggregate regardless**, so the exposure is
  closed. G 4 is protected and M 2 is not, which is finding 1 restated from the other end.

### Protected, **probably** — and this is a question, not an answer

- **The member's final qualifying retirement date.** Subsection A's definition carries an express
  late-Board backstop (occurrences 3 and 4): where the Board does not act within the period the
  definition allows, the FQRD **is** the first day of the second month following the month that period
  expired, *"notwithstanding any other provision of this definition."* **But:** that *"notwithstanding"*
  is confined to **the definition**, and M 2 is not a provision of the definition; and the backstop
  fires only where *"the date that would otherwise apply **under this definition** is earlier than"* the
  reset date, so if M 2's tolling has already pushed the date out, the comparison may never be met.
  **Whether the backstop beats M 2's tolling is open.** I assert only that it is there and that it is
  unresolved.

> **This narrows both experts.** §6.2(c) and M8 both argue about the FQRD limb — the one limb that may
> already have a backstop. **Neither names the three limbs below, and those have no backstop anywhere.**

### Unprotected — three limbs, no backstop in the bill

1. **M 2's tolling of *"any period within which the member or applicant must act under this section or
   under subdivision B 4 f of § 51.1-142.2"*** (occurrence 17). Not the FQRD, so the definition's
   backstop cannot reach it even on its most generous reading.
2. **Edit 3's subdivision D 4 / D 5 filing-date retention** (occurrence 19). **This is the only one of
   the three with a third-party cost** — an indefinitely held queue position displaces other applicants,
   and under subsection B of § 51.1-142.2 displacement is the difference between the subsidised and the
   standard cost.
3. **M 2's duty to act upon the application no later than 15 days after it acts upon the request**
   (occurrences 20 and 21). **A duty that never falls due.** Item 130 does not name this one. It is the
   mirror image of pass 17's F-2 — there a duty fell due before its trigger existed; here it never falls
   due at all.

### The board's 120 days is not implicated, and the figure does not reopen

**Limb 2's unboundedness pre-exists Edit 3.** The base already read *"retains its filing date … until
the Board acts upon the request."* Edit 3 adds 120 days to an endpoint that was already unbounded in the
never-acting case. **The patch does not create this exposure and lengthening the figure from 30 to 120
days does not worsen it.** Stated expressly so that nobody reads finding 2 as a reason to revisit the
board's 14:15 answer. It is not one.

---

## 5. Finding 3 — the recommended cure buys **one limb of three**, and the complete cure is the one that waits on MOO-164

§7 item 130 offers three routes and recommends **(b)**: give M 2 clause (ii) G 4's words. I read clause
(ii) against the three limbs. **Route (b) does not reach limbs 2 or 3.**

Clause (ii) caps *"the aggregate of all **tolling** under this subsection."* The D 4 / D 5 retention is
**not tolling** — it is a separate sentence fixing a retention endpoint, beginning *"An application that
is the subject of a request for reconsideration under this subsection retains its filing date…"* The
15-day application duty is likewise not tolling. **Capping the tolling caps the tolling.**

| Route | Limb 1 — tolling | Limb 2 — the retention (the priced one) | Limb 3 — the 15-day duty | Moves a date? |
|---|---|---|---|---|
| **(a)** nothing | open | open | open | no |
| **(b)** G 4's words into clause (ii) — *the recommendation* | **cured** | **open** | **open** | **yes** |
| **(c)** deem the denial an act for these endpoints | **cured** | **cured** | **cured** | no |

**So the cheapest route spends the only date movement on the table and misses the only limb that has a
price.** Route (c) reaches all three and moves no figure — and the Drafting Specialist is right not to
draft it, because it decides *"acts upon"* and that is MOO-164's.

### The sequencing decision, which is mine, and I am taking it

> **MOO-164 takes this question first, with all three limbs in front of it. MOO-97's route (b) is held
> until MOO-164 lands — not declined, held.**

**Reasons.** Taking (b) first buys one limb of three, moves a date and therefore may move a figure, and
leaves the priced limb open — after which MOO-164 may well deliver route (c) and make (b) redundant.
Deciding it the other way round is how a section ends up with three answers to one question, which is
why (b), (c), (f), (h), (i) and (j) went to MOO-164 as one issue in the first place. **This is the same
call on the same ground, and limb 3 is new to the record, so MOO-164 cannot take it without being told.**

**Sequencing is mine** — the Drafting Specialist's §6.8 and my 13:21 disposition both put it there, and
item 130 routes the substance rather than taking it, which is correct. **No decision of theirs is
disturbed and no text changes on my say-so.**

---

## 6. What I decided, and what I did not

### Taken this heartbeat

1. **Gate 2's blocker edge is re-pointed from MOO-42 to MOO-190.** The cure is enacted, so gate 2 now
   waits on **review of the cure**, not on drafting it. MOO-42 is blocked on MOO-64, MOO-97 and MOO-190
   and will not reach `done` on this item's account, so the old edge was a dead wake path.
   **MOO-141's blockers are now MOO-164 and MOO-190, and both are live.** The stale `done` edge on
   MOO-176 is dropped in the same write.
2. **`moo141-base-recheck-rev61` is corrected** at the §7 table and at a new **§7.1**.
3. **Finding 3's sequencing decision**, §5. MOO-164 first, MOO-97's route (b) held.
4. **Gate 3's instruction is refined**, §2 — anchors resolve within §1, because Edit 3's whole-document
   count is now 2.

### Not taken, with the reason in each case

- **No card to the board.** Two reasons, and the second is new. **First**, as at 17:42: it would put a
  question with two live expert answers and no priced option. **Second**: the question now has in-bill
  precedent and three drafted routes, so when it does reach the board it should arrive as **a
  recommendation with a price**, not as an open question. Carding it now would spend the board's answer
  on the wrong form of the question.
- **The figure is not reopened.** §4's closing paragraph. Limb 2 pre-exists Edit 3.
- **Nothing is drafted.** Finding 1's trap is a reason to be careful about how a cure is justified, not
  a cure. Route (c)'s text is MOO-164's.
- **Card (j)'s coupling needs nothing from me.** The Drafting Specialist does it in the same cut and
  §1's recount confirms the premise — 2 occurrences, both in M 2.
- **No Fiscal & Impact Modeler issue, and one named trigger instead.** MOO-170's **$204,000** bound was
  released as analytic — it quantifies over any vector of ordering dates, hence figure- and
  length-independent. **An unbounded retention is not a longer figure; it is the absence of one**, so I
  do not assume the bound survives limb 2 uncured. **I also do not assert it fails.** The cure is cheap
  and the right order is cure first, re-price only if the cure is declined. **Trigger: if route (a) is
  taken — the residual left uncured — MOO-163 and the declined F-6 cap both re-open on limb 2, on the
  same footing as the existing MOO-49 trigger.** Recorded here rather than opened as an issue, so it is
  visible rather than silent.
- **No Stakeholder Analyst issue.** Unchanged from 13:21: nothing pending changes who is affected.

---

## 7. Where this issue stands

| Gate | Issue | State | What clears it |
|---|---|---|---|
| **1** | **MOO-164** | `blocked` | The *"acts upon"* / act-versus-notice decision, carrying **F-9** — **and now §5's three limbs** |
| **2** | **MOO-190** | `in_progress` | The bounded pass on store revision 63's two sentences. **Re-pointed from MOO-42 this heartbeat** |
| **3** | whoever applies | — | Re-verification against the base **as it stands at that moment**, with §2's refined instruction |
| **4** | — | **closed** | Revision 6 accepted at MOO-176; the cap limb closed at MOO-179 on MOO-170's price |

**The patch itself is unchanged: three edits, +698 characters, nothing applied to the store, and nothing
in this document authorises applying it.**

**Internal working draft material. Not a DLS bill. Not reviewed or cleared by counsel. Pre-decisional.**
