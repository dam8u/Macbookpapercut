# MOO-176 — disposition of revision 6: **accepted as cut**, with one withdrawal and one correction to the record

**Policy Director · 12 October 2026.** Disposing of the Drafting Specialist's deliverable at
[`moo176-revision-6`](/MOO/issues/MOO-176#document-moo176-revision-6), document revision `32d3489a`.

**INTERNAL WORKING DRAFT. Not a Division of Legislative Services bill. Not reviewed by counsel, and
nothing here states or implies that it has been. Pre-decisional and internal.**

---

## 1. Disposition

**Revision 6 is accepted as cut.** It is the current cut of the MOO-141 patch. It stays unapplied.

**Who accepted it, stated precisely.** The Drafting Specialist's confirmation card bound to document
revision `32d3489a` was **accepted by the board at 17:32 on 12 October 2026**, before this disposition
was written. **This document is not that acceptance and does not repeat it.** It is the Policy
Director's disposition on top of it: my independent re-derivation of the figures, the decisions the
deliverable put to me, and two corrections to the record. **Nothing below reverses the board's
acceptance**, and had my verification failed I would have said so here and re-opened rather than
silently re-cut.

Accepted specifically:

| | |
|---|---|
| Edit 3 at 120 days, **+15** | accepted, **independently re-derived** (§2) |
| Patch delta **+698** | accepted, **independently re-derived** in two measures (§2) |
| The three items I required at §2 of the instruction | **delivered** — §6.1, §6.2, §6.3 of the document |
| The 120/120 collision | **answered**, and the answer governs the record (§5) |
| F-6's cap | **held candidate text only**, as instructed; the cap stays **declined** (MOO-179) |
| §6.4 — the 30/120 divergence | **a choice, not a defect. Adopted** (§6) |
| Applied to the store | **nothing** |

**Two things in the deliverable I am changing, and neither touches the text:**

1. **§8.3's first limit is withdrawn.** MOO-169 **did** complete. Store revision 61 is a **reviewed**
   base. §4.
2. **§8.1's enacted-§1 figure needs its convention stated**, because my own base re-check reported a
   different number for the same text. Both numbers are right. §3.

**Nothing in either changes a character of the patch, and neither is a reason to re-cut.**

---

## 2. Independent verification — re-derived from the store, not taken from the deliverable

I fetched `bill-text-s8` from MOO-42 directly and applied the three FIND/READ pairs to a copy. Every
figure in the deliverable reproduces.

| Check | Deliverable says | I measure | |
|---|---|---|---|
| whole document | 271,611 | **271,611** | ✓ |
| Edit 1 — FIND / READ / delta | 135 / 804 / +669 | **135 / 804 / +669** | ✓ |
| Edit 2 — FIND / READ / delta | 106 / 120 / +14 | **106 / 120 / +14** | ✓ |
| Edit 3 — FIND / READ / delta | 106 / 121 / **+15** | **106 / 121 / +15** | ✓ |
| anchor counts, whole document | 1 / 1 / 1 | **1 / 1 / 1** | ✓ |
| anchor counts, §1 | 1 / 1 / 1 | **1 / 1 / 1** | ✓ |
| patch delta, whole document | +698 | **+698** | ✓ |
| patch delta, §1 | +698 | **+698** | ✓ |
| revision 5's Edit 3 on **this** base | +697 | **+697** | ✓ |
| `<u>` / `</u>` balance, §1 and document | 60 / 60 both | **60 / 60 both, before and after** | ✓ |
| *"retention"* in §1 | 0 → 0 | **0 → 0** | ✓ |
| *"or an application"* in §1 | 0 → 0 | **0 → 0** | ✓ |
| *"until the Board acts upon the request"* | 1 → 0 | **1 → 0** | ✓ |
| *"120 days after the Board acts upon the request"* | 0 → 1 | **0 → 1** | ✓ |
| *"30 days after the Board acts upon the request"* | 1 → 1 | **1 → 1** | ✓ |
| *"120 days"* in §1 | 4 → 5 | **4 → 5** | ✓ |
| *"first acts upon it"* **in G 4** | 2, intact | **2, intact** | ✓ |
| *"120 days"* **in subsection M** | 1 → 2 | **1 → 2** | ✓ |

**The two findings that matter are measured, not asserted.** The broken identity is real — the 30-day
string stays at 1 and does not become 2. The twin-120 coincidence is real — within subsection M the
figure goes from one occurrence (clause (ii)'s tolling aggregate) to two (clause (ii) and the retention
endpoint). I confirmed both from the live body.

**The third express *"first acts upon it"* that appears after the patch is Edit 1's own new text in
subsection A, not a third one in G 4.** I sliced G 4 and counted inside it: still two, one for the
disability application and one for the request. The condition on which revision 2's G 4 edit stays
withdrawn holds.

**The +698 agrees in the whole document and in §1 under both conventions at §3.** That is the check that
nothing landed outside §1, and it passes either way you measure §1.

---

## 3. The correction to the record: two numbers for enacted §1, both right

**The deliverable reports enacted §1 at 117,980 characters. My own base re-check on MOO-141 reported
112,554 for the same text at the same store revision.** Neither is wrong and the record should not carry
both without saying which is which.

| Convention | Boundary | Characters |
|---|---|---|
| **store revision 61's own record** (the deliverable's) | `## 1. The bill` → `## 2. Section-by-section` — title line, enacting clause, both Code sections, and the remaining enactment clauses | **117,980** |
| **mine** | `### § 51.1-142.2.` → `### Remaining enactment clauses` — the two Code sections alone | **112,554** |

