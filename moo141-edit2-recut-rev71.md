# MOO-141 — Edit 2 re-cut as revision 8, and the two patches land as one cut

**Policy Director. 13 October 2026. Internal working draft material. Not a Division of Legislative
Services bill. Not reviewed or cleared by counsel. Pre-decisional. Nothing is applied to the store
and nothing in this document authorises applying anything.**

Answering the Drafting Specialist's report of 01:20 on 13 October 2026 — the two items that came back
to this issue out of MOO-164 revision 7.

| | Item | Disposition |
|---|---|---|
| **1** | My Edit 2 makes R-6's notice duty turn on an event that never occurs in the deemed classes | **Accepted and cured in the text.** Edit 2 is re-cut as **revision 8**, +326 against +14 |
| **2** | The two savings are asymmetric again, and MOO-209's F9 wants a joint landing with a cross-reference | **The asymmetry is right and is now *required*, not merely defensible. The joint landing is decided.** The cross-reference is specified and assigned |

**Patch after this re-cut: three edits, +1,159 characters over enacted §1, no word of the bill
deleted.** Revision 6 was +847.

---

## 1. The base moved a tenth time, and every count here is taken at the base as it now stands

`bill-text-s8` is at **document revision 90, store revision 71, 484,408 characters**; enacted §1 is
**134,012** on the store's own convention, sha256 `83a10b74950b5272…`. The Drafting Specialist's
report was counted at store revision 70. **Three new anchors were not tested at revision 71 by
anyone before this document.**

| Edit | §1 | whole document |
|---|---|---|
| **1** — the pendency / tolling deeming, re-cut at revision 69 | **1** | 2 |
| **2** — R-6's notice-duty deadline | **1** | 1 |
| **3** — the D 4 / D 5 retention at 120 days | **1** | 1 |

**And the whole-document duplication has changed hands.** At store revisions 63, 64 and 69, **Edit
3's** FIND read 2 whole-document because §5's cross-reference check quoted it; today **Edit 1's**
FIND reads 2 for the same reason and Edit 3 reads 1. The rule that survives is the rule, not the
instance:

> **Resolve all three anchors within enacted §1 and require a §1 count of exactly 1. A
> whole-document count is not a valid uniqueness test for any of them, and which edit it breaks on
> changes between store revisions.**

**MOO-164's thirteen FINDs also all resolve exactly once at revision 71** — a base that cut has not
seen — and their published delta of **+3,375** re-derives exactly. Their kit is **lifted** into my
verifier rather than re-typed, so a divergence between the two kits is impossible rather than merely
unlikely.

**One new occurrence in the `act upon` family, checked and out of reach.** `acts upon` moved **8 → 9**
in §1 between revisions 69 and 71. The ninth is *"no later than 15 days after the Director of the
Department of Planning and Budget or his designee acts upon the Board's request under subdivision
3."* **The actor is not the Board.** Edit 1's deeming is confined to *"the Board's acting, or last
acting, upon a request"*, so it does not reach it, and neither does 164-7's. **Null result, counted,
not assumed.**

---

## 2. Item 1 — accepted, and cured in my provision

### 2.1 The defect, restated in one paragraph

164-7 deems the Board to act in two classes in which it has not acted: where a reconsideration
request is **denied by operation of law** under store revision 63's sentences, and where the Board
**does not act within the period allowed** on a request under the definition of *"final qualifying
retirement date."* MOO-209's F1 found that 164-7's own saving stopped that deeming from dating R-6's
notice duty, and the cure was to name R-6's duty in 164-7's express exception. **My Edit 2 then makes
the cure inert**, because it re-keys R-6's fifteen days to *the giving of a decision* and in both
deemed classes no decision is ever given. The duty has no start date, so **D 1's lateness extension
cannot fire and 164-8's replacement notice of retirement never becomes available.**

**The report is right, and the smallest cure is in my sentence.** Counted on the combined text in
`moo141-rev71/verify_r71.py`: with revision 6's Edit 2 the duty has **one** deadline and it is
decision-keyed only; with revision 8 it has a residual deadline that the deeming reaches.

### 2.2 The text — Edit 2, revision 8

**FIND** (1 in §1, 1 whole-document):

> it shall give the member written notice of that date no later than 15 days after it acts upon the
> request.

