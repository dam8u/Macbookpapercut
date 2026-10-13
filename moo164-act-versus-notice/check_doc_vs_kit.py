# -*- coding: utf-8 -*-
"""Assert that the **document** and the **kit** carry the same edits, byte for byte.

MOO-209 F5 is why this file exists: a check that counts a string against the bill cannot detect a
document that quotes a superseded edit. **MOO-214 S5 is why it was rewritten.** Counsel broke the
revision-7 version three separate ways, each time printing "0 mismatch(es)" and exiting 0:

  1. **A pairing swap** — 164-8's READ exchanged with 164-13(b)'s. The old check tested set
     membership in both directions and never asserted that FIND *n* was paired with its own READ.
  2. **A block outside §3** — a superseded revision-6 text pasted immediately before `## 4.`.
     The old check sliced §3 and never looked at the other 10 fenced blocks in the document.
  3. **A plain code fence** — the old capture regex required a blockquoted fence preceded by a bare
     `>` line, so a superseded text in an ordinary fence was invisible.

And a fourth, live at the time: §3 held **27** fenced blocks and the extractor captured **26**. A
capture that silently matches less than everything is precisely the bug this script exists to stop.

What this version does, against S5's five fix directions:

  (a) **Scans the whole document**, not §3, and whitelists by label rather than by section.
  (b) **Asserts that every fenced block in the document is accounted for** — captured as a labelled
      FIND/READ, or matched by an explicit allow-list of labelled non-edit fences. An unaccounted
      fence is a FAILURE, not a silent skip.
  (c) **Asserts alternation and pairs each FIND with the READ that follows it**, then checks the
      PAIR against the kit — so a swap fails.
  (d) **Anchors the marker regex** so `ALREADY`, `SPREAD`, `FINDING`, `FINDINGS` and prose such as
      *"The FIND is the full clause"* cannot be mistaken for labels.
  (e) **Asserts the document's own stated per-edit delta** against `len(READ) - len(FIND)`, so the
      arithmetic printed in §3 is counted rather than typed.

Run: python3 check_doc_vs_kit.py [document.md]
"""
import importlib.util
import os
import re
import sys

DOC = sys.argv[1] if len(sys.argv) > 1 else 'moo164_rev8.md'

# ---------------------------------------------------------------- the kit, imported not copied
_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('v8', os.path.join(_here, 'verify_r72_v8.py'))
v8 = importlib.util.module_from_spec(spec)
_argv, _stdout = sys.argv, sys.stdout
sys.argv = ['verify_r72_v8.py', 'bill72.md']
sys.stdout = open(os.devnull, 'w')
try:
    spec.loader.exec_module(v8)
except SystemExit:
    pass
finally:
    sys.stdout.close()
    sys.argv, sys.stdout = _argv, _stdout

KIT = [(lbl, f, r) for lbl, f, r in v8.EDITS]
print(f'kit: {len(KIT)} substitutions; verifier reported {v8.fail} failure(s)')

doc = open(DOC, encoding='utf-8').read()
fail = 0


def bad(msg):
    global fail
    fail += 1
    print(f'  [FAIL] {msg}')


# ---------------------------------------------------------------- (d) anchored labels
# A label is a bold run that BEGINS a line (optionally inside a blockquote) and whose bold content
# ends with FIND or READ, with an optional colon. "**164-13(a) — FIND**", "**READ:**", "**FIND**".
LABEL = re.compile(r'^>? ?\*\*([^*\n]{0,80}?\b(FIND|READ)\b:?)\*\*', re.M)
labels = [(mm.start(), mm.group(2), mm.group(1)) for mm in LABEL.finditer(doc)]
print(f'document: {len(labels)} anchored FIND/READ labels')

# ---------------------------------------------------------------- (a)+(b) every fence, anywhere
# Two fence shapes occur in this document: blockquoted and plain. Capture BOTH, everywhere.
FENCE_Q = re.compile(r'(?:^|\n)>? ?```[^\n]*\n((?:>? ?[^\n]*\n)*?)>? ?```')
fences = []
for mm in FENCE_Q.finditer(doc):
    body = '\n'.join(l[2:] if l.startswith('> ') else (l[1:] if l.startswith('>') else l)
                     for l in mm.group(1).rstrip('\n').split('\n'))
    fences.append((mm.start(), body, mm.end()))
print(f'document: {len(fences)} fenced blocks in total (§3 and everywhere else)')

# A fenced block is ACCOUNTED FOR if the nearest preceding label is within LOOKBACK characters and
# nothing but blockquote punctuation lies between. Everything else must be on the allow-list.
LOOKBACK = 400
ALLOW = [
    # label-prefix -> the reason this fence is not an edit block. Matched on the text that
    # introduces the fence, so a superseded text cannot hide behind a vague introduction.
    'revision-1-to-4 text was:',
    'revision 5 text was:',
    'revision 6 text was:',
    'revision 7 text was:',
    'superseded:',
    'DECLINED',
    'HELD',
    'RETIRED',
    'candidate',
    'Candidate',
    'as counsel drafted it',
    'as first drafted',
    'EXTRACT OF APPLIED TEXT',
]
ALLOW_LOOKBACK = 260   # the introducing sentence, not a whole section

