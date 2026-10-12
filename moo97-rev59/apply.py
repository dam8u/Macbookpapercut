#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply the next store revision of bill-text-s8 — MOO-97, MOO-161's counsel
pass plus the Policy Director's five answers of 12 October 2026.

Nothing here hard-codes a revision, sweep, note or §7 item number: every label
is derived from the live bodies of BOTH documents (store revision 59 moved the
§7 item list into `bill-text-s8-item-list`), every anchor is asserted to occur
exactly once before anything is written, and the writes run in the order
record -> item list -> bill so that no pointer precedes its target.

Usage:  python3 apply.py            # dry run
        python3 apply.py --write    # append the moved note, then PUT both bodies
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
VOL2 = "bill-text-s8-revision-history-2"
ITEMS = "bill-text-s8-item-list"
BASE = os.environ["PAPERCLIP_API_URL"].rstrip("/")
if BASE.endswith("/api"):
    BASE = BASE[:-4]
KEY = os.environ["PAPERCLIP_API_KEY"]
RUN = os.environ.get("PAPERCLIP_RUN_ID", "")

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from edits import EDITS  # noqa: E402
import content  # noqa: E402


def api(method, path, payload=None):
    url = BASE + path
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + KEY)
    req.add_header("Content-Type", "application/json")
    if RUN:
        req.add_header("X-Paperclip-Run-Id", RUN)
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:600]


def get_doc(key):
    st, d = api("GET", "/api/issues/%s/documents/%s" % (MOO42, key))
    assert st == 200, (st, d)
    return d.get("document", d)


def fail(msg):
    print("ASSERTION FAILED: " + msg)
    sys.exit(2)


