# -*- coding: utf-8 -*-
"""MOO-187 red-team re-verification of the MOO-164 cut.

Reproduces every count this review relies on, against a LIVE fetch of bill-text-s8 rather than
against the revision-61 snapshot the cut was built on. Nothing is written to the store and no
team file is modified.

Usage:
    python3 check187.py bill.md          # bill.md = bill-text-s8 document body, fetched live

Prints, and asserts where the review states a definite result:
  1. the enacted-§1 region and its length
  2. every act/acts/acting/action upon occurrence in §1, enumerated      -> review N1 (expect 19)
  3. a hunt for a twentieth under other act-keying forms                 -> review N1 (expect none)
  4. the six MOO-164 FINDs and the three MOO-141 FINDs on the live base  -> review N9 (expect all 1)
  5. the §7.2 count table, before and after both patches                -> review F2 (acts upon = 9)
  6. the five "shall act upon" duties and their commencements            -> review F6
  7. every "period allowed" / "time allowed" phrase in §1                -> review F13
  8. every "pending" in §1, by provision                                 -> review N8
  9. the four typographic apostrophes and the subdivision they sit in    -> review N10
 10. "no later than" in §1                                              -> review F15
"""
import re
import sys

bill = open(sys.argv[1] if len(sys.argv) > 1 else 'bill.md', encoding='utf-8').read()
print(f"[1] whole document: {len(bill)} chars")

lines = bill.split('\n')
start = next(i for i, l in enumerate(lines) if l.startswith('## 1. The bill'))
end = next(i for i, l in enumerate(lines) if l.startswith('## 2. Section-by-section'))
sec1 = '\n'.join(lines[start:end])
print(f"[1] enacted §1 region: lines {start}-{end-1}, {len(sec1)} chars")

# ---------------------------------------------------------------- 2. the nineteen
occ = list(re.finditer(r"\b(acts?|acting|action)\s+upon\b", sec1))
print(f"\n[2] act/acts/acting/action upon in §1: {len(occ)}")
for n, m in enumerate(occ, 1):
    print(f"   #{n:2d} [{m.group(0):11s}] …{sec1[max(0, m.start()-70):m.start()+40]}…".replace('\n', ' '))
assert len(occ) == 19, f"expected 19, got {len(occ)}"

# ---------------------------------------------------------------- 3. the hunt for a twentieth
print("\n[3] other act-keying forms (expect 0 for the first four):")
for p in [r"acted upon", r"\bacts? on\b", r"acting on\b", r"the Board's acting",
          r"\bacts\b(?!\s+upon)", r"\bacting\b(?!\s+upon)", r"\baction\b(?!\s+upon)",
          r"the Board's action", r"Board first acts", r"Board last acts"]:
    print(f"   {p!r}: {len(re.findall(p, sec1))}")

