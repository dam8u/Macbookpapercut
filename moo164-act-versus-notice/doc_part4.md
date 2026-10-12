
---

## 5. Title line, enacting clause and enactment clauses

**Unchanged by this patch**, and reproduced so this document is readable without `bill-text-s8`:

> A BILL to amend and reenact § 51.1-142.2 of the Code of Virginia and to amend the Code of Virginia by
> adding a section numbered 51.1-142.4, relating to the Virginia Retirement System; purchase of prior
> active duty military service credit by state employees; cost; pilot program; post-retirement
> employment; reports.
>
> Be it enacted by the General Assembly of Virginia:
>
> 1. That § 51.1-142.2 of the Code of Virginia is amended and reenacted and that the Code of Virginia
>    is amended by adding a section numbered 51.1-142.4 as follows:

**This patch adds no enactment clause, no effective date, no sunset and no severability clause.** All six
edits are repairs inside a section whose effective-date mechanics already carry them — the second
enactment's 1 July 2029 date and the third enactment's 1 July 2033 expiration with its clause (i) to (iv)
savings — and none is severable from the provision it amends. **The §6.7 question is recorded as settled on
[MOO-162](/MOO/issues/MOO-162) and I am not re-raising it**; if a reviewer puts it in writing that the
third enactment's clause (i) savings are insufficient, it comes back as a card.

---

## 6. The provisions, in full, as amended

**Markup convention, the same one the MOO-141 patch's own cuts use.** The whole of subsection A, subdivision D 1,
subdivision G 2, subdivision G 4 and subsection M is **new language in the bill** — each is already
wrapped in `<u>…</u>` in `bill-text-s8` — so **every word reproduced below is underlined new text in the
bill as it stands**, and nesting a second `<u>` inside it would be ambiguous markup rather than clearer
markup. Inside that wrapper:

- words **this patch adds** are **bolded**;
- words this patch removes are ~~struck through~~;
- words the **MOO-141 patch** adds are ***bold italic*** — at its current cut, [MOO-176](/MOO/issues/MOO-176)'s **revision 6**, with Edit 3 at **120 days** — and
  the words it removes are ~~struck~~ with its text shown next to them — so that a reader can see both
  patches at once at the two provisions where they overlap.

**Every reproduction below was spliced programmatically from the live `bill-text-s8` at store revision 61
today. None is carried forward from any earlier revision.** The apostrophes in the G 4 extract at §6.5 are
shown **normalised** per §8.

### 6.1 Subsection A, final interpretation paragraph — **not amended by this patch**, and this is the provision Decision 1 declines to amend

Reproduced in full because Decision 1 is a decision about it. The bolded italic text is the MOO-141
patch's Edit 1; option (f-2) at §1.1 would have added a fourth sentence here and does not.

@@A@@

### 6.2 The definition of *"final qualifying retirement date"* in subsection A — in full, as amended by **Edit 164-4** and by the MOO-141 patch's **Edit 2**

@@DEF@@

### 6.3 Subdivision D 1 — in full, as amended by **Edit 164-5**

@@D1@@

### 6.4 Subdivision G 2 — in full, as amended by **Edit 164-2**

Candidate (c-2) at §4.2, if the Policy Director selects it, appends one sentence to the fifth-from-last
sentence of this subdivision. It is **not** shown below, because it is not in the patch.

@@G2@@

### 6.5 Subdivision G 4 — the suspension and pendency passage, in full, as amended by **Edit 164-6**

**Convention for this provision, stated because it is the one place I am not reproducing a whole
provision.** Subdivision G 4 is **29,648 characters** and this patch amends three words in one sentence of
it. Revision 5 reproduced the same passage on the same ground. The extract below is the three consecutive
sentences that carry the suspension, the aggregate, and the pendency definition — which is every sentence
this patch touches, every sentence candidate (c-1) would touch, and the context needed to read either.
**Both of G 4's express *"first"*s appear in it and both are intact.**

> <u>@@G4@@</u>

### 6.6 Subsection M — subdivisions 1, 2 and 3 in full, as amended by **Edits 164-1 and 164-3** and by the MOO-141 patch's **Edit 3**

The confirming sentence at §1.3, which I recommend against, would go after M 2's third sentence. Item
124's sentence, if enacted, goes in the same place. **Neither is shown below.** Edit 3 is shown at
**revision 6's 120 days**.

@@M1@@

@@M2@@

@@M3@@

---

## 7. Cross-reference check — performed on store revision 61, with results

**Performed twice: on store revision 61, and on store revision 61 with the three MOO-162 edits applied.
Identical results on both.**

