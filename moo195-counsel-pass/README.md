# MOO-195 — red-team / counsel pass on store revision 65's designation-review advisory

**Internal risk analysis. Not legal advice, not a legal opinion the organization can rely on, and
nothing here states or implies that counsel has cleared the proposal. Pre-decisional and internal.**

- `moo195.md` — the review. **11 findings (0 fatal, 3 serious, 5 moderate, 3 minor) and 11 null
  results.** Also posted as the issue document
  [`moo195-counsel-pass`](/MOO/issues/MOO-195#document-moo195-counsel-pass).
- `check195.py` — reproduces every count the review relies on. 33 checks, 0 failures.
- `fiscal195.py` — the load-bearing fiscal assumption, its test and its sensitivity.

## To reproduce

Fetch the `bill-text-s8` document body from [MOO-42](/MOO/issues/MOO-42) to `bill.md`, then:

```
python3 check195.py bill.md
python3 fiscal195.py
```

`check195.py` asserts §1's length (**121,576**) and `<u>`/`</u>` balance (**60 / 60**), the
advisory's **137** characters and single resolution in §1, every vocabulary count in §5.43
direction 1, the **seven**-item series structure, the **eight** short-form referents and that none
crosses the insertion point, the **ten** ordinal sentence references, and that each of the three
FIND strings handed to Drafting Specialist resolves exactly once in §1.

**The base this review ran against is store revision 65**, document revision `bc0576f5` — the
revision the issue names, fetched live rather than reconstructed.

## The three serious findings, in one line each

1. **F1** — the advisory, acted on by a member who has made *no* designation, destroys the
   § 51.1-162 B protection she already had. The 137 characters can cause the exact loss F10 exists
   to prevent.
2. **F2** — *"before completing payment"* is the wrong deadline. § 51.1-162 A permits redesignation
   until death; the window runs ~27 months on the act's own dials and the advisory closes at the
   first of its four legs. §6.0-65 item 5's claim that it is *"the whole window"* does not hold.
3. **F3** — the Director's question. **Answer: keep the J limb, drop the M limb.** M review's only
   possible output is a remand that cannot give the claimant anything (§ 2.2-4029); the J report
   gives the money committees the same fact at no litigation cost.

**No team file was modified and nothing was written to the store.** MOO-183's engine was not
re-run; `fiscal195.py` uses its published counts only.
