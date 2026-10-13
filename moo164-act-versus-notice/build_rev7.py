# -*- coding: utf-8 -*-
"""Assemble MOO-164 **revision 7** of `moo164-act-versus-notice` from revision 6.

Every edit below is asserted for an exact occurrence count before it is made, so a correction that
silently matches nothing — or matches twice — fails the build instead of shipping. That is the
discipline MOO-209 F5 and F11 earned: a claim about this document is a counted claim.

Inputs : moo164_rev6.md (fetched), repro70.json (the live splice), sec17.md (revision 7's section)
Output : moo164_rev7.md

Run: python3 build_rev7.py
"""
import json
import re

doc = open('moo164_rev6.md', encoding='utf-8').read()
R = json.load(open('repro70.json'))
S17 = open('sec17.md', encoding='utf-8').read()
start_len = len(doc)
log = []


def sub(label, old, new, count=1):
    global doc
    got = doc.count(old)
    assert got == count, f'{label}: expected {count} occurrence(s), found {got}'
    doc = doc.replace(old, new)
    log.append(f'  [{count}x] {label}')


# ===================================================================== 1. the three re-cut edits
# 164-7's exception, extended on F1. Three occurrences: §3.7 (operative), §6.6 (reproduction,
# replaced wholesale below) and §13.7 (the candidate as first drafted — the record).
EXC_OLD = ('Except for the purposes of the duty of the Board under this subsection to act upon an '
           'application no later than 15 days after it acts upon the request,')
EXC_NEW = ('Except for the purposes of the duty of the Board under this subsection to act upon an '
           'application no later than 15 days after it acts upon the request and the duty of the '
           'Board under the definition of "final qualifying retirement date" in subsection A to '
           'give the member written notice of the member\'s final qualifying retirement date,')
sub('F1 — 164-7\'s exception extended (§3.7, §6.6, §13.7)', EXC_OLD, EXC_NEW, 3)

# 164-8: F2 deletes the surplusage, F3 confines the supersession.
sub('F2 + F3 — 164-8\'s tail re-cut',
    'within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes any notice previously filed.',
    'within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member, except that no notice may be filed under this sentence after the member\'s retirement has taken effect.',
    3)
sub('F3 — "a notice already filed" conformed to the member\'s own notice of retirement',
    'or a notice replacing a notice already filed, no later than 30 days after the Board gives the notice',
    'or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives the notice',
    3)

# 164-12: F6 deletes the notwithstanding.
sub('F6 — 164-12\'s notwithstanding deleted',
    'Notwithstanding the definition in subdivision 4, and for the purposes of this subdivision, such an application is pending',
    'For the purposes of this subdivision, such an application is pending',
    3)

# ===================================================================== 2. the record corrections
sub('F5 — the 48-day cap is a chosen outer limit, not a restatement',
    'The cap is not invented: every number in it is already in the section.',
    'The cap is a **chosen outer limit**, and the three figures in it are each in the section. '
    '**It is not a restatement of the periods it displaces, and §17.6 withdraws the claim that it '
    'is: those periods are act + 62 for a request under the definition with every duty met, and '
    'unbounded for a request for reconsideration.** [MOO-209](/MOO/issues/MOO-209) **F5**.')

sub('F7 — "the identical date R-5\'s floor keys to" (§3.7)',
    'the identical formula Edit 164-4 puts\n   into R-5**, and the identical date R-5\'s floor keys to.',
    'the identical formula Edit 164-4 puts\n   into R-5**, and the **identical triggering event** — the expiry of the allowed period — that R-5\'s\n   floor keys to. **Not the identical date, and not the identical class: R-5\'s floor is one month\n   later on the same facts and reaches reconsideration requests too.** §17.7, '
    '[MOO-209](/MOO/issues/MOO-209) **F7**.')

sub('F7 — "two provisions about one date now agree" (§16.1)',
    '**the identical date Edit\n  164-4 already keys R-5\'s floor to**. Two provisions about one date now agree, which is the character of\n  the whole cut.',
    '**the identical triggering event, and the identical\n  nine-word formula, that Edit 164-4 keys R-5\'s floor to** — the expiry of the allowed period.\n  **Corrected at §17.7: the two dates are *not* identical and the provisions do not "agree"; the\n  floor mechanism resolves them, and the member takes the later. The point this was carrying — that\n  trigger two invents no bound — is unaffected.** [MOO-209](/MOO/issues/MOO-209) **F7**.')

