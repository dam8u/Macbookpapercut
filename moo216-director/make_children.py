"""MOO-216 — the Director's disposition: five child issues, and MOO-141's gates re-pointed.

Run once. Writes children.json beside this file. Idempotent only in the sense that re-running
creates duplicates — check children.json first.
"""
import json, os, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
DS = "0cfe7ee0-d4d4-45b3-8df8-3226f933990f"    # Drafting Specialist
FIM = "428b53bf-f49e-4505-a607-3560a26b3d50"   # Fiscal & Impact Modeler
SR = "d2a2feeb-989e-40ec-9cf6-496e7633daa6"    # Statutory Researcher
SA = "ddc8a420-e8bd-4e0d-b13f-5565264264c8"    # Stakeholder Analyst
PD = "705d4b07-92cb-4a50-80f8-fbfab9cccb27"    # Policy Director
MOO141 = "78f25976-b6f1-46e0-b4e8-0a3bc0688d28"
MOO164 = "6ea24562-7d50-4025-9c4d-f119309cac33"
MOO197 = "5bd82780-d999-433d-bd73-ee2c2b4c68a9"

DISCLAIM = ("\n\n**Internal working draft material. Not a Division of Legislative Services bill. "
            "Not reviewed or cleared by counsel. Pre-decisional. Nothing applied to the store.**\n")


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


DRAFT = """**Commissioned by the Policy Director on 13 October 2026, on MOO-216's disposition. The
policy choices are taken. These are drafting tasks, not questions.**

Full disposition: `moo216-disposition.md` on `main`. The pass: `moo216-counsel/moo216-adversarial.md`.
Base: bill store revision 72, document revision `368f5e41`, enacted §1 134,012, sha256
`83a10b74950b5272…`. Kits: `moo141-rev72/verify_r72.py` and `moo216-counsel/verify_216.py`, both
**ALL CHECKS PASS**.

**Revision 9 does not ship as cut.** Five drafting items make revision 10. Edit 2 and Edit 3 are
**unchanged** — do not touch the board's two answers (card (g)'s first limb, card (k-ii)'s 120 days).

## 1. Edit 4's trigger — re-key to the affirmative fact (R4, serious)

Edit 4 today triggers on *"Where the member's final qualifying retirement date **is determined by the
preceding sentence**"* — the **outcome** of the expiry sentence. The expiry sentence turns on *"the
date that would otherwise apply"*, which the Board can move later by granting the later date the
request asked for. **So a Board can defeat the duty retrospectively by acting late and granting:**
notice due 19 April, Board acts 20 June and grants 1 August, and the duty missed on 19 April was never
owed. That is MOO-215's F1 vice in the mirror, in the one provision revision 9 drafted fresh.

**Key it to the affirmative fact**, as F1's cure did: the Board's not having acted upon the request
within the period, in the expiry sentence's own class (*a request the filing of which tolled the
running of the member's final qualifying retirement date under subsection M*).

**One thing to report back on:** on the affirmative trigger the notice can state a date a later Board
grant supersedes. I read R-6's chapeau as picking that up on the later act. **If you read it
otherwise, that is a finding and it comes back to me.**

## 2. Edit 4's period reference — `that period` (R7, moderate)

*"…no later than 15 days after the expiration of the period for acting upon the request referred to in
that sentence."* Grammatically *"referred to in that sentence"* modifies **the request**, not **the
period**, and a reconsideration request has two candidate periods: M 2's 90 days (164-10) and the 30
days after the expiry notice is filed. Reconsideration requests are in the expiry sentence's class.

**Use the anaphor that was already in the words immediately before Edit 4:** *"…after the expiration of
**that period**."* One period, unambiguous, still 164-4-proof, 56 characters shorter, and it
strengthens property 3 rather than spending it.

## 3. Edit 1's saving — the enumeration goes, general words replace it (R5, serious)

Revision 9 extended a **closed** list to five families. That does not open it: on the *Forst* reasoning
this record uses throughout, it implies more strongly against the **nine** of subdivision M 2's
thirteen reviewable classes left outside and the **seven** further express Board duties outside both
lists. And M 2's *"for the purposes of this subsection"* limiter blocks the deemed route in — the same
four-word limiter designed out of Edit 2 on F10, load-bearing again inside Edit 1's saving.

**Replace the enumeration with general words:** the deeming does not determine the date by which the
Board is required to do **anything** under this section. No exception added, both carve-backs kept,
shorter than the enumeration, and the family closes permanently.

**And this cheapens the ask on MOO-164.** The revision-9 ask — 164-7's saving taking Edit 1's three
duty families byte for byte — is **replaced** by the same general words in **both** saving bodies.
Byte-identity of the two bodies is still the deliverable and now costs fewer characters.
`verify_r72.py` holds the two bodies at (1, 1) and expects (2, 0); **that check must be re-pointed to
the general words in revision 10's kit, not "fixed".**

## 4. Edit 4 comes inside three descriptors (R3 items i–iii, decided)

Edit 4 created a **fourth** date document attached to **none** of the definition's machinery. Three of
the six exclusions are decided and are yours to cut:

- **subdivision D 1's lateness enumeration** — so the lateness extension reaches Edit 4's notice. The
  price is known: MOO-217 priced this exact channel at **$11,000 central over 48 months**, range $610
  to $110,000, materiality threshold 94%, local cost $0.
- **D 1's companion later-effective-date right**, which rides in the same sentence and so comes with it.
- **164-13(a)'s disclosure duty** — information only, no date moves. 164-13(a) exists because MOO-209's
  F4 found the duty reached only two of three documents; letting a fourth escape would reproduce F4 in
  the cut that cures it.

**Not yours yet:** 164-13(b)(iv), 164-8's supersession, and an R-7-equivalent floor. Those three are
with the Fiscal & Impact Modeler as a bounded delta. **If the floor is bought, Edit 4's insertion point
must be revisited** — property 4 (R-7's referent) was secured positionally and would then need words.
Do not pre-empt that.

## 5. A base defect, low priority, no card (R9)

The bill's principal "include" provision is **actorless**: *"the next payment of the member's
retirement allowance **shall include** every amount by which the amounts paid to the member fall
short…"* — a property of the payment, imposing a duty on nobody. The bill supplies a Board duty only
for the no-payment-yet case. Base text, not patch text. **No gate, no card.**

## Constraints

- **Four anchors, resolved within enacted §1, each exactly 1. A whole-document count is NOT a valid
  uniqueness test for Edit 1** — it reads 2 because §5's own sweep quotes it.
- **Edit 2 must be applied in the same cut as Edit 1.**
- Re-verify at the base as it stands at the moment of cutting. The base has moved ten times under this
  item.
- **Do not touch the board's two answers.** If you think either needs to change, that is a finding to
  the board, not a drafting decision.
""" + DISCLAIM

