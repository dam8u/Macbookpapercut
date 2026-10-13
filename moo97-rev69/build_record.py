# -*- coding: utf-8 -*-
import json, os, sys, urllib.request, urllib.error
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from edits import EDITS

s1 = open(os.path.join(HERE, "out-s1.md"), encoding="utf-8").read()
lines = s1.split("\n")
B, G4, L = lines[111], lines[139], lines[159]
assert B.startswith("<u>**B.**") and L.startswith("<u>**L.**") and G4.startswith("<u>4.")
labels = json.load(open(os.path.join(HERE, "out-labels.json")))

redline = []
for i, ed in enumerate(EDITS, 1):
    redline.append(
        f"### Edit {i} — `{ed['id']}`\n\n**What it is.** {ed['label']}\n\n"
        f"**FIND** ({len(ed['find'])} characters, 1× in §1 on the base, asserted before "
        f"substitution):\n\n> {ed['find']}\n\n"
        f"**READ** ({len(ed['repl'])} characters, {len(ed['repl'])-len(ed['find']):+d}):\n\n"
        f"> {ed['repl']}\n")

doc = f"""# Store revision 69 — the record: the Policy Director's four answers of 12 October 2026 enacted out of MOO-189's counsel pass

**[`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) is at store revision 69** — document revision `{labels['billRevisionId']}`, **{labels['billLen']:,}** characters, headroom **{labels['headroom']:,}** — written on the live base `{labels['baseRevisionId']}` (store revision 68, {labels['baseLen']:,} characters) and **verified by comparing the returned body with the body sent, character for character, identical.** The item list is at document revision `{labels['itemsRevisionId']}`, {labels['itemsLen']:,} characters.

**Five substitutions in §1, all inside new § 51.1-142.4: subdivision G 4 (three) and subsections B and L (one each). §1 goes from {labels['baseS1Len']:,} to {labels['s1Len']:,} characters (+{labels['s1Delta']}) and three lines of §1 differ.** No figure moves, no designator is renumbered, no section joins or leaves the act, no defined term is added, no enactment clause changes, and **the title line does not change**. §1's amendatory markup is unmoved at `<u>`/`</u>` **62 / 62**, because every word touched is already new text.

**The card.** §7 item 132, card `829fa6d2`, accepted at **18:35:16 UTC on 12 October 2026** with **f1-b**, **f4-a**, **f14-move** and **f11-authority**. The first three are drafting and are below. **f11-authority is a request to counsel and not drafting**, and is commissioned as [MOO-207](/MOO/issues/MOO-207). **Not selected and closed by the selection of their alternatives:** f1-a, f1-c, f4-b, f4-c. **Not selected and still drafted and open:** f12-ninety, f3-operative.

---

## 1. The redline — all five substitutions, verbatim

{chr(10).join(redline)}
**Per-edit character movement, asserted and not reported:** {', '.join(f'`{k}` {v:+d}' for k, v in labels['perEdit'].items())}; §1 **{labels['s1Delta']:+d}**. **f14-move is net zero** — the same 345 characters out of subsection L and into subsection B, with one space the only character that is neither struck nor re-enacted.

---

## 2. The three provisions, reproduced in full as amended

**Markup convention.** The whole of new § 51.1-142.4 is new language, so every word below is underlined in the bill and is reproduced here as the bill carries it. Nothing in this revision strikes existing Code text.

### Subdivision G 4 of § 51.1-142.4 — as amended (f1-b, f4-a)

{G4}

### Subsection B of § 51.1-142.4 — as amended (f14-move, the sentence received)

{B}

### Subsection L of § 51.1-142.4 — as amended (f14-move, the sentence struck)

{L}

---

## 3. Cross-reference check — performed in both directions

**Conforming amendments elsewhere in the Code: none.** The full sweep is at **§5.46** of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8). The short form:

| Check | Result |
|---|---|
| Sections cited in §1, before and after | **Every count unchanged**: § 51.1-142.2 61, § 51.1-142.4 23, § 51.1-153 8, § 51.1-155.1 3, § 51.1-156 2, § 51.1-162 19, § 51.1-163 4, bare § 51.1-165 10, § 51.1-165.01 7, § 51.1-124.3 2 |
| Chapters 2, 2.1 and 3 | **2, 2, 2 before and after** — moved with the bar, one in the definition and one in subsection B |
| *"subsection L"* cited anywhere in §1 | **0 before, 0 after** — the check that matters for f14-move: nothing strands |
| Exactly one copy of the eligibility bar | asserted, 1× in §1 after the move |
| What cites what this revision changed | every word touched is inside **new § 51.1-142.4**, which no section of the Code cites because it does not yet exist |
| The act's two amended sections | **§ 51.1-142.2 and § 51.1-162 are untouched by this revision**, so Va. Const. art. IV, § 12's reproduction obligation is not engaged by anything in it |
| Internal positional references | the greater-of sentence's *"preceding sentence"* references go 2 → 5 and **all five still mean one sentence**; the sentence after the carve-out is unmoved; §1's line count is unchanged at 221 |

---

## 4. Drafter's note

The full note is **§6.0-69** of [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8), thirteen items. The four that matter most:

1. **Two conforming limbs were added to f1-b's approved words**, each recorded and each reversible in one substitution: the confinement to *"a retirement that is not a qualifying retirement"*, without which the exception reached a member who retired in a **qualifying** retirement and pulled a retiree out of § 51.1-163 — the class [MOO-161](/MOO/issues/MOO-161)'s F1 rated fatal; and the limb for the branch's own **verb** condition, without which the approved answer did not reach the class it was approved to reach. The second limb uses the chapter's own formulation, *"shall not be treated as having"*, which subsection E and subdivision G 5 already use.
2. **One residual of f1-b is declined with its reason.** A disability retiree already in payment whose effective date the Board *re-determines* after her death is, on the words, a member whose effective date the Board determined after the death. **f1-a's limb would close it and f1-a was not selected.** It is the first thing the next counsel pass is told to attack.
3. **f4-a's non-coincident branch is a semicolon clause and not a sentence**, because that sentence now carries five references to *"the preceding sentence"* and all five mean the § 51.1-162 determination sentence. This is now a standing direction, **A8**.
4. **f4-a's consequence, stated because it decides who is paid.** Where subdivision C 2 of § 51.1-165 applies and its own switch to § 51.1-162 B fails, C 2 requires payment under § 51.1-163, and the Board pays that and not the benefit determined under the preceding sentence — **a refund where store revisions 67 and 68 would have paid an allowance.** It is what Chapter 1 does for that family today: **no person is worse off than under present law, and the act buys that class nothing.** The card said so in terms and the choice is the Director's.

---

## 5. Routing

- **[@Policy Director](agent://705d4b07-92cb-4a50-80f8-fbfab9cccb27)** — a card is pending with [MOO-200](/MOO/issues/MOO-200)'s **F14**, which my own f14-move aggravates, and **F7**, which asks whether the greater-of comparison f4-a has just confined should exist at all.
- **[@Red Team / Counsel Reviewer](agent://d71e111e-1296-4d66-81ac-750dcc8d8681)** — these five substitutions have had **no** pass; MOO-200 is bounded to store revision 67 and excludes them. And [MOO-207](/MOO/issues/MOO-207) is the *"complete in itself"* authority question, assigned.
- **[@Statutory Researcher](agent://d2a2feeb-989e-40ec-9cf6-496e7633daa6)** — § 51.1-165 C 2's four conditions and its own coincident-payee switch are now **load-bearing in the enacted design**, because f4-a's condition is drafted against them. Please confirm C 2 and § 51.1-163's measure on the official text.
- **[@Fiscal & Impact Modeler](agent://428b53bf-f49e-4505-a607-3560a26b3d50)** — **no figure moves and the *"certified subsidy"* floor is unaffected.** f4-a changes which survivor is paid in a narrow class and f1-b enlarges the class that receives a § 51.1-162 benefit by the member who dies with a disability application pending. MOO-200 §4 puts expected G 4 deaths over the whole pilot at **≈ 0.15**.
- **[@Editor](agent://006142a8-726b-4094-acc8-f6053dd25ee0)** — three risk-section items are below, and **the two *"notwithstanding"* displacements must travel in the drafting request to Division of Legislative Services.** A drafter's note is not enacted.

---

## 6. Three sentences for the Editor

**The bill now says that a member who dies with a disability retirement application pending, whose retirement date the Retirement System fixes after she is dead, is treated as having died before retirement — so her family receives the death benefit the purchased military service credit was bought to increase, instead of a refund of her own contributions.** **Where an optional-retirement election and the death benefit would be paid to different people, the bill pays what the existing option provisions require and does not add a second payment, so no family is worse off than under present law and that family gains nothing from the purchase.** **And the rule that a teacher, a local employee or a member of another state retirement system cannot join the program is moved from the subsection about local governments into the subsection that creates the program, where a reader looking for who may join will find it.**

---

**Internal working draft throughout. Nothing here is a Division of Legislative Services bill, nothing has been reviewed by counsel or by DLS, and no part of it is legally sufficient for introduction. Pre-decisional and internal.**
"""

open(os.path.join(HERE, "rev69-record.md"), "w", encoding="utf-8").write(doc)
print("record length", len(doc))


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def req(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(base() + path, data=data, method=method, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", ""),
        "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


if "--write" in sys.argv:
    st, res = req("PUT", f"/api/issues/{os.environ['PAPERCLIP_TASK_ID']}/documents/moo97-rev69-record",
                  {"title": "Store revision 69 — the record: the Director's four answers out of "
                            "MOO-189 (f1-b, f4-a, f14-move, f11-authority), redline, provisions as "
                            "amended, cross-reference check",
                   "format": "markdown", "body": doc})
    print(st, res.get("latestRevisionId") if isinstance(res, dict) else str(res)[:400])
    assert st in (200, 201) and res.get("body") == doc, "RECORD WRITE FAILED"
    print("RECORD WRITE OK", len(res["body"]))
