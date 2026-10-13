# MOO-204 — candidate 164-9 priced

**Owner: Fiscal & Impact Modeler. 12 October 2026. Pre-decisional and internal.
Not a DLS bill. Not reviewed by counsel.**

## The costing question, in one sentence

Over the 48-month pilot, what does candidate 164-9 — replacing Edit 164-1's cap so
that M 2's tolling endpoint is measured from the later of the Board's acting and the
expiration of the period allowed by this section for acting, rather than from the
Board's acting — cost the Commonwealth, the trust, a locality and the member, and
does it move MOO-140's C2 answer, the live D 4 / D 5 retention figures, the
third-party displacement, or any link in MOO-170's chain?

- **Unit of analysis:** one reconsideration request, and one affected member.
- **Horizon:** the 48-month pilot, FY2027–FY2030. **Every count is members per
  48 months, not members per year.**

## Headline

**$0 on every state line, in every fiscal year, as identities and not as estimates.**
The movement is **+60 days** at the central estimate (endpoint day 55 → day 115),
**0 days** where the Board decides and gives notice promptly, and **+72 days** at the
worst lawful timing. The **300-day card (h) bound does not move**, MOO-140's C2 answer
does not change, and **its published figure does not change either**. Candidate 164-9
**lengthens no link in MOO-170's chain** and moves **no** live retention or displacement
figure. The member bears **$184** at the central estimate as the time value of a
deferral the chapter pays no interest on, range **$0 to $454**; aggregate over the pilot
**$58**, under **$1,300** in the high case. **One new adverse fact, and it is not a
dollar:** the retention's coverage of the tolling endpoint falls from at least +72 days
to +12 days on MOO-141's facts, and to between 0 and −18 days at the worst timing.

## Files

| File | What it is |
|---|---|
| `moo204_inputs.py` | **The assumption register.** Every number the model uses, once, with unit, source and direction of error. Sections A (statutory/drafted), B (inherited live figures, cited as given), C (allowance and rate), D (the one input with no source), E (model controls). |
| `moo204_164_9.py` | The model. Twelve sections, each printing its own working. §0 is a lock gate — nothing below runs if a published day figure fails to reproduce. |
| `out_moo204_run.txt` | Full transcript of the authorised run, 652 lines. |
| `README_MOO204.md` | This file. |

## How to rerun

```bash
cd moo204-164-9
python3 moo204_164_9.py > out_moo204_run.txt 2>&1   # ~70s, exit 0 only if all 14 locks pass
```

Requires `numpy` only (1.26.4 used). It imports `moo163-retention-endpoint` and
`moo170-chain-addendum` from the sibling directories **unchanged** and does not edit
them; it overrides MOO-170's `RETENTION_DAYS_PER_REQUEST` to the board's 120 days in
memory for the §6 re-run only. Deterministic: seed `20261012`, fixed in the register.
**Verified byte-identical across two consecutive runs.**

## Base and vintage

| Input | Vintage | Retrieved |
|---|---|---|
| MOO-164 `moo164-act-versus-notice` | document revision `4fcf01f0` (revision 5) | 12 Oct 2026 |
| MOO-164 `moo164-policy-director-disposition` | document revision `ca64c88e` | 12 Oct 2026 |
| MOO-140 `c2-zero-allowance-answer` | document revision `492158b7` | 12 Oct 2026 |
| MOO-177 `moo177-amendment-record` | document revision `47bdf124` | 12 Oct 2026 |
| MOO-179 `moo179-cap-decision.md` (workspace) | commit `38cc0b9` | 12 Oct 2026 |
| MOO-170 `moo170-chaining-addendum` | document revision `fbb624c6` | 12 Oct 2026 |
| m8-a enacted in M 2 clause (ii) | **store revision 68** | 12 Oct 2026 |
| DHRM salary, VRS multipliers, VRS discount rate | published engine register `moo183-cost-per-participant/engine/inputs.py` (DHRM 6/30/2024; VRS valuation 6/30/2025) | 12 Oct 2026 |
| § 30-19.1:7 | law.lis.virginia.gov, last amended 2010 c. 410 | 12 Oct 2026 |

**Counts are not re-derived here.** MOO-71's participant counts (18, range 9 to 30 over
48 months) are an input, cited as given, and they carry MOO-71's own condition: they are
conditional on the **narrow clause (vi) reading**, open at MOO-49. **That condition
travels with every number in this model.**

