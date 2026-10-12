# -*- coding: utf-8 -*-
import re
bill = open('bill.md', encoding='utf-8').read()
patched = open('patched61.md', encoding='utf-8').read()   # store rev 61 + MOO-162 rev 5

E = [
("164-1  card (b)  M 2 tolling tail -> notice-keyed",
 "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
 "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board gives the person who filed the request written notice of its decision upon the request"),
("164-2  card (h)  G 2 exception, third limb",
 "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
 "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect, the determination takes effect on the first day"),
("164-3  card (j)  M 2 clause (ii) period formula",
 "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
 "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request"),
("164-4  card (l)/F-5  R-5 period formula",
 "within the period this definition allows for acting upon it",
 "within the period allowed by this section for acting upon it"),
("164-5  card (k)/F-9  D 1 descriptor",
 "any notice of a date required by that definition upon the Board's action upon a request",
 "any notice of a date required by that definition by reason of the Board's action upon a request"),
("164-6  conforming  G 4 period formula",
 "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
 "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
]

for base_name, base in (("live store rev 61", bill), ("store rev 61 + MOO-162 rev 5", patched)):
    print(f"\n########## applying to {base_name} ##########")
    out = base
    total = 0
    for tag, f, r in E:
        c = out.count(f)
        print(f"  {tag:46s} FIND count = {c}   delta = {len(r)-len(f):+d}")
        assert c == 1, tag
        out = out.replace(f, r, 1)
        total += len(r)-len(f)
    # apostrophe normalisation, recorded separately and folded into no amendment
    napo = out.count('’')
    out_n = out.replace('’', "'")
    print(f"  apostrophe normalisation: {napo} curly -> straight  (delta {len(out_n)-len(out):+d})")
    print(f"  total amendment delta = {total:+d} characters; final length {len(out_n)}")
    if base_name.startswith("live"):
        open('applied_live.md','w',encoding='utf-8').write(out_n)
    else:
        open('applied_both.md','w',encoding='utf-8').write(out_n)
        FINAL = out_n

print("\n########## post-application invariants (both patches applied) ##########")
F = open('applied_both.md', encoding='utf-8').read()
def cnt(s, label=None):
    print(f"  {s!r:62s} rev61 {bill.count(s):3d}  ->  final {F.count(s):3d}")
for s in ["acts upon","act upon","acting upon","action upon","last acts upon","first acts upon",
          "90 days allowed by this subsection",
          "the period allowed by this section for acting upon",
          "the period allowed to it for acting upon",
          "this definition allows for acting upon it",
          "is pending","was pending",
          "upon the Board's action upon a request",
          "by reason of the Board's action upon a request",
          "until 30 days after the Board acts upon the request",
          "30 days after the Board acts upon the request",
          "in no event later than 120 days after the determination date",
          "’"]:
    cnt(s)
print("\n  chase: every reference to a period 'this definition allows' or 'allowed by this subsection':")
for m in re.finditer(r"allowed (?:by|to)[^.;]{0,80}", F):
    print("    -", m.group(0)[:110])
