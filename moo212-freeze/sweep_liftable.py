#!/usr/bin/env python3
"""MOO-212 item 4 — the liftability guard on cohort back-references.

Eleven occurrences in nine table rows across six documents, from §2 of the Policy Director's
MOO-206 decision document. In a liftable site the minimum is the identifier, so a bare
"the cohort" becomes "the unreduced subdivision A 1 cohort" and the route list is not added.

Each edit is anchored to a substring that occurs on exactly one line of the file, and the
replacement is made inside that line only, the stated number of times. Every assertion is
exact, so the script exits non-zero rather than guessing if the base has moved.

Two sites are deliberately NOT swept, on the Director's direction:
  * the shared headline quote-block's "4.74% of that cohort" — the full phrase stands eight
    lines above in the same quote-block, which never travels in halves;
  * 04-fiscal-analysis.md §13's "$1,641,824 on that cohort" — that is the superseded cohort
    named in its own row, and the authorised cohort's name there would mislabel the figure.

One site is reported, not swept: 07-risk-register.md R1/F1/F2, "the cohort was rebuilt
monthly from membership history". It is a table row, so it is liftable, but it describes how
the model's cohort was constructed rather than naming the cohort behind a figure. The
Director reserved the classification.
"""
import os
import sys

SRC = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
ID = "the unreduced subdivision A 1 cohort"

# (file, line anchor, [(old, new, count)])
EDITS = [
    ("00-cover-and-contents.md",
     "The per-case figures of the workforce exchange, document 04 §10",
     [("on the cohort's mean acceleration", f"on {ID}'s mean acceleration", 1)]),
    ("00-cover-and-contents.md",
     "| The per-member subsidy ceiling and the definition it is written on |",
     [("100% of the cohort the bill admits", f"100% of {ID} the bill admits", 1)]),
    ("02-policy-brief.md",
     "| **Per-member subsidy ceiling of $170,000** | Red-team finding R7 |",
     [("4.74% of the cohort", f"4.74% of {ID}", 1)]),
    ("03-decision-memo.md",
     "~~**Getting $170,000 into the text.**~~",
     [("4.74% of the cohort", f"4.74% of {ID}", 1),
      ("100% of the cohort the bill admits", f"100% of {ID} the bill admits", 1)]),
    ("04-fiscal-analysis.md",
     "The **$80,000** per-member ceiling, and the $100,000 / $80,000 pairing",
     [("100% of the cohort the bill admits", f"100% of {ID} the bill admits", 1)]),
    ("04-fiscal-analysis.md",
     '"Extending the pilot to Plan 2 costs essentially nothing"',
     [("7% of the cohort", f"7% of {ID}", 1)]),
    ("05-bill-drafting-request.md",
     "| 9 | **Per-member ceiling** |",
     [("100% of the cohort the bill admits", f"100% of {ID} the bill admits", 1)]),
    ("05-bill-drafting-request.md",
     "~~**Writing $170,000 into the draft.**~~",
     [("100% of the cohort the bill admits", f"100% of {ID} the bill admits", 1)]),
    ("07-risk-register.md",
     "| **R-F** |",
     [("4.74% of the cohort", f"4.74% of {ID}", 1),
      ("100% of the cohort the bill admits", f"100% of {ID} the bill admits", 1)]),
]

# Sites that must survive the sweep untouched, asserted after it runs.
PROTECTED = [
    ("00-cover-and-contents.md", "4.74% of that cohort", 1),
    ("02-policy-brief.md", "4.74% of that cohort", 1),
    ("03-decision-memo.md", "4.74% of that cohort", 1),
    ("04-fiscal-analysis.md", "4.74% of that cohort", 1),
    ("05-bill-drafting-request.md", "4.74% of that cohort", 1),
    ("06-questions-and-answers.md", "4.74% of that cohort", 1),
    ("07-risk-register.md", "4.74% of that cohort", 1),
    ("08-source-appendix.md", "4.74% of that cohort", 1),
    ("09-sponsor-and-advocacy-plan.md", "4.74% of that cohort", 1),
    ("04-fiscal-analysis.md", "$1,641,824 on that cohort", 1),
    # Ruled no class by the Policy Director on 13 October 2026 (MOO-212): the guard covers
    # back-references to the unreduced subdivision A 1 cohort, and this names the cost model's
    # population, whose antecedent is the Finding cell of its own row. Protected by ruling, not
    # pending one. See moo212-director/moo212-r1f1f2-ruling.md.
    ("07-risk-register.md", "the cohort was rebuilt monthly from membership history", 1),
]


def main():
    applied = 0
    for fn, anchor, subs in EDITS:
        p = os.path.join(SRC, fn)
        lines = open(p, encoding="utf-8").read().split("\n")
        idx = [i for i, l in enumerate(lines) if anchor in l]
        assert len(idx) == 1, f"{fn}: anchor matches {len(idx)} lines — {anchor!r}"
        i = idx[0]
        line = lines[i]
        for old, new, count in subs:
            got = line.count(old)
            assert got == count, f"{fn}:{i + 1}: {old!r} occurs {got}x in the row, expected {count}"
            line = line.replace(old, new)
            applied += count
        lines[i] = line
        open(p, "w", encoding="utf-8").write("\n".join(lines))
        print(f"{fn}:{i + 1}  {sum(c for _, _, c in subs)} occurrence(s) cured")

    print(f"\n{applied} occurrences cured in {len({e[0] for e in EDITS})} documents, "
          f"{len(EDITS)} rows")

    bad = []
    for fn, s, count in PROTECTED:
        t = open(os.path.join(SRC, fn), encoding="utf-8").read()
        if t.count(s) != count:
            bad.append(f"{fn}: {s!r} {t.count(s)}x, expected {count}")
    for b in bad:
        print("PROTECTED SITE DISTURBED — " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
