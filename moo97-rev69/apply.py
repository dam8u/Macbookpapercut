#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 69 of bill-text-s8 — the Policy Director's four answers of 12 October 2026.

Derives every label from the LIVE body and REFUSES to run if the derived label is not the one the
prose was written for. Substitutes inside the §1 slice only, asserts every anchor count before it
touches anything and every post-condition before it writes, and verifies the write from the
returned JSON rather than inferring it.

    python3 apply.py --dry-run     # writes out-body.md / out-items.md, sends nothing
    python3 apply.py               # writes both documents and verifies the responses
"""
import json, os, re, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from edits import EDITS, UNTOUCHED, TERMS
from rec_patches import PATCHES
from items_patch import SLICES

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
ITEMS_KEY = "bill-text-s8-item-list"

REV, S5, S6 = 69, 46, 69                 # what the prose in rec_*.md was written for
PER_EDIT = {"69-A": 354, "69-B": 211, "69-C": 292, "69-D": -345, "69-E": 345}
S1_DELTA = 857
HEADROOM_CLAIM = 41000                   # stated in the §5 preamble patch R1

S1_START = re.compile(r"^## 1\. The bill[ \t]*$", re.M)
S1_END = re.compile(r"^## 2\. Section-by-section summary", re.M)
ITEM = re.compile(r"^(\d+)\. ", re.M)
RETAINED = "\n\n### 7.1 Retained record"


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


def bounds(b):
    starts, ends = list(S1_START.finditer(b)), list(S1_END.finditer(b))
    assert len(starts) == 1, f"'## 1. The bill' resolves {len(starts)} times"
    assert len(ends) == 1, f"'## 2. Section-by-section' resolves {len(ends)} times"
    assert starts[0].start() < ends[0].start()
    return starts[0].start(), ends[0].start()


def sec1(b):
    s, e = bounds(b)
    return b[s:e]


def derive(b):
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    s5 = max(int(m.group(1)) for m in re.finditer(r"^### §?5\.(\d+) ", b, re.M))
    s6 = max(int(m.group(1)) for m in re.finditer(r"^### §?6\.0-(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ October", b).group(1))
    assert hdr == s0, f"the byline says {hdr} but the §0 record is at {s0}"
    return dict(s0=s0, rev=s0 + 1, s5prev=s5, s5=s5 + 1, s6prev=s6, s6=s0 + 1)


def load(path):
    return open(os.path.join(HERE, path), encoding="utf-8").read().rstrip("\n")


def item_positions(b):
    end = b.index(RETAINED)
    return [(int(m.group(1)), m.start()) for m in ITEM.finditer(b)], end


def check_items(b, where):
    pos, end = item_positions(b)
    nums = [n for n, _ in pos]
    assert nums == list(range(1, max(nums) + 1)), f"{where}: §7 not contiguous: {nums}"
    assert max(nums) == 134, f"{where}: §7 runs to {max(nums)}, expected 134"
    assert all(pos[i][1] < pos[i + 1][1] for i in range(len(pos) - 1)), \
        f"{where}: item numbers are out of document order"
    return nums, pos, end


def main():
    dry = "--dry-run" in sys.argv

    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live_rev = doc["body"], doc["latestRevisionId"]
    L = derive(body)
    s, e = bounds(body)
    s1 = body[s:e]
    print(f"live latestRevisionId = {live_rev} | document {len(body)} | §1 {len(s1)} [{s}:{e}]")
    print(f"derived: store revision {L['rev']}, sweep §5.{L['s5']}, note §6.0-{L['s6']}")
    assert (L["rev"], L["s5"], L["s6"]) == (REV, S5, S6), (
        f"the record files are written for store revision {REV}, sweep §5.{S5}, note §6.0-{S6}; "
        f"the live body makes them {L['rev']}, §5.{L['s5']}, §6.0-{L['s6']}. Re-word rec_s0/rec_s5/"
        f"rec_s6/rec_s8 and rec_patches before applying — the kit will not relabel prose it cannot "
        f"re-reason.")
    for lbl, n in ((f"### §5.{S5} ", "sweep"), (f"### §6.0-{S6} ", "note"),
                   (f"### 0.0-{REV} ", "narrative")):
        assert body.count(lbl) == 0, f"{n} heading {lbl!r} already exists"

    # ---- 1. assert every anchor before touching anything -----------------
    for ed in EDITS:
        assert body.count(ed["find"]) == ed["n"], \
            f"{ed['id']}: document count {body.count(ed['find'])}, expected {ed['n']}"
        assert s1.count(ed["find"]) == ed["n1"], \
            f"{ed['id']}: §1 count {s1.count(ed['find'])}, expected {ed['n1']}"
    for p in PATCHES:
        assert body.count(p["find"]) == p["n"], \
            f"{p['id']} ({p['label']}): document count {body.count(p['find'])}, expected {p['n']}"
        assert s1.count(p["find"]) == 0, f"{p['id']} is a record patch but resolves inside §1"
    for lbl, a in UNTOUCHED:
        assert s1.count(a) == 1, f"UNTOUCHED anchor BEFORE — {lbl}: §1 count {s1.count(a)}"
    print(f"asserted: {len(EDITS)} bill FINDs, {len(PATCHES)} record FINDs, "
          f"{len(UNTOUCHED)} untouched anchors each 1× in §1")

    before = {t: s1.count(t) for t in TERMS}
    u_before = (s1.count("<u>"), s1.count("</u>"))
    assert u_before == (62, 62), f"§1 markup is {u_before}, expected (62, 62)"

    # ---- 2. substitute in §1 only, then the record patches outside -------
    s1n = s1
    for ed in EDITS:
        s1n = s1n.replace(ed["find"], ed["repl"])
    out = body[:s] + s1n + body[e:]
    for p in PATCHES:
        out = out.replace(p["find"], p["repl"])
        print(f"   {p['id']}: {p['label'][:70]}  {len(p['repl']) - len(p['find']):+d}")

    # ---- 3. the record layer, inserted newest-first ----------------------
    for anchor, path in ((f"### 0.0-{L['s0']} ", "rec_s0.md"),
                         (f"### §5.{L['s5prev']} ", "rec_s5.md"),
                         (f"### §6.0-{L['s6prev']} ", "rec_s6.md")):
        assert out.count(anchor) == 1, f"insertion anchor {anchor!r} occurs {out.count(anchor)}×"
        out = out.replace(anchor, load(path) + "\n\n" + anchor)
    s8 = "## 8. Status and next step\n\n"
    assert out.count(s8) == 1
    out = out.replace(s8, s8 + load("rec_s8.md") + "\n\n")

    # the byline tracks the revision
    byl = f"**MOO-42 · Drafting Specialist · store revision {L['s0']} · 12 October 2026 · " \
          f"INTERNAL WORKING DRAFT — pre-decisional**"
    assert out.count(byl) == 1, f"byline occurs {out.count(byl)}×"
    out = out.replace(byl, f"**MOO-42 · Drafting Specialist · store revision {L['rev']} · "
                           f"13 October 2026 · INTERNAL WORKING DRAFT — pre-decisional**")

    # ---- 4. post-conditions ----------------------------------------------
    b1o, b1n = s1, sec1(out)
    assert b1n == s1n, "the §1 slice of the assembled body is not the substituted §1"
    assert len(b1o.split("\n")) == len(b1n.split("\n")), "§1 line count changed"
    changed = [i for i, (x, y) in enumerate(zip(b1o.split("\n"), b1n.split("\n"))) if x != y]
    assert len(changed) == 3, f"expected 3 changed §1 lines, got {len(changed)}: {changed}"
    per = {ed["id"]: len(ed["repl"]) - len(ed["find"]) for ed in EDITS}
    assert per == PER_EDIT, per
    assert len(b1n) - len(b1o) == S1_DELTA, f"§1 delta {len(b1n)-len(b1o)}, expected {S1_DELTA}"
    assert (b1n.count("<u>"), b1n.count("</u>")) == u_before, "§1 amendatory markup moved"
    du = out.count("<u>") - body.count("<u>")
    dc = out.count("</u>") - body.count("</u>")
    assert (du, dc) == (2, 1), (
        f"document markup went {du:+d}/{dc:+d}; expected +2/+1 — the two code spans in rec_s0.md "
        f"and rec_s8.md, less R5's stray closing tag, and nothing else")
    assert (body.count("<u>"), body.count("</u>")) == (78, 79), (
        f"the base's markup is {(body.count('<u>'), body.count('</u>'))}, expected (78, 79): R5 is "
        f"written to repair exactly one stray closing tag")
    assert out.count("<u>") == out.count("</u>") == 80, (
        f"document markup {out.count('<u>')}/{out.count('</u>')}, expected 80/80 — balanced for "
        f"the first time since the stray tag was written")
    for lbl, a in UNTOUCHED:
        assert b1n.count(a) == 1, f"UNTOUCHED anchor AFTER — {lbl}: §1 count {b1n.count(a)}"

    # f1-b's two conforming limbs and f4-a's two branches, asserted as text
    for needle, n in (("except that a retirement that is not a qualifying retirement", 1),
                      ("shall not be treated as having retired before the date of death", 1),
                      ("are the same as the person or persons to whom the benefit determined", 1),
                      ("are not the same as the person or persons to whom the benefit determined", 1),
                      ("shall not pay the benefit determined under the preceding sentence", 1),
                      ("the benefit it provides or the benefit", 0)):
        assert b1n.count(needle) == n, f"{needle[:50]!r}: {b1n.count(needle)}, expected {n}"
    # the greater-of branch must stay inside one sentence: no full stop before the semicolon branch
    g = b1n[b1n.index("Nothing in the preceding sentence reduces"):]
    g = g[:g.index("Where the member dies, the Board shall give written notice")]
    assert g.count("preceding sentence") == 5, f"{g.count('preceding sentence')} refs, expected 5"
    assert g.rstrip().endswith("."), "the greater-of slice does not end on a full stop"
    assert g.rstrip()[:-1].count(". ") == 0, (
        "the greater-of sentence has been split into two sentences, so at least one of its five "
        "'preceding sentence' references now has a new antecedent")

    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    assert f"@{L['s5']}@" in out and f"@{L['s5prev']}@" not in out, "the §5 preamble slot is stale"
    headroom = CEILING - len(out)
    assert abs(headroom - HEADROOM_CLAIM) < 1000, (
        f"the §5 preamble claims about {HEADROOM_CLAIM} characters of headroom and the real figure "
        f"is {headroom}")
    after = {t: b1n.count(t) for t in TERMS}
    print(f"post-conditions OK | §1 {len(b1o)} -> {len(b1n)} (+{len(b1n)-len(b1o)}) | "
          f"document {len(body)} -> {len(out)} | headroom {headroom} | §1 lines {changed}")
    print("  §1 term movement: " + ", ".join(f"{t} {before[t]}->{after[t]}"
                                             for t in TERMS if before[t] != after[t]))

    # ---- 5. the item list: two slice replacements, then the move ----------
    st, idoc = req("GET", f"/api/issues/{MOO42}/documents/{ITEMS_KEY}")
    assert st == 200, (st, idoc)
    ibody, irev = idoc["body"], idoc["latestRevisionId"]
    nums_b, pos_b, end_b = check_items(ibody, "BEFORE")
    stranded_b = [n for n, p in pos_b if p > end_b]
    print(f"item list {len(ibody)} chars | items 1..{max(nums_b)} | "
          f"stranded after §7.1: {stranded_b}")
    assert stranded_b == [132, 133, 134], f"expected 132-134 stranded, found {stranded_b}"

    iout = ibody
    for sp in SLICES:
        a = iout.find(sp["start"])
        assert a >= 0 and iout.count(sp["start"]) == 1, \
            f"{sp['id']}: start marker count {iout.count(sp['start'])}"
        z = iout.find(sp["end"], a)
        assert z >= 0 and iout.count(sp["end"]) == 1, \
            f"{sp['id']}: end marker count {iout.count(sp['end'])}"
        z += len(sp["end"])
        old = iout[a:z]
        if sp["must_contain"]:
            assert sp["must_contain"] in old, \
                f"{sp['id']}: the slice does not contain {sp['must_contain']!r}"
        iout = iout[:a] + sp["repl"] + iout[z:]
        print(f"   {sp['id']}: {sp['label'][:70]}  {len(sp['repl']) - len(old):+d}")

    # the move: items 132 to the end of the document, placed before the §7.1 heading
    pos, end = item_positions(iout)
    first = min(p for n, p in pos if n == 132)
    assert first > end, "item 132 is already inside the live list"
    block = iout[first:].rstrip("\n")
    head = iout[:first].rstrip("\n")
    assert head.endswith("resolves there, and §7's numbered items 1 to 70 are unaffected."), \
        "the §7.1 body does not end where the move expects it to"
    pre = head[:head.index(RETAINED)]
    retained = head[head.index(RETAINED):]
    iout = pre + "\n\n" + block + retained + "\n"
    print(f"   moved items 132-134 ({len(block)} chars) into the live list, before §7.1")

    nums_a, pos_a, end_a = check_items(iout, "AFTER")
    assert [n for n, p in pos_a if p > end_a] == [], "an item is still stranded after §7.1"
    assert nums_a == nums_b, "the item numbering changed"
    assert iout.count("<u>") == iout.count("</u>"), "item-list markup unbalanced"
    assert len(iout) < CEILING, f"item list over ceiling: {len(iout)}"
    for probe in ("route (b) is DECLINED by the Policy Director",
                  "THE CARD IS ANSWERED AND THREE OF THE FOUR ANSWERS ARE IN THE TEXT",
                  "**NEW IN STORE REVISION 68, out of [MOO-195](/MOO/issues/MOO-195)'s pass 21"):
        assert iout.count(probe) == 1, f"{probe[:40]!r}: {iout.count(probe)}"
    assert "the recommendation in this item is HELD" not in iout, "the stale annotation survived"
    print(f"item list {len(ibody)} -> {len(iout)} | headroom {CEILING - len(iout)} | "
          f"items 1..{max(nums_a)} contiguous, none stranded")

    if dry:
        open(os.path.join(HERE, "out-body.md"), "w", encoding="utf-8").write(out)
        open(os.path.join(HERE, "out-items.md"), "w", encoding="utf-8").write(iout)
        open(os.path.join(HERE, "out-s1.md"), "w", encoding="utf-8").write(b1n)
        print("DRY RUN — out-body.md, out-items.md, out-s1.md written; nothing sent")
        return

    title = (f"Bill text — S8, §§ 51.1-142.2 and 51.1-162 amended and new § 51.1-142.4; "
             f"store revision {L['rev']} (INTERNAL WORKING DRAFT — not a DLS bill, "
             f"not reviewed by counsel)")
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title, "format": "markdown", "body": out,
                   "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"BILL WRITE FAILED {st}: {str(res)[:500]}")
        sys.exit(2)
    got = res.get("body", "")
    assert got == out, f"returned body differs: {len(got)} vs {len(out)}"
    print(f"BILL WRITE OK — document revision {res.get('latestRevisionId')}, {len(got)} chars, "
          f"store revision {L['rev']}, §1 {len(sec1(got))}")

    st, ires = req("PUT", f"/api/issues/{MOO42}/documents/{ITEMS_KEY}",
                   {"title": idoc.get("title"), "format": "markdown", "body": iout,
                    "baseRevisionId": irev})
    if st not in (200, 201):
        print(f"ITEM-LIST WRITE FAILED {st}: {str(ires)[:500]}")
        sys.exit(3)
    igot = ires.get("body", "")
    assert igot == iout, f"returned item list differs: {len(igot)} vs {len(iout)}"
    print(f"ITEM-LIST WRITE OK — document revision {ires.get('latestRevisionId')}, "
          f"{len(igot)} chars")

    json.dump({"rev": L["rev"], "s5": L["s5"], "s6": L["s6"], "baseRevisionId": live_rev,
               "baseLen": len(body), "baseS1Len": len(b1o),
               "billRevisionId": res.get("latestRevisionId"), "billLen": len(got),
               "s1Len": len(b1n), "s1Delta": len(b1n) - len(b1o), "perEdit": per,
               "headroom": CEILING - len(got), "u_s1": list(u_before),
               "itemsRevisionId": ires.get("latestRevisionId"), "itemsLen": len(igot),
               "terms": {t: [before[t], after[t]] for t in TERMS if before[t] != after[t]}},
              open(os.path.join(HERE, "out-labels.json"), "w"), indent=1)


main()
