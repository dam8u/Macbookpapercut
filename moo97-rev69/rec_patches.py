#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Store revision 69 — in-place corrections to three self-descriptions of this document that
have stopped being true. The rule this document has applied since store revision 62: a stale
self-description is a defect of the record, and it is corrected where it stands.

None of these is inside §1. The kit asserts that.
"""
PATCHES = []


def p(_id, label, find, repl, n=1):
    PATCHES.append(dict(id=_id, label=label, find=find, repl=repl, n=n))


# --- §5's preamble: two figures and one omission -----------------------------
p("R1", "§5 preamble — the current sweep, the list it omitted (§5.44), and the headroom figure, "
        "which was ~180,000 characters and is now about 44,000",
  "The file now has roughly 180,000 characters of headroom against the store's 524,288-character "
  "ceiling, so **nothing has been moved out since store revision 58**, and §5 holds the sweep "
  "written by store revision 67 (**§5.@45@**, the first sweep in this file to report a widened "
  "footprint — the act now amends two sections and adds one) together with the sweeps for store "
  "revisions **65, 63, 62, 61, 60 and 59** — §§5.43, 5.42, 5.41, 5.40, 5.39 and 5.38.",

  "The file has about **41,000** characters of headroom against the store's 524,288-character "
  "ceiling, so **nothing has been moved out since store revision 58**, and §5 holds the sweep "
  "written by store revision 69 (**§5.@46@**, the Policy Director's three drafted answers out of "
  "[MOO-189](/MOO/issues/MOO-189)) together with the sweeps for store revisions **67, 66, 65, 63, "
  "62, 61, 60 and 59** — §§5.45, 5.44, 5.43, 5.42, 5.41, 5.40, 5.39 and 5.38.")

p("R2", "§5 preamble — the correction history, which had itself omitted the omission",
  "**This paragraph named the wrong two through store revisions 60 and 61, store revision 62 "
  "corrected it, store revision 63 did not bring it forward, and store revision 65 brings it "
  "current.**",
  "**This paragraph named the wrong two through store revisions 60 and 61, store revision 62 "
  "corrected it, store revision 63 did not bring it forward, and store revision 65 brought it "
  "current. Store revision 69 corrects it twice over: it had omitted §5.44, the sweep store "
  "revision 66 wrote and which has been in this section ever since, and its headroom figure was "
  "four times the truth.**")

# --- §6's preamble: it omitted §6.0-66 --------------------------------------
p("R3", "§6 preamble — the current note and the list, which omitted §6.0-66",
  " **Store revision 67 adds **§6.0-67**, so the sections below are the drafter's notes for that "
  "revision and for store revisions 65, 63, 62, 61, 60 and 59**",
  " **Store revision 69 adds **§6.0-69**, so the sections below are the drafter's notes for that "
  "revision and for store revisions 67, 66, 65, 63, 62, 61, 60 and 59 — and the list in this "
  "paragraph had omitted §6.0-66, which store revision 66 wrote**")

# --- §8's retention count ---------------------------------------------------
p("R4", "§8.1 — the retained-note count, which store revisions 68 and 69 each advanced",
  "and **store revision 67 makes it nine** — notes for store revisions 67, 65, 63, 62, 61, 60, "
  "59, 58 and 57 —",
  "store revision 67 said nine and **omitted §8's own note for store revision 66**, store "
  "revision 68 added a note without amending this sentence, and **store revision 69 makes it "
  "twelve, counted mechanically** — notes for store revisions 69, 68, 67, 66, 65, 63, 62, 61, "
  "60, 59, 58 and 57 —")

# --- two further record defects found while asserting this revision ---------
p("R5", "a quoted redline in the §0 record carried a stray closing underline tag at the end of "
        "the line, which is why the document's markup was 78 / 79; the document is balanced after "
        "this. §1's own 62 / 62 was never affected",
  "The <u>state agency</u> shall publish the policy.</u>",
  "The <u>state agency</u> shall publish the policy.")

p("R6", "the document's own H1 named one amended section; the act has amended two since store "
        "revision 67, and the bill's title line inside §1 has said so since",
  "# Bill text — S8 Earned-Service Repricing (military service purchase), § 51.1-142.2 and new "
  "§ 51.1-142.4",
  "# Bill text — S8 Earned-Service Repricing (military service purchase), §§ 51.1-142.2 and "
  "51.1-162 amended and new § 51.1-142.4")
