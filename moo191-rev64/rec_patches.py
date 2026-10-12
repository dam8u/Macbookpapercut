# -*- coding: utf-8 -*-
"""Record-layer patches for store revision 65. Same FIND/READ discipline as edits.py.

None of these touches §1. Each is asserted at count 1 over the whole document before any
substitution, and apply.py asserts afterwards that §1 changed on exactly one line.

The byline is not here: store revision 64 left it reading "store revision 63", so apply.py
patches it from whatever the live byline actually says and reports the drift.
"""

PATCHES = []


def P(i, label, find, repl, n=1):
    PATCHES.append(dict(id=i, label=label, find=find, repl=repl, n=n))


P("R2", "§5 preamble — name the live sweeps and the real headroom truthfully",
"The file now has roughly 250,000 characters of headroom against the store's 524,288-character ceiling, so **nothing has been moved out since store revision 58**, and §5 holds the sweeps for store revisions **62, 61, 60 and 59** — §§5.41, 5.40, 5.39 and 5.38. **This paragraph named the wrong two through store revisions 60 and 61 and is corrected here.**",
"The file now has roughly 180,000 characters of headroom against the store's 524,288-character ceiling, so **nothing has been moved out since store revision 58**, and §5 holds the sweeps for store revisions **65, 63, 62, 61, 60 and 59** — §§5.43, 5.42, 5.41, 5.40, 5.39 and 5.38. **Store revision 64 changed no word of either section and wrote no sweep, which is why there is no §5 entry for it.** **This paragraph named the wrong two through store revisions 60 and 61, store revision 62 corrected it, store revision 63 did not bring it forward, and store revision 65 brings it current.**")

P("R3", "§6 preamble — name the live notes truthfully",
"**The 4 sections below are the drafter's notes for store revisions 62, 61, 60 and 59.** This paragraph named store revisions 54 back to 52 through store revisions 59, 60 and 61, none of which corrected it; **it is corrected here, and the rule that a stale self-description is a defect of the record is the reason**.",
"**The 6 sections below are the drafter's notes for store revisions 65, 63, 62, 61, 60 and 59** — store revision 64 changed no word of either section and wrote no note of its own, so **the gap at §6.0-64 is that revision's silence and not a lost note.** This paragraph named store revisions 54 back to 52 through store revisions 59, 60 and 61, none of which corrected it; **it was corrected in store revision 62, store revision 63 added §6.0-63 without updating the count, and store revision 65 brings it current, because the rule that a stale self-description is a defect of the record applies to this paragraph twice over**.")

P("R4", "§8.1 — eight notes, and which two move first",
"**Store revision 62 makes it six** — notes for store revisions 62, 61, 60, 59, 58 and 57 — because the ceiling no longer forces a move and moving another run's record in the heartbeat it was written is how a record gets double-stubbed. **The note for store revision 57 is the one to move first.**",
"**Store revision 62 made it six**, store revision 63 made it seven without saying so, store revision 64 added none, and **store revision 65 makes it eight** — notes for store revisions 65, 63, 62, 61, 60, 59, 58 and 57 — because the ceiling no longer forces a move and moving another run's record in the heartbeat it was written is how a record gets double-stubbed. **The notes for store revisions 57 and 58 are the two to move first.**")

P("R5", "§7 pointer — where store revision 65 writes",
"\n\n## 8. Status and next step\n\n",
"\n\n**Store revision 65 writes into that document too.** It enacts **§7 item 129 answer (4)** — F10's "
"designation-review advisory — which the Policy Director answered at [MOO-188](/MOO/issues/MOO-188) §3.3 "
"with one wording change, and item 129 is marked there with what that answer became. **Answers (1), (2), "
"(3), (5), (6) and (7) stay open**, four of them decide who bears a loss, and this revision answers none "
"of them. This document carries the narrative at §0.0-65, the sweep at §5.43 and the drafter's note at "
"§6.0-65.\n\n## 8. Status and next step\n\n")
