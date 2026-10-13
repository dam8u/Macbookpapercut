# MOO-214 — counsel pass on MOO-164 revision 7

**Internal risk analysis. Not legal advice. Nothing here states or implies that counsel or DLS has cleared any part of this cut. Pre-decisional and internal.**

**13 findings: 0 fatal, 6 serious, 4 moderate, 3 minor.** Plus 12 null results stated expressly, and 4 direct answers.

Base: `bill70.md` at store revision 70, kit at commit `18305c2`. All three scripts run clean as published — `verify_r70_v7.py` 0 failures, `apply164.py` +3,375 with everything outside §1 byte-identical, `check_doc_vs_kit.py` 0 mismatches. **I then broke `check_doc_vs_kit.py` three ways; see S5.** Sentence numbering below is of subdivision D 1 **as applied** (`applied.md`): s11 = the lateness sentence, s12 = 164-8's new sentence, s13 = the disclosure sentence as amended by 164-13.

---

## 1. The strongest case against, in the Board's voice

> *The Lab has spent seven revisions building a machine that tells members about rights and then, at the last turn, takes the rights back. Look at what the member actually gets. Subdivision D 1 will now require us to print, in our own notice, that she "may file that notice of retirement ... no later than 30 days after the Board gives that notice." We will print it. She will read it. And for every member whose retirement has already taken effect — which is most of the members who get a late notice at all, because a notice is late precisely when the dates have already run — the window described in that paragraph is closed on the day it is written. We did not close it. The Lab closed it, in the same sentence, in the clause after the comma. We are being asked to publish a statement of rights that is wrong for the class it is addressed to, and then we will be the ones sued for it.*
>
> *Second: the Lab's own cure for finding F1 identifies the duty it means to revive by a phrase that appears nowhere in the Code. There are three duties in that definition to give the member written notice. The exception names none of them by their words. We will read it as naming the one that fits best and act accordingly, and when the Lab says we read it wrong, the answer is that it never said which one it meant.*
>
> *Third: the Lab says the report required by subsection J will catch our failures to disclose. Read subsection J. The phrase it relies on is not in it. The report catches late notices and matters some other provision sends to the report. It does not catch a failure to state. So the Lab has written a disclosure duty into the written statement — the single document the member actually reads, the one that starts her 30-day clock — and subsection M, which lets a person complain of "a failure of the Board to state in a certification or notice a matter this section requires to be stated in it," does not reach a written statement. The duty is real and the remedy is nowhere. That is a press release.*
>
> *Finally, the Lab is about to recommend this to the Director on the strength of a consistency check that cannot see a swapped block, cannot see a block outside §3, cannot see a block in a plain code fence, and today does not see one of the blocks in §3 of its own document.*

---

## 2. Findings

### SERIOUS

**S1 — 164-8 and 164-13(iv) point their "described in" references at structurally different sentences, and only one of them carries a lateness qualifier. Clause (iv) may overstate the right in the ordinary case.**

s12 says "any notice described in **the preceding sentence**." The preceding sentence is s11, whose operative condition is "**later than the time required by that definition**." Two readings are available: (α) any notice *of the kinds* listed in s11; (β) any notice *given late, as described in* s11. Clause (iv) says "a notice described in **this sentence**" — and s13 is a neutral list of three documents with no lateness qualifier anywhere outside clause (i)'s subject-matter. So clause (iv) is unambiguously (α) while s12 is ambiguous between (α) and (β).

*Failure scenario.* The Board gives the written statement 1 February; the s7 filing period expires 3 March. The member requests a later final qualifying retirement date on 15 April — she may do so "at any time before the date that would otherwise apply." The Board approves on 20 May and gives notice of the later approved date on 28 May: **eight days after the approval, perfectly on time under the definition.** Clause (iv), printed in that very notice, tells her she may file a replacement notice of retirement by 27 June. On reading (β), s12 gives her nothing, because the notice was not late. She files on 20 June, the Board rejects it as outside the s7 period, and her defence is a disclosure the Board will say was simply wrong.

This is not a marginal case. A later-approved-date request is filed *after* the written statement by construction, so the filing period has normally expired before any such notice issues. Reading (β) empties the provision in its commonest application.

