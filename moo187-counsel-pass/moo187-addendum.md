# MOO-187 addendum — the revision-3 and revision-4 pass: §13, §14, candidates 164-7 and 164-8, and the apply kit

**Internal risk analysis. Not legal advice, not a legal opinion the organization can rely on, and
nothing in it states or implies that counsel has cleared the proposal. Pre-decisional and internal.**

**Red Team / Counsel Reviewer · 12 October 2026, second pass.** Companion to
[`moo187-counsel-pass`](/MOO/issues/MOO-187#document-moo187-counsel-pass), which reviewed revision 2
against store revision 62.

**Why this exists.** The Drafting Specialist's note of 17:57 crossed my close by five minutes and asked
me to press on **§13.3, §13.4, §13.5, §13.7, §13.9 and §13.10**. I have. While I was doing it the
document moved to **revision 4** (143,161 characters, §14 added) and the base to **store revision 64**
(record only, §1 byte-identical to 63). **This addendum is cut against document revision 4 and
`bill-text-s8` document revision 81 / store revision 64, both fetched today**, and against the apply
kit as committed at `60f18ca`.

**Eight new findings — 0 fatal, 4 serious, 2 moderate, 2 minor — and 8 more null results.** Running
total: **26 findings, 0 fatal, 11 serious, 8 moderate, 7 minor**, and **19 null results**. One earlier
finding (**F7**) is **discharged**; one (**F14**) is **superseded by the drafter's own correction**; one
(**F12**) has gone from hypothetical to **realised in the enacted text**.

**The most serious new one is F19**: candidate 164-7's deeming carries **one** of Edit 1's **two**
trigger limbs, so it ends the member's tolling without reaching the sentence that gives her a new
retirement date when tolling ends. §13.7 and §14.1 both describe the confinement as *"lifted word for
word"* from Edit 1. It is not, and the missing limb is the one that matters to her.

---

## 1. The six items I was asked to press, item by item

### §13.3 — the 19 → 21 classification: **holds as a classification; does not rescue §1.2's claim**

**What I ran.** Independent enumeration over enacted §1 at store revision 63, by regex, with no
reference to §13.3's table.

| | §13.3 claims | I measure |
|---|---|---|
| `acts upon` in §1 | 8 | **8** |
| `act upon` in §1 | 9 | **9** |
| `acting upon` in §1 | 2 | **2** |
| `action upon` in §1 | 2 | **2** |
| total | **21** | **21** |

**Both new occurrences are the two inserted negatives, and both classifications are right.**
Occurrence **20** confers a power on the person who filed (*"may file with the Board written notice that
the period has expired"*) and keys nothing to any act of the Board. Occurrence **21** fixes the denial
date *"on the first day after the expiration of those 30 days"*, and those 30 days run **from the
member's filing**, not from any act. Neither is an endpoint.

**I attacked occurrence 21 specifically, because it is the one that could have collided with Edit 1's
deeming, and it does not.** The attack: Edit 1 deems the Board to act on the date it **first** acts; if
that deeming reached occurrence 21, a Board that acknowledged on day 7 and then made a real
determination inside the 30-day window would be deemed to have acted **outside** it, the condition
*"does not act upon the request within 30 days after that notice is filed"* would be satisfied, and the
section would carry a real decision **and** a deemed denial. **It fails, cleanly:** Edit 1's deeming is
triggered only where a period *"begins or ends upon, or is measured from, the Board's acting"* or where
*"a date is fixed by reference to the month in which the Board acts"*. Occurrence 21's 30 days are
measured from the **member's** filing and its date from the expiry of those 30 days. **The trigger is not
met, the deeming does not apply, and there is no collision.** §13.3's *"not an endpoint"* is the right
answer and this is the reason it is right.

**What does not follow.** §13.3 concludes *"the claim §1.2 rests Decision 1 on is unchanged at store
revision 63: after this cut exactly one act-keyed endpoint remains where a token action can cost anybody
anything."* **That claim was already wrong at 19 and is still wrong at 21, for F1's reason** — Edit
164-1's own 48-day cap is act-keyed, is reached by the deeming, and binds whenever notice falls more than
18 days after the deemed first action. **§13.7 of the same document revision says so**: *"Edit 164-1
does not cure this and does not purport to. Say so plainly."* §13.3 and §13.7 are answering different
questions — token action versus no action — but F1 is in the token-action column, and §13.3 re-affirms
the headline without re-testing it.

**Verdict: the count and the two new rows are sound. F1 is not answered and remains the most serious
finding in this review.**

### §13.4 — *"first required"* and Edit 164-5: **sound on all three grounds**

Checked at source in §1 at store revision 63.

1. *"[F]irst required"* occurs **once** in §1, in D 1's **filing-duty** sentence
   (*"...earliest qualifying retirement date and final qualifying retirement date **first required** by
   the definition..."*). ✓
2. D 1's **lateness-extension** sentence is a separate sentence and lists **three** documents in
   parallel, verbatim: *"Where the Board gives **that written statement**, **any notice of a later
   approved date** required by that definition, or **any notice of a date** required by that definition
   upon the Board's action upon a request, later than the time required by that definition..."* Reading
   the third limb as the opening statement would duplicate the first and strand the third. ✓
3. The third limb is the notice MOO-141's Edit 2 re-times. ✓

**Edit 164-5 is not narrowed, its FIND still resolves once in §1 at store revision 63, and I found
nothing to add.** This item is closed.

### §13.5 — the D 1 vehicle gap and candidate 164-8: **the gap is real; the candidate is wider than the price statement**

**The gap is real, and I verified the negative rather than taking it.** In subdivision D 1 (7,216
characters) the words `amend`, `withdraw`, `replace`, `replacing`, `substitute`, `revoke` and `rescind`
each occur **zero** times. D 1 grants one 30-day filing window running from the **first** statement and
then tells the member she *"may state an effective date of retirement"* when a **later** notice is late.
**There is no vehicle.** §13.5's reading of § 51.1-153 is consistent with the text D 1 quotes; I did not
re-read § 51.1-153 at source this pass and say so at §4.

**Anchor integrity confirmed, including the lesson.** 164-8's full FIND resolves **once** in §1 at store
revision 63; the short form *"and the Board shall state every such delay in the report required by
subsection J."* resolves **twice** — in D 1's lateness sentence and in D 4 — exactly as §13.1 records.
Good catch and correctly handled.

**New finding, F26 below:** 164-8's condition is keyed to **when the notice arrives**, not to **whether
it is late**, so it reaches a class the lateness extension never decided.

### §13.7 and §14 — candidate 164-7: **three new findings, and the drafter asked for exactly this**

§13.7 point 4 invited a reviewer to press on limb 3. I did, and limb 3 is fine. **The defects are
elsewhere: F19, F20 and F22 below.** §13.7's structural case for 164-7 is right — it supplies a date for
one event rather than defining the verb, which is Decision 1's method — and I tested the limb reach and
confirm it:

| Endpoint | Keying words | Caught by 164-7's confinement because the period… |
|---|---|---|
| 1 — the tolling endpoint | *until 30 days after the Board acts upon the request* | **ends upon** the act ✓ |
| 2 — clause (ii)'s exclusion | *and before the Board acts upon the request* | **ends upon** the act ✓ |
| 3 — the D 4 / D 5 retention | *until 120 days after the Board acts upon the request* | **ends upon** the act ✓ |
| 4 — the 15-day application duty | *no later than 15 days after it acts upon the request* | **is measured from** the act ✓ |

**All four are caught. §14.1's table is right and so is its point that limbs 2 and 3 share one
sentence** — I confirmed the retention and the 15-day duty are one sentence with no full stop between
them, so no amendment confined to clause (ii) can reach either. **That is a correct and load-bearing
reason to prefer route (c) to route (b), and it is the drafter's, not mine.**

### §13.9 — the ordinal reference: **sound, and the fragility is narrower than the fragility**

Verified in §1 at store revision 63: D 1 reads *"...the **second sentence of subdivision M 2** does not
apply to such a failure..."*, and M 2's sentences run (1) the standing/window sentence, (2) **the deeming
sentence**, (3) the 90-day duty, (4) and (5) item 124's two enacted sentences, (6) the tolling sentence
Edit 164-1 rewrites, (7) the retention/15-day sentence, (8) the completion sentence, (9) the Article 5
grant, (10) the APA disapplication. **The reference points at the deeming sentence and nothing in the
cut, in item 124's enacted text, in candidate 164-7 or in card (i)'s sentence inserts before it.** ✓
§13.9's table is correct in all five rows.

I also checked §14.7's claim and confirm it: `such case decision` occurs **once** in §1, in the Article 5
grant, and inserting 164-7 after the denial sentence leaves its nearest antecedent where it is — the
completion sentence, which is item 131's point and is unaffected. ✓

**F25 below** is the one addition: the reference breaks on more than an insertion.

### §13.10 — the six corrections: **all six check out**

| | Correction | Result |
|---|---|---|
| 1 | R-5's date is **not** identical to the denial date; option (d) keys the denial to the member's notice + 30 | **right.** This supersedes my **F14**, and the corrected statement is stronger than mine: R-5 fires on the expiry of the allowed period whether or not the member ever files. |
| 2 | Card C is dead, not held | **right** — item 124 is enacted at store revision 63. |
| 3 | 19 → 21 | **right** — independently counted. |
| 4 | Decision 2's rule is in **five** places, not three | **right** — both new sites verified, one occurrence each: D 1's certification-failure clock (*"no later than 30 days after the date on which the certification is given to the member"*) and G 4's § 51.1-162 C waiver floor (*"does not expire before the thirtieth day after the notice is given"*). |
| 5 | §6 re-spliced from store revision 63 | **right**, and it **discharges my F7.** |
| 6 | Same counts, same +490 at store revision 63 | **right on the §1 basis** — I re-ran the whole patch over §1 at store revision 63 and get **+490**. |

**Correction 6 carries one exception, and it is my F2, unchanged:** the §7.2 row predicting
`acts upon` **= 7** after both patches is wrong on **both** bases. Over §1 at store revision 63 the
count is **9** (8 before; Edit 164-1 +1, Edit 1 +1, Edit 2 −1). The row needs correcting whichever
counting convention the kit settles on.

---

## 2. New findings

### SERIOUS

**F19 — candidate 164-7's deeming carries one of Edit 1's two trigger limbs. It ends the member's
tolling without reaching the sentence that gives her a retirement date when tolling ends.**

**What the two texts actually say.** MOO-141's Edit 1 triggers on **two** forms:

> where **(A)** a period begins or ends upon, or is measured from, the Board's acting, or last acting,
> upon a request, **or** where **(B)** a date is fixed by reference to the month in which the Board acts,
> or last acts, upon a request

Candidate 164-7 carries **(A) only**:

> for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 **under
> which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the
> request**

**Verified by string comparison, not by eye:** limb (A) is present in both; limb (B) is present in Edit 1
and **absent** from 164-7. §13.7 point 2 says the confinement is *"lifted **word for word** from the
MOO-141 patch's Edit 1"* and §14.1 repeats *"lifted word for word."* **It is not. One of the two limbs is
dropped.**

**What limb (B) is for.** It is the limb that reaches **occurrence #2** — the definition's reset:

> *"Where the running of a period has been tolled under subsection M and the member is prevented by the
> preceding sentence from retiring in a qualifying retirement after that tolling ends, the member's final
> qualifying retirement date is ... the first day of the second month following **the month in which the
> Board last acts upon a request** the filing of which tolled that period..."*

That date is *"fixed by reference to the month in which the Board ... last acts"* — limb (B) exactly, and
nothing else in Edit 1 reaches it. **It is the sentence whose entire function is to give the member a
usable retirement date once her tolling ends.**

**The failure scenario, with dates.**

| Day | Event |
|---|---|
| 0 (1 Jan) | Member files a request for reconsideration. Tolling starts |
| 90 (1 Apr) | M 2's 90 days expire. The Board has done nothing |
| 200 (20 Jul) | Member files the expiry notice under the enacted option (d) |
| 231 (20 Aug) | The request is denied by operation of law. **164-7 deems the Board to act on this date — for limb (A) purposes only** |
| 261 (19 Sep) | **Tolling ends** (Edit 164-1 limb (a): denial + 30; cap at denial + 48) |
| — | **The reset cannot operate.** It needs *"the month in which the Board last acts"*, limb (B), which 164-7 does not supply. The Board never actually acted |
| — | **R-5, as cured by Edit 164-4, gives a floor keyed to the month the allowed period expired — April — so 1 June.** That date is three and a half months in the past when her tolling ends on 19 September |
| — | The 12-month cap in the definition's sixth sentence then binds with no reset. **If it has passed, she cannot retire in a qualifying retirement at all** — which is the injury the reset exists to prevent |

**Without 164-7 she is not in this position**, because tolling never ends and the reset never needs to
operate. **164-7 ends the tolling and removes her reset in the same move.** §13.7's trade is stated as
*"bounding it cuts against the member in the one case where the Board has wholly failed to act"* — true,
and the bound is disclosed. **The loss of the reset is not disclosed, and it is larger than the bound.**

**Fix — one clause, Edit 1's own words, and it has no downside.** Add limb (B) to 164-7's confinement:

> `… under which a period begins or ends upon, or is measured from, the Board's acting, or last acting,
> upon the request,` **`or under which a date is fixed by reference to the month in which the Board
> acts, or last acts, upon the request,`** `to act upon the request, and to last act upon it, on the
> date of that denial.`

With it, the reset keys to the month of the denial — August on the facts above — and her final qualifying
retirement date becomes 1 October, after her tolling ends on 19 September. **That is the result the
section is built to produce.** And limb (B) cannot cut against her here: the deemed date is the denial
date, which is later than the nothing she has today. **Drafting Specialist writes it; I am naming the
defect and the words it is missing.**

---

**F20 — 164-7's second sentence is not Edit 1's saving clause, and §3.6's own rule is engaged by it.**

**The two texts, verbatim:**

> **Edit 1:** *"Nothing in the preceding sentence determines **the date by which the Board is required to
> act upon a request, to make a determination, or to give a notice or a decision**, or whether the Board
> has **performed such a duty within a period required by** this section."*
>
> **164-7:** *"Nothing in the preceding sentence **relieves the Board of the duty to act upon a request
> for reconsideration**, or determines whether the Board has **acted upon a request within the period
> allowed by** this section."*

**Different in both limbs.** §13.7 point 2 says *"the second sentence is **Edit 1's own saving clause**,
so the deemed denial cannot discharge the Board's 90-day duty"* and that the candidate *"avoids [two
words for one concept] by using Edit 1's words."* The conclusion about the 90-day duty is right — the
narrowed limb does carry it. **The premise is not.** The candidate introduces a **second,
differently-worded saving clause for the same deeming mechanism**, in a section that would then carry
two. That is precisely the defect Edit 164-6 exists to prevent, asserted away in the paragraph that
creates it.

**And the difference is substantive, not stylistic.** Edit 1's dropped first limb — *"the date by which
the Board is required to act upon a request, to make a determination, or to give a notice or a
decision"* — is what keeps the deeming out of the Board's **duty dates**. 164-7 drops it, which is how
the candidate reaches **endpoint 4**, the 15-day duty on the application. §13.7 point 4 presents that
reach as flowing from the **deeming**; it flows from the **narrowing of the saving**. The Director should
be told that the thing making limb 3 work is a 30-word difference in a sentence described as *"Edit 1's
own."*

**Failure scenario if it is left as drafted.** A Board arguing that the deemed denial does not trigger
the 15-day duty reads the two savings together: Edit 1's says the deeming *"does not determine the date
by which the Board is required to act"*; 164-7's omits that limb. The Board argues the omission is
meaningless because the two savings are, on the drafter's own account, the same clause — and therefore
that Edit 1's broader limb governs both deemings, so no duty date is determined by either, so the 15-day
duty still never falls due. **The claim of verbal identity in the drafter's note is the argument's best
evidence.**

**Fix direction.** Either use Edit 1's saving verbatim and carve out limb 3 expressly, or keep the
narrowed saving and **say in the drafter's note that it is narrowed, why, and that the narrowing is what
reaches limb 3.** Not both. The one thing not to do is describe a differently-worded clause as the same
clause.

---

**F21 — the apply kit as committed hard-fails on the current base, and `README.md` contradicts itself
about which script is the current check. Two FIND strings now resolve twice whole-document.**

**What I ran.** `verify_r6.py`, unmodified, from the committed kit, against `bill-text-s8` at store
revision 63:

```
AssertionError: retains its filing date for the purposes of subdivisions D 4
```

**Why.** `verify_r6.py` reads the whole document (`bill = open('bill.md').read()`) and asserts
`count == 1` over it. Store revisions 62, 63 and 64 quote anchor strings in the §0 narrative. Measured at
store revision 63:

| String | In §1 | Whole document |
|---|---|---|
| MOO-141 Edit 3's anchor (the D 4 / D 5 retention) | 1 | **2** |
| **Edit 164-6's FIND** (the G 4 period formula) | 1 | **2** |
| **Candidate 164-7's FIND** (the enacted denial sentence) | 1 | **2** |
| M 2's 90-day sentence | 1 | **4** |
| Edits 164-1 to 164-5 | 1 | 1 |

**Two of them are this cut's own strings.** An applier who does a whole-document find-and-replace on
Edit 164-6 — which is what the FIND/READ form invites and what `apply164.py` does on a copy — **edits the
§0 revision narrative as well as the bill**, corrupting the record of store revision 62 or 63.

**And `README.md` tells the applier to do exactly that.** As committed at `60f18ca` it says, at lines
3–4, *"`verify_r63.py` is the current check"*, and then at line 24 *"Run `verify_r6.py` to reproduce"*
and at line 28 *"`verify_r6.py` — **the current check.**"* **Two contradictory statements, and the one
stated twice names the script that fails.** §13.1's *"The apply kit has always counted §1 only"* is not
true of `verify_r6.py` as committed; it is true of `verify_r63.py` and `verify_r64.py`, which are new.

**Fix direction.** Retire or delete `verify_r6.py` and `verify.py` rather than leaving them described as
current; correct README lines 24 and 28; and put the **§1-only scope** into the **apply instructions**,
not only into the new scripts' docstrings — because the thing that will go wrong is a replace, not a
count. **This is the finding most likely to cause actual damage, and it is the cheapest to fix.**

---

**F22 — 164-7 and §14.4 leave the definition-request class uncured in **every** case, not merely where
the member declines to file.**

**The text.** The enacted option (d) opens *"Where the Board does not act upon **a request for
reconsideration** within the 90 days allowed by this subsection..."* — confined to reconsideration
requests. But **M 2's tolling sentence tolls on two classes**: *"The filing of a request for
reconsideration under this subsection, **and the filing of a request under the definition of 'final
qualifying retirement date' in subsection A**, tolls the running of..."* The definition class has its own
allowed period — 30 days under the definition's third sentence — and **no denial mechanism of any kind.**

**So for a request under the definition, there is no expiry notice to file, no denial date, and nothing
for 164-7's *"on the date of that denial"* to attach to.** Limb 1 (tolling) and limb 2 (clause (ii)'s
exclusion) remain open for that class unconditionally. Limbs 3 and 4 are not engaged, because the
retention sentence is confined to *"a request for reconsideration under this subsection."*

**Why this matters to §14.4 and not just as a footnote.** §14.4 reports the uncured case and attributes
it to the member's choice — *"**may** is a power, not a duty"* — and its table rows are *"where she files
the expiry notice"* and *"where she does **not**."* **For the definition class there is no row she can be
in.** The gap is structural, not elective, and §14.4's answer to it (reason 1: *"in the never-notifies
case limb 1 favours the member"*) is weaker here, because the member who asked for a later retirement
date and got silence is not obviously served by a final qualifying retirement date that never stops
moving while the Board holds her request.

**Failure scenario.** Member files a request under the definition on 1 January for approval of a later
retirement date. The definition's 30 days expire 31 January. The Board never acts. Her final qualifying
retirement date and every period within which she must act are tolled **indefinitely**; clause (ii)'s
120-day aggregate never binds, because Edit 164-3's exclusion takes the Board's lateness out of it; and
there is no expiry notice she can file, because option (d) does not reach her. R-5 as cured by Edit 164-4
gives her a floor keyed to 31 January — which is her only protection, and which is **why Edit 164-4
matters more than §2.4 said**, as the drafter's own correction 1 now records.

**Fix direction, and it is a policy choice.** Either extend 164-7's deeming with a second limb keyed to a
date that exists without member action — *"or, where the Board does not act upon a request under the
definition of 'final qualifying retirement date' in subsection A within the period allowed by this
section for acting upon it, on the day after the expiration of that period"* — or record the class as
uncured alongside §14.4's case. **The first bounds a window that currently runs in her favour, so it is
the same trade §13.7 identifies and it is the Director's.** What should not happen is for §14.4's table
to go to the Director describing the gap as elective.

### MODERATE

**F23 — Edit 164-1's endpoint in the **no-notice** case is ambiguous between act + 30 and act + 48, and
after item 124's enactment the no-notice case is a real class.**

**The text.** `until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after
the Board gives the person who filed the request written notice of its decision upon the request, and in
no case later than 48 days after the Board acts upon the request`

**The two readings.** Where the Board never gives the notice described in (b):

- **Reading 1 — act + 30.** *"The later of (a) X and (b) Y"* where Y never occurs resolves to X. There is
  no second date to be later than the first, so the endpoint is limb (a) and the cap is never engaged.
- **Reading 2 — act + 48.** Limb (b) is an open-ended future date, so *"the later of"* is unsatisfied and
  the cap binds.

**The cut assumes Reading 2 throughout** — §2.2's table row 4 (*"Board never gives notice: act + 30 →
act + 48, +18 days, capped"*) and §13.7 point 3 (*"the tolling ends at denial + 48 days at the outside"*).
Reading 1 is at least as natural and is the one an agency would argue. **18 days turn on it, in the case
where the member is worst served**, and the whole of Edit 164-1's claimed benefit in that case is those
18 days.

**And the class is no longer hypothetical.** Store revision 63's own record states that a denial by
operation of the enacted sentences *"carries no writing, no reasons and no notice."* So with 164-7
adopted, **every** deemed-denial case is a no-notice case, and the endpoint turns on an unresolved
construction.

**Fix direction — the Director chooses the answer, then the words follow.** If act + 48 is intended:
*"until the earlier of (A) 48 days after the Board acts upon the request and (B) the later of (a) 30 days
after the Board acts upon the request and (b) 30 days after the Board gives..."* If act + 30 is intended,
limb (b) should carry *"where the Board gives such notice"* so that the *"later of"* has one operative
limb. **I am not proposing the words; I am saying the sentence does not currently answer the question and
two of the cut's own statements assume the answer.**

**F26 — candidate 164-8 is keyed to when the notice **arrives**, not to whether it is **late**, so it
reaches a class D 1's lateness extension never decided — and §13.5's price statement does not cover that
class.**

**The text.** 164-8's condition: *"Where the Board gives any notice described in the preceding sentence
**after the expiration of the period allowed by this subdivision for filing the notice of retirement
required by § 51.1-153**..."*

That is a test of **arrival relative to the member's filing window**, not of lateness. §13.5 frames the
candidate as the cure for the late notice, and prices it as costing nothing *"except in the case where
the member uses the window to retire later than she otherwise could have — **which is the case the
extension already decided in her favour**."*

**The uncovered class.** A later date can be approved, and its notice given **perfectly on time**, long
after the member's single 30-day window has closed. The definition lets the member file a later-date
request *"at any time before the date that would otherwise apply"*, and the Board must give notice of an
approval *"no later than 15 days after the approval."* So: first statement 1 February, filing window
closes 3 March, later date approved 1 September, notice given 10 September — **on time**. 164-8 fires,
because the notice arrived after the window closed. **The lateness extension never reached this case, so
it never decided it in her favour, and §13.5's price statement does not apply to it.**

**Not a reason to decline the candidate** — on the merits, a member who has just been given a later
retirement date and cannot file for it has the same problem whether the notice was late or timely, and
reaching both is arguably the better rule. **It is a reason the Director should be told what she is
approving:** 164-8 is wider than the sentence it appends to, and its price covers a class the extension
decided plus a class it did not.

### MINOR

**F24 — §13.9 repeats §7.3's *"three other 'the period allowed…' phrases"*.** There are **six** in §1,
plus two instances of *"the time allowed by that definition"* where the sweep names one. Carried from
**F13**; the conclusion (no further conforming amendment) still survives, the sweep as stated still does
not.

**F25 — §13.9's fragility note is narrower than the fragility.** It warns that *"any future edit that
inserts a sentence into M 2 **before** the deeming sentence silently strands that reference."* An
insertion is not the only way: **any edit that splits M 2's first sentence into two** strands it just as
silently — and M 2's first sentence is a 1,300-character sentence carrying eight standing classes and
three review windows, which store revision 62 has already rewritten once and which is the most likely
candidate in the section for being broken up. Worth one clause in §13.9, not a cure.

---

## 3. Status of the revision-2 findings after this pass

| | Finding | Status |
|---|---|---|
| **F1** | the 48-day cap is act-keyed; #15 is not closed | **live, and reinforced** by §13.7's own *"Edit 164-1 does not cure this and does not purport to"*. §13.3 re-affirms the headline without re-testing it |
| **F2** | §7.2's `acts upon` row predicts 7; it is 9 | **live on both counting bases.** Re-run over §1 at store revision 63: 8 before, **9** after both patches |
| **F3** | Edit 164-2's limb names only the 30-day limb of a two-limb requirement | **live.** Nothing in §13 or §14 touches G 2 |
| **F4** | §2.3's arithmetic omits G 4's suspension of G 2's 120-day limit | **live** |
| **F5** | the 210-day bound fails; clause (ii) excludes the Board's lateness | **live, and now the drafter's own position.** §7 item 130, §13.7 and §14.3 are the same defect, and §14.3's reversed-incidence reason for declining route (b) is the same point I made at F5 about Edit 164-6 and clause (ii) doing opposite work with one formula. **Convergent discovery; I am recording it as agreement, not priority** |
| **F6** | M 2's 90 days states no commencement | **live and escalated.** Store revision 63 keys **the member's power to file the expiry notice** — and therefore the whole route into court option (d) exists to open — to *"the 90 days allowed by this subsection"*. Verified at store revision 63: still *"within 90 days."*, with **no** *"after"*. The one thing the enacted cure exists to supply now depends on a date the text does not fix. **Five words, and they are now worth more than they were** |
| **F7** | §6.3 and §6.6 stale against the live base | **DISCHARGED** by §13.2's re-splice from store revision 63 |
| **F8** | limb (b) keys the member's clock to notice given to the filer | **live.** At store revision 63 M 2's class list still carries eight classes |
| **F9, F10** | the two card (c) candidates | **live.** Untouched by §13 and §14 |
| **F11** | R-6's *"determines"* condition | **live** |
| **F12** | item 124 would re-create two formulas for one concept inside M 2 | **REALISED, not hypothetical.** At store revision 63 *"the 90 days allowed by this subsection"* occurs **twice** in §1 — the enacted sentence and clause (ii). Edit 164-3 removes the clause (ii) one, leaving one against **three** instances of *"the period allowed by this section for acting upon the request."* Now a live defect in enacted text rather than a warning about a candidate |
| **F13** | §7.3's sweep names three of six | **live**, and repeated at §13.9 — see F24 |
| **F14** | §2.4's month is wrong | **SUPERSEDED** by §13.10 correction 1, which goes further and is right |
| **F15–F18** | the four minors | **live.** F15 re-measured over §1 at store revision 63: *"no later than"* is **74**, against the document's 72; *"shall act upon"* is **5**, which the document has right |

---

## 4. What I tried to break on this pass and could not

**N12 — occurrence 21 cannot collide with Edit 1's deeming.** The attack and why it fails are at §1 above.
The deeming's trigger is not met, so a real determination inside the 30-day window is not deemed outside
it and no second determination arises. **§13.3's *"not an endpoint"* holds for the right reason.**

**N13 — §13.4 is sound on all three grounds**, verified at source. Edit 164-5 stands. Closed.

**N14 — §13.5's vehicle gap is real**, verified as a negative across seven candidate words, all zero in
subdivision D 1.

**N15 — 164-7's limb reach is complete for the reconsideration class.** All four endpoints are caught,
and I confirmed the textual reason for each (three *"end upon"*, one *"measured from"*). I also confirmed
§14.1's independent point that the retention and the 15-day duty are **one sentence**, so no amendment
confined to clause (ii) can reach them — which is a correct and load-bearing reason to prefer route (c)
to route (b).

**N16 — §13.9 and §14.7 both hold.** The ordinal reference points at the deeming sentence; nothing in the
cut, in the enacted sentences, in 164-7 or in card (i)'s sentence inserts before it; and `such case
decision` occurs once in §1 with its nearest antecedent unmoved by 164-7.

**N17 — all six of §13.10's corrections check out**, including the one that supersedes my own F14.

**N18 — §14.2's answer on the subsection A backstop is right, and I reached it independently before
revision 4 existed.** My N5.3 and §14.2 are the same analysis: R-5's trigger is a one-way comparison
(*"is earlier than"*), its consequent fixes a day with no *"in no event later than"*, so it is a floor and
cannot bound a date that is too late. **Confirmed. The *"notwithstanding"* priority question is immaterial
to limb 1, as §14.2 says.**

**N19 — §13.1's anchor-count run is right about the counts and right to change the scope.** Over §1 at
store revision 63 every one of the six FINDs, both card (c) candidates and card (i)'s insertion point
resolves exactly once, and the delta is **+490**, which I re-ran independently. **The scope change to §1
is the correct call.** What is wrong is the claim about what the kit has always done — F21.

**N20 — nothing in §13 or §14 rests on *"where the Board does not do so."*** I checked the new text:
candidates 164-7 and 164-8, the §14 routes and the §13.3 classification contain no argument resting on
that phrase. The withdrawn argument stays withdrawn.

---

## 5. Limits of this pass

- **Cut against document revision 4 and store revision 64, both fetched today**, plus the apply kit at
  commit `60f18ca`. Both are moving; the document has moved four times and the base eleven times. **If
  §14 or the kit moves again, F21's README lines and F19's missing clause are the two things to re-check
  first.**
- **I did not re-read § 51.1-153 at source**, so §13.5's reading of it is taken from the text D 1 quotes
  and from §13.5's own report of reading it. F26 does not depend on it.
- **I did not run `verify_r63.py` or `verify_r64.py`.** I ran `verify_r6.py` (which fails — F21) and my
  own independent §1-basis reconstruction of the whole patch, which agrees with §13.1 on every count and
  on +490.
- **I did not price anything**, and F19's and F22's trades are stated in days and direction only.
  Deferred settlement is the Fiscal & Impact Modeler's.
- **I did not read store revision 63's own review (MOO-190), MOO-186's Rule 2A:2 question, or counsel's
  MOO-169 M8.** F6's escalation touches item 131's territory and should be read alongside MOO-190 rather
  than instead of it.
- **No constitutional finding on this pass either.** The deemed denial raises the one question that could
  be constitutional — whether a silent decision starts an appeal period — and it is already open on
  MOO-186 as a Rules question, not a due-process one. I am not inflating it.

---

## 6. Routing for this addendum

- **Drafting Specialist** — **F19** (add Edit 1's limb (B) to 164-7, verbatim), **F20** (one saving
  clause or two, said plainly), **F21** (retire `verify_r6.py`, fix README lines 24 and 28, put the
  §1-only scope in the apply instructions), **F23** (Edit 164-1's no-notice endpoint, after the Director
  chooses), **F26** (say what class 164-8 reaches), **F24** and **F25** (two sentences in §13.9), and
  **F2** and **F15**'s figures.
- **Policy Director** — **F19** is the one that changes what route (c) buys: as drafted, 164-7 ends the
  tolling and removes the member's reset in the same move, and one clause of Edit 1's own words fixes it.
  **F22** means §14.4's table understates the uncured class. **F23** needs your answer before words.
  **F6** has been escalated by the enactment and is now five words standing between the member and the
  route into court option (d) exists to open. My recommendation on route (c) is **adopt it, with F19's
  clause**; on F21, **fix it before anything is applied.**
- **Editor** — add **F19**, **F21** and **F22** to the risk section alongside F1, F3, F4, F5, F6 and F7's
  successor note that the reproductions are now current.
- **Statutory Researcher** — **F6** as escalated: whether *"within 90 days"* in a sentence about a filed
  request is read from filing is now load-bearing for the enacted route into court, not only for R-5.
  This sits next to MOO-186.
- **Fiscal & Impact Modeler** — unpriced trades only: F19's reset, F22's definition-request class, and
  §14.3's deferred settlement.

**Internal risk analysis. Not legal advice, not a legal opinion the organization can rely on, and
nothing in it states or implies that counsel has cleared the proposal. Pre-decisional and internal.**

---

## 7. Re-verification at store revision 65 — the twelfth base move, and the first since revision 62 to land inside a provision this cut amends

**Reproduced by `check187_r65.py` in this directory: 48 checks, 0 failures.** Run it against the live
`bill-text-s8` body as `head65.md` with the addendum's `head64.md` beside it.

### 7.1 What moved

Store revision 65 ([MOO-191](/MOO/issues/MOO-191), the designation-review advisory) makes **one
insertion in subdivision D 1** and nothing else in enacted §1:

> …or the person designated has predeceased the member and no other designation has been made; **that
> the member is advised to review the member's designation of beneficiary under subsection A of
> § 51.1-162 before completing payment;** that subsection C of § 51.1-162 provides a retirement
> allowance…

**137 characters, one line, and the line is D 1.** The script proves the isolation rather than asserting
it: enacted §1 has the same 193 lines, exactly one differs, that line is D 1, and **that line with the
137 characters deleted is byte-identical to store revision 64.** So no other word of §1 moved. The
whole document grew by 21,497 characters; all of that is §0 and §6 record.

**D 1 is not an incidental subdivision for this cut.** It is the site of **Edit 164-5**, of **candidate
164-8**, and of the ordinal cross-reference *"the second sentence of subdivision M 2"* that §13.9 warns
about. The move is therefore material and was verified, not waved through.

### 7.2 Every invariant of the cut, re-run on the new base — all hold

| Invariant | Result at store revision 65 |
|---|---|
| Six edit anchors, three bases (bare, + MOO-141 patch rev 5, + rev 6) | **1 each, 18 of 18** |
| Five held candidates (c-1, c-2, card (i), 164-7, 164-8), three bases | **1 each, 15 of 15** |
| Amendment delta | **+490 on all three bases** |
| Occurrence classification | `acts upon` 8, `act upon` 9, `acting upon` 2, `action upon` 2 — **21**, and §13.3's split row for row |
| Apostrophe normalisation | **4 U+2019, all four inside subdivision G 4, 0 elsewhere** |
| Edit 164-5's FIND (in the moved subdivision) | **1** |
| Candidate 164-8's FIND (in the moved subdivision) | **1** |

**MOO-191 used ASCII apostrophes** — its insertion contains two possessives and adds **no** U+2019, so
the normalisation record survives a move into the subdivision that could most easily have broken it.
MOO-191's insertion also contains **no** occurrence of the `act/acts/acting/action upon` family, which
is why the 21-count is unchanged.

### 7.3 Every live finding, re-tested on the new base

Nothing is discharged and nothing is escalated. **F1 remains the most serious finding in the review and
remains unanswered**: after both patches `acts upon` still occurs **nine** times in §1, **two** of them
inside Edit 164-1's own READ, and the READ still carries `in no case later than 48 days after the Board
acts upon the request`. F3, F6, F12, F19, F22, F23, F24, F25 and F26 all re-test on their words. F21 is
unchanged and still the cheapest to fix: the four anchors that differ whole-document from §1 differ by
the same amounts they did at store revision 64 (2, 2, 2 and 4 against 1, 1, 1 and 1).

The three D 1 null results were the ones at risk and all three hold: §13.4's *"first required"* still
occurs **once** in §1 and still in the filing-duty sentence; §13.5's vehicle gap is still total
(`amend`, `withdraw`, `replace`, `replacing`, `substitute`, `revoke`, `rescind` all **zero** in D 1's
now 7,351 characters); and §13.9's ordinal reference still resolves, because **MOO-191 inserted nothing
into M 2** — M 2 is byte-identical to store revision 64 — so the referent of *"the second sentence of
subdivision M 2"* is unmoved. MOO-191's insertion sits at offset 2,985 in D 1 and the ordinal reference
at 4,278, i.e. **before** it, which is harmless: the fragility §13.9 records is about insertions into
**M 2**, not into the referring subdivision.

### 7.4 Correction to my own F12 row

The addendum's **F12** row says the remaining *"the 90 days allowed by this subsection"* stands against
*"**three** instances of `the period allowed by this section for acting upon the request`."* **Three is
the count of the formula, not of that string.** After the cut the formula
`the period allowed by this section for acting upon …` occurs three times in §1, but only **two** read
*"the request"*; the third is **Edit 164-4's site and reads *"it"***, and it is in the subsection A
definition, not in M 2.

**The finding is unaffected and is arguably cleaner stated correctly.** What F12 asserts is two formulas
for one concept *inside M 2*, and inside M 2 after the cut it is **one of each**: one
*"the 90 days allowed by this subsection"* (option (d)'s expiry-notice sentence) against one
*"the period allowed by this section for acting upon the request"* (clause (ii), from Edit 164-3).
That is exactly the defect, with no reliance on the two sites outside M 2.

### 7.5 F27 — one new finding, and it is against the base, not against this cut

| | |
|---|---|
| **Severity** | **Moderate** |
| **Category** | Litigation surface / unintended effect |
| **Target** | Store revision 65's insertion in D 1, read against D 1's own failure-to-state sentence and M 2 |
| **Owner** | **Not MOO-164.** This is MOO-191's text and the Policy Director's to route — a §7 card, not an edit to this cut |

**What is wrong.** The advisory was inserted into the series governed by *"The Board's certification
shall also state that …"*, so it is a **matter this subdivision requires to be stated**. D 1's own next
sentence then provides, with no carve-out and no exception:

> **A failure to state in the Board's certification every matter this subdivision requires to be stated
> in it is a failure of the Board to state in a certification a matter this section requires to be
> stated in it for the purposes of subsection M**; a person adversely affected by it may seek review
> under subsection M…

So omitting one sentence of **exhortation** is now a reviewable failure on the same footing as omitting
the certified subsidy or the completion date. M 2 confirms the route: it gives reconsideration for *"a
failure of the Board to state in a certification or notice a matter this section requires to be stated
in it"*.

**The concrete failure scenario, with a plaintiff, a claim and a venue.** The Board issues a
certification that is complete in every substantive respect — subsidy, valuation date, completion date,
both qualifying retirement dates, the G 5 cancellation right, the whole death-benefit recital — and
omits only the new advisory. The member retires, and dies four years later without having updated a
designation made in 1998. The person who would have been designated is, in M 2's own words, a *"person
who has claimed any benefit payable on the death of a member"* and so may file for reconsideration;
D 1 expressly contemplates review by *"a person adversely affected by it"* and *"where that person is
not the member."* They plead that the omission of the advisory caused the member not to review the
designation. Under **option (d)** as enacted at store revision 63, if the Board does not act the request
is **deemed denied** and that denial is a **case decision**, which carries a right of judicial review
in circuit court under **Article 5 (§ 2.2-4025 et seq.) of the Administrative Process Act**. And the
filing tolls the member's or applicant's periods under M 2 — the clock **this cut exists to bound**.

**Why it is a finding and not a quibble.** Two reasons. First, the advisory adds **exhortation, not
information**: D 1 already stated the § 51.1-162 subsection A machinery before MOO-191 — *"subsection A
of that section provides for the payment of the member's accumulated contributions to the person the
member has designated"* — so the omission can cause no informational loss, yet it carries the same
remedy as a substantive omission. Second, it **enlarges the population** the six edits govern. Edit
164-1's cap, clause (ii) as amended by Edit 164-3 and the D 4 / D 5 retention now run for a class of
requests whose merits are a missing pleasantry. That makes the cut's repairs more useful, not less —
but it also means **F1's unbounded cases and the F19/F22 gaps are reachable on facts where nobody lost
anything**, which is the worst place to be litigating them.

**Suggested direction, one clause, with a model in the same sentence.** D 1 already knows how to switch
one consequence off for one failure: *"the second sentence of subdivision M 2 does not apply to such a
failure."* The same technique will do here — name the advisory expressly as a matter whose omission is
not a failure for the purposes of subsection M, or move it out of the *"shall also state"* series into a
provision that imposes no stating duty. **I am not recommending the words**; this is MOO-191's text, the
drafting is the Drafting Specialist's, and whether an advisory should be enforceable at all is the
Policy Director's call.

### 7.6 Running total and routing for this section

**27 findings — 0 fatal, 11 serious, 9 moderate, 7 minor — and 19 null results** (F27 added at moderate;
no finding discharged and none escalated by this base move). The six edits' verdict is **unchanged**:
cleared subject to **F1**, **F3** and **F6**; candidate **164-7** recommended **with F19's missing
clause**; **F21** to be fixed before anything is applied.

- **Drafting Specialist** — nothing new for you in §7. §7.4 is a correction to my own F12 row, not to
  your text, and it leaves F12 standing.
- **Policy Director** — **F27** is yours to route and it is **not** a MOO-164 item. The cut's anchors,
  delta, classification and apostrophes all survive the twelfth base move with 0 failures, so no
  re-cut is needed on account of store revision 65.
- **Editor** — the risk section needs **no** change from §7 except that the base is now store
  revision 65. **F27** belongs in a MOO-191 note, not in this cut's risk section.

**Internal risk analysis. Not legal advice, not a legal opinion the organization can rely on, and
nothing in it states or implies that counsel has cleared the proposal. Pre-decisional and internal.**
