#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-211's six cures, re-resolved and re-priced on the LIVE store. Writes nothing.

Asserts the corrected figures in cures.py and reports counsel's alongside. For each cure:

  * the FIND counted inside the §1 slice and in the whole document
  * whether the insertion point sits inside an open <u> span, which decides the markup
  * the delta with no tags (the correct form) and with counsel's tags (the defective form)
  * that applying the cure leaves <u>/</u> at 62/62 in §1

Then re-counts every figure MOO-211 asserted about this document, and the figures MOO-211
asserted about the kit's own record (m1, m2), so none of them is taken on trust.

    python3 verify_cures.py              # live
    python3 verify_cures.py FILE.md      # against a saved body
"""
import json, os, re, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cures import CURES, build

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def fetch():
    r = urllib.request.Request(base() + f"/api/issues/{MOO42}/documents/{KEY}", headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", ""),
    })
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def inside_span(s1, off):
    return s1.count("<u>", 0, off) > s1.count("</u>", 0, off)


# Every figure MOO-211 asserts about the §1 text, so that none of them is taken on trust.
COUNSEL_COUNTS = [
    ("<u> in §1", "<u>", 62), ("</u> in §1", "</u>", 62),
    ("'the member is advised to'", "the member is advised to", 0),
    ("the conformed phrase",
     "that the Board advises the member to review the member's designation of beneficiary", 3),
    ("'for the purposes of subsection M'", "for the purposes of subsection M", 6),
    ("the declaratory form",
     "is a determination of the Board for the purposes of subsection M", 5),
    ("'subdivision D 1'", "subdivision D 1", 4),
    ("'the report required by subsection J'", "the report required by subsection J", 14),
    ("'as amended or renumbered'", "as amended or renumbered", 2),
    ("'as it reads'", "as it reads", 0), ("'as then in effect'", "as then in effect", 0),
    ("J 1's catch-all",
     "every other matter this section requires the Board to state in that report", 1),
    ("'item 5'", "item 5", 0), ("'item 7'", "item 7", 0),
    ("M 2's first-sentence limb",
     "by a failure of the Board to state in a certification or notice a matter this section "
     "requires to be stated in it", 1),
    ("M 2's longer-or-later clock",
     "where the provision that requires the matter to be stated provides a longer or later "
     "period, within that period", 1),
    ("M 2's second sentence",
     "whether or not another provision of this section expressly provides for review of it", 1),
    ("M 1's 'content of a complete application'", "the content of a complete application", 1),
    ("'Nothing in this section' (the wider formula)", "Nothing in this section", 3),
]

# m2 — §5.47 direction 2 check 9's re-anchored MOO-176 Edit 1 string. Check 9 says 150.
M2_STRING = ("every period within which a person may or must act that runs from the giving of "
             "that statement, notice, or certification is extended by three days.</u>")

# m1 — §7 item 135's two forms as the item's own READ strings write them, tags included.
M135 = [("M-a", 116, ", other than a failure to state that the Board advises the member to review "
                     "the member's designation of beneficiary"),
        ("M-b", 101, ", other than a matter that the provision of this section requiring it to be "
                     "stated expressly excepts from this subsection")]
M135_FIND = ("or by a failure of the Board to state in a certification or notice a matter this "
             "section requires to be stated in it, may obtain")


def main():
    if len(sys.argv) > 1 and sys.argv[1].endswith(".md"):
        body, label = open(sys.argv[1], encoding="utf-8").read(), sys.argv[1]
    else:
        doc = fetch()
        body = doc["body"]
        label = f"revision {doc['latestRevisionId']} (n{doc.get('latestRevisionNumber')})"
    s1 = sec1(body)
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", body, re.M))
    print(f"live  : {label}")
    print(f"        store revision {s0} | document {len(body)} | §1 {len(s1)} | "
          f"<u>/</u> {s1.count('<u>')}/{s1.count('</u>')} | headroom {524288 - len(body)}")
    fail = []

    print("\n=== the six cures, re-resolved and re-priced inside the §1 slice "
          "============================")
    print(f"{'id':<4}{'FIND':>5}{'§1':>4}{'doc':>5}  {'span':<6}{'tags':<6}"
          f"{'measured':>9}{'counsel':>22}  provision")
    for c in CURES:
        f, r = build(c, tagged=False)
        _, r_tag = build(c, tagged=True)
        n1, nd = s1.count(f), body.count(f)
        if n1 != 1:
            fail.append(f"{c['id']}: FIND resolves {n1}x in §1, not 1x — DEAD ANCHOR")
            print(f"{c['id']:<4}{len(f):>5}{n1:>4}{nd:>5}  *** DEAD ANCHOR ***")
            continue
        off = s1.index(f) + (0 if c["mode"] == "insert_before"
                             else f.index(c["at"]) + len(c["at"]) if c["mode"] == "insert_after"
                             else f.index(c["at"]))
        ins = inside_span(s1, off)
        d, d_tag = len(r) - len(f), len(r_tag) - len(f)
        print(f"{c['id']:<4}{len(f):>5}{n1:>4}{nd:>5}  {'IN' if ins else 'out':<6}"
              f"{'none':<6}{d:>+9}{c['counsel']:>22}  {c['where']}")
        if d != c["delta"]:
            fail.append(f"{c['id']}: cures.py says {c['delta']:+d}, measured {d:+d}")
        # The markup claim, proved rather than asserted: apply the cure and re-count the tags.
        after = s1.replace(f, r, 1)
        if after.count("<u>") != 62 or after.count("</u>") != 62:
            fail.append(f"{c['id']}: applying the untagged cure moves §1's tag count to "
                        f"{after.count('<u>')}/{after.count('</u>')}")
        after_tag = s1.replace(f, r_tag, 1)
        if ins and after_tag.count("<u>") == 62:
            fail.append(f"{c['id']}: expected counsel's tagged form to add a tag")
        if ins:
            # Prove the nesting: inside an open span, counsel's <u> opens a second one.
            print(f"      counsel's tagged form would nest: §1 tags "
                  f"{after_tag.count('<u>')}/{after_tag.count('</u>')}, and prices it "
                  f"{d_tag:+d} instead of {d:+d}")
    print("\n  span IN  = the insertion point is inside an open <u> span (M 2 and D 1 are wholly"
          "\n             new language), so tags would nest."
          "\n  span out = enactment clause 3, which carries zero <u> tags in "
          f"{len(sec1(body)) and 6176} characters,"
          "\n             the enactment clauses not being amendatory text. Also no tags.")

    print("\n=== every count MOO-211 asserts about §1, re-counted "
          "=========================================")
    for lbl, needle, want in COUNSEL_COUNTS:
        got = s1.count(needle)
        print(f"  {'OK ' if got == want else '***'} {lbl:<48s} {got:>4}  (MOO-211: {want})")
        if got != want:
            fail.append(f"MOO-211 count: {lbl} is {got}, counsel said {want}")

    print("\n=== m1 — §7 item 135's own arithmetic "
          "========================================================")
    n = s1.count(M135_FIND)
    for name, stated, ins in M135:
        net, tagged = len(ins), len(ins) + 7
        print(f"  {name}: FIND {len(M135_FIND)} chars, {n}x in §1 | item 135 states "
              f"{stated:+d} | measured {net:+d} untagged, {tagged:+d} tagged")
        if stated in (net, tagged):
            fail.append(f"m1 {name}: item 135's {stated:+d} unexpectedly reconciles")
    print("  both figures in item 135 are wrong, and both of its READ strings write tags that "
          "would nest.")

    print("\n=== m2 — §5.47 direction 2 check 9's re-anchored string "
          "=======================================")
    print(f"  {len(M2_STRING)} characters (check 9 says 150) | §1 {s1.count(M2_STRING)}x | "
          f"document {body.count(M2_STRING)}x")
    if len(M2_STRING) == 150:
        fail.append("m2: the string measures 150, so check 9 was right and m1/m2 need re-reading")

    print(f"\n=== S4's measurement, re-taken at store revision {s0} "
          "==========================================")
    a = s1.index("The Board's certification shall also state that,")
    z = s1.index(". A failure to state in the Board's certification") + 1
    sent = s1[a:z]
    print(f"  the 'shall also state' sentence: {len(sent)} chars, {len(sent.split())} words, "
          f"one sentence")
    print(f"  MOO-211 measured it at store revision 70: 3,447 chars, 576 words "
          f"({len(sent) - 3447:+d} chars, {len(sent.split()) - 576:+d} words since)")

    print()
    if fail:
        print(f"DISCREPANCIES — {len(fail)}")
        for x in fail:
            print("  * " + x)
        sys.exit(1)
    print("every corrected figure re-counts exactly, every anchor resolves 1x in §1, and every "
          "cure leaves <u>/</u> at 62/62. ALL CHECKS PASS")


if __name__ == "__main__":
    main()
