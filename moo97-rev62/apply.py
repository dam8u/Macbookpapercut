#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-97 store revision 62 — apply kit.

Derives every label from the LIVE body. Asserts every anchor count before
touching anything, and asserts every post-condition before writing. Never
hand-edit a body in context; run this.
"""
import json, os, re, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits import EDITS
from rec_patches import PATCHES

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"

def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u

def req(method, path, payload=None):
    url = base() + path
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", ""),
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()

def sec1(b):
    return b[b.index("## 1. The bill"):b.index("## 2. Section-by-section summary")]

def derive(b):
    """Every label from the live body. Matches '### 0.0-N', '### §5.N' and '### §5.N'-with-sign forms."""
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    s5 = max(int(m.group(1)) for m in re.finditer(r"^### §?5\.(\d+) ", b, re.M))
    s6 = max(int(m.group(1)) for m in re.finditer(r"^### §?6\.0-(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ October", b).group(1))
    assert hdr == s0, f"header says {hdr} but the §0 record is at {s0}"
    return dict(rev=s0 + 1, s0=s0, s5=s5 + 1, s6=s6 + 1)

def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body = doc["body"]
    live_rev = doc["latestRevisionId"]
    L = derive(body)
    print(f"live latestRevisionId = {live_rev}")
    print(f"derived: store revision {L['rev']}, sweep §5.{L['s5']}, note §6.0-{L['s6']}")
    for want, got, what in ((62, L["rev"], "store revision"), (41, L["s5"], "sweep"), (62, L["s6"], "note")):
        if want != got:
            print(f"  !! {what} label moved: planned {want}, live says {got} — relabelling record text")

    # ---- 1. assert every anchor, then substitute --------------------------
    out = body
    for e in EDITS + PATCHES:
        c = out.count(e["find"])
        assert c == e["n"], f"{e['id']} ({e['label']}): found {c}, expected {e['n']}"
    for e in EDITS + PATCHES:
        out = out.replace(e["find"], e["repl"])
    print(f"applied {len(EDITS)} bill edits + {len(PATCHES)} record patches")

    # ---- 2. record insertions, labels relabelled from the live body -------
    def load(p, subs):
        t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), p)).read().rstrip("\n")
        for a, b2 in subs:
            t = t.replace(a, b2)
        return t

    relabel = [("0.0-62", f"0.0-{L['rev']}"), ("§5.41", f"§5.{L['s5']}"), ("§6.0-62", f"§6.0-{L['s6']}"),
               ("store revision 62", f"store revision {L['rev']}"),
               ("STORE REVISION 62", f"STORE REVISION {L['rev']}")]

    ins = [
        (f"### 0.0-{L['s0']} ", load("rec_s0.md", relabel), "before"),
        (f"### §5.{L['s5']-1} ", load("rec_s5.md", relabel), "before"),
        (f"### §6.0-{L['s6']-1} ", load("rec_s6.md", relabel), "before"),
    ]
    for anchor, text, _ in ins:
        assert out.count(anchor) == 1, f"insertion anchor {anchor!r} occurs {out.count(anchor)} times"
        out = out.replace(anchor, text + "\n\n" + anchor)

    s8_anchor = "## 8. Status and next step\n\n"
    assert out.count(s8_anchor) == 1
    out = out.replace(s8_anchor, s8_anchor + load("rec_s8.md", relabel) + "\n\n")

    # ---- 3. post-conditions ----------------------------------------------
    b1o, b1n = sec1(body), sec1(out)
    assert len(b1o.split("\n")) == len(b1n.split("\n")), "§1 line count changed"
    changed = [i for i, (x, y) in enumerate(zip(b1o.split("\n"), b1n.split("\n"))) if x != y]
    assert len(changed) == 5, f"expected 5 changed §1 lines, got {len(changed)}: {changed}"
    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    assert "§ 51.1-163 shall not apply" not in sec1(out), "withdrawn words resurfaced in §1"
    print(f"post-conditions OK | §1 {len(b1o)} -> {len(b1n)} | doc {len(body)} -> {len(out)} "
          f"| headroom {CEILING - len(out)} | §1 lines changed {changed}")

    if "--dry-run" in sys.argv:
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out-body.md"), "w").write(out)
        print("DRY RUN — body written to out-body.md, nothing sent")
        return

    # ---- 4. write and verify from the returned JSON -----------------------
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": doc.get("title"), "format": "markdown",
                   "body": out, "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    got = res.get("body", "")
    assert got == out, f"returned body differs: {len(got)} vs {len(out)}"
    print(f"WRITE OK — document revision {res.get('latestRevisionId')}, {len(got)} characters, "
          f"store revision {L['rev']}")
    json.dump({"rev": L["rev"], "s5": L["s5"], "s6": L["s6"],
               "revisionId": res.get("latestRevisionId"), "len": len(got)},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out-labels.json"), "w"), indent=1)

main()
