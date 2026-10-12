import re, json, sys
sys.path.insert(0,'.')
from edits import EDITS

CITES = ["§ 51.1-142.2","§ 51.1-142.4","§ 51.1-153","§ 51.1-155","§ 51.1-155.1","§ 51.1-156",
         "§ 51.1-162","§ 51.1-163","§ 51.1-165.01","§ 51.1-165.1","§ 51.1-169","§ 51.1-200",
         "§ 51.1-211","§ 51.1-300","§ 2.2-4001","§ 2.2-4021","§ 2.2-4026","§ 8.01-2","§ 2.2-3200",
         "§ 65.2-100","§ 401(a)(37)"]

def bare165(s):
    # "§ 51.1-165" not followed by ".01" or ".1"
    return len(re.findall(r'§ 51\.1-165(?!\.)', s))

def sec1(body):
    i=body.index('## 1. The bill'); j=body.index('## 2. Section-by-section summary')
    return body[i:j]

def apply_edits(body):
    out=body
    for e in EDITS:
        c=out.count(e['find'])
        assert c==e['n'], f"{e['id']}: found {c}, want {e['n']}"
        out=out.replace(e['find'], e['repl'])
    return out

def table(s):
    d={c: s.count(c) for c in CITES}
    d["§ 51.1-165 (bare)"]=bare165(s)
    d['_len']=len(s)
    d['qualifying retirement']=s.count('qualifying retirement')
    d['in service']=s.count('in service')
    return d

if __name__=='__main__':
    before=open(sys.argv[1]).read()
    after=apply_edits(before)
    b1, a1 = sec1(before), sec1(after)
    tb, ta = table(b1), table(a1)
    rows=[]
    for k in list(tb.keys()):
        if tb[k]!=ta[k] or k.startswith('§'):
            rows.append((k, tb[k], ta[k]))
    print(f"{'key':28} before  after")
    for k,x,y in rows:
        mark=' <<' if x!=y else ''
        print(f"{k:28} {x:6} {y:6}{mark}")
    print()
    print('§1 len:', len(b1), '->', len(a1), 'delta', len(a1)-len(b1))
    print('doc len:', len(before), '->', len(after), 'delta', len(after)-len(before))
    # changed-line count over §1
    bl, al = b1.split('\n'), a1.split('\n')
    assert len(bl)==len(al), 'line count changed'
    ch=[i for i,(x,y) in enumerate(zip(bl,al)) if x!=y]
    print('§1 lines changed:', len(ch), ch)
    json.dump({'before':tb,'after':ta,'len1':[len(b1),len(a1)],'lines':ch}, open('counts.json','w'), indent=1)
    open('after.md','w').write(after)
