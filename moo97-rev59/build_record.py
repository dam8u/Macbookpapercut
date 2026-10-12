#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble and PUT `moo161-disposition` on MOO-97.

§2 (the redline) and §5 (the counts and the three provisions in full) are
GENERATED from edits.py and from the body that was actually written, so no
operative string in the record is retyped.
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

MOO97 = os.environ["PAPERCLIP_TASK_ID"]
KEY = os.environ["PAPERCLIP_API_KEY"]
RUN = os.environ.get("PAPERCLIP_RUN_ID", "")
BASE = os.environ["PAPERCLIP_API_URL"].rstrip("/")
if BASE.endswith("/api"):
    BASE = BASE[:-4]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from edits import EDITS  # noqa: E402

LAB = json.load(open(os.path.join(HERE, "out-labels.json")))
NEW = open(os.path.join(HERE, "out-body.md")).read()
OLD = open(os.path.join(HERE, "bill_live2.md")).read()

FINDINGS = {
    "E1": "**F1 (fatal), F2, F15.** The disapplication deleted; the sentence confined to the notification window; the computation base stated.",
    "E2": "**F17, F12, F13, F14.** The waiver split from the election; a fiduciary addressee for a minor and the review clock run from the notice to the person who can act; *\"that date\"* resolved; the rider extended to the amount.",
    "E3": "**F18.** The subsection J hook made person-specific, because E3c created several periods and not one.",
    "E4": "**The Policy Director's F13(c).** A 30-day duty on the employing state agency, with a subsection J line.",
    "E5": "**The Policy Director's F13(e).** The 90-day redetermination run, in the death case, from the date the Board learns of the death.",
    "E6": "**The Policy Director's F10/F11, F9(a)(i) and F9(b).** The release fired where no allowance is payable at all; the cap restored only so far as nothing has been paid under subsection N; a released amount reinstated where the determination is reversed on review.",
    "E7": "**F6.** C 2's in-service condition stated, its own greater-of disclosed, and its payee given by cross-reference rather than by paraphrase.",
    "E8": "**F4.** § 51.1-162 C pays a surviving spouse, minor children **and** parents.",
    "E9": "**F5.** § 51.1-162 A's condition is subsection B alone; subsection C is not mentioned in it.",
    "E10": "**F9.** The omission is a **failure** of the Board, not a determination, and its review period runs 30 days from the G 4 death notice.",
    "E11": "**F9.** M 2's failure limb widened to reach a notice or certification given on time with a required matter left out, and its three filing windows named by kind.",
    "E12": "**F8, F19, F20.** The open class replaced in the reconsideration limb.",
    "E13": "**F8, F19, F20.** The same replacement in the judicial-review limb, as rebuilt by store revision 59.",
}

COUNT_ROWS = [
    ("162", "`§ 51.1-162`", "Nine new references, all inside the three provisions edited."),
    ("163", "`§ 51.1-163`", "**Unchanged in number, changed in composition**: one deleted (the disapplication), one added (C 2's measure, in the certification)."),
    ("165", "`§ 51.1-165` bare", "Unchanged. No displacement added or removed."),
    ("16501", "`§ 51.1-165.01`", "Unchanged. Store revision 58's subsection F limb is untouched."),
    ("153", "`§ 51.1-153`", "Unchanged."),
    ("1422", "`§ 51.1-142.2`", "Unchanged."),
    ("207", "`§ 51.1-207`", "**Still zero — this is finding F10.**"),
    ("218", "`§ 51.1-218`", "**Still zero — this is finding F10.**"),
    ("subJ", "`subsection J`", "One new reporting duty (the state agency's death notice). No amendment to subsection J is needed."),
    ("subN", "`subsection N`", "One new reference (the cap restoration measured by what has been paid). Subsection N is not amended."),
    ("subM", "`subsection M`", "Two new references (the certification's failure limb; the reinstatement on review)."),
    ("notice_class", "`other person to whom this section requires a notice to be given`", "**2 to 0.** The unbounded class is gone from both of M 2's lists."),
]


def provision(text, prefix):
    sec = text[text.index("### <u>§ 51.1-142.4"):text.index("### Remaining enactment clauses")]
    hits = [p for p in sec.split("\n\n") if p.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0]


