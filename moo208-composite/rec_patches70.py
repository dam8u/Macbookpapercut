# -*- coding: utf-8 -*-
"""MOO-208 store revision 70 — in-place record corrections.

Eight. Two bring the §5 and §6 self-describing paragraphs current (a stale self-description is a
defect of the record, and both were already wrong before this revision). Six mark, in place, the
store revision 65 drafter's-note items that the Director's composite supersedes or reverses. None
of them touches an enacted word, and none rewrites the original away: the old reasoning stays
readable and the correction sits next to it.
"""

P1_F = (
    "The file has about **41,000** characters of headroom against the store's 524,288-character "
    "ceiling, so **nothing has been moved out since store revision 58**, and §5 holds the sweep "
    "written by store revision 69 (**§5.@46@**, the Policy Director's three drafted answers out of "
    "[MOO-189](/MOO/issues/MOO-189)) together with the sweeps for store revisions **67, 66, 65, "
    "63, 62, 61, 60 and 59** — §§5.45, 5.44, 5.43, 5.42, 5.41, 5.40, 5.39 and 5.38."
)
P1_R = (
    "The file has about **9,000** characters of headroom against the store's 524,288-character "
    "ceiling, **and store revision 70 is the revision this paragraph has been waiting for since "
    "store revision 58: with its record layer the document landed at 527,893 characters, so it "
    "could not write at all until §5.38 and §5.39 were moved out.** Both are now moved **verbatim** "
    "to the retained-record document, each leaving a stub in the form §5.37 established, and a "
    "reference of the form **§5.38** or **§5.39** resolves there. §5 therefore holds the sweep "
    "written by store revision 70 (**§5.47**, the Policy Director's composite out of "
    "[MOO-191](/MOO/issues/MOO-191), and the first sweep in this file to report a change to the "
    "bill's title line) together with the sweeps for store revisions **69, 67, 66, 65, 63, 62 and "
    "61** — §§5.46, 5.45, 5.44, 5.43, 5.42, 5.41 and 5.40. **Store revision 70 also corrects store "
    "revision 69's cross-reference to its own sweep, which it wrote as *\"§5.@46@\"* — the same "
    "corruption store revision 67 made at *\"§5.@45@\"*, and twice is a pattern rather than a "
    "slip.**"
)

P2_F = (
    "**Store revision 69 adds **§6.0-69**, so the sections below are the drafter's notes for that "
    "revision and for store revisions 67, 66, 65, 63, 62, 61, 60 and 59 — and the list in this "
    "paragraph had omitted §6.0-66, which store revision 66 wrote** — store revision 64 changed "
    "no word of either section and wrote no note of its own, so **the gap at §6.0-64 is that "
    "revision's silence and not a lost note.**"
)
P2_R = (
    "**Store revision 70 adds **§6.0-70**, so the sections below are the drafter's notes for that "
    "revision and for store revisions 69, 67, 66, 65, 63, 62, 61, 60 and 59 — store revision 69 "
    "corrected the omission of §6.0-66 from this list** — store revisions 64 and 68 changed no "
    "word of any section in the act and wrote no note of their own, so **the gaps at §6.0-64 and "
    "§6.0-68 are those revisions' silence and not lost notes.** **The ceiling is live.** Store "
    "revision 70 could not write until §5.38 and §5.39 were moved out to the retained-record "
    "document, and it moved the §5 half of the rotation only. **§6.0-59 and §6.0-60 are the next "
    "to go, and the next revision that is short of room should move them before it writes.**"
)

P3_F = ("This is the Policy Director's wording change at MOO-188 §3.3 and the reason is recorded "
        "there.")
P3_R = P3_F + (
    " **Superseded as to the words, store revision 70 — the item no longer reads *\"is advised to "
    "review.\"*** The Policy Director has taken [MOO-195](/MOO/issues/MOO-195) F9 at "
    "[MOO-208](/MOO/issues/MOO-208) and the item now reads *\"that the Board advises the member "
    "to review.\"* **Everything this item says about the operative verb survives the change; its "
    "conclusion does not.** Naming the Board inside the item is the better drafting answer, "
    "because the item read alone was self-verifying — true because the Board states it — and was "
    "the only one of seven that was. *\"Advises\"* is the Board's own verb, it imposes nothing on "
    "the member, and every no-duty property this item defends is intact. §6.0-70 item 1."
)

P4_F = ("Merging them would have buried advice inside a proposition of law and made it arguable "
        "that the advice is part of what B provides. Separate, the propositions stay together and "
        "the advice is visibly advice.")
P4_R = P4_F + (
    " **Reversed as to position, and not as to either reason, store revision 70.** The Policy "
    "Director has taken [MOO-195](/MOO/issues/MOO-195) F4 at [MOO-208](/MOO/issues/MOO-208) and "
    "the advisory is now item **7 of 7** and no longer item 5. **Both reasons this item gives "
    "survive the move and are served better by it**: at the end of the series the advice is still "
    "its own semicolon item, still introduced by *\"that\"*, still the only item in a different "
    "register, and it is no longer interleaved among the six propositions of law it must not be "
    "read as part of. What the move adds is that it stops splitting item 4's forward reference to "
    "*\"subsection C of that section\"* from the item that restates that citation in full. "
    "§6.0-70 item 4."
)

