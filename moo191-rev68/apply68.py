#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-191 store revision 68 — record-only apply kit.

No bill edit. Four in-place record corrections out of MOO-195's pass 21, a §0 narrative and a §8
note. Derives every label from the LIVE body and refuses to run if the derived label is not the one
the prose was written for. Asserts that §1 is character-for-character unchanged before it writes.

    python3 apply68.py --dry-run    # writes out-body.md, sends nothing
    python3 apply68.py              # applies and verifies from the returned JSON
"""
import json, os, re, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rec_patches68 import PATCHES

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
HERE = os.path.dirname(os.path.abspath(__file__))

# the enacted advisory, and the five FIND strings MOO-195 hands to drafting; each must resolve
# exactly once in §1 on the base as it stands, or the disposition is written against a dead anchor.
ADVISORY = ("that the member is advised to review the member's designation of beneficiary under "
            "subsection A of § 51.1-162 before completing payment;")
MOO195_FINDS = [
    ("F1/F2", ADVISORY),
    ("F3", "and the Board shall state every such failure in the report required by subsection J. "
           "The member shall file the notice of retirement required by § 51.1-153"),
    ("F4 FIND 1", "and no other designation has been made; that the member is advised to review the "
                  "member's designation of beneficiary under subsection A of § 51.1-162 before "
                  "completing payment; that subsection C of § 51.1-162"),
    ("F4 FIND 2", "in the order of precedence that section states."),
    ("F4 FIND 3", "; and that where no benefit is payable"),
    ("F9", "that the member is advised to review the member's designation"),
]


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
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ October", b).group(1))
    rev = s0 + 1
    assert hdr <= s0, f"byline says {hdr} but the §0 record is only at {s0}"
    assert not re.search(rf"^### 0\.0-{rev} ", b, re.M), f"§0.0-{rev} already exists"
    return dict(rev=rev, s0=s0, byline=hdr)


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body = doc["body"]
    live_rev = doc["latestRevisionId"]
    L = derive(body)
    B1 = sec1(body)
    print(f"live latestRevisionId = {live_rev} (revision number {doc.get('latestRevisionNumber')})")
    print(f"base: store revision {L['s0']}, {len(body)} chars, §1 {len(B1)} chars, "
          f"<u>/</u> {B1.count('<u>')}/{B1.count('</u>')}")
    print(f"derived: this is store revision {L['rev']}")
    assert L["rev"] == 68, (
        f"the record files are written for store revision 68; the live body makes this store "
        f"revision {L['rev']}. Re-word rec_s0_68/rec_s8_68 and rec_patches68 before applying — "
        f"do not let the kit relabel prose it cannot re-reason.")

    # ---- 1. anchors MOO-195's disposition depends on, re-counted on the base as it stands ----
    for tag, f in MOO195_FINDS:
        c, c1 = body.count(f), B1.count(f)
        print(f"   MOO-195 anchor {tag:10s} len {len(f):4d}  doc {c}  §1 {c1}")
        assert c1 == 1, f"{tag}: §1 count {c1}, expected 1 — the disposition's anchor is dead"
    series = B1[B1.index("The Board's certification shall also state that,"):]
    series = series[:series.index(". A failure to state in the Board's certification") + 1]
    SEP = re.compile(r"; (?:and )?that[ ,]")          # item 4 opens "; that, to the extent"
    items = len(SEP.findall(series)) + 1
    # +6 so the separator immediately before the advisory ("; that ") falls inside the slice
    at = len(SEP.findall(series[:series.index(ADVISORY) + 6])) + 1
    print(f"   series: {len(series)} chars, {items} items, advisory at item {at}")
    assert items == 7, f"the certification series has {items} items, expected 7"
    assert at == 5, f"the advisory is item {at} of the series, expected 5"

    out = body

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
        print(f"   {p['id']}: {p['label']}  {len(p['repl']) - len(p['find']):+d} chars")

    def load(path):
        return open(os.path.join(HERE, path), encoding="utf-8").read().rstrip("\n")

    anchor = f"### 0.0-{L['s0']} "
    assert out.count(anchor) == 1, f"insertion anchor {anchor!r} occurs {out.count(anchor)} times"
    out = out.replace(anchor, load("rec_s0_68.md") + "\n\n" + anchor)

    s8 = "## 8. Status and next step\n\n"
    assert out.count(s8) == 1
    out = out.replace(s8, s8 + load("rec_s8_68.md") + "\n\n")

    # ---- 3. post-conditions ----------------------------------------------
    N1 = sec1(out)
    assert N1 == B1, (
        f"§1 CHANGED — this revision is record only. {len(B1)} -> {len(N1)} characters")
    # §1 is byte-identical, so no amendatory markup moves. The document's raw counts go +1 each:
    # §0.0-68 states the live §1 <u>/</u> balance and mentions the two tags in one code span.
    du, dc = out.count("<u>") - body.count("<u>"), out.count("</u>") - body.count("</u>")
    assert du == dc == 1, (
        f"document <u>/</u> went {body.count('<u>')}/{body.count('</u>')} -> "
        f"{out.count('<u>')}/{out.count('</u>')} ({du:+d}/{dc:+d}); expected +1/+1, the §0.0-68 "
        f"code span and nothing else")
    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    # the anchors must still resolve after the record patches — the patches quote them
    for tag, f in MOO195_FINDS:
        assert sec1(out).count(f) == 1, f"{tag} no longer resolves 1x in §1 after the record layer"
    print(f"post-conditions OK | §1 unchanged at {len(N1)} | doc {len(body)} -> {len(out)} "
          f"| headroom {CEILING - len(out)}")

    if "--dry-run" in sys.argv:
        open(os.path.join(HERE, "out-body.md"), "w", encoding="utf-8").write(out)
        print("DRY RUN — body written to out-body.md, nothing sent")
        return

    title = re.sub(r"store revision \d+", f"store revision {L['rev']}", doc.get("title") or "")
    if "record only" not in title:
        title = title.replace(f"store revision {L['rev']}",
                              f"store revision {L['rev']} — record only")
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title, "format": "markdown", "body": out, "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    got = res.get("body", "")
    assert got == out, f"returned body differs: {len(got)} vs {len(out)}"
    print(f"WRITE OK — document revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(got)} characters, "
          f"store revision {L['rev']}, §1 {len(sec1(got))}")
    json.dump({"rev": L["rev"], "baseRevisionId": live_rev,
               "revisionId": res.get("latestRevisionId"), "len": len(got), "sec1": len(sec1(got))},
              open(os.path.join(HERE, "out-labels.json"), "w"), indent=1)


main()
