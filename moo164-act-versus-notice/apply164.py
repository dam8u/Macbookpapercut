# -*- coding: utf-8 -*-
"""Apply the MOO-164 edits to a COPY of `bill-text-s8`, at **revision 7** of the cut.

Revision 7 folds MOO-209's counsel pass: **164-7** takes F1's extended exception, **164-8** takes
F2 and F3, **164-12** takes F6, and **164-13** is new — F4's conforming disclosure amendment, in two
substitutions inside one sentence of subdivision D 1. **Thirteen substitutions, delta +3,375.**

Candidates **164-9** (MOO-204's answer) and **164-14** (MOO-209 F10, the Director's answer) are HELD
and are NOT applied here. Candidate **(c-1)** is retired and must never be applied.

>>> APPLY EVERY FIND INSIDE ENACTED §1 ONLY. <<<

Several of these strings also occur in the §0 revision narrative of the store document. A
whole-document find-and-replace WILL corrupt the record of store revision 62, 63, 65 or 70. This
script slices §1 before substituting and asserts afterwards that everything outside §1 is
byte-identical. (MOO-187 finding F21 — the finding most likely to cause actual damage.)

The edit set is lifted verbatim from `verify_r70_v7.py` so the check and the applier cannot drift.

Reads `bill70.md` = `bill-text-s8` as fetched live. Writes `applied.md`. Nothing is written to the
store."""
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'bill70.md'
doc = open(SRC, encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
j = i + 5 + m.start()
head, sec1, tail = doc[:i], doc[i:j], doc[j:]
print(f'whole document {len(doc)} chars; enacted §1 {len(sec1)} chars '
      f'(head {len(head)}, tail {len(tail)})')

SAVING = ("nothing in the preceding sentence determines the date by which the Board is required to act "
          "upon a request, to make a determination, or to give a notice or a decision, or whether the "
          "Board has performed such a duty within a period required by this section.")

E164_7_EXC = ('Except for the purposes of the duty of the Board under this subsection to act upon an '
              'application no later than 15 days after it acts upon the request and the duty of the '
              'Board under the definition of "final qualifying retirement date" in subsection A to '
              'give the member written notice of the member\'s final qualifying retirement date,')
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
 ("164-7 RE-CUT at revision 7 on MOO-209 F1 — the exception now names R-6's notice duty as well",
  "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection.",
  "and that denial constitutes the final determination of the Board upon the reconsideration and a case decision as defined in § 2.2-4001 for the purposes of this subsection. Where a request is denied by operation of the preceding sentence, or where the Board does not act upon a request under the definition of \"final qualifying retirement date\" in subsection A within the period allowed by this section for acting upon it, the Board is deemed, for the purposes of every provision of this section and of subdivision B 4 f of § 51.1-142.2 under which a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon the request, or under which a date is fixed by reference to the month in which the Board acts, or last acts, upon the request, to act upon the request, and to last act upon it, on the date of that denial or, as the case may be, on the day after the expiration of that period. "
  + E164_7_EXC + " " + SAVING),
 ("164-8 RE-CUT at revision 7 on MOO-209 F2 and F3 — surplusage out, the supersession confined",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J.",
  "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J. Where the Board gives any notice described in the preceding sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives the notice; and a notice so filed is filed within the period allowed by this subdivision and supersedes any notice of retirement previously filed by the member, except that no notice may be filed under this sentence after the member's retirement has taken effect."),
 ("164-13(a) NEW at revision 7 on MOO-209 F4 — the disclosure duty reaches the third document",
  "The Board shall state, in the written statement required by that definition and in every notice of a later approved date required by that definition, (i)",
  "The Board shall state, in the written statement required by that definition, in every notice of a later approved date required by that definition, and in every notice of a date required by that definition by reason of the Board's action upon a request, (i)"),
 ("164-13(b) NEW at revision 7 on MOO-209 F4 — clause (iv), the window the member is now told about",
  "; and (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days.",
  "; (iii) that where the Board mails the statement or notice, every period that runs from the giving of it is extended by three days; and (iv) that where the Board gives a notice described in this sentence after the expiration of the period allowed by this subdivision for filing the notice of retirement required by § 51.1-153, the member may file that notice of retirement, or a notice replacing a notice of retirement already filed by the member, no later than 30 days after the Board gives that notice, and that no such notice may be filed after the member's retirement has taken effect."),
 ("164-10 (F6 commencement)",
  "The Board shall act upon a request for reconsideration within 90 days.",
  "The Board shall act upon a request for reconsideration within 90 days after the request is filed."),
 ("164-11 (F12 conforming)",
  "Where the Board does not act upon a request for reconsideration within the 90 days allowed by this subsection, the person who filed the request may file",
  "Where the Board does not act upon a request for reconsideration within the period allowed by this section for acting upon the request, the person who filed the request may file"),
 ("164-12 RE-CUT at revision 7 on MOO-209 F6 — the notwithstanding deleted",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending.",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending. For the purposes of this subdivision, such an application is pending from the date on which the member files it until the date on which the Board grants or denies it."),
]

out, total = sec1, 0
for tag, f, r in EDITS:
    c = out.count(f)
    whole = doc.count(f)
    flag = ('  <-- occurs %d times whole-document; §1-only slicing is why this is safe' % whole
            if whole > 1 else '')
    print(f'  {tag[:64]:64s} §1 FIND = {c}   delta = {len(r)-len(f):+d}{flag}')
    assert c == 1, tag
    out = out.replace(f, r, 1)
    total += len(r) - len(f)

napo = out.count('\u2019')
out = out.replace('\u2019', "'")
print(f'  apostrophe normalisation: {napo} typographic -> straight (non-substantive, §8 of the cut)')
print(f'  total amendment delta = {total:+d} characters')
assert total == 3375, total

final = head + out + tail
assert final[:len(head)] == head, 'the §0 narrative moved — abort'
assert final[len(head) + len(out):] == tail, 'text after §1 moved — abort'
open('applied.md', 'w', encoding='utf-8').write(final)
print(f'wrote applied.md: {len(doc)} -> {len(final)} chars; everything outside §1 byte-identical')
