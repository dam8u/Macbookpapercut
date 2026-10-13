#!/usr/bin/env python3
"""MOO-212 item 1 — re-verify the whole bill-dependent surface at the live store revision.

Pulls every quoted string out of the ten sponsor documents, keeps the ones long enough to be
a quotation of the bill rather than a turn of phrase, and counts each one in section 1 of the
live bill document. A quotation the package prints as the bill's words must occur in the bill.

Strings the package expressly says do NOT occur in the bill are listed in WITHDRAWN and are
asserted to count zero, so the withdrawal cannot rot into a quotation.

Usage:  python3 verify_surface.py [live.md]
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"
LIVE = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else "live.md")
MINLEN = 25

# Quotations the package prints as NOT being in the bill. Each must count zero.
WITHDRAWN = [
    "the limitation in subsection E of § 51.1-153",
    "is not a collection, offset, or withholding for the purposes of this section",
    "the § 51.1-153 B normal-retirement cohort",
]

# Quoted strings that are not quotations of the bill, each with the reason it is not one.
# Every string the sweep finds must be a bill quotation that holds, or be on this list.
NOT_BILL_QUOTES = {
    "$3.0M is the smallest round number that makes the cap not bind":
        "a withdrawn claim of ours, printed as withdrawn",
    "The judgment rate of interest shall be an annual rate of six percent…":
        "§ 6.2-302 of the Code, not the bill",
    "The legal rate of interest shall be an annual rate of six percent":
        "§ 6.2-301 of the Code, not the bill",
    "Virginia is the stingiest state":
        "the opposition's words, printed as theirs",
    "You are selling service credit below its actuarial value":
        "the objection's words, printed as the objection",
    "backfill mechanism named with a decision-maker and an audit":
        "a retired recommendation of ours, printed as retired",
    "most members will never see subsection G":
        "framing the C3 language rule bans, printed as banned",
    "runs against the proposal":
        "the withdrawn direction claim, printed as withdrawn",
    "worse than the documents show":
        "the withdrawn direction claim, printed as withdrawn",
    "the limitation in subsection E of § 51.1-153":
        "expressly withdrawn as not occurring in the bill — asserted zero below",
}


def norm(s):
    s = s.replace("<u>", "").replace("</u>", "").replace("~~", "")
    s = re.sub(r"\*+", "", s)
    s = s.replace(" ", " ").replace("’", "'")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main():
    live = open(LIVE, encoding="utf-8").read()
    a = live.index("\n## 1. The bill")
    b = live.index("\n## 2. Section-by-section summary")
    s1 = norm(live[a:b])
    m = re.search(r"store revision (\d+) · (\d+ \w+ \d{4})", live)
    rev, date = m.group(1), m.group(2)
    print(f"live bill: store revision {rev} ({date}), section 1 is {len(s1)} normalised chars\n")

    quotes = {}
    for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        fn = os.path.basename(p)
        t = open(p, encoding="utf-8").read()
        # document 05 §4 reproduces the bill; blocks.py owns that span.
        if fn == "05-bill-drafting-request.md":
            t = t[:t.index("### Title\n")] + t[t.index("## 5. Open decisions in the draft"):]
        # The package marks a quotation of the bill as *"…"* — italic plus double quote.
        for raw in re.findall(r"\*\"((?:[^\"]|\"\*\s*,?\s*\*?\")+?)\"\*", t):
            q = norm(raw).strip().strip(",.;:")
            if len(q) < MINLEN:
                continue
            quotes.setdefault(q, set()).add(fn)

    missing, ok, excused = [], [], []
    for q, where in sorted(quotes.items()):
        if q in NOT_BILL_QUOTES:
            excused.append((q, sorted(where)))
            continue
        # An elided or bracketed quotation is checked fragment by fragment: the package
        # marks the elision with "…" and a changed initial letter with "[x]".
        # A "[n]" bracket marks a letter the package re-cased to fit its own sentence, so
        # the fragment is counted in both cases before it is called missing.
        frags = [f.strip().strip(",.;:") for f in q.split("…")]
        frags = [f for f in frags if len(f) >= MINLEN]

        def count(f):
            m = re.match(r"^\[(\w)\](.*)$", f, re.S)
            if m:
                rest = m.group(2)
                return (s1.count(m.group(1).lower() + rest)
                        + s1.count(m.group(1).upper() + rest))
            return s1.count(f)

        counts = [count(f) for f in frags]
        if frags and all(counts):
            ok.append((q, sorted(where), len(frags), counts))
        else:
            missing.append((q, sorted(where), list(zip(frags, counts))))

    print(f"{len(ok)} bill quotation(s) hold in the live text; "
          f"{len(missing)} do not; {len(excused)} are not quotations of the bill\n")
    for q, where, nf, counts in ok:
        tag = f"{nf} fragments {counts}" if nf > 1 else f"x{counts[0]}"
        print(f"  HOLDS {tag:22} ({', '.join(where)})  {q[:110]}")
    for q, where, detail in missing:
        print(f"\n  DOES NOT HOLD  ({', '.join(where)})\n    {q[:300]}\n    {detail}")
    print()
    for q, where in excused:
        print(f"  not the bill's words  ({', '.join(where)})  {q[:70]}\n"
              f"      -> {NOT_BILL_QUOTES[q]}")

    print()
    bad = []
    for s in WITHDRAWN:
        n = s1.count(norm(s))
        print(f"  withdrawn string, must be 0: {n}  — {s[:70]}")
        if n:
            bad.append(s)

    # The bill-dependent claims the package states as counts rather than as quotations.
    raw = open(LIVE, encoding="utf-8").read()
    a2 = raw.index("\n## 1. The bill")
    b2 = raw.index("\n## 2. Section-by-section summary")
    r1 = raw[a2:b2]
    sec = r1[r1.index("### <u>§ 51.1-142.4."):r1.index("### § 51.1-162.")]
    s1422 = r1[r1.index("### § 51.1-142.2."):r1.index("### <u>§ 51.1-142.4.")]
    i = sec.index("<u>2. The Board shall not accept an election if the certified subsidy")
    d2 = sec[i:sec.index("<u>3.", i)]

    claims = [
        ("$170,000 stated twice in subdivision D 2", d2.count("$170,000"), 2),
        ("the [$100,000] bracket is gone", r1.count("[$100,000]"), 0),
        ("the per-member subsidy ceiling placeholder is gone",
         r1.count("per-member subsidy ceiling"), 0),
        ('clause (viii) of "eligible member" is in the draft',
         len(re.findall(r"and \(viii\) would reach his unreduced retirement eligibility date", sec)), 1),
        ("§ 51.1-155 cited in subdivision B 4 a of § 51.1-142.2",
         len(re.findall(r"§ 51\.1-155(?![.0-9])", s1422)), 1),
        ("§ 51.1-155 cited in four places in § 51.1-142.4",
         len(re.findall(r"§ 51\.1-155(?![.0-9])", sec)), 4),
        ('"interest" occurs nowhere in § 51.1-142.4', sec.count("interest"), 0),
        ("the contingency inside the cap is still bracketed at [20]", r1.count("[20]"), 1),
        ("the cap is $3,000,000", r1.count("$3,000,000"), 1),
        ("the act amends §§ 51.1-142.2 and 51.1-162 and adds § 51.1-142.4",
         r1.count("to amend and reenact §§ 51.1-142.2 and 51.1-162 of the Code of Virginia and to "
                  "amend the Code of Virginia by adding a section numbered 51.1-142.4"), 1),
        ("the title line names death benefits and designation of beneficiary",
         r1.count("pilot program; death benefits; designation of beneficiary; reports."), 1),
    ]
    print()
    for name, got, want in claims:
        print(f"  {'PASS' if got == want else 'FAIL'}  {name}: {got} (expected {want})")
        if got != want:
            bad.append(name)

    return 1 if (missing or bad) else 0


if __name__ == "__main__":
    sys.exit(main())
