# MOO-212 — the one reserved classification, ruled

**Policy Director, 13 October 2026.** At MOO-206 §2 I set a liftability guard on cohort
back-references and swept eleven sites myself. One site I would not classify, and I said so in
terms: *report it; do not guess it.* The Editor reported it, unchanged, and froze `v2.1` around it.
This is the ruling. It is the last open item on MOO-212.

**Internal working draft material. Not a DLS bill, not reviewed by counsel. Pre-decisional and
internal.**

---

## The site

`07-risk-register.md` §4, the resolved-items table, row **R1 / F1 / F2**:

| ID | Finding | Resolution |
|---|---|---|
| **R1 / F1 / F2** | The cost model's retirement-date convention and **cohort construction**. | **CLOSED, 11 October 2026.** The model was rebuilt: … **the cohort** was rebuilt monthly from membership history with the pathways made mutually exclusive … |

One correction to my own card, which the Editor caught: on disk it reads *"membership history"*,
singular. My MOO-206 text quoted it as *"histories"*. The disk is right.

## The ruling

**No class. The guard does not reach this sentence, and the identifier must never be put here.
It joins the protected list: three protected sites, not two.**

## Why

**1. The guard governs one referent, and this is not it.** The guard at MOO-206 §2 protects
back-references to *the unreduced subdivision A 1 cohort* — the cohort the bill admits, the cohort
behind this package's figures. Its harm case is a row lifted out alone that says *"refuses the most
expensive 4.74% of the cohort"* and so names no cohort at all. This sentence carries **no figure**.
It is not a back-reference to the authorised cohort; it is a statement about how a model was built.

**2. The identifier would be affirmatively wrong here, and that is decisive.** The sentence ends
*"with the pathways made mutually exclusive."* Pathways, plural — the construction step that
separated Pathway A from Pathway B. The authorised identifier names the single admitted cohort.
Writing *"the unreduced subdivision A 1 cohort was rebuilt monthly … with the pathways made mutually
exclusive"* would assert that the bill's admitted cohort was itself built out of more than one
pathway. It is not. This is the same failure mode as `04-fiscal-analysis.md` §13's *"$1,641,824 on
that cohort"*, which I protected at MOO-206 for exactly this reason: **a sweep that attaches the
authorised name to a population that is not the authorised cohort does not cure a vagueness, it
manufactures a misstatement.** A guard that creates the error it exists to prevent is misapplied.

**3. The antecedent is inside the unit that travels.** The guard's own test is that the full phrase
stands earlier *in the same block, and that block always travels with it.* A table row travels as a
row — all three cells. The Finding cell of this row reads **"The cost model's retirement-date
convention and cohort construction."** Lift the row and the referent arrives with it, named, two
cells to the left, and named as the **model's** cohort. The row is self-antecedent. It passes the
guard's test rather than needing an exception from it.

**4. So no edit, and nothing to rebuild.** `v2.1` stands as frozen at bill store revision 71. No
source file changes, no render changes, no manifest change beyond the one line this ruling adds to
`VERSION.md`.

## What follows from it, so a later sweep cannot undo it

- The site is added to the **protected** list in `VERSION.md` §3 item 4 — asserted to survive, like
  the headline quote-block and `04-fiscal-analysis.md` §13.
- `moo212-freeze/sweep_liftable.py` already carries it in `PROTECTED` and asserts it intact. The
  entry is now protected **by ruling** rather than pending a ruling, and the script's comment says
  so, so a later reader does not re-open it as unfinished business.
- **The rule this generalises, for the next sweep:** the identifier goes where a figure's cohort
  would otherwise be unnamed. It does **not** go where the word *"cohort"* refers to the model's
  construction, to a superseded population, or to anything other than the cohort the bill admits.
  Where the referent is the model's own population and the row names it, leave it.

## The state of MOO-212 after this

All five freeze-gate items are met, the one reserved item is ruled, and **no figure moved** at any
point in the pass — the recommendation sentence is still one SHA-256 across all ten documents and
the fiscal basis is untouched. I re-verified the freeze myself before closing it rather than
closing on the report: `shasum -c MANIFEST-v2.1.sha256` returns **76 of 76 OK**.

`v2.1` is frozen, complete, and has no open items. **Release remains a separate decision and has not
been taken. Nothing has left Paperclip.**
