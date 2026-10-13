# -*- coding: utf-8 -*-
"""Assemble moo208-cut.md — the MOO-208 deliverable — from the live store text."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
red = open(os.path.join(HERE, "redline-d1.md"), encoding="utf-8").read()
title_red, d1_red = red.split("\n\n", 1)

HEAD = r"""# MOO-208 — the Policy Director's composite, cut as store revision 70

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by DLS, not legally sufficient for introduction. Pre-decisional and internal.**

**Enacted in [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) as store revision 70** — document revision `d4a67d3d`, number 89, 515,219 characters, §1 **132,557**. Base: document revision `3b9ac270`, number 88, store revision **69**, §1 **131,923**. Narrative at **§0.0-70**, cross-reference sweep at **§5.47**, drafter's note at **§6.0-70**, status at §8. Item list: **§7 item 133 re-scoped, §7 item 135 opened**, in [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list) revision `9a0543af`, number 13.

**What was commissioned, and it is all enacted.** F1 (the object), F2 in form D2b (the terminus, referent named), F3 in form D3c conformed (the channel), F4 (placement), F6 (the no-fault clause), F9 (the actor), and F8's title cure T2. **F5 held and the acknowledgment form not drafted. F7 not cut, its words re-scoped. E1 not re-cut, the [MOO-141](/MOO/issues/MOO-141) patch not applied, [MOO-176](/MOO/issues/MOO-176) revision 6 not touched, [MOO-97](/MOO/issues/MOO-97) §7 item 129's other answers left open.**

> **Three things in this document need your decision and one of them is serious. §5 below.** F3 as enacted does **not** close the subsection M channel, because subdivision M 2 reaches the omission on its own terms and D 1's sentence only ever extended it. The cure is one clause in M 2, drafted at §7 item 135 and not enacted.

---

## 1. The bill, as this revision leaves it

### Title line

"""

BODY_1 = r"""
### Enacting clause

**Be it enacted by the General Assembly of Virginia:**

**1. That §§ 51.1-142.2 and 51.1-162 of the Code of Virginia are amended and reenacted and that the Code of Virginia is amended by adding a section numbered 51.1-142.4 as follows:**

**Unchanged by this revision.** The act's footprint does not move: it still amends §§ 51.1-142.2 and 51.1-162 and still adds § 51.1-142.4. **No section joins or leaves the act, no designator is renumbered, no figure moves, no defined term is added, and the subdivision is no sentence longer or shorter.**

### The two layers of markup in this document, stated because they are easy to confuse

- **`<u>…</u>` is the amendatory markup against the Code of Virginia.** § 51.1-142.4 is a **new section**, so the whole of it — including the whole of subdivision D 1 below — is new language and sits inside `<u>` spans. **This revision adds no amendatory markup at all**: every word it adds falls inside an existing `<u>` span and every word it strikes falls inside one. That is why §1's `<u>`/`</u>` count is **62 / 62 before and after**.
- **Bold marks what this revision adds and ~~strikethrough~~ what it strikes, as against store revision 69.** That is a redline layer for reading, not amendatory markup, and it is **not** in the store. The store holds the clean text.
- The redline below was built by reversing the five substitutions out of the **live** provision and is verified by stripping its own layer and comparing character for character with what the store returned. `build_redline.py`.

### § 51.1-142.4. Military service purchase pilot program for state employees.

**Subdivision D 1, reproduced in full as amended.** This is the whole of the provision the six substitutions touch; five of the six are in it, and the sixth is the title line above. Nothing else in § 51.1-142.4, § 51.1-142.2 or § 51.1-162 is changed by this revision.

"""

BODY_2 = r"""
### Remaining enactment clauses

**Unchanged by this revision**, and reproduced by reference rather than in full because none of them is touched: **enactment 2** (the first enactment becomes effective 1 July 2029), **enactment 3** (§ 51.1-142.4 and the subdivision B 4 and B 2 amendments expire 1 July 2033, with clauses (i) to (iv) preserving administration, the subdivision D 2 limitations, the subsection J reporting and evaluation duties, and the rest), and the enactments after it. They are at `### Remaining enactment clauses` in [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8).

**No effective-date, sunset, reenactment or severability clause is added or changed.** The advisory is inside subdivision D 1 of a section that already has an effective date and an expiration, and it needs no clause of its own. **Note for the record:** the advice expires with § 51.1-142.4 on 1 July 2033 while the designation it points at, under § 51.1-162 A, does not — which is correct, because the act describes § 51.1-162 and does not amend subsection A of it.

---

## 2. The six substitutions, in the order that is the only order