XREF = """**Commissioned by the Policy Director on 13 October 2026, on MOO-216's disposition. This is
one defect from two sides, which is why it is one issue.**

Full disposition: `moo216-disposition.md` on `main` (§2). The pass: `moo216-counsel/moo216-adversarial.md`
(R1, R2, R6, R10). Base: store revision 72. Both kits **ALL CHECKS PASS**, and `verify_r72.py` now
carries six counted checks under `== MOO-216 R1` recording the base facts below.

## The defect, in the fewest words that are true

My §3.2 said 164-7's deemed date *"necessarily precedes any real act of the Board upon the same
request."* **For 164-7's limb 2 that is true. For limb 1 it is false.** M 2's predicate is *"does not
act upon the request **within 30 days after that notice is filed**"* — a **windowed** no-act predicate.
The window opens only when the filer files the expiry notice, and an act **before the window opens is
invisible to it**. The filing right is given on a condition stated as a completed fact and nothing
untrues it; the drafter writes an express continuing condition eleven lines earlier in the same
subdivision (*"at any time before the Board makes the determination"*) and did not here.

| | |
|---|---|
| 1 Mar | reconsideration filed |
| 30 May | the 90 days expire; no act |
| **2 Jun** | **the Board actually acts — one real act** |
| 5 Jun | the filer files the expiry notice |
| 6 Jul | request deemed denied; that denial *is* the final determination and a case decision |

**164-7 deems the Board to act, and to last act, on 6 July. Edit 1 deems it to act, and to last act, on
2 June. 34 days apart, no priority rule in either sentence.** And the other route out fails in the
opposite direction (R2): Edit 1's sentence is **not** a provision within 164-7's confinement clause —
it measures no period and fixes no date by month — so in the pure no-act case Edit 1's *"the date on
which the Board first acts upon it"* has **no referent**.

## Task 1 — the cross-reference, in two limbs, in 164-7

**Requirement 4 of the old specification has fired and this is my answer to it. The priority is
resolved expressly. Draft these two limbs and no more than they need.**

> **Limb 1 — the Board's own duties.** Where a period within which the Board is required to do anything
> under this section runs from the Board's acting, or last acting, upon a request, it runs from the
> **latest** of the dates on which the Board acts or is deemed by any provision of this section to act
> upon that request.
>
> **Limb 2 — the member's periods and clocks.** A date on which the Board is deemed under subdivision
> M 2 to act upon a request is a date on which the Board acts upon it for the purposes of subsection
> A's deeming **only where the Board does not in fact act upon the request**.

**Why limb 1:** a duty must never be capable of having been breached before the obligor could know it
was owed. On the scenario above R-6's deadline becomes **21 July** — where it sat before the reversal.
**Why limb 2:** it gives Edit 1 a referent in the pure no-act case (answering R2), and it stops a
deemed date competing with a real one, so **G 4's pendency window and M's tolling end on the same
day** — which is what MOO-141 exists to fix.

**The amended specification, five requirements replacing four:**

1. **Characterise neither deeming's scope.** No *"governs the case where…"*.
2. ~~Make them cumulative … resolving no priority and choosing no date.~~ **Withdrawn.** It does both.
3. **Resolve the priority expressly, in the two limbs above.**
4. **Add no exception. Move no member date and move no deadline of the Board earlier.**
5. **If it cannot be drafted inside 1, 3 and 4, that is a finding and it comes back to me.**

It goes in **164-7, not in Edit 1** — subsection A comes first, so the later sentence refers back
without a forward reference. **This is now a blocking ask on MOO-164, not a tidy-up.** It also disposes
of §3.2's "wrinkle" (164-7 deems a *last* act and a real act can follow it), so **that separate routing
to you is withdrawn.**

## Task 2 — the base repair in subdivision M 2 (R10)

M 2's deemed-denial sentence runs on a purely temporal condition, so **it can deem denied a
reconsideration the Board has actually decided, including one decided in the member's favour**, and the
deemed denial *is* the final determination and a case decision under § 2.2-4001. A member who won on
2 June loses by operation of law on 6 July because she filed the expiry notice on 5 June. **That is
R1's engine, it is base text neither patch amends, and repairing it is the cheapest cure for R1** — if
it lands, the scenario above disappears from the base.

**Direction:** a continuing condition, so the deeming cannot operate where the Board has acted at any
time before the 30 days expire.

**Owner and boundary.** The sentence is the enacted product of the board's **option (d)** at store
revision 63 (the member-triggered denial). A continuing-condition repair does **not** reverse option
(d); it repairs a gap inside it, so **no card goes to the board on my motion. If you judge that the
repair changes option (d)'s substance, that is a finding and it goes to the board, not to me.**

**Revision 10 must be safe on today's base regardless**, so task 1 lands whether or not task 2 does.
The two are not conditioned on each other.
""" + DISCLAIM

