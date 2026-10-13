
---

## 17. Revision 7 — [MOO-209](/MOO/issues/MOO-209)'s counsel pass folded, and the base at store revision 70

**[MOO-209](/MOO/issues/MOO-209) is `done`: 16 findings (0 fatal, 5 serious, 5 moderate, 6 minor) and
12 null results, taken on an applied copy the reviewer built themselves rather than on my prose.
No finding is rejected. One fix direction is declined on drafting grounds and the words are drafted
at §17.9 so the Policy Director can overrule me in one line.**

Revision 7 **re-cuts three applied edits, adds one, holds one new candidate, and corrects sixteen
statements in place**. §17 is the only part of this document added at revision 7; §6 is re-spliced.
**No decision in §0 to §16 is reversed. Nothing is applied to the store.**

### 17.0 The sixteen findings and what each one did

| | Finding | Severity | Disposition |
|---|---|---|---|
| **F1** | 164-7's exception misses R-6's notice duty | **serious** | **Taken.** 164-7 re-cut, §17.1. **And one limit disclosed, not drafted around** — question **3** |
| **F2** | *"satisfies § 51.1-153"* strips subsection E's cap | **serious** | **Taken as counsel drafted it** — three words deleted. §17.2 |
| **F3** | the supersession has no temporal limit | **serious** | **Taken.** Confined to the member's own notice, with a post-retirement bar. §17.2 |
| **F4** | the new right has no disclosure duty | **serious** | **Taken** as new **Edit 164-13**, plus one repair MOO-209 did not raise. §17.4 |
| **F5** | the 48-day derivation is still wrong; a verifier line counts a true string under a false label | **serious** | **Taken in full.** Record re-cut, the verifier line **deleted**. §17.6. **Bears on [MOO-204](/MOO/issues/MOO-204)** |
| **F6** | 164-12's notwithstanding is surplusage with a negative implication | moderate | **Taken.** Deleted. §17.5 |
| **F7** | *"the identical date"* / *"two provisions… agree"* | moderate | **Taken.** Same event and same formula, not the same date. §17.7 |
| **F8** | subsection C cannot report an M 2 duty; J 1 misquoted | moderate | **Taken.** §7.3 re-cut. §17.7 |
| **F9** | two deemings, one confinement clause, no cross-reference | moderate | **Half discharged by the base, half taken.** §17.3, §17.8 |
| **F10** | *"grants or denies"* leaves pendency open-ended | minor | **Carded as candidate 164-14, HELD** — it changes (c-2)'s cost profile. Question **1** |
| **F11** | §3.8's counted claim is false as counted | minor | **Taken.** §17.7 |
| **F12** | the B 4 f extension is inoperative | minor | **Kept, and the count recorded.** §17.8 |
| **F13** | *"it"* is determinate only by semantic constraint | minor | **DECLINED on drafting grounds.** Words drafted. §17.9 |
| **F14** | *"an application"* against *"the application"* | minor | **Left as cut, with the reason.** §17.8 |
| **F15** | the open case names one of M 2's seven standing classes | minor | **Taken.** §17.7 |
| **F16** | the *"shall act upon"* verifier line tests a string, not the proposition | minor | **Taken.** §17.8 |

**Measured, not predicted.** `verify_r70_v7.py` reports **0 failures** at store revision 70:
**thirteen substitutions, delta +3,375**, on three bases, every anchor exactly once in enacted §1.
Revision 6 was eleven substitutions and +2,551.

---

### 17.1 F1 — the serious one. 164-7's exception is extended, and the one thing it does not cure is stated rather than drafted around

**The finding.** 164-7's saving blocks the deeming from determining *"the date by which the Board is
required … to give a notice or a decision."* Its one express exception named only M 2's 15-day duty
on the application. So **R-6** — the definition's *"where the Board does not [state the date in its
decision] it shall give the member written notice of that date no later than 15 days after it acts
upon the request"* — was **not** reached. In trigger two's class the member got a later retirement
date by operation of Edit 164-4's floor, **no notice duty ever fell due**, D 1's lateness sentence
never fired because nothing was given, and **Edit 164-8's own vehicle never fired for the same
reason**. A permission with no vehicle — the §13.5 defect, reappearing inside the case 164-7 was
promoted to cure.

**I accept it without qualification, and the reason it matters is that it was invisible from the
inside.** §3.7 stated what 164-7 left open and this was not in it.

**The cure, as counsel named it: extend the exception. One clause, no new number, the section's own
words.** 164-7's exception now reads:

> Except for the purposes of the duty of the Board under this subsection to act upon an application
> no later than 15 days after it acts upon the request **<u>and the duty of the Board under the
> definition of "final qualifying retirement date" in subsection A to give the member written notice
> of the member's final qualifying retirement date</u>**, nothing in the preceding sentence
> determines the date by which the Board is required to act upon a request, to make a determination,
> or to give a notice or a decision, or whether the Board has performed such a duty within a period
> required by this section.

**+184 characters. 164-7 goes from +1,153 to +1,337.**

**One drafting choice inside it, and it is the whole of the next sub-section.** The exception
describes R-6 **by the duty** — *"to give the member written notice of the member's final qualifying
retirement date"* — and **not by its deadline formula**. The obvious lift would have been the
descriptor already in the sentence, *"no later than 15 days after it acts upon the request"*, which
resolves **twice** in the base and would have named R-6 in four words. **I did not use it, because
MOO-141's Edit 2 re-keys R-6's 15 days off the Board's act**, and a descriptor keyed to the deadline
would then describe nothing. Counted on both bases by the verifier.

