# -*- coding: utf-8 -*-
"""MOO-214 S5 — three mutations of `moo164_rev7.md` that `check_doc_vs_kit.py` cannot see.

Each mutation leaves the document materially WRONG and the check still prints 0 mismatches.
Run from a COPY of the kit directory. This script does not modify the kit in place; it works in a
temporary directory and restores nothing, because it touches nothing outside it.

    python3 break_check_doc_vs_kit.py /path/to/moo164-act-versus-notice
"""
import os, re, shutil, subprocess, sys, tempfile

KIT = sys.argv[1] if len(sys.argv) > 1 else '.'
FENCE = r'>\n> ```\n((?:> [^\n]*\n)+?)> ```'
NEED = ['verify_r70_v7.py', 'check_doc_vs_kit.py', 'bill70.md', 'moo164_rev7.md']

REV6_164_7_EXC = ('Except for the purposes of the duty of the Board under this subsection to act '
                  'upon an application no later than 15 days after it acts upon the request,')
REV6_164_8_TAIL = '… and supersedes any notice of retirement previously filed by the member.'


def bounds(d):
    return d.index('\n## 3. The patch'), d.index('\n## 4.')


def m_swap(d):
    """Pairing swap: 164-8's READ <-> 164-13(b)'s READ. Both are kit READs, so set membership,
    both-direction membership and the 13/13 counts all still pass."""
    i, j = bounds(d)
    s3 = d[i:j]
    ms = list(re.finditer(FENCE, s3))          # 26 blocks, strict FIND/READ alternation
    a, b = 15, 25                              # 164-8 READ, 164-13(b) READ
    sa, sb = ms[a].span(1), ms[b].span(1)
    A, B = s3[sa[0]:sa[1]], s3[sb[0]:sb[1]]
    s3 = s3[:sa[0]] + B + s3[sa[1]:sb[0]] + A + s3[sb[1]:]
    return d[:i] + s3 + d[j:]


def m_outside(d):
    """A superseded revision-6 READ quoted verbatim outside §3. The script slices §3 only."""
    j = d.index('\n## 4.')
    return d[:j] + '\n\nThe exception as applied reads:\n\n> ```\n> ' + REV6_164_7_EXC + '\n> ```\n\n' + d[j:]


def m_fence(d):
    """A superseded READ inside §3 in a plain (non-blockquoted) fence. The regex requires a
    blockquoted fence preceded by a bare `>` line, so this block is never extracted."""
    j = d.index('\n## 4.')
    return (d[:j] + '\n\nFor reference the revision 6 tail of 164-8 was:\n\n```\n'
            + REV6_164_8_TAIL + '\n```\n\n' + d[j:])


def main():
    base = tempfile.mkdtemp(prefix='moo214-break-')
    for f in NEED:
        shutil.copy(os.path.join(KIT, f), base)
    orig = open(os.path.join(base, 'moo164_rev7.md'), encoding='utf-8').read()

    # Baseline fence census: §3 already holds a block the extractor cannot see.
    i, j = bounds(orig)
    s3 = orig[i:j]
    total = len(re.findall(r'```', s3)) // 2
    seen = len(re.findall(FENCE, s3))
    print(f'[census] §3 fences: {total} present, {seen} captured, {total - seen} invisible')
    print(f'[census] fences outside §3, never scanned: {len(re.findall(chr(96)*3, orig[:i] + orig[j:])) // 2}')

    for name, fn in [('pairing swap', m_swap), ('block outside §3', m_outside),
                     ('plain code fence in §3', m_fence)]:
        open(os.path.join(base, 'moo164_rev7.md'), 'w', encoding='utf-8').write(fn(orig))
        r = subprocess.run([sys.executable, 'check_doc_vs_kit.py'], cwd=base,
                           capture_output=True, text=True)
        tail = r.stdout.strip().splitlines()[-1]
        print(f'[{name:24s}] exit={r.returncode}  {tail}')
    shutil.rmtree(base)


main()
