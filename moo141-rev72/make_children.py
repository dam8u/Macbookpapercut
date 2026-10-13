import json, os, sys, urllib.request, urllib.error
HERE = os.path.dirname(os.path.abspath(__file__))
RT = "d71e111e-1296-4d66-81ac-750dcc8d8681"       # Red Team / Counsel Reviewer
FIM = "428b53bf-f49e-4505-a607-3560a26b3d50"      # Fiscal & Impact Modeler
MOO164, MOO197 = "6ea24562-7d50-4025-9c4d-f119309cac33", "5bd82780-d999-433d-bd73-ee2c2b4c68a9"


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


PASS = """**Commissioned by the Policy Director on 13 October 2026. Bounded. One pass, not one per change.**

MOO-215's sixteen findings are all disposed of and MOO-141 is at **revision 9**, cut and verified at
**bill store revision 72**. Full record: `moo141-rev72-revision9` on MOO-141, and
`moo141-rev72/verify_r72.py` on `main` (`4a09350`). **ALL CHECKS PASS.**

**Why this pass exists.** Nine of the sixteen findings were cured in the text, and **I drafted every
one of those cures myself after MOO-215 named the defect.** That is exactly the condition that made
MOO-214 necessary for MOO-164's revision 7: the reviewer named it, the drafter cured it, and nobody
has read the cure adversarially. **Nothing in revision 9's new text has been read by anyone but me.**

## The four targets, and nothing else

**1. Edit 4 — the only wholly new provision, +268 characters, and the only edit in this patch that is
fully operative applied alone.**

> *"Where the member's final qualifying retirement date is determined by the preceding sentence, the
> Board shall give the member written notice of that date no later than 15 days after the expiration
> of the period for acting upon the request referred to in that sentence."*

Inserted immediately after the definition's expiry sentence and immediately before R-6. §4 of the
record sets out the gap it closes and five properties I claim for it. **Attack the properties, in this
order:** that it widens no chapeau and so cannot put the Board in breach of R-6's *"state the date in
its decision"* branch; that *"the preceding sentence"* and *"that sentence"* both resolve to the expiry
sentence and to nothing else, at this insertion point and after MOO-164's thirteen substitutions; that
it is 164-4-proof; that R-7's referent does not move; and **that subdivision D 1's lateness extension
does not reach it**, which is the claim that makes it fiscally inert and is the kind of claim MOO-215's
F8 was about.

**2. §3.2's structural claim, which is now load-bearing for a reversal of my own ruling.** I reversed
my 01:32 asymmetry ruling and gave Edit 1's exception R-6's notice duty. The reason it moves no date is
this: **both of 164-7's deeming predicates are no-act predicates, so the date 164-7 deems necessarily
precedes any real act of the Board upon the same request, so Edit 1's "first acts upon" rule selects
164-7's deemed date and the two deemings agree by construction.** MOO-215's F4 asserted they fix
different dates — 6 May and 20 June — and I say they cannot. **Find the case where they can**, or
confirm they cannot. Two routes worth trying first: a request on which the Board acts, then a deeming
operates on some other footing; and whether a deemed act is an act for Edit 1's purposes at all.

**3. The four-requirement cross-reference specification at §3.4.** MOO-215's F5 showed my three
requirements were jointly unsatisfiable and that requirement 1 misdescribed my own Edit 1. These four
replace them. **Are they sufficient, and are they jointly satisfiable?** Requirement 2 is the one to
attack: it asserts that stating *"a date deemed under subdivision M 2 to be a date on which the Board
acts is such a date for subsection A's deeming"* resolves no priority and chooses no date. **That
assertion is target 2 in another form, so if target 2 falls, this falls with it.**

**4. Edit 1's extended saving, and the one thing revision 9 asks of MOO-164.** The saving's enumeration
now reaches *"to restore or credit service credit, to recertify or settle a certified subsidy, or to
pay or include any amount"* (MOO-215's F7, which closes my open 17:26 finding of 12 October). Two
questions. **Does the new enumeration reach the three duty families as they are actually worded in the
bill** — *"restore or credit service credit"*, *"recertify and settle it accordingly"*, and the
payment limbs — or does *"recertify or settle"* against the bill's *"recertify and settle"* open a
*Forst* gap of my own making? **And does it reach anything it should not**, in particular any duty
whose date the deeming ought to fix.

## Three things I am asking you NOT to do

- **Do not re-open the board's answers.** Card (g)'s first limb is revision 6's text character for
  character and card (k-ii)'s 120 days are untouched. If you find a defect in either, report it as a
  finding with the board named as the owner — do not treat it as drafting.
- **Do not re-run MOO-215's sixteen findings.** They are disposed of at §0 of the record. If a
  disposition is wrong, that is a finding; a re-derivation of a finding already taken is not.
- **Do not draft into the patch.** Name the defect and the direction, as MOO-215 did. Its F1 was the
  most useful thing either pass has produced and it was one sentence of suggested direction.

## Counted facts you can rely on, and should check

Four anchors, each **exactly 1 in §1**; Edit 1's reads **2** whole-document because §5's own sweep
quotes it, so **a whole-document count is not a valid uniqueness test**. §1 is **134,012** characters,
sha256 `83a10b74950b5272…`, **byte-identical to store revision 71** — asserted in the kit, so
MOO-215's counts carry. Patch **+1,716** (Edit 1 +1,116, Edit 2 +317, Edit 3 +15, Edit 4 +268), in §1
and whole-document alike. `<u>` 62/62. Combined with MOO-164 revision 7: **+5,091**, order-independent
and byte-identical in either order.

**One check in the kit is designed to fail later and must not be "fixed":** the two saving bodies read
**(1, 1)** in the combined text and must read **(2, 0)** once MOO-164 takes the three duty families.
**And revision 8's defective class-1 wording is kept as a live assertion at 0, so MOO-215's F1 stays
visible in the record.**

**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared
by counsel. Pre-decisional. Nothing applied to the store.**"""

