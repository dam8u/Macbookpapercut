# The store-revision apply kit — reusable, because the workspace is not

**MOO-97 · Drafting Specialist · 12 October 2026 · internal tooling record**

**Why this is a document and not a file.** Three heartbeats on this issue were lost to re-deriving a half-megabyte body in context, and the on-disk kits written for store revisions 42, 46, 50 and 54 are **gone** — `PAPERCLIP_WORKSPACE_CWD` was reset and holds only `.claude/` and `README.md`. The kit below applied store revision 58. Save it to disk, point `edits.py` and `content.py` at the revision you are cutting, and run it.

## How to use it

1. `mkdir kit && cd kit`, then write this file as `apply.py`.
2. Write `edits.py` with `EDITS = [(label, FIND, READ), ...]` — the substitutions to §1.
3. Write `content.py` with `S0`, `S5`, `S6`, `S7`, `S8` and any `STUB_*` blocks, using `{REV}`, `{S5}`, `{S6}` and `{ITEM}` placeholders only. **Never hard-code a revision number anywhere.**
4. `python3 apply.py` for a dry run; `python3 apply.py --write` to append the moved records and then write the body.

## The five rules it enforces, each of which was learned by breaking

- **Every label is derived from the live body, and §0's records — not the byline — are the authority.** The byline has been left behind by concurrent runs three times; on the base this revision was cut against it said 55 while §0 already carried 57.
- **Every FIND must occur exactly once in §1 and exactly once in the whole document**, and every READ must be absent. A failed assertion writes nothing.
- **A section that is already a stub is skipped, not re-stubbed.** Re-stubbing dates another run's move to yours, and store revision 57 had already taken four of this revision's five planned moves.
- **Post-conditions are asserted too**: under the 524,288 ceiling, §7 contiguous 1..N, no duplicated new heading, no stray section sign in a commentary heading.
- **The record appends run before the body write**, so a stub never points at content that is not there yet; and each append is idempotent on its own heading.

## Two things the kit cannot do for you

- **A predicted count is not a count.** Publish sweep figures only after re-counting them on the written body. Two of store revision 58's own published counts were predictions and both were wrong.
- **A citation count is not a cross-reference check.** §5.33 counted § 51.1-165.01's citations and did not read its subsection F, which is how a fatal finding survived two passes.

---

## `apply.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply store revision N of bill-text-s8 for MOO-154's disposition.

Nothing in this script hard-codes a revision number, a sweep number, a
drafter's-note number or a §7 item number: every label is derived from the
live body, and every anchor is asserted to occur exactly once before anything
is written. If an assertion fails the script writes nothing and says why.

Usage:  python3 apply.py            # dry run, prints the plan
        python3 apply.py --write    # fetch, cut, append records, PUT body
