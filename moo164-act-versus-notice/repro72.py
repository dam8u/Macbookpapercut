# -*- coding: utf-8 -*-
"""Re-splice the §6 reproductions from `bill-text-s8` at **store revision 70** for **revision 7**
of the MOO-164 cut. Supersedes repro68.py.

Why re-splice. Store revision 69 rewrote **subdivision G 4**; store revision 70 — the Policy
Director's MOO-191 composite out of MOO-208 — made six substitutions, **four of them inside
subdivision D 1** and one in the **title line**. Both provisions are reproduced at §6, so §6 was
stale for the **eighth** time behind anchors that all still resolved exactly once. Every provision is
located **by content, not by line index**.

What changed in the reproduced text itself, all of it MOO-209's counsel findings folded:

  * **164-7** takes F1's extended exception — it now names R-6's notice duty as well as M 2's.
  * **164-8** takes F2 (the `satisfies § 51.1-153` surplusage deleted) and F3 (the supersession
    confined to the member's own notice of retirement, with a post-retirement bar).
  * **164-12** takes F6 — the notwithstanding deleted, G 4's definition being already confined.
  * **164-13** is new: F4's conforming disclosure amendment, in two substitutions inside one
    sentence of D 1.

Markup convention, unchanged across all seven revisions of this cut: the store document already
wraps the bill's own new language in `<u>`/`</u>`. Inside a reproduction, **bold** is this cut's
proposed new language, ~~strikethrough~~ is language it deletes, and ***bold italic*** is the
MOO-141 patch's language, so a reader can see whose words are whose.

Writes repro72.json. Nothing is written to the store.

Run: python3 repro72.py      (reads bill72.md)
"""
import json
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'bill72.md'
head = open(SRC, encoding='utf-8').read()
i = head.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', head[i + 5:])
sec1 = head[i:i + 5 + m.start()]
LINES = [l.strip() for l in sec1.split('\n') if l.strip()]


def line(prefix):
    """The one §1 line whose text, with <u> and ** stripped, starts with prefix."""
    hits = [l for l in LINES if re.sub(r'<u>|\*\*', '', l).startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0]


def mark(text, subs):
    for f, r in subs:
        assert text.count(f) == 1, ('not unique', f[:70], text.count(f))
        text = text.replace(f, r, 1)
    return text


# --- 1. subsection A interpretation paragraph. NOT amended by this cut -------------------------
# Reproduced because MOO-141 Edit 1 lands here and because the three facts behind Edit 164-1's
# 48-day route table are in it. The bold-italic insertion is MOO-141's re-cut Edit 1 at store
# revision 69, saving clause and express exception included; it is theirs, not ours.
A = mark(line('For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, a written statement'), [(
    "every period within which a person may or must act that runs from the giving of that statement, notice, or certification is extended by three days.</u>",
    "every period within which a person may or must act that runs from the giving of that statement, notice, or certification is extended by three days. ***For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Except for the purposes of the duty of the Board under subsection M to act upon an application no later than 15 days after it acts upon the request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.***</u>")])

# --- 2. definition of "final qualifying retirement date" — Edit 164-4 + MOO-141 Edit 2 ----------
DEF = mark(line('"Final qualifying retirement date" means the date that is 12 months'), [
    ("within the period this definition allows for acting upon it",
     "within the period ~~this definition allows~~ **allowed by this section** for acting upon it"),
    # R-6. MOO-141 Edit 2 re-keys this duty off the Board's act. That is why Edit 164-7's new
    # exception (F1) identifies the duty and not its deadline formula — and why the cure goes inert
    # once Edit 2 lands. §17.3 and question 3.
    ("no later than 15 days after it acts upon the request.",
     "no later than 15 days after ~~it acts upon~~ ***it gives its decision upon*** the request***, except that where the request is denied otherwise than by a decision of the Board upon it, or where the period allowed by this section for acting upon the request expires without the Board's acting upon it, it shall give that notice no later than 15 days after the date on which the Board acts upon the request***."),
])