sub('F8 — §7.3\'s report-line claim re-cut',
    '- **Subdivision J 1 and subsection C\'s reporting sentences.** Both report failures *"to make a\n  determination, to give a notice, or to make a payment within a period required by this section."* None of\n  the six edits creates or removes a duty, so neither report line moves. **No amendment.**',
    '- **Subdivision J 1\'s reporting sentence. RE-CUT AT REVISION 7 ON [MOO-209](/MOO/issues/MOO-209) F8 —\n  the conclusion survives, its stated basis did not.** J 1 reports *"every failure of the Board to\n  make a determination, **or to give a notice**, within a period required by this section, stated\n  separately for each provision"* — **no payment limb**; the string with the payment limb that I\n  attributed to it is **M 2\'s own standing sentence**. **And subsection C is dropped from this item\n  altogether**: it reports only failures *"required by this subsection within the period this\n  subsection allows for it"*, so **it cannot report a failure of an M 2 duty at all.** None of the\n  edits creates or removes a duty, so J 1 does not move. **No amendment.** §17.7.')

sub('F8 — the "J 1 and subsection C" conclusion in the revision-6 re-run',
    'So a failure to meet it is reportable under J 1 and subsection C **by the words those\n  provisions already have**, which is the result route (c) was taken to produce.',
    'So a failure to meet it is reportable under J 1 **by the words that provision already\n  has** — **and not under subsection C, which F8 shows cannot reach an M 2 duty** — which is the\n  result route (c) was taken to produce. **F1\'s extended exception strengthens this**, because R-6\'s\n  notice duty sits squarely inside J 1\'s express *"or to give a notice"* limb. §17.7.')

sub('F11 — §3.8\'s counted claim corrected',
    '`amend`, `withdraw`, `replacing`, `substitute` each **0** occurrences in the subdivision —\nand **§ 51.1-153 is silent**.',
    '`withdraw`, `replacing` and `substitute` each **0** occurrences in the subdivision, and `amend` **once** and only in *"the Internal Revenue Code, as amended or renumbered"* — no occurrence of any of the four in any sense bearing on a filed notice ([MOO-209](/MOO/issues/MOO-209) **F11**) — and **§ 51.1-153 imposes no filing vehicle, though it is *not* silent: subsection E caps retroactivity at 90 days before the filing, which is why Edit 164-8 no longer says *"satisfies § 51.1-153"*. F2, §17.2.**')

sub('F15 — the open case named by the enacted sentence\'s own phrase (§3.7)',
    '**The one case still open is the member who files a\nreconsideration request and never files the expiry notice**',
    '**The one case still open is the person who filed a\nreconsideration request and never files the expiry notice** — *the person who filed the request*,\nwhich is the enacted sentence\'s own phrase and reaches all seven of M 2\'s standing classes and not\nonly the member ([MOO-209](/MOO/issues/MOO-209) **F15**)')

sub('F9 — §16.6\'s meaning test restated in its defensible form',
    '**None of the 21 existing occurrences is amended and none changes meaning.**',
    '**None of the 21 existing occurrences is re-worded, and none acquires a different date where the\nsection already fixed one.** *(Restated at revision 7 on [MOO-209](/MOO/issues/MOO-209) **F9**. The\nearlier form — *"none changes meaning"* — was too strong: changing what an existing occurrence means\nin the deemed case is what a deeming is for. §17.3.)*')

# ===================================================================== 3. markers on the record sections
for label, anchor, note in [
    ('§4.2', '### 4.2 Candidate (c-2) — ',
     '\n\n> **SUPERSEDED IN PART AT REVISION 7, kept as the record of the choice.** Edit 164-12 as applied\n> no longer carries *"Notwithstanding the definition in subdivision 4"* — [MOO-209](/MOO/issues/MOO-209)\n> **F6** shows G 4\'s definition is already expressly confined, so there was nothing to notwithstand and\n> the clause weakened six other confinement clauses. **The harmonisation premise argued below is\n> withdrawn; the choice of (c-2) over (c-1) is not.** §17.5. **Candidate 164-14 (F10) would close this\n> edit\'s open end and is HELD — question 1, §17.10.**'),
    ('§13.5', '### 13.5 The real consequence of ',
     '\n\n> **SUPERSEDED IN PART AT REVISION 7, kept as the record of how candidate 164-8 was first drafted.**\n> Two of its premises moved on [MOO-209](/MOO/issues/MOO-209): **§ 51.1-153 is not silent** —\n> subsection E caps retroactivity at 90 days before the filing (**F2**) — and `amend` occurs **once**\n> in D 1, in the Internal Revenue Code formula (**F11**). **The premise the edit rests on survives: D 1\n> confers no power to amend, replace or withdraw a filed notice.** The applied text is at §3.8 and the\n> re-cut at §17.2.'),
    ('§13.7', '### 13.7 New §7 item 130 — ',
     '\n\n> **SUPERSEDED IN PART AT REVISION 7, kept as the record of how candidate 164-7 was first drafted.**\n> Its exception now names **two** duties, not one: [MOO-209](/MOO/issues/MOO-209) **F1** showed that\n> R-6\'s duty to give the member written notice of her final qualifying retirement date was unreached,\n> so in the deemed case no notice duty fell due and neither D 1\'s lateness sentence nor Edit 164-8\'s\n> vehicle could fire. **The applied text is at §3.7 and the re-cut, with the one case it still does\n> not cure, at §17.1.**'),
]:
    assert doc.count(anchor) == 1, (label, anchor, doc.count(anchor))
    k = doc.index(anchor)
    eol = doc.index('\n', k)
    doc = doc[:eol] + note + doc[eol:]
    log.append(f'  [1x] superseded marker on {label}')