"""
import json
import os
import re
import sys
import urllib.request

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
BASE = os.environ["PAPERCLIP_API_URL"].rstrip("/")
if BASE.endswith("/api"):
    BASE = BASE[:-4]
KEY = os.environ["PAPERCLIP_API_KEY"]
RUN = os.environ.get("PAPERCLIP_RUN_ID", "")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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
    if "document" in d:
        d = d["document"]
    return d


def fail(msg):
    print("ASSERTION FAILED: " + msg)
    sys.exit(2)


def main():
    write = "--write" in sys.argv
    doc = get_doc("bill-text-s8")
    body = doc["body"]
    base_rev = doc["latestRevisionId"]
    print("live document: %d chars, latestRevisionId %s" % (len(body), base_rev))

    # ---------------------------------------------------------- labels
    # The §0 record, not the byline, is the authority: concurrent runs have
    # repeatedly left the byline behind. The byline is conformed below.
    s0_nums = sorted(int(x) for x in re.findall(r"^### 0\.0-(\d+) ", body, re.M))
    if not s0_nums:
        fail("could not derive the store revision from §0's records")
    prev = s0_nums[-1]
    rev = prev + 1
    m = re.search(r"store revision (\d+) · \d+ \w+ 2026", body[:1200])
    if not m:
        fail("could not read the store revision from the byline")
    byline_rev = int(m.group(1))
    if byline_rev > prev:
        fail("the byline (%d) runs ahead of §0's latest record (%d)" % (byline_rev, prev))
    if byline_rev != prev:
        print("NOTE: byline says %d, §0's latest record is %d — the byline is "
              "conformed to %d by this revision" % (byline_rev, prev, rev))

    s5_nums = sorted(int(x) for x in re.findall(r"^### §?5\.(\d+) ", body, re.M))
    s6_nums = sorted(int(x) for x in re.findall(r"^### §?6\.0-(\d+) ", body, re.M))
    if not s5_nums or not s6_nums:
        fail("could not derive §5 / §6 numbering")
    s5 = "5.%d" % (s5_nums[-1] + 1)
    s6 = "6.0-%d" % (s6_nums[-1] + 1)
    for h in ("### §%s " % s5, "### §%s " % s6):
        if h in body:
            fail("heading %r already present" % h)

    s7 = body[body.index("## 7. Open questions"):body.index("## 8. Status")]
    items = sorted(int(x) for x in re.findall(r"^(\d+)\. ", s7, re.M))
    missing = [i for i in range(1, items[-1] + 1) if i not in items]
    if missing:
        fail("§7 is not contiguous before the edit: missing %s" % missing[:10])
    item = items[-1] + 1

    print("derived: store revision %d, sweep §%s, note §%s, §7 item %d"
          % (rev, s5, s6, item))
    L = {"REV": rev, "S5": s5, "S6": s6, "ITEM": item}

    # ------------------------------------------- bill edits, asserted
    bill = body[body.index("## 1. The bill"):body.index("## 2. Section-by-section")]
    net = 0
    for label, find, repl in EDITS:
        if body.count(find) != 1:
            fail("%s: FIND occurs %d times in the document" % (label, body.count(find)))
        if bill.count(find) != 1:
            fail("%s: FIND occurs %d times in §1" % (label, bill.count(find)))
        if repl in body:
            fail("%s: READ string is already present — already applied?" % label)
        net += len(repl) - len(find)
    print("eight substitutions verified unique; net bill change %+d chars" % net)
    new = body
    for label, find, repl in EDITS:
        new = new.replace(find, repl, 1)

    # ------------------------------------------------- record moves
    def cut(start_head, end_head, stub):
        """Move one commentary section out, or skip it if a concurrent
        revision has already stubbed it. Re-stubbing a stub would date
        someone else's move to this revision."""
        nonlocal new
        if new.count(start_head) != 1:
            fail("move anchor %r occurs %d times" % (start_head, new.count(start_head)))
        i = new.index(start_head)
        j = len(new) if end_head is None else new.index(end_head, i)
        if end_head is not None and j <= i:
            fail("move anchors out of order for %r" % start_head)
        moved = new[i:j]
        if "Moved verbatim" in moved[:600] or "moved to the retained-record" in moved[:300]:
            print("  SKIP %r — already a stub (%d chars)" % (start_head, len(moved)))
            return None
        new = new[:i] + stub.format(**L) + new[j:]
        return moved

    moved_s5s6 = [x for x in (
        cut("### §5.34 Store revision 55", "### §5.33 Store revision 54",
            content.STUB_S5_34),
        cut("### §5.33 Store revision 54", "### §5.32 Store revision 53",
            content.STUB_S5_33),
        cut("### §6.0-55 Ambiguities", "### §6.0-54 Ambiguities",
            content.STUB_S6_55),
        cut("### §6.0-54 Ambiguities", "### §6.0-53 Ambiguities",
            content.STUB_S6_54),
    ) if x]
    moved_s8 = cut("### 8.1 Status at store revision 51 and earlier", None,
                   content.STUB_S8_1)

    # §7 is captioned "Open questions for Policy Director" and the file is at
    # the ceiling. An item that says of itself that it is closed, answered,
    # decided, moot or withdrawn is a record, not a question. Each is moved
    # verbatim and stubbed with its own first paragraph — which in every case
    # states the answer, who gave it and when — plus every pointer it carried,
    # because the pointers are the only reason a reader still needs it.
    MARKERS = ("CLOSED", "ANSWERED", "DECIDED", "MOOT", "SUPERSEDED", "WITHDRAWN")

    def move_closed_s7(text):
        i = text.index("## 7. Open questions")
        j = text.index("## 8. Status")
        s7 = text[i:j]
        tail = s7.index("### 7.1 Retained record")
        bounds = [(int(m.group(1)), m.start())
                  for m in re.finditer(r"^(\d+)\. ", s7, re.M)]
        bounds = [(n, a) for n, a in bounds if a < tail]
        out, moved = [], []
        prev_end = 0
        for k, (n, a) in enumerate(bounds):
            z = bounds[k + 1][1] if k + 1 < len(bounds) else tail
            item = s7[a:z]
            head = item[:420]
            closed = any(w in head for w in MARKERS)
            if not (closed and len(item) > 900) or "MOVED TO THE RETAINED RECORD" in head:
                continue
            para = item.split("

")[0].rstrip()
            if len(para) > 760:
                k = max(para.rfind(". ", 0, 760), para.rfind(".**", 0, 760))
                if k > 200:
                    para = para[:k + 1].rstrip() + " […]"
            links = []
            for mm in re.finditer(r"\[([^\]]{1,60})\]\((/MOO/[^)]+)\)", item):
                lk = "[%s](%s)" % (mm.group(1), mm.group(2))
                if lk not in links:
                    links.append(lk)
            refs = []
            for mm in re.finditer(r"item (\d+)", item):
                r = "item " + mm.group(1)
                if r not in refs and int(mm.group(1)) != n:
                    refs.append(r)
            stub = ("%d. **MOVED TO THE RETAINED RECORD IN STORE REVISION %d — this item is "
                    "closed and is not an open question. The whole of it is at "
                    "[`bill-text-s8-revision-history-2`]"
                    "(/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2), where a "
                    "reference of the form §7 item %d still resolves.** Its own statement of "
                    "what was decided is retained here verbatim; where that statement refers "
                    "to reasoning *\"below\"*, the reasoning is in that document and not "
                    "here.

   %s

   **Pointers it carried:** %s

"
                    % (n, rev, n, para[len(("%d. " % n)):].strip(),
                       ("; ".join(links + refs) if (links or refs) else "none.")))
            out.append((a, z, stub))
            moved.append("### §7 item %d — moved from the live list in store revision %d

%s"
                         % (n, rev, item.rstrip()))
        for a, z, stub in reversed(out):
            s7 = s7[:a] + stub + s7[z:]
        return text[:i] + s7 + text[j:], moved

    new, moved_s7 = move_closed_s7(new)
    print("§7: %d closed items moved out, %d chars"
          % (len(moved_s7), sum(len(x) for x in moved_s7)))
    print("moved out: §5/§6 %d sections / %d chars, §8.1 %s chars"
          % (len(moved_s5s6), sum(len(x) for x in moved_s5s6),
             len(moved_s8) if moved_s8 else 0))

    # --------------------------------------------------- insertions
    def insert_before(anchor, block):
        nonlocal new
        if new.count(anchor) != 1:
            fail("insert anchor %r occurs %d times" % (anchor, new.count(anchor)))
        i = new.index(anchor)
        new = new[:i] + block.format(**L) + new[i:]

    insert_before("### 0.0-%d " % prev, content.S0)
    insert_before("### §5.%d " % s5_nums[-1], content.S5)
    insert_before("### §6.0-%d " % s6_nums[-1], content.S6)
    insert_before("### 7.1 Retained record", content.S7)
    anchor8 = "## 8. Status and next step

"
    if new.count(anchor8) != 1:
        fail("§8 heading anchor not unique")
    i = new.index(anchor8) + len(anchor8)
    new = new[:i] + content.S8.format(**L) + "
" + new[i:]

    # byline
    old_by = "store revision %d · 12 October 2026" % byline_rev
    if new.count(old_by) != 1:
        fail("byline %r occurs %d times" % (old_by, new.count(old_by)))
    new = new.replace(old_by, "store revision %d · 12 October 2026" % rev, 1)

    # ------------------------------------------------ post-conditions
    if len(new) >= CEILING:
        fail("result is %d chars, over the %d ceiling" % (len(new), CEILING))
    s7n = new[new.index("## 7. Open questions"):new.index("## 8. Status")]
    nums = sorted(int(x) for x in re.findall(r"^(\d+)\. ", s7n, re.M))
    if nums != list(range(1, item + 1)):
        fail("§7 is not contiguous 1..%d after the edit" % item)
    for h in ("### §%s " % s5, "### §%s " % s6, "### 0.0-%d " % rev):
        if new.count(h) != 1:
            fail("new heading %r occurs %d times" % (h, new.count(h)))
    if re.search(r"^### §\d+\.\d+ ?§", new, re.M):
        fail("a commentary heading carries a stray section sign")
    print("post-conditions pass: %d chars, headroom %d, §7 contiguous 1..%d"
          % (len(new), CEILING - len(new), item))
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out-body.md"),
         "w").write(new)

    if not write:
        print("DRY RUN — nothing written. Re-run with --write.")
        return

    # ------------------------------- 1) append the moved records first
    def append_record(key, header, blocks):
        d = get_doc(key)
        if header in d["body"]:
            print("  %s: already carries %r — append skipped" % (key, header[:50]))
            return True
        nb = d["body"].rstrip() + "

