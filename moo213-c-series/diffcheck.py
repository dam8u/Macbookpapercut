# -*- coding: utf-8 -*-
"""MOO-213 verification: diff each drafted entry's memo-ready text against its SOURCE register,
word by word, so every departure is identified rather than assumed absent.
Director's check 1 and check 6 on the MOO-213 approval."""
import re, difflib, os

MINE = open('/Users/davidmoody/.paperclip/instances/default/projects/73723db3-6591-4410-8da2-1f684e9148e4/2ad8b623-c292-4c0c-95ac-31261471bd05/Macbookpapercut/moo213-c-series/moo213-c-series.md', encoding='utf-8').read()
SRC = {
    'C4':  ('moo111-risk-section-carry-through-pass10.md', '## C4 —'),
    'C5':  ('moo111-risk-section-carry-through-pass10.md', '## C5 —'),
    'C6':  ('moo111-risk-section-carry-through-pass10.md', '## C6 —'),
    'C12': ('moo133-risk-section-carry-through-pass12.md', '### C12 —'),
    'C13': ('moo160.md', '### C13 —'),
    'C14': ('moo160.md', '### C14 —'),
    'C15': ('moo160.md', '### C15 —'),
    'C16': ('moo160.md', '### C16 —'),
    'C17': ('moo160.md', '### C17 —'),
    'C18': ('moo160.md', '### C18 —'),
}

def section(body, head, level):
    i = body.index(head)
    m = re.search(r'\n#{1,%d} ' % level, body[i + len(head):])
    return body[i: i + len(head) + (m.start() if m else len(body))]

def quoted(block):
    """the memo-ready blockquote(s): lines starting '> '"""
    out = []
    for ln in block.splitlines():
        if ln.startswith('>'):
            out.append(ln.lstrip('>').strip())
    return ' '.join(out)

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '--').replace('–', '-')
    s = s.replace('**', '').replace('*', '').replace('`', '')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)   # links -> label
    return re.sub(r'\s+', ' ', s).strip()

for entry, (fn, head) in SRC.items():
    src = open(fn, encoding='utf-8').read()
    lvl = 2 if head.startswith('## ') else 3
    s_block = section(src, head, lvl)
    m_block = section(MINE, '### %s —' % entry, 3)
    a, b = norm(quoted(s_block)), norm(quoted(m_block))
    aw, bw = a.split(), b.split()
    sm = difflib.SequenceMatcher(None, aw, bw)
    print('=' * 100)
    print('%s   source %s   (source %d words -> drafted %d words)' % (entry, fn, len(aw), len(bw)))
    print('=' * 100)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        o = ' '.join(aw[i1:i2]); n = ' '.join(bw[j1:j2])
        ctx = ' '.join(aw[max(0, i1 - 7):i1])
        print('  [%s] ...%s' % (tag.upper(), ctx))
        if o: print('      SOURCE  : %s' % o[:400])
        if n: print('      DRAFTED : %s' % n[:400])
        print()
