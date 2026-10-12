# -*- coding: utf-8 -*-
"""Commentary blocks for the store revision being cut. Every label is a placeholder."""

COUNT_PATTERNS = {
    "162": r"§ 51\.1-162",
    "163": r"§ 51\.1-163",
    "165": r"§ 51\.1-165(?!\.)",
    "16501": r"§ 51\.1-165\.01",
    "153": r"§ 51\.1-153",
    "1422": r"§ 51\.1-142\.2",
    "207": r"§ 51\.1-207",
    "218": r"§ 51\.1-218",
    "subN": r"subsection N",
    "subJ": r"subsection J",
    "subM": r"subsection M",
    "notice_class": r"other person to whom this section requires a notice to be given",
}

REC = "[`moo161-disposition`](/MOO/issues/MOO-97#document-moo161-disposition)"
M161 = "[MOO-161](/MOO/issues/MOO-161)"
M154 = "[MOO-154](/MOO/issues/MOO-154)"
M97 = "[MOO-97](/MOO/issues/MOO-97)"


def _c(C, k):
    a, b = C[k]
    return "%d → %d" % (a, b)


def s0_block(L, C):
    return """### 0.0-{REV} Store revision {REV} — {M161}'s counsel pass disposed and the Policy Director's five answers enacted. Thirteen substitutions in subdivisions G 4, D 1 and M 2; the fatal finding cured by deleting four words and confining one sentence

**Thirteen substitutions in three provisions of §1 — subdivisions G 4, D 1 and M 2 of § 51.1-142.4. No figure moves, no designator is renumbered, no section is added or deleted, no defined term is added, and the title line does not change.** Five of the thirteen carry the Policy Director's answers of 12 October to §7 item 122; eight answer {M161}. The record proper is a companion document, {REC}, on the convention store revisions 33, 36, 40, 41, 42, 44, 49, 55 and 58 set: every FIND/READ pair verbatim, subdivisions G 4, D 1 and M 2 reproduced in full as amended, both directions of the sweep, the ambiguities, and every answer drafted and not enacted.

**The fatal finding is cured by taking words out, not by adding them.** **F1**: store revision 58 replaced a self-limiting formulation (*"the Board's receipt of a written notification ... shall not cause § 51.1-163 to apply"*) with a freestanding *"§ 51.1-163 shall not apply to the member's death"*, governed only by *"where clause (i) of this subdivision applies."* Clause (i) is *"dies"*, and its only carve-out is a member who retired in a retirement that is **not** a qualifying retirement — so by negative implication the sentence reached **a member who retired in a qualifying retirement on a basic allowance and died years later as a retiree**, and switched off the one provision that returns her unrecovered contributions to her family. On the reviewer's facts a brother lost $122,000 and the trust fund kept it. **The act, whose case for existing is that forfeiting purchased military service is wrong, forfeited more than the defect it was curing.**

**Two edits, and both are subtractions.** The citation check establishes why: **§ 51.1-163 is captioned *"Death after retirement"* and opens *"If a member dies after the effective date of retirement"* — it cannot reach a pre-effective-date death of its own force at all.** It reaches one only by deeming, and there are exactly three deeming provisions (§ 51.1-165 C 1, § 51.1-165 C 2 and § 51.1-165.01 F), two of which this sentence's notwithstanding already displaces and the third of which it deliberately preserves. **So the disapplication was never load-bearing.** It is deleted, and the sentence is confined to the window in the words D 1's own certification already uses — *"after the Board has received the notification of the member's effective date of retirement required by subdivision D 1 and before that date."* That cures **F1** and, because § 51.1-163 is available again as a measure, **F2** — the greater-of that could not be performed because its input had been switched off.

**This restores the agreed scope; it does not choose a policy.** Every answer the Director has given on this branch — (d), (f), and the certification — speaks to the death of a member who has filed her § 51.1-153 notice and not yet reached her effective date. Reaching a death in retirement was a drafting artefact, not an agreed policy, and §7 item {ITEM} offers the wider alternative if the Director wants it.

**Three propositions of law the certification compelled the Board to state were wrong, and the reviewer re-read the Code to prove it.** § 51.1-162 **C** pays a surviving spouse, **minor children and parents** — not a spouse alone (**F4**), so an unmarried member with a child was being told in an official certification that the work-related death allowance could not reach her child. § 51.1-162 **A**'s condition is *"if no benefits are payable under subsection B"* — subsection C is not mentioned (**F5**), so the act compelled the Board to certify the opposite of the statute and supplied a future plaintiff with his own best evidence. And subdivision C 2 of § 51.1-165 was described as entitling the contingent annuitant, when that is true of one of its two limbs only, and its in-service condition was suppressed (**F6**). **All three are now stated as the Code states them, by cross-reference rather than by paraphrase.**

**The incomplete certification had a remedy that could not work, and now has one that can.** Deeming the omission a *determination* (store revision 58's F7 cure) gave the review right to the only person who had received the certification — the member, who is not adversely affected while she is alive — and ran the clock from a document her survivors never saw. It is now a **failure** of the Board, M 2's failure limb is widened to reach a notice or certification that was given on time and left out a matter the section requires, and the period runs for 30 days from the G 4 death notice, which is the first writing the person adversely affected ever receives.

**The reconsideration class is narrowed because it had no boundary.** *"Other person to whom this section requires a notice to be given"* reached, on the face of the text, **the public**, because subsection K requires the Board to *"give public notice"* of a year in which it accepts no election; it also reached the two money-committee Chairmen, who receive information-only notices. The formula is replaced in both class lists by the two recipients the amendment was for — **the claimant the Board rejected** and **the employer that paid on the member's behalf** — both of which were the stated object of store revision 58's own cure, and both of which are now in the act expressly rather than by accident.

**The Policy Director's five answers.** A **30-day duty on the employing state agency** to tell the Board of the death, with a subsection J line — the crediting deadline runs from when the Board *"learns of"* the death and until now nothing required anyone to tell it. The **90-day redetermination** now runs, in the death case, from the date the Board learns of the death, so it can no longer expire before the Board can begin. The release of a settled amount now fires **where no allowance is payable at all**, not only where someone elects, and restores to the $3,000,000 limitation **only so much as has not already been paid under subsection N**. And a released amount is **reinstated** where the determination that released it is reversed on reconsideration or on judicial review.

**What is not here.** **F3** — what the greater-of is measured on and who is paid it — is on the Director's card, because every form of it moves money between a spouse, a sister, a designated beneficiary and the trust fund. **F7**, the § 51.1-162 C waiver period that can expire before the Board's compelled notice of it arrives, is the reviewer's highest-value repair after F1 and needs an override of another section. **F10**, whether a State Police, VaLORS or Judicial Retirement System member is in this Program at all, is a scope question for the Director and a research question for the Statutory Researcher. All of them, drafted, at §7 item {ITEM} — which since store revision 59 lives in [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list), where a reference of the form *“§7 item n”* resolves.

""".format(REV=L["REV"], ITEM=L["ITEM"], REC=REC, M161=M161, M154=M154)


