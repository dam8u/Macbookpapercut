# MOO-164 apply kit — the act-versus-notice cut, **revision 6**

**Current check: `verify_r69_v6.py` (base `bill69.md`). Current splicer: `repro68.py`. Current
applier: `apply164.py`. There is exactly one of each.** Everything else in this directory is
superseded and is named as such below.

> ## ⚠ `verify_r68_v6.py` IS SUPERSEDED FOR TWO REASONS, NEITHER OF THEM A CHANGE TO THIS CUT
>
> 1. **The base moved to store revision 69** — document revision 88, whole document **482,941**,
>    enacted §1 **131,923**. Revision 69 enacted [MOO-189](/MOO/issues/MOO-189)'s answers.
> 2. **Its `E1_R` fixture was stale.** It carried MOO-141 Edit 1's saving *without* the express
>    exception. [MOO-141](/MOO/issues/MOO-141) re-cut Edit 1 at store revision 69 so that its saving
>    carries 164-7's exception, drafted for subsection A. `verify_r69_v6.py` lifts that text from
>    `moo141-rev68-recut/verify_r69.py` and **cross-checks it** — the MOO-141 patch delta over §1 must
>    come out at **+847**, MOO-141's own published figure, or the check fails.
>
> **Revision 6's text does not change.** 164-7 keeps its exception exactly as cut; Edit 1 was conformed
> to it, not the other way round. The eleven edits and both decisions are byte-identical.

> ## ⚠ THE PATCH IS **ELEVEN** EDITS AT REVISION 6, AND THE DELTA IS **+2,551**
>
> The Policy Director's disposition promoted five held candidates to applied text: **164-7** (carrying
> F19's limb (B)), **164-7-B** (folded into 164-7 as its deeming sentence), **164-8**, **164-10**,
> **164-11**, and **(c-2)** as the new **164-12**. **Candidate 164-9 stays HELD for
> [MOO-204](/MOO/issues/MOO-204) and the edit number 164-9 is reserved, not reused. Candidate (c-1) is
> retired and must not be applied.**
>
> Revision 5's figures were six edits and **+642**. Anything in this directory that still says +642 or
> +490 is a superseded file, not a disagreement.

> ## ⚠ APPLY EVERY FIND INSIDE ENACTED §1 ONLY
>
> From store revision 62 the §0 revision narrative of `bill-text-s8` quotes anchor strings. At store
> revision 68, **five of the eleven FINDs occur more than once whole-document** — 164-10's occurs
> **four** times. **A whole-document find-and-replace will corrupt the revision record.** `apply164.py`
> slices §1 before substituting and asserts afterwards that the head and tail are byte-identical. This
> is [MOO-187](/MOO/issues/MOO-187) finding **F21**, and it is the finding most likely to cause actual
> damage.

> ## ⚠ MOO-141 EDIT 1's BROKEN ANCHOR IS **REPAIRED, BY MOO-141** — AND ITS TEXT HAS CHANGED
>
> Store revision 68 re-cast subsection A's three-day sentence: it is now confined to mailing
> (*"where the Board mails a written statement, notice, or certification"*) and the triplet replaces
> *"that statement or notice"*, so **MOO-141 Edit 1's FIND string resolved 0 times.**
> **MOO-141 re-cut it at store revision 69**, and in the same re-cut **conformed Edit 1's saving clause
> to 164-7's express exception**, drafted for subsection A. The dead string is still kept as
> `E1_F_R65_DEAD` and asserted at **0** so the break stays visible. Edits 2 and 3 still resolve exactly
> once. **MOO-141 now carries its own ordering constraint: its Edit 2 must be applied in the same cut
> as its Edit 1**, because the exception's descriptor resolves twice until Edit 2 consumes the
> occurrence in the definition. Nothing in that reaches this cut's anchors.
>
> **All eleven MOO-164 anchors resolve exactly once at store revision 69**, on all three bases, with
> the identical **+2,551** delta. `verify_r69_v6.py`: **0 failures.**