FISC = """**Commissioned by the Policy Director on 13 October 2026, on MOO-216's disposition (R3, R8).
A bounded delta, not a new model. Do not re-derive MOO-217.**

MOO-217 answered §5's question 4 and is **done**: attaching a subdivision D 1 extension to the Edit 4
notice is **$11,000 central over the whole 48-month pilot** at an illustrative 10% Board no-act rate,
range **$610 to $110,000**, materiality threshold **94%**, local cost **$0**, no dominant fiscal
assumption. **On that answer I have decided items i–iii and they are with the Drafting Specialist.**

**What MOO-216's R3 changed is the package, not the price of item i.** Edit 4's notice is a **fourth**
date document and it sits outside **six** machinery provisions, not one. Three remain unpriced:

| | Provision | What it gives the member |
|---|---|---|
| iv | **164-13(b)'s clause (iv)** | the § 51.1-153 notice-replacement right |
| v | **164-8's supersession right** | a route to file a conforming notice of retirement after a late Board document |
| vi | **an R-7-equivalent date floor** | **the only one of the six that can move a retirement date directly — price this hardest** |

## The three questions

1. **Does the $11,000 central and the 94% threshold change when the package is five provisions instead
   of one?** A delta on your existing model, with the switches you already named.
2. **Confirm that item ii rides inside item i's sentence at no separate cost** — D 1's companion
   later-effective-date right is in the same sentence as the lateness extension, so widening the
   enumeration brings both. If that is wrong, it is a decision I have taken on a false premise and I
   need to know.
3. **Use R8's zero-day floor as a given, and do not model a remedy.** The pass established it from the
   text: the member can reconsider the Board's failure to give the Edit 4 notice (a different *failure*,
   so M 2(i)'s no-second-request bar does not block it), **but** M 2(ii) caps all tolling at **120
   days** and the Edit 4 class has by definition already drawn on it — so **the floor of the self-help
   remedy is zero days.** It is the one quantity here already fixed by the text.

**My stated preference, so you are pricing a decision and not a blank:** all three in. Edit 4 as
drafted gives the member information and not time, and MOO-209's F1 is the harm that reasoning
produced last time. **Tell me what it costs; the choice stays mine.**
""" + DISCLAIM