**REPLACE** (432 characters against the FIND's 106 — **+326**):

> it shall give the member written notice of that date no later than 15 days after it gives its
> decision upon the request, **except that where the request is denied otherwise than by a decision
> of the Board upon it, or where the period allowed by this section for acting upon the request
> expires without the Board's acting upon it, it shall give that notice no later than 15 days after
> the date on which the Board acts upon the request.**

**The first limb is revision 6's, character for character.** The board's answer of 13:13 on 12
October 2026 is untouched in the class the board was shown, and that is a counted assertion, not a
claim: the revision-6 text survives inside revision 8 exactly once, and the decision-keyed limb comes
first.

### 2.3 What it does, class by class

| Class | Before | Revision 6 | **Revision 8** |
|---|---|---|---|
| Board acts once and decides | notice due **act + 15**, trigger not yet determinable — card (g)'s defect | notice due **decision + 15** | **unchanged** |
| Board acts twice and decides (Edit 1's class) | as above | **decision + 15** | **unchanged** |
| Reconsideration **denied by operation of law** — no decision ever | no duty dated | **no duty dated** | notice due **deemed act + 15**, i.e. denial + 15 |
| Board **never acts** within the period allowed | no duty dated | **no duty dated** | notice due **deemed act + 15**, i.e. expiry + 1 + 15 |

**The residual limb is confined on its face to the two classes in which no decision upon the request
is ever given**, so it cannot reach the ordinary case and cannot reverse the board's answer.

### 2.4 Three formulas I drafted and rejected, and one I will not ask for

This is where the work was. The obvious cure is not safe.

1. ***"or, where the Board gives no decision upon the request, no later than 15 days after it acts
   upon the request."*** **Rejected.** At the moment of the act the Board cannot know whether it will
   ever give a decision, so the duty's deadline is **indeterminable ex ante and breached
   retrospectively** — which is card (g)'s own defect in a new place. The board's reason for
   answering card (g) as it did was that a duty must not fall due on a trigger that is not yet
   determinable.
2. **Keying the residual limb to the expiry of a period for *giving a decision*.** **Rejected on a
   counted ground.** For a request under the definition such a period exists — *"no later than 30
   days after the request is filed."* For a reconsideration under subsection M **none does**:
   MOO-209's F5 established that no provision fixes the giving of a decision on a reconsideration by
   any date. The limb would be **empty in the class that matters most**, which is the deemed denial.
3. ***"where the Board is deemed under subsection M to act upon the request."*** **Rejected.** It
   imports the other patch's words into mine, and if this patch ever lands alone it leaves a
   **reference to a deeming that does not exist.** F9 asks for a cross-reference between two
   deemings; it does not ask for one patch's operative date to be unavailable without the other.
4. **Widening 164-7's deeming to reach a *giving*.** **Not asked for, and I agree it should not
   happen.** Deeming a decision given when none has been given starts the member's own clocks
   without her knowledge, which is card (b)'s whole subject and the thing Decision 2 exists to
   prevent. **The Drafting Specialist's refusal is correct and I am recording agreement rather than
   leaving it as their unilateral line.**

**What the chosen formula buys.** It names its two classes expressly, so it is determinable. It
measures from *"the date on which the Board acts upon the request"*, which is exactly the date 164-7
deems and which 164-7's exception already lets the deeming date. **It contains no cross-reference to
any subsection and no reference to any deeming** — both asserted in the verifier — so the two patches
stay textually independent.

### 2.5 Standalone behaviour, and the only ordering rule this creates

**Applied without MOO-164, the residual limb is inert and harmless.** In its two classes there is no
date on which the Board acts, so no deadline is produced — the same position as the base, with no
dangling reference. **Applied with MOO-164, it is operative.** That is the property I wanted, and it
means revision 8 adds **no** new ordering constraint to the three already recorded:

- Edit 2 must be applied in the **same cut** as Edit 1, because Edit 1's exception descriptor
  resolves twice until Edit 2 consumes the occurrence in the definition. **Unchanged.**
- Application of this patch does not precede the MOO-164 cut carrying **F-9** (Edit 164-5).
  **Unchanged — and now load-bearing twice over**, see §2.6.
- **Order independence holds:** MOO-164 then MOO-141 is byte-identical to MOO-141 then MOO-164 on the
  combined text, at a **sixth** store base.

### 2.6 What the residual limb puts into motion, disclosed rather than buried

**It opens D 1's lateness channel in two classes where nothing opened it before.** D 1 extends the
member's final qualifying retirement date by the number of days by which a required statement or
notice is late. Under revision 6 the deemed classes had **no required time**, so there could be no
lateness and no extension. Under revision 8 there is one, so there can be.

**Three things about that, and they are the reason it is not a card.**

- **It reaches D 1 only on 164-5's broader descriptor** — *"any notice of a date required by that
  definition **by reason of** the Board's action upon a request"* — which is the F-9 reading already
  decided. Counted both ways: present once in the combined text, and the narrower pre-164-5
  descriptor is gone.
- **The outer bound does not move.** The definition's own cap — *"the aggregate of all extensions so
  excluded shall not exceed 12 months"* — is intact and unamended, and the limb cannot exceed it.
  **So revision 8 adds no new outer bound on the member's final qualifying retirement date; it adds a
  class in which the existing bound can be reached.**
- **It is not the windfall the board declined.** The board's card (g) reasoning was that D 1's
  extension riding on a duty that **could not have been performed** would be a windfall. In the
  deemed classes the duty **can** be performed: the Board knows the denial date and knows the date
  its period expired, and fifteen days from either is a performable deadline. **The extension is then
  the ordinary consequence of real lateness, which is what D 1 is for.**

**No card, no board answer, no figure** — the effect in the class the board decided is the effect it
decided, and this is a conforming repair of a defect created by the interaction of two unapplied
patches. **But the fiscal trigger is named rather than assumed:** I am **not** asserting $0 for this
limb on my own authority. MOO-163's $0 and MOO-170's $204,000 bound were released on inputs that did
not include a D 1 extension channel in the deemed classes. **Trigger: if the bounded pass at §5
widens the limb beyond the two named classes, or if the 12-month aggregate cap is amended by any
other item, MOO-163 and the declined F-6 cap re-open on this limb on the same footing as the MOO-49
trigger.** Recorded, visible, not opened — the cap is unmoved, so there is nothing to re-price today.

---

## 3. Item 2 — the asymmetry, and F9's joint landing

### 3.1 The asymmetry is not merely principled. After revision 8 it is required

The Drafting Specialist argues at their §17.3 that 164-7's exception naming two duties while Edit 1's
names one tracks a real difference. **I agree, and revision 8 gives the argument a harder form.**

Edit 1's deeming addresses the Board that **acts more than once** and fixes the first act as the act.
After Edit 2, R-6's deadline in that class is measured from **the giving of a decision** and from
nothing else — the residual limb cannot reach a Board that has acted twice and decided. **So Edit 1's
deeming cannot reach R-6's deadline at all, and an exception for it in Edit 1 would except a duty the
deeming cannot touch.** On *Forst* that is worse than silence: surplusage that invites the inference
that the deeming does reach it.

> **Edit 1's exception must name M 2's duty alone, and 164-7's must name both. The asymmetry is the
> correct drafting, and adding R-6 to Edit 1 would be the defect.** Asserted in the verifier:
> Edit 1's exception present once, R-6's descriptor absent from it.

**The saving's 256-character body stays byte-identical between the two sentences**, which is the
discipline MOO-209's N1 asked for and which my verifier now re-asserts independently of theirs.

### 3.2 F9's joint landing — decided, and it is my decision to take

MOO-209's F9 says the two deeming sentences should land as **one joint decision with an express
cross-reference**, because after both patches the section carries two deeming sentences with the
identical 44-word confinement clause, in two subsections, neither cross-referring to the other, and
nothing on their face saying which question each answers. **The Drafting Specialist adopts the routing
and declines to draft it unilaterally. That is the right instinct and it leaves the decision with
me.**

> **Decided. The MOO-141 patch and the MOO-164 cut are applied in one cut, as one decision. MOO-141's
> patch is no longer to be applied independently of MOO-164, and gate 3's re-verification covers both
> sets of anchors — three plus thirteen — at the base as it stands at the moment of application.**

Reasons. The two sentences answer one question between them and a reader has to hold both to get
either right; §2.4's rejected formula 3 shows that the alternative is to make them textually
interdependent, which is worse; and the combined text is the only text in which either has been
verified since revision 7. **Applying them separately would also put the first-applied patch into the
body in a state no pass has read.**

**This is a sequencing decision, not a new scope.** It adds no edit and no figure. It does change
what "done" looks like for this issue: **this issue closes when the joint cut is applied, not when my
three edits are approved.**

### 3.3 The cross-reference — specified here, drafted once, by the owner of the cut

I am not leaving this as "someone should." **It belongs in 164-7**, not in Edit 1, for one reason:
subsection A comes first in the section, so the later sentence is the one that can refer back without
a forward reference, and 164-7 is in the cut that will carry the joint landing.

**What it must do — three requirements, no words from me:**

1. Say, on the face of 164-7, that subsection A's deeming governs the case where the Board **acts
   more than once** upon a request, and that 164-7's governs the case where the Board **does not
   act**.
2. Make clear that the two are **cumulative and non-overlapping**, so neither is read as the
   exclusive rule for deeming an act, and neither is read as impliedly repealing the other.
3. **Move no date and add no exception.** If drafting it requires an exception in either sentence,
   that is a finding and comes back to me, not a drafting choice.

**Assigned to the Drafting Specialist as part of the joint cut.** If it cannot be done without
touching an exception, I decide it.

---

## 4. Verification

`moo141-rev71/verify_r71.py`, run against `moo141-rev71/live.md` — the body read from the store, not
from any document's reproduction of it. **All checks pass.**

- Base: whole document **484,408**; enacted §1 **134,012**; §1 sha256 `83a10b74950b5272…`.
- **All three MOO-141 anchors resolve exactly once in §1.** The dead store-revision-65 string is kept
  and asserted at **0**, so the break of 13 October stays visible.
- **All thirteen MOO-164 FINDs resolve exactly once in §1** at a base that cut has not seen, and
  their **+3,375** re-derives.
- Applied to a copy, §1 only: **revision 6 +847** (their published figure, re-derived), **revision 8
  +1,159**, of which Edit 2 is **+326** against revision 6's **+14**.
- `<u>`/`</u>` **62/62** in §1 before and after, balance 0. `first acts upon` **2 → 3**.
- **No word of the bill is deleted**: revision 6's Edit 2 text survives inside revision 8 exactly
  once, and Edit 1's and Edit 3's replacements are supersets of their FINDs.
- Combined text: **164-7's deeming present, its exception naming R-6 present, the residual limb
  present once, both of its named classes present once each**, and the decision-keyed limb ordered
  first.
- **Order independence**: MOO-164 ∘ MOO-141 == MOO-141 ∘ MOO-164, byte-identical. Combined §1 delta
  **+4,534 = 3,375 + 1,159.**
- Twelve saved provisions, G 4's two express *"first"*s, G 4's anti-delay sentence and M 2's
  deemed-denial sentence all intact and textually unmodified.

**Not applied to the store.** Gate 3 stands and is now a two-patch gate: re-verify all sixteen
anchors, every reproduction, every count and every invariant **at the base as it stands at the moment
of application** — not at store revision 71. The base has moved **ten** times under this item; five
of those moves rewrote a provision this patch reaches without an anchor moving, and one killed an
anchor outright.

---

## 5. Where this stands

| Gate | Issue | What clears it |
|---|---|---|
| **1** | **MOO-164** | The cut that carries 164-5 (F-9), 164-7 and the §3.3 cross-reference, as part of the joint landing |
| **2** | **MOO-197** | Store revision 66's four substitutions — the Rule 2A:2 cure and the member's route into court |
| **3** | whoever applies | Re-verification of **both** patches' anchors at the moment of application, §1-scoped |
| **4** | **new — MOO-215** | A bounded adversarial pass on Edit 2 revision 8 and on §3.3's requirements. **No text in §2.2 has been read adversarially**; MOO-209 named the defect and I drafted the cure, which is the same exposure that made MOO-214 necessary for revision 7 |

**Nothing else is reopened.** The board's 120 days are not reopened. The disclosure duty recorded at
17:42 on 12 October 2026 travels with the figure unchanged. The 17:26 finding — the 60-day
restore-and-settle duty on a reversal on reconsideration, which Edit 1's saving does not reach — is
**still open, still not drafted, and is a named target for the bounded pass.**

---

## 6. What I did not do

- **No card to the board.** The effect in the class the board decided is unchanged and counted; the
  residual limb operates only in classes that did not exist when the board answered at 13:13 on 12
  October 2026, the deemed-denial sentence having been enacted at 17:38 that day. No figure moves.
- **No Fiscal & Impact Modeler issue.** The 12-month aggregate cap is unmoved, so there is nothing to
  re-price. §2.6 names the trigger that would change that.
- **No Stakeholder Analyst issue.** Nothing here changes who is affected.
- **I did not draft the §3.3 cross-reference**, and I did not draft into MOO-164's edits. §3.3 states
  requirements and assigns it; drafting it from this side is how the two sentences diverged.
- **Nothing applied to the store.**

**Internal working draft material. Not a DLS bill. Not reviewed or cleared by counsel.
Pre-decisional.**
