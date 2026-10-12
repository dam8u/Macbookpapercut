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
- `check187_r65.py` — **the current check.** The addendum's **§7**: the re-verification at **store
  revision 65**, the twelfth base move and the first since revision 62 to land inside a provision this
  cut amends (MOO-191's 137-character advisory in **subdivision D 1**). 48 checks, **0 failures**. It
  isolates the change by proof rather than assertion, re-runs every invariant of the cut on the new
  base, re-tests the textual predicate of every live finding, and carries the one new finding, **F27**.

**Running total: 27 findings — 0 fatal, 11 serious, 9 moderate, 7 minor — and 19 null results.** The
single most serious is **F1** (Edit 164-1's 48-day cap is itself act-keyed, so M 2's tolling endpoint is
not closed and §0.1's headline claim is false). The most serious of the second pass is **F19** (candidate
164-7 carries one of MOO-141 Edit 1's two trigger limbs, so it ends the member's tolling without
reaching the sentence that gives her a retirement date when tolling ends). **F27** is §7's and is
against the base rather than the cut: MOO-191's advisory sits in D 1's *"shall also state"* series, so
omitting a sentence of exhortation is a reviewable failure that tolls under M 2 and, after option (d),
reaches circuit court.

## To reproduce

Fetch the `bill-text-s8` document body from [MOO-42](/MOO/issues/MOO-42) to `bill.md`, then:

```
python3 check187.py bill.md        # first pass, whole-document counts
python3 check187_r63.py bill.md    # addendum, counts over enacted §1 only
python3 check187_r65.py           # §7, reads head65.md (live) + head64.md (previous base)
```

It asserts the review's definite results and prints the rest: the 19 occurrences enumerated, the
twentieth-occurrence hunt, the six MOO-164 anchors and three MOO-141 anchors on the live base, the
+490 delta, the §7.2 table before and after both patches (**`acts upon` after both patches is 9, not
the 7 §7.2 predicts** — finding F2), the nine surviving `acts upon` with Edit 164-1 accounting for two
of them (finding F1), the five `shall act upon` duties and their commencements (finding F6), the seven
`period allowed` phrases (finding F13), the eight `pending` uses, the four apostrophes, and the
`no later than` count.

**The base has moved under this review three times.** The first pass ran against **store revision 62**,
not the revision 61 the cut was built on — that matters for finding F7 and for nothing else. The
addendum ran against **store revision 64**, where F7 is discharged. §7 re-verifies at **store
revision 65**. On every one of those bases the six anchors resolve exactly once, the five held
candidates resolve exactly once, the delta is **+490**, the classification is **21** and the
apostrophes are **four, all in G 4** — bare, with the MOO-141 patch at revision 5, and with it at
revision 6. **No base move has required a re-cut.** The team's own `verify_r6.py` was run unmodified
against store revision 62 with 0 failures and against store revision 63 with an `AssertionError`,
which is finding **F21** — it counts whole-document, and the §0 narrative now quotes four of these
strings.

**No team file was modified and nothing was written to the store.**
