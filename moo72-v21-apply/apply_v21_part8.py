#!/usr/bin/env python3
"""MOO-72 / v2.1 pass, part 8 — VERSIONS.md: the banner and the new row. CURRENT moves last."""
import sys
P = "/Users/davidmoody/AgentCreated/VERSIONS.md"
s = open(P, encoding="utf-8").read()

def rep(old, new, tag):
    global s
    if s.count(old) != 1:
        sys.exit(f"MISS [{tag}]: found {s.count(old)}")
    s = s.replace(old, new); print("  " + tag)

rep("""> **`CURRENT` points at `v2.0`, which is internally consistent and verified but has not been
> released.**""",
    """> **`CURRENT` points at `v2.1`, which is internally consistent and verified but has not been
> released.**""",
    "banner-current")

rep("""> **Two caveats travel with `v2.0`'s headline and are not optional.** The participant count of 18.4
> is an **upper bound** — a further eligibility screen is in the live draft and in no model run — and
> the $1.3 million aggregate is the **cheap end** of the retirement window, one-sided dearer by
> +7.5% to +16.3%. `v2.0/VERSION.md` §2 states both.""",
    """> **Two caveats travel with `v2.1`'s headline and are not optional.** The participant count of 18.4
> is an **upper bound** — a further eligibility screen is in the live draft and in no model run — and
> the $1.3 million aggregate is the **cheap end** of the retirement window, one-sided dearer by
> +7.5% to +16.3%. `v2.1/VERSION.md` §2 states both.
>
> **And one figure in `v2.1` is withheld rather than printed.** Two authorised measurements of the
> workforce exchange disagree — on the authorised cohort's mean acceleration, **44.8516** months
> against **42.8910** — so the per-case split is behind a marker, the chart page built on the second
> is held, and the reconciliation is the Policy Director's with the Fiscal & Impact Modeler.
> `v2.1/VERSION.md` §4.""",
    "banner-caveats")

rep("""| **v2.0** | 12 October 2026 | **Current.**""",
    """| **v2.1** | 13 October 2026 | **Current.** The ten documents carried onto the current bill text, with the three counsel items the red team marked must-appear — which were in none of the ten in `v2.0` — in Markdown, PDF and DOCX, and a verified zip. | **The bill text, re-transcribed whole at store revision 69 of 13 October 2026.** The **$170,000** per-member ceiling is now **in** the text at D 2 and the `[$100,000]` bracket is gone, which ten places in eight documents had said was still open; the bill also amends **§ 51.1-162**, which `v2.0` did not carry at all. **C1, C2 and C3 are in the package** with every quotation re-checked at store revision 69, and the mandated cohort phrase is in all ten verbatim. The workforce exchange's *direction* claim is **withdrawn** and its per-case figures are **withheld** on an unresolved conflict between two authorised measurements. **The fiscal basis did not move:** 18.4 participants, $1,321,112 PV, $71,813 per participant, 39% / 78% / 130% of the cap. Full account in [`v2.1/VERSION.md`](v2.1/VERSION.md). |
| **v2.0** | 12 October 2026 | **Superseded by `v2.1`, and not withdrawn.**""",
    "versions-row")

rep("""| **v2.1** | **Not cut, and not yet commissioned as a folder.** The two things that would justify it are the **interactive model re-emitted on the authorised basis** (withheld from `v2.0`, and a model run rather than an editorial change) and the **workforce exchange recomputed on the recommended design's own per-participant anchor** rather than repaired S1's. Both are on the Fiscal & Impact Modeler. Neither moves a recommendation; both move printed figures, so they travel together in one pass. |""",
    """| ~~**v2.1**~~ | **Cut on 13 October 2026** — see the table above. Of the two things reserved for it, the **workforce recomputation** was delivered and is in the folder behind a marker, because it disagrees with the chart set; the **interactive model** was not re-emitted, because its interest-rate block is still unmeasured on the authorised basis and a live dial would publish S8-restricted figures. |
| **v2.2** | **Not cut.** The two things that would justify it are the **workforce exchange reconciled** between the two authorised measurements — which would release the per-case figures and return the held chart page — and the **interactive model re-emitted** with its interest block measured and a publication decision taken on the dial. Both are model work, not editorial. Neither moves a recommendation. |""",
    "planned-v21")

open(P, "w", encoding="utf-8").write(s)
print("part 8 OK")
