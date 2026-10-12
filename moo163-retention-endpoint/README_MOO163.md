# MOO-163 — the D 4 / D 5 filing-date retention endpoint, priced

**Owner: Fiscal & Impact Modeler. 12 October 2026. Pre-decisional and internal.
Not a DLS bill. Not reviewed by counsel.**

## The costing question, in one sentence

Over the 48-month pilot, does moving the day on which a reconsideration applicant loses
her retained filing date — from the Board's first action `F`, to `F + 30` (card (k-ii),
the board's choice of 12 October 2026), to the Board's decision `D` — change the dollars
reserved and settled against subdivision D 2's $3,000,000 cumulative cap, or the number
of members who receive a certified subsidy rather than subsection B standard-cost rights?

- **Unit of analysis:** one certified subsidy reservation.
- **Horizon:** the 48-month pilot. **Every count in this model is members per 48 months,
  not members per year.**

## Headline

**No fiscal impact. The release gate clears.** $0 on the appropriation line under all
three readings; $0 administrative; $0 at the central estimate in actual draw against the
cap, because the cap does not bind and queue position therefore decides nothing. The
effect is non-zero only at high take-up, and there it is a sign-indeterminate change in
**lapse** bounded by $204,000, touching a fraction of one member over the whole pilot.

## Files

| File | What it is |
|---|---|
| `moo163_inputs.py` | **The assumption register.** Every number the model uses, once, with unit, source and direction of error. Sections A (statutory, read off the live text), B (authorised counts from MOO-71, cited as given), C (analyst judgment, labelled as such), D (model controls). |
| `moo163_retention.py` | The model. Eight sections, each printing its own working. |
| `out_moo163_run.txt` | Full transcript of the authorised run. |
| `README_MOO163.md` | This file. |

## How to rerun

```bash
cd moo163-retention-endpoint
python3 moo163_retention.py          # ~30s, exit 0
```

Requires `numpy` only. Deterministic: seed `20261012`, fixed in the register. **Verified
byte-identical across two consecutive runs** — there is no wall-clock line in the output.

## Base and vintage

| Input | Vintage | Retrieved |
|---|---|---|
| `bill-text-s8` (MOO-42) | document revision **73**, 506,992 characters | 12 Oct 2026 |
| MOO-71 `authorised-participant-count` | revision **2** | 12 Oct 2026 |
| MOO-141 `moo141-pendency-answer` | revision **4** | 12 Oct 2026 |

The statutory parameters in register section A were read off revision 73 directly:
the $3,000,000 aggregate cap and $170,000 per-election ceiling (D 2), the `[20]`%
contingency charged inside the cap (D 3), the 90-day decision deadline and the 15-day
follow-on (M 2).

**Counts are not re-derived here.** MOO-71's authorised participant count (18, range
9 to 30) and cap utilisation are inputs to this issue, cited as given, and they carry
MOO-71's own condition: they are conditional on the **narrow clause (vi) reading**, open
at MOO-49. That condition travels with every number in this model.

## What the model does and does not decide

**Does not decide, and must not be read as deciding:** which of the three readings the
text actually produces. That is Statutory Researcher's. The three readings were handed
to the model by the Policy Director and it prices *between* them.

**Two construction questions the model cannot resolve, so it reports both branches of
each** (register section D):

- `QUEUE_DISCIPLINE` — on D 5, does the Board stop at the first application that does not
  fit, or wait-list it and continue down the order?
- `DISPLACEMENT_MODELS` — once retention ends, does the applicant go to the back of the
  queue or drop out of the subsidised queue entirely?

All four combinations are reported in Section 4. **The conclusion is the same in all
four**, which is why the open construction questions do not block the gate.

## Verification performed

1. **Bridge check onto the authorised input.** The model reproduces MOO-71's own
   corrected high-take-up utilisation: 132.2% × 0.8497 = **112.3%**, against MOO-71 §3's
   "near 112%". Reproduced.
2. **Independent cross-check on the mean certified subsidy.** Backing the mean out of
   MOO-71's *stated* 79.3% utilisation gives $110,569 against MOO-48's Pathway A mean of
   $110,042 — **0.5% apart**. This confirms the contingency is handled on the same
   footing in both and that the cap arithmetic here matches MOO-71's. (The *corrected*
   mean is $94k, 14.6% below — reported in full in Section 2, and **not** called
   agreement. The gap is the 12-month rung correction working as MOO-71 §3 says it
   should.)
3. **Monte Carlo error reported, not hidden.** Section 4 prints a paired 95% Monte Carlo
   interval beside every delta and an explicit distinguishable-from-zero verdict. Seven
   of eight high-scenario cells are **not** distinguishable from zero.
4. **Seed-sign test.** Section 5 recomputes a Section 4 quantity on a fresh draw sequence
   and gets the **opposite sign** (−$83 → +$67). A quantity whose sign is a property of
   the seed is zero. This is the single most informative check in the model.
5. **Reproducibility.** Two consecutive runs diffed byte-identical.

## Known limitations, all stated

- **Three of the inputs are analyst judgment with no source**: the reconsideration-seek
  rate, the within-cohort subsidy dispersion (CV), and the first-action / decision day
  distributions. All three are labelled in register section C with the range I would
  defend. Section 5 shows the result is **not** sensitive to any of them.
- **No external count anchor exists.** MOO-71 §3 establishes that no published count of
  § 51.1-142.2 military purchases exists. Section 8's sanity check is therefore a
  *convention* check against Virginia fiscal-note practice on capped programmes, not a
  quantitative one. It validates the $0 line and cannot validate the lapse deltas. Stated
  as such.
- **The `[20]`% contingency is still a drafting bracket** in the live text. A higher rate
  makes the cap bind sooner and would make this provision matter *more*. At the central
  estimate there is headroom from 67.4% to 100%, so the bracket would have to move a long
  way to change the conclusion.
- **The dominant unresolved driver is upstream of this issue**: the clause (vi) reading at
  MOO-49. Narrow gives the counts used here; broad gives ~130 members, on which the cap
  binds in every scenario and **this provision would need repricing**. That is the one
  trigger that should bring MOO-163 back.
