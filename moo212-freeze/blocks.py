#!/usr/bin/env python3
"""MOO-212 — the document 05 block comparison, re-run against the live bill text.

Document 05 §4 reproduces the whole working draft: the title, the enacting clause, both
amended sections, the new section and all five enactment clauses. This script cuts that
reproduction into blocks, normalises each one the same way on both sides, and reports every
block that does not occur in section 1 of the live bill document.

Usage:  python3 blocks.py [live.md]
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC05 = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources/05-bill-drafting-request.md"
LIVE = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else "live.md")

# The reproduced span: from the "### Title" heading under §4 to the line before "## 5.".
START = "### Title\n"
END = "\n## 5. Open decisions in the draft"

# Blocks that are the package's own editorial voice inside the reproduced span, not bill text.
EDITORIAL = ("*Editorial note, not part of the bill.*",)


def norm(s):
    s = s.replace("<u>", "").replace("</u>", "")
    s = s.replace("~~", "")
    s = re.sub(r"\*+", "", s)
    s = s.replace(" ", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def blocks_of(text):
    out = []
    for raw in text.split("\n\n"):
        b = raw.strip()
        if not b or b == "---":
            continue
        if b.startswith("::: ") or b == ":::":
            continue
        out.append(b)
    return out


def main():
    doc = open(DOC05, encoding="utf-8").read()
    i = doc.index(START)
    j = doc.index(END, i)
    repro = doc[i:j]

    live = open(LIVE, encoding="utf-8").read()
    a = live.index("\n## 1. The bill")
    b = live.index("\n## 2. Section-by-section summary")
    s1 = norm(live[a:b])

    bs = blocks_of(repro)
    divergent = []
    editorial = 0
    for n, blk in enumerate(bs, 1):
        if blk.startswith(EDITORIAL):
            editorial += 1
            continue
        nb = norm(blk)
        if nb not in s1:
            divergent.append((n, nb))

    total = len(bs) - editorial
    print(f"{len(divergent)} of {total} blocks divergent "
          f"({editorial} editorial block(s) excluded, {len(bs)} blocks in the span)")
    for n, nb in divergent:
        print(f"\n--- block {n} ({len(nb)} chars) ---\n{nb[:700]}")
    return 1 if divergent else 0


if __name__ == "__main__":
    sys.exit(main())
