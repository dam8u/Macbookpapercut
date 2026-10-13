import json, glob, os, re, sys

root = os.environ['PAPERCLIP_RUN_SCRATCH_DIR'] + '/cap/x'
namepat = sys.argv[1]
vol = sys.argv[2] if len(sys.argv) > 2 else '*'
anchor = sys.argv[3] if len(sys.argv) > 3 else 'section 52'
span = int(sys.argv[4]) if len(sys.argv) > 4 else 6000
for f in glob.glob(root + '/' + vol + '/json/*.json'):
    d = json.load(open(f, encoding='utf-8', errors='replace'))
    n = d.get('name_abbreviation') or ''
    if not re.search(namepat, n, re.I):
        continue
    body = '\n'.join(o.get('text', '') for o in d.get('casebody', {}).get('opinions', []))
    cites = ', '.join(c['cite'] for c in d.get('citations', []))
    print('=' * 10, n, '|', cites, '|', d.get('decision_date'))
    m = re.search(anchor, body, re.I)
    if m:
        s = max(0, m.start() - 1200)
        print(re.sub(r'\s+', ' ', body[s:m.end() + span]))
    else:
        print('[anchor not found; len', len(body), ']')
    print()