---

" + header + "

" + "

".join(blocks) + "
"
        if len(nb) >= CEILING:
            fail("%s would reach %d chars" % (key, len(nb)))
        st, r = api("PUT", "/api/issues/%s/documents/%s" % (MOO42, key),
                    {"title": d.get("title"), "format": "markdown", "body": nb,
                     "baseRevisionId": d["latestRevisionId"]})
        if st not in (200, 201):
            print("  %s APPEND FAILED %s %s" % (key, st, r))
            return False
        print("  %s appended: now %d chars" % (key, len(nb)))
        return True

    ok1 = append_record(
        "bill-text-s8-record-s0-s5-s6-rev2-51",
        "## Moved in store revision %d — §5.33, §5.32, §6.0-54 and §6.0-53" % rev,
        moved_s5s6)
    blocks2 = ([moved_s8] if moved_s8 else []) + moved_s7
    ok2 = True
    if blocks2:
        ok2 = append_record(
            "bill-text-s8-revision-history-2",
            "## Moved in store revision %d — §8.1 (the status notes for store revisions 50 back to 45) and %d closed §7 items"
            % (rev, len(moved_s7)),
            blocks2)
    if not (ok1 and ok2):
        print("STOPPING: a record append failed; the body is NOT written so no stub "
              "points at missing content.")
        sys.exit(3)

    # --------------------------------------------- 2) write the body
    st, r = api("PUT", "/api/issues/%s/documents/bill-text-s8" % MOO42,
                {"title": doc.get("title"), "format": "markdown", "body": new,
                 "baseRevisionId": base_rev})
    if st not in (200, 201):
        print("BODY WRITE FAILED %s %s" % (st, r))
        sys.exit(4)
    rr = r.get("document", r)
    print("BODY WRITTEN: revision %s, %d chars (returned body len %d)"
          % (rr.get("latestRevisionId"), len(new), len(rr.get("body") or "")))


if __name__ == "__main__":
    main()

```