# ===================================================================== 4. §6 re-spliced from store rev 70
i6 = doc.index('\n## 6. The provisions')
j6 = doc.index('\n## 7. Cross-reference')
s6 = doc[i6:j6]
subs = [(mm.start(), mm.group(0)) for mm in re.finditer(r'\n### 6\.\d[^\n]*', s6)]
KEYS = {'6.1': ['A'], '6.2': ['DEF'], '6.3': ['D1'], '6.4': ['G2'], '6.5': ['G4'],
        '6.6': ['M1', 'M2', 'M3']}
new6 = s6[:subs[0][0]]
for n, (pos, h) in enumerate(subs):
    end = subs[n + 1][0] if n + 1 < len(subs) else len(s6)
    body = s6[pos:end]
    num = h.strip().split()[1]
    lines = body.split('\n')
    idx = [k for k, l in enumerate(lines) if l.startswith('<u>') or l.startswith('> ')]
    assert idx, num
    assert len(idx) == len(KEYS[num]), (num, len(idx), len(KEYS[num]))
    for k, key in zip(idx, KEYS[num]):
        lines[k] = R[key]
    new6 += '\n'.join(lines)
    log.append(f'  §{num} re-spliced from store revision 70 ({", ".join(KEYS[num])})')
doc = doc[:i6] + new6 + doc[j6:]

# ===================================================================== 5. §5 — the live title line
sub('§5 — the title line reproduced live at store revision 70',
    '## 5. Title line, enacting clause and enactment clauses',
    '## 5. Title line, enacting clause and enactment clauses\n\n'
    '> **RE-TAKEN LIVE AT REVISION 7, because store revision 70 amended the title.** Its substitution 6\n'
    '> put *"death benefits; designation of beneficiary"* into the *"relating to"* clause. `repro70.py`\n'
    '> now reproduces the title line, the enacting clause and the first enactment **by content**, so this\n'
    '> section cannot go stale silently as §6 has eight times. **This cut adds no section to the act and\n'
    '> removes none, so the amended-and-added counts are unchanged: two amended, one added.**\n>\n'
    '> **Title, as it stands at store revision 70:**\n>\n'
    '> ' + R['TITLE'] + '\n>\n'
    '> **Enacting clause and first enactment:**\n>\n'
    '> ' + R['ENACT'] + '\n>\n'
    '> ' + R['ENACT1'] + '\n')

# ===================================================================== 6. the header and the top blocks
sub('H1 — revision 7',
    '# MOO-164 — "acts upon" and act-versus-notice, decided once: **two decisions, ELEVEN anchored edits at revision 6, one candidate still held, and one candidate retired**',
    '# MOO-164 — "acts upon" and act-versus-notice, decided once: **two decisions, TWELVE anchored edits in THIRTEEN substitutions at revision 7, three candidates held, one retired, one fix direction declined**')

sub('base-move count (narrative)', 'The base has\nmoved thirteen times under this cut.',
    'The base has\nmoved **fifteen** times under this cut — store revisions 69 and 70 since revision 6 was cut.')
sub('base-move count (order block)', 'now held across **five** base moves and two patch revisions',
    'now held across **seven** base moves and two patch revisions')

sub('caveat — two counsel passes, and revision 7\'s text unreviewed',
    '**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared\nby counsel — [MOO-187](/MOO/issues/MOO-187) is an internal adversarial pass by a colleague and is\nexpressly not legal advice.',
    '**Internal working draft material. Not a Division of Legislative Services bill. Not reviewed or cleared\nby counsel — [MOO-187](/MOO/issues/MOO-187) and [MOO-209](/MOO/issues/MOO-209) are internal adversarial\npasses by a colleague and are expressly not legal advice, and revision 7\'s four new and re-cut texts\nhave not been read adversarially at all.')