def s5_block(L, C):
    return """### §{S5} Store revision {REV} — the thirteen substitutions, chased in both directions

**Performed by mechanical count over §1 alone**, not over the whole document, because §2, §6 and §7 quote the operative text and would inflate every figure. **Every count is taken on the body that was written, not predicted.** The full table is at {REC} §5. The results that have to be stated here:

- **`§ 51.1-162` {C162}** — the largest movement, and all of it inside the three provisions edited. **`§ 51.1-163` {C163}: unchanged, and the composition changed.** One reference is deleted (the disapplication that caused F1 and F2) and one is added (the C 2 proposition in the certification, which now names § 51.1-163 as C 2's own measure). **The act still names § 51.1-163 twice and no longer purports to switch it off.**
- **`§ 51.1-165` bare {C165} and `§ 51.1-165.01` {C16501}: both unchanged.** No displacement is added or removed by this revision; the notwithstanding limbs enacted in store revision 58 are untouched, and subdivision C 2 of § 51.1-165 remains preserved rather than displaced.
- **`other person to whom this section requires a notice to be given` {CCLASS}.** The open formula is gone from both of subdivision M 2's class lists and is replaced by two named classes. **Checked against subsection K**, which requires a notice to *the public*: no occurrence of the formula remains anywhere in §1, so the unbounded class is closed on the face of the act.
- **`subsection J` {CSUBJ}, `subsection N` {CSUBN}, `subsection M` {CSUBM}** — one new reporting duty (the state agency's death notice), one new reference to subsection N (the cap restoration measured by what has been paid), and two new references to subsection M (the certification's new failure limb and the reinstatement on review). **No amendment to subsection J is needed**, in the form J 1's closing words already accept (*"every other matter this section requires the Board to state in the report"*), and **no amendment to subsection N is needed**: the release sentence refers to it, and does not change it.
- **`§ 51.1-207` and `§ 51.1-218`: {C207} and {C218} — still zero, and that is finding F10.** § 51.1-163 directs payment *"in the same manner as provided in subsection A of § 51.1-162, subsection A of § 51.1-207, or subsection A of § 51.1-218, in accordance with the retirement plan covering such member."* The act's death branch names only the first. Whether that is a defect depends on whether a State Police, VaLORS or Judicial Retirement System member can be an *"eligible member"* at all — **§7 item {ITEM} and a research question for the Statutory Researcher, not a count.**
- **Subdivisions D 2, D 3, D 7 and subsection E: untouched.** This revision releases, reserves and settles nothing new. **The $3,000,000 limitation's words are not amended**; what changed is how much of a settled amount returns to it.

**Conforming amendments elsewhere in the Code: none.** Outward: the sections this revision newly *cites* — § 51.1-162 and § 51.1-163 — have their **operation unaltered by it**; the only operative displacements in the act are those enacted in store revision 58, and each remains confined to a named subdivision or limb. Inward: **no section of the Code cross-references § 51.1-142.4**, because the act adds it; §§ 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 are not amended by this act and say nothing about it, **which is the standing risk this record has carried since §5.19 and which must travel in the drafting request to Division of Legislative Services — a drafter's note is not enacted.**

**Internal integrity, chased sentence by sentence.** Two sentences are added to subdivision G 4 (the state agency's notice duty and the reinstatement on review), so **every one of G 4's eleven *"preceding sentence"* references was re-resolved on the written body, positionally, against the sentence it resolved to before the edit.** All eleven resolve to the same antecedent as before, and the subdivision has no *"preceding clause"* reference; the one new reference, in the reinstatement sentence, resolves to the release sentence immediately before it. **The reviewer's own fix direction for F13 — *"the date determined under the preceding clause"* — was not taken**, because this subdivision uses *"clause"* for its enumerated clauses (i), (ii), (iii) and (a), (b), (c); the enacted words are *"after the earlier of those dates."*

""".format(S5=L["S5"], REV=L["REV"], ITEM=L["ITEM"], REC=REC,
           C162=_c(C, "162"), C163=_c(C, "163"), C165=_c(C, "165"),
           C16501=_c(C, "16501"), CCLASS=_c(C, "notice_class"),
           CSUBJ=_c(C, "subJ"), CSUBN=_c(C, "subN"), CSUBM=_c(C, "subM"),
           C207=_c(C, "207"), C218=_c(C, "218"))


