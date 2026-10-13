#!/usr/bin/env python3
"""MOO-212 item 1 — set every dateline in the ten documents to the revision checked at.

A dateline states the revision at which the text was checked. It is not a label, so this
script refuses to run unless the bill-dependent surface verifies against the same live file
in the same pass: verify_surface.py and blocks.py are invoked here and a non-zero exit from
either aborts the sweep. Nobody advances a dateline by editing the number.

    python3 set_datelines.py live71.md 71

VERSION.md, the VERSIONS.md row and CURRENT are not touched here; they are the freeze record
and are written by hand after this passes.

Three occurrences name a revision as history rather than as a dateline and are protected:
C2's account of where it was first checked, and C1's account of what revisions 70 and 71
changed. "Store revision 76" is v2.0's mislabelled document-revision number, printed as a
correction, and is never matched.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/Users/davidmoody/AgentCreated/v2.1/08-markdown-sources"

PROTECTED = [
    "at store revision 69, counted",                 # C2: where it was first checked
    "What store revision 70 changed in D 1",         # C1: what revision 70 did
    "store revision 70 to store revision 71",        # C1/C2: unchanged across those two
]
# The Paperclip document-revision counter, which is a different counter from the bill's own.
DOC_COUNTER = ("the document counter stood at **88**", "the document counter stood at **90**")


def run(script, live):
    r = subprocess.run([sys.executable, os.path.join(HERE, script), live],
                       capture_output=True, text=True)
    lines = [l for l in r.stdout.strip().split("\n") if l.strip()]
    print(f"  {script}: exit {r.returncode}")
    for l in lines:
        if re.match(r"^(\d+ of \d+ blocks|\d+ bill quotation)", l) or "FAIL" in l:
            print("      " + l)
    return r.returncode


def main():
    live = sys.argv[1] if len(sys.argv) > 1 else "live.md"
    want = sys.argv[2] if len(sys.argv) > 2 else None
    body = open(os.path.join(HERE, live), encoding="utf-8").read()
    m = re.search(r"store revision (\d+) · (\d+ \w+ \d{4})", body)
    rev, date = m.group(1), m.group(2)
    assert want is None or want == rev, f"asked for {want}, the live file is {rev}"

    print(f"gate — the bill-dependent surface must verify at store revision {rev} first:")
    if run("verify_surface.py", live) or run("blocks.py", live):
        print("\nABORTED: the surface does not verify at this revision, so no dateline moves.")
        return 1

    print(f"\nsetting every dateline to store revision {rev} ({date})")
    total = 0
    for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        t = open(p, encoding="utf-8").read()
        marks = {}
        for n, h in enumerate(PROTECTED):
            if h in t:
                key = f"\x00H{n}\x00"
                marks[key] = h
                t = t.replace(h, key)
        n = len(re.findall(r"store revision (?!76)\d+", t))
        t = re.sub(r"store revision (?!76)\d+", f"store revision {rev}", t)
        if DOC_COUNTER[0] in t:
            t = t.replace(*DOC_COUNTER)
            print(f"  {os.path.basename(p)}: document-revision counter 88 -> 90")
        for key, h in marks.items():
            t = t.replace(key, h)
        if n:
            open(p, "w", encoding="utf-8").write(t)
            print(f"  {os.path.basename(p)}: {n} dateline(s) -> {rev}")
            total += n

    print(f"\n{total} dateline(s) set to store revision {rev}")

    # The package speaks at one revision, and every other number it prints is protected history.
    stale = []
    for p in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        t = open(p, encoding="utf-8").read()
        for mm in re.finditer(r"store revision (\d+)", t):
            if mm.group(1) == rev or mm.group(1) == "76":
                continue
            ctx = t[max(0, mm.start() - 70):mm.end() + 70]
            if not any(h in ctx for h in PROTECTED):
                stale.append(f"{os.path.basename(p)}: store revision {mm.group(1)}  …{ctx}…")
    for s in sorted(set(stale)):
        print("  UNPROTECTED OTHER REVISION — " + s)
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
