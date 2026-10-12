# -*- coding: utf-8 -*-
"""MOO-187 addendum checks — the revision-3/4 pass, at store revision 63/64.

Reproduces every count the addendum relies on. Counts are over **enacted §1 only**, which is the
convention §13.1 of the cut adopts and the right one — see finding F21, which is about the fact that
the committed `verify_r6.py` does not follow it.

Usage:
    python3 check187_r63.py bill.md          # bill.md = bill-text-s8 body, fetched live (store rev 63+)

Groups:
  A. the 21 occurrences and the two new ones                          -> N12, §13.3
  B. whether Edit 1's deeming can collide with occurrence 21          -> N12
  C. the six FINDs and both new candidates, §1 vs whole document      -> F21
  D. candidate 164-7 against MOO-141 Edit 1, limb by limb             -> F19, F20
  E. the §7.2 `acts upon` row on the §1 basis                         -> F2
  F. §13.4's three grounds                                            -> N13
  G. §13.5's vehicle gap                                              -> N14
  H. §13.8's two new Decision-2 sites                                 -> N17
  I. §13.9's ordinal reference and item 131's antecedent              -> N16, F25
  J. F6 and F12 at store revision 63                                  -> F6, F12
"""
import re
import sys

doc = open(sys.argv[1] if len(sys.argv) > 1 else 'bill.md', encoding='utf-8').read()
lines = doc.split('\n')
s = next(i for i, l in enumerate(lines) if l.startswith('## 1. The bill'))
e = next(i for i, l in enumerate(lines) if l.startswith('## 2. Section-by-section'))
sec1 = '\n'.join(lines[s:e])
print(f"base: {len(doc)} chars whole, enacted §1 = {len(sec1)} chars")

# ---- A ----------------------------------------------------------------
occ = list(re.finditer(r"\b(acts?|acting|action)\s+upon\b", sec1))
print(f"\n[A] act/acts/acting/action upon in §1: {len(occ)}  (§13.3 claims 21)")
for p, want in (('acts upon', 8), ('act upon', 9), ('acting upon', 2), ('action upon', 2)):
    got = sec1.count(p)
    print(f"    {p!r:15s} {got:2d}  (§13.3 claims {want})  {'ok' if got == want else 'MISMATCH'}")
assert len(occ) == 21, len(occ)
print("    the two new occurrences:")
for n, m in enumerate(occ, 1):
    c = sec1[max(0, m.start() - 55):m.start() + 65].replace('\n', ' ')
    if 'does not act upon a request for reconsideration within the 90' in c or \
       'does not act upon the request within 30 days' in c:
        print(f"      #{n} …{c}…")

# ---- B ----------------------------------------------------------------
print("\n[B] can Edit 1's deeming reach occurrence 21? Its trigger needs a period measured from, or")
print("    beginning/ending on, the Board's act, or a date fixed by the month of the Board's act.")
o21 = "Where the Board does not act upon the request within 30 days after that notice is filed, the request is denied on the first day after the expiration of those 30 days"
assert sec1.count(o21) == 1
print(f"    occurrence 21's 30 days run from: 'after that notice is filed' -> the MEMBER's filing")
print(f"    occurrence 21's date runs from:   'the expiration of those 30 days' -> the MEMBER's filing")
print("    => Edit 1's trigger is not met; no collision. (N12)")

# ---- C ----------------------------------------------------------------
FINDS = {
 '164-1': "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
 '164-2': "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
 '164-3': "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
 '164-4': "within the period this definition allows for acting upon it",
 '164-5': "any notice of a date required by that definition upon the Board's action upon a request",
 '164-6': "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
 'MOO-141 E3': "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request",
 'cand 164-7': "the request is denied on the first day after the expiration of those 30 days, and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
 'cand 164-8': "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
 'cand 164-8 short': "and the Board shall state every such delay in the report required by subsection J.",
 'M 2 90-day sentence': "The Board shall act upon a request for reconsideration within 90 days.",
}
print(f"\n[C] anchors: §1 vs whole document  (F21 — a whole-document replace is unsafe where whole > 1)")
for k, v in FINDS.items():
    a, b = sec1.count(v), doc.count(v)
    flag = '  <-- whole-document replace UNSAFE' if b > 1 else ''
    print(f"    {k:20s} §1={a}  whole={b}{flag}")
    if k != 'cand 164-8 short':
        assert a == 1, k
assert sec1.count(FINDS['cand 164-8 short']) == 2, "the short anchor should resolve twice (§13.1's lesson)"

# ---- D ----------------------------------------------------------------
E1 = ("where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, "
      "or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request")
E1_SAVE = ("Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, "
           "to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty "
           "within a period required by this section.")
C7 = ("under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request")
C7_SAVE = ("Nothing in the preceding sentence relieves the Board of the duty to act upon a request for reconsideration, "
           "or determines whether the Board has acted upon a request within the period allowed by this section.")
LIMB_A = "a period begins or ends upon, or is measured from"
LIMB_B = "a date is fixed by reference to the month in which the Board acts"
print("\n[D] candidate 164-7 against MOO-141 Edit 1  (F19, F20)")
print(f"    Edit 1 trigger limb A present: {LIMB_A in E1}")
print(f"    Edit 1 trigger limb B present: {LIMB_B in E1}")
print(f"    164-7  trigger limb A present: {LIMB_A in C7}")
print(f"    164-7  trigger limb B present: {LIMB_B in C7}   <-- F19: limb B is DROPPED")
print(f"    savings identical: {E1_SAVE == C7_SAVE}   <-- F20: they are not")
assert LIMB_B in E1 and LIMB_B not in C7
assert E1_SAVE != C7_SAVE
print("    limb B is the only thing in Edit 1 that reaches the definition's reset:")
reset = "the first day of the second month following the month in which the Board last acts upon a request the filing of which tolled that period"
print(f"      reset sentence in §1: {sec1.count(reset)} occurrence(s)")
assert sec1.count(reset) == 1

