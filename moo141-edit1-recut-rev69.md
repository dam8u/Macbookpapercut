# MOO-141 — Edit 1's anchor re-cut, and one finding that changes Edit 1's own words

**Policy Director, 13 October 2026.** Written on the Drafting Specialist's report of 00:30 that Edit 1's
FIND string is dead at store revision 68. The report is right. **It was also already out of date when it
arrived: the base is at store revision 69.** Everything below is counted at revision 69, document
revision 88, and nothing is carried forward from any earlier base.

**Internal working draft material. Not a DLS bill. Not reviewed by counsel. Pre-decisional.**

---

## 1. Headline

**The anchor is repaired and the repair is counted, not asserted. All three anchors resolve exactly once
in enacted §1 at store revision 69.**

**Edit 1's own words change as well, and that is the substantive result of this heartbeat.** MOO-164's
candidate 164-7 is applied in its revision 6 and carries Edit 1's saving clause **verbatim, with one
express exception** naming M 2's 15-day duty on the application. Edit 1 has no such exception. **Two
sentences, otherwise identical, in one section, one with an exception and one without — that is *Forst*
pointed at the patch again, and it would undo the answer taken at revision 5 §0.3.** Edit 1 now carries
the same exception, drafted for its own location.

| | Before this re-cut | After |
|---|---|---|
| Edit 1 FIND | dead at revision 68 | **resolves once in §1** |
| Edit 1 Δ | +669 | **+818** |
| Edit 2, Edit 3 | unchanged | unchanged, +14 and +15 |
| **Patch** | **+698** | **+847** |
| Words deleted from the bill | none | **none** |
| Figures moved | none | **none** |

**No endpoint moves, no figure moves, no designator is renumbered, and the patch still deletes no word
of the bill.**

---

## 2. The break, and the repair

Store revision 68 re-cast subsection A's three-day sentence. Two changes, either of which alone would
have killed the anchor: the extension is **confined to mailing**, and the triplet *"statement, notice, or
certification"* replaces *"that statement or notice."*

> **Dead — 0 occurrences in enacted §1 and 0 whole-document at revision 69:**
> `…that runs from the giving of that statement or notice is extended by three days.</u>`
>
> **Resolves once in enacted §1:**
> `…that runs from the giving of that statement, notice, or certification is extended by three days.</u>`

The dead string is kept in `moo141-rev68-recut/verify_r69.py` as `E1_F_R65_DEAD` and **asserted at 0**, so
the break stays visible rather than being quietly fixed. The Drafting Specialist's `verify_r68_v6.py`
carries the same repair as a **test fixture** and said so; this is the re-cut, taken at the later base.

### 2.1 The substance of the confinement does not reach Edit 1, and here is why

Edit 1's deeming sentence is about the Board's **acting**. The confinement and the new express giving
rule — mailing or electronic transmission, *"except that an electronic transmission completed after
5:00 p.m. is given on the following day"* — are about the Board's **giving**. The two do not meet.
**The Drafting Specialist declined to make that reading and left it to me. It is made here.**

### 2.2 The arithmetic sentence was wrong and the figure is right

MOO-164's Edit 164-1 derives its 48-day cap as `15 + 3 + 30` and explains the 3 as an unconditional
mailing extension. **It is no longer unconditional. The 48 still binds, and it binds at the mailing
case:**

| Route the Board takes | Given | Tolling ends | |
|---|---|---|---|
| **mails on day 15** | day 15 | 15 + 30 + 3 | **48 — the cap** |
| transmits electronically, after 5:00 p.m. on day 15 | day 16 | 16 + 30, no extension | 46 |

**So the cap is still exactly right and the sentence that explains it is wrong.** Re-derived at revision
69, not taken from the earlier record.

---

## 3. The finding: two savings, one exception, and the asymmetry is in the patch

### 3.1 What the two sentences say

**Edit 1, as cut at revision 6:**

> Nothing in the preceding sentence determines the date by which the Board is required to act upon a
> request, to make a determination, or to give a notice or a decision, or whether the Board has performed
> such a duty within a period required by this section.