### 7.1 Every `act / acts / acting / action upon` in enacted §1 — **19 occurrences**, classified

The count matches MOO-141 §4.1's 19. The classification is what Decision 1 rests on.

| # | Provision | What it is | Act-keyed endpoint? | Touched by this patch |
|---|---|---|---|---|
| 1 | definition, later-date request | **duty**, 30 days | no | no |
| 2 | definition, tolling reset | **date fixed by a month** | yes — moves against the member | **no — neutralised downstream**, §1.1 |
| 3 | definition, R-5 trigger | condition | — | no |
| 4 | definition, R-5 period | **period** | — | **Edit 164-4** |
| 5 | definition, condition precedent | condition | — | no (Edit 2 preserves it) |
| 6 | definition, the backstop notice | **duty**, 15 days | — | no (the MOO-141 patch's Edit 2) |
| 7 | subdivision D 1, the descriptor | descriptor | — | **Edit 164-5** |
| 8 | subdivision D 3, DPB Director | **duty**, 30 days, **and not the Board's** | no | no |
| 9 | subdivision D 3, the application | **duty**, 15 days | no | no |
| 10 | subdivision G 4, the aggregate | **failure** | no | **Edit 164-6** |
| 11 | subdivision G 4, the period | **period** | — | **Edit 164-6** |
| 12 | subdivision G 4, pendency of an application | **period** | yes — moves **in** the member's favour | no |
| 13 | subdivision G 4, pendency of a request | **period** | yes — moves **in** the member's favour | no |
| 14 | subsection M 2, the 90 days | **duty** | no | no — card (i), §1.3 |
| 15 | subsection M 2, the tolling endpoint | **period** | yes — moved against the member | **Edit 164-1** |
| 16 | subsection M 2, clause (ii) | **exclusion** | — | **Edit 164-3** |
| 17 | subsection M 2, the D 4 / D 5 retention | **period** | **yes — the one residual.** Queue position only | no (the MOO-141 patch's Edit 3, now 120 days) |
| 18 | subsection M 2, the application duty | **duty**, 15 days | no | no |
| 19 | subsection M 2, that duty's trigger | **trigger** | yes — moves **in** the applicant's favour | no |

**Five endpoints, of which one moved against the member and is now repaired, three move in her or the
applicant's favour, and one — #17 — is the residual priced at $0.** #2 is the fifth and is neutralised,
twice over: by the decision-keyed floor where there is a decision, and by R-5 as cured by Edit 164-4 where
there is not (§2.4).

### 7.2 Counts, every one re-run today on the live base and on an applied copy

**These are whole-document counts**, as the MOO-141 patch's own cuts use, not counts in a slice. One phrase differs between the two framings and is flagged in the table.

| Phrase | Store rev 61 | After both patches | Expected |
|---|---|---|---|
| `acts upon` | 8 | 7 | **7** — Edit 164-1 removes one |
| `act upon` | 8 | 11 | **11** — Edit 1 adds three |
| `last acts upon` | 1 | 1 | **1** |
| `first acts upon` | 2 | 3 | **3** — Edit 1 adds one |
| `acting upon` | 3 | 4 | **4** whole-document — **2 → 3 in enacted §1**; the third occurrence is in §6's commentary, not in the bill |
| `action upon` | 2 | 2 | **2** — Edit 164-5 moves one word before it, not the phrase |
| `30 days after the Board acts upon the request` | 1 | **1** at revision 6; **2** at revision 5 | Edit 164-1's clause (a), plus Edit 3's retention only while it read 30 days. **The identity pass 18 relied on is gone by the board's 120-day answer, not by this cut** — §1.1 |
| `48 days after the Board acts upon the request` | 0 | 1 | **1** |
| `120 days after the Board acts upon the request` | 0 | 1 | **1** — the MOO-141 patch's Edit 3 at revision 6; untouched by this cut |
| `the period allowed by this section for acting upon` | 0 | **3** | **3** — one concept, one formula, three sites |
| `the period allowed to it for acting upon` | 1 | **0** | **0** |
| `the 90 days allowed by this subsection` | 1 | **0** | **0** — item 124 would restore it once, correctly |
| `this definition allows for acting upon it` | 1 | **0** | **0** |
| `upon the Board's action upon a request` | 1 | **0** | **0** |
| `by reason of the Board's action upon a request` | 0 | 1 | **1** |
| `written notice of its decision upon the request` | 0 | 1 | **1** |
| `is pending` / `was pending` | 8 / 1 | 8 / 1 | **unchanged** — card (c) is not in the patch |
| typographic apostrophe `’` | **4** | **0** | **0** — §8 |

### 7.3 Conforming amendments — **one required, and it is in the patch**

**Edit 164-6.** It is the only one. The reasons, provision by provision:

- **Subdivision D 1 → the definition.** D 1 imports *"the time required by that definition"* and the
  descriptor that identifies which notice. Edit 164-5 repairs the descriptor; nothing else in D 1 refers to
  the words any of these edits changes. **No further amendment.**
- **The definition → subsection M.** The definition refers to tolling *"under subsection M"* generically
  and never to M 2's clause (ii) or to its tolling endpoint by its words. **No amendment.**
- **Subsection M 2 → subdivisions D 4 and D 5.** The retention sentence is untouched by this patch.
  **No amendment.**
- **Subdivision G 2 → subsection M.** G 2's floor refers to *"the period allowed to the member by
  subsection M"* — the **member's** period, not the Board's, and a different concept from the one Edit
  164-6 conforms. Edit 164-2 does not change that phrase. **No amendment.**
- **Subdivision G 4 → subdivision G 2.** G 4 suspends *"[n]o period stated in subdivision 2 or in this
  subdivision."* Edit 164-2 adds no new period to G 2; it lifts an existing limit in a new case. **No
  amendment.**
- **Subdivision J 1 and subsection C's reporting sentences.** Both report failures *"to make a
  determination, to give a notice, or to make a payment within a period required by this section."* None of
  the six edits creates or removes a duty, so neither report line moves. **No amendment.** (The J 1 gap
  item 127 identifies is pre-existing and is not mine.)
- **Subdivision B 4 f of § 51.1-142.2.** Reached by Edits 164-1 and 164-3 only through M 2's existing
  *"under this section or under subdivision B 4 f of § 51.1-142.2"*, which both edits preserve verbatim.
  **No amendment.**
- **§ 51.1-153, § 51.1-162, § 51.1-165, § 2.2-4001, § 2.2-4021, § 2.2-4025 et seq.** None refers to any
  word changed. **No amendment.**

**Ten referring provisions chased in both directions. One conforming amendment, in the patch.** This is
the fifth consecutive cut at which the answer has been *"none required"* on the Code side; it is the first
at which one is required **inside** enacted §1, and that is because this is the first cut that introduces
a formula a second provision already had in different words.

---

## 8. §6.7's four apostrophes — normalised, recorded, folded into no amendment

**Performed as a non-substantive normalisation, exactly as the Policy Director directed, and it is not
part of any of the six edits.**

- **Count verified at store revision 61: four typographic apostrophes (U+2019) against 637 straight
  ones.** All four are inside subdivision G 4. Three are in *"the member's final qualifying retirement
  date"* or *"the member's behalf"*; the fourth is in the same subdivision's rescission passage.
- **It changes no meaning and it silently breaks exact-string anchoring**, which is why it is being done.
- **Applied as a whole-document substitution `’` → `'`, net character delta 0**, verified on both bases.
  After it, the typographic count is **0** and the straight count is **641**.
- **Recorded as a non-substantive normalisation and folded into no amendment.** It does not appear in any
  FIND or READ at §3, it carries no markup in §6, and it must be recorded in `bill-text-s8` §0 as a
  normalisation and not as an edit.
- **Order note for the applier: run the normalisation after the six substitutions, not before.** None of
  the six FIND strings contains a typographic apostrophe — I checked — so either order works, but running
  it last keeps the six counts reproducible against the stored base.

---

## 9. Drafter's note — every ambiguity I resolved, and how

**9.1 Why there are two decisions and not eight answers.** The Director's framing was right and it held
all the way through: cards (f) and (i) are one question, cards (b) and (h) are one question, and (c) sits
between them. **The proof that it held is §7.1** — once all 19 occurrences are classified, card (f) stops
being a judgment call and becomes a count: one endpoint moves against the member, and repairing it is 41
words. I did not know that when I started; I expected to recommend the verb definition.

**9.2 The ambiguity in "decide F-5 and the residual in one place, with one answer."** The Director also
said the residual is disposed to item 124 and is not mine to re-decide. I resolved the two as: **F-5 must
be drafted so that R-5 keys to the same date item 124 keys to** — the expiry of M 2's 90 days — **so that
the two agree if both are enacted and F-5 still answers if item 124 is declined.** §2.4. That is the only
reading on which one answer exists. **If the Director meant something else, Edit 164-4 is one word and I
will re-cut it; nothing else in the patch depends on it.**

**9.3 Why the 48-day cap, and why 48.** A bare notice-keyed endpoint is unbounded if the Board gives no
notice, which is the F-6 shape of defect and I am not going to introduce one while F-6 is open. The cap
uses the section's own numbers — Edit 2's 15 days, subsection A's 3, and the existing 30 — so it invents
no period. **The cap is also what holds Edit 164-1 to the carded 18 days** rather than to card (f)'s 78.

**9.4 Clause lettering, and why `(a)` and `(b)`.** M 2's tolling sentence already carries `(i)` and `(ii)`.
G 2's determination-date clauses use `(a)`, `(b)`, `(c)`. Using `(a)` and `(b)` inside a sentence that
already uses `(i)` and `(ii)` for a different purpose is the chapter's own practice and avoids a sentence
with two clause `(i)`s.

**9.5 "The person who filed the request", and why not "the member."** M 2's standing list has seven
classes and the tolling sentence speaks of *"the member or applicant."* Either class can file. **Naming the
filer names the actor and the recipient in one phrase** and covers both classes of tolling request without
reciting the list a third time.

**9.6 Why Edit 164-2's new limb repeats a 25-word cross-reference instead of saying "that sentence."**
Because the antecedent appears **after** the new limb. The section does not cross-refer by paraphrase, and
*"that sentence"* with a forward antecedent is worse than a repetition.

**9.7 What I resolved against myself.** I expected card (b)'s cure to be the simple notice-keyed endpoint,
and I drafted it that way first. It is option (b-2) at §2.2 and I recommend against my own first draft:
it restores 78 days, re-opens MOO-140's C2 and the retention's price, and **removes the act limb that
Edit 1's deeming attaches to.** The capped form keeps the limb and delivers the carded 18 days.

**9.8 What I did not resolve, and will not by drafting choice.** Card (c). Both candidates are drafted; the
choice between them moves an enacted board answer; it is at §10.1 and it is not mine.

**9.9 One thing I checked because the last six cuts have taught me to.** All three MOO-141-patch FIND
strings still resolve exactly once at store revision 61, after a seventh base move that landed in all
three of the provisions that patch reaches. **The patch does not need a re-cut for that move**, at either
revision 5 or revision 6. I would rather report that unasked than have it discovered at application.

**9.10 The patch moved under me mid-cut, and what I did about it.** This cut was built against the
MOO-141 patch at **revision 5**. [MOO-176](/MOO/issues/MOO-176) landed revision 6 — Edit 3 at **120
days** — while I was assembling it. **I re-ran every anchor and every count against the revision-6 base
rather than shipping against a superseded one**, and corrected every statement in this document that
depended on Edit 3's figure. There are four, and they are listed at §9.11 so a reviewer can check them
rather than take my word.

**9.11 The four places the 30/120 answer touched this cut, and what each now says.**

1. **§1.1's *Forst* paragraph.** It said the identity survives. **It does not** — the board's answer
   removed it. The point that survives is that Edit 164-1's clause (a) **keeps the act limb**, so Edit 1's
   deeming still reaches the tolling endpoint.
2. **§3.1's anchor note.** The short-form FIND was non-unique at revision 5 and is unique again at
   revision 6. **The full clause is the anchor on all three bases**, so neither answer strands it.
3. **§2.2's option (b-2) and §9.7.** The rejection no longer rests on the identity; it rests on the 78
   days, on MOO-140's C2, and on (b-2) removing the limb the deeming attaches to.
4. **Every price for the retention row.** MOO-163's $0 was for the 30-day retention.
   **[MOO-177](/MOO/issues/MOO-177) and [MOO-180](/MOO/issues/MOO-180) own the 120-day figure and I do not
   restate the old one as current.** Nothing in either decision turns on which figure it is.

**9.12 The standing caveat, in terms.** This is an internal working draft. It is not a Division of
Legislative Services bill, it has not been reviewed by counsel, and nothing in it states or implies that
it has been or that it is legally sufficient for introduction.

---

## 10. Open questions for the Policy Director — two, and only one blocks anything

### 10.1 Card (c) — which candidate, and the item-46 question

**(c-1)** narrows item 46's carve-out and costs the identified member her allowance for the window between
the Board's first action on her disability application and the G 2 determination taking effect — bounded at
120 days after the determination date, unbounded in the late-notice case, 210 days in the tolled-floor
case after Edit 164-2. **(c-2)** confirms item 46 as enacted and costs nobody anything against today's
reading. **I recommend (c-2).** Neither is in the patch and neither will be applied until this is answered.
**This is the item-46 question the Director said would go to the board.**

### 10.2 Card (i) — belt-and-braces or not

**I recommend not.** The 33-word confirming sentence is drafted at §1.3. It buys certainty on M 2's 90-day
duty and it buys item 123's negative-implication argument against the section's other 72 *"no later than"*
periods, and it complicates item 124's trigger. **Not a blocker: card (i) is closed either way.**

### 10.3 Not a question — two things I am flagging so they are not rediscovered

- **Edit 3's retention could be conformed to notice as well**, which would put both of M 2's endpoints on
  the same footing at the endpoint level rather than at the phrase level. **I have not drafted it**: Edit 3
  is a board decision, now at 120 days on the board's own answer, and it is [MOO-176](/MOO/issues/MOO-176)'s
  to re-cut and not mine. If the Director wants it, it is 29 words at a FIND this patch does not touch.
- **F-5 removes the need for card C as the residual's fallback** (§2.4). Item 124 remains the Director's
  disposition; the fallback is now five words of already-existing text rather than a new sentence.

---

## 11. Verification at store revision 61

### 11.1 The base

`bill-text-s8` on [MOO-42](/MOO/issues/MOO-42), document revision `3efccfe2-8332-4f4a-82ba-a9347141287f`,
revision number **3**, **271,611 characters**, fetched today. The §1 region I counted in — title line through the enactment clauses — spans **117,964 characters**.
`bill-text-s8-item-list`, revision number **3**, **323,866 characters**, read for items 46 and 124.

### 11.2 Anchors — eighteen counts, all 1

Every one of the six FIND strings counted in the **whole document** on each of three bases:

| Edit | Store rev 61 | + MOO-141 patch **rev 5** | + MOO-141 patch **rev 6** | Delta |
|---|---|---|---|---|
| 164-1 | 1 | 1 | 1 | +209 |
| 164-2 | 1 | 1 | 1 | +238 |
| 164-3 | 1 | 1 | 1 | +24 |
| 164-4 | 1 | 1 | 1 | +1 |
| 164-5 | 1 | 1 | 1 | +8 |
| 164-6 | 1 | 1 | 1 | +10 |
| **total** | | | | **+490** |

**The totals are identical on all three bases, which is the test of order-independence** — had any edit
overlapped an anchor of the MOO-141 patch at either revision, the count or the delta would have differed.

**The two candidate texts at §4 and the confirming sentence at §1.3 were counted too**: (c-1)'s FIND = 1,
(c-2)'s FIND = 1, and card (i)'s insertion point = 1, on all three bases. **None is applied.**

### 11.3 Post-application invariants — applied to a **copy**, every one checked

Applied to a copy of each base: final length **272,101** characters on store revision 61 alone,
**272,798** with the MOO-141 patch at revision 5, and **272,799** with it at revision 6; every count in
§7.2 confirmed; **no FIND re-resolved after its own edit**; both of G 4's express *"first"*s intact;
`is pending` and `was pending` unchanged at 8 and 1.

### 11.4 What I did not verify, stated as a limit

- **I did not verify that the MOO-141 patch's three edits produce the document the Director approved**, at
  either revision 5 or revision 6 — only that their FIND strings still resolve once at store revision 61 and
  that my six are independent of them on both. That patch's own verification is its own.
- **I did not re-read [MOO-176](/MOO/issues/MOO-176)'s revision-6 document in full.** I took Edit 3's new
  READ from its cut script and re-derived the base from it; I did not audit its reproductions, its
  four-limb day-37-to-day-127 pricing, or its answer to the 120/120 collision. **If any of those moved an
  anchor I rely on, the counts at §11.2 would have caught it, and they did not.**
- **I did not re-price anything.** The 78 days, the $0, the $204,000 and the 67.4% are MOO-141's and
  MOO-163's figures, cited and not recomputed.
- **I did not read § 51.1-156, § 51.1-162 or § 51.1-165 at source this heartbeat.** The claims at §7.3 that
  they refer to no changed word are from the text of enacted §1's references to them, not from those
  sections.
- **The 14-month figure at §4.1 is pass 10's**, from item 46 as written, and I have not reconstructed it.

### 11.5 Not applied to the store

**Nothing in this document has been written to `bill-text-s8` or to the §7 item list.** The apostrophe
normalisation at §8 is **drafted and verified, not applied**; it is to be performed as part of the next
store revision carrying these edits, and recorded in §0 as a non-substantive normalisation.

---

## 12. Status and next step

**Ready for the Red Team / Counsel Reviewer.** Then back to the Policy Director with the §10.1 answer.

1. **Counsel pass** on the six edits, the two decisions, and the two candidates at §4.
2. **The §10.1 answer** — card (c), which is the item-46 question for the board.
3. **Application**, in either order with the MOO-141 patch, with the three MOO-162 gates and the apostrophe
   normalisation performed in the same store revision.

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by counsel,
and nothing here states or implies that it has been. Pre-decisional and internal.**
