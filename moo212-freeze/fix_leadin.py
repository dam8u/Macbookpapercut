#!/usr/bin/env python3
"""MOO-212 item 5 — the lead-in: keep one, change four words, and carry the note once.

Policy Director, MOO-206 §3. The lead-in stays, because without it the row sits beside "One
pathway only" and reads as *only* those routes — the expressio unius argument reserved at
item 47. But "which the bill defines as" hands our reading to the bill: both definitions cite
§ 51.1-153 whole, and the bill never writes "A, B 2 or B 3".

  which the bill defines as reached through  ->  which is, under the bill, reached through

Five sites. The adopted words after the lead-in are untouched, no "only" is added, and
neither § 51.1-155.1 B nor § 51.1-155.2 A is named. One site in document 03 wraps across a
line break, so the sweep is whitespace-tolerant on the lead-in and nowhere else.

The note is carried once per document, at the first extended-form site, inside the block that
carries the route list — not as a separate paragraph under it — so that a lifted table row
takes the note with it.
"""
import os
import re
import sys

SRC = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
OLD = r"which the bill\s+defines as reached through"
NEW = "which is, under the bill, reached through"
NOTE = ("*The bill's definitions cite § 51.1-153 as a whole, and subsection A or C of "
        "§ 51.1-155.1. The subdivisions of § 51.1-153 named here are the routes within that "
        "section that reach an allowance calculated under subdivision A 1 of § 51.1-155 and "
        "not reduced under subdivision A 2 or A 3.*")
TAIL = "through subsection A or C of § 51.1-155.1."

# document -> expected number of extended-form sites
EXPECTED = {"02-policy-brief.md": 1, "03-decision-memo.md": 1,
            "05-bill-drafting-request.md": 1, "06-questions-and-answers.md": 2}


def main():
    total_leadin = 0
    for fn, n_sites in EXPECTED.items():
        p = os.path.join(SRC, fn)
        t = open(p, encoding="utf-8").read()

        hits = list(re.finditer(OLD, t))
        assert len(hits) == n_sites, f"{fn}: {len(hits)} lead-ins, expected {n_sites}"
        t = re.sub(OLD, NEW, t)
        total_leadin += len(hits)

        # the note, once, at the first extended-form site
        if NOTE in t:
            print(f"{fn}: note already present")
        else:
            i = t.index(TAIL)
            assert t.count(NOTE) == 0
            t = t[:i + len(TAIL)] + " " + NOTE + t[i + len(TAIL):]
        open(p, "w", encoding="utf-8").write(t)

        tt = open(p, encoding="utf-8").read()
        assert tt.count(NOTE) == 1, f"{fn}: note occurs {tt.count(NOTE)}x"
        assert "defines as reached through" not in tt
        assert "only reached through" not in tt and "§ 51.1-155.1 B" not in tt
        assert "§ 51.1-155.2" not in tt
        print(f"{fn}: {len(hits)} lead-in(s) changed, note carried once")

    assert total_leadin == 5, total_leadin
    print(f"\n{total_leadin} lead-ins changed across {len(EXPECTED)} documents; "
          f"note carried once per document")

    # no document retains the old lead-in anywhere
    stale = [f for f in sorted(os.listdir(SRC)) if f.endswith(".md")
             and re.search(r"the bill\s+defines as", open(os.path.join(SRC, f),
                                                          encoding="utf-8").read())]
    assert not stale, stale
    return 0


if __name__ == "__main__":
    sys.exit(main())