**Deliverable:** the issue document
[`moo164-act-versus-notice`](/MOO/issues/MOO-164#document-moo164-act-versus-notice) on
[MOO-164](/MOO/issues/MOO-164). The bill text lives in the Paperclip store, not here.

## Base

Re-verified at **store revision 69** (document revision 88; whole document 482,941 characters;
**enacted §1 131,923**). **The base has moved fourteen times under this cut.**

Revision 6 was cut at store revision 68 (enacted §1 131,066). Revision 69 changed **three** provisions
in enacted §1, counted by a structural diff of the two bodies and not assumed:

| Provision | What revision 69 did | In §6's reproductions? |
|---|---|---|
| subsection **B** | took in the *"No person whom the definition of 'eligible member' … excludes"* sentence | no |
| subsection **L** | gave that sentence up — L is now the Dillon's-Rule sentence alone | no |
| subdivision **G 4** | the retirement-before-death carve-out, and the § 51.1-162 B benefit conditioned on identity of payees | **yes** |

So **§6's G 4 reproduction is stale for the seventh time**, behind anchors that all still resolve
exactly once. Re-splice by `repro68.py`, **by content and not by line index**, in the next cut.
**The other seven reproductions (A, the definition, D 1, G 2, M 1, M 2, M 3) are unaffected at
revision 69.** Nothing in the G 4 change creates or moves a period keyed to the Board's acting or to
notice: *"no later than"* is still **74** in §1 and the verb census is still **21**, both counted.

## Application order

**Application of the MOO-141 patch does not precede this cut carrying F-9.** This cut carries it, so that
condition is satisfied. Beyond that the two patches are **order-independent**, verified on three bases:
store revision 69 as it stands, with the MOO-141 patch carrying Edit 3 at **30 days**, and with it
carrying Edit 3 at **120 days**. Eleven anchors, all 1; delta **+2,551** on all three.

Stated exactly, so the claim is checkable: **the eleven-edit form is verified at store revisions 68
and 69** — two store bases, three patch bases each. The six-edit form was verified the same way at
store revisions 63, 64 and 65. Order-independence of the two patches, and indifference to the 30/120
answer, hold at every one of them.

**The apostrophe normalisation runs AFTER the eleven substitutions, not before.**

## The eleven edits

| Edit | Site | Delta |
|---|---|---|
| 164-1 | M 2, the tolling endpoint | +233 |
| 164-2 | G 2, the 120-day exception | +366 |
| 164-3 | M 2 clause (ii) | +24 |
| 164-4 | the definition, R-5 | +1 |
| 164-5 | D 1, the lateness descriptor | +8 |
| 164-6 | G 4, the period formula | +10 |
| **164-7** | M 2, after the enacted denial sentence — the deemed act, two triggers + saving | **+1,153** |
| **164-8** | D 1, the filing vehicle | **+485** |
| **164-10** | M 2's 90-day duty, commencement | **+27** |
| **164-11** | M 2's expiry-notice sentence, conformed formula | **+24** |
| **164-12** | G 2, item 46's carve-out — this is candidate (c-2) | **+220** |
| | **total** | **+2,551** |

## Files

- `verify_r69_v6.py` — **the current check** (`python3 verify_r69_v6.py bill69.md`). Counts over
  enacted §1 only. Everything the revision-68 check did, plus the MOO-141 fixture cross-check at
  **+847** and the **two savings' symmetry**: after both patches there are two savings, each carrying
  an express exception, one naming *"this subsection"* (164-7, in M 2) and one naming *"subsection M"*
  (Edit 1, in subsection A), and exactly **one** referent for the shared descriptor survives outside
  the two exceptions — M 2's 15-day duty, which is what both exceptions are about. **0 failures.**
- `verify_r68_v6.py` — **superseded**, for the two reasons in the box at the top. Counts over
  enacted §1 only. Eleven anchors on three
  bases, the +2,551 delta, the named MOO-141 Edit 1 break, the verb census, the formula census at five
  sites, the five ordering invariants the promotions create (164-5 before 164-8; 164-7's two
  *"preceding sentence"* references; M 2's sentence order against D 1's ordinal reference; item 131's
  antecedent; (c-1)'s FIND unamended), candidate 164-9's FIND against the **applied** text, the
  apostrophe count **and** its confinement to G 4, and the 300-day arithmetic. Exits non-zero if any of
  them moves.
- `repro68.py` → `repro68.json` — **the current splicer** for the §6 reproductions. Locates every
  provision by content. **Re-run this, do not hand-edit the reproductions**, whenever the base moves.
- `apply164.py` — applies all **eleven** edits to a **copy**, §1 only, with the out-of-§1 byte-identity
  assertion, then performs the apostrophe normalisation.
- `moo164.md` — the assembled deliverable as stored (revision 6).
- `disposition-rev5.md` — the Policy Director's disposition that revision 6 folds in.
- **Superseded, kept only as the record of earlier runs:** `verify_r68.py` (the **six**-edit check at
  store revision 68 — the Director's own run), `verify_r65.py`, `verify_r63.py`, `verify_r64.py`,
  `repro65.py` / `repro65.json`, `repro63.py` / `repro63.json`, `repro.py`, `head63.md`, `head64.md`,
  `s1_64.txt`, `s1_68.txt`, `doc_part1..6.md`. **`verify_r6.py` and `verify.py` were deleted at
  revision 5** — they counted whole-document and hard-failed from store revision 63 on (F21).

## To reproduce

```
# fetch bill-text-s8 from MOO-42 to bill69.md, then:
python3 verify_r69_v6.py bill69.md   # 0 failures expected — the current check
python3 apply164.py bill69.md        # writes applied.md; asserts +2551 and out-of-§1 byte-identity
python3 repro68.py                   # the splicer; point it at the current base before re-reading §6
```

`bill.md` is the **store revision 68** base revision 6 was cut against, kept as the record.
`bill69.md` is the current base.

**Nothing in this kit has been applied to the store.** The apostrophe normalisation is drafted and
verified, not applied; it belongs in the next store revision carrying these edits and must be recorded
in §0 as a non-substantive normalisation.

## Held and retired, so nobody applies them by mistake

- **164-9 — HELD.** F1's five-word cap: *"48 days after the later of the Board's acting upon the request
  and the expiration of the period allowed by this section for acting upon the request."* It amends
  **Edit 164-1's own new text**, so its FIND resolves **0** times in the base and **1** in the applied
  text — both asserted. Priced at [MOO-204](/MOO/issues/MOO-204). **Do not apply without that answer.**
- **(c-1) — RETIRED.** Counsel's F9 makes it defective, not merely impolitic. **Do not apply.** The
  verifier asserts its FIND still resolves once **unamended**, which is how it proves Edit 164-12 leaves
  G 4 alone.
- **Card (i)'s 33-word confirming sentence — DECLINED.**
- **F11 — carried forward, not drafted.** For the next pass that opens the definition.

**Internal working draft. Not a Division of Legislative Services bill. Not legally cleared by
counsel — [MOO-187](/MOO/issues/MOO-187) is an internal adversarial pass, expressly not legal advice,
and the five edits promoted at revision 6 have not been reviewed as applied text at all. Not legally
sufficient for introduction.**
