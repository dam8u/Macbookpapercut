# -*- coding: utf-8 -*-
"""MOO-176 revision 6 cut: re-resolve the three anchors on the live base, apply to a copy,
re-splice every reproduction, re-run every count. Nothing is written to the store."""
import json, os, re, sys

S = os.environ["PAPERCLIP_RUN_SCRATCH_DIR"]
base = open(f"{S}/base.md").read()

S1_START = "## 1. The bill"
S1_END = "## 2. Section-by-section"

def s1(doc):
    a = doc.index(S1_START); b = doc.index(S1_END)
    return doc[a:b]

# ---- the three edits -------------------------------------------------------
E1_FIND = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_READ = ("every period within which a person may or must act that runs from the giving of that statement "
           "or notice is extended by three days. For the purposes of this section and of subdivision B 4 f "
           "of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, "
           "or last acting, upon a request, or where a date is fixed by reference to the month in which the "
           "Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to "
           "last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding "
           "sentence determines the date by which the Board is required to act upon a request, to make a "
           "determination, or to give a notice or a decision, or whether the Board has performed such a duty "
           "within a period required by this section.</u>")

E2_FIND = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_READ = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."

E3_FIND = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_READ_R5 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"
E3_READ_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

EDITS = [("Edit 1", E1_FIND, E1_READ), ("Edit 2", E2_FIND, E2_READ), ("Edit 3", E3_FIND, E3_READ_R6)]

print("== base")
print("  document characters:", len(base))
print("  §1 characters:", len(s1(base)))

print("== anchor resolution on the live base (whole document, and §1)")
ok = True
for name, f, r in EDITS:
    cd, c1 = base.count(f), s1(base).count(f)
    print(f"  {name}: FIND len {len(f)} | document count {cd} | §1 count {c1} | READ len {len(r)} | delta {len(r)-len(f):+d}")
    if cd != 1:
        ok = False
print("  all three resolve exactly once:", ok)

# Edit 2's short form, the trap
short = "no later than 15 days after it acts upon the request"
print("  Edit 2 short form count in §1 (must be 2, which is why the anchor is the full clause):", s1(base).count(short))

# ---- apply to a copy -------------------------------------------------------
applied = base
for name, f, r in EDITS:
    assert applied.count(f) == 1, name
    applied = applied.replace(f, r)

d_doc = len(applied) - len(base)
d_s1 = len(s1(applied)) - len(s1(base))
print("== applied copy")
print("  document characters:", len(applied), f"({d_doc:+d})")
print("  §1 characters:", len(s1(applied)), f"({d_s1:+d})")
print("  the two deltas agree (no edit landed outside §1):", d_doc == d_s1)

# revision 5 comparison: same cut with Edit 3 at 30 days
applied_r5 = base
for name, f, r in [("Edit 1", E1_FIND, E1_READ), ("Edit 2", E2_FIND, E2_READ), ("Edit 3", E3_FIND, E3_READ_R5)]:
    applied_r5 = applied_r5.replace(f, r)
print("  revision-5 equivalent delta on this base:", len(applied_r5) - len(base))
print("  Edit 3 revision 5 delta:", len(E3_READ_R5) - len(E3_FIND), "| revision 6 delta:", len(E3_READ_R6) - len(E3_FIND))

# ---- counts ----------------------------------------------------------------
TERMS = [
 "acts upon", "first acts upon", "last acts upon", "last acting", "acting upon", "action upon",
 "is deemed to act", "or an application", "pending", "month in which",
 "no later than 15 days after it acts upon the request",
 "30 days after the Board acts upon the request",
 "120 days after the Board acts upon the request",
 "until the Board acts upon the request",
 "its decision upon the request", "act upon the application",
 "<u>", "</u>",
]
b1, a1 = s1(base), s1(applied)
print("== counts in §1 (base -> applied)")
rows = []
for t in TERMS:
    rows.append((t, b1.count(t), a1.count(t)))
    print(f"  {t!r}: {b1.count(t)} -> {a1.count(t)}")
print("== counts in the whole document (base -> applied)")
for t in ["<u>", "</u>"]:
    print(f"  {t!r}: {base.count(t)} -> {applied.count(t)}")

json.dump({"doc_base": len(base), "doc_applied": len(applied), "s1_base": len(b1), "s1_applied": len(a1),
           "delta": d_doc, "counts": rows}, open(f"{S}/cut/counts.json", "w"), indent=1)
open(f"{S}/cut/applied.md", "w").write(applied)
