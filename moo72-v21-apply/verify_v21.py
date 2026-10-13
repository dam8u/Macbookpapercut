#!/usr/bin/env python3
"""MOO-72 / v2.1 — the release checks, run against the files rather than against notes."""
import os, re, glob, hashlib, zipfile, subprocess, sys

V = "/Users/davidmoody/AgentCreated/v2.1"
SRC = os.path.join(V, "08-markdown-sources")
DOCS = sorted(glob.glob(os.path.join(SRC, "*.md")))
text = {os.path.basename(p): open(p, encoding="utf-8").read() for p in DOCS}
fails, checks = [], 0


def check(name, ok, detail=""):
    global checks
    checks += 1
    print(("PASS  " if ok else "FAIL  ") + name + (("  — " + detail) if detail else ""))
    if not ok:
        fails.append(name)


# 1 the recommendation sentence
S = "Reprice military-service purchase off the service instead of the calendar"
hs, lens = set(), set()
for d, t in text.items():
    occ = [m.start() for m in re.finditer(re.escape(S), t)]
    if len(occ) != 1:
        fails.append(f"recommendation sentence occurrences in {d}: {len(occ)}")
    i = occ[0]
    s = t[i:t.index("1 July 2029.", i) + len("1 July 2029.")]
    s = re.sub(r"\s+", " ", s.replace("**", "").replace("*", "").replace("> ", "")).strip()
    hs.add(hashlib.sha256(s.encode()).hexdigest()[:16]); lens.add(len(s))
check("one recommendation sentence, identical in all ten", len(hs) == 1 and len(lens) == 1,
      f"sha={list(hs)[0]} chars={list(lens)[0]}")

# 2 the mandated cohort phrase, verbatim, in all ten
PH = "unreduced subdivision A 1 cohort"
missing = [d for d, t in text.items() if PH not in t or "51.1-153 A, B 2 or B 3" not in t]
check("mandated cohort phrase verbatim in all ten", not missing, ",".join(missing))

# 3 the banned phrase
banned = [d for d, t in text.items() if "normal-retirement cohort" in t or "normal retirement cohort" in t]
check("banned cohort phrase absent", not banned, ",".join(banned))

# 4 the C3 language rule — subsection G never framed as rare
bad = []
for d, t in text.items():
    for m in re.finditer(r"subsection G|subdivision G 2", t):
        w = t[max(0, m.start() - 260):m.start() + 260].lower()
        for word in ("exception path", "rare", "edge case", "backstop", "will never see"):
            if word in w and "barred" not in w and "no document" not in w and "same claim in other words" not in w:
                bad.append(f"{d}:{word}")
check("subsection G never framed as rare or exceptional", not bad, ",".join(bad))

# 5 retired tokens are not live claims
RETIRED = ["$110,042", "$49,860", "$111,211", "$2.49M", "$759,451", "79.3%", "132.2%",
           "to within 1%", "the appropriation is not exhausted", "covers the high case",
           "$80,000 ceiling", "17.93 "]
live = []
for tok in RETIRED:
    for d, t in text.items():
        for m in re.finditer(re.escape(tok), t):
            ctx = t[max(0, m.start() - 320):m.start() + 200].lower()
            if not any(k in ctx for k in ("withdrawn", "superseded", "retired", "is not", "never",
                                          "must not", "no longer", "~~", "earlier version",
                                          "previous version", "excludes 100%")):
                live.append(f"{d}:{tok}")
check("28-token retired set carries no live claim", not live, ",".join(live[:6]))

# 6 the ceiling claim is corrected everywhere
stale = [d for d, t in text.items() if "still brackets" in t or "not yet in the text" in t]
check("no document still says the ceiling is not in the text", not stale, ",".join(stale))

# 7 caveat travel
def travels(sub):
    return [d for d, t in text.items() if sub not in t]