**MOO-164's candidate 164-7, applied in its revision 6 — the same sentence, with 20 words in front:**

> **Except for the purposes of the duty of the Board under this subsection to act upon an application no
> later than 15 days after it acts upon the request,** nothing in the preceding sentence determines the
> date by which the Board is required to act upon a request, …

### 3.2 Why the asymmetry bites

Both sentences reach the same duty and **both intend the same result** — the 15-day duty on the
application is keyed to the Board's first act, which is day 22 on the ordinary facts, accepted and
disclosed at revision 5 §0.3. They reach it by **opposite techniques**: Edit 1 by leaving the duty out of
the saving's list of three, 164-7 by excepting it expressly.

**The express exception is the problem, not the omission.** *Forst v. Rockingham Poultry Marketing
Coop.*, 222 Va. 270, 278 (1981) — two different terms in the same act, two different things. A reader who
finds the exception in M 2 and no exception in subsection A infers that in subsection A the duty **is**
saved: that where the Board actually acts, the deeming does not fix the 15-day duty at all. **That is the
revision-5 answer reversed, and reversed in the one case that occurs in the ordinary course.** Pass 17's
F-1 killed Edit 2 on this exact argument, inside the subdivision Edit 2 was drafted for. The argument is
no weaker one subsection away.

### 3.3 The repair, and why it is Edit 1 that moves

**164-7 needs its exception and cannot give it up.** On 164-7's facts the Board never acts, and without
the exception M 2's 15-day duty is a **duty that never falls due** — limb 3 of the three unbounded limbs
reported at 17:57. So the conforming move is Edit 1's, which is also the cheaper one: Edit 1 is unapplied
and is this issue's own.

> **Edit 1's saving, re-cut:** *"**Except for the purposes of the duty of the Board under subsection M to
> act upon an application no later than 15 days after it acts upon the request,** nothing in the
> preceding sentence determines the date by which the Board is required to act upon a request, to make a
> determination, or to give a notice or a decision, or whether the Board has performed such a duty within
> a period required by this section."*

**+149 characters. *"under this subsection"* becomes *"under subsection M"***, because Edit 1 sits in
subsection A and 164-7 sits in M 2. **The effect is the effect already decided.** This is a conforming
repair of a *Forst* exposure, not a choice between outcomes — so it needs no board answer and carries no
figure.

### 3.4 One ordering constraint the repair creates, and it is satisfied

The exception describes its duty by the words *"no later than 15 days after it acts upon the request."*
**That phrase resolves twice in §1 before the patch** — in M 2, and in the definition's date-notice
backstop, which is Edit 2's FIND. **Edit 2 consumes the second one**, re-keying it to *"gives its
decision."* So after the patch the descriptor has exactly **one** referent.

> **Edit 2 must be applied with Edit 1, not after it in a later cut.** Verified both ways in
> `verify_r69.py`: 2 referents before, 1 after, with Edit 1's own exception text excluded from the count.

### 3.5 One side-effect, stated rather than claimed

