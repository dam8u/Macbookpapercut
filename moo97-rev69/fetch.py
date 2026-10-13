import json, os, re, sys, urllib.request, urllib.error
HERE = os.path.dirname(os.path.abspath(__file__))
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u
def req(method, path, payload=None):
    url = base() + path
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID",""),
        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv)>1 else "bill-text-s8"
    out = sys.argv[2] if len(sys.argv)>2 else "live.md"
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{key}")
    assert st == 200, (st, str(doc)[:400])
    b = doc["body"]
    open(os.path.join(HERE,out),"w").write(b)
    meta = dict(key=key, latestRevisionId=doc["latestRevisionId"], title=doc.get("title"), len=len(b))
    json.dump(meta, open(os.path.join(HERE, out.replace(".md","-meta.json")),"w"), indent=1)
    print(json.dumps(meta, indent=1))
    for pat,lbl in ((r"^### 0\.0-(\d+) ","s0"),(r"^### §?5\.(\d+) ","s5"),(r"^### §?6\.0-(\d+) ","s6")):
        ns=[int(m.group(1)) for m in re.finditer(pat,b,re.M)]
        print(lbl, "max", max(ns) if ns else None, "count", len(ns))
    m=re.search(r"store revision (\d+) · \d+ October", b)
    print("byline:", m.group(0) if m else None)
