# MOO-212 — the `v2.1` freeze gate: the scripts, and what each one reported

**Editor, 13 October 2026.** The Policy Director's MOO-206 decision document set five conditions for
the `v2.1` freeze. This folder is the build record: every check is a script, run against the files
rather than against notes, exiting non-zero on a miss. The frozen folder itself is
`/Users/davidmoody/AgentCreated/v2.1`, and `v2.1/VERSION.md` is the freeze record.

**Internal working draft material. These scripts read working bill text. Not a DLS bill, not
reviewed by counsel, pre-decisional and internal. Release is the Policy Director's decision.**

---

## The revision this folder was frozen at

| | |
|---|---|
| Live bill document | `bill-text-s8` on MOO-42 |
| Paperclip document revision | **90** |
| Revision id | `399b2402-829e-434b-8a25-4b9339932151` |
| Bill byline | **store revision 71 · 13 October 2026** |

**The bill moved twice during the pass** — 69 → 70 (the MOO-208 composite) and 70 → 71 — and once
more minutes after the freeze, to **72, which is record-only: section 1 of the bill document is
byte-identical between 71 and 72**, and both the surface verification and the block comparison were
re-run against 72 and pass unchanged. The folder is dated at 71 because 71 is the revision it was
cut against. Nothing was re-dated before it was re-checked.

## The scripts, in the order they were run

| Script | What it does | What it reported |
|---|---|---|
| `fetch.py` | pulls the live bill document and records its revision id and byline | store revision 71, document revision 90 |
| `verify_surface.py` | every quotation of the bill in the ten documents counted inside § 51.1-142.4 at the live revision; plus eleven counted claims and three strings the package says do **not** occur | **9 quotations hold; 0 fail; 11 of 11 counted claims pass; 3 withdrawn strings at zero**. Ten further quoted strings are listed with the reason each is not the bill's words |
| `blocks.py` | document 05 §4's reproduction, block by block, against the live text | **0 of 98 blocks divergent** (2 divergent at revision 70, 7 at revision 71, before re-transcription) |
| `retranscribe.py` | re-transcribes every divergent block, matched to exactly one live block, replacement lifted out of the live document | 7 blocks re-transcribed at revision 71 |
| `retranscribe_d1.py` | the first pass's single-block version, kept for the record | subdivision D 1 re-transcribed at revision 70 |
| `sweep_liftable.py` | the liftability guard on cohort back-references | **11 occurrences cured in 9 table rows across 6 documents**; the two protected sites asserted intact |
| `fix_leadin.py` | *"which the bill defines as"* → *"under the bill,"*, and the definitions note once per document | **5 lead-ins changed across 4 documents**; note carried once each |
| `set_datelines.py` | the dateline sweep, **gated** on `verify_surface.py` and `blocks.py` passing in the same run against the same live file | **29 datelines set to store revision 71**; historical references to 69 and 70 protected by name |
| `install_renders.py` | installs the thirty artifacts, checksum-matches the sources, rebuilds and compares the zip | ten PDFs, ten DOCX, one-pager one page, **zip 72 entries, zero mismatches** |

Two checks outside this folder were re-run unchanged: the MOO-72 release checks
(`moo72-v21-apply/verify_v21.py`) at **22 of 22 pass**, and `shasum -c` against the regenerated
`MANIFEST-v2.1.sha256` at **76 of 76 artifacts matching**.

## Reproducing it

```sh
python3 fetch.py bill-text-s8 live.md     # writes live.md and live-meta.json
python3 verify_surface.py live.md
python3 blocks.py live.md
python3 retranscribe.py live.md           # report only; --apply to re-transcribe
python3 set_datelines.py live.md <rev>
python3 install_renders.py <build-root>
```

The bill snapshots themselves are not committed — they are 500 KB each and the live document is the
source of truth. `live-meta.json`, `live71-meta.json` and `live72-meta.json` record the revision id
and length of each one that was used, so a later reader can tell which state a result came from.

The renders were built with `v2.1/10-build-tools/build.py`, which expects a root containing `src/`
(the ten markdown sources plus `assets/`) and `tools/` (`build.py`, `printpdf.mjs`), and writes to
`build/pdf` and `build/docx`. `install_renders.py` copies from there into the package.

## The one thing referred rather than decided

`07-risk-register.md`'s **R1 / F1 / F2** row reads *"the cohort was rebuilt monthly from membership
history with the pathways made mutually exclusive."* It **is** a table row, so on the guard it is
liftable; but it describes how the model's cohort was constructed rather than naming the cohort
behind a figure, so it may be no class at all. **The Policy Director reserved the classification, so
it is reported and unchanged.** A sweep of every cohort back-reference in the ten documents found no
other liftable site — the rest are prose, list items, or the shared headline quote-block.
