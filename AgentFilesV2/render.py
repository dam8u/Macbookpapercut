"""Shared renderer: one block list -> one .docx and one .pdf.

Block forms:
  ("title", text)          ("sub", text)
  ("h1", text)             ("h2", text)
  ("p", text)              ("note", text)      bold-ish callout paragraph
  ("ul", [text, ...])      ("ol", [text, ...])
  ("table", caption_or_None, [[header...], [row...], ...])
  ("hr",)
Inline markup in text: **bold**, *italic*.
"""
import html
import re
import subprocess
from pathlib import Path

import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor, Inches

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TOKEN = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*)")


def _runs(paragraph, text):
    for piece in TOKEN.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            r = paragraph.add_run(piece[2:-2]); r.bold = True
        elif piece.startswith("*") and piece.endswith("*"):
            r = paragraph.add_run(piece[1:-1]); r.italic = True
        else:
            paragraph.add_run(piece)


def _inline_html(text):
    out = []
    for piece in TOKEN.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            out.append(f"<strong>{html.escape(piece[2:-2])}</strong>")
        elif piece.startswith("*") and piece.endswith("*"):
            out.append(f"<em>{html.escape(piece[1:-1])}</em>")
        else:
            out.append(html.escape(piece))
    return "".join(out)


def to_docx(blocks, path):
    d = docx.Document()
    s = d.sections[0]
    s.left_margin = s.right_margin = Inches(0.9)
    s.top_margin = s.bottom_margin = Inches(0.85)
    d.styles["Normal"].font.name = "Calibri"
    d.styles["Normal"].font.size = Pt(10.5)
    for b in blocks:
        kind = b[0]
        if kind == "title":
            p = d.add_paragraph(style="Title"); _runs(p, b[1])
        elif kind == "sub":
            p = d.add_paragraph(); _runs(p, b[1])
            for r in p.runs:
                r.italic = True; r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        elif kind == "h1":
            p = d.add_paragraph(style="Heading 1"); _runs(p, b[1])
        elif kind == "h2":
            p = d.add_paragraph(style="Heading 2"); _runs(p, b[1])
        elif kind == "p":
            p = d.add_paragraph(); _runs(p, b[1])
        elif kind == "note":
            p = d.add_paragraph(); _runs(p, b[1])
            p.paragraph_format.left_indent = Inches(0.25)
            for r in p.runs:
                r.font.size = Pt(10)
        elif kind == "ul":
            for item in b[1]:
                p = d.add_paragraph(style="List Bullet"); _runs(p, item)
        elif kind == "ol":
            for item in b[1]:
                p = d.add_paragraph(style="List Number"); _runs(p, item)
        elif kind == "table":
            cap, rows = b[1], b[2]
            if cap:
                p = d.add_paragraph(); _runs(p, cap)
                for r in p.runs:
                    r.bold = True; r.font.size = Pt(10)
            t = d.add_table(rows=len(rows), cols=len(rows[0]))
            t.style = "Light Grid Accent 1"
            t.alignment = WD_TABLE_ALIGNMENT.LEFT
            for i, row in enumerate(rows):
                for j, cell in enumerate(row):
                    c = t.cell(i, j)
                    c.text = ""
                    para = c.paragraphs[0]
                    _runs(para, str(cell))
                    for r in para.runs:
                        r.font.size = Pt(9.5)
                        if i == 0:
                            r.bold = True
            d.add_paragraph()
        elif kind == "hr":
            p = d.add_paragraph("_" * 86)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.color.rgb = RGBColor(0xBB, 0xBB, 0xBB)
        else:
            raise ValueError(kind)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    d.save(path)
    return path


