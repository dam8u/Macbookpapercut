#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal markdown -> .docx for the MOO working drafts, so the Director can edit them.

Handles headings, paragraphs, bullet and numbered lists, pipe tables, blockquotes and fenced
code. Inline **bold**, *italic*, `code` and [text](link) are rendered; nothing else is claimed.

    python3 md2docx.py disposition.md "MOO-191 - Policy Director disposition of MOO-195.docx"
"""
import re, sys
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

INLINE = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`|\[[^\]]+?\]\([^)]*?\))", re.S)


def runs(par, text):
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            # nested inline markers inside a bold span are dropped, not rendered twice
            par.add_run(piece[2:-2].replace("`", "")).bold = True
        elif piece.startswith("`") and piece.endswith("`"):
            r = par.add_run(piece[1:-1]); r.font.name = "Consolas"; r.font.size = Pt(9)
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            par.add_run(piece[1:-1]).italic = True
        elif piece.startswith("["):
            m = re.match(r"\[([^\]]+)\]\(([^)]*)\)", piece)
            par.add_run(m.group(1)).underline = True
        else:
            par.add_run(piece)


def convert(src, dst):
    lines = open(src, encoding="utf-8").read().split("\n")
    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(10.5)
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if not s:
            i += 1; continue

        if s.startswith("```"):                                   # fenced code
            i += 1; buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            r = p.add_run("\n".join(buf)); r.font.name = "Consolas"; r.font.size = Pt(9)
            continue

        if s.startswith("|") and i + 1 < len(lines) and set(
                lines[i + 1].strip()) <= set("|-: "):             # pipe table
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not set("".join(cells)) <= set("-: "):
                    rows.append(cells)
                i += 1
            width = max(len(r) for r in rows)
            t = doc.add_table(rows=0, cols=width); t.style = "Table Grid"
            for n, row in enumerate(rows):
                cs = t.add_row().cells
                for j in range(width):
                    cs[j].text = ""
                    runs(cs[j].paragraphs[0], row[j] if j < len(row) else "")
                    if n == 0:
                        for rr in cs[j].paragraphs[0].runs:
                            rr.bold = True
            doc.add_paragraph()
            continue

        if s.startswith("---"):
            doc.add_paragraph().add_run("_" * 60)
            i += 1; continue

        m = re.match(r"(#{1,6})\s+(.*)", s)
        if m:
            doc.add_heading(re.sub(r"[*`]", "", m.group(2)), min(len(m.group(1)), 4))
            i += 1; continue

        if s.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.space_after = Pt(8)
            runs(p, s.lstrip("> ").strip())
            i += 1; continue

        m = re.match(r"[-*]\s+(.*)", s)
        if m:
            runs(doc.add_paragraph(style="List Bullet"), m.group(1))
            i += 1; continue

        m = re.match(r"(\d+)\.\s+(.*)", s)
        if m:
            runs(doc.add_paragraph(style="List Number"), m.group(2))
            i += 1; continue

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        runs(p, s)
        i += 1

    doc.save(dst)
    print("wrote", dst)


if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
