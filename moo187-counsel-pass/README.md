# MOO-187 — red-team / counsel pass on the MOO-164 act-versus-notice cut

**Internal risk analysis. Not legal advice, not a legal opinion the organization can rely on, and
nothing here states or implies that counsel has cleared the proposal. Pre-decisional and internal.**

- `moo187.md` — the **first pass**, on document revision 2 against store revision 62. 18 findings
  (0 fatal, 7 serious, 6 moderate, 5 minor) and 11 null results. Issue document
  [`moo187-counsel-pass`](/MOO/issues/MOO-187#document-moo187-counsel-pass).
- `check187.py` — reproduces every count the first pass relies on. Counts **whole-document**, matching
  the convention the cut's §7.2 used at the time.
- `moo187-addendum.md` — the **second pass**, on document revision 4 against store revision 64 and the
  apply kit at `60f18ca`: §13, §14, candidates 164-7 and 164-8. 8 further findings (0 fatal, 4 serious,
  2 moderate, 2 minor) and 8 further null results. Issue document
  [`moo187-addendum`](/MOO/issues/MOO-187#document-moo187-addendum).
- `check187_r63.py` — reproduces every count the addendum relies on. Counts over **enacted §1 only**,
  which is the convention the cut's §13.1 adopts and the right one; finding **F21** is about the fact
  that the committed `verify_r6.py` does not follow it and fails on the current base.

**Running total: 26 findings — 0 fatal, 11 serious, 8 moderate, 7 minor — and 19 null results.** The
single most serious is **F1** (Edit 164-1's 48-day cap is itself act-keyed, so M 2's tolling endpoint is
not closed and §0.1's headline claim is false). The most serious of the second pass is **F19** (candidate
164-7 carries one of MOO-141 Edit 1's two trigger limbs, so it ends the member's tolling without
reaching the sentence that gives her a retirement date when tolling ends).

## To reproduce

Fetch the `bill-text-s8` document body from [MOO-42](/MOO/issues/MOO-42) to `bill.md`, then:

```
python3 check187.py bill.md        # first pass, whole-document counts
python3 check187_r63.py bill.md    # addendum, counts over enacted §1 only
```

It asserts the review's definite results and prints the rest: the 19 occurrences enumerated, the
twentieth-occurrence hunt, the six MOO-164 anchors and three MOO-141 anchors on the live base, the
+490 delta, the §7.2 table before and after both patches (**`acts upon` after both patches is 9, not
the 7 §7.2 predicts** — finding F2), the nine surviving `acts upon` with Edit 164-1 accounting for two
of them (finding F1), the five `shall act upon` duties and their commencements (finding F6), the seven
`period allowed` phrases (finding F13), the eight `pending` uses, the four apostrophes, and the
`no later than` count.

**The base this review ran against is store revision 62**, not the revision 61 the cut was built on.
That matters for finding F7 and for nothing else: the six anchors still resolve exactly once and the
delta is still +490 on revision 62, on revision 62 with the MOO-141 patch at revision 5, and with it at
revision 6. The team's own `verify_r6.py` was run unmodified against the live base with 0 failures.

**No team file was modified and nothing was written to the store.**