CSS = """
@page { size: Letter; margin: 0.85in 0.9in; }
* { box-sizing: border-box; }
body { font-family: Calibri, Carlito, "Helvetica Neue", Arial, sans-serif;
       font-size: 10.5pt; line-height: 1.42; color: #1a1a1a; margin: 0; }
h1.doc-title { font-size: 20pt; color: #17365D; margin: 0 0 2px; font-weight: 600;
               letter-spacing: -0.2px; }
p.sub { font-size: 9.5pt; color: #555; font-style: italic; margin: 0 0 14px; }
h2 { font-size: 13.5pt; color: #365F91; margin: 20px 0 6px; font-weight: 600;
     page-break-after: avoid; }
h3 { font-size: 12pt; color: #4F81BD; margin: 15px 0 4px; font-weight: 600;
     page-break-after: avoid; }
p { margin: 0 0 7px; }
p.note { margin-left: 18px; font-size: 10pt; }
ul, ol { margin: 0 0 8px; padding-left: 22px; }
li { margin-bottom: 3px; }
p.caption { font-weight: 700; font-size: 10pt; margin: 14px 0 4px; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 0 0 12px; font-size: 9.5pt;
        page-break-inside: avoid; }
th { background: #4F81BD; color: #fff; text-align: left; font-weight: 600;
     padding: 4px 7px; border: 0.5pt solid #4F81BD; }
td { padding: 4px 7px; border: 0.5pt solid #B8CCE4; vertical-align: top; }
tbody tr:nth-child(even) td { background: #EFF4FA; }
hr { border: 0; border-top: 0.75pt solid #ccc; margin: 18px 0; }
strong { font-weight: 700; }
"""


def to_pdf(blocks, path, scratch):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "title":
            out.append(f'<h1 class="doc-title">{_inline_html(b[1])}</h1>')
        elif kind == "sub":
            out.append(f'<p class="sub">{_inline_html(b[1])}</p>')
        elif kind == "h1":
            out.append(f"<h2>{_inline_html(b[1])}</h2>")
        elif kind == "h2":
            out.append(f"<h3>{_inline_html(b[1])}</h3>")
        elif kind == "p":
            out.append(f"<p>{_inline_html(b[1])}</p>")
        elif kind == "note":
            out.append(f'<p class="note">{_inline_html(b[1])}</p>')
        elif kind in ("ul", "ol"):
            items = "".join(f"<li>{_inline_html(i)}</li>" for i in b[1])
            out.append(f"<{kind}>{items}</{kind}>")
        elif kind == "table":
            cap, rows = b[1], b[2]
            if cap:
                out.append(f'<p class="caption">{_inline_html(cap)}</p>')
            head = "".join(f"<th>{_inline_html(str(c))}</th>" for c in rows[0])
            body = "".join(
                "<tr>" + "".join(f"<td>{_inline_html(str(c))}</td>" for c in r) + "</tr>"
                for r in rows[1:])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
        elif kind == "hr":
            out.append("<hr>")
    title = next((b[1] for b in blocks if b[0] == "title"), "document")
    doc = (f"<!doctype html><html><head><meta charset='utf-8'>"
           f"<title>{html.escape(re.sub(TOKEN, lambda m: m.group(0).strip('*'), title))}</title>"
           f"<style>{CSS}</style></head><body>{''.join(out)}</body></html>")
    tmp = Path(scratch) / (Path(path).stem + ".html")
    tmp.write_text(doc, encoding="utf-8")
    out = Path(path)
    if out.exists():
        out.unlink()
    # Chrome writes the PDF and then sometimes exits non-zero on teardown
    # (CVDisplayLink / watchdog noise on macOS). Judge success by the file.
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
         "--no-pdf-header-footer", f"--print-to-pdf={out}", tmp.as_uri()],
        capture_output=True, timeout=300)
    if not out.exists() or out.stat().st_size < 5000:
        raise RuntimeError(f"PDF not produced for {out}")
    return path


def to_markdown(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "title":
            out.append(f"# {b[1]}")
        elif kind == "sub":
            out.append(f"*{_strip(b[1])}*")
        elif kind == "h1":
            out.append(f"## {b[1]}")
        elif kind == "h2":
            out.append(f"### {b[1]}")
        elif kind in ("p", "note"):
            out.append(b[1])
        elif kind == "ul":
            out.append("\n".join(f"- {i}" for i in b[1]))
        elif kind == "ol":
            out.append("\n".join(f"{n}. {i}" for n, i in enumerate(b[1], 1)))
        elif kind == "table":
            cap, rows = b[1], b[2]
            if cap:
                out.append(f"**{cap}**")
            esc = lambda c: str(c).replace("|", "\\|").replace("\n", " ")
            out.append("\n".join([
                "| " + " | ".join(esc(c) for c in rows[0]) + " |",
                "|" + "---|" * len(rows[0]),
            ] + ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows[1:]]))
        elif kind == "hr":
            out.append("---")
    return "\n\n".join(out) + "\n"


def _strip(s):
    return re.sub(r"\*+", "", s)


def build(blocks, stem, folder, scratch):
    folder = Path(folder)
    a = to_docx(blocks, folder / f"{stem}.docx")
    b = to_pdf(blocks, folder / f"{stem}.pdf", scratch)
    return a, b
