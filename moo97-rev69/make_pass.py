# -*- coding: utf-8 -*-
import json, os, sys, urllib.request, urllib.error
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from edits import EDITS
labels = json.load(open(os.path.join(HERE, "out-labels.json")))

pairs = []
for i, ed in enumerate(EDITS, 1):
    pairs.append(f"### Edit {i} — `{ed['id']}` — {ed['label']}\n\n**FIND** ({len(ed['find'])} chars):\n\n"
                 f"> {ed['find']}\n\n**READ** ({len(ed['repl'])} chars, {len(ed['repl'])-len(ed['find']):+d}):\n\n> {ed['repl']}\n")

desc = f"""**Bounded, self-contained adversarial pass on five substitutions and nothing else.** Everything you need is in this description; you do not need to read [MOO-97](/MOO/issues/MOO-97) or any document on it.

**The base.** `bill-text-s8` on [MOO-42](/MOO/issues/MOO-42), **store revision 69**, document revision `{labels['billRevisionId']}`, §1 = {labels['s1Len']:,} characters. All five substitutions are in **new § 51.1-142.4** — subdivision **G 4** (three), subsection **B** (one), subsection **L** (one). Read the surrounding provisions in §1 of that document; read §§ 51.1-124.3, 51.1-153, 51.1-156, 51.1-162, 51.1-163, 51.1-165 and 51.1-165.01 **at source on LIS**, not from any quotation in our record.

**What they are.** The Policy Director's four answers of 12 October 2026 out of [MOO-189](/MOO/issues/MOO-189)'s counsel pass: **f1-b** (the cure to MOO-189's **fatal** F1), **f4-a** (confining subdivision G 4's greater-of to coincident payees), **f14-move** (moving the state-system eligibility bar from subsection L to subsection B) and **f11-authority** (a request to counsel, commissioned separately as [MOO-207](/MOO/issues/MOO-207) and **not** part of this pass).

---

## The five substitutions, verbatim

{chr(10).join(pairs)}

---

## Eight things to attack, in this order

1. **f1-b's residual, which I named and did not draft against.** A disability retiree **already in payment** whose effective date the Board *re-determines* after her death is, on the words, *"a retirement the effective date of which the Board determines after the date of the member's death."* Does the exception reach her? If it does, what does it cost, and who pays? (The unselected alternative **f1-a** would have added *"and a retirement allowance has become payable to the member under that retirement"*; taking it was not open to me because the Director chose (b) over (a).)
2. **Whether the confinement I added — *"that is not a qualifying retirement"* — leaves any member of F1's class out.** Can a retirement whose effective date the Board determines after the member's death ever be a **qualifying retirement** as subsection A defines it, and if so does that member need the exception for either limb?
3. **Whether the second limb I added does its job.** The branch that pays the death benefit is conditioned on *"clause (i) of this subdivision applies **and the member has not retired before the date of death**."* Read clause (i), its carve-out and the new exception together: is that condition now satisfied for the member who died with a disability application pending whose effective date was fixed, after her death, to a date before it? If not, the Director's approved answer does not reach its own class.
4. **f4-a's coincident-payee test — is it determinate when the Board must apply it?** *"The person or persons to whom that subdivision requires a benefit to be paid"* against *"the person or persons to whom the benefit determined under the preceding sentence would be payable."* Attack **partial** overlap (C 2 reaches two parents, § 51.1-162 B reaches one of them), minors and fiduciaries, a designation made and revoked, and the order of precedence where no designation exists.
5. **f4-a's non-coincident branch.** *"The Board shall pay the benefit that subdivision provides and shall not pay the benefit determined under the preceding sentence."* Does that purport to defeat an entitlement § 51.1-162 confers of its own force, and is there any case in which it leaves a person worse off **than present law** (not than store revision 68)?
6. **The five *"preceding sentence"* references in that one sentence.** Every one of them is meant to be the § 51.1-162 determination sentence, which is why the new branch is a semicolon clause and not a sentence. Check each.
7. **f14-move.** Does the bar operate differently in subsection B than it did in subsection L? Attack: whether it now conditions the **purchase** rather than the **election**; whether standing next to *"An eligible member may purchase…"* invites the argument that the definition's exclusions are only those the bar enumerates; and whether anything in §1 or §2 refers to the bar by location.
8. **Anything these five make worse that [MOO-200](/MOO/issues/MOO-200) reported against store revision 67** — in particular its **F14**, since f14-move removes from subsection L the sentence F14 wanted kept and made express.

## Findings you must NOT re-run

- **[MOO-200](/MOO/issues/MOO-200)'s F1 to F18** on store revision 67. They are reported, they are mine to dispose, and the disposition is the next revision. Only tell me where **these five substitutions** change one of them.
- **[MOO-189](/MOO/issues/MOO-189)'s F1 (fatal) and F4** as defects of store revision 67 — these substitutions are their cure. Attack the cure, not the defect.
- **[MOO-161](/MOO/issues/MOO-161) F1** (the sentence reaching the retiree) and **[MOO-169](/MOO/issues/MOO-169) F1** (the sentence missing the abolished-position member). Both are cured and both are what the confinement in point 2 protects.
- **The Policy Director's standing direction of 12 October 2026:** subdivision G 4's death-branch condition stays a condition on the member's **retirement status** and never returns to a filing, notification, acceptance or Board-receipt event. **Two cures have each tried a window and each drew a fatal finding.** If a defect needs a form of that condition the direction forecloses, **report it as fatal and say so — you do not owe me a cure**, and it becomes a card for the Director rather than a drafting fix.

## Two premises I would like to be wrong about

1. That the exception's *"the Board determines"* is naturally read as the single determination of an effective date when a retirement is approved, so that a later correction is not that determination (point 1).
2. That in f4-a's non-coincident case the family is in exactly the position Chapter 1 puts them in today, so that **no person is worse off than under present law** even though store revisions 67 and 68 would have paid more.

## How to report

**Post your findings as a comment and/or a document on THIS issue and mark it `done`.** A fatal verdict is a completed pass — `done`, not `blocked`. Rate each finding fatal / serious / moderate / minor, quote the exact words at fault, give the authority, give a concrete failure scenario with a named loser, and give a fix direction. **State your null results too** — what you checked and found sound is as useful to me as what you found. Fixes are mine.

*Internal working draft material throughout. Nothing in this draft is a Division of Legislative Services bill, nothing has been reviewed by DLS, and no part of it is legally sufficient for introduction.*
"""
open(os.path.join(HERE, "pass-desc.md"), "w", encoding="utf-8").write(desc)
print("desc", len(desc))


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/"); return u[:-4] if u.endswith("/api") else u


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
    st, res = req("POST", f"/api/companies/{os.environ['PAPERCLIP_COMPANY_ID']}/issues", {
        "title": "Bounded counsel pass on store revision 69's five substitutions — the cure to "
                 "MOO-189's fatal F1, the greater-of confined to coincident payees, and the "
                 "eligibility bar moved out of subsection L",
        "description": desc, "priority": "high", "status": "todo",
        "assigneeAgentId": "d71e111e-1296-4d66-81ac-750dcc8d8681",
        "parentId": os.environ["PAPERCLIP_TASK_ID"]})
    print(st, res.get("identifier"), res.get("id") if isinstance(res, dict) else str(res)[:300])
    json.dump({"id": res.get("id"), "identifier": res.get("identifier")},
              open(os.path.join(HERE, "pass-issue.json"), "w"), indent=1)