def s6_block(L, C):
    return """### §{S6} Ambiguities resolved in store revision {REV}

Fourteen. **All fourteen in full at** {REC} **§6. No policy was chosen by drafting choice.** The six a later reader must not undo are these.

**1. The fatal finding was answered by deletion and confinement, not by the carve-out the reviewer offered first.** F2 offered two forms: carve the disapplication (*"except that for the purposes of subdivision C 2 ... as though this sentence had not been enacted"*) or delete it. **Deletion is enacted**, because the citation check shows the disapplication was never load-bearing — § 51.1-163 reaches a pre-effective-date death only by the deeming in § 51.1-165 C 1, § 51.1-165 C 2 and § 51.1-165.01 F, and the sentence's notwithstanding already handles the first and third. **A carve-out would have preserved the words that caused F1.**

**2. The window is stated in D 1's words, not in the reviewer's.** The fix direction read *"after the Board has received a written notification of the member's effective date of retirement given under subdivision D 1 and before the effective date of retirement stated in it."* D 1's certification already says *"after the Board has received the notification of the member's effective date of retirement required by this subdivision and before that date,"* and **the act may not use two formulations for one concept.** The enacted words are D 1's, with *"this subdivision"* becoming *"subdivision D 1."*

**3. Confining the sentence is treated as restoring the agreed scope, not as deciding a policy.** A fatal finding may not be resolved by drafting choice. This one is not: the Director's answers (d), (f) and the certification all speak to the member who has filed her § 51.1-153 notice and not yet retired, and the sentence's reach beyond that window was an artefact of how store revision 58 was cut. **The wider alternative — keeping the disapplication and confining it instead to a member who has not retired — is drafted at §7 item {ITEM} and is not enacted.**

**4. The release trigger's second branch needed a date and the card did not state one.** The Director's answer fires the release *"where no retirement allowance is payable ... because no such allowance is payable to any person"* — a case in which there is no election to date it from. The enacted words run it from the Board's determination that no such allowance is payable, on the model of every other period in this subdivision. **Without a date the duty would have had no deadline, which is an unenforceable duty.**

**5. F6's certification wording states C 2's payee by cross-reference and names nobody.** The reviewer's fix direction ended *"to the person entitled to it under the provision under which the greater benefit is determined"* — a payee rule. **That rule is F3's question and F3 is on the card**, so the enacted proposition says only that each of C 2's two benefits is *"payable to the person entitled to it under the provision under which it is determined"*, which is a statement of existing law and not a direction to pay anybody. **The certification is now accurate about a question the operative text has not yet answered, and §7 item {ITEM} is where that is answered.**

**6. F14 is enacted as to the rider only.** The notice rider now reaches *"the amount of any benefit payable to that person"* as well as entitlement, so the Board is no longer compelled to state a figure it does not have. **The reviewer's companion cure — a supplemental notice with a fresh review period where the Board later determines an amount differently — is a new duty that was not agreed, and is drafted at §7 item {ITEM} instead of enacted.**

**Two findings declined, with reasons.** **F16** (the deemed determination as a tolling lever) is declined on the reviewer's own analysis: M 2 caps the aggregate of all tolling at 120 days and denies tolling to a second request on the same determination, the cap holds, and the cost of closing the residue exceeds the exposure. **F21** (the new class reaches notices required by *"this section"* while M 2's tolling sentence reaches periods under § 51.1-142.2 as well) is declined because the cure would **widen** a class this revision narrows for F8, in the same breath and for the sake of symmetry alone. **Both are recorded so that neither is re-run as new.**

""".format(S6=L["S6"], REV=L["REV"], ITEM=L["ITEM"], REC=REC)


