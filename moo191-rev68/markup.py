#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render each MOO-195 candidate as amendatory markup against the live base.

Underline marks what the candidate would ADD to store revision 68; strikethrough marks what it
would strike. The marking is produced by difflib on the live sentence and the post-edit sentence,
not by hand, so the document cannot drift from what the substitution actually does.

    python3 markup.py > markup.md
"""
import difflib, importlib, re, sys

sys.argv = [sys.argv[0], "--no-run"]
spec = importlib.util.spec_from_file_location("cand", "candidates.py")

# candidates.py calls sys.exit at import; run it in a guarded namespace instead.
src = open("candidates.py", encoding="utf-8").read().replace("sys.exit(main())", "")
ns = {"__name__": "cand"}
exec(compile(src, "candidates.py", "exec"), ns)

get, sec1, C = ns["get"], ns["sec1"], ns["C"]
MOO42, KEY = ns["MOO42"], ns["KEY"]
series_of, shape = ns["series_of"], ns["shape"]

doc = get(f"/api/issues/{MOO42}/documents/{KEY}")
S1 = sec1(doc["body"])


def sentence_span(text, idx, width=0):
    """The smallest unit of `text` containing offset idx: the '; ' clause inside the certification
    series, else the '. ' sentence. `width` extends the span by that many characters each way,
    clamped to the nearest boundary, so a reader sees the clause in its neighbours' company."""
    a = max(text.rfind(". ", 0, idx) + 2, text.rfind("; ", 0, idx) + 2, 0)
    z1, z2 = text.find(". ", idx), text.find("; ", idx)
    z = min(x for x in (z1 + 1 if z1 >= 0 else len(text), z2 + 1 if z2 >= 0 else len(text), len(text)))
    if width:
        a = max(text.rfind(". ", 0, max(a - width, 0)) + 2, 0) or a
    return text[a:z]


def mark(old, new):
    out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag == "equal":
            out.append(new[j1:j2])
        else:
            if i2 > i1:
                out.append("~~" + old[i1:i2] + "~~")
            if j2 > j1:
                out.append("<u>" + new[j1:j2] + "</u>")
    return "".join(out)


print("# MOO-195 candidates — amendatory markup against store revision 68\n")
print(f"Base: document revision `{doc['latestRevisionId'][:8]}`, §1 {len(S1)} characters.\n")
for c in C:
    out = S1
    for find, read in c["edits"]:
        out = out.replace(find, read, 1)
    print(f"## {c['id']} — {c['finding']}  ({len(out) - len(S1):+d} characters)\n")
    for find, read in c["edits"]:
        i = S1.index(find)
        old_s = sentence_span(S1, i)
        # locate the same sentence in the post-edit text by its unchanged opening
        head = old_s[:60]
        new_s = sentence_span(out, out.index(head)) if head in out else old_s
        print("> " + mark(old_s, new_s).replace("\n", " ") + "\n")
    items, at = shape(out, c["probe"])
    print(f"*Series after: {items} items, advisory at item {at}.*\n")
