# -*- coding: utf-8 -*-
"""MOO-164 — re-verification at **store revision 68** (document revision 87), the thirteenth base move.

This is the first base move at which an anchor has broken. **The broken anchor is MOO-141's, not
MOO-164's.** Store revision 68 re-cast subsection A's three-day mailing sentence, so MOO-141 Edit 1's
FIND string now resolves **0** times. It is repaired below, marked `E1_F_R68`, and the old string is
kept as `E1_F_R65_DEAD` so the break is visible rather than quietly fixed.

Every count is taken over **enacted §1 only** (finding F21). Several anchors resolve twice or four times
whole-document because the revision narratives quote them; a whole-document replace would edit the
record as well as the bill.

Run: python3 verify_r68.py bill.md
Nothing is written to the store.
"""
import re
import sys

fail = 0


def chk(label, got, want):
    global fail
    ok = got == want
    if not ok:
        fail += 1
    print(f'   [{"ok" if ok else "FAIL"}] {label}: {got} (expected {want})')


doc = open(sys.argv[1] if len(sys.argv) > 1 else 'bill.md', encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
S1 = doc[i:i + 5 + m.start()]
print(f'== base: whole document {len(doc)} chars; enacted §1 {len(S1)} chars')

# ---------------------------------------------------------------- MOO-141 patch
# DEAD at store revision 68 — kept so the break is on the face of the kit.
E1_F_R65_DEAD = ("every period within which a person may or must act that runs from the giving of that "
                 "statement or notice is extended by three days.</u>")
# REPAIRED — store revision 68 re-cast the sentence: it is now confined to mailing ("where the Board
# mails a written statement, notice, or certification") and the triplet replaces "that statement or
# notice". A separate new sentence in the same paragraph supplies the electronic-giving rule.
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

print('\n== MOO-141 patch anchors at store revision 68 — the one break, named')
chk('E1 FIND as written for store rev 65 (DEAD — this is the break)', S1.count(E1_F_R65_DEAD), 0)
chk('E1 FIND repaired for store rev 68', S1.count(E1_F_R68), 1)
chk('E2 FIND', S1.count(E2_F), 1)
chk('E3 FIND', S1.count(E3_F), 1)


def build(body, e3):
    out = body
    for f, r in ((E1_F_R68, E1_R), (E2_F, E2_R), (E3_F, e3)):
        assert out.count(f) == 1, 'MOO-141 FIND not unique: ' + f[:50]
        out = out.replace(f, r, 1)
    return out


# ---------------------------------------------------------------- the six edits, revision 5
EDITS = [
 ("164-1 (card (b), REVISED at F8/F18/F23)",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the Board acts upon the request"),
 ("164-2 (card (h), REVISED at F3)",
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
]

CANDIDATES = {
 "164-7 FIND (item 130 deeming)": "the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
 "164-8 FIND (D 1 vehicle)": "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
 "164-10 FIND (F6 commencement)": "The Board shall act upon a request for reconsideration within 90 days.",
 "164-11 FIND (F12 conforming)": "Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file with the Board written notice that the period has expired.",
 "(c-1) FIND": "For the purposes of this subdivision an application for a disability retirement allowance is pending",
 "(c-2) FIND": "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.",
 "card (i) insertion point": "The Board shall act upon a request for reconsideration within 90 days.",
}

BASES = [("store rev 68", S1),
         ("store rev 68 + MOO-141 patch rev 5", build(S1, E3_R5)),
         ("store rev 68 + MOO-141 patch rev 6", build(S1, E3_R6))]

print('\n== the thirteen MOO-164 anchors, on three bases, counted over §1 only')
for name, body in BASES:
    print(f'  -- {name} ({len(body)} chars)')
    for label, f, r in EDITS:
        chk(label, body.count(f), 1)
    for label, f in CANDIDATES.items():
        chk(label, body.count(f), 1)

print('\n== delta of the six edits (revision 5 text) — expected +642 on every base')
for name, body in BASES:
    out = body
    for label, f, r in EDITS:
        assert out.count(f) == 1
        out = out.replace(f, r, 1)
    d = len(out) - len(body)
    chk(f'{name} delta', d, 642)

only164 = S1
for label, f, r in EDITS:
    only164 = only164.replace(f, r, 1)
patched141 = build(S1, E3_R6)
both = patched141
for label, f, r in EDITS:
    both = both.replace(f, r, 1)

print('\n== F2 — the verb, counted and never predicted')
for ph in ['acts upon', 'act upon', 'acting upon', 'action upon']:
    print(f'   {ph:14} §1 base={S1.count(ph):3}  +164 only={only164.count(ph):3}  '
          f'+141 only={patched141.count(ph):3}  both={both.count(ph):3}')
STEM = re.compile(r"\b(?:acts|act|acting|action)\s+upon\b")
for nm, bd in [('store rev 68 §1', S1), ('+ MOO-164 cut', only164),
               ('+ MOO-141 patch rev 6', patched141), ('+ both', both)]:
    print(f'   occurrence census {nm:26} {len(STEM.findall(bd))}')

print('\n== the formula, after 164-3 / 164-4 / 164-6')
chk('"the period allowed by this section for acting upon"', only164.count('the period allowed by this section for acting upon'), 3)
chk('  of which "... the request"', only164.count('the period allowed by this section for acting upon the request'), 2)
chk('  of which "... it" (164-4)', only164.count('the period allowed by this section for acting upon it'), 1)
chk('"the period allowed to it for acting upon the request" after 164-6', only164.count('the period allowed to it for acting upon the request'), 0)
chk('"the period this definition allows" after 164-4', only164.count('the period this definition allows'), 0)

print('\n== figures this document quotes, re-counted at store revision 68')
chk('"no later than" in §1', S1.count('no later than'), 74)
chk('"shall act upon" in §1', S1.count('shall act upon'), 5)
chk('"the 90 days allowed by this subsection" in §1 (F12 still live)', S1.count('the 90 days allowed by this subsection'), 2)
chk('  of which removed by Edit 164-3', S1.count('the 90 days allowed by this subsection') - only164.count('the 90 days allowed by this subsection'), 1)

print('\n== NEW AT STORE REVISION 68 — three facts the cut did not know')
chk('m8-a is ENACTED: clause (ii) 90-day proviso on the excluded periods',
    S1.count('the aggregate of all periods so excluded shall not exceed 90 days'), 1)
chk('the three-day extension is now confined to mailing',
    S1.count('where the Board mails a written statement, notice, or certification'), 1)
chk('new electronic-giving rule in subsection A',
    S1.count('transmits it electronically to an address that person has provided to the Board for that purpose'), 1)
chk('new 5:00 p.m. rule in subsection A',
    S1.count('an electronic transmission completed after 5:00 p.m. is given on the following day'), 1)

print('\n== question 4 — D 1\'s ordinal reference into M 2, and 164-7\'s two "preceding sentence" refs')
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
print('   every MOO-164 insertion point sits at or after offset',
      min(S1.index(f) for _, f, _ in EDITS if S1.count(f) == 1))
chk('no MOO-164 edit or candidate inserts before M 2 sentence 2',
    all(S1.index(f) > pos[1] or S1.index(f) < S1.index(M2_SENTENCES[0]) for _, f, _ in EDITS), True)

print('\n== apostrophes (§6.7 record item)')
chk('typographic apostrophes in §1', S1.count('’'), 4)
print('   straight apostrophes in §1:', S1.count("'"))

print('\n== F21 — whole-document counts, for the strings a whole-document replace would corrupt')
for label, f in [('164-6 FIND', EDITS[5][1]),
                 ('164-7 FIND', CANDIDATES['164-7 FIND (item 130 deeming)']),
                 ('164-10 / card (i) FIND', CANDIDATES['164-10 FIND (F6 commencement)']),
                 ('164-11 FIND', CANDIDATES['164-11 FIND (F12 conforming)']),
                 ('MOO-141 E3 FIND', E3_F)]:
    print(f'   {label:26} §1={S1.count(f)}  whole document={doc.count(f)}')

print(f'\n== {fail} failure(s)')
sys.exit(1 if fail else 0)
