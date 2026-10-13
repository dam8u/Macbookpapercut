#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 73 of bill-text-s8 — the Policy Director's six approved cures, cut in one
revision, with the retention rotation the two preambles had named and the §7 item layer.

Derives every label from the LIVE body and refuses to run if the derived label is not the one the
record prose was written for. Substitutes inside the §1 slice only, **re-counts each anchor at
the moment it is applied, against its predecessors' output and never against the base**, and
proves §1's movement by a LINE DIFF rather than by a character delta — the rule MOO-211 R5 put in
place of the delta check, applied here for the first time to a revision that writes §1.

    python3 apply73.py --dry-run    # writes out-*.md, sends nothing
    python3 apply73.py              # writes the bill, vol 2 and the item list
"""
import json, os, re, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cures73 import CURES, PROPOSED, TERMS, UNTOUCHED, LINES_CHANGED, TOTAL, build
from moves73 import MOVES, PATCHES
from items73 import H135_F, H135_R, T135_F, T135_R, ITEM137, ITEM138

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY, VOL2_KEY, ITEMS_KEY = ("bill-text-s8", "bill-text-s8-revision-history-2",
                            "bill-text-s8-item-list")

REV, S5, S6 = 73, 49, 73          # what rec_s0/rec_s5/rec_s6/rec_s8 and moves73.py were written for
HEADROOM_IN = 21702               # quoted in every stub, in §5.49 check 7, in §0.0-73 and in §8
TOP_ITEM = 136                    # the item list the new items' prose is written against

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
        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def bounds(b):
    st, en = list(S1_START.finditer(b)), list(S1_END.finditer(b))
    assert len(st) == 1, f"'## 1. The bill' resolves {len(st)}×"
    assert len(en) == 1, f"'## 2. Section-by-section' resolves {len(en)}×"
    assert st[0].start() < en[0].start()
    return st[0].start(), en[0].start()


def sec1(b):
    s, e = bounds(b)
    return b[s:e]


def derive(b):
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    s5 = max(int(m.group(1)) for m in re.finditer(r"^### §?5\.(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ \w+ 2026", b).group(1))
    assert hdr == s0, f"the byline says {hdr} but the §0 record is at {s0}"
    return dict(s0=s0, rev=s0 + 1, s5prev=s5, s5=s5 + 1, s6=s0 + 1)


def load(p):
    return open(os.path.join(HERE, p), encoding="utf-8").read().rstrip("\n")


def cut(b, head, stop):
    assert b.count(head) == 1, f"{head!r} occurs {b.count(head)}×"
    a = b.index(head)
    z = b.index(stop, a)
    return b[a:z], a, z


def main():
    dry = "--dry-run" in sys.argv

    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live_rev = doc["body"], doc["latestRevisionId"]
    L = derive(body)
    s1 = sec1(body)
    head_in = CEILING - len(body)
    print(f"live latestRevisionId = {live_rev} (number {doc.get('latestRevisionNumber')})")
    print(f"base: store revision {L['s0']} | document {len(body)} | §1 {len(s1)} | "
          f"<u>/</u> {s1.count('<u>')}/{s1.count('</u>')} | headroom {head_in}")
    print(f"derived: store revision {L['rev']}, sweep §5.{L['s5']}, note §6.0-{L['s6']}")
    assert (L["rev"], L["s5"], L["s6"]) == (REV, S5, S6), (
        f"the record files are written for store revision {REV}, sweep §5.{S5}, note §6.0-{S6}; "
        f"the live body makes them {L['rev']}, §5.{L['s5']}, §6.0-{L['s6']}. Re-word the rec_*.md "
        f"files, moves73.py and items73.py before applying — this kit will not relabel prose it "
        f"cannot re-reason.")
    assert head_in == HEADROOM_IN, (
        f"every stub, §5.49 check 7, §0.0-73 and §8 quote {HEADROOM_IN} characters of inherited "
        f"headroom and the live figure is {head_in}. Re-word them before applying: a quoted "
        f"figure that is not the figure is the defect §6.0-71 item 10 is about.")
    for lbl, n in ((f"### §5.{S5} ", "sweep"), (f"### §6.0-{S6} ", "note"),
                   (f"### 0.0-{REV} ", "narrative")):
        assert body.count(lbl) == 0, f"{n} heading {lbl!r} already exists"

    # ---- 1. assert everything before touching anything ----------------------------------
    for lbl, a in UNTOUCHED:
        assert s1.count(a) == 1, f"UNTOUCHED anchor BEFORE — {lbl}: §1 count {s1.count(a)}"
    for p in PATCHES:
        assert body.count(p["find"]) == p["n"], \
            f"{p['id']} ({p['label']}): document count {body.count(p['find'])}, expected {p['n']}"
        assert s1.count(p["find"]) == 0, f"{p['id']} is a record patch but resolves inside §1"
    for mv in MOVES:
        sec, _, _ = cut(body, mv["head"], mv["stop"])
        assert "**Moved verbatim**" not in sec, (
            f"{mv['id']}: {mv['head']} is ALREADY A STUB. Re-stubbing a stub dates another "
            f"revision's move to this one. Drop it from MOVES.")
        assert len(sec) > 2000, f"{mv['id']}: {mv['head']} is only {len(sec)} chars — already thin"
    before = {t: s1.count(t) for t in (n for n, _, _ in TERMS)}
    for needle, b4, _ in TERMS:
        assert s1.count(needle) == b4, \
            f"BEFORE {needle[:40]!r}: §1 count {s1.count(needle)}, expected {b4}"
    print(f"asserted: {len(UNTOUCHED)} untouched anchors, {len(PATCHES)} record patches, "
          f"{len(MOVES)} movable sections none of which is a stub, {len(TERMS)} before-counts")

    # ---- 2. the six cures, inside §1, each anchor re-counted as it is applied -----------
    s, e = bounds(body)
    s1n = s1
    for c in CURES:
        f, r = build(c)
        n = s1n.count(f)
        assert n == 1, (f"{c['id']}: FIND resolves {n}× in §1 AT THE MOMENT OF APPLICATION — "
                        f"stop and report rather than widening the anchor")
        line = s1n.count("\n", 0, s1n.index(f))
        d = len(r) - len(f)
        assert d == c["delta"], f"{c['id']}: measured {d:+d}, cures73.py says {c['delta']:+d}"
        s1n = s1n.replace(f, r, 1)
        flag = "" if d == c["approved"] else f"  DEPARTS {d - c['approved']:+d}"
        print(f"   {c['id']:<4} line {line:<4} {d:+5d}{flag:<14}  {c['where']}")
    assert len(s1n) - len(s1) == TOTAL, f"§1 delta {len(s1n)-len(s1):+d}, expected {TOTAL:+d}"
    out = body[:s] + s1n + body[e:]

    # ---- 3. the record patches, outside §1 ---------------------------------------------
    for p in PATCHES:
        n = out.count(p["find"])
        assert n == p["n"], f"{p['id']}: count became {n} after an earlier substitution"
        out = out.replace(p["find"], p["repl"])
        print(f"   {p['id']} {len(p['repl']) - len(p['find']):+6d}  {p['label']}")

    # ---- 4. the retention rotation ------------------------------------------------------
    moved, freed = {}, 0
    for mv in MOVES:
        sec, a, z = cut(out, mv["head"], mv["stop"])
        moved[mv["id"]] = sec
        stub = mv["stub_head"] + "\n\n" + mv["stub"] + "\n\n\n"
        freed += len(sec) - len(stub)
        out = out[:a] + stub + out[z:]
        print(f"   {mv['id']} moved {mv['head']} ({len(sec)} chars) -> stub {len(stub)} "
              f"({len(stub) - len(sec):+d})")

    # ---- 5. the new record layer, inserted newest-first --------------------------------
    for anchor, path in ((f"### 0.0-{L['s0']} ", "rec_s0_73.md"),
                         (f"### §5.{L['s5prev']} ", "rec_s5_73.md"),
                         (f"### §6.0-71 ", "rec_s6_73.md")):
        assert out.count(anchor) == 1, f"insertion anchor {anchor!r} occurs {out.count(anchor)}×"
        out = out.replace(anchor, load(path) + "\n\n" + anchor)
    s8h = "## 8. Status and next step\n\n"
    assert out.count(s8h) == 1
    out = out.replace(s8h, s8h + load("rec_s8_73.md") + "\n\n")

    bm = re.search(r"\*\*MOO-42 · Drafting Specialist · store revision \d+ · \d+ \w+ 2026 · "
                   r"INTERNAL WORKING DRAFT — pre-decisional\*\*", out)
    assert bm, "byline not found"
    byl = bm.group(0)
    assert out.count(byl) == 1, f"byline occurs {out.count(byl)}×"
    out = out.replace(byl, byl.replace(f"store revision {L['s0']}", f"store revision {L['rev']}"))
    print(f"   byline -> store revision {L['rev']}")

    # ---- 6. post-conditions. The line diff is the proof. -------------------------------
    b1n = sec1(out)
    assert b1n == s1n, "the §1 slice of the assembled body is not the substituted §1"
    la, lb = s1.split("\n"), b1n.split("\n")
    assert len(la) == len(lb), f"§1 line count {len(la)} -> {len(lb)}"
    changed = [i for i, (x, y) in enumerate(zip(la, lb)) if x != y]
    assert len(changed) == LINES_CHANGED, \
        f"expected {LINES_CHANGED} changed §1 lines, got {len(changed)}: {changed}"
    for i in changed:
        who = ("subdivision D 1" if "**D. 1.**" in lb[i] else
               "subsection M 2" if lb[i].lstrip("<u>").startswith("2. A member, retiree") else
               "enactment clause 3" if lb[i].startswith("**3. That") else None)
        assert who, f"§1 line {i} changed and is none of D 1, M 2 or enactment clause 3"
        print(f"   §1 line {i:<4} {len(la[i])} -> {len(lb[i])} ({len(lb[i]) - len(la[i]):+d})  "
              f"{who}")
    for needle, _, af in TERMS:
        assert b1n.count(needle) == af, \
            f"AFTER {needle[:40]!r}: §1 count {b1n.count(needle)}, expected {af}"
    for lbl, a in UNTOUCHED:
        assert b1n.count(a) == 1, f"UNTOUCHED anchor AFTER — {lbl}: §1 count {b1n.count(a)}"
    # the series: nine items, eight semicolons, advisory last, before and after
    for lbl, t, endmark in (("before", s1, ". A failure to state in the Board's certification"),
                            ("after", b1n, ". A statement this subdivision requires")):
        d1 = [l for l in t.split("\n") if "**D. 1.**" in l][0]
        sent = d1[d1.index("The Board's certification shall also state that,"):
                   d1.index(endmark) + 1]
        assert sent.count(";") == 8, f"{lbl}: {sent.count(';')} semicolons in the series"
        assert sent.rstrip(".").endswith("not having reviewed it"), \
            f"{lbl}: the advisory is not the last item of the series"
    # S5 adds exactly one sentence to D 1 and nothing else gains or loses one
    d1b = [l for l in s1.split("\n") if "**D. 1.**" in l][0]
    d1a = [l for l in b1n.split("\n") if "**D. 1.**" in l][0]
    assert d1a.count(". ") - d1b.count(". ") == 1, "D 1's sentence count moved by something else"
    # the two proposals must still anchor on what was written, since two items cite them
    for p in PROPOSED:
        f, r = build(p)
        assert b1n.count(f) == 1, f"PROPOSED {p['id']}: FIND resolves {b1n.count(f)}× in §1"
        print(f"   proposal {p['id']:<5} anchors 1× on the written §1, {len(r) - len(f):+d}, "
              f"not enacted")
    # the title line is untouched by this revision
    ttl = re.search(r"^\*\*A BILL to amend and reenact .*$", b1n, re.M).group(0)
    assert "death benefits; designation of beneficiary" in ttl and ttl.endswith("reports.**"), ttl
    assert ttl == re.search(r"^\*\*A BILL to amend and reenact .*$", s1, re.M).group(0), \
        "the title line moved and this revision does not touch it"

    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    assert len(out) < CEILING, (
        f"OVER CEILING: {len(out)} > {CEILING}. §5.45/§5.46 and §6.0-66/§6.0-67 are next.")
    headroom = CEILING - len(out)
    # §5.49 check 7 and §0.0-73 both assert what the revision would have cost without the
    # rotation. Assert it here so neither can go stale.
    gross = len(out) - len(body) + freed
    assert (gross, len(body) + gross) == (37554, 540140), (
        f"§5.49 check 7 and §0.0-73 quote a cut-plus-record-layer cost of 37,554 and an "
        f"unrotated document of 540,140; measured {gross} and {len(body) + gross} "
        f"(freed {freed}, net {len(out) - len(body)}). Re-word them before applying.")
    print(f"   without the rotation this revision would have stood at {len(body) + gross} "
          f"against the {CEILING} ceiling ({gross:+d} for the cut and its record layer)")
    after = {t: b1n.count(t) for t in (n for n, _, _ in TERMS)}
    print(f"\npost-conditions OK | §1 {len(s1)} -> {len(b1n)} ({len(b1n)-len(s1):+d}) | "
          f"document {len(body)} -> {len(out)} ({len(out)-len(body):+d}) | "
          f"headroom {head_in} -> {headroom}")
    print("  §1 term movement: " + ", ".join(f"{t[:34]} {before[t]}->{after[t]}"
                                             for t in before if before[t] != after[t]))
    open(os.path.join(HERE, "out-body-73.md"), "w", encoding="utf-8").write(out)
    open(os.path.join(HERE, "out-s1-73.md"), "w", encoding="utf-8").write(b1n)

    # ---- 7. vol 2 takes everything that left, verbatim ---------------------------------
    st, v = req("GET", f"/api/issues/{MOO42}/documents/{VOL2_KEY}")
    assert st == 200, (st, v)
    vbody, vrev = v["body"], v["latestRevisionId"]
    block = ("\n\n---\n\n## Moved in store revision 73 of `bill-text-s8` — sweeps §5.43 and "
             "§5.44, drafter's notes §6.0-63 and §6.0-65\n\n**Moved verbatim and in full.** "
             f"`bill-text-s8` arrived at store revision 73 with {HEADROOM_IN} characters of "
             "headroom against the 524,288-character ceiling and could not take that revision's "
             "record layer. These four blocks are the ones §5's and §6's own preambles had "
             "already named as next to move. Nothing below is rewritten, abridged or summarised; "
             "each block left a stub in the bill naming its durable result and pointing here. "
             "**These are dated per-revision records: every figure in them is the figure as at "
             "the revision named in its own heading, and a later revision may have superseded "
             "it. The live record is in `bill-text-s8` itself.**\n\n"
             + "\n\n".join(moved[k].rstrip("\n") for k in ["M1", "M2", "M3", "M4"]) + "\n")
    vout = vbody.rstrip("\n") + block
    for k in ["M1", "M2", "M3", "M4"]:
        assert moved[k].rstrip("\n") in vout, f"{k} did not land in vol 2 verbatim"
    assert len(vout) < CEILING, f"vol 2 OVER CEILING: {len(vout)}"
    print(f"vol 2 {len(vbody)} -> {len(vout)} (+{len(vout)-len(vbody)}) | "
          f"headroom {CEILING - len(vout)}")
    open(os.path.join(HERE, "out-vol2-73.md"), "w", encoding="utf-8").write(vout)

    # ---- 8. the item list: 135 closed, 137 and 138 opened ------------------------------
    st, idoc = req("GET", f"/api/issues/{MOO42}/documents/{ITEMS_KEY}")
    assert st == 200, (st, idoc)
    ibody, irev = idoc["body"], idoc["latestRevisionId"]
    end = ibody.index(RETAINED)
    pos = [(int(m.group(1)), m.start()) for m in ITEM.finditer(ibody)]
    nums = [n for n, _ in pos]
    assert nums == list(range(1, max(nums) + 1)), f"§7 not contiguous: {nums}"
    assert max(nums) == TOP_ITEM, f"§7 runs to {max(nums)}; the new items are written for a list "
    assert [n for n, p in pos if p > end] == [], "an item is stranded after §7.1"
    for f, lbl in ((H135_F, "item 135's label"), (T135_F, "item 135's closing paragraph")):
        assert ibody.count(f) == 1, f"{lbl} resolves {ibody.count(f)}×"
    iout = ibody.replace(H135_F, H135_R).replace(T135_F, T135_R)
    assert ITEM137.startswith("137. ") and ITEM138.startswith("138. ")
    pre, retained = iout[:iout.index(RETAINED)], iout[iout.index(RETAINED):]
    iout = pre.rstrip("\n") + "\n\n" + ITEM137 + "\n\n" + ITEM138 + retained + "\n"
    pos2 = [(int(m.group(1)), m.start()) for m in ITEM.finditer(iout)]
    end2 = iout.index(RETAINED)
    assert [n for n, _ in pos2] == list(range(1, TOP_ITEM + 3)), \
        f"§7 not contiguous after: {[n for n, _ in pos2][-6:]}"
    assert [n for n, p in pos2 if p > end2] == [], "a new item landed after §7.1"
    assert all(pos2[i][1] < pos2[i + 1][1] for i in range(len(pos2) - 1)), "items out of order"
    assert len(iout) < CEILING, f"item list OVER CEILING: {len(iout)}"
    print(f"item list {len(ibody)} -> {len(iout)} ({len(iout)-len(ibody):+d}) | items 1..."
          f"{TOP_ITEM + 2} contiguous, none stranded | 135 closed, 137 and 138 opened")
    open(os.path.join(HERE, "out-items-73.md"), "w", encoding="utf-8").write(iout)

    if dry:
        print("\nDRY RUN — nothing sent.")
        return

    for key, rev, text, title in (
            (KEY, live_rev, out,
             f"Bill text — S8, §§ 51.1-142.2 and 51.1-162 amended and new § 51.1-142.4; store "
             f"revision {L['rev']} (INTERNAL WORKING DRAFT — not a DLS bill, not reviewed by "
             f"counsel)"),
            (VOL2_KEY, vrev, vout, None),
            (ITEMS_KEY, irev, iout,
             f"bill-text-s8 — §7 open-question item list, items 1 to {TOP_ITEM + 2} (split out "
             f"of the bill in store revision 59)")):
        payload = {"format": "markdown", "body": text, "baseRevisionId": rev}
        if title:
            payload["title"] = title
        st, r = req("PUT", f"/api/issues/{MOO42}/documents/{key}", payload)
        if st not in (200, 201):
            print(f"WRITE FAILED {key}: {st} {str(r)[:400]}")
            sys.exit(1)
        got = r.get("body", "")
        if got != text:
            print(f"{key}: the returned body is NOT the body sent ({len(got)} vs {len(text)}) — "
                  f"treat as failed")
            sys.exit(2)
        print(f"WROTE {key}: revision {r.get('latestRevisionId')} "
              f"(number {r.get('latestRevisionNumber')}) | {len(got)} chars | returned body "
              f"identical to the body sent, character for character")
        if key == KEY:
            print(f"       title: {r.get('title')}")


if __name__ == "__main__":
    main()