The difference is **5,426 characters**: the title line, the enacting clause and the remaining enactment
clauses. **I re-measured both today and both reproduce exactly.**

**Going forward, use the store's convention — 117,980 — because it is the one the store's own record
reports and the one the next base move will be measured against.** My narrower figure stays useful for
one purpose only: it is the measure that isolates the **Code text** from the enactment apparatus, and
the patch delta is **+698 under both**, which is the stronger form of the no-leakage check than either
alone. **The movement I reported on MOO-141 — enacted text down 2,279 while the whole document grew
21,382 — was measured on the narrow convention throughout, so it is internally consistent and still
holds.**

---

## 4. §8.3's first limit is withdrawn: store revision 61 **is** a reviewed base

**The deliverable records that MOO-169 did not complete, reported a terminal limit failure at 14:27, was
moved to `blocked`, and delivered no findings — so that revision 6 is cut against an unreviewed base.**
**That is wrong, and it is an honest error: the last three comments on MOO-169 are exactly the failure
notices the Drafting Specialist describes.** What those comments do not show is that **two runs executed
MOO-169 concurrently and the first one finished.**

**The pass of record exists:** [`counsel-pass-rev61`](/MOO/issues/MOO-169#document-counsel-pass-rev61) —
**1 fatal, 9 serious, 9 moderate, 4 minor, 12 null results**, with the thirteen substitutions verified
string by string and all 97 sections of Title 51.1 Chapter 1 fetched for the null sweep. MOO-169 is
`done` because it genuinely completed.

**So the limit is withdrawn, and the consequence for sequencing is the opposite of the one the
deliverable draws:** pass 19 is **not** the first review of anything in store revision 61, it does not
need to carry the base, and it can stay as narrow as MOO-180 commissions it.

### 4.1 What the counsel pass says about the three provisions revision 6 amends — **nothing collides**

I checked the pass against the patch rather than taking the headline count.

- **The fatal finding (F1) is in subsection E1**, on the in-service waiver and the § 51.1-153
  notification window. **It does not touch subsection A's interpretation paragraph, the definition of
  *"final qualifying retirement date"*, or M 2's retention sentence.** It does not reach any of the three
  FIND strings. **Revision 6's cut is unaffected by it.**
- **Two findings reach M 2, and neither reaches the sentence Edit 3 amends.** **F5** is on M 2's *second*
  sentence — the deeming of a certification as a determination — colliding with E10's 30-day review
  window. **M8** is on clause (ii)'s tolling aggregate and its exclusion. **The retention sentence, the
  fifth of eight, draws no finding.**
- **M5 is on D 1's first proposition**, which is Edit 2's cross-reference neighbourhood and not Edit 2's
  text. Edit 2 is unchanged and unaffected.

**That is a real result and it should be said plainly: the only provision in this patch that the
counsel pass had anything to say about is M 2, and what it said lands on the two sentences either side
of the one we amended.**

### 4.2 One place where the counsel pass sharpens the deliverable rather than contradicting it

**M8 and the deliverable's §6.2(c) are the same clock, pulled in opposite directions.** §8.

---

## 5. The 120/120 collision — the Drafting Specialist's reading governs

**I told them on MOO-179 that if they read the text differently their reading governs the text. They
do, and it does.** Recorded as the reading of record:

> On the text, clause (ii) aggregates *"all **retention** under this sentence."* The sentence fixes only
> when the retention **ends**; it begins when the application becomes the subject of a request — the
> filing. So the retention measured under clause (ii) is **127 days** on the ordinary facts against a
> **120-day** aggregate. **The cap takes 7 days off the board's own grant on the *first* request, with no
> chain at all, and takes more the longer the Board sits before first acting.** Clause (i) is therefore
> **unreachable**, not surplusage.

**This is sharper than my framing in two ways and I accept both.** I put it as a disjunction — clause
(ii) either duplicates clause (i) in more words or reaches into pendency. They show the second limb is
the one the text actually produces, and that it bites before any second request exists. **My framing
implied the damage needed a chain. It does not.**

**The structural point stands on its own and is the one to carry forward:** at 120 days per request, no
aggregate set at 120 can leave clause (i) any work; the two clauses can only do different jobs if the
aggregate **exceeds** the per-request figure. Pass 18 drafted a pair that was coherent at 30 and cannot
be coherent at 120 with both numbers at 120.

**Nothing operative turns on it today.** F-6's cap is **declined** on MOO-179 and the decline is
unchanged by this: MOO-170 found the chain cannot add demand, only reorder it, so the appropriation line
stays $0 at the central estimate and the high-take-up effect stays inside the same $204,000 lapse bound
at any chain length. **§9 of the deliverable is held candidate text and is not in the operative text.**

**What the collision answer is for.** It is the record of why, if trigger 2 ever fires and the cap
revives, **clause (ii) does not come back with it.** The live limb is clause (i) alone, and the form I
would start from is the deliverable's **candidate A** — no figure, no aggregate, no measurement
question, and it avoids *"retention"*, a noun that appears zero times in §1. **Candidate B is not
revived with it. §9.4 stays on the record as the cheapest option.** None of that is a decision today.

---

## 6. The 30/120 divergence is a **choice**. Adopted, and the defect test becomes a standing check

**§6.4's conclusion is adopted. No card is opened and nothing goes to the board on this.** The three
tests are the right three and the reasoning is sound: the divergence is legible from the two sentences
alone (different objects, different verbs, different limits); nothing in §1 measures a period from the
two endpoints being equal, across twelve chased referring provisions; and there is no reading in which
the longer retention makes the member worse off, because no provision is measured from the retention's
end.

**I am promoting their defect test from a note to a standing check**, because it is the kind of thing
that is true today and can stop being true on any base move:

> **Standing check, at every future cut of this patch and again at application.** Confirm that no
> provision in §1 (a) treats the end of the retention as the end of the tolling, or (b) measures a
> member's duty from the retention's expiry. **If one appears, the 30/120 divergence has become a defect
> that day, and the figure comes back to me as a card with options for the board.**

**Confirmed absent at store revision 61** — I re-ran it today. It joins §8.4's application list, and it
goes to MOO-180 as a named item so a reviewer tests the test and not only the conclusion.

---

## 7. The twin *"120 days"* in M 2 — no clarifier, and it goes to pass 19 as a named question

**Confirmed from the live text (§2): within subsection M the figure goes 1 → 2 after Edit 3** — clause
(ii)'s *"the aggregate of all tolling under this subsection shall not exceed 120 days"* and the
retention's *"until 120 days after the Board acts upon the request."* Two limits, two objects, one
number, one subsection.

**I agree it is foreclosed on the text, and for the reason given:** clause (ii) is an exception
introduced by *"except that"* on the **tolling** sentence, it is confined by its own words to *"all
tolling under this subsection,"* and the retention sentence tolls nothing — it says the application
*"retains its filing date."* Pass 18 reached the same place from the other direction. **I re-read
clause (ii) in the live body today and its object is *"all tolling"*, not retention.**

**The five-word clarifier is not drafted and I am not asking for it.** It adds an operative provision
nobody agreed, to cure a misreading that the text already forecloses, and the cap decision that might
have justified drafting it alongside something else has gone the other way. **Declining to draft it was
the right call and it was theirs to make.**

**It goes to MOO-180 as a named question**, phrased as a test rather than a request: does the
foreclosure hold on a cold reading of M 2, or does the coincidence of figures create a live ambiguity a
court could take? **If the reviewer says it is live, the clarifier becomes a card and I take it. If they
say it is foreclosed, the disclosure stays in the drafter's note and in the memo's risk section and
nothing is drafted.**

---

## 8. §6.2(c) — the member-clock residue. No card today, and here is why, and where it lives

**§6.2(c) is the most useful paragraph in the deliverable and it was volunteered against their own
case.** The point: tolling ends day 37 whatever Edit 3 says, so from day 37 the member's final
qualifying retirement date and every period in which she must act are running again — while the
application whose queue place she is holding has still not been acted upon. **A preserved queue position
is worth only what the final qualifying retirement date lets her use.** So the board's 120 days delivers
the retention's purpose and does not deliver a complete remedy.

**That is correct, and it is now doubly on the record, because counsel found the same clock from the
other side.** The pass of record's **M8** says clause (ii)'s tolling cap *"excluding any period after
the expiration of the 90 days allowed by this subsection and before the Board acts upon the request"*
leaves every day of Board delay past 90 days tolling **without limit**, extending the member's final
qualifying retirement date and holding the certified subsidy against the cap for as long as the Board
does not act. **M8's fix direction is to make the member's final qualifying retirement date run again
once the 90 days expire. §6.2(c)'s implied cure is to let it stop for longer.**

**So the two findings are one question with two answers pulling opposite ways**, and the question is:
*what happens to the member's own clocks while the Board is late?* **Neither can be decided inside this
patch, and neither should be.** That question is the whole subject of
[MOO-141](/MOO/issues/MOO-141) — the two clocks and their endpoints — which is where §0.2's call (one
pendency event, two endpoints) was taken and where any change to the tolling endpoint has to be taken.

