# MOO-164 apply kit — the act-versus-notice cut, **revision 7**

**Current check: `verify_r70_v7.py` (base `bill70.md`). Current splicer: `repro70.py`. Current
applier: `apply164.py`. Current document build: `build_rev7.py`. Current consistency check:
`check_doc_vs_kit.py`. There is exactly one of each.** Everything else is superseded and is named as
such below.

```
python3 verify_r70_v7.py bill70.md   # 0 failures expected — the current check
python3 apply164.py bill70.md        # writes applied.md; asserts +3375 and out-of-§1 byte-identity
python3 repro70.py bill70.md         # writes repro70.json — the §6 reproductions, by content
python3 build_rev7.py                # writes moo164_rev7.md; 0 post-condition failures expected
python3 check_doc_vs_kit.py          # 0 mismatches expected — the document against the kit
```

> ## ⚠ THE PATCH IS **TWELVE EDITS IN THIRTEEN SUBSTITUTIONS** AT REVISION 7, AND THE DELTA IS **+3,375**
>
> [MOO-209](/MOO/issues/MOO-209)'s counsel pass is folded. **164-7** takes F1's extended exception,
> **164-8** takes F2 and F3, **164-12** takes F6, and **164-13 is new** on F4 — two substitutions
> inside one sentence of subdivision D 1.
>
> Revision 6 was eleven substitutions and **+2,551**; revision 5 was six and **+642**. Anything in
> this directory that still says +2,551, +642 or +490 is a superseded file, not a disagreement.

> ## ⚠ APPLY EVERY FIND INSIDE ENACTED §1 ONLY
>
> From store revision 62 the §0 revision narrative of `bill-text-s8` quotes anchor strings. At store
> revision 70, **five of the thirteen FINDs occur more than once whole-document** — 164-10's occurs
> **four** times. **A whole-document find-and-replace will corrupt the revision record.**
> `apply164.py` slices §1 before substituting and asserts afterwards that the head and tail are
> byte-identical. This is [MOO-187](/MOO/issues/MOO-187) finding **F21**, and it is the finding most
> likely to cause actual damage.

> ## ⚠ TWO HELD CANDIDATES AND ONE DECLINED FIX — DO NOT APPLY ANY OF THEM
>
> - **164-9 — HELD.** The two-limb cap closing the last 60 days at M 2's tolling endpoint. Priced at
>   [MOO-204](/MOO/issues/MOO-204) (*take it, with 164-10*), **still held pending the Policy
>   Director**. It amends **Edit 164-1's own new text**, so its FIND resolves **0** in the base and
>   **1** in the applied text — both asserted.
> - **164-14 — HELD.** [MOO-209](/MOO/issues/MOO-209) **F10**: *"or the application is otherwise
>   disposed of"*, +39 characters. It amends **Edit 164-12's own new text** — same 0/1 pattern.
>   **Held because it narrows (c-2), whose cost-neutrality is the express reason no item-46 card went
>   to the board.** Question 1.
> - **164-7-F13 — DECLINED on drafting grounds**, words drafted at §17.9. F13's *"for acting upon
>   that request"* would create a **sixth variant** of the formula card (j) and Edit 164-6 exist to
>   conform. The Policy Director can overrule it in one line.
> - **(c-1) — RETIRED.** Counsel's first-pass F9 makes it defective, not merely impolitic. The
>   verifier asserts its FIND still resolves once **unamended**, which is how it proves Edit 164-12
>   leaves G 4 alone.
> - **Card (i)'s 33-word confirming sentence — DECLINED.**
> - **First-pass F11 — carried forward, not drafted.** For the next pass that opens the definition.

