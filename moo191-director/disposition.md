# MOO-191 — the Policy Director's disposition of MOO-195

**All eight decisions answered. One composite edit authorised. The commission is extended to the title line.**

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by DLS, not legally sufficient for introduction. Pre-decisional and internal.**

**Base: store revision 68, document revision `db67d2bb`, number 87.** Document 449,196 characters; §1 **131,066** characters; §1 `<u>`/`</u>` **62 / 62**; the subdivision D 1 certification series at **7 items** with the advisory at item **5 of 7**. I re-counted every anchor myself on that live base before writing this, by the script at `moo191-director/director_composite.py`. The base had not moved since the disposition was built.

---

## 1. The decisions, in one table

| # | Finding | My decision | Form | §1 movement |
|---|---|---|---|---|
| **1** | F1 — give the advice an object | **Take** | D1's words | +72 |
| **2** | F2 — the terminus | **Take** | **D2b**, the referent named | +130 |
| **3** | F3 — the channel (my reserved question) | **Take** | **D3c, conformed** — see §3 | +229 |
| **4** | F4 — placement | **Take** | D4 | +0 |
| **5** | F5 — a route | **Hold.** Do not draft the acknowledgment form | — | — |
| **6** | F6 — the no-fault clause | **Take** — I depart from the drafter's conditional; reason at §6 | D6's words | +156 |
| **7** | F9 — name the actor | **Take** | D9's words | +7 |
| **8** | F8 — the title | **Take T2.** I extend the commission to the title line | T2 | +44 (document) |

**F7** stays carded at §7 item 133, re-scoped — §8 below. **F10 and F11** were applied at store revision 68 and are closed.

**Net: §1 131,066 → 131,656 (+590); the document 449,196 → 449,830 (+634).**

The movement column above sums to **+594**, not +590, and the disposition's own combined figures give **+576**. Both gaps are real and both are accounted for:

- **−4**, because the four findings that share one item travel as one item rather than four, which saves that much connective. This is the disposition's DALL figure of +361 and I reproduce it exactly.
- **+14**, because conforming D3c's two descriptive phrases to F9's wording costs seven characters twice. **The disposition did not carry this**, having priced D3c and D9 as independent cuts. They are not independent, and that is the next section.

---

## 2. One thing the disposition got wrong, and it would have broken the cut

**D3c and D9 cannot be applied as independent substitutions, and if D3c goes first the cut fails silently.** I verified this rather than reasoned it; the demonstration is the first block `director_composite.py` prints.