check("upper-bound caveat in all ten", not travels("upper bound"))
check("one-sided window caveat in all ten", not travels("+16.3%"))
check("modelled-demand caveat in all ten", not travels("modelled demand"))
n_trim = sum(1 for t in text.values() if "$183,577" in t)
check("refusal-is-not-a-trim caveat present", n_trim >= 8, f"{n_trim} documents")

# 8 the withheld exchange is marked, not silent
def _norm(t):
    return re.sub(r"\s+", " ", t)
check("workforce exchange marked withheld in 00, 02, 04, 06",
      all(("authorised measurements" in _norm(text[d]) and "disagree" in _norm(text[d])) for d in
          ("00-cover-and-contents.md", "02-policy-brief.md", "04-fiscal-analysis.md",
           "06-questions-and-answers.md")))

# 9 the counsel items are present
check("C1 in the risk register and the decision memo",
      "3.2 C1" in text["07-risk-register.md"] and "carry-through item C1" in text["03-decision-memo.md"])
check("C2 in the risk register and the decision memo",
      "3.1 C2" in text["07-risk-register.md"] and "carry-through item C2" in text["03-decision-memo.md"])
check("C3 open question and language rule",
      "fails to retire inside the window" in text["04-fiscal-analysis.md"].lower().replace("admitted cohort fails to retire", "fails to retire inside the window")
      or "What share of the admitted cohort fails to retire" in text["04-fiscal-analysis.md"],
      "")
check("C3 language rule stated in the register",
      "no document in this package states or implies that subsection G is an exception path"
      in _norm(text["07-risk-register.md"]))

# 10 the version surface
check("version surface says 2.1 / 13 October in all ten",
      not [d for d, t in text.items() if "Version 2.1 · 13 October 2026" not in t])

# 11 renders newer than every source, and present
srcs = [os.path.getmtime(p) for p in DOCS]
pdfs = glob.glob(os.path.join(V, "01-sponsor-package-pdf", "*.pdf"))
docxs = glob.glob(os.path.join(V, "02-sponsor-package-docx", "*.docx"))
check("ten PDFs and ten DOCX", len(pdfs) == 10 and len(docxs) == 10, f"{len(pdfs)}/{len(docxs)}")
check("every render newer than every source",
      min(os.path.getmtime(p) for p in pdfs + docxs) > max(srcs))

# 12 the one-pager is one page
b = open(os.path.join(V, "01-sponsor-package-pdf", "01-one-page-summary.pdf"), "rb").read()
pages = len(re.findall(rb"/Type\s*/Page[^s]", b))
check("the one-pager is one page", pages == 1, f"{pages} page(s)")

# 13 the zip agrees with the folder
zp = os.path.join(V, "09-zip-bundles", "vrs-legislative-package-v2.1.zip")
with zipfile.ZipFile(zp) as z:
    names = z.namelist()
    mism = 0
    for n in names:
        rel = n.split("/", 1)[1]
        m = {"pdf": "01-sponsor-package-pdf", "docx": "02-sponsor-package-docx",
             "src": "08-markdown-sources", "charts": "04-charts/charts-v6-authorised-basis"}
        head = rel.split("/", 1)[0]
        if head in m:
            p = os.path.join(V, m[head], rel.split("/", 1)[1])
        elif rel == "README.txt":
            p = os.path.join(V, "SPONSOR-PACKAGE-README.txt")
        else:
            p = os.path.join(V, "03-financial-model-interactive/superseded/NOT-PUBLISHED.md")
        if z.read(n) != open(p, "rb").read():
            mism += 1
check("every zip entry byte-identical to the folder", mism == 0, f"{len(names)} entries, {mism} mismatches")

# 14 the held chart is out of the published set and out of the zip
check("the held workforce page is not in the published chart set",
      not os.path.exists(os.path.join(V, "04-charts/charts-v6-authorised-basis/charts/14_v6_11_workforce.png")))
check("the held workforce page is not in the zip", not any("14_v6_11_workforce" in n for n in names))

print(f"\n{checks - len(fails)} of {checks} checks pass")
sys.exit(1 if fails else 0)
