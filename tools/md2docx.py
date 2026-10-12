import re,sys
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

src,out = sys.argv[1], sys.argv[2]
lines = open(src).read().split('\n')
doc = Document()
st = doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(11)

inline = re.compile(r'(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`|~~.+?~~|\[[^\]]+?\]\([^)]*?\))')
def add_runs(p, text):
    # strip markdown links to their label
    for tok in inline.split(text):
        if not tok: continue
        if tok.startswith('**') and tok.endswith('**'):
            r=p.add_run(tok[2:-2]); r.bold=True
        elif tok.startswith('`') and tok.endswith('`'):
            r=p.add_run(tok[1:-1]); r.font.name='Consolas'
        elif tok.startswith('~~') and tok.endswith('~~'):
            r=p.add_run(tok[2:-2]); r.font.strike=True
        elif tok.startswith('*') and tok.endswith('*') and len(tok)>2:
            r=p.add_run(tok[1:-1]); r.italic=True
        elif tok.startswith('['):
            m=re.match(r'\[([^\]]+)\]\(([^)]*)\)',tok)
            add_runs(p, m.group(1)) if m else p.add_run(tok)
        else:
            p.add_run(tok)

def flush(buf, kind):
    if not buf: return
    text=' '.join(x.strip() for x in buf).strip()
    if not text: return
    if kind=='quote':
        p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(0.35)
        add_runs(p, text); 
        for r in p.runs: r.italic=True if not r.bold else r.italic
    elif kind=='bullet':
        p=doc.add_paragraph(style='List Bullet'); add_runs(p, text)
    elif kind=='number':
        p=doc.add_paragraph(style='List Number'); add_runs(p, text)
    else:
        p=doc.add_paragraph(); add_runs(p, text)
    buf.clear()

buf=[]; kind='para'; table=[]
def flush_table():
    global table
    rows=[r for r in table if not re.match(r'^\s*\|[\s:|-]+\|\s*$', r)]
    cells=[[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    if not cells: table=[]; return
    n=max(len(c) for c in cells)
    t=doc.add_table(rows=0, cols=n); t.style='Table Grid'
    for i,row in enumerate(cells):
        cl=t.add_row().cells
        for j in range(n):
            txt=row[j] if j<len(row) else ''
            p=cl[j].paragraphs[0]; add_runs(p, txt)
            if i==0:
                for r in p.runs: r.bold=True
    table=[]

for raw in lines:
    line=raw.rstrip()
    if line.startswith('|'):
        flush(buf,kind); table.append(line); continue
    if table: flush_table()
    if not line.strip():
        flush(buf,kind); kind='para'; continue
    if line.strip()=='---':
        flush(buf,kind); continue
    m=re.match(r'^(#{1,4})\s+(.*)$', line)
    if m:
        flush(buf,kind)
        h=doc.add_heading(level=min(len(m.group(1)),4)); add_runs(h, m.group(2)); continue
    if line.startswith('>'):
        if kind!='quote': flush(buf,kind); kind='quote'
        buf.append(line.lstrip('>').strip()); continue
    mb=re.match(r'^\s*[-*]\s+(.*)$', line)
    if mb:
        flush(buf,kind); kind='bullet'; buf.append(mb.group(1)); flush(buf,kind); kind='para'; continue
    mn=re.match(r'^\s*\d+\.\s+(.*)$', line)
    if mn:
        flush(buf,kind); kind='number'; buf.append(mn.group(1)); flush(buf,kind); kind='para'; continue
    if kind in ('para','quote'):
        buf.append(line)
    else:
        kind='para'; buf.append(line)
flush(buf,kind)
if table: flush_table()
doc.save(out)
print('wrote', out)
