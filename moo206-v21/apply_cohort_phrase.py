#!/usr/bin/env python3
"""Apply the MOO-205 §3.5 cohort-phrase register entry to the ten sponsor documents.

MOO-206, Editor. One edit per class-1 / class-2 / class-3 site, each asserted to match
exactly once in the base text so the script fails loudly rather than guessing if the base
has moved. Run it against a directory of the ten markdown sources:

    python3 apply_cohort_phrase.py <dir>

Base: AgentCreated/v2.0/08-markdown-sources as at 12 October 2026. If any assertion fails,
the base has changed and the site must be re-classified by hand before re-running.
"""
import pathlib
import sys

PHRASE = "the unreduced subdivision A 1 cohort, reached through § 51.1-153 A, B 2 or B 3"
EXT = ("reached through § 51.1-153 A, B 2 or B 3, or, on an involuntary separation or a "
       "lawfully abolished office, through subsection A or C of § 51.1-155.1")
NOWEIGHT = "Neither of those two routes carries weight in the modelled distribution."

SHARED_DOCS = ("00-cover-and-contents 02-policy-brief 03-decision-memo 04-fiscal-analysis "
               "05-bill-drafting-request 06-questions-and-answers 07-risk-register "
               "08-source-appendix 09-sponsor-and-advocacy-plan").split()

