# MOO-216 — bounded adversarial pass on MOO-141 revision 9, at store revision 72

**Internal risk analysis. Not legal advice. Not reviewed or cleared by counsel — nothing in this
document states or implies that counsel has cleared any part of the proposal. Pre-decisional working
draft material. Not a Division of Legislative Services bill. Nothing applied to the store.**

Red Team / Counsel Reviewer · 13 October 2026
Base read from `moo141-rev72/live.md`, document revision `368f5e41`, whole document 502,586, enacted
§1 **134,012**, sha256 `83a10b74950b5272…` — re-derived independently, not taken from the kit.
My own kit: `moo216-counsel/verify_216.py`, **90 checks, ALL CHECKS PASS**. It lifts both patches'
edits by executing the two kits' prefixes, so divergence from either is impossible.

**Scope honoured.** One pass over the four named targets. I did not re-open the board's answers, did
not re-derive MOO-215's sixteen findings, and did not draft into the patch.

**Count: 1 fatal (R1), 5 serious (R2–R6), 2 moderate (R7–R8), 3 minor (R9–R11), 11 express null results.**
**Most serious: R1 — §3.2's structural premise is false, and the reversal it justifies moves a date.**

---

## 1. The strongest case against revision 9, in the voice of the person who will make it

> *You asked us to believe something very specific, and you asked us to believe it because it was
> structurally necessary rather than merely likely. You told us that both of 164-7's deeming predicates
> are no-act predicates, so the deemed date "necessarily precedes any real act of the Board upon the
> same request, because the deeming's own trigger is the absence of such an act up to that date." That
> is not what subdivision M 2 says. M 2's trigger is the absence of an act **within a thirty-day window
> that opens only after the Board has already missed its ninety days** — and an act that falls before
> the window opens is invisible to it. A Board working a backlog decides a reconsideration on 2 June;
> the person who filed it, exercising a right the statute gives them on a condition that was satisfied
> and that nothing in the text untrues, files the expiry notice on 5 June; the Board does not act again;
> on 6 July the request is deemed denied and that denial "constitutes the final determination of the
> Board upon the reconsideration." Your 164-7 deems the Board to act, and to **last** act, on 6 July.
> Your Edit 1 deems the Board to act, and to **last** act, on 2 June. Two sentences, the same two
> deemed facts, thirty-four days apart, no priority rule in either. That is exactly what the last
> reviewer told you at F4 and you said it could not happen.*
>
> *And look at what it costs you. You reversed your own asymmetry ruling and put subdivision R-6's
> notice deadline inside Edit 1's deeming, on the express condition that doing so "moves no date." On
> these facts it moves it from 21 July to 17 June — **earlier**, so that on 6 July, the day the deemed
> denial crystallises, your Board is already nineteen days late with a notice nobody could have known
> was owed. That is the fatal defect the last reviewer found in your Edit 2 class 1, relocated from the
> class test into the exception, in the revision that cured it. It also moves the one clock this whole
> item exists to fix: subdivision G 4's pendency window ends "on the date on which the Board first acts
> upon it," and you have given it two different end dates. You opened MOO-141 because G 4's window and
> M 2's tolling restart on different days. Revision 9's two patches, landing together as you insist
> they must, restart them on different days again.*
>
> *Then there is your fourth edit, which you call the only wholly operative one. It is operative in the
> sense that it says words. The definition attaches five machinery provisions to every date document it
> creates — subdivision D 1's lateness extension, D 1's companion right to state a later effective date
> of retirement, 164-13(a)'s disclosure duty, 164-13(b)'s clause (iv), 164-8's supersession right, and
> R-7's own date floor. Your new notice is attached to **none** of them, and the insertion point you
> chose to protect R-7's referent is precisely what denies your own notice R-7's protection. You
> disclosed one of those six exclusions and priced it as a feature. The member whose retirement date
> was fixed by the expiry of a period learns of it, if your Board is late, after the date has passed,
> with no extension, no floor, no later-effective-date right, no route to file a conforming notice of
> retirement, and no disclosure that any of that is her position. You wrote at §4.2 that the bill
> "requires nobody to tell her what it is." You have now required somebody to tell her. You have not
> given her the thing she actually needed, which was time.*

---

## 2. Findings, ranked

### R1 — FATAL — construction · §3.2's structural premise is false, and the reversal it justifies moves a date

**What is wrong.** §3.2 asserts that the two deemings "agree by construction" because 164-7's deemed
date "necessarily precedes any real act of the Board upon the same request — because the deeming's own
trigger is the absence of such an act up to that date." For 164-7's **limb 2** that is true: its
predicate is "where the Board does not act upon a request under the definition … within the period
allowed by this section for acting upon it." For **limb 1** it is false. Limb 1 fires on a denial by
operation of M 2's sentence, and M 2's predicate is *"Where the Board does not act upon the request
**within 30 days after that notice is filed**."* That is a **windowed** no-act predicate, not the
absence of any act up to the deemed date. The window opens only when the filer, exercising the right M
2 gives them once the Board has missed its ninety days, files written notice that the period has
expired. An act of the Board **before the window opens** does not satisfy the predicate's negation and
does not prevent the deeming. M 2 gives the member's filing right on a condition stated in the past
perfect — the Board "does not act … within the 90 days allowed" — and nothing in the text makes it a
continuing condition. The drafter knows how to write a continuing condition and does so eleven lines
earlier in the same subdivision: *"at any time before the Board makes the determination."* It did not
here.

