# -*- coding: utf-8 -*-
import json, os, sys, urllib.request, urllib.error


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


DETAILS = """**Two of [MOO-200](/MOO/issues/MOO-200)'s findings land on answers you approved yesterday, and one of them my own revision made worse. Everything below is drafted word for word. I have picked none of them.**

MOO-200's pass on store revision 67 reported at 00:15 UTC today — **0 fatal, 5 serious, 7 moderate, 6 minor, 12 null results**. Its eighteen findings are mine to dispose and that is the next revision. **These two are on this card because they bear on what store revision 69 has just enacted**, and because one of them is a consequence of f14-move rather than of anything counsel found in your answer.

---

### F14 — subsection L's audience. **f14-move aggravates this and you should know it before anything else.**

**The finding.** Subsection L exists to tell localities, school boards and the Commission on Local Government that the act does not reach them. Its first sentence says so for duties and costs; its second sentence **used to say so expressly for teachers and local employees**, until store revision 67 replaced the enumeration with a cross-reference to the definition — which counsel says made the comfort derivative. **f14-move, which you approved, removes the sentence from that subsection altogether**, so the subsection addressed to that audience now says nothing on the subject.

**The eligibility rule is unchanged.** The bar is in the act, in subsection B, and the definition is where it has always been. **This is an audience question, not a defect in the bar** — which is why it is a card and not a repair.

- **(1) F14-L — give subsection L back an express sentence for its own audience.** Drafted, as a new second sentence of subsection L: *"Nothing in this section makes a teacher, an employee of a political subdivision, or an employee of a local school board an eligible member, and no such person is eligible to make an election under this section."* **Cumulative with f14-move: the bar stays in subsection B, where you put it, and subsection L speaks to its reader again.** About 215 characters. **This is the answer I would take if you want one**, because it costs nothing and reverses nothing you decided.
- **(2) F14-reverse — put the bar back in subsection L and undo f14-move.** One substitution each way, net zero characters. **Alternative to (1), not cumulative.** It restores exactly the text counsel reviewed, and it re-creates the defect f14-move was approved to cure: the person looking for who may join the program does not find the bar next to the grant.
- **(3) F14-anchor — give the bar a time anchor.** Counsel's separate point, and it is **independent of where the bar sits**: the definition of *"eligible member"* excludes by each of clauses (i) to (viii), several of which are time-dependent, while the bar states no date. The anchor exists elsewhere — subdivision D 4 determines eligibility *"as of the filing date of the applicant's complete application"* — so the better reading is sound, but on its face the bar invites the argument that a member who later ceases to satisfy a clause **was never eligible and her accepted election is void.** Drafted, replacing the bar's opening: *"No person who is not an eligible member, determined as of the filing date of that person's complete application, is eligible to make an election under this section"*, and the enumeration follows unchanged. **Cumulative with (1) or (2).** **It changes words you approved twice** — f10-b put the enumeration there and f14-move moved it — which is why it is here rather than in the text.

---

### F6 and F7 — the greater-of comparison f4-a has just confined. **Counsel says it changes no amount for anyone.**

**The finding.** **F7:** in the branch where subdivision C 2 of § 51.1-165 routes to § 51.1-163, the comparison is a lump sum of accumulated contributions against a lifetime allowance, and the Program's own eligibility clauses confine participants to members at or near their unreduced date — so the allowance wins on any plausible basis. In the branch where C 2 routes to § 51.1-162 B, both sides are **the same number**, because the G 4 benefit *is* § 51.1-162 computed on the member's creditable service. *"The clause is surplusage."* **F6:** the basis the clause names — *"the actuarial assumptions and factors the Board uses to determine actuarial equivalence under § 51.1-165"* — is not an identifiable set: § 51.1-124.3 defines *"actuarial equivalent"* by *"actuarial tables **adopted** by the Board"*, § 51.1-165 does not assign the Board a determination of actuarial equivalence, and **no § 51.1-165 option converts an allowance into a lump sum at all**, so the named set does not contain the factor the named comparison needs.

**f4-a neither cures nor worsens either.** It changes **when** the comparison runs, not what it is measured on.

- **(4) F7-strike — strike the greater-of comparison and the death-dating together.** Counsel's first fix direction. It removes about 400 characters from subdivision G 4 and leaves the savings clause and f4-a's two branches. **Alternative to (5).** **Weigh this:** the dating was your own answer `s163-valuation` of 12 October, approved to cure the one incomputable side of the measure; striking it reverses that answer, and if counsel's reading of C 2 is ever held wrong the comparison is gone.
- **(5) F7-keep + F6-fix — keep the comparison and name the basis in the Code's own words.** Drafted: for *"determined on the actuarial assumptions and factors the Board uses to determine actuarial equivalence under § 51.1-165"* read <u>*"as actuarial equivalents within the meaning of § 51.1-124.3"*</u>. **Alternative to (4).** 29 words become 8, the basis becomes a thing the Board has **adopted** and a court can find, and **the act stops attributing to § 51.1-165 a determination that section does not make.** The drafter's note will say the clause is not expected to be operative.

---

**What is NOT on this card, deliberately.** MOO-200's **F1** (the certification compels the Board to state, unqualified, that a partial lump-sum election does not reduce the § 51.1-162 B death allowance — counsel's most serious finding, and it bites on **every** certification, not on a death), **F2** (f7-a can bar the Commonwealth's payment for ever, because § 51.1-162 B's election has no deadline anywhere in the Code — its cure needs **one number** from you), **F3** (§ 51.1-162 C's new clause is permanent while § 51.1-142.4 expires 1 July 2033), **F4**, **F5** and the remaining twelve. **They come with the disposition, as drafted answers, so that you see them against the text they will land in.** Say so if you would rather have F2's number now.

**Still open and not re-asked:** §7 item 132's **f12-ninety** and **f3-operative**; §7 item 60's **(a)**, **(b)** and **(c)** — the elected-option class whose contingent annuitant is a sibling, an adult child or an unmarried partner; and [MOO-191](/MOO/issues/MOO-191)'s seven undrafted answers on the designation-review advisory.

**Internal working draft throughout. Nothing here is a Division of Legislative Services bill, nothing has been reviewed by DLS, and no part of it is legally sufficient for introduction.**"""