# The revision-6 banner gets a revision-7 banner above it.
BANNER = '''> ## REVISION 7 — [MOO-209](/MOO/issues/MOO-209)'s counsel pass, folded
>
> **16 findings — 0 fatal, 5 serious, 5 moderate, 6 minor — and 12 null results, taken on an applied
> copy the reviewer built themselves. No finding is rejected.** **§17 is the only part of this document
> added at revision 7**; **§6 is re-spliced from store revision 70** and **§5's title line is now taken
> live**. Every statement that MOO-209 or the base made false is corrected **in place** and listed in a
> table at **§17.13**.
>
> | | Folded in at revision 7 | Where |
> |---|---|---|
> | 1 | **164-7 re-cut** — the exception now reaches R-6's notice duty, so a notice duty falls due in the deemed case (**F1**) | §17.1 |
> | 2 | **164-8 re-cut** — the *"satisfies § 51.1-153"* surplusage deleted (**F2**), the supersession confined to the member's own notice with a post-retirement bar (**F3**) | §17.2 |
> | 3 | **Edit 164-13, new** — F4's conforming disclosure amendment: clause **(iv)**, the third document, and the series' *"and"* moved | §17.4 |
> | 4 | **164-12 re-cut** — the notwithstanding deleted; G 4's definition was already confined (**F6**) | §17.5 |
> | 5 | **The 48-day derivation withdrawn and restated** — 48 is a **chosen outer limit**, and the mislabelled verifier line is **deleted** (**F5**) | §17.6 |
> | 6 | **Seven record corrections** — F7, F8, F9, F11, F14, F15, F16 — and N1 and N2 made into counted assertions | §17.7, §17.8 |
> | 7 | **F13 declined** on drafting grounds, with the words drafted so the Director can overrule in one line | §17.9 |
> | 8 | **Candidate 164-14 (F10) carded and HELD** — it narrows (c-2), whose cost-neutrality is why no board card was raised | §17.10 |
>
> **Thirteen substitutions; the delta is +3,375, not +2,551. Three questions for the Policy Director at
> §17.12.** Every figure in §17 is **counted** by `verify_r70_v7.py`, which reports **0 failures** at
> store revision 70.

'''
sub('revision-7 banner inserted above the revision-6 banner',
    "> ## REVISION 6 — the Policy Director's disposition, folded in",
    BANNER + "> ## REVISION 6 — the Policy Director's disposition, folded in")

# The application-order block, restated for thirteen substitutions at store revision 70.
sub('application-order block restated for revision 7',
    '**RESTATED AT REVISION 6 for eleven edits at store revision 68.**',
    '''> **RESTATED AGAIN AT REVISION 7 for THIRTEEN substitutions at store revision 70.** Every FIND
> resolves **exactly once** in enacted §1 on each of three bases — store revision 70 as it stands, and
> with the MOO-141 patch carrying Edit 3 at **30** and at **120** days — with the **identical +3,375
> delta** in all three. **So this cut is still order-independent of the MOO-141 patch and still
> indifferent to the 30/120 answer**, now at a **fifth** store base and for thirteen substitutions
> rather than eleven. `verify_r70_v7.py`: **0 failures**. §17.11.

**SUPERSEDED, kept as the revision-6 record: restated at revision 6 for eleven edits at store revision 68.**''')

# The MOO-141 broken-anchor box: repaired by MOO-141 at store revision 69.
sub('MOO-141 broken-anchor box — repaired by MOO-141',
    '> **MOO-141 must re-cut its own Edit 1; this cut does not do it for them.** Edits 2 and 3 still resolve\n> exactly once. §16.5.',
    '> **REPAIRED BY MOO-141 AT STORE REVISION 69, and their re-cut also conformed Edit 1\'s saving to\n> 164-7\'s express exception.** The dead string is kept and asserted at **0** so the break stays visible.\n> Edits 2 and 3 still resolve exactly once, and the MOO-141 fixture is cross-checked against their own\n> published **+847** delta rather than trusted. **MOO-141 now carries its own ordering constraint: its\n> Edit 2 must be applied in the same cut as its Edit 1.** §16.5, and §17.3 for why the two savings are\n> now asymmetric and why that is principled.')

# ================================================= 6b. §3 and §3.11 brought to revision 7
sub('§3 heading — thirteen substitutions at store revision 70',
    '## 3. The patch — **eleven** anchored edits at revision 6, verified at store revision 68 and on an applied copy',
    '## 3. The patch — **TWELVE** anchored edits in **THIRTEEN** substitutions at revision 7, verified at store revision 70 and on an applied copy')

