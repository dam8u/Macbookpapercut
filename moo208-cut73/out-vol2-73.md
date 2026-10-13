# bill-text-s8 — retained record, second volume: the §0 narrative for store revisions 38 to 41, the sweeps §5.20 to §5.23, and §6.0-26, §6.0-35, §6.0-36 and §6.0-38, and §3

**MOO-42 · Drafting Specialist · opened at store revision 43, 12 October 2026 · INTERNAL WORKING DRAFT — pre-decisional, not a Division of Legislative Services bill, not reviewed by counsel or DLS. Nothing here is cleared for external use.**

**Why a second volume.** [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history) stands at 523,352 characters against the document store's 524,288-character ceiling and **cannot absorb another move**. `bill-text-s8` arrived at store revision 43 with **23 characters** of headroom, and pass 14's record would not fit. The sections below are moved here **verbatim**, with every lettered label, numbered item, table row and check number preserved, so a `§0.0000000000000000d`- or `§5.21`-style reference still resolves. **Nothing was rewritten and nothing was summarised away.** Each one is replaced in `bill-text-s8` by a stub restating its durable results and naming anything in it that is superseded.

**Three warnings for a reader who arrives here first.**

1. **Three rows of §5.21's sweep are corrected by pass 14 and must not be relied on as written** — the ordinal-reference row (P14-17), the *"limitation year"* count (P14-18), and the count of provisions that move with the final qualifying retirement date, which is six and not five (N14-2). The corrections are at `bill-text-s8` §5.24.
2. **§5.20's Checks 2, 3 and 4 carry corrections already recorded in their own text**, from [MOO-119](/MOO/issues/MOO-119)'s pass 13.
3. **§3's cap-utilisation range — low 38, central 76, high 126 percent — is §3's own reservation-basis arithmetic and is superseded for every external use** by MOO-32 v6's authorised **78.1872** percent central and **130.31** percent high on **18.3965** participants. §3's reasoning about the cap is unaffected. The stub in `bill-text-s8` says the same, so nobody has to come here to find it out.
4. **§6.0-36 item 1 is the record of the second withdrawal of the window-envelope assurance.** Store revision 43 states the envelope as a statement of the text and not as a warranty, and two residuals are in front of the Policy Director at §7 items 68 and 71.

---


## 0.000000000000000000000000000000000 Store revision 41 — [MOO-119](/MOO/issues/MOO-119)'s pass 13 drafted out. Two edits, 484 characters, and the first gives subsection C's quantity limit a value it did not have for a measured, admitted class

**The record proper is a companion document from the start** —
[`pass13-disposition`](/MOO/issues/MOO-87#document-pass13-disposition) — on the convention store
revisions 33, 36 and 40 set. It carries the finding-by-finding disposition of all twelve findings, the
redline, the measured class, and the record corrections in full. What follows is the summary.

**Pass 13 returned 12 findings — 0 fatal, 4 serious, 4 moderate, 4 minor — and does not recommend
reversing store revision 38's deletion.** It found what neither the deletion nor any of §7 item 35's
three checks reached: a class for whom clause (ii) of subsection C has **no value at all**.

**Edit 1 — subsection C's new third sentence says what clause (ii) does where no quantity of service can
answer it.** For a Plan 1 member under age 50 at the filing date, § 51.1-153 B 2 requires age 50 **and**
30 years of creditable service, so no number of months of creditable service causes her to have reached
her unreduced retirement eligibility date as of that date: the solution set is **empty**, and the bill
did not say whether that yields a cap of **zero** — on which the deleted bar would have refused her,
with notice — or **no binding limb**. Clause **(vi)** admits her at the boundary, one month short of 50.
**0.0826 participants in the class, 0.0259 admitted, at $145,396 to $166,226 of certified subsidy
each** against subdivision D 2's $170,000 ceiling: de minimis in aggregate, **not** de minimis per
member, and resolved before this revision by whoever at the Board wrote the spreadsheet.

**It enacts the reading the authorised basis is measured on, which is why no figure moves.**
`moo32_v6_engine.py`'s `need_months_at` returns `INF`, not 0, for that class, so **18.3965 admitted**
and [MOO-71](/MOO/issues/MOO-71)'s **18 (range 9 to 30)** already stand on the reading now in the text;
the other reading is **18.3706**, about $4,000 of the $3,000,000 lower. **Direction of effect: nil
against the authorised count, upward against the alternative**, and the ground for choosing is the
Director's own — a count may not travel on a basis the statute does not require. The sentence also makes
the choice a **determination stated in the certification**, which subdivision M 2 reaches; before it
there was nothing stated and nothing to review.

**Edit 2 — clause (v) of *"eligible member"* now carries clause (ii)'s entitlement base, verbatim.**
Store revision 34 gave clause (ii) the words *"taking account of all creditable service for which the
member is entitled to credit as of that date"* and §6.0-38 item 4 records that clause (v) was
deliberately left alone, which invited the inference that the instruction does not reach the limb that
is now the **sole** screen for the same fact (F-11, F-12). **Direction of effect: ~~it can only exclude,
never admit~~ <u>[Store revision 46, on pass 14's **M-1**: no quantity of creditable service can postpone
an unreduced retirement eligibility date, but the direction of effect of the base specification itself
is not determinate on the face of the statute. Corrected here and in §8's status note for store
revision 41; the text question is §7 item 82 and [MOO-124](/MOO/issues/MOO-124) has answered the
research question it turns on.]</u>**, because more creditable service cannot postpone an unreduced date; on the authorised
basis it moves nothing, the engine carrying one service variable per member so that the split-base case
is not representable.

**One serious finding is live and not enacted: F-3, at §7 item 70.** An accepted election with nothing
to buy has no defined downstream operation. Edit 1 closes the **pre-acceptance** route to it. **Two
post-acceptance routes survive, and the reviewer's own repair does not reach them** — its sentence is
keyed to **acceptance**, while subdivision D 6's second sentence clause (i) and subdivision B 4 f clause
(i) of § 51.1-142.2 both operate after it. Item 70 drafts the repair that does.

**Four findings are corrections to this record and are made in place:** §5.20's Check 2 is **not**
independent of Check 1 (F-4), Check 3 loses **two** rows and not one (F-6), Check 1's *"two
occurrences"* is **one** (F-9), and Check 4's *"option (c)"* is **item 22's** (F-10). Clause **(vi)** is
named co-load-bearing with clause (v) (F-2), and § 51.1-124.3's *"membership service for which credit is
**allowable**"* replaces the unsourced *"same basis"* as the ground of the containment (F-11).

**I rebased twice, and the label moved twice.** This was drafted against store revision 38; **store
revision 39** ([MOO-117](/MOO/issues/MOO-117)'s pass 12, seventeen edits) and **store revision 40**
([MOO-118](/MOO/issues/MOO-118)'s pass 13, one re-cut clause) landed under it. So this is **41**, and
§5.23 and §6.0-41 take the numbers after store revision 40's §5.22 and §6.0-40. **Neither revision
touched either provision this one changes:** I verified **subsection C and the definition of *"eligible
member"* byte-identical** to my base before editing, and nothing of either revision is reversed or
renumbered here. **One of store revision 39's edits bears on item 70 and does not rescue it** — its new
closing sentence of *"final qualifying retirement date"* operates on *"the date that would otherwise
apply under this definition"*, and on a zero-credit election no such date arises, because the first
sentence runs from the earliest qualifying retirement date and that runs from the Board crediting *"all
of the service credit purchased."* The trace at item 70 is checked against the landed text.

**Housekeeping, which was not optional.** The file had **3,555 characters** of headroom, two concurrent
revisions having spent it, and this revision's summary, sweep, ambiguities, item and banner are about
22,000. **Six sections are moved verbatim** to [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history): the **§0 records for store revisions
37, 36 and 35**, **§5.19** and **§6.0-37** (so that the whole of store revision 37's record sits in one
place), and **§7.1** (the retained record of numbers and choices that were mine). Every lettered label,
numbered item, table row and check number is preserved, each is stubbed here with its durable results,
and **each of the three §0 records already had a companion record document of its own and keeps its §8
banner**. **This is the most any one revision of this file has moved**, and the reason is in the
sentence above rather than in anything about the sections themselves. **Nothing was summarised away.** The live §0 narrative is store revisions 38 to 41. Citation
sweep **§5.23**; ambiguities **§6.0-41**.


## 0.00000000000000000000000000000000 Store revision 40 — [MOO-118](/MOO/issues/MOO-118)'s pass 13 answered: both subdivision G 4 edits survive, the residual disapplication is re-cut to name its three targets, and §7 item 60 gains two answers. One anchor, no figure moved.

**Pass 13 returned 0 fatal, 3 serious, 2 moderate and 3 minor against the 169 characters store revision
37 enacted, and both edits survive** — *"neither is fatal and each is an improvement on the words it
replaced."* The three serious findings are **one question**, and it is the one neither edit answers: in
the death case, **what the survivor's benefit is measured on**. That decides who bears a loss, so it goes
to the Director at **§7 item 60**, which now carries two further answers, **(d)** and **(e)**. Finding by
finding: [`moo118-disposition`](/MOO/issues/MOO-97#document-moo118-disposition).

**a. The one change to the bill.** In the third sentence of subdivision G 4 the residual disapplication
goes from 143 characters to 423. It now **names the three requirements a deceased member cannot satisfy**
— being in service, giving written notification, and an effective date falling after the last day of
service — and widens the residual criterion's sources from *"that definition or § 51.1-153"* to **that
definition, § 51.1-153, § 51.1-155.1 and subdivision D 1**. Findings **F5**, **F4**, **F6**. **No deeming,
no section displaced, no payee changed, no measure stated, no figure moved**, and the title does not
change.

**b. Why the enumeration went back in.** §6.0-37 item 5 traded it away for brevity, and **F5** shows the
cost: on the **class** reading the bare criterion reaches § 51.1-153's in-service and notification
requirements but **not** subsection E's effective-date requirement, because what defeats the member there
is that **G 4 itself** fixes the deemed date at the date of death — so coverage turned on the **calendar**.
The criterion survives as a **residual behind** the enumeration, so nothing it reached is surrendered, and
the **age-and-service thresholds** and the definition's **unreduced** element are still not named and still
apply: the Director's decided middle treatment of G 4, undisturbed, and **F1** is the report of what
follows from it. **F7 and F8 are declined** with reasons at §6.0-40 items 3 and 4, and **F1, F2 and F3 are
deliberately not drafted in** — each fix direction *states a measure*, and every measure takes money from
someone (§6.0-40 item 5).

**c. §7 items 59, 60 and 61 are moved into §7's live list, between items 58 and 62.** Store revision 37
wrote them **after** §7.1, which is captioned a *retained record*, so a reader of the live list never
reached them — and store revision 39, knowing they existed, numbered its own new items from **62**, leaving
59 to 61 as a gap in the sequence. That gap is now filled by the items themselves. **Moved intact and
unamended except for item 60's two new answers, and nothing is renumbered.**

**d. Three rows of §5.19 did not hold and are corrected in place.** § 51.1-165 and § 51.1-165.01 **are**
cited in the bill, six times between them; § 51.1-153 appears in subdivision D 1 **four** times, not
three; *"qualifying retirement"* is used **26** times other than in a dated term, not 20. All three
re-counted here. Only **§ 51.1-162 and § 51.1-163** are cited nowhere.

**e. Rebased once, and the numbers moved under it.** This revision was cut against store revision 38 and
**store revision 39 landed under it** — [MOO-117](/MOO/issues/MOO-117)'s pass 12, seventeen edits — which
took the label 39, §5.21, §6.0-39 and the moves of §5.16, §6.0-24, §6.0-25, §6.1a and §6.2a. So this is
store revision **40**, written on store revision 39, with sweep **§5.22** and ambiguities **§6.0-40**.
**Store revision 39 touched none of subdivision G 4's death branch**, and every anchor edited here was
re-verified present and unique in its body first. Nothing in store revision 39 is reversed or renumbered.

**f. Housekeeping, which was not optional.** The file had **7,808** characters of headroom after store
revision 39. **§5.18** (store revision 36's eleven-edit sweep, now closed by pass 12), **§5.17** (store revision 35's, whose counts
[MOO-118](/MOO/issues/MOO-118) §3 superseded), **§6.2** (revision 5's ambiguities) and **§6.0-20**
(revision 20's, most of which store revision 38's deletion superseded) are **moved verbatim** to [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history), every table row and bracketed in-line correction preserved, each stubbed
below with its durable results, on the convention store revisions 34, 36, 38 and 39 used. **Nothing was
summarised away.**


## 0.0000000000000000000000000000000 Store revision 39 — MOO-117's pass 12 drafted out. Seventeen edits in twelve provisions, no figure moved, and the one serious finding I would not have introduced the bill with is closed

**Full record: [`pass12-disposition`](/MOO/issues/MOO-42#document-pass12-disposition).** Written as its
own document from the start, on the convention set by `rev21-record`, `rev22-record` and the three
earlier pass dispositions, because this file has no room for a record of that size. **It carries the
finding-by-finding table, all seventeen edits verbatim, the two departures from pass 12's own fix
direction with reasons, the F-24 no-change reasoning, and the cross-reference sweep.** §5.21 and
§6.0-39 below are stubs that point at it; nothing in it is summarised away here.

[MOO-117](/MOO/issues/MOO-117)'s pass 12 — the bounded adversarial and counsel review of store
revision 36's eleven edits — returned **26 findings: 0 fatal, 8 serious, 13 moderate, 5 minor, plus 20
express null results.** It says in terms that no edit in store revision 36 prevents the bill from
operating, creates a facial constitutional defect, or defeats the enactment. **Disposition: 18 drafted
out (16 by express edit and F-3 by consequence), 1 no change needed, 7 with the Director at §7 items 62
to 69.** `12`, `$3,000,000`, `$170,000` and the `[20]` percent contingency are untouched, no section is
added or deleted, no designator is renumbered, and the bill title does not change.

**I re-read all 26 quoted strings against the live body before editing**, because store revisions 37
and 38 landed after pass 12 started. Every one was present as quoted.


### a. The three that cost a real person real money

**1. The protective branch was shortening the ordinary window — F-1, and it is the finding of the
pass.** G 4's re-keyed clock ran from *"the earliest of"* three dates, one of which is the G 4 ninetieth
day. For **every** member separated more than three months before her final qualifying retirement date
the ninetieth day is the earliest, so the Board was commanded to strip her purchased credit while
subsection F still permitted her to retire. Pass 12's member is separated nine months early, is
correctly told she has until 1 December 2032, and by the time she files to retire on 1 November 2032 —
inside her own window — her credit is gone, her retirement is not a qualifying retirement, and G 1 never
settles. **Being involuntarily separated early is what cost her the subsidy.** The clock now runs from
the **earlier of (a) the later of** the ninetieth day and her final date, **and (b)** the date she
retires in a non-qualifying retirement. It is one phrase and it is the reason this revision exists.

**2. The deeming rule deemed the retirement and not the date — F-2, F-3 and F-9, closed by one
replacement.** Store revision 36's edit 1 said such a retirement *"is a qualifying retirement"* and left
the member's final qualifying retirement date where it was. So she had taken a qualifying retirement
**after** her final date: subsection F was breached on its face, **D 7 commanded release of the
reservation at the same moment G 1 commanded settlement**, and D 2 commanded the opposite of D 7 — the
art. X, § 7 exposure §7 item 40 exists to address, arrived at by accident. Pass 12's note that *"this is
the route the drafter correctly rejected for edit 2 and then took for edit 1"* is accurate and the
criticism is fair. The sentence now **moves the date**, as edit 2 does, and three things disappear
together: the fiction, the F breach and the D 7 conflict. **F-3 needed no edit of its own** — G 2's clock
runs from *"the member's final qualifying retirement date, if any"*, so once the date moves the clock
moves with it and can no longer mature before the member may use the protection. F-9's 21-month
ambiguity goes with it: *"the month in which the Board **last acts upon a request** the filing of which
tolled that period."* **And the new date-setter is capped on its face at 12 months beyond the outer
bound**, which is the point I take most seriously in this revision — see §6.0-39 item 1.

**3. A federal-tax statement the statute cannot make — F-8, the cheapest high-value fix in the pass.**
Store revision 36 deleted B 4 g's designation and kept B 4 a's definition, which is the operative half:
*"'Limitation year' means the calendar year."* **26 C.F.R. § 1.415(j)-1(a) makes the calendar year a
default only** — *"unless the terms of a plan provide otherwise"* — and (d) provides that once
established a limitation year *"may be changed only by amending the plan."* B 4 f computes against the
term three times, including the completion-date extension, so on a plan with a 1 July limitation year the
statute would have commanded the Board to accept a payment it may not accept, and the exposure is plan
qualification. The term is now defined **by reference to the plan**. One consequence for the Director
and for the Editor: **[MOO-115](/MOO/issues/MOO-115) stops being load-bearing for the bill text** — the
answer no longer changes a word of the draft. **And §7 item 57's candidate designation should not now be
adopted**: it asserts the same plan-document fact at subdivision level, which is the thing (a) forbids.
Item 57 is annotated accordingly.


### b. Eight more, each a real failure

- **F-6 · the separation trigger could be arranged.** § 2.2-3200 B's definition is **inclusive** —
  *"includes, but is not limited to"* — and its second limb is *being placed on leave without
  pay-layoff or equivalent status*. The bill's carve-out subtracts only performance, misconduct and
  resignation, the agency's notice duty specified **no content**, and § 51.1-124.11 reaches only a
  *knowingly* false statement. So a one-day layoff-status placement recorded as a reorganization bought
  three months of window and three months of reservation, with no recovery route and no false statement
  by anybody. The notice must now state the **date and the cause** and be **certified by the agency head
  or his designee**, and the extension operates **only** where the Board has received such a notice or has
  otherwise determined that a separation occurred. It is a trigger gap, not a fraud gap, and I have not
  reopened §7 item 42.
- **F-7 · the date could move silently and nothing could undo what followed.** Edit 2 operated by force
  of law on the date of the separation; every Board duty ran on knowledge; and G 4's rescission sentence
  reached a later disability approval and a later death and nothing else. **F-6's condition pre-empts most
  of it** — the date can no longer move before the Board knows — and the **rescission limb is enacted as
  the backstop** for the Board that determines the fact late. It also **reinstates the reservation**,
  which pass 12 did not ask for and which the fix needs: without it the member retires in a qualifying
  retirement, G 1 settles, and subsection N pays against a reservation G 2 had already released.
- **F-5 · the Board was commanded to misdescribe every member's deadline.** D 1 still told every member
  her extended date was *"subject to the outer bound stated in the last sentence of that definition"* —
  and edit 1 had added two sentences after the bound, so the last sentence was the **floor**, which is the
  opposite of an outer bound. The ordinal is dropped rather than corrected, because sentence counts rot
  and this is the second time one has.
- **F-4 · the floor left two readings twelve months apart.** It was drafted as a floor and not as a
  date-setter, so where the Board's statement was very late *"notwithstanding the two preceding
  sentences"* switched the bound off and left D 1's day-for-day extension uncapped. It is a date-setter
  now, Reading B is gone, and the bound stays alive for every other purpose.
- **F-15 · the notice floor had no consequence**, in a section that uses the device four sentences away.
  A determination that takes effect three days early — which it can, because the three-day mailing
  allowance extends the M 2 period the floor is keyed to — is now **of no effect**, in G 4's own words.
- **F-16 · the date of an involuntary separation was undefined** and the imported definition supplies two
  candidates **six months apart**. It is the termination date, or the placement date where there is a
  placement on leave without pay-layoff or equivalent status.
- **F-11 · the beneficiary got no mailing allowance and no giving rule.** Edit 4 widened the actor to *"a
  member or an applicant"* and so left every other recipient outside both — including the person entitled
  to a benefit on the member's death, who has 30 days to seek review of a rescission. Pass 12's cure is
  the right one and it is to **stop enumerating**: *"the person"*, *"a person"*.
- **F-20 and F-25 · the seventh adverse notice and the undefined trigger.** The excess notice was the only
  one of seven that did not tell the applicant her fallback rights and the standard cost; it does now. And
  *"until the excess is eliminated"* — the Board's hard stop on accepting elections — is defined, **by
  reference to D 2's limitation rather than by quoting $3,000,000 a second time.**


### c. Two departures from pass 12's own fix direction, and one no-change

**F-22 and F-18 are drafted out by different cures than the ones proposed**, and the reasons are at
[`pass12-disposition`](/MOO/issues/MOO-42#document-pass12-disposition) §3. In short: adding G 4's
extension to the general outer bound would have **re-created F-1's harm** for the member whose date
already sits at the bound, so the ratchet is capped directly instead (*"not … by reason of more than one
involuntary separation"*); and extending the window for the member who was never given her dates would
have made her final date depend on an act the Board may never perform — **the third unbounded limb in
this definition's history**, after the two I have already had to withdraw an assurance about — so she is
put inside **G 4 clause (iii)** on the face of the text instead, which vests her credit and extends no
window.

**F-24 needs no change and the reason is recorded** at §4 of the disposition: once every accepted
election has been settled, cancelled or determined, a late agency notice can no longer harm any member,
so J 1's tail is not extended to catch it.


### d. What is with the Director, and what pass 12 found that is worth more than its findings

**Seven items, §7 items 62 to 69**, five of them routed there by pass 12 itself — the over-cap D 3
request with no operative consequence (which pass 12 says expressly *"is the Director's call, not
mine"*), whether the excess certification engages subsection K, whether a reinstatement should be
characterised as a determination for subsection M, whether an employer gets a right of review, and how
wide enactment 3 clause (i) should be. **Item 67** is F-17's cure, which is a new quarterly
reconciliation duty on the Board, and **item 69** is F-26, which pass 12 expressly left out of scope.
**Item 68 is mine** and is the residual of the F-4 and F-18 cures.

**Three null results are worth more to us than most of the findings.** **N-1: my departure from pass
11's first fix on the separated member was right**, and pass 12 traced the stranding I predicted through
G 1, G 4's settlement sentence and subsection N and found it holds. **N-6: pass 12 had the
deeming-rule-gaming scenario drafted and could not build it** — M 2's 120-day aggregate cap and the
definition's own filing limit confine member-initiated tolling to about four months — and it reports the
failure because it is the premise of F-3. **N-17: edits 9, 10 and 11 raise no Article X defect**, on both
sections opened at source; the opposition will plead it as constitutional and the pleading fails, and
the memo must not concede it.

**One caveat that travels with F-8.** eCFR redirected, so pass 12 read 26 C.F.R. § 1.415(j)-1 at Cornell
LII. That mirror is the whole ground of the edit I have enacted. I have not re-opened it in this
revision and I am not representing that I have; the fix is drafted so that the answer does not change
the text either way, which is why it is safe to take on a mirror.

---


## 0.000000000000000000000000000000 Store revision 38 — §7 item 35 option (b) enacted. Subsection C's zero bar and its refusal notice are deleted, MOO-32's measurement is annotated, and §7 item 26 closes with it. One deletion, no figure moved.

**Two sentences out of subsection C and nothing in.** This revision discharges the standing obligation
[MOO-87](/MOO/issues/MOO-87) recorded at 03:11 on 12 October 2026 and store revision 36 did not carry
out: enact §7 item 35 option (b), land MOO-32's annotation at that item, and close §7 item 26 with it.
**Store revision 36 drafted out pass 11 without the enactment**, and the statement in the annotation
that option (b) would be enacted in that revision is corrected here rather than left standing
(§6.0-38 item 2).

**This revision was rebased once while it was being built.** It was drafted against store revision 36
and **store revision 37 landed under it** — [MOO-104](/MOO/issues/MOO-104)'s counsel review, two
minimal cures and the G 4 deeming withdrawn — so this is store revision **38**, written on store
revision 37, and §5.20 and §6.0-38 take the numbers after that revision's §5.19 and §6.0-37. **Store
revision 37 touched G 4, not subsection C**, and every anchor this revision edits was re-verified
present and unique in its body before the edit was made. Nothing in store revision 37 is reversed,
re-opened or renumbered here.

**a. What came out.** Subsection C's third and fourth sentences: the bar — *"The Board shall not accept
an election for which the amount determined under clause (ii) of this subsection is zero."* — and the
refusal notice that began *"Where the amount determined under clause (ii) of this subsection is
zero."* Subsection C now ends at *"...and the completion date, in the certification required by
subsection D."* Because **§ 51.1-142.4 is a wholly new section**, the deleted words are simply absent
from the draft; they are **not** struck through, since strikethrough would assert they were in the
Code, and they never were. A reader comparing this draft against store revision 36 must read this
record — the markup will not show the deletion, which is the convention revision 7 established and
revision 16 restated.

**b. Why, in one line.** Clause (ii) is measured *"as of the filing date of the member's complete
application"* and clause (v) of *"eligible member"* requires that the member *"has not reached his
unreduced retirement eligibility date ... on the date the member files a complete application"* —
same date, same basis, one-way containment. If clause (ii) is zero she has reached that date, clause
(v) fails, she is not an eligible member, and subsection C opens *"An eligible member may purchase."*
**For every person subsection C addresses, clause (ii) is greater than zero**, so the bar could not
fire and its own notice duty could not be triggered.

**c. The authority, stated because it was not mine to begin with.** Store revision 30 opened item 35 as
the Policy Director's, because deleting an enacted provision is a policy act. The Director routed
MOO-32's measurement back with *"it is a drafting question, not a modelling one, and I am not reaching
into the text — this is the fact, and the call is yours."* **I took option (b) on that routing and I
am naming it here so the reversal is cheap**: one word from the Director and the two sentences go
back, with §7 item 26 re-opening in the form it now carries.

**d. No figure moves, and this one really does not.** The participant count is identical on all three
options of item 35 — the admitted population is fixed by clauses (v) to (viii) on every one of them,
and the bar sat downstream of all four. MOO-32 measured the bar as refusing **0.0000 of 19.6304** on
the authorised cohort, a **strict subset** of clause (vii)'s no-advance band (1.014822), against
**0.4631** on the revision 18 text without clause (vii). **The deletion is not founded on that count**
— see paragraph b — and no option here depends on the count staying at zero.

**e. Housekeeping, which was not optional.** The file had **3,281 characters** of headroom under the
document store's 524,288-character ceiling and this revision's record did not fit. **Three superseded
sections are moved verbatim** to
[`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history) — **§5.14**
(store revision 32's sweep), **§5.15** (store revision 33's sweep for its 24 edits) and **§6.3**
(revision 2's ambiguity record, the oldest material in the file) — every check number, table row and
lettered label preserved, each stubbed here with its durable results, on the convention store
revisions 34 and 36 used. **Nothing was summarised away**, and each stub names the one row of its
section that a later reader must not rely on. The live sweeps are now §5.16 to §5.20 and the live
ambiguity records §6.0-18 onward. Citation sweep **§5.20**; ambiguities **§6.0-38**.


### 5.20 Store revision 38 — the one deletion, checked in three directions

**No conforming amendment is required and none is made.** One provision changed, by deletion, so the
sweep is small; it is run in the three directions store revision 34's §5.16 established — outward from
the deleted words, inward from every citer of the provision, and against what the deleted words
measured.

**Check 1 — inward: what cites the deleted sentences?** **Nothing.** The bar and its notice are cited
by no provision of either section and by no enactment clause. The phrase that would have stranded is
*"the reason stated in the preceding sentence"*, and its **one** occurrence in the bill is in
**subdivision D 2**, where the preceding sentence is D 2's own *"The Board shall not accept an election
for which the certified subsidy exceeds $170,000."* D 2's notice is a **self-contained clone** of the
[**Corrected in store revision 41 on pass 13's F-9:** *two* occurrences was wrong and the conclusion is stronger than it was stated — the only other occurrence in this file is the **drafted and unenacted** replacement at §7 item 34 item 4, which is not bill text.] D 2's notice is a self-contained clone of the
deleted one, as §7 item 34 item 4 records; it is unaffected, and the asymmetry item 34 item 4
describes is now one repaired notice and no clone, which is the better of the two readings it offered.

**Check 2 — inward: does any review or notice route depend on the deleted notice?** **No.**
Subdivision M 2 is a **general** review provision — *"a determination of the Board under this
section"* — and not an enumeration of reviewable determinations, so deleting a notice strands no limb
of it. The member the bar was written for keeps M 2 review, and reaches it earlier: she is refused
under subdivision **D 4**, inside the 30-day eligibility determination, with written reasons, the
standard-cost statement of her subdivision B 2 rights, and review under subsection M.

[**Corrected in store revision 41 on pass 13's F-4: this check is not independent of Check 1, and Check 1 is the whole of the ground.** All four elements are present in subdivision D 4, but D 4's notice duty fires only *"[w]here the Board determines that an applicant is not an eligible member"*, and clause (ii) is **not** an eligibility criterion — the definition of *"maximum purchasable amount"* says so in terms, which is why clauses (vi) to (viii) are drafted blind to it. So D 4 reaches the member **if and only if** she fails clause (v), which is the proposition Check 1 asserts. Three checks were certified and two of them are one check. The member for whom clause (ii) has **no value** is reached by neither, which is pass 13's F-1 and is closed in the text by store revision 41's first edit.]

**Check 3 — outward and against the measured provision: what did the deleted words consume?** Clause
(ii) of subsection C, and nothing else. Clause (ii) survives with all of its other consumers intact;
**§5.16's enumeration of the nine consumers of clause (ii) and of subsection C loses **rows (c) and (d)** — the bar and its notice, two of the nine — and no other row moves; the live enumeration is **seven**.** [**Corrected in store revision 41 on pass 13's F-6**, which read *"exactly one"*: §5.16 enumerates the bar and the notice as two separate rows and both are deleted. A later pass must re-run the inward sweep against seven, and no deleted sentence survives in the text.] The two sentences that state and time the clause (ii) determination —
subsection C's second sentence, which carries both the 30-day determination deadline and the
certification list — are **not touched**, so the duty to determine and state the amount is undisturbed.

**Check 4 — the post-acceptance zero case is still governed.** **Subdivision D 6's fourth sentence**
cancels the election where a recertification reduces or corrects the clause (ii) amount to zero,
refunds every amount paid, releases the reservation and requires notice. Since **item 22's** option (c) froze clause
(ii) at the filing date, that sentence is now the **only** route by which an amount determined under
clause (ii) of zero can arise at all, and it is unaffected by this deletion. **It remains the weakest
notice in the section** — no deadline and no standard-cost figure — and the repair it needs is drafted
at §7 item 34 item 5.

[**Three corrections in store revision 41, all from pass 13.** **F-10:** *"option (c)"* here is **item 22's**, not item 35's — item 35's option (c) is the rejected limb that deletes clause (v) and keeps the bar. **F-8:** *"no review route"* **does not hold** and is withdrawn — subdivision D 6's **third** sentence gives express subsection M review of *"every recertification under this subdivision"* with a 30-day deadline attached to it, and the zero cancellation is by definition produced by such a recertification; M 2 reaches it independently. The deadline and standard-cost limbs stand, and §7 item 34 item 5's drafted repair drops its review limb accordingly. **F-5:** the state the deleted bar guarded against is an accepted election with nothing to **buy**, and D 6's fourth sentence reaches only the **clause (ii)** route to it — subdivision D 6's second sentence clause (i) and subdivision B 4 f clause (i) of § 51.1-142.2 each permit a reduction of the **elected quantity** to zero without clause (ii) moving at all. Pre-existing rather than caused by the deletion, and drafted at **§7 item 70**, which is now the outstanding defect in the zero case.]

**Check 5 — what this deletion makes historical.** §6.0-20's discussion of where R3's sentence sits in
subsection C, and **§5.10 Check 5**'s record of the residual fragility in the phrase *"the reason
stated in the preceding sentence"* as subsection C used it, are now records of a provision that is no
longer in the text. **Neither is amended** — they are the record of what earlier revisions certified,
and bracketing corrections into them is the convention revision 8 established and revision 16
restated. §5.14's stub carries the same note for store revision 32's inward column.


### 5.21 Store revision 39 — the seventeen edits, chased in both directions

**Performed. Full table at [`pass12-disposition`](/MOO/issues/MOO-42#document-pass12-disposition) §5.**
Nine mechanical checks on the operative text and four downstream traces. The durable results:

- ***"last sentence"* now appears nowhere in the operative text** — F-5 removed the only occurrence, and
  no new reference to a sentence by ordinal was introduced. This is the second ordinal reference in this
  definition to rot; the register for the future is to name the provision, not the sentence.
- ***"the earliest of"* survives once**, in G 4's settlement sentence, where three dates are genuinely
  alternatives. F-1's limb was the other one.
- **All five uses of *"limitation year"* in B 4 f now resolve to the plan's own year.** Nothing is
  stranded by the B 4 g deletion or by F-8's redefinition, and B 4 f needed no amendment.
- ***"member or applicant"* and *"a member or an applicant"*: 0 occurrences.** Both were in the giving
  rule and both are now *"person"*. The widening is strictly inclusive, so nothing that relied on the
  rule is narrowed.
- ***"is a qualifying retirement"*: 0 occurrences.** The deeming fiction is out of the bill.
- **Five provisions move together with the final qualifying retirement date** — G 2's clock, F-1's new
  clock, subsection F's duty, D 7's release, and D 1's notice content — because every one of them names
  the defined term rather than restating the date. **That is the property that makes F-2's cure also cure
  F-3 and dissolve the F / D 7 conflict without a carve-out in either provision.**
- **F-6's condition bites on the extension only.** The 90-day vesting branch is unchanged and still runs
  from the separation itself, so a member whose agency never notifies keeps the vesting branch inside her
  unmoved window and loses only the extension.
- **Title, enacting clause and all enactment clauses: unchanged.** No edit adds, deletes or renumbers a
  subsection, subdivision or clause, so no enactment-clause list needed conforming.


### 5.22 Store revision 40 — the one re-cut clause, chased in both directions

Full sweep at [`moo118-disposition`](/MOO/issues/MOO-97#document-moo118-disposition) §5; the four rows that carry a result are here.

| Check | Result |
| --- | --- |
| **§ 51.1-155.1** — the one citation new to subdivision G 4 | **Not new to the section.** Already cited in the subsection A definition of *"qualifying retirement"*, which admits a service retirement *"under § 51.1-153 or under subsection A or C of § 51.1-155.1."* **No new section joins the act**, which still amends one and adds one, and the title does not change. Pass 13 **F6** verified that § 51.1-155.1 A and C impose no in-service, notification or effective-date requirement of their own, so naming the section **disapplies nothing today**; it is named because naming one of the definition's two gateways and not the other invites the inference that the unnamed one survives. |
| **"subdivision D 1"** — the first reference to D 1 from inside G 4 | D 1 cites § 51.1-153 four times and carries two duties of its own that restate it: the compelled notice of retirement, and the proviso that the stated effective date be *"on or after the day following the member's last day of service."* Both are requirements **of D 1** and not of § 51.1-153, so the old clause left them standing against a dead member (**F4**). Naming D 1 in the enumeration and in the residual reaches both. **D 1 is not amended**, and the disapplication is confined by *"In the case of death"* and twice by *"for that purpose."* |
| **The three enumerated limbs** | Verified against the official text of § 51.1-153 this revision. *"Member in service"* and *"upon written notification to the Board setting forth the date the retirement is to become effective"* appear in **five** gateways — subsection A, subdivisions B 1, B 2 and B 3, and subsection D — so the limb reads *"any requirement of § 51.1-153"* and not *"of subsection A"* as the reviewer's fix direction had it, which would have reached one of five. The Code's own idiom is followed: § 51.1-153 C says *"any requirements as to the member being in service shall not apply."* |
| **Conforming amendments elsewhere in the Code** | **None required and none made.** § 51.1-153, § 51.1-155.1 and subdivision D 1 are cited and not amended; § 51.1-155 is still named nowhere in G 4 (zero occurrences, re-counted); § 51.1-162 and § 51.1-163 remain cited nowhere, which is the standing trade and the reason **§7 item 60, the memo's risk section and the drafting request to DLS** have to carry it. **Consumers of the hypothetical** are unchanged, because the clause only switches requirements **off** inside a sentence scoped to the death case — checked at all nine locations where *"qualifying retirement"* is used, and pass 13's null results 1, 3 and 5 agree. **Enactment clauses:** nothing to add. **Markup:** the clause sits inside G 4's existing `<u>` block and nothing is struck through, because § 51.1-142.4 is wholly new. |

---


### 5.23 Store revision 41 — the two edits, checked in three directions

**No conforming amendment is required and none is made.** Two provisions changed, both by addition, and
the sweep runs in the three directions §5.16 established — outward from the new words, inward from every
citer of the changed provisions, and against what the changed words measure. Five checks; the full
working is at [`pass13-disposition`](/MOO/issues/MOO-87#document-pass13-disposition) §5.

**Check 1 — outward: does the new third sentence of subsection C strand an ordinal?** **No, and this is
the check that had to be run first.** Adding a sentence to subsection C renumbers the sentences of
subsection C, so every ordinal reference to them had to be found. **There is none.** The operative text
contains 20 references of the form *"the first sentence"*, *"the preceding sentence"* or *"the second
sentence of subdivision B 2"* — counted against the text as landed — and **not one of them refers to a
sentence of subsection C**; the string *"sentence of subsection C"* appears **nowhere** in the bill; the
closest are enactment 3's references to *"the second sentence of subdivision B 2"* and *"the first
sentence of subdivision D 2"*, both outside this subsection and both unmoved. The record references to
*"subsection C's third sentence, the zero bar"* and *"subsection C's fourth sentence"* are in §5.20,
§6.0-20 and §5.10 and are the record of a provision no longer in the text; they are **not** amended, on
the bracketing convention revision 8 established, and §5.20 Check 5 already says so.

**Check 2 — outward: every term the new sentence uses is already defined or already in the chapter.**
*"Creditable service"* is Code-defined (§ 51.1-124.3); *"unreduced retirement eligibility date"*,
*"complete application"*, *"election"* and *"the certification required by subsection D"* are defined or
used in terms in this section; *"the filing date of the member's complete application"* is clause (ii)'s
own formulation, fixed by subdivision D 4 *"for all purposes of this section"*. **One new internal
citation is created** — *"clause (ii) of this subsection"*, the first such citation inside subsection C
since the deletion — and it is a standing obligation on any later renumbering of subsection C's clauses,
alongside the convention sentence's citation of clause (vii) recorded at §5.16.

**Check 3 — inward: the eight citers of subsection C, each tested against the new sentence.** All eight
read correctly and none is stranded. **The one that matters is the definition of *"maximum purchasable
amount"***, which provides in terms that *"[c]lause (ii) of subsection C does not limit the maximum
purchasable amount"* — so the new sentence **cannot move the maximum purchasable amount**, and because
clauses (vi) to (viii) of *"eligible member"* run on that amount, **admission is unchanged on either
reading**. That is the textual reason no figure moves. The *"complete application"* definition confines
what the Board may require to what is necessary to determine *"the service credit the member may
purchase under subsection C"*, which the new sentence makes determinable rather than indeterminate.
Subdivision D 6's trigger (*"the service credit the member may purchase under subsection C would
change"*) stays reachable through clauses (i) and (iii). Subdivision D 6's fourth sentence and
subdivision B 4 f clause (i) and D 6's second sentence clause (i) are considered in Check 5.

**Check 4 — inward: clause (v) is cited by number nowhere in the bill.** Verified mechanically against the text as landed: the
strings *"clause (v)"* and *"clause (vi)"* appear **zero** times in the operative text; *"clause
(vii)"* appears **once**, in the month-convention sentence of the same definition; and the single
occurrence of *"clause (viii)"* is in subdivision B 1 of § 51.1-142.2, where it refers to clause (viii)
**of that subdivision** and not to the definition. The clause (v)
edit therefore strands nothing, and the phrase *"a complete application"* is kept in clause (v) so that
clauses (vi) and (vii)'s *"that application"* keeps its antecedent — which is why the date formulation
of clause (v) is **not** aligned with clause (ii) as pass 13's F-12 suggested; see §6.0-41 item 3.

**Check 5 — against what the changed words measure, and the one thing this sweep does not certify.**
Clause (ii) measures a number of months at a fixed date and the new sentence states what it does when
that number does not exist; clause (v) measures a date on the same base as clause (ii), which is now on
the face of both limbs. **What this sweep does not reach is the elected quantity.** Subdivision D 6's
fourth sentence governs an amount determined under **clause (ii)** that is reduced or corrected to zero;
it does not govern an **election** reduced to zero under D 6's second sentence clause (i) or under
subdivision B 4 f clause (i) of § 51.1-142.2. That is pass 13's F-5, it is pre-existing rather than
caused by either edit, and the repair is drafted at **§7 item 70**.


### 6.0-26 Ambiguities resolved in store revision 34

1. **Whether to enact pass 10's S-1 at all, when the reviewer routed it to the Director.** Enacted,
   and this is the one reviewer routing I did not follow. The grounds are at §0.x b: the
   membership-service base was **my own** words from store revision 22 and nobody chose it; the agreed
   minimum-necessary rule requires the base that produces the date; and the direction of effect is
   downward on cost, so nothing the Director may decide is foreclosed by repairing it now. **The
   reversal is one phrase and is drafted in §7 item 43.** What I would not do is leave the bill's only
   quantity measured against a term that cannot produce the date it is measured to.
2. **Which words to put in place of *"membership service."*** Not the reviewer's one-word substitution.
   *"The creditable service the member has **earned**"* would read to exclude credit she **bought** or
   was **granted**, which is the entire population S-1 is about, so the defect would have survived in
   part; and *"credited to the member"* would charge her for her employer's reporting lag. **"All
   creditable service for which the member is entitled to credit as of that date"** reaches earned,
   purchased and granted credit alike and is proof against the lag. It is four words longer than the
   minimal fix and I think the four words are load-bearing. Clause (iii)'s *"creditable service the
   member has earned as a state employee"* is **left alone**: there the word *earned* is doing real
   work, because clause (iii) is a limb about state service rather than about her position.
3. **The month-end fallback: symmetric, and the arithmetic that justifies it.** Pass 10's M-3 found
   that the convention as enacted in store revision 32 **refused a thirty-day advance and admitted a
   twenty-eight-day one** — a member moved from 31 March to 1 March was told she had not moved her date
   by a month, because the fallback pulled the boundary back to 28 February. The fallback is now *"on or
   before the **first day of the month in which that second date falls**."* **The check that makes this
   safe:** the corresponding-date rule's own shortest month is 1 February against 1 March, which is
   **28 days**; the symmetric fallback's shortest is 29 March against 1 March, which is also **28
   days**. So the repair **admits nothing shorter than the convention already admitted**, and it
   removes a tightening of up to three days that applied only to members whose without-purchase date
   fell on the 29th, 30th or 31st of a month whose predecessor was shorter. **The Director's one-month
   threshold is untouched**; expressing it in days instead is item 44's neighbour and still theirs.
4. **A date rule, not a period rule, and out of clause (vii).** Pass 10's M-4 is right that the old
   sentence defined *"a month"* as a period **ending** on the corresponding day — and a month-long
   period ending on 28 February begins on 28 January and never touches 31 March, so it could not
   measure the interval the clause compares. The convention now says when one date **is at least one
   month earlier than** another, which is the comparison clause (vii) actually makes, and it says it in
   its own sentence rather than as the third comma-separated fragment inside an enumerated clause.
   *"The later of those two dates"* (Mi-11) disappears with it: more creditable service cannot postpone
   an unreduced retirement eligibility date, so the later of the two was always the without-purchase
   date and the indirection cost a reader an antecedent hunt for nothing. **The cost of moving it** is
   the new internal citation recorded in §5.16, and I judged an unreadable sentence the worse of the
   two.
5. **Mi-9 — which purpose the rounding rule serves, since the reviewer asked me to say.** It fixes the
   **direction** of rounding and nothing else. It does **not** make the purchasable quantity a whole
   number of months, and it was not meant to: limbs (i) and (iii) are expressed in years and take no
   rounding rule, and clause (i) can itself be fractional — four years less 1.3 years previously
   purchased is 32.4 months — so for about **one member in eleven**, where limb (i) or (iii) binds, the
   *"least of"* still yields a fractional cap. **Administrability in whole months was not the purpose
   and is not achieved.** If the Director wants it, it is a different and larger edit and it belongs in
   its own item.
6. **Mi-12 — *"exact complements"* is withdrawn; the relation is one-way containment.** §7 item 35 and
   store revision 32's §0.x f said clause (ii) and clause (v) were exact complements. They are nested,
   not complementary: because membership service is a **subset** of creditable service, clause (ii) = 0
   still implies clause (v) fails — which is the only direction item 35 relies on, so **the
   verification holds** — but the converse failed, since a member with prior service credit could fail
   clause (v) while clause (ii) was positive. **S-1's repair closes the gap in fact as well as in
   direction**, because the two now run on the same base; I am still withdrawing the word, because the
   verification should not rest on an edit the Director may reverse.
7. **M-7 enacted rather than routed, and why that is not a new rule.** Four words widen D 6's trigger
   to a **corrected** record. Without them the fourth sentence of D 6 — cancel the election, refund
   every amount, release the reservation, notify the member of her subsection B rights — had no
   reachable trigger under option (c), because clause (ii) is a historical computation as of a fixed
   past date and the only thing that can move it is a correction to the record of those facts. D 6's
   final sentence deals expressly with *"an error by the **Board** in a certification"* and says
   nothing about an error in the **record**, which made the omission look considered rather than
   accidental; pass 10's scenario is the member whose agency reports six months of her service late,
   who on corrected facts **was never an eligible member**, and for whom no provision in the bill is
   keyed. I have restored the work rather than left the sentence as a dead letter, and §0.x d records
   that it strengthens item 35 (b) rather than disturbing it.


### 6.0-35 Ambiguities resolved in store revision 35

**Stated in full in [`moo64-record`](/MOO/issues/MOO-42#document-moo64-record) §a and §6.** **Four changed
the Director's words and are mine:** item 28's **death limb narrowed** to a case to which clause (i) of G 4
applies, because the approved words would have reversed the [MOO-44](/MOO/issues/MOO-44) line (the policy
question is item 45 and I did not take it); a **tolling sentence**, without which G 2's duties contradict the
new prohibition; a **60-day deadline** on the rescission; and the **no-recovery limb enacted inside G 4's
existing prohibition** rather than as a second overlapping sentence.

**Nine more are pass-10 repairs to those same words, and they are mine too:** *"is settled"* rather than
*"may be settled"* (**S1**); the tolling reaching every period of both kinds in subdivision 2 and G 4
(**S2**, **S3** — § 51.1-156 A is why the second is a real collision); **notice and subsection M review** on
the rescission (**M8**); the redetermination run from the approval and the bar extended to the notice
(**m19**); *"pending"* **defined** as from filing until the Board first acts, which bounds the gaming surface
without a cap — the cap is item 52 (**M12**); a determination in contravention **of no effect** (**m18**); a
**deadline** on the reinstatement (**M16**); and D 1's notice stating the outer bound, the rounding-forward
rule and the three-day rule, with the floor stated as a permission (**M9**, **M10**).

**Two consequences stated rather than cured.** A refund already paid under G 2 (ii) is not recovered on a
restoration — bounded by **less than one month of credit at standard cost**, which is item 50. And the
settlement bar is lifted by a **deeming inside the rescission sentence** rather than by amending the bar
sentence, so the bar still reads naturally for every other case.


### 6.0-36 Ambiguities resolved in store revision 36

Seven, and the first is the one that has now been wrong twice.

1. **The retirement window's envelope, stated once and not restated.** §6.0-24 said the window had *"four
   bounded components, each bounded on the face of the text."* It was wrong about D 1, which store revision
   33 cured; and store revision 33's own cure was wrong about subsection M, which this revision cures.
   **The envelope the text now delivers is: 12 months, plus the three-month processing extension, plus at
   most 120 days of tolling, plus the days of the Board's own lateness — the whole subject to an outer
   bound of 12 months after the date that applies under the first sentence of the definition or the later
   date approved under it, and subject to a floor so that the bound cannot fall before the first day of the
   second month after the Board tells the member her dates.** Two things I will not do: state that envelope
   as an assurance that every component is bounded, because the sentence has had to be withdrawn twice and
   a committee staffer will read the record as well as the bill; and resolve the choice of bound by
   drafting, which is **§7 item 39** and now carries pass 11's changed recommendation.
2. **Whether to bound the tolling or to give the Board's silence a consequence.** Pass 11 offered three
   cures and I took none of them whole. A 180-day cap on the excluded period introduces a figure nobody
   has priced. A deemed refusal at 120 days is a **consequence for the member** — she loses her
   reconsideration because the Board was slow — and it is the mirror of the § 2.2-4021 B default judgment
   that §7 item 33 was withdrawn to avoid, pointed the other way. Option (a)'s absolute 21-month bound is a
   policy choice and an unpriced numeral. **What is enacted keeps the member's protection and bounds the
   date**: the window closes on time, and a member whose tolling has not ended by then may still retire in
   a deemed qualifying retirement within about a month of the Board acting. The cost is one more sentence
   in an already long definition, and the benefit is that **nothing the Board fails to do can lengthen the
   period a reservation is charged against the $3,000,000.**
3. **Which cure to take for the involuntarily separated member.** Recorded at §0.x a 2 rather than here,
   because it is the one place in this revision where I departed from a reviewer's own first fix, and the
   reason — that disapplying the final-date limb would strand settlement and put the subsidy on the trust
   with no appropriation behind it — is a finding of mine rather than a drafting preference.
4. **Whether the final-date extension on an involuntary separation should be open-ended.** It is not. It
   reaches only a separation occurring **on or before** the date that would otherwise be the member's final
   qualifying retirement date. Without that limit, a member separated in 2040 — whose election had long
   since been determined under G 2 — would acquire a fresh window, and the only thing stopping the subsidy
   being settled would be G 4's bar on settling after a determination has taken effect, which is a thin
   place to rest a cost. With it, the branch protects the member it was written for and nobody else.
5. **Whether the three-day mailing allowance should reach the Board's own deadlines.** It still does not.
   Store revision 33 made that choice deliberately — the allowance exists to protect a person who learns of
   a decision by post, not to give the decider more time — and widening it to *"a member or an applicant"*
   does not disturb it. The one consequence is finding 9's, which is why the G 2 notice floor now tracks
   the member's period rather than a fixed 30 days.
6. **Whether to keep a § 415 limitation-year designation at all.** B 4 g is deleted rather than confined.
   The cheapest compliant version — *"For the purposes of this subdivision, the limitation year is the
   calendar year"* — would say in the Code what B 4 a already says in the same subdivision, and the
   designation's only possible federal effect would be one the regulation requires to be made by plan
   amendment. **If the Director wants a designation kept, §7 item 57 has the sentence.** The real question
   is a fact about VRS's plan document, which is with Statutory Researcher at
   [MOO-115](/MOO/issues/MOO-115), and the bill should not guess it.
7. **What the wait-listed applicant is told.** She is told the fact, the amount and the date of an excess
   that moved her place in the queue, and she may seek reconsideration of the reinstatement. She is **not**
   told the cause or the member's identity. Pass 11 established that there is no privacy or FOIA bar on
   telling her, so this is a choice rather than a constraint: the information she needs in order to decide
   whether to complain is the existence and size of the excess, and the information that identifies another
   member in a cohort of nineteen is not. The Chairmen, who can do something about an unappropriated
   excess, get all of it.


### 6.0-38 Ambiguities resolved in store revision 38

**1. Deletion, not strikethrough, and the reason is that the section is new.** § 51.1-142.4 is added by
this act, so every word of it is new language and the whole section is underlined. Striking the two
sentences through would assert that they stand in the Code today and are being removed from it, which
is false. They therefore leave the draft silently, and §0.x a records what left so the comparison
against store revision 36 is possible.

**2. One sentence of MOO-32's annotation is corrected rather than inserted verbatim, and I am naming
it because I promised the paragraph verbatim.** The drafted paragraph said option (b) *"is enacted in
the revision that drafts out [MOO-107](/MOO/issues/MOO-107)'s pass 11"*. **That revision landed as
store revision 36 and did not enact it**, so the sentence would have gone into the bill asserting
something untrue of the bill. It now reads that option (b) is enacted in **store revision 38**, says
what store revision 36 did not do, and drops the sentence *"Until then the bar stands in the text."*,
which the enactment falsifies. **Every other word of the paragraph is the drafted text unaltered**,
and the record at [`moo32-zero-bar-measurement`](/MOO/issues/MOO-87#document-moo32-zero-bar-measurement)
§6 keeps the original wording.

**3. I kept the three checks and both rejected options under item 35 rather than cutting them to the
decision.** The cheaper edit would have replaced the whole item with the enacted result. I did not,
for two reasons: the next counsel pass has to **re-run** the three checks against the deletion as
landed, not against the deletion as proposed, so the checks must be in front of it; and the Director's
reversal is a live option, which needs the weighing of (a) and (c) to still be on the page. The item
is longer than the decision requires and that is deliberate.

**4. I did not touch clause (v), clause (vii), or subsection C's second sentence.** Item 35 is express
that *"the bar and clause (v) must be amended together or not at all <u>[store revision 46: §7 item 35 now reads *"the bar, clause (v) and clauses (vi) to (viii)"* in both of its statements of the rule — pass 14's **S-2**; this quotation is annotated rather than rewritten so the earlier state of the rule stays visible]</u>"*, and option (b) is the limb that
keeps clause (v). Option (c) — delete clause (v), keep the bar — remains not recommended for the
reason the item gives: it moves an eligibility fact out of the definition that collects them and
screens thirty days later.

**5. What I did not do, and it is the one thing a reader may expect.** I did not add any replacement
screen. There is no provision anywhere in the bill that now tests whether clause (ii) is zero at the
certification stage, and that is the intended result: the fact is tested once, at admission, by clause
(v). If the Director wants a belt-and-braces screen retained, option (a) is the reversal and it is one
sentence restored, not a new draft.

[**Two corrections in store revision 41, from pass 13's F-1 and F-2.** The statement that *"the fact is tested once, at admission, by clause (v)"* is a **dichotomy that does not cover one measured class**: for a Plan 1 member under age 50 at the filing date, clause (ii) is neither zero nor greater than zero — no number of months of service answers it — and clause (v) passes. **Store revision 41's first edit closes that case in the text.** And the screen that confines the class is clause **(vi)**, not clause (v): clause (v) is a date test such a member passes, and it is clause (vi)'s one-month reachability window that makes the class 0.0826 participants instead of the whole age-49 band. Pass 13 verified that a member six months short of 30 years who turns 50 next month passes clause (vii) and **fails clause (vi)**. The *"amend together or not at all"* rule is extended to clauses (vi) to (viii) at §7 item 35 accordingly.]

---

## Moved in store revision 44 — §3, what the actuarial cost statement will need from this draft

**Moved verbatim from [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) in store revision 44**, which
enacted the Policy Director's [MOO-101](/MOO/issues/MOO-101) answers together with
[MOO-98](/MOO/issues/MOO-98)'s and [MOO-121](/MOO/issues/MOO-121)'s findings and arrived with **11,042**
characters of headroom against a record of about 26,000. It went out under the Director's standing rule on
MOO-101 section E — ***"§3 moves next; §1, §5, §6 and §7 stay with the bill"*** — and it is the first
section of §1 to §8 other than a record section to leave the file. **Every item number and every bracketed
in-line correction is preserved**, so a citation of the form **§3 item 7** still resolves here, and the
stub left in its place carries the durable results. **Nothing was rewritten and nothing was summarised
away.** Read warning 3 above before taking any number out of it.

## 3. What the actuarial cost statement will need from this draft

> **ADDED IN STORE REVISION 33 — two items the § 30-19.1:7 statement needs that are not repricings, both
> from [MOO-95](/MOO/issues/MOO-95)'s pass 9, which reran the model from its own copy and reproduced
> every published figure.**
>
> **1. Cap utilisation on the reservation basis, which is the basis the cap actually counts.** Low
> **38 percent**, central **76 percent**, high **126 percent**, each including the mandatory 20 percent
> contingency. So **on the published high take-up branch the $3,000,000 is over-subscribed and refuses
> roughly one election in five before a dollar is spent**, and **central headroom is $723,758 — about six
> reservations** at the mean reservation-basis certified subsidy of $100,311 plus contingency. The
> sentence the statement needs, and it is one sentence: *the $3,000,000 is a cumulative cap over the
> pilot and a settled subsidy is never released, so the cap rations total admissions rather than
> concurrent ones; on the high take-up branch it is 126 percent subscribed.* Pass 9 also confirms
> independently that **the 12-month window does not ease the $3,000,000**, because reservations are
> certified on the anticipated **earliest** qualifying retirement date.
>
> **2. An interest-free deferral the cap newly bounds.** B 4 b fixes the amount payable irrespective of
> when payment is made and stops statutory interest at the valuation date, so B 4 f's 24-month cap fixes
> for the first time the outer size of the deferral: a member may pay as late as **36 months after
> acceptance** at a price struck on the original valuation date. At the assumed rate of return that is of
> the order of **$11,000 to $13,000 of foregone investment return per deferring member**, borne by the
> **trust**, outside the certified subsidy and outside the appropriation. The cap is an improvement —
> before it the deferral was unbounded — and the residual belongs in the statement as a quantified,
> one-sided omission alongside the retirement-date distribution in item 4 below.
>
> **And one branch count that is now right.** §7 item 41 records that a member may hold a reservation and
> pay nothing; until that item is answered, no statement of how many members the appropriation reaches
> may assume that every accepted election is a purchase.

> **Revision 9 warning — read before quoting any figure in this section.** Every aggregate and
> per-member certified-subsidy figure below comes from [MOO-53](/MOO/issues/MOO-53) and predates
> [MOO-48](/MOO/issues/MOO-48)'s priced run of **the bill as drafted**. The controlling set is
> [`package-v11-corrections`](/MOO/issues/MOO-3#document-package-v11-corrections) **§4**, which among
> other things puts mean certified subsidy per member at **$110,042** (90th $160,468, maximum
> $208,905) and gives the headline as **about $2.0 million** to the Commonwealth. This section has
> **not** been re-written on that set, because its cap arithmetic is itself under query at
> [MOO-71](/MOO/issues/MOO-71) and rewriting §3 now would replace three stale figures with a stale
> section. The reconciliation is revision 10's. **Until then nothing in §3 may be quoted against the
> authorised set**, and no exhaustion year, denial percentage or funded-election count is authorised
> at all. See §0.0000000e.


> **Revision 24 — the figure set at the 12-month rung, from [MOO-85](/MOO/issues/MOO-85), and the one
> sentence that must go in the statement.** The Director moved the retirement window to 12 months on
> 12 October 2026 and every authorised figure had been priced at rung 1, so the set was re-walked.
> **At the 12-month rung net trust cost is $1.4 million in present value** (range $0.71M to $2.4M on
> take-up; nominal aggregate certified subsidy **$1,789,417** central, which is the figure D 2 counts
> because a reservation is a dollar amount certified and not a discounted one), spread over **18.9
> members** at a mean certified subsidy of **$94,649** and a median of **$93,898**. Per-member
> percentiles: 75th **$123,757**, 90th **$147,423**, 95th **$158,237**, maximum **$194,837** — against
> rung 1's $137,754 / $160,468 / $170,755 / $208,905. **The distribution does not shift in parallel**:
> the body falls 13.8 percent and the tail only 6.7 percent, because the dearest members are the ones
> furthest from their counterfactual retirement date, where the marginal month of deferral is cheapest.
> **Participant count is unchanged at 18.9.** Five things the statement has to say alongside those
> numbers:
>
> 1. **Cap utilisation does not move, and the window does not ease the $3,000,000.** The cap counts
>    subsidies **reserved**, and reservations are certified on the anticipated earliest qualifying
>    retirement date. MOO-85 reproduces MOO-78's utilisation figures unchanged. An artifact that
>    carries the lower trust cost alongside the old cap sentence is consistent; one that implies the
>    longer window relieves the appropriation is not.
> 2. **$170,000 stands on the basis D 2 screens.** The Director's own rule returns **$160,468 at the
>    12-month rung — the same figure it returned at rung 1** — and $170,000 sits about 5.9 percent above
>    it and refuses about **5.4 percent** of the cohort. On the priced rung-12 amount the rule would
>    return about $145,000 and on the intended-bite basis about $155,000; the choice between the three
>    is the Director's (§7 item 3) and I have moved nothing.
> 3. **The ceiling refuses; it does not trim, and the two differ by a factor of twenty.** Whole
>    certified subsidy of refused members, central: **$183,577.** Excess over $170,000 only: **$9,147.**
>    The first is the figure the statement needs.
> 4. **The dominant assumption is not the rung and not take-up.** `pv_with_design` values one retirement
>    date for every member, so rung 12 prices **every member retiring on the last permissible day** —
>    the cheap end, one month short of the cheapest. All-at-the-earliest-date is **+16.3 percent**;
>    uniform over the thirteen permissible dates is **$1,517,644, +7.5 percent**, which reports as
>    **$1.5M against $1.4M** at two significant figures. The exposure is **one-sided**: every deviation
>    from all-at-the-final-date is dearer, and there is no published distribution of chosen retirement
>    dates inside a VRS window, so the assumption has no external anchor. **This is the assumption to
>    put in front of a patron, not the rung label.**
> 5. **The subsection A floor binds at this rung and did not at rung 1.** 0.41 of 18.91 members (2.17
>    percent), +0.14 percent of the aggregate, and it changes no refusal count. A longer window lowers
>    the certified subsidy and does not lower the B 4 a standard cost, so the floor catches up from
>    below. It is a one-sided omission that grows with the window.
>
> **Rung arithmetic, for the record.** The earliest qualifying retirement date is itself ladder rung 1,
> so the drafted final date is **rung 13** ($1,390,216, −1.5 percent, still $1.4M at two significant
> figures) and the outer bound with the three-month processing extension is **rung 16** ($1,324,049,
> −6.2 percent, which does move the second significant figure). Both are **cheaper**, so the authorised
> figure is conservative against the rung arithmetic alone.

> **Revision 24 — two inputs no run has, from pass 8 §4 and pass 7 §4.** Neither is a reprice and
> neither is mine to produce. First, **the priced run carries no rate of failure to retire in a
> qualifying retirement**, and a G 2 failure rate makes the bill *cheaper* while cutting the delivered
> benefit — at a 20 percent failure rate the Commonwealth has administered 18.9 elections to buy about
> 15 accelerated retirements, and nothing in the subsection J report distinguishes the two. Second,
> **release timing is now a fiscal input**: revision 21's G 2 trigger releases a failed member's
> reservation up to twelve months earlier than before, which returns capacity to the pool sooner and
> matters wherever the ceiling binds. Third, from pass 7: **the document reports the distribution of
> certified months and nowhere reports the distribution of acceleration months**, which is the quantity
> the behavioural claim is actually about and the gap a committee would find first. **Revision 24 also
> adds a third and a fourth outcome branch to the accounting**: a member whose quantity is recertified
> to zero now has her election **cancelled** with a full refund (D 6), and a reservation released
> otherwise than in accordance with D 7 is now **reinstated** over the cap (G 4). Any statement that
> every accepted election either settles, is re-valued, or vests is now incomplete.

§ 30-19.1:7 obliges the VRS Board to prepare an impact statement on any bill that amends Title 51.1,
and the procedural resolution sets the deadline (in 2026, Rule 7 of HJ 29 — statements for all VRS
bills filed by day one, due roughly two weeks later). The statement decides the bill. Eight points
the drafter can speak to:

1. **The cap is drafted so that the scorer does not have to assume uptake** — but say honestly what
   it does and does not bound. The number VRS cannot derive (how many state employees are veterans
   with purchasable service) does not control the Commonwealth's exposure, because § 51.1-142.4 D
   forbids acceptance until the subsidy is certified and reserved. HB 1867 (2023) is the cautionary
   case: VRS wrote that it could not determine the population, assumed 1 percent of 150,000 teachers
   and produced $50 million. **This draft gives VRS a ceiling to score instead of an assumption to
   invent.** Two caveats that must travel with that sentence: no § 51.1 bill in the 2015–2026 record
   carried a binding aggregate cap, so there is no Virginia precedent for how VRS will treat one;
   and **the cumulative-or-per-fiscal-year question is no longer bracketed:
   revision 6 drafted the Director's choice of the cumulative limit in D 2 and conformed Enactment 3
   (ii), and §7 item 6 records it as closed. The statement should say plainly that $3,000,000 is a
   limit across the pilot, not per fiscal year, and that a settled subsidy stays charged against it.
   MOO-44 §8's roughly $9,000,000 difference is resolved in favour of the smaller figure, so the
   scorer no longer has two bills to choose between** — which removes the "a scorer who cannot tell
   which bill it is will score the larger" risk rather than leaving it open. **[Conformed in
   revision 7.** Through revision 6 this item still read *"whether the cap is cumulative or per
   fiscal year is still bracketed (§7 item 2), which is worth roughly $9,000,000 … a scorer who
   cannot tell which bill it is will score the larger."* That was a revision 6 conforming miss — the
   question was decided on [MOO-60](/MOO/issues/MOO-60) and drafted into D 2 in revision 6 — and it
   also pointed at the wrong §7 item. **This correction is mine and is not a decision**: it records a
   choice already made, and it changes no bill text and no figure. Flagged to Policy Director in the
   revision 7 handoff rather than fixed silently.**]**
2. **"Certified subsidy" now measures one liability change, not two overlapping ones.** Revision 1
   defined it as the actuarial-equivalent-cost quote *plus* an acceleration term. MOO-45 §2.2 found
   that the AEC quote already contains an eligibility-acceleration element, so the two terms
   overlapped by **$2,374,550 aggregate / $23,028 per member — 44 percent of net plan cost.**
   Revision 2 takes one liability measure in two states of the world. It still captures the
   behavioural cost, which is the point MOO-7 and MOO-31 both insisted on and which MOO-31 priced at
   $5,370,529 with the retirement condition against $1,445,239 without it. A cap defined only on the
   price difference would not bind the real cost; the floor in the last sentence of the definition
   guarantees it is never *less* than the price difference.
3. **The acceleration counterfactual is now in the Code, and that is worth more than any other
   sentence in the draft.** MOO-44 §8 showed that leaving it to the Board put the realised cost
   anywhere between **$3.0M (28 elections) and $11,148,043 (213 elections, 3.7× the cap)** without
   anyone breaching the statute — because a Board measuring acceleration against the member's
   earliest unreduced date gets zero acceleration by construction for a minimum-necessary purchaser.
   The definition now names the assumption set (the most recent valuation) and the counterfactual
   (the member's retirement date projected by the retirement decrements in those assumptions,
   without the purchased credit). **That confirmation has been obtained, and the actuary should be
   given its result** ([MOO-53](/MOO/issues/MOO-53) §6.3): the drafted counterfactual forecloses
   **both** zero-acceleration readings on **all 44 priced cells**, with a minimum margin of **+3.33
   years** over the retire-on-the-date reading and **+1.79 years** over the earliest-unreduced
   reading, because a decrement projection returns a certain date only if some rate reaches 100
   percent and the highest published Plan 1 rate below the terminal age is **31 percent at age 66**.
   Two things the actuary must be told with it. **First, the standard is worth more than MOO-44
   estimated**: the reading it forecloses would meter **$10,510** per election, admit the entire
   cohort, never exhaust the appropriation, and leave the trust carrying **$10,996,295 — 3.67× the
   appropriation**, or **$31,743,870** on MOO-44's demand-unconstrained basis. **Second, MOO-44 §8's
   statement that the floor alone converts the worst case is wrong** (MOO-53 §6.4): under that
   reading the floor certifies **$2,621,670**, which is *below* the $3,000,000, so every modelled
   member is admitted and nothing is rationed until demand exceeds **113 elections**. Clause (ii) is
   the first line; the floor is the second.
4. **SUPERSEDED IN REVISION 9 — the ceiling is $170,000, set off the distribution, and MOO-46
   Decision 2(e)'s rule is retired as its basis.** The Director directed the figure on 11 October
   2026; `package-v11-corrections` §3.2 finds Decision 2(e)'s rule has no solution; and the figure is
   the 90th percentile of the bill's own Pathway-A-only cohort (90th **$160,468**, maximum
   **$208,905**) rounded up. **The definition does not move with it** — §0.0000000b. Everything from
   here to the end of this item is the revision-5 derivation, retained as the record of how the
   bracket was reasoned and **not** as the current basis; its exclusion rates and trimmed amounts are
   **trim-basis** quantities and D 2 refuses rather than trims (§0.0000000c).

   **The per-member ceiling is bracketed, and MOO-46 item 2 makes it a rule rather than a figure:**
   *the lowest round figure at which the appropriation funds at least 30 elections in the adverse
   (dearest-first) order*, the figure to come from MOO-48. Revision 2 filled the blank with $80,000;
   revision 3 hands it back, because MOO-46 directs the blank to stay and because the window numeral
   (item 7 below) moves the distribution the rule is applied to. **Revision 5 fills the bracket with
   `[$100,000]`, and the MOO-45 derivation this paragraph used to carry is superseded.**
   [MOO-53](/MOO/issues/MOO-53) §4 repriced the sweep on the definition as drafted:

   | | on the drafted definition (MOO-53 §4) |
   |---|---|
   | Cheapest Pathway A election — the cohort the bill admits | **$81,278** |
   | So `[$80,000]` excludes | **100 percent of the bill-eligible cohort**, trimming $1,978,064 (36 percent) and leaving the worst-affected member **$90,343** short |
   | MOO-46 Decision 2(e)'s rule — lowest round figure funding ≥ 30 elections dearest-first | **$100,000** on the A+B cohort **and** $100,000 on the Pathway-A-only cohort |
   | What $100,000 costs | 62.2 percent of the A+B cohort and **69.1 percent** of the bill-eligible cohort lose part of their subsidy; worst uncovered amount **$70,343**; $1,244,262 trimmed |
   | If Pathway A is to be held whole instead | **$175,000** (A-only) or **$185,000** (A+B) — excludes nobody and trims nothing, so it does no fiscal work the model can see, but it bounds the within-cell salary dispersion the model does not resolve |

   **Three warnings for the actuary.** First, the exclusion rate and the trim are **upper bounds**:
   the model does not re-estimate take-up against the ceiling. Second, the ceiling has become a
   **sensitive instrument on a definition where it used to be a blunt one** — MOO-45's flat
   $30,000-wide identical-set band is gone, the identical-set interval around the figure has
   collapsed to **$4,114**, and every candidate figure now selects a materially different set of
   members. Third, **the modes have inverted**: Pathway B's maximum rose from $54,974 to **$182,800**
   and now exceeds Pathway A's **$170,343**, so MOO-46 Decision 2(e)'s "touches no Pathway B
   election" limb is **unsatisfiable** — which is §7 item 13. The arithmetic that justifies a ceiling
   at all, restated on the drafted definition: with no ceiling the appropriation funds **18.1**
   elections; at $100,000 it funds **30.0**.
5. **The dates are the draft's, not the model's, and MOO-45 §4 has re-labelled the table.**
   Effective July 1, 2029; expiry July 1, 2033. VRS's implementation year is **FY2029**, election
   years are **FY2030–FY2033**, and the first year carrying amortised liability is **FY2031**. Every
   dollar magnitude carries; only the labels move. One structural point is not a re-label: the
   systems charge now lands in a year with no program activity, so **the bill costs $375,000 of
   nongeneral fund and nothing else for its first two fiscal years** — a better fact for a money
   committee, not a worse one. July 1, 2029 is a fiscal-year boundary, so no program year is split.
   MOO-45 §4.3 records that chart `09_fiscal_year_stack.png` still carries FY2028–FY2031 and **must
   not leave the team** until it is replaced.
6. **Four inputs the statement will demand.** VRS will need a nongeneral fund implementation line and
   the draft does not appropriate one (MOO-31 assumed $375,000; the Virginia record on comparable
   bills runs about $78,000 for HB 1867 (2023) to $175,000 for HB 687/SB 622 (2024), with roughly
   $36,000 a year ongoing on HB 1306 (2026)); expect "Budget Amendment Necessary: Yes" regardless.
   VRS's own actuarial-equivalent quotes for the affected profiles, which the standard-cost ceiling
   makes operationally necessary rather than merely prudent. VRS's § 415(n) read on the employer
   payment. And VRS's administrative construction of § 51.1-155 A 2 — which Enactment 5 (iii) now
   puts on the record a year before the reenactment vote. The middle two are MOO-37's 12 November
   2026 Benefits & Actuarial Committee ask.

7. **The retirement window is the dominant cost dial, and the statement has to carry the numeral,
   not the concept.** MOO-46 item 4 records that the 0-month setting revision 2 drafted moves the
   repaired cost from $3.65M to **$5.20M — 101 percent of repaired S1** — without changing the price
   by a dollar, and that the repaired sensitivity puts a **55 percent swing** on the deadline length.
   Three consequences for the statement. First, **no figure in it is meaningful until the bracket in
   "final qualifying retirement date" is filled**; the aggregate $3,000,000, the per-member ceiling,
   MOO-45 §3.3's FY2031 exhaustion and 58 percent denial rate, and the 28-to-57-election reach range
   are all 0-month numbers. Second, the direction of travel is the opposite of the intuition: a
   **longer** window is **cheaper** per election, because the member commences later and the
   acceleration the Commonwealth is buying shrinks — so a longer window buys *more* veterans with the
   same appropriation. Third, revision 3's settlement redetermination in G 1 is what lets the
   statement say that honestly: the Commonwealth reserves on the dearest assumption and pays on the
   fact, so a long window does not have to be scored as though every member retires on day one.
8. **Neither benefit tier is costless, and the draft now says both are in.** MOO-46 item 6 withdraws
   MOO-7 §5 — Plan 2 is about 7 percent of participants and reaches eligibility by the Rule of 90
   under **§ 51.1-153 B 3**, not by a 30-year gate — and directs that **no document may imply any
   tier is costless.** `[Citation corrected in revision 8 per `
   `[MOO-65](/MOO/issues/MOO-65) F-3; `
   `[@Fiscal & Impact Modeler](agent://428b53bf-f49e-4505-a607-3560a26b3d50) to note. No figure`
   ` moves and no re-run is required.]` Revisions 1 through 7 pinned this to § 51.1-155 **A 3**,
   which is the wrong section and matters because the revision 7 negative limb excludes an allowance
   *"reduced under subdivision A 2 or A 3."* **Rule-of-90 eligibility and the unreduced allowance
   come from § 51.1-153 B 3, which routes the benefit to subdivision A 1**; § 51.1-155 A 3 is the
   *reduction* provision, in which the rule of 90 appears only as the benchmark the reduction is
   measured to. Read as it stood, a fiscal-note analyst would have concluded that the bill excludes
   the entire Plan 2 segment. **It does not, and no figure in this section was ever computed that
   way.** The bill's own evidence that the two differ in cost is already in the text:
   B 4 a states two published normal cost rates, 12.50 percent and 10.74 percent, and the lower rate
   means a **lower member price and therefore a larger certified subsidy** for a Plan 2 purchaser of
   the same service. The statement must not describe Plan 2 inclusion as a rounding item. One
   drafting consequence worth noting for the actuary: the conforming amendment to § 51.1-155 A 2
   does no work for a Plan 2 member, because A 3 — which governs them — already says "creditable
   service" throughout. The fix is Plan-1-specific; the eligibility is not.

**Two sentences that belong in the statement rather than being discovered by a hostile witness —
and in revision 9 one of them has no authorised figure behind it.** First: **the cap can ration, and
the statement must describe it as one.** Subsections D 4 and D 5 build a wait-list and a notice
procedure; a document that denies the cap rations is denying machinery the bill carefully builds. But
**no exhaustion year, no denial percentage and no funded-election count is authorised** — the Director
has held the cap-sufficiency claim, and the arithmetic is queried at
[MOO-71](/MOO/issues/MOO-71). `[Revision 9 correction: this paragraph previously stated "exhausted in
FY2030, denies 72.7 percent, 18.1 elections funded, 30.0 at the ceiling" as current. Those are MOO-53
figures, superseded by `[MOO-48](/MOO/issues/MOO-48)` and now held. They are removed rather than
restated.]` Second: **the program reaches a few dozen members at most**, and the statement should say
so in those terms. `[Revision 9 correction: the "508-member pilot pool" figure this sentence carried is
withdrawn and appears nowhere in this document.]` One further point the ceiling now forces into the
statement: **D 2 refuses an election above $170,000 rather than trimming it**, so the ceiling's fiscal
effect is the whole certified subsidy of each refused member and not the excess — every trim-basis
figure in the record is the wrong quantity for this text (§0.0000000c).

**Three further things the § 30-19.1:7 statement must carry, all from
[MOO-53](/MOO/issues/MOO-53), and the first is the one most likely to be got wrong.**

1. **The redraft did not reduce the certified subsidy. It more than doubled it.** Aggregate certified
   subsidy on the drafted definition is **$10,996,295**, mean **$111,211** per member — against
   **$4,930,054** and **$49,860** on the published MOO-7 judgment basis, **+123 percent**. Removing
   revision 1's double count lowered the number by $2,374,550; pinning clause (ii) to VRS's own
   retirement decrements raised it by $6,063,425. The drafted figure is **1.48×** the revision-1
   double-counted figure it replaces. **No document in this package may describe the redraft as
   having reduced the subsidy.** The counterfactual retirement age moves from 63.58 to **66.83**, and
   the effect lands hardest on the Pathway-B-type profile, whose charged acceleration rises from 0.37
   years to 4.27.
2. **The selection point, which is the only honest answer to the hostile sentence.** Mean certified
   subsidy is **1.87× the full current-law price** of the credit the member is buying, and that is
   the number a hostile fiscal statement will quote. The answer is that a retirement decrement is a
   **population** rate applied by clause (ii) to a **self-selected** subgroup: on VRS's own first-year
   rates, **13.8 of 98.9 members — 14 percent of the cohort — would have retired within a year of the
   election anyway**, and the act certifies a full acceleration subsidy for each of them. So **the
   drafted definition overstates true economic cost.** The direction matters differently in two
   places: for the **$3,000,000 cap** it is conservative and safe, because the Board meters more per
   election and admits fewer, so the appropriation cannot be overrun; but **anyone who quotes
   $111,211 as "the cost of serving one veteran" is quoting too high a number**, and the statement
   should say so rather than let a committee find it. No adjustment is made in the model and none can
   be made under the statute as drafted: clause (ii) tells the Board to use the decrements, full stop.
3. **The negative-subsidy cell is gone, and the floor binds on nobody.** MOO-31 §2.4's crossover
   warning and MOO-45 §2.3's −$726 cell do not appear inside the modelled cohort, because subdivision
   B 4 b's **lesser-of** forecloses them — the member pays the lesser of the formula price and standard
   cost, so the price discount cannot go negative. It binds on 2 cells, 4.9 members, worth +$2,816.
   Separately, on the drafted definition the statutory **floor** is the operative amount for **0 of
   98.9 members**: certified subsidy exceeds standard cost less payments on every cell. The floor is
   doing no work against the definition as drafted, and that is exactly why it is kept — it is the
   backstop against a reading-down of clause (ii), where it more than doubles the metered amount. One
   caveat to state: every modelled member is outside the 24-month election window, so standard cost is
   the dearer § 51.1-142.2 B 3 price for all of them, and the floor as reported is an **upper** bound
   on how often it binds.

**And one thing the statement must say about the contingency, because the two are a matched pair.**
Revision 5 charges the `[20]` percent contingency against the $3,000,000 (D 2, D 3). On a 25 percent
contingency the alternative — leaving it outside — requires an appropriation of **$3,750,000**; inside,
the elections funded dearest-first fall from 18.1 to **14.0**. Both are priced
([MOO-53](/MOO/issues/MOO-53) §7.1) and the choice is §7 item 15. The contingency percentage itself is a
**lower bound**: MOO-53 could not price the discount-rate channel, and the discount rate is the
second-largest driver in the whole model (±50bp = 31 percent of base).

**Finally, the sensitivity the statement should lead with, because it is not the thing anyone has been
arguing about.** Three drivers move aggregate certified subsidy by more than 25 percent, and **none of
them is the counterfactual**: take-up at 2× central (+100 percent), take-up at the high level (+74
percent), and removing the retire-immediately guardrail (−34 percent). A ±10 percent move in the
retirement decrements is worth only +10.2 / −7.7 percent. Two consequences. The honest uncertainty in
this bill is **take-up**, as MOO-31 and MOO-45 both said. And **the redrafted definition and subsection
F are a matched pair** — the definition is only large because the guardrail forces immediate
retirement, and the guardrail is only defensible because the definition prices what it causes.
**Neither may be changed without repricing the other.**

**Do not characterise this bill as fiscally neutral, as contribution recovery without subsidy, or as
producing workforce savings.** MOO-35 R2 is unambiguous that the "not a subsidy" premise fails: the
draft's own § 51.1-142.4 A concedes a subsidy exists by defining, certifying, reserving and capping
it. That concession is the draft's strongest feature in a money committee, not its weakness. MOO-44
§9 item 15 asks that this instruction go into the Editor's style sheet verbatim; it should.

One further sentence for the statement, on the interest choice, from MOO-45 §3.4: **the bill's
choice to start the interest clock at the end of the 36-month averaging period rather than at entry
is worth 19.1 percent of the member price and about $1,050,740 of Commonwealth cost on the design as
drafted.** The Commonwealth pays more because of that choice. It is defensible — charging interest
on a compensation average that has not yet been earned is hard to explain to a member — but it is a
priced choice and it should be on the record.

---

**Revision 7 adds one sentence to this section and moves no figure in it.** The admitted cohort is
defined by a **normal-retirement allowance under subdivision A 1 of § 51.1-155 that is not reduced
under subdivision A 2 or A 3**, so neither the reduced routes (§ 51.1-153 B 1 and § 51.1-153 D) nor
the 50/10 computation under § 51.1-155 A 5 can admit a member or settle a subsidy. That is the
**unreduced subdivision A 1 cohort — reached through § 51.1-153 A, B 2 or B 3 —** that every figure in
this section is priced on, so **no number in §3, in MOO-31 `model-s8-s9`, or in the MOO-53 reprice
needs re-running because of revision 7 or revision 8.** [MOO-65](/MOO/issues/MOO-65) §5 tested that
conclusion independently, by enumerating every route to a § 51.1-153 service retirement allowance and
comparing the admitted set to the priced population in item 8 above, and reached the same answer. If
the fiscal statement needs a sentence on the point, that is the sentence — it is the Director's own
formulation on [MOO-62](/MOO/issues/MOO-62), and it is worth carrying because a reader who sees two
limbs where revision 6 had one will otherwise ask what the second limb cost.

**Revision 12 moves no figure in this section either, but it adds two determinations the statement has
to price and one it has to stop assuming.** Neither is a change in the design; both are the cost of
provisions that close defects.

1. **Settlement on death, disability and Board error is now a determination, not a silence.** G 4
   settles the certified subsidy on the earliest of death, the commencement of a disability allowance,
   and the member's actual retirement, and runs the same lesser-of redetermination G 1 runs. So the
   statement must price **a second actuarial determination in those cases too**, and — the part that
   matters for the Commonwealth's side of the ledger — it must stop treating those cases as costing
   the appropriation nothing. **Before revision 12 they cost the appropriation nothing and cost the
   trust the whole subsidy**, which is not a saving; it is a misallocation that the fiscal statement
   would have reported as a saving. The expected frequency is small — the mortality and disability
   decrements over a window of `[12]` months on a cohort at or near unreduced eligibility — and the
   Fiscal & Impact Modeler should state it rather than leave it at "small."
2. **The § 415 deferral in B 4 f can push a completion date, and therefore a valuation date, into a
   later limitation year.** That changes the interest run in B 4 b and the anticipated earliest
   qualifying retirement date in the certified-subsidy definition, both of which are recertified under
   D 6. It does not change any price in the model; it changes which fiscal year an election lands in.
   The statement should say that the fiscal-year distribution of elections is **not** fully determined
   by the acceptance date.
3. **One assumption to drop.** Any statement that every accepted election either settles on a
   retirement inside the window or is re-valued under G 2 is now wrong — G 4 is a third outcome with
   its own settlement. The §30-19.1:7 statement's outcome tree needs the third branch.
4. **ADDED IN STORE REVISION 34 — two things the statement must carry about the bill's only quantity,
   and one of them is a correction against this file.** (a) The clause (ii) **rounding** rule raises the
   mean certified quantity by **+0.89 months** against the published 19.89 and moves cap utilisation by
   **−0.08 percentage points**, 79.32 → 79.24, because the marginal month of clause (ii) credit is close
   to **subsidy-neutral**: the member pays the total-normal-cost price for it under B 4 b and it buys no
   further acceleration. It must **not** be described using the 0.46-against-0.93 spread, which is a
   tolerance band and not a rounding basis — see §0.x c. (b) The clause (ii) **base** repair, §7 item
   43, lowers quantity for members holding non-membership creditable service and is **unmeasured**,
   because the engine runs with `prior = 0.0`. Both are one-sided omissions with a known direction,
   which is what § 30-19.1:7 asks the statement to disclose.

---

---

## Moved in store revision 45 — §8 status notes for store revisions 39, 38, 37, 36 and 34

**Moved verbatim** out of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) when store
revision 45 was written, because that revision arrived with 15,624 characters of headroom
and its record did not fit. Every figure, label, table row and caveat is preserved; each section is
replaced in the bill document by a stub restating its durable results. **Nothing was rewritten or
summarised away.** Read it as a dated record: it states what was true of the bill at the revision it
names, and nothing in it governs the current text, which is §1 of the bill document.

*Relabelled.* This block was appended while the bill document still stood at store revision 43 and was
first headed *"store revision 44"*. **Store revision 44 is a real and different revision** — the Policy
Director's MOO-101 answers — which landed from a concurrent run while this revision's body was in
flight, so this revision was re-cut from scratch against it and became **45**. The move itself is
unchanged; only the numeral was wrong.

> **STORE REVISION 39 — [MOO-117](/MOO/issues/MOO-117)'s PASS 12 DRAFTED OUT. Seventeen edits in twelve
> provisions. 26 findings: 0 fatal, 8 serious, 13 moderate, 5 minor, plus 20 express null results.
> 18 drafted out, 1 no change needed, 7 with the Director at §7 items 62 to 69. No figure moved, no
> section added or deleted, no designator renumbered, and the bill title unchanged.**
>
> **Full record: [`pass12-disposition`](/MOO/issues/MOO-42#document-pass12-disposition)** — the
> finding-by-finding table, all seventeen edits verbatim, the two departures from pass 12's own fix
> direction, the F-24 no-change reasoning and the cross-reference sweep. §0.x, §5.21 and §6.0-39 above
> are the pointers.
>
> **The three that cost a real person real money, all closed.** G 4's clock ran from *"the earliest of"*
> three dates and therefore stripped the purchased credit of **every** member separated more than three
> months before her window closed, while subsection F still permitted her to retire (**F-1**). The
> deeming rule deemed the **retirement** and not the **date**, so subsection F was breached on its face
> and **D 7 commanded release of the reservation at the same moment G 1 commanded settlement** (**F-2**,
> which also carried **F-3** and **F-9**). And B 4 a asserted that the § 415 limitation year *"means the
> calendar year"*, which 26 C.F.R. § 1.415(j)-1(a) makes a **default only** — a plan-qualification
> exposure, not a drafting embarrassment (**F-8**).
>
> **Two consequences outside the text.** **[MOO-115](/MOO/issues/MOO-115) stops being load-bearing for
> the bill**: the limitation year is now defined by reference to the plan, so the answer no longer changes
> a word. And **§7 item 57's candidate designation should not now be adopted** — it asserts the same
> plan-document fact at subdivision level. Item 57 is annotated.
>
> **Not publishable, and the reasons have changed.** Pass 12 is explicit that nothing in store revision
> 36 is fatal and that the architecture survives, and **F-1, F-6 and F-8 — three of the four items pass
> 12 named for the memo's risk section — are now closed in the text and must not be carried as live
> defects.** What stands in the way of publication is unchanged in kind: **none of these seventeen edits
> has been attacked by anyone**; the Director's list is now nineteen open items; and no money figure may
> be published until [MOO-71](/MOO/issues/MOO-71) closes.
>
> **One thing I am not doing in this revision.** I am **not** restating the assurance that the retirement
> window's components are each bounded on the face of the text. I have had to withdraw it twice and
> §6.0-39 item 1 gives the component list as a statement of the text instead, with the one unbounded
> residual named at §7 item 68 rather than cured by a numeral nobody chose.
>
> **One caveat that travels with F-8.** eCFR redirected, so pass 12 read 26 C.F.R. § 1.415(j)-1 at
> Cornell LII. That mirror is the whole ground of the edit. I have not re-opened it and I am not
> representing that I have; the fix is drafted so that the answer cannot change the text either way.
>
> **Housekeeping, taken rather than asked.** This file had **10,211** characters of headroom on arrival,
> which is less than a record of this size costs. **§5.16, §6.0-24, §6.0-25, §6.1a and §6.2a are moved
> verbatim** to [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history),
> every lettered label, check number and table row preserved, each replaced by a stub restating its
> durable results. **Nothing was rewritten and nothing was summarised away.** Same decision and same
> reason as the moves in store revisions 23, 24, 30, 32, 33, 34, 35, 37 and 38 — §7 item 53.


> **STORE REVISION 38 — §7 ITEM 35 OPTION (b) ENACTED. Subsection C's zero bar and its refusal notice
> are deleted, MOO-32's measurement is annotated at the item, and §7 item 26 closes with it. One
> deletion, no figure moved, no designator renumbered, no section added.**
>
> **This discharges a standing obligation, it does not answer a review.** [MOO-87](/MOO/issues/MOO-87)
> undertook at 03:11 on 12 October 2026 to enact option (b) in the revision that drafted out pass 11.
> **Store revision 36 drafted out pass 11 and did not carry the enactment**, so it is carried here, and
> the annotation's own statement that it would be enacted in that revision is corrected rather than
> left standing (§6.0-38 item 2).
>
> **Why the bar went.** Clause (ii) is measured at the filing date and clause (v) of *"eligible
> member"* tests the same fact on the same date, so for every person subsection C addresses clause
> (ii) is greater than zero: the bar could not fire and its own notice duty could not be triggered.
> **The ground is containment, which holds on any population** — not MOO-32's measurement, which
> refuses **0.0000 of 19.6304** on the authorised cohort and corroborates the choice without founding
> it. **The participant count is identical on all three options of item 35.**
>
> **Whose call it was.** Store revision 30 opened item 35 as the Policy Director's. The Director routed
> MOO-32's measurement back with *"the call is yours"*, and I took option (b) on that routing. **One
> word from the Director reverses it**: the two sentences go back and §7 item 26 re-opens.
>
> **Still not publishable, and this revision adds a reason.** The deletion has had **no counsel pass of
> its own** — [MOO-119](/MOO/issues/MOO-119) is the bounded pass for it, and it must re-run §5.20's
> five checks against the deletion as landed, not as proposed. Store revision 36's eleven edits are
> still before [MOO-117](/MOO/issues/MOO-117) (pass 12), and **store revision 37's two cures have had
> no pass of their own either**. This revision does not touch either set: pass 12's
> bounded scope is subsection M's tolling, the 90-day limb, G 2's allowance bar, B 4 g, the three-day
> mailing allowance, the over-cap reinstatement and enactment 3, and **subsection C's zero bar is in
> none of them**. §7 items 31 to 58 remain open apart from 26, which closes here. Citation check
> **§5.20**; ambiguities **§6.0-38**; the record is **§0.x** above.

> **STORE REVISION 37 — [MOO-104](/MOO/issues/MOO-104)'s counsel review of the clause drafted but never applied is answered, and the clause is withdrawn.** **15 findings: 1 fatal, 5 serious, 6 moderate,
> 3 minor**, plus nine null results. **The fatal finding is against the cure and not against the live
> text**, so the cure is gone and **162 characters** are enacted in its place, both inside subdivision
> G 4: § 51.1-153's requirements a member cannot satisfy *"by reason of his death"* are disapplied for
> the existing *"as though"* hypothetical (MOO-96's F-7, with S10-F9's five words), and
> *"Notwithstanding the preceding sentence"* is re-anchored to *"the crediting required by"* it
> (S10-F12). **No figure moves**, no deeming is created, no section joins the act, the title does not
> change, and `12`, `$3,000,000`, `$170,000` and `[20]` percent are untouched.
>
> **Why the drafted clause is not here.** It deemed the member to have retired *"for the purposes of
> this section"* while sending the payment duty out to *"this chapter"* — and §§ 51.1-162, 51.1-163 and
> 51.1-165 are not in this section. It would also have satisfied **subdivision G 1**, switching off
> G 4's own settlement machinery by its own terms, and its calculation limb reached the survivor's
> benefit but not the **certified subsidy**. **Keeping the sentence and adding one disapplication avoids
> all three, which is why I did not take the three repairs the review offered me.**
>
> **Three things are open and none of them is drafting.** **Item 59** — the partial-lump-sum tier notice,
> re-cut on S10-F4, F5, F6 and F7 and with one of its own premises corrected as a **citation failure**
> (§ 51.1-165.01 B 1 clause (i) is a disjunction; the 2x and 3x tiers are unreachable for the modelled
> **B 2** cohort only). **Item 60** — the death case, with **both of the review's premises corrected**:
> the survivor half reaches a narrower class than stated, and the fiscal half runs through the
> *"certified subsidy"* **floor** rather than through the deeming, which means option (b) does nothing
> unless it disapplies the floor expressly. Three answers drafted, none enacted, and a third one of
> mine. **Item 61** — three answers to items already on the card: the 120-day tolling cap **confirmed**
> (do not reopen), item 39 given a third alternative by a second reviewer who insists on an absolute
> bound, and item 34 item 2's M 2 amendment widened to carry **two** missing classes in one sentence.
>
> **Still not publishable, and the reason has changed.** Store revision 33's 24 edits have had no
> adversarial pass, and this revision's two have had none either. **What is new is that the one fatal
> finding on the bill is now a live policy question with a priced per-event cost**
> ([MOO-105](/MOO/issues/MOO-105): **$106,253** of certified subsidy per event for a credit worth $0) and
> that **four findings must appear in the memo's risk section** — S10-F1, S10-F4, S10-F8 and the
> § 51.1-162 non-citation, which §7 item 60 alone does not discharge. Record:
> [`moo104-disposition`](/MOO/issues/MOO-97#document-moo104-disposition).

> **STORE REVISION 36 — [MOO-106](/MOO/issues/MOO-106)'s pass 11 drafted out. Eleven edits in ten
> provisions, no figure moved, and one definition paragraph deleted.** Pass 11 is the adversarial and
> counsel review of store revision 33's 24 edits: **19 findings on the enacted text — 0 fatal, 6 serious,
> 9 moderate, 4 minor — plus 3 serious defects in candidate texts not in the bill**, with **seventeen
> express null results** and the headline that **nothing is fatal and the architecture survives**.
> **13 are drafted out, 3 corrected in the record, 2 statements of mine withdrawn, and 4 are the
> Director's at §7 items 55 to 58.**
>
> **The three that change what the bill does.** The **retirement window is bounded for the third time**,
> and this time the bound reaches the limb that was unbounded: §6.0-24's assurance was false a **second**
> time, because the unbounded component is now the **tolling in subsection M** and store revision 33's own
> edit unbounded it — one unanswered reconsideration letter held the window open indefinitely with a
> reservation charged against the $3,000,000 throughout, and the Commonwealth then settled a subsidy for a
> **negative** acceleration. The bound now reaches tolling and M 2's protection survives as a **deeming
> rule**, which is pass 11's own repair for its preferred option and **introduces no new figure**. The
> **involuntarily separated member's 90 days is now 90 days** — it was a ceiling and not a floor, and for a
> member separated in the last quarter of her window it could be **zero**; I took pass 11's alternative
> rather than its first fix, because disapplying the final-date limb would have stranded settlement and put
> the subsidy on the **trust** with no appropriation behind it. And G 2's **allowance bar is keyed to the
> election rather than to the member**, which closes an over-inclusion worth up to $170,000 to the trust and
> an under-inclusion that withheld the whole pension of the member who paid **nothing**.
>
> **Also: B 4 g is deleted** — I created it last revision and 26 C.F.R. § 1.415(j)-1 shows a limitation
> year cannot be designated for a subset of a plan's participants; **the three-day mailing allowance now
> reaches B 4 f's 30-day § 415 election period and every period of an "applicant"**, which §5.15 wrongly
> said it already did; **the over-cap reinstatement must now request the appropriation it spends**, under
> Va. Const. art. X, § 7; **its notice is split so a wait-listed applicant is not told another member's
> business**, and the reinstatement is reviewable; and **enactment 3 now preserves the member's rights and
> periods past the sunset, not only the Board's verbs**.
>
> **Still not publishable**, and the reasons have changed: the eleven edits have had **no adversarial pass
> of their own** ([MOO-117](/MOO/issues/MOO-117) is pass 12); §7 items 55 to 58 are new and items 31 to 54
> are open; and the **1 July 2030 parker cliff** at §0.x d is a more adverse statement of the cap exposure
> than any published figure, with two lines at [MOO-116](/MOO/issues/MOO-116). Citation check **§5.18**;
> ambiguities **§6.0-36**; the whole record is in
> [`pass11-disposition`](/MOO/issues/MOO-42#document-pass11-disposition).

> **Store revision 35 — the Director's four answers drafted out, with [MOO-99](/MOO/issues/MOO-99)'s pass 10
> (6 serious, 10 moderate, 3 minor) folded into the same words.** §7 items **27 to 30** are closed. **Six
> edits in three provisions** — the § 51.1-155.1 gateway in both definitions, D 1's notice sentence, four new
> sentences in G 4, seven words in G 4's final sentence, and a deadline on the reinstatement — **with nine
> further pass-10 repairs inside the wording of the answers themselves.** **Item 29 needed no edit and
> nothing was re-enacted.** The highest-value repair was one word: *"may be settled"* is now *"is settled"*,
> because the draft would have made the Commonwealth's payment of a named member's subsidy a standardless
> Board discretion. **Two findings needed no edit because store revision 33 had already cured them**, which I
> verified rather than assumed. Two new citations (**§ 51.1-155.1 A and C**, **§ 51.1-156 A and H**) are
> checked in **§5.17**; ambiguities at **§6.0-35**; **the whole record is in
> [`moo64-record`](/MOO/issues/MOO-42#document-moo64-record)**. **No figure moves on the actual-facts reading
> of the gateway**, and **item 48 is the one open question that could move one**. **Items 45 to 54 are with
> the Director**, with candidate text for every one and none of it in the bill. **Still not publishable:**
> these six edits have had no adversarial pass of their own; §7 item 22's drafting is
> [MOO-87](/MOO/issues/MOO-87); and items 31 to 54 are open.

> **STORE REVISION 34 — [MOO-103](/MOO/issues/MOO-103)'s pass 10 drafted out. Four edits, no numeral
> moved, and the bill's only quantity provision was measuring against the wrong defined term.**
> This is the bounded counsel review of store revision 32's three edits. **12 findings: 0 fatal, 2
> serious, 5 moderate, 5 minor**, and its headline is that **all three of those edits stand** — none
> breaks a cross-reference, strands a designator, moves a numeral or reaches a provision it should
> not — with **no serious constitutional problem** found in them. **4 are closed in the text, 6 are
> corrected in the record, 2 are the Director's, and one reviewer routing I did not follow.**
>
> **The finding of the pass is against me.** Clause (ii) of subsection C asked for the months of
> **creditable service** the member needs and then measured that need against her **membership
> service** — two different defined terms, with the narrower one as the base, so the need was
> overstated by every month of credit she **bought** or was **granted**. On the reviewer's facts a
> member aged 57 with 26 years of service plus 4 years purchased under B 1 (iv) needed 36 months and
> clause (ii) returned 84, so she could buy **48 months of subsidised credit against a need of 36**
> and nothing in clauses (vi) to (viii) screened it. **The words were mine, from store revision 22's
> option (c) drafting, and nobody chose them.** The base is now *"all creditable service for which the
> member is entitled to credit as of that date."* I enacted the repair although the reviewer routed it
> to the Director, because the base was never agreed, because the agreed minimum-necessary rule needs
> the base that produces the date, and because the direction of effect is **downward** on cost — and
> **the reversal is one phrase, drafted in §7 item 43.**
>
> **Also in the text:** the rounding rule now names its referent; the clause (vii) month convention
> leaves the clause, becomes its own sentence, is re-expressed as a **date** rule rather than a period
> rule, and its month-end fallback is made **symmetric**, because as enacted it refused a **thirty-day**
> advance and admitted a **twenty-eight-day** one; and subdivision D 6's trigger reaches a **corrected**
> record, which restores work to a cancellation-and-refund sentence option (c) had made a dead letter.
>
> **Two figure statements, one of them a correction against this file.** The clause (ii) rounding is
> **+0.89 months** per member against the published 19.89 and **−0.08 points** of cap utilisation, and
> it must **not** be described using the 0.46-against-0.93 spread, which is a tolerance band and not a
> rounding basis. The base repair is **unmeasured** in every run to date, because the engine holds
> `prior = 0.0`. Both are in §3 and in item 43's note to Fiscal.
>
> `12`, `$3,000,000`, `$170,000` and `[20]` percent are untouched; no section is added; no designator
> is renumbered; the title does not change. Full disposition:
> [`pass10-disposition`](/MOO/issues/MOO-87#document-pass10-disposition) on
> [MOO-87](/MOO/issues/MOO-87).

---

## Moved in store revision 46 — §6.0-39, §6.0-40 and §0.1

**Moved verbatim from [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) in store revision 46**, which drafts out [MOO-123](/MOO/issues/MOO-123)'s pass 14. That file had 17,740 characters of headroom on arrival and the revision's in-file footprint is about 11,400, so three sections moved and each is stubbed in place with its durable results. **Every numbered item, check number and table row is preserved and nothing was summarised away.** References of the form **§6.0-39**, **§6.0-40** and **§0.1** resolve here. The full record of store revision 46 is [`moo123-pass14-disposition`](/MOO/issues/MOO-87#document-moo123-pass14-disposition).

---

### 6.0-39 Ambiguities resolved in store revision 39

1. **The one choice in this revision that is mine and that nobody asked for: the 12 months in F-2's
   date-setter.** Making the deeming rule move the date is pass 12's own device and is not a choice. But a
   date keyed to *"the month in which the Board last acts"* is unbounded in the Board's own default, and
   **M 2's 90-day duty to act has no consequence** — §7 item 33's candidate, which would have given it
   one, is withdrawn. I have had to withdraw the assurance that this definition's components are each
   bounded on the face of the text **twice**, in store revisions 33 and 36, and both times the cause was a
   limb running on a Board act with no cap. So the limb is capped at **12 months beyond the outer bound**,
   which covers pass 12's own ten-month over-run scenario with margin. **The numeral is mine.** I used 12
   because it is already the window's length and introduces no figure the Code does not carry; a tighter
   number is available and is a one-word edit. **I am not restating the bounded-components assurance in
   this revision.** What I will say is the component list, as a statement of the text and not as a
   warranty: 12 months, plus up to three months of approved later date, plus day-for-day Board lateness
   under D 1 and tolling under subsection M, both capped by the outer bound at 12 months beyond the
   first-sentence date, plus at most a further 12 months on the tolling limb where the Board over-runs its
   own 90 days — **and the floor, which is keyed to a Board act and is the one component with no figure
   bounding it. That residual is §7 item 68 and it is stated rather than cured.**
2. **F-18: who is "unable to retire … by reason of an error of the Board."** Pass 12's cure extended the
   window; mine puts the member inside G 4 clause (iii) instead. The ambiguity I had to resolve is
   **which member** — the clause is drafted to reach a member who **retires at a time when the statement
   has not been given**, and so reaches the never-told member and not the member whose statement was
   merely late. The late-statement member has the floor. The reason for the line is that a window
   extension costs cap occupancy and can be engineered against the Board's own lateness, whereas vesting
   on retirement cannot be engineered by the member at all: she cannot cause the Board not to give the
   statement. **The cost of the line is that it is a bright one** — a statement given one day before she
   retires takes her out of the clause and leaves her with the floor.
3. **F-22: "more than one involuntary separation" rather than an aggregate of months.** Both close the
   ratchet. I took the count rather than a months cap because a months cap needs a numeral and the count
   needs none, and because the second separation leaves the member the 90-day vesting branch within her
   already-extended window. **The cost is visible: a member genuinely RIF'd twice gets the extension
   once.** That is a real, if rare, hard edge and it is stated rather than buried.
4. **F-6: "the agency head or his designee" rather than a human resources officer.** Pass 12 proposed
   certification by *"the agency's human resources officer."* No such office is named in Title 51.1 or in
   § 2.2-3200 et seq. and agency practice varies, so the certification is keyed to the formula the Code
   already uses throughout for an agency act. **I also declined pass 12's own warning case** and did not
   key the trigger to eligibility for a transitional severance benefit under § 2.2-3202, which would have
   excluded the legislative- and judicial-branch members this bill deliberately covers.
5. **F-25: by reference, not by figure.** Pass 12's fix quoted *"$3,000,000"* from D 2. The definition is
   keyed to *"the limitation in the first sentence of subdivision D 2"* instead, so **the figure appears
   once in the Code and a future amendment to it cannot leave the stop-and-resume rule behind.**
6. **F-7's reinstatement, which pass 12 did not ask for.** Its fix rescinded the determination and
   restored the credit and stopped there. Chasing it through: after rescission the member retires in a
   qualifying retirement, so the subsidy settles under **G 1** and not under G 4 — and G 4's existing
   reinstatement sentence is timed to *"the date on which the certified subsidy is settled under this
   subdivision."* So the reservation G 2 had released would never have been reinstated and subsection N
   would have paid against nothing. The new sentence invokes the existing machinery expressly, including
   its over-cap charge and its notices, and times it to the rescission.

---

### 6.0-40 Ambiguities resolved in store revision 40

Nine in full at [`moo118-disposition`](/MOO/issues/MOO-97#document-moo118-disposition) §6; the five that decided text are here.

1. **Enumerate, or keep the bare criterion?** **Enumerate, with the criterion kept behind it.** §6.0-37
   item 5 chose the bare criterion for brevity; **F5** shows it cannot reach both of its own stated
   targets. An enumeration in front of a residual is the standard form and costs 280 characters. **The
   residual is not narrowed**, so nothing it reached is surrendered, and *expressio unius* is weak against
   a residual that is express and general.
2. **Name the section, not the gateway; write the effective-date limb to the substance, not the sources.**
   The in-service and notification requirements appear in **five** places in § 51.1-153, so *"any
   requirement of § 51.1-153"* reaches all five and is shorter than the reviewer's *"subsection A"*; and
   one limb written to the substance of the effective-date requirement reaches § 51.1-153 E **and**
   subdivision D 1's restated proviso, answering **F4** and **F5** together.
3. **F7 declined.** *"Notwithstanding the crediting required by the preceding sentence"* attaches the
   conflict-resolver to a **duty** rather than a provision, which is not the chapter's idiom, and the
   reviewer concedes it **changes no outcome on the better reading**. The offered cure restates the
   displacement in substantive words — and the scope of that displacement is exactly what **F2** puts to the
   Director at item 60. **Re-cutting the sentence now and again when item 60 is answered is two changes
   where one will do.** Recorded open, not closed.
4. **F8 declined.** Nothing requires the Board to state which requirements it treated as disapplied. That
   is a **new duty on the Board** and was not agreed; the reviewer expressly does not rate it an
   invalidity risk, and item 1's enumeration is most of the answer. Noted for the Director: G 4's written
   notice duty sits in the **partial-payment** branch only, so a full-payment death carries **no** notice
   duty at all — that is the sentence to extend if F8 is to be answered.
5. **F1, F2 and F3 not drafted in, and that is a choice with a reason.** Each fix direction **states a
   measure** for the survivor's benefit, and every available measure takes money from someone: the
   survivor, the trust, the General Fund or the employing agency. [MOO-104](/MOO/issues/MOO-104)'s fatal
   finding was that a cure which made the death case **worse** than the text it replaced is worse than no
   cure — and enacting **half** of **F2** does exactly that, because naming the service base alone, or
   importing subdivision G 3's guard alone, settles the partial-payment death on the reading that makes the
   premise unconstructible in **100 percent** of those cases. **F2 goes whole**, as item 60's **(e)**;
   F1's answer as **(d)**.

---

---

## 0.1 Retained §0 narrative — one pointer for revisions 2 through 33

**Every §0 record for revisions 2 through 33 is in
[`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history), verbatim and
with every lettered subsection label preserved**, so a `§0.0000000000000000000000c`-style reference still
resolves there; each also survives verbatim in the store revisions of this document that still held it.
**Store revision 35 moved store revision 33's record out and replaced ten separate pointer stubs with this
one table**, because the record and the stubs together had reached about 34,000 characters of a file that
is at the platform's ceiling, and the alternative was being unable to enact the Director's answers at all.
**The stubs are in the history document too** — nothing was summarised away and nothing was rewritten.
**The remaining question, which is the Director's, is §7 item 53.**

| Record | The durable result this file still relies on, and where it lives here |
|---|---|
| **Store revision 33** | [MOO-95](/MOO/issues/MOO-95)'s pass 9 — 29 findings, 0 fatal — in **24 edits**. The retirement window now has an **outer bound**: a final qualifying retirement date as extended under D 1 is *"in no event later than 12 months after the date determined under the first two sentences"* of its definition, and **the numeral is the drafter's, which is card item 39**. G 2 gained the term ***"the determination date"***, with a referent in the involuntary-separation branch as well, and a **60-day deadline for the notice**. G 2's allowance bar no longer reaches a member whose election the **Board itself cancelled**. G 4's **over-cap reinstatement carries four safeguards** — notice to the money-committee Chairmen and to each waiting-list applicant within 15 days, the amount and cause of the excess, a J-report line, and no further election until the excess is eliminated. And **enactment 3 no longer lets the pilot's price expire out from under a member mid-contract.** Citation check **§5.15**; card items **39 to 42** |
| **Store revision 32** | Pass 9's three edits on the option (c) drafting — clause (ii) rounding, the clause (vii) month convention, the filing date in D 1. Citation check **§5.14**; card items **36 to 38** |
| **Store revision 30** | The [MOO-84](/MOO/issues/MOO-84) review in four edits: subsection C's 30-day determination deadline, the zero-refusal notice triggering on the fact and pricing limb (a) alone, and — most consequential — **option (c) has made subsection C's zero bar unreachable**. Ambiguities **§6.0-25**; card items **34 and 35** |
| **Store revision 24** | Pass 7, pass 8 and [MOO-85](/MOO/issues/MOO-85) in 37 edits: **G 2's trigger reads *"final qualifying retirement date, if any"*** and no determination is required of a member credited under G 3 or G 5; the **60-day/120-day** effect deadlines; **$170,000 stands** on the 12-month rung. Ambiguities **§6.0-24** |
| **Revisions 23, 22, 21, 20, 18** | The 12-month window, the removal of § 51.1-155 from the bill, the Article 2 deletion, pass 5's and the S6 review's drafting, and [MOO-79](/MOO/issues/MOO-79)'s four residuals. Citation checks **§5.9 to §5.11a**; ambiguities **§6.0-18 to §6.0-22** |
| **Revisions 17 and 16** | Clause (vi) bounded by what the member can actually buy; the application-date leg; **the rule that the revision number is the store's**. Citation checks **§5.7 and §5.8** |
| **Revisions 12 down to 2** | The money flow closing on death, disability and Board error; the processing extension's standard, deadline and review right; **$170,000 and the obligor**; the two-limb eligibility test. Citation checks **§5.1 to §5.6** |

---

# Added in store revision 47 — the §0 narrative for store revisions 43, 44 and 45, the sweeps §5.24 and §5.25, and §6.0-43 and §6.0-45

**Moved on 12 October 2026 from `bill-text-s8`, which arrived at store revision 47 with about 6,400 characters of headroom against the store's 524,288-character ceiling and could not hold pass 15's record.** Every section below is **verbatim**, with every lettered label, numbered item, table row and check number preserved, so a `§0.x`-, `§5.24`- or `§6.0-43`-style reference still resolves. **Nothing was rewritten and nothing was summarised away.** Each is replaced in `bill-text-s8` by a stub restating its durable results.

**Two things in what follows are superseded by store revision 47 and must not be quoted as current.** **§6.0-43 item 2** — the claim that store revision 43's new G 4 settlement sentence "is caught by the two existing bars without amendment" is right about a **first** settlement and **wrong about a second**; that is [MOO-127](/MOO/issues/MOO-127)'s pass-15 finding S-1 and it is barred in store revision 47. **§6.0-43 item 7 and the corresponding row of §5.24** — the account of the rescission date-setter's 12-month cap as a bound does not hold: the cap had **no referent in the ordinary case**, and store revision 47 made it determinate without making it a bound. See `bill-text-s8` §0.x c, §5.27 and §7 item 85.


## Moved verbatim: §0 narrative — store revision 45

## 0.0000000000000000000000000000000000000 Store revision 45 — §7 item 60 is answered by the Policy Director. Answer (d) is enacted, so the death branch now **names** the benefit it orders paid; [MOO-118](/MOO/issues/MOO-118)'s **F8** is answered with one notice duty; and 972 characters of hypothetical come out

**The record proper is a companion document from the start** — [`moo97-rev45-record`](/MOO/issues/MOO-97#document-moo97-rev45-record) — on the convention store revisions 33, 36, 40 and 41 set. It carries the redline, the full cross-reference sweep, the nine ambiguities, subdivision G 4's death branch **reproduced in full as amended**, the routing table and the Editor's three sentences. What follows is the summary.

**The decision.** The checkbox card on [MOO-97](/MOO/issues/MOO-97) was accepted on 12 October 2026 with **two** of its options: item 60's **(d) — name the measure** — and **F8's notice duty in the full-payment death case**. **(a)** the narrow bridge, **(b)** the settlement cap and **(c)** the employer refund were **not** selected and stay live at item 60. **(e) is closed rather than unselected**, and that is a correction to my own record: (d) subsumes its first half, and its second half is unnecessary because the last sentence of **subsection E** already withholds the unreduced retirement eligibility date from every member who has not paid in full (§6.0-45 item 6).

**The three changes, all inside subdivision G 4 of new § 51.1-142.4.** **One**, the deeming and all four disapplications are **deleted**, 972 characters down to 148: out come *"as though the member had retired in a qualifying retirement on the date of death"*, the three date requirements of *"qualifying retirement"*, store revision 40's enumeration of § 51.1-153, and the residual limb naming § 51.1-153, § 51.1-155.1 and subdivision D 1. **Nothing is surrendered, because nothing is deemed** — G 4 no longer asks whether the member retired, so no requirement of retirement is left to disapply. **Two**, the measure, in the Director's words but for one: <u>"The benefit payable under this subdivision shall be the benefit this chapter provides on the death of a member in service, computed on the service credit credited under this subdivision."</u> It closes [MOO-118](/MOO/issues/MOO-118)'s **F1**, **F2** and **F3** together and **names no section**, so MOO-96's **F-4** is not reopened. **Three**, the notice limb is struck out of the refund sentence — where it sat **inside** the *"adverse federal tax consequence"* clause and so arguably ran only in the tax case — and re-enacted as its own sentence covering **every** death, with the benefit and its computation added to its contents and review under subsection M. The two new sentences are 847 characters.

**What this costs, because the Director bought it and a reader should not have to find it.** (d) measures the benefit on what **this chapter** gives on the death of a member in service. For a member who has filed the notice **subdivision D 1 compels** her to file, § 51.1-165 C 1 provides that *"in all cases"* of death before the effective date but after the Board has the notification, benefits are paid under **§ 51.1-163** — a refund of her own contributions — unless § 51.1-165 C 2's spouse, minor child or parent saves her. **(d) names the measure; it does not displace that routing, and only item 60 (a) does.** So the elected-option class is **still unanswered**, now in words that are settled rather than arguable. That is back with the Director as a fresh card on [MOO-97](/MOO/issues/MOO-97), not buried here.

**No figure moves.** No definition is added, no section joins the act, no designator is renumbered, and the title of the bill does not change. Citation check **§5.25**; ambiguities **§6.0-45**; the two new sentences have had **no counsel pass** and that is [MOO-126](/MOO/issues/MOO-126). **Headroom:** the revision arrived at **15,624** characters; §6.0-39 is moved verbatim to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2), the second retained-record document, because [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history) is itself **936** characters from the ceiling. **§7 item 53 is now a three-document problem.**

## Moved verbatim: §0 narrative — store revision 44

## 0.000000000000000000000000000000000000 Store revision 44 — the Policy Director's MOO-101 answers enacted, together with MOO-98's reassigned findings and MOO-121's counsel review. Seventeen substitutions in nine provisions, subsection C's zero bar and its refusal notice restored verbatim, no figure moved

**Whole record in [`moo101-cut-record`](/MOO/issues/MOO-42#document-moo101-cut-record); this file had no
room for it**, on the convention store revisions 33, 36, 40, 41 and 42 set. That document carries all
seventeen FIND/READ pairs with the anchor each was verified unique against, the finding-by-finding
disposition of MOO-121's **19** findings and MOO-98's **8** reassigned ones, the **three** edits withdrawn
on rebase, the cross-reference sweep in both directions, and the ambiguities resolved. **No §5.x sweep and
no §6.0-x section is added here; both are in that document.**

**Five answers of the Director's are in the operative text.** §7 item 34's five repairs, all five
([MOO-84](/MOO/issues/MOO-84)'s F3, F4 and F8, the F1 clone in D 2, and D 6's cancellation notice); clause
(vii) re-keyed on answer **(B)** so that it tests *"the least of the member's maximum purchasable amount
and the amount specified in clause (ii) of subsection C"* rather than a quantity the member may not buy;
MOO-98's S3 on **variant 1**, a new enactment 3 clause **(v)**; enactment 3 clause (i) gains the word
*"notice"*; and the **parity clock** for D 2's refusal notice. §7 items 34, 35 and 26 are answered and
closed on their faces.

**Subsection C's third and fourth sentences are back, verbatim.** The Director answered the conflict
between MOO-101's *"[d]o not delete subsection C's zero bar in this revision"* and store revision 38's
enactment of §7 item 35 option (b): **(a) governs.** The bar and its refusal notice are restored in their
original position and in the form they had in store revision 37, with store revision 24's standard-cost
limb and store revision 30's fact-keyed trigger and *"30 days after the member's application is
completed"* clock. **Store revision 41's third sentence is undisturbed and the two are complementary** —
the bar fires where the clause (ii) amount **is zero**, revision 41's sentence governs where clause (ii)
**has no value at all**. The restoration is also what gives subdivision D 7's new release limb a referent
(MOO-121's **S2**).

**MOO-98's M1 is enacted in form (B)**, which the same answer selected: subsection C's two 30-day duties
now carry a line in the subsection J report, review of a **failure** at any time until the notice is
given, and the member's own window running from **actual** notice. **Subdivision M 2's gateway is widened
to reach a failure to act**, without which that right would run into a gateway confined to determinations
(MOO-121's **M5**), and M 2's tolling and judicial-review sentences are conformed to the four classes its
first sentence now names (**M4**).

**Three of MOO-121's five serious findings are repairs to words this revision was about to enact, and all
three are taken.** **S1** — re-keying D 2's trigger to the fact stranded the words that state the adverse
action, so the notice now states *"the Board's determination that it may not accept the election"*; it is
the only statutory exit for **1.2339** expected refusals, **6.29 percent** of the live applicant set of
19.6304. **S3** — my narrowing of §7 item 34 item 5 rested on a premise about D 6's third sentence that
fails twice, so both dropped limbs are enacted as the Director directed them. **M3** — the filing-date
retention sentence is enacted without its durational limit, which implied a divestment the bill never
provides for. **M1** and null result 2 — the new clause (v) carries a savings for subdivision B 4 a of
§ 51.1-142.2, so the Board is not left quoting a *"standard cost"* under a definition that expired, and
terminates on withdrawal or death as well as on performance.

**Three edits drafted for this cut were withdrawn on rebase, and one of them was the one I had called the
fiscal event.** The cut was built on store revision 32 and **revisions 33 to 42 landed under it**. MOO-98's
**S1** (clause (ii)'s offset base) was enacted in store revision 33; **M6** closes in fact with it; M5's
refund limb was enacted more widely in store revision 36; and **MOO-98's M2** — clause (ii)'s indeterminate
case — was enacted in **store revision 41**, differently and better, as subsection C's third sentence <u>[store revision 46: the fifth, store revision 44 having restored two before it]</u>. My
drafted string for it would have **contradicted** the landed text and is withdrawn. MOO-121's **S4**, which
attacks that landed sentence rather than anything in this revision, is **§7 item 78** and is not resolved
here.

**No figure moves, and this is now measured rather than argued.** Section B moves the participating count
by **zero members on both edits**: clause (vii)'s advance is capped by the member's remaining shortfall and
does not scale with the quantity credited, which Fiscal proved cellwise — **0 of 5,552 cells differ,
maximum difference 0.000000000000 months, 0.0000 expected elections** — and section B edit 2 is withdrawn
on the Director's answer, so the per-member quantity does not move either. **18.3965 participants, 78.1872
percent cap utilisation and $1,321,112 of net trust cost stand**, and D 7's release limb is what makes the
first of those true rather than an improvement on it.

**Six new items are on the card as §7 items 75 to 80**, and none of them blocks anything: D 7's release is
still under-inclusive in four cases; two words of M1's cure are mine rather than Red Team's; the parity
clock leaves one word unconformed; **S4**'s uncapped class is a money question about an enacted sentence;
*"applicant"* is still undefined and the definition I proposed was wrong; and six smaller residues are
recorded with reasons.

**Rebased twice while it was being built, and the second rebase cost nothing.** This cut was drafted on
store revision 32, rebuilt on store revision 42, and **store revision 43** — [MOO-122](/MOO/issues/MOO-122)'s
pass 14, fourteen edits in nine provisions — landed under it before it could be saved, a concurrent run
holding the file. So this is store revision **44**, written on store revision 43, and its new §7 items take
the numbers **75 to 80** after pass 14's items 71 to 74. **All seventeen anchors were re-verified unique in
store revision 43's operative region before substitution and every one of them held**: pass 14's edits are
in subdivisions G 2, G 4, D 1 and the definition of *"final qualifying retirement date"*, and this revision
touches none of them. **Nothing of store revision 43 is reversed, re-opened or renumbered here**, and
pass 14's §5.24 and §6.0-43 stand as the live sweep and ambiguity sections.

**Housekeeping, which was not optional.** The file arrived at **11,042** characters of headroom. **§3 is moved
verbatim** into the second volume of the retained record,
[`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2), because
[`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history) is itself
within 1,000 characters of the same ceiling, and store revision 41 had already had to open volume 2 for
the same reason. §3 went out under the Director's standing rule on [MOO-101](/MOO/issues/MOO-101) section E
(*"§3 moves next; §1, §5, §6 and §7 stay with the bill"*), every item number and bracketed correction
preserved, stubbed below with its durable results. **Nothing was summarised away.** §7 item 53 is still
the standing precondition for every further revision of this file.

## Moved verbatim: §0 narrative — store revision 43 and its lettered subsections

## 0.00000000000000000000000000000000000 Store revision 43 — [MOO-122](/MOO/issues/MOO-122)'s pass 14 drafted out. Fourteen edits in nine provisions, no figure moved, and the one finding the reviewer would not have introduced the bill with is closed

**Full record:** [`pass14-disposition`](/MOO/issues/MOO-42#document-pass14-disposition), written as its own
document from the start because this file had **23 characters** of headroom on arrival. Sweep **§5.24**;
ambiguities **§6.0-43**; the four questions are **§7 items 71 to 74**; banner **§8**.

**The pass.** The bounded adversarial and counsel review of store revision 39's seventeen edits:
**20 findings — 0 fatal, 8 serious, 8 moderate, 4 minor — plus 12 express null results.** It says the fatal
count expressly: no edit in store revision 39 prevents the bill from operating, creates a facial
constitutional defect, or defeats the enactment, and it could not make a case against the architecture.

**Disposition of all 20: 14 drafted out in fourteen edits, 1 declined in part with reasons, 2 corrected in
the record, 1 routed to the Director as a choice, 1 recorded with no text defect, and 1 corrected against
the reviewer's own fix direction.** `12`, `$3,000,000`, `$170,000` and the `[20]` percent contingency are
untouched by every edit; no section is added, deleted or renumbered; the bill title does not change.

**I re-read all 20 quoted strings against the live body before editing**, because narrative revision 42
(the [MOO-64](/MOO/issues/MOO-64) items, nine edits in six provisions) landed after pass 14 finished. Every
string was present as quoted. Revision 42's E3 touched the **disability-and-death** rescission sentence and
not the **involuntary-separation** rescission limb, which is the limb P14-7 and P14-12 address, so no
finding in the pass is addressed to superseded text.

### a. The three that cost a real person real money

**1. An appropriation trigger that fired on the Board's lawful silence — P14-1, and it is my defect from
store revision 39.** The F-18 cure said, in the indicative and with no discretion, that a member who
retires *"at a time when the Board has not given the statement"* is unable to retire in a qualifying
retirement **by reason of an error of the Board**. The Board has **15 days after crediting** to give that
statement, and for the whole of that period — and for the entire period before crediting — the condition
is true and the Board is in perfect compliance. So a member who paid up, filed and went one month early
engaged G 4 clause (iii): her credit vested at the pilot price and up to **$170,000** of certified subsidy
settled and became payable under subsection N **for an acceleration that never happened**, and the Board
could not refuse. The deeming is now confined to the case where the time allowed for giving the statement
**has expired**. The F-18 cure costs nothing, because the never-told member's statement is always overdue.

**2. The never-told member who does not retire was still stripped — P14-5, and she is the modal case.**
Edit 7 reached *"a member who **retires"***. Pass 12's F-18 member is the one who **does not** retire,
because she has never been told in writing that there is a date. She is not rescued anywhere else: the
floor and D 1's day-for-day extension are both keyed to the Board **giving** the statement and neither
fires if it is never given. So her bare first-sentence date matured, G 2 cut her four years back to the
sixteen months her payments bought at standard cost, and she never knew there was a deadline. The second
limb of the new sentence reaches her by the passing of the date rather than by a retirement. **It extends
no window and adds nothing to cap occupancy** — her date does not move; her credit vests and the subsidy
settles and clears on the date it would otherwise have been stripped.

**3. Two classes of reservation had no terminating event at all — P14-15, paired with P14-5.** Clause (iii)
states a **status**, not an event, and a member can occupy it without ever retiring: the clearest case is
the member who pays in full and whom the Board never credits. Her credit vests, which **bars D 7's
release**, and subdivisions 2 and 3 are disapplied — but the settlement sentence had only three limbs, all
of which require a death, a disability effective date or a retirement. **Her reservation and contingency
were charged against the $3,000,000 with no terminating event, for the life of the Program and beyond**,
because enactment 3 clause (ii) keeps them charged after expiry. On twelve elections one such election
removes about **6 percent** of the Program's capacity permanently. One new sentence settles her on her
final qualifying retirement date or, where she has none, on the completion date.

### b. Five more, each a real failure

- **P14-2 — the F-3 cure was not secured, and the pass 12 disposition's reasoning for leaving it alone was
  mine.** I wrote that F-3 was *"drafted out by F-2's fix, with no separate edit"* because *"once the date
  itself moves, the clock moves with it."* That depends on the date-setter operating **before** G 2's clock
  matures, and its date cannot be computed until the Board acts. Two readings are available and the text
  chose neither; **administrators will take the one on which they can compute something**, and on that
  reading the protection is self-nullifying in its only class of application. **Nothing suspended a Board
  period during subsection M tolling** — M 2 tolls periods *"within which the member must act"*, G 4's
  suspension was confined to a pending **disability** application, and G 2's own exception reaches only
  subdivision 4's three devices. G 4's existing non-running formula now reaches a pending tolling request
  too, which makes the cure independent of which reading wins. **This is the second half of pass 12's own
  F-3 fix, which my disposition declined.**
- **P14-3 — a date moved by force of law and nobody had to tell her.** The date-setter says the member's
  final qualifying retirement date **is** the first day of the second month after the Board acts. The
  definition's statement duty is a one-off due 15 days after crediting, and its only follow-on reaches a
  date *approved* by the Board; this date is approved by nobody. So the Board could answer her
  reconsideration in January 2034, give her a window to 1 March 2034, and the only writing the statute
  obliged it to send her would still say her window closed on 1 March 2033. **The statute gave her a window
  and told nobody.** The Board must now state the date in the decision it is already writing.
- **P14-4 — the statute ordered the Board to misinform her.** D 1 clause (i) still commanded the Board to
  state *"that the date so extended is subject to the outer bound stated in that definition"*, and that is
  now untrue for three classes of member, two of them created by store revision 39: the floor member and
  the date-setter member both operate *"notwithstanding"* the bound, and the G 4-extended member is outside
  it because the bound by its own words reaches only the date *"as extended under subdivision D 1 or as
  tolled under subsection M."* **The same mandated document therefore contained her actual date and a
  recital that that date was subject to a bound she was past.** *"The limits stated in that definition"*
  is true whichever sentence governs her, and the recital's only job is to tell her the date is not
  open-ended.
- **P14-6 — the proviso put the finding of fact in the hands of the party that pays for it.** The extension
  operated where the Board *"has otherwise determined"*; the Board's duty to write to her ran from when it
  *"otherwise learns"*; the rescission limb used a third predicate, *"learned"*. So a Board that **learns**
  of a separation owed her, within 15 days, a notice stating her **unextended** deadline, and nothing
  obliged it to take the one further step that would move it. **And she could not compel that step** —
  § 2.2-4001 confines a *"case decision"* to *"any agency proceeding or determination"*, and a failure to
  determine is neither, so Article 5 has nothing to review. The extension now operates where the Board has
  **learned of facts from which it is required to determine**, and the member has an express route to file
  the evidence and a 30-day determination with notice, reasons and subsection M review.
- **P14-7 — strip, rescind, restore, reinstate over the cap, freeze the Program, strip again.** The
  rescission limb restored the credit and reinstated the reservation and gave the member **no date she
  could use**, because the extension is a fixed arithmetic function of a separation date now months in the
  past. Meanwhile the reinstatement is charged over the cap and the next sentence commands the Board to
  *"accept no further election until the excess is eliminated"* — and the excess could clear only on a
  second G 2 determination for which no period ran. **Every wait-listed applicant paid for the agency's
  filing failure in the interval.** The limb now carries the date-setter, so the member retires, G 1
  settles, and the excess clears on settlement.

### c. Two choices of mine inside the fourteen, and one departure from the reviewer

**P14-8 — I took the reviewer's primary fix and it reduces a member windfall. Direction of effect stated.**
Store revision 39 made a G 2 determination that takes effect too early *"of no effect"*, and the section
supplies **no route to undo** a refund already paid or a reservation already released and re-let to the
next applicant off the waiting list. G 4's reinstatement sentence does not reach it, because that release
**was** in accordance with D 7. So a three-day mailing miscount left her credit never reduced, her
reservation held for somebody else, and the aggregate charged over $3,000,000 — an unfunded liability
flowing into the employer contribution rate at the next valuation. The determination now **takes effect
instead on the first day on which it may take effect**. Her notice period and her M 2 period are preserved
in full; what she loses is a windfall nobody decided to give her. **The nullity with the three verbs it
would need is drafted at §7 item 73 and one edit restores it.**

**P14-9 — the reviewer's own fix direction does not work, and I have not enacted either half. §7 item 71.**
It proposes keying the 12-month cap to *"12 months after the first day of the second month following the
month in which the Board last so acts"* — which is the date the sentence already sets, so the cap would
never bind and would be surplusage. The finding behind it is real: keyed to the outer bound, the cap turns
a cure for Board delay into a **ceiling on Board delay**, and past about 21 months it gives her nothing.
But the cap **is** the occupancy bound, so removing its bite is the Director's call and not mine. Three
options are drafted in the item.

**P14-6's deeming device is declined and drafted. §7 item 74.** The reviewer would deem the separation
determined where the Board does not act in 30 days. With the predicates aligned the extension already
operates on the Board's **learning**, so the deeming adds certainty rather than substance — and deeming a
fact found against the party that must fund it is a choice about cap occupancy, which is the same reason
§7 item 33's deemed decision was withdrawn.

### d. What is with the Director, and the two things in the pass worth more than its findings

**Four items: 71 (the cap's measuring point), 72 (P14-10, which reading of G 4's clock to enact — about
three months of reservation occupancy per repeat separation), 73 (restore the nullity, or keep the cure),
74 (the deeming device).** Only 72 is a question the reviewer put to the Director; the other three are
mine, raised rather than resolved by drafting.

**First: the eCFR caveat is resolved.** Pass 12's F-8 rested on a **Cornell mirror**, and I said so and
said the fix was drafted so the answer could not change the text either way. Pass 14 opened
26 C.F.R. § 1.415(j)-1(a), (b) and (d) at **eCFR's own versioner API** and the mirror was accurate word for
word: the calendar year is the default *"[u]nless the terms of a plan provide otherwise"*, a plan has only
one limitation year, and *"[o]nce established, the limitation year may be changed only by amending the
plan."* **F-8's ground is sound and [MOO-115](/MOO/issues/MOO-115) is no longer load-bearing for the bill
text.**

**Second: the nondelegation challenge to *"otherwise determined"* fails, and no document of ours may
concede it.** Virginia requires a delegation to specify policies and fix definite standards, but the same
line holds that a delegation of the power to **ascertain and determine whether facts or conditions
required by a law exist** is not of itself arbitrary — and *"an involuntary separation occurred"* is a fact
under a borrowed statutory definition. **The exposure from P14-6 is procedural and sounds in the
Administrative Process Act, not in the Constitution.** The reviewer could not open *Ames v. Town of
Painter* at source and founded no live finding on it; neither do I.

## Moved verbatim: §5.25 — the store revision 45 sweep

### 5.25 Store revision 45 — one deletion and two new sentences, chased in both directions

**Performed. Full table at [`moo97-rev45-record`](/MOO/issues/MOO-97#document-moo97-rev45-record) §3.** Seven checks, counted mechanically over the bill text alone and not the commentary. **No conforming amendment is required and none is made. No section leaves the act and none joins it; the act still amends one section and adds one, and the title line is unchanged. Enactment clauses: nothing to add. Markup: both new sentences sit inside subdivision G 4's existing `<u>` block and nothing is struck through, because § 51.1-142.4 is wholly new text — words removed from new text are simply absent.** The five results that carry weight:

- **The deletion strands nothing.** § 51.1-153 goes 10 → 8 in the bill and **2 → 0 inside G 4**, still cited by two definitions and four times by subdivision D 1; § 51.1-155.1 goes 3 → 2 and **1 → 0 inside G 4**; subdivision D 1 goes 4 → 2 and **2 → 0 inside G 4**, where it was named only in order to switch its own two duties off. *"Qualifying retirement"* goes 59 → 55, all four lost uses being inside the deleted words.
- **One citation is new to the bill: *"subdivision B 4 e of § 51.1-142.2"*** (0 → 1), in the notice sentence, naming the paying employer. The paragraph is verified to exist in the amended § 51.1-142.2, which **is** a section the act amends. It is a deliberate asymmetry with G 4's refund sentence, which identifies the same class by paraphrase: a notice duty has to be determinate as to its addressee.
- ***"the death of a member in service"* is the chapter's own vocabulary**, not a coined term — § 51.1-162 B operates where a member *"dies in service"* and § 51.1-153 A speaks of *"any member in service"*, both re-read on the official text this revision — and the bill already used *"a member in service"* in clause (i) of *"eligible member"*.
- **Where the measure lands.** § 51.1-165 C 1 is **not displaced**: for the filed-notice death this chapter's answer is § 51.1-163, and for the member with no spouse, minor child or surviving parent it is § 51.1-162 A. §§ 51.1-162 and 51.1-163 remain cited **nowhere** in the bill, re-counted at zero each, so the collision stays invisible on the face of the act and must travel in the memo's risk section and in the drafting request to DLS.
- **Nothing depended on the deleted hypothetical.** Checked at every use of *"qualifying retirement"* and at subsections H and N: settlement in the death case runs on clause (a) of G 4's own settlement sentence, the redetermination substitutes *"that date"*, H and N key on **settlement**, and G 1's trigger is an **actual** effective date of retirement a deceased member never has.

## Moved verbatim: §5.24 — the store revision 43 sweep

### 5.24 Store revision 43 — the fourteen edits, chased in both directions, and three rows of §5.21 corrected

**Performed. Full table at [`pass14-disposition`](/MOO/issues/MOO-42#document-pass14-disposition) §4.**

**Outward — every citation the fourteen edits introduce or touch.** They introduce **no new section
citation**. The references they use are to provisions of this act — the definition of *"final qualifying
retirement date"*, subdivision D 7, subdivisions G 1 to G 5, subsection M, subsection N, subdivision B 4 f
of § 51.1-142.2 and clause (ii) of that subdivision — and every one resolves. `§ 2.2-3200` is unchanged by
edit 10, which adds a residual date limb and does not touch the borrowed definition. `§ 415` and the
regulations are unchanged by edits 12 and 13.

**Inward — every provision that reads what the fourteen edits changed.**

- **Edit 1 and edit 2 (G 4 clause (iii) and the new settlement trigger).** Clause (iii) is read by G 4's
  vesting sentence, by the settlement sentence's limb (c), by D 7's second sentence (the bar on release),
  by G 2's exclusion limb and by subsection N. All five are consistent with both limbs of the confined
  deeming, and the new settlement sentence is expressly subject to the two existing bars — no settlement
  after the reservation has been released in accordance with D 7 or after a determination under
  subdivision 2 or 3 has taken effect. **The new sentence invokes the redetermination and subsection N by
  reference rather than by an ordinal**, so the lesser-of cap, the release of the excess and the
  no-obligation guarantee all reach it without amendment.
- **Edit 3 (the non-running sentence).** Reaches periods *"stated in subdivision 2 or in this
  subdivision"*. Checked against subsection M's own 120-day aggregate tolling cap: no conflict, because
  M 2 caps tolling of **member** periods and edit 3 suspends **Board** periods. Checked against G 2's
  120-day outer limit on when a determination must take effect: that limit is a period stated in
  subdivision 2 and is therefore suspended with the rest, which is the result the finding required.
- **Edit 4 (the definition's new duty).** Does not move any date. The only provision that reads it is
  subsection M's reconsideration decision, which the Board is already writing.
- **Edit 5 (D 1 clause (i)).** Notice **content** only. No provision computes anything from the recital.
- **Edits 6 and 7 (the proviso and the member's route).** The proviso governs the extension only; the
  90-day vesting branch still runs from the separation itself and is unchanged, so a member whose agency
  never notifies keeps the vesting branch inside her unmoved window. The new determination is expressly a
  determination for subsection M, so the review right attaches without amending M 2.
- **Edit 8 (the rescission limb's date-setter).** Moves the final qualifying retirement date, which is
  the carrier for all six downstream provisions identified at §5.21 as corrected below. Checked each:
  subsection F's duty, D 7's release, G 2's clock, G 4's clock, D 1's notice content and the definition of
  *"qualifying retirement"*. **None needs a carve-out**, which is the property that made the F-2 cure work
  and makes this one work.
- **Edit 9 (G 2's timing floor).** *"Of no effect"* now appears **once** in the operative text, in G 4's
  disability instance, where the section supplies rescission, restoration and reinstatement. The refund
  sentence, the release of the reservation and the first-payment sentence all key to the determination
  *taking effect*, so each moves with the cured date and none is stranded.
- **Edit 10 (the residual separation date).** *"The date of the involuntary separation"* appears **three**
  times in G 4 — the 90-day vesting branch, the extension and the agency's 15-day notice duty — and all
  three now have a date for every separation within § 2.2-3200 B.
- **Edit 11 (the rescission limb's datum).** Read only by that limb.
- **Edits 12 and 13 (B 4 f).** The confined carve-out is read by G 4 clause (iii), which is now narrower
  against the member in exactly one respect and wider in the respect the finding identified: a Board error
  in a **B 4 c redetermination** is again an error of the Board. The cap exception is read by D 7's second
  sentence, which already saves a reservation while a clause (ii) election stands.
- **Edit 14 (the notices sentence).** Notice content only; subsection J already requires every
  reinstatement and every excess to be reported.

**Mechanical.** *"Of no effect"*: 2 → **1**. *"The date of the involuntary separation"*: **3**, unchanged.
*"The earliest of"*: **1**, in G 4's settlement sentence. *"This subdivision 4"*: **2** after edit 12, both
in § 51.1-142.2 B 4. *"Limitation year"* in §1: 6 → **7**, of which **5** are in B 4 f after edit 13. *"Is of no effect"* in subdivision G 2: **0**. Title, enacting clause and every
enactment clause: **unchanged** — no edit adds, deletes or renumbers a subsection, subdivision or clause.

**Three rows of §5.21's sweep are corrected, and all three corrections are against me.**

1. **P14-17.** The row claiming *"no new reference to a sentence by ordinal was introduced"* does not hold.
   Store revision 39's edit 18 introduced one — *"the limitation in the first sentence of subdivision
   D 2"* — which is the seventh *"first sentence"* in the operative text, and its edit 5 added **two** new
   *"the preceding sentence"* references to a definition that now runs to nine sentences. **I would keep
   both**, because *"first sentence"* is stable where *"last sentence"* is not, but the row was wrong.
   Store revision 43 adds **no** new ordinal reference to a sentence: the new settlement sentence names
   clauses (a), (b) and (c) and the conditions themselves rather than a sentence.
2. **P14-18.** The uses of *"limitation year"* in B 4 f were **four**, not the five the row claimed. Six
   occurrences existed in §1: the defined term, one inside the definition's own body, and four in B 4 f.
   All four resolve correctly on the plan's own year, so the conclusion survived and only the count was
   wrong. **Edit 13 adds a fifth**, in the 24-month cap's new exception, so the row's number is now right
   for the wrong reason: §1 carries **seven** occurrences and B 4 f carries **five**, and the fifth
   resolves on the same plan year as the other four.
3. **Pass 14 N14-2.** The provisions that move with the final qualifying retirement date are **six**, not
   five. The sixth — and the one that makes the whole cure work — is the **definition of *"qualifying
   retirement"* itself**, which is why moving the date moves everything downstream of it without a
   carve-out anywhere.

## Moved verbatim: §6.0-45

### 6.0-45 Ambiguities resolved in store revision 45

**Nine in full at [`moo97-rev45-record`](/MOO/issues/MOO-97#document-moo97-rev45-record) §4; the six that decided text are here.**

1. **Where (d) goes.** Two later sentences of G 4 anchor on *"the preceding sentence"*, so a sentence inserted after the death sentence would have re-pointed both. It is enacted **at the end of the death branch**, which is where item 60 (d) proposed it and which leaves every anchor reading what it read before. The measure is general to the subdivision, so position does not narrow it.
2. **Nothing of the disapplications survives, and that is the point of taking (d).** Store revision 40 spent 423 characters enumerating what a dead member cannot satisfy and store revision 37 spent 143 before it. All of it is gone, because a requirement only had to be switched off while the text **deemed** a retirement that could not have happened. **I am recording the reversal of my own two revisions explicitly**, so that nobody later restores half of it on the strength of §6.0-40.
3. **A scope defect in the old notice limb, found here rather than by the review, and cured.** *"and shall give written notice …"* sat inside the *"except that … adverse federal tax consequence"* clause, whose nearest subject is that clause's own *"the Board shall apply"* — so on the strict reading the partial payer was owed notice **only** where her refund could not be paid. Lifting the notice into its own sentence answers F8 and cures that at once, which is why the change is a re-cut and not an addition.
4. **The deadline is the crediting, and the crediting is itself undated in the death branch — stated, not fixed.** I used the struck limb's own trigger rather than invent a second one. But G 4 gives the Board no date by which to credit in the death case, so the notice is bounded in content and not in time. **A crediting deadline is a new duty on the Board and was not agreed**; it is named at item 60 as the smallest remaining repair.
5. **(e) is closed, not merely unselected — and that corrects §6.0-40 item 5, item 60 (e) and [MOO-118](/MOO/issues/MOO-118)'s F2, all of which are mine or rest on my words.** Importing subdivision **G 3's guard** into G 4 is **unnecessary**: the last sentence of **subsection E** already provides that *"except for the purposes of the definition of 'eligible member' in subsection A, no member shall be treated as having reached his unreduced retirement eligibility date by reason of an election before payment in full is received"*, and a member who dies before completing payment has not paid in full. **E's carve-out for G 4 reaches the crediting limb only**, not this one. G 3's own sentence restates E for its own case, so **there is no asymmetry between G 3 and G 4 to cure** — I said there was, and there is not.
6. **One word of the approved sentence is changed, and I am naming it.** The card said *"the benefit the chapter provides"*; the enacted words are *"the benefit **this** chapter provides"*. The bill says *"this chapter"* in eleven other places and nowhere *"the chapter"*, so the bare article would have been the only one of its kind in the act. **It changes no meaning and it is still a change to words the Director approved.**

## Moved verbatim: §6.0-43

### 6.0-43 Ambiguities resolved in store revision 43

1. **Where the deeming line falls, and it is drawn at the expiry of the Board's own time.** Edit 1 had to
   choose between three readings of *"the Board has not given the statement"*: at any time (store revision
   39's text, which deems an error while the Board is in compliance and pays a subsidy for an acceleration
   that never happened), only where the statement is **overdue**, or only where it is never given at all.
   **I took the middle one.** The last would have left the member whose statement comes two years late
   outside the cure for no reason, and the first is P14-1. The cure for the never-told member is unaffected,
   because her statement is always overdue.
2. **Whether the new settlement trigger is a fourth limb of *"the earliest of"* or a separate sentence.
   A separate sentence.** As a fourth limb it would have been ambiguous in tense — a clause (iii) member
   who later retires could have settled on the earlier of her final date and her retirement, which is not
   the intention — and it would have put a conditional limb inside a list of three unconditional dates. As
   a sentence it states its own condition in the past (*"has neither died nor been approved … nor
   retired"*) and its own date, and it is caught by the two existing bars without amendment.
3. **The settlement date for the member who has no final qualifying retirement date.** She is the member
   the Board never credited, so the certification's **completion date** is the only date in her file that
   is both certain and connected to the election. The alternative — the date the Board makes the
   determination — would have let the Board's own delay choose the valuation date of the quantity it pays,
   which is the defect P14-1 is about in another form.
4. **The reviewer's fix for P14-9 is surplusage and I did not enact it.** Keying the 12-month cap to
   *"12 months after the first day of the second month following the month in which the Board last so
   acts"* bounds a date by itself plus twelve months, so the cap could never bind. The real choice is
   between bounding occupancy and never cutting the member off, and there is no middle: the cap **is** the
   occupancy bound. **§7 item 71**, three options drafted.
5. **Edit 9 reduces a member protection and the direction of effect is stated rather than netted away.**
   A determination that takes effect three days early is no longer a nullity; it takes effect on the first
   day on which it lawfully may. Her 30-day notice floor and her M 2 reconsideration period are preserved
   in full. What she loses is the windfall — four years of credit never reduced — which was a by-product
   of the F-15 fix's wording and was never a decided policy, and which the section had no machinery to
   deliver. **The nullity with the three verbs and two notices it would need is drafted at §7 item 73.**
6. **Edit 7 gives the member a route and not a remedy against inaction.** The 30-day determination carries
   notice, reasons and subsection M review. It does **not** carry the reviewer's deeming rule, because
   with edit 6's predicates aligned the extension already operates on the Board's **learning** of the
   facts, so the deeming would add certainty rather than substance — and deeming a fact against the party
   that funds it is a cap-occupancy choice. **§7 item 74.**
7. **Edit 8's outer bound is 12 months and the numeral is mine, taken from the section's own register.**
   The first sentence of the definition, the outer bound and B 4 f's extension all use 12. The reviewer
   proposed the same figure. It bounds the rescission branch the way the date-setter bounds the tolling
   branch, so neither branch can run on a Board act with no cap — which is the failure mode I have had to
   withdraw an assurance about twice.
8. **The window envelope is stated as a statement of the text and not as a warranty.** With store revision
   43 the components are: 12 months from the earliest qualifying retirement date; plus the three-month
   processing extension; plus at most 120 days of tolling; plus any days of the Board's own lateness, now
   bounded by the outer bound except where the floor or the date-setter lawfully overrides it; plus at most
   one G 4 extension of about four months; plus, on a rescission, the date-setter in edit 8, itself capped
   at 12 months. **Two residuals are open and both are in front of the Director rather than cured by a
   numeral of mine: §7 item 71 (the cap's measuring point) and §7 item 68 (the floor).** I am not
   restating the assurance a third time.

# Moved in store revision 48 — §6.0-41, §5.1 and §6.0-46

**Moved verbatim from [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) in store revision 48 (MOO-128's pass 15 drafted out), every check number, table row, figure and lettered label preserved. Nothing was summarised away.** Each section is stubbed in place in the bill file with its durable results. **§6.0-41 includes the annotation store revision 46 added to it on pass 14's M-1, which is live and is preserved word for word; its open question is §7 item 82.** **§6.0-46 was moved because store revision 48 supersedes its subject** — store revision 46's edit was a relief from determining a clause (ii) amount and edit 1 replaces it with a substituted determination — and its three durable results are carried in the stub. **§5.1 is the oldest sweep in the file and 27 later sweeps have re-run its checks; its durable result is that no conforming amendment is needed for any reference to § 51.1-142.2, and none is made.** Reason for the move: store revision 48 arrived at 7,350 characters of headroom and its record did not fit; the first retained-record document is 936 characters from the store's 524,288-character ceiling.

### 6.0-41 Ambiguities resolved in store revision 41

**1. I enacted the non-binding reading of clause (ii), and the choice was mine.** The bill is silent and
both readings are available: an empty solution set yields zero, or it yields no limit. I took **no
limit**, on three grounds in this order. The authorised participant count and MOO-71's **18 (range 9 to
30)** are measured on that reading, so enacting it is the one way to put the count on a basis the
statute requires rather than on a convention in a model file. The other reading gives the member a cap
of zero and, since store revision 38, no provision refuses her — so it produces pass 13's F-3 state
rather than a refusal, and taking it would require restoring the bar as well. And of the two, only the
non-binding reading leaves a member who is one month from an unreduced date she cannot advance by
service free to buy the credit clauses (i) and (iii) allow her. **The direction of effect is stated
rather than buried: against the alternative reading the sentence is worth +0.0259 participants and
about $4,000 of the $3,000,000, and up to $166,226 for one member.**

**2. I added a statement duty rather than a notice duty, and the deadline is the certification's.** The
Board must *"so state in that certification in place of the amount determined under that clause"* <u>[store
revision 46: the sentence now reads *"in place of the amount that clause would otherwise require to be
stated"*, and the Board *"is not required to determine an amount under that clause"* at all — pass 14's
**S-3** and **m-2**; the quotation is annotated rather than rewritten]</u> — so
the determination is on the face of the document the member receives, which makes it a determination of
the Board that subdivision M 2 reaches. I did **not** give it its own 30-day deadline or notice
sentence: subsection C's second sentence already carries the 30-day determination deadline, and the
certification's own timing is subdivision D 1's. **The consequence of non-compliance is the one the
other three amounts have** — the certification is a precondition of acceptance under D 1 — and that is
the honest limit of the cure. A notice duty keyed to this statement alone would be a new provision, and
it is not mine to add.

**3. I declined the date half of pass 13's F-12 and took only the base half.** F-12 proposed that
clause (v) read *"as of the filing date of the member's complete application"* in place of *"on the date
the member files a complete application"*, aligning its date reference with clause (ii). I did not,
for two reasons that are drafting reasons and not disagreement: clauses (vi), (vii) and (viii) all use
the **event** form (*"the date the member files that application"*), so aligning clause (v) alone would
cure one asymmetry by creating three; and clauses (vi) and (vii) refer back to *"that application"*,
whose antecedent is clause (v)'s *"a complete application"*. Subdivision D 4's retention of the filing
date *"for all purposes of this section"* already carries clause (v), which is why F-12 reports the
point as sound-but-tightenable rather than as a defect. **What I did take is the half that bears on
containment**: the entitlement base, inserted in the words clause (ii) uses, so that the two limbs read
on one base on the face of the bill and not only by construction.

**4. The *"amend together or not at all"* rule now reaches clauses (vi) to (viii), and that is pass
13's F-2.** §7 item 35 attached the rule to clause (v) alone. Clause (v) is a date test that a member
short of an **age** passes; the limb that actually confines the class to a one-month window is clause
**(vi)**. The rule is restated at the item to cover clauses (vi) to (viii), because a later revision
that widens clause (vi)'s window — a natural ask — would widen the class the new third sentence
addresses, with no bar downstream to catch it.

**5. What I did not do.** I did not restore the deleted bar in any form, and I did not add the
acceptance bar pass 13 recommends. Both are §7 item 70, drafted in full, with the reason the
recommended sentence does not reach the two routes it is offered against.

### 5.1 References to § 51.1-142.2

| Cross-reference | Status under this draft | Why |
|---|---|---|
| **§ 51.1-124.3, "Creditable service"** — *"prior service as set forth in § 51.1-142.2 plus membership service for which credit is allowable"* | **No amendment needed. Confirmed by MOO-44 §5(a).** | § 51.1-124.3 separately defines **"Prior service"** as *"service rendered prior to becoming a member of the Retirement System,"* which active duty military service before VRS membership satisfies on the face of the definition. The purchase authority stays in subdivision B 2 of § 51.1-142.2; § 51.1-142.4 conditions only the price. MOO-44 tested the contrary hypothesis and it failed. The declaratory sentence in § 51.1-142.4 B is kept and is now framed "For the avoidance of doubt," per MOO-44 §5(a) rider 1, so it cannot be read to imply that an ordinary B 2 purchase might not be creditable service. |
| **§ 51.1-124.3, "Purchase of service contract"** | No amendment needed. | Section-wide reference; no subsection is renumbered and no subdivision is moved. |
| **§ 51.1-142.3 A** — *"clause (iv) of subdivision B 1 of § 51.1-142.2"* | No amendment needed. **Verified MOO-54.** | B 1 is reproduced verbatim and unchanged; its clause lettering is untouched. The new material is a fourth subdivision of subsection B. The "subdivision B 1" pin is itself post-c. 563: c. 563 conformed this reference from "subdivision A 1" when it relettered § 51.1-142.2, so the draft is reading the current text, not the 2025 text. |
| **§ 22.1-296 D** — cross-references § 51.1-142.2 (added by 2026, c. 563) | No amendment needed. **Verified MOO-54.** | Depends on B 1 clause (i), which is unchanged. |
| **§ 51.1-303 B** (Judicial Retirement System) — *"Service purchased in accordance with the provisions of § 51.1-142.2 shall not be considered in determining the actuarial equivalent for early retirement…"* | No amendment needed, and judges are expressly out. | § 51.1-142.4 A excludes members of Chapter 3 from "eligible member" by name, alongside Chapter 2 (SPORS) and Chapter 2.1 (VaLORS), so § 51.1-303 B operates exactly as today. MOO-5 §9.2 asked for this expressly. |
| **§ 51.1-142.2 F and G** | Not amended; **reconciled in the new text.** | F supplies partial-credit mechanics, which § 51.1-142.4 G 3 points at rather than duplicating; subsection E of § 51.1-142.4 now also forecloses any additional charge arising from the payment method, which closes MOO-44's S9. G is overridden only to the extent of the 5 percent member floor, by the express "Notwithstanding subsection G" in B 4 e. |
| **§ 51.1-142.4** | **Available. Verified MOO-54.** | Article 6 contains §§ 51.1-140 (repealed), 141, 142 (repealed), 142.2, 142.3, 143 (repealed) and 143.1. There is no § 51.1-142.4. Confirmed by the strongest test available: **zero occurrences of the string "51.1-142.4" in the full text of Title 51.1** (MOO-54 §6.2, 11 October 2026), and the Article 6 table of contents lists only §§ 51.1-140, 51.1-141, 51.1-142, 51.1-142.2, 51.1-142.3, 51.1-143 and 51.1-143.1. (**§ 51.1-142.1 *does* exist as a repealed section number** — repealed by Acts 2001, cc. 686 and 697, and rendered in the full-chapter view under the combined catchline *"§§ 51.1-142, 51.1-142.1. Repealed."* — so it is **not** available for reuse. Revision 3 said there was no § 51.1-142.1; the section-page table of contents shows only "§ 51.1-142 Repealed", which is how it was missed. This is the second instance of the two-renderings-disagree problem recorded in MOO-49 §9 gap 2 — see the §0.0 method note.) The row's conclusion is unaffected: this bill numbers its new section 51.1-142.4 and nothing occupies that number. Re-verified by MOO-44 §9 item 1 and again by MOO-54. |

### 6.0-46 Ambiguities resolved in store revision 46 — performed; recorded in the companion document

**Ten items in full at [`moo123-pass14-disposition`](/MOO/issues/MOO-87#document-moo123-pass14-disposition) §6.** The five a later reader must not have to reconstruct:

1. **I used *"is not required"* and not pass 14's *"shall not be required"***, because §6.1's rule is that *"shall"* creates a duty and is never used for a statement of fact, and the relief of a duty is not a duty. Both forms are good Virginia style; this one keeps the bill internally consistent, and the choice was deliberate rather than a transcription slip.
2. **I declined a *"notwithstanding the second sentence of this subsection"* opener**, although it would have been shorter and more emphatic, because it would have created the **first sentence-ordinal citation into subsection C** in the operative text, and this file has now had three sentence-ordinal references rot — store revisions 41 and 44 each moved one. **The rule is §6.1's: name the provision, not the sentence.** Specific-over-general does the same work with no hostage.
3. **The relief is from the duty to *determine*, not from clause (ii).** The sentence still says clause (ii) *"does not limit"* and does not say it *"does not apply"*, which would have been a larger claim and would have disturbed the definition of *"maximum purchasable amount"*, which excludes clause (ii) in terms.
4. **Store revision 42's contingency sentence does not move the trigger class, and that reason is legal rather than measured.** The two § 51.1-155.1 routes are gated at age 50 or above, so they were already unreachable by a class that is under 50 at the filing date; and for a member aged 50 or above § 51.1-153 B 2 stays reachable by a finite quantity of service, so clause (ii) yields a number and the trigger does not fire. **I have not re-run the engine and I assert no figure**; the confirmation is with Fiscal at [MOO-129](/MOO/issues/MOO-129).
5. **M-1's direction-of-effect claim is corrected rather than abandoned.** *"It can only exclude, never admit"* now reads: **no quantity of creditable service can postpone an unreduced retirement eligibility date; the direction of effect of the base specification itself is not determinate on the face of the statute.** Both occurrences are corrected. The text question is §7 item 82's, and [MOO-124](/MOO/issues/MOO-124) has answered the research question it turns on — in a direction that cuts against pass 14's own reading of it.

---

## 0.00000000000000000000000000000000000000 Store revision 46 — [MOO-123](/MOO/issues/MOO-123)'s pass 14 drafted out. One edit, 88 characters, relieving a mandatory duty the Board could not perform; and pass 14's most serious finding does not hold against the store

**Whole record in [`moo123-pass14-disposition`](/MOO/issues/MOO-87#document-moo123-pass14-disposition); this file had no room for it**, on the convention store revisions 33, 36, 40, 41, 42, 43 and 44 set. That document carries the redline, the answer to S-1 with its string counts, the finding-by-finding disposition of all 11 findings, the cross-reference sweep **§26**, the ambiguities **§6.0-46**, and **the full drafted text of §7 items 81, 82 and 83 and of the addendum to §7 item 70**. **No §26 or §6.0-46 body is added here; both are stubs that point there.**

**The edit, verbatim, in subsection C's no-limit sentence** (the section is wholly new language and is underlined in the bill, so the strikethrough is for your eye only and the markup will not show it):

> … clause (ii) of this subsection does not limit the service credit the member may purchase, <u>the Board is not required to determine an amount under that clause,</u> and the Board shall so state in that certification in place of the amount ~~determined under that clause~~ <u>that clause would otherwise require to be stated</u>.

**Pass 14's S-3.** The second sentence commands the Board to determine each of the three amounts within 30 days; the no-limit sentence displaced only the **statement**. For the trigger class — a Plan 1 member under age 50, short of an **age** and not of service — the Board was left under an unqualified 30-day mandatory duty to determine an amount whose solution set the same sentence declares empty, and **store revision 44's new subsection J reporting sentence had just made that failure reportable in every case.** The edit also takes pass 14's **m-2** in the same words.

**S-1 does not hold.** Both of store revision 41's edits were in this document when the review landed and are in it now — verified by string count at document revision 47, `41a3bbd9`, 524,265 characters, and re-verified on rebase at document revision 50, `cd40622b`. §7 ran items 1 to 70 with no duplicate and no gap, which disposes of **m-1** too. The one part of S-1 that holds is its report about §6.0-39 items 2 and 3, and that mislabelling was in MOO-123's commission rather than in this file. Evidence at §2 of the record.

**Disposition of 11 findings: 1 drafted out (S-3, with m-2), 1 answered against the reviewer on the evidence (S-1), 2 already closed in the text (S-2, m-1), 1 closed by store revision 42 under me (Q1's contingency residual), 1 mostly closed by store revision 44 under me with the residue drafted (M-3), 3 carried into drafted items (M-1/M-2, M-5, and Q5's route trace), and 2 corrected in the record (M-1's direction-of-effect claim, M-4).** Second edit of this revision: **§7 item 35 stated its own protection rule twice, in two widths, and the narrow occurrence is widened** — pass 14's S-2 found a real residue there. **No figure moves. No designator is renumbered. No section is added. Nothing was moved out and no space was freed**, because a concurrent heartbeat had already prepared the §8 move that `bill-text-s8-revision-history-2` records as store revision 45.

---

## 0.000000000000000000000000000000000000000 Store revision 47 — [MOO-127](/MOO/issues/MOO-127)'s pass 15 drafted out. Seventeen edits in eleven provisions, no figure moved, and the double settlement the reviewer found is closed

**Whole record in [`pass15-disposition`](/MOO/issues/MOO-42#document-pass15-disposition), written as its own
document from the start because this file arrived with about 6,400 characters of headroom.**

**What landed.** [MOO-127](/MOO/issues/MOO-127)'s **pass 15** — the bounded adversarial and counsel review of
store revision 43's fourteen edits — returned **25 findings (0 fatal, 6 serious, 11 moderate, 8 minor) plus 15
express null results**. **Disposition of all 25: 17 drafted out in seventeen edits, 1 recorded as no change
with the reason (m-6), 3 corrected in the record, and 4 routed to the Director as §7 items 84 to 87 with the
annotations to items 71, 72 and 73 that go with them.** `12`, `$3,000,000`, `$170,000` and the `[20]` percent
contingency are untouched by every edit; no section is added, deleted or renumbered; the bill title does not
change.

**I re-read all fourteen of pass 15's quoted strings and all seventeen of my own target strings against the
live body before editing**, because store revisions 44, 45 and 46 landed after the pass verified against
document revision `9cfa093e`. Every one was present exactly once. **No finding in the pass is addressed to
text that had already changed.**

### a. The one that pays twice — S-1, and it is the converse of a claim of mine

Store revision 43's new settlement sentence sits **outside** the *"earliest of"* sentence and carries no
exclusion from it. §6.0-43 item 2 said it "is caught by the two existing bars without amendment." **That is
right about a first settlement and wrong about a second**, which is the reviewer's point and which I accept:
the backstop reaches a release under subdivision D 7 and a determination under subdivision 2 or 3, and for a
clause (iii) member neither can have happened — D 7's second sentence bars release because her credit vests,
and subdivision 2 is disapplied. So a member settled on her passed final qualifying retirement date could be
settled **again** on her death years later, and subsection N — which keys its duty to *"upon the settlement"*
— pays on each. **Up to $170,000 twice on one election.**

**Enacted: fix (a), eight words widened to fourteen** — *"and no certified subsidy is settled more than once
under this subdivision or under subdivision 1."* I added the subdivision 1 limb the reviewer did not, so the
rule is single-settlement across the section rather than inside G 4 only. **The structural answer — making
the date clause (d) of *"the earliest of"* — is better and longer, and it is §7 item 84**, because choosing a
restructure over a bar is the Director's call and because this file is at the store ceiling. **Direction of
effect: (a) can only reduce what the Commonwealth pays and forecloses nothing (b) would do.**

### b. Three more that cost a real person real money

**The Board's clocks stopped and the member's did not — S-3.** Store revision 43 suspended every G 2 and G 4
period while a tolling request is pending, to secure pass 12's F-3 cure. **Subsection M 2 caps the member's
identical tolling at 120 days and expressly excludes the Board's own overrun past its 90 days; the Board's
non-running had no cap at all.** On the reviewer's facts a Board that took fifteen months to answer one
request was in perfect compliance on the day it answered and had four months left, while the member was paid
**nothing** throughout, because G 2 bars any allowance before the determination. The non-running is now
subject to M 2's two limits **in M 2's own words**, confined to the tolling-request limb: the
disability-application limb is deliberately untouched, because a member cannot be asked to hold a disability
application open on a clock.

**The cure could command two mandatory dates at once — S-4.** Store revision 43 replaced the nullity for a
determination noticed too late with a cure that makes it take effect on the first day it lawfully may. The
cure was confined to *"this sentence"*, and two sentences later G 2 says a determination shall take effect
*"in no event later than 120 days after the determination date"* — a mandatory limit with no stated
consequence, which the cure does not reach. On a late notice the two commands are directly opposed, and on one
of the two readings the determination takes effect **inside the member's reconsideration period**, which is
the defect the cure exists to remove. The outer limit now yields expressly where the Board gives its notice
late. **It is the Board's own lateness that moves the limit, so the member loses nothing and the Board gains
nothing.**

**A member could lose four years of credit because her extension turned on a duty that may not exist — S-5.**
Store revision 43's third predicate asked whether the Board *"has otherwise learned of facts from which it is
required by this subdivision to determine"* that a separation occurred. The only sentence in G 4 that
**requires** a determination is the member's own filing sentence — so where the Board learns from DHRM's
subsection J 2 report, from a payroll system or from a transfer record, the predicate is satisfied on one
reading and not on the other, and the text chose neither. On the narrow reading a member whose agency never
filed and who never knew the right existed keeps her old date, it passes, and subdivision 2 cuts her purchase
back to what her payments bought at standard cost — **while the Board was simultaneously under a duty to write
and tell her the date she must retire by.** It now reads *"has otherwise learned of the involuntary
separation"*, the formula the subdivision already uses twice, and the three competing knowledge standards
become one. **This also withdraws the unqualified claim in §7 item 74 that store revision 43 aligned the
predicate with the Board's learning: it did so where the member had filed, and not otherwise.**

### c. The cap I wrote cannot do the job I wrote it for, and the reviewer's own fix has the same defect

**S-2.** The rescission limb's cap read *"12 months after the date that would have applied under this
subdivision had the Board determined the separation on the date it learned of it."* The reviewer is right
twice: the counterfactual is **inert**, because the extension sentence's date is a function of the separation
date alone and the Board's knowledge is only a condition in its proviso; and in the ordinary case — a member
separated well before her final qualifying retirement date, where the extension sentence never operates —
**no date "would have applied under this subdivision" at all and the cap has no referent.** On the reading
that it is therefore inoperative the setter runs uncapped on a Board act, which is the failure mode §6.0-43
item 7 says the edit exists to prevent. On the competing reading the cap is a date already in the past at the
rescission, so her credit is restored and immediately re-stripped — **the cure defeating itself in the one
case it was drafted for.**

**Enacted: the cap now measures from the date of the involuntary separation, which always exists and which
the Board must determine anyway, and it is subordinated expressly to the rescission-based date so that it can
never produce a date the member cannot use.**

**And here is the part I have to say against the reviewer's fix, because it is the same point it made about
mine.** Its proposal — *"12 months after the date of the involuntary separation, and in no event earlier than
the first day of the second month following the month in which the Board rescinds"* — puts the floor at the
base, so the cap can **never bind**. Mine has the same property, and I enacted it knowing that: it removes
the undefined term and the member-stripping reading, and it leaves the policy where it belongs. **The bound
cannot sit on the retirement date at all.** A rescission can only happen when the Board learns, so the only
real bound is a limit on the rescission itself — and that strips the member whose agency never filed. **That
is §7 item 85, with both alternatives drafted, and it is the occupancy choice already in front of you at §7
item 71.**

### d. Eleven more, briefly

**M-1** — the 15-day member notice fell due fifteen days **before** the determination it must describe,
because a member's own filing is a date on which the Board "otherwise learns"; where the Board learns by that
filing the notice now runs from the determination. **M-4** — enactment 3 clause (i) preserves what *the
Board* must do, and **subsection N's duty is the Commonwealth's**; clause (i) now names it, so the
appropriation for a post-expiry settlement does not rest on the reach of a fiction. **M-5** — the
no-final-date limb settled on a date that can precede the date clause (iii) first applies, spending the
Board's 90-day redetermination period before the duty was known to exist; the valuation date stays where it
was and the clock now runs from the Board's determination. **M-6** — the tolling date-setter's own statement
duty had no time and no consequence, so a member whose date moved on her own reconsideration could be outside
her window with no extension and no deeming; the duty now has 15 days, and D 1's extension and G 4's two
deeming limbs both reach it. **M-7** — the rescission datum is now her date as it stood before the
determination was made *or, if later, before it took effect*, which is where her own reconsideration can move
it. **M-9 with m-4** — subdivision B 4 f's 24-month cap excepted exactly the **first day** of a limitation
year, so the Board could extend to a single day and the member had one day to pay; the exception now matches
the twelve months the extension sentence itself requires. **M-10** — subsection J 1 counted rescissions and
not the elections settled **because the Board erred**, each of which is an appropriation of up to $170,000
triggered by the Board's own default; the count is added. **m-1** — *"first"* acts. **m-3** — *"this
subdivision"* for *"subdivision f of this subdivision 4"*, which is shorter and exact. **m-5** — the
Chairmen's reinstatement notice now carries the same bar on identifying a member that the wait-list notice in
the same sentence already had.

### e. One finding I did not draft, with the reason

**m-6 — the residual limb of *"involuntary separation"* stays, and the reason is now stronger.**
**Corrected on [MOO-136](/MOO/issues/MOO-136), 12 October 2026.** § 2.2-3200 B is **open** — *"'Involuntary separation'
**includes, but is not limited to,** terminations and layoffs…"* — so the limb addresses a **non-empty**
residual class and not an empty set. Pass 15's quotation omitted those five words, the closed-set reading
recorded here is **withdrawn**, and **pass 14's P14-11 premise holds**. [MOO-136](/MOO/issues/MOO-136) re-opened the
section at source; the attribution is to it, not to pass 15. **I am keeping the limb on the merits**: the
residual catches an involuntary separation in which the member neither has employment terminate nor is placed
on leave without pay-layoff or equivalent status but ceases to occupy the position — § 51.1-155.1 D's
*"failure to obtain reappointment"*, already recorded at §7 item 8 and §6.2, and an officer whose position is
abolished. The limb and *"or equivalent status"* both stay exactly as drafted.

### f. Three corrections to the record, two of them mine

**§6.0-43 item 2** — *"caught by the two existing bars without amendment"* is now marked as right about a
first settlement and wrong about a second (S-1). **§7 item 74's** alignment claim is narrowed (S-5).
**`pass14-disposition` §3 point 3** — the capacity claim is **overstated on the face of subdivision D 2**:
what store revision 43's settlement sentence recovers is the **contingency**, because D 2's second sentence
keeps the settled amount charged and enactment 3 clause (ii) keeps it charged after expiry. On the figures as
they stand that is about one sixth of the charge, not the charge. **I move no figure and the restatement is
Fiscal's**; it is [MOO-134](/MOO/issues/MOO-134).

**And one correction to the reviewer, found by my own sweep:** its §3 table records `$170,000` as appearing
**once**. It appears **twice** — the ceiling in subdivision D 2 and the refusal notice store revision 44
restored in the same subdivision. Both name the same figure, both are untouched, and nothing in the pass turns
on it.

---

## 0.0000000000000000000000000000000000000000 Store revision 48 — [MOO-128](/MOO/issues/MOO-128)'s pass 15 drafted out. Four edits; the two serious findings it would not have introduced the bill with are cured.

**7 findings — 0 fatal, 3 serious, 3 moderate, 1 minor, plus a premise failure and 6 express null results.** **4 drafted out** (S-1, S-2, M-1, m-1), **1 to the Policy Director with three options drafted verbatim** (S-3, §7 item 88), **1 recorded as an interaction the MOO-101 restoration carries** (M-2), **1 corrected in the record** (M-3). **No figure moves. No designator is renumbered. No section is added.** Whole record, including the full subsection C as amended, the six ambiguities and the three S-3 options: [`moo128-pass15-disposition`](/MOO/issues/MOO-87#document-moo128-pass15-disposition). Sweep **§5.28**; ambiguities **§6.0-48**.

**a. The premise failure was a read/write race, not a lost edit.** Pass 15 reports store revision 46's edit is not in the store. It read document revision **51**, `91baade7`, 506,548 characters, 08:17:12.962Z; store revision 46 landed as document revision **52**, `ac8c1de6`, 517,909 characters, **08:28:06.936Z** — eleven minutes later, and both strings were present. **Its §0 was accurate as to what it read and wrong only as to the inference**, the opposite of pass 14's analogous discrepancy, which I could not resolve to any address. **The instruction that failed was mine:** a reviewer cannot check a revision id against §0.x, because §0.x for a revision is written in the same `PUT` as the edit it records. [MOO-137](/MOO/issues/MOO-137) names the id and character count to read and says to stop if they differ. **Six of the seven findings are not about that edit** — S-1, S-2, M-2, M-3 and m-1 are against **store revision 44's restoration of subsection C's zero bar and its re-keying of clause (vii)**, which no pass had reviewed.

**b. What the four edits cure.** **S-1:** the restored bar fires on the state of the Board's **record** (*"the amount determined under clause (ii) … is zero"*), not of the world, and nothing told the Board that an undeterminable amount is not a zero — so the same member was refused on one administrator's record and certified on another's. **Edit 1** replaces store revision 46's *relief* from determining with a **substituted determination**: the Board must determine, in place of an amount, that **no amount is specified**. The duty is discharged by performance rather than defeated by a canon, no *"amount determined"* exists for the bar to test, and the impossibility becomes a determination reviewable under M 2. **Edit 2** closes the construction route behind it, because on pass 15's **M-2** the only way to give the unreachable bar a class was to read *no value* as a zero. **S-2:** clause (vii) reads *"the least of"* two amounts and that member's second operand does not exist, so the **eligibility gate itself** was unevaluable on a second 30-day clock; **edit 3** supplies the operand in clause (vi)'s own idiom. **m-1:** **edit 4** adds subdivision J 1's residual limb.

**c. No figure moves, and edit 3 is what stops one moving.** [MOO-129](/MOO/issues/MOO-129) confirmed the trigger class at **0.0826 expected elections in 24 cells, 0.0259 admitted, 18.3965 unchanged**; the alternative reading is **18.3706**. **Pass 15 §4 asked Fiscal for a cell count that already exists**, so nothing is routed to Fiscal and nothing re-priced. **CONFIRMED IN STORE REVISION 51, and the claim stands.** [MOO-137](/MOO/issues/MOO-137)'s pass 16, finding **M-5**, challenged *"no figure moves"* for edit 3 on the ground that it converts an unevaluable gate into an admission for a recurring class. [MOO-144](/MOO/issues/MOO-144) answered it on the authorised basis: the **0.0259 admitted is inside 18.3965, not additional to it** (18.3964963814311 − 0.0258958319082 = 18.3706005495229 exactly), the engine returns an empty set for the class rather than a number and already certifies her **maximum purchasable amount**, and **edit 3 moves the certified amount on 0 of 5,552 cells**. **Two descriptors in M-5 do not reproduce and must not be carried forward:** the class buys **exactly 3.0 years**, not *"at or near the four-year maximum"* (the binding limb is (a), the subdivision B 2 entitlement), and the measured advance is **6 to 30 months**, not 47.

**d. Rebased once, and the label moved.** Drafted against store revision 46 (document revision 52); **store revision 47 landed under it** — [MOO-127](/MOO/issues/MOO-127)'s pass 15 of the other branch, seventeen edits in eleven provisions — taking 47, §5.27, §6.0-47 and §7 items to 87. So this is **48** on 47, sweep **§5.28**, ambiguities **§6.0-48**, item **88**. **Every anchor was re-verified present and unique in revision 47's body before I edited**; it touched neither subsection C's no-value sentence, clause (vii) nor subdivision J 1, and nothing of it is reversed or renumbered here. It also left the §0 byline reading *"store revision 46"*, which this revision corrects.


---

## Moved in store revision 50 — verbatim, from `bill-text-s8`
**Reason.** `bill-text-s8` arrived at store revision 50 with **1,866 characters** of headroom against the document store's 524,288-character ceiling, which is less than one revision's record costs. Seven sections are moved here **verbatim**, each replaced in `bill-text-s8` by a stub that restates its durable results and points here. **Nothing was rewritten and nothing was summarised away.** Every lettered label, numbered item, table row and check number is preserved as written. The §8 status notes for store revisions 44, 43, 41, 40 and 33 are the oldest five remaining in that file; the notes for store revisions 45 to 49 stay there.

### Moved in store revision 50 — §8 status note for store revision 44

> **STORE REVISION 44 — THE POLICY DIRECTOR'S [MOO-101](/MOO/issues/MOO-101) ANSWERS ENACTED, WITH
> [MOO-98](/MOO/issues/MOO-98)'s REASSIGNED FINDINGS AND [MOO-121](/MOO/issues/MOO-121)'s COUNSEL REVIEW.
> Seventeen substitutions in nine provisions, subsection C's zero bar and its refusal notice restored
> verbatim, no figure moved, no designator renumbered, no section added.**
>
> **Five of the Director's answers are in the text**: §7 item 34's five repairs (M 2 twice, D 7, D 2,
> D 6); clause (vii) re-keyed on answer **(B)**; MOO-98's S3 on **variant 1** as a new enactment 3 clause
> **(v)**; the word *"notice"* in enactment 3 clause (i); and the **parity clock** for D 2's refusal
> notice. **Item 35 is answered (a) — both deleted sentences are back** — and MOO-98's **M1** is enacted
> in **form (B)** with M 2's gateway widened to reach a failure to act. §7 items 34, 35 and 26 close.
>
> **MOO-121 returned 19 findings — 0 fatal, 5 serious, 8 moderate, 6 minor — against the strings, before
> they landed.** Disposition: **7 cured in the words enacted** (S1, S3, M1, M3, M4, M5, m1), **1 cured by
> the Director's answer** (S2 — subsection C has a notice again), **1 superseded on rebase** (M6), **6
> carried into new items 75 and 77 to 80** (S4, S5, M2, M7, M8, and the minors), and **4 null results
> recorded** (m2 to m5, each with its reason). **Nothing above moderate is both live and undrafted.**
>
> **No figure moves, and it is measured.** Section B moves the participating count by **zero members on
> both edits** — Fiscal's cellwise proof is 0 of 5,552 cells, 0.0000 expected elections — and edit 2 is
> withdrawn, so per-member quantity does not move either. **18.3965 participants, 78.1872 percent cap
> utilisation, $1,321,112 net trust cost.** D 7's release limb is what makes the cap figure **true**
> rather than an improvement on it.
>
> **Three edits were withdrawn on rebase and one of them was the one I had called this cut's fiscal
> event.** MOO-98's S1 was enacted in store revision 33, M5's refund limb more widely in store revision
> 36, and **MOO-98's M2 in store revision 41** — so the string I had drafted for it would have
> contradicted the landed text. **This cut therefore carries no fiscal event at all.**
>
> **Still not publishable, and the reasons are specific.** The seventeen strings have had **one** counsel
> pass (MOO-121) and the seven repairs made in response to it have had **none** — the widened M 2 gateway
> reaches every period in the section and is the widest of them. **§7 item 78 is live and serious**: a
> sentence store revision 41 enacted leaves a measured, admitted class buying up to **six times** the
> credit it needs, and 69 percent of that class is refused at the $170,000 ceiling as a result. The record
> is **§0.x** above and [`moo101-cut-record`](/MOO/issues/MOO-42#document-moo101-cut-record); §3 is moved
> to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2).

### Moved in store revision 50 — §8 status note for store revision 43

> **STORE REVISION 43 — [MOO-122](/MOO/issues/MOO-122)'S PASS 14 DRAFTED OUT. Fourteen edits in nine
> provisions. No figure moves, no designator is renumbered, no section is added, the bill title does not
> change, and `12`, `$3,000,000`, `$170,000` and the `[20]` percent contingency are untouched.**
>
> **20 findings — 0 fatal, 8 serious, 8 moderate, 4 minor — plus 12 express null results**, on the
> seventeen edits of store revision 39. The reviewer says the fatal count expressly and records that it
> could not make a case against the architecture. Disposition: **14 drafted out, 1 declined in part with
> reasons, 2 record corrections, 1 to the Director as a choice, 1 recorded with no text defect, 1 corrected
> against the reviewer's own fix direction.**
>
> **The one the reviewer would not have introduced the bill with is closed.** Store revision 39's F-18 cure
> deemed a Board **error** wherever the Board had not yet given a statement it had 15 days to give — so a
> member who paid up, filed and went one month early vested her credit at the pilot price and up to
> **$170,000** became payable under subsection N for an acceleration that never happened, with no
> discretion to refuse. The deeming is now confined to the case where the time for giving the statement
> **has expired**, which costs the never-told member nothing.
>
> **Two classes of reservation had no terminating event at all** — the clause (iii) member who never
> retires, whose credit vests, whose release D 7 bars and for whom the settlement sentence had no limb; and
> the member rescinded into a window that had already closed. One permanently charged election removes
> about **6 percent** of a $3,000,000 ceiling. Both are closed, by a new settlement sentence and by the
> date-setter in the rescission limb.
>
> **Still not publishable, and the reasons are specific.** **None of these fourteen edits has been attacked
> by anyone** — [MOO-127](/MOO/issues/MOO-127) is the bounded pass, and three of them (the new settlement
> sentence, the rescission date-setter and the G 2 timing cure) create or change the operation of money.
> **§7 items 71 to 74 are new**, item 73 records the one place in this revision where I reduced a
> protection a review had put in, and §7 items 31 to 70 are otherwise unchanged. **No money figure may be
> published** while [MOO-71](/MOO/issues/MOO-71) is open. Citation check **§5.24**; ambiguities
> **§6.0-43**; the record is **§0.x** above and
> [`pass14-disposition`](/MOO/issues/MOO-42#document-pass14-disposition).

### Moved in store revision 50 — §8 status note for store revision 41

> **STORE REVISION 41 — [MOO-119](/MOO/issues/MOO-119)'s PASS 13 DRAFTED OUT. Two edits, 484
> characters, and the first gives subsection C's quantity limit a value it did not have for a measured,
> admitted class. No figure moves, no designator is renumbered, no section is added.**
>
> **12 findings — 0 fatal, 4 serious, 4 moderate, 4 minor — and the pass does not recommend reversing
> store revision 38's deletion.** Disposition: **2 drafted out** (F-1 and F-11/F-12), **6 corrected in
> the record** (F-2, F-4, F-6, F-7, F-9, F-10), **1 corrected in a drafted option** (F-8, whose review
> limb leaves §7 item 34 item 5), and **2 carried into a new drafted item** (F-3 and F-5, which are
> §7 item 70). The one finding above moderate that is still live is **F-3**, and it is drafted in full.
>
> **Edit 1.** Where no number of months of creditable service would answer clause (ii) — a Plan 1 member
> under age 50, who is short of an **age** and not of service — **clause (ii) does not limit**, and the
> Board must state that in the certification in place of the amount. That is the reading
> `moo32_v6_engine.py` already measures, so **18.3965 admitted and MOO-71's 18 (range 9 to 30) are
> unmoved**; the alternative reading is 18.3706, about $4,000 of the $3,000,000 lower, and up to
> **$166,226 per member** turned on a word the bill did not supply.
>
> **Edit 2.** Clause (v) of *"eligible member"* now carries clause (ii)'s entitlement base in clause
> (ii)'s own words. ~~It can only exclude, never admit,~~ <u>[Store revision 46, on pass 14's **M-1**:
> no quantity of creditable service can postpone an unreduced retirement eligibility date, but the
> direction of effect of the base specification itself is not determinate on the face of the statute —
> open at §7 item 82.]</u> It closes the asymmetry that invited the
> inference that store revision 34's instruction did not reach the limb that is now the sole screen.
>
> **Still not publishable, and the reasons are specific.** These two edits have had **no counsel pass**
> — [MOO-123](/MOO/issues/MOO-123) is the bounded pass for them, and the first edit is a new operative
> sentence enacting a model convention into statute. **§7 item 70 (F-3) is live and serious**, and §7
> items 31 to 61 are otherwise unchanged. Citation check **§5.23**; ambiguities **§6.0-41**; the record
> is **§0.x** above and [`pass13-disposition`](/MOO/issues/MOO-87#document-pass13-disposition).

### Moved in store revision 50 — §8 status note for store revision 40

> **STORE REVISION 40 — [MOO-118](/MOO/issues/MOO-118)'S PASS 13 ANSWERED. Both subdivision G 4 edits
> survive; the residual disapplication is re-cut to name its three targets; §7 items 59, 60 and 61 are
> moved into §7's live list and item 60 gains two answers. One anchor, no figure moved, no designator
> renumbered, no section added.**
>
> **The two cures store revision 37 enacted have now had their pass.** 0 fatal, 3 serious, 2 moderate,
> 3 minor, and the reviewer's verdict that each edit *"is an improvement on the words it replaced."*
> Three findings are enacted as **one** re-cut clause (**F5**, **F4**, **F6**); two are declined with
> reasons (**F7**, **F8** — §6.0-40 items 3 and 4); and the three serious findings are **one question that
> is not drafting** — the death case's benefit **measure** — now §7 item 60's **(d)** and **(e)**.
>
> **Rebased once.** Store revision 39 ([MOO-117](/MOO/issues/MOO-117)'s pass 12) landed under this one and
> took the label 39, §5.21, §6.0-39 and five moves, so this is store revision **40** on store revision 39,
> sweep **§5.22**, ambiguities **§6.0-40**.
>
> **Still not publishable, and the reasons have changed.** Store revision 38's deletion is before
> [MOO-119](/MOO/issues/MOO-119). **This revision's own re-cut clause has had no pass** and it is wider
> than what it replaced, so it belongs in the next bounded pass rather than one of its own — and **if §7
> item 60 (d) is taken that clause comes out again**, so the pass should wait for the Director's answer.
>
> **Headroom, and §7 item 53 is now the standing precondition for every revision.** This revision arrived
> at **7,808** characters and had to move **four** more superseded records out to fit, after store
> revisions 38 and 39 together moved six. §5's and §6's remaining older records should move in one
> authorised pass of about 90,000 characters: a decision about the record, not the bill.

### Moved in store revision 50 — §8 status note for store revision 33

> **STORE REVISION 33 — [MOO-95](/MOO/issues/MOO-95)'s pass 9 drafted out. 24 edits, no figure moved,
> and no finding in the pass is fatal.** This is the adversarial and counsel review of revision 24's 37
> bill-text edits, and it is a **different pass** from [MOO-93](/MOO/issues/MOO-93)'s pass 9 above.
> **29 findings: 0 fatal, 9 serious, 12 moderate, 8 minor.** It recorded in terms that it looked for a
> finding that defeats the design or its stated basis and did not find one, and that *"the architecture
> survives this pass."* **24 are closed in the text, 1 needed no edit, 4 are the Director's.**
> `12`, `$3,000,000`, `$170,000` and `[20]` percent are untouched; no section is added; the title does
> not change.
>
> **Three of the edits change what the bill does.** A member whose election **the Board itself
> cancelled** under revision 24's own D 6 to-zero branch could have **her entire retirement allowance
> withheld**, for up to four months, a decade later, to make a determination that reduces nothing and
> refunds nothing — pass 9's S-1, and the finding with the worst headline-to-cost ratio in the package.
> G 2's 30-day notice floor and its new 120-day backstop could command **incompatible dates**, because
> nothing said when the notice must be given, and the Board's cheapest escape restored the unbounded
> deferral pass 8's F-2 was about — S-3; the anchor was also missing altogether in the
> involuntary-separation branch. And **the pilot price could expire out from under a member
> mid-contract**: enactment 3 preserved the wrong sentence of B 2 and revision 24's new clause (iv)
> restored the pricing paragraph without its carve-out, so a member still paying instalments after
> 1 July 2033 faced the **actuarial equivalent cost** — pass 8's F-10, re-created in a cleaner form.
>
> **One assurance I gave the Director was false and is corrected.** §6.0-24 said the retirement window
> has *"four bounded components, each bounded on the face of the text."* The fourth — D 1's extension by
> the days of the Board's own lateness — had **no cap at all**, so a statement never given left the
> window open for ever and the Commonwealth would settle a subsidy for a **negative** acceleration.
> Bounded in this revision at 12 months, which is the Director's own window length; **the numeral is
> mine and is §7 item 39**, with two tighter alternatives drafted.
>
> **Four findings are the Director's, each drafted in §7 and none enacted.** **Item 39** — the window's
> outer bound. **Item 40** — the over-cap reinstatement duty, which now carries four safeguards; the
> structural alternative is to make an unlawful release **void ab initio**, which never exceeds the cap
> but makes an innocent member's acceptance ultra vires, and that is a choice between two innocent
> members. **Item 41** — a member may hold a reservation for up to 24 months, pay nothing, walk away at
> no cost and file again, against central headroom of about **six reservations**; the cure is a new rule.
> **Item 42** — there is no anti-fraud provision, and any recovery provision collides with subsection F's
> no-clawback directive. **And I have withdrawn my own recommendation on item 33**: the case-decision
> sentence would import § 2.2-4021 B's **deemed-decision default**, so a member refused by the $170,000
> ceiling could obtain a reservation by the Board's silence against limitations D 2 calls
> *"self-executing."* The substitute is the Code's own § 51.1-124.11 formula, which came from the review.
>
> **Two things for the fiscal statement, neither a reprice.** Pass 9 reran the model from its own copy
> and reproduced every published figure, including $160,468 and the 5.4 percent refusal share; what it
> adds is cap utilisation on the reservation basis — **38 / 76 / 126 percent** at low / central / high
> take-up, so **$3,000,000 is 126 percent subscribed on the published high branch** and central headroom
> is **$723,758, about six reservations**. And B 4 f's new 24-month cap fixes for the first time the
> outer size of an **interest-free deferral**, worth of the order of $11,000 to $13,000 per deferring
> member, borne by the **trust** and outside the certified subsidy.
>
> **Not publishable, and the reasons have changed.** None of the 24 edits has been attacked by anyone;
> four items on the Director's list now change what the bill does rather than only how it reads; and
> **§ 2.2-4002 must not be described as cleared** — pass 9's M-12 establishes that the verification this
> document relied on answered a narrower question than §7 items 31 to 33 rest on.

### Moved in store revision 50 — §6.0-47 — ambiguities resolved in store revision 47

### 6.0-47 Ambiguities resolved in store revision 47

1. **S-1: the bar, not the restructure, and the bar is wider than the one offered.** The reviewer gave me
   two fixes and said (a) is cheaper and (b) better. I took **(a)** and widened it from *"under this
   subdivision"* to *"under this subdivision or under subdivision 1"*, so the rule is single-settlement
   across the whole of subsection G rather than inside G 4. **Reason for not taking (b):** moving the date
   into *"the earliest of"* as clause (d) is a restructure of the sentence three passes have certified, and
   it changes which of two settlement dates governs a member who later retires — a question nobody has
   been asked. **(b) is drafted in full at §7 item 84** and adopting it is a substitution, not a redraft.
   **Direction of effect of what I enacted: downward on what the Commonwealth pays, and it forecloses
   nothing.**
2. **S-2: the cap is now determinate and is, by construction, inert — and I am saying so rather than
   letting it read as a bound.** See §0.x c. A cap measured from any date before the rescission either
   binds and produces a date the member cannot use, or is subordinated to the rescission-based date and
   never binds. **There is no third possibility, and that is true of the reviewer's own proposed wording as
   much as of mine.** What the edit buys is a datum that always exists and the removal of the reading that
   re-strips the member. **What it does not buy is an occupancy bound, and §7 item 85 says so in terms.**
3. **S-3: the cap is confined to the tolling-request limb and the disability limb is untouched, on
   purpose.** M 2's two limits exist because a member can file requests; a disability application is not a
   tactic and a member cannot be asked to hold one open against a clock. Pass 12 and pass 13 certified the
   disability limb and I have not reopened it.
4. **S-4: reconciled by content, not by priority.** I did not write a priority rule between the two
   mandatory sentences, because a priority rule leaves one of them breached. The outer limit now **yields**
   where the Board's own notice is late, so on the facts that produce the conflict there is no longer a
   conflict. **The trigger is the Board's lateness, so the member cannot engineer it and the Board gains
   nothing by it.**
5. **M-6: the statement duty gets a time, which is what let the two existing cures reach it.** The tolling
   date-setter's statement had no deadline, so D 1's day-for-day extension had nothing to measure and
   G 4's deeming limbs had no expired period to point at. Giving it **15 days** — the period the
   definition already uses for the main statement — made both reachable without new machinery. The 15 days
   is mine; nobody chose it; it is recorded here as a choice and not as a repair.
6. **M-6 again: the deeming limbs are generalised from *"the statement"* to *"a statement or notice of the
   member's final qualifying retirement date required by"* the definition.** That is wider than the
   finding asked for and it is deliberate: the definition can state a member's date in three places, and a
   limb that names only one of them will be wrong again the next time a date-setter is added.
7. **m-6: no change, with the reason, at §0.x e.** The residual limb of *"involuntary separation"* stays.
8. **What I did not resolve by drafting.** The occupancy bound (item 85), the restructure (item 84), the
   edit-7 filing's tolling and its repetition (item 86), the acceptance freeze in the success case
   (item 87), and the three adjacents annotated into items 71, 72 and 73. **Every one of them moves either
   a count, an appropriation or a member's remedy, and none of them is mine.**

### Moved in store revision 50 — §5.27 — cross-reference sweep for store revision 47

### 5.27 Store revision 47 — the seventeen edits, chased in both directions

**Performed. No conforming amendment is required and none is made.** Full sweep, check by check, at
[`pass15-disposition`](/MOO/issues/MOO-42#document-pass15-disposition) §4.

**The durable results.**

1. **String verification before editing.** All **17** target strings present in the live body **exactly
   once** (document revision 52, `ac8c1de6`, 517,909 characters), and all **14** of pass 15's quoted strings
   likewise, after store revisions 44, 45 and 46 had landed under the review. **Nothing was addressed to
   superseded text.**
2. **No superseded string survives anywhere in the document.** Six checks — the deleted counterfactual, the
   deleted *"facts from which it is required"* predicate, *"subdivision f of this subdivision 4"*, the old
   deeming-limb formula, the old rescission datum and the unqualified outer limit — all **zero** occurrences
   in the bill text and zero in the commentary.
3. **Protected figures.** `$3,000,000` ×1; `$170,000` **×2**, both in subdivision D 2 and both untouched
   (pass 15's §3 table records ×1 and is corrected — see §0.x f); `[20]` percent ×1; the 12-month first
   sentence of *"final qualifying retirement date"* present and unaltered.
4. **No new sentence-ordinal citation is introduced.** `"last sentence"` **0** in the bill text — the one
   place I needed to point at the tolling date-setter's statement duty is keyed to its **content**, *"a date
   required by that definition upon the Board's action upon a request"*, not to its position; and
   `"second sentence"` remains **1**, the pre-existing reference in enactment 3 to subdivision B 2 of
   § 51.1-142.2. This is the correction pass 14's P14-17 made against me and it is honoured.
5. **S-4's cure points at exactly one sentence.** Only one sentence of G 2 *"requires notice to be given
   before the determination takes effect"* — the notice-floor sentence. The 60-day notice-timing sentence
   requires notice and not notice before effect; the allowance-bar sentence is about payment. **One
   referent, named descriptively.**
6. **Cross-references chased in both directions for every edit.** E1 into subdivision 1 and subsection N;
   E3 into subsection M 2 clauses (i) and (ii); E5 into G 2's second sentence, subsection A's mailing rule
   and M 2's 30 days; E6 into the two other knowledge formulas in G 4; E7 into the agency-notice sentence
   that follows it; E8 into subsection N and enactment 3 clauses (ii) to (v); E9 into the redetermination
   sentence and subdivision D 3; E10 and E11 into D 1's clauses (i) to (iii) and into G 4's deeming limbs;
   E13 into subdivision 2's effective-date machinery; E14 into B 4 f's extension sentence and clauses (i)
   to (iii); E15 into subsection J 1's terminal condition; E17 into the wait-list limb in the same
   sentence. **Nothing is stranded and no provision now points at a referent that does not exist.**
7. **Three sources I did not re-open and am not representing that I did.** § 2.2-3200 B (pass 15, for a
   no-change decision at m-6), § 2.2-4001 and § 2.2-4026 (pass 15, quoted at source for S-6, which is
   routed and not enacted), and art. X, § 11 (pass 15, verbatim at source). Each is attributed where it
   is used. **[MOO-136](/MOO/issues/MOO-136) has since re-opened § 2.2-3200 B at
   source** (12 October 2026): it reads *"includes, but is not limited to"*, the set is **open**, and the
   closed-set reading is withdrawn — see §6.5 of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8). The sentences above stand as a record of what was true when
   they were written, and the no-change decision at m-6 now rests on the merits.

### Moved in store revision 50 — §6.1 — the structure note

### 6.1 Structure

1. **Three Code locations now, not two.** The *price* lives in a new subdivision B 4 of
   § 51.1-142.2, where MOO-5 §11(2) said to put it. The *program machinery* lives in a new
   § 51.1-142.4. And revision 2 adds one sentence to **subdivision A 2 of § 51.1-155**, because that
   is where the early-retirement reduction actually lives. MOO-5 §9.2 named § 51.1-124.3 as the
   highest-risk conforming amendment and MOO-44 §5(a) establishes that it named the wrong section:
   § 51.1-124.3 needs nothing and § 51.1-155 needs one sentence.
2. **On X1 I took the targeted fix, not the clean one, and the reason matters.** MOO-44 offered two
   options: amend A 2's "30 years of service" to read "30 years of creditable service," which is
   probably a correction of a pre-existing drafting slip; or add a provision that purchased election
   credit counts for A 2. **I drafted the second, inside A 2 itself.** The global swap would change
   the reduction trigger for *every* member who has ever purchased *any* service under § 51.1-142.2
   — all eight B 1 categories, withdrawn-contribution restorations, sick leave, workers'
   compensation service — at ordinary prices, outside the pilot, outside the cap and outside
   everything MOO-31 and MOO-45 priced. That is an unpriced change of unknown size dressed as a
   technical correction, and a money committee is entitled to be told about it. The targeted sentence
   does exactly the pilot's work and nothing else. **MOO-52 has since settled it, and more
   favourably than either option assumed:** § 51.1-153 B 2 routes this cohort's benefit to
   subdivision A 1, which carries no reduction, so A 2 is not the operative provision for them at
   all. The sentence is belt-and-braces and costs nothing. Revision 2 ended this item with "if VRS
   does not, the sentence is the bill" — that was wrong, and it was wrong in the safe direction.
   MOO-52 also supplies a second reason the targeted form beats the global swap: bare "*N* years of
   service" used as a benefit threshold appears in exactly two places in Chapter 1, A 2 and
   **§ 51.1-138 C**, so a bill that amended A 2 alone would strand the identical defect one section
   away. Enactment 5 (iii) stays, because MOO-52 found no AG opinion, Virginia case or Board policy
   construing the word.
3. **I cut the second inserted phrase in B 3 and kept the first**, which is MOO-44 §4's explicit
   call and I accept it without reservation. The first phrase is necessary: without it a member
   inside a 24-month window who elects has two live prices and no rule. The second phrase was the
   direct cause of X3 — it removed the actuarial-equivalent price from election purchasers, which is
   what left the lesser-of ceiling measuring against nothing. Subdivision B 4 d already disapplies
   the 24-month limitation, so the second exception was redundant to the design and fatal to the
   price. One phrase deleted; revision 1's §6.1 item 2 and §7 item 4 are closed.
4. **"Standard cost" replaces every reference to "subdivision B 3" as the source of a price.** There
   were eight. MOO-44 §9 item 2 and its citation ledger establish that subsection B contains
   numbered subdivisions 1, 2 and 3 followed by three *undesignated* paragraphs, and that both
   pricing sentences sit in the first of those paragraphs — so "the amount required under subdivision
   3" was pointing at a ratio rule that states no amount. Rather than cite an undesignated paragraph
   eight times, or renumber the subsection and disturb § 51.1-142.3 A's reference to B 1, I defined
   the price counterfactually: *what the member would pay if subdivision 4 did not apply.* That is
   self-contained, it makes the comparison against **current law** rather than against a provision
   the act has just qualified, and it reads correctly in all eight places.
5. **No clawback anywhere, as directed, and revision 2 closes the one hole in it.** The structure:
   payment completes, then the credit posts, then the member retires, then the subsidy settles. A
   member who does not retire has already paid and already holds credit, so the only operation left
   is to re-value at ordinary prices, refund the excess and release the reservation. MOO-44's S7
   found the one place this broke: subsection F forbids withholding anything from a *retiree*, while
   G 2 directed the Board to reduce credit — which, once an allowance was in pay status, meant
   recomputing it downward, i.e. doing the thing F forbids. **G 2 now bars payment of any allowance
   until the determination is made and takes effect**, so nothing is ever overpaid and F's promise is
   kept literally. MOO-44 §9 item 9 is right that S7 and S6 were defects *in* the architecture, not
   *of* it.
6. **Pathway B is still out structurally rather than by label.** Clause (v) of "eligible member" now
   excludes anyone who has already reached his unreduced retirement eligibility date without the
   purchased credit. Adding Pathway B back later is still an amendment to one clause.
7. **The cap is still an admission rule, and three of its unguided delegations are now bounded.**
   MOO-44 §7's delegation table listed four determinations controlling admission and cost with no
   statutory standard. Three are now in the Code: the acceleration counterfactual (named assumption
   set and named decrement basis), the contingency amount (a flat percentage rather than "sufficient
   in the Board's judgment"), and the Board's processing lag (capped at three months, written
   reasons, and retroactive payment so the member bears no loss). The fourth — "complete
   application" — is bounded by a necessity test rather than a list, and is now backed by published
   procedures and express APA Article 5 review, which MOO-44 §7 says is the combination that makes
   it tolerable.
8. **Enactment devices unchanged in kind, extended in scope.** Delayed effective date (July 1,
   2029), four-year expiry (July 1, 2033) with a servicing tail, reenactment held against the first
   enactment only, and Enactment 5 in the partial form MOO-6 recommended. Revision 2 adds that the
   § 51.1-155 amendment **does not expire** — an election accepted on 30 June 2033 retires months
   later and needs A 2 to read the same way when it does — and adds the Board's A 2 construction to
   Enactment 5's report, so the answer to X1 is on the record before the 2028 vote whether or not
   Statutory Researcher gets it first.

9. **The deadline is a parameter, and I built it as two dates rather than one adjustable one.** MOO-46
   asked that the number of months be a single edit. The obvious way — "the first day of the *n*th
   month following the month in which the Board credits…" — fails at `[0]`, which is one of the five
   rungs on MOO-48's ladder, because there is no zeroth month following a month. So the window is
   anchored instead: "earliest qualifying retirement date" is a fixed point, and "final qualifying
   retirement date" is *"the first day of the month that is `[12]` months after"* it. At `[0]` that
   phrase resolves to the earliest date itself and reproduces revision 2 word for word; at `[6]`,
   `[12]`, `[18]` and `[24]` it reads naturally. **One numeral, five rungs, no other edit.** The
   anchoring has a second benefit: G 2, D 7 and subsection F can all name the deadline by its defined
   term rather than restating it, so no provision can drift out of step with the bracket.
10. **The member chooses the date inside the window; the Board does not.** Revision 2 had the Board
    fix the effective date, which was right when there was only one lawful date and the Board alone
    knew when the credit would post. With a window that allocation would be wrong twice over: it
    would give the Board a discretion with no statutory standard — exactly the defect MOO-44 §7's
    delegation table attacks — and it would make the member's retirement date someone else's
    decision. So the Board's duty is now informational and time-bound (state both dates in writing
    within 15 days of posting the credit, which is before the member resigns, preserving the
    protection MOO-44 S6 asked for) and the **choice is the member's**, exercised through the
    § 51.1-153 notice. The three-month processing extension survives, attached to the *final* date
    rather than to the member's chosen date, and so does the retroactive-payment guarantee.
11. **On the certified subsidy I chose "reserve dear, settle true" over the three alternatives, and
    it is the one judgment in revision 3 that a reviewer should attack first.** A window makes the
    valuation date indeterminate and something had to name it. Four options existed. *Value at the
    earliest date with no true-up*: determinate, but it reserves and pays for an acceleration that a
    member who retires at month 23 did not cause — and MOO-46 item 3 is explicit that a cap biting on
    an inflated number "denies veterans for no reason." *Value at the final date*: understates the
    reservation for the member who goes immediately, which is the expensive case, so the cap would
    not bind. *Value on a behavioural assumption inside the window*: re-imports exactly the
    unbounded-Board-judgment defect MOO-44 S3 found, and that term is 73 percent of the number.
    *Reserve at the earliest date and redetermine at the actual date, capped at the reservation*:
    determinate at admission, honest at settlement, and self-correcting in the direction that frees
    money for other veterans. I drafted the fourth. **It is more machinery than MOO-46 asked for, and
    I would rather be told to cut it than have the cap bite on a number nobody can compute.** If it
    is cut, the honest fallback is the first option with the overstatement disclosed in the fiscal
    statement, not the third.
12. **The redetermination is drafted so that it cannot become a clawback by accident.** The directive
    that there is no post-purchase debt is the oldest adopted constraint in this package, and a
    provision that recomputes a number after the member has retired is precisely where it would be
    lost. G 1 therefore says in terms that a redetermination creates no obligation of the member, of
    any beneficiary or of any employer, does not reduce credited service, and does not affect the
    retirement allowance. It moves money between the Commonwealth and the trust and touches nothing
    the member holds. The cap at "the amount last certified and reserved" also means it can only ever
    move in the member's and the program's favour.

### Moved in store revision 50 — §6.4 — where I deliberately did not go

### 6.4 Where I deliberately did not go

- **No appropriation, and no contingency-on-appropriation clause.** A Code bill does not appropriate,
  and MOO-6 records SFAC's written objection that such clauses "should be used sparingly or not used
  at all." MOO-44 §9 item 13 agrees the decision is right and adds the sting: declining a contingency
  clause does not relieve the act of naming an **obligor**. That is why subsection O is drafted and
  bracketed rather than omitted.
- **No New York-style residual-employer-cost sentence.** MOO-44 §9 item 13 confirms the omission is
  correct.
- **No S9 language.** See §4.
- **No savings claim, anywhere in the text.** K 2 collects replacement cost and K 3 must distinguish
  recorded retirement dates from estimated changes in timing. That is the most the record supports.
- **No veteran-preference recital or purpose clause.** Virginia bills rarely carry them, and a
  recital characterising the price as contribution recovery would hand the opposition MOO-35 R2.
- **I did not move the K 3 evaluation date, and I did not add a second evaluation.** At a 12- or
  24-month window the 1 December 2032 evaluation reports a cohort that has mostly not retired yet.
  The fix is a date change or one added sentence, but which one is right depends on the numeral MOO-48
  returns *and* on whether the Director wants an evaluation in front of the 2033 Session. Proposing
  rather than drafting: §7 item 5.
- **I did not change the 12-month payment period in subsection E to track the window.** It is
  independent — the window opens only after payment completes — and lengthening it would reopen the
  quantity-stability problem MOO-44 S5 closed. Recorded because a reader may expect the two periods
  to move together. They should not.
- **I did not add a minimum notice period to the employer.** A member in a long window may retire on
  30 days' notice to VRS and whatever notice their agency's policy requires, which is the same
  position as any other retiring state employee. Subsection J's backfill control is where agency
  planning lives, and adding a service-notice duty here would be a new obligation on the member that
  no cited document directs.
- **I did not adopt MOO-44 §5(c)'s middle treatment of G 4.** It is cheaper than the draft and closes
  real exposure, and MOO-44 is right that G 2 re-valuation creates no debt and so does not
  reintroduce MOO-15 F4. But it is a policy choice about whom the Commonwealth subsidises when no
  acceleration occurs, and MOO-44 says in terms that it is the Director's. **§7 item 8** (revision 3
  pointed to item 4 here; that was a stale pointer, corrected in revision 4).

---

---

## Moved verbatim: §7 item 22 — moved on [MOO-142](/MOO/issues/MOO-142) to make room for that issue's record corrections

*Moved out of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) §7 in store revision 51 for the
ceiling reason recorded at §0 of that revision. **Verbatim**, every lettered limb, sub-item and figure
preserved, so a reference of the form **§7 item 22** or **option (b) of item 22** resolves here. The item was
**answered on 12 October 2026 and nothing in it is open**; no operative bill text is involved.*

22. **ANSWERED 12 OCTOBER 2026 — OPTION (c), AND THE DRAFTING IS [MOO-87](/MOO/issues/MOO-87).**
    The Director's answer, relayed on [MOO-85](/MOO/issues/MOO-85): *"subsection C clause (ii) measured
    as of the filing date, with a bar on a purchase that does not advance the member's unreduced
    retirement eligibility date by at least a month,"* decided on [MOO-71](/MOO/issues/MOO-71) on
    MOO-78's figures. **Nothing is open here. The drafting is done and it is in the store**: MOO-87 drafted it as revision 22, which could not be written while this run held the checkout, and revision 24 **rebases it in** — see §0.x f. **Pass 9 ([MOO-93](/MOO/issues/MOO-93)) has now reviewed the two changed places and returned no fatal finding; store revision 32 closes three of its eleven findings in the text, records three as already closed, corrects four statements in the record, and routes the residuals to items 36, 37 and 38 — see §0.x of revision 32 and §5.14.** Pass 7's **F-9 is cured** by the deletion of C's early-completion sentence and **F-7 is superseded** by the deletion of the extension freeze; **F-22 is held, and §0.x f item 3 gives a reason that is new: C (i) carries the four-year statutory cap, so measuring it at the filing date would let the pilot breach a cap it cannot raise.**
    Three pass-7 findings travel with it rather than being drafted in revision 24, because fixing any of
    them against the completion-date measurement would collide with (c): **F-9** (C's third sentence
    hands the member the dial — an advised member asks for redetermination as of month 1 and is
    certified about 18 months where an unadvised member is certified about 8, so the programme's
    delivered quantity is allocated by access to a benefits adviser; (c) removes the lever because the
    measurement date no longer depends on payment timing), **F-21** (new, and the mirror of everything
    the card was about: clause (vi) *under*-admits by up to twelve months of gap, refusing a member
    whose application-date gap exceeds her maximum purchasable amount by less than the eligibility she
    will accrue before the completion date — so the bill simultaneously admitted members who would buy
    nothing and refused members who would buy their full entitlement, through one unstandardised date),
    and **F-22** (C (i) and C (iii) carry no measurement date at all, which is benign today and
    conspicuous beside a clause (ii) that has one). **The historical note below is retained record.**

    **RETAINED RECORD — NEW IN REVISION 18; PRICED ON [MOO-81](/MOO/issues/MOO-81); REFRAMED AND
    RE-RECOMMENDED IN STORE REVISION 23. On what date is the purchasable quantity measured, and who
    chooses that date?** `[An opening strikethrough marker stood here, unterminated, through`
    `revision 28, and is replaced with this marker in revision 29: strikethrough in this document is`
    `amendatory markup and not emphasis, and an unclosed one struck the rest of the item on any`
    `renderer that honours it. The same defect at item 31 is repaired the same way.]`
    From [MOO-77](/MOO/issues/MOO-77) F2. Subsection C (ii) measures the quantity *"as of the
    completion date stated in the Board's certification"*; subsection E makes that same date the
    **deadline for payment**, caps it at **12 months** after acceptance, and gives the Board **no floor
    and no standard** for choosing it. Clause (vi) of *"eligible member"* admits on the gap the member
    has at the **application** date. Every month between those two dates is a month the member no
    longer needs to buy — and, since revision 18's zero bar, a month closer to being refused outright.

    **Priced, central take-up** ([MOO-81](/MOO/issues/MOO-81) §1.2). The ladder's rung 0 reproduces the
    engine's own application-date quantity on all 5,328 cells, so the rungs run from the application
    date:

    | measurement date | accepted | refused at C (ii) = 0 | months bought, **accepted** cohort | per-member certified subsidy | aggregate trust cost PV | veterans reached by $3.0m |
    |---|---|---|---|---|---|---|
    | application date | 18.91 | 0.00 (0.0%) | 19.34 | $125,419 | $1,871,447 | **16.66** |
    | + 3 months | 17.17 | 1.73 (9.2%) | 17.66 | $122,526 | $1,659,866 | 15.54 |
    | + 6 months | 15.38 | 3.53 (18.7%) | 16.02 | $120,049 | $1,453,854 | 14.29 |
    | **+ 12 months — the statutory maximum, and the text as it stands** | **12.14** | **6.76 (35.8%)** | **12.77** | **$114,504** | **$1,097,874** | **11.81** |

    **Two corrections to what revision 18 told you, and the second reverses its conclusion.**

    - **The "8.20 months" headline is a mean over all applicants**, with the certified zeros averaged
      in at zero. A member who is actually **accepted** at the 12-month date buys **12.77** months,
      and the whole of the gap between 8.20 and 12.77 is the **35.8 percent who are refused**. So this
      is a **count** dial, not a price dial: across subsection E's full span the per-member subsidy
      moves by a factor of **1.10** and the accepted count by **1.56**.
    - **"In opposite directions" is withdrawn.** Revision 18's item 22 closed by saying the dial moves
      the per-member subsidy and the number of veterans reached in opposite directions, so that the
      choice was a trade. **Revision 18's own zero bar made that false.** Without the bar the count is
      identical at every rung and only the price falls — which was revision 16's world, and the
      reasoning was right there. With the bar, the late date refuses 6.76 members and **$442,842** of
      subsidy with them, so the count falls faster than the price. **The 12-month maximum is the worse
      end on both measures. There is no trade to balance.**

    **And my recommendation of (b) is withdrawn, because the pricing exposed a defect in my own
    sentence.** (b) was *"the earliest date … consistent with the method of payment the member
    elects."* A purchase payment agreement runs to subsection E's own 12-month ceiling, so **the
    standard binds nothing at all for an agreement payer** — on the modeller's 40 percent lump-sum
    share, which he marks as judgment with no source, that is three applicants in five. Worse than
    ineffective: it makes the size of a veteran's benefit turn on whether she can write a cheque. Two
    members identical in service, gap, grade and agency buy **17.66** and **12.77** months — **$8,022**
    of certified subsidy apart, with a materially different retirement date — because one had the cash.
    I will not recommend a sentence that does that. And it is worth saying that **the text already does
    a weaker version of the same thing**: subsection C's early-payment clause lets a member who pays
    early request redetermination as of the earlier date, which is the same lever, also keyed to cash.

    **Four ways to go. (a) and (b) as before, (c) carried forward, (d) new and recommended.**

    - **(a) Leave it.** The zero bar stops the absurd case and the Board's discretion stays. It is the
      only option that is principled on minimum-necessary-months — the member buys exactly the gap she
      still has on the day she finishes paying — and it is the worst option on reach, on count and on
      every per-member figure the sponsor documents quote. It also leaves **35.8 percent of applicants
      admitted and then refused**, which is a bad fact in a hearing whatever its arithmetic.
    - **(b) The payment-method standard. Withdrawn**, for the reason above. The sentence is unchanged
      and preserved in [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history)
      and in revision 18's record if you want it anyway.
    - **(c) Measure at the application date. THIS IS THE DIRECTOR'S ANSWER, AND IT IS DRAFTED AS THE
      FILING DATE OF THE COMPLETE APPLICATION.** The only option under which the member buys the
      quantity
      she was admitted on, and the only one that makes the zero bar a dead letter rather than a screen:
      clause (v) of *"eligible member"* already requires that the member **has not** reached her
      unreduced retirement eligibility date at application, so C (ii) measured there is always at least
      one month and **nobody admitted can be refused**. Best on reach (**16.66**) and dearest in
      aggregate. It re-opens the minimum-necessary-months question [MOO-49](/MOO/issues/MOO-49) settled
      (item 10): a member paying over twelve months earns twelve months of service while she pays, so
      she buys up to twelve months of **surplus** credit at the pilot price, which raises her allowance
      rather than only accelerating it. That objection is real. One drafting detail: C (ii)'s
      *"membership service the member will have earned by that date"* would have to become *"has
      earned"*, because the date is no longer in the future.
    - **(d) NEW — sever the measurement date from the payment deadline and fix it by statute.
      SUPERSEDED BY THE ANSWER, AND MY RECOMMENDATION OF IT IS WITHDRAWN**, because (c) severs the
      same coupling and fixes the numeral at zero rather than at three months. The one thing (d)
      bought that (c) does not is the bound on surplus credit — at three months the member earns at
      most three months of membership service while she pays, where at the filing date she can earn up
      to twelve — and that is **§7 item 10**, the minimum-necessary-months rule itself, which is still
      open and still the Director's. Retained below because it is the reasoning the answer was given
      against. One
      edit in subsection C and nothing at all in subsection E:

      > (ii) the number of months of creditable service the member needs in order to have reached his
      > unreduced retirement eligibility date as of ~~the completion date stated in the Board's
      > certification under subsection D~~ <u>the date **three** months after the date on which the
      > member filed his complete application</u>, taking account of the membership service the member
      > will have earned by that date;

      The completion date keeps its two proper jobs — the **deadline for payment** (still 12 months,
      subsection E untouched, payroll deduction unaffected) and the anchor for the anticipated earliest
      qualifying retirement date in clause (i) of *"certified subsidy"*, which is a payment-timing fact
      and belongs there. The measurement date becomes a fixed statutory date: **identical for both
      payment methods, knowable at certification, in nobody's discretion, and a single numeral you can
      move along the ladder above.** At three months it takes about four-fifths of (c)'s reach gain
      (**15.54** of 16.66), cuts the admitted-then-refused share from 35.8 percent to **9.2 percent**,
      and bounds the surplus credit (c) is criticised for at three months rather than twelve. **I
      recommend it.**

      **Three conforming consequences, all simplifications, and the third is the one that persuaded
      me. All three are now done — on (c) rather than on (d), in revision 24.** C's early-payment
      redetermination requirement stopped doing anything for clause (ii) and is **deleted** outright
      rather than cut back to clauses (i) and (iii) (pass 7's **F-9**, cured); C's extension sentence,
      which froze clause (ii) at the completion date last stated before an extension, became a dead
      letter and is **deleted** (pass 7's **F-7**, superseded); and **pass 5's finding that the § 415
      deferral defeats itself disappears structurally rather than by patch**, because the quantity no
      longer moves when the completion date moves. Revision 18 fixed that by hand with the extension
      sentence. The answer removes the coupling that caused it. All three were conforming rather than
      policy, and all three were drafted with the answer in the same revision.

    **One channel to decide with it, and it is the group a floor protects.** Of the 6.76 refusals at the
    statutory maximum, [MOO-81](/MOO/issues/MOO-81) §7 finds that **5.43 accrue** past the 30-year or
    Rule-of-90 leg and genuinely no longer need to buy, but **1.34 reach an age leg** — Plan 1 at 65 and
    Plan 2 at SSRA 67, each needing only five years of service, which every admitted member already has.
    A member admitted on a **service** gap whose 65th or 67th birthday falls inside the window has her
    purchasable amount extinguished **by the birthday**, holding the same service gap she applied with.
    (d) at three months shrinks that group to members with a birthday inside three months; (c) removes
    it. **The honest form of what the bar does to both groups is a minimum-acceleration test, and nobody
    has chosen one** — as drafted, the bar refuses a member whose acceleration is smaller than whatever
    lag the Board's chosen date happens to create. If that is the policy, the statute should say it
    rather than let it fall out of an administrative date. Drafted and **not** inserted, as a candidate
    for subsection C:

    > <u>The Board shall not accept an election unless the member's unreduced retirement eligibility
    > date, determined without the service credit to be purchased and as of the date the member filed
    > his complete application, is later than [six] months after that date.</u>

    **I will not turn any of this by drafting.** Every option moves money — the aggregate spans
    $1,097,874 to $1,871,447 at central take-up, all of it inside $3,000,000 — and the
    minimum-acceleration test is a new provision no cited document directs. Two things to have in front
    of you when you answer. The answer **moves the $170,000 ceiling's bite**: the ceiling refuses
    **2.25** members at the application-date rung and **0.33** at twelve months
    ([MOO-81](/MOO/issues/MOO-81) check C), so [MOO-85](/MOO/issues/MOO-85) cannot finish its re-walk
    until this is answered, and I have told them so. And **every per-member figure in the sponsor
    documents is a rung-0 figure**, so leaving the text at (a) makes them wrong in the member's favour
    by about 9 percent on the subsidy and by a third on the count.


---

**Note added in store revision 53.** A block headed *"Moved in store revision 52 — verbatim, from `bill-text-s8`"* was appended to this document earlier on 12 October 2026 while store revision 53 was being built, carrying store revision 49's §0 record, §5.30 and §6.0-50. **It is removed, and nothing is lost:** store revision 52 landed in the meantime and moved the whole retained §0, §5 and §6 record — including those three sections — to [`bill-text-s8-record-s0-s5-s6-rev2-51`](/MOO/issues/MOO-42#document-bill-text-s8-record-s0-s5-s6-rev2-51) on the Policy Director's answer to §7 item 53. That document is the authoritative copy; keeping a second one here, labelled with a move that store revision 52 performed differently, would have been a record defect. **The [MOO-144](/MOO/issues/MOO-144) confirmation added to §0.x c of store revision 48 above is kept** — that correction is store revision 53's and it stands.

---

## Moved in store revision 58 — §8.1 (the status notes for store revisions 50 back to 45) and 13 closed §7 items

### 8.1 Status at store revision 51 and earlier — retained

> **STORE REVISION 50 — [MOO-135](/MOO/issues/MOO-135)'s PASS 16 DRAFTED OUT. Sixteen edits in nine
> provisions. No figure moves, no designator is renumbered, no section is added or deleted, and the
> title does not change.** Pass 16 returned **0 fatal, 5 serious, 8 moderate, 7 minor** on store
> revision 47's seventeen edits, answered all eight of my questions, and delivered the timing map for
> all seventeen in place of a figure test. **Of the twelve findings routed to me, eleven are drafted
> out; one was already on the Director's list as §7 item 93 and is annotated rather than drafted twice.**
> The full record is [`pass16-disposition`](/MOO/issues/MOO-42#document-pass16-disposition); the
> narrative is §0.x, the sweep §5.30, the ambiguities §6.0-50.
>
> **What is in the text.** The Board's **silence** can no longer settle a certified subsidy for a member
> who never retires (R-5) — store revision 47's own widening had made one unanswered request a route to a
> full settlement, and that was my defect. Four new **floors** give a member a date she can use where a
> Board clock has run out (R-5, R-1, R-9), and **every one is a floor and not a setter**, so none can pull
> a member's date forward. The clause-(iii) determination now **exists as a duty**, with a deadline, a
> notice, a report line and a fallback clock (R-2). The clause I lifted out of subsection M 2, which
> reversed meaning in its new home, is **replaced with a direct statement that chooses no numeral**
> (R-3, R-8). Subdivision G 2's effective-date rule reaches an **absent** notice as well as a late one,
> with its referent tightened (R-4). And the **inert 12-month cap I enacted knowing it could never bind is
> deleted** (R-14).
>
> **The envelope, stated as a fact and not as an assurance**, because I have withdrawn that assurance
> twice: **12 months of base window, plus the three-month processing extension, plus at most 120 days of
> tolling, plus a day-for-day extension for the Board's own lateness capped at 12 months in the
> aggregate** (R-13, new in this revision; direction of effect on reservation occupancy **longer**;
> reversal at §6.0-50 item 5).
>
> **Not publishable.** The sixteen changed places have had **no adversarial pass of their own** —
> [MOO-140](/MOO/issues/MOO-140) is the bounded pass 17. **§7 item 89 is still a FATAL finding carded to
> the Director and enacted nowhere**, and items 90 to 99 are in the same position. Pass 16 **concedes no
> Va. Const. art. X, § 7 defect** and no document of ours may concede one. **Nothing here is cleared for
> external use.**

> **STORE REVISION 49 — [MOO-120](/MOO/issues/MOO-120)'s PASS 12 DRAFTED OUT. Five repairs to the
> words the Director's [MOO-64](/MOO/issues/MOO-64) answers put in; the fatal finding and the three
> serious ones are drafted and ENACTED NOWHERE. No figure moves, no designator is renumbered, no
> section is added, and the title does not change.**
>
> **What is in the text.** Item 54's valuation limb now carries the death branch's **recertification**
> sentence, so the subsidy settles on the credit the member actually bought rather than on the whole
> certification (M-1). The rescission sentence says *"restore or credit service credit as this
> subdivision provides,"* because a subdivision 3 determination reduces nothing (M-4). The item-48
> confining sentence's trigger date has a referent in the four places this section applies the
> definition without stating an as-of date (M-3). Enactment clause 3 clause (iii) carries the apparatus
> subsection J's third report line reads (m-1). Subsection F's lead example no longer asserts a deferral
> item 46 made conditional (m-2). **Record, all five FIND/READ pairs, the cross-reference sweep
> (§5.29), the ambiguities (§6.0-49) and the candidate text: [`moo120-pass12-disposition`](/MOO/issues/MOO-42#document-moo120-pass12-disposition).**
>
> **Not publishable, and the reason is the sharpest it has been. §7 item 89 is FATAL**: G 4's
> settlement bar still forbids, through its **D 7** limb, the settlement item 54 commands — so item 54
> is inoperative in every case it was written for. Two insertions cure it and they are not enacted.
> **Three serious findings are open with drafted text**: J 1's terminal date cannot arrive (item 90),
> the late-filed disability approval in the class § 51.1-156 H **compels** the Board to admit (item
> 91), and clause (iii) Board error having no rescission route (item 92). **Items 89 to 99 are
> with the Director on a question card.**
>
> **Two corrections that run against the review.** S-4's forced-effect mechanism does not operate —
> item 28's tolling reaches the 120-day bound. And **§ 51.1-156 H is mandatory in exactly the class item
> 49(i) excludes**; the reviewer quoted its permissive first sentence only, and my earlier record was
> right. Both are in §4 of the companion document, with the citation quoted in full.
>
> **The five edits of this revision have had no adversarial pass of their own.** That is the next review
> and it is not scheduled.

> **STORE REVISION 48 — [MOO-128](/MOO/issues/MOO-128)'s PASS 15 DRAFTED OUT. Four edits, and the two
> serious findings the reviewer would not have introduced the bill with are cured. No figure moves, no
> designator is renumbered, no section is added.** **This is a different pass 15 from store revision
> 47's**, which is [MOO-127](/MOO/issues/MOO-127)'s on the other branch; this one is bounded to
> subsection C.
>
> **7 findings — 0 fatal, 3 serious, 3 moderate, 1 minor, plus a premise failure and 6 express null
> results.** **4 drafted out** (S-1, S-2, M-1, m-1), **1 to the Director with three options drafted
> verbatim** (S-3, §7 item 88), **1 recorded** (M-2), **1 corrected in the record** (M-3). Record:
> [`moo128-pass15-disposition`](/MOO/issues/MOO-87#document-moo128-pass15-disposition).
>
> **The two that matter.** Subsection C's restored zero bar fires on the state of the Board's **record**,
> not of the world, so the same member was refused on one administrator's record and certified on
> another's. **Edit 1** makes the impossibility a **substituted determination** — *"no amount is
> specified"* — so the duty is discharged by performance and the determination is reviewable under M 2;
> **edit 2** states that such a determination **is not** a determination of zero. **Edit 3** supplies
> clause (vii)'s missing second operand, store revision 44 having left the **eligibility gate itself**
> unevaluable on a second 30-day clock — the finding pass 15 said it would not introduce the bill with.
>
> **The premise failure was a read/write race.** Pass 15 read document revision **51** at 08:17:12.962Z;
> store revision 46 landed as revision **52** at **08:28:06.936Z**, both strings present. **The
> instruction that failed was mine** — §0.x is written in the same `PUT` as its own edit, so it cannot
> check the read. **18.3965 admitted is unmoved** and the alternative reading of clause (vii) is 18.3706.
>
> **Still not publishable.** No counsel pass on these four — [MOO-137](/MOO/issues/MOO-137) is the
> bounded one, and §6.0-48 item 1 names the choice I most want it to test. **§7 item 88 is live and
> serious and it is the Director's.** `PUBLISH-NOTE.md` and `VERSION-fragment-bill-text.md` still repeat
> the wrong store fact that the latest revision is 21, which is [MOO-97](/MOO/issues/MOO-97)'s.
>
> **ANNOTATED IN STORE REVISION 53 — [MOO-137](/MOO/issues/MOO-137)'s pass 16 ran, and two statements
> above need correcting.** (1) *"No figure moves"* was **unsupported for edit 3**, which converts an
> unevaluable gate into an admission for a recurring class rather than for one applicant;
> **[MOO-144](/MOO/issues/MOO-144) confirms the claim** — the authorised 18.3965 already includes that
> class, 0.0259 of it, exactly 18.3706 without it, and edit 3 moves the certified amount on 0 of 5,552
> cells. **The claim stands as confirmed, not as asserted.** (2) **§6.0-48 item 1's choice was tested and
> it holds** — substituted performance does discharge the duty on its own — **but edit 1 discharged it out
> of the only period the section requires (S-1), and store revision 53 gives it its own 30-day period.**
> Edit 2's boundary ran on the record only (M-3) and now runs on the world too. **Pass 16's S-2 — that
> none of these four edits had landed — was already false when it was written**; see the store revision 53
> note above for the two document revision ids and the timestamps.


> **STORE REVISION 47 — [MOO-127](/MOO/issues/MOO-127)'s PASS 15 DRAFTED OUT. Seventeen edits in eleven
> provisions. No figure moves, no designator is renumbered, no section is added, the bill title does not
> change.**
>
> **25 findings — 0 fatal, 6 serious, 11 moderate, 8 minor, plus 15 express null results.** **17 drafted
> out**, **1 no change with the reason** (m-6), **3 corrected in the record**, **4 with the Director** as
> §7 items **84 to 87** with addenda to items **71, 72 and 73**. **Whole record:**
> [`pass15-disposition`](/MOO/issues/MOO-42#document-pass15-disposition). Sweep **§5.27**; ambiguities
> **§6.0-47**; record **§0.x** above.
>
> **The one that mattered.** Store revision 43's settlement sentence for the member who never retires sat
> outside G 4's *"the earliest of"* sentence with no exclusion from it, and **subsection N keys its duty to
> *"upon the settlement"***. So the same certified subsidy could settle twice — on her passed date and
> again on her death — and the Commonwealth could pay up to **$170,000 twice on one election**. **It is
> barred now**, across subsection G and not only inside G 4. §6.0-43 item 2's claim that the sentence was
> "caught by the two existing bars without amendment" is right about a first settlement and **wrong about a
> second**, and is corrected.
>
> **Three more that cost a real person real money, all closed.** The **Board's** clocks stopped with no cap
> while the member's identical tolling was capped at 120 days and expressly excluded the Board's own
> overrun (S-3). The cure for a late-noticed determination could command two mandatory dates at once, on
> one reading taking effect **inside** the member's reconsideration period (S-4). And a member whose agency
> never filed could lose four years of credit because her extension turned on whether the Board was
> *"required by this subdivision to determine"* a separation — a duty that may not exist on those facts
> (S-5).
>
> **One thing I have to say about my own cap, and about the reviewer's fix for it.** The rescission limb's
> 12-month cap had **no referent in the ordinary case**. It now measures from the separation date and is
> subordinated to the rescission-based date, so no reading re-strips a member. **It is therefore inert, by
> construction, and so is the wording the reviewer proposed** — a cap measured from any date before the
> rescission either binds and names a date in the past or never binds. **The occupancy bound cannot sit on
> the retirement date**, and §7 item 85 puts the real choice to the Director rather than hiding it in a
> cap that reads like one.
>
> **Two for the fiscal statement, neither a reprice.** `pass14-disposition` §3 point 3's capacity claim is
> **overstated on the face of subdivision D 2**: what the settlement sentence recovers is the
> **contingency**, because D 2's second sentence keeps the settled amount charged and enactment 3 clause
> (ii) keeps it charged after expiry — about one sixth of the charge, not the charge
> ([MOO-134](/MOO/issues/MOO-134)). And the acceptance freeze **lifts if the member fails and is permanent
> if she succeeds** (§7 item 87).
>
> **Still not publishable.** None of these seventeen places has been attacked by anyone —
> [MOO-135](/MOO/issues/MOO-135) is the bounded pass and this draft goes nowhere until it reports. Four
> questions are with the Director. **And one standing warning in this banner is retired, because I have
> now checked it rather than repeating it:** `PUBLISH-NOTE.md` and `VERSION-fragment-bill-text.md` in the
> working tree **no longer state a store revision other than 47** — the [MOO-97](/MOO/issues/MOO-97)
> "latest revision is 21" staleness was true when it was raised and both files have since been rewritten,
> this refresh included. **The reason not to publish from them is the four above, not a stale number.**

> **STORE REVISION 46 — [MOO-123](/MOO/issues/MOO-123)'s PASS 14 DRAFTED OUT. One edit, 88
> characters, relieving a mandatory duty the Board could not perform. No figure moves, no designator is
> renumbered, no section is added.**
>
> **11 findings — 0 fatal, 3 serious, 5 moderate, 3 minor.** **1 drafted out** (S-3, with m-2 in the
> same words), **1 answered against the reviewer on the evidence** (S-1), **2 already closed in the
> text** (S-2, m-1), **1 closed by store revision 42 under me** (Q1's contingency residual), **1 mostly
> closed by store revision 44 under me, with the residue drafted** (M-3), **3 carried into drafted
> items** (§7 items 81, 82, 83 and the item 70 addendum), and **2 corrected in the
> record** (M-1, M-4). **Whole record:**
> [`moo123-pass14-disposition`](/MOO/issues/MOO-87#document-moo123-pass14-disposition).
>
> **The edit.** Subsection C's no-limit sentence said clause (ii) does not limit and displaced the
> Board's duty to **state** the amount. It did not displace the second sentence's duty to **determine**
> it, so for the trigger class the Board was under an unqualified 30-day mandatory duty to determine an
> amount whose solution set the same sentence declares empty — and store revision 44's new subsection J
> reporting sentence had just made that failure reportable in every case. It now reads *"…does not limit
> the service credit the member may purchase, **the Board is not required to determine an amount under
> that clause**, and the Board shall so state in that certification in place of the amount **that clause
> would otherwise require to be stated**."*
>
> **Read §0.x before this file is relied on for the store's state.** Pass 14's most serious finding is
> that neither of store revision 41's edits is in this document. **Both are, and were when the review
> landed** — verified by string count at document revision 47, `41a3bbd9`, 524,265 characters. Its Q1 to
> Q3 were run against the commission's quotation, which was accurate; **Q4 and Q5 were run against a body
> I cannot resolve to any address and are both re-run** in the companion record.
>
> **Four things are with the Director and none of them is drafted out.** §7 item 81 — the statement
> duty's *or else*, 16 characters. §7 item 82 — the base on which this bill measures service, the
> same question as §7 item 43, on which [MOO-124](/MOO/issues/MOO-124) has now reported in a direction
> that cuts against pass 14's reading of it; five options, recommendation (b), nothing enacted. §7 item
> 83 — the member whose cap a Board error raises and who has no way to take it. And §7 item 70's
> addendum — four routes to a zero-credit election, four options, recommendation (d).
>
> **One disclosure for the risk section rather than for here.** The no-limit sentence's whole operative
> scope is set by **clause (vi)** of *"eligible member"*, not by clause (v): at the authorised one-month
> roll the class is 0.0826 participants and 0.0259 admitted; at a roll of zero it is exactly empty; at
> twelve months it is 1.2144 and 0.2069, and 24.0167 admitted — still inside
> [MOO-71](/MOO/issues/MOO-71)'s authorised 18 (range 9 to 30). **Pass 14's figures, re-run on the
> authorised basis; sensitivities, not a re-pricing**, and §7 item 35's protection rule names clauses
> (vi) to (viii) for that reason.
>
> **Still not publishable.** This edit has had **no counsel pass** — [MOO-128](/MOO/issues/MOO-128) is
> the bounded one and this draft goes nowhere until it reports. `PUBLISH-NOTE.md` and
> `VERSION-fragment-bill-text.md` in the working tree still repeat the wrong store fact that the latest
> revision is 21, which is [MOO-97](/MOO/issues/MOO-97)'s, and nothing should be published from them
> until it is fixed.

> **STORE REVISION 45 — §7 ITEM 60 ANSWERED BY THE POLICY DIRECTOR. Answer (d) is enacted, so the
> death branch names the benefit it orders paid; [MOO-118](/MOO/issues/MOO-118)'s F8 is answered with one
> notice duty; 972 characters of deeming and disapplication come out. No figure moves, no designator is
> renumbered, no section is added, and the title does not change.**
>
> **What the bill now says in the death case.** The Board credits the purchased service credit and pays
> the benefit; **the benefit is the one this chapter provides on the death of a member in service,
> computed on the credit credited**; and the estate, the person entitled to the benefit and the paying
> employer get written notice of the credit, the benefit and its computation, any refund and the Board's
> reasons within 30 days, reviewable under subsection M. **The four disapplications I wrote in store
> revisions 37 and 40 are reversed by this one, deliberately** — with no deemed retirement there is no
> requirement of retirement to switch off (§6.0-45 item 2).
>
> **Still not publishable, and the reason is sharper than last revision's.** (d) names the measure and
> **does not displace § 51.1-165 C 1**, which routes every filed-notice death to § 51.1-163 and a refund
> of the member's own contributions. **§7 item 60 (a) is the only drafted answer that reaches that class
> and it is not enacted** — put back to the Director as a fresh card on
> [MOO-97](/MOO/issues/MOO-97). The two new sentences have had **no counsel pass**
> ([MOO-126](/MOO/issues/MOO-126) is the bounded pass), store revision 41's two edits are before
> [MOO-123](/MOO/issues/MOO-123), and **§7 item 70 (pass 13's F-3) is live and serious**. Citation check
> **§5.25**; ambiguities **§6.0-45**; record **§0.x** above.

> **STORE REVISIONS 44, 43, 41, 40 and 33 — their §8 status notes are moved verbatim** to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2) in store revision 50, under the heading *"Moved in store revision 50"*, with every figure, link and caveat preserved. **Reason:** this revision arrived at 1,866 characters of headroom against the store's 524,288-character ceiling, which is less than one revision's record costs. **Their durable results, so this file does not lose them:** store revision 44 enacted the Director's MOO-101 answers (seventeen substitutions, five decisions); store revision 43 drafted out MOO-122's pass 14 in fourteen edits and closed P14-1, the appropriation trigger that fired on the Board's lawful silence; store revision 41 drafted out MOO-119's pass 13 in two edits and enacted subsection C's no-limit sentence; store revision 40 answered MOO-118's pass 13 on both G 4 edits; and store revision 33 drafted out MOO-95's pass 9 in 24 edits. **The §8 status note for store revision 45 is now the oldest in this file**, and the notes for store revisions 46 to 50 are above.

> **STORE REVISIONS 39, 38, 37, 36 and 34 — their §8 status notes are moved verbatim** to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2), under
> the heading *"Moved in store revision 45"*, with every figure, link and caveat preserved. The note
> for store revision 33 is retained below as the oldest one in this file, and the note for every store
> revision later than 39 is above. **Reason:** this revision arrived at 15,624 characters of
> headroom and its record did not fit, and the first retained-record document is 936 characters from
> the store's 524,288-character ceiling. **§7 item 53 is now a three-document problem** — the bill file,
> volume 1 and volume 2 — and moving records is the standing precondition for every further revision.

**§8's status notes for revision 32 and older are now in [`bill-text-s8-revision-history`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history)**, moved verbatim in store revision 37 under the heading `# Moved in store revision 37 — §8's status notes for revision 32 and older`. **§8 above retains the notes for store revisions 37, 36, 35, 34 and 33.** Same method and same reason as the moves in store revisions 32, 33, 34 and 35, which **§7 item 53** records: this file had **8,473** characters of headroom on arrival and store revision 37 is a record of a counsel review. Nothing was rewritten and nothing was summarised away, and the notes survive verbatim in this document's store revisions 21 through 36. **One paragraph moved out was also false where it stood** — the paragraph beginning *"Per the Done checklist"* certifies that § 51.1-155 *"is newly amended"* and reports a cross-reference sweep on that basis; **revision 21 dropped that conforming amendment on the Director's direction**, so the act amends one section and adds one. The current statement is **§5.11** and the store revision 21 note retained above.

**This is an internal working draft, not a Division of Legislative Services bill, and it has not
been reviewed by counsel.**


### §7 item 1 — moved from the live list in store revision 58

1. **X2 — who pays the certified subsidy? CLOSED AND DRAFTED IN REVISION 9. Nothing is open here.**
   The Director answered **Alternative A — the Commonwealth pays** on the question card of 11 October
   2026. Subsection O is now operative text, the `[X2 — OBLIGOR …]` instruction block is deleted, and
   D 1, D 2, D 3 and subsection L all stand, so the cap machinery describes money that actually
   moves (§0.0000000a). The reasoning below is retained as the record of the choice, **not** as a
   live question, so that a reviewer does not re-open it against the 13 January 2027 prefile date.
   **Prior record:** MOO-46 item 1 may already have answered this and I was not going to assume it. "The aggregate figure stays $3,000,000, and its meaning changes. It is
   the appropriation, not a forecast" reads as a choice of **Alternative A** — the Commonwealth pays
   from an appropriation — because a figure cannot be an appropriation if the trust absorbs the cost
   through the employer contribution rate. If that is what you meant, say so and I will unbracket
   subsection O and this question closes. If it was a statement about the fiscal statement rather
   than about the obligor, the question stands as put in revision 2: The act defines it, certifies it, obtains DPB's
   confirmation, reserves it, caps it, settles it and releases it — and no provision names an
   obligor, a fund, a transfer or an appropriation. "Settled" currently has no operative consequence
   beyond vesting the credit. Two legitimate bills:
   - **Alternative A (drafted as subsection O):** on settlement the Commonwealth pays the certified
     subsidy to the retirement system from an appropriation made for that purpose, and the Board
     accounts for it separately. This is what makes D 3's DPB confirmation confirm something, and
     what makes the $3,000,000 a real limit.
   - **Alternative B:** the trust absorbs the cost through the ordinary employer contribution rate.
     That is a real bill and art. X, § 11 guarantees the trust is made whole — but then the cap, the
     reservation, the DPB confirmation and the kill switch are decorative, and MOO-44 is right that
     leaving them in would mislead the scorer. Choosing B means **deleting** subdivisions D 2 and
     D 3, subsection L, and the reservation words in D 1.
   **This is the one decision the draft cannot survive without.** Under Alternative B the honest
   fiscal statement says the cost reaches the employer contribution rate that every state agency
   pays, which is the hostile sentence MOO-35 §7 simulated.

### §7 item 2 — moved from the live list in store revision 58

2. **The window numeral — DECIDED AND DRAFTED IN REVISION 21 AT 12 MONTHS. Nothing is open here.**
   The Director answered **12 months — $1,411,988** on the question card of 12 October 2026, against
   the authorised ladder (0 months $1,661,819 · 6 $1,539,576 · 12 $1,411,988 · 18 $1,279,235 · 24
   $1,141,496). *"Final qualifying retirement date"* now reads *"the date that is 12 months after
   the member's earliest qualifying retirement date"* and the bracket is gone. **Three things follow
   and two of them are not mine.** First, **every money figure in the package was priced at the
   0-month rung** — `package-v11-corrections` §4, MOO-48's own "rung 1 not rung 0 as drafted" — so
   the authorised set moves to the 12-month column and the $170,000 ceiling has to be re-walked on
   the distribution at that rung (item 3, and [MOO-85](/MOO/issues/MOO-85)). Second, the real outer
   bound is **15 months**, because of the three-month extension in item 25. Third, pass 4's **F3 is
   not affected** — revision 12 closed it against the Board's own written statement of the window
   rather than against the retirement date, so it works identically at every rung, and my revision-11
   claim that F3 and the numeral were "one question, not two" was corrected in revision 12 and is
   corrected again here. **The reasoning below is retained as the record of the choice, not as a live
   question.** One edit, in the definition of
   "final qualifying retirement date," and nothing else in the bill moves with it. You asked me to
   tell you whether a longer deadline breaks anything structural. **The answer is no, and your
   reading of G 2 is right** — G 2 re-values the member's own payments at ordinary prices and bills
   nobody, so it works identically at 0 and at 24 months. Three *other* provisions did break and
   revision 3 fixes all three (D 1's notice, D 3's reservation life, K 1's reporting tail — §0). The
   only thing I cannot fix by drafting is that **both money figures were priced on the 0-month
   design**, which is items 3 and 9. Two further things you should have before you pick off the
   ladder. First, a longer window does **not** reopen Pathway A: clause (vii) tests eligibility at
   crediting, and clause (vi) at application; neither is keyed to retirement, so a 24-month window
   admits exactly the same members as a 0-month one. ` [Corrected in revision 18 —` [MOO-77](/MOO/issues/MOO-77) `F10.]` Second, a longer window weakens the political story rather than the statute — a member who
   pays, posts credit, and then works two more years is harder to describe as a workforce-turnover
   measure, and subsection J's backfill control (item 7) is doing less work the longer the window
   runs. That is a presentational cost, not a drafting defect, and it is the one argument I can see
   for a short window that the model will not show you.

   **Revision 12 removes one thing from this item and adds another.** Removed: I told you in
   revision 11 that pass 4's fatal F3 and this numeral were *"one question, not two."* **They are
   two, and F3 is now drafted and closed at every rung** (§0.0000000000a) — so nothing fatal is
   waiting on your answer here. Added, and it is a genuine point for a short window that I did not
   have before: § 51.1-153 E requires the effective date of retirement to be **after the member's
   last day of service**, so at the zero rung the member must set a last day of service against a
   crediting date they cannot yet know. Revision 12 cures that by letting the member fix the
   crediting date (§0.0000000000b), **but the cure is administration the member has to get right, and
   at 6 months or more it is a backstop nobody uses.** The numeral is still yours; it is no longer
   holding a fatal finding hostage.

### §7 item 7 — moved from the live list in store revision 58

7. **J — backfill control. DECIDED: NONE. DRAFTED AND CLOSED IN REVISION 10. Nothing is open here.**
   The Director answered *"no backfill provision"* on the question card of 11 October 2026. Subsection
   J is deleted, K through O are renumbered up one letter, every cross-reference is chased, and the
   bill title loses *"state agency position vacancies"* — §0.00000000. **Two consequences for
   [Editor](/MOO/agents/editor), flagged rather than left to be discovered:** this removes the bill's
   only workforce-cost control, so the workforce-turnover argument rests on member behaviour rather
   than on a provision, and **four of the ten sponsor documents currently assert a backfill
   provision**; and the bill now makes no reference to Title 23.1 at all, so the covered-institution
   objection has nothing left to attach to. **The record of the three alternatives is retained
   below for the file only.** Alternative 1 (fill two of
   three) has the Michigan/Missouri/Iowa analogue; Alternative 3 (central approval) is the most
   administrable and the most intrusive; Alternative 2 is the payroll cap. All three now carry the
   public-safety floor and the § 23.1-1021 carve-out.

### §7 item 8 — moved from the live list in store revision 58

8. **G 4 — DECIDED: the middle treatment. DRAFTED AND CLOSED IN REVISION 10.** The Director
   answered *"middle"* on 11 October 2026 and G 4 now reads that way: death and Board error vest at
   the pilot price; disability vests and is recertified; and involuntary separation vests **only** if
   the member retires in a qualifying retirement within 90 days of it, failing which subdivision 2's
   ordinary re-valuation applies. **Three things about the drafting you should know.** (a) The old
   12-month rehire rule is **deleted**, because it existed to police a vesting carve-out that no
   longer exists — MOO-44 S10's arbitrage is closed by removing the prize rather than by detecting
   the trick. (b) **The hard edge, stated rather than buried:** a member separated *before* the
   earliest qualifying retirement date cannot retire in a qualifying retirement at all, so the
   90-day door is shut for them and subdivision 2 applies. That is the middle treatment working as
   intended — the Commonwealth does not pay an acceleration subsidy where no acceleration occurred —
   and the member is made whole in money, because subdivision 2 refunds their own payments and bills
   nobody. It is the one case where the middle treatment is harsher than full vesting on a member
   who did nothing wrong. (c) For part of this population the door is wider than it looks: a member
   with 20 or more years who is involuntarily separated may already retire unreduced at age 50 under
   § 51.1-155.1, independent of any purchase. **The question as it was put, retained as the
   record:**
   **The question as it was put, retained as the record:** keep full vesting on death, disability and
   involuntary separation, or take MOO-44's middle treatment? Revision 2 keeps full vesting and adds the anti-arbitrage rule, the Board-error
   carve-out and disability recertification. MOO-44 §5(c) proposes instead: vest on death; vest on
   disability but recertify; and **apply G 2 re-valuation to involuntary separation** unless the
   member retires within 90 days of it. Acceleration is 73 percent of the certified subsidy, and in
   every G 4 case no acceleration occurs, so full vesting over-pays by roughly $38,000 per case on
   MOO-31's central figures. Two things sharpen the choice. MOO-44 establishes that G 2 is not a
   clawback — it refunds the member's own money and bills nobody — so MOO-15 F4 does not bar it.

   **And the second argument, corrected in revision 4 — you should have the real population before
   you choose.** Revision 3 said here that a member with 20 or more years who is involuntarily
   separated "may already retire unreduced at age 50 under § 51.1-155.1," so that for part of the
   G 4 involuntary-separation population the subsidy buys an acceleration the Code already delivered. **That was built
   on a misread row** ([MOO-54](/MOO/issues/MOO-54) §6.1; §5.2 of this document is now corrected). The
   argument survives and is in one respect *stronger* — § 51.1-155.1 A confers the **full allowance
   under subdivision A 1**, not merely relief from the A 2 reduction — but the overlap is far narrower
   than revision 3 implied. It requires **all four** of the following at once:

   - **a Plan 1 member** — pre-1 July 2010 entry **and** at least 60 months of creditable service as
     of 1 January 2013. Prongs (1) and (2) of § 51.1-155.1 A's proviso push a Plan 2 member's age from
     50 to **60**, which is at or past ordinary unreduced eligibility and so delivers no acceleration.
     (Prong (3), hybrid enrolment, is inert because § 51.1-142.4 A already excludes hybrid members);
   - **one of a closed list of positions** — a position described by subdivision 1, 2 (each excluding
     Judicial Retirement System members), 3, 4 (excluding an officer elected by popular vote), 7, 13,
     14, 15, 16, 17 or 20 of § 2.2-2905; **or** an agency headship appointed by a state board,
     commission or council; **or** a school division superintendency appointed by a school board under
     § 22.1-60. Revision 3's parenthetical said "state employees," which materially overstated it;
   - **20 or more years of creditable service** at the date of separation; and
   - **an involuntary separation as § 51.1-155.1 D defines it** — *"any dismissal, requested
     resignation, or failure to obtain reappointment"* — **which is not the definition § 51.1-142.4
     uses.** The overlap is gated by § 51.1-155.1's own definition, not ours (§6.2).

   So the honest statement of this argument is: **for a small subset of G 4 involuntary-separation cases — Plan 1
   members in listed positions — the subsidy buys an acceleration the Code already delivers.** That is
   still a real reason to prefer MOO-44 §5(c)'s treatment, and it is still worth the sentence in the
   patron brief, but it is **not** a reason that reaches the general run of involuntarily separated
   state employees, and the choice should not be made on the inflated premise. **Two sub-questions
   come with it:** whether you want § 51.1-142.4's definition of "involuntary separation" aligned with
   § 51.1-155.1 D (§6.2 — my recommendation is no, and the reason is the requested-resignation
   arbitrage); and whether Fiscal & Impact Modeler can put a count on the Plan 1 listed-position
   subset, because if it is two members the argument should come out of the brief rather than be
   corrected in it. I can ask on instruction.

### §7 item 13 — moved from the live list in store revision 58

13. **MOOT IN REVISION 21 — the exemption is gone, so there is nothing left to restore.** The
    Director answered **"drop the exemption entirely and let the procedures go through Article 2"**
    on the question card of 12 October 2026. § 2.2-4006 C's two-day step was the smallest thing the
    exemption cost; with no exemption claimed the procedures go through the whole of Article 2,
    which subsumes it. The drafted sentence is **not** inserted and is retained below only as the
    record. **What replaced this question is §7 item 27**, which is about the timetable rather than
    the transparency step. *(Retained record:)* Subsection N exempts the Board's procedures from APA Article 2 rulemaking, which it has to
    if the program is to open on 1 July 2029.** Subsection N exempts the Board's procedures from APA Article 2 rulemaking, which it has to
    if the program is to open on 1 July 2029. § 2.2-4006 C attaches a transparency step to exemptions
    *"claimed under this section or § 2.2-4002 or 2.2-4011"*: a regulation put before a board must be
    given to any member of the public who asks for it at least two days before the meeting. An
    exemption written into § 51.1-142.4 M (subsection N before revision 10) sits outside all three, so the step does not attach.
    Nothing goes unpublished — N already requires the Board to adopt **and publish** — but the
    pre-meeting availability is lost. **One sentence restores it, and I have drafted rather than
    inserted it:** *"The Board shall make any procedure proposed to be adopted or amended under this
    subsection available, no less than two days before the meeting at which the Board will consider
    it, to any member of the public who requests a copy."* My recommendation is to take it: it costs
    the Board nothing, it is a step the APA would have required but for the exemption, and a
    committee that notices the exemption will ask what replaced it. But it is an obligation no cited
    document directs, so it is yours.

### §7 item 16 — moved from the live list in store revision 58

16. **MOOT IN REVISION 9 — the rule is retired, so neither limb has to give way.**
    [`package-v11-corrections`](/MOO/issues/MOO-3#document-package-v11-corrections) §3.2 finds MOO-46
    Decision 2(e)'s rule has no solution at all (a *lower* ceiling funds *more* elections, so "the
    lowest round figure" is $0, and 30 elections exceeds the whole central cohort), and the Director
    has set the ceiling off the distribution instead. **No answer is needed. Record only, below.**

    **New, from [MOO-53](/MOO/issues/MOO-53) §4.4: MOO-46 Decision 2(e)'s two limbs no longer have a
    common solution, and which one gives way is yours.** The rule was *fund at least 30 elections
    dearest-first* **and** *touch no Pathway B election*. On the redrafted definition the second limb is
    **unsatisfiable below $182,800** — Pathway B's maximum rose from $54,974 to $182,800 and now
    **exceeds** Pathway A's $170,343, so the modes have inverted — and at $182,800 the ceiling trims
    nothing and funds 18.1 elections, not 30. **I have drafted on the 30-election limb**, which is
    what gives `[$100,000]`. The Pathway B limb is also arguably moot, since § 51.1-142.4 A clause (v)
    removes Pathway B from the bill by construction (MOO-46 Decision 3.1, confirmed in
    [MOO-49](/MOO/issues/MOO-49)) — but it was your rule and I am not going to retire half of it
    silently. **If you intended the Pathway B limb to control, the ceiling has to come out of the bill
    altogether**, because no figure satisfies it and binds.

### §7 item 17 — moved from the live list in store revision 58

17. **"Unreduced retirement eligibility date" and the 50/10 route — DECIDED AND DRAFTED; CLOSED IN
    REVISION 7. Nothing is open here and a reviewer should not re-open it.** Revision 6's
    cross-reference check found that the definition's negative test did not exclude the 50/10 route,
    which § 51.1-155 **A 5** pays and which neither A 2 nor A 3 reduces, so that age 50 with 10 years
    became a member's unreduced retirement eligibility date — excluding much of the target cohort
    under clause (v) and permitting a zero-month purchase under C (ii). You decided it on
    [MOO-62](/MOO/issues/MOO-62): **take the fix, and keep the negative limb as well as the positive
    one**, because the positive limb standing alone has the mirror defect — A 2 and A 3 compute no
    allowance of their own (each says *"The allowance shall be determined in the same manner as for
    normal retirement"* and then reduces it), so a reduced early-retirement allowance can be called
    *"calculated in accordance with subdivision A 1"* and the **reduced** date becomes the unreduced
    eligibility date. Revision 7 drafts both limbs in **both** definitions, so the admission test and
    the settlement test stay word-identical and the [MOO-49](/MOO/issues/MOO-49) §4.2 route is closed
    against the mirror reading as well as the literal one. **Three things to record rather than
    revisit.** First, **Option 2 was declined and no research issue is open**: the § 51.1-155 A 5
    question — is an A 5 payment a "service retirement allowance," and does VRS administratively
    treat 50/10 as unreduced eligibility? — changes **no operative text** against the combined
    phrase, because an A 5 allowance fails the positive limb however it is answered. It is closed, not
    pending. Second, **no priced quantity moves**: the cohort every figure in the package is priced
    on is the **unreduced subdivision A 1 cohort, reached through § 51.1-153 A, B 2 or B 3**, paid
    under subdivision A 1 and reduced under neither A 2 nor A 3, and both limbs admit it.
    `[Description corrected in revision 8; revision 7 called this "the § 51.1-153 B
    normal-retirement cohort." Subsection B is captioned Early retirement and B 1 inside it is
    excluded. The set and every figure are unchanged —` [MOO-65](/MOO/issues/MOO-65) `F-3.]` Third, the two things **not** to do are drafted
    against on the record — no *"solely"* (it would drop an A 1 + A 4 abolished-system transferee) and
    no tier test in place of *"whichever applies to the member"* (§6.1a item 2). **The only thing left
    for you on this item is to confirm you are content with the drafted words**, which are the words
    you wrote.

### §7 item 18 — moved from the live list in store revision 58

18. **The four [MOO-65](/MOO/issues/MOO-65) repairs — ANSWERED 12 OCTOBER 2026, ALL FOUR ENACTED IN
    REVISION 21. CLOSED. Nothing is open here.** The Director answered **F-1 Candidate B, F-2 both
    repairs, F-4 the long form, F-8 enact**, and all four are in the bill — redline at
    §0.0000000000000000, cross-reference check at §5.11. **Three further repairs were enacted with
    them**, from [MOO-82](/MOO/issues/MOO-82)'s review of the enacted text: **S-1** (the trailing
    section list bounded on each limb, retiring a null reference to a lump-sum distribution that
    § 51.1-165 does not contain), **M-2** (the definition reordered so the date requirements attach to
    the actual retirement) and **m-1** (*"that date"* given its antecedent). None was pre-approved and
    §6.0-21 states the ground for each. **Still closed:** both limbs stand, Option 2 stays declined, no *"solely"*, no tier test, and no figure moves. **[MOO-82](/MOO/issues/MOO-82) left five
    findings that are the Director's: items 27 to 30 below.** The four questions as asked are retained in §0.00000.

### §7 item 22 — moved from the live list in store revision 58

22. **ANSWERED 12 OCTOBER 2026 — OPTION (c), AND THE DRAFTING IS [MOO-87](/MOO/issues/MOO-87) — performed;
    moved verbatim to the retained-record document on [MOO-142](/MOO/issues/MOO-142). Nothing in this item is
    open.**

    **Moved verbatim** to
    [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2), every
    lettered limb, sub-item and figure preserved, so a reference of the form **§7 item 22** or **option (b) of
    item 22** still resolves there. Same reason and method as §7.1 and the §0 and §6.0-n records moved in store
    revisions 34 through 50: this file was **886 characters** from the store's 524,288-character ceiling and
    [MOO-142](/MOO/issues/MOO-142)'s record corrections did not fit. A fully answered item was chosen over an
    open one, and this one carries **no external sub-item reference** that the pointer does not resolve.

    **The durable result.** Subsection C clause (ii) is measured **as of the filing date**, with a bar on a
    purchase that does not advance the member's unreduced retirement eligibility date by at least a month —
    the Director's option **(c)**, decided on [MOO-71](/MOO/issues/MOO-71) on MOO-78's figures and relayed on
    [MOO-85](/MOO/issues/MOO-85). It is **drafted and in the store**: MOO-87 wrote it as revision 22 and
    revision 24 rebased it in. Pass 9 ([MOO-93](/MOO/issues/MOO-93)) reviewed the two changed places and
    returned no fatal finding. Pass 7's **F-9** is cured and **F-7** superseded; **F-22** is held for the
    reason at §0.x f item 3. **No operative text moved in this relocation**, and §7's numbered items 1 to 100
    are unaffected.

### §7 item 26 — moved from the live list in store revision 58

26. **REVISION 30: THE FIRST HALF IS RESOLVED IN THE OPERATIVE TEXT AND THE SECOND IS WITHDRAWN.
    What remains for you is whether to reverse the first half, and the two deletions that do it are
    written out at §6.0-25 item 2.** This item asked whether subsection C's refusal notice should carry
    subdivision D 4's full package. **The standard-cost quote is now in the text** — store revision 24
    added it and store revision 30 keeps it and corrects the quantity it prices. I am not treating that
    as my choice to defend: [MOO-84](/MOO/issues/MOO-84)'s F6 classified the omission as a
    **consistency defect rather than a policy choice** (every other notice in the section that states
    the subsection B right also states the price), and its **F5** showed that subdivision D 5's third
    sentence already purported to reach every denial notice at the standard cost — two provisions giving
    different contents for one letter, not resolvable without answering this. **If you want it out, the
    two deletions must be made together.**

    **The further-application statement stays out, and the reason has changed from "arguable" to
    "futile".** MOO-84's F7 is right that clause (ii) is **non-increasing in the date it is measured
    at** — the member earns membership service as time passes, so the months she still needs only fall.
    A bare invitation to re-file is therefore not of uncertain value; it is an invitation to the same
    refusal. **This reverses the recommendation this item carried in revision 20.**

    **And option (b) that this item used to carry no longer exists.** F7's alternative was to disclose
    subsection C's early-payment redetermination route, under which the member could ask to be
    remeasured at an earlier date, where clause (ii) is positive. **Option (c) deleted that sentence**
    (§0.x f of revision 24's record), so there is no route in the text to disclose. Creating one would
    be a new route into the programme, not notice content, and it is not drafted.

    **One thing to read with this item: §7 item 35.** Option (c) has made subsection C's zero bar
    **unreachable**, so the notice this item is about can no longer be triggered at all, and the member
    it was written for is refused under subdivision D 4 instead — where she receives the full package
    including both of the two limbs this item was about. **If you take item 35 option (b), this item
    closes with it.**

    **CLOSED IN STORE REVISION 38, BY ITEM 35 OPTION (b), AS THIS ITEM SAID IT WOULD BE.** The
    refusal notice whose contents this item was about is **deleted from subsection C**, so there is no
    letter here left to specify and nothing in this item is actionable. The member it was written for
    is refused under subdivision **D 4**, whose notice already carries both limbs this item weighed —
    the statement of her rights under subsection B of § 51.1-142.2 and the standard-cost quote — and
    carries them with a 30-day deadline and review under subsection M. **Nothing in this item is
    withdrawn**: its first half is resolved by deletion rather than by reversal, and its finding that
    a bare invitation to re-file is futile stands as the record of why that limb stayed out. If the
    Director reverses item 35, this item re-opens in the form it has immediately above.



    **RE-OPENED IN STORE REVISION 44, IN THE FORM IT HAS IMMEDIATELY ABOVE, ON THE DIRECTOR'S ANSWER
    THAT §7 ITEM 35 (a) GOVERNS.** The refusal notice this item is about is back in subsection C, so
    there is again a letter here whose contents can be specified, and the closure above is spent. **What
    is live is only the first half**, and the Director has already answered it on MOO-101: *"keep both
    halves of revision 30's cure"* — the standard-cost quote stays in subsection C's notice and
    subdivision D 5's third sentence stays bounded — and *"[t]he two deletions at §6.0-25 item 2 are
    **not** taken."* **The further-application statement stays out and nothing is to be drafted to
    re-create a pre-acceptance remeasurement route.** So the item re-opens and closes in the same
    revision, on the answer it already had: **nothing in it is actionable, and its finding that a bare
    invitation to re-file is futile stands as the record of why that limb stayed out.** Store revision
    43's restoration also returns the consistency ground this answer relied on, because every surviving
    applicant notice in the section again states the subsection B right and its price (see §7 item 34
    item 5 and MOO-98's M4).

**Items 27 to 30 came from the [MOO-82](/MOO/issues/MOO-82) counsel review and all four were answered by
the Director on 12 October 2026. All four are closed and three are drafted into the bill in store revision
34.** The failure scenario and the authority for each are still in
[`rev21-record`](/MOO/issues/MOO-42#document-rev21-record) §7; the disposition is here, and the items the
answers and [MOO-99](/MOO/issues/MOO-99)'s pass 10 generated are **43 to 52** below.

### §7 item 28 — moved from the live list in store revision 58

28. **ANSWERED 12 OCTOBER 2026 — BOTH CLAUSES. DRAFTED AND CLOSED IN STORE REVISION 35, WITH ONE
    NARROWING THAT IS NOW ITEM 43.** G 4 carries the bar on determining or giving notice while a disability
    application is pending, the tolling that makes it performable, *"pending"* defined, the
    rescission-and-restoration duty with a 60-day deadline and its own notice and review right, the
    redetermination clock, and the no-recovery limb named inside G 4's existing prohibition. **The death limb
    is narrowed** to a case to which clause (i) of G 4 applies, because the approved words would have reversed
    the [MOO-44](/MOO/issues/MOO-44) line (§6.0-35). **Pass 10 rated the draft of this item its most serious
    finding and it is repaired here** — *"may be settled"* is *"is settled."* **Items 45, 46, 49, 50, 51, 52
    and 54 are its residuals**, and **item 46 — the price of the bar, which pass 10 raises independently as
    its own serious finding — is the one I would take first.**

### §7 item 30 — moved from the live list in store revision 58

30. **ANSWERED 12 OCTOBER 2026 — OPEN THE GATEWAY FOR SUBSECTIONS A AND C ONLY. DRAFTED AND CLOSED IN
    STORE REVISION 35.** Both definitions now read *"under § 51.1-153, or under subsection A or C of
    § 51.1-155.1."* **Subsection B is excluded by the answer, against my recommendation to include it**, and
    the consequence is recorded and not cured (§5.17, item 47). **And the ground for the answer was better
    than the one I gave:** my record said no member was harmed by exclusion because *"G 4 (iii) vests the
    credit on the involuntary separation itself,"* and **there is no such clause** — on the closed reading the
    member separated at 50 failed G 4's 90-day condition and subdivision 2 clawed her credit back. **No priced
    quantity moves on the actual-facts reading** (§5.17) — but **pass 10 found a second reading of the same
    words under which the admission rule moves in both directions, which is item 48, and it is the one open
    question in this revision that can move a number.**

### §7 item 34 — moved from the live list in store revision 58

34. **ANSWERED 12 OCTOBER 2026 — ALL FIVE ENACTED IN STORE REVISION 44, THREE OF THEM WITH A REPAIR
    [MOO-121](/MOO/issues/MOO-121) FOUND IN THE DRAFTED WORDS.** The commission was extended to M 2, D 7,
    D 2 and D 6 for this purpose only, and the five strings as enacted are at
    [`moo101-cut-record`](/MOO/issues/MOO-42#document-moo101-cut-record) §2, each with the anchor it was
    verified unique against. **Nothing in this item is open.**

    - **1 — F3, the filing date through an M 2 reconsideration: enacted, less its durational limit.** The
      drafted sentence ended *"until 30 days after the Board acts upon the request"*, and MOO-121's **M3**
      is right that a retention rule with an expiry invites the negative implication that the filing date
      is **lost** when the retention lapses — which nothing in the bill provides for. The sentence is
      enacted without those words and the date is retained for all purposes of subdivisions D 4 and D 5.
      **Reversible by restoring six words.**
    - **2 — F4, M 2's class: enacted on the first cure, as directed.** M 2 now reads *"A member, retiree,
      beneficiary, or applicant."* **Reversible in one word.** Three conforming amendments went with it,
      each inside the same subdivision: the tolling sentence now tolls a period within which *"the member
      **or applicant**"* must act (MOO-121 **M4** — D 4's 60-day completion window is an applicant's
      period); the judicial-review savings sentence names the same four classes (MOO-121 endorses; it was
      my own residue); and the gateway reaches **a failure of the Board to act**, which is what makes the
      Director's answer on MOO-98's M1 operative — see item 76.
    - **3 — F8, D 7's release on refusal: enacted as drafted.** The cap-arithmetic consequence is
      measured and it is **not** a change to any published figure: MOO-32 v6 already charges nothing
      against the $3,000,000 for a ceiling-refused election, so **this sentence is what makes the
      published 78.19 percent true rather than an improvement on it**. Worth **$65,473** of peak charge,
      **+2.18** points of the cap and about **one** point of take-up headroom ([MOO-102](/MOO/issues/MOO-102)).
      The release is **under-inclusive in four further cases** and that is item 75.
    - **4 — the F1 clone in D 2: enacted at both substitutions, and the first one needed a repair.**
      Re-keying the trigger to the fact stranded the words *"of the determination, of the reasons for
      it"* — their antecedent was the determination named in the stricken trigger — so the notice would
      have stated a dollar figure and a price list and **nothing that says the applicant is out**
      (MOO-121 **S1**, its headline finding). It now states *"the Board's determination that it may not
      accept the election, of the reasons for that determination."* **This notice is the only statutory
      exit for 1.2339 expected refusals, 6.29 percent of the live applicant set of 19.6304.** The clock is
      the Director's **parity answer** of 12 October 2026 — *"no later than 30 days after the member's
      application is completed"* — so both refusal notices now run on one clock keyed to a fact and
      neither waits on an act the bill never deadlines. **One word is left unconformed and it is on
      purpose: the sentence otherwise names *"the applicant"*. See item 77.**
    - **5 — D 6's cancellation notice: enacted in full, as directed, and my narrowing of it was wrong.**
      I had enacted the standard-cost limb only, on the premise that D 6's third sentence already supplied
      the 30 days and the review route. MOO-121's **S3** re-read that sentence and the premise fails
      twice: the 30 days bound the **recertification** notice, a different notice with different content,
      and the review route runs to **the recertification**, not to the cancellation — which operates by
      force of statute and so is doubtfully a *"determination of the Board"* at M 2's gateway at all.
      Both dropped limbs are enacted in the Director's own words. The *expressio unius* worry recorded
      against the review limb in this item is answered by the gateway amendment under item 2 above,
      which now reaches a failure as well as a determination, so the express grant is no longer the only
      one of its kind.

---

## §8 status notes moved in store revision 60 — store revisions 55, 54, 53 and 52

> **STORE REVISION 55 — [MOO-131](/MOO/issues/MOO-131)'s CONFORMING AMENDMENTS DRAFTED OUT, from
> [MOO-130](/MOO/issues/MOO-130). Eight substitutions in six provisions, 1,175 characters. No figure
> moves, no designator is renumbered, no section is added or deleted, and the title does not change.**
> The six: subdivisions D 1, D 2, D 4, J 1 and M 2 of § 51.1-142.4, and enactment 3 clause (v) of the
> act; M 2 takes three of the eight. Record: [`moo131-conforming-record`](/MOO/issues/MOO-131#document-moo131-conforming-record). Narrative §0.0-55; sweep §5.34; drafter's note
> §6.0-55; residues §7 item 107. Applied on [MOO-148](/MOO/issues/MOO-148).
>
> **What is in the text.** Subdivision D 1 now **dates the determination it reports** — 30 days from a
> completed application — which makes D 2's notice performable and gives D 3 and D 7 the event they both
> depended on (**1.2339 expected $170,000-ceiling refusals** closed, 6.2855 percent of the 19.6304 live
> applicant set). M 2's filing-date retention is **bounded by the Board's act**, on subdivision D 3's own
> device, with a 15-day companion duty. A **one-sentence deeming** in M 2 makes thirteen classes of act
> and event reviewable *"for the purposes of this subsection,"* closing all seven of the un-named
> adverse-action points. Subdivision J 1 must now report **every failure to determine or to notify,
> stated separately for each provision**. Enactment 3 clause (v) saves the **failure** limb as well as
> the determination, so the duty and the remedy expire together after 1 July 2033. And subdivision D 4
> states the **mode of withdrawal** — a power, by written notice, effective on receipt — which supplies
> the referent D 3 and clause (v) both used without defining.
>
> **No new consequence clause was written.** E1's and E4's periods borrow their *"or else"* from M 2's
> failure limb and from E7's new report item; stating the period is what created both.
>
> **One anchor was re-cut and the finding was re-checked, not re-anchored blind.** Store revision 54
> re-worded subdivision J 1's closing catch-all to *"and, to the extent not otherwise required by this
> subdivision, every other matter this section requires the Board to state in that report."* The
> re-worded catch-all still **collects** report duties and **creates none**, so the roughly twenty-one
> Board periods whose own provisions say nothing about reporting were still unreported and E7 is still
> needed. **The inserted words are unchanged at 153 characters** and still sit before the catch-all.
>
> **What is not here, so it is not mistaken for an oversight.** **MOO-130's S3 was already enacted by
> store revision 47**, in that cut's own and better-anchored words, and was **not drafted twice**. **S6**
> — M 2's deemed denial — is the Director's, at **§7 item 88**. **M5, M6 and m1 to m6 make no bill edit,
> per the commission.** **§7 item 76's standing offer to reverse form (B) is declined, and the reviewer
> has withdrawn it — form (B) stands**, and item 76 should be closed rather than left standing as an
> offer. **§7 item 78** is untouched and nothing here waited on it.
>
> **Housekeeping.** This revision arrived at **15,909 characters** of headroom with **three** full sets of
> §0, §5 and §6 in the file. On the rotation store revision 52 set up at §0.1, **store revision 52's §0.0
> narrative, its sweep §5.31 and its drafter's note §6.0-52 are moved verbatim** to [`bill-text-s8-record-s0-s5-s6-rev2-51`](/MOO/issues/MOO-42#document-bill-text-s8-record-s0-s5-s6-rev2-51), each replaced
> by a stub restating its durable result, so §0.x, §5.31 and §6.0-52 still resolve. **No bill text moved,
> nothing was rewritten and nothing was summarised away.**
>
> **Not publishable. The eight new strings have had no counsel pass**, and two of them — E5's deeming
> and E1's period — are the widest text in the section. **This revision closes no §7 item and opens one**,
> item 107, whose point (d) must be answered together with **§7 item 88**. Nothing here is cleared for
> external use, none of it has been reviewed by counsel or by Division of Legislative Services, and no
> part of it may be described as cleared or sent to a patron or to Division of Legislative Services.

> **STORE REVISION 54 — the Policy Director's six answers of 12 October 2026 enacted, with MOO-126's
> F9 and F4.** Seven edits to §1, all inside new § 51.1-142.4: subdivision **G 4** takes (f) in place of
> (d), the crediting deadline, the rebuilt death notice and the report-and-release sentences;
> subdivision **D 1** takes the pre-filing disclosure; subdivision **M 2** takes the personal
> representative of a deceased member's estate, in **both** of its class lists. **No designator is
> renumbered, no figure moves, no section joins or leaves the act, no defined term is added, and the
> title line does not change.**
>
> **The one place the enacted words are not the card's words** is the pre-filing disclosure, which the
> card required to state that such a death is determined under § 51.1-165 C — a proposition (f), approved
> on the same card, makes false for exactly the members who receive the writing. The duty is enacted with
> the content the act now produces and the verbatim alternative is at **§7 item 106**, which is where
> the three other open consequences of the card are too. **§6.0-54 item 3.**
>
> **(f) supersedes (d).** (d)'s sentence is out of the bill; its computation limb is carried into (f)
> word for word, because without it nothing ties the benefit to the credit the member bought. §6.0-54
> item 2.
>
> **Cross-reference sweep §5.33, both directions. Conforming amendments elsewhere in the Code: none.**
> §§ 51.1-162 and 51.1-163 were cited nowhere in the act and are now cited; that is the authorised
> reversal of [MOO-96](/MOO/issues/MOO-96)'s **F-4**, and the fact that § 51.1-165 C 1 is displaced by a
> *"notwithstanding"* invisible to a reader of § 51.1-165 **must travel in the drafting request to
> Division of Legislative Services** — a drafter's note is not enacted.
>
> **No adversarial pass has seen any of these seven edits.** They are wider than anything store revisions
> 47 to 50 touched, and the last unreviewed cure drafted into this subdivision was rated **fatal**. The
> next bounded pass belongs here.
>
> **Nothing was moved out to make room, which has not been true since store revision 33.** This revision
> arrived 42,971 characters from the ceiling because store revision 53 executed the Director's
> answer to **§7 item 53**. One housekeeping consequence, not a change to the bill: **§5 and §6 now hold three
> revisions apiece**, because store revision 53 and this one each added a section without moving the
> previous one out. Both preambles say so and name what the next revision must move.
>
> **Cut four times — as 50, as 51, as 53 and as 54.** Every label is derived from the live body and every
> anchor asserted unique, so the rebases cost nothing; the third caught a real collision, store revision
> 52 having given the disability branch a refund sentence identical to the death branch's but for
> three words.

> **STORE REVISION 53 — [MOO-137](/MOO/issues/MOO-137)'s PASS 16 DRAFTED OUT. Five edits in three
> provisions — subsection C's no-value sentence, a new boundary sentence beside it, and subdivision J 1's
> residual limb. No figure moves, no designator is renumbered, no section is added or deleted, and the
> title does not change.** Pass 16 returned **0 fatal, 2 serious, 5 moderate, 3 minor** on store revision
> 48's four edits. It is a different pass 16 from [MOO-135](/MOO/issues/MOO-135)'s, which store revision 50
> drafted out. Full record:
> [`moo137-pass16-disposition`](/MOO/issues/MOO-145#document-moo137-pass16-disposition); narrative §0.0-53,
> sweep §5.32, ambiguities §6.0-53.
>
> **What is in the text.** The substituted no-amount determination **gets back the period it was
> discharged out of** — *"no later than 30 days after the member's application is completed"* — which
> restores subsection C's J-report duty, subdivision M 2's reconsideration gateway and M 2's Article 5
> route in one move, because all three key on a **period-defined** failure. **That was S-1, it was serious,
> and it was against my own edit**: without a period the Board could never make the determination, never
> certify, and leave the member with no report, no reconsideration and no petition. The boundary that said
> a no-amount determination is not a zero determination now also **runs on the world**, so an analyst who
> enters `0` in an empty field cannot engage the acceptance bar (M-3). *"Specified **under**"* is conformed
> to the section's own *"specified **in**"* (M-2). J 1's residual limb is made **expressly
> non-duplicative** and points at J 1's own report (M-4, m-3), and *"that certification"* gets its express
> referent (m-1). **No sentence ordinal is used anywhere in the five.**
>
> **Two things the Director should read.** **§7 item 88's recommendation moves from (c) to (d)** on
> [MOO-139](/MOO/issues/MOO-139)'s findings: (d) legislates the § 2.2-4001 case-decision predicate on the
> § 9.1-405 model instead of assuming it in a savings clause, where (c)'s source text is tied to fraud
> recovery and is pre-decisional. **And *"no figure moves"* is now confirmed rather than asserted** —
> pass 16's **M-5** was right to challenge it for edit 3, and [MOO-144](/MOO/issues/MOO-144) answered that
> the authorised **18.3965 already includes** the empty-solution-set class (0.0259 inside it; exactly
> 18.3706 without it) and that edit 3 moves the certified amount on **0 of 5,552 cells**. Two M-5
> descriptors do not reproduce: the class buys **exactly 3.0 years**, not four, and the advance is **6 to 30
> months**, not 47.
>
> **S-2 is closed as already false.** It reported that the promotion had not run, on document revisions
> **53** (`d746986d`, 08:48:39.652Z) and **54** (`609c9f3e`, 08:50:34.051Z), publishing at 09:05:23 without
> re-reading; store revision 48 had landed between those events as document revision
> **`34d252a6-c17c-481a-8f69-6eb1a3d9b9ac`** (522,443 characters), and the corrected address was posted at
> 08:59:37. **Nothing in this record implies the promotion is outstanding.** The reviewer read honestly,
> said so prominently, and verified its own baseline — which is why its other findings were usable.
>
> **Not publishable.** The five changed places have had **no counsel pass of their own** —
> [MOO-153](/MOO/issues/MOO-153) is the bounded one and carries the document revision id and character
> count. §7 items 98 and 100 to 102 are carded to the Director and enacted nowhere. **Nothing here is
> cleared for external use.**

> **STORE REVISION 52 — [MOO-64](/MOO/issues/MOO-64)'S SEVEN ANSWERS ENACTED, AND THE RETAINED RECORD
> MOVED OUT. Thirteen edits in four provisions: the definition of *"unreduced retirement eligibility
> date"*, subdivision G 3, subdivision G 4 (nine edits) and subdivision J 1 (three edits). +3,337
> characters of bill text. No figure moves, no designator is renumbered, no section is added or deleted,
> and the title does not change.**
>
> **The fatal is cured.** Pass 12's F-1 — item 54's rescue inoperative in every case it was written for,
> because G 4's settlement bar has a **D 7 release** limb the rescission did not disapply and a
> reinstatement limb that reached only releases *"otherwise than"* under D 7 — is closed by both
> insertions the Director approved. Insertion (i) sits in the rescission sentence, which already reads
> *"a determination under subdivision 2 or 3"*, so **the G 3 branch and the pre-existing G 2 branch are
> cured together.** The survivor now gets the crediting **and** the subsidy.
>
> **Pass 12's four serious findings are all enacted**: J 1's terminal date can now arrive (S-1); the
> member whose late disability application § 51.1-156 H **compelled** the Board to admit keeps the
> rescission, while every other late filing is expressly shut out (S-2 with M-6); clause (iii), error of
> the Board, has the rescission route the other two clause-events always had (S-3); and the member who
> wins on reconsideration or judicial review has a duty to restore, a deadline, and her arrears (S-4).
> **All five of the cheap bundle are in** — the confinement operates section-wide, the one month-for-month
> offset is authorised and nothing else is, G 3's second sentence yields on rescission, the subdivision-3
> rescission refunds the excess, and §3 requires the fiscal statement to quantify the two one-sided costs.
>
> **Four changes inside the approved text are mine and are at §6.0-52 items 1 to 4.** The one that
> matters: **item 93 as carded would have reproduced the fatal defect in new words** — a determination
> reversed on review *has* taken effect, so the bar forbade the settlement item 93 commanded, and nothing
> reinstated the released reservation. Both limbs are drafted into item 93 and into insertion (ii). The
> other three are a redetermination clock that gained item 92's third trigger, a refund that gained the
> death branch's 60-day deadline and adverse-tax fallback, and an arrears formula that now reaches a
> **modification** as well as a reversal. **That last one moves money and is carded as §7 item 105 rather
> than left in the note.**
>
> **The record is out of this file, on the Director's answer to §7 item 53.** 101,593 characters of retained
> §0, §5 and §6 moved verbatim to
> [`bill-text-s8-record-s0-s5-s6-rev2-51`](/MOO/issues/MOO-42#document-bill-text-s8-record-s0-s5-s6-rev2-51);
> §0.1 carries the index and every **§0.x**, **§5.n** and **§6.0-n** reference up to revision 51 still
> resolves. **Before the move this file had 4,008 characters of headroom** and both earlier retained-record
> documents were effectively full — the ~235-character fatal fix would have fitted and its record would
> not. The file now has room for several revisions' records, and §5 and §6 carry the **current** revision
> in full, which is where my own output bar requires them to be.
>
> **What is NOT done.** The thirteen edits of this revision have had **no adversarial pass of their own**
> — that is **pass 17**, sent as [MOO-152](/MOO/issues/MOO-152), which reproduces all thirteen edits in its description. **Three open items are new and none is enacted**: item 103,
> no member-initiated route to a clause (iii) error determination; item 104, no subsection J line for the
> new refunds, reversals and modifications; item 105, confirmation of the arrears formula. **Item 98 was
> not asked and stays open.** Items 89 to 97 and 99 are closed.
>
> **No priced quantity moves and nothing needs re-running.** Items 89, 92, 93 and 97 move **settlement**
> toward the basis every figure already prices — the unreduced subdivision A 1 cohort reached through
> § 51.1-153 A, B 2 or B 3, priced as settling — by removing bars and gaps that refused it; items 90, 94,
> 95 and 96 touch a reporting date, a scope phrase, an offset and a deeming sentence. **Nothing in §3,
> `model-s8-s9` or the [MOO-85](/MOO/issues/MOO-85) reprice needs re-running.** Two edits spend money
> one-sidedly, both on answers the Director took on that footing, and the quantification is §7 item 99's
> and Fiscal's.
>
> **Internal working draft. Not a Division of Legislative Services bill. Not reviewed by counsel.
> Pre-decisional.**

---

## Moved in store revision 61 — §8's status note for store revision 56

### §8 status note for store revision 56 — moved from the live list in store revision 61

> **STORE REVISION 56 — [MOO-153](/MOO/issues/MOO-153)'s COUNSEL PASS ON STORE REVISION 53
> DISPOSITIONED. One edit to the bill text, +6 characters, and six new §7 items. No figure moves, no
> designator is renumbered, no section is added or deleted, and §1 is otherwise untouched.** The edit:
> subsection C's fifth sentence takes a second `shall` before *"state that determination"* (counsel's
> m-1), which forecloses a mis-parse and does nothing else. Record:
> [`moo153-counsel-disposition`](/MOO/issues/MOO-145#document-moo153-counsel-disposition). Narrative
> §0.0-56; sweep §5.35; drafter's note §6.0-56; new items §7 108 to 113. Applied on
> [MOO-145](/MOO/issues/MOO-145).
>
> **Why only one edit.** Counsel returned **0 fatal, 3 serious, 4 moderate, 2 minor**. Five of the nine
> need a provision that was never agreed, or reverse a choice the Policy Director's own direction
> produced, so each is drafted verbatim in the companion document and carried into a §7 item with
> options and a recommendation — **and none of them is in the bill.** The two to read first: **item
> 108**, where the Board can meet all seventy-odd periods and still strand an eligible member
> permanently, because nothing obliges it to file the subdivision D 3 request or to issue the subsection
> D certification; and **item 110**, the § 2.2-4021 B deemed-decision default, which counsel finds
> **already live without option (d)** and which **no option on item 88 addresses at all**.
>
> **S-1 of the pass — *"store revision 53 never landed"* — is false as to the fact, right as to the
> process, and the process defect is mine.** Store revision 53 is document revisions 63 and 64
> (`2af78c15`, 481,320 characters; `917b16d1`, 481,317 characters, 12:28:13.953Z), and all five edits
> survive in the head. **[MOO-153](/MOO/issues/MOO-153) was created at 12:24:46, three minutes before
> that write**, so counsel read the true head as it stood when it woke and the anchor comment the brief
> pointed it at did not yet exist. I commissioned a counsel pass on a revision I had not applied. The
> three rules adopted in consequence are at §0.0-56.
>
> **Record housekeeping, under the predecessor rule.** Store revision 53's own §0.0-53, §5.32 and
> §6.0-53 are moved **verbatim** to
> [`bill-text-s8-record-s0-s5-s6-rev2-51`](/MOO/issues/MOO-42#document-bill-text-s8-record-s0-s5-s6-rev2-51)
> and stubbed here, that pass being closed. §0 keeps three narratives, §5 three sweeps, §6 three notes.
>
> **Next step: the Policy Director.** Items 108 to 113, and item 88 with them, are theirs. **Nothing in
> this file is cleared for external use. Internal working draft — not a Division of Legislative
> Services bill, not reviewed by counsel, not legally sufficient for introduction.**

---

## Moved in store revision 71 of `bill-text-s8` — sweeps §5.40 to §5.42, drafter's notes §6.0-59 to §6.0-62, and §8's status notes for store revisions 57 to 62

**Moved verbatim and in full.** `bill-text-s8` arrived at store revision 71 with 9069 characters of headroom against the 524,288-character ceiling and could not take the revision at all. Nothing below is rewritten, abridged or summarised; each section left a stub in the bill naming its durable result and pointing here. **These are dated per-revision records: every figure in them is the figure as at the revision named in its own heading, and a later revision may have superseded it. The live record is in `bill-text-s8` itself.**

### §5.42 Store revision 63 — the one insertion, chased in both directions

**Result: no conforming amendment is required, and nothing is stranded.** Counts are taken over §1 of the body that was written, not predicted.

**Direction 1 — what the new sentence cites.**

| Cited | Occurrences in §1 | Result |
|---|---|---|
| *"the 90 days allowed by this subsection"* | **2** after the insertion (1 before): M 2 clause (ii) and the new sentence | Both refer to the same duty, M 2's *"The Board shall act upon a request for reconsideration within 90 days."* (1 occurrence). **Coupling recorded:** this is the phrase [MOO-141](/MOO/issues/MOO-141) **card (j)** is about, so if card (j) re-keys it the new sentence moves with it. One edit either way |
| § 2.2-4001 | **1** before, **2** after | The existing use is M 2's completion sentence; the new use is the deemed denial. Both are the defining citation for *"case decision"*, and neither is a paraphrase |
| *"final determination … upon the reconsideration"* | **1** before, **2** after | The new sentence adopts option (d)'s own predicate rather than inventing a second term for one concept |

**Direction 2 — what cites the things the new sentence touches.** Every *"act/acts/acting upon"* in §1 — **17** occurrences, unchanged by this revision, re-listed from the live body. The two that matter:

| Provision | Endpoint | Moved by this revision? |
|---|---|---|
| M 2, tolling sentence — *"until 30 days after the Board acts upon the request"* | the Board's act | **No.** A denial under the new sentence is not an act of the Board, so the endpoint is not reached. §7 item 130 |
| M 2 — *"retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"* | the Board's act | **No.** Same reason, and this is the endpoint [MOO-141](/MOO/issues/MOO-141) card (k) is about. §7 item 130 |

**Three further checks.**

1. **No reference by sentence ordinal is introduced.** The new sentence names its referent by its words (*"the 90 days allowed by this subsection"*), not by position, so the two sentences store revision 62 added to M 2 do not strand it.
2. **No existing provision is contradicted.** M 2's completion sentence operates on a completed reconsideration and the new sentence on one that is never completed; the two classes are disjoint, so no event produces two case decisions.
3. **M 3 is checked against the new sentence and does not reach it.** M 3 disapplies *"[t]he sentence of subsection B of § 2.2-4021 providing that a decision shall be deemed to be in favor of the named party, and the corresponding sentence of subsection C"*. The new sentence deems a denial, which is the opposite, so M 3 neither bars it nor needs amending. **This is the point on which the express case-decision characterisation is safe.**

### §5.41 Store revision 62 — the twenty-one substitutions, chased in both directions

**Performed by mechanical count over §1 alone**, not over the whole document, because §2 and §6 quote the operative text and would inflate every figure. **Every count below is taken on the body that was written.** The full table is at [`moo169-disposition`](/MOO/issues/MOO-97#document-moo169-disposition) §5.

**Forward direction — every section this revision cites, counted before and after.**

| Citation | Before | After | Why it moved |
| --- | --- | --- | --- |
| `§ 51.1-162` | 11 | **13** | The restated § 51.1-162 B and C propositions, the f7-toll waiver-period override, and f11-disclose. |
| `§ 51.1-163` | 2 | **3** | The restated subdivision C 2 proposition names § 51.1-163 as C 2's own first-limb measure. **The act still does not purport to switch § 51.1-163 off anywhere.** |
| `§ 2.2-4026` | 0 | **1** | New. M9's saving clause is **the act's first citation of § 2.2-4026**, though subdivision M 2 has relied on Article 5 since store revision 40. |
| `§ 8.01-2` | 0 | **1** | New, and **the act's only citation into Title 8.01**. m1's standard for *"person under a disability"* and *"fiduciary"*. |
| `§ 51.1-200`, `§ 51.1-211`, `§ 51.1-300` | 1 each | **2 each** | f10-b's restatement in subsection L, in the same chapter form the definition of *"eligible member"* already uses. |
| `§ 51.1-165` bare | 7 | 7 | **Unchanged.** No displacement is added or removed. |
| `§ 51.1-165.01` | 7 | 7 | **Unchanged**, for the same reason. |
| `§ 51.1-142.2` | 61 | 61 | Unchanged. |
| `§ 51.1-153` | 8 | 8 | **Unchanged, and this is the point of E1.** The deleted window was the act's only attempt to key the death branch to the § 51.1-153 notice. |
| `§ 51.1-155`, `§ 51.1-155.1`, `§ 51.1-156`, `§ 51.1-169`, `§ 2.2-4001`, `§ 2.2-4021`, `§ 2.2-3200`, `§ 65.2-100` | unchanged | unchanged | No edit reaches them. |

**Reverse direction — conforming amendments elsewhere in the Code: none required, and one available and not drafted.**

- **None required.** The act continues to amend **one** section (§ 51.1-142.2) and to add **one** (§ 51.1-142.4). No section of the Code cross-references § 51.1-142.4, because it does not yet exist; the reference to § 51.1-142.4 in subdivision B 4 c of § 51.1-142.2 is created by this act and is checked at §5.11. Citing a section does not require amending it, so §§ 51.1-162, 51.1-163, 51.1-165, 51.1-165.01, 8.01-2, 2.2-4001, 2.2-4021 and 2.2-4026 are cited and unamended, as they have been since store revision 40.
- **One available and not drafted, and it is new in this revision. The f7-toll sentence is the act's first operative override of a *period* stated in a section this act does not amend.** The two *"notwithstanding"* clauses displace the **routing** of §§ 51.1-165 C 1 and 51.1-165.01 F; f7-toll instead provides that *"the period stated in subsection C of § 51.1-162 within which a waiver must be made does not expire before the thirtieth day after the notice is given."* **A reader of § 51.1-162 C will not learn that from § 51.1-162 C.** The conforming amendment is one clause — *"except as subdivision G 4 of § 51.1-142.4 provides"* — and drafting it would add § 51.1-162 to the act's amended sections, change the title line and change the first enactment clause. **That is a decision about the act's footprint and it is the Director's**, so it is drafted nowhere and is answer 7 at §7 item 129. The same reasoning was applied to § 51.1-155 in revision 21 and is recorded at §5.11.
- **Internal conforming amendment performed.** Subdivision D 1's first compelled proposition carried the identical window to the one deleted from subdivision G 4, so widening G 4 alone would have compelled the Board to certify a rule narrower than the act gives. **E2 conforms it in the same revision**, and the same substitution carries M5's correction.

**Three checks run inside §1 and reported as results, not assumptions.**

1. **The M 2 class list occurs exactly twice** — once in the reconsideration sentence and once in the Article 5 savings sentence — and **both were replaced**. A person with a reconsideration right and no court was the defect store revision 59 was written to avoid, and it is avoided here.
2. **Five lines of §1 differ and no others**: subdivision D 1, subdivision G 4, subsection L, subdivision M 2, subsection N. The line count of §1 is unchanged, so **no designator is renumbered and no paragraph is split or joined**.
3. **`in service` 13 → 14** — the single new occurrence is M6's insertion of § 51.1-162 C's own in-service condition into the certification. *"In service"* remains **undefined in § 51.1-124.3**, which is why E1 keeps the express waiver that follows it; this is recorded at §6.0-62 item 1 and is the subject of [MOO-169](/MOO/issues/MOO-169) F1's authority list.

### §5.40 Store revision 61 — the thirteen substitutions, chased in both directions

**Performed by mechanical count over §1 alone**, not over the whole document, because §2, §6 and §7 quote the operative text and would inflate every figure. **Every count is taken on the body that was written, not predicted.** The full table is at [`moo161-disposition`](/MOO/issues/MOO-97#document-moo161-disposition) §5. The results that have to be stated here:

- **`§ 51.1-162` 9 → 11** — the largest movement, and all of it inside the three provisions edited. **`§ 51.1-163` 2 → 2: unchanged, and the composition changed.** One reference is deleted (the disapplication that caused F1 and F2) and one is added (the C 2 proposition in the certification, which now names § 51.1-163 as C 2's own measure). **The act still names § 51.1-163 twice and no longer purports to switch it off.**
- **`§ 51.1-165` bare 7 → 7 and `§ 51.1-165.01` 7 → 7: both unchanged.** No displacement is added or removed by this revision; the notwithstanding limbs enacted in store revision 58 are untouched, and subdivision C 2 of § 51.1-165 remains preserved rather than displaced.
- **`other person to whom this section requires a notice to be given` 2 → 0.** The open formula is gone from both of subdivision M 2's class lists and is replaced by two named classes. **Checked against subsection K**, which requires a notice to *the public*: no occurrence of the formula remains anywhere in §1, so the unbounded class is closed on the face of the act.
- **`subsection J` 15 → 16, `subsection N` 3 → 4, `subsection M` 31 → 33** — one new reporting duty (the state agency's death notice), one new reference to subsection N (the cap restoration measured by what has been paid), and two new references to subsection M (the certification's new failure limb and the reinstatement on review). **No amendment to subsection J is needed**, in the form J 1's closing words already accept (*"every other matter this section requires the Board to state in the report"*), and **no amendment to subsection N is needed**: the release sentence refers to it, and does not change it.
- **`§ 51.1-207` and `§ 51.1-218`: 0 → 0 and 0 → 0 — still zero, and that is finding F10.** § 51.1-163 directs payment *"in the same manner as provided in subsection A of § 51.1-162, subsection A of § 51.1-207, or subsection A of § 51.1-218, in accordance with the retirement plan covering such member."* The act's death branch names only the first. Whether that is a defect depends on whether a State Police, VaLORS or Judicial Retirement System member can be an *"eligible member"* at all — **§7 item 128 and a research question for the Statutory Researcher, not a count.**
- **Subdivisions D 2, D 3, D 7 and subsection E: untouched.** This revision releases, reserves and settles nothing new. **The $3,000,000 limitation's words are not amended**; what changed is how much of a settled amount returns to it.

**Conforming amendments elsewhere in the Code: none.** Outward: the sections this revision newly *cites* — § 51.1-162 and § 51.1-163 — have their **operation unaltered by it**; the only operative displacements in the act are those enacted in store revision 58, and each remains confined to a named subdivision or limb. Inward: **no section of the Code cross-references § 51.1-142.4**, because the act adds it; §§ 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 are not amended by this act and say nothing about it, **which is the standing risk this record has carried since §5.19 and which must travel in the drafting request to Division of Legislative Services — a drafter's note is not enacted.**

**Internal integrity, chased sentence by sentence.** Two sentences are added to subdivision G 4 (the state agency's notice duty and the reinstatement on review), so **every one of G 4's eleven *"preceding sentence"* references was re-resolved on the written body, positionally, against the sentence it resolved to before the edit.** All eleven resolve to the same antecedent as before, and the subdivision has no *"preceding clause"* reference; the one new reference, in the reinstatement sentence, resolves to the release sentence immediately before it. **The reviewer's own fix direction for F13 — *"the date determined under the preceding clause"* — was not taken**, because this subdivision uses *"clause"* for its enumerated clauses (i), (ii), (iii) and (a), (b), (c); the enacted words are *"after the earlier of those dates."*

### §6.0-62 Ambiguities resolved in store revision 62

**Seventeen. All seventeen in full at** [`moo169-disposition`](/MOO/issues/MOO-97#document-moo169-disposition) **§6. No policy was chosen by drafting choice; six findings and one approved option were deliberately left undrafted and are §7 item 129.** The twelve a later reader must not undo are these.

**1. The fatal finding was cured by widening, and the words are the subdivision's own, not the reviewer's.** [MOO-169](/MOO/issues/MOO-169) F1's fix direction offered *"and the member dies before the effective date of any retirement of the member."* **That is vacuous for the member who never retired at all** — there is no effective date for the death to precede — and that member is the largest part of the class the finding is about. The enacted condition is *"and the member has not retired before the date of death"*, which is the negative of the carve-out clause (i) already states in its own second sentence (*"Clause (i) of this subdivision does not apply where the member has retired in a retirement that is not a qualifying retirement before the date of death"*). **It carries the retiree carve-out the reviewer insisted on**: a member who retired in a qualifying retirement and died years later is excluded, so MOO-161 F1's forfeiture cannot return, and § 51.1-163 — *"Death after retirement"* — governs her as it governs anyone in her position. **Do not re-narrow this to a window.** Two revisions have now tried and each drew a fatal finding.

**2. The widening restores the Director's approved scope; it does not choose one.** Answer **(f)**, approved on 12 October 2026, directed that the Board determine the benefit *"under § 51.1-162 as on the death of a member in service"* and was unconditional on notification at store revisions 54, 58 and 60. **The window was this drafter's cure to MOO-161 F1 and is recorded as such at §0.0-61.** Restoring the approved scope is drafting; narrowing it was the choice, and it is reversed.

**3. F3 and F4 are cured by one bounded addition, and this is not a reversal of §6.0-61.** Store revision 61 removed *"other person to whom this section requires a notice to be given"* because, on the face of the act, it reached **the public** — subsection K requires the Board to *"give public notice"* — and the two money-committee Chairmen, whose notices are information-only and two of which are expressly anonymised. **What was wrong with that formula was the absence of a subject-matter boundary, not its generality.** The enacted words carry one: *"person to whom this section requires a notice to be given **in respect of a benefit payable on the death of a member**."* Subsection K's notice is of a fact, not of a death benefit; the Chairmen's notices are of reinstatements and excesses. **The accidental class stays out and the conservator of a minor beneficiary comes back in.**

**4. The adverse-determination gate is dropped entirely, not narrowed.** *"Person who claimed any benefit … and whom the Board determined is not entitled to it"* made standing turn on the Board having acted, so the Board could defeat review by never deciding — and M 2's **failure** limb, which exists for Board inaction, was unavailable to the person Board inaction hurts. *"Person who **has** claimed any benefit payable on the death of a member"* reaches the claimant whose claim was never determined. **A remedy that cannot be used by the person the duty protects is a defect, not a policy setting**, which is why this is drafted rather than carded.

**5. F4's wider formula is declined, with the residual named.** The reviewer offered *"or fiduciary of, or person to whom this section requires a notice to be given in respect of, a person in any of the foregoing classes."* **The enacted words reach every fiduciary the act actually writes to**, because the only fiduciary the act makes an addressee is the fiduciary of a death-benefit payee, in subdivision G 4's notice sentence. **The residual is a fiduciary acting for a living member under a disability** — she receives the subdivision D 1 certification and her conservator is in no class. No finding reaches it and no provision of the act requires notice to her fiduciary, so it is not drafted; it is flagged for the next pass and is in the routing table.

**6. F5 is cured in half, deliberately.** Four defects are cured in one substitution: the remedy reached only the six propositions and now reaches *"every matter this subdivision requires to be stated"*; it named *"a failure of the Board"*, which is not a category subdivision M 2 contains, and now names M 2's own category word for word; the member's period ran from a death notice she will never receive and now runs from the certification she was given; and M 2's second sentence, which deemed the certification a determination and had already closed her 30 days, is **expressly disapplied to such a failure**, so there is one window and not two. **What is not drafted is the reviewer's discovery rule** — *"or from the date she files written evidence of the omission, whichever is later"* — because an open-ended limitation period is a policy setting and not the resolution of a contradiction. §7 item 129 answer 3.

**7. F6's numeral is the chapter's own.** M 2's third window was empty for every provision but subdivision D 1: subsection C's statement duties, subdivision D 2's over-cap notice, the definition of *"final qualifying retirement date"*, subdivision G 4's death notice and rescission notice and the reinstatement notices provide **no** period for review of a matter **omitted** from them. The enacted default is **30 days after the certification or notice is given**, which is the period the same sentence already uses for a determination, with a rider preserving any longer or later period a provision does supply. **No new numeral was invented.**

**8. F8's fix direction is corrected, and only the charging rule is enacted.** The reviewer asked for the general reinstatement sentence's *"charging rule and excess consequences"* by reference. **The excess consequences already applied.** Subdivision G 4's notice sentence opens *"The Board shall give written notice of every reinstatement under this subdivision"*, so the notice to the Chairmen, the notice to every subdivision D 5 waiting-list applicant, the subdivision D 3 confirmation, the certification of the excess to the Governor, the subsection J line and *"shall accept no further election until the excess is eliminated"* all reached a reinstatement under this release already. **Only the charging rule was missing**, and it is added in eighteen words. Adopting the consequences again by reference would have put two formulations of one concept in one subdivision.

**9. M2's stranded words are cured by deletion.** *"Together with any contingency amount released with it"* pointed at the preceding sentence, which releases only *"the amount settled"*; contingency amounts are released by subdivision G 4's redetermination sentence and by subdivision D 7. **Nothing was ever released with it.** Deleting four words is smaller than redirecting them and loses nothing.

**10. M9 is enacted as an anti-implied-repeal saving, not as a widening.** § 2.2-4026 A grants direct review to any *"party aggrieved by and claiming unlawfulness of a case decision"*, and subdivision M 3 disapplies only Articles 3 and 4 and the two deemed-approval sentences. The enumerated class in M 2's Article 5 sentence was therefore either inert or a silent withdrawal of an Administrative Process Act right, which would need express words. **The saving clause says which**, in one sentence, and it is the act's first citation of § 2.2-4026.

**11. m1 cross-refers § 8.01-2 rather than defining the terms.** *"Minor or … under a disability"* and *"guardian, conservator, committee, or other fiduciary"* were undefined for Title 51.1; § 8.01-2 defines both but opens *"As used in this title."* **A definition written into § 51.1-142.4 A would create a Title 51.1 meaning that could drift from Title 8.01's**, and the concept is the Code's, not this act's. The cross-reference is the smaller change and it is the act's only citation into Title 8.01.

**12. f10-b is enacted in the chapter form, and the Director should know the scope decision was already the law of the act.** The card's drafted sentence named *"the State Police Officers' Retirement System, … the Virginia Law Officers' Retirement System, or … the Judicial Retirement System."* **The definition of *"eligible member"* already provides that it *"does not include a member of a retirement system established under Chapter 2 (§ 51.1-200 et seq.), Chapter 2.1 (§ 51.1-211 et seq.), or Chapter 3 (§ 51.1-300 et seq.)."*** Three names and three chapters coincide today, but a fourth system established under one of those chapters would be caught by the chapters and missed by the names, and two formulations of one concept is a defect. **The enacted sentence uses the chapters**, and it sits in subsection L beside the existing sentence that restates the teacher exclusion the same definition carries — so the structure is the act's own. **It confirms the scope rather than changing it**, and because of that the sister-system question routed to the Statutory Researcher is now moot for this act rather than answered.

**Five more, in brief.** **13.** f7-toll's anchor was reworded to *"a notice required by this subdivision on the death of a member"*, because *"the notice required by this subdivision"* is ambiguous — subdivision G 4 requires five notices. **14.** f3-a's measure has one incomputable side and the cure is drafted and not enacted: § 51.1-163 measures *"any excess of his accumulated contributions **as of the effective date of his retirement**"*, and in a pre-effective-date death that date never arrived; §7 item 129 answer 2. **15.** m4 takes no words: § 51.1-162 B supplies its own age presumptions and expressly disapplies subdivision A 4 of § 51.1-155, and nothing in this revision modifies them — one line for the memo so nobody later reads E1 as changing them. **16.** M7, M8 and F7 are not drafted in; each is a new duty, a numeral that moves time, or a rule about when the Commonwealth pays. **17.** The conforming amendment to § 51.1-162 C is available, is one clause, and is not drafted, because it would add a section to the act's footprint; §5.41 and §7 item 129 answer 7.

### §6.0-61 Ambiguities resolved in store revision 61

Fourteen. **All fourteen in full at** [`moo161-disposition`](/MOO/issues/MOO-97#document-moo161-disposition) **§6. No policy was chosen by drafting choice.** The six a later reader must not undo are these.

**1. The fatal finding was answered by deletion and confinement, not by the carve-out the reviewer offered first.** F2 offered two forms: carve the disapplication (*"except that for the purposes of subdivision C 2 ... as though this sentence had not been enacted"*) or delete it. **Deletion is enacted**, because the citation check shows the disapplication was never load-bearing — § 51.1-163 reaches a pre-effective-date death only by the deeming in § 51.1-165 C 1, § 51.1-165 C 2 and § 51.1-165.01 F, and the sentence's notwithstanding already handles the first and third. **A carve-out would have preserved the words that caused F1.**

**2. The window is stated in D 1's words, not in the reviewer's.** The fix direction read *"after the Board has received a written notification of the member's effective date of retirement given under subdivision D 1 and before the effective date of retirement stated in it."* D 1's certification already says *"after the Board has received the notification of the member's effective date of retirement required by this subdivision and before that date,"* and **the act may not use two formulations for one concept.** The enacted words are D 1's, with *"this subdivision"* becoming *"subdivision D 1."*

**3. Confining the sentence is treated as restoring the agreed scope, not as deciding a policy.** A fatal finding may not be resolved by drafting choice. This one is not: the Director's answers (d), (f) and the certification all speak to the member who has filed her § 51.1-153 notice and not yet retired, and the sentence's reach beyond that window was an artefact of how store revision 58 was cut. **The wider alternative — keeping the disapplication and confining it instead to a member who has not retired — is drafted at §7 item 128 and is not enacted.**

**4. The release trigger's second branch needed a date and the card did not state one.** The Director's answer fires the release *"where no retirement allowance is payable ... because no such allowance is payable to any person"* — a case in which there is no election to date it from. The enacted words run it from the Board's determination that no such allowance is payable, on the model of every other period in this subdivision. **Without a date the duty would have had no deadline, which is an unenforceable duty.**

**5. F6's certification wording states C 2's payee by cross-reference and names nobody.** The reviewer's fix direction ended *"to the person entitled to it under the provision under which the greater benefit is determined"* — a payee rule. **That rule is F3's question and F3 is on the card**, so the enacted proposition says only that each of C 2's two benefits is *"payable to the person entitled to it under the provision under which it is determined"*, which is a statement of existing law and not a direction to pay anybody. **The certification is now accurate about a question the operative text has not yet answered, and §7 item 128 is where that is answered.**

**6. F14 is enacted as to the rider only.** The notice rider now reaches *"the amount of any benefit payable to that person"* as well as entitlement, so the Board is no longer compelled to state a figure it does not have. **The reviewer's companion cure — a supplemental notice with a fresh review period where the Board later determines an amount differently — is a new duty that was not agreed, and is drafted at §7 item 128 instead of enacted.**

**Two findings declined, with reasons.** **F16** (the deemed determination as a tolling lever) is declined on the reviewer's own analysis: M 2 caps the aggregate of all tolling at 120 days and denies tolling to a second request on the same determination, the cap holds, and the cost of closing the residue exceeds the exposure. **F21** (the new class reaches notices required by *"this section"* while M 2's tolling sentence reaches periods under § 51.1-142.2 as well) is declined because the cure would **widen** a class this revision narrows for F8, in the same breath and for the sake of symmetry alone. **Both are recorded so that neither is re-run as new.**

### §6.0-60 Ambiguities resolved in store revision 60

**Every one of the Director's eight answers is enacted as given. Four things inside those answers are mine, and they are listed first.**

1. **Item 117(a) is wider than the carded words, deliberately.** The card read *"an application filed **within a period set forth in** subsection A or B of § 51.1-156."* Enacted: *"an application **the filing of which did not require a waiver of** a ninety-day notification period set forth in subsection A or B of § 51.1-156."* The carded form reaches only the member inside the ninety days after termination. **It misses the purest class-4 case of all:** a member whose final qualifying retirement date passes while she is **still in service** — she has not retired at all, which is why subdivision 2 reduced her — and who then applies for a disability retirement allowance as *"[a]ny member in service"* under § 51.1-156 A, for whom **that subsection sets no period**. She needs no waiver, she broke no deadline, and on the carded words she was excluded while a member who filed eight months late was rescued. The enacted form is defined by the thing the class has in common — that no waiver was needed — and reaches both.

2. **Item 117(b) anchors on clause (ii) alone and not on the whole of subsection H.** § 51.1-156 H's mandatory limb has two conditions: (i) the member *"would otherwise qualify for disability retirement but for failing to comply"*, and (ii) the Medical Board's certification of three facts. **Clause (i) is supplied by the approval itself** — the trigger operates only where the member *"is thereafter approved for a disability retirement allowance"*, and a member who is approved has otherwise qualified. Anchoring on both would have made the Board prove a condition its own approval had already decided. **This is the point of the finding:** the enacted trigger is a **fact the Board can see in its file**, not a legal conclusion about what the Board *"was required"* to do.

3. **No express subsection J report line was drafted for item 103's determination, and no fallback was drafted for pass 17's M-9 — and the second of those is a decision, not an omission.** J 1 already reports *"every failure of the Board to make a determination, or to give a notice, within a period required by this section, stated separately for each provision"*, so an express line would be surplusage. **M-9 is CLOSED and needs no text.** It was held to item 103 on the ground that the redetermination clock has no fallback where the Board never makes the error determination. With item 103 enacted the gap is **self-consistent and remediable**: the clock sentence opens *"Where the Board rescinds a determination"*, and the rescission cannot occur without the determination, so a fallback date would start a clock that never runs. What the member needed was a **remedy for the absent determination**, and item 103 gives her one — a 30-day period, a notice duty, review under subsection M 2's failure limb, judicial review under Article 5, and a line in the J report. **Drafting a deemed determination instead would have been a policy choice nobody made.**

4. **Item 120(b) is enacted as a conjunctive duty, not as an exception.** The carded repair was *"the same words R2 enacted in the rescission branch"* — an *"except that where the member has died"* clause. **In the death branch the member has always died**, so the condition is always true and the exception form is nonsense. Enacted: *"and shall pay the whole of that refund to the member's estate … and shall apply no amount of it to the purchase of service credit."* The form also cures **pass 18's M18-3** as a by-product: as an exception restating the verb without a period, the death refund could be read to carry away the main clause's **60-day deadline**; as a conjunctive duty it cannot, and the estate keeps the deadline.

**Five further choices, none of which changes which member passes either definitional test.**

5. **Item 114's amendment leaves the two existing *notwithstanding* clauses standing.** They become surplusage. Deleting them would be tidier and would re-open the argument the amendment exists to foreclose — that the bar was never meant to catch these cases at all — and store revision 52 legislated twice on the strict historical-fact reading. **Surplusage is the cheaper of the two risks.** The record states it so a reader does not take the redundancy for a drafting slip.

6. **Item 114's *"in full"* is confined to the whole-reservation release and that is what makes it operative.** D 7 releases *"to the extent of any reduction"* on a D 6 recertification and releases the whole reserved amount in its other five limbs. Had the amendment read *"released in accordance with subdivision D 7 and has not been reinstated"* it would have cured nothing for the D 6 member, because her partial release is never reinstated — it was correct.

7. **Item 118(b)'s long-stop is the last sentence of J 1 and reads on *"report under this subdivision."*** The card attached it to limb (a) of the first sentence. Placed there it would not have reached the **third** sentence's further report, which has its own trigger, and the duty would still have been interminable on the facts item 118 describes. As the closing sentence it bounds **every** report J 1 requires, which is what the card's stated purpose — *"makes the duty terminable whatever happens"* — asks for. It is confined to *"this subdivision"*, so J 2 and J 3 are untouched.

8. **Item 103's route is confined to the period after a determination under subdivision 2 or 3 has taken effect.** Before that moment the Board is already under a **60-day** duty to determine whether clause (iii) applies, with a 15-day notice duty, a J report line and review under subsection M; an unconditioned member-filing route would have put a **second clock on one determination**, which is pass 18's M18-9. The gap the Director's answer was aimed at is the **later** determination in the rescission sentence — the one with no period, no route and no notice — and the enacted sentence reaches exactly that. **No conforming limb is needed to connect it to the rescission:** the rescission trigger reads *"or the Board thereafter determines that the member was unable to retire in a qualifying retirement by reason of an error of the Board"*, which the new determination satisfies on its own words, and the redetermination clock already runs *"from the date on which … the Board makes the determination stated in this subdivision."*

9. **Item 120(a) is enacted although pass 18 shows its stated premise is false, and the part that would actually fix the problem is carded.** The card's ground was that *"G 4 credits the whole purchase on clauses (ii) and (iii) too."* It does not: G 4's crediting duties are confined to **death** and to the **rescission** branch, and clause (ii) switches off G 3's partial-crediting duty along with subdivisions 2 and 3. So for a member approved for a disability retirement allowance **before** completing payment, with no prior determination, there is **no crediting duty to lift a bar in front of**. The amendment is still right on its own terms — E's death-only exception conflicted on its face with G 4's unqualified *"Subsection E does not prevent the crediting of service credit required by this subdivision"* — and it is enacted on that narrower ground. **The crediting duty is §7 item 126**, drafted in full, enacted nowhere, and recommended: it decides what a partial payer is credited with and what she is refunded, which is a money question and the Director's.

### §6.0-59 Ambiguities resolved in store revision 59

**1. Option (d)'s class list was five revisions out of date, and carrying it verbatim would have reversed another revision's cure.** §7 item 88's option (d) was drafted in store revision 53 and opened *"Any member, retiree, beneficiary, or applicant."* Store revision 58 then widened subdivision M 2's class to six in **both** of its occurrences — adding *"personal representative of a deceased member's estate, or other person to whom this section requires a notice to be given"* — and one of the two **was** the judicial-review sentence (§5.37). **Resolved by enacting (d) with M 2's own six-class list.** The alternative was to enact the drafted words and silently take the Article 5 right from the rejected claimant and the subdivision B 4 e employer, which is a policy change nobody directed. *"Any member"* became *"A member"* for the same reason — it is how M 2's own first sentence opens, and the chapter should not have two forms for one class. **I regard this as conforming and not as a policy choice**, and it is flagged at item 88 so the Director can reverse it if the narrowing was intended.

**2. The limb and subdivision M 3 overlap, and the overlap is kept rather than cured.** § 2.2-4021 is in Article 3, so item 88's limb disapplies it to a reconsideration, and M 3 then disapplies its deemed-decision sentences *"to a determination of the Board under this section or to a reconsideration under subdivision 2."* **Resolved in favour of keeping both**, for three reasons: both were directed in those words; M 3's other half — determinations generally — is where counsel found the exposure **already live** and the limb does not reach it; and M 3 survives the removal of the limb, which is the thing most likely to be revisited. **The cost is a negative-implication argument** that a reader could build out of M 3 naming reconsiderations at all. I think it fails, and it is carded at item 123 with the one-substitution cure rather than resolved by me.

**3. The two 15-day clocks nearly duplicate an existing one, and both are kept.** Subdivision D 3's fifth sentence already requires the Board to *"act upon the application no later than 15 days after the confirmation is obtained."* The new D 1 sentence requires the certification to be **given** within 15 days of the same trigger. **Resolved by keeping both:** same period, same trigger, different act — *giving the certification* is what subdivision D 1 makes the condition of acceptance, and *acting upon the application* is the accept-or-wait-list decision. They cannot conflict. **Collapsing them into one would have required choosing which act the single clock governs, and that is a policy choice I was not given.**

**4. Where the deadline runs from, in subdivision J 1's new trigger.** The drafted form ended *"no later than the first December 1 following **it**"*, where *"it"* had two candidate antecedents — the rescission and the matter. **Resolved by naming them:** *"following that rescission or the date on which that matter arises, as the case may be."* A matter *arises* on a date and a rescission *occurs* on one; the two verbs are not interchangeable and the deadline needs a date for each. **No change of substance, recorded because it is a departure from text the Director approved.**

**5. Which sentence of subsection C carries the report duty — and the fact that I had it wrong.** Items 108 and 109 and [`moo153-counsel-disposition`](/MOO/issues/MOO-145#document-moo153-counsel-disposition) §4 all called it the *"seventh"* sentence. **It is the eighth.** The sixth and seventh are the two boundary sentences — the characterisation boundary from store revision 48's edit 2, and the world-side boundary from pass 16's M-3 — and item 111, in the same document, numbered them correctly, so §4 was internally inconsistent. **The amended words were never in doubt**, because the target was identified by quotation and not by ordinal, and that is the whole argument for quoting. **Resolved by amending the sentence that contains the quoted words and correcting the label in both places.**

**6. Whether to record the disagreement on item 88 in the bill or only in the item list.** The Director's answer took the optional limb over a recommendation I had withdrawn on counsel's objection. **Resolved by recording it in both, in the §2 plain-English row, in §0.0-59 c and at item 88 — with the cost stated and not netted away.** A later reader of the bill alone must be able to see that disapplying Articles 3 and 4 removes the member's informal-fact-finding and formal-hearing rights in the reconsideration, that counsel objected, and that the direction was the Director's. **It is not my place to re-litigate it and I have not; it is my place to make sure nobody has to discover it.**

**7. What the document split is, and what it is not.** Item 112 directed the split *"before anything leaves Paperclip."* **Resolved by treating it as a document boundary and not as a control.** Both documents are internal issue documents on the same issue and anyone who can read one can read the other. The honest statement of the benefit is that releasing the bill text is now a separate act from releasing the item list; the honest statement of the limit is at item 125, which asks the release question I cannot answer.

### §8 status notes for store revisions 62, 61, 60, 59, 58 and 57

> **STORE REVISION 62 — [MOO-169](/MOO/issues/MOO-169)'s COUNSEL PASS DISPOSED AND THE POLICY DIRECTOR'S SEVEN
> ANSWERS OF 12 OCTOBER 2026 ENACTED. Twenty-one substitutions in subdivision D 1, subdivision G 4,
> subsection L, subdivision M 2 and subsection N of § 51.1-142.4. No figure moves, no designator is
> renumbered, no section joins or leaves the act, no defined term is added, and the title line does not
> change.** Record: [`moo169-disposition`](/MOO/issues/MOO-97#document-moo169-disposition). Narrative
> §0.0-62; sweep §5.41; drafter's note §6.0-62; the carded answers §7 item 129. Cut and applied on
> [MOO-97](/MOO/issues/MOO-97).
>
> **The fatal finding, cured by taking the window out.** Store revision 61 confined the death-benefit
> sentence to the window between the Board's receipt of the member's § 51.1-153 notice and her effective
> date of retirement. **A member who is out of service after an involuntary separation, whom subdivision
> D 1 expressly tells she need not file that notice early, and who dies before filing, fell outside it** —
> so the in-service waiver never reached her, § 51.1-162 B was unavailable, and § 51.1-162 A paid her
> survivor a refund of contributions while the Commonwealth settled and paid the certified subsidy on the
> date of her death. **The window is deleted**; the sentence is conditioned on the member not having
> retired before the date of death, which is the carve-out clause (i) already uses, and that cures **F1**
> and **F2** together. It **restores answer (f) as the Director approved it** — the confinement was the
> drafter's, not the Director's.
>
> **Three compelled propositions of law were wrong and are now right.** § 51.1-165 **C 2** switches to
> § 51.1-162 B **only where the contingent annuitant and the § 51.1-162 B payee are the same person or
> persons**, and the certification's *"each payable to the person entitled to it under the provision under
> which it is determined"* described a mechanism the Code does not have (F9). § 51.1-162 **B** pays a
> **designated** spouse, minor child or parent, or, absent a designation, in the order of precedence it
> states — survival alone is not enough, so a member who designated her sister in 2009 and is survived by
> her mother gets nothing from the purchase (F10). § 51.1-162 **C** requires death **in service** (M6).
>
> **The remedy for an incomplete certification now works for the living member**, who is the person most
> adversely affected by one: it reaches every matter the subdivision requires, names subdivision M 2's own
> category, runs her 30 days from the certification she actually received, and expressly disapplies M 2's
> second sentence so there is one window and not two (F5, m2). M 2's third window, which was **empty
> everywhere but subdivision D 1**, now carries the chapter's own 30 days (F6).
>
> **The reconsideration class is widened, with the boundary store revision 61 was reaching for.** Standing
> had turned on the Board having already decided against the claimant, so the Board could defeat review by
> never deciding, and the same narrowing stripped the **court-appointed conservator** whom the same
> revision had made the addressee of the death notice (F3, F4). Both class lists now name *"person who
> **has** claimed any benefit payable on the death of a member"* and *"person to whom this section requires
> a notice to be given **in respect of a benefit payable on the death of a member**."* The public and the
> money-committee Chairmen stay out, on the face of the act.
>
> **The $3,000,000 bar is made arithmetically honest in two of three places.** A reinstated settled amount
> is now charged against the subdivision D 2 limitations notwithstanding that the amount available is
> thereby exceeded (F8); the release cannot be required twice of the same amount (M3); and four stranded
> words are deleted (M2). **The third is not cured and is the Director's**: subsection N fixes no time for
> payment while subdivision G 4 settles on the date of death, so whether a subsidy that buys no benefit
> comes back to the cap is unregulated (F7).
>
> **The Director's seven.** The greater-of's **measure** and its **payee**; the **§ 51.1-162 C waiver
> period**, which the act's own clocks could destroy before the Board's notice of it arrived — **the act's
> first operative override of a period stated in a section this act does not amend**; a **further notice
> with a fresh review period** where an amount is later determined differently; **lateness reviewable for
> 30 days after it is cured**; the express statement that a **§ 51.1-162 death benefit is not charged
> against the subdivision D 2 limitations**; and the **confinement of the Program to Chapter 1 members**,
> enacted in subsection L in the chapter form the definition of *"eligible member"* already uses — which
> means the scope decision was already the law of the act and the sentence confirms it.
>
> **Not here, and on the Director's card at §7 item 129:** subsection **N's payment timing** (F7), the
> **§ 51.1-163 valuation date** without which the approved measure has one incomputable side, F5's
> **discovery rule**, F10's **designation-review advisory**, **M7**'s death-identification duty, **M8**'s
> Board-operated tolling channel, and the **conforming amendment to § 51.1-162 C**. **Four of the seven
> decide who bears a loss and none is picked.** Still open and not re-asked: §7 item 60's (a), (b) and (c)
> — the elected-option class whose contingent annuitant is a sibling, an adult child or an unmarried
> partner — and the five unenacted answers at item 122.
>
> **Next step: an adversarial pass on these twenty-one substitutions, and then the Director's card.** They
> have had none, they are the widest this subdivision has taken, and **the last three passes on it each
> returned a fatal finding.**

> **STORE REVISION 61 — [MOO-161](/MOO/issues/MOO-161)'s COUNSEL PASS DISPOSED AND THE POLICY DIRECTOR'S FIVE ANSWERS ENACTED.
> Thirteen substitutions in subdivisions G 4, D 1 and M 2 of § 51.1-142.4. No figure moves, no designator is
> renumbered, no section is added or deleted, no defined term is added, and the title line does not change.**
> Record: [`moo161-disposition`](/MOO/issues/MOO-97#document-moo161-disposition). Narrative §0.0-61; sweep §5.40; drafter's note §6.0-61; the seven drafted answers §7 item
> 128. Cut and applied on [MOO-97](/MOO/issues/MOO-97).
>
> **The fatal finding, cured by subtraction.** Store revision 58's freestanding *"§ 51.1-163 shall not apply
> to the member's death"* reached a member who retired in a qualifying retirement on a basic allowance and
> died years later in retirement, and forfeited her unrecovered contributions to the trust fund — on the
> reviewer's facts $122,000 owed to a brother. **§ 51.1-163 is captioned *"Death after retirement"* and
> cannot reach a pre-effective-date death of its own force**, so the disapplication was never load-bearing:
> it is **deleted**, and the sentence is **confined to the notification window** in D 1's own words. That
> cures **F1** and **F2** together, and restores the agreed scope rather than choosing a policy.
>
> **Three compelled propositions of law were wrong and are now right.** § 51.1-162 C pays a spouse, **minor
> children and parents** (F4); § 51.1-162 A's condition is *"no benefits are payable under subsection B"*
> and **does not mention subsection C** (F5); and subdivision C 2 of § 51.1-165 entitles the contingent
> annuitant on **one of its two limbs only**, with an in-service condition the certification had suppressed
> (F6). **An incomplete certification is now a *failure* of the Board** whose review period runs 30 days
> from the G 4 death notice, which is the first writing the person adversely affected ever sees (F9).
>
> **The reconsideration class is narrowed because it had no boundary**: *"other person to whom this section
> requires a notice to be given"* reached **the public**, through subsection K's public notice, and the two
> money-committee Chairmen. Both of subdivision M 2's class lists now name the **rejected claimant** and the
> **paying employer** expressly (F8, F19, F20).
>
> **The Director's five.** A 30-day duty on the employing **state agency** to report the death, with a
> subsection J line; the **90-day redetermination** run from the date the Board learns of the death; the
> release fired where **no allowance is payable at all** and restoring to the $3,000,000 limitation **only so
> much as has not been paid under subsection N**; and **reinstatement** of a released amount where the
> determination is reversed on review.
>
> **Not here, and on the Director's card at §7 item 128:** **F3** (the greater-of's measure and payee —
> three payees and no basis of comparison), **F7** (the § 51.1-162 C waiver that can expire before the
> Commonwealth's notice of it arrives), **F10** (whether a State Police, VaLORS or JRS member is in this
> Program at all — also with the Statutory Researcher), **F11**, **F14's** supplemental notice, M 2's
> lateness-after-cure, and F8's gated alternative. **F16 and F21 are declined with reasons at §6.0-61.**
>
> **For the memo's risk section:** F1 and F11 together (the legal and fiscal sides of one clause), F7 and
> F8. **For the Fiscal & Impact Modeler:** the reviewer's structural challenge — not a number in the model
> but the assumption underneath it, that every cost of the act flows through the certified subsidy. F1's cure
> restores that assumption; the residue is the C 2 greater-of, at about one case every three years.


> **STORE REVISION 60 — [MOO-64](/MOO/issues/MOO-64)'s EIGHT ANSWERS OF 12 OCTOBER 2026 ENACTED IN
> THIRTEEN SUBSTITUTIONS IN FIVE PROVISIONS.** Items 114, 115, 116, 117, 118, 119, 103 and 104 are
> enacted, and of the cheap bundle 120(a), 120(b) and 121's subsection M 2 limb; **the interest limb was
> not selected and is not in the text.** The five provisions are the definition of *"unreduced retirement
> eligibility date"* in subsection A, subsection E, subdivision G 4, subdivision J 1 and subdivision M 2
> of § 51.1-142.4. **No figure moves, no designator is renumbered, no section is added or deleted, no
> defined term is added, and the title line does not change.** Narrative **§0.0-60**; sweep **§5.39**;
> drafter's note **§6.0-60**. **The closures for items 114 to 121, 103 and 104, and two new items 126 and
> 127, are in [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list)**, where store
> revision 59 moved the §7 list. Record, with every FIND and ENACTED string verbatim:
> [`moo64-rev60-record`](/MOO/issues/MOO-42#document-moo64-rev60-record).
>
> **This is store revision 60, not 59, and the items are 126 and 127, not 123 and 124.** A concurrent run
> published store revision 59 under this cut — the §7 split and the answers to items 88 and 108 to 113 —
> and **item 113's enactment changed one of this revision's own anchors**, J 1's further-report sentence,
> which was re-anchored before item 118(b) was applied. **Store revision 59 touched none of the other
> twelve anchors and nothing in it is reversed, re-opened or renumbered.** §0.0-60 states it in full.
>
> **What the thirteen do.** The **settlement bar is amended once** instead of carrying a *notwithstanding*
> for each rescission route, which closes the two doors that still reached its D 7-release limb — the
> member whose purchase is reduced on a D 6 recertification and who then dies, and the
> involuntary-separation rescission. The **reversal sentence no longer commands settlement where none is
> due**. The **arrears formula is net rather than gross**, with a limb for a determination reversed in its
> entirety. The disability carve-out now reaches the member who **filed on time**, and its trigger is the
> **Medical Board's certification** rather than a counterfactual about what the Board was required to do.
> **Disability-application pendency counts against the 120-day aggregate**, and **J 1 has a twenty-year
> long-stop**. The § 51.1-155.1 confinement gains the **missing temporal rule**, so the member
> involuntarily separated at 50 can take the retirement G 4's hardship branch requires of her. The member
> may now **file written evidence of an error of the Board** and oblige a determination within 30 days,
> reviewable under subsection M. **J 1 reports reversals, restored credit and every amount paid or
> refunded.** Subsection E's crediting exception names the disability and error cases; the **death
> branch's refund no longer buys service credit for a dead member**; and **subsection M 2 reaches a
> failure to make a payment.**
>
> **Four wording changes inside the Director's answers are mine** and are at §6.0-60 items 1 to 4: item
> 117(a) is **wider** than the card, because the carded words missed the member still in service, for whom
> § 51.1-156 A sets no period at all; item 117(b) anchors on **clause (ii) alone**, the approval supplying
> clause (i); item 120(b) is a **conjunctive duty rather than an exception**, which also cures pass 18's
> M18-3; and item 103's route is **confined to the period after a determination has taken effect**, so one
> determination does not acquire two clocks. **Pass 17's M-9 is CLOSED with no text, and the reason is at
> §6.0-60 item 3.**
>
> **What is NOT done.** **[MOO-156](/MOO/issues/MOO-156)'s pass 18 — 6 serious, 11 moderate, 3 minor on
> store revision 57's six repairs — is NOT dispositioned.** Eighteen of its twenty findings are read and
> unanswered and are the next cut's work. **One of them, S18-6, defeats the stated premise of item 120(a),
> which is enacted anyway on a narrower ground, with the part that actually fixes the problem carded as
> §7 item 126 and enacted nowhere.** **These thirteen substitutions have had no adversarial pass of their
> own** — that is [MOO-167](/MOO/issues/MOO-167).
>
> **Internal working draft. Not a Division of Legislative Services bill. Not reviewed by counsel or by DLS.
> Pre-decisional.**

> **STORE REVISION 59 — THE POLICY DIRECTOR'S SEVEN ANSWERS OF 12 OCTOBER 2026 ENACTED. Five
> provisions of § 51.1-142.4 amended, one new subdivision M 3, item 111 declined, and §7's item list
> split into its own document. No figure moves, no designator is renumbered, no section joins or
> leaves the act, no defined term is added, and the title line does not change.** Narrative
> **§0.0-59**; sweep **§5.38**; drafter's note **§6.0-59**. Dispositions at items 88, 108, 109, 110,
> 111, 112 and 113 of [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list).
> Answered and applied on [MOO-145](/MOO/issues/MOO-145).
>
> **The thing this revision fixes.** Subdivision D 3 must now **file** the Department of Planning and
> Budget request within 15 days of a completed application, and subdivision D 1 must **give** the
> certification within 15 days of the confirmation. Before them the Board could meet every period the
> section stated and still strand an eligible member for ever, because D 1 bars acceptance until the
> certification issues and nothing required it to issue. The existing 90-day applicant notice now
> fires at about **day 105** instead of never. Subsection C's reporting duty reaches a failure **to
> state**, and subdivision J 1's post-terminal further report has an **independent trigger** so a
> matter arising after the last report has somewhere to go without a rescission.
>
> **Item 88 is answered (d) WITH the optional second limb, over my own withdrawn recommendation, and
> the cost is stated and not netted away.** The completed reconsideration is a § 2.2-4001 case
> decision **by statute**, which answers pass 15's S-3 at the root — § 2.2-4026 A needs a case
> decision and a savings clause cannot create one. **But disapplying Articles 3 and 4 removes
> § 2.2-4019 informal fact finding, § 2.2-4020 formal hearings and the hearing officer from the
> reconsideration.** Counsel objected that this strips the member of hearing rights the bill exists to
> confer; I accepted that and withdrew my recommendation in store revision 56; **the Director's
> direction overrides it, which is the Director's to do.** M 2's own floor — 30-day window, written
> reasons, 90-day duty to act, tolling — is what remains. **One conforming change was not optional:**
> option (d)'s drafted class named four, and store revision 58 had widened M 2's class to six in both
> occurrences, one of which was this very sentence — so the six-class list is carried in rather than
> dropped (§6.0-59 ambiguity 1).
>
> **New subdivision M 3** disapplies § 2.2-4021 B's and C's deemed-decision sentences to a
> determination under the section and to a reconsideration, so agency silence cannot award a subsidy
> against the $170,000 and $3,000,000 limits. § 2.2-4021 read at source: it is in **Article 3**.
>
> **What is NOT done, and one of them is a gap this revision opened.** **Item 124:** because Article 3
> contains § 2.2-4021, the limb and M 3 together mean a reconsideration the Board never completes
> produces **no case decision at all**, so there is no Article 5 route — a position that was uncertain
> before and is now settled against the member by two express exclusions. The cure is drafted at item
> 124, recommends a deemed **denial** on the 91st day rather than a deemed win, and **is not enacted**.
> **Item 123** is the limb/M 3 redundancy. **Item 125** asks what happens to the item list on release.
> **Item 111 is declined**, so counsel's M-2 stands as an accepted cost. **And the eight substitutions
> of store revision 58 still have no adversarial pass of their own.**
>
> **§7 is now [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list).** This
> document went from 510,963 characters to **249,041**, of which §1 is 112,886 — about 275,000
> characters of headroom against the 524,288 ceiling, and the end of the pressure that forced seven
> record moves since store revision 33. **The split is a document boundary, not a containment
> control.**
>
> **Internal working draft. Not a Division of Legislative Services bill. Not reviewed or cleared by
> counsel or by DLS. Not legally sufficient for introduction. Pre-decisional and internal. Nothing in
> store revision 59 is cleared for external use.**


> **STORE REVISION 58 — [MOO-154](/MOO/issues/MOO-154)'s COUNSEL PASS DISPOSED. Eight substitutions in
> subdivisions G 4, D 1 and M 2 of § 51.1-142.4, answering eleven of sixteen findings. No figure moves, no
> designator is renumbered, no section is added or deleted, no defined term is added, and the title line
> does not change.** Record: [`moo154-disposition`](/MOO/issues/MOO-97#document-moo154-disposition).
> Narrative §0.0-58; sweep §5.37; drafter's note §6.0-58; the nine drafted answers §7 item 122. Cut and
> applied on [MOO-97](/MOO/issues/MOO-97).
>
> **The fatal finding.** (f)'s notwithstanding reached subdivision C 1 of § 51.1-165 and **not subsection F
> of § 51.1-165.01**, which routes the same death to § 51.1-163 by its own force — so for every member who
> elects the partial lump sum the act did nothing, while the certification compelled the Board to tell her
> that no such option governed her death benefit. The notwithstanding now names **so much of subsection F as
> requires payment under § 51.1-163**, which leaves that subsection's own disapplication of the in-service
> requirement working for the member. **§ 51.1-165 C 2 is preserved rather than displaced**: the act pays the
> greater of C 2's benefit and (f)'s, so no member is worse off than under present law.
>
> **What else is in the text.** *"As on the death of a member in service"* is given the Code's own hook —
> § 51.1-165.01 F's *"the requirement that the member be in service shall not apply"* — because neither term
> is defined in § 51.1-124.3. The computation base becomes *"taking account of"* the credited service rather
> than *"on"* it, which was reading the allowance onto the purchased months alone and gave a widow about
> one-fourteenth of it. **Three of the certification's four compelled propositions of law were wrong** and are
> restated: only C 1 is displaced, § 51.1-162 B is also conditioned on § 51.1-162 C, and a death compensable
> under the Virginia Workers' Compensation Act is governed by § 51.1-162 C and not by A. The certification
> gains a **consequence** — a determination for subsection M and a line in the subsection J report — because
> the issue's premise that D 1's day-for-day extension carried it was wrong. The notice is owed to **each**
> person entitled, its period no longer vanishes when crediting is late, it starts afresh for a person
> identified later, and it may no longer state a period § 51.1-162 does not contain. **Subdivision M 2 now
> reaches any person the section requires a notice to be given** — the rejected claimant and the B 4 e
> employer, each of whom the act hands a notice and neither of whom could use it.
>
> **What is NOT done.** **F5, the ERF residual this issue was opened on, is not closed** — subsection E's
> second limb may leave the survivor a reduced allowance the Commonwealth priced as unreduced. It and eight
> more are drafted in full and enacted nowhere at §7 item 122; four of the nine decide who bears a loss.
> **These eight substitutions have had no adversarial pass of their own.**
>
> **Internal working draft. Not a Division of Legislative Services bill. Not reviewed by counsel or by DLS.
> Pre-decisional.**


> **STORE REVISION 57 — [MOO-152](/MOO/issues/MOO-152)'s PASS 17 DISPOSITIONED. Six substitutions in
> four provisions of §1, four record corrections, no policy enacted, no designator renumbered, nothing
> added to or removed from the act, the title unchanged, and no figure moved.** Subdivision G 3 and
> subdivision G 4 carry the repairs; **subsection E is named but not amended**; the two definitions are
> untouched. Narrative **§0.0-57**; sweep **§5.36**; note **§6.0-57**; carded findings **§7 items 114 to
> 121**. Record: [`moo152-pass17-disposition`](/MOO/issues/MOO-42#document-moo152-pass17-disposition).
>
> **Pass 17 returned 0 fatal, 8 serious, 9 moderate, 5 minor** on store revision 52's thirteen edits,
> verified all thirteen present in the live store as carded, re-opened § 51.1-156 H, A, B and D
> verbatim, replicated the engine's `g4_exposure` to the digit, and found **no constitutional defect**
> on single object, special legislation, Dillon's Rule, delegation, vagueness, takings or contract
> impairment.
>
> **Every repair is to words the Director's own answers put in**, and none changes which member passes
> either definitional test: a **payee** for the subdivision-3 rescission refund where the trigger is
> death, with its adverse-tax fallback yielding to that case; a reinstatement **deadline that is not
> already past**; the **two fallbacks subdivision 2 already has** for arrears on a reversal; item 96
> made **operative** at last, subsection E having carried the same deeming bar independently; and the
> authorised offset made **reciprocal** and stated as a **power**.
>
> **What is NOT here. No serious finding is cured.** S-1 — the settlement bar's release limb, reached by
> a member whose purchase is reduced on a D 6 recertification and who then dies — **is the fatal item 89
> cured through a different door, and it is carded as item 114 rather than fixed silently**, because
> amending the bar settles subsidies the bar on its face refuses and that spends money. **Publication is
> blocked on items 114, 115, 116 and 117**, the four pass 17 would not publish without. **M-9 is held to
> item 103** and **m-5 needs no edit**. **Item 105 is CLOSED** — the enacted arrears formula stands and
> its residual defect is item 116.
>
> **One claim of this record is withdrawn.** *"No priced quantity moves"* does not survive: the
> admission half is **sound and independently verified**, the settlement half is not. **The only
> statement authorised from here:** *no admission quantity moves; the settlement count moves upward by
> an amount the current engine cannot value.* The re-run is requested, not asserted, and **no figure in
> the package is restated**. **The six new strings have had no counsel pass of their own.**
>
**§8's status note for store revision 56 is moved verbatim** to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2) **by store revision 61**, where a reference of the form *"§8's note for store revision N"* still resolves. §8 retains the five most recent: 61, 60, 59, 58, 57. **Nothing is rewritten or summarised away, and §1 is untouched by the move.**

**The status notes for store revisions 55, 54, 53 and 52 are moved verbatim** to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2) in store revision 60, every blockquote, figure and caveat preserved, so a reference to the status note for any of those revisions still resolves there. **§8 now carries store revisions 60, 59, 58, 57 and 56** — the current note and the four before it, which is the retention this subsection states.

---

## Moved in store revision 73 of `bill-text-s8` — sweeps §5.43 and §5.44, drafter's notes §6.0-63 and §6.0-65

**Moved verbatim and in full.** `bill-text-s8` arrived at store revision 73 with 21702 characters of headroom against the 524,288-character ceiling and could not take that revision's record layer. These four blocks are the ones §5's and §6's own preambles had already named as next to move. Nothing below is rewritten, abridged or summarised; each block left a stub in the bill naming its durable result and pointing here. **These are dated per-revision records: every figure in them is the figure as at the revision named in its own heading, and a later revision may have superseded it. The live record is in `bill-text-s8` itself.**

### §5.44 Store revision 66 — the two insertions and sixteen substitutions, chased in both directions

**Result: four conforming amendments were required and all four are enacted in this revision; after them nothing is stranded.** Counts are taken over **enacted §1** of the body that was written, not predicted, and the before-counts were taken on store revision 65 (document revision `bc0576f5`) at the moment of application.

**Direction 1 — what the new words cite, and whether the act says it in its own words.**

| Cited or used | Occurrences in §1 | Result |
|---|---|---|
| **subdivision G 1** (in the deeming sentence) | **7** before, **8** after | Accurate and already the act's own form. Subdivision G 1's third sentence is one of the commanded releases the deeming sentence has to reach: *"The Board shall release the amount by which the amount reserved for the election … exceeds the amount settled."* §1 cites G 1 by this exact form seven times already |
| **subdivision D 3** (in the deeming sentence) | **3** before, **4** after | Accurate. D 3's third sentence commands *"the Board shall release it when the certified subsidy is settled under subdivision G 1 or G 4 or the reservation is released under subdivision 7"* — a release on none of D 7's grounds, which is why it is named |
| *"by this subdivision"* (the deeming sentence's reference to G 4's own releases) | the act's standing form, unmoved | G 4 refers to itself as *"this subdivision"* throughout. **It carries two commanded releases**: the redetermination release (the same words as G 1's, lower-cased and joined by *"and"*) and the death-case release. The general words reach both; see *"including"* below |
| *"required or permitted"* | **1** before, **2** after | **Not new — it is the act's own existing word pair**, already in subsection F: *"Nothing **required or permitted** by subdivision G 2, G 3, G 4, or G 5 …"*. Deliberately a pair: *"required"* alone would have left out any release the act **permits** without commanding, and the exclusion would have been silent. §6.0-66 item 2 |
| *"For the purposes of the next sentence"* | **0** before, **1** after | New, and it is the scoping device the whole edit depends on. Checkable on its face and self-limiting. §6.0-66 item 1 records the one fragility and why it was accepted |
| **subsection A of § 51.1-142.4** (in the new B 4 a definition) | **1** before, **2** after | **The form is already this act's own for exactly this cross-section reference:** subdivision B 4 f of § 51.1-142.2 already reads *"a notice being given for the purposes of this subdivision as provided in **subsection A of § 51.1-142.4**."* So § 51.1-142.2 already cites that subsection by this form, and the new definition matches it. Not a paraphrase and not a bare section cite |
| *"state agency"* / *"state agencies"* / *"State agency"* | **12** before, **34** after (lowercase singular **11 → 31**, plural **0 → 1**, capitalised defined-term form **1 → 2**) | **The act's own defined term, already used as an operative noun eleven times** before this cut — including subsection I 1's *"performs services for a state agency"* and I 2's *"A state agency shall report to the Board"*. The substitutions use the same noun in the same case and introduce **no second word for one concept**. The one new plural is subsection J 1's conformed report content |
| *"from whose appropriation an amount was paid"* | **0** before, **10** after | New, and counsel's suggested words. It names the fund the money came out of, which is the fact that decides who is owed a refund and who may seek review. §6.0-66 item 6 |

**Direction 2 — what cites the things the new words are inserted into, and what the substitutions stranded.**

| Provision | What it reaches | Moved by this revision? |
|---|---|---|
| The reinstatement sentence of subdivision G 4 | the sentence the deeming provision scopes | **Not one character.** The deeming sentence is inserted **before** it and changes none of its words. Both of its occurrences of `otherwise than in accordance with subdivision D 7` stand, which is the point of choosing deeming over the alternative affirmative trigger |
| The settlement bar — *"No certified subsidy is settled under this subdivision after the reservation … has been released **in full in accordance with subdivision D 7** and has not been reinstated"* | when a certified subsidy may be settled at all | **No, and this is the independent use a global deeming provision would have broken.** `For the purposes of the next sentence` confines the deeming to one sentence, so the bar reads exactly as before. Re-counted: **1 before, 1 after** |
| The rescission sentence and the reversal/modification sentence (*"notwithstanding that the reservation for the election has been released in accordance with subdivision D 7"*) | that a settlement survives a release | **No. 1 occurrence each, before and after**, character for character |
| The compelled notice sentence — *"of whether the release was in accordance with subdivision D 7"* | what the Board must tell the two money-committee Chairmen | **No, and deliberately.** The alternative form would have had to conform this to *"of whether the release was one this section required or permitted"*, **changing compelled notice content**. The deeming sentence leaves it alone. **1 before, 1 after** |
| The involuntary-separation sentence's borrowing — *"in the manner this subdivision requires in the case of a reservation released otherwise than in accordance with subdivision D 7"* | the *manner* of reinstatement, not the trigger | **No. 1 before, 1 after.** It borrows timing and mechanics and is unaffected by what the trigger deems |
| Subdivision D 7 itself | the closed list | **No.** The deeming operates *"for the purposes of the next sentence"* only; **D 7's own grounds for release are not widened**, nothing new expires a reservation, and the Board acquires no new power to release |
| `accept no further election until the excess is eliminated` | the self-executing consequence the defect triggered | **No. 1 before, 1 after.** It still operates — on a genuine excess, which is what it was drafted for |
| **"Certified subsidy" definition, clause (iii) and the floor sentence** | *"the amounts payable by the member and by any employer under subdivision B 4 of § 51.1-142.2"* | **YES — conformed, twice.** B 4's payer is now the state agency, so *"any employer"* here would have pointed at a payer B 4 no longer names. → *"by any state agency"* |
| **Subsection J 1, report content** | *"the amounts paid by members and by employers"* | **YES — conformed.** The report must name the class that actually pays. → *"by members and by state agencies"*, and the plural now describes a real plural |
| **Fifth enactment clause, clause (ii)** | *"the payment methods and the employer payment authorized by subdivision B 4 of § 51.1-142.2"* | **YES — conformed.** It is the Board's § 415 determination of the very payment B 4 e authorises. → *"the state agency payment authorized …"* |
| Subdivision B 4 e's first sentence (the five-percent floor) | *"funds other than funds paid by an employer to or on behalf of the member"* | **No, and the non-conformance is the decision.** §6.0-66 item 4: the floor disqualifies **funds**, and the class must stay as wide as § 51.1-124.3 makes it. Conforming it would have **loosened** the floor |
| Subsection G of § 51.1-142.2 — *"Any employer may elect to pay an equivalent amount in lieu of all member contributions"* | the subsection B 4 e opens by displacing (*"Notwithstanding subsection G"*) | **No. This is existing Code text, not underlined, and outside this act's footprint.** The *"Notwithstanding subsection G"* link still resolves, because B 4 e still displaces the same subsection |
| Subdivision B 4 d — *"funds paid by an employer"* | — | **Not present.** The phrase occurs once in B 4 and it is in B 4 e's floor sentence, already accounted for above |
| Subdivision M 2's two class lists | who may seek reconsideration and judicial review | **Substituted, and that is the repair.** The Commonwealth is no longer in the classes in its own right, so § 2.2-507 A no longer puts the Attorney General on both sides. **No other member of either class is added or removed, and no article or number changes** |
| Subsections H and N, which turn on settlement under *"subdivision G 1 or G 4"* | settlement, not release | **No.** Neither reaches the reinstatement sentence or the word *"employer"*. The deeming sentence changes nothing about when a subsidy is settled |

**Direction 3 — the six surviving uses of *"employer"* in § 51.1-142.4, each resolved individually.** **None is left by inadvertence.**

| Surviving use | Why it stays |
|---|---|
| Subsection B — *"no **employer** shall require, request, or induce any employee to make an election"* | **Anti-coercion, and width is protective.** § 51.1-124.3's *"employer"* is wider than *"state agency"*. Narrowing it would leave a payer outside the class free to pressure a member. **Keep the wider prohibition** |
| Subsection F — *"No member shall be liable to the retirement system, to an **employer**, or to the Commonwealth"* | **Non-liability shield; width is protective.** The member should be immune against the widest class of claimant, not the narrowest |
| Subdivision G 1 — *"shall not create any obligation of the member, of any beneficiary, or of any **employer**"* | **No-obligation shield; same reason.** It protects the employer too, and narrowing it would expose a non-agency employer to an obligation the act means no one to have |
| Subdivision G 4 — *"shall not create any obligation of the member, of any survivor or beneficiary of the member, or of any **employer**"* | Same shield, same reason |
| Subdivision G 4 — *"nothing in this subdivision creates any liability … to the retirement system, to an **employer**, or to the Commonwealth"* | Same shield, same reason |
| Subdivision I 3 — *"no **employer** contributions under § 51.1-145 shall be payable for that period"* | **A term of art.** *"Employer contributions"* is the name of a thing § 51.1-145 creates. It is not a reference to a payer under B 4 e and **cannot be renamed by this act** |

**The line, stated once:** *"employer"* was conformed wherever it **denotes the payer under subdivision B 4 e**, and kept wherever it is a **liability or coercion shield** (where the wider § 51.1-124.3 class is the protective one) or a **statutory term of art**. **Four conformed, six kept.** A reader who finds *"employer"* in § 51.1-142.4 after this cut is looking at a shield or at § 51.1-145's term, never at a payer.

**Six further checks.**

1. **No reference by position is stranded and no existing sentence boundary moves — and this is the check Edit 1 could most easily have failed.** Edit 1 inserts **a whole sentence** between two existing sentences of subdivision G 4 and changes neither; the fifteen substitutions all fall **inside** existing sentences and none contains a period, so **every existing sentence of §1 has the same boundaries before and after**. §1 carries **29** references to a sentence by position before the cut and **30** after — *"preceding sentence"* **19**, *"first sentence"* **8**, *"second sentence"* **2**, and the one *"next sentence"* this revision creates. **Thirteen of the *"preceding sentence"* references are inside subdivision G 4, and every one was located by offset against the insertion point.** The nearest on either side is **1,797 characters before** it (the reversal/modification sentence's *"settled as required by the preceding sentence"*, upstream and unaffected) and **4,270 characters after** it (in the involuntary-separation material, with several unchanged sentences in between). **No *"preceding sentence"* reference sits in the sentence immediately following the insertion, so none of them now points at the deeming sentence instead of what it meant.** Subdivision G 4's death-case release refers to *"the first sentence of subdivision D 2"*, which is in another subdivision and unmoved. The deeming sentence's own *"the next sentence"* is the one positional reference this revision creates, and §6.0-66 item 1 records its fragility.
2. **The deeming sentence's *"the next sentence"* resolves to the reinstatement sentence, verified on the written body and not assumed.** The sentence immediately following the insertion begins *"Where a reservation has been released otherwise than in accordance with subdivision D 7,"* — confirmed by reading the amended paragraph, not by predicting it.
3. **Nine anchors belonging to other open cuts were re-counted over §1 after every substitution and each resolves exactly once** — [MOO-141](/MOO/issues/MOO-141) Edits 1, 2 and 3 as [MOO-176](/MOO/issues/MOO-176) revision 6 leaves them, and all six [MOO-164](/MOO/issues/MOO-164) act-versus-notice FINDs. **No anchor of another cut shares a sentence with anything this revision touched.**
4. **One defined term is added and no existing definition is touched.** § 51.1-142.4 A still defines **13** terms, none reworded — **and MOO-196's figure of 18 is wrong, which the record should say.** Counted on the body: *Certified subsidy, Complete application, Earliest qualifying retirement date, Election, Eligible member, Final qualifying retirement date, Involuntary separation, Maximum purchasable amount, Program, Qualifying retirement, Standard cost, State agency, Unreduced retirement eligibility date* — **13**, before and after. **Nothing in finding A2 turns on the count:** the two facts that matter are that *"employer"* is **not** among them and *"state agency"* **is**, and both are confirmed. Subdivision B 4 a now defines **seven** instead of six, inserted alphabetically between *"Standard cost"* and *"Statutory interest"*, and **no other definition in B 4 a moves a character**. The term *"state agency"* is now **defined in both sections that use it**, which is the condition that was missing.
5. **No curly apostrophe was created, normalised or moved.** §1 carries **4** before and **4** after. The ten substitutions were anchored on `employer that paid`, which stops **before** `on the member's behalf`, so the single curly-apostrophe occurrence in subdivision G 4 was caught by the same substitution as the other nine. **The hazard MOO-196 flagged was dissolved by the choice of anchor rather than handled by a second pass.** Normalising the four remains available as a separate minor tidy and is **not** done here.
6. **No figure, threshold, percentage or date moves.** The **$3,000,000** limitation, the **20 percent** contingency, the **five percent** member-funded floor, the **12.50** / **10.74 percent** normal cost rates, every 15-, 30-, 60- and 90-day period, and every July 1 and December 1 are untouched. **Fiscal & Impact Modeler has nothing to re-cost from this revision:** the cut changes who is named and when a reinstatement duty bites, and it **removes** a shutdown that would have fired on correct settlements. It moves no price.

### §5.43 Store revision 65 — the one substitution, chased in both directions

**Result: no conforming amendment is required, and nothing is stranded.** Counts are taken over **enacted §1** of the body that was written, not predicted, and the before-counts were taken on store revision 64 (document revision 81) at the moment of application. **Store revision 64 changed no word of §1, so these counts are also store revision 63's.**

**Direction 1 — what the advisory cites, and whether it says it in the act's own words.**

| Cited or used | Occurrences in §1 | Result |
|---|---|---|
| **subsection A of § 51.1-162** | **0** before, **1** after | §1 reaches A three times, always as *"subsection A of **that** section"* inside a sentence that has already named § 51.1-162. The advisory is its own semicolon item, and the item after it restarts with the full citation *"that subsection C of § 51.1-162"*, so the **full citation is the only unambiguous form here**. Not a paraphrase: the proposition two items earlier already cites A for the designation itself |
| *"designation of beneficiary"* | **0** before, **1** after | **Verified at source on 12 October 2026.** § 51.1-162 A requires each member to *"designate who is to receive a refund of accumulated contributions"*, pays *"the designated beneficiary"*, and calls the act *"the designation"*; subsection B pays *"the person or persons designated as provided in subsection A."* The phrase is **the cited subsection's own vocabulary**, and §1's own *"designation"* (**3** before, **4** after — the fourth is this one) and *"designated"* (**5**, unmoved) are the same concept and not a second one. **Precision, store revision 68:** the compound *"designation of beneficiary"* does **not** itself appear in § 51.1-162 A — A's words are *"designate who is to receive a refund of accumulated contributions"*, *"the designated beneficiary"*, *"the designation"* and *"If no designation has been made."* **This row's claim is that the component vocabulary is A's, and that claim holds as written.** The compound is new to the act and to § 51.1-162, and it is nonetheless the right noun, because A does pay *"the designated beneficiary"* and does call the act *"the designation."* No text changes. [MOO-195](/MOO/issues/MOO-195) F11 |
| *"before completing payment"* | **2** before, **3** after | **The act's own phrase, and one of the two is in this very subdivision** — D 1 already certifies *"the member's right to cancel the election under subdivision G 5 at any time before completing payment"*, and G 4 uses it for a member who *"dies before completing payment."* So the advisory's deadline is **the same event the subdivision already uses twice**, needs no definition, and is the point at which the member's own cancellation right also ends |
| *"is advised"* / *"advised"* | **0** before, **1** after | A new operative word in §1, and that is the point of it: §6.0-65 item 1. It is not *"shall"*, it is not *"should"*, and it creates no duty and no power |

**Direction 2 — what cites the thing the advisory is inserted into.**

| Provision | What it reaches | Moved by this revision? |
|---|---|---|
| D 1's failure sentence — *"A failure to state in the Board's certification **every matter this subdivision requires to be stated** in it"* (1 occurrence in §1, unmoved) | every matter the subdivision compels, which now includes the advisory | **Yes, and deliberately.** Omitting the advice is reviewable under subsection M, with the member's 30 days running from the certification she received, and the Board must state the failure in the **subsection J** report. Accepted by the Director at MOO-188 §3.4 and **not** excepted |
| Subsection M 2 | the review channel D 1's failure sentence routes into | **No.** D 1's failure sentence already names M 2's own category and already disapplies M 2's second sentence for such a failure. One more compelled matter needs no amendment of M |
| Subsection J | the report of failures | **No.** The duty is *"every such failure"*, which is generic by construction |
| The § 51.1-162 B proposition immediately before the advisory, and the § 51.1-162 C and § 51.1-162 A propositions immediately after it | the series the advisory now sits inside | **No.** The advisory is a new item between existing items; no existing item's words change, and the series' semicolon-and-*"that"* structure is preserved. The closing *"and that where no benefit is payable under subsection B"* item still closes the series |

**Four further checks.**

1. **No reference by position is introduced or stranded, and no sentence boundary moves.** The insertion falls **inside an existing sentence** — the certification's series — and contains no period, so subdivision D 1 has the same sentences before and after it. §1 carries **ten** references to a sentence by ordinal, re-counted on the written body; **none of them is to a sentence of subdivision D 1** (the two *"first sentence of this subdivision"* references are in subdivisions D 2 and G 2). Nothing in §1 refers to the certification's items by ordinal or count — no occurrence of *"the preceding proposition"*, *"the foregoing"* or any similar form in D 1 — so adding an item strands nothing.
2. **Nine anchors that belong to other open cuts were re-counted over §1 after the substitution and each resolves exactly once** — [MOO-141](/MOO/issues/MOO-141) Edits 1, 2 and 3 as [MOO-176](/MOO/issues/MOO-176) revision 6 leaves them, and all six [MOO-164](/MOO/issues/MOO-164) act-versus-notice FINDs. **The substitution is 137 characters inside one sentence of D 1 and reaches none of them.**
3. **No defined term is added and no definition is touched.** The advisory uses no term subsection A defines, and *"member"*, *"designation"* and *"payment"* carry the meanings they already carry.
4. **The advisory compels a statement about a section this act does not amend, and that is not new.** D 1 already compels six propositions about § 51.1-162 and § 51.1-165. **It remains true that a reader of § 51.1-162 learns nothing from § 51.1-162** — that exposure is §7 item 129 answer (7), which is **not** answered here and which would change the act's footprint and its title line. **Two corrections, store revision 68.** First, **answer (7) has since been answered**: the Policy Director approved **s162c-conforming** at 18:04:59 UTC on 12 October 2026 and store revision 67 enacted it, so § 51.1-162 is now reproduced in full as amended in §1, the title line names it, and the first enactment clause follows. Second, this check **conflated two things**: answer (7) is specifically the § 51.1-162 **C** waiver-period operative override and its conforming amendment, not the general point that a reader of § 51.1-162 learns nothing from § 51.1-162. **The advisory overrides nothing and does not enlarge answer (7)** — [MOO-195](/MOO/issues/MOO-195) N8. What the advisory does leave open is a different and smaller exposure, an instruction with no addressable machinery, which is [MOO-195](/MOO/issues/MOO-195) F5 and is before the Director at [MOO-191](/MOO/issues/MOO-191). **And the exposure the conforming amendment did not cure is [MOO-195](/MOO/issues/MOO-195) F8:** the title line now names § 51.1-162, but its *"relating to"* clause still says nothing of death benefits or beneficiary designations, and subdivision D 1 now compels seven statements about them.

### §6.0-65 Ambiguities resolved in store revision 65

1. **Why *"is advised to review"* and not *"should review"*, and why neither is *"shall review."*** The series it joins is six propositions of law, each introduced by *"that"*, and a seventh item reading *"that the member **should** review"* would have read as a statement of what the law requires of the member. **It is not a duty, and it must not be capable of being read as one** — a member who does not review her designation breaks nothing, loses no right and is not late for anything. *"Is advised to review"* states the only thing that is true: the Board's certification carries advice. **The operative verb belongs to the Board's carrier sentence** — *"The Board shall not accept an election until the Board has, in writing, certified to the member … that …"* — so the actor, the addressee, the writing and the moment are all already named, and the advisory adds no unnamed actor. This is the Policy Director's wording change at MOO-188 §3.3 and the reason is recorded there. **Superseded as to the words, store revision 70 — the item no longer reads *"is advised to review."*** The Policy Director has taken [MOO-195](/MOO/issues/MOO-195) F9 at [MOO-208](/MOO/issues/MOO-208) and the item now reads *"that the Board advises the member to review."* **Everything this item says about the operative verb survives the change; its conclusion does not.** Naming the Board inside the item is the better drafting answer, because the item read alone was self-verifying — true because the Board states it — and was the only one of seven that was. *"Advises"* is the Board's own verb, it imposes nothing on the member, and every no-duty property this item defends is intact. §6.0-70 item 1.
2. **Why it is its own semicolon item and not an appendage to the § 51.1-162 B proposition.** The designation is subsection B's fact, which is the argument for putting the advice inside B's item, and it is the wrong argument: **B's item states what the law does, and the advisory states what the member is advised to do.** Merging them would have buried advice inside a proposition of law and made it arguable that the advice is part of what B provides. Separate, the propositions stay together and the advice is visibly advice. **Reversed as to position, and not as to either reason, store revision 70.** The Policy Director has taken [MOO-195](/MOO/issues/MOO-195) F4 at [MOO-208](/MOO/issues/MOO-208) and the advisory is now item **7 of 7** and no longer item 5. **Both reasons this item gives survive the move and are served better by it**: at the end of the series the advice is still its own semicolon item, still introduced by *"that"*, still the only item in a different register, and it is no longer interleaved among the six propositions of law it must not be read as part of. What the move adds is that it stops splitting item 4's forward reference to *"subsection C of that section"* from the item that restates that citation in full. §6.0-70 item 4.
3. **Why the full citation *"subsection A of § 51.1-162"* and not *"subsection A of that section."*** §1 uses the short form three times, and each time inside a sentence that has already named § 51.1-162. The advisory is a **new item** and the item that follows it restarts with the full citation (*"that subsection C of § 51.1-162"*), so the short form would have made the referent depend on an item two places back. §5.43 direction 1. **The reason changes with the position; the result does not, store revision 70.** The advisory is now the last item and the item before it names *"subsection B of § 51.1-162"*, so the short form would now have resolved. The full citation is kept anyway, for a reason this item did not need: the item now carries three propositions and shifts to *"that section"* twice inside itself, so it must supply its own referent and not borrow a neighbour's. §6.0-70 item 3.
4. **Why *"designation of beneficiary"* is the right noun and not a second word for one concept.** § 51.1-162 A, verified at source on 12 October 2026, requires each member to *"designate who is to receive a refund of accumulated contributions"*, pays *"the designated beneficiary"*, and calls the act *"the designation"*; B pays *"the person or persons designated as provided in subsection A."* **The advisory therefore points the member at the cited subsection using that subsection's own noun**, while §1's own *"designation"* carries the same meaning it already carries.
5. **Why *"before completing payment"* and not a date, a period, or *"before the Board accepts the election."*** The phrase is already in this subdivision — the certification states *"the member's right to cancel the election under subdivision G 5 at any time before completing payment"* — and in subdivision G 4. **The advisory's deadline is the same event, and it is the last moment at which the purchase can still be undone.** **Correction, store revision 68 — the second reason this item gave is not true and is withdrawn.** As written at store revision 65 the item continued *"and the whole window during which re-designating changes the outcome."* **Nothing in § 51.1-162 A fixes a designation at the completion of payment.** A's own words contemplate redesignation at any time — *"If no designation has been made, or the death of the designated person occurs prior to the death of the member and another designation has not been made"* — so the window in which re-designating changes the § 51.1-162 outcome runs to the earlier of the member's death and the last of the act's retirement-date legs: about 27 months on the act's own dials (subsection E's 12 months to pay and 1 to credit, and the two retirement-date definitions in subsection A), and without end for a member who does not retire. *"Before completing payment"* closes the **first** of those legs. **Store revision 69 — the deadline stands, and the false implicature it carried is cured by words that now follow it.** The Policy Director has taken [MOO-195](/MOO/issues/MOO-195) F2 in form D2b at [MOO-208](/MOO/issues/MOO-208): *"before completing payment"* is kept as the prompt to act now, and the item then states that the member may make or change the designation under subsection A of § 51.1-162 *"at any time before the member's death."* Read together they say do it now, and know you can change it later. **The enacted deadline was never the defect; the inference a reader could draw from it standing alone was.** §6.0-70 item 2. [MOO-195](/MOO/issues/MOO-195) F2, verified at source on 12 October 2026. **The enacted deadline is the Policy Director's approved word and is not changed by this record revision**; whether to extend it, re-point it or leave it stand is before the Director at [MOO-191](/MOO/issues/MOO-191) with the words drafted. A fixed period would have needed a trigger, a definition and a consequence for missing it, and there is no consequence, because there is no duty.
6. **Why the advisory is not excepted from D 1's failure sentence, and what it costs.** **The Policy Director decided this at MOO-188 §3.4 before the cut, and I have not drafted around it.** Omitting the advice is a failure to state *"every matter this subdivision requires to be stated"*, so it is reviewable under subsection M and reportable under subsection J. The cost is that **a review channel now exists for the omission of a sentence that creates no right** — while the member lives it returns the only remedy that matters, which is time to re-designate before payment completes, and after she dies it adds nothing because no remedy can re-designate for her. **The Director has said that if the counsel pass thinks the channel is worth more argument than the advice is worth, they will re-take that one point; it is one clause either way, and the clause is this item.** **Correction, store revision 68 — this item sent that question to the wrong card.** As written at store revision 65 it named the counsel gate at [MOO-192](/MOO/issues/MOO-192), which is the subsection E1 gate and has the channel out of scope. **The question went to pass 21 at [MOO-195](/MOO/issues/MOO-195)**, which answered it: **keep the subsection J limb and drop the subsection M limb**, because M review's only possible output is a remand that can give the claimant nothing — § 2.2-4029 bars a court from supplying the agency action — while the J report puts the same fact before the money committees at no litigation cost and with no claimant needed. **That recommendation is enacted at store revision 70, in form D3c conformed to F9's wording.** The Policy Director has taken [MOO-195](/MOO/issues/MOO-195) F3 at [MOO-208](/MOO/issues/MOO-208) and has expressly reversed the acceptance at MOO-188 §3.4, on counsel's remedy analysis — § 2.2-4029 bars a court from supplying the agency action — and on two further reasons of the Director's own. **So this item's heading is no longer the law of the draft**: omission of the advice is now excepted from D 1's deeming of a failure to state for the purposes of subsection M, and is kept in the subsection J report. **What the exception does not do, recorded and not drafted around: subdivision M 2 reaches the omission on its own terms, so the channel stays open and no cure inside D 1 can close it.** §6.0-70 item 5 and **§7 item 135**, drafted and not enacted. [MOO-195](/MOO/issues/MOO-195) F3 and F10.
7. **What I did not draft, and it is not silence.** The advisory tells the member to look; it does **not** give her a way to re-designate inside the act, does not require the Board to send her her current designation with the certification, and does not toll anything while she reviews. § 51.1-162 A already lets her designate *"in a manner prescribed by the Board"* at any time, so the act needs no machinery, and **a notice that enclosed her designation of record would be a new duty with an administrative cost that nobody has agreed.** It is the kind of thing that belongs on MOO-97's card if anyone wants it, not in a cut commissioned as one edit. **Confirmed, store revision 70.** The Policy Director has **held** [MOO-195](/MOO/issues/MOO-195) F5 at [MOO-208](/MOO/issues/MOO-208) and has directed that **the acknowledgment form is not to be drafted**, because it moves the advisory toward a member obligation and the advisory's whole value is that it demands nothing of her. The route question goes to the subsection J report instead: if the pilot's own reports show the advice being buried, that is the evidence on which to require a route, and it will be evidence rather than a guess. §6.0-70 item 7.

### §6.0-63 Ambiguities resolved in store revision 63

1. **Why *"the person who filed the request"* and not *"the member."*** M 2's class of persons who may seek reconsideration is seven categories wide — member, retiree, beneficiary, applicant, personal representative of a deceased member's estate, person who claimed a death benefit and was refused, and employer that paid on a member's behalf. A notice right keyed to *"the member"* would have given the estate, the refused death-benefit claimant and the paying employer a reconsideration they could not convert into a decision. The enacted words follow the filing, which is the only fact common to all seven.
2. **Why the denial is made a case decision in terms rather than by relying on the completion sentence.** §0.0-63 repair 1. The alternative was to amend the completion sentence to add *"or upon a denial under this subsection"*, which touches an enacted sentence three passes have certified; the insertion touches nothing.
3. **Why *"first day after the expiration of those 30 days"* and not *"the last day."*** §0.0-63 repair 2: a denial on the last day of a period in which the Board may still lawfully act puts two inconsistent determinations on one date.
4. **Why the 30 days are not tolled, extended or qualified.** The member's 30-day notice period under the new sentence runs from her own filing, so there is nothing for the Board to delay. Subsection M 2's tolling operates on *"any period within which the member or applicant must act"* — and the new period is one in which the **Board** must act, so the tolling provision does not reach it and no carve-out is needed.
5. **Why the denial is not deemed an act of the Board.** §0.0-63, last paragraph, and §7 item 130. Deeming it an act would have ended the member's tolling and her D 4 / D 5 filing-date retention as a by-product — two endpoints that belong to [MOO-164](/MOO/issues/MOO-164) and card (k) and that nobody has decided. **A cure for a residual must not move a priced endpoint in passing.**
6. **What the board's answer costs, stated and not netted away.** Up to 30 further days before the member may go to court, and a member who never files the notice never gets a decision. That is the same bargain § 2.2-4021 B strikes against every party before every agency in the Commonwealth, which is why option (d) was modelled on it — but it is a cost, and it falls on the member who does not know she has a right to assert. The board was given that trade in terms on the card and took it.


7. **A defect in these two sentences that I found after they were in the store, and it is mine. §7 item 131.** Item 2 above says the denial is made a case decision *"in terms rather than by relying on the completion sentence"*, which was the right repair. It is not a complete one. Subdivision M 2's express Article 5 grant is keyed to *"such case decision"*, whose nearest antecedent is the completion sentence it was written to avoid depending on; and the characterisation I drafted is bounded *"for the purposes of this subsection"*, which is the one qualification that does not travel to § 2.2-4026. **Neither reading is fatal alone and the pair is.** Both repairs are one phrase, both are drafted in full at §7 item 131, and **neither is enacted** — the limiting phrase is in the option (d) text the board approved verbatim, and the alternative repair edits a sentence [MOO-169](/MOO/issues/MOO-169)'s pass certified. **No figure moves on either.** Named to [MOO-190](/MOO/issues/MOO-190) as the first thing to break.
