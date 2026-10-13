#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-208 store revision 70 — the Policy Director's composite, applied.

Six substitutions as ONE revision: F4 (lift), F9+F1+F2+F6 (set down as item 7), F4 (the series'
"and"), F3 (the subsection M exception), F3 (the subsection J limb), T2 (the title line). All six
are inside §1; the title line sits under `### Title`, which is inside §1 — see the note at
POST-CONDITIONS below.

Every FIND is re-counted inside the §1 slice at the moment it is applied. A FIND that does not
resolve exactly once aborts before anything is written. Derives its own store-revision label from
the live body and refuses to run if the label is not the one the record prose was written for.

    python3 composite.py --dry-run    # writes out-body.md, sends nothing
    python3 composite.py              # applies and verifies from the returned JSON
"""
import json, os, re, sys, urllib.request, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rec_patches70 import PATCHES
import rotate70

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"
HERE = os.path.dirname(os.path.abspath(__file__))
THIS_REV = 70

# ---------------------------------------------------------------- the words

# F9's actor, F1's object, F2's terminus with the referent named, F6's no-fault clause, as one
# semicolon item at the end of the certification series. Three co-ordinate "that" propositions,
# each hanging off the carrier "The Board's certification shall also state ... that".
ADVISORY = (
    "that the Board advises the member to review the member's designation of beneficiary "
    "under subsection A of § 51.1-162, and the effect of that designation under subsection B "
    "of that section, before completing payment, that the member may make or change that "
    "designation under subsection A of that section at any time before the member's death, "
    "and that nothing in this subdivision requires the member to review the designation or "
    "affects any benefit by reason of the member's not having reviewed it"
)

# D3c's descriptive phrase, CONFORMED to F9's wording. Unconformed it describes a matter the
# subdivision no longer requires to be stated, so the M exception excepts nothing and the J limb
# reports nothing. One phrase, used in both limbs, so the two limbs share one vocabulary.
EXCEPTION = ("that the Board advises the member to review the member's designation "
             "of beneficiary")

# Ordered substitutions, all inside §1. The order is forced: steps 4 and 5 write EXCEPTION, which
# contains step 2's own output, so the item must be relocated and rewritten first.
STEPS = [
    ("1  F4 — lift the advisory out of item 5",
     "and no other designation has been made; that the member is advised to review the member's "
     "designation of beneficiary under subsection A of § 51.1-162 before completing payment; "
     "that subsection C of § 51.1-162",
     "and no other designation has been made; that subsection C of § 51.1-162"),

    ("2  F9+F1+F2+F6 — set it down as item 7",
     "in the order of precedence that section states.",
     "in the order of precedence that section states; and " + ADVISORY + "."),

    ("3  F4 — move the series' 'and' to the new last item",
     "; and that where no benefit is payable",
     "; that where no benefit is payable"),

    ("4  F3 — except the advice from the subsection M limb",
     "A failure to state in the Board's certification every matter this subdivision requires to "
     "be stated in it is a failure of the Board",
     "A failure to state in the Board's certification every matter this subdivision requires to "
     "be stated in it, other than a failure to state " + EXCEPTION + ", is a failure of the Board"),

    ("5  F3 — keep it in the subsection J report",
     "and the Board shall state every such failure in the report required by subsection J.",
     "and the Board shall state every such failure, and every failure to state " + EXCEPTION +
     ", in the report required by subsection J."),

    ("6  T2 — the title line",
     "pilot program; post-retirement employment; reports.",
     "pilot program; death benefits; designation of beneficiary; "
     "post-retirement employment; reports."),
]

# The scope held. MOO-176 revision 6's three FIND strings are not touched and must still resolve
# exactly once after the composite.
MOO176_FINDS = [
    ("Edit 1", "every period within which a person may or must act that runs from the giving of "
               "that statement or notice is extended by three days.</u>"),
    ("Edit 2", "it shall give the member written notice of that date no later than 15 days after "
               "it acts upon the request."),
    ("Edit 3", "retains its filing date for the purposes of subdivisions D 4 and D 5 until the "
               "Board acts upon the request"),
]

D9_FIND = "that the member is advised to review the member's designation"
SEP = re.compile(r"; (?:and )?that[ ,]")


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


def sec1(b):
    """Enacted §1 only — located by content, never by line index."""
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def series_of(s1):
    a = s1.index("The Board's certification shall also state that,")
    z = s1.index(". A failure to state in the Board's certification") + 1
    return s1[a:z]


def shape(s1, probe):
    s = series_of(s1)
    items = len(SEP.findall(s)) + 1
    at = len(SEP.findall(s[:s.index(probe) + 6])) + 1 if probe in s else None
    return items, at


def derive(b):
    s0 = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", b, re.M))
    hdr = int(re.search(r"store revision (\d+) · \d+ October", b).group(1))
    rev = s0 + 1
    assert hdr <= s0, f"byline says {hdr} but the §0 record is only at {s0}"
    assert not re.search(rf"^### 0\.0-{rev} ", b, re.M), f"§0.0-{rev} already exists"
    return dict(rev=rev, s0=s0, byline=hdr)


def load(path):
    return open(os.path.join(HERE, path), encoding="utf-8").read().rstrip("\n")


def main():
    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live_rev = doc["body"], doc["latestRevisionId"]
    L = derive(body)
    B1 = sec1(body)
    print(f"live latestRevisionId = {live_rev} (revision number {doc.get('latestRevisionNumber')})")
    print(f"base: store revision {L['s0']}, {len(body)} chars, §1 {len(B1)} chars, "
          f"<u>/</u> {B1.count('<u>')}/{B1.count('</u>')}")
    print(f"derived: this is store revision {L['rev']}")
    assert L["rev"] == THIS_REV, (
        f"the record files are written for store revision {THIS_REV}; the live body makes this "
        f"store revision {L['rev']}. Re-word rec_s0_70 / rec_s5_47 / rec_s6_70 / rec_s8_70 and "
        f"rec_patches70 before applying — do not let the kit relabel prose it cannot re-reason.")

    # ---- 1. the sequencing hazard, demonstrated rather than asserted -----------------
    print("\nthe sequencing hazard that forces one composite:")
    print(f"   D9's FIND resolves {B1.count(D9_FIND)}x in the live §1")
    u = B1
    for i in (3, 4):
        u = u.replace(STEPS[i][1], STEPS[i][2].replace(EXCEPTION, D9_FIND + " of beneficiary"), 1)
    print(f"   after D3c unconformed and applied first it resolves {u.count(D9_FIND)}x — dead anchor")

    # ---- 2. the composite, every anchor re-counted at the moment it is applied -------
    print("\nthe six substitutions, in order, counted inside the §1 slice:")
    cur = B1
    for name, f, r in STEPS:
        n = cur.count(f)
        print(f"   {name:<52s} FIND {len(f):4d} chars  {n}x  "
              f"{'OK' if n == 1 else '*** DEAD ANCHOR ***'}  {len(r) - len(f):+d}")
        if n != 1:
            sys.exit(f"{name}: anchor resolved {n}x, not 1x — nothing applied, nothing written")
        cur = cur.replace(f, r, 1)

    out = body.replace(B1, cur, 1)

    # ---- 3. record layer -------------------------------------------------------------
    # The byline carries a date as well as a label, and the date is whatever the last revision
    # wrote. Derive the whole line rather than hard-coding either half.
    bm = re.search(r"\*\*MOO-42 · Drafting Specialist · store revision \d+ · "
                   r"\d+ October 2026 · INTERNAL WORKING DRAFT — pre-decisional\*\*", out)
    assert bm, "byline not found"
    byline_f = bm.group(0)
    byline_r = byline_f.replace(f"store revision {L['byline']}", f"store revision {L['rev']}")
    assert out.count(byline_f) == 1, f"byline occurs {out.count(byline_f)} times"
    assert byline_r != byline_f, f"byline label not advanced: {byline_f}"
    out = out.replace(byline_f, byline_r)
    print(f"   byline: {byline_f}\n        -> {byline_r}")

    for p in PATCHES:
        c = out.count(p["find"])
        assert c == p["n"], f"{p['id']} ({p['label']}): found {c}, expected {p['n']}"
    for p in PATCHES:
        out = out.replace(p["find"], p["repl"])
        print(f"   {p['id']}: {p['label']}  {len(p['repl']) - len(p['find']):+d} chars")

    for path, anchor, where in (
        ("rec_s0_70.md", f"### 0.0-{L['s0']} ", "§0"),
        ("rec_s5_47.md", "### §5.46 ", "§5"),
        ("rec_s6_70.md", "### §6.0-69 ", "§6"),
    ):
        assert out.count(anchor) == 1, f"{where} anchor {anchor!r} occurs {out.count(anchor)} times"
        out = out.replace(anchor, load(path) + "\n\n" + anchor)

    s8 = "## 8. Status and next step\n\n"
    assert out.count(s8) == 1
    out = out.replace(s8, s8 + load("rec_s8_70.md") + "\n\n")

    # ---- 3a. the retention rotation §0.1 sets, forced by the ceiling ------------------
    # With the record layer the document lands over the store's 524,288-character ceiling and
    # cannot be written at all. The §5 paragraph has named §5.38 and §5.39 as the next to move out
    # since store revision 58; this is the revision that is short of room. Verbatim out, stub in.
    pre_rot = len(out)
    out, moved_text, rot_report = rotate70.rotate(out)
    print(f"   rotation: document would have been {pre_rot}")
    for head, blk, stb, d in rot_report:
        print(f"      {head} moved out verbatim: {blk} chars -> {stb}-char stub ({d:+d})")
    print(f"   rotation freed {pre_rot - len(out)} chars; {len(moved_text)} chars to {rotate70.RETAINED}")

    # ---- 4. post-conditions ----------------------------------------------------------
    N1 = sec1(out)
    d1, dd = len(N1) - len(B1), len(out) - len(body)
    print(f"\n   §1        {len(B1)} -> {len(N1)}  ({d1:+d})")
    print(f"   document  {len(body)} -> {len(out)}  ({dd:+d})   record layer {dd - d1:+d}")
    # The Director's §1 figure of +590 counts steps 1-5 only. Step 6 is the title line, which lives
    # under `### Title` INSIDE §1, so §1's measured movement is +634 and not +590. The document
    # figure of 449,830 the Director required is unaffected and is met exactly by the bill change.
    # The Director's §1 figure of +590 counts steps 1-5 only. Step 6 is the title line, which
    # lives under `### Title` INSIDE §1, so §1's measured movement is +634 and not +590. The
    # Director's ABSOLUTE figures (§1 131,656; document 449,830) were counted on store revision 68
    # and are spent: store revision 69 landed first. The delta is what carries over.
    assert d1 == 634, f"§1 moved {d1:+d}, expected +634 (+590 steps 1-5, +44 the title line)"
    assert len(B1) == 131923 and len(N1) == 132557, (len(B1), len(N1))

    assert B1.count("<u>") == N1.count("<u>") == 62, "§1 <u> count moved"
    assert B1.count("</u>") == N1.count("</u>") == 62, "§1 </u> count moved"
    assert shape(N1, "that the Board advises the member to review") == (7, 7), \
        f"series shape {shape(N1, 'that the Board advises the member to review')}, expected (7, 7)"
    assert series_of(B1).count(";") == series_of(N1).count(";") == 6, "semicolon count moved"
    assert series_of(B1).count(".") == series_of(N1).count("."), "a sentence boundary moved"
    assert N1.count("the member is advised to") == 0, "the old advisory survives in §1"
    assert N1.count(EXCEPTION) == 3, \
        f"conformed phrase appears {N1.count(EXCEPTION)}x in §1, expected 3 (item, M, J)"
    assert N1.count("pilot program; death benefits; designation of beneficiary; "
                    "post-retirement employment; reports.") == 1, "title line not cured"
    # MOO-176 revision 6 is out of scope. The post-condition is "not touched", so the count must
    # be UNCHANGED, not necessarily 1 — Edit 1's anchor was already dead on the base, killed by a
    # revision later than MOO-176 revision 6 and not by this one. Asserting 1 here would abort on
    # a defect this revision did not cause and must not cure.
    for tag, f in MOO176_FINDS:
        b4, af = B1.count(f), N1.count(f)
        assert b4 == af, f"MOO-176 revision 6 {tag}: {b4}x -> {af}x in §1 — this cut moved it"
        print(f"   MOO-176 rev 6 {tag}: {b4}x -> {af}x in §1"
              f"{'  *** ANCHOR ALREADY DEAD ON THE BASE ***' if af != 1 else ''}")
    assert len(out) < CEILING, (
        f"over ceiling: {len(out)} > {CEILING}. Rotate more record out (§6.0-59 and "
        f"§6.0-60 are next) rather than truncating the note.")
    for pat, lbl in ((r"^### 0\.0-", "§0"), (r"^### §?5\.", "§5"), (r"^### §?6\.0-", "§6")):
        heads = re.findall(pat + r"(\d+)", out, re.M)
        assert len(heads) == len(set(heads)), f"duplicate {lbl} heading: {heads}"
    assert out.count(f"store revision {L['rev']} ·") == 1, "byline not unique"
    print(f"   series    7 items, advisory at item 7 of 7 | 6 semicolons | "
          f"'the member is advised to' 0x | conformed phrase 3x")
    print(f"post-conditions OK | headroom {CEILING - len(out)}")

    if "--dry-run" in sys.argv:
        open(os.path.join(HERE, "out-body.md"), "w", encoding="utf-8").write(out)
        open(os.path.join(HERE, "out-retained.md"), "w", encoding="utf-8").write(moved_text)
        print("DRY RUN — body to out-body.md, rotated record to out-retained.md, nothing sent")
        return

    # ---- 5. the retained-record document FIRST -------------------------------------
    # If this write lands and the bill write then fails, the retained document holds a duplicate
    # copy of two sweeps, which is recoverable. The other order loses them.
    st, rd = req("GET", f"/api/issues/{MOO42}/documents/{rotate70.RETAINED}")
    assert st == 200, (st, rd)
    for head, _, _, _ in rot_report:
        assert rd["body"].count(head + " ") == 0, f"{head} already in the retained document"
    rbody = rd["body"].rstrip("\n") + moved_text
    assert len(rbody) < CEILING, f"retained document over ceiling: {len(rbody)}"
    rtitle = rd.get("title") or ""
    if "§5.38" not in rtitle:
        rtitle = rtitle.rstrip() + "; sweeps §5.38 and §5.39 moved in in store revision 70"
    st, rres = req("PUT", f"/api/issues/{MOO42}/documents/{rotate70.RETAINED}",
                   {"title": rtitle[:300], "format": "markdown", "body": rbody,
                    "baseRevisionId": rd["latestRevisionId"]})
    if st not in (200, 201):
        print(f"RETAINED WRITE FAILED {st}: {str(rres)[:400]}")
        sys.exit(2)
    assert rres.get("body") == rbody, "retained document returned a different body"
    print(f"RETAINED WRITE OK — {rotate70.RETAINED} revision {rres.get('latestRevisionId')} "
          f"(number {rres.get('latestRevisionNumber')}), {len(rres['body'])} characters")

    # The title line of the DOCUMENT, not of the bill. This revision changes enacted text, so it
    # must not inherit store revision 68's "record only".
    title = re.sub(r"store revision \d+(?: — record only)?",
                   f"store revision {L['rev']}", doc.get("title") or "")
    assert "record only" not in title, title
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title, "format": "markdown", "body": out, "baseRevisionId": live_rev})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    got = res.get("body", "")
    assert got == out, f"returned body differs: {len(got)} vs {len(out)}"
    print(f"WRITE OK — document revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(got)} characters, "
          f"store revision {L['rev']}, §1 {len(sec1(got))}")
    print(f"title: {res.get('title')}")
    json.dump({"rev": L["rev"], "baseRevisionId": live_rev,
               "retainedRevisionId": rres.get("latestRevisionId"),
               "retainedLen": len(rres.get("body", "")),
               "revisionId": res.get("latestRevisionId"), "len": len(got),
               "sec1": len(sec1(got)), "title": res.get("title")},
              open(os.path.join(HERE, "out-labels.json"), "w"), indent=1)


main()
