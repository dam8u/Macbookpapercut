# moo208-composite — the Policy Director's composite, cut as store revision 70

The disposition at [MOO-191](/MOO/issues/MOO-191) commissioned at [MOO-208](/MOO/issues/MOO-208):
**six substitutions as one revision.** F1, F2 (D2b), F3 (D3c conformed), F4, F6, F9 and F8's title
cure T2. **F5 held, the acknowledgment form not drafted. F7 not cut, its words re-scoped.**

**Enacted.** `bill-text-s8` store revision **70** — document revision `d4a67d3d`, number 89,
515,219 characters, §1 **132,557 (+634)**. Base: store revision **69**, document revision
`3b9ac270`, §1 131,923. Item list revision `9a0543af`, number 13: §7 item 133 re-scoped, §7 item
135 opened. Retained-record document revision `7f3e3d81`, number 11.

| File | What it does |
|---|---|
| `composite.py` | The apply kit. Fetches the live base, demonstrates the D3c/D9 sequencing hazard, applies the six substitutions with every anchor re-counted **inside the §1 slice at the moment it is applied**, applies the record layer and the forced rotation, asserts every post-condition, writes the retained-record document first and the bill second, verifies both from the returned JSON. Aborts before writing on a dead anchor or a failed post-condition |
| `rotate70.py` | The §5 retention rotation §0.1 sets: §5.38 and §5.39 out verbatim, stubs in. **Forced, not discretionary** — see below |
| `rec_s0_70.md` · `rec_s5_47.md` · `rec_s6_70.md` · `rec_s8_70.md` | The §0 narrative, the §5 cross-reference sweep, the §6 drafter's note, the §8 status block |
| `rec_patches70.py` | Eight in-place record corrections, each marked, none rewritten away |
| `items70.py` | §7 item 133 re-scoped on the Director's direction; §7 item 135 opened with the M 2 cure drafted in two forms and enacted nowhere |
| `build_redline.py` | The two-layer redline of subdivision D 1 and the title line, built by reversing the substitutions out of the **live** text and verified by stripping back to it character for character |
| `build_cut.py` · `moo208-cut.md` | The MOO-208 deliverable |

```
python3 composite.py --dry-run && python3 composite.py
python3 items70.py --dry-run && python3 items70.py
python3 build_redline.py && python3 build_cut.py
```

## Three things that are not in the commission and are in the record

1. **Serious — F3 does not close the subsection M channel.** M 2's first sentence reaches *"a
   failure of the Board to state in a certification or notice a matter this section requires to be
   stated in it"* on its own terms, and its clock expressly contemplates another provision giving
   *"a longer or later period"*. **D 1's sentence extends subsection M; it does not constitute it**,
   so the exception withdraws only the extension — and the extension it withdraws is the survivor's
   subdivision G 4-notice clock. **No cure inside D 1 can work.** Drafted in M 2 at §7 item 135 and
   **not enacted**: it opens a provision the commission did not open.
2. **The F3 residue is wider than the Director's statement of it**, and creates an asymmetry with
   the re-scoped item 133: misstating item 7's other two propositions would be unreached while
   omitting them stays reviewable. Strict scoping to the six propositions needs the series
   designated (i) to (vii) — a renumbering the commission forbade.
3. **[MOO-176](/MOO/issues/MOO-176) revision 6's Edit 1 anchor is dead, and this revision did not
   kill it** (0× before and after; Edits 2 and 3 are 1× before and after). The provision was widened
   to *"that statement, notice, or certification"* after that revision was written. Re-anchored
   string at §5.47 direction 2 check 9. **Not re-cut** — out of scope.

## Two corrections to the commission itself

- **The §1 post-condition could not be met as stated.** The Director required §1 at **+590** on the
  footing that substitution 6 landed *"outside §1"*. The bill's title line sits under `### Title`,
  which is **inside** §1 as §1 is bounded in that document, so §1's measured movement is **+634**.
  The kit asserts the corrected delta and would have aborted on the stated one. §6.0-70 item 9.
- **The rotation was forced.** With its record layer the document landed at **527,893** against the
  store's **524,288** ceiling and could not be written at all. §5.38 and §5.39 are moved verbatim on
  the rotation §0.1 sets, which the §5 paragraph has named as next since store revision 58. **Only
  the §5 half was performed; §6.0-59 and §6.0-60 are next.** The document closes at about **9,000**
  characters of headroom.

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by
DLS, not legally sufficient for introduction. Pre-decisional and internal.**
