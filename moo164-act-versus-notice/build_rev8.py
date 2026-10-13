# -*- coding: utf-8 -*-
"""Assemble MOO-164 **revision 8** of `moo164-act-versus-notice` from revision 7.

Every edit below is asserted for an exact occurrence count before it is made, so a correction that
silently matches nothing — or matches twice — fails the build instead of shipping.

The four re-cut substitutions are replaced by swapping **the whole revision-7 READ string for the
whole revision-8 READ string**, taken from the two verifiers rather than retyped. That is MOO-214
S5's lesson applied to the build: a document edit expressed as a whole-block swap cannot leave half
a superseded text behind, and the before/after strings cannot drift from the kit.

Inputs : moo164_rev7.md (fetched), repro72.json (the live splice), sec18.md (revision 8's section),
         verify_r70_v7.py and verify_r72_v8.py (the two edit tables)
Output : moo164_rev8.md

Run: python3 build_rev8.py
"""
import importlib.util
import json
import os
import re
import sys


def load(name, base):
    spec = importlib.util.spec_from_file_location(name, name)
    mod = importlib.util.module_from_spec(spec)
    argv, out = sys.argv, sys.stdout
    sys.argv, sys.stdout = [name, base], open(os.devnull, 'w')
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    finally:
        sys.stdout.close()
        sys.argv, sys.stdout = argv, out
    return mod


V7 = load('verify_r70_v7.py', 'bill70.md')
V8 = load('verify_r72_v8.py', 'bill72.md')
assert V8.fail == 0, f'verify_r72_v8.py reports {V8.fail} failure(s)'
OLD = {lbl.split(' ')[0]: (f, r) for lbl, f, r in V7.EDITS}
NEW = {lbl.split(' ')[0]: (f, r) for lbl, f, r in V8.EDITS}
assert set(OLD) == set(NEW), (set(OLD) ^ set(NEW))

doc = open('moo164_rev7.md', encoding='utf-8').read()
R = json.load(open('repro72.json'))
S18 = open('sec18.md', encoding='utf-8').read()
start_len = len(doc)
log = []


def sub(label, old, new, count=1):
    global doc
    got = doc.count(old)
    assert got == count, f'{label}: expected {count} occurrence(s), found {got}'
    doc = doc.replace(old, new)
    log.append(f'  [{count}x] {label}')


# ============================================================ 1. the four re-cut substitutions
# Order matters: §6's reproductions are re-spliced wholesale from repro72.json FIRST, so the
# marked-up copies of the superseded texts leave with them and what remains to swap is §3's fences
# and the §4/§13 record quotations. Each swap is then a WHOLE-READ or WHOLE-TAIL swap taken from
# the two verifiers rather than retyped, and the post-condition is that **no** superseded fragment
# survives anywhere in the document.
KEYS = {'6.1': ['A'], '6.2': ['DEF'], '6.3': ['D1'], '6.4': ['G2'], '6.5': ['G4'],
        '6.6': ['M1', 'M2', 'M3']}
i6 = doc.index('\n### 6.1 ')
j6 = doc.index('\n## 7. ')
s6 = doc[i6:j6]
new6 = ''
hs = [(mm.start(), mm.group(0)) for mm in re.finditer(r'\n### 6\.[0-9][^\n]*', s6)]
new6 += s6[:hs[0][0]]
for n, (pos, h) in enumerate(hs):
    end = hs[n + 1][0] if n + 1 < len(hs) else len(s6)
    body = s6[pos:end]
    num = h.strip().split()[1]
    lines = body.split('\n')
    idx = [k for k, l in enumerate(lines) if l.startswith('<u>') or l.startswith('> ')]
    assert idx, num
    assert len(idx) == len(KEYS[num]), (num, len(idx), len(KEYS[num]))
    for k, key in zip(idx, KEYS[num]):
        lines[k] = R[key]
    new6 += '\n'.join(lines)
    log.append(f'  §{num} re-spliced from store revision 72 ({", ".join(KEYS[num])})')
doc = doc[:i6] + new6 + doc[j6:]


