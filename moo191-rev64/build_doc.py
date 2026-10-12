#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the MOO-191 deliverable document from doc_head.md + the LIVE store body.

Subdivision D 1 as amended, the title line and the enactment clauses are spliced from
`bill-text-s8` at the moment of assembly and never hand-carried. Writes moo191.md and, unless
--dry-run, PUTs it as the issue document `moo191-advisory-cut` on MOO-191.
"""
import json, os, re, sys, urllib.request, urllib.error

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
MOO191 = os.environ["PAPERCLIP_TASK_ID"]
KEY = "moo191-advisory-cut"
HERE = os.path.dirname(os.path.abspath(__file__))
NEW = ("that the member is advised to review the member's designation of beneficiary "
       "under subsection A of § 51.1-162 before completing payment; ")


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def req(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(base() + path, data=data, method=method, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", ""),
        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


st, doc = req("GET", f"/api/issues/{MOO42}/documents/bill-text-s8")
assert st == 200, (st, doc)
body = doc["body"]
i = body.index("\n## 1.")
m = re.search(r"\n## (?!1\.)", body[i + 5:])
S = body[i:i + 5 + m.start()]
LINES = [l.strip() for l in S.split("\n") if l.strip()]


def line(prefix):
    hits = [l for l in LINES if re.sub(r"<u>|\*\*|~~", "", l).startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0]


D1 = line("D. 1. The Board shall not accept an election")
assert D1.count(NEW) == 1, D1.count(NEW)
# the same provision with the enacted words visibly flagged, for the reader who wants the diff
D1_FLAG = D1.replace(NEW, "**" + NEW.rstrip() + "** ", 1)
TITLE = line("A BILL to amend and reenact") if any(
    re.sub(r"<u>|\*\*|~~", "", l).startswith("A BILL to amend and reenact") for l in LINES) else None
ENACT = [l for l in LINES if re.match(r"^(\d+)\. That ", re.sub(r"<u>|\*\*|~~", "", l))]

head = open(os.path.join(HERE, "doc_head.md"), encoding="utf-8").read().rstrip("\n")
out = head.replace("{{D1}}", D1).replace("{{D1_FLAG}}", D1_FLAG)
out = out.replace("{{TITLE}}", TITLE or "_(the title line is reproduced in the store body)_")
out = out.replace("{{ENACT}}", "\n\n".join(ENACT) if ENACT else "_(see the store body)_")
out = out.replace("{{REVID}}", doc["latestRevisionId"]).replace("{{REVNO}}", str(doc["latestRevisionNumber"]))
out = out.replace("{{DOCLEN}}", f"{len(body):,}").replace("{{S1LEN}}", f"{len(S):,}")
assert "{{" not in out, out[out.index("{{"):out.index("{{") + 80]
open(os.path.join(HERE, "moo191.md"), "w", encoding="utf-8").write(out)
print(f"assembled {len(out)} characters | D 1 {len(D1)} | enactment clauses {len(ENACT)}")

if "--dry-run" in sys.argv:
    print("DRY RUN — nothing sent")
    sys.exit(0)

st, cur = req("GET", f"/api/issues/{MOO191}/documents/{KEY}")
payload = {"title": "MOO-191 — the designation-review advisory, cut as store revision 65 (INTERNAL WORKING DRAFT)",
           "format": "markdown", "body": out,
           "baseRevisionId": cur["latestRevisionId"] if st == 200 else None}
st, res = req("PUT", f"/api/issues/{MOO191}/documents/{KEY}", payload)
if st not in (200, 201):
    print(f"WRITE FAILED {st}: {str(res)[:400]}")
    sys.exit(2)
assert res.get("body") == out
print(f"WRITE OK — {KEY} revision {res.get('latestRevisionId')} (number {res.get('latestRevisionNumber')})")
