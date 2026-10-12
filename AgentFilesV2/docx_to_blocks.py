"""Read an existing .docx back into render.py block form, in document order.

Used to amend a document that was built before render.py existed, then re-emit
both the .docx and the .pdf from one source so the two cannot diverge.
"""
import re

import docx
from docx.table import Table
from docx.text.paragraph import Paragraph

STYLE_MAP = {"Title": "title", "Heading 1": "h1", "Heading 2": "h2",
             "List Bullet": "ul", "List Number": "ol"}


def _runs_to_md(p):
    out = []
    for r in p.runs:
        t = r.text
        if not t:
            continue
        if r.bold and t.strip():
            lead = t[: len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            out.append(f"{lead}**{t.strip()}**{trail}")
        elif r.italic and t.strip():
            lead = t[: len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            out.append(f"{lead}*{t.strip()}*{trail}")
        else:
            out.append(t)
    s = "".join(out)
    s = re.sub(r"\*\*\s*\*\*", "", s)
    s = re.sub(r"(?<!\*)\*\s*\*(?!\*)", "", s)
    return s


def load(path):
    d = docx.Document(path)
    body = d.element.body
    blocks = []
    pending_list = None
    pending_caption = None

    def flush_list():
        nonlocal pending_list
        if pending_list:
            blocks.append((pending_list[0], pending_list[1]))
            pending_list = None

    for child in body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "p":
            p = Paragraph(child, d)
            text = _runs_to_md(p)
            style = p.style.name
            kind = STYLE_MAP.get(style, "p")
            if kind in ("ul", "ol"):
                if pending_list and pending_list[0] == kind:
                    pending_list[1].append(text)
                else:
                    flush_list()
                    pending_list = [kind, [text]]
                continue
            flush_list()
            if not text.strip():
                continue
            if set(text.strip()) == {"_"}:
                blocks.append(("hr",))
                continue
            if kind == "title":
                blocks.append(("title", text))
                continue
            if kind == "p":
                # the first italic grey line under a Title is the subtitle
                if (len(blocks) == 1 and blocks[0][0] == "title"
                        and all(r.italic for r in p.runs if r.text.strip())):
                    blocks.append(("sub", _strip_marks(text)))
                    continue
                # a short all-bold paragraph immediately before a table is its caption
                if (text.startswith("**") and text.endswith("**")
                        and _next_is_table(child)):
                    pending_caption = text[2:-2]
                    continue
            blocks.append((kind, text))
        elif tag == "tbl":
            flush_list()
            t = Table(child, d)
            rows = []
            for r in t.rows:
                rows.append([_runs_to_md(c.paragraphs[0]) if c.paragraphs else ""
                             for c in r.cells])
            blocks.append(("table", pending_caption, rows))
            pending_caption = None
    flush_list()
    return blocks


def _strip_marks(s):
    return re.sub(r"\*+", "", s)


def _next_is_table(el):
    nxt = el.getnext()
    while nxt is not None:
        tag = nxt.tag.split("}")[-1]
        if tag == "tbl":
            return True
        if tag == "p":
            p_text = "".join(nxt.itertext()).strip()
            if p_text:
                return False
        nxt = nxt.getnext()
    return False