def swap(tag, label, old_s, new_s, require=1):
    """Replace every occurrence of a superseded text and report how many. `require` is the minimum
    the build insists on; the real guard is the zero-superseded-fragment assertion below, which no
    partial quotation can slip past."""
    global doc
    got = doc.count(old_s)
    assert got >= require, f'{tag} {label}: expected at least {require}, found {got}'
    doc = doc.replace(old_s, new_s)
    log.append(f'  [{got}x] {tag} — {label}')


for tag in ('164-7', '164-8', '164-13(b)', '164-12'):
    of, orr = OLD[tag]
    nf, nr = NEW[tag]
    assert of == nf, f'{tag}: the FIND moved between revisions — that is a re-anchor, not a re-cut'
    swap(tag, 'whole READ block', orr, nr)
    if orr.startswith(of) and nr.startswith(nf):
        swap(tag, 'READ tail, where the document quotes the new text alone',
             orr[len(of):].strip(), nr[len(nf):].strip(), require=0)
    assert doc.count(nf) >= 1, tag

# §13.7 records candidate 164-7 as first drafted at revision 5 — a different FIND, no limb (B) —
# and its saving carries the same superseded exception. The exception alone is swapped there, so
# the document nowhere states a descriptor the cut no longer uses. Listed at §18.14 item 1.
swap('164-7', "the exception, where §13.7 records the candidate as first drafted",
     V7.E164_7_EXC, V8.E164_7_EXC)

sub('§3.12 — bullets 2 and 3 re-cut on S2, M1 and S1',
    '2. **Clause (iv) discloses the limit as well as the right** — *"and that no such notice may be filed\n   after the member\'s retirement has taken effect"*, which is Edit 164-8\'s own F3 bar. Clause (i)\n   already discloses its own limits (*"subject to the limits stated in that definition"*), and **a\n   disclosure that overstates a right is worse than no disclosure**, because the member relies on it.\n3. **It says *"a notice described in this sentence"* and not *"the preceding sentence."*** The',
    '2. **RE-CUT AT REVISION 8 ON [MOO-214](/MOO/issues/MOO-214) S2 AND M1. Clause (iv) states the\n   disqualifying condition in its TRIGGER and the right in full.** Revision 7 disclosed the window\n   first and the bar after the grant — and for the member whose retirement has already taken effect,\n   which is most of the class that gets a late notice at all, the window described was closed on the\n   day it was written. The condition is now *"and the member has not retired"*, inside the *"where"*.\n   And clause (iv) now carries the two limbs revision 7 omitted — that a notice so filed **is filed\n   within the period allowed by this subdivision** and **supersedes** the member\'s earlier notice —\n   because supersession is the whole benefit and a member who cannot tell whether her replacement\n   notice wins will rationally do nothing. **A disclosure that overstates a right is worse than no\n   disclosure; one that understates it is worse still, because she acts on it.** §18.2.\n3. **It says *"a notice of a kind described in this sentence"* and not *"the preceding sentence."*** The')

sub('§17.4 — clause (iv) as quoted in the revision-7 narrative, re-cut',
    "> ~~; and~~ **<u>;</u>** (iii) that where the Board mails the statement or notice, every period that\n> runs from the giving of it is extended by three days**<u>; and (iv) that where the Board gives a\n> notice described in this sentence after the expiration of the period allowed by this subdivision\n> for filing the notice of retirement required by § 51.1-153, the member may file that notice of\n> retirement, or a notice replacing a notice of retirement already filed by the member, no later than\n> 30 days after the Board gives that notice, and that no such notice may be filed after the member's\n> retirement has taken effect</u>**.\n\n**+454 characters. Edit 164-13 totals +557 across two substitutions.**",
    '> ~~; and~~ **<u>;</u>** (iii) that where the Board mails the statement or notice, every period that\n> runs from the giving of it is extended by three days**<u>; and (iv) that where the Board gives a\n> notice of a kind described in this sentence after the expiration of the period allowed by this\n> subdivision for filing the notice of retirement required by § 51.1-153 and the member has not\n> retired, the member may file that notice of retirement, or a notice replacing a notice of\n> retirement already filed by the member, no later than 30 days after the Board gives that notice,\n> and that a notice so filed is filed within the period allowed by this subdivision and supersedes\n> any notice of retirement previously filed by the member</u>**.\n\n**RE-CUT AT REVISION 8 on [MOO-214](/MOO/issues/MOO-214) S1, S2 and M1: +564 characters; Edit 164-13\ntotals +667 across two substitutions.** It was +454 and +557 at revision 7. §18.2.')