sub('§3 lead paragraph — the revision-7 figures',
    """**Whoever applies this must use the FIND strings verbatim, and must apply every one of them inside
enacted §1 only.** Each is counted over §1 of store revision 68, and each is counted **three times** —
on the base as it stands, on the base with the MOO-141 patch at **revision 5**, and on it with the patch
at **revision 6** (Edit 3 at 120 days). **All thirty-three counts are 1, and the delta is +2,551 on all
three bases.** `verify_r68_v6.py` reports **0 failures**; `apply164.py` applies all eleven to a copy and
asserts that everything outside §1 is byte-identical.""",
    """**Whoever applies this must use the FIND strings verbatim, and must apply every one of them inside
enacted §1 only.** Each is counted over §1 of **store revision 70**, and each is counted **three
times** — on the base as it stands, on the base with the MOO-141 patch at **revision 5**, and on it with
the patch at **revision 6** (Edit 3 at 120 days). **All thirty-nine counts are 1, and the delta is
+3,375 on all three bases.** `verify_r70_v7.py` reports **0 failures**; `apply164.py` applies all
thirteen substitutions to a copy and asserts that everything outside §1 is byte-identical.

> **REVISION 7 CHANGED FOUR OF THE EDITS BELOW, on [MOO-209](/MOO/issues/MOO-209).** **164-7** takes
> F1's extended exception; **164-8** takes F2 and F3; **164-12** takes F6; and **164-13** is new, on F4,
> in two substitutions inside one sentence of D 1. The FIND/READ blocks in §3.7, §3.8 and §3.11 carry the
> revision-7 text; **§17.1 to §17.5 carry the reasoning, and §17.13 lists every statement corrected in
> place.** **Revision 6 was eleven substitutions and +2,551.**""")

sub('§3 table — the three re-cut rows, 164-13, and the total',
    """| **164-7** | M 2, after the enacted denial sentence | item 130, route (c), in 164-7-B's two-trigger form | **+1,153** |
| **164-8** | D 1, the lateness-extension sentence | the filing vehicle | +485 |
| **164-10** | M 2's 90-day duty | F6 — the commencement | +27 |
| **164-11** | M 2's expiry-notice sentence | F12 — the conformed formula | +24 |
| **164-12** | G 2, item 46's carve-out | card (c), candidate **(c-2)** | +220 |
| | | **total** | **+2,551** |""",
    """| **164-7** | M 2, after the enacted denial sentence | item 130, route (c), two triggers; **re-cut on F1** | **+1,337** |
| **164-8** | D 1, the lateness-extension sentence | the filing vehicle; **re-cut on F2 and F3** | **+621** |
| **164-13(a)** | D 1, the disclosure duty's document list | **new on F4** | **+103** |
| **164-13(b)** | D 1, clause **(iv)** and the series' *"and"* | **new on F4** | **+454** |
| **164-10** | M 2's 90-day duty | F6 — the commencement | +27 |
| **164-11** | M 2's expiry-notice sentence | F12 — the conformed formula | +24 |
| **164-12** | G 2, item 46's carve-out | card (c), candidate **(c-2)**; **re-cut on F6** | **+167** |
| | | **total** | **+3,375** |""")

sub('§3 — "There is no Edit 164-9" extended to the two new held candidates',
    """**§16.4** states the one thing the applier needs about it: it amends **Edit 164-1's own new text**, so it
cannot be applied to the base, and its FIND resolves exactly once in the **applied** text — counted.""",
    """**§16.4** states the one thing the applier needs about it: it amends **Edit 164-1's own new text**, so it
cannot be applied to the base, and its FIND resolves exactly once in the **applied** text — counted.

**Revision 7 adds two more held candidates and reserves their numbers the same way: 164-14**
([MOO-209](/MOO/issues/MOO-209) F10, question 1, §17.10), which likewise amends **Edit 164-12's own new
text**; and **164-7-F13** (F13, declined on drafting grounds, §17.9). **There is no Edit 164-14 and no
Edit 164-7-F13 in this patch.** Candidate **(c-1)** is retired and must never be applied.""")

sub('§3 FIND bases — store revision 70',
    'in enacted §1 at store revision 68', 'in enacted §1 at store revision 70', 5)

sub('§3.11 — the notwithstanding paragraph replaced by F6\'s disposition',
    """***"Notwithstanding the definition in subdivision 4"*** makes the divergence deliberate on the face of
the text, because without it subsection G would define *"pending"* for a disability application twice,
differently, in adjacent subdivisions, and the natural judicial move on a word defined twice in one
subsection is to **harmonise**, with the drafter no longer choosing which gives way.""",
    """**DELETED AT REVISION 7 on [MOO-209](/MOO/issues/MOO-209) F6: the edit no longer opens
*"Notwithstanding the definition in subdivision 4."*** The premise was that subsection G would otherwise
define *"pending"* twice and a court would harmonise. **It is not made out: G 4's definition opens *"for
the purposes of this subdivision"* and never travelled into G 2, so there was nothing to notwithstand —
and a word confined twice is not a word defined twice.** The clause bought presentational comfort in G 2
at the cost of inviting the argument that the section's **other six** confinement clauses of the same
family, having no notwithstanding beside them, *do* travel. **Where the divergence goes instead is where
the Policy Director had already put it — the §0 record and the designation-review read-through.** §17.5.""")

