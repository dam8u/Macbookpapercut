# MOO-176 — revision 6 of the MOO-141 patch (Edit 3 re-cut to 120 days)

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed by
counsel. Pre-decisional and internal.**

- `moo176-revision-6.md` — the deliverable, identical to the issue document
  `moo176-revision-6` on MOO-176.
- `cut176.py` — re-resolves the three FIND anchors on the live `bill-text-s8` body, applies all
  three edits to a **copy**, and re-runs every count in §4.1. Nothing is written to the store.
- `build_reproductions.py` — re-splices the eight §3 reproductions from the live body and applies
  the patch's own bold/strikethrough markup.

Both scripts read the live base from `$PAPERCLIP_RUN_SCRATCH_DIR/base.md`, which is the body of
`bill-text-s8` as fetched at the time of the cut (store revision 61, document revision
`3efccfe2-8332-4f4a-82ba-a9347141287f`, 271,611 characters, enacted §1 117,980 characters).

**Verified at store revision 61:** three anchors resolve exactly once in the document and in §1;
Edit 3 is +15 characters; the patch is +698 in both the document and enacted §1; `<u>`/`</u>` balance
60/60; seven of eight reproductions byte-identical to revision 5, M 2 changed (+494) and replaced.