*Fix direction.* Three words in s12: "any notice **of a kind** described in the preceding sentence." Or add ", whether or not given later than the time required by that definition,".

---

**S2 — Clause (iv) discloses a 30-day window that is void on arrival for the already-retired member, and the bar is stated as an afterthought rather than a precondition.**

s12's bar: "no notice may be filed under this sentence after the member's retirement has taken effect." Clause (iv) repeats it, in both cases *after* the grant.

*Failure scenario.* Written statement 1 February; filing period expires 3 March. The member files her § 51.1-153 notice on 20 February stating an effective date of 1 April. Her request tolls; the Board acts 10 May and gives the R-6 notice on 20 June — late. s11 engages: her final qualifying retirement date is extended, and s11 expressly says she "may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice," i.e. 1 July. She wants 1 July. **Her retirement took effect on 1 April. The window s12 opens on 20 June was already closed on 20 June.** Clause (iv) in the Board's notice told her she had 30 days.

Worse for a subclass: s9's second limb makes retirement "take effect on that date" **retroactively** where the notice was filed after its stated effective date. For that member the barring event can be in the past at the moment the Board gives the notice, and she cannot know it without parsing s9.

I accept the policy: you cannot unretire her, and my own MOO-209 sentence was that she "gets nothing from this vehicle." The defect is not the bar. **The defect is a disclosure that presents a window first and the disqualifying condition second**, in a document whose whole purpose is reliance by a member without counsel.

*Fix direction.* State the condition in the trigger, not the tail: "(iv) that where the Board gives a notice described in this sentence after the expiration of the period ... **and the member's retirement has not taken effect**, the member may file ...". And a separate question for the Director, which is policy and not mine: s11 grants a right the already-retired member cannot exercise. That gap is in the base at store revision 70; 164-8 confirms it rather than creating it, but it should be surfaced, not left silent.

---

**S3 — 164-7's exception identifies R-6 by a paraphrase that matches at least two duties and possibly three. The cut already contains a determinate descriptor and does not use it.**

Counted against the base, inside the definition of "final qualifying retirement date":

| | duty | deadline keyed to |
|---|---|---|
| R-3 | "shall give the member written notice of **its determination and of the reasons for it**" | 30 days after the request is filed |
| R-4b | "shall give the member written notice of **any later date approved** after that statement" | 15 days after the approval |
| R-6 | "it shall give the member written notice of **that date**" | 15 days after it acts upon the request |

`"give the member written notice of that date"` = 1 in §1. `"written notice of the member's final qualifying retirement date"` = **0**. The exception's words are a paraphrase, and R-4b answers it squarely: by the definition's first sentence, a later approved date **is** the member's final qualifying retirement date. R-3 answers it on a second step: a determination approving a later date is a determination of that date.

This is the §9.6 principle the Drafting Specialist set, applied against its author. Cross-reference by paraphrase.

*Failure scenario.* The Board argues the exception names R-4b, whose 15 days runs "after the approval" — an event that in the deemed case never occurs — and therefore that the exception is spent without ever touching R-6. The member argues R-6 is the better fit. She is probably right, but she has to win an argument the text should never have put to her. The tail risk is R-3: the exception, read to include R-3, makes the deeming "determine the date by which the Board is required to **act upon a request**" for R-3's purposes — the exact thing the saving's first limb exists to forbid — and the deemed act date is the day after expiry, which hands the Board a textual hook for having acted in time.

*Fix direction — and this is the single most valuable change in this review.* **Use the descriptor the cut has already coined.** After 164-5 and 164-13(a), the string "notice of a date required by that definition by reason of the Board's action upon a request" resolves **exactly twice** in §1 (0 times in the base), and both uses name R-6's notice and nothing else. Replace the exception's second limb with "the duty of the Board under the definition of 'final qualifying retirement date' in subsection A to give a notice of a date required by that definition by reason of the Board's action upon a request." That descriptor is (a) determinate, (b) **not deadline-keyed**, so it survives MOO-141 Edit 2 for the same reason you rejected the four-word lift, and (c) conformed to 164-5 and 164-13, so all three move together or not at all. It costs nothing and it closes S3 without re-opening anything.

