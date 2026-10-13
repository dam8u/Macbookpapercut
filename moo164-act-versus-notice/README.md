# MOO-164 apply kit — the act-versus-notice cut, **revision 8**

**Current check: `verify_r72_v8.py` (base `bill72.md`). Current splicer: `repro72.py`. Current
applier: `apply164.py`. Current document build: `build_rev8.py`. Current consistency check:
`check_doc_vs_kit.py`. Current adversarial harness for that check: `break_check_rev8.py`. There is
exactly one of each.** Everything else is superseded and is named as such below.

```
python3 verify_r72_v8.py bill72.md   # 0 failures expected — the current check
python3 apply164.py bill72.md        # writes applied.md; asserts +4210 and out-of-§1 byte-identity
python3 repro72.py bill72.md         # writes repro72.json — the §6 reproductions, by content
python3 build_rev8.py                # writes moo164_rev8.md; 0 post-condition failures expected
python3 check_doc_vs_kit.py          # 0 mismatches expected — the document against the kit
python3 break_check_rev8.py          # 0 mutations the check cannot see — MOO-214 S5's own harness
```

> ## ⚠ THE PATCH IS **TWELVE EDITS IN THIRTEEN SUBSTITUTIONS** AT REVISION 8, AND THE DELTA IS **+4,210**
>
> [MOO-214](/MOO/issues/MOO-214)'s counsel pass is folded — 13 findings, none rejected. **164-7**
> takes **S3** (the paraphrase descriptor out, the determinate one in), **m2** and the Policy
> Director's MOO-141 **§3.3 cross-reference**; **164-8** takes **S1** and **m1**; **164-13(b)** takes
> **S2** and **M1**; **164-12** takes **M3**.
>
> Revision 7 was thirteen substitutions and **+3,375**; revision 6 eleven and **+2,551**; revision 5
> six and **+642**. Anything in this directory that still says +3,375, +2,551, +642 or +490 is a
> superseded file, not a disagreement.

> ## ⚠ APPLY EVERY FIND INSIDE ENACTED §1 ONLY
>
> From store revision 62 the §0 revision narrative of `bill-text-s8` quotes anchor strings. At store
> revision 72, **five of the thirteen FINDs occur more than once whole-document** — 164-10's occurs
> **four** times. **A whole-document find-and-replace will corrupt the revision record.**
> `apply164.py` slices §1 before substituting and asserts afterwards that the head and tail are
> byte-identical. This is [MOO-187](/MOO/issues/MOO-187) finding **F21**, and it is the finding most
> likely to cause actual damage.

> ## ⚠ SIX HELD CANDIDATES AND ONE DECLINED FIX — DO NOT APPLY ANY OF THEM
>
> - **164-9 — HELD.** The two-limb cap closing the last 60 days at M 2's tolling endpoint. Priced at
>   [MOO-204](/MOO/issues/MOO-204) (*take it, with 164-10*), **still held pending the Policy
>   Director**. It amends **Edit 164-1's own new text**, so its FIND resolves **0** in the base and
>   **1** in the applied text — both asserted.
> - **164-14 — HELD.** [MOO-209](/MOO/issues/MOO-209) **F10**: *"or the application is otherwise
>   disposed of"*, +39 characters. It amends **Edit 164-12's own new text** — same 0/1 pattern.
> - **164-15 — HELD, NEW AT REVISION 8.** [MOO-214](/MOO/issues/MOO-214) **S6**: the non-receipt
>   saving on s12's 30-day window, **+210 characters**. It adds a **chosen** outer bound of 90 days,
>   which is why it is a question and not a repair. **If taken, clause (iv) must be conformed in the
>   same cut.** Amends Edit 164-8's own new text — 0/1.
> - **164-16 — DECLINED, NEW AT REVISION 8.** Counsel's impose-not-except form of **S3**. Declined
>   because MOO-141's Edit 2 **revision 8** already imposes the residual deadline on R-6 itself, so
>   this would be a **second duty to give the same notice**. Words drafted at §18.1.
> - **164-17 — HELD, NEW AT REVISION 8.** [MOO-214](/MOO/issues/MOO-214) **S4**: the failure-to-state
>   and J-report route for the written statement and the notices, **+589 characters**, modelled on
>   D 1's own certification sentence. Amends Edit 164-13(b)'s own new tail — 0/1.
> - **164-18 — HELD, NEW AT REVISION 8.** [MOO-214](/MOO/issues/MOO-214) **M2**: the
>   one-concept-one-word alternative, **+33 characters**. **Its FIND is in the BASE and CONTAINS Edit
>   164-12's FIND, so 164-12 and 164-18 are mutually exclusive** — asserted. It rewrites
>   [MOO-42](/MOO/issues/MOO-42) §7 item 46's own sentence, so it is the Director's call.
> - **164-7-F13 — DECLINED on drafting grounds**, words drafted at §17.9. F13's *"for acting upon
>   that request"* would create a **sixth variant** of the formula card (j) and Edit 164-6 exist to
>   conform. The Policy Director can overrule it in one line.
> - **(c-1) — RETIRED.** The verifier asserts its FIND still resolves once **unamended**, which is how
>   it proves Edit 164-12 leaves G 4 alone.
> - **Card (i)'s 33-word confirming sentence — DECLINED.**
> - **First-pass F11 — carried forward, not drafted.**