**Decision: no card today, and no re-opening of the figure.** Three reasons:

1. **It is not a defect in revision 6.** Lengthening the retention cannot have created a residue it did
   not create; the residue is in the **tolling** endpoint, which this patch does not amend.
2. **Carding it today would put a question to the board that has two live expert answers and no priced
   option.** M8's direction has a fiscal side that nobody has modelled.
3. **MOO-141 is the home and it is already structurally correct for this** — it is blocked on MOO-164
   and MOO-42 as first-class edges, so the item lands there and waits for the right moment rather than
   generating a card now.

**One thing I will not let slide: the board must not read its own answer as having bought more than it
bought.** Recorded here, and it travels with the figure:

> **The board's 120 days buys the member's place in the D 4 / D 5 queue for 120 days after the Board
> first acts. It does not stop the member's own retirement clock, which stops 30 days after that same
> first act. Where the Board is late, the queue place can outlive the member's ability to use it.**

**That sentence is a disclosure duty at the next memo**, it is not a plain-language summary sentence,
and it is not quotable as one. It goes to MOO-141 as the named candidate card, paired with M8.

---

## 9. The plain-language layer — already caught up; nothing is left to me

The Drafting Specialist's cross-link on this issue (17:21) flagged that the released summary's sentence 3
and register §4's replacement sentence were still on the superseded 30-day figure. **Both were released
corrected four minutes later and the cross-link is answered, not outstanding.**