**Deliverable:** the issue document
[`moo164-act-versus-notice`](/MOO/issues/MOO-164#document-moo164-act-versus-notice) on
[MOO-164](/MOO/issues/MOO-164), **revision 7**, 322,095 characters. The bill text lives in the
Paperclip store, not here.

## Base

**Store revision 70** — whole document **515,219**; **enacted §1 132,557**. **The base has moved
fifteen times under this cut.**

Revision 6 was cut at store revision 68 (§1 131,066) and re-verified at 69 (§1 131,923). Two moves
since:

| | What moved | Reproduced at §6? | Anchor moved? |
|---|---|---|---|
| store rev **69** | **G 4** rewritten; subsections B and L exchanged a sentence | **G 4 yes** | no |
| store rev **70** | **D 1** — the certification series' new item 7, the subsection M exception, the subsection J limb, the series' *"and"*; and the **title line** | **D 1 yes**, title yes | no |

**Eighth stale reproduction behind anchors that all still resolved exactly once.** `repro70.py`
re-splices every provision **by content, not by line index**, and now also reproduces the **title
line, enacting clause and first enactment** so §5 cannot go stale silently either.

**Store revision 70 did one thing for this cut, unasked:** its substitution 3 moved D 1's
certification series' *"and"* to that series' new last item — the identical repair Edit 164-13(b)
needs for the disclosure series. **Precedent, not preference.**

## Application order

**Application of the MOO-141 patch does not precede this cut carrying F-9.** This cut carries it, so
that condition is satisfied. Beyond that the two patches are **order-independent**, verified on three
bases: store revision 70 as it stands, with the MOO-141 patch carrying Edit 3 at **30 days**, and
with it carrying Edit 3 at **120 days**. **Thirty-nine counts, all 1; delta +3,375 on all three.**

Stated exactly, so the claim is checkable: **the thirteen-substitution form is verified at store
revision 70**; the eleven-edit form was verified at store revisions 68 and 69; the six-edit form at
63, 64 and 65. **Order-independence and indifference to the 30/120 answer hold at every one.**

**The apostrophe normalisation runs AFTER the substitutions, not before.**

## The thirteen substitutions

| Edit | Site | Rev 6 | **Rev 7** |
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

`verify_r70_v7.py` sums the per-substitution deltas and asserts them against the measured total, so
this table is counted and not added up by hand.

## What revision 7's check adds, and why each line exists

Every one of these exists because [MOO-209](/MOO/issues/MOO-209) asked for a **proposition** rather
than a string:

- **F1** — the extended exception's second descriptor has exactly **one** referent (R-6), counted on
  the base; **and R-6's own keying is counted on both bases**, which is how the MOO-141 Edit 2
  interaction is made visible rather than argued. **This is the one thing revision 7 cannot close by
  drafting** — see below.
- **F5** — the mislabelled line is **deleted, not relabelled**. Replaced by a count of the duty the
  notice-keyed endpoint actually keys to, of which there is **none** (*"notice of its decision"* is
  **0** in the base). **48 is a chosen outer limit, not a restatement of the section's arithmetic.**
- **F16** — a commencement phrase is asserted **within each** of the five *"shall act upon"* duties,
  not once against 164-10's own sentence.
- **N1** — the saving's **256-character** body is asserted **byte-identical** between 164-7 and
  MOO-141 Edit 1. The *"word for word"* claim was made twice and was false twice (first-pass F19,
  F20). **`verbatim` is a counted claim.**
- **N2** — every *"preceding sentence"* reference in the applied §1 is counted, and revision 7 is
  asserted to add **exactly three** — two in 164-7, one in 164-8, **none in 164-13**.
- **F12** — the act-upon family is counted at **0** anywhere in § 51.1-142.2, so the next reader does
  not go looking for the provision the B 4 f extension reaches. **The clause is kept.**
- **F6** — 164-12 is asserted to add a confinement clause and **no** notwithstanding.
- **F4** — the disclosure series is asserted to carry **exactly one** *"; and ("*, before **(iv)** and
  not before **(iii)**, in both directions.
- **`check_doc_vs_kit.py`** — extracts every FIND and READ block from §3 of the built document and
  asserts each appears **verbatim** in the kit's edit table, both ways. **F5's lesson one level up: a
  check that counts strings against the bill cannot detect a document that quotes a superseded
  edit**, and revision 7 re-cut four of them.

## The one thing revision 7 cannot close by drafting

**F1's cure is operative on store revision 70 and INERT after MOO-141's Edit 2.** Edit 2 re-keys R-6's
15 days from the Board's **act** to the **giving of its decision**, which 164-7's confinement clause
does not reach. On the combined text R-6 becomes a duty keyed to an event that in the deemed case
never occurs — limb 3's shape, relocated to the definition by a patch that is not this one. **Both
counts are in the verifier.** The smallest cure is a second limb in **MOO-141's Edit 2**, which is
theirs; [MOO-141](/MOO/issues/MOO-141) has been told and nothing has been drafted into their patch.
**164-7's deeming will not be made to reach a *giving*** — deeming a decision given when it has not
been would start the member's own clocks without her knowledge, which is card (b)'s whole subject.

## Files

- `verify_r70_v7.py` — **the current check**. Counts over enacted §1 only.
- `repro70.py` → `repro70.json` — **the current splicer**. Locates every provision by content.
  **Re-run this, do not hand-edit the reproductions**, whenever the base moves.
- `apply164.py` — **the current applier**. Applies all thirteen substitutions to a **copy**, §1 only,
  with the out-of-§1 byte-identity assertion, then performs the apostrophe normalisation. **Its edit
  set is lifted verbatim from `verify_r70_v7.py` so the check and the applier cannot drift.**
- `build_rev7.py` → `moo164_rev7.md` — **the current document build**. Every in-place correction is
  asserted for an exact occurrence count before it is made, so a correction that matches nothing — or
  twice — fails the build instead of shipping.
- `check_doc_vs_kit.py` — **the current consistency check** between the document and the kit.
- `sec17.md` — revision 7's new section, as drafted.
- `bill70.md` — the current base. `bill69.md` / `bill.md` — store revisions 69 and 68, kept as record.
- `moo164.md` — the assembled deliverable as stored at revision 6. `disposition-rev5.md` — the
  Policy Director's disposition that revision 6 folded in.
- **Superseded, kept only as the record of earlier runs:** `verify_r69_v6.py`, `verify_r68_v6.py`,
  `verify_r68.py`, `verify_r65.py`, `verify_r64.py`, `verify_r63.py`, `repro68.py` / `repro68.json`,
  `repro65.py` / `repro65.json`, `repro63.py` / `repro63.json`, `repro.py`, `head63.md`, `head64.md`,
  `s1_64.txt`, `s1_68.txt`, `doc_part1..6.md`. **`verify_r6.py` and `verify.py` were deleted at
  revision 5** — they counted whole-document and hard-failed from store revision 63 on (F21).

**Nothing in this kit has been applied to the store.** The apostrophe normalisation is drafted and
verified, not applied; it belongs in the next store revision carrying these edits and must be
recorded in §0 as a non-substantive normalisation.

**Internal working draft. Not a Division of Legislative Services bill. Not legally cleared by
counsel — [MOO-187](/MOO/issues/MOO-187) and [MOO-209](/MOO/issues/MOO-209) are internal adversarial
passes, expressly not legal advice, and revision 7's four new and re-cut texts have not been read
adversarially at all. Not legally sufficient for introduction.**
