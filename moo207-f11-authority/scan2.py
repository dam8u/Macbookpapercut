import json, glob, os, re, sys

root = os.environ['PAPERCLIP_RUN_SCRATCH_DIR'] + '/cap/x'
pat = sys.argv[1]
ctx = int(sys.argv[2]) if len(sys.argv) > 2 else 800
rows = []
for f in glob.glob(root + '/*/json/*.json'):
    raw = open(f, encoding='utf-8', errors='replace').read()
    if not re.search(pat, raw):
        continue
    d = json.loads(raw)
    body = '\n'.join(o.get('text', '') for o in d.get('casebody', {}).get('opinions', []))
    cites = ', '.join(c['cite'] for c in d.get('citations', []))
    for m in re.finditer(pat, body):
        s = max(0, m.start() - ctx)
        rows.append((d.get('decision_date', ''), d.get('name_abbreviation'), cites,
                     re.sub(r'\s+', ' ', body[s:m.end() + ctx])))
rows.sort()
for date, n, c, snip in rows:
    print('###', n, '|', c, '|', date)
    print(snip)
    print()