payload = {
    "kind": "request_checkbox_confirmation",
    "idempotencyKey": "checkbox:moo97:rev69-moo200-f14-f7:v1",
    "title": "Store revision 69 is in the text — two MOO-200 findings land on the answers you just approved",
    "summary": "F14 (subsection L's audience, which f14-move aggravates) and F6/F7 (the greater-of "
               "comparison f4-a confines). Five drafted answers; check any combination.",
    "continuationPolicy": "wake_assignee",
    "payload": {
        "version": 1,
        "prompt": "Check what you want drafted. (1) and (2) are alternatives; (3) is cumulative with "
                  "either; (4) and (5) are alternatives.",
        "detailsMarkdown": DETAILS,
        "options": [
            {"id": "f14-L", "label": "(1) F14-L — give subsection L an express sentence for its own audience (cumulative with f14-move)",
             "description": "New second sentence of L naming teachers, political-subdivision employees and local school board employees. ~215 characters. Reverses nothing you decided."},
            {"id": "f14-reverse", "label": "(2) F14-reverse — put the bar back in subsection L and undo f14-move (alternative to (1))",
             "description": "Net zero characters. Restores the text counsel reviewed and re-creates the defect f14-move cured."},
            {"id": "f14-anchor", "label": "(3) F14-anchor — give the bar a time anchor at the filing date of the complete application",
             "description": "Cumulative with (1) or (2). Closes the argument that a member who later ceases to satisfy a clause was never eligible. Changes words you approved twice."},
            {"id": "f7-strike", "label": "(4) F7-strike — strike the greater-of comparison and the death-dating together (alternative to (5))",
             "description": "Counsel's first fix direction, ~400 characters out. It reverses your own s163-valuation answer of 12 October."},
            {"id": "f7-f6-fix", "label": "(5) F7-keep + F6-fix — keep the comparison and name the basis as § 51.1-124.3 defines it (alternative to (4))",
             "description": "\"As actuarial equivalents within the meaning of § 51.1-124.3\". 29 words become 8; the basis becomes a thing the Board has adopted and a court can find."},
        ],
        "minSelected": 0,
        "maxSelected": None,
        "acceptLabel": "Draft what I have checked",
        "rejectLabel": "Discuss first",
        "rejectRequiresReason": True,
        "rejectReasonLabel": "What should change?",
        "supersedeOnUserComment": True,
    },
}
st, res = req("POST", f"/api/issues/{os.environ['PAPERCLIP_TASK_ID']}/interactions", payload)
print(st, json.dumps(res, indent=1)[:500] if isinstance(res, dict) else res[:800])
if isinstance(res, dict) and res.get("id"):
    json.dump({"interactionId": res["id"], "status": res.get("status")},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "card-out.json"), "w"), indent=1)
