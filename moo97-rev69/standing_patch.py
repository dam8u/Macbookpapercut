# -*- coding: utf-8 -*-
import json, os, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
b = open(os.path.join(HERE, "standing.md"), encoding="utf-8").read()
meta = json.load(open(os.path.join(HERE, "standing-meta.json")))

A5_NEW = """### A5. Route (b) on §7 item 130 — M 2's uncapped tolling — is DECLINED, and is not a conforming amendment

**Decision, 13 October 2026, out of [MOO-164](/MOO/issues/MOO-164), on this issue's thread. It supersedes the hold of 12 October, which this section used to record.**

> **Route (b) is declined, as a decision and not by implication — and (b) + (c) is declined too.**

**Four things follow, and all four are binding.**

1. **Route (b) is not to be drafted** — not on [MOO-97](/MOO/issues/MOO-97), not on [MOO-164](/MOO/issues/MOO-164), and not in any store revision. It is declined, not held, so there is nothing to release.
2. **Route (b) must never be written up as a conforming amendment**, and this is the ground of the declination. It carries subdivision G 4's words — *"a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate"* — into subdivision M 2, **where the incidence reverses.** G 4's non-running protects *"a period within which the Board is required to act or a period within which a determination is required to take effect"*, so denying the extension makes the Board bear its own delay. M 2's tolling protects *"the member's final qualifying retirement date and … any period within which the member or applicant must act"*, so the identical words make **the member** bear it. Verified on the live text of both. **The form is conserved and the effect reverses: it is a policy choice wearing a conforming amendment's clothes.**
3. **Route (c) is adopted in [MOO-164](/MOO/issues/MOO-164)** — candidate 164-7 with the trigger limb (B). **(b) + (c) was the real question and it was declined too:** clause (ii) would be bounded twice, by two instruments for one concept, and the only case (b) uniquely covers is the case where unbounded tolling **favours** the member.
4. **Limb (i) is already bounded and route (b) was never needed for the rest.** **m8-a**, enacted at store revision 67, closes M 2 clause (ii) with *"provided that the aggregate of all periods so excluded shall not exceed 90 days"*. And the Director's own correction: the subdivision D 4 / D 5 filing-date retention and the 15-day duty to act on the application are **one sentence, and it is the sentence after clause (ii)** — so **no amendment confined to clause (ii) could ever have reached either.**

**The four-endpoint inventory still stands and is still the map.** M 2's tolling terminus (bounded by m8-a); M 2's subdivision D 4 / D 5 filing-date retention; M 2's 15-day duty to act upon the application; **and a fourth in subsection A's definition of *"final qualifying retirement date"*** — the Board's 15-day duty to notify the member of that date. Counted and quoted at [`moo97-m2-act-endpoint-inventory`](/MOO/issues/MOO-97#document-moo97-m2-act-endpoint-inventory). **Candidate 164-7-B gives the definition-request class a determinate date; it still has no deemed denial and so no case decision, where the reconsideration class has one, and the Director has carded that asymmetry rather than sending it to drafting.**

**[MOO-92](/MOO/issues/MOO-92)'s third residual is closed by this decision**, and §7 item 130 carries the annotation as of store revision 69.

---

### A8 — Subdivision G 4's greater-of sentence must stay one sentence

**Enacted at store revision 69 and binding on every later amendment of it.** That sentence now contains **five** references to *"the preceding sentence"*, and every one of them means the sentence that determines the benefit under § 51.1-162 — not the greater-of sentence itself. **f4-a's non-coincident branch is therefore joined to it by a semicolon and is deliberately not a sentence of its own.** Any further amendment of that branch, or any new branch of it, **must stay inside the same sentence**; a full stop gives every reference inside the new sentence a new antecedent and the branch becomes a rule about the wrong benefit. The apply kit for store revision 69 asserts this mechanically — the slice from *"Nothing in the preceding sentence reduces"* to *"Where the member dies"* must contain exactly five references and exactly one full stop, at its end — and the assertion should be carried forward.

---

### A9 — A new §7 item goes in the live list, before the §7.1 retained-record heading

**Store revision 69 found items 132, 133 and 134 written *after* the *"### 7.1 Retained record"* subsection**, which is captioned a retained record, so a reader of the live list never reached them. **This is the second occurrence** — store revision 37 did it with items 59, 60 and 61, and store revision 39 then numbered its own items from 62 in the belief that the earlier three were elsewhere. The three are moved back, verbatim and unrenumbered, in store revision 69. **Every kit that appends a §7 item must assert that the last live item precedes the §7.1 heading, and that the list is contiguous from 1 before and after.**

---"""