P5_F = ("The advisory is a **new item** and the item that follows it restarts with the full "
        "citation (*\"that subsection C of § 51.1-162\"*), so the short form would have made the "
        "referent depend on an item two places back. §5.43 direction 1.")
P5_R = P5_F + (
    " **The reason changes with the position; the result does not, store revision 70.** The "
    "advisory is now the last item and the item before it names *\"subsection B of § 51.1-162\"*, "
    "so the short form would now have resolved. The full citation is kept anyway, for a reason "
    "this item did not need: the item now carries three propositions and shifts to *\"that "
    "section\"* twice inside itself, so it must supply its own referent and not borrow a "
    "neighbour's. §6.0-70 item 3."
)

P6_F = "*\"Before completing payment\"* closes the **first** of those legs."
P6_R = P6_F + (
    " **Store revision 69 — the deadline stands, and the false implicature it carried is cured by "
    "words that now follow it.** The Policy Director has taken "
    "[MOO-195](/MOO/issues/MOO-195) F2 in form D2b at [MOO-208](/MOO/issues/MOO-208): *\"before "
    "completing payment\"* is kept as the prompt to act now, and the item then states that the "
    "member may make or change the designation under subsection A of § 51.1-162 *\"at any time "
    "before the member's death.\"* Read together they say do it now, and know you can change it "
    "later. **The enacted deadline was never the defect; the inference a reader could draw from "
    "it standing alone was.** §6.0-70 item 2."
)

P7_F = ("**That recommendation is not enacted here**: it reverses a point the Director decided at "
        "MOO-188 §3.4, and it is before the Director at [MOO-191](/MOO/issues/MOO-191) with the "
        "words drafted. [MOO-195](/MOO/issues/MOO-195) F3 and F10.")
P7_R = (
    "**That recommendation is enacted at store revision 70, in form D3c conformed to F9's "
    "wording.** The Policy Director has taken [MOO-195](/MOO/issues/MOO-195) F3 at "
    "[MOO-208](/MOO/issues/MOO-208) and has expressly reversed the acceptance at MOO-188 §3.4, on "
    "counsel's remedy analysis — § 2.2-4029 bars a court from supplying the agency action — and on "
    "two further reasons of the Director's own. **So this item's heading is no longer the law of "
    "the draft**: omission of the advice is now excepted from D 1's deeming of a failure to state "
    "for the purposes of subsection M, and is kept in the subsection J report. **What the exception "
    "does not do, recorded and not drafted around: subdivision M 2 reaches the omission on its own "
    "terms, so the channel stays open and no cure inside D 1 can close it.** §6.0-70 item 5 and "
    "**§7 item 135**, drafted and not enacted. [MOO-195](/MOO/issues/MOO-195) F3 and F10."
)

P8_F = ("It is the kind of thing that belongs on MOO-97's card if anyone wants it, not in a cut "
        "commissioned as one edit.")
P8_R = P8_F + (
    " **Confirmed, store revision 70.** The Policy Director has **held** "
    "[MOO-195](/MOO/issues/MOO-195) F5 at [MOO-208](/MOO/issues/MOO-208) and has directed that "
    "**the acknowledgment form is not to be drafted**, because it moves the advisory toward a "
    "member obligation and the advisory's whole value is that it demands nothing of her. The "
    "route question goes to the subsection J report instead: if the pilot's own reports show the "
    "advice being buried, that is the evidence on which to require a route, and it will be "
    "evidence rather than a guess. §6.0-70 item 7."
)

PATCHES = [
    dict(id="R1", n=1, label="§5 intro brought current — §5.47 added, the '§5.@46@' corruption "
                             "corrected, the ceiling flagged", find=P1_F, repl=P1_R),
    dict(id="R2", n=1, label="§6 intro brought current — §6.0-70 added, §6.0-66 restored",
         find=P2_F, repl=P2_R),
    dict(id="R3", n=1, label="§6.0-65 item 1 — superseded as to the words by F9", find=P3_F,
         repl=P3_R),
    dict(id="R4", n=1, label="§6.0-65 item 2 — placement reversed by F4, both reasons preserved",
         find=P4_F, repl=P4_R),
    dict(id="R5", n=1, label="§6.0-65 item 3 — the citation reason restated for the new position",
         find=P5_F, repl=P5_R),
    dict(id="R6", n=1, label="§6.0-65 item 5 — the terminus kept and the implicature cured",
         find=P6_F, repl=P6_R),
    dict(id="R7", n=1, label="§6.0-65 item 6 — F3 now enacted; the M 2 residue named",
         find=P7_F, repl=P7_R),
    dict(id="R8", n=1, label="§6.0-65 item 7 — F5 held, the acknowledgment form not to be drafted",
         find=P8_F, repl=P8_R),
]