---

**S4 — The disclosure duty 164-13 creates has no enforcement route as to the written statement, and the subsection J route you relied on does not exist.**

You wrote that you rely on "subsection J's report reaching *'every failure … to state a matter this section requires to be stated.'*" **Counted in J 1: "failure to state" = 0. "requires to be stated" = 0.** The phrase is not in subsection J. J 1's two relevant limbs are "every failure of the Board to make a determination, or to give a notice, **within a period required by this section**" — lateness, not content — and "every other matter this section requires the Board to state **in that report**," which is a pointer to provisions that expressly route something into the report. Nothing routes a failure to state clause (iv) there. D 1 s6 does route failures into the J report, but s6 is confined on its face to "a failure to state in the Board's **certification** every matter **this subdivision** requires to be stated **in it**" — count of "in the Board's certification" in D 1 = 1, and it is s6's. The written statement and the two notices are not certifications.

Subsection M partly saves you, but only partly. M 2's trigger is "a failure of the Board to state in **a certification or notice** a matter this section requires to be stated in it." **"written statement" appears 0 times in M 2**, and the giving rule at the end of subsection A treats "a written statement, notice, or certification" as three species. So:

| failure | M 2 review | J report |
|---|---|---|
| to state clause (iv) in a **notice** | **yes** | no |
| to state clauses (i)–(iv) in the **written statement** | **no** | no |

*Failure scenario.* The Board issues written statements that omit clause (ii) and clause (iv). A member who files a § 51.1-153 notice she would have dated differently had she been told seeks reconsideration under M 2. The Board demurs: the written statement is not a certification and not a notice; M 2 does not reach it; and the J report has no failure-to-state limb to catch it either. She has no administrative remedy and, having no case decision, no route into Article 5 of the Administrative Process Act.

Most of this is a base defect and I am not asking you to fix the base. But **164-13 enlarges an unenforceable duty**, and the written statement is the document the s7 filing clock runs from, so it is the one that matters most.

*Fix direction.* Smallest: a conforming sentence in D 1 on the model of s6, extending the failure-to-state and J-report machinery to the written statement and the notices required by that definition. Alternative, outside this cut: amend M 2's trigger to "in a certification, written statement, or notice" (2 occurrences of "certification or notice" in M 2). The Director should decide whether that is a MOO-164 item or a new one.

---

**S5 — `check_doc_vs_kit.py` passes on three separately corrupted documents, and today it already fails to see one block in §3 of the live document.**

I broke it rather than argue with it. All runs below print **"0 mismatch(es)"** and exit 0.

1. **Pairing swap.** I exchanged 164-8's READ block with 164-13(b)'s READ block in §3 of `moo164_rev7.md`. The document now states that 164-8 inserts clause (iv) into the disclosure sentence and that 164-13(b) inserts the 30-day window sentence — a complete mis-statement of two of the four edits in scope. **0 mismatches.** The script tests set membership in both directions and the two counts; it never asserts that FIND block *n* is paired with its own READ, nor that blocks alternate.
2. **Out of §3.** `s3 = doc[doc.index('\n## 3. The patch'):doc.index('\n## 4.')]`. I pasted revision 6's superseded 164-7 exception, verbatim and unlabelled, immediately before `## 4.`. **0 mismatches.** There are **10 fenced blocks outside §3** in the current document, none of them checked — and §17, the section that explains revision 7's re-cuts, is where a superseded text is most likely to survive.
3. **Fence shape.** The regex is `>\n> ```\n((?:> [^\n]*\n)+?)> ``` ` — it requires a blockquoted fence preceded by a bare `>` line. I added a superseded 164-8 tail inside §3 in a plain code fence. **0 mismatches.**
4. **Already live.** §3 contains **27 fenced blocks; the script captures 26.** The uncaptured one is 164-1's revision-1-to-4 text, introduced by `revision-1-to-4 text was:` followed by a blank line and then `> ``` `. It is correctly labelled as superseded today, so no harm — but it is proof that the extractor silently drops blocks from the live document, which is finding F5 one level up, exactly as you suspected.
5. **Marker regex.** `\*\*[^*\n]*(?:FIND|READ)[^*\n]*\*\*` matches any bold run containing those substrings. §3 currently has **four** such matches that are not labels, including `**The FIND is the full clause and not the bare phrase, deliberately.**` and `** Edit 164-5's FIND sits in the **`. None flips a label today because a real label is always nearer. Note that `ALREADY`, `SPREAD`, `FINDING` and `FINDINGS` all match — and this team writes `**FINDING F19**`.

