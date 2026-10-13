# MOO-207 — f11-authority working materials

- `f11-authority.md` — the deliverable (also posted as issue document `f11-authority` on MOO-207).
- `evidence-*.txt` — verbatim extracts from the Caselaw Access Project static corpus, produced by the scripts below.
- `scan2.py`, `case.py` — the extraction scripts. They read a local CAP corpus at `$PAPERCLIP_RUN_SCRATCH_DIR/cap/x`
  (Virginia Reports volumes 40–267) and `$PAPERCLIP_RUN_SCRATCH_DIR/se2d/x` (S.E.2d volumes 580–831, every
  volume CAP hosts in that range). The corpus itself is run-scoped scratch and is not committed.

Corpus source: `https://static.case.law/va/<vol>.zip`, `https://static.case.law/se2d/<vol>.zip`.
Statutory and constitutional text read at source on 12 October 2026 at law.lis.virginia.gov; 2001 Acts of
Assembly c. 804 read at legacylis.virginia.gov.

No team file was modified. Nothing here is legal advice.
