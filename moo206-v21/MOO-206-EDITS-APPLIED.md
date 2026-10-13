# MOO-206's two edits, as applied to `v2.1` — read this before freezing the folder

**Editor, 12 October 2026, 20:52 local.** This folder is **open**. There is deliberately **no
`VERSION.md`** in it, so rule 1 of the file-output convention has not frozen it, `CURRENT` still
points at `v2.0`, and the `VERSIONS.md` row is untouched. Whoever freezes `v2.1` owns `VERSION.md`,
the `VERSIONS.md` row and the `CURRENT` pointer. **This note is not that record** — it is the list
of what MOO-206 put in, so the freeze record is accurate and nothing is inserted twice.

Authority: the Policy Director's answers at MOO-205, applied under MOO-206, with the `v2.1` cut
confirmed on the MOO-206 thread.

---

## 1. C2 — the zero-allowance window, carried into the risk section

| Where | What |
|---|---|
| `08-markdown-sources/07-risk-register.md` **§3.1** | The **full approved text**, under the dateline *"verified at store revision 68 (12 October 2026)"*, with the MOO-164 caveat as the paragraph immediately after the figure, the sources line, and item 46 stated **permissively** (*the bar does not apply*). |
| `08-markdown-sources/03-decision-memo.md` **§7** | **R-H (carry-through item C2)** — the memo-length form, with the figure and its mandatory condition in **one sentence**, the unbounded never-notice case, and a pointer to document 07 §3.1 for the full text and sources. The §7 lead-in now reads *"the four that would actually kill the bill, and one exposure in the drafted text that a committee will find"*. |

**One departure from verbatim, stated so it can be reversed in one edit.** The approved text's third
paragraph opens *"The provision has been repaired repeatedly and the memo should say so."* The four
words *"and the memo should say so"* are an instruction to the editor rather than a statement about
the bill, so document 07 prints *"The provision has been repaired repeatedly."* and then the
repairs. Nothing else was cut, softened or reordered.

**The approved text re-verified against the live bill before it was printed.** The bill moved to
**store revision 69** (13 October 2026) while MOO-206 was open. All five quotations in the approved
text still occur **exactly once** at revision 69; the string the Director struck — *"is not a
collection, offset, or withholding for the purposes of this section"* — still occurs **zero** times;
and subdivision G 2's refund sentence is unchanged. Revision 69's five substitutions are in
subdivision G 4 and subsections B and L. **G 4 is in C2's sources line**, so the dateline decision —
whether C2 is re-dated at 69 or stays at 68 — is the Policy Director's, and nothing in C2 is wrong
at 69 either way.

## 2. The cohort phrase — MOO-205 §3.5, applied per site

The register entry keys the form to the sentence, so the pass is per site and not one global
sentence. **Verbatim phrase: 17 uses, and every one of the ten documents carries it. Extended form:
5 sites. Sentences split: 2.** Banned phrase: 0. *"normal retirement"* as a short form: 0. No
*"only"* is bound to the route list, and neither § 51.1-155.1 B nor § 51.1-155.2 A is named
anywhere, so §7 item 47 stays the Director's to answer.

| Site | Document | Class | What changed |
|---|---|---|---|
| S1 | the shared headline block, **all nine** | 1 | the cohort behind the 18.4 count now reads the verbatim phrase |
| S2 | the shared headline block, **all nine** | 1 | *"4.74% of **that** cohort"* — a back-reference to S1 eight lines above |
| S3 | the shared headline block, **all nine** | — | **narrowed.** It read *"The cohort behind every figure in this package is the unreduced subdivision A 1 cohort…"*, which is **not true** of the figures this package labels on another basis — the Pathways A + B pair (1.50× / 61%), the full-cohort sensitivity baseline, and the superseded cohort in document 04 §13. It now carries that exception. |
| 01-a | one-page summary | 1 | the only cohort site in the document |
| 02-a | policy brief | 1 | the A + B cohort is named in the same cell, so the phrase goes in full |
| 02-b | policy brief | 2 | the *"One pathway only"* row now says what date the member must reach |
| 03-a | decision memo | 1 | the member-price pair |
| 03-b | decision memo | **3 — split** | test sentence takes the extended form, figure sentence takes the verbatim phrase |
| 04-a | fiscal analysis | 1 | the A + B cohort is named in the same note |
| 04-b | fiscal analysis | 1 | the retirement-deadline ladder's table caption |
| 04-c | fiscal analysis | 1 | the full-cohort sensitivity baseline is named in the same note |
| 05-a | drafting request | 2 | element 5, *Eligibility* |
| 06-a | questions and answers | **3 — split** | subsection C's bar, then the ceiling's 4.74% |
| 06-b | questions and answers | 2 | the windfall-channel bullet |

**Two editorial decisions in this pass, both reversible, both the Director's to overrule.**

1. **The verbatim phrase is written in full at the first class-1 site in each document, at any
   class-1 site that sits beside a differently-labelled cohort, and at any class-1 site carrying a
   headline figure. Other class-1 sites keep a back-reference** (*"that cohort"*, *"the cohort"*).
   The word *"cohort"* occurs 88 times across the ten documents of `v2.0`; writing the 14-word phrase at all of them
   would not be English. The alternative — the phrase in full at every class-1 site — is a
   one-command change.
2. **The extended form is introduced by *"which the bill defines as"*** at all five sites. Three of
   them sit next to the pre-existing words *"One pathway only"*, and without the descriptive lead-in
   the row can be read as *only* those routes — which is the expressio unius argument the Director
   reserved to themselves at §7 item 47.

**Where the extended form stands beside a figure it carries limit 2 verbatim** — *"Neither of those
two routes carries weight in the modelled distribution."* — at 03-b, 05-a and 06-a.

**Reproduced bill text was not touched.** `05-bill-drafting-request.md` reproduces the definitions of
*"qualifying retirement"* and *"unreduced retirement eligibility date"*, which name the routes in the
bill's own words. That is the bill speaking, not us describing it: no class, no edit.

## 3. Derived artifacts rebuilt from these sources

`01-sponsor-package-pdf` (ten PDFs) and `02-sponsor-package-docx` (ten DOCX) were rebuilt with
`10-build-tools/build.py` after the edits, and the sources were checksummed before and after the
build to confirm the renders match what is in `08-markdown-sources`. **The one-page summary is still
one page** on the PDF page tree. `09-zip-bundles` now holds
`vrs-legislative-package-v2.1-DRAFT.zip`; the `v2.0` zip was not carried into this folder.

## 4. What this pass did **not** do

- **No `VERSION.md`, no `VERSIONS.md` row, no `CURRENT` move.** The folder is open on purpose.
- **The other eleven C-series carry-through items — C1, C4, C5, C6, C12 to C18 — are still in no
  artifact.** Only C2 was authorised and only C2 is in.
- **No figure moved**, nothing was softened, and no caveat was dropped.

**Internal working draft material. This folder reproduces working bill text. Not a DLS bill, not
reviewed by counsel, pre-decisional and internal. Release is the Policy Director's decision.**