FISC = """**Opened by the Policy Director on 13 October 2026, on MOO-215's F8, which I accept in full.**

## What I got wrong, stated plainly, because it is the whole reason this issue exists

The MOO-141 patch creates a channel through which a member's **final qualifying retirement date** can
be extended under subdivision D 1 by the number of days a notice is late. I declined to open a
pricing issue on this ground:

> *"The 12-month aggregate cap is unmoved, so there is nothing to re-price."*

**That is a category error and it is withdrawn.** The cap is a bound **per member**. What drives cost
in MOO-163 is a **population** against a fixed $3,000,000 pool. An unmoved per-member cap says nothing
about how many members reach it.

**And I set a trigger that has now fired on its own terms:** the limb re-opens MOO-163 and the declined
F-6 cap *"if the bounded pass widens the limb beyond its two named classes."* MOO-215 widened it on
three independent grounds. I wrote the trigger and I am honouring it.

## The four questions

**Q1. The two missing inputs.** MOO-215 reports that of MOO-163's twenty levers, **none** touches
final-qualifying-retirement-date extension, notice lateness, or a Board no-act rate, and that the two
inputs needed to screen this channel exist in **no register in this project**:

- the **Board no-act rate** — the share of requests on which the Board does not act within the period
  allowed; and
- the rate at which **funded members file later-date requests** under the definition of *"final
  qualifying retirement date"*.

**Can they be sourced, bounded, or honestly declared unobtainable?** An express "cannot be screened on
existing inputs" is a usable answer and I would rather have it than a figure built on a guessed rate.

**Q2. Are MOO-163's $0 and MOO-170's $204,000 bound silent on this channel, or do they cover it?**
MOO-215's reading is that both price **queue ordering against a fixed pool** and therefore neither
covers nor excludes a D 1 extension channel. **If that is right, say so** — the consequence is that
"$0 on this limb" was an unpriced assertion rather than a counted one, which is what I need on the
record. MOO-170's bound was released as **analytic over any vector of ordering dates**, hence figure-
and length-independent; **an unbounded or extended retention is not a longer figure, it is the absence
of one**, so please state expressly whether the bound's ground survives this channel.

**Q3. Is Edit 4 fiscally inert, as I claim?** Edit 4 is new at revision 9 and adds a notice duty where
the Board does **not** act. I claim it carries **no** D 1 extension, and the ground is textual:
subdivision D 1 extends for *"any notice of a date required by that definition **upon**"* — or, after
MOO-164's 164-5, *"**by reason of**"* — *"the Board's **action** upon a request"*, and Edit 4's notice
is required by reason of the Board's **not** acting. **Test the claim on your model, not on my
reading.** If it holds, Edit 4 adds a duty and no cost.

**Q4. Price the option I did not take.** Because of Q3, Edit 4 gives the member the information and
**not the time**: if the Board is late with the Edit 4 notice she has no extension. **What would it
cost to attach a D 1 extension to the Edit 4 notice?** I have neither taken this nor carded it, and I
will not decide it on an unpriced basis. This is the one genuinely new policy option in the patch.

## Scoping you should not have to re-derive

- **The dominant class is class 2** — the definition request from the funded cohort, linear in the
  no-act rate. Class 1, the deemed denial under subdivision M 2, has **two independent no-act gates**
  and is quadratic in a small number: MOO-215 puts it at 0.038 members even at a 20% no-act rate.
  **My own earlier reasoning was about class 1, which is the negligible one.**
- **MOO-215's crossover is 15.6%** against MOO-170's own stated resolution of 2.80 members, and their
  class-2 column assumes **every** funded member files one later-date request, which over-counts. Their
  script is `moo215-adversarial/d1_channel_test.py` on `main` (`6a4b8e6`); it **imports** MOO-163's
  register and writes nothing to your files.
- **Do not condition the scoping on MOO-164's 164-5.** MOO-215's F12 is right: D 1's pre-164-5
  descriptor already tracks R-6's chapeau nearly word for word, so **this channel opens whether or not
  164-5 lands.** My ordering reason that said otherwise is withdrawn.
- **Neither MOO-215 nor I assert a non-zero figure.** The honest position is that the channel is
  probably immaterial at a plausible no-act rate and that the answer is currently **unknown rather
  than known to be zero**. A return at or near $0 with a stated basis is a complete answer.

## What turns on it

**This is a blocker edge on MOO-141 and a release gate.** The patch should not be applied while a
channel it widens is unpriced. **MOO-163 and the declined F-6 cap re-open only if you come back
non-zero**, on the same footing as the MOO-49 trigger. **Nothing here reopens the board's 120 days**
(answered 14:15 on 12 October 2026) or MOO-179's declined cap on my own motion.

Patch under test: **revision 9**, four edits, **+1,716** in enacted §1, cut at bill store revision 72.
Record: `moo141-rev72-revision9` on MOO-141, and `moo141-rev72/verify_r72.py` on `main` (`4a09350`).

**Internal working draft material. Not a DLS bill. Not reviewed by counsel. Pre-decisional. Nothing
applied to the store.**"""

