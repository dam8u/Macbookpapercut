#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 4 — the top-level README's basis block and its account of the
withheld interactive model. Additive; run after part 3."""
import sys
P = "/Users/davidmoody/AgentCreated/v2.1/SPONSOR-PACKAGE-README.txt"
s = open(P, encoding="utf-8").read()

def rep(old, new, tag):
    global s
    n = s.count(old)
    if n != 1:
        sys.exit(f"MISS [{tag}]: found {n}\n---\n{old[:200]}\n---")
    s = s.replace(old, new)
    print(f"  {tag}")

rep("""date are superseded; document 04 section 13 lists every one of them and says
why.""",
"""date are superseded; document 04 section 13 lists every one of them and says
why.

The BILL TEXT is a different thing from the fiscal basis and has its own date.
Document 05 transcribes it at STORE REVISION 69 of 13 October 2026 - the whole
working draft, both amended sections, the new section and all five enactment
clauses. Two things in it changed since v2.0 was cut and a reader of v2.0 needs
both: the bill now also AMENDS Va. Code 51.1-162, and the per-member ceiling of
$170,000 IS NOW IN THE TEXT at subdivision D 2, where the draft previously
bracketed [$100,000]. The contingency inside the cap is still bracketed at
[20] percent and is an open figure.""",
    "readme-bill-revision")

rep("""Re-emitting its arrays on the authorised basis is a model run, not an editorial
change, and it is commissioned rather than improvised. See the NOT-PUBLISHED.md
beside the file.""",
"""The authorised data now EXISTS - the five data blocks were re-emitted on the
authorised basis and are in 05-model-code-and-data/ - but two things stop the
model being rebuilt in this version, and neither is editorial. The STATUTORY
INTEREST DIAL is the one block that could not be measured on the authorised
basis: away from 6.00% its figures are derived by rescaling, and the modeller's
own instruction is that this block must be re-measured before it ships. And
every row of that dial away from 6.00% carries the standing publication
restriction on the S8 family's comparative dollar figures, so a live dial would
publish restricted figures to anyone who moved it. It ships as a static 6.00%
column or the restriction is lifted first, and that is a publication decision.
See the NOT-PUBLISHED.md beside the file.""",
    "readme-interactive-model")

open(P, "w", encoding="utf-8").write(s)
print("part 4 OK")
