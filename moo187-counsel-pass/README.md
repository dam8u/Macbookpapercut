# MOO-187 — red-team / counsel pass on the MOO-164 act-versus-notice cut

**Internal risk analysis. Not legal advice, not a legal opinion the organization can rely on, and
nothing here states or implies that counsel has cleared the proposal. Pre-decisional and internal.**

- `moo187.md` — the review. 18 findings (0 fatal, 7 serious, 6 moderate, 5 minor) and 11 null results.
  Also posted as the issue document [`moo187-counsel-pass`](/MOO/issues/MOO-187#document-moo187-counsel-pass).
- `check187.py` — reproduces every count the review relies on.

## To reproduce

Fetch the `bill-text-s8` document body from [MOO-42](/MOO/issues/MOO-42) to `bill.md`, then:

```
python3 check187.py bill.md
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
