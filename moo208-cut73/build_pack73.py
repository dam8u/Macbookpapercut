#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the MOO-208 deliverable `moo208-rev73` and write it to the issue.

The three reproductions are not pasted: they are taken from `repro-73.md`, which `check73.py`
generates from the LIVE bill and verifies by stripping its bold markers back to the live line
character for character. So the deliverable cannot drift from what was enacted.

    python3 build_pack73.py --dry-run
    python3 build_pack73.py
"""
import json, os, re, sys, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
MOO208 = "53282470-ef04-4f17-a47f-f786bac47729"
KEY = "moo208-rev73"


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


def load(p):
    return open(os.path.join(HERE, p), encoding="utf-8").read().rstrip("\n")


def main():
    repro = load("repro-73.md")
    assert repro.count("### ") == 3, f"repro-73.md holds {repro.count('### ')} reproductions"
    body = load("pack_head.md") + "\n\n" + repro + "\n\n" + load("pack_tail.md") + "\n"

    # the reproductions must still be the live provisions, and the three cures' words must each
    # appear exactly once in the assembled pack's reproduction block
    for needle in ("that that designation determines the payment of a benefit under that section "
                   "only where the member dies before retirement",
                   "nothing in this section, and no procedure adopted under subsection M,",
                   "A statement this subdivision requires of the effect of a provision of "
                   "§ 51.1-162",
                   "other than a failure to state that the Board advises the member to review the "
                   "member's designation of beneficiary, may obtain",
                   "requires the Board to state a matter in the report required by subsection J",
                   "or to a failure of the Board to state in a certification or notice a matter "
                   "that section requires to be stated in it"):
        n = repro.replace("**", "").count(needle)
        assert n == 1, f"the reproductions, with the bold markers stripped, carry {needle[:48]!r} {n}×"
    print(f"pack {len(body)} chars | reproductions {len(repro)} chars | six cures each 1× in them")
    open(os.path.join(HERE, "moo208-rev73.md"), "w", encoding="utf-8").write(body)

    if "--dry-run" in sys.argv:
        print("DRY RUN — written to moo208-rev73.md, nothing sent")
        return

    st, cur = req("GET", f"/api/issues/{MOO208}/documents/{KEY}")
    payload = {"title": "MOO-208 — the Director's six approved cures, cut as store revision 73, "
                        "with two adverse findings drafted and enacted nowhere (INTERNAL WORKING "
                        "DRAFT)",
               "format": "markdown", "body": body,
               "baseRevisionId": cur.get("latestRevisionId") if st == 200 else None}
    st, r = req("PUT", f"/api/issues/{MOO208}/documents/{KEY}", payload)
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(r)[:400]}")
        sys.exit(1)
    if r.get("body") != body:
        print("WRITE RETURNED A DIFFERENT BODY — treat as failed")
        sys.exit(2)
    print(f"WROTE {KEY}: revision {r.get('latestRevisionId')} "
          f"(number {r.get('latestRevisionNumber')}) | {len(body)} chars | returned body "
          f"identical to the body sent")


if __name__ == "__main__":
    main()
