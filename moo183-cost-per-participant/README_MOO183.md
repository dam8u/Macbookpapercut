# MOO-183 — participant counts and cost per participant

## What is in here

| file | what it is |
|---|---|
| `moo183_inputs.py` | the assumption register and the lock set. Every number the model treats as given is here, once, with a unit, a source, a vintage and a direction of error. |
| `moo183_cpp.py` | the model. Locks first; nothing below the locks runs if one fails. |
| `engine/` | the **published** repaired (v2) engine, copied byte-for-byte from `AgentCreated/v1.0/05-model-code-and-data/python`. **Not modified by this issue.** |
| `out_moo183_run.txt` | the transcript of the run that produced every figure in the MOO-183 findings document. |
| `out_moo183_rows.csv` | 42 rows: 7 designs × 3 take-up cases × 2 retirement rungs, with participants, trust cost PV, cost per participant and mean acceleration. |
| `out_moo183_recommended_ladder.csv` | the recommended row on all six rungs plus the current-statutory-basis row. |

## How to rerun

```bash
cd moo183-cost-per-participant
python3 moo183_cpp.py > out_moo183_run.txt 2>&1   # ~11 min, exit 0 only if every §0 lock passes
```

Python 3.11, no third-party packages. Deterministic — no RNG anywhere in this run.

## What the locks prove

§0 re-runs the published engine for S1, S3, S5, S6, S8-i4, S8-i5 and S8-i6 at low,
central and high take-up and asserts it reproduces `out_v2_scenarios.csv` — the file
§5 of `model-s8-s9-repaired` prints and the §3 scoreboard scores on — to within 51
cents and 0.51 participants on both the count and the cost. All seven pass exactly.

So the participant counts in the findings document are not a new estimate of anything.
They are the denominators that were always inside the runs that produced the cost
figures the package already prints.

## The one thing to know before reading any figure

**The §3 scoreboard and the §3b coverage table are on a 6-month retirement deadline,
not on the authorised 12-month rung.** The 12-month rung was priced for the recommended
design (MOO-48 / MOO-85) and never for the scoreboard. This model reports both bases
for all seven designs and does not mix them in a single row. Choosing which basis the
§3b table prints is the Policy Director's call, and it has to be made for the whole
table at once.

Pre-decisional and internal. Not a VRS actuarial result. Nothing reliable beyond two
significant figures.