1. **The anchor dies.** D9's FIND — `that the member is advised to review the member's designation` — resolves **1× in the live §1**. D3c writes that same phrase into the subdivision **twice more**, once in the subsection M exception and once in the subsection J limb. After D3c it resolves **3×**. The disposition states D9's anchor as 1× in §1, which was true of the base it was counted on and false of the base D3c leaves.
2. **Worse than a dead anchor: a silent mismatch.** If the two were applied in the other order, or D9 scoped to the item alone, D3c's exception would describe *"a failure to state that the member is advised to review…"* while the subdivision would require the Board to state *"that the Board advises the member to review…"*. A strict reader gets an exception that excepts nothing and, in the second substitution, a report limb that reports nothing. **F3 would be enacted and do no work, in both directions.** Nothing in the document flags this, because the document prices every candidate against the live base and never against another candidate's output.

The disposition is right that D1, D2b, D6 and D9 share one FIND and must travel together. The rule is wider than it states: **D3c travels with them too.** Hence one composite, in the order at §7, with D3c's phrases conformed.

This is a counting discipline the drafter otherwise applies well, and the fix is small. I record it because the next pass should price candidates against each other's output, not only against the base.

---

## 3. Decision 3 — F3, the channel. Taken, in form D3c conformed.

**I reverse my acceptance at MOO-188 §3.4.** Omission of the advisory is excepted from the subsection M review limb and kept in the subsection J report limb.

**What changed, and why that is a reason and not a second thought.** At §3.4 I accepted the channel knowing the advisory would be reviewable. What I did not have was the remedy analysis. Counsel supplied it: § 2.2-4029 bars the court from supplying the designation, so subsection M review's only possible output is a remand that cannot give a claimant anything. I accepted a cost without knowing the benefit was nil. A decision taken on an incomplete account of the remedy is a decision worth retaking, and a decision I decline to defend merely because I made it.

**Two further reasons of my own, which counsel did not reach.**

1. **The review window and the harm never overlap.** Review runs 30 days from the certification. The harm from an un-given advisory materialises at the member's death, when the designation turns out to be wrong — years or decades later, to a survivor who was never served the certification. The limb is closed long before anyone can know they were hurt by the omission.
2. **The limb protects only the members who do not need it.** A member who notices the advisory is missing from her certification is, by that fact, a member who already knows designations matter. The member the advisory exists for is the one who would not notice. So the M limb is available precisely to those with no use for it, and unavailable to those with a use.

**The honest counter, which I accept as the price.** An advisory excepted from M review is enforceable by no individual. I take that trade because the J report is the apt channel for this act: it is a **pilot programme with reports in its title**, omission of advice is a systemic administrative failure rather than an individual wrong, and aggregate reporting to the money committees is how a pilot is supervised. Not reviewable is not unenforced.

**On form, D3c, and the drafter is right about why.** D3a asserts *"is not a failure for the purposes of subsection M"* in the sentence after the one deeming it a failure, and turns on an undefined *"advice"*. D3b cures both and buys a reference by position — *"the advice described in the next sentence"* — which breaks the day anyone inserts a sentence between them. D3c carves the exception into the deeming clause and names the matter in the subdivision's own words. **Conformed to F9's wording**, per §2.

**A residue I am leaving open rather than burying.** After the composite, item 7 states three propositions: the advice, the member's power to redesignate, and the no-fault clause. D3c's exception names only the first. So a Board that gave the advice but omitted the other two would still face M review on them. I am not drafting that away, for two reasons: the power to redesignate is a proposition of law in the same register as the other six items and belongs in the M limb; and a certification that omits the advice clause will in practice omit all three, so the residue is theoretical. **Counsel's next pass should test it.** I would rather carry a named residue than a three-way split inside one item.

---

## 4. Decision 1 — F1. Taken.

The only finding where the enacted words can cause the loss they exist to prevent. § 51.1-162 B rewards doing nothing and punishes doing the wrong thing: a member with no designation is paid through the order of precedence, a member who designated a non-qualifying person is paid by neither branch. *"Review your designation"* with no object invites the second. Store revision 67 put both branches of B into item 4, so D1 only has to point her at it. Seventy-two characters to stop the advisory from being the but-for cause of the harm is not a close call.

## 5. Decision 2 — F2. Taken, in form D2b.

*"Before completing payment"* carries a false implicature — that completing payment does something to the designation. Nothing in § 51.1-162 A fixes a designation at that moment; it is revocable until death. Store revision 62 was cut to stop the certification misleading the member, and leaving a false implicature in enacted text is the same defect in a smaller font.

**I keep both clauses deliberately.** *"Before completing payment"* is the prompt to act now, and the certification is handed over at exactly the moment the member is thinking about the purchase; the new clause removes the implicature that the window shuts then. Read together they say: do it now, and know you can change it later. That is the message I want.

**D2b over D2a** for the reason the drafter gives and I verified: once F1's object precedes it, D2a's *"that subsection"* takes subsection B as nearest antecedent and the power is in A. D2b names the subsection. That is a repair, not a policy change, and I am not interested in enacting counsel's words when counsel's words are wrong. D2c does not arise, F1 being taken.

## 6. Decisions 4, 5, 6 and 7

**Decision 4 — F4, placement. Taken. It reverses my recorded decision and both of my reasons survive it.** My reasons at MOO-188 §3.3 and §6.0-65 item 2 were that the advice must be its own semicolon item and visibly advice. At item 7 of 7 it is still its own item, still introduced by *"that"*, still the only item in a different register. What it gains: it stops splitting item 4's forward reference to *"subsection C of that section"* from item 6, which resolves it, and it sits beside the subsection A item it is actually about. **Zero characters, verified not assumed.**

On the case against — that the least legally substantive item takes the most emphatic position — I think that is a feature. The closing position is where a reader looks for what to do next, and F5's worry is that a member reads past the advisory. **F4 is part of my answer to F5, at no cost.**

**Decision 5 — F5, a route. Held, and the acknowledgment form is not to be drafted.** F5's substance is real: advice with no route invites nominal compliance. But D5 compels an administrative particular — the Board's prescribed manner — into a statute, where it will go stale, when § 51.1-162 A already locates it in Board procedure. And it adds a matter inside D 1, so the failure sentence reaches it; taking D5 would enlarge, with administrative detail, exactly the channel decision 3 narrows.

**Do not draft the acknowledgment form.** It moves the advisory toward a member obligation. MOO-188 §3.3 avoided that deliberately and I am not reversing it: the advisory's whole value is that it costs the member nothing and demands nothing of her. The drafter was right to name it as available and to refuse to choose it.

**Where the route question goes instead:** the J report. If the pilot's reports show the advisory being buried, that is the evidence on which to require a route, and it will be evidence rather than a guess. Noted for the Editor's risk section.

**Decision 6 — F6, the no-fault clause. Taken. I depart from the drafter's conditional, and here is why.** The drafter recommends declining D6 if D3c is taken, on the ground that *"the forum in which the argument bites is largely gone"* with the M limb. **That does not follow.** The forum counsel describes is the **Board's own reconsideration of a survivor's benefit claim** — *"The certification advised the member to review her designation. She did not."* Subsection M review concerns the Board's failure to state a matter. The two are different proceedings, and D3c touches only the second. The fault argument survives decision 3 intact, in the one forum where the Board is both the advisor and the adjudicator.

There is also a symmetry I am not willing to give up. Decision 3 narrows the Board's exposure for failing to give the advice. It would be indefensible to narrow the Board's exposure and leave the advisory usable **against** the member. D6 closes that for 156 characters. On the objection that a no-fault clause invites the question why the other six items lack one: the distinction is principled and the clause states it — this is the only item addressed to the member's own conduct, and the other six are propositions about what the Code provides.

**Decision 7 — F9, name the actor. Taken.** Seven characters. My recorded reason at §6.0-65 item 1 — that the carrier sentence already names the Board — is a good pragmatic answer and a bad drafting answer: the item read alone is self-verifying, true because the Board states it, and it is the only such item in a list of seven. *"The Board advises the member"* names the actor and keeps every no-duty property, *"advises"* being the Board's verb and imposing nothing. Name the actor in every duty is my own rule and it applies to words I approved.

## 7. The one composite I authorise

**Five ordered substitutions in §1 and one in the title line, as a single revision.** Every FIND re-counted on the live base at the moment it is applied; the sequence is forced by §2. The relocated item:

> **…to a surviving relative in the order of precedence that section states; and that the Board advises the member to review the member's designation of beneficiary under subsection A of § 51.1-162, and the effect of that designation under subsection B of that section, before completing payment, that the member may make or change that designation under subsection A of that section at any time before the member's death, and that nothing in this subdivision requires the member to review the designation or affects any benefit by reason of the member's not having reviewed it.**

The failure sentence:

> **A failure to state in the Board's certification every matter this subdivision requires to be stated in it, other than a failure to state that the Board advises the member to review the member's designation of beneficiary, is a failure of the Board to state in a certification a matter this section requires to be stated in it for the purposes of subsection M; … and the Board shall state every such failure, and every failure to state that the Board advises the member to review the member's designation of beneficiary, in the report required by subsection J.**

| # | What | FIND | Movement |
|---|---|---|---|
| 1 | F4 — lift the advisory out of item 5 | 208 chars, 1× | −137 |
| 2 | F9+F1+F2+F6 — set it down as item 7 | 47 chars, 1× | +502 |
| 3 | F4 — move the series' *"and"* to the new last item | 38 chars, 1× | −4 |
| 4 | F3 — except the advice from the subsection M limb | 131 chars, 1× | +116 |
| 5 | F3 — keep it in the subsection J report | 84 chars, 1× | +113 |
| 6 | T2 — the title line | 51 chars, 1× in the document | +44 |

Steps 1 to 5 sum to **+590** in §1; step 6 adds **+44** to the document outside §1.

**Post-conditions I require asserted before the write and re-checked after it:** §1 **131,066 → 131,656**; the document **449,196 → 449,830**; §1 `<u>`/`</u>` **62 / 62 unchanged**; the certification series **7 items, advisory at item 7 of 7**; six semicolons in the series, unchanged; **zero occurrences of *"the member is advised to"* left in §1**; the conformed phrase appearing **exactly three times** in §1 — the item, the M exception, the J limb. No figure moves, no designator is renumbered, no section joins or leaves the act, no defined term is added, and the subdivision is no sentence longer or shorter.

**Scope held.** **E1 is not re-cut.** The MOO-141 patch is not applied and MOO-176 revision 6's strings are not touched. **MOO-97 §7 item 129's other answers stay open.** D5 is not applied. F7 is not cut.

**Re-resolve everything on the base as it stands at the moment of application.** The base moved three times under the last cut and MOO-197, MOO-199 and MOO-200 are live. An anchor counted in this document is not an anchor.

## 8. F7 and F8

**F7 — the misstatement limb. Stays carded at §7 item 133, and re-scope it.** Decision 3 is now taken, so the limb should reach **the six propositions of law and not the advisory**: a matter excepted from subsection M review needs no misstatement limb, and drafting one for it would re-open the channel I just closed. Amend item 133's drafted words to that scope and leave it uncut. It is a property of the failure sentence approved at store revision 62, not of this advisory, and it belongs in a commission of its own.

**F8 — the title. T2, and I extend the commission.** The drafter is right that the cure is now cheaper than the disclosure. Store revision 67 opened the title and the act amends § 51.1-162 on its face, while the *"relating to"* clause names no death benefit, no beneficiary and no designation — fair notice of six of the seven items D 1 compels. **T2 over T1** because the object the act now embraces is not only the payment of a death benefit but the member's designation of one, which is what all seven statements and the advisory are about. The title line is outside the commission as the drafter received it; **I am the commissioner and I am extending it.** T2 goes in this revision, substitution 6.

The Editor still needs the risk section. A title cured in an internal draft is not a cured title until DLS says so, and *Dean v. Paolicelli*, 194 Va. 219 (1952), is the authority a reader of the memo will want.

## 9. What I am not deciding

1. **Whether the advisory should exist.** Settled at MOO-188 §3.3 and not reopened.
2. **F3's residue** — whether the M exception should reach item 7's other two propositions. Named at §3, left to counsel's next pass.
3. **Whether to require a route.** Held at decision 5, to be decided on the pilot's own reports.
4. **Anything about E1.** Under a counsel gate and untouched.

## 10. Reproducing this

`moo191-director/director_composite.py` fetches the live base, demonstrates the D3c/D9 hazard, applies the six substitutions in order with every anchor re-counted, and asserts every post-condition at §7. **It writes nothing to the store.**

```
python3 director_composite.py
```

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by DLS, not legally sufficient for introduction. Pre-decisional and internal.**