def s7_block(L, C):
    return """{ITEM}. **NEW IN STORE REVISION {REV}, from {M161} — seven answers drafted in full and enacted nowhere.** Each is drafted word for word at {REC} §7 so it can be enacted with one substitution. **Three of them move money between named people and I have not picked one.** Items 60, 106, 107 and the five unenacted answers at item 122 are unaffected and stay open.
    - **(1) F3 — what the greater-of is measured on, and who is paid it. The sharpest thing in the pass after F1.** Subdivision G 4 directs the Board to pay *"the benefit it provides or the benefit determined under the preceding sentence, whichever is greater."* The two sides are **different kinds of money payable to different people**: C 2's first limb is a lump sum payable, through § 51.1-162 A's manner, to the designated beneficiary or a surviving relative by order of precedence; the act's side is a monthly allowance payable to § 51.1-162 B's first qualifying person. On the reviewer's facts a member names her **mother** as contingent annuitant, is survived by a **husband**, and has her **sister** as designated beneficiary: three payees, one direction to pay *"whichever is greater,"* and no basis of comparison. Three answers, any combination: **(a)** state the measure — *"the two being compared on the basis of actuarial equivalence as of the date of the member's death determined on the assumptions then in use by the Board"*; **(b)** state the payee — *"and the Board shall pay it to the person to whom the provision under which the greater benefit is determined requires it to be paid"*; **(c)** confine the greater-of to the case where the payees coincide, which is C 2's own *"however"* limb, and let C 2's first limb be displaced. **(c) is the smallest and it takes a right from the designated beneficiary; (b) names a payee, which is why it is yours.**
    - **(2) F7 — the compelled notice of a right that may already have expired. The reviewer's highest-value repair after F1.** § 51.1-162 C's waiver must be made *"within ninety days after the death of the member."* G 4's notice is due at the outer limit 90 days after the Board **learns** of the death (60 to credit, 30 to notify). **Every day the Board takes to learn of the death is a day by which the Commonwealth's own notice of the right can post-date the expiry of it**, and the person who loses by it has no remedy, because the Board gave the notice inside the period the act allows. Drafted: *"Where the Board gives the notice required by this subdivision later than 30 days after the death of the member, the period stated in subsection C of § 51.1-162 within which a waiver must be made does not expire before the thirtieth day after the notice is given to the person entitled to make it."* **It overrides a period in another section, which is why it is yours and not mine.** The state agency's new 30-day death notice, enacted in this revision, shortens the exposure but does not close it.
    - **(3) F10 — whether a State Police, VaLORS or Judicial Retirement System member is in this Program at all.** § 51.1-142.2's purchase right runs to *"any member in service"*; subsection L excludes teachers and employees of political subdivisions and **does not exclude the sister systems**; § 51.1-200 applies Chapter 1 to the State Police Officers' Retirement System *"except as otherwise provided."* The act's death branch names **§ 51.1-162 alone**, while § 51.1-163 names §§ 51.1-162, 51.1-207 and 51.1-218 *"in accordance with the retirement plan covering such member."* Two answers: **(a)** generalise, in subdivision G 4 and in D 1's certification, to *"§ 51.1-162, § 51.1-207, or § 51.1-218, as applicable to the retirement plan covering the member"*; or **(b)** confine the Program to Chapter 1 members by one sentence in subsection L, which is cheaper and is a scope decision. **Routed to the Statutory Researcher for the list of sister-system death-benefit sections before either is enacted.**
    - **(4) F11 — say expressly that the death benefit is outside the cap, or leave it to inference.** Every cost control in the act is addressed to the *certified subsidy*: D 2's $3,000,000 and $170,000 limits, subsection K's kill-switch, subsection N's appropriation. **A benefit determined under G 4 is none of those things; it falls on the trust fund.** Drafted for subsection N: *"Nothing in this section charges a benefit payable under § 51.1-162 against the limitations in subdivision D 2."* **It changes nothing and discloses everything**, which is the argument for and against it. F1's cure removes the large exposure; what remains is the C 2 greater-of, which the reviewer priced at about one case every three years.
    - **(5) F14's companion — a supplemental notice where the Board later determines an amount differently.** Entitlement can be clear while the amount is not: a work-related death's § 51.1-162 C allowance waits on a Workers' Compensation award. This revision defers the notice until the amount is determined; the drafted sentence adds a **further** notice, with a fresh review period, where the Board afterwards determines the amount differently. **It is a new duty on the Board and was not agreed.**
    - **(6) M 2 — make lateness reviewable after it is cured.** The failure limb closes *"at any time before the Board makes the determination or gives the notice,"* so a member whose crediting was 30 days late has no remedy for the lateness the moment it is cured. Drafted: *"or, where the Board has made the determination or given the notice late, within 30 days after it does so."* **Small, and it is a new right.**
    - **(7) F8's alternative — keep the general notice class, gated.** This revision replaced *"other person to whom this section requires a notice to be given"* with two named classes, because the formula reached the public through subsection K. If the Director wants the general formula back, the gated form is *"or other person to whom this section requires a notice of a determination affecting that person to be given."* **Not enacted; the narrow form is in the text.**

""".format(ITEM=L["ITEM"], REV=L["REV"], REC=REC, M161=M161)