# --- 3. subdivision D 1 — Edits 164-5, 164-8 and 164-13 ----------------------------------------
# Store revision 70 rewrote four places in this subdivision (the certification series' new item 7,
# the subsection M exception, the subsection J limb, and the series' "and"). None of them is a site
# of this cut, and none moved an anchor; the reproduction is re-taken anyway because it is stale.
D1 = mark(line('D. 1. The Board shall not accept an election'), [
    # Edit 164-5 — card (k) / F-9: the lateness sentence's third descriptor.
    ("any notice of a date required by that definition upon the Board's action upon a request",
     "any notice of a date required by that definition ~~upon~~ **by reason of** the Board's action upon a request"),
    # Edit 164-8 — the filing vehicle, RE-CUT at revision 7 on MOO-209 F2 and F3.
    ("the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
     "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. **Where the Board gives any notice of a kind described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member, except that no notice may be filed under this sentence after the member has retired.**"),
    # Edit 164-13(a) — F4: the disclosure duty reaches the third document.
    ("The Board shall state, in the written statement required by that definition and in every notice of a later approved date required by that definition, (i)",
     "The Board shall state, in the written statement required by that definition**,** ~~and~~ in every notice of a later approved date required by that definition, **and in every notice of a date required by that definition by reason of the Board's action upon a request,** (i)"),
    # Edit 164-13(b) — F4: clause (iv).
    ("; and (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days.",
     "**;** ~~and~~ **(iii)** that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days**; and (iv) that where the Board gives a notice of a kind described in this sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153 and the member has not retired, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives that notice, and that a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member**."),
])

# --- 4. subdivision G 2 — Edit 164-2 + Edit 164-12, which is candidate (c-2) --------------------
G2 = mark(line('2. If the member does not retire in a qualifying retirement'), [
    ("or has not given it within 60 days after the determination date, the determination takes effect on the first day",
     "or has not given it within 60 days after the determination date, **or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect,** the determination takes effect on the first day"),
    # Edit 164-12 — RE-CUT at revision 7 on MOO-209 F6: the notwithstanding is deleted.
    ("and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.",
     "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. **For the purposes of this subdivision, an application of the member for a disability retirement allowance under this chapter is pending from the date on which the member files it until the date on which the Board grants or denies it.**"),
])

# --- 5. G 4 suspension and pendency passage — Edit 164-6; (c-1) is NOT applied ------------------
# Store revision 69 rewrote this passage (the retirement-before-death carve-out and the
# § 51.1-162 B benefit conditioned on identity of payees), so it is re-taken by content.
s = sec1.find('The Board shall not make a determination under subdivision 2, and shall not give the notice required by subdivision 2, while an application')
k = 'such a request is pending from the date on which the member files it until the date on which the Board first acts upon it.'
e = sec1.find(k, s) + len(k)
assert s > 0 and e > s, (s, e)
G4 = sec1[s:e].replace('’', "'")   # apostrophes normalised, per §8
G4 = mark(G4, [
    ("within the period allowed to it for acting upon the request shall not extend that aggregate",
     "within the period ~~allowed to it~~ **allowed by this section** for acting upon the request shall not extend that aggregate"),
])

