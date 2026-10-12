# MOO-176 — the MOO-141 patch, revision 6: **Edit 3 re-cut to 120 days** on the board's answer, re-cut whole against `bill-text-s8` **store revision 61**

**INTERNAL WORKING DRAFT. Not a Division of Legislative Services bill. Not reviewed by counsel, and
nothing in it has been cleared by counsel. Pre-decisional and internal to Paperclip. Nothing here is a
claim that the text is legally sufficient for introduction; only Division of Legislative Services
drafts official bills.**

---

## 0. Revision 6 in one page

### 0.1 What revision 6 is

**One text change against revision 5, and a whole re-cut around it.** The board answered the one
question left open by the Policy Director's disposition of revision 5
([MOO-162](/MOO/issues/MOO-162) §5) at 14:15 on 12 October 2026: option `to-120`, *"Lengthen to 120
days after the Board acts upon the request."* Edit 3's READ string is re-cut to that figure. Nothing
else in the patch moves, and nothing here reopens §0.2's call (one pendency event, two endpoints),
§0.3's answer (keep F-1's deletion, day 22 accepted), Edit 1 or Edit 2.

| | Revision 5 | Revision 6 |
|---|---|---|
| Edit 1 — subsection A interpretation paragraph | +669 | **+669, unchanged** |
| Edit 2 — the 15-day date-notice backstop, card (g) | +14 | **+14, unchanged** |
| Edit 3 — M 2's D 4 / D 5 retention, card (k-ii) | +14 (*30 days*) | **+15 (*120 days*)** |
| Document delta | +697 | **+698** |
| Base | store revision 60 / 250,229 chars | **store revision 61 / 271,611 chars** |

**The figure is verified, not taken.** The Director's prediction is confirmed to the character by
applying all three edits to a copy of the live body: Edit 3 is **+15** against the base string, not
+14, and the patch is **+698**, not +697. §8.2 carries the measurement.

### 0.2 What the figure buys, measured

On the ordinary facts the patch is drafted around — request filed day 0, Board first acts day 7,
reconsideration decided day 85 — and with every clock keyed to the **first** act by Edit 1's deeming:

| | Revision 5 (30 days) | Revision 6 (120 days) |
|---|---|---|
| Board's duty to act on the application | day 22 | day 22 |
| M 2's tolling ends | day 37 | **day 37 — Edit 3 does not touch it** |
| the retention ends | day 37 | **day 127** |
| against the reconsideration decided day 85 | **expires 48 days short** | **covers it, 42 days to spare** |
| against the outer bound M 2's own 90 days allows (day 90) | expires 53 days short | covers it, **37 days to spare** |

**That was the whole of the board's question and it is answered.** The retention now outlives the
decision whose outcome the retained filing date exists to preserve, on the ordinary facts and on the
worst case M 2 itself permits.

### 0.3 The thing you must read before anything else: the identity pass 18 endorsed is gone

**Revision 5 §1.3 rested Edit 3 in part on an identity.** After Edit 3 at 30 days the phrase *"30 days
after the Board acts upon the request"* appeared **twice** in M 2 — once for the tolling endpoint, once
for the retention — and nowhere else in the bill, and pass 18 tested that identity and endorsed it:
*"under Forst the identity is what secures the same meaning for both."*

**At 120 days that identity is gone.** The count table proves it: *"30 days after the Board acts upon
the request"* is now **1 → 1** (the tolling endpoint alone) and *"120 days after the Board acts upon
the request"* is **0 → 1**. The two periods sit in the same subsection in different numbers, and the
retention outlives the tolling endpoint by **90 days**.

**§6 states the divergence as deliberate, prices the 90-day gap, and says what carries Edit 3 now that
the identity does not.** It is the first substantive section of this document because it is the first
thing a reviewer will reach for. **It does not reopen the figure**, and on my reading the divergence is
a **choice with a disclosed limit**, not a defect — §6.4 says what would make it a defect.

---
## 1. The patch — three anchored edits, re-resolved at store revision 61

**Whoever applies this must use the FIND strings verbatim.** Each was counted today in the whole
271,611-character document and again in §1 alone, not in a slice, on the live body.

### 1.1 Edit 1 — subsection A, final interpretation paragraph. **Unchanged from revision 5**

> **FIND** (135 characters; count = **1** in the whole document and **1** in §1 at store revision 61):
>
> ```
> every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>
> ```
>
> **READ** (804 characters, **+669**):
>
> ```
> every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.</u>
> ```

The anchor is still the paragraph's last 135 characters and still sits immediately before
`<u>**B.** The Program is established.` — **re-verified on store revision 61, not carried forward.**
The paragraph itself is byte-identical to store revision 60 (§3.1).

### 1.2 Edit 2 — card (g). The backstop notice, re-keyed to the decision. **Unchanged from revision 5**

**In the definition of *"final qualifying retirement date"* in subsection A, in its penultimate
sentence.**

> **FIND** (106 characters; count = **1** in the whole document and **1** in §1 at store revision 61):
>
> ```
> it shall give the member written notice of that date no later than 15 days after it acts upon the request.
> ```
>
> **READ** (120 characters, **+14**):
>
> ```
> it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request.
> ```

**The FIND must be the full clause and not the short form.** *"no later than 15 days after it acts upon
the request"* **still resolves twice** in §1 at store revision 61 — here, and in M 2's duty to act upon
the application, which Edit 2 must not touch and does not. Re-counted today: **2**. That is the fifth
consecutive base at which the short form resolves twice, and the reason the anchor is the whole clause.

### 1.3 Edit 3 — card (k-ii). M 2's D 4 / D 5 filing-date retention. **RE-CUT TO 120 DAYS**

**In subdivision M 2, in its fifth sentence of eight** — re-counted on the live body at store revision
61, which did not change the sentence's position (§3.3).

> **FIND** (106 characters; count = **1** in the whole document and **1** in §1 at store revision 61):
>
> ```
> retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request
> ```
>
> **READ** (121 characters, **+15**):
>
> ```
> retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request
> ```

