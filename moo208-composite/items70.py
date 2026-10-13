#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-208 store revision 70 — the §7 item list.

Two operations, both on `bill-text-s8-item-list`, both directed or required by the Director's
disposition at MOO-191:

  * **item 133 re-scoped**, as the Director directed: F3 being taken, the misstatement limb must
    not reach a matter excepted from subsection M review, so the drafted words are re-written and
    the residue the re-scoping leaves is recorded in the item rather than drafted around.
  * **item 135 opened**, because the cross-reference sweep for store revision 70 found that F3's
    exception does not close the subsection M channel — subdivision M 2 does not look at
    subdivision D 1 — and the cure is one clause in M 2, a provision this commission did not open.
    Drafted in two forms and enacted nowhere.

Nothing is answered and nothing is closed. Item 134 and item 129's open answers are untouched.

    python3 items70.py --dry-run
    python3 items70.py
"""
import json, os, re, sys, urllib.request, urllib.error

CEILING = 524288
MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8-item-list"
BILL = "bill-text-s8"

# ---------------------------------------------------------------- item 133, re-scoped

OLD_HEAD = ("133. **NEW IN STORE REVISION 68, out of [MOO-195](/MOO/issues/MOO-195)'s pass 21 on "
            "the designation-review advisory (finding F7) — drafted in full and enacted nowhere. "
            "The failure sentence catches omission and misses misstatement.**")
NEW_HEAD = ("133. **NEW IN STORE REVISION 68, out of [MOO-195](/MOO/issues/MOO-195)'s pass 21 on "
            "the designation-review advisory (finding F7) — drafted in full and enacted nowhere. "
            "RE-SCOPED IN STORE REVISION 70 on your direction at [MOO-208](/MOO/issues/MOO-208), "
            "F3 having been taken. The failure sentence catches omission and misses "
            "misstatement.**")

OLD_DRAFTED = (
    "    **Drafted, in D 1's failure sentence:** *\"A failure to state in the Board's certification "
    "every matter this subdivision requires to be stated in it<u>, or the statement of any such "
    "matter otherwise than as this subdivision requires it to be stated,</u> is a failure of the "
    "Board to state in a certification a matter this section requires to be stated in it for the "
    "purposes of subsection M…\"*"
)
NEW_DRAFTED = (
    "    **Drafted as it stood at store revision 68, before F3 was taken:** *\"A failure to state "
    "in the Board's certification every matter this subdivision requires to be stated in it<u>, or "
    "the statement of any such matter otherwise than as this subdivision requires it to be "
    "stated,</u> is a failure of the Board…\"* **That scope is now wrong**, because *\"any such "
    "matter\"* reaches the advice, which store revision 70 has excepted from D 1's subsection M "
    "deeming. A misstatement limb over the advice would re-open the channel you closed.\n"
    "\n"
    "    **Re-scoped, store revision 70. This is the drafted text as it now stands, against the "
    "failure sentence as store revision 70 left it:** *\"A failure to state in the Board's "
    "certification every matter this subdivision requires to be stated in it, other than a failure "
    "to state that the Board advises the member to review the member's designation of beneficiary, "
    "<u>or the statement in the Board's certification of any matter this subdivision requires to be "
    "stated in it, other than that the Board advises the member to review the member's designation "
    "of beneficiary, otherwise than as this subdivision requires it to be stated,</u> is a failure "
    "of the Board to state in a certification a matter this section requires to be stated in it for "
    "the purposes of subsection M…\"* **+253 characters.** The exception is written in the same "
    "words the enacted exception uses, so the two limbs share one vocabulary and the phrase does "
    "one job in both.\n"
    "\n"
    "    **What the re-scoping reaches, and where it differs from your instruction. Recorded, not "
    "drafted around.** You directed that the limb reach *\"the six propositions of law and not the "
    "advisory.\"* **The drafted words reach every required matter other than the advice — the six "
    "propositions *and* item 7's other two propositions, the power to re-designate and the no-fault "
    "clause.** That is the F3 residue you named at §3 of the disposition, surfacing a second time: "
    "D3c's exception names only the first of item 7's three propositions, so those two stay inside "
    "D 1's deeming for omission, and the limb above keeps them inside it for misstatement too. "
    "**Scoping strictly to the six and no further is not draftable on the present text**: the seven "
    "items are undesignated clauses of one sentence, there is no handle to cite, and the only clean "
    "handle is designating them (i) through (vii) — a renumbering your commission forbade and a "
    "separate edit. **The alternative, if you want the strict scope, is that renumbering**; it is "
    "one cut over one sentence and it would also give the M exception a handle. §6.0-70 item 6."
)

OLD_NOT_ENACTED = (
    "    **Not enacted, for three reasons, and the third is the one that matters.** The defect is a "
    "property of a sentence **you approved at store revision 62**, not of the 137 characters cut at "
    "store revision 65; it is outside a cut commissioned as one edit; and **it interacts with the "
    "channel question** — if you take pass 21's F3 recommendation and except the advisory from "
    "subsection M review, the advisory needs no misstatement limb either, and the clause would then "
    "reach only the six propositions. **Decide F3 first.** The whole disposition is at "
    "[`moo195-disposition`](/MOO/issues/MOO-191#document-moo195-disposition)."
)
NEW_NOT_ENACTED = (
    "    **Still not enacted, and the reason has changed.** At store revision 68 the third and "
    "controlling reason was *\"decide F3 first.\"* **F3 is now decided and taken**, so that reason "
    "is spent. What remains: the defect is a property of a sentence **you approved at store "
    "revision 62** and not of the advisory, you commissioned store revision 70 as six named "
    "substitutions and this is not one of them, and the strict scope you asked for needs a "
    "renumbering you forbade. **So the words are re-scoped and the card stays open**, as you "
    "directed at [MOO-208](/MOO/issues/MOO-208). The whole disposition is at "
    "[`moo191-director-disposition`](/MOO/issues/MOO-191#document-moo191-director-disposition).\n"
    "\n"
    "    **One thing store revision 70 changed about this item's premise, and it cuts the other "
    "way.** This item has always said of the advisory that *\"there is no channel.\"* **After store "
    "revision 70 there still is one** — subdivision M 2 reaches a failure to state a matter this "
    "section requires to be stated on its own terms, and D 1's exception withdraws only D 1's own "
    "extension of it. That is **§7 item 135**, and it means the misstatement gap this item "
    "describes sits next to an omission channel that F3 did not in fact close. **Read items 133 "
    "and 135 together before deciding either.**"
)

# ---------------------------------------------------------------- item 135, new

ITEM_135 = """
135. **NEW IN STORE REVISION 70, out of the cross-reference sweep for that revision (§5.47 direction 2, check 1) — drafted in two forms and enacted nowhere. F3's exception does not close the subsection M channel, because subdivision M 2 does not look at subdivision D 1.** You took [MOO-195](/MOO/issues/MOO-195) F3 in form D3c conformed at [MOO-208](/MOO/issues/MOO-208), to except omission of the designation-review advice from subsection M review while keeping it in the subsection J report. **The J half works in full.** The M half does not, and the reason is in the act's own words.

    **Subdivision M 2's first sentence confers the channel independently.** It gives written reconsideration to a person adversely affected *"by **a failure of the Board to state in a certification or notice a matter this section requires to be stated in it**."* The advice is a matter **this subdivision** requires to be stated and D 1 is part of **this section**, so the omission is inside M 2's limb with no help from D 1.

    **D 1's sentence extends M 2; it does not constitute it.** M 2's own clock for a failure to state runs *"within 30 days after the certification or notice is given or, **where the provision that requires the matter to be stated provides a longer or later period, within that period**."* M 2 therefore anticipates that a provision like D 1 will extend it — which is precisely what D 1's bespoke clock does, giving the member 30 days from the certification and a claimant who is not the member 30 days from the subdivision G 4 notice. **An exception written into a conferring sentence confers less; it does not withdraw what another subdivision independently gives.** And §1 carries six *"for the purposes of subsection M"* clauses, the other five all declaratory (*"X is a determination of the Board for the purposes of subsection M"*), while M 2's second sentence says in terms that its own reach operates *"whether or not another provision of this section expressly provides for review of it."*

    **So what the exception actually did.** The member keeps reconsideration under M 2 on a 30-day clock from the certification. A claimant who is not the member — a survivor — **loses the subdivision G 4-notice clock, which was the only clock she could ever have used**, because the certification is handed to the member years before the survivor learns the designation was wrong. And M 2's second sentence, which D 1 had disapplied for the member, applies to her case again. **That is narrower than the status quo for the survivor and unchanged for the member, which is close to the opposite of the trade you took F3 for.**

    **No cure inside D 1 can work**, because the defect is that M 2 does not look at D 1. The clause has to go in M 2. **Two forms, both +1 substitution, neither enacted.**

    **Form M-a — name the matter in M 2, in the words the act already uses. Recommended.** FIND, 128 characters, 1× in §1: *"or by a failure of the Board to state in a certification or notice a matter this section requires to be stated in it, may obtain"*. READ: *"or by a failure of the Board to state in a certification or notice a matter this section requires to be stated in it<u>, other than a failure to state that the Board advises the member to review the member's designation of beneficiary</u>, may obtain"*. **+116 characters, and no conforming change anywhere else.** The exception then appears a fourth time in the same words, so there is still one vocabulary and one concept; it is visible in the provision that confers the channel, which is where a reader of subsection M looks; and it needs no reader to treat D 1's deeming clause as exhaustive.

    **Form M-b — a generic hook in M 2, plus a conforming clause in D 1.** READ in M 2: *"…a matter this section requires to be stated in it<u>, other than a matter that the provision of this section requiring it to be stated expressly excepts from this subsection</u>, may obtain"* — **+101 characters**, using the same hook M 2's clock already uses (*"the provision that requires the matter to be stated"*). It is cheaper for a second exception later, but it needs **+42 in D 1** so that D 1's exception says expressly that it excepts the matter from subsection M, and it buys a cross-reference by description where M-a buys one by name. **Take M-b only if you expect more exceptions.**

    **What neither form does.** Neither reaches item 7's other two propositions — the power to re-designate and the no-fault clause — because D3c's exception does not, and you left that residue to counsel's next pass. **Widening the exception to all three propositions is a third decision and it should be taken once, in both D 1 and M 2 together**, not twice in different places.

    **Why it is not cut.** It opens subdivision M 2, which store revision 70's commission did not open; it reverses nothing you decided, but it changes the effect of something you did decide, and that is yours and not mine. **The whole of the reasoning is at §6.0-70 item 5 and §5.47 direction 2, check 1.** Read with item 133.