sub('§3.12 — the false subsection J consequence, corrected (S4)',
    '***Who, what, by when, or else:*** the actor is the **Board**, the object is **four statements**, the\noccasion is **each of three documents**, and the consequence is **subsection J\'s report**, which reaches\n*"every failure … to state a matter this section requires to be stated."* No new reporting words are\nneeded and none are added — §7.3.',
    '***Who, what, by when, or else:*** the actor is the **Board**, the object is **four statements**, and\nthe occasion is **each of three documents**. **THE "OR ELSE" IS CORRECTED AT REVISION 8 ON\n[MOO-214](/MOO/issues/MOO-214) S4.** Revision 7 said the consequence was subsection J\'s report,\n*"which reaches \'every failure … to state a matter this section requires to be stated.\'"* **That\nphrase is not in subsection J. Counted: *"failure to state"* 0, *"requires to be stated"* 0.** The\nconsequence is what the base actually supplies: **a failure to state clause (iv) in a *notice* is\nreviewable under subsection M 2**, whose trigger reaches *"a certification or notice"*; **a failure to\nstate anything in the *written statement* is reviewable nowhere, and is in no report.** Candidate\n**164-17** would supply the route; it is drafted and **held**. §18.8, question 2.')
sub('§17.4 — the same false consequence, withdrawn (S4)',
    '**Who, what, by when, or else:** the actor is the Board, the object is the\nfour statements, the occasion is each of three documents, and the consequence is J 1\'s report, which\nreaches *"every failure … to state a matter this section requires to be stated."*',
    '**Who, what, by when, or else:** the actor is the Board, the object is the\nfour statements, and the occasion is each of three documents. **The consequence stated here is\nWITHDRAWN at revision 8 — the phrase attributed to J 1 is not in subsection J, counted 0. §18.8.**')

# After the swaps, no superseded fragment of the four re-cut texts may survive anywhere.
for stale in ["give the member written notice of the member's final qualifying retirement date",
              'any notice described in the preceding sentence',
              'a notice described in this sentence',
              "the member's retirement has taken effect",
              'such an application is pending from the date on which the member files it',
              'no such notice may be filed']:
    n = doc.count(stale)
    assert n == 0, f'superseded fragment survives {n} time(s): {stale!r}'
log.append('  [0x] every superseded fragment of the four re-cut texts is gone from the document')

# ============================================================ 2. the figures the re-cuts move
sub('§3 table — 164-7', '| **+1,337** |', '| **+2,004** |')
sub('§3 table — 164-8', '| **+621** |', '| **+613** |')
sub('§3 table — 164-13(b)', '| **+454** |', '| **+564** |')
sub('§3 table — 164-12', '| **+167** |', '| **+233** |')
sub('§3 table — total', '| | | **total** | **+3,375** |', '| | | **total** | **+4,210** |')

sub('§3.7 — 164-7 re-measured at revision 8',
    '**RE-MEASURED AT REVISION 7: 245 words, +1,337 characters**',
    '**RE-MEASURED AT REVISION 8: 372 words, +2,004 characters** — of which **S3**\'s determinate '
    'descriptor is +19, **m2**\'s sentence +132, and the Policy Director\'s MOO-141 §3.3 '
    'cross-reference +516. It was 245 words and +1,337 at revision 7')
sub('§3.8 — 164-8 re-measured at revision 8',
    '**RE-MEASURED AT REVISION 7: 97 words, +621 characters**',
    '**RE-MEASURED AT REVISION 8: 106 words, +613 characters** — **S1** adds ten characters and '
    '**m1** takes eighteen out, so the edit is again shorter as well as more correct. It was 97 '
    'words and +621 at revision 7')
sub('§3.11 — 164-12 re-measured at revision 8',
    '**RE-MEASURED AT REVISION 7: 30 words, +167 characters**',
    '**RE-MEASURED AT REVISION 8: 41 words, +233 characters**, **M3**\'s noun phrase written out. '
    'It was 30 words and +167 at revision 7')
