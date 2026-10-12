#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create the bounded counsel-pass child issue for store revision 61."""
import json
import os
import sys
import urllib.request
import urllib.error

MOO97 = os.environ["PAPERCLIP_TASK_ID"]
COMPANY = os.environ["PAPERCLIP_COMPANY_ID"]
KEY = os.environ["PAPERCLIP_API_KEY"]
RUN = os.environ.get("PAPERCLIP_RUN_ID", "")
BASE = os.environ["PAPERCLIP_API_URL"].rstrip("/")
if BASE.endswith("/api"):
    BASE = BASE[:-4]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from edits import EDITS  # noqa: E402

REVIEWER = "d71e111e-1296-4d66-81ac-750dcc8d8681"

parts = [open(os.path.join(HERE, "rt_head.md")).read().rstrip(), ""]
for label, find, repl in EDITS:
    parts.append("### %s\n" % label)
    parts.append("**BEFORE** (store revision 60):\n\n> %s\n" % find.replace("\n", " "))
    parts.append("**AFTER** (store revision 61):\n\n> %s\n" % repl.replace("\n", " "))
parts.append("""---

**Read them against subdivisions G 4, D 1 and subsection M 2 whole** in [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) §1 — they are the three longest paragraphs of new § 51.1-142.4 — and against the live text of §§ 51.1-153, 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 on the Virginia LIS. **Verify each string against the live document before attacking it; the document moves under this issue regularly.**

**INTERNAL WORKING DRAFT. Not a Division of Legislative Services bill, not reviewed by DLS, not legally sufficient for introduction.**""")
body = "\n".join(parts)
open(os.path.join(HERE, "rt_desc.md"), "w").write(body)
print("description: %d chars" % len(body))

if "--write" not in sys.argv:
    print("DRY RUN")
    sys.exit(0)

payload = {
    "title": "Bounded counsel pass on store revision 61's thirteen substitutions — E1's cure of MOO-161's "
             "fatal finding by deletion and confinement, the certification's three restated propositions, "
             "the narrowed M 2 class, and the Director's five answers",
    "description": body,
    "parentId": MOO97,
    "assigneeAgentId": REVIEWER,
    "priority": "high",
    "status": "todo",
    "idempotencyKey": "moo97:counsel-pass:rev61",
}
req = urllib.request.Request(BASE + "/api/companies/%s/issues" % COMPANY,
                             data=json.dumps(payload).encode(), method="POST")
req.add_header("Authorization", "Bearer " + KEY)
req.add_header("Content-Type", "application/json")
if RUN:
    req.add_header("X-Paperclip-Run-Id", RUN)
try:
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read().decode() or "{}")
        d = d.get("issue", d)
        print("CREATED:", d.get("identifier"), d.get("id"), d.get("status"), d.get("assigneeAgentId"))
        json.dump({"id": d.get("id"), "identifier": d.get("identifier")},
                  open(os.path.join(HERE, "review-issue.json"), "w"))
except urllib.error.HTTPError as e:
    print("FAILED", e.code, e.read().decode()[:600])
    sys.exit(2)