# ---- E ----------------------------------------------------------------
E1_F = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_R = ("every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. "
        "For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, "
        "the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or "
        "last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board "
        "first acts upon it. " + E1_SAVE + "</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"
READS = {
 '164-1': FINDS['164-1'].replace("until 30 days after the Board acts upon the request",
   "until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after the Board gives the person who filed the request written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request"),
 '164-2': "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect, the determination takes effect on the first day",
 '164-3': "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request",
 '164-4': "within the period allowed by this section for acting upon it",
 '164-5': "any notice of a date required by that definition by reason of the Board's action upon a request",
 '164-6': "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate",
}
out, delta = sec1, 0
for f, r in ((E1_F, E1_R), (E2_F, E2_R), (FINDS['MOO-141 E3'], E3_R6)):
    assert out.count(f) == 1
    out = out.replace(f, r, 1)
for k in ('164-1', '164-2', '164-3', '164-4', '164-5', '164-6'):
    f, r = FINDS[k], READS[k]
    assert out.count(f) == 1, k
    out = out.replace(f, r, 1)
    delta += len(r) - len(f)
print(f"\n[E] §1-basis amendment delta: {delta:+d}  (§13.1 claims +490)")
assert delta == 490, delta
print(f"    `acts upon` over §1: before={sec1.count('acts upon')}  after both patches={out.count('acts upon')}"
      f"   <-- F2: §7.2 predicts 7")
assert out.count('acts upon') == 9

# ---- F ----------------------------------------------------------------
print("\n[F] §13.4's three grounds  (N13)")
print(f"    'first required' in §1: {sec1.count('first required')}")
late = "Where the Board gives that written statement, any notice of a later approved date required by that definition, or any notice of a date required by that definition upon the Board's action upon a request, later than the time required by that definition"
print(f"    lateness sentence with its three limbs, verbatim: {sec1.count(late)} occurrence(s)")
assert sec1.count('first required') == 1 and sec1.count(late) == 1

# ---- G ----------------------------------------------------------------
d1 = sec1[sec1.index('<u>**D. 1.**'):]
d1 = d1[:d1.index('<u>2. The Board shall')] if '<u>2. The Board shall' in d1 else d1[:26000]
print(f"\n[G] §13.5's vehicle gap: subdivision D 1 is {len(d1)} chars  (N14)")
for w in ('amend', 'withdraw', 'replacing', 'replace', 'substitute', 'revoke', 'rescind'):
    n = len(re.findall(w, d1))
    print(f"    {w!r:12s} {n}")
    assert n == 0, w

# ---- H ----------------------------------------------------------------
print("\n[H] §13.8's two new Decision-2 sites  (N17)")
for p in ("no later than 30 days after the date on which the certification is given to the member",
          "does not expire before the thirtieth day after the notice is given"):
    print(f"    {sec1.count(p)}  {p!r}")
    assert sec1.count(p) == 1

# ---- I ----------------------------------------------------------------
print("\n[I] §13.9's ordinal reference and item 131's antecedent  (N16, F25)")
print(f"    'the second sentence of subdivision M 2' in §1: {sec1.count('the second sentence of subdivision M 2')}")
print(f"    'such case decision' in §1: {sec1.count('such case decision')}")
m2 = sec1[sec1.index('<u>2. A member, retiree'):]
m2 = m2[:m2.index('<u>3. The sentence of subsection B')]
sents = [x for x in re.split(r'(?<=\.)\s+(?=[A-Z"(])', m2) if x.strip() not in ('<u>2.',)]
print(f"    M 2 sentence count: {len(sents)}; sentence 2 is the deeming sentence: "
      f"{sents[1].startswith('Every determination')}")
print(f"    item 124's two enacted sentences are M 2 sentences 4 and 5: "
      f"{sents[3].startswith('Where the Board does not act upon a request for reconsideration')} / "
      f"{sents[4].startswith('Where the Board does not act upon the request within 30 days')}")
assert sents[1].startswith('Every determination')

# ---- J ----------------------------------------------------------------
print("\n[J] F6 and F12 at this base")
print(f"    'act upon a request for reconsideration within 90 days.'       {sec1.count('act upon a request for reconsideration within 90 days.')}")
print(f"    'act upon a request for reconsideration within 90 days after'  {sec1.count('act upon a request for reconsideration within 90 days after')}"
      "   <-- F6: no commencement is stated")
print(f"    'the 90 days allowed by this subsection' in §1: {sec1.count('the 90 days allowed by this subsection')}"
      "   <-- F12: realised; Edit 164-3 removes one of the two")
print(f"    'the period allowed by this section for acting upon' after both patches: "
      f"{out.count('the period allowed by this section for acting upon')}")
print(f"    'the 90 days allowed by this subsection' after both patches: "
      f"{out.count('the 90 days allowed by this subsection')}   <-- two formulas, one concept, inside M 2")
print(f"\n    'no later than' in §1: {len(re.findall('no later than', sec1))}  (the document says 72)")
print(f"    'shall act upon' in §1: {len(re.findall('shall act upon', sec1))}  (the document says 5 — correct)")

print("\nAll assertions passed.")
