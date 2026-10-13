#!/usr/bin/env python3
"""MOO-212 — re-transcribe document 05's reproduced subdivision D 1 at the live revision.

The replacement text is lifted out of the live bill document, not retyped, so the
reproduction cannot drift from it by a keystroke. The old block must match exactly once or
the script exits non-zero.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOC05 = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources/05-bill-drafting-request.md"
LIVE = os.path.join(HERE, "live.md")

live = open(LIVE, encoding="utf-8").read()
a = live.index("\n## 1. The bill")
b = live.index("\n## 2. Section-by-section summary")
s1 = live[a:b]
sec = s1[s1.index("### <u>§ 51.1-142.4."):s1.index("### § 51.1-162.")]

i = sec.index("<u>**D. 1.** The Board shall not accept an election")
j = sec.index("\n\n<u>2. The Board shall not accept an election if the certified subsidy", i)
new = sec[i:j].strip()
assert new.startswith("<u>**D. 1.**") and new.endswith("extended by three days.</u>"), new[-120:]
assert "\n" not in new, "live D 1 is not a single block"
assert "that the Board advises the member to review the member's designation of beneficiary" in new
assert "other than a failure to state that the Board advises the member" in new

doc = open(DOC05, encoding="utf-8").read()
olds = [ln for ln in doc.split("\n") if ln.startswith("<u>**D. 1.** The Board shall not accept")]
assert len(olds) == 1, f"{len(olds)} candidate D 1 blocks in document 05"
old = olds[0]
assert "that the member is advised to review the member's designation of beneficiary" in old

if old == new:
    print("document 05's D 1 already matches the live text; nothing to do")
    sys.exit(0)

assert doc.count(old) == 1
open(DOC05, "w", encoding="utf-8").write(doc.replace(old, new))
print(f"re-transcribed subdivision D 1: {len(old)} chars -> {len(new)} chars")
