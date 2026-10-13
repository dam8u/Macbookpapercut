#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render each MOO-195 candidate as amendatory markup against the live base, word by word.

Supersedes markup.py, which diffed character by character and produced markup no drafter would
recognise — `that the ~~membe~~<u>Boa</u>r~~ is~~<u>d</u> advise~~d~~<u>s the member</u>` — and which
printed two candidates (D3a, D5) with no markup at all, because its span logic lost edits that
cross a sentence boundary.

This version:

  * diffs on word boundaries, so a changed phrase is marked whole and its replacement marked
    whole, with whitespace kept outside the markers;
  * takes the span from the OUTPUT as well as the input, so an edit that inserts or extends a
    sentence is captured instead of falling outside the window;
  * prints each touched passage once, not once per edit;
  * does NOT emit `<u>` or `~~` inside the passage. Subdivision D 1 sits inside an open `<u>` run
    — the whole of § 51.1-142.4 is new language and is underlined end to end in the bill text, and
    the passage itself carries no marker of its own (verified: 0 `<u>`, 0 `</u>`, 0 `~~` between
    the series' first word and the failure sentence's last). Underlining a candidate's additions
    there would nest a marker inside a marker, and striking them would read as language deleted
    from the Code rather than from the draft. So a candidate's own delta is marked `[ADDED: …]`
    and `[STRUCK: …]`, against the draft, and the `<u>`/`</u>` balance is reported unchanged;
  * ASSERTS, for every candidate, that stripping the ADDED brackets reproduces the live text
    exactly and stripping the STRUCK brackets reproduces the post-edit text exactly. A candidate
    whose markup does not reconstruct both sides is a failure, not a warning.

    python3 markup2.py > markup2.md
"""
import re, sys

sys.argv = [sys.argv[0]]
src = open("candidates.py", encoding="utf-8").read().replace("sys.exit(main())", "")
ns = {"__name__": "cand"}
exec(compile(src, "candidates.py", "exec"), ns)

get, sec1, C = ns["get"], ns["sec1"], ns["C"]
MOO42, KEY, series_of, shape = ns["MOO42"], ns["KEY"], ns["series_of"], ns["shape"]

FAIL_A = "A failure to state in the Board's certification"
FAIL_Z = "The member shall file the notice of retirement required by § 51.1-153"


def failure_of(s):
    """The failure sentence, plus anything inserted between it and the next sentence."""
    return s[s.index(FAIL_A):s.index(FAIL_Z)]


from markdiff import mark, check, WS  # noqa: E402

doc = get(f"/api/issues/{MOO42}/documents/{KEY}")
S1 = sec1(doc["body"])
rev = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", doc["body"], re.M))

SERIES_A = "The Board's certification shall also state that,"
assert S1[S1.index(SERIES_A):S1.index(FAIL_Z)].count("<u>") == 0
assert S1[S1.index(SERIES_A):S1.index(FAIL_Z)].count("~~") == 0

print(f"# MOO-195 candidates — the passages as they would read, against store revision {rev}\n")
print(f"Base: document revision `{doc['latestRevisionId'][:8]}`, §1 **{len(S1):,}** characters, "
      f"`<u>`/`</u>` **{S1.count('<u>')} / {S1.count('</u>')}**.\n")
print("**Marking convention, and why it is not underline and strikethrough.** Subdivision D 1 is "
      "inside an open `<u>` run: § 51.1-142.4 is a new section, so it is new language underlined "
      "end to end in the bill text, and the passage carries no marker of its own (asserted: 0 "
      "`<u>`, 0 `</u>`, 0 `~~` from the series' first word to the failure sentence's last). "
      "Underlining a candidate's addition there would nest a marker inside a marker, and striking "
      "it would read as language deleted from the Code rather than from the draft. So each "
      "candidate's own delta is marked **[ADDED: …]** and **[STRUCK: …]** *against the draft*, and "
      "the `<u>`/`</u>` balance is reported for each. In the bill as introduced every word below "
      "is underlined. Each passage is reproduced in full as it would read, and each candidate's "
      "marking is asserted to reconstruct both the live text and the post-edit text exactly.\n")

PASSAGE = (("the certification series of subdivision D 1, in full as amended", series_of),
           ("subdivision D 1's failure sentence, in full as amended", failure_of))

for c in C:
    out = S1
    for find, read in c["edits"]:
        assert out.count(find) == 1, f"{c['id']}: anchor resolves {out.count(find)}x in §1"
        out = out.replace(find, read, 1)
    items, at = shape(out, c["probe"])
    print(f"## {c['id']} — {c['finding']}  ({len(out) - len(S1):+,} characters)\n")
    for label, span in PASSAGE:
        old, new = span(S1), span(out)
        if old == new:
            continue
        marked, was, amended = mark(old, new)
        check(marked, was, amended, old, new)
        print(f"**{label}.**\n")
        print("> " + marked.replace("\n", " ") + "\n")
    print(f"*After: the series has {items} items and the advisory is item {at} of {items}; "
          f"`<u>`/`</u>` {out.count('<u>')} / {out.count('</u>')}, unchanged.*\n")

print("*Every candidate's markup reconstructs both sides exactly; every anchor resolved once.*")
