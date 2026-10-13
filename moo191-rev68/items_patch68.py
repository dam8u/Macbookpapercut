#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 68 — the item-list half. Record only; it answers no open item on the merits.

Two new items out of MOO-195's pass 21 (F7, and the conservator residual the pass was asked to
answer), and item 129's residual marked answered. Both new items are drafted word for word and
enacted nowhere.

    python3 items_patch68.py --dry-run
    python3 items_patch68.py
"""
import json, os, re, sys, urllib.request, urllib.error

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8-item-list"
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


RESIDUAL = ("**A conservator acting for a living member under a disability receives the "
            "subdivision D 1 certification and is in no class in subdivision M 2.** The next "
            "counsel pass is asked to say whether that is a defect or a non-case.")

RESIDUAL_R = RESIDUAL + (
    " **ANSWERED — [MOO-195](/MOO/issues/MOO-195)'s pass 21, 12 October 2026: a non-case**, "
    "because subdivision M 2's class is a list of **parties in interest** and not of "
    "representatives, and a conservator appointed under Chapter 20 of Title 64.2 asserts no claim "
    "of their own — they exercise **the member's** standing, and *\"a member\"* is the first "
    "category M 2 names. The act's other fiduciary references are in subdivision G 4 and are needed "
    "there precisely because they concern **death** benefits, where the member has no standing left "
    "to exercise. **The narrow residual the pass does leave is carded as item 134 and is drafted "
    "and not enacted.**")

ITEM_133 = """

133. **NEW IN STORE REVISION 68, out of [MOO-195](/MOO/issues/MOO-195)'s pass 21 on the designation-review advisory (finding F7) — drafted in full and enacted nowhere. The failure sentence catches omission and misses misstatement.** Subdivision D 1's failure sentence reaches *"a **failure to state** in the Board's certification every matter this subdivision requires to be stated in it"*, and subdivision M 2's general limb reaches *"a **failure** of the Board to state in a certification or notice a matter this section requires to be stated in it."* **Both are framed on absence. Neither reaches a matter that is stated and wrong.**

    **Why it bites hardest on the advisory, which is why the pass raised it here.** The six propositions of law in D 1's series are long and interlocking and a certification template will lift them as one block from the statute; they are present or absent together. **The advisory is short, separable and in a different register, and it is exactly the line a plain-language template editor rewrites.** Rendered as *"Your beneficiary designation on file with VRS will apply to this purchase,"* it is present — so it is no omission — and it is **wrong**, because the designation on file may defeat the subsection B allowance entirely. The member is actively misled, there is no channel, and the subsection J report records the matter as stated.

    **Drafted, in D 1's failure sentence:** *"A failure to state in the Board's certification every matter this subdivision requires to be stated in it<u>, or the statement of any such matter otherwise than as this subdivision requires it to be stated,</u> is a failure of the Board to state in a certification a matter this section requires to be stated in it for the purposes of subsection M…"*

    **Not enacted, for three reasons, and the third is the one that matters.** The defect is a property of a sentence **you approved at store revision 62**, not of the 137 characters cut at store revision 65; it is outside a cut commissioned as one edit; and **it interacts with the channel question** — if you take pass 21's F3 recommendation and except the advisory from subsection M review, the advisory needs no misstatement limb either, and the clause would then reach only the six propositions. **Decide F3 first.** The whole disposition is at [`moo195-disposition`](/MOO/issues/MOO-191#document-moo195-disposition).

134. **NEW IN STORE REVISION 68 — item 129's conservator residual, answered. A non-case on the main question, with one narrow intake residual drafted and not enacted.** Item 129 asked the next counsel pass whether it is a defect that a conservator acting for a **living** member under a disability receives the subdivision D 1 certification and appears in no class in subdivision M 2. [MOO-195](/MOO/issues/MOO-195)'s pass 21 §7 answers: **a non-case.** M 2's class is a list of **parties in interest**, not of representatives. A conservator appointed under Chapter 20 of Title 64.2 asserts no claim of their own; they exercise **the member's** standing, and *"a member"* is the first category M 2 names. The act's other fiduciary references sit in subdivision G 4 and are needed there because those provisions concern **death** benefits, where the member has no standing left to exercise and the fiduciary must be named in their own right.

    **The residual, which is narrow and real enough to card.** Subdivision M 2 opens *"A member … adversely affected by a determination"* and then requires a *"written request filed."* **If the Board reads the filing requirement as personal to the member, a conservator's filing could be refused at intake**, forcing a petition that would plainly succeed and costing the member the time the tolling provision exists to give her.

    **Drafted, as one clause added to M 2's class:** *"<u>or a fiduciary within the meaning of § 51.1-1012 acting for any of them</u>."*

    **Not enacted.** It is outside the scope of the one-edit cut at [MOO-191](/MOO/issues/MOO-191), it widens a standing class you have not been asked about, and the answer above is enough to close the residual as item 129 posed it. **Say whether you want the clause; it is one substitution and it reverses nothing.**
"""


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body = doc["body"]
    live_rev = doc["latestRevisionId"]
    print(f"live latestRevisionId = {live_rev} (number {doc.get('latestRevisionNumber')}), "
          f"{len(body)} chars")

    nums = [int(m.group(1)) for m in re.finditer(r"^(\d+)\. ", body, re.M)]
    assert nums == sorted(nums), "the item numbers are not in order; stop and look"
    assert nums[-1] == 132, f"the list ends at item {nums[-1]}, not 132 — re-word before applying"
    for n in (133, 134):
        assert not re.search(rf"^{n}\. ", body, re.M), f"item {n} already exists"

    hdr_f, hdr_r = "items 1 to 132", "items 1 to 134"
    assert body.count(hdr_f) == 1, f"header {hdr_f!r} occurs {body.count(hdr_f)} times"
    assert body.count(RESIDUAL) == 1, f"item 129's residual occurs {body.count(RESIDUAL)} times"

    out = body.replace(hdr_f, hdr_r).replace(RESIDUAL, RESIDUAL_R)
    out = out.rstrip("\n") + "\n" + ITEM_133

    nums2 = [int(m.group(1)) for m in re.finditer(r"^(\d+)\. ", out, re.M)]
    assert nums2 == nums + [133, 134], f"numbering broke: {nums2[-6:]}"
    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    assert out.count("<u>") == out.count("</u>") == body.count("<u>") + 2, \
        (f"<u>/</u> went {body.count('<u>')}/{body.count('</u>')} -> "
         f"{out.count('<u>')}/{out.count('</u>')}; expected +2 and equal — the two drafted clauses")
    print(f"items 133 and 134 added, item 129's residual marked answered | "
          f"{len(body)} -> {len(out)} chars | headroom {CEILING - len(out)}")

    if "--dry-run" in sys.argv:
        open(os.path.join(HERE, "out-items.md"), "w", encoding="utf-8").write(out)
        print("DRY RUN — written to out-items.md, nothing sent")
        return

    title = re.sub(r"items 1 to \d+", "items 1 to 134", doc.get("title") or "")
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title, "format": "markdown", "body": out, "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    assert res.get("body", "") == out, "returned body differs"
    print(f"WRITE OK — document revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(out)} characters")


main()
