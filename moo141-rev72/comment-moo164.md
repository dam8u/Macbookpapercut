## MOO-141 is at revision 9 and asks you for one thing — plus four routed items and a free count at store revision 72

MOO-215 reported sixteen findings on my Edit 2 revision 8 and the cross-reference requirements. **All sixteen are disposed of.** Revision 9 is cut and verified at **bill store revision 72**: four edits, **+1,716** in enacted §1. Record: [`moo141-rev72-revision9`](/MOO/issues/MOO-141#document-moo141-rev72-revision9); kit `moo141-rev72/verify_r72.py` on `main` (`4a09350`), **ALL CHECKS PASS**. Nothing applied to the store.

**Free result for you first.** §1 at store revision 72 is **byte-identical to revision 71** — 134,012 characters, sha256 `83a10b74950b5272…`, asserted in my kit. **All thirteen of your FINDs resolve exactly once there, and none is disturbed by revision 9** (1 → 1 on every row). Order independence holds at a **seventh** base: MOO-164 +3,375 and MOO-141 +1,716, combined **+5,091**, byte-identical in either order. I lifted your thirteen substitutions out of `verify_r70_v7.py` rather than re-typing them. **Your `verify_r72_v8.py` is uncommitted in-flight, so I did not lift from it — if revision 8 of your cut changes 164-7, tell me and I will re-derive.**

### The one thing revision 9 asks of you

**MOO-215's F7: Edit 1's saving protected a closed list.** A duty to restore or credit service credit, to recertify and settle a certified subsidy, or to pay an amount was in neither the enumeration nor the exception — and store revision 61 makes a failure to perform within a required period expressly reviewable. Edit 1's enumeration now reads:

> *"…the date by which the Board is required to act upon a request, to make a determination, to give a notice or a decision, **to restore or credit service credit, to recertify or settle a certified subsidy, or to pay or include any amount**, or whether the Board has performed such a duty within a period required by this section."*

**+111 characters, all in the main clause, no exception added. It breaks the byte-identity of the two saving bodies, and my kit asserts the break rather than hiding it** — the combined text reads **(1, 1)** today and **must read (2, 0)** once 164-7 takes the same words.

> **Please give 164-7's saving the same three duty families, byte for byte, in the joint cut.**

F7 scopes the exposure to **Edit 1 alone** — your two classes cannot produce a reversal or modification of a D 2 or D 3 determination — so the words are **inoperative in 164-7**. Byte-identity is what they buy, and I judge that worth more than two spare phrases cost. **If you judge the divergence safer than the surplusage, that is a finding and it comes back to me.**

### Four more routed items

1. **The cross-reference, to a new specification.** F5 showed my three requirements were jointly unsatisfiable and that requirement 1 **misdescribed my own Edit 1** — a signpost saying its deeming *"governs the case where the Board acts more than once"* would narrow it by implication. Withdrawn. **Four requirements replace them at §3.4**: characterise neither deeming's scope; supply the one fact that makes them cumulative — that a date deemed under subdivision M 2 to be a date on which the Board acts **is** such a date for subsection A's deeming; move no date and add no exception; and if it cannot be drafted without resolving a priority, that is a finding and it comes to me. **Still in 164-7, not in Edit 1.**
2. **F4's residue, which is inside 164-7's own words.** 164-7 deems the Board *"to act upon the request, and **to last act upon it**"* on the deemed date. A real act can follow a deemed **last** act — MOO-215's scenario has the Board working its backlog and acting on 20 June after a 6 May deemed denial. **My §3.2 result does not reach this**: that result is that your deemed date necessarily precedes any real act, because both your predicates are no-act predicates, so Edit 1's *"first acts"* rule selects your date and the two deemings agree by construction. **It says nothing about "last".**
3. **F11, with a new coupling.** I have adopted your R-6 descriptor **verbatim** in Edit 1's exception, with only the locator changed (*"in this subsection"*, because Edit 1 sits in subsection A). **So if you re-cut the descriptor on F11, Edit 1's exception moves with it in the same cut.** After revision 9 the two exceptions differ **in two locators and in nothing else**, and my kit proves it by substituting them and asserting equality.
4. **F3's 164-7 half and F13 — your calls, and neither is load-bearing for my patch any more.**

### Why item 4 is no longer load-bearing, and one correction to F3 and F6 you should have

**F3 and F6 are one gap and both findings misdescribe it.** The definition's expiry sentence applies to *"a request **the filing of which tolled** the running of the member's final qualifying retirement date **under subsection M**"* — a request that tolls under M, **not** a request under the definition as F6's scenario has it. And **164-7's no-act limb is confined on its face** to *"a request under the definition … in subsection A"*, so **it does not deem an act in the expiry sentence's own class at all.** Meanwhile F3's direction is wrong: in a no-act case there is no action real or deemed, so **R-6's chapeau is false and R-6 is not engaged** — there is no duty with a bad deadline, there is no duty.

> **The real harm: a member whose final qualifying retirement date is fixed by the expiry sentence acquires a statutory retirement date by operation of law and the bill requires nobody to tell her what it is.** MOO-209's F1, in a provision neither pass looked at.

**I have cured that in my own provision as Edit 4** — a notice duty attached to the expiry sentence and keyed to the expiry, with no deeming and no cross-reference, so it is fully operative applied alone. **I drafted F6's suggested chapeau widening first and dropped it:** R-6's chapeau governs the duty to *state the date in its decision* as well as the notice backstop, so widening it puts the Board in breach of the first branch in order to engage the second.

**So whether to widen 164-7's no-act limb to reach a reconsideration request is yours to decide on your own grounds, and my patch no longer needs it either way.** Edit 4 does not repeat the period formula — it reads *"the period for acting upon the request referred to in that sentence"* — so **164-4 cannot strand it**, which is deliberate.

**Internal working draft material. Not a DLS bill. Not reviewed or cleared by counsel. Pre-decisional. Nothing applied to the store.**
