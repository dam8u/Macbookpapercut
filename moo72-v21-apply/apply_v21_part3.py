#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 3 — cross-reference repairs found by the sweep, and the
top-level README. Additive; run after parts 1 and 2."""
import os, sys
DST = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
ROOT = "/Users/davidmoody/AgentCreated/v2.1"

def rep_file(path, old, new, count=1, tag=""):
    s = open(path, encoding="utf-8").read()
    n = s.count(old)
    if n != count:
        sys.exit(f"MISS [{tag}] in {path}: expected {count}, found {n}\n---\n{old[:200]}\n---")
    open(path, "w", encoding="utf-8").write(s.replace(old, new))
    print(f"  {tag:34s} {os.path.basename(path)}")

# The exchange is §10 of document 04, not §9. v2.0 pointed at §9 in three places.
rep_file(os.path.join(DST, "04-fiscal-analysis.md"),
         "Its *label* was wrong and is corrected in §9. | — |",
         "Its *label* was wrong and is corrected in §10. | — |",
         tag="04-xref-s9-to-s10")

# The top-level README: version line, the section set, and the interactive-model reason.
rep_file(os.path.join(ROOT, "SPONSOR-PACKAGE-README.txt"),
"""Virginia Policy Lab · Version 2.0 · 12 October 2026
Amending Va. Code § 51.1-142.2 (purchase of prior active-duty military service)""",
"""Virginia Policy Lab · Version 2.1 · 13 October 2026
Amending Va. Code §§ 51.1-142.2 and 51.1-162 and adding § 51.1-142.4
(purchase of prior active-duty military service)""",
tag="readme-version-and-sections")