# (file, site id, class, old, new)
EDITS = [
    # ---------------------------------------------------------------- the shared headline block
    ("@shared", "S1", "class 1 — the cohort behind the 18.4 count",
     "> 30.7** — measured on § 51.1-142.4 C as option (c) with the no-advance bar of clause (vii) in the\n"
     "> cohort. **That count is an upper bound",
     "> 30.7** — measured on § 51.1-142.4 C as option (c) with the no-advance bar of clause (vii) in the\n"
     "> unreduced subdivision A 1 cohort, reached through § 51.1-153 A, B 2 or B 3. **That count is an\n"
     "> upper bound"),
    ("@shared", "S2", "class 1 — back-reference, phrase established eight lines above",
     "> ceiling refuses the most expensive 4.74% of the cohort — and the bill still brackets `[$100,000]`,",
     "> ceiling refuses the most expensive 4.74% of that cohort — and the bill still brackets `[$100,000]`,"),

    # ---------------------------------------------------------------- 01 one-pager
    ("01-one-page-summary.md", "01-a", "class 1 — the only cohort site in the document",
     "  **1.42× approximate normal cost**, and **43% of the current-law price**, on the bill's cohort.",
     "  **1.42× approximate normal cost**, and **43% of the current-law price**, on " + PHRASE + "."),

    # ---------------------------------------------------------------- 02 policy brief
    ("02-policy-brief.md", "02-a", "class 1 — A + B cohort named in the same cell",
     "These two figures are the **Pathways A+B** cohort; on the bill's own narrower cohort the member pays **1.42×** and **43%**",
     "These two figures are the **Pathways A+B** cohort; on " + PHRASE + " the member pays **1.42×** and **43%**"),
    ("02-policy-brief.md", "02-b", "class 2 — the eligibility-test row",
     "| **One pathway only** — a member already eligible for an unreduced benefit is excluded | Red-team finding F6 | Closes the windfall channel: someone already retiring next month cannot take the price and deliver nothing. |",
     "| **One pathway only** — a member already eligible for an unreduced benefit is excluded | Red-team finding F6 | Closes the windfall channel: someone already retiring next month cannot take the price and deliver nothing. The date the member must reach is the unreduced retirement eligibility date, which the bill defines as " + EXT + ". |"),

    # ---------------------------------------------------------------- 03 decision memo
    ("03-decision-memo.md", "03-a", "class 1 — the member-price pair",
     "Across the bill's own cohort the member pays **1.42× approximate normal cost** and **43% of the",
     "Across " + PHRASE + " the member pays **1.42× approximate normal cost** and **43% of the"),
    ("03-decision-memo.md", "03-b", "class 3 — split: test sentence, then figure sentence",
     "5. **One pathway only.** A member already eligible for an unreduced benefit is excluded. That\n"
     "   closes the windfall channel and it is most of why the bill's cohort is **18.4 rather than 79.2**.",
     "5. **One pathway only.** A member already eligible for an unreduced benefit is excluded — the\n"
     "   date the member must reach is the unreduced retirement eligibility date, which the bill\n"
     "   defines as " + EXT + ".\n"
     "   " + NOWEIGHT + " That closes the windfall channel and it is most of why " + PHRASE + "\n"
     "   is **18.4 rather than 79.2**."),

    # ---------------------------------------------------------------- 04 fiscal analysis
    ("04-fiscal-analysis.md", "04-a", "class 1 — A + B cohort named in the same note",
     "always be labelled as such;** the bill's own narrower cohort pays 1.42× and 43% and is priced in §2.",
     "always be labelled as such;** " + PHRASE + " pays 1.42× and 43% and is priced in §2."),
    ("04-fiscal-analysis.md", "04-b", "class 1 — table caption",
     "**The retirement-deadline ladder**, bill cohort, 6.00% statutory interest:",
     "**The retirement-deadline ladder**, " + PHRASE + ", 6.00% statutory interest:"),
    ("04-fiscal-analysis.md", "04-c", "class 1 — full-cohort baseline named in the same note",
     "the bill's own cohort is about a quarter of that baseline and the percentages carry.)*",
     PHRASE + " is about a quarter of that baseline and the percentages carry.)*"),

    # ---------------------------------------------------------------- 05 drafting request
    ("05-bill-drafting-request.md", "05-a", "class 2 + limit 2 — element 5, Eligibility",
     "| 5 | **Eligibility** | A Plan 1 or Plan 2 **state agency employee** who is **not** already eligible for an unreduced allowance without the purchase, and **would be** eligible on the first of the month after the credit posts. This is the narrow reading and it is deliberate — the broad reading, reaching any member whose eligibility date merely moves forward, costs **3.7×**. |",
     "| 5 | **Eligibility** | A Plan 1 or Plan 2 **state agency employee** who is **not** already eligible for an unreduced allowance without the purchase, and **would be** eligible on the first of the month after the credit posts. The date the member must reach is the unreduced retirement eligibility date, which the bill defines as " + EXT + ". " + NOWEIGHT + " This is the narrow reading and it is deliberate — the broad reading, reaching any member whose eligibility date merely moves forward, costs **3.7×**. |"),

    # ---------------------------------------------------------------- 06 questions and answers
    ("06-questions-and-answers.md", "06-a", "class 3 — split: test sentence, then figure sentence",
     "**And the appropriation is not the first thing that turns a member away.** The bill's own limits do\n"
     "that: subsection C refuses an election that would not advance the member's unreduced retirement\n"
     "eligibility date, and the $170,000 per-member ceiling refuses the most expensive 4.74% of the\n"
     "cohort. Between them they refuse about **2.2 of a 20.65** modelled population at the central\n"
     "estimate — about 1.0 by the eligibility bars, about 1.2 by the ceiling — where the appropriation\n"
     "refuses none.",
     "**And the appropriation is not the first thing that turns a member away.** The bill's own limits do\n"
     "that. Subsection C refuses an election that would not advance the member's unreduced retirement\n"
     "eligibility date — the date the member must reach, which the bill defines as " + EXT + ".\n"
     + NOWEIGHT + " And the $170,000 per-member ceiling refuses the most expensive 4.74% of " + PHRASE + ".\n"
     "Between them they refuse about **2.2 of a 20.65** modelled population at the central\n"
     "estimate — about 1.0 by the eligibility bars, about 1.2 by the ceiling — where the appropriation\n"
     "refuses none."),
    ("06-questions-and-answers.md", "06-b", "class 2 — the windfall-channel bullet",
     "- **The windfall channel is closed by the eligibility definition.** A member already eligible for\n"
     "  an unreduced benefit — who could have satisfied every condition while retiring on a date they had\n"
     "  already chosen — is excluded from the bill entirely.",
     "- **The windfall channel is closed by the eligibility definition.** A member already eligible for\n"
     "  an unreduced benefit — who could have satisfied every condition while retiring on a date they had\n"
     "  already chosen — is excluded from the bill entirely. The date the member must reach is the\n"
     "  unreduced retirement eligibility date, which the bill defines as " + EXT + "."),
]


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    applied = 0
    for fname, site, note, old, new in EDITS:
        targets = [root / (d + ".md") for d in SHARED_DOCS] if fname == "@shared" else [root / fname]
        for p in targets:
            t = p.read_text(encoding="utf-8")
            n = t.count(old)
            assert n == 1, f"{p.name}: site {site} matched {n} times, expected 1 — base has moved"
            p.write_text(t.replace(old, new), encoding="utf-8")
            applied += 1
        print(f"ok  {site:6} {note}  ({'all nine shared' if fname == '@shared' else fname})")
    print(f"\n{applied} replacements across {len(EDITS)} sites.")


if __name__ == "__main__":
    main()
