#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The six approved cures, re-resolved on the LIVE store and priced as cut. Writes nothing.

Applies them in document order inside the §1 slice, re-counting each anchor against the output of
its predecessors rather than against the base, then reports:

  * every standing post-condition, before and after
  * the §1 line diff — the rule MOO-211 R5 put in place of a character delta
  * the cross-reference counts the §5 sweep asserts, in both directions, so no figure in that
    sweep is prose
  * both departures from the approved strings, priced against the approved form

    python3 verify73.py              # live
    python3 verify73.py FILE.md      # against a saved body
"""
import difflib, json, os, re, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cures73 import CURES, PROPOSED, TERMS, UNTOUCHED, LINES_CHANGED, TOTAL, APPROVED_TOTAL, build

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
CEILING = 524288


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def fetch(key=KEY):
    r = urllib.request.Request(base() + f"/api/issues/{MOO42}/documents/{key}", headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", "")})
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


# ---- the sweep's own figures, both directions ------------------------------------------------
# Direction 1 — outward, from the new words to what they cite.
OUTWARD = [
    ("S3  'that section' in item 7 resolves to § 51.1-162",
     "advises the member to review the member's designation of beneficiary under subsection A of "
     "§ 51.1-162", 1),
    ("S3  the terminus clause, as cut", "that that designation determines the payment of a "
     "benefit under that section only where the member dies before retirement", 1),
    ("S5  § 51.1-162 cited expressly in the saving clause",
     "of the effect of a provision of § 51.1-162, of § 51.1-163, of § 51.1-165, or of "
     "§ 51.1-165.01", 1),
    ("M4  the widened no-fault subject",
     "nothing in this section, and no procedure adopted under subsection M, requires the member "
     "to review the designation", 1),
    ("M4  subsection M 1 is the procedure power it now reaches",
     "The Board shall adopt and publish, no later than July 1, 2029, procedures for administering",
     1),
    ("M3  clause (iii) names the report in the act's standing phrase",
     "requires the Board to state a matter in the report required by subsection J", 1),
    ("S2  clause (v)'s new failure-to-state limb",
     "or to a failure of the Board to state in a certification or notice a matter that section "
     "requires to be stated in it", 1),
    ("S1  the exception in M 2, in the conformed words",
     "stated in it, other than a failure to state that the Board advises the member to review "
     "the member's designation of beneficiary, may obtain", 1),
]
# Direction 2 — inward, every provision that points at what was amended.
INWARD = [
    ("provisions pointing into subsection M generally", "for the purposes of subsection M", 6),
    ("the declaratory 'is a determination of the Board' family",
     "is a determination of the Board for the purposes of subsection M", 5),
    ("provisions naming subdivision D 1", "subdivision D 1", 4),
    ("provisions naming the subsection J report", "the report required by subsection J", 15),
    ("the subsection J report's catch-all limb",
     "every other matter this section requires the Board to state in that report", 1),
    ("M 2's second sentence, disapplied for the member by D 1",
     "whether or not another provision of this section expressly provides for review of it", 1),
    ("M 2's longer-or-later clock, which D 1's extension feeds",
     "where the provision that requires the matter to be stated provides a longer or later "
     "period, within that period", 1),
    ("enactment clause 3's internal cross-reference to clause (i)",
     "except as clause (i) of this enactment provides", 2),
    ("enactment clause 3's internal cross-reference to clause (iv)",
     "notwithstanding clause (iv) of this enactment", 1),
    ("the D 1 failure sentence's own subsection M hand-off",
     "is a failure of the Board to state in a certification a matter this section requires to be "
     "stated in it for the purposes of subsection M", 1),
]


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
          f"<u>/</u> {s1.count('<u>')}/{s1.count('</u>')} | headroom {CEILING - len(body)}")
    fail = []

    print("\n=== the six cures, applied in document order, each anchor re-counted on its "
          "predecessors' output ===")
    print(f"{'id':<4}{'FIND':>5}{'§1 n':>6}{'line':>6}{'cut':>7}{'approved':>10}  provision")
    cur = s1
    for c in CURES:
        f, r = build(c)
        n = cur.count(f)
        if n != 1:
            fail.append(f"{c['id']}: FIND resolves {n}× in §1 at the moment of application")
            print(f"{c['id']:<4}{len(f):>5}{n:>6}  *** DEAD ANCHOR ***")
            continue
        line = cur.count("\n", 0, cur.index(f))
        d = len(r) - len(f)
        mark = "" if d == c["approved"] else f"  <- DEPARTS ({d - c['approved']:+d})"
        print(f"{c['id']:<4}{len(f):>5}{n:>6}{line:>6}{d:>+7}{c['approved']:>+10}{mark}  "
              f"{c['where']}")
        if d != c["delta"]:
            fail.append(f"{c['id']}: cures73.py says {c['delta']:+d}, measured {d:+d}")
        cur = cur.replace(f, r, 1)
    print(f"\n  total as cut {TOTAL:+d} | total as approved {APPROVED_TOTAL:+d} | "
          f"departure {TOTAL - APPROVED_TOTAL:+d} (S3 −4, M3 +24)")
    if len(cur) - len(s1) != TOTAL:
        fail.append(f"§1 delta {len(cur)-len(s1):+d}, cures73.py totals {TOTAL:+d}")

    print("\n=== the §1 line diff — MOO-211 R5's rule in place of a character delta ===")
    la, lb = s1.split("\n"), cur.split("\n")
    if len(la) != len(lb):
        fail.append(f"§1 line count {len(la)} -> {len(lb)}")
    changed = [i for i, (x, y) in enumerate(zip(la, lb)) if x != y]
    print(f"  §1 {len(s1)} -> {len(cur)} ({len(cur) - len(s1):+d}) | lines {len(la)} -> "
          f"{len(lb)} | changed {changed}")
    for i in changed:
        who = ("subdivision D 1" if "**D. 1.**" in lb[i] else
               "subsection M 2" if lb[i].lstrip("<u>").startswith("2. A member, retiree") else
               "enactment clause 3" if lb[i].startswith("**3. That") else "UNEXPECTED")
        print(f"    line {i:>4}  {len(la[i]):>6} -> {len(lb[i]):>6}  "
              f"({len(lb[i]) - len(la[i]):+5d})  {who}")
        if who == "UNEXPECTED":
            fail.append(f"§1 line {i} changed and is none of D 1, M 2 or enactment clause 3")
    if len(changed) != LINES_CHANGED:
        fail.append(f"{len(changed)} §1 lines changed, expected {LINES_CHANGED}")

    print("\n=== standing post-conditions, before -> after ===")
    for needle, b4, af in TERMS:
        g0, g1 = s1.count(needle), cur.count(needle)
        ok = (g0, g1) == (b4, af)
        print(f"  {'OK ' if ok else '***'} {needle[:62]:<64s} {g0:>3} -> {g1:<3} "
              f"(expected {b4} -> {af})")
        if not ok:
            fail.append(f"term {needle[:40]!r}: {g0}->{g1}, expected {b4}->{af}")

    print("\n=== the certification series, which nothing in this cut may re-shape ===")
    for lbl, text in (("before", s1), ("after", cur)):
        d1 = [l for l in text.split("\n") if "**D. 1.**" in l][0]
        a = d1.index("The Board's certification shall also state that,")
        z = d1.index(". A failure to state in the Board's certification") + 1
        if lbl == "after":
            z = d1.index(". A statement this subdivision requires") + 1
        sent = d1[a:z]
        items = sent.count(";") + 1
        print(f"  {lbl:<7} series sentence {len(sent):>5} chars, {len(sent.split()):>4} words, "
              f"{sent.count(';')} semicolons, {items} items, advisory last: "
              f"{'yes' if sent.rstrip('.').endswith('not having reviewed it') else 'NO'}")
        if sent.count(";") != 8 or items != 9:
            fail.append(f"{lbl}: the series has {sent.count(';')} semicolons / {items} items")
        if not sent.rstrip(".").endswith("not having reviewed it"):
            fail.append(f"{lbl}: the advisory is not the last item of the series")
    # D 1 gains exactly one sentence, S5's, and no other provision gains or loses one.
    d1b = [l for l in s1.split("\n") if "**D. 1.**" in l][0]
    d1a = [l for l in cur.split("\n") if "**D. 1.**" in l][0]
    print(f"  subdivision D 1 sentences: {d1b.count('. ') } -> {d1a.count('. ')} "
          f"(S5 adds exactly one)")
    if d1a.count(". ") - d1b.count(". ") != 1:
        fail.append("D 1's sentence count moved by something other than S5's one sentence")

    print("\n=== anchors this commission forbids disturbing ===")
    for lbl, a in UNTOUCHED:
        g0, g1 = s1.count(a), cur.count(a)
        print(f"  {'OK ' if g0 == g1 == 1 else '***'} {lbl:<40s} {len(a):>4} chars  "
              f"§1 {g0} -> {g1}")
        if not g0 == g1 == 1:
            fail.append(f"UNTOUCHED {lbl}: §1 {g0} -> {g1}, expected 1 -> 1")

    print("\n=== §5 sweep, direction 1 — outward, from the new words to what they cite ===")
    for lbl, needle, want in OUTWARD:
        got = cur.count(needle)
        print(f"  {'OK ' if got == want else '***'} {lbl:<62s} {got:>3}  (expected {want})")
        if got != want:
            fail.append(f"outward {lbl}: {got}, expected {want}")

    print("\n=== §5 sweep, direction 2 — inward, every provision that points at what was "
          "amended ===")
    for lbl, needle, want in INWARD:
        got = cur.count(needle)
        print(f"  {'OK ' if got == want else '***'} {lbl:<62s} {got:>3}  (expected {want})")
        if got != want:
            fail.append(f"inward {lbl}: {got}, expected {want}")

    print("\n=== the two departures from the approved strings, priced both ways ===")
    for c in CURES:
        if "depart" not in c:
            continue
        print(f"  {c['id']}: as cut {c['delta']:+d}, as approved {c['approved']:+d}  "
              f"({c['delta'] - c['approved']:+d})")
        print(f"      {c['depart']}")
    # S3's approved form, demonstrated: it produces a second conjunction in a three-clause series.
    appr = CURES[0]["ins"].replace(", that that designation", ", and that that designation", 1)
    d1 = [l for l in cur.split("\n") if "**D. 1.**" in l][0]
    k = d1.index("and that the Board advises the member")
    item7 = d1[k:d1.index(". A statement this subdivision requires")]
    print(f"\n  item 7 as cut carries {item7.count(', and that ')} ', and that ' conjunction(s) "
          f"and {item7.count(', that ')} ', that ' clause(s); the approved S3 string would make "
          f"the first {item7.count(', and that ') + 1}")
    if item7.count(", and that ") != 1:
        fail.append(f"item 7 carries {item7.count(', and that ')} ', and that ' conjunctions, "
                    f"expected 1")
    print(f"  M3 as approved would have cited 'that report', whose only antecedent in clause "
          f"(iii) is 'the last report': "
          f"{'present' if 'the last report and evaluation required by that subsection' in cur else 'ABSENT'}")

    print("\n=== the finding on the cut text: S1 narrows the channel and does not close it ===")
    print("  M 2's deeming sentence names a certification expressly:        "
          f"{cur.count('Every determination, certification, redetermination') } ×")
    print("  D 1 disapplies that sentence only for 'such a failure':        "
          f"{cur.count('the second sentence of subdivision M 2 does not apply to such a failure where the person adversely affected is the member')} ×")
    print("  and 'such a failure' no longer reaches the advice failure, which S1 and D 1 both "
          "except.")
    for p in PROPOSED:
        f, r = build(p)
        n = cur.count(f)
        print(f"  {p['id']}: FIND {len(f)} chars, {n}× in §1 as cut, {len(r) - len(f):+d}  "
              f"({p['where']})")
        if n != 1:
            fail.append(f"PROPOSED {p['id']}: FIND resolves {n}× in §1 as cut")
        after = cur.replace(f, r, 1)
        if (after.count("<u>"), after.count("</u>")) != (62, 62):
            fail.append(f"PROPOSED {p['id']}: would move §1's tag counts")
        print("      NOT ENACTED. Drafted only so that it can be priced and decided.")

    print("\n=== the second gap the sweep found: S5 does not reach the subdivision G 4 notice ===")
    g4 = [l for l in cur.split("\n") if l.startswith("<u>4. Subdivisions 2 and 3 shall not apply")][0]
    for lbl, needle in (
            ("G 4 requires a statement of a subsection C of § 51.1-162 right",
             "of any right under subsection C of § 51.1-162 of a beneficiary entitled to the "
             "entire amount of a retirement allowance under that subsection to waive the "
             "allowance"),
            ("G 4 requires a statement of the subsection C waiver period",
             "and of the period stated in that subsection within which the waiver must be made"),
            ("G 4 requires a statement of a subsection B of § 51.1-162 election",
             "of any right under subsection B of § 51.1-162 of the person to whom an allowance is "
             "payable under that subsection to elect")):
        n = g4.count(needle)
        print(f"  {'OK ' if n == 1 else '***'} {lbl:<62s} {n} ×")
        if n != 1:
            fail.append(f"G 4 gap: {lbl} resolves {n}×")
    print(f"  S5 as enacted is keyed to 'this subdivision', which is subdivision D 1, so it "
          f"reaches none of the three.")
    print(f"  the act's own compound 'that statement, notice, or certification': "
          f"{cur.count('that statement, notice, or certification')} × in §1 (subsection A)")

    print("\n=== S4's measurement, re-taken on the cut text ===")
    d1 = [l for l in cur.split("\n") if "**D. 1.**" in l][0]
    a = d1.index("The Board's certification shall also state that,")
    z = d1.index(". A statement this subdivision requires") + 1
    s = d1[a:z]
    print(f"  the 'shall also state' sentence: {len(s)} chars, {len(s.split())} words, one "
          f"sentence, nine items")
    print(f"  store revision 70: 3,447 / 576 | store revision 72: 3,680 / 612 | as cut: "
          f"{len(s)} / {len(s.split())}  ({len(s) - 3680:+d} chars, "
          f"{len(s.split()) - 612:+d} words from this cut)")

    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "s1-73.md"), "w",
         encoding="utf-8").write(cur)
    print("\n§1 as it would read written to s1-73.md")
    print("\n".join(list(difflib.unified_diff(
        s1.split("\n"), cur.split("\n"), "s1-72", "s1-73", lineterm="", n=0))[:5]))

    print()
    if fail:
        print(f"DISCREPANCIES — {len(fail)}")
        for x in fail:
            print("  * " + x)
        sys.exit(1)
    print("every anchor resolves 1× at the moment it is applied, exactly three §1 lines move, "
          "the markup is unchanged at 62/62, and every sweep figure re-counts. ALL CHECKS PASS")


if __name__ == "__main__":
    main()