Every FIND was re-counted **inside the §1 slice at the moment it was applied** — after its predecessor's output, not against the base. All six resolved exactly once. `composite.py` aborts before writing anything if one does not.

| # | Finding | FIND | 1× | Δ |
|---|---|---|---|---|
| 1 | **F4** — lift the advisory out of item 5 | `and no other designation has been made; that the member is advised to review the member's designation of beneficiary under subsection A of § 51.1-162 before completing payment; that subsection C of § 51.1-162` (208) | ✓ | **−137** |
| 2 | **F9 + F1 + F2 + F6** — set it down as item 7 of 7 | `in the order of precedence that section states.` (47) | ✓ | **+502** |
| 3 | **F4** — move the series' *"and"* to the new last item | `; and that where no benefit is payable` (38) | ✓ | **−4** |
| 4 | **F3** — except the advice from D 1's subsection M deeming | `A failure to state in the Board's certification every matter this subdivision requires to be stated in it is a failure of the Board` (131) | ✓ | **+116** |
| 5 | **F3** — keep it in the subsection J report | `and the Board shall state every such failure in the report required by subsection J.` (84) | ✓ | **+113** |
| 6 | **T2** — the title line | `pilot program; post-retirement employment; reports.` (51) | ✓ | **+44** |

**Why one revision and not six cuts.** D1, D2b, D6 and D9 all substitute on one FIND string, so they travel together — and **D3c travels with them, which the disposition did not carry.** D3c writes D9's 61-character FIND into the subdivision **twice more**, so D9's anchor goes from 1× to 3×. In the other order D3c's exception would have described *"a failure to state that the member is advised to review…"* while the subdivision required *"that the Board advises the member to review…"*: **F3 would have been enacted and inert in both limbs, with nothing failing.** The apply kit demonstrates that before it applies anything.

**Post-conditions, asserted before the write and re-checked on the returned body.** §1 **131,923 → 132,557 (+634)**. §1 `<u>`/`</u>` **62 / 62 unchanged**. The certification series **7 items, advisory at item 7 of 7**. **Six semicolons in the series, unchanged.** The series' period count unchanged, so **no sentence boundary moved**. **Zero occurrences of *"the member is advised to"* left in §1.** The conformed phrase **exactly 3× in §1** — the item, the M exception, the J limb. No figure moved, no designator renumbered, no section joined or left the act, no defined term added.

**One post-condition I corrected rather than reported as met.** The Director required §1 at **+590** on the footing that substitution 6 *"adds +44 to the document outside §1."* **It is not outside §1**: the bill's title line sits under `### Title`, which is inside §1 as §1 is bounded in that document. The +590 is substitutions 1 to 5 measured on the §1 slice before the title line was touched. **§1's measured movement is +634, and the kit asserts the corrected delta and would have aborted on the stated one.** The absolute figures are spent in any event — store revision 69 landed between the disposition and this cut — so the deltas are what carried over.

---

## 3. Conforming amendments

**None are required and none is made.** The cross-reference check was performed in both directions and is at **§5.47** of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8). **Out: seven citations chased, every one accurate.** **In: ten checks, nine clean and one adverse.**

**The clean results, in one line each.** **Subsection J** — subdivision J 1's enumeration ends *"and, to the extent not otherwise required by this subdivision, every other matter this section requires the Board to state in that report"*, so the new J limb is picked up with no amendment and **substitution 5 does the whole of what it was taken to do.** **§ 51.1-162 A and B** — not amended by this act and not to be; the item describes them, using A's own nouns, and B's two branches were already in item 4 of the series. **Subdivisions G 4 and G 5** — unchanged in wording; nothing stranded. **§2's plain-English summary** — zero occurrences of *"designation"*, *"advis"*, *"certification shall also state"* or the title line, verified by count. **Nothing in the enacted text counts the series by position**, which is why F4 cost zero characters. **The old advisory's words** — *"the member is advised to"* now occurs **0× in §1**; its surviving occurrences are historical record and correct as history.

**The adverse result is at §5 below.**

---

## 4. Drafter's note

**The full note is §6.0-70** of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) — eleven items and four open questions. The structure choices, in short:

1. **F9's *"advises"* over *"is advised"*.** The carrier sentence already named the Board, so the actor was never missing from the subdivision — but **the item read alone was self-verifying**, true merely because the Board stated it, and it was the only one of seven that was. *"Advises"* is the Board's own verb and imposes nothing on the member. Every no-duty property §6.0-65 item 1 defends survives.
2. **Why both the terminus and the power are stated.** *"Before completing payment"* was never the defect; the **inference from it standing alone** was. Kept as the prompt to act now, with the power to re-designate until death stated after it: do it now, and know you can change it later. **The power is a correct reading of § 51.1-162 A and an inference from A's structure, not a quotation of an express grant** — A fixes no moment and A's own fallback contemplates a later designation. The words are tied to A so they follow A if A is amended. **This is the highest-risk proposition in the new item and it is recorded as such.**
3. **Why the full citation opens the item and *"that section"* runs inside it.** The item now carries three propositions and shifts referent twice inside its own span, so it must supply its own referent and not borrow a neighbour's — the more so because the last item in a series is the one a certification template is most likely to lift out of it.
4. **Why item 7 of 7, and why it is free.** Still its own semicolon item, still introduced by *"that"*, still the only item in a different register — and no longer interleaved among the six propositions of law it must not be read as part of. It also stops splitting item 4's forward reference to *"subsection C of that section"* from the item that restates that citation in full. **Zero characters, verified not assumed.**
5. **D3c over D3a and D3b.** D3a asserts the exception in the sentence after the one deeming it a failure; D3b buys a reference by position that breaks the day a sentence is inserted between them. **D3c carves the exception into the deeming clause and names the matter in the subdivision's own words.** Conforming it to F9's wording was not style: unconformed, both limbs would have described a matter the subdivision no longer requires.
6. **What is not drafted, and it is not silence.** No acknowledgment form (held, and directed not to be drafted), no route, no misstatement limb. The route question goes to the subsection J report, so that a requirement would rest on the pilot's own evidence rather than a guess.
7. **The title line.** T2 over T1 because the object the act now embraces is not only the payment of a death benefit but **the member's designation of one**, which is what all seven statements are about; *"death benefits"* alone would have given notice of six of them. Placed after *"pilot program"*, following the clause's existing order, in the same semicolon-separated lower-case style. **The commission did not reach the title line and the Director extended it expressly** — recorded, because an edit outside the commission as received should never rest on inference.

---

## 5. What needs your decision, in order of weight

**1. Serious — F3 does not close the channel it was taken to close. Drafted at §7 item 135 and not enacted.**

**Subdivision M 2's first sentence confers the channel independently of subdivision D 1.** It reaches a person adversely affected *"by a failure of the Board to state in a certification or notice a matter this section requires to be stated in it."* The advice is a matter **this subdivision** requires to be stated and D 1 is part of **this section**. Three features of the act's own words make this more than a reading:

- **M 2's clock anticipates D 1.** It runs *"within 30 days after the certification or notice is given or, **where the provision that requires the matter to be stated provides a longer or later period, within that period**."* D 1's bespoke clock is that longer period — 30 days from the certification for the member, 30 days from the subdivision G 4 notice for a claimant who is not the member. **M 2 contemplates a provision like D 1 extending it, not constituting it.**
- **D 1's sentence is conferring, not constituting.** It deems, it extends the clock, and it disapplies M 2's second sentence for the member. An exception written into a conferring sentence confers less; it does not withdraw what another subdivision independently gives.
- **The act's pattern says the same.** §1 carries six *"for the purposes of subsection M"* clauses; the other five are all declaratory (*"X is a determination of the Board for the purposes of subsection M"*), and **M 2's second sentence says in terms that its reach operates *"whether or not another provision of this section expressly provides for review of it."***

**So what substitution 4 actually did.** The member keeps reconsideration under M 2 on a 30-day clock from the certification. A claimant who is not the member — **a survivor — loses the subdivision G 4-notice clock, which was the only clock she could ever have used**, because the certification is handed to the member years before the survivor learns the designation was wrong. And M 2's second sentence, which D 1 had disapplied for the member, applies to her case again. **Narrower than the status quo for the survivor, unchanged for the member: close to the opposite of the trade you took F3 for.** Substitution 5, the J limb, is unaffected and works in full.

**Why it is enacted anyway.** The words are yours, approved verbatim; the cure is a provision nobody has agreed; and **no cure inside D 1 can work**, because the defect is that M 2 does not look at D 1. **The clause has to go in M 2, which this commission did not open.** Two forms are drafted at §7 item 135 — **M-a**, naming the matter in M 2 in the words the act already uses, **+116 and no conforming change anywhere else, which I recommend**; and **M-b**, a generic hook in M 2 at **+101** plus **+42** in D 1, cheaper only if you expect more exceptions. **Take one, leave both, or send it to counsel — but the record should not sit with F3 described as taken and the channel described as closed.**

**2. The scope of §7 item 133 as re-scoped.** You directed that F7's misstatement limb reach *"the six propositions of law and not the advisory."* **The draftable scope is *"every matter other than the advice"*, which reaches the six propositions *and* item 7's other two** — the power to re-designate and the no-fault clause. Strict scoping needs a handle the text does not have: the seven items are undesignated clauses of one sentence, and the only clean handle is **designating them (i) through (vii)**, a renumbering your commission forbade and a separate edit. The words are re-scoped to the draftable form and the difference is recorded in the item, not drafted around. **If you want the strict scope, the renumbering is the cut** — and it would give the M exception a handle too.

