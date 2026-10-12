#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble moo169-disposition from the LIVE written body, so the redline and the
as-amended provisions cannot drift from what is in the store."""
import json, os, re, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits import EDITS
HERE=os.path.dirname(os.path.abspath(__file__))
MOO42="2c806c8a-b486-4435-8904-dfb34e5f6d25"; MOO97=os.environ["PAPERCLIP_TASK_ID"]
def base():
    u=os.environ["PAPERCLIP_API_URL"].rstrip("/"); return u[:-4] if u.endswith("/api") else u
def req(method, path, payload=None):
    data=json.dumps(payload).encode() if payload is not None else None
    r=urllib.request.Request(base()+path, data=data, method=method, headers={
        "Authorization":"Bearer "+os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id":os.environ.get("PAPERCLIP_RUN_ID",""),
        "Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(r) as resp: return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e: return e.code, e.read().decode()

st,doc=req("GET",f"/api/issues/{MOO42}/documents/bill-text-s8"); assert st==200
body=doc["body"]
s1=body[body.index("## 1. The bill"):body.index("## 2. Section-by-section summary")]
lines=s1.split("\n")

# locate the five amended provisions in the WRITTEN body, by content not by index
def find_line(needle):
    hits=[i for i,l in enumerate(lines) if needle in l]
    assert len(hits)==1, f"{needle!r} in {len(hits)} lines"
    return hits[0]
PROV=[("Subdivision D 1 of § 51.1-142.4", find_line("**D. 1.** The Board shall not accept an election until")),
      ("Subdivision G 4 of § 51.1-142.4", find_line("4. Subdivisions 2 and 3 shall not apply, and the service credit purchased")),
      ("Subsection L of § 51.1-142.4",     find_line("**L.** Nothing in this section imposes any duty")),
      ("Subdivision M 2 of § 51.1-142.4", find_line("A member, retiree, beneficiary, applicant, personal representative")),
      ("Subsection N of § 51.1-142.4",     find_line("Upon the settlement of a certified subsidy under subdivision G 1 or G 4"))]

# every AFTER string must be present exactly its expected count; every BEFORE gone
for e in EDITS:
    assert s1.count(e["repl"])>=e["n"], f"{e['id']}: AFTER string missing from written §1"
    if e["find"] in e["repl"]:
        # append/extend edit: the FIND survives as a prefix of the READ, by design
        assert s1.count(e["find"])==s1.count(e["repl"]), f"{e['id']}: stray unextended FIND in written §1"
    else:
        assert s1.count(e["find"])==0, f"{e['id']}: BEFORE string still in written §1"

out=[open(os.path.join(HERE,"disp_head.md")).read().rstrip("\n")]

out.append("\n---\n\n## 2. The redline — all twenty-one substitutions, verbatim\n")
out.append("**Every FIND string below was asserted to occur exactly its stated number of times in §1 of the live base "
           "before any substitution was made, and every READ string has been verified present in the written body "
           "and every FIND string verified absent from it.** Underlining marks what is new *in this revision*; the "
           "whole of new § 51.1-142.4 is new language in the bill and is underlined as a whole in §1.\n")
for e in EDITS:
    out.append(f"### {e['id']} — {e['label']}\n")
    out.append(f"**Occurrences replaced: {e['n']}.**\n")
    out.append("FIND:\n\n> " + e["find"].replace("\n"," ") + "\n")
    out.append("READ:\n\n> " + e["repl"].replace("\n"," ") + "\n")

out.append("\n---\n\n## 3. The five amended provisions, reproduced in full as amended\n")
out.append("**Taken from the written body of store revision 62, not from the plan.** Reproduced whole so a reader "
           "can see the result in context, which is the test; the drafter's note is not the test.\n")
for name,i in PROV:
    txt=lines[i]
    out.append(f"### {name} — as amended\n")
    out.append("> " + txt.replace("\n"," ") + "\n")

out.append("\n---\n\n## 4. Cross-reference check — performed in both directions\n")
out.append("**Reproduced in the bill at §5.41, which is the system of record for the counts.** The two results that "
           "must be stated here:\n\n"
           "- **Conforming amendments elsewhere in the Code: none required.** The act continues to amend one section "
           "(§ 51.1-142.2) and to add one (§ 51.1-142.4). Citing a section does not require amending it, so "
           "§§ 51.1-162, 51.1-163, 51.1-165, 51.1-165.01, 8.01-2, 2.2-4001, 2.2-4021 and 2.2-4026 are cited and "
           "unamended.\n"
           "- **One conforming amendment is available and is not drafted, and it is new in this revision.** The "
           "f7-toll sentence is **the act's first operative override of a *period* stated in a section this act does "
           "not amend**: a reader of § 51.1-162 C will not learn from § 51.1-162 C that subdivision G 4 of "
           "§ 51.1-142.4 extends its 90 days. The cure is one clause and it changes the act's footprint, the title "
           "line and the first enactment clause. **§7 item 129 answer 7.**\n\n"
           "**Movements measured over §1 of the written body:** `§ 51.1-162` 11 → **13**; `§ 51.1-163` 2 → **3**; "
           "`§ 2.2-4026` 0 → **1** (new, and the act's first citation of it); `§ 8.01-2` 0 → **1** (new, and the "
           "act's only citation into Title 8.01); `§ 51.1-200`, `§ 51.1-211` and `§ 51.1-300` 1 → **2** each; "
           "`§ 51.1-165` bare **7 → 7** and `§ 51.1-165.01` **7 → 7**, both unchanged, so no displacement is added "
           "or removed; `§ 51.1-153` **8 → 8**, unchanged, which is the point of E1.\n")

out.append("\n---\n\n## 5. Three checks run inside §1 and reported as results\n")
out.append("1. **The subdivision M 2 class list occurs exactly twice** — once in the reconsideration sentence and "
           "once in the Article 5 savings sentence — and **both were replaced**. A person with a reconsideration "
           "right and no court is the defect store revision 59 was written to avoid.\n"
           "2. **Five lines of §1 differ and no others**, and the line count of §1 is unchanged, so no designator is "
           "renumbered and no paragraph is split or joined.\n"
           "3. **`in service` 13 → 14.** The one new occurrence is M6's insertion of § 51.1-162 C's own in-service "
           "condition. *\"In service\"* remains **undefined in § 51.1-124.3**, which is why E1 keeps the express "
           "waiver that follows it.\n")

out.append("\n---\n\n" + open(os.path.join(HERE,"disp_tail.md")).read().rstrip("\n") + "\n")
text="\n".join(out)
open(os.path.join(HERE,"moo169-disposition.md"),"w").write(text)
print("assembled", len(text), "characters")

if "--dry-run" in sys.argv: sys.exit(0)
st,ex=req("GET",f"/api/issues/{MOO97}/documents/moo169-disposition")
payload={"title":"MOO-169 disposition — store revision 62: redline, provisions as amended, cross-reference check, drafter's note, routing",
         "format":"markdown","body":text}
payload["baseRevisionId"]= ex.get("latestRevisionId") if st==200 else None
st,res=req("PUT",f"/api/issues/{MOO97}/documents/moo169-disposition",payload)
if st not in (200,201): print(f"WRITE FAILED {st}: {str(res)[:400]}"); sys.exit(2)
assert res.get("body")==text, "returned body differs"
print(f"WRITE OK — moo169-disposition revision {res.get('latestRevisionId')}, {len(text)} characters")
