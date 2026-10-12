# -*- coding: utf-8 -*-
"""MOO-164 revision 5 — re-verification at **store revision 65**, the twelfth base move, with the
counsel findings from MOO-187 applied.

Every count is taken over **enacted §1 only**. Store revisions 62-65 quote three of these anchor
strings in the §0 narrative, so a whole-document count returns 2 for those three (finding F21).

Run: python3 verify_r65.py bill.md
Nothing is written to the store."""
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
E1_F = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_R = ("every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. "
        "For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, "
        "the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or "
        "last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board "
        "first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to "
        "make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by "
        "this section.</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R5 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

def build(body, e3):
    out = body
    for f, r in ((E1_F, E1_R), (E2_F, E2_R), (E3_F, e3)):
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

BASES = [("store rev 65", S1),
         ("store rev 65 + MOO-141 patch rev 5", build(S1, E3_R5)),
         ("store rev 65 + MOO-141 patch rev 6", build(S1, E3_R6))]

print('\n== anchors: six edits + held candidates, on three bases, counted over §1 only')
for name, body in BASES:
    print(f'  -- {name} ({len(body)} chars)')
    for label, f, r in EDITS:
        chk(label, body.count(f), 1)
    for label, f in CANDIDATES.items():
        chk(label, body.count(f), 1)

print('\n== delta of the six edits (revision 5 text)')
for name, body in BASES:
    out = body
    for label, f, r in EDITS:
        assert out.count(f) == 1
        out = out.replace(f, r, 1)
    print(f'   {name}: {len(body)} -> {len(out)}  delta = +{len(out) - len(body)}')

print('\n== F2 — `acts upon` counted, not predicted')
patched141 = build(S1, E3_R6)
both = patched141
for label, f, r in EDITS:
    both = both.replace(f, r, 1)
only164 = S1
for label, f, r in EDITS:
    only164 = only164.replace(f, r, 1)
for ph in ['acts upon', 'act upon', 'acting upon', 'action upon']:
    print(f'   {ph:14} §1 base={S1.count(ph):3}  +164 only={only164.count(ph):3}  +141 only={patched141.count(ph):3}  both={both.count(ph):3}')

print('\n== F13/F24 — the "period allowed" / "time allowed" sweep, counted')
for ph in ['the period allowed', 'the time allowed']:
    print(f'   {ph}: §1 = {S1.count(ph)}')
for mm in re.finditer(r'the (?:period|time) allowed[^.;,]{0,80}', S1):
    print('     ·', mm.group(0)[:95])

print('\n== F15 — figures the document quotes')
chk('"no later than" in §1', S1.count('no later than'), 74)
chk('"shall act upon" in §1', S1.count('shall act upon'), 5)
chk('"the 90 days allowed by this subsection" in §1 (F12, realised)', S1.count('the 90 days allowed by this subsection'), 2)
chk('formula stem "the period allowed by this section for acting upon" after 164-3/164-4/164-6', only164.count('the period allowed by this section for acting upon'), 3)
chk('  of which "... the request"', only164.count('the period allowed by this section for acting upon the request'), 2)
chk('  of which "... it" (164-4, antecedent is a request)', only164.count('the period allowed by this section for acting upon it'), 1)
chk('"the period allowed to it for acting upon the request" after 164-6', only164.count('the period allowed to it for acting upon the request'), 0)
chk('"the period this definition allows" after 164-4', only164.count('the period this definition allows'), 0)

print('\n== occurrence census of the verb, base and after both patches')
STEM = re.compile(r"\b(?:acts|act|acting|action)\s+upon\b")
for nm, bd in [('store rev 65 §1', S1), ('+ MOO-164 cut', only164), ('+ MOO-141 patch rev 6', patched141), ('+ both', both)]:
    print(f'   {nm:26} {len(STEM.findall(bd))}')

print('\n== F16 — where item 46 sits, counted from the end of G 2')
g2 = S1[S1.index('### G. Determination'):] if '### G. Determination' in S1 else None
k = S1.find('Nothing in this subdivision prevents the payment of a retirement allowance')
seg = S1[k:]
tail = seg[:seg.find('\n')] if '\n' in seg else seg
print('   item 46 sentence located at §1 offset', k)

print('\n== F21 — whole-document vs §1 counts for the three strings that now resolve twice')
for label, f in [('164-6 FIND', EDITS[5][1]), ('164-7 FIND', CANDIDATES['164-7 FIND (item 130 deeming)']),
                 ('MOO-141 E3 FIND', E3_F), ('M 2 90-day sentence', CANDIDATES['164-10 FIND (F6 commencement)'])]:
    print(f'   {label:22} §1={S1.count(f)}  whole document={doc.count(f)}')

print('\n== apostrophes (§6.7 record item)')
print('   typographic apostrophes in §1:', S1.count('’'), '  straight:', S1.count("'"))

print(f'\n== {fail} failure(s)')
sys.exit(1 if fail else 0)
