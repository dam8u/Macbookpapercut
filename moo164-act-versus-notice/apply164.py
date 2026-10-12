# -*- coding: utf-8 -*-
"""Apply the six MOO-164 edits to a COPY of `bill-text-s8`, at revision 5 of the cut.

>>> APPLY EVERY FIND INSIDE ENACTED §1 ONLY. <<<

Three of these strings also occur in the §0 revision narrative of the store document. A
whole-document find-and-replace WILL corrupt the record of store revision 62, 63 or 65. This script
slices §1 before substituting and asserts afterwards that everything outside §1 is byte-identical.
(MOO-187 finding F21.)

Reads `bill.md` = `bill-text-s8` as fetched live. Writes `applied.md`. Nothing is written to the
store."""
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'bill.md'
doc = open(SRC, encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
j = i + 5 + m.start()
head, sec1, tail = doc[:i], doc[i:j], doc[j:]
print(f'whole document {len(doc)} chars; enacted §1 {len(sec1)} chars '
      f'(head {len(head)}, tail {len(tail)})')

E = [
("164-1  card (b)  M 2 tolling endpoint, notice-keyed with a floor and a cap",
 "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
 "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board gives written notice of its decision upon the request to the member and to the person who filed the request, but in no case earlier than 30 days after the Board acts upon the request and in no case later than 48 days after the Board acts upon the request"),
("164-2  card (h)  G 2 exception, third limb naming the requirement",
 "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
 "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the requirement of this subdivision that notice be given no less than 30 days, and in no case less than the period allowed to the member by subsection M within which to request reconsideration of the determination, before the determination takes effect, the determination takes effect on the first day"),
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

out, total = sec1, 0
for tag, f, r in E:
    c = out.count(f)
    whole = doc.count(f)
    flag = '  <-- occurs %d times whole-document; §1-only slicing is why this is safe' % whole if whole > 1 else ''
    print(f'  {tag:70s} §1 FIND = {c}   delta = {len(r)-len(f):+d}{flag}')
    assert c == 1, tag
    out = out.replace(f, r, 1)
    total += len(r) - len(f)

napo = out.count('’')
out = out.replace('’', "'")
print(f'  apostrophe normalisation: {napo} typographic -> straight (non-substantive, §8 of the cut)')
print(f'  total amendment delta = {total:+d} characters')
assert total == 642, total

final = head + out + tail
assert final[:len(head)] == head, 'the §0 narrative moved — abort'
assert final[len(head) + len(out):] == tail, 'text after §1 moved — abort'
open('applied.md', 'w', encoding='utf-8').write(final)
print(f'wrote applied.md: {len(doc)} -> {len(final)} chars; everything outside §1 byte-identical')