OLD_A5_START = "### A5. Route (b) on §7 item 130"
OLD_A5_END = "](/MOO/issues/MOO-97#document-moo97-m2-act-endpoint-inventory).\n\n---"
a = b.index(OLD_A5_START)
z = b.index(OLD_A5_END, a) + len(OLD_A5_END)
assert b.count(OLD_A5_START) == 1
b = b[:a] + A5_NEW + b[z:]

# Part C's first bullet: the item-130 annotation is no longer owed
C_OLD_START = "- **§7 item 130 does not carry the hold.**"
C_OLD_END = "with the incidence reversal in A5, and with the fourth limb."
a = b.index(C_OLD_START)
z = b.index(C_OLD_END, a) + len(C_OLD_END)
b = b[:a] + ("- **§7 item 130's annotation is TAKEN, in store revision 69.** It had still read *\"I "
             "recommend this one\"* against route (b) with no annotation through store revision 66, "
             "then carried store revision 67's *held* annotation. **Store revision 69 replaces that "
             "annotation with the declination**, its ground, the adoption of route (c), the "
             "Director's correction to the four-limb table, and the closing of MOO-92's third "
             "residual. **Nothing on that item is owed.**") + b[z:]

# Part D is spent: everything in it was enacted at store revision 67
D_OLD = "## Part D — Approved by the board and awaiting application"
a = b.index(D_OLD)
b = b[:a] + """## Part D — Approved and awaiting application: **none**

**Card `c67b1907` (§7 item 129, four of six approved, 12 October 2026) was applied in full at store revision 67** — f7-a in subsection N, the § 51.1-163 valuation date in subdivision G 4, m8-a in subdivision M 2 clause (ii), and the § 51.1-162 C conforming amendment, which took § 51.1-162 into the title line, into the first enactment clause and into §1 reproduced at length. **Not selected and not to be drafted:** f7-b, f3-c, F5's discovery rule, M7's death-matching duty, m8-b.

**Card `829fa6d2` (§7 item 132, four of six approved, 12 October 2026) was applied in full at store revision 69** — f1-b and f4-a in subdivision G 4, f14-move out of subsection L and into subsection B, and f11-authority commissioned as [MOO-207](/MOO/issues/MOO-207) rather than drafted, because it is a request to counsel. **Not selected, and closed by the selection of their alternatives:** f1-a, f1-c, f4-b, f4-c. **Not selected and still drafted and open at §7 item 132:** f12-ninety and f3-operative.

**Two conforming limbs were added to f1-b's approved words and are recorded at §6.0-69 items 2 and 3** — the confinement to a retirement that is *not* a qualifying retirement, and the limb for the branch's own verb condition. **Either is reversible in one substitution and neither moves a cost.**

**Nothing approved is awaiting application.** What is outstanding is in the other direction: **[MOO-200](/MOO/issues/MOO-200)'s eighteen findings on store revision 67 are undisposed** — 0 fatal, 5 serious, 7 moderate, 6 minor, reported 00:15 UTC on 13 October 2026 — and three of them (F6, F7, F14) bear on what store revision 69 enacted. **F14 is aggravated by f14-move** and is on the Director's card.
"""
out = b
print("new length", len(out))


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


for probe, n in (("A5. Route (b) on §7 item 130 — M 2's uncapped tolling — is DECLINED", 1),
                 ("is HELD, not declined", 0), ("### A8 —", 1), ("### A9 —", 1),
                 ("## Part D — Approved and awaiting application: **none**", 1)):
    assert out.count(probe) == n, (probe, out.count(probe))
assert "{" not in out.replace("{", "{") or True

st, res = req("PUT", f"/api/issues/{os.environ['PAPERCLIP_TASK_ID']}/documents/standing-drafting-directions",
              {"title": "Standing drafting directions — new § 51.1-142.4 (binding on every future revision)",
               "format": "markdown", "body": out,
               "baseRevisionId": meta["latestRevisionId"]})
print(st, res.get("latestRevisionId") if isinstance(res, dict) else str(res)[:400],
      len(res.get("body", "")) if isinstance(res, dict) else "")
assert st in (200, 201) and res.get("body") == out, "STANDING-DIRECTIONS WRITE FAILED"
print("STANDING-DIRECTIONS WRITE OK")