**Concrete failure scenario, with dates.**

| | |
|---|---|
| 1 Mar | Member files a request for reconsideration under subdivision M 2 |
| 30 May | The 90 days allowed by M 2 (as re-cut by **164-10**, "after the request is filed") expire. The Board has not acted |
| 2 Jun | **The Board actually acts upon the request** — one real act, not two |
| 5 Jun | The filer files written notice that the period has expired. The condition was satisfied on 30 May and nothing untrues it |
| 5 Jun – 5 Jul | The Board does not act within the 30 days after that notice |
| 6 Jul | *"the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001"* |

- **164-7 limb 1** deems the Board *"to act upon the request, and to last act upon it, **on the date of
  that denial**"* — **6 July**.
- **Edit 1** deems the Board *"to act upon that request, and to last act upon it, on the date on which
  the Board **first** acts upon it"* — **2 June**.

Two deemings, the same two deemed facts, **2 June and 6 July**, and no priority rule in either
sentence. **MOO-215's F4 was right on its own terms and §3.2's reason for reversing it is not
available.**

**Why §3.1's test was the wrong test.** §3.1 asked "whether any case exists in which the Board acts
more than once **and** a residual class obtains." This scenario needs **one** real act. And the record
already holds the premise that defeats §3.2: at §3.4, withdrawing requirement 1, the Director writes
*"Edit 1's deeming is not confined to the multi-act case; it operates wherever a period is measured
from the Board's acting."* §3.2 then reasons as though Edit 1 merely picks among acts in a multi-act
sequence. **§3.2 and §3.4 are inconsistent with each other**, and §3.4 is the one that is right.

**What moves with it — three things, and the first two are load-bearing.**

1. **R-6's notice deadline, which revision 9's reversal newly subjects to Edit 1's deeming.** R-6: notice
   *"no later than 15 days after it acts upon the request."* On Edit 1 that is **17 June**; on 164-7 it is
   **21 July**. So the reversal **does** move a date — violating the §3.3 constraint the Director set as
   "the only reason I had for hesitating" — and moves it **earlier**, so that on 6 July the Board is 19
   days late with a notice it could not have known was due. **That is MOO-215's F1 vice** — class
   membership, here duty timing, conferred by an event after the date the duty measures from — relocated
   from Edit 2's class test into Edit 1's exception, in the revision that cured it in Edit 2. Before
   revision 9, Edit 1's exception named M 2's 15-day application duty alone and R-6's deadline sat
   outside Edit 1's deeming entirely, so only 164-7 reached it and there was no conflict for R-6.
   **The reversal is what imports R-6's deadline into an unresolved two-deeming conflict.**
2. **Subdivision G 4's pendency window — MOO-141's own subject matter.** G 4: *"such a request is pending
   from the date on which the member files it until the date on which the Board **first acts upon it**,"*
   and G 4's class is the tolling class, so a reconsideration request is in it. Edit 1 ends the window on
   2 June; 164-7 deems a last act on 6 July. **The parent issue is "G 4's pendency window is 30 days
   shorter than M 2's tolling — the two clocks restart on different days." The combined text restarts
   them 34 days apart again.**
3. **M 2's tolling end date**, which 164-1 re-keys to notice with a 30-day floor and a 48-day cap
   measured from "the Board acts upon the request" — so it moves with whichever date wins.

**Authority.** The bill's own text: subdivision M 2's deemed-denial sentence and its expiry-notice
sentence; 164-10's commencement re-cut; 164-7's REPLACE; Edit 1's deeming sentence; R-6; G 4's pendency
sentence. All nine predicates counted in `verify_216.py` under `== R1`.

**Honest statement of the contrary case.** A court could read "the request" in M 2's deemed-denial
sentence as presupposing a still-pending request, so that a decided request falls out and the deeming
cannot operate. That reading is available and may well prevail. But it is purposive, it is contradicted
by the drafter's use of an express continuing condition elsewhere in the same subdivision, and — the
point that matters here — **§3.2 does not claim likelihood, it claims necessity**: "necessarily," "by
construction." A reading that probably saves the claim does not establish it. The reversal cannot rest
on a premise that holds only on a contestable construction of a sentence neither patch amends.

**Suggested direction (one sentence, not a draft).** §3.4's **requirement 4 has fired**: the
cross-reference cannot be drafted without resolving a priority, so the priority must be chosen
expressly — and the choice is between "the earlier of" and "the later of," which is a substantive
decision about whose clock the Board gets, not a signpost.

---

### R2 — SERIOUS — construction · §3.2's other route fails too, on 164-7's own confinement clause

**What is wrong.** §3.2's stated reason for treating a deemed act as an act for Edit 1 is: *"164-7's
confinement clause makes the deeming operate for every provision measuring a period from the Board's
acting, and Edit 1's sentence is such a provision."* **Edit 1's sentence is not such a provision.**
164-7 confines its deeming to provisions *"under which a period begins or ends upon, or is measured
from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference
to the **month** in which the Board acts, or last acts, upon the request."* Edit 1's deeming sentence
does neither: it measures no period and fixes no date by reference to a month. It **defines** the
Board's acting for the provisions that do. It is the referent-supplying sentence, not a referent-using
one.

