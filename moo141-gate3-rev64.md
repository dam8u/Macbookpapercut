# MOO-141 — gate 3 re-verification at store revision 64

**Policy Director, 12 October 2026, 18:01 UTC.** Internal working draft material. Not a DLS bill. Not reviewed or cleared by counsel. Pre-decisional.

This is a **standing-evidence pass**, not a new decision. MOO-141 is blocked on [MOO-164](/MOO/issues/MOO-164) and [MOO-190](/MOO/issues/MOO-190) and nothing here unblocks either. It exists because the base under this patch has now moved **eight** times, and because the one thing an applier must be able to trust — that the three FIND strings still resolve — is only worth anything on the day it is checked.

## 1. The base

| | |
|---|---|
| Document | `bill-text-s8` on [MOO-42](/MOO/issues/MOO-42) |
| Live revision | `d552f1ed-79ac-4e15-a0d4-f4550f22596a`, updated 17:53:53 UTC |
| Store revision | **64** |
| Whole document | **324,617** characters (320,665 at revision 63 — **+3,952**) |
| Enacted §1, store convention | **121,439** characters — **unchanged from revision 63** |
| §1 sha256 | `fd45c611fa4e5cadd5e2239fc7d9bb133289259296314c72eb281c58054bc43c` |

**Store revision 64 is record-only, and its own heading says so**: *"No bill text changed; one defect in store revision 63's two sentences recorded as §7 item 131."* The whole +3,952 characters is record. §1 did not move, so for the first time in eight bases this patch needs nothing re-spliced.

**The §1 hash is recorded so the next pass can prove byte-identity rather than infer it from a character count.** Revision 63 was never hashed; from here it is.

## 2. The three anchors

Read from the store, not from any document's own reproductions.

| Edit | Whole document | **§1** | Delta on application |
|---|---|---|---|
| 1 — the pendency / tolling re-key | 1 | **1** | +669 |
| 2 — card (g), the 15-day date-notice backstop | 1 | **1** | +14 |
| 3 — card (k-ii), the D 4 / D 5 retention at 120 days | **2** | **1** | +15 |
| **Patch** | | | **+698** |

Applied to a copy: **§1 delta +698, whole-document delta +698** — the two agree, so no edit lands outside §1. `<u>` balance **60 / 60** in §1 before and after, **61 / 61** whole-document.

**The §1-scoped uniqueness rule from the revision-63 triage stands, and is now evidenced at a second base.** Edit 3's FIND resolves twice in the document — operatively at offset **189,816** in §1, and at offset **229,336** inside §5's cross-reference check, where a sweep quoted it.

> **Resolve all three anchors within §1 and require a §1 count of exactly 1. A whole-document count is not a valid uniqueness test for Edit 3.**

## 3. Counts and invariants in §1 (before → after application)

| Term | Before | After |
|---|---|---|
| `acts upon` | 8 | 8 |
| `act upon` | 9 | 12 |
| `acting upon` | 2 | 2 |
| `action upon` | 2 | 2 |
| `first acts upon` | 2 | **3** |
| `last acts upon` | 1 | 1 |
| `pending` | 9 | 9 |
| `the 90 days allowed by this subsection` | 2 | 2 |
| `no later than 15 days after it acts upon the request` | 2 | **1** |
| `120 days after the Board acts upon the request` | 0 | **1** |

`first acts upon` **must** read 3 after application, because Edit 1's own definition contains the phrase. Both of G 4's express *"first"*s are intact — the condition on which revision 2's withdrawn G 4 edit stays withdrawn.

**Store revision 63's two deemed-denial sentences are intact in M 2** — all three operative strings present exactly once in §1. **Store revision 62's G 4 anti-delay sentence is intact**, which is what finding 1 of the revision-63 triage turns on.

## 4. Two items, neither of them a decision taken here

### 4.1 Item 131 is the live question about the member's route into court, and it is correctly placed

Store revision 64 records the Drafting Specialist's own finding against their own enacted sentences: M 2's Article 5 grant runs to a person aggrieved by *"such case decision"*, whose nearest antecedent is the **completion** sentence, and the enacted characterisation is bounded *"for the purposes of this subsection"* while § 2.2-4026 sits outside the subsection. Each reading survives alone; the pair closes the route.

**Two one-phrase repairs are drafted and neither is enacted, which is right**: the limiting phrase is inside the words the board approved verbatim on 12 October at 17:38, so removing it is the board's call and not a drafter's. §0.0-63's repair 1 is qualified in place rather than withdrawn.

**This is why gate 2 points at MOO-190 and not at MOO-42.** Gate 2 was about whether a member facing a Board that never acts has a route into court. The cure is enacted; item 131 is the one open question about whether it works. **If MOO-190 confirms the defect, it reaches the board as a card from me with the two drafted repairs and no new figure. Nothing is carded today, because carding a defect before its review has reported spends the board's answer on a provisional reading.**

### 4.2 A numbering collision in the shared workspace, flagged not fixed

The workspace carries `moo191-rev64/` — [MOO-191](/MOO/issues/MOO-191)'s cut of the F10 designation-review advisory into subdivision D 1, labelled **"the one bill edit of store revision 64."** **Store revision 64 is taken, by the record-only revision above, and the advisory is not in the live body** (count 0 in §1 and 0 whole-document). That cut therefore lands as **store revision 65** and the number in its own record text needs changing.

**It is not a defect in the cut.** `moo191-rev64/edits.py` asserts all three MOO-141 FIND strings as untouched anchors before substituting, which is the right discipline and is why this patch is not exposed to it. **Recorded for whoever applies MOO-191; not mine to renumber.**

## 5. Where MOO-141 stands

| Gate | Issue | What clears it |
|---|---|---|
| **1** | **MOO-164** | The *"acts upon"* decision, carrying F-9 and the three unbounded limbs from the revision-63 triage |
| **2** | **MOO-190** | The bounded pass on revision 63's two sentences — **item 131 first** |
| **3** | whoever applies | Re-verification at the moment of application, §1-scoped. **Evidenced at store revision 64 by this document** |
| **4** | — | Closed — revision 6 accepted at MOO-176, cap limb closed at MOO-179 |

**The patch is unchanged: three edits, +698 characters. Nothing is applied to the store and nothing here authorises applying it.**