def main():
    write = "--write" in sys.argv
    doc = get_doc("bill-text-s8")
    body = doc["body"]
    base_rev = doc["latestRevisionId"]
    idoc = get_doc(ITEMS)
    ibody = idoc["body"]
    ibase = idoc["latestRevisionId"]
    print("bill:  %d chars, headroom %d, rev %s" % (len(body), CEILING - len(body), base_rev))
    print("items: %d chars, headroom %d, rev %s" % (len(ibody), CEILING - len(ibody), ibase))

    # ------------------------------------------------------------- labels
    s0 = sorted(int(x) for x in re.findall(r"^### 0\.0-(\d+) ", body, re.M))
    if not s0:
        fail("could not derive the store revision from §0's records")
    prev, rev = s0[-1], s0[-1] + 1
    m = re.search(r"store revision (\d+) · \d+ \w+ 2026", body[:2000])
    if not m:
        fail("could not read the byline")
    byline = int(m.group(1))
    if byline > prev:
        fail("the byline (%d) runs ahead of §0's latest record (%d)" % (byline, prev))
    if byline != prev:
        print("NOTE: byline %d, §0 record %d — byline conformed to %d" % (byline, prev, rev))

    s5n = sorted(int(x) for x in re.findall(r"^### §?5\.(\d+) ", body, re.M))
    s6n = sorted(int(x) for x in re.findall(r"^### §?6\.0-(\d+) ", body, re.M))
    if not s5n or not s6n:
        fail("could not derive §5 / §6 numbering")
    s5, s6 = "5.%d" % (s5n[-1] + 1), "6.0-%d" % (s6n[-1] + 1)
    for h in ("### §%s " % s5, "### §%s " % s6, "### 0.0-%d " % rev):
        if h in body:
            fail("heading %r already present in the bill" % h)

    itail = ibody.index("### 7.1 Retained record")
    items = sorted(int(x) for x in re.findall(r"^(\d+)\. ", ibody[:itail], re.M))
    missing = [i for i in range(1, items[-1] + 1) if i not in items]
    if missing:
        fail("the item list is not contiguous before the edit: missing %s" % missing[:10])
    item = items[-1] + 1
    print("derived: store revision %d, sweep §%s, note §%s, §7 item %d" % (rev, s5, s6, item))
    L = {"REV": rev, "S5": s5, "S6": s6, "ITEM": item, "PREV": prev}

    # -------------------------------------------------- bill edits, asserted
    bill = body[body.index("## 1. The bill"):body.index("## 2. Section-by-section")]
    for label, find, repl in EDITS:
        if body.count(find) != 1:
            fail("%s: FIND occurs %d times in the bill document" % (label, body.count(find)))
        if bill.count(find) != 1:
            fail("%s: FIND occurs %d times in §1" % (label, bill.count(find)))
        if repl in body:
            fail("%s: READ already present — already applied?" % label)
    new = body
    for label, find, repl in EDITS:
        new = new.replace(find, repl, 1)
    nbill = new[new.index("## 1. The bill"):new.index("## 2. Section-by-section")]
    print("%d substitutions verified unique; §1 %d -> %d chars (%+d)"
          % (len(EDITS), len(bill), len(nbill), len(nbill) - len(bill)))

    C = {}
    for key, pat in content.COUNT_PATTERNS.items():
        C[key] = (len(re.findall(pat, bill)), len(re.findall(pat, nbill)))

    # ----------------------------------------------------- §8 record move
    s8_start = new.index("## 8. Status and next step")
    s8 = new[s8_start:]
    blocks = [(mm.start() + s8_start, int(mm.group(1)))
              for mm in re.finditer(r"> \*\*STORE REVISION (\d+)", s8)]
    moved_s8, moved_nums = [], []
    if len(blocks) < 5:
        print("NOTE: §8 holds %d status notes; nothing is moved" % len(blocks))
    else:
        tailmark = new.index("**The status notes for store revisions", s8_start)
        cut_from = blocks[4][0]
        for k in range(4, len(blocks)):
            a = blocks[k][0]
            z = blocks[k + 1][0] if k + 1 < len(blocks) else tailmark
            moved_nums.append(blocks[k][1])
            moved_s8.append("### §8 status note for store revision %d — moved from the live "
                            "list in store revision %d\n\n%s"
                            % (blocks[k][1], rev, new[a:z].rstrip()))
        kept = [n for _, n in blocks[:4]]
        phrase = ("**§8's status note for store revision %d is" % moved_nums[0]
                  if len(moved_nums) == 1 else
                  "**§8's status notes for store revisions %s are"
                  % ", ".join(str(n) for n in moved_nums))
        new = new[:cut_from] + content.STUB_S8.format(
            REV=rev, PHRASE=phrase,
            KEPT=", ".join(str(n) for n in [rev] + kept)) + new[tailmark:]
        print("§8: moving notes %s (%d chars); retained %s"
              % (moved_nums, sum(len(x) for x in moved_s8), [rev] + kept))

    # ------------------------------------------------- bill insertions
    def ins(target, anchor, block):
        if target.count(anchor) != 1:
            fail("insert anchor %r occurs %d times" % (anchor, target.count(anchor)))
        i = target.index(anchor)
        return target[:i] + block + target[i:]

    new = ins(new, "### 0.0-%d " % prev, content.s0_block(L, C))
    new = ins(new, "### §5.%d " % s5n[-1], content.s5_block(L, C))
    new = ins(new, "### §6.0-%d " % s6n[-1], content.s6_block(L, C))
    new = ins(new, "## 8. Status and next step", content.s7stub_block(L, C))
    anchor8 = "## 8. Status and next step\n\n"
    if new.count(anchor8) != 1:
        fail("§8 heading anchor not unique")
    i = new.index(anchor8) + len(anchor8)
    new = new[:i] + content.s8_block(L, C) + "\n" + new[i:]

    old_by = "store revision %d · 12 October 2026" % byline
    if new.count(old_by) != 1:
        fail("byline %r occurs %d times" % (old_by, new.count(old_by)))
    new = new.replace(old_by, "store revision %d · 12 October 2026" % rev, 1)
    ttl_new = re.sub(r"store revision \d+", "store revision %d" % rev,
                     doc.get("title") or "", count=1)

    # ------------------------------------------------- item-list edits
    inew = ins(ibody, "### 7.1 Retained record", content.s7_block(L, C))
    for label, find, repl in content.DOC_EDITS_SPEC:
        repl = repl.format(REV=rev)
        if inew.count(find) != 1:
            fail("item-list edit %s: FIND occurs %d times" % (label, inew.count(find)))
        if repl in inew:
            fail("item-list edit %s: READ already present" % label)
        inew = inew.replace(find, repl, 1)
        print("item-list edit applied: %s" % label)
    old_hdr = "# bill-text-s8 — §7, the open-question item list: items 1 to %d" % items[-1]
    if inew.count(old_hdr) != 1:
        fail("item-list heading %r occurs %d times" % (old_hdr, inew.count(old_hdr)))
    inew = inew.replace(old_hdr, "# bill-text-s8 — §7, the open-question item list: items 1 to %d" % item, 1)
    ittl = re.sub(r"items 1 to \d+", "items 1 to %d" % item, idoc.get("title") or "", count=1)

    # -------------------------------------------------------- post-conditions
    for tag, text in (("bill", new), ("item list", inew)):
        if len(text) >= CEILING:
            fail("%s result is %d chars, over the %d ceiling" % (tag, len(text), CEILING))
    nums = sorted(int(x) for x in re.findall(r"^(\d+)\. ", inew[:inew.index("### 7.1 Retained record")], re.M))
    if nums != list(range(1, item + 1)):
        fail("the item list is not contiguous 1..%d after the edit" % item)
    for h in ("### §%s " % s5, "### §%s " % s6, "### 0.0-%d " % rev):
        if new.count(h) != 1:
            fail("new heading %r occurs %d times" % (h, new.count(h)))
    if re.search(r"^### §\d+\.\d+ ?§", new, re.M):
        fail("a commentary heading carries a stray section sign")
    if "other person to whom this section requires a notice to be given" in nbill:
        fail("the open notice class survives somewhere in §1")
    print("post-conditions pass: bill %d chars (headroom %d); item list %d chars "
          "(headroom %d); items contiguous 1..%d"
          % (len(new), CEILING - len(new), len(inew), CEILING - len(inew), item))
    open(os.path.join(HERE, "out-body.md"), "w").write(new)
    open(os.path.join(HERE, "out-items.md"), "w").write(inew)
    json.dump({"rev": rev, "s5": s5, "s6": s6, "item": item, "counts": C,
               "bill_len": len(new), "items_len": len(inew),
               "base_rev": base_rev, "items_base_rev": ibase,
               "moved_s8": moved_nums},
              open(os.path.join(HERE, "out-labels.json"), "w"), indent=1)

    if not write:
        print("DRY RUN — nothing written. Re-run with --write.")
        return

    # ---------------------------------- 1) append the moved §8 note first
    if moved_s8:
        d = get_doc(VOL2)
        header = ("## Moved in store revision %d — §8's status note for store revision %s"
                  % (rev, ", ".join(str(n) for n in moved_nums)))
        if header in d["body"]:
            print("  %s already carries this header — append skipped" % VOL2)
        else:
            nb = d["body"].rstrip() + "\n\n---\n\n" + header + "\n\n" + "\n\n".join(moved_s8) + "\n"
            if len(nb) >= CEILING:
                fail("%s would reach %d chars" % (VOL2, len(nb)))
            st, r = api("PUT", "/api/issues/%s/documents/%s" % (MOO42, VOL2),
                        {"title": d.get("title"), "format": "markdown", "body": nb,
                         "baseRevisionId": d["latestRevisionId"]})
            if st not in (200, 201):
                print("  %s APPEND FAILED %s %s" % (VOL2, st, r))
                print("STOPPING: nothing else is written, so no stub points at missing content.")
                sys.exit(3)
            print("  %s appended: now %d chars" % (VOL2, len(nb)))

    # ---------------------------------- 2) the item list, then the bill
    st, r = api("PUT", "/api/issues/%s/documents/%s" % (MOO42, ITEMS),
                {"title": ittl, "format": "markdown", "body": inew,
                 "baseRevisionId": ibase})
    if st not in (200, 201):
        print("ITEM-LIST WRITE FAILED %s %s" % (st, r))
        print("STOPPING: the bill is NOT written, so §0/§5/§6 do not point at a missing item.")
        sys.exit(4)
    print("ITEM LIST WRITTEN: revision %s, %d chars"
          % ((r.get("document", r)).get("latestRevisionId"), len(inew)))

    st, r = api("PUT", "/api/issues/%s/documents/bill-text-s8" % MOO42,
                {"title": ttl_new, "format": "markdown", "body": new,
                 "baseRevisionId": base_rev})
    if st not in (200, 201):
        print("BODY WRITE FAILED %s %s" % (st, r))
        print("NOTE: item %d IS written to the item list; a retry must skip it." % item)
        sys.exit(5)
    rr = r.get("document", r)
    print("BODY WRITTEN: revision %s, %d chars (returned body len %d)"
          % (rr.get("latestRevisionId"), len(new), len(rr.get("body") or "")))
    if (rr.get("body") or "") != new:
        print("WARNING: the returned body differs from what was sent")


if __name__ == "__main__":
    main()
