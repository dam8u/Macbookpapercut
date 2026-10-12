#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits import EDITS
HERE=os.path.dirname(os.path.abspath(__file__))
RT_AGENT="d71e111e-1296-4d66-81ac-750dcc8d8681"
MOO97=os.environ["PAPERCLIP_TASK_ID"]
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

DIRECTOR={"E16":"f3-a + f3-b","E17":"f14-supp","E18":"f7-toll","E19":"m2-lateness","E20":"f10-b","E21":"f11-disclose"}
parts=[open(os.path.join(HERE,"rt_head.md")).read().rstrip("\n")]
parts.append("\n## The twenty-one substitutions, before and after, in full\n")
parts.append("**Each FIND string was asserted to occur exactly its stated number of times in §1 of store revision 61 "
             "before any substitution was made.** Twenty occur once; the subdivision M 2 class list occurs twice, "
             "once in each of its two lists, and both were replaced. **E16 to E21 are the Policy Director's approved "
             "answers, not findings** — attack them as drafting, not as policy; the policy is settled.\n")
for e in EDITS:
    tag=f" **[Director's answer {DIRECTOR[e['id']]}]**" if e["id"] in DIRECTOR else ""
    parts.append(f"### {e['id']} — {e['label']}{tag}\n")
    parts.append(f"Occurrences replaced: **{e['n']}**.\n")
    parts.append("**BEFORE:**\n\n> " + e["find"].replace("\n"," ") + "\n")
    parts.append("**AFTER:**\n\n> " + e["repl"].replace("\n"," ") + "\n")
parts.append("""
## Output bar

Severity-rated findings (fatal / serious / moderate / minor), each with the **exact words at fault**, the **authority quoted** from the live Code of Virginia, and a **concrete failure scenario** — named facts, a named loser, and the amount or right lost. State your **null results** as null results; a check you ran and that came back clean is worth as much to me as a finding. Re-verify every citation you rely on against Virginia LIS rather than against this description.

**You are not counsel of record. Nothing you write clears this draft, and `bill-text-s8` remains an internal working draft — not a Division of Legislative Services bill, not reviewed by DLS, not legally sufficient for introduction.**
""")
desc="\n".join(parts)
print("description", len(desc), "characters")
if "--dry-run" in sys.argv:
    open(os.path.join(HERE,"rt_desc.md"),"w").write(desc); sys.exit(0)
st,res=req("POST", f"/api/companies/{os.environ['PAPERCLIP_COMPANY_ID']}/issues", {
    "title":"Bounded counsel pass on store revision 62's twenty-one substitutions — E1's fourth cure of the death branch, E9's widened M 2 class, E7's single window, E11's charging rule, and the five restated propositions",
    "description":desc, "assigneeAgentId":RT_AGENT, "parentId":MOO97,
    "status":"todo", "priority":"high",
    "idempotencyKey":f"moo97-rev62-counsel-pass:{MOO97}"})
if st not in (200,201): print(f"CREATE FAILED {st}: {str(res)[:500]}"); sys.exit(2)
print("CREATED", res.get("identifier"), res.get("id"))
json.dump({"id":res.get("id"),"identifier":res.get("identifier")}, open(os.path.join(HERE,"review-issue.json"),"w"))
