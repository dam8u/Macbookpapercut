#!/usr/bin/env python3
"""MOO-212 item 3 — re-transcribe document 05's reproduced bill text at the live revision.

Not two named blocks: every divergent block, found by the block comparison rather than by
reading. Each divergent block is matched to exactly one block of the live bill by similarity,
the match must be unambiguous, and the replacement is lifted out of the live document rather
than retyped. Report-only unless --apply is given.

    python3 retranscribe.py live71.md            # report
    python3 retranscribe.py live71.md --apply     # report and re-transcribe
"""
import difflib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC05 = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources/05-bill-drafting-request.md"
START, END = "### Title\n", "\n## 5. Open decisions in the draft"
EDITORIAL = ("*Editorial note, not part of the bill.*",)
THRESHOLD = 0.80


def norm(s):
    s = s.replace("<u>", "").replace("</u>", "").replace("~~", "")
    s = re.sub(r"\*+", "", s)
    s = s.replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def blocks_of(text):
    out = []
    for raw in text.split("\n\n"):
        b = raw.strip()
        if not b or b == "---" or b.startswith("::: ") or b == ":::":
            continue
        out.append(b)
    return out


def word_diff(a, b):
    sm = difflib.SequenceMatcher(None, a.split(), b.split())
    bits = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        old, new = " ".join(a.split()[i1:i2]), " ".join(b.split()[j1:j2])
        bits.append(f"      - {old[:400]}\n      + {new[:400]}")
    return "\n".join(bits) or "      (whitespace only)"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply = "--apply" in sys.argv
    live_path = os.path.join(HERE, args[0] if args else "live.md")

    live = open(live_path, encoding="utf-8").read()
    m = re.search(r"store revision (\d+) · (\d+ \w+ \d{4})", live)
    rev, date = m.group(1), m.group(2)
    s1_raw = live[live.index("\n## 1. The bill"):live.index("\n## 2. Section-by-section summary")]
    live_blocks = [b for b in blocks_of(s1_raw) if not b.startswith(("#", "## "))]
    live_norm = [norm(b) for b in live_blocks]
    s1n = norm(s1_raw)

    doc = open(DOC05, encoding="utf-8").read()
    i, j = doc.index(START), doc.index(END)
    repro = doc[i:j]
    bs = blocks_of(repro)

    print(f"live bill: store revision {rev} ({date}); {len(live_blocks)} bill blocks")
    print(f"document 05 §4: {len(bs)} blocks in the reproduced span\n")

    divergent, subs = [], []
    for n, blk in enumerate(bs, 1):
        if blk.startswith(EDITORIAL):
            continue
        nb = norm(blk)
        if nb in s1n:
            continue
        divergent.append(n)
        scored = sorted(((difflib.SequenceMatcher(None, nb, ln).ratio(), k)
                         for k, ln in enumerate(live_norm)), reverse=True)
        best, k = scored[0]
        second = scored[1][0] if len(scored) > 1 else 0.0
        print(f"--- block {n}: divergent (best live match {best:.3f}, next {second:.3f})")
        if best < THRESHOLD:
            print("    NO CONFIDENT MATCH — this block must be resolved by hand\n")
            continue
        if best - second < 0.02:
            print("    AMBIGUOUS MATCH — two live blocks score alike; resolve by hand\n")
            continue
        print(word_diff(nb, live_norm[k]) + "\n")
        subs.append((blk, live_blocks[k]))

    print(f"{len(divergent)} divergent block(s); {len(subs)} with an unambiguous live match")
    if not apply:
        print("\nreport only — pass --apply to re-transcribe")
        return 1 if divergent else 0

    for old, new in subs:
        assert doc.count(old) == 1, f"block is not unique in document 05: {old[:80]}"
        doc = doc.replace(old, new)
    open(DOC05, "w", encoding="utf-8").write(doc)
    print(f"\nre-transcribed {len(subs)} block(s) at store revision {rev}")
    return 1 if len(subs) != len(divergent) else 0


if __name__ == "__main__":
    sys.exit(main())