if "--write" in sys.argv:
    out = {}
    for key, title, desc, agent, pri in (
        ("pass", "Bounded adversarial pass on MOO-141 revision 9 — Edit 4, the reversed asymmetry "
                 "ruling's structural premise, the four cross-reference requirements, and Edit 1's "
                 "extended saving", PASS, RT, "high"),
        ("fiscal", "Price the subdivision D 1 extension channel the MOO-141 patch opens — the Board "
                   "no-act rate, the later-date filing rate, Edit 4's claimed neutrality, and the "
                   "cost of attaching an extension to the Edit 4 notice", FISC, FIM, "medium")):
        st, res = req("POST", f"/api/companies/{os.environ['PAPERCLIP_COMPANY_ID']}/issues", {
            "title": title, "description": desc, "priority": pri, "status": "todo",
            "assigneeAgentId": agent, "parentId": os.environ["PAPERCLIP_TASK_ID"]})
        print(key, st, res.get("identifier") if isinstance(res, dict) else str(res)[:400])
        out[key] = {"id": res.get("id"), "identifier": res.get("identifier")} if isinstance(res, dict) else None
    json.dump(out, open(os.path.join(HERE, "children.json"), "w"), indent=1)

    ids = [MOO164, MOO197] + [v["id"] for v in out.values() if v and v.get("id")]
    st, res = req("PATCH", f"/api/issues/{os.environ['PAPERCLIP_TASK_ID']}", {
        "blockedByIssueIds": ids,
        "unblockDescriptor": {
            "owner": {"agentId": "705d4b07-92cb-4a50-80f8-fbfab9cccb27"},
            "action": (
                "Revision 9 is cut and verified at bill store revision 72 (four edits, +1,716 in "
                "enacted §1; record moo141-rev72-revision9; kit moo141-rev72/verify_r72.py, ALL "
                "CHECKS PASS). All sixteen MOO-215 findings are disposed of, so MOO-215's edge is "
                "dropped — it is done, and a done edge is a dead wake path. Four gates remain, all "
                "first-class blocker edges except gate 4. GATE 1 MOO-164: the joint cut carrying "
                "164-5 (F-9), 164-7, the §3.4 cross-reference and the five routed items at §8 — "
                "including 164-7's saving taking Edit 1's three new duty families byte for byte. "
                "GATE 2 MOO-197: store revision 66's four approved edits. GATE 3 the new bounded "
                "pass: nothing in revision 9 has been read adversarially, because MOO-215 named the "
                "defects and I drafted the cures. GATE 5 the new fiscal issue: the subdivision D 1 "
                "extension channel is unpriced and MOO-215's F8 showed my ground for not asking was "
                "wrong — the patch is not applied while a channel it widens is unpriced. GATE 4 is "
                "not an issue: whoever applies re-verifies all four MOO-141 anchors and all thirteen "
                "MOO-164 anchors §1-scoped at the base as it stands at that moment — a "
                "whole-document count is NOT a valid uniqueness test for Edit 1, and Edit 2 must be "
                "applied in the same cut as Edit 1. Then release the joint cut for application."),
        }})
    print("PATCH", st, res if isinstance(res, str) else res.get("identifier"))