def s8_block(L, C):
    return """> **STORE REVISION {REV} — {M161}'s COUNSEL PASS DISPOSED AND THE POLICY DIRECTOR'S FIVE ANSWERS ENACTED.
> Thirteen substitutions in subdivisions G 4, D 1 and M 2 of § 51.1-142.4. No figure moves, no designator is
> renumbered, no section is added or deleted, no defined term is added, and the title line does not change.**
> Record: {REC}. Narrative §0.0-{REV}; sweep §{S5}; drafter's note §{S6}; the seven drafted answers §7 item
> {ITEM}. Cut and applied on {M97}.
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
> **Not here, and on the Director's card at §7 item {ITEM}:** **F3** (the greater-of's measure and payee —
> three payees and no basis of comparison), **F7** (the § 51.1-162 C waiver that can expire before the
> Commonwealth's notice of it arrives), **F10** (whether a State Police, VaLORS or JRS member is in this
> Program at all — also with the Statutory Researcher), **F11**, **F14's** supplemental notice, M 2's
> lateness-after-cure, and F8's gated alternative. **F16 and F21 are declined with reasons at §{S6}.**
>
> **For the memo's risk section:** F1 and F11 together (the legal and fiscal sides of one clause), F7 and
> F8. **For the Fiscal & Impact Modeler:** the reviewer's structural challenge — not a number in the model
> but the assumption underneath it, that every cost of the act flows through the certified subsidy. F1's cure
> restores that assumption; the residue is the C 2 greater-of, at about one case every three years.

""".format(REV=L["REV"], S5=L["S5"], S6=L["S6"], ITEM=L["ITEM"], REC=REC, M161=M161, M97=M97)