sub('§3.12 — 164-13 re-measured at revision 8',
    '**+454 characters. Edit 164-13 totals +557 across the two substitutions.**',
    '**RE-MEASURED AT REVISION 8: +564 characters; Edit 164-13 totals +667 across the two '
    'substitutions.** **S2** moves the bar into the trigger and **M1** adds the timeliness deeming '
    'and the supersession, which revision 7 omitted. It was +454 and +557 at revision 7. §18.2.')

sub('§3 lead — the revision-8 counts and base',
    'Each is counted over §1 of **store revision 70**, and each is counted **three\ntimes** — on the base as it stands, on the base with the MOO-141 patch at **revision 5**, and on it with\nthe patch at **revision 6** (Edit 3 at 120 days). **All thirty-nine counts are 1, and the delta is\n+3,375 on all three bases.** `verify_r70_v7.py` reports **0 failures**',
    'Each is counted over §1 of **store revision 72**, and each is counted **three\ntimes** — on the base as it stands, on the base with the MOO-141 patch carrying Edit 3 at **30 days**,\nand on it with Edit 3 at **120 days**. **RESTATED AT REVISION 8: all thirty-nine counts are 1, and\nthe delta is +4,210 on all three bases.** `verify_r72_v8.py` reports **0 failures**')
sub('§3.12 — the −4 series-repair sentence keeps its arithmetic against the new total',
    '**It is\n   −4 characters, and it is why the patch delta is +3,375 and not +3,379.**',
    '**It is\n   −4 characters, and it is why the patch delta is +4,210 and not +4,214.**')

# ============================================================ 4. §5 — the live title line
sub('§5 — the title line re-taken at store revision 72',
    '> **RE-TAKEN LIVE AT REVISION 7, because store revision 70 amended the title.**',
    '> **RE-TAKEN LIVE AGAIN AT REVISION 8, at store revision 72. Store revision 71 amended the title\n'
    '> once more — MOO-200\'s F15 took *"post-retirement employment"* out of the *"relating to"*\n'
    '> clause, −28 characters. The amended-and-added counts are unchanged: two amended, one added.**\n'
    '>\n'
    '> **SUPERSEDED, kept as the revision-7 record: re-taken live at revision 7, because store\n'
    '> revision 70 amended the title.**')

# ============================================================ 5. header, banner, order block
sub('H1 — revision 8',
    '# MOO-164 — "acts upon" and act-versus-notice, decided once: **two decisions, TWELVE anchored edits in THIRTEEN substitutions at revision 7, three candidates held, one retired, one fix direction declined**',
    '# MOO-164 — "acts upon" and act-versus-notice, decided once: **two decisions, TWELVE anchored edits in THIRTEEN substitutions at revision 8, SIX candidates held, one retired, one fix direction declined**')

sub('base-move count (narrative)',
    'The base has\nmoved **fifteen** times under this cut — store revisions 69 and 70 since revision 6 was cut.',
    'The base has\nmoved **seventeen** times under this cut — store revisions 71 and 72 since revision 7 was cut,\nand **§6 has now been re-spliced for the ninth time behind anchors that all still resolved exactly\nonce.**')
sub('base-move count (order block)', 'now held across **seven** base moves and two patch revisions',
    'now held across **nine** base moves and three patch revisions')

sub('caveat — three counsel passes, and revision 8\'s text unreviewed',
    '**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared\nby counsel — [MOO-187](/MOO/issues/MOO-187) and [MOO-209](/MOO/issues/MOO-209) are internal adversarial\npasses by a colleague and are expressly not legal advice, and revision 7\'s four new and re-cut texts\nhave not been read adversarially at all.',
    '**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared\nby counsel — [MOO-187](/MOO/issues/MOO-187), [MOO-209](/MOO/issues/MOO-209) and\n[MOO-214](/MOO/issues/MOO-214) are internal adversarial passes by a colleague and are expressly not\nlegal advice, and revision 8\'s four re-cut texts and four held candidates have not been read\nadversarially at all.')