sub('§3.11 — the word and character count re-measured',
    """**38 words, +220 characters. CORRECTED AT REVISION 6: §4.2 called it *"twenty words"* and then
*"twenty-eight"*; counted, the new sentence is 38 words and 219 characters, +220 with the space.**""",
    """**RE-MEASURED AT REVISION 7: 30 words, +167 characters**, the notwithstanding having gone. It was
38 words and +220 at revision 6, and §4.2 called it *"twenty words"* and then *"twenty-eight"* before
anyone counted it. **Every figure in this line is counted by `verify_r70_v7.py`.**""")

sub('§3.11 — "grants or denies" now carries F10 and candidate 164-14',
    """for the **G 2 reduction determination** and the collision would have made the carve-out circular — F10.""",
    """for the **G 2 reduction determination** and the collision would have made the carve-out circular — F10
of the first pass, and [MOO-209](/MOO/issues/MOO-209) **N8** confirms the collision is cleanly avoided
(*"determination"*/*"determined"* 26 times in G 2; *"grants"* and *"denies"* once each and nowhere else).
**But MOO-209 F10 finds the words leave pendency open-ended where the Board neither grants nor denies —
it defers, or the application is withdrawn or closed administratively. Candidate 164-14 closes that end
in six words and is HELD, because it narrows (c-2) and (c-2)'s cost-neutrality is the express reason no
item-46 card went to the board. Question 1, §17.10.**""")

sub('§0.3 — the revision-7 delta alongside the revision-6 one',
    '**+2,551 characters of amendment across eleven edits at revision 6.**',
    '**+3,375 characters of amendment across twelve edits in thirteen substitutions at revision 7** — it\nwas **+2,551** across eleven at revision 6,')

# ================================================= 6c. tidy-ups the first two passes exposed
sub('§0.3 — repair the delta sentence my own revision-7 edit left ungrammatical',
    '**+3,375 characters of amendment across twelve edits in thirteen substitutions at revision 7** — it\nwas **+2,551** across eleven at revision 6, It was **+642** across six at',
    '**+3,375 characters of amendment across twelve edits in thirteen substitutions at revision 7.** It\nwas **+2,551** across eleven at revision 6, **+642** across six at')

sub('application order — the revision-7 base table, in the same form as the revision-6 one',
    """> rather than eleven. `verify_r70_v7.py`: **0 failures**. §17.11.

**SUPERSEDED, kept as the revision-6 record: restated at revision 6 for eleven edits at store revision 68.** Every one of the eleven FIND strings
below resolves **exactly once** in enacted §1 in each of **three** bases, with the **identical +2,551
delta** in all three:""",
    """> rather than eleven. `verify_r70_v7.py`: **0 failures**. §17.11.
>
> | Base | Thirteen FINDs | Delta |
> |---|---|---|
> | `bill-text-s8` store revision **70** as it stands | all 1 | **+3,375** |
> | store revision 70 + MOO-141 patch **revision 5** (Edit 3 at 30 days) | all 1 | **+3,375** |
> | store revision 70 + MOO-141 patch **revision 6** (Edit 3 at 120 days) | all 1 | **+3,375** |
>
> **Thirty-nine counts, all 1; one delta, identical on all three.** The MOO-141 fixture is itself
> cross-checked against their published **+847**, Edit 3 at 120 days, so a stale fixture fails the check
> instead of passing quietly — which is how revision 6's own fixture was caught.

**SUPERSEDED, kept as the revision-6 record.** Restated at revision 6 for eleven edits at store
revision 68: every one of the eleven FIND strings below resolved **exactly once** in enacted §1 in each
of **three** bases, with the **identical +2,551 delta** in all three:""")

sub('application order — F21 count is thirteen FINDs now, not eleven',
    '**One fact the applier needs: apply every FIND inside enacted §1 only.** Five of the eleven FIND strings',
    '**One fact the applier needs: apply every FIND inside enacted §1 only.** Five of the **thirteen** FIND strings')

sub('application order — the stale MOO-141 lead-in folded into the repair note',
    """> **⚠ THE MOO-141 PATCH ITSELF HAS A BROKEN ANCHOR AND IT IS NOT THIS CUT'S.** Store revision 68 re-cast
> subsection A's three-day sentence — it is now confined to **mailing** and the triplet *"statement,
> notice, or certification"* replaces *"that statement or notice."* **MOO-141 Edit 1's FIND string
> resolves 0 times.** `verify_r68_v6.py` keeps the dead string and asserts it at **0** so the break stays
> visible, and carries a working repair **solely** so the order-independence test above can be run.
> **REPAIRED BY MOO-141 AT STORE REVISION 69, and their re-cut also conformed Edit 1's saving to
> 164-7's express exception.** The dead string is kept and asserted at **0** so the break stays visible.""",
    """> **⚠ THE MOO-141 PATCH HAD A BROKEN ANCHOR, IT WAS NEVER THIS CUT'S, AND IT IS NOW REPAIRED.** Store
> revision 68 re-cast subsection A's three-day sentence — confining it to **mailing**, with the triplet
> *"statement, notice, or certification"* replacing *"that statement or notice"* — and **MOO-141 Edit 1's
> FIND string resolved 0 times.** **MOO-141 re-cut it at store revision 69, and in the same re-cut
> conformed Edit 1's saving to 164-7's express exception.** The dead string is still kept and asserted at
> **0** so the break stays visible.""")

