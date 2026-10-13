# -*- coding: utf-8 -*-
"""Build the redline of subdivision D 1 and of the bill's title line for the MOO-208 deliverable.

Two layers of markup, and the deliverable says so in terms:

  * `<u>…</u>` is the AMENDATORY markup against the Code of Virginia. The whole of subdivision D 1
    is new language in a new section, so all of it sits inside one `<u>` span and this revision
    adds no markup — which is why §1's `<u>`/`</u>` count is 62 / 62 before and after.
  * **bold** marks what store revision 70 ADDS and ~~strikethrough~~ what it STRIKES, as against
    store revision 69. That is the redline layer. It is not amendatory markup and it is not in the
    store.

The redline is built by reversing the five substitutions out of the LIVE text, so it cannot drift
from the store, and it is verified by stripping its own layer and comparing character for character
with the live provision. Sentinels are used during construction so that the `**D. 1.**` designator
already in the text is not mistaken for redline.
"""
import json, os, re, urllib.request

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
HERE = os.path.dirname(os.path.abspath(__file__))
AO, AC, DO, DC = "\x01", "\x02", "\x03", "\x04"   # add open/close, delete open/close

ADVISORY = (
    "that the Board advises the member to review the member's designation of beneficiary "
    "under subsection A of § 51.1-162, and the effect of that designation under subsection B "
    "of that section, before completing payment, that the member may make or change that "
    "designation under subsection A of that section at any time before the member's death, "
    "and that nothing in this subdivision requires the member to review the designation or "
    "affects any benefit by reason of the member's not having reviewed it"
)
EXCEPTION = ("that the Board advises the member to review the member's designation "
             "of beneficiary")
OLD_ADVISORY = ("that the member is advised to review the member's designation of beneficiary "
                "under subsection A of § 51.1-162 before completing payment")

# (live text, redline text) — each must resolve exactly once in the live provision.
PAIRS = [
    ("and no other designation has been made; that subsection C of § 51.1-162",
     f"and no other designation has been made;{DO} {OLD_ADVISORY};{DC} that subsection C of "
     f"§ 51.1-162"),
    (f"in the order of precedence that section states; and {ADVISORY}.",
     f"in the order of precedence that section states{AO}; and {ADVISORY}{AC}."),
    ("; that where no benefit is payable", f";{DO} and{DC} that where no benefit is payable"),
    (f"be stated in it, other than a failure to state {EXCEPTION}, is a failure of the Board",
     f"be stated in it{AO}, other than a failure to state {EXCEPTION},{AC} is a failure of the "
     f"Board"),
    (f"and the Board shall state every such failure, and every failure to state {EXCEPTION}, "
     f"in the report required by subsection J.",
     f"and the Board shall state every such failure{AO}, and every failure to state {EXCEPTION},"
     f"{AC} in the report required by subsection J."),
]

TITLE_PAIR = ("pilot program; death benefits; designation of beneficiary; post-retirement",
              f"pilot program; {AO}death benefits; designation of beneficiary;{AC} post-retirement")


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def get(p):
    r = urllib.request.Request(base() + p, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"]})
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


def unredline(s):
    """Strip the redline layer: additions kept, struck text dropped. Must give the live text."""
    s = re.sub(DO + ".*?" + DC, "", s, flags=re.S)
    return s.replace(AO, "").replace(AC, "")


def render(s):
    return s.replace(AO, "**").replace(AC, "**").replace(DO, "~~").replace(DC, "~~")


def main():
    doc = get(f"/api/issues/{MOO42}/documents/bill-text-s8")
    rev = max(int(x) for x in re.findall(r"^### 0\.0-(\d+) ", doc["body"], re.M))
    assert rev == 70, f"live document is at store revision {rev}, expected 70"
    live1 = sec1(doc["body"])

    a = live1.index("<u>**D. 1.**")
    z = live1.index("</u>", live1.index("every period that runs from the giving of it is extended "
                                        "by three days.")) + 4
    d1 = live1[a:z]
    assert d1.count("<u>") == d1.count("</u>") == 1, (
        "subdivision D 1 is expected to be one <u> span; it is "
        f"{d1.count('<u>')}/{d1.count('</u>')}")

    red = d1
    for i, (f, r) in enumerate(PAIRS, 1):
        n = red.count(f)
        assert n == 1, f"redline step {i}: live anchor resolves {n}x, expected 1"
        red = red.replace(f, r, 1)
    assert unredline(red) == d1, "redline does not strip back to the live provision"

    title = [l for l in live1.split("\n") if "A BILL to amend" in l][0]
    assert title.count(TITLE_PAIR[0]) == 1
    tred = title.replace(*TITLE_PAIR)
    assert unredline(tred) == title, "title redline does not strip back"

    print(f"D 1: live {len(d1)} chars, one <u> span, redline strips back exactly")
    print(f"title line: redline strips back exactly")
    open(os.path.join(HERE, "redline-d1.md"), "w", encoding="utf-8").write(
        render(tred) + "\n\n" + render(red) + "\n")
    open(os.path.join(HERE, "d1-as-amended.md"), "w", encoding="utf-8").write(d1 + "\n")
    print("written: redline-d1.md, d1-as-amended.md")


main()
