# moo211-cures — [MOO-211](/MOO/issues/MOO-211)'s counsel pass disposed, six cures drafted and none enacted

Deliverable: [`moo208-cures`](/MOO/issues/MOO-208#document-moo208-cures) on
[MOO-208](/MOO/issues/MOO-208). **Store revision 72 is record only: §1 is byte-for-byte what store
revision 71 left it, proved by diff.**

| File | What it does |
|---|---|
| `cures.py` | The six cures as FIND/READ data, re-priced. **Enacts nothing.** Also lists the six record corrections |
| `verify_cures.py` | Re-resolves all six on the live store, re-counts every figure MOO-211 asserts, and proves the markup point by applying each cure and re-counting the tags |
| `rec72.py` · `rec_patches72.py` · `rec_s0_72.md` · `rec_s8_72.md` | Store revision 72, record only: nine in-place corrections, the §0 narrative and the §8 status note |
| `items72.py` | §7 items 133 and 135 corrected — item 135 is the card the Director acts from and both its figures were wrong |
| `build_pack.py` · `moo208-cures.md` | The deliverable, with D 1, M 2 and enactment 3 reproduced in full as they would read |

```
python3 verify_cures.py
python3 rec72.py --dry-run && python3 rec72.py
python3 items72.py --dry-run && python3 items72.py
python3 build_pack.py
```

Enacted: `bill-text-s8` store revision **72**, document revision `368f5e41` (number 92), 502,586
characters, headroom 21,702. Item list revision `97486e31` (number 15).

## The three things worth re-running

**All six cures still anchor, and the base had moved again.** Counsel verified on store revision
70; **store revision 71 landed first and moved §1 by +1,455**, to 134,012. Every one of the six
FIND strings still resolves **1× inside the §1 slice**, and **all nineteen counts MOO-211 asserts
about §1 re-count exactly.** Nothing in the pass was spent.

**Five of counsel's six figures do not hold, and three of its cures would have damaged the text.**
Counsel wrote `<u></u>` tags into five cures. **S1, S3, S5 and M4 sit inside an open `<u>` span**
— M 2 and D 1 are wholly new language — so the tags would have **nested**, taking §1 from 62/62 to
63/63. **S2 and M3 sit in enactment clause 3, which carries zero `<u>` tags in 6,176 characters.**
So **no cure carries a tag** and all six leave the counts at 62/62. Corrected: **S1 +115, S2 +118,
S3 +127, S5 +310, M3 +95 (counsel said +94), M4 +42. Total +807.**

**A matching character delta is a checksum and this record called it a proof.** §5.47 check 10 is
corrected (R5). `rec72.py` is the first kit to carry the replacement rule: its decisive
post-condition is a **diff** showing §1 after is identical to §1 before, not a delta assertion.
Two offsetting changes pass a delta, and so does a zero-character change — and store revision 70
contains one.

## Two findings of my own, beyond counsel's

- **Counsel's "F3 residue" does not exist**, and nor does the version of it this record carried.
  Item 7 carries **one advisory and two propositions of law**, so the series carries **eight
  propositions of law and one advisory**, not six and one. The drafted scope *"every matter other
  than the advice"* reaches all eight and excepts the one. **No renumbering, no three-way split.**
- **Extending that to §7 item 135 is mine and not counsel's.** Item 135 recorded as a defect that
  neither form of the M 2 cure reaches item 7's other two propositions. **That is the right answer,
  not a defect:** those two are propositions of law, and widening the exception would remove
  subsection M review from two propositions nobody proposed to remove it from. Flagged for the
  Director rather than fixed silently.

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or
by DLS, not legally sufficient for introduction. Pre-decisional and internal.**
