# MOO-217 — the subdivision D 1 extension channel priced, and Edit 4's claimed neutrality tested

**Fiscal & Impact Modeler · 13 October 2026 · answers [MOO-217](/MOO/issues/MOO-217), the four
questions opened on [MOO-215](/MOO/issues/MOO-215)'s F8**

> **Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by
> counsel. Pre-decisional and internal. No figure here is a VRS actuarial result and nothing here is
> reliable beyond two significant figures (MOO-46 Decision 4). Nothing applied to the store.**

---

## 0. The answer, before anything else

**The release gate does not clear on a $0, and it does not fail on a material figure. It clears on a
named condition, and the condition is not fiscal.**

**Read this paragraph first, because the usual sensitivity sentence does not apply here.** No fiscal
input in this model swings the answer by more than 10% on a 10% move — not the Board no-act rate, not
the cohort, not the amount settled. **There is no dominant fiscal assumption and refining any input
would be wasted work.** What controls the answer is five questions, **none of them fiscal** — two belong to
Statutory Researcher, one to Counsel, one is a timing question about the end of the pilot, and one is
MOO-49's clause (vi) reading already upstream of MOO-163.
They are named in §8.2 and each is a switch, not a dial.

| | |
|---|---|
| **Central estimate** | **$11,000** over the whole 48-month pilot, at an illustrative 10% Board no-act rate. Range **$610 (low) to $110,000 (high)** at that same rate. |
| **The rate the estimate hangs on** | **Unobtainable, and declared so.** Swept 0%–50%, never assumed. The answer is reported as a **threshold in that rate**: central materiality at **94%**, high at **8.8%**. |
| **Is it $0?** | **No. It is not $0 and it is not material.** The honest fiscal-note line is *"indeterminate, not material, mechanism described."* |
| **Q1 — the two missing inputs** | Board no-act rate **unobtainable** (missing denominator). Later-date filing rate **not sourceable, but bounded from text** at 5%–60%. **A third input neither of us named is also needed** and it *was* in the record — MOO-204's. |
| **Q2 — MOO-163 / MOO-170** | **Both silent.** MOO-163's $0 neither covers nor excludes it. **MOO-170's analytic ground survives the question you asked and does not reach this channel at all** — the bound quantifies over *orderings*, and this channel moves *settle versus release*. |
| **Q3 — Edit 4 fiscally inert?** | **Property 5 is correct. "Fiscally inert" does not follow from it and is not confirmed.** Edit 4 is inert on D 1 — and *that is the reason* it lands inside subdivision G 4 clause (iii), where the money is. |
| **Q4 — price the option** | **$0 on the appropriation line and $0 on the D 2 cap.** Attaching the extension *substitutes* for the G 4 route rather than adding to it. One unpriceable term, declared. |
| **The structural finding** | **Your two claims cannot both be true at once.** One statutory reading flips which instrument carries the exposure; the exposure itself does not move. |
| **Local cost / unfunded mandate** | **$0 local. No unfunded mandate on localities, explicitly.** Every duty in the channel is the Board's. |

### One sentence for the Editor, written for them as asked

> The subdivision D 1 extension channel the revision 9 patch opens prices at **$11,000** over the
> whole 48-month pilot at an illustrative 10% Board no-act rate — a rate that exists in no published
> series and is therefore swept rather than assumed, with central materiality only at a 94% no-act
> rate — so the channel is **immaterial at every rate a reader could defend**, but it is **not $0 on
> its merits**, because Edit 4's new notice duty is inert on subdivision D 1 exactly as the Policy
> Director claims and *thereby* lands inside subdivision G 4 clause (iii), where a notice not given
> converts a released reservation into a settlement the Commonwealth must pay under subsection N, so
> attaching a D 1 extension to the Edit 4 notice costs nothing on the appropriation line and merely
> moves that same exposure off Edit 4 and onto the extension.

---

## 1. The costing question and the horizon

Over the 48-month pilot, does the channel through which a member's final qualifying retirement date
can move **when the Board does not act** — the subdivision D 1 lateness extension, and the new Edit 4
notice attaching to the definition's expiry sentence — change the amount the Commonwealth pays to the
retirement system under subsection N, or the number of members who receive a certified subsidy rather
than subsection B standard-cost rights?