BANNER = '''> ## REVISION 8 — [MOO-214](/MOO/issues/MOO-214)'s counsel pass, folded
>
> **13 findings — 0 fatal, 6 serious, 4 moderate, 3 minor — plus 12 null results and four direct
> answers. No finding is rejected.** **§18 is the only part of this document added at revision 8**;
> **§6 is re-spliced from store revision 72**, the ninth time, and **§5's title line is re-taken**.
> Every statement MOO-214 or the base made false is corrected **in place** and listed at **§18.14**.
>
> | | Folded in at revision 8 | Where |
> |---|---|---|
> | 1 | **164-7 re-cut** — the exception stops naming R-6 by a **paraphrase** that also matched R-3 and R-4b, and uses the determinate descriptor this cut already coined (**S3**) | §18.1 |
> | 2 | **164-7 also takes m2** — one sentence, so that a decision deemed to exist is not deemed to *state* what a decision must state | §18.3 |
> | 3 | **164-7 carries the Policy Director's MOO-141 §3.3 cross-reference**, drafted to their three requirements and naming the other deeming **by content, not by citation** | §18.5 |
> | 4 | **164-8 re-cut** — *"of a kind"* (**S1**), and *"after the member has retired"* (**m1**) | §18.2, §18.3 |
> | 5 | **164-13(b) re-cut** — the bar moves into clause (iv)'s **trigger** (**S2**), and clause (iv) now states the **timeliness deeming** and the **supersession** it omitted (**M1**) | §18.2 |
> | 6 | **164-12 re-cut** — the noun phrase written out, as G 4's model does (**M3**) | §18.4 |
> | 7 | **The subsection J enforcement claim withdrawn and counted at 0** (**S4**) | §18.8 |
> | 8 | **`check_doc_vs_kit.py` rewritten** against all five of **S5**'s fix directions, after counsel broke the old one three ways while it printed *"0 mismatch(es)"* | §18.11 |
> | 9 | **Four candidates drafted and HELD** — **164-15** (S6), **164-16** (counsel's impose-not-except form, declined), **164-17** (S4) and **164-18** (M2) | §18.6–§18.8 |
>
> **Thirteen substitutions; the delta is +4,210, not +3,375. Three questions for the Policy Director
> at §18.13.** Every figure in §18 is **counted** by `verify_r72_v8.py`, which reports **0 failures**
> at store revision 72.

'''
sub('revision-8 banner inserted above the revision-7 banner',
    "> ## REVISION 7 — [MOO-209](/MOO/issues/MOO-209)'s counsel pass, folded",
    BANNER + "> ## REVISION 7 — [MOO-209](/MOO/issues/MOO-209)'s counsel pass, folded")

sub('application-order block restated for revision 8',
    '> **RESTATED AGAIN AT REVISION 7 for THIRTEEN substitutions at store revision 70.**',
    '''> **RESTATED AGAIN AT REVISION 8 for THIRTEEN substitutions at store revision 72.** Every FIND
> resolves **exactly once** in enacted §1 on each of three bases — store revision 72 as it stands, and
> with the MOO-141 patch carrying Edit 3 at **30** and at **120** days — with the **identical +4,210
> delta** in all three. **So this cut is still order-independent of the MOO-141 patch and still
> indifferent to the 30/120 answer**, now at a **sixth** store base. `verify_r72_v8.py`: **0
> failures**. §18.12.
>
> **The Policy Director has decided the joint landing on [MOO-141](/MOO/issues/MOO-141): that patch
> and this cut are applied in ONE cut, as one decision.** The §3.3 cross-reference this cut now
> carries does **not** create that dependency — it names the other deeming by its content, so with
> MOO-141 absent the class is empty and the clause is inert. §18.5.

**SUPERSEDED, kept as the revision-7 record: restated at revision 7 for thirteen substitutions at store revision 70.**''')

# ============================================================ 6. the record corrections
sub('§17.1 — the extension described as reaching R-6 and nothing else',
    '### 17.1 F1 — the serious one. 164-7\'s exception is extended, and the one thing it does not cure is stated rather than drafted around',
    '### 17.1 F1 — the serious one. 164-7\'s exception is extended, and the one thing it does not cure is stated rather than drafted around\n\n'
    '> **CORRECTED AT REVISION 8 — [MOO-214](/MOO/issues/MOO-214) S3.** The descriptor this section\n'
    '> settles on, *"to give the member written notice of the member\'s final qualifying retirement\n'
    '> date,"* is a **paraphrase**, and counted on the base it answers to **three** duties in that\n'
    '> definition, not one: R-3, R-4b and R-6. **Revision 8 replaces it with the determinate descriptor\n'
    '> 164-5 and 164-13(a) put into the bill.** The reasoning in this section for *why* R-6 must be\n'
    '> excepted survives unchanged; only the words that identify R-6 are superseded. **§18.1.**')

