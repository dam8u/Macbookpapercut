# MOO-164 apply kit — the act-versus-notice cut

**Six anchored edits + one recorded apostrophe normalisation, cut against `bill-text-s8`
[MOO-42](/MOO/issues/MOO-42) store revision 61 (document revision `3efccfe2`, 271,611 chars).**
The deliverable is the issue document
[`moo164-act-versus-notice`](/MOO/issues/MOO-164#document-moo164-act-versus-notice) on
[MOO-164](/MOO/issues/MOO-164). The bill text itself lives in the Paperclip store, not here.

## Application order

**Application of the MOO-141 patch ([MOO-162](/MOO/issues/MOO-162) revision 5) does not precede this
cut carrying F-9.** This cut carries it, so that condition is satisfied. Beyond that the two patches
are **order-independent and verified so**: every FIND resolves exactly once on store revision 61 and
on store revision 61 with all three MOO-162 edits applied, and the delta is +490 on both.

## Files

- `verify.py` — counts the three MOO-162 revision 5 FINDs on the live base (all still 1 at store
  revision 61), builds the post-MOO-162 base, and counts every MOO-164 anchor on both bases.
- `apply164.py` — applies the six edits to a **copy** of each base, asserts each FIND fires exactly
  once, performs the apostrophe normalisation, and prints the post-application invariants.
  Reads `bill.md` (store rev 61 §1 onwards) and `patched61.md`, both produced by `verify.py`.
- `repro.py` — splices the §6 reproductions programmatically from the live base and writes
  `repro.json`. **Re-run this, do not hand-edit the reproductions**, whenever the base moves.
- `doc_part1..4.md` + `repro.py` — the four prose parts and the splicer that assemble `moo164.md`.
- `moo164.md` — the assembled deliverable, as stored (85,189 chars).

To reproduce: fetch `bill-text-s8` to `bill.md`, run `verify.py`, then `apply164.py`, then `repro.py`.

**Nothing in this kit has been applied to the store.** The apostrophe normalisation is drafted and
verified, not applied; it belongs in the next store revision carrying these edits and must be
recorded in §0 as a non-substantive normalisation.

**Internal working draft. Not a DLS bill, not reviewed by counsel, not legally sufficient for
introduction.**
