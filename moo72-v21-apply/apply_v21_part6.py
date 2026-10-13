#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 6 — the chart set's basis note records the held page and the
bill-revision correction. Additive."""
import sys
P = "/Users/davidmoody/AgentCreated/v2.1/04-charts/charts-v6-authorised-basis/BASIS-NOTE.md"
s = open(P, encoding="utf-8").read()

def rep(old, new, tag):
    global s
    if s.count(old) != 1:
        sys.exit(f"MISS [{tag}]: found {s.count(old)}")
    s = s.replace(old, new); print("  " + tag)

rep("""Clause (viii) of "eligible member" is in the live draft at revision 76 and is in
no committed model run.""",
    """Clause (viii) of "eligible member" is in the live draft at store revision 69 of
13 October 2026 and is in no committed model run.""",
    "basis-note-revision-69")

rep("""Three superseded chart sets are kept at [`../superseded/`](../superseded/) and must not be used with
these documents.""",
"""**One page of this set is held out of it, and it is not superseded.** `14_v6_11_workforce.png` and
its photocopy proof are at [`../held-pending-reconciliation/`](../held-pending-reconciliation/),
because two authorised measurements of the workforce exchange disagree — on the authorised cohort's
mean acceleration (**42.8910** months here against 44.8516 in the recomputation) and most in the
conservative case. The ten documents withhold the per-case split for the same reason and state both
sets in document 04 §10, so the page is held rather than published beside text that declines to
print its figures. Nothing is wrong with the page on its own basis, and `HELD.md` beside it says
what would put it back. **The set is therefore 14 published pages, not 15.**

Three superseded chart sets are kept at [`../superseded/`](../superseded/) and must not be used with
these documents.""",
    "basis-note-held-page")

open(P, "w", encoding="utf-8").write(s)
print("part 6 OK")
