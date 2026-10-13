# MOO-199 — the authorised-basis model export, and the workforce exchange recomputed

## What is in here

| file | what it is |
|---|---|
| `moo199_inputs.py` | the assumption register and the lock set. Every number the model treats as given is here, once, with a unit, a source, a vintage and a direction of error. |
| `moo199_export.py` | the model. Locks first (§0); nothing below the locks runs if one fails. |
| `out_moo199_run.txt` | the transcript of the run that produced every figure in the findings document. |
| `out_moo199_model_data.json` | **the export.** The five blocks plus `meta`, `headline` and `sensitivity`. This is the deliverable for product 1. |
| `out_moo199_ladder.csv` | the authorised retirement-deadline ladder, six rungs. |
| `out_moo199_member_price_grid.csv` | 56 cells of the S8 member-price surface at 6.00%. |
| `out_moo199_interest_dial.csv` | the statutory-interest dial, 4.00%–7.00%. **Every row but 6.00% is `publication_restricted`.** |
| `out_moo199_cap_sweep.csv` | cap utilisation against the cap dial — the table the cap tab should be wired to. |
| `out_moo199_cap_admission.csv` | the cap as an admission rule on trust cost — the table that shows what the *wrong* wiring says. |
| `out_moo199_workforce_exchange.csv` | the three differential cases on the recommended design's anchor. |
| `out_moo199_workforce_by_rung.csv` | the exchange at all six rungs. The rung-invariance result. |
| `out_moo199_breakeven_grid.csv` | months of acceleration × replacement differential, net of the anchor. |

No engine code is in this folder. The model imports the published repaired (v2) engine
from `../moo183-cost-per-participant/engine/`, where MOO-183 committed it byte-for-byte.
**This issue modifies no line of it.**

## How to rerun

```bash
cd moo199-authorised-export
python3 moo199_export.py > out_moo199_run.txt 2>&1   # ~90s, exit 0 only if every §0 lock passes
```

Python 3.11, no third-party packages. Deterministic — no RNG anywhere in this run.

## What the locks prove (§0 of the transcript)

- **§0.1** The runner reproduces the published MOO-48 deadline ladder at **all six rungs ×
  three take-up levels** — trust cost PV to the cent, participants, and mean acceleration
  months to three decimals. 30 assertions, all exact.
- **§0.2** The same run reproduces the **authorised member-price pair**, 1.42× ANC and 43%
  of AEC (MOO-72 repair register item C).
- **§0.3** The authorised ladder's rung-12 value equals the MOO-32 v6 trust PV to 50 cents,
  and the cost per participant is $71,813 at low, central and high alike.
- **§0.4** Cap utilisation is `(1 + 20% contingency) × certified reserved ÷ cap`, and that
  formula reproduces the authorised **78.1872%** central and **130.31%** high to five
  decimal places. This is what pins the cap sweep down without a new run.
- **§0.5** The model reproduces **the exchange the documents actually print** — repaired S1
  at the 6-month rung, $64,678 per participant, 71% coverage. Without this lock the
  recomputation would have nothing to be a correction *of*.

## The one thing to know before reading any figure

**The engine that computes the authorised basis is not in this workspace.**
`AgentCreated/v2.0/05-model-code-and-data/model-current-12-october/moo32_v6_engine.py` is
not in this repository, not in any `instances/default/workspaces/*` tree, and a
filesystem-wide search for a directory named `AgentCreated` returns no match. Nor is
`make_model.py`.

So every block of the export carries a **quality** label and the export carries
`meta.key_binding_verified = false`:

| block | quality |
|---|---|
| retirement-deadline ladder | **authorised** (cited); low/high scaled by the take-up ratio |
| member-price grid | **measured**, and basis-invariant — option (c) and the no-advance bar are not terms of the member price |
| statutory-interest dial | **measured on the MOO-48 cohort**; authorised only at 6.00%; off-6.00% authorised PVs are *derived by anchored rescaling* |
| cap sweep (utilisation) | **measured** — exact arithmetic on the authorised figure set |
| cap sweep (admission) | **measured on the MOO-48 cohort**; shape only, not a level |
| workforce exchange | **measured**, on the MOO-48 cohort's salary and acceleration, with the direction of error stated |

The interest dial is the only block that **needs** the v6 engine to be authorised, and it
is the one block the v2.1 pass must re-measure with the folder in hand.

Pre-decisional and internal. Not a VRS actuarial result. Nothing reliable beyond two
significant figures. Release is the Policy Director's decision.
