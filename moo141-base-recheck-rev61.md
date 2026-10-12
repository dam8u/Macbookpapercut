# MOO-141 — base re-check at store revision 61, and two findings for gate 4

**Policy Director, 12 October 2026.** Written because MOO-162 went `done` and the issue woke with no
first-class blocker left on it, while **four of its four gates to application are open**. This records
what I verified against the live bill text today, the two findings that came out of it, and the gates
re-stated as blocker edges rather than as prose in a comment.

**Internal working draft material. Not a DLS bill. Not reviewed by counsel. Pre-decisional.**

---

## 1. Headline

**The base has moved a seventh time, and it moved inside all three provisions this patch amends.
All three FIND anchors still resolve exactly once.** That is the fourth time in this item's life that
a provision the patch reaches has been rewritten without an anchor moving, and it is the whole case
for gate 3.

**Nothing in the patch is invalidated.** Two things need to go into work that is already live:
one named target for gate 4's bounded re-review (§4), and one confirmation for MOO-164 (§5).

---

## 2. What I verified, directly from the document store

| | Value |
|---|---|
| `bill-text-s8` document revision | **76** (`3efccfe2`) |
| Store revision | **61** |
| Whole document | **271,611** characters |
| Enacted text (§ 51.1-142.2 + § 51.1-142.4) | **112,554** characters |
| Base the patch was last verified against | store revision 60, 250,229 characters whole / 114,833 enacted |

**The whole document grew by 21,382 characters while the enacted text shrank by 2,279.** The growth is
store revision 61's own record; the shrinkage is store revision 61 curing its fatal finding **by deleting
words**, which is what its own §0.0-61 says it did. **The two move in opposite directions, so document
size is not a proxy for whether the bill moved** — which is the same lesson as the anchors.

### 2.1 The three anchors, counted in the whole 271,611-character document

| Edit | FIND | Count |
|---|---|---|
| **1** | `…is extended by three days.</u>` | **1** |
| **2** | `it shall give the member written notice of that date no later than 15 days after it acts upon the request.` | **1** |
| **3** | `retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request` | **1** |

### 2.2 The `act upon` family in the enacted text at store revision 61

| Phrase | Count |
|---|---|
| `acts upon` | **8** |
| `act upon` | **7** |
| `acting upon` | **2** |
| `action upon` | **2** |
| `last acts upon` | **1** |
| `first acts upon` | **2** |

`acts upon` at 8 and `last acts upon` at 1 agree with revision 5's §4.1 pre-application figures.
**Both of G 4's express *"first"*s are intact**, which is the condition on which the withdrawn Edit 2
of revision 2 stays withdrawn.

---

## 3. What store revision 61 did, and why it matters to gate 3

Its own heading: *"Thirteen substitutions in subdivisions G 4, D 1 and M 2."* **Those are the three
provisions this patch reaches, and not one anchor moved.**

It also did three things that bear on the patch's reasoning:

1. **M 2's failure limb is widened** to reach *"a failure of the Board to make a determination, to give
   a notice, **or to make a payment** within a period required by this section"*, and a failure to state
   a required matter in a certification or notice.
2. **The reconsideration class is narrowed** from *"other person to whom this section requires a notice
   to be given"* to the rejected claimant and the paying employer.
3. **The 90-day redetermination in the death case now runs from the date the Board learns of the
   death.** Checked: that period is not measured from the Board's acting upon a request, so **Edit 1
   does not reach it.** Null result, stated so nobody re-derives it.

---

## 4. Finding 1 — Edit 1's saving enumerates duties, and revision 61 added one it does not name

**This is a named target for gate 4's bounded re-review. I am not drafting it and it does not reopen
the figure.**

Edit 1's saving sentence reads:

> Nothing in the preceding sentence determines the date by which the Board is required **to act upon a
> request, to make a determination, or to give a notice or a decision**, or whether the Board has
> performed such a duty within a period required by this section.

**It is a closed list of three duties.** Store revision 61 made a **failure to make a payment** within
a required period expressly reviewable under M 2, and M 2's deeming sentence already treats a
*crediting of service credit* and a *recertification* as determinations.

### 4.1 The null result first

I checked every payment and refund deadline in the enacted text. They run from **the recertification**,
**the determination taking effect**, **the crediting of the service credit**, and **the receipt of the
notice of cancellation** — none of them from the Board's acting upon a request. **So on the face of it
the omission is harmless, and I would have left it there but for one clause.**

### 4.2 The one clause

> Where a determination under subdivision 2 or 3 that has taken effect is reversed or modified on
> reconsideration under subsection M or on judicial review, the Board shall restore or credit service
> credit …, shall recertify and settle it accordingly, **no later than 60 days after the reversal or
> modification** …

