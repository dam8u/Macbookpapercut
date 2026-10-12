# Store revision 61 apply kit — MOO-97

**Applied.** `bill-text-s8` store revision 61 (document revision `3efccfe2`, 271,611 chars) and
`bill-text-s8-item-list` item 128, both on [MOO-42](/MOO/issues/MOO-42). Record:
`moo161-disposition` on MOO-97. The bill text itself lives in the Paperclip store, not here.

## Files

- `gen_edits.py` — extracts every FIND as a live substring from a snapshot of the bill and builds
  each READ by sub-replacements that must each fire exactly once. Writes `edits.py`. **Re-run this,
  do not hand-edit `edits.py`**, whenever the base moves.
- `edits.py` — the thirteen generated substitutions for store revision 61 (kept as the record of
  exactly what was applied).
- `apply.py` — derives every label from the live bodies of BOTH documents, asserts every anchor
  unique, moves §8's oldest status note out, and writes in the order record -> item list -> bill.
  `python3 apply.py` is a dry run; `--write` writes.
- `content.py` / `patch_content.py` — the §0, §5, §6, §7-stub, §7-item and §8 commentary blocks.
- `build_record.py` + `rec_head.md` / `rec_mid.md` / `rec_tail.md` — assembles and PUTs
  `moo161-disposition`; §2 and §5 are generated from `edits.py` and the written body.
- `make_review.py` + `rt_head.md` — creates the bounded counsel-pass issue (MOO-169).
- `card.py` — the Policy Director's checkbox card (seven drafted answers).
- `comment.md` — the heartbeat comment as posted.
- `out-labels.json` — the labels and counts this revision was written with.

To reproduce: fetch `bill-text-s8` §1 to `bill.md`, run `gen_edits.py`, then `apply.py`.

**Internal working draft. Not a DLS bill, not reviewed by DLS, not legally sufficient for introduction.**