STAT = """**Commissioned by the Policy Director on 13 October 2026, on MOO-216's disposition (R5).**

**What changed since the pass routed this to you: the enumeration goes either way.** I have adopted the
general-words direction unconditionally, so your answer no longer decides whether Edit 1's saving keeps
its list. **It decides how the memo states the residual risk**, and that is still worth having exactly
right.

## The question

Subdivision M 2 makes **thirteen** classes of Board action reviewable: *"Every determination,
certification, redetermination, recertification, reduction, cancellation, rescission, restoration,
crediting of service credit, placement on a waiting list, expiration of a reservation, denial of an
election, and refusal to accept an election under this section is a determination of the Board **for
the purposes of this subsection**."*

Revision 9's saving reached **four** by name. **Nine were outside it.** And the pass reads the
four-word limiter *"for the purposes of this subsection"* as blocking the deemed route in, so that
those thirteen are not "determinations" for the purposes of a saving that sits in **subsection A**.

**Is the limiter as confining as that?** Specifically: does it prevent an action M 2 deems a
determination *for its own purposes* from being a determination for the purposes of a provision in
subsection A? Authority and the contrary case both, please.

**Why it matters beyond the memo.** This is the **same limiter** I designed out of Edit 2's class 1 on
MOO-215's F10 as load-bearing and undisclosed — and it had become load-bearing again inside Edit 1's
saving, undisclosed, one revision later. If your answer is that it does **not** confine, then the
general words are belt-and-braces and the memo says so; if it does confine, the memo carries it as a
residual risk the general words close.

**Also still live and unchanged: F2's register question** — *decision* against *determination* in
R-6's deadline. **If *determination* is right, it changes the board's decided text and it comes back to
the board, not to me.**
""" + DISCLAIM

STAKE = """**Commissioned by the Policy Director on 13 October 2026, on MOO-216's disposition (R10).**

The **state agency from whose appropriation an amount was paid on a member's behalf** has express
standing in §1 and is a named person in subdivision M 2. MOO-215's F1 put it on the map as the litigant
in a scenario that **F1's cure then removed from the patch**. MOO-216's R10 gives it a second,
independent scenario — and **this one survives, because it lives in the base and neither patch amends
it.**

## The scenario

M 2's deemed-denial sentence runs on a purely temporal condition. So it can deem denied a
reconsideration the Board has **actually decided**, including one decided in the member's favour, and
the deemed denial *"constitutes the final determination of the Board upon the reconsideration and a
case decision as defined in § 2.2-4001."*

| | |
|---|---|
| 30 May | the Board's 90 days expire without an act |
| **2 Jun** | **the Board decides the reconsideration — in the member's favour** |
| 5 Jun | the filer files the expiry notice (the condition was satisfied on 30 May) |
| 6 Jul | the request is **deemed denied**, and that denial is the final determination |

**A member who won on 2 June loses by operation of law on 6 July because she filed the expiry notice on
5 June.** The agency's exposure runs the other way too: an amount paid on her behalf, and a
determination it relied on, displaced without adjudication.

## What I am asking for

1. **Where this lands on the stakeholder map** — the agency, the member, VRS, and the Board as
   administrator — in the form the map already uses.
2. **Who notices it first in a committee setting**, and whose question it is likely to be.
3. **Whether the agency's interest here is aligned or opposed to the member's.** My reading is aligned
   on the remedy and opposed on who bears the cost, but that is a guess and it is your field.

**Not asked:** whether to repair it. That is routed to the Drafting Specialist with me as the decision
owner (a continuing-condition repair inside the board's option (d), with a card to the board only if the
repair changes option (d)'s substance).
""" + DISCLAIM