**Deliverable:** the issue document
[`moo164-act-versus-notice`](/MOO/issues/MOO-164#document-moo164-act-versus-notice) on
[MOO-164](/MOO/issues/MOO-164), **revision 8**, **367,394 characters** (370,174 bytes — the figure `wc -c` gives, which is not the same thing and is not the figure the store reports). The bill text lives in the
Paperclip store, not here.

## Base

**Store revision 72** — whole document **502,586**; **enacted §1 134,012**. **The base has moved
seventeen times under this cut.**

Revision 7 was cut at store revision 70 (§1 132,557). Two moves since:

| | What moved | Reproduced at §6? | Anchor moved? |
|---|---|---|---|
| store rev **71** | **thirteen substitutions in §1** — MOO-210's R2/R5/R6 and nine MOO-200 findings — in **G 4**, the **certification**, **subsection N** and the **title line** | **G 4 and D 1 yes**, title yes | no |
| store rev **72** | **record only.** MOO-211's counsel pass disposed into the record | — | no |

**Ninth stale reproduction behind anchors that all still resolved exactly once.** `repro72.py`
re-splices every provision **by content, not by line index**, and carries its own post-conditions:
each revision-8 text asserted present once, each superseded form asserted absent.

**Store revision 72's "record only" is proved, not taken on trust:** `verify_r72_v8.py` compares
enacted §1 against the store-revision-71 copy at `../moo141-rev71/live.md` and asserts byte-identity.

## Application order

**Application of the MOO-141 patch does not precede this cut carrying F-9.** This cut carries it, so
that condition is satisfied. Beyond that the two patches are **order-independent**, verified on three
bases: store revision 72 as it stands, with the MOO-141 patch carrying Edit 3 at **30 days**, and
with it carrying Edit 3 at **120 days**. **Thirty-nine counts, all 1; delta +4,210 on all three.**

**The Policy Director has decided the joint landing on [MOO-141](/MOO/issues/MOO-141): that patch and
this cut are applied in ONE cut.** The §3.3 cross-reference this cut now carries does **not** create
that dependency — it names the other deeming **by content**, so with MOO-141 absent the class is
empty and the clause is inert. Counted 0 / 1 / 2 across the three bases.

Stated exactly, so the claim is checkable: **the revision-8 form is verified at store revision 72**;
the revision-7 form at 70; the eleven-edit form at 68 and 69; the six-edit form at 63, 64 and 65.
**Order-independence and indifference to the 30/120 answer hold at every one.**

**The apostrophe normalisation runs AFTER the substitutions, not before.**

## The thirteen substitutions

| Edit | Site | Rev 7 | **Rev 8** |
|---|---|---|---|
| 164-1 | M 2, the tolling endpoint | +233 | +233 |
| 164-2 | G 2, the 120-day exception | +366 | +366 |
| 164-3 | M 2 clause (ii) | +24 | +24 |
| 164-4 | the definition, R-5 | +1 | +1 |
| 164-5 | D 1, the lateness descriptor | +8 | +8 |
| 164-6 | G 4, the period formula | +10 | +10 |
| **164-7** | M 2 — the deemed act, its saving, m2's sentence and the §3.3 cross-reference | +1,337 | **+2,004** (S3, m2, §3.3) |
| **164-8** | D 1, the filing vehicle | +621 | **+613** (S1, m1) |
| 164-13(a) | D 1, the disclosure duty's document list | +103 | +103 |
| **164-13(b)** | D 1, clause (iv) and the series' *"and"* | +454 | **+564** (S2, M1) |
| 164-10 | M 2's 90-day duty, commencement | +27 | +27 |
| 164-11 | M 2's expiry-notice sentence | +24 | +24 |
| **164-12** | G 2, item 46's carve-out | +167 | **+233** (M3) |
| | **total** | **+3,375** | **+4,210** |

`verify_r72_v8.py` sums the per-substitution deltas and asserts them against the measured total, so
this table is counted and not added up by hand.

## What revision 8's check adds, and why each line exists

- **S3** — the exception's descriptor is asserted to be the one 164-5 and 164-13(a) put into the
  bill, at **three** sites; the revision-7 paraphrase is asserted **absent**; and its two rival
  referents (**R-3** and **R-4b**) are counted, so the ambiguity is a number rather than an argument.
  The descriptor is also asserted to contain **no deadline formula**, which is why MOO-141's Edit 2
  cannot detach it.
- **M4** — the *expressio unius* inference is shown **inert**, not argued away: MOO-141 Edit 2 at
  **its** revision 8 is applied beside this cut and R-6's ordinary-class deadline is counted as
  decision-keyed, so Edit 1's deeming cannot reach it either way.
- **N1 preserved** — m2's cure is a **separate sentence**, so the saving's 256-character body stays
  byte-identical between 164-7 and MOO-141 Edit 1. Asserted, as before.
- **§3.3** — each of the Director's three requirements is a counted assertion, including requirement
  3 by **absence**: no *"no later than"*, no *"days"*, no *"month"*, no *"date of"*, no *"except"*.
- **S1/S2/M1** — s12 and clause (iv) are asserted to share every operative limb, in both directions.
- **S4** — *"failure to state"* and *"requires to be stated"* are counted at **0** in subsection J.
- **store rev 72** — enacted §1 is asserted **byte-identical** to store revision 71.

## What revision 8's consistency check adds — [MOO-214](/MOO/issues/MOO-214) **S5**

Counsel broke the revision-7 `check_doc_vs_kit.py` three ways; each time it printed *"0
mismatch(es)"*. The rewrite takes all five fix directions — whole-document scan, every fence
accounted for, FIND/READ **pairing**, an anchored label regex, and the stated per-edit deltas checked
against `len(READ) − len(FIND)`. **`break_check_rev8.py` re-runs counsel's three mutations plus a
fourth and reports 0 the check cannot see.** It caught a real bug in the rewrite on its first run —
the delta window started at the fence's own offset, so a 1,200-character READ block consumed it — and
one real false claim in the document, at §3.12.

**`apply164.py` now IMPORTS the edit table from `verify_r72_v8.py`** instead of holding a copy
described as *"lifted verbatim."* An import cannot drift from its source; a copy can, and saying it
cannot is the shape of claim MOO-209 F19 was about.

## Files

- `verify_r72_v8.py` — **the current check**. Counts over enacted §1 only.
- `repro72.py` → `repro72.json` — **the current splicer**, with its own post-conditions.
  **Re-run this, do not hand-edit the reproductions**, whenever the base moves.
- `apply164.py` — **the current applier**. §1 only, byte-identity assertion, then the apostrophes.
- `build_rev8.py` → `moo164_rev8.md` — **the current document build**.
- `check_doc_vs_kit.py` — **the current consistency check**; `break_check_rev8.py` — its harness.
- `sec18.md` — revision 8's new section, as drafted.
- `bill72.md` — the current base. `bill70.md` / `bill69.md` / `bill.md` — store revisions 70, 69 and
  68, kept as record.
- `moo164_rev7.md` — the deliverable as stored at revision 7. `moo164_rev6.md`, `moo164.md` —
  earlier. `disposition-rev5.md` — the Policy Director's disposition revision 6 folded in.
- **Superseded, kept only as the record of earlier runs:** `verify_r70_v7.py` (still imported by
  `build_rev8.py` as the source of the revision-7 READ strings it swaps out, and for nothing else),
  `verify_r69_v6.py`, `verify_r68_v6.py`, `verify_r68.py`, `verify_r65.py`, `verify_r64.py`,
  `verify_r63.py`, `build_rev7.py`, `repro70.py` / `repro70.json` and the earlier `repro*`,
  `head63.md`, `head64.md`, `s1_64.txt`, `s1_68.txt`, `s1_70.txt`, `doc_part1..6.md`.

**Nothing in this kit has been applied to the store.** The apostrophe normalisation is drafted and
verified, not applied; it belongs in the next store revision carrying these edits and must be
recorded in §0 as a non-substantive normalisation.

**Internal working draft. Not a Division of Legislative Services bill. Not legally cleared by
counsel — [MOO-187](/MOO/issues/MOO-187), [MOO-209](/MOO/issues/MOO-209) and
[MOO-214](/MOO/issues/MOO-214) are internal adversarial passes, expressly not legal advice, and
revision 8's four re-cut texts and four held candidates have not been read adversarially at all.
Not legally sufficient for introduction.**