## What the model does and does not decide

**Does not decide, and must not be read as deciding:** what the statutory text produces.
The tolling mechanics, the C2 route through G 2's notice floor, the two classes of
request, and F-6's clause (i)/(ii) findings were all handed to me by the Policy
Director, MOO-164 and MOO-170 and are used as given. I did not read the statute for
myself.

**One construction question the model cannot resolve, so it reports both branches**
(register section E):

- `CLAUSE_II_BRANCHES` — does M 2 clause (ii)'s 120-day aggregate clip a **single**
  request's endpoint (the branch MOO-164 §2.2 states), or bound only the sum across
  requests?

**The dollars are identical on both branches.** The branches differ only in whether the
retention coverage margin bottoms out at 0 days or at −18 days, and that is Statutory
Researcher's question, not mine.

## Verification performed

1. **14 locks, run as a gate.** Every published day figure is re-derived from the
   register: MOO-177's day 37, day 127 and +42; MOO-164 §2.2's day 55 and the 48 = 15 +
   3 + 30 derivation; §15.4's day 115 and day 138; card (f)'s 78; the 18 + 60 split; the
   300-day card (h) bound with m8-a enacted; MOO-140's 240. **All 14 pass.** The script
   exits 1 if any fails.
2. **MOO-179 §2.2's published displacement reproduced exactly.** The §6 re-run of
   MOO-170's sweep at the board's 120-day retention gives **2.800 mean and 11 in the
   worst draw** against MOO-179's published "2.80 ... with 11 members in the worst
   draw", and `back_of_queue_gated` flat at 0.00. This is what makes §6 load-bearing
   rather than assertion.
3. **The days-dimension invariance re-tested at 164-9's own figures.** MOO-179 §2.3
   found the days dimension carries no fiscal warrant at any figure, on links of 33, 40
   and 120 days. §6 re-runs it at **115 and 138** — candidate 164-9's endpoint and its
   outer bound — on a shared draw set. **Every saturated cell identical across all five
   link lengths.**
4. **The coverage margin scanned, not assumed.** §2 scans every first-action day from 0
   to 120 at the worst lawful decision and notice, for both classes of request and both
   branches, so the worst margin is found rather than guessed.
5. **Internal consistency check on the dollars.** The same PV formula applied to the
   window C2 already publishes gives $209; candidate 164-9 adds $184, +88% of a loss
   already in MOO-140 §4's memo-ready text. Reported as an internal check, not an
   external one.
6. **Reproducibility.** Two consecutive runs diffed byte-identical.

## Known limitations, all stated

- **One input has no source at all**: `NON_QUALIFYING_RETIREMENT_SHARE`, the fraction of
  funded participants who reach a G 2 cutback determination. No authorised count of that
  class exists in this project — MOO-71's funnel counts eligibility, take-up and the
  three statutory refusals, not members who elect, are funded and then fail to retire
  qualifying. It scales the aggregate linearly and nothing else, and §4 prints a
  **ceiling row** showing what the arithmetic does if every funded participant were in
  the class.
- **Two further judgment inputs**: service years at retirement, and the low and high legs
  of the member discount rate. The central rate leg is sourced — 6.75%, the VRS assumed
  rate and the statutory interest rate the chapter uses for refunded-service purchases.
- **No external count anchor and no comparable prior fiscal impact statement exist.**
  MOO-71 §3 establishes that no published count of § 51.1-142.2 purchases exists. §8's
  check is therefore a **convention** check against the test § 30-19.1:7 actually sets,
  which validates the three $0 state lines and the no-mandate finding and **cannot**
  validate the member-side time value. Stated as such rather than dressed up.
- **The $0 administrative line is conditional on candidate 164-10.** 164-9's cap is
  measured from the *expiration* of M 2's 90-day period, and that period has no stated
  commencement in the enacted text. 164-10 supplies one and the Policy Director's
  disposition §10 takes it. If 164-10 were dropped, 164-9's cap would not be computable
  from the text and the administrative line would not be $0.
- **The dominant unresolved driver is upstream and unchanged**: MOO-49's clause (vi)
  reading. Broad gives roughly 130 members, the cap binds in every scenario, and
  MOO-163, MOO-170, MOO-179 and this issue reopen together. Candidate 164-9 does not
  change that and adds no trigger of its own.