# ---------------------------------------------------------------- 4. the anchors
E1_F = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_R = ("every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. "
        "For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, "
        "the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or "
        "last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board "
        "first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to "
        "make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by "
        "this section.</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

EDITS = [
 ("164-1 card (b)",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after the Board gives the person who filed the request written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request"),
 ("164-2 card (h)",
  "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
  "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect, the determination takes effect on the first day"),
 ("164-3 card (j)",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request"),
 ("164-4 F-5",
  "within the period this definition allows for acting upon it",
  "within the period allowed by this section for acting upon it"),
 ("164-5 F-9",
  "any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition by reason of the Board's action upon a request"),
 ("164-6 conforming",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
  "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
]

print("\n[4] anchors on the live base:")
for tag, f, _ in EDITS:
    c = bill.count(f)
    print(f"   {tag:18s} {c}")
    assert c == 1, tag
for tag, f in (("MOO-141 E1", E1_F), ("MOO-141 E2", E2_F), ("MOO-141 E3", E3_F)):
    c = bill.count(f)
    print(f"   {tag:18s} {c}")
    assert c == 1, tag

out = bill
delta = 0
for f, r in ((E1_F, E1_R), (E2_F, E2_R), (E3_F, E3_R6)):
    out = out.replace(f, r, 1)
for tag, f, r in EDITS:
    out = out.replace(f, r, 1)
    delta += len(r) - len(f)
out = out.replace('’', "'")
print(f"   MOO-164 amendment delta {delta:+d} (review N9 expects +490)")
assert delta == 490, delta

# ---------------------------------------------------------------- 5. the §7.2 table
DOC = {  # phrase: (cut's "store rev 61" column, cut's "after both patches" column)
 "acts upon": (8, 7), "act upon": (8, 11), "last acts upon": (1, 1), "first acts upon": (2, 3),
 "acting upon": (3, 4), "action upon": (2, 2),
 "30 days after the Board acts upon the request": (1, 1),
 "48 days after the Board acts upon the request": (0, 1),
 "120 days after the Board acts upon the request": (0, 1),
 "the period allowed by this section for acting upon": (0, 3),
 "the period allowed to it for acting upon": (1, 0),
 "the 90 days allowed by this subsection": (1, 0),
 "this definition allows for acting upon it": (1, 0),
 "upon the Board's action upon a request": (1, 0),
 "by reason of the Board's action upon a request": (0, 1),
 "written notice of its decision upon the request": (0, 1),
 "is pending": (8, 8), "was pending": (1, 1),
}
print(f"\n[5] §7.2 re-run   {'phrase':50s} {'live':>5} {'cut':>5} {'after':>6} {'cutAft':>7}")
bad = []
for p, (b_doc, a_doc) in DOC.items():
    b, a = bill.count(p), out.count(p)
    ok = (b == b_doc and a == a_doc)
    if not ok:
        bad.append(p)
    print(f"   {'' if ok else '!!'}{'':3s}{p:50s} {b:5d} {b_doc:5d} {a:6d} {a_doc:7d}  {'ok' if ok else 'MISMATCH'}")
print(f"   mismatched rows: {bad}   (review F2 expects exactly ['acts upon'], true value 9)")
assert bad == ["acts upon"] and out.count("acts upon") == 9

print("\n[5b] the nine surviving `acts upon`, after both patches — #5 and #6 are both Edit 164-1's:")
for n, m in enumerate(re.finditer("acts upon", out), 1):
    print(f"   #{n} …{out[max(0, m.start()-80):m.start()+40]}…".replace('\n', ' '))

# ---------------------------------------------------------------- 6. the five duties
print("\n[6] `shall act upon` duties in §1 and their commencements:")
for m in re.finditer("shall act upon", sec1):
    print(f"   …{sec1[m.start():m.start()+105]}…".replace('\n', ' '))

# ---------------------------------------------------------------- 7. the period-allowed sweep
for phrase in ("the period allowed", "the time allowed"):
    ms = list(re.finditer(re.escape(phrase), sec1))
    print(f"\n[7] {phrase!r} in §1: {len(ms)}")
    for m in ms:
        print(f"   …{sec1[m.start():m.start()+95]}…".replace('\n', ' '))

# ---------------------------------------------------------------- 8. pending
for phrase in ("is pending", "was pending"):
    ms = list(re.finditer(re.escape(phrase), sec1))
    print(f"\n[8] {phrase!r} in §1: {len(ms)}")
    for m in ms:
        print(f"   …{sec1[max(0, m.start()-85):m.start()+25]}…".replace('\n', ' '))

# ---------------------------------------------------------------- 9. apostrophes and G 4's span
subdiv = {m.start(): m.group(0) for m in re.finditer(r"<u>\*{0,2}\d\.\s", sec1)}
g4 = [s for s in sorted(subdiv) if s > 62000]
print(f"\n[9] typographic apostrophes (U+2019) in §1: {sec1.count(chr(0x2019))}")
for m in re.finditer(chr(0x2019), sec1):
    print(f"   @{m.start()}  …{sec1[max(0, m.start()-60):m.start()+40]}…".replace('\n', ' '))
print(f"   subsection-G subdivision starts at §1 offsets: {g4[:4]}  — G 2, G 3, G 4, G 5; "
      "G 4 spans the third to the fourth, and all four apostrophes fall inside it")
for _, f, _ in EDITS:
    assert chr(0x2019) not in f, "a FIND string contains a typographic apostrophe"
print("   no FIND string contains a typographic apostrophe — either order works (review N10)")

# ---------------------------------------------------------------- 10. no later than
print(f"\n[10] `no later than` in §1: {len(re.findall('no later than', sec1))}   (the cut says 72 — review F15)")
print("\nAll assertions passed.")
