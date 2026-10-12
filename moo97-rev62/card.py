#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, sys, urllib.request, urllib.error
MOO97=os.environ["PAPERCLIP_TASK_ID"]
def base():
    u=os.environ["PAPERCLIP_API_URL"].rstrip("/"); return u[:-4] if u.endswith("/api") else u
def req(method, path, payload=None):
    data=json.dumps(payload).encode() if payload is not None else None
    r=urllib.request.Request(base()+path, data=data, method=method, headers={
        "Authorization":"Bearer "+os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id":os.environ.get("PAPERCLIP_RUN_ID",""),
        "Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(r) as resp: return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e: return e.code, e.read().decode()

OPTS=[
 ("f7-a","(1) F7(a) — bar the Commonwealth's payment until the benefit is known",
  "Alternative to (b). Delays the Commonwealth's cash and keeps it out of the trust fund until the benefit is known, so the release actually operates. The load-bearing fiscal assumption of the whole package depends on one of these two."),
 ("f7-b","(1) F7(b) — repay the Commonwealth and restore the cap where already paid",
  "Alternative to (a). Takes money back out of the trust fund after settlement, which is what MOO-96's F-3 and Va. Const. art. X, § 11 bear on. Cleaner cash timing, harder constitutionally."),
 ("s163-valuation","(2) The § 51.1-163 valuation date — your approved measure has one incomputable side",
  "One clause, cumulative with what is enacted. § 51.1-163 measures contributions 'as of the effective date of his retirement' and in a pre-effective-date death that date never arrived. It fixes an amount, which is why it is not enacted."),
 ("f3-c-instead","(2, alt) f3-c instead — confine the greater-of to where C 2 itself pays under § 51.1-162 B",
  "Alternative to the valuation date. Dissolves the problem rather than solving it, because both figures are then of the same kind. You did not select it last card; it takes a right from the designated beneficiary."),
 ("f5-discovery","(3) F5's discovery rule — her 30 days also run from the day she files evidence of the omission",
  "The contradiction is cured in store revision 62; this is about whether her window is useful. An open-ended limitation period, which is why it is a policy setting and not drafting."),
 ("f10-advisory","(4) F10 — compel the Board to tell her to review her designation of beneficiary",
  "On the reviewer's analysis the cheapest thing on this card. § 51.1-162 B pays a designated relative; a member who designated her sister in 2009 and is survived by her mother gets nothing from the purchase. A new compelled statement."),
 ("m7-matching","(5) M7 — a quarterly Board duty to match against death records, deemed knowledge on a match",
  "Closes the loop where an agency never reports and so the Board never learns of the death and never reports the failure. A new duty with an administrative cost, and the vital-records citation must come from the Statutory Researcher before it is drafted into the act."),
 ("m8-a","(6) M8(a) — cap the Board-operated tolling exclusion at 90 days",
  "Alternative to (b). Bounds Board delay without ever costing the member her qualifying retirement."),
 ("m8-b","(6) M8(b) — restart the member's final qualifying retirement date once the Board's 90 days expire",
  "Alternative to (a). Stronger discipline on the Board, and it can cost the member her qualifying retirement through no fault of her own."),
 ("s162c-conforming","(7) The conforming amendment to § 51.1-162 C — it widens the act's footprint",
  "One clause, but it adds § 51.1-162 to the amended sections, changes the title line and changes the first enactment clause. The act has amended one section and added one since revision 21 removed § 51.1-155 on your direction."),
]
DETAILS = """**Store revision 62 is in the text.** [MOO-169](/MOO/issues/MOO-169)'s fatal finding is cured, fourteen of its findings are enacted, two are declined with reasons, and **all seven of the answers you selected on 12 October 2026 are in**. Full record: [`moo169-disposition`](/MOO/issues/MOO-97#document-moo169-disposition). Each answer below is drafted word for word at **§7 item 129** in [`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list).

**Two things about your last card you should know before answering this one.**

- **f10-b's scope decision was already the law of the act.** The definition of *"eligible member"* already excludes *"a member of a retirement system established under Chapter 2 (§ 51.1-200 et seq.), Chapter 2.1 (§ 51.1-211 et seq.), or Chapter 3 (§ 51.1-300 et seq.)."* I enacted the sentence in subsection L **in the chapter form, not the three-named-system form the card carried**, because two formulations of one concept is a defect. **It confirms the scope rather than changing it**, and the sister-system question routed to research is now moot for this act.
- **f3-a's measure has one incomputable side.** That is answer 2 below, and it is the only item on this card that arises from an answer you have already given.

**Four of the seven decide who bears a loss and I have picked none.** **F7 first** — it is not only a drafting gap. On subsection N's own words (*"upon the settlement"*) **nothing is ever released**, so a certified subsidy that buys no benefit stays charged against the $3,000,000 cap forever, and at the $170,000 per-election ceiling each such death permanently removes one election from the admitted cohort — the reviewer puts it at **5.6 to 5.9 percent fewer admissions per occurrence**. The party who pays is the next applicant on the subdivision D 5 waiting list.

**Alternation notes.** (1) **(a) or (b), not both.** (2) **the valuation date or f3-c, not both.** (6) **(a) or (b), not both.** Items 3, 4, 5 and 7 are independent and may be combined with anything.

**Still open and not re-asked:** §7 item **60**'s (a), (b) and (c) — the elected-option class whose contingent annuitant is a sibling, an adult child or an unmarried partner. Subdivision G 4 routes her death to § 51.1-162 and § 51.1-162 B pays only a designated spouse, minor child or parent, so **she remains unanswered**. Also the five unenacted answers at item **122**, and items **106**, **107**, **126** and **127**.

**Internal working draft throughout. Nothing here is a Division of Legislative Services bill, nothing has been reviewed by DLS, and no part of it is legally sufficient for introduction.**"""

payload={
 "kind":"request_checkbox_confirmation",
 "idempotencyKey":f"checkbox:{MOO97}:rev62-moo169-answers:v1",
 "title":"Store revision 62 is in: MOO-169's fatal finding cured, fourteen findings enacted, your seven answers in — seven new answers drafted and none enacted",
 "summary":"Check each answer you want drafted into the bill. Four of the seven decide who bears a loss. F7 first.",
 "continuationPolicy":"wake_assignee",
 "payload":{
   "version":1,
   "prompt":"Check each answer you want drafted into the bill.",
   "detailsMarkdown":DETAILS,
   "options":[{"id":i,"label":l,"description":d} for i,l,d in OPTS],
   "minSelected":0,"maxSelected":None,
   "acceptLabel":"Draft the checked answers",
   "rejectLabel":"Discuss first",
   "rejectRequiresReason":True,
   "rejectReasonLabel":"What should change?",
 },
}
st,res=req("POST", f"/api/issues/{MOO97}/interactions", payload)
if st not in (200,201): print(f"CARD FAILED {st}: {str(res)[:600]}"); sys.exit(2)
print("CARD OK", res.get("id"), res.get("status"))
json.dump({"id":res.get("id"),"status":res.get("status")}, open("card.json","w"))