*Fix direction.* (a) Scan the whole document, not §3, and whitelist by label rather than by section. (b) Assert `len(captured_fences) == total fence count` in the scanned range — a capture that silently matches nothing is the bug the script exists to prevent. (c) Assert alternation and pair each FIND with the READ that follows it, then check the **pair** against the kit, not the two strings separately. (d) Anchor the marker regex to `^\*\*(?:\S+ — )?(?:FIND|READ):?\*\*` or require a word boundary. (e) Assert the document's stated per-edit deltas against `len(r)-len(f)` — the arithmetic in §3 is unchecked today.

---

**S6 — R-6's notice starts two 30-day clocks that run from mailing, in a case the member has no reason to expect, and 164-8 newly makes one of them a forfeiture.**

You asked whether the member now gets a notice she can be prejudiced by. She does, and the prejudice is new.

The giving rule in subsection A: a notice "is given on the date the Board **mails** it ... or transmits it electronically," not on receipt (+3 days if mailed, by the second limb). Clocks that run from R-6's notice: s12's 30-day refiling window (**new**, and a forfeiture — miss it and the right is gone); and M 2's 30 days to seek reconsideration of a failure to state a matter, "within 30 days after the certification or notice is given." Before this cut, a member who never received an R-6 notice lost nothing she could have had. After 164-8 she loses the refiling right, and clause (iv) — the disclosure meant to warn her — is printed in the document that did not arrive.

*Failure scenario.* The Board mails the R-6 notice to a stale address on 20 June. It is "given" 20 June. The window closes 23 July (mailed, +3). The member learns of her extended final qualifying retirement date on 1 August from her payroll office. She has no vehicle and no reconsideration route, and the only document that would have told her either is the one she never saw.

*Fix direction.* Drafting Specialist's call between: key s12's 30 days to the later of the giving and the member's actual receipt; or lengthen the window; or add a saving for non-receipt. Note the base already has a non-receipt problem across the section — I am flagging it here only because 164-8 attaches a **forfeiture** to it for the first time.

---

### MODERATE

**M1 — Clause (iv) omits the two operative limbs of s12: the timeliness deeming and the supersession.**

Word by word, s12 vs clause (iv):

| s12 | clause (iv) | effect |
|---|---|---|
| "any notice described in **the preceding sentence**" | "a notice described in **this sentence**" | **S1** |
| "the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives the notice" | same, "**that** notice" | immaterial |
| "a notice so filed **is filed within the period allowed by this subdivision**" | *absent* | **M1** |
| "and **supersedes any notice of retirement previously filed by the member**" | *absent* | **M1** |
| "except that no notice may be filed under this sentence after the member's retirement has taken effect" | "and that no such notice may be filed after the member's retirement has taken effect" | **S2**, and see m1 |

You asked whether you had understated the right. **Yes, here, and in the part that matters most.** Supersession is the whole benefit.

*Failure scenario.* The member filed a notice on 20 February stating 1 April. On 28 May she receives a notice carrying clause (iv) telling her she "may file ... a notice replacing a notice of retirement already filed by the member." She cannot tell whether the replacement displaces the first notice, is a nullity because a notice is already on file, or sits alongside it with her retirement still taking effect 1 April. She does nothing, because doing nothing is the safe-looking choice, and she loses the later date she was entitled to state under s11. A member acting on a disclosure needs to know that the new notice wins.

*Fix.* Append to clause (iv): "and that a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member."

---

**M2 — 164-12 puts a second definition of "pending" in subsection G, three sentences from the first, in near-identical words and with a different endpoint, and nothing in the text marks the divergence.**

As applied, subsection G now contains both:

- G 4: "For the purposes of this subdivision an application for a disability retirement allowance is pending from the date on which the member files it until the date on which **the Board first acts upon it**."
- G 2 (new): "For the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which **the Board grants or denies it**."

I think the divergence is substantively right — G 2 is about permitting and excusing payment, G 4 about stopping clocks and barring determinations, and they should not end on the same day. **But the text gives no signal**, and the two sentences are close enough in wording that a reader will take one of them for a slip.

*Failure scenario.* Member files a disability application 1 March. The Board refers it to the Medical Board on 1 April — its first act. It denies the application 1 September. Under G 4 the application ceased to be pending on 1 April, so the subdivision 2 clocks resume and the bar on determining lifts. Under G 2 as amended it remains pending until 1 September, so allowance payments through August are excused. Board counsel, reading only the definition that names the application in full — G 4's, since G 2's says "such an application" — treats pendency as having ended 1 April, concludes the G 2 saving does not excuse the April-to-August payments, and suspends the member's allowance or re-opens a determination already taken effect.

*Fix.* Either conform the endpoints, or mark the divergence in two words: "For the purposes of this subdivision, **and notwithstanding the definition in subdivision 4**, ...".

To your direct question — **is a reader of G 2 alone misled?** No; G 2 alone is coherent. The reader who is misled is the one who reads G 2 and G 4 together, which is every reader who has to apply either.

---

**M3 — 164-12's "such an application" is a back-reference across a sentence boundary, where the model it copies uses the full noun phrase.**

The new sentence opens "For the purposes of this subdivision, **such an application** is pending ...". Its antecedent — "an application of the member for a disability retirement allowance under this chapter" — is in the *previous* sentence. G 4's equivalent, which this is modelled on, is self-contained: "an application for a disability retirement allowance is pending from ...". This is the liftability guard the Director adopted at MOO-206, failing in a new sentence.

It resolves today, in sequence. It stops resolving if any later edit inserts a sentence between the two, or if the definition is relocated to subsection A where this section's other definitions live. Cost of the fix: eleven words. *Fix:* write the noun phrase out, as G 4 does.

---

**M4 — the asymmetry argument is principled in its reason and unsafe in its form. F9 bites harder than it did.**

Your §17.3 argument is correct as a statement of *why* the two exception lists differ, and I accept it. It is not an answer to F9, because F9 was never about the reason — it was about a reader who has only the text. If both patches land, subsection M will carry two deeming sentences and two savings, in adjacent text, with exception lists of different length and no cross-reference between them. Revision 7 widened that divergence from zero named duties to one.

*Failure scenario.* A court construing MOO-141 Edit 1's saving applies *expressio unius*: the drafter excepted R-6 from the other saving and did not except it here, so the omission is deliberate, so R-6 is **not** excepted from Edit 1's saving. That is the adverse reading, it is available on the face of the text, and the only answer to it lives in a Lab document the court will never see.

*Fix.* This does not need F9's full joint-decision remedy. One sentence in whichever saving lands second — "the exceptions stated in this sentence and in [the other] are cumulative," or an express cross-reference — removes the inference. Flag for the Editor: **this is a must-appear item in the memo's risk section** if both patches are recommended.

---

### MINOR

**m1 — "the member's retirement has taken effect" uses a bare phrase this section never otherwise uses unqualified.** "the member's retirement" occurs 10 times in §1 and is qualified every time: "the member's retirement **on** [a date]," "the member's retirement **allowance**," "the member's retirement **in a qualifying retirement**," and s9's "the member's retirement shall take effect on that date." s12 and clause (iv) introduce the eleventh and twelfth, both bare. In D 1's context it reads as the retirement effected by the § 51.1-153 notice — which is what you intend and is why your "a member who never filed cannot have retired" is right as to her original filing. The residual is a member who has retired under subsection A or C of § 51.1-155.1, or on disability, without a § 51.1-153 notice: "the member's retirement" has, in ordinary words, taken effect. *Fix:* "the retirement stated in that notice has taken effect," or "the member has retired."