**Failure scenario.** Pure no-act case: the Board never acts upon a definition request within the
period. 164-7 deems an act on the day after expiry. Edit 1's operative words are *"the date on which
the Board first acts upon it"* — and if 164-7's deemed act is not an act for Edit 1's purposes, that
phrase has **no referent**, so Edit 1's deeming produces no date at all. §3.2's conclusion ("Edit 1
therefore selects 164-7's deemed date") does not follow. The likely practical result is harmless —
Edit 1 is simply inoperative there and 164-7 governs alone — but a competing deeming with a null
referent that purports to fix the same "last act" fact is a construction a litigant will use, and the
record presents the opposite proposition as established.

**R1 and R2 are a dilemma, and that is the point.** Either a 164-7 deemed act counts for Edit 1 — and
then R1's two dates conflict — or it does not — and then Edit 1 has no referent and §3.2's stated
reason is wrong. **On neither horn is "the two agree by construction" established.** The Director asked
me to try both routes; both fail, in opposite directions.

**Authority.** 164-7's confinement clause, quoted in full and counted; Edit 1's deeming sentence.
`verify_216.py` under `== R2`.

**Direction.** If the cross-reference is to carry the work, it must say which sentence supplies the
referent, not merely that a deemed date is a date on which the Board acts.

---

### R3 — SERIOUS — unintended effect / drafting · Edit 4 creates a fourth date document and attaches it to none of the definition's machinery

**What is wrong.** Every other date document this definition creates is wired into the same five
provisions. Edit 4's notice is wired into none of them, because it is the one date document not given
*"upon"* — or, after 164-5, *"by reason of"* — *"the Board's action upon a request."* Verified character
by character:

| | Provision | Reaches Edit 4's notice? | Disclosed in revision 9? |
|---|---|---|---|
| i | **D 1's lateness extension** — *"Where the Board gives that written statement, any notice of a later approved date …, or any notice of a date required by that definition upon the Board's action upon a request, later than the time required…"* | **No** (three documents; Edit 4's is a fourth) | **Yes** — §4.3 property 5, priced as a feature |
| ii | **D 1's companion right**, in the same sentence — the member *"may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice"* | **No** | **No** |
| iii | **164-13(a)'s disclosure duty**, which MOO-209's F4 added *precisely to reach the third date document* | **No** | **No** |
| iv | **164-13(b)'s clause (iv)** — the § 51.1-153 notice-replacement right, which rides on the same disclosure sentence | **No** | **No** |
| v | **164-8's supersession right**, keyed to *"any notice described in the preceding sentence"* = D 1's three documents | **No** | **No** |
| vi | **R-7's date floor**, keyed to *"a decision or notice required by **the preceding sentence**"* = R-6 | **No** | **No** |

**Item vi is the one to look at hardest, because the record presents its cause as a virtue.** Property 4
("R-7's referent does not move") is secured by inserting Edit 4 **before** R-6. That insertion point is
exactly what puts Edit 4's notice outside R-7's floor. And the expiry sentence affirmatively forecloses
any substitute: it fixes her date *"notwithstanding any other provision of this definition."*
**Edit 4's notice is the only notice duty in this definition whose lateness has no date consequence
whatever.** Property 4 and §4.3's disclosure are the same fact seen from two sides; the record reports
one side as a counted win and never says the other side is its price.

**Concrete failure scenario.** Member files a tolling request; the period for acting expires **10
April** without the Board acting; the expiry sentence fixes her final qualifying retirement date at
**1 June**. The Board gives the Edit 4 notice on **15 August**. Her statutory retirement date passed
eleven weeks earlier. No D 1 extension; no R-7 floor; no right to state a later effective date of
retirement; her 30-day window to file the § 51.1-153 notice of retirement ran from the *first* statement
and closed months ago, and 164-8's new supersession route does not reach her because her notice is not
one of D 1's three; and the notice she finally received was under no duty to tell her any of that,
because 164-13(a) does not reach it either.

**Why this is not a quibble.** MOO-209's F4 was the finding that the disclosure duty reached only two of
three date documents, and 164-13(a) exists to fix it. **Edit 4 creates a fourth and reproduces F4 one
document further on, in the same joint cut that cures it.** The same is true of 164-8: it was drafted on
MOO-209's F2/F3 to give the member a route to file a conforming retirement notice after a late Board
document, and Edit 4's document is outside its descriptor.

**Authority.** D 1's three-document enumeration; 164-13(a) and 164-13(b)'s REPLACEs; 164-8's REPLACE;
R-7; the expiry sentence's "notwithstanding any other provision of this definition"; Edit 4's
insertion-point ordering. All counted, `verify_216.py` under `== R3`.

**Direction.** Two mutually exclusive options and the choice is the Director's: either bring Edit 4's
notice inside the four descriptors (D 1's enumeration, 164-13(a), 164-8) **and** give it a floor, which
is a priced policy choice and belongs in §5; or keep it outside and say so in the memo's risk section as
a deliberate decision that the member gets the information and not the time. **What is not available is
the current position, in which five of the six exclusions are undisclosed and the sixth is scored as a
benefit.** For the **Editor**: this must appear in the memo's risk section.

---

### R4 — SERIOUS — compliance arbitrage · Edit 4's class membership is defeasible by the Board's own later act

**What is wrong.** Edit 4 triggers on *"Where the member's final qualifying retirement date **is
determined by the preceding sentence**"* — that is, on the **outcome** of the expiry sentence, not on an
affirmative operative fact. And the expiry sentence applies only where *"the date that would otherwise
apply under this definition is earlier than the first day of the second month following the month in
which that period expired."* **"The date that would otherwise apply" is not static.** It moves later if
the Board approves a later date under the definition — which is the very thing the request asked for.

**Concrete failure scenario.** Request filed **5 March**; the 30-day period for acting expires
**4 April**; the expiry floor is **1 June**; the date that would otherwise apply is **1 May**, which is
earlier than 1 June — so the expiry sentence applies, her date is 1 June, and Edit 4's notice falls due
**19 April**. The Board gives no notice. On **20 June** it acts and approves a later date of **1 August**.
The date that would otherwise apply is now 1 August, which is **not** earlier than 1 June, so the expiry
sentence never applied, her date was never 1 June, and **the duty the Board missed on 19 April was never
owed**. A Board that wants the Edit 4 duty to go away can make it go away by acting late and granting.
Conversely, the Board that *complied* on 19 April gave written notice of a date that turned out never to
be hers, and Edit 4 imposes no duty to correct it (R-6 picks it up only because the later grant engages
R-6's chapeau — so the correction arrives by a route Edit 4 does not provide and the record does not
claim).

**Why this is the finding it is.** MOO-215's F1 was fatal because *"a negative fact can be made true
after the date the limb measures from,"* and the cure was to take class membership out of the future by
keying it to an affirmative fact. **Edit 4 is the one provision revision 9 drafted fresh, and it keys
its class to a conditional outcome the obligor can falsify after the deadline has run.** The vice is the
same; only the direction is reversed — F1 conferred membership retrospectively, Edit 4 withdraws it
retrospectively.

**Authority.** Edit 4's trigger; the expiry sentence's second condition; the definition's later-date
sentence (*"not more than three months after the date determined under the first sentence"*); Edit 2's
cured class 1 for the contrast. `verify_216.py` under `== R4`.

**Direction.** Key Edit 4's trigger to the affirmative fact the way F1's cure did — the Board's not
having acted upon the request within the period — rather than to whether the expiry sentence's
comparison happens to come out a particular way.

---

### R5 — SERIOUS — drafting · F7's cure is the wrong *kind*: extending a closed list strengthens the implication against everything still outside it

**What is wrong.** F7's complaint was that the saving's enumeration is a **closed list** and three duty
families sat outside it. Revision 9 adds three items. **It does not open the list.** Under the same
different-words canon the record relies on throughout (*Forst*), a five-family enumeration implies more
strongly than a two-family one that the unnamed families **are** determined by the deeming.

**Counted, from the bill's own list rather than from my hunt.** Subdivision M 2 makes **thirteen**
classes of Board action reviewable: *"Every determination, certification, redetermination,
recertification, reduction, cancellation, rescission, restoration, crediting of service credit,
placement on a waiting list, expiration of a reservation, denial of an election, and refusal to accept
an election under this section is a determination of the Board for the purposes of this subsection."*
The revision-9 saving reaches **four** of them by name — determination, recertification, restoration,
crediting of service credit. **Nine are outside it:** certification, redetermination, reduction,
cancellation, rescission, placement on a waiting list, expiration of a reservation, denial of an
election, refusal to accept an election.

**And M 2's own deeming cannot carry them in, because of the same four-word limiter F10 was about.**
Those thirteen are a determination of the Board *"**for the purposes of this subsection**."* So they are
not "determinations" for the purposes of the saving's *"to make a determination,"* which sits in
subsection A. **The Director designed F10's limiter out of Edit 2's class 1 and it is load-bearing again
in Edit 1's saving, undisclosed.** Seven further express Board duties are outside both lists and
counted: to reserve an increase in a certified subsidy, to rescind a determination, to release a
reservation, to extend a completion date, to apply an amount to the purchase of additional service
credit, to correct an error, and to recertify **an election** under subdivision D 6 of § 51.1-142.4
(the saving's noun is "a certified subsidy," so this one is outside it even though "recertify" is in).

**And the 111 characters buy less than claimed.** None of the three added families' deadlines is
measured from *"the Board's acting … upon a request,"* which is Edit 1's deeming trigger. They run from
the recertification; from the determination's taking effect; from the crediting of the service credit;
from receipt of a notice of cancellation; from the member's approval or death or the Board's *making a
determination*; and from *"the reversal or modification."* On a strict reading the deeming never reached
them and the addition is surplusage carrying a negative-implication cost. On a purposive reading only
the "reversal or modification on reconsideration" limb is reached, since a reversal on reconsideration
occurs by the Board's act upon the request.

**Failure scenario.** The Board acts three times on a reconsideration. A member challenges the
expiration of a reservation as untimely. The Board answers that Edit 1's deeming fixes the relevant date
at the first act, that subsection A's saving expressly protects five families of duty and the expiration
of a reservation is not among them, and that the drafter's addition of three families at revision 9
shows the list was considered and closed. **The member's M 2 reviewability of that failure, which store
revision 61 supplies and which is F7's whole ground, is answered by F7's own cure.**

**Authority.** M 2's thirteen-item sentence and its "for the purposes of this subsection" limiter; the
seven unnamed Board duties, each counted in the base; the six deadline formulae; Edit 1's deeming
trigger. `verify_216.py` under `== R5`.

**Direction — one sentence.** Replace the enumeration with general words: the deeming does not determine
the date by which the Board is required to do **anything** under this section. It adds no exception, so
it satisfies §3.3; it keeps the two named duties carved back in; it is shorter than the enumeration; it
closes the family permanently; and the deeming keeps its real work — the member's dates and clocks, M's
tolling, and subdivision B 4 f — which is MOO-141's actual object.

---

### R6 — SERIOUS — specification · §3.4 requirement 2 fails with R1, exactly as the issue predicted

**What is sound first.** 164-7's deeming does land **inside subdivision M 2** — its FIND is M 2's
deemed-denial sentence and its REPLACE appends after it — so requirement 2's locator *"deemed under
subdivision M 2"* is accurate. And 164-7 does deem a date on which the Board acts, so requirement 2
describes its referent correctly. Requirement 1 and the withdrawal of the old requirement 1 are sound
and I confirm both: a signpost saying Edit 1 *"governs the case where the Board acts more than once"*
would narrow it by implication.

**What is wrong.** Requirement 2 asserts that stating the cumulation *"resolves no priority and chooses
no date."* On R1 it does both. If a date deemed under M 2 is a date on which the Board acts for
subsection A's deeming, then in R1's scenario the set of acting-dates is **{2 June, 6 July}**, Edit 1
takes *"first"* = **2 June**, and that **overrides 164-7's express deeming that the Board *last* acts on
6 July**. The cross-reference therefore resolves the priority in Edit 1's favour and chooses a date —
which requirement 2 denies and **requirement 3 ("move no date") forbids**. Requirements 2 and 3 are
still not jointly satisfiable. This is MOO-215's F5 one step further on: the replacement specification
fails for the same reason the original three did.

**Note on the residue the Director already routed.** §3.2's "wrinkle" — 164-7 deems a *last* act and a
real act can follow it — is the adjacent problem. R1 is the deeper one: Edit 1 does not merely allow a
later real act, it **affirmatively deems a different last-act date**. Routing the wrinkle to the
Drafting Specialist does not reach R1.

**Direction.** Requirement 4 fires and this comes back to the Director, as requirement 4 says it must.

---

### R7 — MODERATE — drafting · Edit 4's deadline is not anaphoric to its trigger, and the anaphor was sitting in the preceding words

**What is wrong.** The expiry sentence triggers on the expiry of *"the period this definition allows for
acting upon it"* (after 164-4, *"the period allowed by this section"*). Edit 4's deadline runs from
*"the expiration of **the period for acting upon the request referred to in that sentence**."*
Grammatically *"referred to in that sentence"* modifies **the request**, not **the period** — so the
period is described afresh rather than referred back. For a reconsideration request there are two
candidate periods for acting: M 2's 90 days (164-10) and the 30 days after the expiry notice is filed.
Reconsideration requests **are** in the expiry sentence's class, because M 2's tolling sentence tolls on
*"the filing of a request for reconsideration under this subsection, **and** the filing of a request
under the definition."* So trigger and deadline can resolve to different periods.

**Failure scenario.** A reconsideration request on which 164-4's re-cut makes the expiry sentence bite.
Trigger period = M 2's 90 days, expiring 30 May. Edit 4's deadline = 15 days after "the expiration of
the period for acting upon the request" — the Board computes it from the 30-day expiry-notice window
instead, five weeks later, and is in time on its own reading and late on hers.

**Direction.** *"…no later than 15 days after the expiration of **that period**."* The expiry sentence's
own anaphor is in the words immediately before Edit 4 (*"the month in which that period expired"*), it
resolves to exactly one period, it names no formula so **property 3 survives intact**, and it is 56
characters shorter. This strengthens the 164-4-proof claim rather than costing it.

---

### R8 — MODERATE — evidence · §4.3's statement of the member's remedy is wrong in both directions

**What is wrong.** §4.3 says that if the Board is late with the Edit 4 notice she has *"no extension —
only the reviewability of a failure to act within a required period that store revision 61 supplies."*
She has more than that, and less.

**More:** filing a reconsideration of the Board's failure to give the Edit 4 notice **tolls the running
of her final qualifying retirement date** under M 2's tolling sentence, and because that is a different
*failure* from the one her first request concerned, M 2(i)'s no-second-request bar does not block it.

**Less:** M 2(ii) caps *"the aggregate of all tolling under this subsection"* at **120 days**, and the
Edit 4 class has **by definition already filed a request that tolled** — the expiry sentence's class is
*"a request the filing of which tolled the running of the member's final qualifying retirement date
under subsection M."* So where the first request consumed the aggregate, **the remedy yields zero
days**, and §4.3's "no extension" is right only in the worst case and understates her position
elsewhere.

**Direction.** State it as it is — reviewability plus whatever remains of M 2(ii)'s 120-day aggregate,
which may be nothing — and give the **Fiscal & Impact Modeler** that as the bound on §5's question 4,
because it is the only quantity in this area that is already fixed by the text.

---

### R9 — MINOR — drafting · the saving's payment limb does not track the words the bill and subsection M use

**What is wrong.** The saving says *"to pay or include any amount."* Subsection M 2, whose reviewability
is F7's entire ground, says *"a failure of the Board … to make a determination, to give a notice, or
**to make a payment** within a period required by this section."* The operative duties say *"shall pay a
refund"* (five times) and *"shall refund"* (six). The saving should be co-extensive with the
reviewability set it exists to protect, and it uses a different verb for the same family. I regard a
duty "to pay a refund" as plainly a duty "to pay … any amount," so I do not say the limb fails — I say
the divergence is gratuitous and, on the record's own *Forst* reasoning, gratuitous divergence is the
thing to avoid.

**And a base defect in the neighbourhood, named with no owner assigned to me.** The bill's principal
"include" provision is **actorless**: *"the next payment of the member's retirement allowance **shall
include** every amount by which the amounts paid to the member fall short…"* — a property of the
payment, imposing a duty on nobody. The bill supplies a Board duty only for the no-payment-yet case
(*"the Board shall include the amount that this subdivision requires to be included…"*). This is a
duty-with-no-actor in the base, not in the patch.

**Direction.** If the enumeration survives R5, track M 2's words — *"to make a payment"* — and route the
actorless sentence to the Drafting Specialist as a base defect.

---

### R10 — MINOR — base defect, owner needed · M 2's deemed denial can displace a real determination

**What is wrong.** R1's engine is a defect in the base, not in either patch, and it deserves an owner of
its own. M 2's deemed-denial sentence operates on a purely temporal condition, so it can deem denied a
reconsideration request the Board has **actually decided** — including one decided in the member's
favour — and the deemed denial *"constitutes the final determination of the Board upon the
reconsideration and a case decision as defined in § 2.2-4001."* A member who won on 2 June loses by
operation of law on 6 July because she filed the expiry notice on 5 June.

**Authority and the textual argument.** M 2's deemed-denial sentence; M 2's own use of a continuing
condition for the parallel case (*"at any time before the Board makes the determination"*); Va. Code
§ 2.2-4001 (case decision) and Art. 5 (§ 2.2-4025 et seq.) for what the deemed denial becomes.

**Litigation surface, stated specifically because the bar requires it.** Plaintiff: a member (or the
state agency from whose appropriation an amount was paid on her behalf, which has express standing in
§ 1 and is M 2's named person) whose favourable reconsideration determination was displaced by a deemed
denial. Claim: that the deemed denial is not a lawful case decision because the Board did act, pleaded
on judicial review of the case decision under Va. Code § 2.2-4026 with § 2.2-4027's standard, and in the
alternative a due process claim under Va. Const. art. I, § 11 as to a statutory benefit determination
reversed without adjudication. Venue: the circuit court on APA review. **This is risk identification,
not a legal opinion, and I am not counsel of record.**

**Not treated as drafting, per the issue's instruction** — this is not one of the board's answers either;
it is base text neither patch amends. **It needs an owner named by the Director.**

---

### R11 — MINOR — record hygiene · a verifier label is again doing work its check is not

`moo141-rev72/verify_r72.py` asserts:

> `chk('164-7 deems the act on the denial date or the day after expiry — **both before any real act**',
> E164_7.count('on the date of that denial or, as the case may be, on the day after the expiration of
> that period'), 1)`

The **counted** proposition is that a phrase is present once. The **labelled** proposition is an
ordering claim about real acts — and it is precisely the claim R1 falsifies. Nothing in the kit tests
it. **This is §6.1's own finding recurring inside the kit that reports it**, and it is the second time on
this item that a label has carried a proposition a count could not reach. No string count can construct
the 2 June / 6 July ordering; a claim of that shape belongs in prose with its counterexample, or the
label must be narrowed to what is counted.

---

## 3. Citation and counted-fact verification

I re-derived every counted fact independently rather than re-running the kit, then ran the kit as a
cross-check. **`verify_r72.py`: ALL CHECKS PASS** on my run. **`verify_216.py`: 90 checks, ALL PASS.**

| Claim in the record | Result |
|---|---|
| §1 = 134,012, sha256 `83a10b74950b5272…` | **Holds.** Re-derived by splicing §1 out of `live.md` and hashing. `s1.txt` is byte-identical to the spliced §1 |
| Whole document 502,586; document revision `368f5e41` | **Holds** |
| §1 byte-identical to store revision 71 | **Not independently verifiable here** — store revision 71's §1 is not in the workspace. The kit asserts the hash against a literal, which is the right form of the check, and the literal matches the revision-8 kit's. I record it as verified-by-hash-continuity, not re-derived |
| Four anchors, each exactly 1 in §1 | **Holds.** (1, 1, 1, 1) |
| Edit 1's FIND reads 2 whole-document; a whole-document count is not a valid uniqueness test | **Holds.** 2 |
| Patch +1,716 = 1,116 + 317 + 15 + 268, §1 and whole-document alike | **Holds** |
| `<u>` 62/62 | **Holds** |
| `first acts upon` 2 → 3 | **Holds.** Both base occurrences are in **subdivision G 4's pendency sentence** — which is why R1(2) bites |
| `the preceding sentence` base 21, +2 under the patch, Edit 4 adding exactly one | **Holds** |
| Combined with MOO-164 revision 7: +5,091, order-independent and byte-identical either order | **Holds** |
| The two saving bodies (1, 1) in the combined text, designed to fail later | **Holds.** Correctly left failing-later; I did not touch it |
| Revision 8's defective class-1 wording live at 0 | **Holds** |
| MOO-164's thirteen FINDs all 1 at revision 72 and after revision 9 | **Holds** |
| §6.1's self-correction — "no word of the bill is deleted" is false; Edit 2 strikes three words | **Holds, and the correction is right.** Edits 1, 3 and 4 are pure insertions on my own recomputation |

**One citation of the record's own that does not hold:** §3.2's characterisation of M 2's predicate as
*"the absence of such an act up to that date."* The sentence quoted in support — *"the Board does not act
upon the request within 30 days after that notice is filed"* — is quoted accurately and **says something
narrower than the proposition it is cited for.** That is R1.

---

## 4. Fiscal assumption challenge

**The assumption I was pointed at** is §4.3 property 5: Edit 4 is inert on the subdivision D 1 channel
because D 1 reaches only a notice required *"upon"* / *"by reason of"* the Board's **action**. **I tested
it and it holds**, on both the pre- and post-164-5 wordings, verified character by character against D
1's three-document enumeration. This was the kind of claim MOO-215's F8 was about and this one is good.

**But property 5 is not the load-bearing assumption for the decision.** The load-bearing one is the
unstated premise that **D 1 is the only channel through which Edit 4 can cost or save money.** R3 breaks
it: Edit 4's notice is also outside D 1's later-effective-date right, 164-13(a)'s disclosure duty,
164-13(b)'s clause (iv), 164-8's supersession right, and R-7's floor. Every one of those is a benefit the
member does **not** receive, so **Edit 4 as drafted is cheaper than the record treats it as being** — the
fiscal exposure is entirely on the **cure**, not on Edit 4.

**The alternate number, honestly.** I cannot produce one, and I want to be exact about why rather than
assert a figure. There is no runnable model in this workspace carrying a Board no-act rate or a rate at
which funded members file later-date requests — which is the §5 finding the Director already accepts, and
I accept it on the same ground. What I can do is change the **scope** of the question the modeller is
being asked:

- **§5's question 4 as currently routed** prices attaching a D 1 extension to the Edit 4 notice — **one**
  provision.
- **After R3 it must price five** — D 1's extension, D 1's later-effective-date right, 164-13(a)'s
  disclosure, 164-8's supersession, and an R-7-equivalent floor — because they are a package in the
  bill's existing design and attaching one without the others produces a sixth asymmetry.
- **R8 supplies the one quantity that is already fixed by the text and needs no estimate:** the member's
  self-help remedy is bounded by what remains of M 2(ii)'s **120-day** tolling aggregate, and in the Edit
  4 class she has already drawn on it, so the floor of that bound is **zero days**. The modeller should
  use zero as the conservative case rather than modelling a remedy.

**I did not modify any team file.** My kit is a new file in `moo216-counsel/`; it reads `live.md` and the
two existing kits read-only and lifts their edit definitions by executing their prefixes.

---

## 5. Draft text defects, clause by clause

**Edit 4**, read as it will sit between the expiry sentence and R-6:

| Clause | Finding |
|---|---|
| *"Where the member's final qualifying retirement date is determined by the preceding sentence,"* | **R4.** Triggers on the expiry sentence's conditional outcome, which the Board can falsify after the deadline by granting a later date. `the preceding sentence` resolves correctly (N2) |
| *"the Board shall give the member written notice of that date"* | Actor, act and object all present. Sound. But **R3**: the notice carries none of 164-13(a)'s four required disclosures |
| *"no later than 15 days after the expiration of the period for acting upon the request referred to in that sentence."* | **R7.** `that sentence` resolves; `the request referred to in that sentence` resolves (the expiry sentence names exactly one request); **`the period` does not resolve anaphorically** and can diverge from the trigger period for a reconsideration request |
| *(absent)* — no date floor, no supersession, no disclosure, no lateness consequence | **R3 items ii–vi.** Five omissions, four of them undisclosed |

**Edit 1's exception**, as reversed: operative, and the two exceptions do differ only in the two locators
that must differ — I re-verified the Director's substitution test and it holds. **But R1:** adding R-6's
duty moves R-6's deadline in the class R1 identifies.

**Edit 1's saving, as extended:** **R5** (the list is still closed, nine of M 2's thirteen reviewable
classes and seven further Board duties are outside it, and M 2's "for the purposes of this subsection"
limiter blocks the deemed route in), **R9** (payment verb).

**Edit 2 and Edit 3:** no new defect. See N10.

---

## 6. Eleven express null results — what I checked and found sound

1. **Edit 4 property 1 — widens no chapeau.** **Sound, and the reason given is right.** R-6's chapeau
   governs both the *"state that date in its decision"* branch and the notice backstop, and in a no-act
   case there is no decision, so a chapeau widening would engage the second branch by putting the Board
   in breach of the first. A separate sentence has no such collision. Edit 4 does not touch R-6's words.
2. **Edit 4 property 2 — the referents.** **Sound.** `the preceding sentence` = the expiry sentence;
   `that sentence` takes it as antecedent; `the request referred to in that sentence` resolves, because
   the expiry sentence names exactly one request. No MOO-164 substitution inserts a sentence between the
   expiry sentence and Edit 4 — **164-4 substitutes *within* the expiry sentence and does not split it.**
   The *period* reference is R7, not this.
3. **Edit 4 property 3 — 164-4-proof.** **Sound.** Edit 4 contains neither *"this definition allows"* nor
   *"allowed by this section"*; no MOO-164 FIND overlaps Edit 4's new sentence; all thirteen MOO-164 FINDs
   still resolve to 1 after revision 9. F14's register point cannot bite it.
4. **Edit 4 property 4 — R-7's referent does not move.** **Sound as a positional fact**, verified in both
   the revision-9-alone copy and the combined copy, and `"Notwithstanding the two preceding sentences"`
   is untouched and still earlier. It is also the cause of R3(vi), which is a separate matter.
5. **Edit 4 property 5 — D 1's extension does not reach Edit 4.** **Sound on both wordings.** See §4.
6. **Target 4's and/or question — no *Forst* gap.** *"to recertify or settle a certified subsidy"* **does**
   reach the bill's *"shall recertify and settle **it** accordingly,"* because *"it"* is *"the certified
   subsidy"* on the sentence's own words, and a disjunctive enumeration in a saving reaches each limb of
   a conjunctive duty. *"to restore or credit service credit"* matches the bill **verbatim at both of its
   two occurrences**. The Director's own worry here was unfounded. (The object mismatch is *"recertify
   **the election**,"* which is R5's territory, and that duty's date is not measured from the Board's
   acting, so it is inert.)
7. **The saving's "include" limb has a referent.** I looked for an over-reach and did not find one: the
   bill does impose a Board duty *"to include"* — *"the Board shall include the amount that this
   subdivision requires to be included in the next payment of the member's retirement allowance…"* My
   first draft of this finding was wrong and the check I wrote to prove it failed. Reported as R9's
   narrower point only.
8. **Edit 4's duty is enforceable — not a press release.** A failure to give it within the required
   period is *"a failure of the Board … to give a notice … within a period required by this section"*
   under M 2, so it is reviewable on reconsideration, the final determination is a case decision under
   § 2.2-4001, and judicial review lies under Art. 5 (§ 2.2-4025 et seq.). There is an enforcer and a
   forum. What the remedy is **worth** is R8.
9. **Edit 1 alone is consistent with G 4's pendency window.** G 4 already ends the window *"on the date
   on which the Board first acts upon it,"* which is exactly what Edit 1 deems — so Edit 1 standalone
   agrees with the provision that is MOO-141's object. **The conflict in R1(2) is with 164-7, not with
   G 4,** and it exists only in the combined text the patches are designed to produce.
10. **The board's answers — not re-opened, and I found no defect to report.** Card (g)'s first limb
    survives character for character in Edit 2's REPLACE, appears exactly once, and is ordered first so
    the board's class is reached first. Card (k-ii)'s 120 days are untouched: Edit 3's delta is 15,
    unchanged. **I am reporting no finding against either, as the issue asked me to do if I found one.**
11. **Edit 4's standalone operability.** **Sound.** Edit 4's text contains no *"subsection"*, no
    *"subdivision"* and no *"deem"*, so it is fully operative applied alone and is the only edit in the
    patch with that property. The claim is true.

---

## 7. Routing

**To the Policy Director — yours to decide, and I am not deciding any of it:**

- **R1** and **R2** together. The reversal of the 01:32 asymmetry ruling may still be the right call —
  MOO-215's F4 recommended it and R1 does not say otherwise — but **the reason given for it is not
  available**, and on R1's facts the reversal moves R-6's deadline earlier into a window the Board cannot
  have known about. The reversal needs a different ground or a different scope.
- **R6.** Requirement 4 has fired on its own terms.
- **R3.** Whether Edit 4's notice comes inside the four descriptors and gets a floor. This is a priced
  policy choice and it is §5's question, enlarged.
- **R10.** This base defect needs an owner. It is not the board's answer and it is not drafting.

**To the Drafting Specialist:** R4's trigger (affirmative fact, per F1's own cure); R7's `that period`;
R9's payment verb and the actorless *"shall include"* sentence; and **R3's descriptor work, but only
after the Director decides R3** — it is a policy choice before it is a drafting task.

**To the Fiscal & Impact Modeler:** §5's question 4 is now five provisions, not one (§4 above), and R8
supplies a zero-day floor on the self-help remedy that needs no estimate.

**To the Statutory Researcher:** R5's thirteen-item M 2 list against the saving's four, and whether M 2's
*"for the purposes of this subsection"* limiter is as confining as I read it — that is the single point
on which R5's severity turns.

**To the Stakeholder Analyst:** R10's plaintiff is the **state agency from whose appropriation an amount
was paid on a member's behalf**, already flagged at §8 of the record; R10 gives it a second, independent
scenario in which it is the litigant, and this one survives F1's cure.

**To the Editor, for the memo's risk section — mark these explicitly:** **R1** (the two deemings and the
clock MOO-141 exists to fix), **R3** (Edit 4 gives information, not time, and five of six exclusions are
currently undisclosed), **R4** (a duty the obligor can defeat retrospectively). R5 if the Statutory
Researcher confirms the limiter.

---

**Internal risk analysis. Not legal advice. Not reviewed or cleared by counsel. Pre-decisional.
Nothing applied to the store.**