# --- 6. subsection M 1, 2, 3 -------------------------------------------------------------------
M1 = line('M. 1. The Board shall adopt and publish')
M2 = mark(line('2. A member, retiree, beneficiary, applicant, personal representative'), [
    # Edit 164-10 — F6: give M 2's 90-day duty a commencement.
    ("The Board shall act upon a request for reconsideration within 90 days.",
     "The Board shall act upon a request for reconsideration within 90 days **after the request is filed**."),
    # Edit 164-11 — F12: conform the enacted expiry-notice sentence's period formula.
    ("Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file",
     "Where the Board does not act upon a request for reconsideration within ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request**, the person who filed the request may file"),
    # Edit 164-7 — route (c), two triggers, RE-CUT at revision 7 on MOO-209 F1.
    ("and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
     "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. **Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of \"final qualifying retirement date\" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. Except for the purposes of the duty of the Board under this subsection to act upon an application no later than 15 days after it acts upon the request and the duty of the Board under the definition of \"final qualifying retirement date\" in subsection A to give a notice of a date required by that definition by reason of the Board's action upon a request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section. The Board is not deemed by this subsection to have stated a member's final qualifying retirement date in a decision upon a request. The provision of this subsection deeming the Board to act upon a request applies where the Board does not act upon the request, and neither limits nor is limited by any provision of this section deeming the Board to act upon a request, and to last act upon it, on the date on which the Board first acts upon it, which applies where the Board acts upon a request more than once; the two provisions apply cumulatively, and neither is the exclusive rule for determining the date on which the Board acts upon a request.**"),
    # Edit 164-1 — card (b): the tolling endpoint.
    ("until 30 days after the Board acts upon the request, except that (i)",
     "until 30 days after the Board **gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board** acts upon the request **and in no case later than 48 days after the Board acts upon the request**, except that (i)"),
    # Edit 164-3 — card (j): clause (ii)'s stranded formula.
    ("excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
     "excluding any period after the expiration of ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request** and before the Board acts upon the request"),
    # MOO-141 patch Edit 3, at its revision 6 — 120 days.
    ("retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request",
     "retains its filing date for the purposes of subdivisions D 4 and D 5 until ***120 days after*** the Board acts upon the request"),
])
M3 = line('3. The sentence of subsection B of § 2.2-4021')

# --- 7. the title line, reproduced because store revision 70 amended it ------------------------
TITLE = line('A BILL to amend and reenact')
ENACT = line('Be it enacted by the General Assembly of Virginia:')
ENACT1 = line('1. That §§ 51.1-142.2 and 51.1-162 of the Code of Virginia are amended and reenacted')

out = {'A': A, 'DEF': DEF, 'D1': D1, 'G2': G2, 'G4': '> ' + G4,
       'M1': M1, 'M2': M2, 'M3': M3,
       'TITLE': TITLE, 'ENACT': ENACT, 'ENACT1': ENACT1}
json.dump(out, open('repro72.json', 'w'), ensure_ascii=False)
for k2, v in out.items():
    print(f'{k2:6s} {len(v):7d}')
print('store revision 72 §1 length', len(sec1))

# ---------------------------------------------------------------- post-conditions
# MOO-214 S5's lesson applied to the splicer: a mark() whose FIND does not match raises, but a
# re-cut that never reached this file would pass silently. Each revision-8 text is asserted present
# once, and each superseded form absent everywhere.
_bad = 0
for _lbl, _k, _frag in [
    ('MOO-141 Edit 2 rev 8 residual limb', 'DEF', 'except that where the request is denied otherwise than by a decision of the Board upon it'),
    ('164-8 S1 "of a kind"', 'D1', 'any notice of a kind described in the preceding sentence'),
    ('164-8 m1 bar', 'D1', 'after the member has retired.**'),
    ('164-13(b) S2 trigger', 'D1', 'and the member has not retired, the member may file'),
    ('164-13(b) M1 limbs', 'D1', 'and that a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member**'),
    ('164-12 M3 noun phrase', 'G2', 'an application of the member for a disability retirement allowance under this chapter is pending from the date'),
    ('164-7 S3 descriptor', 'M2', "to give a notice of a date required by that definition by reason of the Board's action upon a request"),
    ('164-7 m2 sentence', 'M2', 'The Board is not deemed by this subsection to have stated'),
    ('164-7 §3.3 cross-reference', 'M2', 'the two provisions apply cumulatively'),
]:
    _n = out[_k].count(_frag)
    _bad += 0 if _n == 1 else 1
    print(f'  [{"ok" if _n == 1 else "FAIL"}] revision-8 text present once — {_lbl}: {_n}')
for _frag in ["the member's retirement has taken effect",
              "give the member written notice of the member's final qualifying retirement date",
              'such an application is pending from the date',
              'any notice described in the preceding sentence',
              'a notice described in this sentence']:
    _n = sum(v.count(_frag) for v in out.values())
    _bad += 0 if _n == 0 else 1
    print(f'  [{"ok" if _n == 0 else "FAIL"}] superseded form absent — {_frag[:58]}: {_n}')
print(f'{_bad} splice post-condition failure(s)')
sys.exit(1 if _bad else 0)
