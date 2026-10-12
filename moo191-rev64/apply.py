#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-191 store revision 64 — apply kit.

One bill edit (the F10 designation-review advisory, MOO-188 §3.3, verbatim) plus the record layer.
Derives every label from the LIVE body, asserts every anchor count before touching anything, and
asserts every post-condition before writing. Never hand-edit a body in context; run this.

    python3 apply.py --dry-run     # writes out-body.md, sends nothing
    python3 apply.py               # applies and verifies from the returned JSON
"""
import json, os, re, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits import EDITS, UNTOUCHED
from rec_patches import PATCHES

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
HERE = os.path.dirname(os.path.abspath(__file__))


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
    """Enacted §1 only — located by content, never by line index."""
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def derive(b):
    """Labels from the LIVE body. §0 and §6 are keyed to the store revision number; §5 is a
    sequence, because a record-only revision writes a §0 narrative and no sweep."""
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    s5 = max(int(m.group(1)) for m in re.finditer(r"^### §?5\.(\d+) ", b, re.M))
    s6prev = max(int(m.group(1)) for m in re.finditer(r"^### §?6\.0-(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ October", b).group(1))
    rev = s0 + 1
    assert hdr <= s0, f"byline says {hdr} but the §0 record is only at {s0}"
    if hdr != s0:
        print(f"  !! byline drift: the byline says store revision {hdr}, the §0 record is at {s0}; "
              f"the byline is corrected to {rev} by this revision")
    assert not re.search(rf"^### §?6\.0-{rev} ", b, re.M), f"§6.0-{rev} already exists"
    return dict(rev=rev, s0=s0, s5=s5 + 1, s6=rev, s6prev=s6prev, byline=hdr)


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body = doc["body"]
    live_rev = doc["latestRevisionId"]
    L = derive(body)
    B1 = sec1(body)
    print(f"live latestRevisionId = {live_rev} (revision number {doc.get('latestRevisionNumber')})")
    print(f"base: store revision {L['s0']}, {len(body)} chars, §1 {len(B1)} chars")
    print(f"derived: this is store revision {L['rev']}, sweep §5.{L['s5']}, note §6.0-{L['s6']}")
    if L["rev"] != 63:
        print(f"  !! MOO-191 commissioned this cut as store revision 63; the live record is at "
              f"{L['s0']}, so it is cut and recorded as store revision {L['rev']}")
    assert L["rev"] == 65 and L["s5"] == 43, (
        f"the record files are written for store revision 65 / §5.43; the live body makes this "
        f"store revision {L['rev']} / §5.{L['s5']}. Re-word rec_s0/s5/s6/s8 and rec_patches "
        f"before applying — do not let the kit relabel prose it cannot re-reason.")

    # ---- 1. the bill edit: counts re-resolved on the base as it stands ----
    for e in EDITS:
        c, c1 = body.count(e["find"]), B1.count(e["find"])
        print(f"   {e['id']}: FIND {len(e['find'])} chars, count {c} in the document, {c1} in §1, "
              f"delta {len(e['repl']) - len(e['find']):+d}")
        assert c == e["n"], f"{e['id']}: document count {c}, expected {e['n']}"
        assert c1 == e["n1"], f"{e['id']}: §1 count {c1}, expected {e['n1']}"
    assert len(EDITS) == 1 and len(EDITS[0]["find"]) == 164 and len(EDITS[0]["repl"]) == 301, \
        "the Director's FIND/READ are 164 and 301 characters — one of them has been altered"

    out = body
    for e in EDITS:
        out = out.replace(e["find"], e["repl"])

    # ---- 2. record layer -------------------------------------------------
    byline_f = (f"**MOO-42 · Drafting Specialist · store revision {L['byline']} · 12 October 2026 "
                f"· INTERNAL WORKING DRAFT — pre-decisional**")
    byline_r = byline_f.replace(f"store revision {L['byline']}", f"store revision {L['rev']}")
    assert out.count(byline_f) == 1, f"byline {byline_f!r} occurs {out.count(byline_f)} times"
    out = out.replace(byline_f, byline_r)
    for p in PATCHES:
        c = out.count(p["find"])
        assert c == p["n"], f"{p['id']} ({p['label']}): found {c}, expected {p['n']}"
    for p in PATCHES:
        out = out.replace(p["find"], p["repl"])
    print(f"applied {len(EDITS)} bill edit + {len(PATCHES)} record patches")

    def load(path):
        t = open(os.path.join(HERE, path), encoding="utf-8").read().rstrip("\n")
        return t

    for anchor, text in ((f"### 0.0-{L['s0']} ", load("rec_s0.md")),
                         (f"### §5.{L['s5']-1} ", load("rec_s5.md")),
                         (f"### §6.0-{L['s6prev']} ", load("rec_s6.md"))):
        assert out.count(anchor) == 1, f"insertion anchor {anchor!r} occurs {out.count(anchor)} times"
        out = out.replace(anchor, text + "\n\n" + anchor)

    s8 = "## 8. Status and next step\n\n"
    assert out.count(s8) == 1
    out = out.replace(s8, s8 + load("rec_s8.md") + "\n\n")

    # ---- 3. post-conditions ----------------------------------------------
    N1 = sec1(out)
    assert len(B1.split("\n")) == len(N1.split("\n")), "§1 line count changed"
    changed = [i for i, (x, y) in enumerate(zip(B1.split("\n"), N1.split("\n"))) if x != y]
    assert len(changed) == 1, f"expected exactly 1 changed §1 line, got {len(changed)}: {changed}"
    assert len(N1) - len(B1) == 137, f"§1 delta {len(N1) - len(B1):+d}, expected +137"
    assert N1.count("<u>") == B1.count("<u>") == 60, "§1 <u> count moved"
    assert N1.count("</u>") == B1.count("</u>") == 60, "§1 </u> count moved"
    # the document's raw count goes +2: §0.0-65's block quote of the enacted words, and that
    # narrative's own code-span mention of the two tags. The balance must stay equal.
    assert out.count("<u>") == out.count("</u>") == body.count("<u>") + 2, \
        f"document <u>/</u> went {body.count('<u>')}/{body.count('</u>')} -> " \
        f"{out.count('<u>')}/{out.count('</u>')}, expected +2 and equal"
    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    # the nine anchors that belong to other open cuts, re-counted over §1 AFTER the substitution
    for tag, f in UNTOUCHED:
        c = N1.count(f)
        print(f"   untouched: {tag:38s} §1 count {c}")
        assert c == 1, f"{tag}: §1 count {c}, expected 1"
    # the vocabulary counts §5.43 states
    for phrase, want in (("subsection A of § 51.1-162", 1), ("designation of beneficiary", 1),
                         ("before completing payment", 3), ("is advised", 1),
                         ("subsection A of that section", 3), ("designation", 4), ("designated", 5),
                         ("every matter this subdivision requires to be stated", 1)):
        got = N1.count(phrase)
        assert got == want, f"§5.43 says {phrase!r} is {want} in §1 after the edit; it is {got}"
    print(f"post-conditions OK | §1 {len(B1)} -> {len(N1)} | doc {len(body)} -> {len(out)} "
          f"| headroom {CEILING - len(out)} | §1 line changed {changed}")

    if "--dry-run" in sys.argv:
        open(os.path.join(HERE, "out-body.md"), "w", encoding="utf-8").write(out)
        print("DRY RUN — body written to out-body.md, nothing sent")
        return

    # ---- 4. write and verify from the returned JSON -----------------------
    title = re.sub(r"store revision \d+", f"store revision {L['rev']}", doc.get("title") or "")
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title, "format": "markdown", "body": out, "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    got = res.get("body", "")
    assert got == out, f"returned body differs: {len(got)} vs {len(out)}"
    print(f"WRITE OK — document revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(got)} characters, store revision {L['rev']}")
    json.dump({"rev": L["rev"], "s5": L["s5"], "s6": L["s6"], "baseRevisionId": live_rev,
               "revisionId": res.get("latestRevisionId"), "len": len(got), "sec1": len(sec1(got))},
              open(os.path.join(HERE, "out-labels.json"), "w"), indent=1)


main()
