# -*- coding: utf-8 -*-
"""MOO-214 S5, answered: counsel's three mutations, plus a fourth, run against the REWRITTEN check.

Counsel broke `check_doc_vs_kit.py` three ways at revision 7 and the script printed "0 mismatch(es)"
and exited 0 each time. This harness reproduces all three against `moo164_rev8.md` and the rewritten
check, and asserts that each one now **fails**. A fourth mutation — a mis-stated per-edit delta —
tests S5's fix direction (e), which the revision-7 script had no equivalent of.

Everything happens in a temporary directory. Nothing in the kit is modified.

    python3 break_check_rev8.py
"""
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile

KIT = os.path.dirname(os.path.abspath(__file__))
NEED = ['verify_r72_v8.py', 'check_doc_vs_kit.py', 'bill72.md', 'moo164_rev8.md']

spec = importlib.util.spec_from_file_location('v8', os.path.join(KIT, 'verify_r72_v8.py'))
v8 = importlib.util.module_from_spec(spec)
_a, _o = sys.argv, sys.stdout
sys.argv, sys.stdout = ['verify_r72_v8.py', os.path.join(KIT, 'bill72.md')], open(os.devnull, 'w')
try:
    spec.loader.exec_module(v8)
except SystemExit:
    pass
finally:
    sys.stdout.close()
    sys.argv, sys.stdout = _a, _o
E = {lbl.split(' ')[0]: (f, r) for lbl, f, r in v8.EDITS}

# A superseded revision-7 text, used as the thing that must not be able to hide.
REV7_EXC = ('Except for the purposes of the duty of the Board under this subsection to act upon an '
            'application no later than 15 days after it acts upon the request and the duty of the '
            'Board under the definition of "final qualifying retirement date" in subsection A to '
            'give the member written notice of the member\'s final qualifying retirement date,')


def m_swap(d):
    """(c) Pairing swap: 164-8's READ <-> 164-13(b)'s READ, both of them real kit READs."""
    A, B = E['164-8'][1], E['164-13(b)'][1]
    ia, ib = d.index(A), d.index(B)
    assert ia < ib
    return d[:ia] + B + d[ia + len(A):ib] + A + d[ib + len(B):]


def m_outside(d):
    """(a)+(b) A superseded text quoted in a blockquoted fence OUTSIDE §3, with no label."""
    j = d.index('\n## 4.')
    return d[:j] + '\n\nThe exception as applied reads:\n\n> ```\n> ' + REV7_EXC + '\n> ```\n\n' + d[j:]


def m_fence(d):
    """(b) A superseded text INSIDE §3 in a plain, non-blockquoted fence."""
    j = d.index('\n## 4.')
    return (d[:j] + '\n\nFor reference the revision 7 exception was:\n\n```\n' + REV7_EXC
            + '\n```\n\n' + d[j:])


def m_delta(d):
    """(e) A per-edit delta mis-stated beside its own READ block."""
    old = '**RE-MEASURED AT REVISION 8: +564 characters'
    assert d.count(old) == 1
    return d.replace(old, '**RE-MEASURED AT REVISION 8: +999 characters')


def run(base):
    p = subprocess.run([sys.executable, 'check_doc_vs_kit.py', 'moo164_rev8.md'],
                       cwd=base, capture_output=True, text=True)
    return p.returncode, p.stdout


def main():
    base = tempfile.mkdtemp(prefix='moo214-break-rev8-')
    for f in NEED:
        shutil.copy(os.path.join(KIT, f), base)
    orig = open(os.path.join(base, 'moo164_rev8.md'), encoding='utf-8').read()

    rc, out = run(base)
    print(f'baseline (unmutated): exit {rc}')
    print('   ' + out.strip().splitlines()[-1])
    assert rc == 0, 'the unmutated document should pass'

    bad = 0
    for name, fn, want in [('S5.1 pairing swap', m_swap, 'NOT PAIRED'),
                           ('S5.2 superseded text outside §3', m_outside, 'no FIND/READ label'),
                           ('S5.3 superseded text in a plain fence', m_fence, 'no FIND/READ label'),
                           ('S5.e mis-stated per-edit delta', m_delta, 'stated delta')]:
        open(os.path.join(base, 'moo164_rev8.md'), 'w', encoding='utf-8').write(fn(orig))
        rc, out = run(base)
        caught = rc != 0 and want in out
        bad += 0 if caught else 1
        print(f'   [{"CAUGHT" if caught else "MISSED"}] {name}: exit {rc}')
        for line in out.splitlines():
            if '[FAIL]' in line:
                print('        ' + line.strip()[:150])
        open(os.path.join(base, 'moo164_rev8.md'), 'w', encoding='utf-8').write(orig)

    shutil.rmtree(base)
    print(f'{bad} mutation(s) the rewritten check still cannot see')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
