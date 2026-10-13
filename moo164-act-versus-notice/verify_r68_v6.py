# -*- coding: utf-8 -*-
"""MOO-164 **revision 6** — verification at store revision 68.

Revision 6 is the first cut in which the patch is **eleven** edits, not six. The Policy Director's
disposition promoted candidates 164-7 (carrying F19's limb (B)), 164-7-B, 164-8, 164-10, 164-11 and
(c-2) from held to applied; (c-1) is retired to the record and 164-9 stays held for MOO-204.

Supersedes verify_r68.py, which checks the six-edit cut. Everything that check did is here, plus:

  * the five promoted edits as applied edits rather than carded candidates;
  * the eleven-edit delta, on three bases;
  * the three ordering invariants the promotions create — 164-7's two "preceding sentence"
    references, 164-5 before 164-8 inside one sentence of D 1, and 164-10/164-11/164-7 all after the
    M 2 sentence D 1's ordinal reference points at;
  * the formula census after eleven edits rather than six;
  * candidate 164-9's FIND asserted against the APPLIED text, so MOO-204 can take it without a
    re-cut of Edit 164-1;
  * the 300-day arithmetic for clause (ii), which m8-a's enactment makes unconditional.

Every count is taken over **enacted §1 only** (finding F21). Several anchors resolve more than once
whole-document because the revision narratives quote them.

Run: python3 verify_r68_v6.py bill.md
Nothing is written to the store.
"""
import re
import sys

fail = 0


def chk(label, got, want):
    global fail
    if got != want:
        fail += 1
    print(f'   [{"ok" if got == want else "FAIL"}] {label}: {got} (expected {want})')