**m2 — the deemed "case decision" invites an argument that it is deemed to contain what the law requires.** M 2's existing sentence makes the constructive denial "the final determination of the Board upon the reconsideration and a case decision." R-6's duty arises only "where the Board does not [state the date in its decision]." A Board could argue that a decision deemed to exist is deemed to state what a decision must state, so the condition fails and the notice duty never arises. It is a stretch — there is no document — but it is cheap to foreclose. *Fix:* in 164-7, "and the Board is not deemed to have stated that date in a decision upon the request."

**m3 — in the no-act branch, the deeming does not actually move the final qualifying retirement date, because R-5b overrides it.** R-5a fixes the date by reference to "the month in which the Board last acts," so the deeming reaches it; R-5b fixes it by reference to "the month in which that period expired" and does so "**notwithstanding any other provision of this definition**." Where the period expires 31 March, the deemed act is 1 April: R-5a would give 1 June, R-5b gives 1 May, and R-5b wins. Not a defect — the texts resolve — but worth knowing that 164-7's deeming buys the member nothing on the date itself in the branch it was written for. Its value there is the notice duty, which is S3's subject.

---

## 3. Direct answers to the five questions you put

**Q: Does excepting R-6 from the saving actually make its date fall due, or does it merely remove an obstacle?** It makes it fall due. Without the exception, R-6's "15 days after it acts upon the request" is a period measured from the Board's acting, the deeming would supply the act date, and the saving's first limb forbids the deeming from "determin[ing] the date by which the Board is required to ... give a notice." With the exception that bar is lifted for R-6, the deeming supplies date X, and the deadline is X+15. **The mechanism works.** R-6's opening predicate survives too: R-6 is a provision under which a period is measured from the Board's acting, so the deeming operates "for the purposes of" R-6 as a whole, predicate included, and R-5a makes the deemed action one that determines the date. **The exception is sound; the descriptor that names what is excepted is not (S3).**

**Q: Does it disturb what the saving's second limb was protecting — N4?** No. The deeming deems an **act**, not a performance of the notice duty. Removing R-6 from the second limb lets the deeming determine whether the Board performed in time, and the answer it determines is that the Board did not, because nothing deems a notice given. N4 holds for R-6. (See m2 for the one argument that could be run the other way, and its five-word cure.)

**Q: Was I right to refuse to make 164-7's deeming reach a *giving*?** **Yes, unambiguously.** Deeming a decision given would start the member's M 2 clocks and the s12 window against her without any document — card (b)'s subject and Decision 2's purpose. Do not do it.

**Q: Is there a smaller cure inside MOO-164 for the MOO-141 Edit 2 interaction?** **Yes, and it is the same fix as S3.** Stop excepting a duty and impose one. Add to 164-7, after the exception: a free-standing duty — where a request is denied or not acted upon as described, and the Board has not stated the member's final qualifying retirement date in a decision upon the request, the Board shall give the member written notice of that date no later than 15 days after the date on which it is deemed to act. That duty is keyed to **the deemed act date and nothing else**, so MOO-141 Edit 2's re-keying of R-6 cannot reach it; it does not deem a giving, so Decision 2 is respected; it needs no paraphrase descriptor, so S3 dissolves; and a failure to give it is reviewable under M 2 ("a failure of the Board ... to give a notice ... within a period required by this section," exercisable "at any time before the Board ... gives the notice") and reportable under J 1's lateness limb. It is larger in characters than the exception and smaller in risk. **I recommend it over the exception, and it does not displace your recommendation of a second limb in MOO-141 Edit 2 — it makes MOO-164 no longer depend on it.**

**Q: Is the F2 deletion safe?** **Yes, and the link is exact.** s9's subject is "**A notice filed within the period allowed by this subdivision** satisfies § 51.1-153"; s12's deeming says a notice so filed "**is filed within the period allowed by this subdivision**" — the same words, each resolving once in D 1. The concessive "notwithstanding that it is filed after the effective date of retirement stated in it" removes an objection; it does not restrict the subject, and a concession that is not engaged does not disable the main clause. s9's second limb carries the retroactive-payment consequence through on the same subject ("such a notice"). This was the question you were least sure of; it is the one I am most sure of. If you want belt and braces for the price of three words, the ones F2 removed were exactly the ones that would supply it.

---

## 4. What I checked and found sound — expressly