- **Unit of analysis: one member-event.** One member, one no-act occasion, one outcome on the
  settle/release line. **Not** one reservation (MOO-163's unit) and **not** one queue-ordering date
  (MOO-170's unit). The change of unit is the whole reason this is a separate issue and it is most of
  the answer to question 2.
- **Horizon: the 48-month pilot.** July 1 effective date; FY2028 implementation only; FY2029 first
  benefit year (MOO-183 §8). These events need an accepted election, credited service credit, a filed
  request, a no-act, *then* the passage of a date, so they are **back-loaded to FY2030–FY2033**.

**The money chain, because every figure hangs off it.** Subsection F requires retirement in a
qualifying retirement by the final qualifying retirement date. **G 1**: she does → subsidy **settled**,
credit vests at the subsidised cost. **G 2**: she does not → credit **reduced** to standard-cost
equivalent, excess **refunded**, reservation **released**. **G 4**: three exceptions where 2 and 3 do
not apply and the credit vests at the subsidised cost anyway — death, disability approval, and
*"unable to retire in a qualifying retirement by reason of an error of the Board."* And **subsection
N**: *"Upon the settlement of a certified subsidy under subdivision G 1 **or G 4**, the Commonwealth
shall pay the amount settled to the retirement system from an appropriation made for that purpose."*

**So a settlement is an appropriation outlay and a release is not.** That is the line this channel
lands on, and it is a different line from the one MOO-163 and MOO-170 priced.

*(Naming note, because two issues in this project use the label "G 4" for different things: every
reference here is to a subdivision of subsection G of the new § 51.1-142.4. MOO-204's "G 4 aggregate,
120 days" is a later proviso in that same subdivision, not clause (iii).)*

---

## 2. Question 1 — the two missing inputs

### 2.1 Confirmed on a wider scan than MOO-215 ran

The model walks every `*inputs.py` in the project and lists the levers by name. **291 levers across
seven pre-existing registers. Neither input appears in any of them.** So *"$0 on this limb"* was an
unpriced assertion, not a counted one, and the finding stands.

### 2.2 The Board no-act rate — **unobtainable**, and the reason is a missing denominator

- VRS publishes no on-time-decision rate for § 51.1-142.2 purchase determinations.
- **MOO-71 §3 establishes that no published count of § 51.1-142.2 military purchases exists at all.**
  A rate needs a denominator and the denominator does not exist. Denominator discipline forbids
  reporting a rate here.
- **The bill would create the series prospectively** — subsection J requires the Board to report every
  failure to give a notice in time and every D 1 delay. A figure a bill has to commission is a figure
  nobody collects now.
- There is no other-state analogue of the § 51.1-142.4 certified subsidy to scale by population.

**Declared unobtainable — not guessed, and not defaulted to zero.** It is swept across
0/1/2/5/10/20/35/50% and **the answer is reported as a threshold in it** (§7.2), so no figure in this
deliverable is conditioned on a rate I cannot source. You said an express *"cannot be screened on
existing inputs"* was a usable answer; this is the stronger version of it — it *can* be screened, as
a threshold, without the rate.

### 2.3 The later-date filing rate — not sourceable, but **bounded from text**

Bounded above by 1.00, which is what MOO-215 used and which they said over-counts. The definition
narrows it on three grounds: the ground for relief is confined to a *"cause not attributable to the
member"*, so a member without one has nothing to ask for; the relief is confined to **not more than
three months** and to the first day of a month; and the Board *"shall approve a later date **on its
own initiative** or upon the written request of the member"*, which removes the need to file in
exactly the cases most likely to have a qualifying cause. Against that, filing is costless, may be
made at any time before the date, and D 1 obliges the Board to advertise the mechanism.

**Carried as analyst judgment, 20% central, band 5%–60%.** I would not defend 1.00 as a central case
and I would not defend 0.

### 2.4 A third input the question did not name — and it was already in the record

**Exposure is not harm.** MOO-215 counted members whose date *can* move; money moves only where her
date actually passes without a qualifying retirement. That conversion needs a **harm realisation
rate**, which MOO-215 implicitly set to 1.00. 1.00 over-counts for a textual reason: **the expiry
sentence is protective.** It sets her date to the first day of the second month after the period
expired and applies *only* where the date that would otherwise apply is earlier. A no-act hands her at
least a further month. What it does not hand her, before Edit 4, is **the date**.

Searching for your two inputs turned up a third that already existed. **MOO-204's
`NON_QUALIFYING_RETIREMENT_SHARE`** — 2% / 5% / 15% — is the fraction of *funded* participants who do
not retire qualifying and so reach a G 2 cutback. That is the **unconditional** rate of the very event
this channel turns on, and an unconditional rate is a **floor** on a conditional one whose condition
(the Board's silence) can only make the event more likely. So the harm rate here is **not free-hand**:

| | low | central | high |
|---|---|---|---|
| MOO-204 unconditional non-qualifying-retirement share | 0.02 | 0.05 | 0.15 |
| × information-failure multiplier — **analyst judgment**, 2×–8× defensible | 5.0 | 5.0 | 3.3 |
| = **harm realisation rate used here** | **0.100** | **0.250** | **0.495** |

The multiplier is the only free parameter, which is deliberate: it gives the reviewer one number to
attack rather than a composite.

---

## 3. Question 2 — are MOO-163's $0 and MOO-170's $204,000 silent, or do they cover it?

### 3.1 MOO-163's $0 — **silent**, on two independent tests

**Lever test.** No final-qualifying-retirement-date lever, no notice-lateness lever, no no-act rate.
Shown mechanically (§2.1).

**Unit test, which is the stronger one.** MOO-163's own stated mechanism is: *"The retention endpoint
can move money only where queue position decides who is funded. Queue position decides that only where
the $3.00M cap **binds**."* This channel does not touch queue position — it touches whether a
reservation already made is **settled or released**, and a settle/release flip moves an appropriation
outlay under subsection N whether or not the cap binds.

**So yes, and put it on the record as you asked: "$0 on this limb" was an unpriced assertion rather
than a counted one.**

### 3.2 MOO-170's bound — **its ground survives your question, and does not reach this channel**

You asked whether the bound's ground survives, since *"an unbounded or extended retention is not a
longer figure, it is the absence of one."* **On that question MOO-170 is right and the answer is yes.**
I reconstructed the derivation and it reproduces $204,000 exactly: fill the queue in filing-date order
against a fixed $3,000,000; the fill stops when the next application does not fit, so the unreserved
residual is strictly under $170,000 × 1.2 = $204,000; two orderings each leave a residual in that
interval, so the difference in total **reserved** is bounded by it. **There is no `k` and no retention
length in that derivation.** A retention of any length yields some ordering date or none, and either
way the fill is still a fill of the same fixed pool by some order. The absence of a figure is not a
counter-example.

**But the bound does not transfer here, and the reason is the quantifier, not the length.** Read what
it quantifies over: **orderings of a fixed set** against a fixed pool, bounding the amount
**reserved**. It holds constant the two things this channel moves — (1) the set is fixed, and this
channel does not reorder it but changes whether a member already inside it ends in G 1/G 4 or G 2; and
(2) the bounded quantity is reserved, and MOO-163 says in terms *"note what the delta **is**: it is a
change in **lapse**."* A settle/release flip is not a change in lapse; it is a change in the amount
**paid**.

**Stated expressly, as asked: the bound's ground survives the retention-length question and does not
reach this channel at all.** The $204,000 is a bound on a different variable.

### 3.3 The correct hard bound, derived the same analytic way

Each event converts at most one release into one settlement, and a settlement is bounded by D 2's
per-election ceiling. So `0 ≤ exposure ≤ min(N × $170,000, unexpended balance of the cap)`, and the
second term is **$980,000 at the central cohort**.

**And the sign is not indeterminate here, which is the second difference from MOO-170.** This channel
runs one way only — toward settlement, toward payment. There is no symmetric branch in which the
Board's lateness causes a member to be paid *less*. **So unlike MOO-163's lapse delta it cannot cancel
across events and cannot be dismissed as sign-indeterminate noise.** It is small or it is zero; it is
never offsetting.

---

## 4. Question 3 — is Edit 4 fiscally inert? Tested on my model, not on your reading

Three screens, each a verbatim string test on the enacted §1 extract at store revision 72, so each
fails loudly if the text moves. **The legal effect of each is Statutory Researcher's; what is mine is
the test.**

### 4.1 Screen 1 — D 1's enumeration. **Property 5 holds.**

D 1 reaches three notice species, and **none of the three reaches Edit 4's notice**:

| limb | why it does not reach Edit 4's notice |
|---|---|
| *"that written statement"* | the statement first required by the definition, due 15 days after the Board credits the purchased credit. A different instrument, different trigger. |
| *"any notice of a later approved date required by that definition"* | presupposes an **approval**. In a no-act case there is none. |
| *"any notice of a date required by that definition upon the Board's **action** upon a request"* | presupposes the Board's **action**. Edit 4's notice is required by reason of the Board's **not** acting. |

**0 of 3 limbs. Property 5 is confirmed on the test, not merely on the reading.**

### 4.2 Screen 2 — and it is **164-5-independent**, as F12 says

Pre-164-5: *"**upon** the Board's **action** upon a request."* Post-164-5: *"**by reason of** the
Board's **action** upon a request."* The operative word in both is **action**, and a re-cut of the
connective does not reach the noun it connects to. **Nothing in this deliverable is conditioned on
164-5.**

### 4.3 Screen 3 — **and this is where the claim stops holding.** Subdivision G 4 clause (iii)

Clause (iii) deems Board error where *"a member whose final qualifying retirement date passes at a
time when the Board has **not given such a statement or notice** and the time allowed by that
definition for giving it has expired."* Element by element against Edit 4's notice:

| element | Edit 4 | |
|---|---|---|
| *"a statement or notice of the member's final qualifying retirement date"* | *"written notice of **that date**"*, and that date is her FQRD | **satisfied** |
| *"required by that definition"* | inserted **into** the definition, after the expiry sentence | **satisfied** |
| *"the time allowed by that definition … has expired"* | Edit 4 supplies a time: 15 days after the period expires. **Before Edit 4 there was no such time, because there was no such duty.** | **satisfied** |
| the carve-out — *"does not include the notice of the Board's determination upon a request … no later than 30 days after the request is filed"* | Edit 4's notice is **not** that notice: that one is due 30 days after **filing** and presupposes a determination; Edit 4's is due 15 days after the **period expires** and presupposes none | **not carved out** |

**And read the carve-out's own reason:** *"the remedies of the member for a failure of the Board to
give that notice are those provided by **subdivision D 1**, by that definition, and by subsection M."*
**The bill carves a notice out of clause (iii) precisely because D 1 already remedies it.** Property 5
establishes that D 1 does *not* remedy Edit 4's notice. **On the carve-out's own logic, that is the
reason Edit 4's notice belongs inside clause (iii).**

### 4.4 Verdict — two findings, not one

**(a) Property 5 is correct as written.** No D 1 extension attaches to Edit 4's notice on either
wording. Your textual ground survives the test.

**(b) "Fiscally inert" does not follow from it, and is not confirmed.** Edit 4 adds a required notice
of a final qualifying retirement date where none was required. Its non-giving triggers clause (iii)'s
deeming limb; a clause (iii) case is **settled** rather than released; and a settlement is paid by the
Commonwealth under subsection N. **Edit 4 is inert on the D 1 channel and not inert on the G 4
channel. The claim was tested in the place you pointed at and it is right there — the cost is one
subdivision over, and property 5 is the reason it is there.**

**One qualification I will not bury.** Clause (iii)'s main limb is *"unable to retire in a qualifying
retirement by reason of an error of the Board"*, and the deeming sentences are expressed *"for the
purposes of clause (iii)."* Whether they are **inclusive** or **exhaustive** is Statutory Researcher's;
whether a member in the expiry-sentence class could reach clause (iii) **without** Edit 4 on the
un-deemed limb is Red Team / Counsel Reviewer's. **I do not set that probability and I report the
whole 0–1 interval.**

---

## 5. The population, and two corrections to MOO-215's scoping — both adverse

**5.1 The expiry sentence needs ONE no-act gate, not two.** MOO-215's class 1 is quadratic because
they modelled the M 2 **deemed denial**, which has two independent gates. The sentence Edit 4 attaches
to is not that one — *"Where the Board does not act upon a request the filing of which tolled the
running of the member's final qualifying retirement date under subsection M within the period this
definition allows for acting upon it…"* **One no-act.** So **both** classes are linear here, and
MOO-215's class-1 column under-counts the expiry-sentence class by a factor of the no-act rate itself
(0.189 vs 0.038 at a 20% rate — five times larger). **Reported because it moves adversely.**

**5.2 But class 1's membership is conditional on MOO-164's 164-4, and I do not assume it.** The
sentence says *"within the period **this definition** allows."* The definition allows **30 days**, on a
request under the definition; the **90 days** for a reconsideration request are allowed by M 2, not by
the definition. So pre-164-4 the sentence arguably reaches **class 2 only**; 164-4's re-cut to *"the
period allowed by this section"* would bring class 1 in. **Both are reported, and class 2 — the
dominant class — is unconditional on either 164-4 or 164-5.**

**5.3 Exposed versus harmed, central scenario, 48 months, class 1 included.**

| no-act rate | class 1 | class 2 | **exposed** | **harmed** |
|---|---|---|---|---|
| 1% | 0.010 | 0.036 | 0.045 | 0.011 |
| 5% | 0.047 | 0.179 | 0.227 | 0.057 |
| 10% | 0.095 | 0.359 | 0.453 | 0.113 |
| 20% | 0.189 | 0.717 | 0.906 | 0.227 |
| 50% | 0.473 | 1.793 | **2.266** | 0.566 |

**"Exposed" is MOO-215's quantity and it is the one that approaches MOO-170's 2.80 resolution.
"Harmed" is the quantity that can move a dollar, and it is an order of magnitude smaller.** MOO-215
did not over-reach — they said expressly that their class-2 column assumes every funded member files
one request. Both corrections are theirs to have flagged.

**5.4 The per-member day cap, which is what the withdrawn ground was about.** D 1's excluded aggregate
is **365 days per member**. Cohort extension-days are population × per-member days: at a 20% no-act
rate, 0.906 members × up to 365 days = up to 331 member-days. **Your withdrawal of that ground is
correct and this is the demonstration of it — the cap bounds days per member and the cost driver is a
population on the settle/release line.**

---

## 6. Question 4 — the price of attaching a D 1 extension to the Edit 4 notice

### 6.1 The counterfactual, worked on the harmed member

| | without the extension (revision 9 as drafted) | with the extension |
|---|---|---|
| | no D 1 remedy (§4.1) → she misses a qualifying retirement → **G 4 clause (iii)** deems Board error → credit vests at the **subsidised** cost → **settled** | her date moves out by the lateness days → she retires **in** a qualifying retirement → **G 1 settles** |
| subsection N | **pays the amount settled** | **pays the amount settled** |

**Both branches end in a settlement paid under subsection N, of the same election.** On the
appropriation line the option is a **substitute** for the G 4 route, not an addition to it.

| price of the option | |
|---|---|
| on the subsidy and the D 2 cap | **$0** |
| on the retirement allowance | **unobtainable** — §6.3 |
| administrative | **small and favourable** — §6.4 |

### 6.2 The corollary, and it is the one that matters for the gate

| if Edit 4's notice is… | cost of **Edit 4 alone** | cost of **attaching D 1** |
|---|---|---|
| **inside** G 4 clause (iii) (§4.3) | N × S × (1 − p_base) | **≈$0**, allowance term only |
| **outside** G 4 clause (iii) | **$0** (information only) | N × S × conversion |

**Your two claims — "Edit 4 is fiscally inert" and "attaching a D 1 extension is a policy choice with
a price" — are each true in exactly one row, and they are the same row-flip. They cannot both be true
at once, and they cannot both be false at once.** The total exposure of the patch on this line is
**N × S either way**. The statutory reading decides *which instrument carries it*, not *whether it
exists*. **That is the finding, and it is why "price the option I did not take" could not be answered
without also re-testing the option you did.**

### 6.3 The one term I cannot price — declared, not estimated

*"Qualifying retirement"* is defined as a retirement the allowance for which *"is calculated in
accordance with subdivision A 1 of § 51.1-155 and **is not reduced** under subdivision A 2 or A 3."*
G 4 clause (iii) vests the service credit; **it does not make her retirement a qualifying one.** So the
extension route may hand the member an **unreduced** allowance where the G 4 route leaves a reduced
one. That differential needs early-retirement reduction factors and an age/service distribution for
this cohort. **None exists in this project**, MOO-71 §3 establishes no published count of these
purchases exists at all, and my role bars me from introducing individual-level data to build one.

**Declared unobtainable. Direction of error: upward on the option.** Incidence: at most the N harmed
members of §5, so bounded by that population and not by the cohort. **This is a data request to VRS,
and it is the only one this issue generates.**

*One smaller term in the other direction, flagged and not quantified:* a G 1 settlement is
redetermined and capped at *"the amount so redetermined or the amount last certified and reserved,
whichever is less"*, while a G 4 vest carries no such redetermination haircut. **So the extension
route may settle slightly less than the G 4 route does** — favourable to attaching it, magnitude
unpriceable without the redetermination formula and an actual-versus-anticipated date distribution.

### 6.4 The administrative term, both directions, **no positions modelled**

**New, from Edit 4:** one notice per no-act event, on a clock that already exists for three other
notice species, triggered on the expiry of a period the Board already tracks for subsection J
reporting. At §5's volumes this is **single-digit notices over four years**.

**Avoided, by attaching the extension:** the whole G 2 machinery on each converted event — a 60-day
determination, a notice no less than 30 days before it takes effect, a credit reduction, refunds to
the member and to any state agency — plus the G 4 determination within 60 days with its own 15-day
notice.

**Net: favourable to attaching the extension**, and below the threshold at which a Virginia fiscal
note prints a figure rather than *"can be absorbed with existing resources."* **No position count is
modelled** — a known gap carried from MOO-183 §8, not a finding of this issue. One-time versus
ongoing: the notice trigger is a one-time systems change inside the $375,000 one-time nongeneral-fund
VRS implementation allowance MOO-183 already carries. **I do not assign it a fiscal year** — MOO-183's
table labels that allowance FY2029 while its §8 says FY2028 carries implementation only, and resolving
that label is MOO-183's, not mine to pick.

### 6.5 The per-event figure, S — carried from MOO-163 §2, not re-derived

| basis | figure |
|---|---|
| corrected authorised ladder *(MOO-163's carried figure)* | **$94,000** |
| MOO-71 stated basis | $111,000 |
| MOO-48 Pathway A mean *(independent)* | $110,042 |
| **D 2 hard ceiling, per election** | **$170,000** |

**And a direction-of-error reversal worth naming:** MOO-163 carries $94,000 because a *lower* mean
makes *its* cap bind later, which is cautious **there**. Here the per-event figure **is** the cost, so
$94,000 is the **optimistic** end. The scenario table uses $94,000 central and the $111,000 stated
basis in the high case, and every line is bounded by $170,000.

---

## 7. The regime test, the scenario table, and the thresholds

### 7.0 A regime test that has to run first, and it **inverts MOO-163's condition**

A settlement instead of a release is net new appropriation **only where the released money would have
funded nobody else** — that is, where the cap does **not** bind. Where it **does** bind, D 5 requires
the Board to *"accept the election if and when sufficient amounts become available"*, so the freed room
would have funded a wait-listed applicant, the aggregate stays at the cap, and the effect is
**displacement of a member rather than a dollar**.

**MOO-163's mechanism is live only where the cap binds. This channel's mechanism is live only where it
does not. The two issues are active in complementary regimes.** So MOO-163's $0 was established on
precisely the case in which this channel is loudest — **an independent and stronger answer to question
2 than §3 gives.**

| scenario | cohort | utilisation | cap | headroom = exposure ceiling |
|---|---|---|---|---|
| low | 8.97 | 33.7% | does not bind | $2,000,000 |
| central | 17.93 | 67.4% | does not bind | **$980,000** |
| high | 29.89 | 112.3% | **binds** | **$0 — displacement only** |

*(The 33.7% / 67.4% / 112.3% reproduce MOO-163's published utilisations; both are asserted as
self-tests in the model.)*

**So the high scenario's dollar line is bounded by $0 of headroom and its effect is displacement in
members — unless the release would have come too late in the pilot for any wait-listed applicant to
use it, in which case the money lapses either way and the settlement is net new outlay.** §8.3 shows
these events are back-loaded to the last two fiscal years, so **that caveat is live and I cannot
resolve it. Both branches are reported and I do not pick one.**

### 7.1 Channel exposure over the 48-month pilot, class 1 included

**Two significant figures throughout** — the cohort count these descend from is given to two figures,
so a dollar-exact cell would be false precision.

| no-act rate | low | central | **high — lapse branch** | **high — displacement branch** |
|---|---|---|---|---|
| 1% | $61 | $1,100 | $11,000 | $0 |
| 5% | $310 | $5,300 | $57,000 | $0 |
| **10%** | **$610** | **$11,000** | **$110,000** | **$0** |
| 20% | $1,200 | $21,000 | $230,000 | $0 |
| 35% | $2,100 | $37,000 | $400,000 | $0 |
| 50% | $3,100 | $53,000 | $570,000 | $0 |

The low and central columns are identical in both branches — nowhere near the headroom, so the cap
regime does not bite there. **The high column collapses from hundreds of thousands to $0 on the
displacement branch. The high line is not a figure, it is a pair.**

### 7.2 The thresholds — solved analytically, no Monte Carlo error anywhere

| scenario | S | no-act rate for **1 harmed member** | for **$100,000** | for **one full $170,000** |
|---|---|---|---|---|
| low | $94,000 | >100% (unreachable) | >100% (unreachable) | >100% (unreachable) |
| **central** | $94,000 | **88.3%** | **93.9%** | >100% (unreachable) |
| high | $111,000 | 9.8% | **8.8%** | 15.0% |

### 7.3 Against MOO-215's 15.6% crossover

Reproduced on their own basis: 2.80 ÷ 17.93 = **15.6%**, asserted as a self-test. **The two inversions
answer different questions** — theirs is *"when does this stop being below MOO-170's member
resolution"*, mine is *"when does this put a dollar on an appropriation line"*. Central dollar
threshold 94%, high 8.8%, against their 15.6%. **Theirs is the earlier warning and mine is the later
one; neither contradicts the other, and a reader who wants the conservative trigger should take
theirs.**

---

## 8. Sensitivity, local cost, fund split, timing

### 8.1 No fiscal input controls the answer

One-at-a-time, +10% off the central cell at a 10% no-act rate:

| input moved +10% | swing |
|---|---|
| Board no-act rate | 10.0% |
| harm realisation rate | 10.0% |
| amount settled per election | 10.0% |
| funded cohort | 10.0% |
| later-date filing rate | 7.9% |
| M 2 seek rate | 2.1% |

**Nothing above 25%. The largest swing is 10.0%.** The cohort lands at exactly 10% and not above it
because it scales **both** classes, so **there is no super-linear term in this model**. The two
sub-linear swings (7.9% + 2.1%) **sum to 10%**, which is the mechanical check that the two classes
partition the population with nothing double-counted and nothing dropped.

### 8.2 What does control it — all five non-fiscal, ranked

1. **Whether the member already recovered under clause (iii) without Edit 4**, on the un-deemed limb.
   Multiplies the whole Edit 4 answer by (1 − p_base): at 1.00 Edit 4 is inert and the exposure sits
   on the option; at 0.00 it sits on Edit 4. **Swing 100%.** A legal probability —
   **Red Team / Counsel Reviewer's**, with the inclusive-or-exhaustive reading of clause (iii)
   **Statutory Researcher's**.
2. **Whether Edit 4's notice is inside clause (iii) at all** (§4.3). A binary; it does not change the
   total exposure, only which instrument carries it. **Statutory Researcher's.**
3. **The Board no-act rate** — unobtainable, swept, reported as a threshold.
4. **Which cap regime the cohort is in** (§7.0) — the difference between the whole high figure and
   $0, turning on whether a wait-listed applicant is still fundable when the release would have
   occurred.
5. **MOO-49's clause (vi) reading** — broad gives ~130 members instead of 18. The cohort is exactly
   linear here, so 7× the cohort is 7× the figure, **but it also pushes utilisation far past the cap
   and moves the whole answer onto the displacement branch.** Broad clause (vi) requires repricing
   this channel too, **and it would not simply scale.**

**A 10% move in items 1, 2 or 4 does not exist — none of them is continuous.** That is why §0 names
them instead of naming a fiscal driver.

### 8.3 Local cost, fund split, biennium timing

**Local cost $0, and no unfunded mandate on localities — stated explicitly because that is a finding
in itself.** Every duty in this channel is the Board's: give a notice, act on a request, make a
determination, report under subsection J. The only duty the section puts on anyone else falls on *"a
state agency that employs or last employed a member"*, which is not a locality. The population is the
State Employee plan (MOO-183 §8). **No locality acquires a duty, a cost, or a reporting obligation.**

**Fund split — declared open.** Subsection N pays *"from an appropriation made for that purpose"*, so a
settlement is an appropriation line, not a trust-absorbed cost. MOO-183 §8 carries a 47% general-fund
share **on the amortisation of trust cost**; I have **not** applied it here, because a subsection N
settlement is a direct payment of the amount settled and not an amortised trust cost, and I have no
authority for the split on that line. Direction: a GF share below 100% would move §7's figures
**down**. **This is the one place where a §7 figure could only improve on better information.**

**Biennium timing.** Earliest event lands FY2030, back-loaded across FY2030–FY2033. **At the central
figures there is less than one event in the whole pilot, so a fiscal-year split of it would be false
precision and is not offered.** If the high line is taken, FY2032–FY2033 carry it.

---

## 9. External sanity check

**No quantitative external anchor exists, and that is established rather than asserted:** MOO-71 §3
establishes no published count of § 51.1-142.2 purchases exists at all, §2.2 establishes no no-act
rate exists for any denominator, and there is no other-state analogue to scale by population. So two
checks are available and **both are reported, including where one disagrees.**

**Convention check** against Virginia fiscal-note practice on capped, self-executing programmes. A
channel that cannot exceed a ceiling already appropriated for, produces single-digit events over a
four-year pilot at any defensible rate, and has no local component, is reported as *"$0"* or
*"indeterminate but not material"*, with the mechanism described. **Result: agreement with the central
line — and the convention cannot validate the high line. It validates $0 and nothing else**, which is
exactly MOO-163's and MOO-170's own disclosure about this check.

**Basis-mismatched cross-check** on the per-event figure. MOO-183 Table A reports $55,000–$66,000 per
participant on a **net trust cost** basis, PV at 6/30/2025. The per-event figure here is
$94,000–$111,000 on a **certified subsidy** basis, nominal. **Ratio 1.42× to 2.02×. This is not
agreement and I am not calling it agreement** — a certified subsidy is a gross reserved amount, net
trust cost is net of member payments and discounted. The check establishes only that the per-event
figure is the right **order of magnitude** for one member of this cohort: tens of thousands, not
thousands and not millions. A ~2× gap on a basis difference of exactly this kind is expected; **a 20×
gap would have refuted the figure. Falsifiable, and not refuted.**

**What would falsify the whole answer.** A published VRS on-time-decision rate worse than ~9% failure
for determinations of this kind, or a clause (vi) reading that puts ~130 members in the cohort.
**Either one brings this issue back.**

---

## 10. What re-opens, what does not, and what I am handing to whom

**On your trigger:** you said MOO-163 and the declined F-6 cap re-open **if I come back non-zero**.
**I come back non-zero on the mechanism and immaterial on the figure, and I do not think that fires
your trigger — but that is your call and I am not making it for you.** My reading of the gate: the
figure at every defensible no-act rate is below the convention at which a fiscal note prints anything,
the two classes' margin against MOO-170's own resolution is intact, and **nothing in this model
re-cuts a live MOO-163 or MOO-170 number.** What *is* non-zero is the finding in §4.3, and it is a
drafting finding with a price attached rather than a price that disturbs a published figure.

**Not reopened by anything here:** the board's 120 days, MOO-179's declined cap, MOO-170's $204,000
(§3.2 confirms its ground on its own terms), MOO-163's published cells.

**Handed on, by role:**

- **Statutory Researcher** — (1) is Edit 4's notice within G 4 clause (iii)'s deeming limb and outside
  its carve-out (§4.3)? (2) are clause (iii)'s deeming sentences inclusive or exhaustive? (3) does the
  expiry sentence reach a reconsideration request pre-164-4, or only a definition request (§5.2)?
- **Red Team / Counsel Reviewer** — the un-deemed limb: could an expiry-sentence member reach clause
  (iii) *without* Edit 4? That is `G4_BASELINE_AVAILABILITY` and it is the top sensitivity.
- **Policy Director** — the option itself. §6.2 is the decision-relevant fact: **the exposure does not
  disappear if you decline the option; it relocates onto Edit 4.**
- **VRS, via you** — the one data request: early-retirement reduction factors and an age/service
  distribution for this cohort, to price §6.3's allowance differential.

---

## 11. Assumption register

Full text with units, sources, vintages and directions of error in
`moo217-d1-extension/moo217_inputs.py`. Every number in this document traces to a row below or to a
cited source. Retrieval date for every Paperclip-internal source: 12 October 2026.

| # | assumption | value | unit | source | direction of error |
|---|---|---|---|---|---|
| 1 | D 2 aggregate cap | $3,000,000 | dollars, cumulative | **text**, store rev 72 | none |
| 2 | D 2 per-election ceiling | $170,000 | dollars/election | **text** | none |
| 3 | D 3 contingency rate | 20% | fraction | **text** — still a `[20]` bracket | higher makes the cap bind sooner |
| 4 | period allowed, definition request | 30 | days | **text** | none |
| 5 | M 2 period, reconsideration request | 90 | days | **text** | none |
| 6 | Edit 4 notice deadline | 15 | days after period expiry | **drafted**, revision 9 Edit 4 | none |
| 7 | D 1 excluded aggregate | 365 | days **per member** | **text** | none — and it bounds days, not members |
| 8 | mailing extension | 3 | days | **text**, D 1 | lengthens downstream periods |
| 9 | subsection N payment window | 60 | days after settlement | **text** | none |
| 10 | pilot length | 48 | months | MOO-71 via MOO-163 | none |
| 11 | funded cohort | 17.93 (8.97–29.89) | members/48 months | MOO-71 rev 2 via MOO-163, **cited as given** | conditional on **narrow clause (vi)**; broad is ~7× |
| 12 | refused members | 2.70 | members/48 months | MOO-163 §B, four refusal rows | over-counts — cautious here |
| 13 | M 2 seek rate | 0.35 (0.15–0.60) | fraction of refused | **analyst judgment**, MOO-163 | symmetric; 2.1% swing |
| 14 | cap utilisation | 67.4% (33.7–112.3) | fraction | MOO-163 §2, reproduced as a self-test | decides the §7.0 regime |
| 15 | amount settled per election | $94,000 ($94k–$111k) | dollars | MOO-163 §2, **not re-derived** | $94k is the **optimistic** end here |
| 16 | **Board no-act rate** | **swept 0–50%** | fraction of requests | **NONE — declared unobtainable** | n/a: reported as a threshold |
| 17 | later-date filing rate | 0.20 (0.05–0.60) | fraction of cohort | **analyst judgment**, bounded from text | symmetric; 7.9% swing |
| 18 | non-qualifying-retirement share | 0.05 (0.02–0.15) | fraction of funded | **MOO-204**, cited as given | a **floor** on row 19 |
| 19 | information-failure multiplier | 5.0 (3.3–5.0) | dimensionless | **analyst judgment**, 2×–8× defensible | the only free parameter in the harm rate |
| 20 | harm realisation rate | 0.250 (0.100–0.495) | fraction of no-act events | **derived**, 18 × 19 | symmetric; 10.0% swing |
| 21 | `G4_BASELINE_AVAILABILITY` | **0–1 interval reported** | probability | **a legal question, not a fiscal input** | **top sensitivity; 100% swing** |
| 22 | materiality floor | $100,000 | dollars/48 months | **reporting convention**, as MOO-163 §8 / MOO-170 §7 | not a legal threshold |
| 23 | MOO-170 resolution | 2.80 | members/48 months | MOO-170, **their figure on their terms** | none |
| 24 | MOO-183 cost per participant | $55k–$66k | dollars/participant | MOO-183 Table A | **basis mismatch**, §9 — not agreement |
| 25 | GF/NGF split on a subsection N settlement | **declared open** | — | none; MOO-183's 47% is for amortised trust cost | a GF share <100% moves §7 **down** |

---

## 12. Files and how to rerun

| file | what it is |
|---|---|
| `moo217-d1-extension/moo217_inputs.py` | **The assumption register.** Sections A–F. MOO-163's register is imported unchanged and re-exported so the reader can see exactly which of its levers this issue leans on. |
| `moo217-d1-extension/moo217_d1_channel.py` | The model. Sections 0–11, each printing its own working, plus a self-test block. |
| `moo217-d1-extension/out_moo217_run.txt` | Captured transcript of the run of record. |
| `moo217-d1-channel-priced.md` | This document. |

```bash
cd moo217-d1-extension
python3 moo217_d1_channel.py            # ~1s, exit 0, prints the whole analysis
python3 moo217_d1_channel.py > out_moo217_run.txt
```

**No dependencies beyond the standard library** — no numpy, and **no random draw anywhere in this
model**, so there is no Monte Carlo error on any figure and every threshold is a division.
**Verified byte-identical across two consecutive runs and across a clean start with `__pycache__`
removed.** The script reproduces **every number** in this document; nothing here is quoted from a
prior run.

**Verification performed**

1. **22 assertions, all passing** — 14 in the §11 self-test block and 8 inline screens in §0 and
   §4 — including that the
   §7.0 regime table reproduces MOO-163's published 33.7% and 67.4% utilisations, that MOO-215's 15.6%
   crossover reproduces on their stated basis, that the reconstructed MOO-170 derivation gives
   $204,000 exactly, and that the harm rate never falls below MOO-204's unconditional floor.
2. **Three verbatim string screens** on the store-revision-72 extract (D 1's extension sentence,
   clause (iii)'s deeming sentence, clause (iii)'s carve-out, subsection N's payment obligation). The
   extract's character count is asserted against the register, so a moved store **fails the run**
   rather than drifting.
3. **MOO-163, MOO-170 and MOO-204 registers imported and never written to** — asserted in the
   self-test and confirmed by `git status`: this issue's work touches no file outside
   `moo217-d1-extension/` and this document.
4. **Partition check** — the two classes' sub-linear sensitivity swings sum to exactly 10%, proving
   nothing is double-counted or dropped between them.

**Known limitations, all stated:** the Board no-act rate is unobtainable and swept, so there is no
point estimate of it anywhere; the retirement-allowance differential in §6.3 is unobtainable and is a
data request to VRS; `G4_BASELINE_AVAILABILITY` is a legal probability I report as an interval rather
than set; the GF/NGF split on a subsection N settlement is declared open; no position count is
modelled (carried gap from MOO-183 §8); and every count remains conditional on **MOO-49's narrow
clause (vi) reading**, which travels with the figures as it does at MOO-163 and MOO-170.
