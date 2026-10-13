# -*- coding: utf-8 -*-
"""Assert that the **document** and the **kit** carry the same edits, byte for byte.

MOO-209 F5 is the reason this file exists. A check that counts a string cannot detect a false label,
and the same is true one level up: `verify_r70_v7.py` can report 0 failures against the live bill
while the issue document — the thing the Policy Director and the board actually read — carries a
superseded FIND or READ block. **Revision 7 re-cut four edits, so that risk is at its highest here.**

This script extracts every fenced FIND and READ block from §3 of `moo164_rev7.md` and asserts that
each one appears verbatim in `verify_r70_v7.py`'s EDITS table, and that the counts match both ways.

Run: python3 check_doc_vs_kit.py
"""
import importlib.util
import re
import sys

spec = importlib.util.spec_from_file_location('v7', 'verify_r70_v7.py')
v7 = importlib.util.module_from_spec(spec)
sys.argv = ['verify_r70_v7.py', 'bill70.md']
_out = sys.stdout
sys.stdout = open('/dev/null', 'w')
try:
    spec.loader.exec_module(v7)
except SystemExit:
    pass
finally:
    sys.stdout = _out

KIT_F = {f for _, f, _ in v7.EDITS}
KIT_R = {r for _, _, r in v7.EDITS}
print(f'kit: {len(v7.EDITS)} substitutions, {len(KIT_F)} distinct FINDs, {len(KIT_R)} distinct READs')

doc = open('moo164_rev7.md', encoding='utf-8').read()
s3 = doc[doc.index('\n## 3. The patch'):doc.index('\n## 4.')]

# Pair each quoted code fence with the nearest preceding **FIND**/**READ** marker, rather than trying
# to match label and fence in one regex. The labels wrap over several quoted lines in places, and
# "READ" carries its colon inside the bold (`**READ:**`), so one regex over both is brittle.
blocks = []
markers = [(mm.start(), 'FIND' if 'FIND' in mm.group(0) else 'READ')
           for mm in re.finditer(r'\*\*[^*\n]*(?:FIND|READ)[^*\n]*\*\*', s3)]
for mm in re.finditer(r'>\n> ```\n((?:> [^\n]*\n)+?)> ```', s3):
    prior = [k for p_, k in markers if p_ < mm.start()]
    assert prior, mm.start()
    text = '\n'.join(l[2:] if l.startswith('> ') else l[1:]
                     for l in mm.group(1).rstrip('\n').split('\n'))
    blocks.append((prior[-1], text))
finds = [t for k, t in blocks if k == 'FIND']
reads = [t for k, t in blocks if k == 'READ']
print(f'document §3: {len(finds)} FIND blocks, {len(reads)} READ blocks')

fail = 0
for n, t in enumerate(finds, 1):
    if t not in KIT_F:
        fail += 1
        print(f'  [FAIL] FIND block {n} is not in the kit: {t[:90]!r}…')
for n, t in enumerate(reads, 1):
    if t not in KIT_R:
        fail += 1
        print(f'  [FAIL] READ block {n} is not in the kit: {t[:90]!r}…')
for _, f, r in v7.EDITS:
    if f not in finds:
        fail += 1
        print(f'  [FAIL] kit FIND is not in the document: {f[:90]!r}…')
    if r not in reads:
        fail += 1
        print(f'  [FAIL] kit READ is not in the document: {r[:90]!r}…')
if len(finds) != len(v7.EDITS) or len(reads) != len(v7.EDITS):
    fail += 1
    print(f'  [FAIL] block counts differ: {len(finds)} FIND / {len(reads)} READ against '
          f'{len(v7.EDITS)} kit substitutions')

print(f'{fail} mismatch(es) between the document and the apply kit')
sys.exit(1 if fail else 0)
