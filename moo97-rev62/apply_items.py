#!/usr/bin/env python3
import json, os, re, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from item128 import *
MOO42="2c806c8a-b486-4435-8904-dfb34e5f6d25"; KEY="bill-text-s8-item-list"
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

st,doc=req("GET",f"/api/issues/{MOO42}/documents/{KEY}"); assert st==200,(st,doc)
b=doc["body"]; live=doc["latestRevisionId"]
nums=[int(m.group(1)) for m in re.finditer(r"^(\d{1,3})\. ", b, re.M)]
assert nums==list(range(1,max(nums)+1)), f"item list not contiguous before: max {max(nums)}"
nxt=max(nums)+1
print(f"live rev {live} | items contiguous 1..{max(nums)} | next item = {nxt}")
item=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"item129.md")).read().rstrip("\n")
if nxt!=129:
    print(f"  !! item number moved: planned 129, live says {nxt} — relabelling")
    item=re.sub(r"^129\. ", f"{nxt}. ", item)
    item=item.replace("§7 item 129", f"§7 item {nxt}")
for f,n in ((FIND_128_HEAD,1),(TITLE_FIND,1),(ANCHOR_129,1)):
    assert b.count(f)==n, f"anchor count {b.count(f)} != {n} for {f[:60]!r}"
out=b.replace(FIND_128_HEAD,REPL_128_HEAD).replace(TITLE_FIND,TITLE_REPL.replace("129",str(nxt)))
out=out.replace(ANCHOR_129, "\n"+item+"\n"+ANCHOR_129)
nums2=[int(m.group(1)) for m in re.finditer(r"^(\d{1,3})\. ", out, re.M)]
assert nums2==list(range(1,nxt+1)), f"item list not contiguous after: {[n for n in range(1,nxt+1) if n not in nums2]}"
print(f"post: contiguous 1..{nxt} | {len(b)} -> {len(out)}")
if "--dry-run" in sys.argv: print("DRY RUN"); sys.exit(0)
st,res=req("PUT",f"/api/issues/{MOO42}/documents/{KEY}",
           {"title":doc.get("title"),"format":"markdown","body":out,"baseRevisionId":live})
if st not in (200,201): print(f"WRITE FAILED {st}: {str(res)[:400]}"); sys.exit(2)
assert res.get("body")==out, "returned body differs"
print(f"WRITE OK — item list revision {res.get('latestRevisionId')}, {len(out)} characters, item {nxt} added")
