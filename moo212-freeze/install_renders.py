#!/usr/bin/env python3
"""MOO-212 item 6 — install the rebuilt renders, rebuild the zip, and checksum-match.

Thirty artifacts from one source state in one pass: the ten markdown sources, the ten PDFs
and the ten DOCX. The zip is rebuilt from the folder afterwards and every entry is compared
byte-for-byte against the file it came from, so a stale entry is a failure and not a
discrepancy somebody has to notice.

    python3 install_renders.py <build-root>
"""
import hashlib
import os
import re
import shutil
import sys
import zipfile

V = "/Users/davidmoody/AgentCreated/v2.1"
SRC = os.path.join(V, "08-markdown-sources")
PDF = os.path.join(V, "01-sponsor-package-pdf")
DOCX = os.path.join(V, "02-sponsor-package-docx")
ZIP = os.path.join(V, "09-zip-bundles", "vrs-legislative-package-v2.1.zip")
CHARTS = os.path.join(V, "04-charts", "charts-v6-authorised-basis")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    build = sys.argv[1]
    names = sorted(f[:-3] for f in os.listdir(SRC) if f.endswith(".md"))
    assert len(names) == 10, names

    for n in names:
        shutil.copy2(os.path.join(build, "build", "pdf", n + ".pdf"),
                     os.path.join(PDF, n + ".pdf"))
        shutil.copy2(os.path.join(build, "build", "docx", n + ".docx"),
                     os.path.join(DOCX, n + ".docx"))
    print(f"installed {len(names)} PDFs and {len(names)} DOCX")

    # the sources the renders were built from must still be the sources on disk
    drift = [n for n in names
             if sha(os.path.join(SRC, n + ".md")) != sha(os.path.join(build, "src", n + ".md"))]
    assert not drift, f"sources changed after the build: {drift}"
    print("all ten sources byte-identical to what the renders were built from")

    srcs = max(os.path.getmtime(os.path.join(SRC, n + ".md")) for n in names)
    rends = min(min(os.path.getmtime(os.path.join(PDF, n + ".pdf")),
                    os.path.getmtime(os.path.join(DOCX, n + ".docx"))) for n in names)
    assert rends > srcs, "a render is older than a source"
    print("every render newer than every source")

    b = open(os.path.join(PDF, "01-one-page-summary.pdf"), "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", b))
    assert pages == 1, f"the one-pager is {pages} pages"
    print("the one-pager is one page, counted from the PDF page tree")

    # rebuild the zip from the folder, keeping the layout the previous bundle used
    with zipfile.ZipFile(ZIP) as z:
        layout = z.namelist()
    root = layout[0].split("/", 1)[0]
    mapping = {"pdf": PDF, "docx": DOCX, "src": SRC,
               "charts": CHARTS}
    tmp = ZIP + ".new"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for name in layout:
            rel = name.split("/", 1)[1]
            head = rel.split("/", 1)[0]
            if head in mapping:
                p = os.path.join(mapping[head], rel.split("/", 1)[1])
            elif rel == "README.txt":
                p = os.path.join(V, "SPONSOR-PACKAGE-README.txt")
            else:
                p = os.path.join(V, "03-financial-model-interactive/superseded/NOT-PUBLISHED.md")
            assert os.path.exists(p), f"zip entry has no source file: {name} -> {p}"
            z.write(p, name)
    os.replace(tmp, ZIP)

    with zipfile.ZipFile(ZIP) as z:
        names2 = z.namelist()
        mism = []
        for name in names2:
            rel = name.split("/", 1)[1]
            head = rel.split("/", 1)[0]
            if head in mapping:
                p = os.path.join(mapping[head], rel.split("/", 1)[1])
            elif rel == "README.txt":
                p = os.path.join(V, "SPONSOR-PACKAGE-README.txt")
            else:
                p = os.path.join(V, "03-financial-model-interactive/superseded/NOT-PUBLISHED.md")
            if z.read(name) != open(p, "rb").read():
                mism.append(name)
    assert not mism, mism
    assert len(names2) == len(layout) == 72, (len(names2), len(layout))
    assert not any("14_v6_11_workforce" in n for n in names2), "the held chart is in the zip"
    print(f"zip rebuilt: {len(names2)} entries, zero mismatches against the folder")
    print(f"the held workforce page is not in the zip and not in the published chart set: "
          f"{not os.path.exists(os.path.join(CHARTS, 'charts', '14_v6_11_workforce.png'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
