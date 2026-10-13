#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-191 — the Policy Director's composite, verified on the live base.

The Director's disposition of MOO-195 takes F1, F2, F3, F4, F6, F9 and F8's title cure.
Because D1, D2b, D6 and D9 all substitute on the same FIND string, and because D3c INTRODUCES
two further copies of D9's FIND string, none of them can be applied as an independent cut. This
script states the one ordered sequence that works, re-counts every anchor on the LIVE base at the
moment it is applied, and asserts the end state.

It writes NOTHING to the store. Run:

    python3 director_composite.py
"""
import json, os, re, sys, urllib.request

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def get(path):
    r = urllib.request.Request(base() + path, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"]})
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


SEP = re.compile(r"; (?:and )?that[ ,]")


def series_of(s1):
    a = s1.index("The Board's certification shall also state that,")
    z = s1.index(". A failure to state in the Board's certification") + 1
    return s1[a:z]


def shape(s1, probe):
    s = series_of(s1)
    items = len(SEP.findall(s)) + 1
    at = len(SEP.findall(s[:s.index(probe) + 6])) + 1 if probe in s else None
    return items, at


# ------------------------------------------------------------------ the words
# The relocated advisory item: F9's actor, F1's object, F2's terminus, F6's no-fault clause,
# as one semicolon item at the end of the certification series. Three co-ordinate "that"
# propositions, each hanging off "The Board's certification shall also state".
ADVISORY = (
    "that the Board advises the member to review the member's designation of beneficiary "
    "under subsection A of § 51.1-162, and the effect of that designation under subsection B "
    "of that section, before completing payment, that the member may make or change that "
    "designation under subsection A of that section at any time before the member's death, "
    "and that nothing in this subdivision requires the member to review the designation or "
    "affects any benefit by reason of the member's not having reviewed it"
)

# D3c's exception, CONFORMED to F9's wording. Unconformed it describes a matter the subdivision
# no longer requires to be stated, so the M exception does no work and the J limb reaches nothing.
EXCEPTION = ("that the Board advises the member to review the member's designation "
             "of beneficiary")

# Ordered substitutions. Each FIND must resolve exactly 1x at the moment it is applied.
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
]

TITLE_FIND = "pilot program; post-retirement employment; reports."
TITLE_READ = ("pilot program; death benefits; designation of beneficiary; "
              "post-retirement employment; reports.")

D9_FIND = "that the member is advised to review the member's designation"


def main():
    d = get("/api/issues/%s/documents/%s" % (MOO42, KEY))
    body = d["body"]
    print("Live base: document revision %s, number %s" % (
        d.get("latestRevisionId"), d.get("latestRevisionNumber")))
    print("Title:     %s" % d.get("title"))
    s1 = sec1(body)
    print("Document %d chars; §1 %d chars; §1 <u>/</u> %d/%d\n" % (
        len(body), len(s1), s1.count("<u>"), s1.count("</u>")))

    # ---- the hazard, demonstrated rather than asserted
    print("The sequencing hazard that forces one composite:")
    print("  D9's FIND resolves %dx in the live §1." % s1.count(D9_FIND))
    u = s1
    u = u.replace(STEPS[3][1], STEPS[3][2].replace(EXCEPTION,
        "that the member is advised to review the member's designation of beneficiary"), 1)
    u = u.replace(STEPS[4][1], STEPS[4][2].replace(EXCEPTION,
        "that the member is advised to review the member's designation of beneficiary"), 1)
    print("  After D3c as counsel's pass left it, it resolves %dx — a dead anchor." % u.count(D9_FIND))
    print("  So D3c's two descriptive phrases are conformed to F9's wording, and the")
    print("  advisory is relocated and rewritten BEFORE the failure sentence is touched.\n")

    # ---- the composite
    cur = s1
    for name, f, r in STEPS:
        n = cur.count(f)
        status = "OK" if n == 1 else "*** DEAD ANCHOR ***"
        print("  %-52s FIND %4d chars  %dx  %s" % (name, len(f), n, status))
        if n != 1:
            sys.exit("anchor did not resolve exactly once; nothing applied")
        cur = cur.replace(f, r, 1)

    print()
    print("  §1            %d -> %d  (%+d)" % (len(s1), len(cur), len(cur) - len(s1)))
    print("  §1 <u>/</u>   %d/%d -> %d/%d" % (
        s1.count("<u>"), s1.count("</u>"), cur.count("<u>"), cur.count("</u>")))
    print("  series        %d items, advisory at %d -> %d items, advisory at %d" % (
        shape(s1, "that the member is advised to review") +
        shape(cur, "that the Board advises the member to review")))
    print("  semicolons in the series  %d -> %d" % (
        series_of(s1).count(";"), series_of(cur).count(";")))
    print("  'the member is advised to' left in §1: %d" % cur.count("the member is advised to"))
    print("  exception phrase in §1: %d (item, M exception, J limb)" % cur.count(EXCEPTION))

    # ---- the title
    print()
    print("  T2  title FIND resolves %dx in the document; %+d chars" % (
        body.count(TITLE_FIND), len(TITLE_READ) - len(TITLE_FIND)))
    if body.count(TITLE_FIND) != 1:
        sys.exit("title anchor did not resolve exactly once")

    nb = body.replace(s1, cur, 1).replace(TITLE_FIND, TITLE_READ, 1)
    print("  document      %d -> %d  (%+d)" % (len(body), len(nb), len(nb) - len(body)))

    # ---- post-conditions the Director asserted
    assert cur.count(EXCEPTION) == 3
    assert cur.count("the member is advised to") == 0
    assert s1.count("<u>") == cur.count("<u>") == 62
    assert shape(cur, "that the Board advises the member to review") == (7, 7)
    print("\nAll assertions pass. Nothing written to the store.")


if __name__ == "__main__":
    main()
