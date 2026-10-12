#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys
import urllib.request
import urllib.error

MOO97 = os.environ["PAPERCLIP_TASK_ID"]
KEY = os.environ["PAPERCLIP_API_KEY"]
RUN = os.environ.get("PAPERCLIP_RUN_ID", "")
BASE = os.environ["PAPERCLIP_API_URL"].rstrip("/")
if BASE.endswith("/api"):
    BASE = BASE[:-4]

DETAILS = """**Store revision 61 is in the text.** [MOO-161](/MOO/issues/MOO-161)'s counsel pass returned **20 findings — 1 fatal, 9 serious, 6 moderate, 4 minor** — and your five answers of 12 October are enacted with eight of its findings. **The fatal one was cured by taking words out:** store revision 58's *"§ 51.1-163 shall not apply to the member's death"* reached a member who **retired in a qualifying retirement and died years later in retirement**, and forfeited her unrecovered contributions — on the reviewer's facts $122,000 owed to a brother. § 51.1-163 cannot reach a pre-effective-date death of its own force at all, so the words were never load-bearing: they are deleted and the sentence is confined to the notification window in D 1's own language. **I treated that as restoring the agreed scope rather than choosing a policy, and the wider alternative is on this card if the intention was wider.**

**These seven are drafted word for word and enacted nowhere.** Every word of each is at [`moo161-disposition`](/MOO/issues/MOO-97#document-moo161-disposition) §7, and each is one substitution. **Check any combination; I will draft exactly what you check.** Four notes before you do.

- **(1) F3 is the one I would put first.** Subdivision G 4 tells the Board to pay *"whichever is greater"* of two benefits that are **different kinds of money payable to different people**. On the reviewer's facts — contingent annuitant her **mother**, surviving **husband**, designated beneficiary her **sister** — there are three candidate payees, one direction to pay the greater, and no basis of comparison. **(a) and (b) are cumulative. (c) is an alternative to both** and is the smallest, but it takes a right from the designated beneficiary.
- **(2) F7 is the reviewer's highest-value repair after F1, and it overrides a period in another section.** § 51.1-162 C's waiver expires 90 days after the death; the act's notice of that right is due up to 90 days after the Board **learns** of the death. Every day of delay is a day by which the Commonwealth's own letter can arrive after the right it describes has gone.
- **(3) F10's two forms are alternatives — check at most one — and neither should be cut until the Statutory Researcher confirms the sister-system sections.** Checking one tells me the direction, not the date.
- **(4) F8's gated alternative works against what is enacted.** The narrow class is in the text now; the gated general formula would put the Chairmen and the public back inside the words and rely on a court to keep them out.

**Doing nothing on (4) F11 is a decision**: the $3,000,000 cap then bounds reservations and not the Commonwealth's whole exposure, and that has to be stated in the fiscal note and in the memo's risk section whether or not the sentence is enacted.

**Not on this card and still open:** §7 item 60's (a), (b) and (c) — the elected-option class whose contingent annuitant is a sibling, an adult child or an unmarried partner — and the five answers at §7 item 122 you did not select, including **F5's two forms, the ERF residual this issue was opened on**.

**Internal working draft throughout. Not a Division of Legislative Services bill, not reviewed by DLS, not legally sufficient for introduction.**"""

OPTIONS = [
    ("f3-a", "(1) F3(a) — state the measure: the two benefits compared on actuarial equivalence as of the date of death",
     "Cumulative with (b). 'Whichever is greater' currently states no basis of comparison between a lump sum and a lifetime allowance."),
    ("f3-b", "(1) F3(b) — state the payee: pay the person whom the provision producing the greater benefit requires",
     "Cumulative with (a). It names a payee by cross-reference, which is why it is yours. Without it, three people have a colourable claim to one payment."),
    ("f3-c", "(1) F3(c) — confine the greater-of to the case where the payees coincide (C 2's own 'however' limb)",
     "Alternative to (a) and (b). Smallest change; it lets C 2's first limb be displaced outright and takes a right from the designated beneficiary."),
    ("f7-toll", "(2) F7 — the § 51.1-162 C waiver does not expire before the 30th day after the Board's late notice",
     "The reviewer's highest-value repair after the fatal finding. It overrides a period stated in another section of the Code."),
    ("f10-a", "(3) F10(a) — generalise the death branch to §§ 51.1-162, 51.1-207 and 51.1-218 as applicable to the member's plan",
     "Alternative to (b). Keeps the sister systems in the Program but requires reframing all six certification propositions. Waits on the Statutory Researcher."),
    ("f10-b", "(3) F10(b) — confine the Program to Chapter 1 members by one sentence in subsection L",
     "Alternative to (a). One sentence, cheaper, and a scope decision: it excludes State Police, VaLORS and Judicial Retirement System members from the Program."),
    ("f11-disclose", "(4) F11 — say expressly in subsection N that a § 51.1-162 death benefit is not charged against the D 2 limitations",
     "Changes nothing and discloses everything. Not enacting it is also a decision, and either way the fiscal note cannot present $3,000,000 as the act's maximum exposure."),
    ("f14-supp", "(5) F14's companion — a further notice, with a fresh review period, if an amount is later determined differently",
     "A new duty on the Board. The case is a Workers' Compensation award that changes the benefit months after the first notice."),
    ("m2-lateness", "(6) M 2 — make lateness reviewable for 30 days after the Board cures it",
     "Today the failure limb closes the instant the Board acts, so a 30-day-late crediting becomes unchallengeable as lateness. A new right, and small."),
    ("f8-gated", "(7) F8's alternative — restore the general notice class in a gated form instead of the two named classes",
     "Works against what is enacted. 'Other person to whom this section requires a notice of a determination affecting that person to be given' keeps the public out by construction rather than on the face of the act."),
]

payload = {
    "kind": "request_checkbox_confirmation",
    "idempotencyKey": "checkbox:%s:moo161-answers:rev61" % MOO97,
    "title": "Store revision 61 is in: MOO-161's fatal finding cured, eight findings enacted, and seven answers drafted — three of which decide who is paid",
    "summary": "The fatal finding was cured by deleting words, not adding them. These seven are drafted and enacted nowhere; four notes on alternation and one on doing nothing.",
    "continuationPolicy": "wake_assignee",
    "payload": {
        "version": 1,
        "prompt": "Check each answer you want drafted into the bill.",
        "detailsMarkdown": DETAILS,
        "options": [{"id": i, "label": l, "description": d} for i, l, d in OPTIONS],
        "minSelected": 0,
        "maxSelected": None,
        "acceptLabel": "Draft what I have checked",
        "rejectLabel": "Discuss first",
        "rejectRequiresReason": True,
        "rejectReasonLabel": "What should change?",
        "supersedeOnUserComment": True,
        "target": {"type": "issue_document", "issueId": MOO97, "key": "moo161-disposition",
                   "revisionId": "b2c677c0-ac7d-4b0c-a0ca-6d211c4feae8"},
    },
}

url = BASE + "/api/issues/%s/interactions" % MOO97
req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST")
req.add_header("Authorization", "Bearer " + KEY)
req.add_header("Content-Type", "application/json")
if RUN:
    req.add_header("X-Paperclip-Run-Id", RUN)
try:
    with urllib.request.urlopen(req) as r:
        d = json.loads(r.read().decode() or "{}")
        d = d.get("interaction", d)
        print("CARD CREATED:", d.get("id"), d.get("status"), len(d.get("payload", {}).get("options", [])), "options")
except urllib.error.HTTPError as e:
    print("FAILED", e.code, e.read().decode()[:600])
    sys.exit(2)
