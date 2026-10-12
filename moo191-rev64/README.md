# MOO-191 apply kit — F10's designation-review advisory, cut as store revision 65

**Applied to the store.** One anchored substitution of 137 characters in **subdivision D 1 of
§ 51.1-142.4**, approved verbatim by the Policy Director at
[MOO-188](/MOO/issues/MOO-188) §3.3 and commissioned at §8 on [MOO-191](/MOO/issues/MOO-191).
The bill text lives in the Paperclip store, not here:
[`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8). The deliverable is
[`moo191-advisory-cut`](/MOO/issues/MOO-191#document-moo191-advisory-cut).

**Commissioned as store revision 63; cut as store revision 65.** The label moved twice while the cut
was being prepared — 63 was taken at 17:44 UTC by the §7 item 124 cut, 64 at 17:53 UTC by a
record-only revision — so `apply.py` derives every label from the live body and refuses to run if
the derived label is not the one the record prose was written for. **An anchor counted yesterday is
not an anchor, and a label derived ten minutes ago is not a label.**

## What was written

| Where | What |
|---|---|
| `bill-text-s8` §1 | the one substitution in subdivision D 1 (document revision 82) |
| `bill-text-s8` record | §0.0-65 narrative, §5.43 sweep, §6.0-65 drafter's note, §8 note; byline, §5/§6/§8 self-descriptions and the §7 pointer brought current |
| `bill-text-s8` title | corrected from *"store revision 65 — record only"*, inherited from store revision 64 (document revisions 83 and 84) |
| `bill-text-s8-item-list` | §7 item 129 answer (4) marked **answered and enacted, do not re-cut**; the other six untouched (document revision 9) |
| `moo191-advisory-cut` on MOO-191 | the deliverable — D 1 in full as amended, spliced from the live body |

## Files

- `edits.py` — the one bill edit (FIND/READ verbatim, the Director's words), plus `UNTOUCHED`: the
  nine anchors of other open cuts that are re-counted over §1 **after** the substitution.
- `rec_patches.py` — the record-layer patches. The byline is **not** here: store revision 64 left it
  reading *"store revision 63"*, so `apply.py` patches it from whatever the live byline says.
- `rec_s0.md`, `rec_s5.md`, `rec_s6.md`, `rec_s8.md` — the §0, §5, §6 and §8 record as inserted.
- `apply.py` — asserts every count before touching anything and every post-condition before writing:
  one changed §1 line, §1 delta exactly +137, §1 `<u>`/`</u>` still 60/60, no duplicate record
  heading, unique byline, the nine untouched anchors, and the eight vocabulary counts §5.43 states.
  `--dry-run` writes `out-body.md` and sends nothing.
- `items_patch.py` — the item-list marking. Record only; it answers nothing.
- `build_doc.py` + `doc_head.md` — assemble the deliverable, splicing subdivision D 1, the title line
  and the five enactment clauses from the live body. **Re-run it, do not hand-carry the
  reproduction**, whenever the base moves.

To reproduce: `python3 apply.py --dry-run`, `python3 items_patch.py --dry-run`,
`python3 build_doc.py --dry-run`. All three refuse to write if a count is off.

**Internal working draft. Not a DLS bill, not cleared by counsel or DLS, not legally sufficient for
introduction.**
