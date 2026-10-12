# MOO-170 — serial chaining of Edit 3's retention, bounded addendum to the MOO-163 price

**Internal working draft material. Not a DLS bill. Not reviewed by counsel. Pre-decisional.**

Bounded addendum to [MOO-163](/MOO/issues/MOO-163). The MOO-163 baseline is reused, not
re-derived, and the authorised narrow clause (vi) basis is not re-opened. No drafting is
proposed here; the cap text is the Policy Director's to take or leave.

## The costing question, in one sentence

Taking as given (from pass 18's F-6, MOO-166) that the retention sentence Edit 3 amends
carries neither of the tolling sentence's two limits — so a second or subsequent request
starts another 30 days and there is no aggregate ceiling — does serial chaining of that
retention move the bound, the displacement figure, or the $0 central estimate that
MOO-163 reported for the 48-month pilot?

Unit of analysis: one member's effective queue-ordering date, over a cohort, per
48-month pilot. Time horizon: the pilot, 1,440 days.

## Headline

**No. The $204,000 bound survives chaining unchanged, it is still lapse rather than
cost, and the central estimate is $0 at every chain length including an unbounded one.**

The bound is **analytic, not simulated**, and the chain does not break the derivation.
MOO-163 §3's bound quantifies over *any* vector of ordering dates against a fixed
$3,000,000 pool; a chain of any length is another such vector. There is no `k` in the
derivation. This is the paragraph the Policy Director said would close questions 1 and 2,
and it does.

What chaining *does* change is **who moves, not how much money moves**. On two of the
three displacement branches the count of members whose funded-or-wait-listed outcome
changes rises about 21× (0.14 → 2.80 members over 48 months) — and the two rising
branches rise for opposite reasons. That figure is still inside the resolution of the
inputs, but by a narrower margin than at MOO-163, and it is reported in members rather
than dollars.

| Question | Answer |
| --- | --- |
| 1. Bound still analytic under chaining? | **Yes.** Derivation untouched; it already quantified over all orderings. |
| 2. If not, what is the bound? | Unchanged: **\|Δ\| < $204,000 over 48 months, lapse not cost.** Largest value observed anywhere in the sweep: $332, 0.163% of the bound. |
| 3. Does displacement move? | **It moves, it rises, it still stays below resolution.** 0.14 → 2.80 members mean; gated branch flat at 0.00. Narrower margin than before. |
| 4. A chain length at which the central estimate stops being $0? | **No. Only if the cap binds** — and that turns on MOO-49's clause (vi) reading, not on the chain. A chain cannot add demand. |

### One sentence for the Editor

Serial chaining of Edit 3's uncapped 30-day filing-date retention does not move the
MOO-163 price: the bound stays at |Δ| < $204k over the 48-month pilot and stays lapse
rather than cost, because the bound quantifies over all queue orderings of a fixed cohort
and a chain of any length is only another ordering, so the central estimate remains $0 at
every chain length including an unbounded one — the central estimate stops being $0 only
if the cap binds, which turns on MOO-49's clause (vi) reading and not on the chain.

## Files

| File | What it is |
| --- | --- |
| `moo170_chain_inputs.py` | **The assumption register.** Sections E–G: only what is new to MOO-170. Every other input is imported unchanged from `../moo163-retention-endpoint/moo163_inputs.py`. |
| `moo170_chain.py` | The model. Sections 1–8 plus a self-test, printed in full. |
| `out_moo170_run.txt` | Captured output of the run of record. |
| `README_MOO170.md` | This file. |

## How to rerun

```
cd moo170-chain-addendum
python3 moo170_chain.py            # ~1 minute, prints the whole addendum
python3 moo170_chain.py > out_moo170_run.txt
```

Requires `numpy`. Deterministic: seeds `20261012` (headline) and `20261013` (seed test)
are in the register. The script reproduces **every** number in this README and in the
issue comment; nothing is quoted from a prior run.

## Base, vintage, and what is handed to me

- **MOO-163 baseline, unchanged.** Cohort construction, subsidies, filing dates, the
  $3,000,000 D 2 cap, the $170,000 per-election ceiling, the 1.20 contingency load, the
  `strict_stop` / `skip_ahead` queue disciplines and the 20,000-draw convention are all
  imported. The addendum does not edit them.
- **The statutory reading is handed to me, not derived.** That the retention sentence
  carries no clause (i) and no clause (ii) comes from the Policy Director via pass 18's
  F-6. Whether that reading is right is Statutory Researcher's. If the limits do reach
  retention after all, the chain collapses to k = 1 with a 120-day ceiling and MOO-163
  stands unmodified — the favourable direction. This addendum prices the adverse one.
- **Who bears it is already mapped.** MOO-125 maps the subdivision D 5 waiting-list
  applicant as cost-bearer; the party is not re-established here.
- Retrieval date for every Paperclip-internal source: 12 October 2026.

## Sensitivity — what controls the answer, and what does not

**Nothing in this addendum is sensitive to a chain-geometry input.** `CHAIN_LINK_DAYS`
(33 / 40 / 120 days, analyst judgment) and `CHAIN_CONTINUATION_RATE` (10–70%, analyst
judgment) are both disposed of by construction: the sweep evaluates k = 1 … 44 *and* the
unbounded limit exactly, which brackets every continuation rate including 1.00, and
Section 5 shows the saturated cell is identical at all three link lengths. Link length
decides only how fast the chain saturates, not what it saturates at.

The two things that do control the answer are the same two that controlled MOO-163, and
both are upstream of this issue:

1. **Whether the cap binds at all** — MOO-49's clause (vi) reading. Narrow gives the
   counts used here and the cap does not bind at the central estimate (67.4%); broad
   gives ~130 members and it binds in every scenario. A 10% move in the cohort count
   moves the high-cell answer far more than a 10× move in chain length does. **Broad
   clause (vi) requires repricing with or without the chain. The chain is not the
   trigger; MOO-49 is.**
2. **Which displacement construction D 4 / D 5 requires** — Statutory Researcher's. Worth
   under $200 at MOO-163; chaining raises its stake, in members rather than dollars.

## Verification performed

- **Self-test on the disclosed noise floor.** A `$0.01` floor is applied to deltas and
  verdicts, because the `back_of_queue_gated` branch produces an *identical* allocation
  across chain lengths and its paired delta is float residue (−4.7e−10, one ULP on a
  $2.47M sum), which MOO-163's `|Δ| > 1.96·se` test otherwise reports as a finding. The
  self-test proves the floor is inert: every cell it reclassifies has flips 0/0, i.e. the
  same members funded in the same order. Largest residue suppressed is under a billionth
  of a dollar; the smallest substantive figure reported anywhere is $4.
- **Bridge check onto MOO-163's k = 1 high cell.** k = 1 *is* the card (k-ii) endpoint
  MOO-163 priced. It lands in the same low-hundreds-of-dollars, not-distinguishable-from-
  zero regime on the same cohort, with matching flip counts. It reproduces to within
  Monte Carlo error, **not to the dollar** — the RNG consumption order differs — and it
  is not offered as re-ratifying MOO-163's exact cell values.
- **Internal consistency, analytic vs simulated.** The lemmas predict every swept cell
  lands strictly inside $204k. Largest observed: $332, 0.163% of the bound. **Agreement.**
  Falsifiable: a cell outside the bound would have refuted the analytic claim.
- **Multiple-comparison accounting.** 2 of the 54 swept cells cross the 1.96·se line, at
  a threshold that produces 2.7 such cells by chance. Both are named in Section 4 rather
  than omitted; the larger is $309, 0.15% of the bound, and changes no answer.
- **Seed test at the long chain.** Reported as it came out, not as it was hoped:
  **this run did not reproduce MOO-163's sign flip.** All 12 long-chain cells kept their
  sign across two seeds. What it does show is weaker — every cell sits inside its own 95%
  MC interval and the seed-to-seed swing reaches $421, larger than half the printed
  deltas — so the long-chain dollar figures are no better resolved than MOO-163's, but
  they have **not** been shown to be exactly zero. That is precisely why question 2 is
  answered with the analytic bound, which uses none of these draws.

## Known limitations, all stated

- **One disclosed change to the MOO-163 code path.** `back_of_queue` is split into
  `back_of_queue_asis` (MOO-163's implementation verbatim; faithful at k = 1, an artefact
  at large k because it relegates a member who never lost the retained date) and
  `back_of_queue_gated` (relegation conditioned on retention ending before exhaustion).
  Both are reported. Section 2 quantifies what the split costs at k = 1 — it is within
  Monte Carlo error there, which is what makes the generalisation safe to introduce.
- **No external quantitative anchor exists.** MOO-71 §3 establishes there is no published
  count of § 51.1-142.2 military purchases, so there is nothing to scale from another
  state or a prior Virginia fiscal impact statement. The external check available is a
  *convention* check against Virginia fiscal-note practice on capped, self-executing
  programmes, and it validates the $0 line only. **It cannot validate the lapse deltas or
  the flip counts**, which are internal to this model.
- **The administrative channel is reported, not priced into a line.** A chain is more
  requests, which MOO-163 did not cover. Even at k = 44 and the high seek rate the volume
  is 8–33 Board requests per year on top of an existing 90-day M 2 process — below the
  threshold at which a Virginia fiscal note reports a figure rather than "can be absorbed
  with existing resources". Section 7.
- **Not priced here, by role:** legal exposure from an uncapped chainable entitlement
  (Red Team / Counsel Reviewer); whether successive requests about successive waiting-list
  placements are "the same determination" (Statutory Researcher — the sweep spans k = 1 to
  unbounded regardless, so no answer is assumed); whether to take the cap (Policy
  Director).