S312 = '### 3.12 Edit 164-13 — subdivision D 1, the disclosure duty. **NEW AT REVISION 7**, [MOO-209](/MOO/issues/MOO-209)\'s **F4**\n\n**Why it exists.** Edit 164-8 creates a 30-day window for the member whose only filing window closed\nwhile her request was pending. **The sentence that follows requires the Board to tell her about every\nother consequence of a late statement or notice — the extension, the effective-date permission, the\nthree-day mailing extension — and said nothing about this one.** Counsel\'s worked case is the whole of\nit: the Board gives a late notice on 1 November, states (i), (ii) and (iii) exactly as required, the\nmember reads that she *"may state"* a later effective date, is told of **no vehicle**, and lets the 30\ndays run. **The Board has complied with every duty in the subdivision and the vehicle expires unused.**\nA window the only document she receives does not mention is not a remedy. **The reasoning is at §17.4.**\n\n**Two substitutions, inside one sentence, applied in this order.**\n\n> **164-13(a) — FIND** (count = **1** in enacted §1 at store revision 70; **1** whole-document):\n>\n> ```\n> The Board shall state, in the written statement required by that definition and in every notice of a later approved date required by that definition, (i)\n> ```\n>\n> **READ:**\n>\n> ```\n> The Board shall state, in the written statement required by that definition, in every notice of a later approved date required by that definition, and in every notice of a date required by that definition by reason of the Board\'s action upon a request, (i)\n> ```\n\n**+103 characters.** The disclosure sentence reached **two** documents; Edit 164-8\'s trigger reaches\n**three**. The one it missed is **Edit 164-5\'s descriptor** — *"any notice of a date required by that\ndefinition by reason of the Board\'s action upon a request"* — which is **R-6\'s notice**, the document\ntrigger two\'s class turns on. **The new words use the conformed descriptor, so 164-5 and 164-13 cannot\ndiverge**; the verifier asserts that 164-5\'s FIND precedes both of 164-13\'s inside D 1.\n\n> **164-13(b) — FIND** (count = **1** in enacted §1 at store revision 70; **1** whole-document):\n>\n> ```\n> ; and (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days.\n> ```\n>\n> **READ:**\n>\n> ```\n> ; (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days; and (iv) that where the Board gives a notice described in this sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives that notice, and that no such notice may be filed after the member\'s retirement has taken effect.\n> ```\n\n**+454 characters. Edit 164-13 totals +557 across the two substitutions.**\n\n***Who, what, by when, or else:*** the actor is the **Board**, the object is **four statements**, the\noccasion is **each of three documents**, and the consequence is **subsection J\'s report**, which reaches\n*"every failure … to state a matter this section requires to be stated."* No new reporting words are\nneeded and none are added — §7.3.\n\n**Three drafting choices in it, each one mine and each one stated.**\n\n1. **The FIND swallows *"; and"* before clause (iii) so that the series\' conjunction moves to the new\n   last item.** Adding (iv) without moving it would leave **two** *"and"*s in one series. **Store\n   revision 70 set the precedent in this very subdivision** — its substitution 3 moved D 1\'s\n   certification series\' *"and"* to that series\' new last item, for four characters. **MOO-209 did not\n   raise this; the base did.** The verifier asserts it in both directions: exactly one *"; and ("* in the\n   series, before **(iv)** and not before **(iii)**, with clause (iii) otherwise unchanged. **It is\n   −4 characters, and it is why the patch delta is +3,375 and not +3,379.**\n2. **Clause (iv) discloses the limit as well as the right** — *"and that no such notice may be filed\n   after the member\'s retirement has taken effect"*, which is Edit 164-8\'s own F3 bar. Clause (i)\n   already discloses its own limits (*"subject to the limits stated in that definition"*), and **a\n   disclosure that overstates a right is worse than no disclosure**, because the member relies on it.\n3. **It says *"a notice described in this sentence"* and not *"the preceding sentence."*** The\n   disclosure sentence lists the three documents itself after 164-13(a), so the reference is internal\n   and cannot be stranded by an insertion. **Edit 164-13 therefore adds no *"preceding sentence"*\n   reference at all** — counted, and the reason §17.8 can say revision 7 adds exactly three and all\n   three are 164-7\'s and 164-8\'s.\n\n**What it does not do.** It does not reach the **written statement**, because 164-8\'s trigger does not:\nD 1\'s filing window runs **from that statement**, so a late statement can never arrive after the window\nhas closed — [MOO-209](/MOO/issues/MOO-209) **N11**, which I could not break either.\n\n---\n'