- **Register §4's replacement sentence** — released on MOO-178 §2 in the corrected 120-day form, with
  the superseded *"two endpoints … 30 days after that"* form struck and the reason recorded.
  `moo172-risk-items.md` §4 in the repo carries it.
- **Sentence 3** — released in substance on MOO-178 §3 with the backward comparison struck, and cut by
  its author on **MOO-181** at document revision `14531574`. All three sentences are clean and quotable.
- **The deliverable's §5.2 point is right** — memo risk item 3 is wrong as written, because Edit 3 is now
  net **+42** rather than net **−48**. **That is MOO-177's whole subject**, it is assigned to the Editor
  at high priority, and it is blocked on this issue alone. **Accepting revision 6 releases it.**

**One carrier question on MOO-181 is open and addressed to me** — whether register §6 points at the
MOO-181 copy of `moo178-patch-summary-recut` or whether I re-post the identical body onto MOO-178. **It
is mine, it is answered separately on that issue, and it blocks nothing here.**

---

## 10. Two orphans this review exposed, and what I did about each

Neither is MOO-176's work. Both were found by reading the record around it, and leaving either unowned
would be worse than the scope cost of naming them.

### 10.1 The fatal finding's proceed/don't-proceed call is **mine** and had no issue carrying it

The pass of record's §8 ends: *"**Policy Director** — the proceed/don't-proceed call on F1 is yours. My
view is that the subdivision should not go to DLS with E1 in its current form."*

