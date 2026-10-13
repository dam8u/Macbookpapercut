# MOO-209 — counsel pass on MOO-164 revision 6

**Deliverable:** the findings comment on [MOO-209](/MOO/issues/MOO-209). `moo209.md` is the same text.

- `moo209.md` — the review. 16 findings (0 fatal, 5 serious, 5 moderate, 6 minor), 12 null results.
- `check209.py` — my own check. Tests the **propositions** revision 6 asserts, not the strings
  `verify_r68_v6.py` counts. `python3 check209.py` → ALL CHECKS PASS. Output in `out_check209.txt`.
- `bill.md` — byte copy of the kit's `bill.md` (store revision 68, unmodified).
- `apply164.py`, `verify_r68_v6.py` — byte copies of the kit's scripts, unmodified.
- `applied209.md` — **my** applied copy, built here by `apply164.py bill.md`. §1 delta **+2,551**.

**Why there is a local applied copy.** `moo164-act-versus-notice/applied.md` was overwritten by a
concurrent run at 20:43 while this review was in progress (it gained six `"preceding sentence"`
references where the eleven edits add three). Nothing in the kit was modified by this review. Every
count in `moo209.md` is taken against `applied209.md`.

Kit scripts re-run, all clean: `verify_r68_v6.py` 0 failures; `apply164.py` +2,551 with out-of-§1
byte-identity; `repro68.py` re-splices by content.

**Internal adversarial review. Not legal advice. Nothing here states or implies that counsel or the
Division of Legislative Services has cleared any part of this text. Pre-decisional and internal.**
