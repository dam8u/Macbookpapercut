# -*- coding: utf-8 -*-
"""Apply the MOO-164 edits to a COPY of `bill-text-s8`, at **revision 8** of the cut.

Revision 8 folds MOO-214's counsel pass: **164-7** takes S3 (the paraphrase descriptor replaced by
the determinate one the cut already coined), m2 and the Policy Director's MOO-141 §3.3
cross-reference; **164-8** takes S1 and m1; **164-13(b)** takes S2 and M1; **164-12** takes M3.
**Thirteen substitutions, delta +4,210.**

Candidates **164-9**, **164-14**, **164-15**, **164-16**, **164-17** and **164-18** are HELD and are
NOT applied here. Candidate **(c-1)** is retired and must never be applied.

>>> APPLY EVERY FIND INSIDE ENACTED §1 ONLY. <<<

Several of these strings also occur in the §0 revision narrative of the store document. A
whole-document find-and-replace WILL corrupt the record of store revision 62, 63, 65, 70 or 71. This
script slices §1 before substituting and asserts afterwards that everything outside §1 is
byte-identical. (MOO-187 finding F21 — the finding most likely to cause actual damage.)

**The edit set is now IMPORTED from `verify_r72_v8.py`, not copied into this file.** Through
revision 7 it was a copy, described in this docstring as "lifted verbatim" — which is exactly the
shape of claim MOO-209 F19 and MOO-214 S5 were about. A copy cannot be asserted identical; an
import cannot differ.

Reads `bill72.md` = `bill-text-s8` as fetched live. Writes `applied.md`. Nothing is written to the
store."""
import importlib.util
import os
import re
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else 'bill72.md'

# -- import the single source of truth, with the verifier's own output suppressed ---------------
_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('v8', os.path.join(_here, 'verify_r72_v8.py'))
_v8 = importlib.util.module_from_spec(_spec)
_argv, _stdout = sys.argv, sys.stdout
sys.argv = ['verify_r72_v8.py', SRC]
sys.stdout = open(os.devnull, 'w')
try:
    _spec.loader.exec_module(_v8)
except SystemExit:
    pass
finally:
    sys.stdout.close()
    sys.argv, sys.stdout = _argv, _stdout
EDITS = _v8.EDITS
EXPECTED_DELTA = 4210
assert _v8.fail == 0, f'verify_r72_v8.py reports {_v8.fail} failure(s) on {SRC} — fix that first'
print(f'edit set imported from verify_r72_v8.py: {len(EDITS)} substitutions, 0 verifier failures')

doc = open(SRC, encoding='utf-8').read()
i = doc.index('\n## 1.')
m = re.search(r'\n## (?!1\.)', doc[i + 5:])
j = i + 5 + m.start()
head, sec1, tail = doc[:i], doc[i:j], doc[j:]
print(f'whole document {len(doc)} chars; enacted §1 {len(sec1)} chars '
      f'(head {len(head)}, tail {len(tail)})')

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

napo = out.count('’')
out = out.replace('’', "'")
print(f'  apostrophe normalisation: {napo} typographic -> straight (non-substantive, §8 of the cut)')
print(f'  total amendment delta = {total:+d} characters')
assert total == EXPECTED_DELTA, (total, EXPECTED_DELTA)

final = head + out + tail
assert final[:len(head)] == head, 'the §0 narrative moved — abort'
assert final[len(head) + len(out):] == tail, 'text after §1 moved — abort'
open('applied.md', 'w', encoding='utf-8').write(final)
print(f'wrote applied.md: {len(doc)} -> {len(final)} chars; everything outside §1 byte-identical')
