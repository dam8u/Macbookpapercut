# MOO-217 — the subdivision D 1 extension channel, priced

**Fiscal & Impact Modeler. 13 October 2026. Pre-decisional and internal. Not a DLS bill.
Not reviewed by counsel.**

The deliverable is `../moo217-d1-channel-priced.md`. This directory holds the model it
reproduces.

| file | what it is |
|---|---|
| `moo217_inputs.py` | **The assumption register.** Sections A–F. MOO-163's register is imported unchanged and re-exported, so the reader can see which of its levers this issue leans on without any value being copied. MOO-204's non-qualifying-retirement share is imported as a value with its source. |
| `moo217_d1_channel.py` | The model. Sections 0–11, each printing its own working, plus a self-test. |
| `out_moo217_run.txt` | Captured transcript of the run of record. |

## How to rerun

```bash
cd moo217-d1-extension
python3 moo217_d1_channel.py            # ~1s, exit 0
python3 moo217_d1_channel.py > out_moo217_run.txt
```

**Standard library only** — no numpy. **No random draw anywhere**, so there is no Monte
Carlo error on any figure and every threshold is a division. Verified byte-identical
across two consecutive runs and across a clean start with `__pycache__` removed. Exits
non-zero if any assertion fails.

## What it reads, and what it never writes

- Reads `../moo141-rev72/s1.txt` — the enacted §1 extract (134,012 characters) of
  `bill-text-s8` at **store revision 72**, the cut MOO-141 revision 9 is written against.
  The character count is asserted, so a moved store **fails the run** rather than drifting.
- Imports `../moo163-retention-endpoint/moo163_inputs.py` unchanged.
- Writes nothing outside this directory. Confirmed by `git status` and asserted in §11.

## The four answers, in one line each

1. **Board no-act rate — unobtainable** (no denominator exists); swept 0–50% and the
   answer reported as a **threshold in it**. Later-date filing rate — **bounded from text**
   at 5–60%, analyst judgment. A **third** input is also needed and MOO-204 already had it.
2. **MOO-163 and MOO-170 are both silent.** MOO-170's analytic ground survives the
   question asked and does **not reach this channel** — it quantifies over orderings and
   bounds *lapse*; this channel moves *settle versus release*.
3. **Property 5 holds; "fiscally inert" does not follow from it.** Edit 4 is inert on D 1
   and *therefore* lands inside subdivision G 4 clause (iii), where a notice not given
   converts a release into a settlement the Commonwealth pays under subsection N.
4. **Attaching a D 1 extension costs $0 on the appropriation line** — it substitutes for
   the G 4 route. The exposure does not disappear if the option is declined; **it
   relocates onto Edit 4.**

Central figure: **$11,000** over the 48-month pilot at an illustrative 10% no-act rate
(range $610–$110,000). Central materiality threshold **94%**. Local cost **$0**, **no
unfunded mandate on localities**.