STUB_S8 = """{PHRASE} moved verbatim** to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2) **by store revision {REV}**, where a reference of the form *"§8's note for store revision N"* still resolves. §8 retains the five most recent: {KEPT}. **Nothing is rewritten or summarised away, and §1 is untouched by the move.**

"""


def s7stub_block(L, C):
    return """**Store revision {REV} writes into that document too.** {M161}'s counsel pass on store revision 58's eight substitutions returned **1 fatal, 9 serious, 6 moderate and 4 minor findings, and 12 null results**. Eight of its findings are enacted in §1 by this revision, two are declined with reasons at §{S6}, and **seven are drafted in full and enacted nowhere** — they are **§7 item {ITEM}**, written in that document. The same revision enacts **five of the nine answers at §7 item 122**, which the Policy Director selected on 12 October 2026; item 122 is marked there with what was enacted and what stays open. This document carries the narrative at §0.0-{REV}, the sweep at §{S5} and the drafter's note at §{S6}.

""".format(REV=L["REV"], S5=L["S5"], S6=L["S6"], ITEM=L["ITEM"], M161=M161)


# Substitutions outside §1: the live record has to say what happened to the
# card it posted, or §7 presents five enacted answers as open questions.
DOC_EDITS_SPEC = [
    ("item 122 — the Director's answers of 12 October",
     "122. **NEW IN STORE REVISION 58, from [MOO-154](/MOO/issues/MOO-154) — nine answers drafted in full and enacted nowhere. Four of them decide who bears a loss and I have not picked one.**",
     "122. **ANSWERED IN PART by the Policy Director on 12 October 2026 and ENACTED IN STORE REVISION {REV}: (2)(i), (3), (4), (6) and (7) — the cap restoration measured by what has been paid under subsection N, the reinstatement on review, the release trigger where no allowance is payable, the state agency's 30-day death notice, and the redetermination clock run from the date the Board learns of the death. STILL OPEN AND NOT RE-ASKED: (1) F5's two forms, (2)(ii), (5) F12's period, (8) F15's payee and (9) the § 51.1-165 C 2 displacement.** Originally from [MOO-154](/MOO/issues/MOO-154): nine answers drafted in full, four of which decide who bears a loss.")
]
