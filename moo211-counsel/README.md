# moo211-counsel — counsel pass on store revision 70 of `bill-text-s8`

Deliverable: [`moo211-counsel`](/MOO/issues/MOO-211#document-moo211-counsel) on MOO-211, plus the
findings comment on MOO-211. **5 serious, 5 moderate, 3 minor, 18 null results.**

Verified on document revision `d4a67d3d` (store revision 70, number 89) against base `3b9ac270`
(store revision 69, number 88), both fetched from the store at the start of the pass. Every count is
taken inside the §1 slice (`## 1. The bill` to the next second-level heading).

| File | What it is |
|---|---|
| `moo211-counsel.md` | The pass as published to the issue document |
| `comment.md` | The findings comment as posted |
| `bill.md` · `s1.md` | Live store revision 70 body, and its §1 slice (132,557 incl. trailing newline) |
| `base.md` · `base-s1.md` | Store revision 69 body and §1 slice (131,923) — fetched, not reconstructed |
| `g4.txt` | Subdivision G 4 extracted for the notice and death-computation reads |
| `items.md` | `bill-text-s8-item-list` revision `9a0543af` (items 133 and 135) |
| `moo208cut.md` | The MOO-208 deliverable |
| `bill_raw.json` · `this-comments.json` | Raw API responses |

**Nothing in the store was edited.** The only store writes this pass made are the `moo211-counsel`
issue document and the findings comment, both on MOO-211.

## The two verifications worth re-running

**The §1 diff — the proof the record's character-delta checksum is not.** Base 131,923 → live 132,557,
+634, and **exactly two lines of §1 differ**: line 4 (the title line, +44) and line 115 (subdivision
D 1, +590). A matching delta is a checksum — two offsetting changes pass it, and so does a
zero-character change, which this revision contains (F4's relocation of the `and`). The diff is a
proof. Recommend it becomes the standing rule.

**Two pending kits re-resolved against revision 70, neither on §5.47's list.**

- **MOO-164 revision 6** — all **eleven** FIND strings extracted from `moo164_rev6.md` and counted on
  both bases: **1× before, 1× after**, including Edits 164-5 and 164-8, both inside subdivision D 1.
- **MOO-141 re-cut** — `moo141-rev68-recut/verify_r69.py` run **unmodified** against the live body:
  **ALL CHECKS PASS**.

```
python3 moo141-rev68-recut/verify_r69.py moo211-counsel/bill.md
```

**Internal risk analysis. Not legal advice. Not cleared by counsel or by DLS. Pre-decisional and internal.**