**What the cure buys.** The Board's silence becomes a breach of a notice duty, which **J 1 expressly
reports** (*"every failure of the Board to make a determination, or to give a notice, within a period
required by this section, stated separately for each provision"*). When the notice is eventually
given it is **late**, so D 1's lateness sentence fires and **Edit 164-8's vehicle fires with it**.

**What it does not buy, and counsel said so first: the Board that never gives the notice at all.**
D 1's lateness trigger keys to the Board *giving* a document *"later than the time required"* — not
to the expiry of the time required. Nothing is given, so nothing fires. **Curing that means re-keying
D 1's lateness trigger to an expiry, which is a different and much larger change, and I am not
drafting it.** It is recorded here and routed to [MOO-42](/MOO/issues/MOO-42)'s §7.

### 17.1a The MOO-141 Edit 2 interaction — **question 3**, and the one thing in revision 7 I cannot close by drafting

**Stated plainly: F1's cure is operative on store revision 70 as it stands and goes INERT once
MOO-141's Edit 2 lands, and the reason is not a defect in either patch.**

| | R-6's 15 days runs from | Does 164-7's deeming reach it? | Is F1 cured? |
|---|---|---|---|
| store revision 70, this cut alone | **the Board's act** | **yes** — the confinement clause reaches periods *"measured from … the Board's acting"* | **yes** |
| + MOO-141's Edit 2 | **the giving of its decision** | **no** — the deeming reaches no period keyed to a giving | **no**, and in a new form |

**After Edit 2, R-6 is a duty keyed to an event that in the deemed case never occurs.** That is
*exactly* limb 3's shape — the defect route (c) was adopted to cure — relocated from M 2 to the
definition by a patch that is not mine. **Both counts are in the verifier, so this is visible and not
argued.**

**Three things follow, and none of them is mine to choose.**

1. **The two patches each remain correct standing alone**, which is why the cure is applied rather
   than withheld. Order-independence is unaffected: the delta is +3,375 on all three bases.
2. **The combined text needs one more limb, and it belongs to MOO-141's Edit 2**, which is the
   provision that moves R-6's key. The smallest form I can see is a second limb in Edit 2 for the
   case where no decision is given. **I have told [MOO-141](/MOO/issues/MOO-141) and I have not
   drafted into their patch.**
3. **I will not make 164-7's deeming reach a *giving*.** Deeming a decision to have been given when
   it has not been would start the member's own clocks without her knowledge — the precise harm
   Decision 2 exists to prevent, and card (b)'s whole subject. **That is a line I am not crossing by
   drafting choice.**

---

### 17.2 F2 and F3 — Edit 164-8 re-cut. The edit gets **shorter** in one place and bounded in another

**F2. *"[S]atisfies § 51.1-153"* was stated flat, and D 1 defers to subsection E of that section
twice.** Subsection E caps retroactivity: *"[t]he effective date of retirement … shall not be more
than 90 days prior to the filing of the notice of retirement."* D 1's own retroactivity sentence and
its clause (ii) are both *"subject to subsection E of § 51.1-153."* Mine was not. So 164-8 either
overrode subsection E by implication — an unflagged amendment to Chapter 1 that nothing in this cut
discloses — or was read down, in which case the words were false for the date the member most wants.

**Taken exactly as counsel drafted it: delete the three words. −22 characters.** They were
surplusage. 164-8 already deems the replacement *"filed within the period allowed by this
subdivision"*, and **D 1's existing sentence then does the work with the subsection E qualification
attached**: *"A notice filed within the period allowed by this subdivision satisfies § 51.1-153 …
subject to subsection E of § 51.1-153."* The verifier asserts the deletion **and** that D 1's own
sentence still carries the qualification, so the work is provably still done somewhere.

**And I will name my own error rather than the finding.** I wrote an unqualified restatement of a
rule the subdivision states twice with a qualification. **Do not restate a rule you can cross-refer
to** — that is §9.6's own principle, applied against me.

**F3. The supersession had no temporal limit, so it purported to unmake a retirement that had
already taken effect** — five months of allowance paid under a notice that no longer exists, a G 1
election unsettled, and the member pushed into a G 2 determination with its reduction and refund
machinery. Two smaller defects in the same eleven words: *"any notice previously filed"* was
unbounded **as to kind** (D 1 uses *"notice"* for the Board's own documents) and **as to filer**.

**Taken, as counsel drafted it.** The tail now reads:

> and a notice so filed is filed within the period allowed by this subdivision ~~, satisfies
> § 51.1-153,~~ and supersedes any notice **<u>of retirement</u>** previously filed **<u>by the
> member, except that no notice may be filed under this sentence after the member's retirement has
> taken effect</u>**.

**The trade is honest and I state it rather than let the words imply otherwise: the member whose
retirement has already taken effect gets nothing from this vehicle.** Counsel's sentence on it is
the right one — pretending otherwise buys a payment problem rather than a remedy. **The class 164-8
exists for is the member whose single filing window closed while her request was pending and who has
therefore *not* retired**, and the bar does not touch her.

**164-8 goes from +485 to +621.** `replacing a notice already filed` is conformed to `replacing a
notice of retirement already filed by the member` in the same breath, because the same two defects
sat in that phrase.

---

### 17.3 The two savings after F1 — the asymmetry is **principled**, and that is a change from what §16.6 asserted

At revision 6 the verifier asserted the two savings were **symmetric**: two savings, two exceptions,
each naming one duty, one naming *"this subsection"* and one *"subsection M"*. **After F1 they are
not symmetric — 164-7's exception names two duties and MOO-141 Edit 1's names one — and I have to say
whether that is a defect.**

**It is not, and the reason is the same fact as §17.1a.**

- **164-7 must except R-6**, because its deeming addresses the Board that **never acts**, and in that
  case there is no decision for R-6's duty to key to. Without the exception, R-6 is dead in the one
  class the deeming exists to reach.
- **Edit 1 need not**, because its deeming addresses the Board that **acts twice** — a case in which
  a decision does arrive — and because **MOO-141's Edit 2 re-keys R-6 to the giving of that
  decision**. Edit 2 is MOO-141's answer for R-6, and it is a better one for the two-act case than an
  exception would be.

**So the asymmetry tracks a real difference in what the two deemings do.** The verifier now asserts
the shape rather than the symmetry: two savings, two exceptions, **neither bare**, each naming a
different subsection, and the saving's 256-character body **byte-identical** between them — which is
**N1**, the claim that was stated as *"word for word"* twice and was false twice. It is now a counted
assertion, which is the only form that claim should ever take again.

**What survives of F9, and it is a record item not a text item.** The section would carry **two
deeming sentences with the identical 44-word confinement clause, in two subsections, with neither
cross-referring to the other** and nothing on the face of either saying which question it answers —
one answers *which* act, one answers *what if none*. **Counsel's routing is right and I adopt it: the
two deemings should land as one joint decision with an express cross-reference, not as two
independent patches.** That is a question for the Policy Director across both issues and it is posted
on [MOO-141](/MOO/issues/MOO-141), not resolved here.

**Also corrected: §16.6's test was too strong.** It asserted *"no existing occurrence is amended or
changed in meaning."* Counsel is right that *"changed in meaning"* cannot be true of a deeming —
changing what existing occurrences mean in the deemed case is the whole point. **The defensible form,
adopted at revision 7: no occurrence is re-worded, and none acquires a different date where the
section already fixed one.** Decision 1 is honoured on that test, and the verb census is 21 in the
base against 31 applied with every new occurrence attributed.

---

### 17.4 F4 — new **Edit 164-13**: the conforming disclosure amendment, in two substitutions inside one sentence of D 1

**The finding.** The sentence immediately after 164-8's insertion point requires the Board to state
**(i)** the extension, **(ii)** the effective-date permission and **(iii)** the three-day mailing
extension, in the statement and in every notice of a later approved date. **164-8 adds a fourth
consequence of exactly that family — a 30-day window to file or replace the § 51.1-153 notice — and
added no clause (iv).** The member reads that she *"may state"* a later effective date, is told of no
vehicle, and lets the 30 days run. The Board has complied with every duty in the subdivision. **A
window the only document she receives does not mention is not a remedy.**

**Taken. And this is the finding I would have wanted raised against me, because 164-8 was promoted on
the ground that it supplies a vehicle for a permission that had none — and a vehicle nobody is told
about is the same defect one level up.**

**164-13(a) — the disclosure duty reaches the third document.** The sentence listed two documents;
164-8's trigger reaches **three**. The one it missed is Edit 164-5's descriptor, *"any notice of a
date required by that definition by reason of the Board's action upon a request"* — which is R-6's
notice, the document trigger two's class turns on.

> The Board shall state, in the written statement required by that definition**<u>,</u>** ~~and~~ in
> every notice of a later approved date required by that definition, **<u>and in every notice of a
> date required by that definition by reason of the Board's action upon a request</u>**, (i) …

**+103 characters.** Note it uses the **conformed** descriptor, so 164-5 and 164-13 cannot diverge.

**164-13(b) — clause (iv), and one repair MOO-209 did not raise.**

> ~~; and~~ **<u>;</u>** (iii) that where the Board mails the statement or notice, every period that
> runs from the giving of it is extended by three days**<u>; and (iv) that where the Board gives a
> notice described in this sentence after the expiration of the period allowed by this subdivision
> for filing the notice of retirement required by § 51.1-153, the member may file that notice of
> retirement, or a notice replacing a notice of retirement already filed by the member, no later than
> 30 days after the Board gives that notice, and that no such notice may be filed after the member's
> retirement has taken effect</u>**.

**+454 characters. Edit 164-13 totals +557 across two substitutions.**

**The repair counsel did not raise, and the base did.** Adding a fourth item to a series whose
conjunction sits before the third would leave **two** *"and"*s in one series. **Store revision 70 set
the precedent in this very subdivision** — its substitution 3 moved D 1's certification series'
*"and"* to the new last item, for 4 characters. I have done the same, and the verifier asserts it in
both directions: exactly one *"; and ("* in the series, before **(iv)** and not before **(iii)**, and
clause (iii) otherwise unchanged. **−4 characters, and it is the reason the delta is +3,375 and not
+3,379.**

**Clause (iv) discloses the limit as well as the right**, because clause (i) already discloses its
own limits (*"subject to the limits stated in that definition"*) and a disclosure that overstates a
right is worse than none. **Who, what, by when, or else:** the actor is the Board, the object is the
four statements, the occasion is each of three documents, and the consequence is J 1's report, which
reaches *"every failure … to state a matter this section requires to be stated."*

---

### 17.5 F6 — 164-12's notwithstanding is deleted. Counsel is right that it was **more** than enough

**The finding.** G 4's definition opens *"**For the purposes of this subdivision** an application for
a disability retirement allowance is pending …"* — counted, once, unamended. **It never travelled
into G 2. There was nothing to notwithstand.** And §4.2's premise — that subsection G would define
*"pending"* twice and a court would harmonise — is not made out, because **a word confined twice is
not a word defined twice.**

**The consequence is the part that decided it.** A litigant reads the notwithstanding as the drafter's
acknowledgment that, but for it, G 4's confinement **would** have reached G 2 — and then says the same
about every other confinement clause in the section with no notwithstanding beside it. **Enacted §1
carries seven clauses of that family.** The clause bought presentational comfort in G 2 by weakening
six confinement clauses elsewhere. **That is a bad trade and I made it.**

**Taken: delete `Notwithstanding the definition in subdivision 4, and `, and capitalise. −53
characters. 164-12 goes from +220 to +167.** It now reads:

> **<u>For the purposes of this subdivision, such an application is pending from the date on which
> the member files it until the date on which the Board grants or denies it.</u>**

**Where the divergence goes instead, exactly where counsel put it and where the Director had already
directed it: the §0 record and the designation-review read-through.** The Policy Director's
disposition of question 1 said the board must be **told**, in that read-through, that subsection G
will define *"pending"* twice, differently, in adjacent subdivisions, deliberately. **That statement
is unaffected by F6 — it is still true, and it is still the right channel. What F6 removes is the
attempt to say it in the operative text.**

---

### 17.6 F5 — the 48-day cap is a **chosen outer limit**, and a verifier line was counting a true string under a false label

**This is the finding I would least like to have left standing, because the false form of it is the
form [MOO-204](/MOO/issues/MOO-204) was asked to price against.**

§16.2 fixed the mailing half of the derivation and left the load-bearing half. Three things, all of
them counsel's and all of them right:

1. **The 15 belongs to a different document.** R-6's 15 days governs a notice of the member's **final
   qualifying retirement date**, and only *"where the Board does not state that date in its
   decision."* Edit 164-1's endpoint runs 30 days from *"written notice of **its decision** upon the
   request."* Different document.
2. **No provision of the section requires that document by any date.** *"[N]otice of its decision"*
   resolves **0 times** in enacted §1 at store revision 70 and **1** time only because Edit 164-1
   adds it — both counted. For a request under the definition the governing duty is *"written notice
   of its determination and of the reasons for it, no later than 30 days after the request is
   filed"* — the same deadline as the act. **For a request for reconsideration there is no deadline
   at all.**
3. **So *"nothing reaches past 48"* is false.** Definition request, Board acts on day 1 of the
   30-day window, gives notice of its determination on day 30 — every duty met — and mails it:
   the uncapped notice-keyed endpoint is **act + 29 + 30 + 3 = act + 62**. Reconsideration request:
   **unbounded**.

> **THE CORRECTED STATEMENT, which replaces §2.2's route table and §9.3's claim.** **48 is a chosen
> outer limit.** The periods it displaces are **act + 62** for a request under the definition with
> every duty met, and **unbounded** for a request for reconsideration. **The claim that *"every
> number in it is already in the section"* does not hold, and is withdrawn.** What survives
> unchanged: **the figures 15, 3 and 30 are each in the section**, the **+18** movement figure
> (48 − 30) follows from the cap itself and is unaffected, and clause (ii)'s **120-day** aggregate
> still binds on top.

**The script was wrong in the way I said I would rather hear about.** `verify_r68_v6.py` and
`verify_r69_v6.py` asserted a line labelled *"the definition's 15-day notice backstop, which supplies
the 15 in 48 = 15 + 3 + 30"* at count 1. **The string was there; the proposition in the label was
false; and a check that counts a string cannot detect that.** The line is **deleted** at revision 7,
not relabelled, and replaced by a count of the duty the endpoint actually keys to — **of which there
is none**, which is the finding itself.

**What this changes for [MOO-204](/MOO/issues/MOO-204), and it is the Policy Director's to action.**
MOO-204 priced candidate **164-9** — the two-limb cap that closes the remaining 60 days — and it is
`done`, with the answer *take it, with 164-10*. **The pricing is not disturbed; the framing around it
is.** MOO-204 was told the cap *"merely restates the section's arithmetic."* It does not. **164-9
remains HELD and cross-referenced; the Policy Director's standing answer on question 7 of the
revision-5 set was to keep the cap and treat the 60 days as a priced decision, and nothing in F5
disturbs that answer — only the sentence that justified it.**

---

### 17.7 F7, F8, F11 and F15 — four record corrections, each taken

**F7 — *"the identical date"* is not accurate: same triggering event, same formula, different date,
and a wider class.** Two provisions:

| | Formula | On a request filed 1 July, 30 days expiring 31 July |
|---|---|---|
| **R-5's floor** (Edit 164-4) | *"the first day of the second month following the month in which that period expired"* | **1 September** |
| **164-7's trigger two** | *"the day after the expiration of that period"* | **1 August** — and R-3 then gives **1 October** |

**No harm follows**, because R-5 bites only *"where the date that would otherwise apply … is
earlier"* and the member takes the later; **but the two provisions do not *"agree"*, and the
resolution is the floor mechanism, not agreement.** And **the classes differ**: R-5 reaches *"a
request the filing of which tolled"* her date — **which includes a request for reconsideration** —
where trigger two reaches a definition request only. **R-5 is wider.**

**Corrected everywhere it appears: the same triggering event and the same formula.** That is enough
to carry the point the Policy Director's question-9 reasoning needs — **that trigger two invents no
bound** — and that reasoning is unaffected. *"The identical date"* and *"two provisions about one
date now agree"* are withdrawn. **This is §16.2's defect in a second place: the figure was right and
the sentence explaining it was wrong**, and twice in one document is a pattern, not a slip. **The
rule I am taking from it: an identity claim is a counted claim.** Both formulas are now in the
verifier's formula census and the divergence above is in the record.

**F8 — §7.3's *no new duty* conclusion holds; its stated basis did not.** Both halves were wrong:

- **Subsection C** reads *"every failure to make a determination, to state a matter **this
  subsection** requires it to state, or to give a notice, **required by this subsection** within the
  period **this subsection** allows for it."* It is confined to subsection C's own duties. **It
  cannot report a failure of an M 2 duty at all.** Dropped from the claim.
- **J 1** reads *"every failure of the Board to make a determination, **or to give a notice**, within
  a period required by this section, stated separately for each provision."* **No payment limb.** The
  string I attributed to it — with the payment limb — resolves once in enacted §1 and it is **M 2's
  own standing sentence**, not either report line. Now quoted correctly.

**The conclusion survives on J 1 alone**, and only if a failure *to act upon an application* is a
failure *to make a determination*. That is the right reading on ordinary meaning, and I record
counsel's counterweight rather than bury it: **the bill's own practice elsewhere is to attach an
express report line to each duty — five instances of *"shall state in the report required by
subsection J every failure to …"* — and M 2's 15-day duty has none.** No amendment is recommended;
the J 1 catch-all would take *"or to act upon an application"* if the Policy Director wants the route
beyond argument, and counsel does not recommend it over the ordinary-meaning reading. **Neither do
I.** **And note F1 strengthens this**, not weakens it: the extended exception puts R-6's notice duty
squarely inside J 1's *"or to give a notice"* limb, which is express.

**F11 — §3.8's counted claim was false as counted.** `amend` occurs **once** in D 1, in *"§ 401(a)(37)
of the Internal Revenue Code, **as amended or renumbered**."* Immaterial to the premise — it is not a
power over a notice — **but false as stated, and a counted claim that is false as counted is the
thing this document most needs not to do.** Restated: *no occurrence of any of the four in any sense
bearing on a filed notice; `amend` occurs once, in the Internal Revenue Code formula; `withdraw`,
`replacing` and `substitute` are 0 as claimed.* **The §13.5 premise that Edit 164-8 rests on is
unaffected — D 1 still has no power to amend, replace or withdraw a filed notice.** The other half
of that premise did move, and it is **F2**.

**F15 — the open case names one of M 2's seven standing classes.** I wrote *"the member who files a
reconsideration request and never files the expiry notice."* M 2's standing list has **seven**
classes, and the enacted expiry notice is given to *"the person who filed the request"* — who may be
a personal representative of a deceased member's estate or a state agency. **Corrected to the
enacted sentence's own phrase, *the person who filed the request*, everywhere the open case is
stated.** This is the same defect as naming a duty without naming its actor, committed in the note
instead of the text.

---

### 17.8 F9's surviving limb, F12, F14, F16, N1, N2, and counsel's answer to question 2

- **F12 — the B 4 f extension is inoperative on the present text, and it is KEPT.** The act-upon
  family resolves **0 times anywhere in § 51.1-142.2** — the verifier now slices that section out of
  §1 and counts it, so the next reader does not go looking for the provision the clause reaches. It
  mirrors M 2's tolling sentence, which names B 4 f for a different purpose (periods within which the
  **member** must act), and it is 46 characters of insurance against a future amendment. **Counsel's
  cure was *keep it and record the count*; that is what is done.**
- **F14 — *"an application"* against *"the application"*: left as cut, and here is why.** The
  descriptor resolves once, the duty it names resolves once, and D 3's similar 15-day application
  duty is keyed to *"after the confirmation is obtained"* and cannot be caught. **Conforming the
  article would de-synchronise 164-7's exception from MOO-141 Edit 1's, which uses the same words**,
  and N1's byte-identity assertion is worth more than the article. **Recorded, per counsel, because
  the exception's safety rests on the descriptor matching exactly one duty and a reviewer should know
  it is not a verbatim lift of the duty's own words.**
- **F16 — taken.** The verifier asserted *"every 'shall act upon' duty states a commencement"* by
  counting 164-10's own sentence at 1. It now **searches for a commencement phrase inside each of the
  five occurrences** and asserts 5. Counsel checked all five independently and the proposition is
  true; it is now tested.
- **N1 — taken, and it is the most important null result in the pass.** The saving's 256-character
  body is asserted **byte-identical** between 164-7 and MOO-141 Edit 1. The *"word for word"* claim
  was made twice and was false twice (F19, F20). **It is now a count, and `verbatim` will never
  again appear in this document as prose where it can appear as an assertion.**
- **N2 — taken in its stronger form.** The verifier asserted adjacency only for the new
  *"preceding sentence"* references. It now counts the base and the applied text and asserts that
  revision 7 adds **exactly three** — two in 164-7, one in 164-8 — with **164-13 adding none**,
  because it says *"this sentence"*. Counsel re-resolved all 22 in the applied text against their
  actual predecessor and found 19 pre-existing references unchanged; I have not re-done their work
  and I am not claiming it as mine.
- **Question 2, answered by counsel: do not convert 164-7's two *"preceding sentence"* references.**
  **Accepted.** *"The preceding sentence"* is the bill's own instrument — 18 occurrences in enacted
  §1, plus one *"the two preceding sentences"*, and **zero** cross-references by content paraphrase.
  Converting these two would make 164-7 the only provision in the section that cross-refers by
  paraphrase, against §9.6's own principle. **The two instruments are different risk classes**: D 1's
  *"the second sentence of subdivision M 2"* is an absolute ordinal into another subdivision and
  breaks silently on any insertion before M 2's second sentence; *"the preceding sentence"* is
  relative and adjacent. **Counsel's one addition is adopted: the adjacency requirement goes into
  MOO-42's §7 record in the words a future drafter will search for**, because a verifier can only
  protect the base it was written against.

---

### 17.9 F13 — **declined on drafting grounds**, with the words drafted so the Policy Director can overrule me in one line

**The finding.** In 164-7's trigger two, *"within the period allowed by this section for acting upon
**it**"* has four singular nouns between *"a request"* and *"it"* — *the definition*, *subsection A*,
*the period*, *this section*. None can be *"acted upon"*, so the antecedent is the request and
**counsel says the reading is secure**. But the last-antecedent rule points the wrong way, the
sentence then uses *"the request"* five times, and it contains two different request concepts.
**Counsel's cure: *"for acting upon that request"*, +10 characters.**

**I decline it, and the reason is card (j).** The phrase is a **conformed term**. Edits 164-3, 164-4,
164-6, 164-7 and 164-11 exist so that *"the period allowed by this section for acting upon …"* stands
at **five** sites and every variant at **none** — that is the whole of card (j) and the conforming
amendment at §7.3. **Counsel's cure introduces a sixth variant of the term, to defeat an argument
counsel itself calls secure.** And the same *"it"* already sits in **R-5** after *"subsection M"*,
which Edit 164-4 points at the section: so the pattern is consistent across the two provisions
§17.7 is about, and breaking it in one of them is worse than the ambiguity.

**Trading a real conforming gain at five sites for a hypothetical reading gain at one is not a trade
I will make by drafting choice.** But it is **+10 characters and no figure moves**, so it is cheap if
the Policy Director disagrees:

> **Candidate 164-7-F13, drafted and not applied.** In Edit 164-7's trigger two, for *"for acting
> upon it"* read *"for acting upon that request"*. **+10 characters.** Consequence, counted: the
> formula census becomes **4 at `… for acting upon the request` / 1 at `… it` / 1 at `… that
> request`**, and the variant count goes from **0 to 1**. If the Policy Director takes it, **Edit
> 164-4's R-5 site should take it too**, or the inconsistency simply moves — and Edit 164-4 is card
> (l) and settled, so that is a reopening and not a repair.

---

### 17.10 F10 — candidate **164-14**, HELD. This one changes (c-2)'s cost profile, so it is not mine. **Question 1**

**The finding.** *"[G]rants"* and *"denies"* each resolve **0 times in enacted §1** before Edit
164-12, and § 51.1-156 does not use them — the Medical Board *"shall certify … that the member should
be retired."* The section's own words for the same event, in the adjacent subdivision, are *"the date
on which the Board **first acts upon it**"* and *"**approved for** a disability retirement allowance
under this chapter."*

**The gap.** The Board neither grants nor denies: it **defers** pending further medical evidence, the
application is **withdrawn**, or it is **closed administratively**. Under G 2 as amended by 164-12 the
application is then **pending indefinitely**, so item 46's carve-out validates every allowance paid
for as long as that lasts. **Under G 4's words it would have ended at the first act.** Counsel
confirms §4.2's *"nobody loses"* holds — the no-recovery limb exists and the Commonwealth bears it
(N9) — **but the amount between the first act and a disposal that never comes is unbounded and
unpriced.**

> **Candidate 164-14, drafted and NOT applied.** In Edit 164-12, for *"until the date on which the
> Board grants or denies it"* read *"until the date on which the Board grants or denies it **<u>or
> the application is otherwise disposed of</u>**"*. **+39 characters.** Its FIND resolves **0** times
> in the base and **1** in the applied text — both asserted — so it goes in after Edit 164-12 or not
> at all, exactly like 164-9.

**Why it is held and not applied, and this is the Policy Director's own reasoning turned back on the
candidate.** The disposition of question 1 took **(c-2) over (c-1)** and declined to put an item-46
card to the board, on the express ground that **(c-2) confirms item 46 exactly as enacted and costs
nobody anything**. **164-14 narrows pendency, and narrowing pendency shortens the period the
carve-out validates.** The incidence still falls on the Commonwealth either way, because the
no-recovery limb absorbs it — so **no member loses** — but the Commonwealth's exposure changes, and
*cost-neutrality was the reason (c-2) needed no board card*. **Applying 164-14 silently would spend
that reasoning without saying so.** I am not doing that.

**Question 1, with my recommendation.** **Take it.** An unbounded, unpriced open end at a carve-out
is worth 39 characters to close, the words are the ordinary administrative-law residue, and the
alternative — *"until the date on which the Board first acts upon it"* — would collapse the
divergence from G 4 and so defeat (c-2)'s entire purpose, which is why counsel ruled it out and so do
I. **If the Fiscal & Impact Modeler should see the open end first, that is a one-line question to
them and it does not block anything in this cut.**

---

### 17.11 The base at store revision 70 — §6 re-spliced for the **eighth** time, and the verification

**Store revision 70 landed between the Policy Director's disposition and this cut.** It is the
Director's own composite of [MOO-191](/MOO/issues/MOO-191), commissioned at
[MOO-208](/MOO/issues/MOO-208): six substitutions, **four of them inside subdivision D 1** and one in
the **title line**. Whole document **515,219**; enacted §1 **132,557** (revision 6 was cut at
131,066 and re-verified at 131,923).

| | What moved | Reproduced at §6? | Anchor moved? |
|---|---|---|---|
| store rev **69** | subdivision **G 4** rewritten; subsections B and L exchanged a sentence | **G 4 yes** | no |
| store rev **70** | **D 1** — the certification series' new item 7, the subsection M exception, the subsection J limb, the series' *"and"*; and the **title line** | **D 1 yes**, title yes | no |

**Eighth stale reproduction behind anchors that all still resolved exactly once.** `repro70.py`
re-splices all of them **by content, not by line index**, and now also reproduces the **title line,
enacting clause and first enactment** so §5 cannot go stale silently either.

**What store revision 70 did *for* this cut, unasked.** Its substitution 3 **moved D 1's
certification series' *"and"* to the new last item** — the identical repair Edit 164-13(b) needs for
the disclosure series. **That is the fourth time somebody else's revision has made an argument of
mine for me**, and it is why §17.4's series fix is a precedent rather than a preference.

**`verify_r70_v7.py` — 0 failures.** Every figure in §17 is counted by it.

| | |
|---|---|
| Anchors | **13 substitutions, every FIND exactly 1** in enacted §1, on **three** bases |
| Delta | **+3,375 on all three bases** — so still **order-independent of the MOO-141 patch and still indifferent to the 30/120 answer**, now at a **fifth** store base and for thirteen substitutions |
| Per-substitution deltas | summed by the script and asserted against the measured total, so the table below is counted and not added up by hand |
| MOO-141 fixture | cross-checked at their published **+847**, Edit 3 at 120 days; **+846** at 30 days |
| Verb census | **21** in the base, **31** applied, **26** with the MOO-141 patch, **36** with both |
| Formula | **5** sites, **every variant at 0** |
| *"no later than"* | **74** in §1, unchanged |
| clause (ii) | **300 days unconditionally** — m8-a's proviso resolves once and survives Edit 164-3, both counted |
| Apostrophes | **4**, still all inside G 4, against **206** straight |
| F21 | five of the thirteen FINDs resolve more than once whole-document — 164-10's **four** times. `apply164.py` slices §1 and asserts byte-identity outside it |

**The thirteen substitutions, measured.**

| Edit | Site | Revision 6 | **Revision 7** |
|---|---|---|---|
| 164-1 | M 2, the tolling endpoint | +233 | +233 |
| 164-2 | G 2, the 120-day exception | +366 | +366 |
| 164-3 | M 2 clause (ii) | +24 | +24 |
| 164-4 | the definition, R-5 | +1 | +1 |
| 164-5 | D 1, the lateness descriptor | +8 | +8 |
| 164-6 | G 4, the period formula | +10 | +10 |
| **164-7** | M 2 — the deemed act and its saving | +1,153 | **+1,337** (F1) |
| **164-8** | D 1, the filing vehicle | +485 | **+621** (F2, F3) |
| **164-13(a)** | D 1, the disclosure duty's document list | — | **+103** (F4) |
| **164-13(b)** | D 1, clause (iv) and the series' *"and"* | — | **+454** (F4) |
| 164-10 | M 2's 90-day duty, commencement | +27 | +27 |
| 164-11 | M 2's expiry-notice sentence | +24 | +24 |
| **164-12** | G 2, item 46's carve-out | +220 | **+167** (F6) |
| | **total** | **+2,551** | **+3,375** |

**Held, and the numbers are reserved not reused: 164-9** (the two-limb cap, priced at
[MOO-204](/MOO/issues/MOO-204)), **164-14** (F10, question 1), **164-7-F13** (F13, §17.9).
**Retired: (c-1)** — the verifier still asserts its FIND resolves once **unamended**, which is how it
proves Edit 164-12 leaves G 4 alone. **Declined: card (i)'s 33-word confirming sentence.**

**One thing I did not do, stated so it is not mistaken for having been done.** I have **not** re-read
store revisions 66, 67, 69 or 70 for substance beyond the provisions this cut touches. The verifier
proves nothing in them moved an anchor, a count or a quoted figure; **it does not prove nothing in
them bears on the two decisions.** [MOO-200](/MOO/issues/MOO-200) is the right place for that, as the
Policy Director said of their own run.

---

### 17.12 Questions for the Policy Director — **three**

**1. Candidate 164-14 (F10) — close 164-12's open end?** *"[O]r the application is otherwise disposed
of"*, +39 characters. **I recommend taking it.** It bounds an unbounded, unpriced exposure. **It is
yours and not mine because it narrows (c-2), and (c-2)'s cost-neutrality is the express reason you
declined to put an item-46 card to the board.** No member loses either way — the no-recovery limb
absorbs it — but the Commonwealth's exposure changes. §17.10.

**2. F9's surviving limb — do the two deemings land as one joint decision?** After both patches the
section carries two deeming sentences with the identical 44-word confinement clause, in two
subsections, **with neither cross-referring to the other**, one answering *which act* and one
answering *what if none*. **Counsel's routing is that they should land as one decision with an
express cross-reference, and I agree.** This is a question across this issue and
[MOO-141](/MOO/issues/MOO-141), posted on both. **I have not drafted the cross-reference, because
drafting it unilaterally into either patch is how the two would diverge again.** §17.3.

**3. The MOO-141 Edit 2 interaction — who cures R-6 on the combined text?** F1's cure is **operative
on store revision 70 and inert after MOO-141's Edit 2**, because Edit 2 re-keys R-6 off the Board's
act. On the combined text R-6 becomes a duty keyed to an event that in the deemed case never occurs —
**limb 3's shape, relocated to the definition by a patch that is not mine.** Both counts are in the
verifier. **My recommendation: a second limb in MOO-141's Edit 2 for the no-decision case.** I have
told MOO-141 and I have **not** drafted into their patch. **I will not make 164-7's deeming reach a
*giving*** — deeming a decision given when it has not been would start the member's own clocks
without her knowledge, which is card (b)'s whole subject. §17.1a.

**Not questions, and recorded so they are not mistaken for open: F5 bears on
[MOO-204](/MOO/issues/MOO-204)'s framing and not on its number**, and your standing answer to keep
the cap is undisturbed (§17.6); **F13 is declined on drafting grounds** with the words drafted so you
can overrule it in one line (§17.9); and **question 2 of the MOO-209 set is answered by counsel**, in
favour of keeping 164-7's two *"preceding sentence"* references (§17.8).

**What leaves this document.** To [MOO-141](/MOO/issues/MOO-141): questions 2 and 3, and the fact
that their Edit 1's saving now has one exception against 164-7's two, with the principled reason.
To [MOO-42](/MOO/issues/MOO-42)'s §7: the Board that never gives R-6's notice at all (§17.1), and
the adjacency requirement for *"the preceding sentence"* in the words a future drafter will search
for (§17.8).

---

### 17.13 Statements corrected in place at revision 7

Listed so the reviewer can check them rather than take my word, in the same form as §15.6 and §16.7.

| | Statement as it stood | Corrected statement | Finding |
|---|---|---|---|
| 1 | §2.2 / §9.3: the 48-day cap *"is not invented: every number in it is already in the section"* | **Withdrawn.** 48 is a **chosen outer limit**; the periods it displaces are act + 62 and unbounded. The three figures are each in the section; the cap is not a restatement of them | **F5** |
| 2 | the verifier line *"the definition's 15-day notice backstop, which supplies the 15 in 48 = 15 + 3 + 30"* | **Deleted, not relabelled.** Replaced by a count of the duty the endpoint keys to, of which there is **none** | **F5** |
| 3 | §3.7, §16.1: trigger two fixes *"the identical date Edit 164-4 already keys R-5's floor to"* | **Same triggering event and same formula; different date and a wider class.** 1 August against 1 September on the worked facts | **F7** |
| 4 | §16.1: *"two provisions about one date now agree"* | **They do not agree; the floor mechanism resolves them.** The point it was carrying — that trigger two invents no bound — is unaffected | **F7** |
| 5 | §7.3: both J 1 and subsection C report failures *"to make a determination, to give a notice, or to make a payment within a period required by this section"* | **Subsection C is confined to its own duties and cannot report an M 2 duty at all — dropped.** J 1 has **no payment limb**; quoted correctly. The *no new duty* conclusion survives on J 1 alone | **F8** |
| 6 | §3.8: *"`amend`, `withdraw`, `replacing`, `substitute` each 0 occurrences in the subdivision"* | **`amend` occurs once**, in the Internal Revenue Code formula. The other three are 0. The premise — no power over a filed notice — is unaffected | **F11** |
| 7 | §3.8, §13.5: § 51.1-153 *"is silent"* on a replacement notice | **Not silent. Subsection E caps retroactivity at 90 days before filing**, and D 1 defers to it twice | **F2** |
| 8 | §3.7, §14.8, §16.1: the open case is *"the member who … never files the expiry notice"* | ***The person who filed the request*** — M 2 has seven standing classes and the enacted notice runs to the filer, who may be an estate's representative or a state agency | **F15** |
| 9 | §16.6: *"no existing occurrence is amended or changed in meaning"* | **Too strong.** *No occurrence is re-worded, and none acquires a different date where the section already fixed one* | **F9** |
| 10 | §16.6: the two savings are **symmetric** | **Asymmetric and principled** — 164-7's exception names two duties, Edit 1's one, for the reason at §17.3 | **F1, F9** |
| 11 | §3.7: what 164-7 leaves open | **Incomplete.** It did not state that R-6's notice duty was unreached, which is **F1** | **F1** |
| 12 | §3.11, §4.2: G 2 and G 4 would define *"pending"* twice and a court would harmonise | **A word confined twice is not a word defined twice.** Both definitions are expressly confined. The notwithstanding is deleted | **F6** |
| 13 | §3.8: the vehicle *"supersedes any notice previously filed"* | Confined to **the member's own notice of retirement**, with a **post-retirement bar** | **F3** |
| 14 | §3.8: the vehicle *"satisfies § 51.1-153"* | **Three words deleted.** D 1's own sentence does the work, with subsection E attached | **F2** |
| 15 | the title line's amended-section count | **Unchanged at two amended plus one added — and store revision 70 amended the *"relating to"* clause**, which §5 now reproduces live rather than quoting | base |
| 16 | *"the base has moved thirteen times"* | **Fifteen times** — store revisions 69 and 70 since revision 6 was cut | base |

**Superseded in place, with a pointer rather than a rewrite: §3.7, §3.8 and §3.11 carry the
revision-7 text**; **§4.2, §13.5 and §13.7 keep the candidate as first drafted, as the record of what
changed and why**, each marked at its head.

### 17.14 Status

**Blocked on the counsel pass over revision 7's new and re-cut text, as a first-class edge, and back
to the Policy Director with its findings addressed.** **This is my own gate and I will say why I set
it rather than reassigning straight up:** MOO-209 **named** these cures, but it did not **draft**
them — I did, and F19 is the standing proof that my drafting of somebody else's named cure can carry
a defect that passes every count. **Four texts have never been read adversarially: F1's extended
exception, F3's confined supersession, the whole of Edit 164-13, and the series repair.** The three
questions above are **not** blocked by that pass and the Policy Director can action them in parallel.

**Internal working draft material. Not a Division of Legislative Services bill.
[MOO-187](/MOO/issues/MOO-187) and [MOO-209](/MOO/issues/MOO-209) are internal adversarial passes by
a colleague and are expressly not legal advice; revision 7's four new and re-cut texts have not been
reviewed as applied text at all. Nothing here states or implies that counsel or the Division of
Legislative Services has cleared it. Pre-decisional and internal. Nothing applied to the store.**