**3. The F3 residue, which is now wider than your statement of it.** You named it: D3c's exception covers only the first of item 7's three propositions, so omitting the other two stays reviewable. **What follows is an asymmetry with item 133**: misstating those two would be unreached while omitting them stays reviewable — the mirror image of the gap F7 exists to close. **Widening the exception to all three propositions is one decision and should be taken once, in D 1 and M 2 together**, not twice in different places.

**4. A dead anchor I found while verifying the scope held, and this revision did not cause it.** **[MOO-176](/MOO/issues/MOO-176) revision 6's Edit 1 cannot be applied as written.** Its FIND ends *"…from the giving of that statement or notice is extended by three days.</u>"*; the live provision reads *"…from the giving of that statement**, notice, or certification** is extended by three days.</u>"*, widened by a revision later than MOO-176 revision 6. **0× on the base and 0× after this composite; Edits 2 and 3 are 1× before and 1× after.** The re-anchored string is at §5.47 direction 2, check 9. **I have not re-cut it** — MOO-176 revision 6 is expressly out of scope — but whoever owns it should know before they try.

**5. The ceiling, which is now a live constraint.** With its record layer this revision landed at **527,893** characters against the store's **524,288** limit and **could not write at all** until **§5.38 and §5.39 were moved verbatim** to [`bill-text-s8-record-s0-s5-s6-rev2-51`](/MOO/issues/MOO-42#document-bill-text-s8-record-s0-s5-s6-rev2-51) — the rotation §0.1 sets and the move the §5 paragraph has named as next since store revision 58. Each left a stub in the form §5.37 established; **no sweep is edited and no enacted word is touched by the move.** Only the §5 half was performed. **§6.0-59 and §6.0-60 remain and are next**, and the document closes at about **9,000** characters of headroom — roughly one more revision of this size. **The structural answer, when you want it, is that §5 and §6 should hold the current entry and one predecessor and nothing else**: the rule as written lets each section grow until a revision is blocked, which means the blocked revision pays for every revision before it.

---

## 6. Reproducing this

| File | What it does |
|---|---|
| `composite.py` | Fetches the live base, demonstrates the D3c/D9 sequencing hazard, applies the six substitutions with every anchor re-counted inside the §1 slice, applies the record layer and the forced rotation, asserts every post-condition, writes the retained-record document first and the bill second, and verifies both from the returned JSON |
| `rotate70.py` | The §5 retention rotation: §5.38 and §5.39 out verbatim, stubs in |
| `rec_s0_70.md`, `rec_s5_47.md`, `rec_s6_70.md`, `rec_s8_70.md` | The narrative, the sweep, the drafter's note, the status block |
| `rec_patches70.py` | The eight in-place record corrections |
| `items70.py` | §7 item 133 re-scoped and §7 item 135 opened |
| `build_redline.py` | The redline in §1 above, built by reversing the substitutions out of the live text and verified by stripping back to it |

```
python3 composite.py --dry-run && python3 composite.py
python3 items70.py --dry-run && python3 items70.py
python3 build_redline.py
```

**For the Editor, in three sentences.** The Board's certification for a military-service purchase must already tell a member what happens to her death benefit if she dies before retiring; this revision makes it also tell her, in the Board's own voice and as the last of seven statements, to review her beneficiary designation **and what that designation does under § 51.1-162 B**, that she may change it at any time before she dies, and that nothing in the provision requires her to review it or costs her a benefit if she does not. Failing to give that advice is no longer treated by subdivision D 1 as a reviewable failure to state, but it must be reported to the money committees in the Board's annual report on the pilot. The bill's title now says the act relates to death benefits and the designation of a beneficiary, which it always did.

**Risk section the Editor needs:** the title point — *Dean v. Paolicelli*, 194 Va. 219 (1952), and **a title cured in an internal draft is not a cured title until DLS says so**; and the F3 point — **an advisory omission remains reviewable under subdivision M 2 whatever subdivision D 1 now says, and the survivor's clock is shorter than it was.**

---

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by DLS, not legally sufficient for introduction. Pre-decisional and internal.**
"""

out = HEAD + title_red.strip() + "\n" + BODY_1 + d1_red.strip() + "\n" + BODY_2
open(os.path.join(HERE, "moo208-cut.md"), "w", encoding="utf-8").write(out)
print("moo208-cut.md", len(out), "chars")
