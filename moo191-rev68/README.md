# moo191-rev68 — the MOO-195 disposition kit

Builds [`moo195-disposition`](/MOO/issues/MOO-191#document-moo195-disposition) on MOO-191: the
thirteen candidates that answer MOO-195's seven open findings, drafted word for word and **enacted
nowhere**. Nothing in this directory writes to the store.

| File | What it does |
|---|---|
| `candidates.py` | The thirteen candidates. Re-counts every FIND on the **live** base, in the document and in §1 separately, applies each to a scratch copy of §1, and reports the character movement, the `<u>`/`</u>` balance, the item count of the D 1 certification series and the position of the advisory in it. Exits non-zero on a dead anchor |
| `markdiff.py` | Word-level amendatory marking, and the assertions that each marking reconstructs **both** the live text and the post-edit text |
| `markup2.py` | The passages alone, for a quick read |
| `build_disposition.py` | Builds the disposition document |
| `apply68.py`, `items_patch68.py`, `rec_patches68.py`, `rec_s0_68.md`, `rec_s8_68.md` | The record-only apply kit for **store revision 68**, already applied |
| `markup.py`, `markup.md` | **Superseded.** Diffed character by character — `that the ~~membe~~<u>Boa</u>r~~ is~~<u>d</u> advise~~d~~<u>s the member</u>` — and printed D3a and D5 with no marking at all, its span logic having lost edits that cross a sentence boundary. Kept so the defect and its repair are both on the record |

```
python3 candidates.py          # anchors, counts, movement, series shape
python3 markup2.py             # the passages
python3 build_disposition.py   # the document
```

## Why the marking is not underline and strikethrough

Subdivision D 1 sits inside an open `<u>` run: § 51.1-142.4 is a new section, so it is new language
underlined end to end in the bill text, and the passage carries no marker of its own — asserted, 0
`<u>`, 0 `</u>` and 0 `~~` from the series' first word to the failure sentence's last. Underlining a
candidate's addition there would nest a marker inside a marker, and striking one would read as
language deleted from the **Code** rather than from the **draft**. Each candidate's own delta is
therefore marked `[ADDED: …]` / `[STRUCK: …]` against the draft, and the `<u>`/`</u>` balance is
reported for every candidate.

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by
DLS, not legally sufficient for introduction.**
