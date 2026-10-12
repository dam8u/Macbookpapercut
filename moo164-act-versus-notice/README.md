# MOO-164 apply kit — the act-versus-notice cut

**Re-verified at store revision 63 (document revision 79, 320,665 chars). `verify_r63.py` is the
current check and `repro63.py` is the current splicer; the store-revision-61 versions are retained as
the record of the original cut.** Store revisions 62 and 63 rewrote D 1, G 4 and M 2 — three of the
provisions reproduced at §6 — without disturbing a single anchor, which is why the reproductions are
re-spliced and never hand-carried. Every count in `verify_r63.py` is taken over **enacted §1 only**:
store revisions 62 and 63 quote three of these anchor strings in the §0 narrative, so a
whole-document count now returns 2 or 3 for those three.

**Six anchored edits + one recorded apostrophe normalisation, cut against `bill-text-s8`
[MOO-42](/MOO/issues/MOO-42) store revision 61 (document revision `3efccfe2`, 271,611 chars).**
The deliverable is the issue document
[`moo164-act-versus-notice`](/MOO/issues/MOO-164#document-moo164-act-versus-notice) on
[MOO-164](/MOO/issues/MOO-164). The bill text itself lives in the Paperclip store, not here.

## Application order

**Application of the MOO-141 patch does not precede this cut carrying F-9.** This cut carries it, so
that condition is satisfied. Beyond that the two patches are **order-independent and verified so on
three bases**: store revision 61 as it stands, store revision 61 with the MOO-141 patch at
**revision 5** (Edit 3 at 30 days), and with it at **revision 6** (Edit 3 at 120 days, from
[MOO-176](/MOO/issues/MOO-176), which landed mid-cut). Eighteen counts, all 1; delta **+490** on all
three. Run `verify_r6.py` to reproduce.

## Files

- `verify_r6.py` — **the current check.** Builds both MOO-141-patch bases (revision 5 and revision 6),
  counts every MOO-164 anchor and every held candidate on all three bases, and asserts the +490 delta.
- `verify.py` — the first two-base version, kept as the record of what was run before revision 6 landed.
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

## Two candidates added at §13, neither applied

- **164-7** (item 130) — M 2, two sentences, +583 chars: a request denied by operation of item 124's
  enacted sentences is deemed acted upon on the date of the denial, **for period purposes only**, in
  MOO-141 Edit 1's own words and with Edit 1's own saving clause. Without it, four act-keyed endpoints
  run without end where the Board never acts, and Edit 164-1's 48-day cap cannot engage.
- **164-8** — D 1, one sentence, +485 chars: the member may file or replace her § 51.1-153 notice
  within 30 days where a later notice is given after her single filing window has closed.

Both FIND strings are asserted at count 1 in `verify_r63.py`. Neither is applied; both are questions
for the Policy Director at §13.12.