sub('§17.4 — the subsection J reliance withdrawn',
    '### 17.4 F4 — new **Edit 164-13**: the conforming disclosure amendment, in two substitutions inside one sentence of D 1',
    '### 17.4 F4 — new **Edit 164-13**: the conforming disclosure amendment, in two substitutions inside one sentence of D 1\n\n'
    '> **WITHDRAWN AT REVISION 8 — [MOO-214](/MOO/issues/MOO-214) S4.** Where this section relies on\n'
    '> subsection J\'s report reaching a **failure to state**, it is wrong. Counted in subsection J:\n'
    '> *"failure to state"* **0**, *"requires to be stated"* **0**. J 1 reports **lateness**, and its\n'
    '> other limb is a pointer to provisions that expressly route something into the report; nothing\n'
    '> routes a failure to state clause (iv) there. **A failure to state it in a *notice* is reviewable\n'
    '> under M 2; a failure to state anything in the *written statement* is reviewable nowhere.**\n'
    '> Candidate **164-17** is drafted and held. **§18.8, question 2.**')

# ============================================================ 7. append §18
assert doc.rstrip().endswith('store.**'), doc[-120:]
doc = doc.rstrip('\n') + '\n' + S18

open('moo164_rev8.md', 'w', encoding='utf-8').write(doc)
print('\n'.join(log))
print(f'\nmoo164_rev7.md {start_len} chars -> moo164_rev8.md {len(doc)} chars (+{len(doc)-start_len})')

# ============================================================ 8. post-conditions
P = doc
PRE18 = doc[:doc.index('\n## 18. Revision 8')]   # §18 quotes the superseded forms deliberately
checks = [
    ('§18 is present once', P.count('## 18. Revision 8'), 1),
    ('three questions, numbered', P.count('### 18.13 Questions for the Policy Director'), 1),
    ('the corrections table is present', P.count('### 18.14 Statements corrected in place at revision 8'), 1),
    ('the revision-8 banner is above the revision-7 banner',
     P.index('## REVISION 8') < P.index('## REVISION 7'), True),
    ('no superseded 164-7 exception descriptor survives outside §18',
     PRE18.count("to give the member written notice of the member's final qualifying retirement date"), 0),
    ('  and §18 names it, once, as the text that was replaced',
     P.count("to give the member written notice of the member's final qualifying retirement date") -
     PRE18.count("to give the member written notice of the member's final qualifying retirement date"), 1),
    ('the determinate descriptor stands in the exception at every site it is quoted',
     P.count('in subsection A to give a notice of a date required by that definition by reason of'), 3),
    ('m2\'s sentence is present at its three sites', P.count(V8.NOT_STATED), 3),
    ('the §3.3 cross-reference is present at its three sites', P.count(V8.XREF), 3),
    ('no bare "the member\'s retirement has taken effect" outside §18',
     PRE18.count("the member's retirement has taken effect"), 0),
    ('clause (iv) states the supersession wherever it is quoted',
     P.count('and that a notice so filed is filed within the period allowed by this subdivision'), 3),
    ('the patch total is +4,210 and no operative +3,375 survives outside a revision-7 label',
     P.count('+4,210') >= 6, True),
    ('the four held candidates are each named', [P.count(f'164-{n}') > 0 for n in (15, 16, 17, 18)], [True] * 4),
    ('§6.3 carries clause (iv) as re-cut', R['D1'].count('and the member has not retired'), 1),
    ('§6.6 carries the cross-reference', R['M2'].count('the two provisions apply cumulatively'), 1),
    ('§6.2 carries MOO-141 Edit 2 at ITS revision 8', R['DEF'].count('except that where the request is denied otherwise than by'), 1),
]
bad = 0
for lbl, got, want in checks:
    ok = got == want
    bad += 0 if ok else 1
    print(f'  [{"ok" if ok else "FAIL"}] {lbl}: {got} (expected {want})')
print(f'{bad} post-condition failure(s)')
sys.exit(1 if bad else 0)