# ================================================= 6d. §3.12 for Edit 164-13, and two stale figures
sub('§3.7 — 164-7 re-measured after F1',
    """**217 words, +1,153 characters** — 141 words and 743 characters in the deeming sentence, 76 words and
408 in the saving. **Revision 5 priced 164-7 alone at 170 words and +898; 164-7-B's second trigger is
the difference**, and §16.7 records that the earlier figure is superseded rather than wrong.""",
    """**RE-MEASURED AT REVISION 7: 245 words, +1,337 characters** — 141 words and 743 characters in the
deeming sentence, 104 words and 592 in the saving and its now two-duty exception. **F1's extension is
+184 of that.** It was 217 words and +1,153 at revision 6; revision 5 priced 164-7 alone at 170 words
and +898, 164-7-B's second trigger being that difference. **Each superseded figure is recorded rather
than rewritten away** — §16.7 and §17.13.""")

sub('§3.8 — 164-8 re-measured after F2 and F3',
    '**81 words, +485 characters.** *Who, what, by when, or else:*',
    """**RE-MEASURED AT REVISION 7: 97 words, +621 characters** — **F2** takes three words out (−22) and
**F3** puts the confinement and the post-retirement bar in (+158). It was 81 words and +485 at
revision 6. **The edit is more correct and, in one of its two limbs, shorter.** §17.2.

*Who, what, by when, or else:*""")

sub('§3 — Edit 164-13 inserted as §3.12',
    """designation-review read-through, is the deliberate divergence: subsection G will define *"pending"*
twice, differently, in adjacent subdivisions, on purpose.**

---
""",
    """designation-review read-through, is the deliberate divergence: subsection G will define *"pending"*
twice, differently, in adjacent subdivisions, on purpose.**

---

""" + S312)

# ===================================================================== 7. append §17
assert doc.rstrip().endswith('internal.**') or doc.rstrip().endswith('store.**'), doc[-120:]
doc = doc.rstrip('\n') + '\n' + S17

open('moo164_rev7.md', 'w', encoding='utf-8').write(doc)
print('\n'.join(log))
print(f'\nmoo164_rev6.md {start_len} chars -> moo164_rev7.md {len(doc)} chars (+{len(doc)-start_len})')

# ===================================================================== 8. post-conditions
P = doc
checks = [
    ('no superseded 164-7 exception survives', P.count(EXC_OLD + ' nothing'), 0),
    ('the extended exception stands at three sites', P.count(EXC_NEW), 3),
    ('no "satisfies § 51.1-153," survives', P.count('satisfies § 51.1-153,'), 0),
    ('"supersedes any notice previously filed" survives only in §17.13\'s corrections table',
     P[:P.index('\n## 17. Revision 7')].count('supersedes any notice previously filed'), 0),
    ('"Notwithstanding the definition in subdivision 4" survives only where labelled as deleted or as record',
     P.count('Notwithstanding the definition in subdivision 4'), 5),
    ('clause (iv) is in the §6.3 reproduction', R['D1'].count('(iv) that where the Board gives a notice'), 1),
    ('the §6.3 reproduction shows the series\' "and" moved', R['D1'].count('~~and~~ **(iii)**'), 1),
    ('§17 is present once', P.count('## 17. Revision 7'), 1),
    ('three questions, numbered', P.count('### 17.12 Questions for the Policy Director'), 1),
    ('the +3,375 figure appears in the banner, the order block and §17',
     P.count('+3,375') >= 3, True),
    ('every pre-§3.1 "+2,551" sits under a revision-6 label or a revision-7 contrast',
     P[:P.index('\n### 3.1 ')].count('+2,551'), 8),
    ('the §3 table totals +3,375', P.count('| | | **total** | **+3,375** |'), 1),
    ('§3.11 no longer argues the notwithstanding; the premise survives only in §4.2, under a marker that withdraws it',
     P[:P.index('\n## 4.')].count('the natural judicial move on a word defined twice'), 0),
    ('§0.3\'s delta sentence is repaired', P.count('at revision 6, It was'), 0),
    ('the revision-7 base table is present', P.count('| Base | Thirteen FINDs | Delta |'), 1),
    ('§3.12 carries Edit 164-13', P.count('### 3.12 Edit 164-13'), 1),
    ('  with both substitutions as FIND/READ blocks', P.count('**164-13(a) — FIND**') + P.count('**164-13(b) — FIND**'), 2),
    ('no stale "+1,153" or "+485" operative figure', P.count('**217 words, +1,153 characters**') + P.count('**81 words, +485 characters.**'), 0),
]
bad = 0
for lbl, got, want in checks:
    ok = got == want
    bad += 0 if ok else 1
    print(f'  [{"ok" if ok else "FAIL"}] {lbl}: {got} (expected {want})')
print(f'{bad} post-condition failure(s)')
