#!/usr/bin/env python3
"""MOO-195 — reproduces every count the counsel pass relies on.

Usage:  python3 check195.py bill.md
where bill.md is the `bill-text-s8` body fetched from MOO-42
(store revision 65, document revision bc0576f5).

Nothing is written. No team file is modified.
"""
import re, sys

ADVISORY = ("that the member is advised to review the member's designation of "
            "beneficiary under subsection A of § 51.1-162 before completing payment;")

def section1(t):
    return t[t.find('## 1. The bill'):t.find('## 2. Section-by-section')]

def series(s1):
    d1 = s1[s1.find("**D. 1.**"):]
    i = d1.find("The Board's certification shall also state that")
    j = d1.find("A failure to state in the Board's certification")
    assert 0 <= i < j, "D 1 series not located"
    return d1[i:j]

def main(path):
    t = open(path).read()
    s1 = section1(t)
    ok = []
    def chk(label, got, want=None):
        if want is None:
            ok.append((label, got, 'reported'))
        else:
            assert got == want, f"{label}: got {got}, expected {want}"
            ok.append((label, got, 'OK'))

    # --- the enacted text, and the movement figures the record asserts -------
    chk("len(section 1)", len(s1), 121576)
    chk("<u> in section 1", s1.count('<u>'), 60)
    chk("</u> in section 1", s1.count('</u>'), 60)
    chk("advisory occurrences in section 1", s1.count(ADVISORY), 1)
    chk("advisory occurrences in whole document", t.count(ADVISORY), 2)  # +0.0-65 block quote
    chk("len(advisory) incl. leading space", len(' ' + ADVISORY), 137)

    # --- vocabulary claims of sweep 5.43 direction 1 -------------------------
    chk("'designation of beneficiary' in section 1", s1.count('designation of beneficiary'), 1)
    chk("'designation' in section 1", s1.count('designation'), 4)
    chk("'designated' in section 1", s1.count('designated'), 5)
    chk("'before completing payment' in section 1", s1.count('before completing payment'), 3)
    chk("'is advised' in section 1", s1.count('is advised'), 1)
    chk("'subsection A of that section' in section 1", s1.count('subsection A of that section'), 3)
    chk("'subsection A of § 51.1-162' in section 1", s1.count('subsection A of § 51.1-162'), 1)

    # --- series structure: 7 items, semicolon-and-'that', 'and that' closes --
    ser = series(s1)
    parts = ser.split('; ')
    chk("items in the 'shall also state that' series", len(parts), 7)
    chk("item 4 (0-indexed) is the advisory",
        parts[4].strip() == ADVISORY[:-1], True)
    for n in range(1, 6):
        chk(f"item {n} opens with 'that '", parts[n].startswith('that '), True)
    chk("closing item opens with 'and that '", parts[6].startswith('and that '), True)

    # --- referent check: no 'that section'/'that subsection' crosses item 4 --
    # Every short-form referent must sit in an item that has already named its
    # antecedent. A leading "that subsection C of § 51.1-162" is the series
    # conjunction, not a referent, so matches at offset 0 are skipped.
    bad, shortforms = [], 0
    for n, p in enumerate(parts):
        for m in re.finditer(r'that (?:sub)?section', p):
            if m.start() == 0:
                continue
            shortforms += 1
            if '§ 51.1-16' not in p[:m.start()]:
                bad.append((n, p[max(0, m.start()-50):m.start()+30]))
    chk("short-form referents in the series", shortforms, 8)
    chk("short-form referents resolving outside their own item", len(bad), 0)
    chk("short-form referents in the advisory item",
        len(re.findall(r'that (?:sub)?section', parts[4])), 0)

    # --- sentence-ordinal references: ten, none to a sentence of D 1 ---------
    ordinals = re.findall(r'(?:first|second|third|fourth|fifth) sentence', s1)
    chk("ordinal sentence references in section 1", len(ordinals), 10)
    chk("'first sentence of this subdivision' in section 1",
        s1.count('first sentence of this subdivision'), 2)
    for junk in ('the preceding proposition', 'the foregoing'):
        chk(f"{junk!r} in section 1", s1.count(junk), 0)

    # --- the failure sentence and its two limbs -----------------------------
    chk("failure-sentence anchor in section 1",
        s1.count('every matter this subdivision requires to be stated'), 1)
    chk("J-limb anchor in section 1",
        s1.count('and the Board shall state every such failure in the report '
                 'required by subsection J. The member shall file the notice of '
                 'retirement required by § 51.1-153'), 1)

    # --- FIND strings the review hands to Drafting Specialist ---------------
    for f in (ADVISORY,
              "and no other designation has been made; that the member is advised",
              "in the order of precedence that section states."):
        chk(f"FIND resolves once in section 1: {f[:48]}...", s1.count(f), 1)

    for label, got, status in ok:
        print(f"  [{status:8}] {label}: {got}")
    print(f"\n{len(ok)} checks, 0 failures.")

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'bill.md')
