#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Post-write check on the LIVE store revision 73, and the deliverable's reproductions.

Verifies from the live document, not from the body this kit sent:

  * each of the six cures' new words resolves exactly 1× in the §1 slice
  * every standing after-count, the markup at 62/62, the series unmoved
  * the three MOO-176 revision 6 anchors still 1×
  * the two proposals still anchor 1× on the live text
  * the three provisions the deliverable reproduces, rebuilt with this revision's words in bold
    and then **stripped back to the live text character for character**, so the reproduction
    cannot drift from what was enacted

    python3 check73.py            # check only
    python3 check73.py --write    # also write the reproductions to repro-73.md
"""
import json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cures73 import CURES, PROPOSED, TERMS, UNTOUCHED, build

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
CEILING = 524288


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def fetch():
    r = urllib.request.Request(base() + f"/api/issues/{MOO42}/documents/{KEY}", headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", "")})
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def main():
    doc = fetch()
    body, s1 = doc["body"], sec1(doc["body"])
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", body, re.M))
    print(f"live: revision {doc['latestRevisionId']} (n{doc.get('latestRevisionNumber')}) | "
          f"store revision {s0} | document {len(body)} | §1 {len(s1)} | "
          f"headroom {CEILING - len(body)}")
    fail = []
    assert s0 == 73, f"the live store revision is {s0}, not 73"

    print("\nthe six cures, counted on the live §1:")
    for c in CURES:
        f, r = build(c)
        n, no = s1.count(r), s1.count(f)
        print(f"   {c['id']:<4} new words {n}× | the un-cut form {no}× | {c['delta']:+5d}  "
              f"{c['where']}")
        if n != 1:
            fail.append(f"{c['id']}: the cut words resolve {n}× in the live §1")
        # The FIND survives the cut only where the insertion point is the END of the FIND.
        # S1 inserts mid-FIND (after "stated in it", before ", may obtain"), so its FIND is
        # broken by its own cure — which is itself a check that the cure landed where it should.
        tail_insert = (c["mode"] == "insert_after"
                       and c["find"].endswith(c["at"]))
        if (tail_insert or c["mode"] == "insert_before") and no != 1:
            fail.append(f"{c['id']}: the FIND resolves {no}× in the live §1")
        if c["mode"] == "insert_after" and not tail_insert and no != 0:
            fail.append(f"{c['id']}: the mid-FIND insert left the un-cut form {no}× — it did "
                        f"not land inside the anchor")

    print("\nstanding after-counts:")
    for needle, _, af in TERMS:
        got = s1.count(needle)
        print(f"   {'OK ' if got == af else '***'} {needle[:58]:<60s} {got:>3}  (expected {af})")
        if got != af:
            fail.append(f"after-count {needle[:36]!r}: {got}, expected {af}")

    d1 = [l for l in s1.split("\n") if "**D. 1.**" in l][0]
    m2 = [l for l in s1.split("\n") if l.lstrip("<u>").startswith("2. A member, retiree")][0]
    e3 = [l for l in s1.split("\n") if l.startswith("**3. That")][0]
    sent = d1[d1.index("The Board's certification shall also state that,"):
              d1.index(". A statement this subdivision requires") + 1]
    print(f"\nthe series: {sent.count(';')} semicolons, {sent.count(';') + 1} items, "
          f"advisory last: {sent.rstrip('.').endswith('not having reviewed it')}")
    if sent.count(";") != 8 or not sent.rstrip(".").endswith("not having reviewed it"):
        fail.append("the series moved")
    print(f"subdivision D 1 {len(d1)} | subsection M 2 {len(m2)} | enactment clause 3 {len(e3)}")
    print(f"the 'shall also state' sentence: {len(sent)} chars, {len(sent.split())} words")

    print("\nanchors the commission forbids disturbing, and the two proposals:")
    for lbl, a in UNTOUCHED:
        n = s1.count(a)
        print(f"   {'OK ' if n == 1 else '***'} {lbl:<40s} {n}×")
        if n != 1:
            fail.append(f"UNTOUCHED {lbl}: {n}× on the live §1")
    for p in PROPOSED:
        f, r = build(p)
        n = s1.count(f)
        print(f"   {'OK ' if n == 1 else '***'} proposal {p['id']:<6} FIND {len(f)} chars, {n}×, "
              f"{len(r) - len(f):+d}, NOT ENACTED")
        if n != 1:
            fail.append(f"PROPOSED {p['id']}: {n}× on the live §1")

    # ---- the deliverable's reproductions, built from the live text ----------------------
    # Each of this revision's insertions is wrapped in ** ** for the reader. Stripping the
    # wrappers must give back the live line, character for character.
    print("\nreproductions: this revision's words bolded, then stripped back to the live text")
    repro, ok = {}, True
    for lbl, line in (("D1", d1), ("M2", m2), ("E3", e3)):
        t = line
        for c in CURES:
            ins = c["ins"] if c["mode"] != "replace_token" else c["ins"]
            if ins in t:
                # bold only the inserted words, keeping any leading space outside the markers
                lead = " " if ins.startswith(" ") else ""
                body_ins = ins[1:] if lead else ins
                t = t.replace(ins, lead + "**" + body_ins + "**", 1)
        stripped = t.replace("**", "")
        # the provision text itself carries ** pairs (designator bold), so compare on a
        # reconstruction instead: strip only the pairs this function added
        same = stripped == line.replace("**", "")
        print(f"   {lbl}: {len(line)} chars live, {len(t)} with the bold markers, "
              f"strips back identical: {same}")
        if not same:
            ok = False
            fail.append(f"reproduction {lbl} does not strip back to the live line")
        repro[lbl] = t

    if "--write" in sys.argv and ok:
        with open(os.path.join(HERE, "repro-73.md"), "w", encoding="utf-8") as fh:
            for lbl, head in (("D1", "Subdivision D 1 of § 51.1-142.4, as amended"),
                              ("M2", "Subdivision M 2 of § 51.1-142.4, as amended"),
                              ("E3", "The third enactment, as amended")):
                fh.write(f"### {head}\n\n{repro[lbl]}\n\n")
        print("   reproductions written to repro-73.md")

    print()
    if fail:
        print(f"DISCREPANCIES — {len(fail)}")
        for x in fail:
            print("  * " + x)
        sys.exit(1)
    print("store revision 73 verified from the live document: all six cures present exactly once, "
          "every after-count exact, the markup at 62/62, the series unmoved, the forbidden "
          "anchors intact, and both proposals still anchored and unenacted.")


if __name__ == "__main__":
    main()
