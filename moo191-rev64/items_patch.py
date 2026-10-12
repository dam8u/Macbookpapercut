#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-191 — mark §7 item 129 answer (4) as answered and enacted in `bill-text-s8-item-list`.

Record only. It answers nothing: the Policy Director answered answer (4) at MOO-188 §3.3 and this
writes into the item list what that answer became, which is the same treatment item 128 got when
store revision 62 enacted it. **Answers (1), (2), (3), (5), (6) and (7) are not touched.**

    python3 items_patch.py --dry-run
    python3 items_patch.py
"""
import json, os, re, sys, urllib.request, urllib.error

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8-item-list"
REV = 65
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


P1_F = ("**Four of the seven decide who bears a loss and I have picked none.** Items 60, 106, 107, "
        "126 and 127, and the five unenacted answers at item 122, are unaffected and stay open.")
P1_R = P1_F + (
    "\n\n    **ANSWER (4) IS ANSWERED AND ENACTED — store revision %d, 12 October 2026, and it is "
    "the only one of the seven that is.** The Policy Director answered it at "
    "[MOO-188](/MOO/issues/MOO-188) §3.3 with one wording change and commissioned the cut at §8; it "
    "is enacted in subdivision D 1 by store revision %d and recorded at §0.0-%d, §5.43 and §6.0-%d "
    "of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8). **Answers (1), (2), (3), (5), "
    "(6) and (7) remain open and unanswered, and this marking decides none of them.**"
) % (REV, REV, REV, REV)

P2_F = ("Drafted, appended to that proposition: *\"and that the member should review the member's "
        "designation of beneficiary under subsection A of § 51.1-162 before completing payment.\"* "
        "**It is a new compelled statement and was not agreed.** It is also, on the reviewer's "
        "analysis, the cheapest thing on this card.")
P2_R = P2_F + (
    " **ANSWERED AND ENACTED in store revision %d.** It was agreed by the Policy Director at "
    "[MOO-188](/MOO/issues/MOO-188) §3.3 and cut on [MOO-191](/MOO/issues/MOO-191) as one anchored "
    "substitution of 137 characters. **Two things changed on the way in.** The verb: the enacted "
    "words read *\"that the member **is advised to** review the member's designation of beneficiary "
    "under subsection A of § 51.1-162 before completing payment\"*, because every other item in that "
    "series is a proposition of law introduced by *\"that\"* and *\"should review\"* would have read "
    "as a statement of what the law requires of the member, which it is not. The place: **its own "
    "semicolon item immediately after the § 51.1-162 B proposition**, not an appendage to it, so the "
    "propositions of law stay together and the advice is visibly advice. **Do not re-cut it.** The "
    "consequence the Director took at MOO-188 §3.4 is that subdivision D 1's failure sentence reaches "
    "the advisory, so omitting it is reviewable under subsection M and reportable under subsection J; "
    "the advisory is not excepted from that sentence."
) % REV

PATCHES = [("129 preamble", P1_F, P1_R), ("129 answer (4)", P2_F, P2_R)]


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live = doc["body"], doc["latestRevisionId"]
    print(f"live {KEY}: revision {live} (number {doc.get('latestRevisionNumber')}), {len(body)} chars")
    out = body
    for tag, f, r in PATCHES:
        c = out.count(f)
        print(f"   {tag}: FIND count {c}, delta {len(r) - len(f):+d}")
        assert c == 1, f"{tag}: count {c}, expected 1"
    for _, f, r in PATCHES:
        out = out.replace(f, r, 1)
    # nothing but item 129 may move
    ob, nb = body.split("\n"), out.split("\n")
    assert len(nb) - len(ob) == 2, f"line count moved by {len(nb) - len(ob)}, expected +2"
    assert out.count("129. **NEW IN STORE REVISION 62") == 1
    for other in ("- **(1) F7", "- **(2) The measure you approved", "- **(3) F5's discovery rule",
                  "- **(5) M7", "- **(6) M8", "- **(7) The conforming amendment"):
        assert out.count(other) == 1, other
    print(f"post-conditions OK | {len(body)} -> {len(out)}")
    if "--dry-run" in sys.argv:
        open(os.path.join(HERE, "out-items.md"), "w", encoding="utf-8").write(out)
        print("DRY RUN — nothing sent")
        return
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": doc.get("title"), "format": "markdown", "body": out,
                   "baseRevisionId": live})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    assert res.get("body") == out, "returned body differs"
    print(f"WRITE OK — {KEY} revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(out)} characters")


main()