An express exception implies the duty excepted would otherwise have been caught by the saving, and so
implies that the duties **not** listed and **not** excepted — to restore, to credit, to recertify, to
settle — are within it. **That is the favourable direction for the open finding of 17:26** (the 60-day
restore-and-settle duty on a reversal on reconsideration, which the saving's closed list does not name).
**It is an argument and not a cure, I am not treating the finding as closed, and it stays a named target.**

---

## 4. What I verified, at store revision 69

| | Value |
|---|---|
| `bill-text-s8` document revision | **88** (`3b9ac270`) |
| Store revision | **69** |
| Whole document | **482,941** characters |
| Enacted §1 | **131,923** characters |
| §1 sha256 | **`bc0a4bf513d01a54…`** |
| Base the report of 00:30 was cut at | store revision 68 |

**§1 grew from 121,439 at revision 64 to 131,923.** § 51.1-162 **joined the act's amended sections** at
store revision 67, so §1 is three Code sections now and not two. Any comparison of §1 sizes across
revision 67 is a comparison of different things.

### 4.1 Anchors — §1-scoped, which is still the only valid uniqueness test

| Edit | §1 | whole document | Δ |
|---|---|---|---|
| 1 — the pendency re-key, re-cut | **1** | 1 | **+818** |
| 2 — the 15-day date-notice backstop | **1** | 1 | +14 |
| 3 — the D 4 / D 5 retention at 120 days | **1** | **2** | +15 |

**Edit 3 still resolves twice whole-document**, because a sweep quotes it. Third base at which that is
true. An applier who tests uniqueness over the whole document gets 2 and will either stop or patch the
record.

### 4.2 Counts and invariants

`acts upon` **8**, `act upon` **9**, `acting upon` **2**, `action upon` **2**, `last acts upon` **1**,
`first acts upon` **2** — and **3** after application, because Edit 1's own deeming sentence contains the
phrase. Both of G 4's express *"first"*s intact, which is the condition on which revision 2's withdrawn
G 4 edit stays withdrawn. G 4's anti-delay sentence intact. M 2's deemed-denial sentence intact.
`<u>` 62 / `</u>` 62 in §1, unchanged by the patch and balanced after it.

**Applied to a copy: §1 delta +847 and whole-document delta +847 — they agree, so no edit lands outside
§1.** `verify_r69.py`, all checks pass.

### 4.3 MOO-164 is not applied to the store, so Edit 1 still has work

Counted, because a saving clause that duplicates one already in the body would be a reason to withdraw
Edit 1 rather than re-cut it:

| | §1 at revision 69 |
|---|---|
| the saving sentence, in either form | **0** |
| 164-7's express exception | **0** |
| 164-1's notice-keyed tolling replacement | **0** |
| **164-1's act-keyed FIND, still the live text** | **1** |

**And 164-1's floor and cap limbs both read *"after the Board acts upon the request"*, so Edit 1's deeming
reaches both.** Edit 1 is not redundant on MOO-164's landing.

---

## 5. A free result for MOO-164, which they have not had yet

They verified eleven anchors at store revision 68 on three bases. **I ran their eleven FIND strings at
store revision 69, which they have not seen, and against revision 69 plus this re-cut patch.**

> **All eleven resolve exactly once at store revision 69. Not one is disturbed by this patch — 1 → 1 on
> every row.** Order-independence holds at a fourth base and survives the re-cut.

**What is now stale in their kit:** `verify_r68_v6.py`'s `E1_R` fixture is revision 6's Edit 1, without
the exception. **It is a fixture, so nothing of theirs is wrong — but their next cut should lift Edit 1
from here.**

---

## 6. What I did not do

- **No card to the board.** §3.3 is a conforming repair that preserves an answer already given, and it
  carries no figure. Carding it would ask the board to re-decide something it has decided.
- **The 120 days are not reopened**, and nothing here bears on the figure.
- **The finding of 17:26 is not cured** — §3.5 is an argument in its favour and it stays a named target.
- **Nothing is drafted for the three unbounded limbs.** Route (b) is **declined**, as a decision, and
  store revision 69's record §5 now says so against §7 item 130; route (c) is adopted at MOO-164.
- **Nothing is applied to the store and nothing here authorises applying it.**

---

## 7. Where this stands

| Gate | Issue | What clears it |
|---|---|---|
| **1** | **MOO-164** | The *"acts upon"* cut lands, carrying F-9 as Edit 164-5 and 164-7 with limb (B) |
| **2** | **MOO-197** | Store revision 66's four edits — F1's Rule 2A:2 cure and the rest |
| **3** | whoever applies | Re-verification at **the base as it stands at that moment**, §1-scoped, with Edit 2 applied in the same cut as Edit 1 (§3.4) |
| **4** | — | **Closed** |

**The base has now moved nine times under this item, and twice since the report that woke it.** Four of
those moves rewrote a provision the patch reaches without an anchor moving, and **this is the first that
killed an anchor outright.** Gate 3 is not a formality.

**The patch: three edits, +847 characters, no word deleted, no figure moved.**