**+15 characters. Four words inserted, nothing struck.** Revision 5 inserted three words (*"30 days
after"*) for +14; revision 6 inserts *"120 days after"* for **+15**. **One character more, and the
patch becomes +698.** Both figures were produced by applying the edits to a copy and measuring, not by
counting by hand — §8.2.

**What the figure does to the subsection's vocabulary is in §0.3 and §6**, and it is the one thing in
revision 6 a reviewer must be sent at directly.

### 1.4 Subdivision G 4 — still no edit

**Not amended by any of the three edits.** Revision 2's withdrawn G 4 edit — striking *"first"* from
G 4's request limb — stays withdrawn on pass 17's F-1, on the condition that both of G 4's express
*"first"*s are intact. **Re-counted on the live body at store revision 61: *"first acts upon it"*
appears twice in G 4**, once for the disability application and once for the request, and the pendency
definition sentence is byte-identical to store revision 60 (§3.4). **The condition holds and the
withdrawal stands.**

---

## 2. Title line, enacting clause and enactment clauses

**Unchanged by this patch**, and reproduced so the draft is readable without `bill-text-s8`. Re-read
against store revision 61, which did not change the title line:

> A BILL to amend and reenact § 51.1-142.2 of the Code of Virginia and to amend the Code of Virginia by
> adding a section numbered 51.1-142.4, relating to the Virginia Retirement System; purchase of prior
> active duty military service credit by state employees; cost; pilot program; post-retirement
> employment; reports.
>
> Be it enacted by the General Assembly of Virginia:
>
> 1. That § 51.1-142.2 of the Code of Virginia is amended and reenacted and that the Code of Virginia
>    is amended by adding a section numbered 51.1-142.4 as follows:

**This patch adds no enactment clause, no effective date, no sunset and no severability clause**, and
revision 6 does not change that. The board's answer is a figure inside an existing sentence; it is not
severable from the provision it amends, and it needs no effective-date mechanics of its own beyond the
second enactment's 1 July 2029 date and the third enactment's 1 July 2033 expiration with its clause
(i) to (iv) savings, which already carry it. Revision 5 §6.7's reasoning is unchanged and the Policy
Director recorded it as settled.

**One consequence of the figure worth a line here, because it is an enactment-clause question and not
a drafting one.** The third enactment's clause (i) savings continue *"every right of a member under
those provisions and every period allowed to a member by those provisions"* past the 1 July 2033
expiration. A 120-day retention running from a Board act late in the window therefore survives
expiration on the same words a 30-day one did. **No new clause is needed and none is drafted.**

---
## 3. The provisions, in full, as amended

**Markup convention, unchanged from revision 5.** The whole of subsection A, subdivision D 1,
subdivision D 3, subdivision G 4 and subsection M is **new language in the bill** — each is already
wrapped in `<u>…</u>` in `bill-text-s8` — so **every word reproduced below is underlined new text in
the bill as it stands**, and nesting a second `<u>` inside it would be ambiguous markup rather than
clearer markup. Inside that wrapper: the words **this patch adds** are **bolded**; the words it removes
are ~~struck through~~. Revision 6 has three struck words, all in Edit 2, exactly as revision 5 did. On
application to the store they are simply removed from the surrounding underlined text.

**Every reproduction below was re-spliced programmatically from the live `bill-text-s8` at store
revision 61 today and diffed, character for character, against revision 5's own reproductions. None is
carried forward.** Of the eight provisions revision 5 reproduced, **seven came back byte-identical and
one came back changed** — subdivision M 2, which is the provision Edit 3 sits in. **That is the fifth
time in seven cuts that the standing warning has fired**, and the first time it has fired on the
provision the one live text change is inside. §8.4.

### 3.1 Subsection A, final interpretation paragraph — as amended by **Edit 1**

<u>For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, a written statement or notice required of the Board is given on the date the Board mails it to the person to whom it is required to be given or transmits it electronically to an address that person has provided to the Board for that purpose, except that an electronic transmission completed after 5:00 p.m. is given on the following day. For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where the Board mails a written statement or notice, every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.**For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.**</u>

**Diff against revision 5's reproduction: the unamended part is byte-identical.** Store revision 61
did not touch this paragraph. The bolded text is Edit 1, unchanged from revision 5.

### 3.2 The definition of *"final qualifying retirement date"* in subsection A — in full, as amended by **Edit 2**

<u>"Final qualifying retirement date" means the date that is 12 months after the member's earliest qualifying retirement date, except that the Board shall approve a later date where the Board's own processing requirements, or any other cause not attributable to the member, make the member's retirement on or before the date that would otherwise apply under this definition impracticable. A later date approved under this definition shall be the first day of a month and shall be not more than three months after the date determined under the first sentence of this definition. The Board shall approve a later date on its own initiative or upon the written request of the member, which the member may file at any time before the date that would otherwise apply under this definition or before any later date approved under this definition; the Board shall act upon such a request, and shall give the member written notice of its determination and of the reasons for it, no later than 30 days after the request is filed; and the member may seek review of the determination under subsection M. The Board shall determine the member's earliest qualifying retirement date and final qualifying retirement date, and shall state both of them and the reasons for any later date approved under this definition, in writing to the member no later than 15 days after the Board credits to the member the service credit purchased under the member's election, and shall give the member written notice of any later date approved after that statement no later than 15 days after the approval. Where the member's final qualifying retirement date as extended under subdivision D 1 or as tolled under subsection M is not the first day of a month, the member's final qualifying retirement date is the first day of the next month. In no event shall a member's final qualifying retirement date, as extended under subdivision D 1 or as tolled under subsection M, be later than 12 months after the date that applies under the first sentence of this definition or, where a later date has been approved under this definition, after that later date, except that this sentence does not apply to an extension under subdivision D 1 by reason of a statement or notice given later than the time required by this definition, and the aggregate of all extensions so excluded shall not exceed 12 months. Where the running of a period has been tolled under subsection M and the member is prevented by the preceding sentence from retiring in a qualifying retirement after that tolling ends, the member's final qualifying retirement date is, notwithstanding the preceding sentence, the first day of the second month following the month in which the Board last acts upon a request the filing of which tolled that period, and in no event later than 12 months after the latest date the preceding sentence permits. Notwithstanding the two preceding sentences, where the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which the Board gives the statement required by this definition, the member's final qualifying retirement date is that first day. Where the Board does not act upon a request the filing of which tolled the running of the member's final qualifying retirement date under subsection M within the period this definition allows for acting upon it, and the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which that period expired, the member's final qualifying retirement date is, notwithstanding any other provision of this definition, that first day. Where the Board's action upon a request determines a member's final qualifying retirement date under this definition, the Board shall state that date in its decision upon the request, and where the Board does not do so it shall give the member written notice of that date no later than 15 days after ~~it acts upon~~ **it gives its decision upon** the request. Where the date that would otherwise apply under this definition is earlier than the first day of the second month following the month in which the Board gives a decision or notice required by the preceding sentence, the member's final qualifying retirement date is, notwithstanding any other provision of this definition, that first day.</u>

**Diff against revision 5's reproduction: byte-identical.** Store revision 61 did not touch this
definition, including the 30-day request duty in its third sentence and the decision-keyed floor in its
last sentence.

### 3.3 Subsection M — subdivisions 1, 2 and 3 in full, as amended by **Edit 3**, re-spliced at store revision 61

**M 2 moved again, and this is the provision Edit 3 is in.** Reproduced in full, with M 1 and M 3,
because Edit 3 sits in the middle of M 2 and *readable as amended* requires the reader to reach the end
of the subdivision — and because the board's figure now has to be read against the tolling sentence
immediately before it.

<u>**M. 1.** The Board shall adopt and publish, no later than July 1, 2029, procedures for administering this section, which shall address the content of a complete application, the channels through which an application may be filed, the determination of initial average compensation where records are incomplete, the determination and reservation of certified subsidies and contingency amounts, the waiting list, recertification, the crediting of service, settlement, cancellation, refunds, and the review of the Board's determinations. The Board shall publish the procedures on its website and shall make them available to any person on request.</u>

<u>2. A member, retiree, beneficiary, applicant, personal representative of a deceased member's estate, person who claimed any benefit payable on the death of a member and whom the Board determined is not entitled to it, or employer that paid on a member's behalf, adversely affected by a determination of the Board under this section, or by a failure of the Board to make a determination, to give a notice, or to make a payment within a period required by this section, or by a failure of the Board to state in a certification or notice a matter this section requires to be stated in it, may obtain, upon written request filed within 30 days after the notice of the determination is given or, in the case of a failure to make a determination, to give a notice, or to make a payment, at any time before the Board makes the determination, gives the notice, or makes the payment, or, in the case of a failure to state a matter, within the period provided by the provision that requires the matter to be stated, written reconsideration by the Board stating the reasons for its decision. Every determination, certification, redetermination, recertification, reduction, cancellation, rescission, restoration, crediting of service credit, placement on a waiting list, expiration of a reservation, denial of an election, and refusal to accept an election under this section is a determination of the Board for the purposes of this subsection, whether or not another provision of this section expressly provides for review of it. The Board shall act upon a request for reconsideration within 90 days. The filing of a request for reconsideration under this subsection, and the filing of a request under the definition of "final qualifying retirement date" in subsection A, tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request, except that (i) no second or subsequent request for reconsideration of the same determination or of the same failure, and no second or subsequent request under that definition, tolls any period under this section or under subdivision B 4 f of § 51.1-142.2, and (ii) the aggregate of all tolling under this subsection shall not exceed 120 days, excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request. An application that is the subject of a request for reconsideration under this subsection retains its filing date for the purposes of subdivisions D 4 and D 5 until **120 days after** the Board acts upon the request, and the Board shall act upon the application no later than 15 days after it acts upon the request. Upon completion of a reconsideration under this subsection, the final determination issued by the Board shall constitute a case decision as defined in § 2.2-4001. A member, retiree, beneficiary, applicant, personal representative of a deceased member's estate, person who claimed any benefit payable on the death of a member and whom the Board determined is not entitled to it, or employer that paid on a member's behalf, aggrieved by, and claiming the unlawfulness of, such case decision, shall have a right to seek judicial review thereof in accordance with Article 5 (§ 2.2-4025 et seq.) of the Administrative Process Act. Articles 3 (§ 2.2-4018 et seq.) and 4 (§ 2.2-4024) of the Administrative Process Act shall not apply to a reconsideration under this subsection.</u>

<u>3. The sentence of subsection B of § 2.2-4021 providing that a decision shall be deemed to be in favor of the named party, and the corresponding sentence of subsection C of that section, shall not apply to a determination of the Board under this section or to a reconsideration under subdivision 2.</u>

**M 2 is 494 characters longer than revision 5 reproduced it. Four changes, none of them this patch's
— all store revision 61, [MOO-161](/MOO/issues/MOO-161)'s counsel pass enacted:**

1. **Both of M 2's class lists are rewritten, and the open formula is gone.** *"or other person to whom
   this section requires a notice to be given"* comes out of **both** the reconsideration class and the
   judicial-review class — the formula that reached, on the face of the act, *the public*, through
   subsection K's public-notice duty — and is replaced in each by two named classes: *"person who
   claimed any benefit payable on the death of a member and whom the Board determined is not entitled
   to it, or employer that paid on a member's behalf."* Store revision 61's own sweep records the
   formula at **2 → 0** in §1.
2. **The failure limb is widened by a third class**, reaching *"a failure of the Board to state in a
   certification or notice a matter this section requires to be stated in it"* — an omission from a
   document that was given on time.
3. **That new class gets its own filing window:** *"or, in the case of a failure to state a matter,
   within the period provided by the provision that requires the matter to be stated."*
4. **The existing failure window is spelled out** — *"in the case of a failure to make a determination,
   to give a notice, or to make a payment"* replaces *"in the case of such a failure"*, which no longer
   had one referent.

**Edit 3's FIND string is unaffected by all four and still resolves exactly once**, M 2 is still
**eight sentences**, and the retention sentence is still the **fifth**. The tolling sentence's
*"until 30 days after the Board acts upon the request"* is untouched, which is why §0.3's identity
point is about Edit 3's figure and not about a base move. But revision 5's reproduction of M 2 is
**stale** and this one replaces it. **An anchor that still resolves is not evidence the reproductions
are current** — fifth instance, and the first on the provision the live text change is inside.

**One consequence of change 1 and change 2 that the board did not have in front of it, and it is a
widened base rather than a defect.** Edit 3's retention attaches to *"an application that is the
subject of a request for reconsideration under this subsection"*. Store revision 61 widened **who may
request** (a rejected death-benefit claimant, and an employer that paid on a member's behalf) and
**what they may request about** (an omission from a certification or notice). **So the 120 days now
attaches on more routes than the 30 days did when the board chose the figure.** It is the base that
widened, not this edit, and nothing in the board's answer turns on it — but it is the kind of thing a
pricing model needs, and §6.2 routes it to [MOO-170](/MOO/issues/MOO-170) rather than carding it.

### 3.4 Subdivision G 4 — the suspension and pendency passage. **Not amended by this patch**

**Reproduced because it is the provision [MOO-141](/MOO/issues/MOO-141) is about.** The whole of G 4
runs to some 29,600 characters at store revision 61 and the rest of it is not reached; the three
sentences that are reached are these, re-spliced verbatim today:

<u>… The Board shall not make a determination under subdivision 2, and shall not give the notice required by subdivision 2, while an application of the member for a disability retirement allowance under this chapter is pending, and a determination made in contravention of this sentence is of no effect. No period stated in subdivision 2 or in this subdivision, whether it is a period within which the Board is required to act or a period within which a determination is required to take effect, runs while such an application is pending or while a request the filing of which tolls the running of the member’s final qualifying retirement date under subsection M is pending, except that the aggregate of all such non-running by reason of such requests and by reason of applications for a disability retirement allowance filed after the first such application shall not exceed 120 days, and a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate. For the purposes of this subdivision an application for a disability retirement allowance is pending from the date on which the member files it until the date on which the Board first acts upon it, and such a request is pending from the date on which the member files it until the date on which the Board first acts upon it. …</u>

**Diff against revision 5's reproduction: byte-identical.** Store revision 61 **did** amend G 4 — two
sentences were added, the employing state agency's 30-day death-notice duty and the reinstatement of a
released amount on reconsideration or judicial review — but **not these three sentences**, and neither
new sentence keys a period to the Board's acting upon a request. §4.2 chases both.

**Both of G 4's express *"first"*s are intact**, which is the condition on which revision 2's G 4 edit
stays withdrawn, and **G 4's own 120-day aggregate is not Edit 3's 120 days** — it caps non-running
while an application or request is *pending*, and pendency ends at the **first act**, where Edit 3's
120 days *begin*. Two clocks, two triggers, no overlap. §6.3 carries this.

### 3.5 Subdivision D 1 — the extension sentence. **Unchanged**

**Reproduced because it is the provision through which card (g)'s 0-to-12-month swing runs, and Edit 2
is what closes it.**

<u>… Where the Board gives that written statement, any notice of a later approved date required by that definition, or any notice of a date required by that definition upon the Board's action upon a request, later than the time required by that definition, the member's final qualifying retirement date is extended by the number of days by which the statement or notice is late, the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. …</u>

**Diff against revision 5's reproduction: byte-identical**, including the descriptor *"any notice of a
date required by that definition upon the Board's action upon a request"* that pass 18's F-9 is about —
which the Policy Director routed to [MOO-164](/MOO/issues/MOO-164)'s cut as card 2 and gate 1. Store
revision 61 **did** amend D 1, in the certification the fatal finding was about, but **not this
sentence**.

### 3.6 Subdivision D 3 — in full, **not amended by this patch**

**Reproduced because it is the parallel retention provision, and because the board's figure now makes
the two retentions differ by 120 days where before they differed by 30.**

<u>3. Before reserving a certified subsidy the Board shall obtain the written confirmation of the Director of the Department of Planning and Budget, or his designee, that funds appropriated and legally available for the purposes of this section are sufficient to fund the reservation. The Board shall file the request required by this subdivision no later than 15 days after the member's application is completed. The Director or his designee shall act upon the Board's request within 30 days after the request is filed. If the Director or his designee does not act within that period, the Board shall give written notice of that fact, and of the date of the Board's request, to the member and to the Chairmen of the House Committee on Appropriations and the Senate Committee on Finance and Appropriations no later than 15 days after that period expires, and shall state every such lapse in the report required by subsection J. An application for which a request under this subdivision is pending retains its filing date for the purposes of subdivisions 4 and 5, and the Board shall act upon the application no later than 15 days after the confirmation is obtained. Where a request under this subdivision has been pending for 90 days, the Board shall give the applicant written notice of that fact, of the applicant's rights under subsection B of § 51.1-142.2, and of the standard cost, determined as of the date of the notice, of the service credit, if any, the applicant is eligible to purchase under subdivision B 2 of § 51.1-142.2 as of that date. If the Director or his designee determines that funds appropriated and legally available are not sufficient to fund the reservation, the Board shall place the application on a waiting list in the order determined under subdivision 4, shall give the applicant the notice required by subdivision 5, shall give written notice of the determination and of the reasons stated for it to the Chairmen of the House Committee on Appropriations and the Senate Committee on Finance and Appropriations no later than 15 days after the determination, shall state every such determination in the report required by subsection J, and shall request a further confirmation under this subdivision no less often than annually and no later than 30 days after the general appropriation act making appropriations for that fiscal year becomes law, until the application is accepted, the applicant withdraws it, or this section expires. A placement on the waiting list under this subdivision is a determination of the Board for the purposes of subsection M. The Board shall also reserve, at the time it reserves each certified subsidy, a contingency amount equal to `[20]` percent of that certified subsidy, to fund any recertification required by subdivision 6. A contingency amount reserved under this subdivision is charged against the limitation in subdivision 2, and the Board shall release it when the certified subsidy is settled under subdivision G 1 or G 4 or the reservation is released under subdivision 7. A reservation shall remain in effect until the certified subsidy is settled under subdivision G 1 or G 4 or the reservation is released under subdivision 7. The Board shall obtain a further written confirmation under this subdivision for each fiscal year in which any reservation remains in effect; until that confirmation is obtained the Board shall accept no further election, but the absence of the confirmation shall not release any reservation, shall not affect any election the Board has accepted, and shall not affect any service credit the Board has credited.</u>

**Diff against revision 5's reproduction: byte-identical.** Store revision 61 did not touch D 3.

**The one thing the figure does here, and it is a disclosure and not a defect.** D 3's retention runs
*"while"* a confirmation request is pending and its paired duty falls *"no later than 15 days after the
confirmation is obtained"* — it is **keyed to the confirmation, not to the Board's acting upon a
request**, so Edit 1's trigger does not reach it and Edit 3's figure does not move it by a day. **After
revision 6 the two sibling retentions in the same section are a bare pendency on one route and a
pendency plus 120 days on the other.** That divergence is not created by Edit 3 — it is created by
D 3's own event-keying, which is [MOO-171](/MOO/issues/MOO-171)'s question and the Policy Director's
card 6 — but **the figure widens it from 30 days to 120 and a reader will notice.** Not drafted, no
card opened, stated here and in §6.3 so it is in the record before pass 19 finds it.

---
## 4. Cross-reference check — performed on store revision 61, with results

### 4.1 Counts, every one re-run today on the live base and on an applied copy

| Measure | Store revision 61 | After the three edits |
|---|---|---|
| document characters | 271,611 | **272,309 (+698)** |
| enacted §1 characters | 117,980 | **118,678 (+698)** |
| *"acts upon"* in §1 | 8 | **8** |
| *"first acts upon"* in §1 | 2 | **3** |
| *"last acts upon"* in §1 | 1 | **1** |
| *"last acting"* in §1 | 0 | **1** |
| *"acting upon"* in §1 | 2 | **2** |
| *"action upon"* in §1 | 2 | **2** |
| *"is deemed to act"* in §1 | 0 | **1** |
| *"or an application"* in §1 | 0 | **0** |
| *"pending"* in §1 | 9 | **9** |
| *"month in which"* in §1 | 14 | **15** |
| *"no later than 15 days after it acts upon the request"* | 2 | **1** |
| ***"30 days after the Board acts upon the request"*** | **1** | **1 — and this is the identity, broken** |
| ***"120 days after the Board acts upon the request"*** | **0** | **1** |
| *"until the Board acts upon the request"* | 1 | **0** |
| *"its decision upon the request"* | 1 | **2** |
| *"act upon the application"* in §1 | 2 | **2** |
| *"retention"* in §1 | **0** | **0** |
| *"120 days"* in §1 | 4 | **5** |
| `<u>` / `</u>` in §1 | 60 / 60 | **60 / 60** |
| `<u>` / `</u>` in document | 60 / 60 | **60 / 60** |

**Three rows a reviewer must read against revision 5's table, because they are where the board's answer
shows up:**

- ***"30 days after the Board acts upon the request"* is 1 → 1**, where revision 5 had **1 → 2**. The
  second occurrence revision 5 created no longer exists. **That single row is the identity pass 18
  endorsed, and its disappearance is the whole of §6.**
- ***"120 days after the Board acts upon the request"* is 0 → 1.** A string that was nowhere in the bill.
- ***"120 days"* is 4 → 5.** The four existing sites are **two in G 4** (the determination-effect limit
  and its disapplying proviso), **one in G 4's non-running aggregate**, and **one in M 2's clause (ii)
  tolling aggregate**. §6.3 reads Edit 3's fifth against all four.

**The *"acts upon"* count is 8 → 8**, unchanged from revision 5 and for the same reason (F-7's deeming
removed two and Edit 2 removed a third). All eight live sites were re-located in the live §1 today and
are the same eight revision 5 inventoried; store revision 61 added none and removed none.

**All eight live *"acts upon"* sites in §1, re-located at store revision 61:**

| # | Site | Resolved by Edit 1? |
|---|---|---|
| 1 | the (d) reset — *"last acts upon a request"* | **yes**, by trigger limb 2 |
| 2 | the backstop notice — *"15 days after it acts upon the request"* | removed by Edit 2 |
| 3–4 | G 4's pendency — *"first acts upon it"* ×2 | n/a, already *"first"* |
| 5 | M 2's tolling endpoint | **yes** |
| 6 | M 2's clause (ii) endpoint | **yes** |
| 7 | M 2's retention endpoint — Edit 3's target | **yes** |
| 8 | M 2's 15-day application duty | **yes**, by F-1's deletion |

### 4.2 Conforming amendments — **none required**, and the two new candidates store revision 61 created are chased

**The ten referring provisions revision 5 chased are re-chased and the answer is unchanged on every
one.** Eleven of the twelve rows in revision 5's table are byte-identical in the base (§3), and the
twelfth — M 2's own new sentences — is read below. **Store revision 61 created two new candidates that
revision 5 could not have chased, and both are answered no.**

| Referring provision | Reference | Needs amending? |
|---|---|---|
| **D 1's extension sentence** | *"any notice of a date required by that definition upon the Board's action upon a request"* | **No.** Edit 2 moves the notice's timing, not its source. Pass 18's F-9 is a tightening, routed to [MOO-164](/MOO/issues/MOO-164) as the Policy Director's card 2 and gate 1. Byte-identical at store revision 61. |
| **The decision-keyed floor** (definition, last sentence) | *"a decision or notice required by the preceding sentence"* | **No.** Runs from actual giving, not from a due date. Switched off where no decision issues, which is a consequence and the subject of gate 2, not a stranded reference. Byte-identical. |
| **The R-5 floor** (definition) | *"the period this definition allows for acting upon it"* | **No**, and not reached by any edit. Inoperative for M 2 reconsideration requests. Routed to [MOO-164](/MOO/issues/MOO-164) as card 3. Byte-identical. |
| **The (d) reset** (definition) | *"the month in which the Board last acts upon a request"* | **No.** Trigger limb 2 reaches it expressly; F-8 makes limb 1 symmetric. Byte-identical. |
| **G 4's pendency sentences** | *"until the date on which the Board first acts upon it"* ×2 | **No.** Already keyed to the first act in terms. Byte-identical. |
| **G 4's non-running limb** | *"the period allowed to it for acting upon the request"* | **No.** Unqualified and reaches both request classes. Byte-identical. |
| **G 4's 120-day non-running aggregate** | *"shall not exceed 120 days"* | **No, and this is a new reading created by the figure, not a stranded reference.** G 4's aggregate caps non-running **while an application or request is *pending***, and G 4's own third sentence ends pendency at the Board's **first act** — the date on which Edit 3's 120 days **begin**. The two periods are consecutive, not concurrent, and neither is measured over the other. §6.3. |
| **M 2's clause (ii) 120-day tolling aggregate** | *"the aggregate of all tolling under this subsection shall not exceed 120 days"* | **No, and this is the other new reading.** Clause (ii) is an exception on the **tolling** sentence, introduced by *"except that"*, and caps *"all **tolling** under this subsection"*. The retention sentence is a separate sentence and does not toll anything; it says the application *"retains its filing date"*. Pass 18 held the retention sentence carries **neither** of the tolling limits, and the figures now coinciding does not change which sentence a limit sits in. §6.3 and §9. |
| **D 3's retention and application duty** | *"the confirmation is obtained"* | **No.** Keyed to the confirmation, not to the Board's acting upon a request. Byte-identical. §3.6 carries the one disclosure the figure adds. |
| **M 2's case-decision, judicial-review and Articles 3/4 sentences; M 3** | *"a reconsideration under this subsection"* | **No.** None keys a period to the Board's acting upon a request. |
| **NEW — G 4's reinstatement sentence** (store revision 61) | *"no later than 30 days after the determination is reconsidered or reviewed"* | **No, on the words.** Edit 1's trigger is keyed to a **formula** — *"the Board's acting, or last acting, upon a request"* — and this period is measured from *"the determination **is reconsidered or reviewed**"*, a different verb with the determination as its subject. **The sentence also reaches judicial review**, which is not the Board acting upon anything, so reading Edit 1's deeming into it would give one period two start dates depending on route. The narrow reading is the only coherent one and no amendment is needed. **Stated at length because the phrase is new and a reviewer will raise it.** |
| **NEW — G 4's state-agency death-notice duty** (store revision 61) | *"no later than 30 days after the agency learns of it"* | **No.** Measured from the agency's knowledge, not from any Board act. Edit 1 does not reach it and Edit 3 does not touch it. |
| **Subdivision B 4 f of § 51.1-142.2** | named in Edit 1's trigger | **No.** Edit 1 names it expressly in both limbs; no amendment to § 51.1-142.2 is needed to receive it. |
| **Subsection C's reporting sentence; subdivision J 1** | *"every failure to make a determination, to state a matter…, or to give a notice"* | **No.** Reaches Edit 2's re-keyed notice as a notice, without naming its due date. Store revision 61 added a J line for the state agency's notice; it does not reference any amended sentence. |

**Result: no conforming amendment is required by any of the three edits.** **Fifth consecutive cut at
which the answer is none**, twelve referring provisions chased in both directions and two of them new
today. The reason is unchanged: all three edits move **dates and interpretive rules**, not designators,
defined terms or duties' addressees — and the board's answer changes a number inside a date, which is
the smallest possible footprint for a change of this kind.

---

## 5. Direction of effect — Edit 3 at 120 days

### 5.1 The arithmetic, on the facts the patch is drafted around

Every clock below is keyed to the Board's **first** act, because that is what Edit 1's deeming does and
what §0.2 decided. `R` = the request is filed, day 0; `F` = the Board first acts, day 7; `D` = the
reconsideration is decided, day 85; M 2's own outer bound is 90 days from `R`.

| Clock | Where it comes from | Revision 5 | Revision 6 |
|---|---|---|---|
| the Board's duty to act on the **application** | M 2, second half of the retention sentence, `F + 15` | day 22 | **day 22, unmoved** |
| M 2's **tolling** ends | M 2's tolling sentence, `F + 30` | day 37 | **day 37, unmoved — Edit 3 does not touch the tolling sentence** |
| the **retention** ends | M 2's retention sentence, Edit 3 | day 37 | **day 127** |
| against the decision, day 85 | | **48 days short** | **covers it, 42 days to spare** |
| against the outer bound, day 90 | | 53 days short | **covers it, 37 days to spare** |
| against the application duty, day 22 | | 15 days of margin | **105 days of margin** |

**The board's question is answered on both the ordinary case and the worst case the subsection itself
permits.** At 30 days the retention could not reach a decision M 2 allows the Board 90 days to make,
under any facts, because 30 < 90 − 0. At 120 days it reaches it whenever the Board's first act is no
later than day 30 — and the Board's first act is the act M 2's 90-day sentence starts from, so in
practice it always does.

### 5.2 What revision 6 does to revision 5's net figure, and the memo item that changes

**Revision 5's risk item 3 said: Edit 1 shortens the retention by 78 days on the ordinary facts and
Edit 3 gives back 30 — net −48, retention ending day 37 against a decision on day 85.** On the board's
figure that item is superseded:

- Edit 1 still shortens the retention by `D − F` = **78 days**;
- Edit 3 now gives back **120**;
- **net +42**, and the retention ends **day 127** against a decision on day 85.

**Edit 3 no longer merely cures M 2's self-defeat gap; it delivers the retention's purpose**, which is
what revision 5 §5.3 said 30 days could not do and what the board was asked about. **The Editor's memo
risk item 3 is now wrong as written and must be replaced**, and [MOO-172](/MOO/issues/MOO-172) is the
Policy Director's route for that — they have told me they sent it. **I have not touched the released
summary** ([MOO-175](/MOO/issues/MOO-175) is its own question and is not mine).

### 5.3 The patch is still uniformly member-adverse on **tolling**, and that has not changed

Edit 1 shortens M 2's tolling by `D − F` = 78 days on the ordinary facts; the model is
`charged(X) = min(X + 30, 120)`; card (l) closed at **129 against 128** on pass 18's rebuild, which is
first-action worse by one day, and the Policy Director accepted the correction. **None of that moves,
because Edit 3 does not touch the tolling sentence.** The board lengthened the retention, not the
tolling — which is exactly why §6 exists.

---
## 6. The three items the Policy Director required in the document, not in a comment

### 6.1 Item 1 — the divergence is deliberate, and here is what each period does

**The statement, on the face of the note.** M 2 now contains two periods measured from the same event
by the same words and set at different numbers: the **tolling** endpoint at 30 days and the
**retention** endpoint at 120 days. **That divergence is intended. The two periods do different jobs,
run against different risks, and protect the member against different parties.** They were never one
rule with one number; they were two rules that happened to share a number.

**What the tolling does.** The tolling sentence stops the running of *"the member's final qualifying
retirement date and of any period within which the member or applicant must act under this section or
under subdivision B 4 f of § 51.1-142.2."* Every one of those is **a clock the member must beat**. The
risk it addresses is that the member's own deadlines expire while she is waiting on the Board.
**Its beneficiary is the member and the adverse party is the calendar.** It is finished as soon as the
member knows the outcome and has had a reasonable interval to act on it, which is what 30 days is for,
and it is capped at a 120-day aggregate by clause (ii) precisely because an unbounded tolling would
move the member's retirement date without limit.

**What the retention does.** The retention sentence preserves *"its filing date for the purposes of
subdivisions D 4 and D 5"* — D 4 being the rule that the Board accepts elections **in the order in
which eligible members file complete applications**, and D 5 the waiting list that order feeds.
**The retention is a priority rule, not a deadline rule.** The risk it addresses is not that the member
will miss a date; it is that **the member's place in a queue will be taken by somebody else while the
Board reconsiders**. Its beneficiary is the member and **the adverse party is another applicant**.
Nothing the member can do preserves it, so no interval for the member to act is relevant to its length.

**Why the member needs the longer one, in one sentence.** The tolling has to outlast the member's own
deadlines, which it can do in 30 days because the member is told the outcome and then acts; the
retention has to outlast **the Board's reconsideration**, and M 2's own third sentence gives the Board
**90 days** to complete that — so a retention measured from the **first** act, which Edit 1's deeming
requires, cannot survive the Board's own allotted time in anything under 90 days plus the pendency the
first act consumed. **30 days was arithmetically incapable of the job; 120 is capable of it with 37
days to spare against the outer bound M 2 itself permits.**

**Two different periods doing two different jobs is ordinary drafting. The test is whether the
divergence is legible on the face of the statute, and it is**: the two sentences name different objects
(*"any period within which the member or applicant must act"* against *"its filing date for the
purposes of subdivisions D 4 and D 5"*), use different verbs (*"tolls"* against *"retains"*), and carry
different limits. **A reader who asks why the numbers differ finds the answer in the sentences
themselves without reaching this note**, which is the standard I am required to meet.

### 6.2 Item 2 — the gap between day 37 and day 127, priced

**The window is 90 days per request**, and on the ordinary facts it is day 37 (tolling ends) to day 127
(retention ends), of which **48 days fall before the decision** on day 85 and **42 days after it**.
Inside it the application keeps its D 4 / D 5 filing date while the member's own clocks are running
again.

**It does something, and it does three separable things. Here is each, and whether it bites.**

**(a) For the member, where the Board complies with its own duty: it does nothing, and that is
correct.** The Board's duty to act on the application falls at **day 22** — fifteen days after the first
act, under the second half of the very sentence Edit 3 amends. If the Board performs, the application
has been acted upon by day 22, it is no longer an application awaiting its turn, and the retained filing
date has already done all the work it will ever do. **The gap is then empty by construction.** It is
insurance, and insurance that never pays is not a defect in the policy.

**(b) For the member, where the Board does not comply: the gap is the whole of what the board bought,
and it is the only thing standing between the member and the loss of her place.** On the ordinary facts
the Board is in breach from day 22 and does not resolve the reconsideration until day 85. Under revision
5 the member's priority died on day 37, forty-eight days before the decision that was supposed to
restore it — **so a member who won her reconsideration won a determination about an application that had
already lost its queue position.** Under revision 6 the priority survives to day 127. **The gap is
precisely the remedy for Board delay, and Board delay is the only circumstance in which the retention
was ever going to matter.**

**(c) The gap does not carry the member's own clocks, and that is a real limit on what the board
bought.** Tolling ends on day 37 whatever Edit 3 says. So from day 37 the member's final qualifying
retirement date, and every period within which she must act, are running again — while the application
she is holding a place in the queue for has still not been acted upon. **A preserved queue position is
worth something only if the member can still use the acceptance when it arrives**, and what lets her use
it is the final qualifying retirement date, which the gap does not stop. **So the board's 120 days
delivers the retention's purpose and does not deliver a complete remedy**; the residue is a
member-clock problem, not a retention problem, and the only cure for it would be a change to the
**tolling** endpoint, which §0.2 has already decided the structure of and which is not in scope here.
**I am not drafting it, not carding it, and not treating it as a reason to revisit the figure.** It is
stated so the Policy Director can decide whether it is worth a card of its own, and so that nobody later
reads the board's answer as having bought more than it bought.

**(d) For third parties, the gap is the entire widened cost, and it is 90 days per request.** Under
revision 5 the retention and the tolling expired on the same day, so there was no window in which an
application held a D 4 / D 5 place while nothing else about it was suspended. Under revision 6 there are
**90 such days per request**, and in each of them a later-filed complete application sits behind an
application that may yet be withdrawn, cancelled, or never accepted. **That is not an incidental effect
of the figure; it is the figure.** Three things follow:

- **It is the limb [MOO-170](/MOO/issues/MOO-170) is pricing**, and the number it needs is now 90 days
  of post-tolling retention per request rather than zero. **I have not re-priced anything and will not**
  — [MOO-163](/MOO/issues/MOO-163)'s release priced one 30-day endpoint, and the Policy Director has told
  the Fiscal & Impact Modeler that MOO-170 now prices a 120-day limb.
- **It is why the cap is a paired item.** The board widened the one limb whose cost falls on third
  parties, and widened it by a factor of four. §9.
- **The class of requests that can open such a window widened in the base today**, independently of the
  figure — store revision 61 added a rejected death-benefit claimant and a paying employer to M 2's
  requester class and an omitted-matter failure to its subject class (§3.3). **A pricing model should
  have both changes, not one.**

**So: the window does something. It is empty where the Board performs, it is the whole remedy where the
Board does not, it is bounded by a member clock it does not stop, and it is the whole of the third-party
cost. None of those four readings is a reason to change the figure, and the fourth is the reason the cap
is now live.**

### 6.3 Item 3 — the *Forst* identity argument no longer supports Edit 3, and here is what does

**Stated plainly, as required.** Revision 5 §1.3 recorded that after Edit 3 the phrase *"30 days after
the Board acts upon the request"* appeared **twice** in M 2 and nowhere else in the bill, and that pass
18 tested that identity and endorsed it: *"under Forst the identity is what secures the same meaning for
both."* **At 120 days that argument is unavailable. The identity does not exist. The count table at
§4.1 shows the string at 1 → 1 instead of 1 → 2, and the argument pass 18 endorsed cannot be made about
a phrase that occurs once.** Nothing in this document relies on it, and any reader of revision 5 who
carries that reasoning forward is carrying something that is no longer true.

**What carries Edit 3 instead. Three things, and the first two are stronger than what they replace.**

**1. The identity that actually had to hold still holds, verbatim.** What *Forst* and *Hubbard* secure is
that the **same words** bear the **same meaning** in the same instrument. The words that must bear the
same meaning in both sentences are ***"the Board acts upon the request"*** — the measuring **event** —
and those six words are **byte-identical in both sentences**, before and after the board's answer. The
difference between the two periods is a **number of days**, and a number is not a term whose meaning has
to be construed. **The identity argument was always about the event and never about the figure; the
figure was along for the ride.** Removing the figure from the shared string removes nothing the canon was
doing.

**2. Edit 1's deeming is the real guarantor, it is express, and it does not depend on the figures
matching.** Edit 1 provides that where a period *"begins or ends upon, or is measured from, the Board's
acting, or last acting, upon a request,"* the Board **is deemed** to act on the date of its **first**
act. Both of M 2's periods are measured from the Board's acting upon a request. **So both are keyed to
the same date by express statutory command, not by inference from identical wording.** That is a stronger
guarantee than the canon it replaces — a canon yields to contrary indication, a deeming provision does
not — and it is indifferent to whether the periods are 30 and 30 or 30 and 120. **This is the answer to
give pass 19, and it is the answer I would have given even at 30 days, because the deeming was always
doing the work the identity was being credited for.**

**3. The figure's provenance, and the gap in it, which is disclosed and not buried.** The Policy
Director's recommendation to the board said 120 *"uses a figure already in the subsection."* **That is
true of the subsection and not true of the endpoint.** *"120 days"* appears four times in §1 before this
edit — twice in G 4 (a determination-effect limit and the proviso that disapplies it), once in G 4's
non-running aggregate, and once in **M 2's clause (ii) tolling aggregate** — and **not once as an
endpoint measured from the Board's acting upon a request.** The figure the recommendation pointed at is
clause (ii)'s **aggregate cap on tolling**, which is a different kind of limit on a different object.
**The Policy Director has recorded that they own this gap. I am recording the same thing from the text's
side: the figure is not invented, and the provenance argument is weaker than "already in the
subsection" suggests.**

**And the provenance has a cost that runs the opposite way from the broken identity, which is the one
new finding in this cut.** After Edit 3, *"120 days"* appears **twice in subdivision M 2**: clause (ii)'s
*"the aggregate of all tolling under this subsection shall not exceed 120 days"* and the retention's
*"until 120 days after the Board acts upon the request."* **Two different limits, two different objects,
one number, one subsection.** A reader can be invited to think the retention is the clause (ii) aggregate
applied to the retention, or is subject to it.

**It is foreclosed on the text, and I am stating why rather than relying on it being obvious.** Clause
(ii) is one of two exceptions introduced by *"except that"* **on the tolling sentence**, it is confined
by its own words to *"all **tolling** under this subsection,"* and the retention sentence does not toll
anything — it says the application *"**retains** its filing date."* Pass 18 reached the same conclusion
from the other direction, holding that the retention sentence carries **neither** of the tolling
sentence's two limits. **The figures coinciding does not move a limit from one sentence to another.** But
it makes the misreading easier rather than harder, and **it is a disclosure for the memo and a named
question for pass 19, not a defect in the text.**

**I have not drafted a clarifier.** If the Policy Director wants one, the smallest is five words
appended to the retention sentence — *"and clause (ii) of the preceding sentence does not apply to the
retention of a filing date under this sentence"* — and it is **not** candidate text here, because it
adds a provision nobody agreed and because the cap decision at §9 may make it unnecessary or may need to
be drafted with it. **Raised in the note, which is where an unagreed provision belongs.**

### 6.4 Is the divergence a defect or a choice? A choice — and here is what would make it a defect

**The Policy Director's instruction is that if the divergence is a defect rather than a choice it comes
back as a card with options and goes to the board as a card, and that it is not mine to re-decide. On my
reading it is a choice.** Three tests, and it passes all three:

1. **Legibility.** The two sentences name different objects, use different verbs and carry different
   limits, so the divergence is explicable from the statute without this note (§6.1).
2. **No stranded reference.** Nothing in §1 measures a period from, or conditions anything on, the two
   endpoints being equal. Twelve referring provisions were chased and none does (§4.2).
3. **No reading in which the longer retention makes the member worse off.** The retention is a pure
   addition to the member's position; lengthening it cannot shorten anything else, because no other
   provision is measured from the retention's end.

**What would make it a defect, so the Policy Director and pass 19 have the test and not just the
conclusion:** a provision somewhere in §1 that treats the end of the retention as the end of the
tolling, or that measures a member's duty from the retention's expiry. **There is none at store revision
61 — but the base has moved seven times under this patch and this is exactly the kind of sentence a
future store revision could add.** If one appears, the divergence becomes a defect that day. **That is a
check for whoever applies this, and it is in §8.4's list.**

---
## 7. Drafter's note — every ambiguity revision 6 resolved, and how

**Revision 6 is one figure. Everything below is a choice I had to make to cut it, or a choice I
declined to make.**

### 7.1 What I changed, and what I refused to change with it

**One string moved: Edit 3's READ.** I did not touch Edit 1, Edit 2, the title line, the enacting
clause, the enactment clauses, or any reproduction except where the live base forced a re-splice. **The
smallest change that achieves the agreed policy is a four-word insertion, and that is what revision 6
is.** The temptation at a figure change is to tidy the sentence around it — to align the tolling
endpoint, to add the clarifier at §6.3, to take the cap while the sentence is open. **Each of those is a
provision nobody agreed, and each would have created opposition for free.** They are in the note and in
§9 and nowhere else.

### 7.2 The ambiguity I had to resolve to cut it at all: where the four words go

*"120 days after"* could sit in three places in the sentence: before *"the Board acts upon the request"*
(as drafted), as a trailing *"and in no event later than 120 days after the Board acts upon the
request"*, or as a separate sentence. **I took the first, which is revision 5's structure with one
figure changed, for two reasons.** It keeps the FIND string to 106 characters and the edit to a single
anchored substitution, so the cut is verifiable by counting; and it keeps the sentence's two halves —
the retention and the Board's 15-day application duty — in **one provision**, which is where a duty, its
actor, its deadline and its object belong. **A trailing clause or a second sentence would have split
them.**

### 7.3 Why *"120 days after"* and not *"120 days from"* or *"within 120 days of"*

**Because the subsection already says *"after."*** The tolling endpoint reads *"until 30 days **after**
the Board acts upon the request"*, M 2's filing window reads *"within 30 days **after** the notice …
is given"*, and the retention's own second half reads *"no later than 15 days **after** it acts upon the
request."* **Matching the chapter's existing vocabulary is the rule even where I would write it
differently**, and here it also keeps the board's answer verbatim: the option the board took is worded
*"Lengthen to 120 days **after** the Board acts upon the request."* **The enacted words are the board's
words.**

### 7.4 The figure is written as *"120 days"* and not as *"four months"* or *"120"*

**Days, because every other period in M 2 and in G 4's pendency sentences is in days**, and mixing units
inside one subsection invites a construction question about whether a different unit means a different
measure. **Spelled as *"120 days"*** because that is the form of all four existing *"120 days"* sites in
§1. **No figure in this patch is bracketed**, unlike D 3's `[20]` percent, because the board has decided
this one.

### 7.5 Operative verbs — nothing in this edit creates or removes a duty or a power

*"Retains"* is **indicative**, not *"shall retain"*, and it is the base's own verb. That is correct here
and deliberate: the sentence states a **legal consequence** that attaches to an application by operation
of law, not a duty on anybody and not a permission. **A *"shall"* would have been a defect** — there is
no actor who retains the filing date; the application has it. The duty in the same sentence — *"the
Board shall act upon the application no later than 15 days after it acts upon the request"* — keeps its
*"shall"*, its named actor (the Board), its object (the application), and its deadline (day 22), and
revision 6 does not touch any of the four.

### 7.6 Operative terms — nothing new is defined and nothing new needs defining

**Every term in the inserted words is already in the chapter**: *"days"*, *"the Board"*, *"acts upon"*
(interpreted by Edit 1), *"the request"* (the request for reconsideration that is the sentence's own
subject). ***"Retention"* as a noun appears zero times in §1** and I have not introduced it — which is
also why pass 18's cap text cannot be taken verbatim (§9.3).

### 7.7 Dillon's Rule, and the delegation boundary

**Neither is engaged by revision 6.** No duty or power is conferred on a locality; the actor throughout
is the Board, a state agency. **No rule-making is delegated by this edit** — M 1 requires the Board to
adopt procedures addressing, among other things, *"the waiting list"* and *"the review of the Board's
determinations"*, and the board's figure is an express statutory period that those procedures cannot
shorten or lengthen. **That is worth one line in the memo**: lengthening the retention in the statute
rather than in M 1's procedures is what makes it enforceable by the member.

### 7.8 What I did not do, and why

- **I did not align the tolling endpoint to 120 days.** It would deliver §6.2(c)'s residue, and it is a
  second policy decision the board was not asked and §0.2 has already structured. **Not drafted, not
  carded, named in §6.2(c).**
- **I did not draft the clause (ii) clarifier.** §6.3. An unagreed provision belongs in the note.
- **I did not put the cap in the operative text.** The Policy Director's instruction, and §9 holds it.
- **I did not re-price anything.** [MOO-170](/MOO/issues/MOO-170) is the Fiscal & Impact Modeler's.
- **I did not reopen the Editor's released summary.** [MOO-172](/MOO/issues/MOO-172) carries the figure
  correction and the Policy Director has sent it. §5.2 records that risk item 3 is now wrong as written
  so the record shows I found it; the fix is not mine.
- **I did not touch any of [MOO-164](/MOO/issues/MOO-164)'s six cards**, and I confirm from the text
  that nothing in them turns on whether Edit 3 says 30 days or 120: F-9 is D 1's descriptor, F-5 is the
  definition's R-5 period, and neither is measured from the retention.
- **I did not decide the cap.** §9 is candidate text and an answer to a question, not a recommendation
  to enact.

---

## 8. Verification at store revision 61

### 8.1 The base, and the three anchors

| | |
|---|---|
| document | `bill-text-s8` on [MOO-42](/MOO/issues/MOO-42) |
| revision id | `3efccfe2-8332-4f4a-82ba-a9347141287f` |
| store revision | **61** |
| characters | **271,611** |
| enacted §1 | **117,980** characters, measured from `## 1. The bill` to `## 2. Section-by-section`, which is the convention store revision 61's own record uses and reports at 117,980 |
| title line | unchanged at store revision 61 |

**All three FIND strings resolve exactly once in the whole document and exactly once in §1**, counted on
the live body today, not carried forward:

| Edit | FIND chars | count, whole document | count, §1 | READ chars | delta |
|---|---|---|---|---|---|
| Edit 1 | 135 | **1** | **1** | 804 | **+669** |
| Edit 2 | 106 | **1** | **1** | 120 | **+14** |
| Edit 3 | 106 | **1** | **1** | 121 | **+15** |

**Edit 2's short form resolves twice in §1**, as at every cut since revision 2 — the second being M 2's
application duty — which is why the anchor is the full clause. **Re-counted: 2.**

### 8.2 Post-application invariants — applied to a **copy**, every one checked

Every figure in §4.1 was produced by applying all three edits to a copy of the live body and measuring
both the copy and the live body with the same code. Specifically verified:

- **document delta +698** to the character, and **enacted §1 delta +698** — the two agree, which is the
  check that no edit landed outside §1;
- **the Policy Director's prediction re-derived rather than taken.** Edit 3's READ is **121** characters
  against a **106**-character FIND, so **+15**; revision 5's was **120** against 106, so **+14**. The
  same three edits cut with revision 5's Edit 3 on **this** base give **+697**, and with the board's
  figure **+698**. **Both figures confirmed, independently of the issue description.**
- **`<u>` and `</u>` balance 60 / 60 in §1 and 60 / 60 in the document**, before and after;
- ***"or an application"* is 0 in §1 both before and after**, so F-1's deletion remains verified by
  absence and store revision 61 did not reintroduce the phrase;
- ***"until the Board acts upon the request"* is 1 → 0** and ***"120 days after the Board acts upon the
  request"* is 0 → 1**, which together are the whole of the board's answer as it appears in the text;
- ***"30 days after the Board acts upon the request"* is 1 → 1**, which is the broken identity measured
  rather than asserted;
- ***"retention"* is 0 → 0 in §1** — revision 6 introduces no new noun;
- **all eight live *"acts upon"* sites** re-located in the live §1 and accounted for in §4.1's table;
- **the amended interpretation paragraph re-read end to end** and still sits immediately before
  `<u>**B.** The Program is established.`;
- **M 2 re-counted at eight sentences** with the retention sentence fifth, so §1.3's descriptor is
  current;
- **both of G 4's express *"first"*s re-counted** (*"first acts upon it"* ×2), which is the condition on
  which revision 2's G 4 edit stays withdrawn;
- **all eight revision-5 reproductions re-spliced and diffed character for character**: **seven
  byte-identical**, **one changed** — M 2, +494 characters (§3.3).

### 8.3 What I did not verify, stated as a limit

I did not re-read the whole of G 4's ~29,600 characters or the whole of subsection D; I spliced and
diffed the provisions this patch reaches and the provisions that reference them, and I read store
revision 61's own record and sweep (§0.0-61 and §5.40) for what it did outside them. **Two limits
matter:**

1. **Store revision 61's thirteen substitutions have not been counsel-reviewed.**
   [MOO-169](/MOO/issues/MOO-169) was commissioned to review them and **did not complete** — it reported
   a terminal limit failure at 14:27 and was moved to `blocked` by the runtime, with no findings
   delivered. **So revision 6 is cut against an unreviewed base.** That is not a defect in this cut, but
   it is a fact the Policy Director should hold before commissioning the single pass 19, because pass 19
   would otherwise be the first review of anything in store revision 61 — and it is scoped to Edit 3's
   figure, the broken identity and the cap, not to the base.
2. **If store revision 61 reached a cross-reference listed in §4.2 outside the sentences I spliced, this
   cut would not have caught it.** I read its own sweep, which reports none, and I chased the two new
   G 4 sentences by hand (§4.2).

### 8.4 Not applied to the store — and the warning has now fired five times

**Nothing in this document has been applied to `bill-text-s8`.** All work was done on a copy in this
run's scratch directory and no team file was modified. **Application is a separate step, needs its own
re-verification at that moment, and nothing here authorises it.**

**The standing warning, restated because it has now fired five times out of seven.** The base has moved
under this patch at store revisions 57, 58, 59, 60 and 61. **At every one of those moves all three
anchors still resolved, and at five of them a reproduction was stale anyway** — today's stale one being
**M 2, the provision the one live text change is inside.** Whoever applies this must re-resolve the FIND
counts and re-splice every §3 reproduction against the base **as it stands at the moment of
application**, not against store revision 61. **An anchor that still resolves is not evidence the
reproductions are current.**

**Two checks to add to that list at application, both new today:**

- **§6.4's defect test** — confirm that no provision added since store revision 61 measures a member's
  duty from the end of the retention, or treats the retention's end as the tolling's end. If one has
  been added, the 30 / 120 divergence has become a defect and the figure goes back to the Policy
  Director as a card.
- ***"120 days"* in §1** — re-count it. It is 4 before this patch and 5 after. If the base has added
  more, §6.3's foreclosure argument has to be re-read against them.

---
## 9. F-6's cap — held candidate text, and the 120/120 collision answered

**Nothing in this section is in the operative text, and nothing in it is a recommendation to enact.**
Card 4 was declined on [MOO-163](/MOO/issues/MOO-163)'s released price and returns on two named
triggers; the board's figure widens the one limb whose cost falls on third parties, so the cap is now a
paired item and **the Policy Director decides it when [MOO-170](/MOO/issues/MOO-170)'s chaining answer
lands.** What follows is the text and the answer to one question.

### 9.1 The question, and the answer on the text: **the second horn, and it is worse than framed**

**Pass 18's cap, as drafted:**

> …, except that (i) no second or subsequent request for reconsideration of the same determination
> continues the retention and (ii) the aggregate of all retention under this sentence shall not exceed
> 120 days.

**At 30 days per request the two clauses did different work.** Clause (i) barred repeat requests about
**the same determination**; clause (ii) capped the total at 120, so **four** requests about **different**
determinations were needed to exhaust it. Each clause reached a case the other did not.

**At 120 days per request, the answer on the text is the Policy Director's second horn — the aggregate is
measured over something that includes the pendency period — and the consequence is one step worse than
the question allows for: it cuts the board's grant on the *first* request alone, before any chain
exists.**

**The reasoning, on the words.** Clause (ii) caps *"the aggregate of all **retention** under this
sentence."* The thing it aggregates is therefore the **period for which an application retains its
filing date** under the sentence. **The sentence fixes only when that period *ends*** — *"until 120 days
after the Board acts upon the request"* — and says nothing about when it begins. It begins when the
application becomes *"the subject of a request for reconsideration"*, which is when the **request is
filed**. So:

| | |
|---|---|
| retention begins | the request is filed, **day 0** |
| retention ends | 120 days after the Board's first act, **day 127** |
| **retention measured under clause (ii)** | **127 days** |
| clause (ii)'s aggregate | **120 days** |
| **effect** | the aggregate is exhausted on **day 120**, **7 days before the board's grant expires** |

**So the cap as drafted takes 7 days off the board's own 120 on the ordinary facts, on a single request,
with no chaining at all — and it takes more the longer the Board sits on the request before first
acting.** The amount it takes is exactly the pendency period, which the member does not control. **A cap
that silently shortens the figure the board just chose, by an amount the Board itself sets, cannot be
enacted in that form.**

**And clause (i) is not merely surplusage on this reading — it is unreachable.** The aggregate bites on
day 120 of the first request, so no second request ever gets to be barred by clause (i). Clause (i)
would never operate.

**The Policy Director's first horn is also fatal, and it is what you get if you fix the measurement.**
Suppose clause (ii) were redrafted to aggregate only the **post-act tail** — the 120 days the board
granted, excluding pendency. Then the first request's tail is 120 days, the aggregate is 120 days, and
the aggregate is exhausted **exactly** by request one. Clause (i) again has nothing to do. **This is the
structural point and it does not depend on drafting at all: at 120 days per request, no aggregate set at
120 can leave clause (i) any work. The two clauses can only do different jobs if the aggregate exceeds
the per-request figure.** Pass 18 drafted a pair that was coherent at 30 and cannot be coherent at 120
in any form that keeps both numbers at 120.

**So, answering the question as put: on the text it is the second reading, clause (ii) cuts into the
board's 120 days, and clause (i) is unreachable rather than surplusage. Fixing the measurement converts
the defect into the first reading, where clause (i) is surplusage. Either way the pair does not survive
the board's figure.**

### 9.2 The cap in the smallest form that survives the collision — **candidate A**

**Drop the aggregate. Widen the per-request bar.** Once the per-request figure is 120 days, the only
bound the cap is actually for is *"one retention period per application, not an indefinite chain"* — and
a single clause says that without a figure, without an aggregate, and without a measurement question.

> **Edit 3 as it would read with the cap** (the cap is the underlined words; the rest is Edit 3 as cut in
> revision 6):
>
> An application that is the subject of a request for reconsideration under this subsection retains its
> filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the
> request, <u>except that no application retains its filing date under this sentence by reason of a
> second or subsequent request for reconsideration</u>, and the Board shall act upon the application no
> later than 15 days after it acts upon the request.

**Cost: 136 characters. Edit 3's READ becomes +151 against its FIND, and the patch becomes +834.**

**Why this is the smallest form that works, point by point:**

- **No figure, so no collision.** It cannot cut the board's grant, because it does not measure anything.
- **No aggregate, so no measurement question** — the day-0-or-day-7 problem at §9.1 disappears.
- **It bounds the chain completely.** One application, one retention period, however many determinations
  the Board makes and however many requests the member files. That is a harder bound than clause (ii)'s
  120-day aggregate ever was.
- **It introduces no new word.** *"Retains its filing date"* and *"second or subsequent request for
  reconsideration"* are both already in M 2 — the latter verbatim in the tolling sentence's clause (i),
  so the cap borrows the subsection's own formula rather than inventing one.
- **It avoids *"retention."*** The noun appears **zero** times in §1 (§4.1), so pass 18's clause (ii)
  would have introduced an undefined operative term into a sentence that already has a perfectly good
  verb. **That is an independent reason not to take pass 18's words even if the figures had not
  collided.**
- **It keeps the sentence's duty intact** — actor, object, deadline and consequence stay in the same
  provision, in the same order.

**The one policy consequence, named rather than buried.** Candidate A **drops the
*"of the same determination"* limit**. Pass 18's clause (i) barred only repeat requests about the *same*
determination, leaving a chain open across *successive* determinations — which is precisely the chaining
limb [MOO-170](/MOO/issues/MOO-170) is pricing. **Candidate A bars the second request whatever it is
about.** That is what makes it a cap rather than a gesture, and it is a real narrowing: a member whose
first reconsideration succeeds and who is then adversely affected by a *second, different* determination
about the same application gets no retention the second time. **That is the Policy Director's call, not
mine, and it is the whole of what is being decided.**

### 9.3 If the Policy Director wants to keep the same-determination limit — **candidate B, and its price**

Keeping clause (i)'s narrower bar means the chain must be bounded by an aggregate, and **the aggregate
must exceed 120 or clause (i) is dead** (§9.1). It must also be drafted to measure only the post-act
tail, or it eats the grant:

> …, except that (i) no application retains its filing date under this sentence by reason of a second or
> subsequent request for reconsideration of the same determination or of the same failure and (ii) the
> aggregate of all periods for which an application retains its filing date under this sentence after
> the Board acts upon a request shall not exceed `[240]` days

**Cost: 358 characters; the patch becomes +1,056.** **The figure is bracketed because it is not decided
and I am not choosing it** — any number at or below 120 reproduces the collision. `[240]` is shown only
to make the structure readable; it is two retention periods and it is a policy choice with its own
third-party cost, which nobody has priced.

**I do not recommend candidate B.** It is two and a half times the text, it reintroduces an aggregate
and a measurement question, and it needs a new figure the board has not been asked for. **Candidate A is
the answer to the question as asked: the smallest form that survives the collision.**

### 9.4 A third option the Policy Director should have, because it is cheaper than both

**Take no cap and let the Board's own duty do the work.** The same sentence already requires the Board to
act on the application **within 15 days of acting on the request** — day 22. A chain of retentions can
only exist where the Board **breaches that duty repeatedly**, because a determined application is no
longer in the D 4 queue awaiting its turn. **So the chaining exposure MOO-170 is pricing is conditional
on serial Board breach of an express statutory deadline**, and the cap buys protection against a
hypothesis the statute already forbids. **That is an argument for the price, not a drafting conclusion**,
and it belongs in MOO-170's hands rather than mine — but it is the cheapest of the three and it would be
wrong of me to give you two priced options and hide the free one.

**All of §9 is held. None of it is in the operative text. The decision is the Policy Director's when
MOO-170's chaining answer lands.**

---

## 10. Status and next step

**Revision 6 is cut and verified.**

1. **The board's answer is in the text**: Edit 3 reads *"until 120 days after the Board acts upon the
   request"*, **+15 characters**, and the patch is **+698**. Both figures re-derived on the live base, not
   taken (§8.2).
2. **The cut is whole, not incremental.** All three anchors re-resolved and counted in the document and
   in §1; all eight reproductions re-spliced and diffed (seven byte-identical, M 2 changed and replaced);
   every §4.1 count re-run; every §8.2 invariant re-run on an applied copy; the character delta verified
   in both the document and enacted §1.
3. **The three items the Policy Director required are in the document**: the divergence stated as
   deliberate with each period's job (§6.1); the day 37-to-day 127 window priced in four limbs, three of
   which bite (§6.2); and the *Forst* identity recorded as gone, with the two stronger grounds that carry
   Edit 3 instead and the figure-provenance gap disclosed from the text's side (§6.3).
4. **The 120/120 collision is answered on the text** — the second reading, cutting the board's grant by
   the pendency period on the first request alone, with clause (i) unreachable — and **the cap is drafted
   as held candidate text in three forms with their prices and the one policy consequence named** (§9).
5. **One new finding, disclosed not buried**: *"120 days"* now appears twice in M 2 with two different
   objects, which is foreclosed on the text and is a question for pass 19 (§6.3).
6. **One limit the Policy Director should hold before commissioning pass 19**:
   [MOO-169](/MOO/issues/MOO-169) did not complete, so **store revision 61 is an unreviewed base**
   (§8.3).

**What I did not do, restated so the boundary is on the record:** nothing applied to the store; the cap
not decided and not in the operative text; nothing re-priced; the Editor's released summary not
reopened; none of [MOO-164](/MOO/issues/MOO-164)'s six cards touched; the bounded re-review **not**
commissioned, per §5 of the Policy Director's instruction — **one** pass 19 after the cap decision, not
one per change.

**Next step is the Policy Director's**, on the sequencing they set: hold revision 6, decide the cap when
MOO-170's chaining answer lands, then commission the single bounded pass 19 to
[@Red Team / Counsel Reviewer](agent://d71e111e-1296-4d66-81ac-750dcc8d8681) covering Edit 3's new
figure, the broken identity and the cap if it is taken.

**Not applied to the store. Application remains a separate step and a separate decision, and it needs
its own re-verification at that moment.**

---

**INTERNAL WORKING DRAFT. Not a Division of Legislative Services bill. Not reviewed by counsel, and
nothing in it states or implies that it has been. Pre-decisional and internal.**