def main():
    out = [open(os.path.join(HERE, "rec_head.md")).read().rstrip(), ""]

    # ----------------------------------------------------------- §2 redline
    out.append("---\n\n## 2. The thirteen substitutions, verbatim\n")
    out.append("**Every FIND below is the live text of store revision 60 and every READ is the text of "
               "store revision 61.** Underlining in the bill marks language new to the Code, so these "
               "strings are reproduced as they stand in the act rather than re-marked here.\n")
    for label, find, repl in EDITS:
        key = label.split(" ")[0]
        out.append("### %s\n" % label)
        out.append(FINDINGS.get(key, ""))
        out.append("\n**FIND** (%d characters):\n\n> %s\n" % (len(find), find.replace("\n", " ")))
        out.append("**READ** (%d characters, %+d):\n\n> %s\n" % (len(repl), len(repl) - len(find),
                                                                 repl.replace("\n", " ")))

    mid = open(os.path.join(HERE, "rec_mid.md")).read()
    cut = mid.index("## 6. Ambiguities resolved")
    out.append("---\n\n" + mid[:cut].rstrip() + "\n")

    # ------------------------------------------- §5 counts and provisions
    out.append("---\n\n## 5. Cross-reference check — performed in both directions\n")
    out.append("**Counted by machine over §1 alone**, on the body that was written and then re-counted on "
               "the body the store returned. §1 goes from **%d** to **%d** characters; **three lines of §1 "
               "differ** and they are the three provisions below.\n"
               % (len(OLD[OLD.index("## 1. The bill"):OLD.index("## 2. Section-by-section")]),
                  len(NEW[NEW.index("## 1. The bill"):NEW.index("## 2. Section-by-section")])))
    out.append("| Citation | Before | After | Note |\n|---|---|---|---|")
    for key, lbl, note in COUNT_ROWS:
        a, b = LAB["counts"][key]
        out.append("| %s | %d | %d | %s |" % (lbl, a, b, note))
    out.append("""
**Conforming amendments elsewhere in the Code: none.**

- **Outward.** The sections this revision newly cites — § 51.1-162 and § 51.1-163 — have their **operation unaltered by it**. The only operative displacements in the act are those enacted in store revision 58, each confined to a named subdivision or limb (§ 51.1-165 C 1, and so much of § 51.1-165.01 F as requires payment in accordance with § 51.1-163). **This revision removes a purported disapplication of § 51.1-163 and adds none.**
- **Inward.** **No section of the Code cross-references § 51.1-142.4**, because the act adds it. §§ 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 are **not amended by this act** and say nothing about it. That is the standing risk this record has carried since §5.19 of the bill document: a reader of § 51.1-165 alone will not find the displacement. **It must travel in the drafting request to Division of Legislative Services, because a drafter's note is not enacted.**
- **Internally.** Two sentences are added to subdivision G 4, so all **eleven** of its *"preceding sentence"* references were re-resolved positionally on the written body against the antecedent each had before the edit. **All eleven resolve to the same sentence; zero mismatches.** The subdivision has no *"preceding clause"* reference, and this revision does not create one. The one new reference — in the reinstatement sentence — resolves to the release sentence immediately before it.
- **The §7 item list is a second document now.** Store revision 59 moved it to [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list). This revision writes **item 128** there and marks **item 122** with what the Director enacted; the item list is asserted contiguous **1 to 128** before and after, so a reference of the form *"§7 item n"* still resolves.
""")

    for prefix, title in (("<u>4. Subdivisions 2 and 3 shall not apply", "Subdivision G 4 of new § 51.1-142.4, in full as amended"),
                          ("<u>**D. 1.**", "Subdivision D 1 of new § 51.1-142.4, in full as amended"),
                          ("<u>2. A member, retiree", "Subsection M 2 of new § 51.1-142.4, in full as amended")):
        out.append("### %s\n" % title)
        out.append(provision(NEW, prefix) + "\n")

    out.append("---\n\n" + mid[cut:].rstrip() + "\n")
    out.append("---\n\n" + open(os.path.join(HERE, "rec_tail.md")).read().rstrip() + "\n")

    body = "\n".join(out)
    open(os.path.join(HERE, "record.md"), "w").write(body)
    print("record assembled: %d chars" % len(body))

    if "--write" not in sys.argv:
        print("DRY RUN")
        return

    url = BASE + "/api/issues/%s/documents/moo161-disposition" % MOO97
    payload = {"title": "MOO-161 disposition — store revision 61: 20 findings disposed, 13 "
                        "substitutions enacted (the fatal finding cured by deletion), 7 answers drafted",
               "format": "markdown", "body": body, "baseRevisionId": None}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="PUT")
    req.add_header("Authorization", "Bearer " + KEY)
    req.add_header("Content-Type", "application/json")
    if RUN:
        req.add_header("X-Paperclip-Run-Id", RUN)
    try:
        with urllib.request.urlopen(req) as r:
            d = json.loads(r.read().decode() or "{}")
            d = d.get("document", d)
            print("WRITTEN: %s, %d chars" % (d.get("latestRevisionId"), len(d.get("body") or "")))
    except urllib.error.HTTPError as e:
        print("FAILED %s %s" % (e.code, e.read().decode()[:400]))
        sys.exit(2)


if __name__ == "__main__":
    main()
