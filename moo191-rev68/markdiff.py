#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Word-level amendatory marking, shared by markup2.py and build_disposition.py.

Subdivision D 1 sits inside an open `<u>` run — § 51.1-142.4 is a new section, underlined end to
end in the bill text — so a candidate's own delta cannot be shown with `<u>` or `~~` without
nesting a marker inside a marker or reading as a deletion from the Code rather than from the
draft. It is marked `[ADDED: ...]` / `[STRUCK: ...]` against the draft instead, and every marking
is asserted to reconstruct both the live text and the post-edit text.
"""
import difflib, re

def toks(s):
    return re.findall(r"\S+|\s+", s)


def wrap(s, open_mk, close_mk):
    """Mark s, leaving its leading and trailing whitespace outside the markers."""
    core = s.strip()
    lead = s[:len(s) - len(s.lstrip())]
    trail = s[len(s.rstrip()):]
    return f"{lead}{open_mk}{core}{close_mk}{trail}"


def coalesce(ops, bridge=3):
    """Absorb a short equal run that sits between two changes into one change.

    difflib minimises characters, not legibility: for `member is advised` -> `Board advises the
    member` it keeps `member` equal in the middle and emits an insert, an equal and a delete, which
    renders as `the [ADDED: Board advises the] member [STRUCK: is advised] to review`. A drafter
    expects the old phrase struck whole and the new phrase added whole. `bridge` is in tokens, and
    whitespace tokens count, so 3 bridges at most one short word."""
    out = []
    for op in ops:
        op = tuple(op)
        if (out and op[0] != "equal" and out[-1][0] != "equal"):
            _, i1, _, j1, _ = out.pop()
            out.append(("replace", i1, op[2], j1, op[4]))
            continue
        if (len(out) >= 2 and op[0] != "equal" and out[-1][0] == "equal"
                and out[-2][0] != "equal" and out[-1][2] - out[-1][1] <= bridge):
            out.pop()
            _, i1, _, j1, _ = out.pop()
            out.append(("replace", i1, op[2], j1, op[4]))
            continue
        out.append(op)
    return out


def mark(old, new):
    """Return (marked, as_was, as_amended). The two reconstructions are built in the same walk as
    the marked string, so they are exact rather than recovered by stripping brackets — bracket
    stripping cannot be exact, because deleting an inserted run leaves the space beside it."""
    a, b = toks(old), toks(new)
    out, was, amended = [], [], []
    for tag, i1, i2, j1, j2 in coalesce(
            difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()):
        if tag == "equal":
            out.append("".join(b[j1:j2]))
            was.append("".join(a[i1:i2]))
            amended.append("".join(b[j1:j2]))
            continue
        o, n = "".join(a[i1:i2]), "".join(b[j1:j2])
        was.append(o)
        amended.append(n)
        for text, mk in ((o, "STRUCK"), (n, "ADDED")):
            if not text:
                continue
            if text.strip():
                out.append(wrap(text, "**[" + mk + ": ", "]**"))
            else:
                out.append(text)
    return "".join(out), "".join(was), "".join(amended)


STRUCK = re.compile(r"\*\*\[STRUCK: (.*?)\]\*\*", re.S)
ADDED = re.compile(r"\*\*\[ADDED: (.*?)\]\*\*", re.S)
WS = re.compile(r"\s+")


def check(marked, was, amended, old, new):
    """The walk must reconstruct both sides exactly, and the marked string as a reader reads it —
    ignoring the ADDED runs, then ignoring the STRUCK runs — must match both sides too."""
    assert was == old, "the walk does not reconstruct the live text"
    assert amended == new, "the walk does not reconstruct the post-edit text"
    def flat(s):
        return WS.sub(" ", s).strip()

    read_as_was = flat(ADDED.sub("", STRUCK.sub(r"\1", marked)))
    read_as_amended = flat(STRUCK.sub("", ADDED.sub(r"\1", marked)))
    assert read_as_was == flat(old), "read with the additions ignored, it is not the live text"
    assert read_as_amended == flat(new), "read with the strikes ignored, it is not amended"
    assert "<u>" not in marked and "~~" not in marked, "emitted a bill marker inside an open run"
    assert marked.count("**[") == marked.count("]**"), "unbalanced bracket"


