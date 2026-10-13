# -*- coding: utf-8 -*-
"""MOO-141 — the re-cut of Edit 1's anchor, verified at store revision 69.

The wake report (Drafting Specialist, 00:30 on 13 October 2026) was cut at store revision 68.
The base moved again to store revision 69 before this re-cut was made, so every count here is
taken at revision 69, document revision 88, and nothing is carried forward from revision 68.

The dead string is kept as E1_F_R65_DEAD and asserted at 0, so the break stays visible.
Counts are taken over enacted §1 only; Edit 3's FIND resolves twice whole-document because a
sweep quotes it, which is why the §1-scoped rule exists.

Run: python3 verify_r69.py live.md
Nothing is written to the store.
"""
import hashlib, re, sys

fail = 0
def chk(label, got, want):
    global fail
    ok = got == want
    if not ok: fail += 1
    print(f'   [{"ok" if ok else "FAIL"}] {label}: {got} (expected {want})')

doc = open(sys.argv[1] if len(sys.argv) > 1 else 'live.md', encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i+5:])
S1 = doc[i:i+5+m.start()]
print(f'== base: whole document {len(doc)}; enacted §1 {len(S1)}; §1 sha256 '
      f'{hashlib.sha256(S1.encode()).hexdigest()[:16]}')

E1_F_R65_DEAD = ("every period within which a person may or must act that runs from the giving of that "
                 "statement or notice is extended by three days.</u>")
E1_F = ("every period within which a person may or must act that runs from the giving of that "
        "statement, notice, or certification is extended by three days.</u>")
SAVING = ("nothing in the preceding sentence determines the date by which the Board is required to act "
          "upon a request, to make a determination, or to give a notice or a decision, or whether the "
          "Board has performed such a duty within a period required by this section.")
# Re-cut Edit 1. The deeming sentence is unchanged from revision 6. The saving now carries 164-7's
# express exception verbatim, so the two savings in the section are not asymmetric (finding 1).
E1_R = (E1_F[:-len('</u>')] +
        " For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period "
        "begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, "
        "or where a date is fixed by reference to the month in which the Board acts, or last acts, upon "
        "a request, the Board is deemed to act upon that request, and to last act upon it, on the date "
        "on which the Board first acts upon it. Except for the purposes of the duty of the Board under "
        "subsection M to act upon an application no later than 15 days after it acts upon the request, "
        + SAVING + "</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

print('\n== anchors at store revision 69 — §1-scoped, which is the only valid uniqueness test')
chk('E1 FIND as written for store rev 65 (DEAD)', S1.count(E1_F_R65_DEAD), 0)
chk('E1 FIND as written for store rev 65 (DEAD), whole doc', doc.count(E1_F_R65_DEAD), 0)
chk('E1 FIND re-cut', S1.count(E1_F), 1)
chk('E2 FIND', S1.count(E2_F), 1)
chk('E3 FIND', S1.count(E3_F), 1)
chk('E3 FIND whole-document (expected >1: a sweep quotes it)', doc.count(E3_F), 2)

print('\n== what revision 68 changed, confirmed in the live text')
chk('three-day extension is confined to mailing', S1.count('where the Board mails a written statement, notice, or certification'), 1)
chk('express giving rule present', S1.count('is given on the date the Board mails it to the person to whom it is required to be given or transmits it electronically'), 1)
chk('5:00 p.m. electronic cut-off present', S1.count('an electronic transmission completed after 5:00 p.m. is given on the following day'), 1)

print('\n== MOO-164 is not applied to the store, so Edit 1 still has work to do')
chk('164-1 act-keyed tolling endpoint still live', S1.count('until 30 days after the Board acts upon the request'), 1)
chk('164-1 notice-keyed replacement not in the body', S1.count('until 30 days after the Board gives written notice of its decision upon the request'), 0)
chk('164-7 / Edit 1 saving not in the body', S1.count(SAVING), 0)

print('\n== the act-upon family in enacted §1')
for p, want in (('acts upon', 8), ('act upon', 9), ('acting upon', 2), ('action upon', 2),
                ('last acts upon', 1), ('first acts upon', 2)):
    chk(p, S1.count(p), want)
chk("G 4's anti-delay sentence intact", S1.count('shall not extend that aggregate'), 1)
chk("M 2's deemed-denial sentence intact", S1.count('that denial constitutes the final determination of the Board upon the reconsideration'), 1)

print('\n== applied to a copy')
def build(body):
    out = body
    for f, r in ((E2_F, E2_R), (E1_F, E1_R), (E3_F, E3_R)):
        assert out.count(f) == 1, 'FIND not unique in the scope being patched: ' + f[:50]
        out = out.replace(f, r, 1)
    return out
S1p = build(S1)
chk('§1 delta', len(S1p) - len(S1), 847)
chk('<u> open in §1 unchanged', S1p.count('<u>'), S1.count('<u>'))
chk('</u> close in §1 unchanged', S1p.count('</u>'), S1.count('</u>'))
chk('<u>/</u> balanced in §1', S1p.count('<u>') - S1p.count('</u>'), 0)
chk('first acts upon after application', S1p.count('first acts upon'), 3)
chk('E2 FIND consumed', S1p.count(E2_F), 0)
chk('one saving sentence, with one exception', S1p.count(SAVING), 1)
DESC = 'no later than 15 days after it acts upon the request'
# 2 after application: M 2's duty sentence, and Edit 1's own exception describing it. Edit 2
# consumes the third, in the definition, which is what leaves the descriptor with one referent.
chk('descriptor occurrences after application', S1p.count(DESC), 2)
chk('referents for the exception, excluding the exception itself',
    S1p.replace("Except for the purposes of the duty of the Board under subsection M to act upon an "
                "application " + DESC + ',', '').count(DESC), 1)
chk('same descriptor resolves twice before Edit 2', S1.count('no later than 15 days after it acts upon the request'), 2)
chk('exception reaches M 2 by name', S1p.count('the duty of the Board under subsection M to act upon an application'), 1)

print('\n== the 48-day worst case under MOO-164 Edit 164-1, re-derived at revision 69')
# notice due day 15 after the act; mailed, so given day 15 and the 30 days that run from the
# giving are extended by three; electronic after 5:00 p.m. gives day 16 and no extension.
print(f'   mailed      : 15 + 30 + 3 = {15+30+3}')
print(f'   e-mail >5pm : 15 + 1 + 30 = {15+1+30}')
chk('cap binds at the mailing case', max(15+30+3, 15+1+30), 48)

print('\n' + ('ALL CHECKS PASS' if not fail else f'{fail} CHECK(S) FAILED'))
sys.exit(1 if fail else 0)