**A reversal on reconsideration is the Board's act upon a request for reconsideration.** Edit 1's
trigger is not keyed to a form of words; it reaches any period *"measured from the Board's acting, or
last acting, upon a request."* If it reaches this one, the 60 days is deemed to run from the Board's
**first** act on the request — and the saving does not name a duty to restore, to credit, to recertify
or to settle, nor a duty to pay.

**Failure scenario, on the ordinary facts used throughout this item.** First act day 7, reconsideration
decided day 85. The 60 days expires **day 67**. **The Board is in breach of a 60-day duty 18 days
before the reversal that triggered it exists** — and under revision 61 that failure is reviewable, with
its own 30-day clock. **This is pass 17's F-2 in a provision neither pass looked at.**

**And the same clause would then measure its 60 days from two different events depending on the limb** —
the deemed first act where the reversal is on reconsideration, the judgment where it is on judicial
review, because on judicial review there is no act of the Board upon a request for the rule to bite on.

**Two shapes of answer, and the re-reviewer should say which:** either the trigger does not reach a
period measured from *"the reversal or modification"* at all — in which case say so and the finding
closes — or the saving's list needs the duties revision 61 made reviewable. **The second is a drafting
change and it is the drafter's, not mine.**

---

## 5. Finding 2 — the live D 1 descriptor reads *"first required"*, which is MOO-164's F-9

Edit 2's §4.2 rests on the condition precedent keeping **subdivision D 1's reference alive**. At store
revision 61 D 1 reads:

> The member shall file the notice of retirement required by § 51.1-153 … no later than 30 days after
> the date on which the Board gives the member the written statement of the member's earliest qualifying
> retirement date and final qualifying retirement date **first required** by the definition of *"final
> qualifying retirement date"* in subsection A.

**On its face *"first required"* selects the opening statement and not the backstop notice** — which is
the narrow reading F-9 is about. **That is gate 1, it is live at MOO-164, and the live text favours the
narrow side.** Recorded, not decided: MOO-164 owns it and deciding it here is how a section ends up with
two answers to one question.

---

## 6. Gate 4's cap limb closed while I was writing this

MOO-170's bounded addendum answers the chaining question: **the $204,000 bound is analytic, survives
chaining unchanged, stays lapse rather than cost, and the central estimate is $0 at every chain length
including an unbounded one.** Displacement rises about 21× — 0.14 to 2.80 members over 48 months — and
stays inside the resolution of the inputs by a narrower margin than at MOO-163. **MOO-170 is `done`.**

**On that input F-6's cap stays declined** — `moo179-cap-decision.md`, committed at `789eb89`. The one
thing I would have asked of it is already answered there: the bound's ground is that it quantifies over
any vector of ordering dates, so **it is figure-independent as well as length-independent**, and the
board's move from 30 days to 120 does not revive the cap. **Trigger 2 is untouched — if MOO-49's clause
(vi) lands broad, the cap and MOO-163 re-open together.**

**So gate 4 is now only the bounded re-review of revision 6**, and §4 above is the second named target
for it, alongside Edit 3's figure and the broken 30-day identity.

---

## 7. The four gates, now carried as blocker edges

Prose in a comment is not a wake signal. MOO-141 is `blocked` on all four:

| Gate | Issue | What clears it |
|---|---|---|
| **1** | **MOO-164** | The *"acts upon"* / act-versus-notice decision, carrying **F-9** — §5 above is evidence for it |
| **2** | **MOO-42** | The no-decision residual: §7 item 124's deemed denial, or pass 18's card C if item 124 is declined |
| **3** | **MOO-176** | Revision 6 at 120 days, re-cut against store revision 61 — §2 and §3 above are its base |
| **4** | **MOO-176** | Revision 6 passes **one** bounded re-review — Edit 3's figure, the broken 30-day identity, and §4 above. **Its cap limb is closed**: §6 |

**Gate 3's own instruction is unchanged and is now evidenced four times over: whoever applies this
re-verifies all three anchors, re-splices every reproduction and re-runs every count against the base
as it stands at that moment.** An anchor that still resolves is not evidence that anything around it
is current — store revision 61 is the fourth proof of that.

---

## 8. What I did not do

- **I did not draft anything.** §4 is a target for review and §5 belongs to MOO-164.
- **I did not decide F-6's cap here.** It is MOO-179's, it is taken there on MOO-170's price, and §6
  records it rather than re-deciding it.
- **I did not reopen Edit 3's figure.** The board took 120 days at 14:15 and that answer governs.
- **I did not touch the store.** Nothing in the patch is applied, and nothing here authorises applying it.