**MOO-169 is closed. No live issue carries that call.** A fatal finding with a named decision-owner and
no ticket is the most serious gap on this board today, and it is mine.

**Action: [MOO-188](/MOO/issues/MOO-188), assigned to me, high priority.** It gets its own decision
document, not a paragraph in a patch disposition — the subject is subsection E1 and § 51.1-162, not the
two-clock patch.
**F1's fix direction is also unowned on the drafting side** (MOO-64's revision 7 is two definitions and
does not reach it), and the issue carries that as its second item so the cure is commissioned in the
same breath as the call, with counsel's warning attached: **do not re-widen the sentence without the
retiree carve-out.**

### 10.2 MOO-182 was created with no assignee

**MOO-182** — the three additions and one retraction the second MOO-169 run found against the pass of
record, including the E6 / D 7 reinstatement fork that is expressly put to me — is `todo`, `high`, and
**unassigned**, so nothing will ever run it. **Action: assigned to Red Team / Counsel Reviewer**, whose
work it is and who authored it. **It is ready — no blockers — and it does not wait on gate 4.**

---

## 11. Gate status, and what is still not done

**Gate 4 is released by this acceptance.** [MOO-180](/MOO/issues/MOO-180) is blocked on this issue and
on nothing else; it wakes on the status change and sees the final shape once, as designed. **Three items
as commissioned, plus the two named items this disposition adds: §6's defect test, and §7's twin-120
question.** Its scope note to *"read MOO-169's result"* now points at a real document, and §4 above tells
it what that document does and does not say about this patch — so the pass does not have to carry the
base.

**Unchanged and not re-opened:** §0.2's call (one pendency event, two endpoints); §0.3's answer (keep
F-1's deletion, day 22 accepted); Edit 1; Edit 2; the board's figure; MOO-163's released price;
MOO-164's six cards, none of which turns on 30 against 120.

**Not done, and deliberately:**

- **Nothing is applied to the store.** Application is a separate step and a separate decision. It needs
  its own re-verification at that moment, against the base as it stands then — **not against store
  revision 61.** §8.4's list governs, now with §6's defect test and the *"120 days"* re-count on it.
- **The warning has fired five times in seven and today's stale reproduction was inside M 2**, the
  provision the one live text change sits in. **An anchor that still resolves is not evidence the
  reproductions are current.** That is the rule for whoever applies this and for MOO-180.
- **Nothing re-priced.** MOO-170 is closed; the 90-days-per-request third-party limb at §6.2(d) is
  described, not costed, and the deliverable is right that a pricing model needs store revision 61's
  widened requester and subject classes as well as the figure.
- **No clarifier drafted** (§7). **No cap in the operative text** (§5). **No card opened** (§6, §8).

---

**MOO-176 is closed. Revision 6 stands as the current cut, unapplied.**

**INTERNAL WORKING DRAFT. Not a Division of Legislative Services bill. Not reviewed by counsel.
Pre-decisional and internal.**
