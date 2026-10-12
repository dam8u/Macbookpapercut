# -*- coding: utf-8 -*-
"""Record-layer patches for store revision 62. Same FIND/READ discipline as edits.py."""

PATCHES = []
def P(i, label, find, repl, n=1):
    PATCHES.append(dict(id=i, label=label, find=find, repl=repl, n=n))

P("R1", "byline — store revision 62",
"**MOO-42 · Drafting Specialist · store revision 61 · 12 October 2026 · INTERNAL WORKING DRAFT — pre-decisional**",
"**MOO-42 · Drafting Specialist · store revision 62 · 12 October 2026 · INTERNAL WORKING DRAFT — pre-decisional**")

P("R2", "§5 preamble — name the live sweeps truthfully",
"The file now has roughly 275,000 characters of headroom against the store's 524,288-character ceiling, so **nothing was moved out in store revision 59**, and §5 holds the sweeps for store revisions 59 and 58. The retention rule the Director set in answering §7 item 53 still stands; it is simply no longer forced.",
"The file now has roughly 250,000 characters of headroom against the store's 524,288-character ceiling, so **nothing has been moved out since store revision 58**, and §5 holds the sweeps for store revisions **62, 61, 60 and 59** — §§5.41, 5.40, 5.39 and 5.38. **This paragraph named the wrong two through store revisions 60 and 61 and is corrected here.** The retention rule the Director set in answering §7 item 53 still stands; it is simply no longer forced, and the next revision that is short of room should move §5.38 and §5.39 out first.")

P("R3", "§6 preamble — name the live notes truthfully",
"**The 3 sections below are the drafter's notes for store revisions 54 back to 52, and all but §6.0-54 should move out with the next revision**, so that this section holds the current one only — the retention the Director's answer to §7 item 53 set.",
"**The 4 sections below are the drafter's notes for store revisions 62, 61, 60 and 59.** This paragraph named store revisions 54 back to 52 through store revisions 59, 60 and 61, none of which corrected it; **it is corrected here, and the rule that a stale self-description is a defect of the record is the reason**. The retention the Director's answer to §7 item 53 set — this section holds the current note only — still stands and is no longer forced by the ceiling; the next revision that is short of room should move §6.0-59 and §6.0-60 out first.")

P("R4", "§8.1 — six notes, and what moves first",
"**§8 retains the current note and the four before it**, which is the retention the Director's answer to §7 item 53 set and which §8 had let slip to ten.",
"**§8 retains the current note and the four before it**, which is the retention the Director's answer to §7 item 53 set and which §8 had let slip to ten. **Store revision 62 makes it six** — notes for store revisions 62, 61, 60, 59, 58 and 57 — because the ceiling no longer forces a move and moving another run's record in the heartbeat it was written is how a record gets double-stubbed. **The note for store revision 57 is the one to move first.**")

P("R5", "§7 pointer — where store revision 62 writes",
"This document carries the narrative at §0.0-61, the sweep at §5.40 and the drafter's note at §6.0-61.",
"This document carries the narrative at §0.0-61, the sweep at §5.40 and the drafter's note at §6.0-61.\n\n**Store revision 62 writes into that document too.** [MOO-169](/MOO/issues/MOO-169)'s counsel pass on store revision 61's thirteen substitutions returned **1 fatal, 9 serious, 9 moderate and 4 minor findings, and 12 null results**. **Fourteen of its findings are enacted in §1 by this revision** — F1, F2, F3, F4, F5 in part, F6, F8, F9, F10, M1, M2, M3, M4, M5, M6, m1 and m3 — **six are drafted or left undrafted with reasons** at §6.0-62, and the same revision enacts **all seven of the answers the Policy Director selected at §7 item 128 on 12 October 2026**. Item 128 is marked there with what each answer became, and **§7 item 129** carries the seven questions this revision could not answer by drafting choice. This document carries the narrative at §0.0-62, the sweep at §5.41 and the drafter's note at §6.0-62.")