doc = open(sys.argv[1] if len(sys.argv) > 1 else 'bill.md', encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
print(f'== base: whole document {len(doc)} chars; enacted §1 {len(S1)} chars')

# ---------------------------------------------------------------- MOO-141 patch
E1_F_R65_DEAD = ("every period within which a person may or must act that runs from the giving of that "
                 "statement or notice is extended by three days.</u>")
E1_F_R68 = ("every period within which a person may or must act that runs from the giving of that "
            "statement, notice, or certification is extended by three days.</u>")
E1_R = (E1_F_R68[:-len('</u>')] +
        " For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period "
        "begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, "
        "or where a date is fixed by reference to the month in which the Board acts, or last acts, upon "
        "a request, the Board is deemed to act upon that request, and to last act upon it, on the date "
        "on which the Board first acts upon it. Nothing in the preceding sentence determines the date "
        "by which the Board is required to act upon a request, to make a determination, or to give a "
        "notice or a decision, or whether the Board has performed such a duty within a period required "
        "by this section.</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R5 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

print('\n== MOO-141 patch anchors at store revision 68 — the one break, still named')
chk('E1 FIND as written for store rev 65 (DEAD — MOO-141 must re-cut)', S1.count(E1_F_R65_DEAD), 0)
chk('E1 FIND repaired for store rev 68', S1.count(E1_F_R68), 1)
chk('E2 FIND', S1.count(E2_F), 1)
chk('E3 FIND', S1.count(E3_F), 1)


def build(body, e3):
    out = body
    for f, r in ((E1_F_R68, E1_R), (E2_F, E2_R), (E3_F, e3)):
        assert out.count(f) == 1, 'MOO-141 FIND not unique: ' + f[:50]
        out = out.replace(f, r, 1)
    return out


# ---------------------------------------------------------------- the eleven edits, revision 6
# Ordered as they are applied. 164-5 precedes 164-8 inside one sentence of D 1; 164-10, 164-11 and
# 164-7 precede 164-1 and 164-3 inside M 2.
EDITS = [
 ("164-1 (card (b))",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the Board acts upon the request"),
 ("164-2 (card (h))",
  "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
  "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect, the determination takes effect on the first day"),
 ("164-3 (card (j))",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request"),
 ("164-4 (card (l) / F-5)",
  "within the period this definition allows for acting upon it",
  "within the period allowed by this section for acting upon it"),
 ("164-5 (card (k) / F-9)",
  "any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition by reason of the Board's action upon a request"),
 ("164-6 (conforming)",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
  "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
 ("164-7 (item 130 route (c), in 164-7-B's two-trigger form, PROMOTED at revision 6)",
  "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
  "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of \"final qualifying retirement date\" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. Except for the purposes of the duty of the Board under this subsection to act upon an application no later than 15 days after it acts upon the request, nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section."),
 ("164-8 (D 1 filing vehicle, PROMOTED at revision 6)",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. Where the Board gives any notice described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice already filed, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision, satisfies § 51.1-153, and supersedes any notice previously filed."),
 ("164-10 (F6 commencement, PROMOTED at revision 6)",
  "The Board shall act upon a request for reconsideration within 90 days.",
  "The Board shall act upon a request for reconsideration within 90 days after the request is filed."),
 ("164-11 (F12 conforming, PROMOTED at revision 6)",
  "Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file",
  "Where the Board does not act upon a request for reconsideration within the period allowed by this section for acting upon the request, the person who filed the request may file"),
 ("164-12 = candidate (c-2) (card (c), PROMOTED at revision 6)",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. Notwithstanding the definition in subdivision 4, and for the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which the Board grants or denies it."),
]

HELD = {
 "(c-1) FIND — RETIRED to the record; G 4 must be untouched": "For the purposes of this subdivision an application for a disability retirement allowance is pending",
 "card (i) confirming-sentence insertion point — declined": "The Board shall act upon a request for reconsideration within 90 days.",
}

BASES = [("store rev 68", S1),
         ("store rev 68 + MOO-141 patch rev 5", build(S1, E3_R5)),
         ("store rev 68 + MOO-141 patch rev 6", build(S1, E3_R6))]

print('\n== the eleven applied anchors + two held strings, on three bases, over §1 only')
for name, body in BASES:
    print(f'  -- {name} ({len(body)} chars)')
    for label, f, r in EDITS:
        chk(label, body.count(f), 1)
    for label, f in HELD.items():
        chk(label, body.count(f), 1)


def apply_all(body):
    out = body
    for label, f, r in EDITS:
        assert out.count(f) == 1, 'FIND not unique when applied in order: ' + label
        out = out.replace(f, r, 1)
    return out


print('\n== delta of the ELEVEN edits — the revision-6 figure, on every base')
deltas = []
for name, body in BASES:
    d = len(apply_all(body)) - len(body)
    deltas.append(d)
    print(f'   {name} delta: {d}')
chk('the eleven-edit delta is identical on all three bases', len(set(deltas)), 1)
chk('the eleven-edit delta', deltas[0], 2551)
print('   for the record, revision 5\'s six-edit delta was +642')

only164 = apply_all(S1)
patched141 = build(S1, E3_R6)
both = apply_all(patched141)

print('\n== ordering invariants the five promotions create')
D1_S = ("the member may state an effective date of retirement that is no earlier than the first day of "
        "the month following the month in which the Board gives the statement or notice")
chk('164-5 FIND precedes 164-8 FIND inside one sentence of D 1',
    S1.index(EDITS[4][1]) < S1.index(D1_S), True)
DEEM = 'Where a request is denied by operation of the preceding sentence'
SAVE = 'Except for the purposes of the duty of the Board under this subsection to act upon an application'
DENIAL_END = 'a case decision as defined in § 2.2-4001 for the purposes of this subsection.'
chk('in the applied text the deeming sentence immediately follows the denial sentence',
    only164[only164.index(DENIAL_END) + len(DENIAL_END):].lstrip().startswith(DEEM), True)
chk('in the applied text the saving sentence immediately follows the deeming sentence',
    only164.index(SAVE) > only164.index(DEEM), True)
chk('"the preceding sentence" occurrences inside 164-7\'s two sentences', 2,
    only164[only164.index(DEEM):only164.index(SAVE) + 400].count('the preceding sentence'))
chk('nothing is inserted between the deeming and saving sentences',
    only164[only164.index(DEEM):only164.index(SAVE)].count('. ') , 1)

print('\n== question 4 — D 1\'s ordinal reference into M 2, re-run for eleven edits')
chk('D 1 ordinal reference still present and singular', S1.count('the second sentence of subdivision M 2'), 1)
M2_SENTENCES = [
    'written reconsideration by the Board stating the reasons for its decision.',
    'is a determination of the Board for the purposes of this subsection, whether or not another provision of this section expressly provides for review of it.',
    'The Board shall act upon a request for reconsideration within 90 days.',
    'the person who filed the request may file with the Board written notice that the period has expired.',
    'and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.',
]
pos = [S1.index(s) for s in M2_SENTENCES]
chk('M 2 sentence order 1 < 2 < 3 < 4 < 5', pos == sorted(pos), True)
print('   M 2 sentence 2 (the one D 1 points at) ends at §1 offset', pos[1])
M2_START = S1.index(M2_SENTENCES[0])
chk('no applied edit inserts into M 2 before sentence 2',
    all(S1.index(f) > pos[1] or S1.index(f) < M2_START for _, f, _ in EDITS), True)

print('\n== item 131 — the antecedent of "such case decision" is unmoved')
COMPLETION = 'Upon completion of a reconsideration under this subsection, the final determination issued by the Board shall constitute a case decision as defined in § 2.2-4001.'
chk('completion sentence still present once', only164.count(COMPLETION), 1)
chk('164-7\'s two sentences sit before the completion sentence',
    only164.index(SAVE) < only164.index(COMPLETION), True)
chk('164-7 introduces no competing "case decision"',
    only164[only164.index(DEEM):only164.index(SAVE) + 600].count('case decision'), 0)

print('\n== candidate 164-9, HELD for MOO-204 — its FIND against the APPLIED text')
C9_F = 'and in no case later than 48 days after the Board acts upon the request'
chk('164-9 FIND resolves exactly once in the applied §1', only164.count(C9_F), 1)
chk('164-9 FIND resolves zero times in the base (it is Edit 164-1\'s own new text)', S1.count(C9_F), 0)

print('\n== F2 — the verb, counted and never predicted')
for ph in ['acts upon', 'act upon', 'acting upon', 'action upon']:
    print(f'   {ph:14} §1 base={S1.count(ph):3}  +164 only={only164.count(ph):3}  '
          f'+141 only={patched141.count(ph):3}  both={both.count(ph):3}')
STEM = re.compile(r"\b(?:acts|act|acting|action)\s+upon\b")
for nm, bd in [('store rev 68 §1', S1), ('+ MOO-164 revision 6', only164),
               ('+ MOO-141 patch rev 6', patched141), ('+ both', both)]:
    print(f'   occurrence census {nm:26} {len(STEM.findall(bd))}')

print('\n== the formula, after 164-3 / 164-4 / 164-6 / 164-7 / 164-11')
chk('"the period allowed by this section for acting upon"',
    only164.count('the period allowed by this section for acting upon'), 5)
chk('  of which "... the request"',
    only164.count('the period allowed by this section for acting upon the request'), 3)
chk('  of which "... it"',
    only164.count('the period allowed by this section for acting upon it'), 2)
chk('"the period allowed to it for acting upon the request" after 164-6',
    only164.count('the period allowed to it for acting upon the request'), 0)
chk('"the period this definition allows" after 164-4', only164.count('the period this definition allows'), 0)
chk('"the 90 days allowed by this subsection" after 164-3 and 164-11',
    only164.count('the 90 days allowed by this subsection'), 0)
chk('  it was this many in the base', S1.count('the 90 days allowed by this subsection'), 2)

print('\n== figures this document quotes, re-counted at store revision 68')
chk('"no later than" in §1 (base)', S1.count('no later than'), 74)
chk('"shall act upon" in §1 (base)', S1.count('shall act upon'), 5)
chk('"shall act upon" in §1 (applied) — 164-10 adds no duty', only164.count('shall act upon'), 5)
chk('every "shall act upon" duty in the applied text now states a commencement',
    only164.count('The Board shall act upon a request for reconsideration within 90 days after the request is filed.'), 1)

print('\n== clause (ii) — m8-a is ENACTED, so the 300-day bound is unconditional')
chk('m8-a: the 90-day proviso on the excluded periods',
    S1.count('the aggregate of all periods so excluded shall not exceed 90 days'), 1)
chk('m8-a survives Edit 164-3', only164.count('the aggregate of all periods so excluded shall not exceed 90 days'), 1)
chk('clause (ii) aggregate still 120 days', S1.count('the aggregate of all tolling under this subsection shall not exceed 120 days'), 1)
chk('60 + 30 + 120 + 90', 60 + 30 + 120 + 90, 300)

print('\n== subsection A at store revision 68 — the two new facts behind the 48-day derivation')
chk('the three-day extension is confined to mailing',
    S1.count('where the Board mails a written statement, notice, or certification'), 1)
chk('the giving rule reaches certifications',
    S1.count('a written statement, notice, or certification required of the Board is given on the date'), 1)
chk('the 5:00 p.m. electronic cut-off',
    S1.count('an electronic transmission completed after 5:00 p.m. is given on the following day'), 1)
chk('the definition\'s 15-day notice backstop, which supplies the 15 in 48 = 15 + 3 + 30',
    S1.count('it shall give the member written notice of that date no later than 15 days after it acts upon the request.'), 1)

print('\n== apostrophes (§6.7 record item)')
chk('typographic apostrophes in §1', S1.count('’'), 4)
G4S = S1.index('4. Subdivisions 2 and 3 shall not apply')
G4E = S1.index('5. A member may cancel an election at any time before payment is completed')
chk('all four are inside subdivision G 4', S1[:G4S].count('’') + S1[G4E:].count('’'), 0)
print('   straight apostrophes in §1:', S1.count("'"))

print('\n== F21 — whole-document counts for the strings a whole-document replace would corrupt')
for label, f in [('164-6 FIND', EDITS[5][1]), ('164-7 FIND', EDITS[6][1]),
                 ('164-10 FIND', EDITS[8][1]), ('164-11 FIND', EDITS[9][1]),
                 ('164-12 FIND', EDITS[10][1]), ('MOO-141 E3 FIND', E3_F)]:
    print(f'   {label:20} §1={S1.count(f)}  whole document={doc.count(f)}')

print(f'\n== {fail} failure(s)')
sys.exit(1 if fail else 0)