"""


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def req(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(base() + path, data=data, method=method, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"],
        "X-Paperclip-Run-Id": os.environ.get("PAPERCLIP_RUN_ID", ""),
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(r) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main():
    # The item list must describe the bill as it actually stands, so check the bill first.
    st, bd = req("GET", f"/api/issues/{MOO42}/documents/{BILL}")
    assert st == 200, (st, bd)
    bb = bd["body"]
    i = bb.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", bb[i + 5:])
    s1 = bb[i:i + 5 + m.start()]
    rev = max(int(x) for x in re.findall(r"^### 0\.0-(\d+) ", bb, re.M))
    assert rev == 70, f"the bill is at store revision {rev}; these items are written for 70"
    # item 135's FIND, and the exception the re-scoped item 133 is written against
    f135 = ("or by a failure of the Board to state in a certification or notice a matter this "
            "section requires to be stated in it, may obtain")
    exc = (", other than a failure to state that the Board advises the member to review the "
           "member's designation of beneficiary,")
    assert s1.count(f135) == 1, f"item 135's FIND resolves {s1.count(f135)}x in §1"
    assert s1.count(exc) == 1, f"the enacted exception resolves {s1.count(exc)}x in §1"
    print(f"bill: store revision {rev}, §1 {len(s1)} chars | item 135 FIND 1x | exception 1x")

    st, doc = req("GET", f"/api/issues/{MOO42}/documents/{KEY}")
    assert st == 200, (st, doc)
    body, live = doc["body"], doc["latestRevisionId"]
    print(f"item list: revision {live} (number {doc.get('latestRevisionNumber')}), {len(body)} chars")

    for tag, f in (("133 head", OLD_HEAD), ("133 drafted", OLD_DRAFTED),
                   ("133 not-enacted", OLD_NOT_ENACTED)):
        assert body.count(f) == 1, f"item {tag}: found {body.count(f)}, expected 1"
    assert "\n135. " not in body, "item 135 already exists"
    assert body.count("\n134. **") == 1, "item 134 not found exactly once"

    out = body
    for f, r in ((OLD_HEAD, NEW_HEAD), (OLD_DRAFTED, NEW_DRAFTED),
                 (OLD_NOT_ENACTED, NEW_NOT_ENACTED)):
        out = out.replace(f, r, 1)
    # 135 goes after 134, which is the last item. Append at the end of the numbered list, which is
    # the end of the document as store revision 68 left it.
    assert out.rstrip().endswith(out.rstrip()[-1]), "unexpected"
    out = out.rstrip("\n") + "\n" + ITEM_135.rstrip("\n") + "\n"

    assert out.count("\n135. ") == 1
    assert len(out) < CEILING, f"over ceiling: {len(out)}"
    # nothing else answered or closed
    assert out.count("\n134. **") == 1
    print(f"item list {len(body)} -> {len(out)}  ({len(out) - len(body):+d}) | "
          f"headroom {CEILING - len(out)}")

    if "--dry-run" in sys.argv:
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out-items.md"),
             "w", encoding="utf-8").write(out)
        print("DRY RUN — nothing sent")
        return

    title = doc.get("title") or ""
    title = re.sub(r"items 1 to \d+", "items 1 to 135", title)
    st, res = req("PUT", f"/api/issues/{MOO42}/documents/{KEY}",
                  {"title": title, "format": "markdown", "body": out, "baseRevisionId": live})
    if st not in (200, 201):
        print(f"WRITE FAILED {st}: {str(res)[:400]}")
        sys.exit(2)
    assert res.get("body") == out, "returned body differs"
    print(f"WRITE OK — revision {res.get('latestRevisionId')} "
          f"(number {res.get('latestRevisionNumber')}), {len(res['body'])} characters")
    print(f"title: {res.get('title')}")


main()
