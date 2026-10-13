#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 7 — the release surface outside the version folder:
ERRATA.md's account of what is current. VERSIONS.md and CURRENT are written after this."""
import sys
P = "/Users/davidmoody/AgentCreated/ERRATA.md"
s = open(P, encoding="utf-8").read()

def rep(old, new, tag):
    global s
    if s.count(old) != 1:
        sys.exit(f"MISS [{tag}]: found {s.count(old)}")
    s = s.replace(old, new); print("  " + tag)

rep("""evening. Updated 12 October 2026, when `v2.0` was cut and `CURRENT` moved to it.**""",
    """evening. Updated 12 October 2026, when `v2.0` was cut, and again on 13 October 2026, when `v2.1`
was cut and `CURRENT` moved to it.**""",
    "errata-byline")

rep("""**`CURRENT` now points at `v2.0`, which supersedes `v1.0` in full.**""",
    """**`CURRENT` now points at `v2.1`, which supersedes `v2.0`, which superseded `v1.0` in full.**""",
    "errata-current")

rep("""| **The ten sponsor documents** | **`v2.0`** — i.e. `CURRENT`. Rebuilt 12 October 2026, internally consistent, verified, **not released** |""",
    """| **The ten sponsor documents** | **`v2.1`** — i.e. `CURRENT`. Cut 13 October 2026 on the current bill text, internally consistent, 22 of 22 release checks pass, **not released**. `v2.0` is superseded and is not edited |""",
    "errata-documents-row")

rep("""| The bill text | **MOO-42**, `bill-text-s8` **document revision 76** — re-transcribed into `v2.0` document 05; counsel-reviewed on MOO-187, not DLS-drafted |""",
    """| The bill text | **MOO-42**, `bill-text-s8` at **store revision 69 of 13 October 2026** — re-transcribed whole into `v2.1` document 05, including § 51.1-162, which the bill now also amends and which `v2.0` did not carry. The **$170,000** per-member ceiling is now **in** the text at D 2; the `[$100,000]` bracket is gone. *(`v2.0` cited "document revision 76": that was the Paperclip document counter, not the bill's own store-revision byline. The counters had drifted and the bill's own counter governs.)* Counsel passes on MOO-187 and since; not DLS-drafted |""",
    "errata-bill-text-row")

rep("""| The interactive financial model | **Withheld from `v2.0`.** Its embedded data is the superseded family. Kept at `v2.0/03-financial-model-interactive/superseded/` |""",
    """| The interactive financial model | **Withheld from `v2.1` too.** The authorised data now exists, but the statutory-interest dial is unmeasured on that basis and a live dial would publish S8-restricted figures. Kept at `v2.1/03-financial-model-interactive/superseded/` |
| The workforce exchange | **Per-case figures withheld, and the conflict is open.** Two authorised measurements disagree on the authorised cohort's mean acceleration — **44.8516** months against **42.8910** — and most in the conservative case. `v2.1/VERSION.md` §4 states both; the chart page built on the second is held at `v2.1/04-charts/held-pending-reconciliation/` |
| The three must-appear counsel items | **In the package from `v2.1`.** They were in none of the ten documents in `v2.0`: C1 and C2 at document 07 §§3.1–3.2 and document 03 §7, C3 as a language rule plus one open question |""",
    "errata-model-row")

open(P, "w", encoding="utf-8").write(s)
print("part 7 OK")
