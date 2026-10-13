#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-208 store revision 72 — RECORD ONLY. MOO-211's counsel pass, disposed into the record.

No word of any section in the act changes. The decisive post-condition is therefore not a
character delta but an IDENTITY: §1 after must be byte-for-byte §1 before. That is the rule
MOO-211 §5 established against this kit's own record patch R5 — a matching delta is a checksum,
a diff is a proof — and this is the first kit to carry it.

Following the convention this file sets for store revisions 64 and 68, a record-only revision
writes a §0 narrative and a §8 status note and NO §5 sweep and NO §6 note: there is no
cross-reference to chase when no citation moves.

    python3 rec72.py --dry-run    # writes out-body-72.md, sends nothing
    python3 rec72.py              # applies and verifies from the returned JSON
"""
import difflib, json, os, re, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rec_patches72 import PATCHES
from cures import CURES, build

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
HERE = os.path.dirname(os.path.abspath(__file__))
THIS_REV = 72


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def req(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(base() + path, data=data, method=method, headers={
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
    """Enacted §1 only — located by content, never by line index."""
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def load(p):
    return open(os.path.join(HERE, p), encoding="utf-8").read().rstrip("\n")


def derive(b):
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ \w+ 2026", b).group(1))
    rev = s0 + 1
    assert hdr <= s0, f"byline says {hdr} but the §0 record is only at {s0}"
    assert not re.search(rf"^### 0\.0-{rev} ", b, re.M), f"§0.0-{rev} already exists"
    return dict(rev=rev, s0=s0, byline=hdr)


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live_rev = doc["body"], doc["latestRevisionId"]
    L = derive(body)
    B1 = sec1(body)
    print(f"live latestRevisionId = {live_rev} (number {doc.get('latestRevisionNumber')})")
    print(f"base: store revision {L['s0']}, {len(body)} chars, §1 {len(B1)} chars, "
          f"<u>/</u> {B1.count('<u>')}/{B1.count('</u>')}")
    print(f"derived: this is store revision {L['rev']}")
    assert L["rev"] == THIS_REV, (
        f"the record files are written for store revision {THIS_REV}; the live body makes this "
        f"store revision {L['rev']}. Re-word rec_s0_72 / rec_s8_72 / rec_patches72 before "
        f"applying — do not let the kit relabel prose it cannot re-reason.")

    # ---- 1. the six cures still anchor, on the base this revision is actually writing on ----
    # The record prose asserts this. Assert it here too, so the prose cannot go stale silently.
    print("\nthe six cures counsel proposes, re-counted on this base (none is applied here):")
    for c in CURES:
        f, r = build(c, tagged=False)
        n = B1.count(f)
        d = len(r) - len(f)
        print(f"   {c['id']:<3} FIND {len(f):>4} chars  {n}x in §1  {d:+5d}  "
              f"{'OK' if n == 1 and d == c['delta'] else '*** CHECK ***'}  {c['where']}")
        assert n == 1, f"{c['id']}: FIND resolves {n}x in §1 — the record prose would be wrong"
        assert d == c["delta"], f"{c['id']}: measured {d:+d}, cures.py says {c['delta']:+d}"
        after = B1.replace(f, r, 1)
        assert after.count("<u>") == 62 and after.count("</u>") == 62, \
            f"{c['id']}: the untagged cure moves §1's tag count"

    # ---- 2. the record layer -----------------------------------------------------------
    out = body
    bm = re.search(r"\*\*MOO-42 · Drafting Specialist · store revision \d+ · "
                   r"\d+ \w+ 2026 · INTERNAL WORKING DRAFT — pre-decisional\*\*", out)
    assert bm, "byline not found"
    byline_f = bm.group(0)
    byline_r = byline_f.replace(f"store revision {L['byline']}", f"store revision {L['rev']}")
    assert out.count(byline_f) == 1, f"byline occurs {out.count(byline_f)} times"
    assert byline_r != byline_f, f"byline label not advanced: {byline_f}"
    out = out.replace(byline_f, byline_r)
    print(f"\n   byline -> {byline_r}")

    for p in PATCHES:
        c = out.count(p["find"])
        assert c == p["n"], f"{p['id']} ({p['label']}): found {c}, expected {p['n']}"
    for p in PATCHES:
        out = out.replace(p["find"], p["repl"])
        print(f"   {p['id']}: {p['label']}  {len(p['repl']) - len(p['find']):+d}")

    anchor = f"### 0.0-{L['s0']} "
    assert out.count(anchor) == 1, f"§0 anchor {anchor!r} occurs {out.count(anchor)} times"
    out = out.replace(anchor, load("rec_s0_72.md") + "\n\n" + anchor)

    s8 = "## 8. Status and next step\n\n"
    assert out.count(s8) == 1
    out = out.replace(s8, s8 + load("rec_s8_72.md") + "\n\n")

    # ---- 3. post-conditions. The first one is the only one that matters. ----------------
    N1 = sec1(out)
    print(f"\n   §1        {len(B1)} -> {len(N1)}  ({len(N1) - len(B1):+d})")
    print(f"   document  {len(body)} -> {len(out)}  ({len(out) - len(body):+d})")

    # IDENTITY, not delta. R5's own correction, applied to the kit that wrote it.
    if N1 != B1:
        d = list(difflib.unified_diff(B1.splitlines(), N1.splitlines(), lineterm="", n=0))
        sys.exit("§1 CHANGED in a record-only revision — nothing written.\n" + "\n".join(d[:40]))
    print("   §1 identity: byte-for-byte unchanged (diff, not delta) — OK")

    # And the record-only convention: no new §5 sweep, no new §6 note.
    for pat, lbl, want in ((r"^### §?5\.(\d+) ", "§5", 0), (r"^### §?6\.0-(\d+) ", "§6", 0)):
        b4 = set(re.findall(pat, body, re.M))
        af = set(re.findall(pat, out, re.M))
        assert af == b4, f"{lbl} headings changed: added {af - b4}, lost {b4 - af}"
        print(f"   {lbl} headings unchanged ({len(af)}) — record-only convention held")
    assert out.count(f"### 0.0-{L['rev']} ") == 1, "§0.0-72 not unique"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert len(out) < CEILING, (
        f"over ceiling: {len(out)} > {CEILING}. §6.0-63 and §6.0-65 are the next to rotate out.")
    # The <u> counts are a property of §1, which is identical; assert anyway, cheaply.
    assert N1.count("<u>") == N1.count("</u>") == 62
    print(f"post-conditions OK | headroom {CEILING - len(out)}")

    if "--dry-run" in sys.argv:
        open(os.path.join(HERE, "out-body-72.md"), "w", encoding="utf-8").write(out)
        print("DRY RUN — body to out-body-72.md, nothing sent")
        return

    title = doc.get("title") or ""
    nt = re.sub(r"store revision \d+", f"store revision {L['rev']}", title)
    if "record only" not in nt.lower():
        nt = nt.rstrip() + " — store revision 72 record only"
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": nt[:300], "format": "markdown", "body": out,
                   "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:600]}")
        sys.exit(2)
    if res.get("body") != out:
        print("WRITE RETURNED A DIFFERENT BODY — treat as failed")
        sys.exit(2)
    rb = res["body"]
    assert sec1(rb) == B1, "returned body's §1 is not the base's §1"
    print(f"WRITE OK — revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(rb)} chars")
    print(f"title: {res.get('title')}")
    print("verified from the returned JSON: §1 byte-for-byte unchanged, "
          f"store revision {L['rev']} record only")


if __name__ == "__main__":
    main()