1. **All three scripts, as published.** `verify_r70_v7.py` 0 failures; `apply164.py` 13 FINDs each resolving exactly 1× in enacted §1, +3,375, `applied.md` 518,594, everything outside §1 byte-identical; `check_doc_vs_kit.py` 0 mismatches. The §1-only slicing and the five multi-resolving FINDs are handled correctly — F21 holds.
2. **F2's deletion.** Sound, with the exact-string link above.
3. **"under this sentence" is determinate.** s12 is one sentence; a semicolon does not end it. The bar reaches both the original-filing limb and the replacement limb, which is right.
4. **The "except that" scope.** It follows limb B, so on proximity it could be read to qualify only the timeliness-and-supersession limb. "No notice may be **filed** under this sentence" rescues it: only limb A confers a filing authority, so the bar can only be reaching limb A. **Your choice of "this sentence" over "this subdivision" is what saves this.**
5. **"the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153" is determinate** — s7's 30 days from the first written statement. "period allowed by this subdivision" resolves 2× in D 1 and both uses are consistent with s7.
6. **"after the member's retirement has taken effect" is a determinate date** on this section's own words in the D 1 case (s9 second limb) and under § 51.1-153 otherwise. The indeterminacy is in *which retirement* (m1), not in *when*.
7. **Clause (iv)'s "a notice" excludes the written statement, and does not need to say so.** s13 names the written statement as "the written statement," the other two as notices; N11's reasoning for s12's "any notice" carries over exactly. **Parallel confirmed.**
8. **The three documents are the same three in both lists.** s11's set after 164-5 and s13's set after 164-13(a) are identical. The only divergence is the lateness qualifier (S1), not the membership.
9. **The series repair is correct.** As applied: "...; (ii) ...; (iii) that where the Board mails the statement or notice ...; and (iv) ...". One conjunction, correctly placed, matching store revision 70's own move on D 1's certification series. **Deleting "and" before (iii) changes nothing in clause (iii)'s meaning** — it is a series conjunction, and (iii) retains its own "that where ..." introduction and its full predicate.
10. **The ordering invariant holds.** Inserting s12 between s11 and s13 strands nothing. s12's "the preceding sentence" is s11. s13's "that definition" still reaches the definition named in s7, because s12 introduces no competing definition — I checked the applied text, not the assertion. Your verifier's claim is not weaker than it looks.
11. **164-12's premise is right.** G 4's pendency definition is confined by its own words to "this subdivision" and never travelled into G 2, so there was nothing to notwithstand. The deletion leaves the sentence's work intact. N10's antecedent chain still resolves — subject to M3's fragility point, which is about durability, not present meaning.
12. **You were right not to lift "no later than 15 days after it acts upon the request."** It resolves twice in the base (M 2's application duty and R-6's notice duty), so it would not have identified R-6 even before MOO-141 Edit 2 re-keyed it. The exception's **first** limb is determinate: "under this subsection" + "act upon an **application**" fixes it uniquely on M 2's sentence.

---

## 5. For the Editor — must appear in the memo's risk section

- **S4** (disclosure duty with no enforcement route as to the written statement; the subsection J reliance does not exist).
- **S2** (a statutory disclosure that advertises a window closed for the class most likely to read it).
- **M4** (two savings with asymmetric exception lists and no cross-reference, if both patches are recommended).

## 6. Handoffs

- **Drafting Specialist** — S1, S2, S3, M1, M2, M3, m1, m2 and the §3 fix list in S5 are all yours. S3's fix and the Q4 answer are the same change; take them together.
- **Statutory Researcher** — one citation failure to record: the phrase attributed to subsection J ("every failure … to state a matter this section requires to be stated") is not in subsection J. Counted 0.
- **Policy Director** — three calls are yours: whether S3's cure takes the form I recommend (impose, not except) or stays as an exception with a conformed descriptor; whether S4's enforcement gap is a MOO-164 item or a new issue; and the policy question under S2 about s11's right in the hands of a member who has already retired.
- **MOO-141** — your recommendation of a second limb in Edit 2 stands and is right. If S3's cure is adopted, MOO-164 no longer depends on it.