if __name__ == "__main__":
    out = {}
    specs = (
        ("draft", "Revision 10's drafting items on MOO-216's disposition — Edit 4's affirmative "
                  "trigger, `that period`, general words for Edit 1's saving, and Edit 4 inside D 1 "
                  "and 164-13(a)", DRAFT, DS, "high"),
        ("xref", "The cross-reference in two limbs, and the subdivision M 2 base repair that is R1's "
                 "engine — one defect from two sides", XREF, DS, "high"),
        ("fiscal", "Bounded fiscal delta on MOO-216 R3 — does MOO-217's $11,000 central move when the "
                   "Edit 4 package is five provisions instead of one?", FISC, FIM, "medium"),
        ("stat", "Does M 2's \"for the purposes of this subsection\" limiter confine its thirteen "
                 "reviewable classes against a saving in subsection A?", STAT, SR, "medium"),
        ("stake", "The state agency as litigant in MOO-216's R10 — a deemed denial displacing a real "
                  "determination in the member's favour", STAKE, SA, "medium"),
    )
    for key, title, desc, agent, pri in specs:
        st, res = req("POST", f"/api/companies/{os.environ['PAPERCLIP_COMPANY_ID']}/issues", {
            "title": title, "description": desc, "priority": pri, "status": "todo",
            "assigneeAgentId": agent, "parentId": os.environ["PAPERCLIP_TASK_ID"]})
        print(key, st, res.get("identifier") if isinstance(res, dict) else str(res)[:300])
        out[key] = {"id": res.get("id"), "identifier": res.get("identifier")} if isinstance(res, dict) else None
    json.dump(out, open(os.path.join(HERE, "children.json"), "w"), indent=1)

    gates = [MOO164, MOO197] + [out[k]["id"] for k in ("draft", "xref", "fiscal") if out.get(k)]
    st, res = req("PATCH", f"/api/issues/{MOO141}", {
        "blockedByIssueIds": gates,
        "unblockDescriptor": {
            "owner": {"agentId": PD},
            "action": (
                "MOO-216's bounded pass is disposed of (moo216-disposition.md on main) and REVISION 9 "
                "DOES NOT SHIP AS CUT. R1 is fatal: subdivision M 2's deemed-denial predicate is "
                "WINDOWED, so 164-7's deemed date does not necessarily precede a real act, and the "
                "two deemings fix dates 34 days apart on one real act. §3.2's premise and §3.3's "
                "'moves no date' are withdrawn; the reversal of the asymmetry ruling stands on §3.1 "
                "alone and the priority is now resolved expressly in two limbs (disposition §2.3). "
                "Nothing was applied to the store, so nothing is rolled back. GATE 1 MOO-164: the "
                "joint cut, now carrying the two-limb cross-reference as a BLOCKING ask and general "
                "words in both saving bodies instead of three duty families. GATE 2 MOO-197: store "
                "revision 66's four approved edits. GATE 3 (the bounded pass) is DISCHARGED. GATE 5 "
                "MOO-217 is done and answered ($11,000 central, 94% threshold, local $0) — what "
                "replaces it is the bounded delta on R3 items iv-vi. NEW GATES: revision 10's "
                "drafting items, and the cross-reference plus the M 2 base repair. GATE 4 is not an "
                "issue: whoever applies re-verifies all four MOO-141 anchors and all thirteen MOO-164 "
                "anchors §1-scoped at the base as it stands at that moment — a whole-document count "
                "is NOT a valid uniqueness test for Edit 1, and Edit 2 must be applied in the same "
                "cut as Edit 1. Then the Director cuts revision 10 and commissions one bounded pass "
                "over it on the same terms as MOO-216."),
        }})
    print("PATCH MOO-141", st, res if isinstance(res, str) else res.get("identifier"))
