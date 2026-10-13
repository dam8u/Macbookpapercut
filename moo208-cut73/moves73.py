# -*- coding: utf-8 -*-
"""Store revision 73 — the retention rotation, each block verbatim, each leaving a stub.

The four blocks are the ones §5's and §6's own preambles had already named as next to move. A
block is moved only if it is NOT already a stub (asserted in apply73.py), so this revision cannot
re-stub a stub or date another revision's move to itself.
"""

VOL2 = ("[`bill-text-s8-revision-history-2`]"
        "(/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2)")

_WHY = ("**Moved verbatim** to " + VOL2 + ", in store revision 73, because the file arrived "
        "21,702 characters from the 524,288-character ceiling and could not take store revision "
        "73's record layer. This is the rotation {sec}'s own preamble had already named. A "
        "reference of the form **{ref}** resolves there. Its durable result: {res}")

MOVES = [
    dict(id="M1", head="### §5.44", stop="### §5.43",
         stub_head="### §5.44 Store revision 66 — performed; the sweep is moved verbatim to the "
                   "retained-record document in store revision 73",
         stub=_WHY.format(sec="§5", ref="§5.44",
                          res="store revision 66's two insertions and sixteen substitutions "
                              "chased in both directions, with **four conforming amendments "
                              "required and all four enacted in that revision**, and the finding "
                              "that *\"required or permitted\"* is the act's own existing word "
                              "pair — already in subsection F — so that the deeming sentence "
                              "reaches both of subdivision G 4's commanded releases and any "
                              "release the act permits without commanding.")),

    dict(id="M2", head="### §5.43", stop="### §5.42",
         stub_head="### §5.43 Store revision 65 — performed; the sweep is moved verbatim to the "
                   "retained-record document in store revision 73",
         stub=_WHY.format(sec="§5", ref="§5.43",
                          res="store revision 65's one substitution — the designation-review "
                              "advisory — chased in both directions with **no conforming "
                              "amendment required**, and the precision that the compound "
                              "*\"designation of beneficiary\"* appears neither in § 51.1-162 A "
                              "nor anywhere else in the act, while its component vocabulary is "
                              "that subsection's own.")),

    dict(id="M3", head="### §6.0-65", stop="### §6.0-63",
         stub_head="### §6.0-65 Ambiguities resolved in store revision 65 — performed; moved "
                   "verbatim to the retained-record document in store revision 73",
         stub=_WHY.format(sec="§6", ref="§6.0-65",
                          res="why the advisory is not a duty and why the operative verb belongs "
                              "to the Board's carrier sentence — **the reasoning that survived "
                              "the Director's F9 and F4 decisions at "
                              "[MOO-208](/MOO/issues/MOO-208) although both of its conclusions "
                              "were reversed**, the item no longer reading *\"is advised to "
                              "review\"* and no longer sitting where that note put it.")),

    dict(id="M4", head="### §6.0-63", stop="### §6.0-62",
         stub_head="### §6.0-63 Ambiguities resolved in store revision 63 — performed; moved "
                   "verbatim to the retained-record document in store revision 73",
         stub=_WHY.format(sec="§6", ref="§6.0-63",
                          res="why subsection M 2's deemed denial follows **the filing** and not "
                              "*\"the member\"* — the only fact common to all seven categories "
                              "of person who may seek reconsideration — why the denial falls on "
                              "the first day after the 30 days and not the last, and the rule "
                              "that **a cure for a residual must not move a priced endpoint in "
                              "passing**, which is why the denial is not deemed an act of the "
                              "Board.")),
]

# The two self-descriptions that go stale the moment the rotation is performed. This file has
# recorded a stale preamble as a defect of the record three times; it is not going to write a
# fourth.
PATCHES = [
    dict(id="73-P1", label="§5's preamble: what §5 holds, and the next rotation",
         find="§5 therefore holds the sweep written by store revision 70 (**§5.47**, the Policy "
              "Director's composite out of [MOO-191](/MOO/issues/MOO-191), and the first sweep in "
              "this file to report a change to the bill's title line) together with the sweep "
              "written by store revision 71 (**§5.48**, which disposes two counsel passes in one "
              "revision) and the sweeps for store revisions **69, 67, 66 and 65** — §§5.46, 5.45, "
              "5.44 and 5.43.",
         repl="**Store revision 73 moved §5.43 and §5.44 out** — the rotation the last sentence "
              "of this paragraph had named — on arriving 21,702 characters from the ceiling and "
              "being unable to write its record layer at all. **§5 therefore holds five sweeps: "
              "§5.49** (store revision 73, the Policy Director's six approved cures, with two "
              "adverse results), **§5.48** (store revision 71, which disposes two counsel passes "
              "in one revision), **§5.47** (store revision 70, the composite out of "
              "[MOO-191](/MOO/issues/MOO-191), and the first sweep in this file to report a "
              "change to the bill's title line) and **§5.46** (store revision 69), together with "
              "**§5.45** for store revision 67.",
         n=1),
    dict(id="73-P2", label="§5's preamble: the next two to move",
         find="The next revision that is short of room should move **§5.43 and §5.44** out first.",
         repl="**The next revision that is short of room should move §5.45 and §5.46 out "
              "first**, which would leave §5 holding the current sweep and its two predecessors.",
         n=1),
    dict(id="73-P3", label="§6's preamble: what §6 holds, and the next rotation",
         find="**Store revision 71 adds **§6.0-71**, so the sections below are the drafter's "
              "notes for that revision and for store revisions 70, 69, 67, 66, 65 and 63 — the "
              "notes for store revisions 62, 61, 60 and 59 were moved out in store revision 71, "
              "which is what §6's own preamble had told the next revision short of room to do**",
         repl="**Store revision 73 adds **§6.0-73** and moves §6.0-63 and §6.0-65 out — the "
              "rotation this paragraph had named — so the sections below are the drafter's notes "
              "for store revisions 73, 71, 70, 69, 67 and 66; the notes for store revisions 62, "
              "61, 60 and 59 went out in store revision 71 on the same instruction**",
         n=1),
    dict(id="73-P4", label="§6's preamble: the gaps, and the next two to move",
         find="**§6.0-63 and §6.0-65 are the next to go.**",
         repl="**Store revision 73 performed both halves of the rotation at once**, §5.43 and "
              "§5.44 with §6.0-63 and §6.0-65, rather than leaving the second half to a revision "
              "that would have to move it under pressure as store revision 71 did. **§6.0-66 and "
              "§6.0-67 are the next to go.**",
         n=1),
    dict(id="73-P5", label="§6's preamble: the gap list, which store revision 73 does not join",
         find="so **the gaps at §6.0-64, §6.0-68 and §6.0-72 are those revisions' silence and not "
              "lost notes.**",
         repl="so **the gaps at §6.0-64, §6.0-68 and §6.0-72 are those revisions' silence and not "
              "lost notes** — store revision 73 writes a note of its own and does not join that "
              "list.",
         n=1),
    dict(id="73-P6", label="§6's preamble: the retention sentence, brought current",
         find="the next revision that is short of room should move §6.0-63 and §6.0-65 out first.",
         repl="the next revision that is short of room should move §6.0-66 and §6.0-67 out "
              "first.",
         n=1),
]