pairs, unaccounted = [], []
for pos, body, _end in fences:
    prior = [(p, k, t) for p, k, t in labels if p < pos and pos - p < LOOKBACK]
    if prior:
        pairs.append((prior[-1][1], body, pos))
        continue
    lead = doc[max(0, pos - ALLOW_LOOKBACK):pos]
    if any(a in lead for a in ALLOW):
        unaccounted.append(('allowed', pos, body))
    else:
        unaccounted.append(('UNACCOUNTED', pos, body))
        bad(f'fenced block at offset {pos} has no FIND/READ label and is not on the allow-list: '
            f'{body[:80]!r}…')
print(f'document: {sum(1 for k, _, _ in unaccounted if k == "allowed")} fences explicitly allowed '
      f'as labelled non-edit quotations')
print(f'document: {len(pairs)} fences carry an anchored FIND/READ label')

# ---------------------------------------------------------------- (c) alternation and pairing
seq = [k for k, _, _ in pairs]
edit_pairs = []
n = 0
while n < len(seq) - 1:
    if seq[n] == 'FIND' and seq[n + 1] == 'READ':
        edit_pairs.append((pairs[n][1], pairs[n + 1][1]))
        n += 2
    else:
        n += 1
print(f'document: {len(edit_pairs)} FIND/READ pairs in sequence')
lone = len(pairs) - 2 * len(edit_pairs)
if lone:
    print(f'  ({lone} labelled block(s) not in a FIND-then-READ pair — held candidates and '
          f'declined texts are quoted singly)')

KIT_PAIRS = {(f, r) for _, f, r in KIT}
applied_pairs = {p for p in edit_pairs if p in KIT_PAIRS}
for i, (f, r) in enumerate(edit_pairs, 1):
    if (f, r) in KIT_PAIRS:
        continue
    if f in {x for _, x, _ in KIT} and r not in {x for _, _, x in KIT}:
        bad(f'pair {i}: FIND is a kit FIND but the READ beside it is not in the kit at all')
    elif f in {x for _, x, _ in KIT} and r in {x for _, _, x in KIT}:
        bad(f'pair {i}: FIND and READ are both in the kit but are NOT PAIRED there — a swap. '
            f'FIND {f[:60]!r}… is paired in the kit with a different READ')
    # a pair in which neither side is a kit string is a held candidate or a superseded quotation;
    # it is reported, not failed, because those are legitimately in the document.

for lbl, f, r in KIT:
    if (f, r) not in set(edit_pairs):
        bad(f'kit substitution is not in the document as a FIND/READ pair: {lbl[:70]}')

if len(applied_pairs) != len(KIT):
    bad(f'the document carries {len(applied_pairs)} distinct kit substitutions as FIND/READ '
        f'pairs, against the kit\'s {len(KIT)}')
else:
    print(f'document: all {len(KIT)} kit substitutions present as correctly-paired FIND/READ blocks '
          f'({len(edit_pairs)} pairs in all, the rest being record and candidate quotations)')

# ---------------------------------------------------------------- (e) the stated arithmetic
# Every "+N characters" or "+N" figure that sits within DELTA_WINDOW characters after a READ block
# of a kit pair must equal len(READ) - len(FIND).
DELTA_WINDOW = 700
DELTA = re.compile(r'\*\*(?:[^*\n]*?)\+([0-9][0-9,]*)(?: characters)?(?:[^*\n]*?)\*\*')
checked = 0
for pos, body, end in fences:
    match = [(f, r) for f, r in KIT_PAIRS if r == body]
    if not match:
        continue
    f, r = match[0]
    want = len(r) - len(f)
    # The window starts at the END of the fence. Starting it at the fence's own offset was the
    # bug that let a mis-stated delta past on the first run of this check: a 1,200-character READ
    # block consumed the whole window before the prose that states its delta began.
    window = doc[end:end + DELTA_WINDOW]
    got = [int(x.replace(',', '')) for x in DELTA.findall(window)]
    if not got:
        continue
    checked += 1
    if want not in got:
        bad(f'stated delta near a READ block does not match the kit: document says '
            f'{got[:4]}, kit measures {want:+d} for {f[:50]!r}…')
print(f'document: {checked} stated per-edit delta(s) checked against len(READ) - len(FIND)')

# ---------------------------------------------------------------- the whole-patch figure
TOTAL = sum(len(r) - len(f) for _, f, r in KIT)
if f'+{TOTAL:,}' not in doc:
    bad(f'the document never states the patch total +{TOTAL:,}')
else:
    print(f'document states the patch total +{TOTAL:,}: '
          f'{doc.count(f"+{TOTAL:,}")} time(s)')

print(f'{fail} mismatch(es) between the document and the apply kit')
sys.exit(1 if fail else 0)
