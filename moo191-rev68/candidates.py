#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOO-191 — the seven MOO-195 findings the Policy Director must decide, drafted and verified.

Nothing here writes to the store. For each candidate it re-counts the FIND on the LIVE base
(document and §1), applies the substitution to a scratch copy of §1, and reports the character
movement, the <u>/</u> balance, the item count of the D 1 certification series and the position of
the advisory in it. Run:

    python3 candidates.py
"""
import json, os, re, sys, urllib.request, urllib.error

MOO42 = "2c806c8a-b486-4435-8904-dfb34e5f6d25"
KEY = "bill-text-s8"


def base():
    u = os.environ["PAPERCLIP_API_URL"].rstrip("/")
    return u[:-4] if u.endswith("/api") else u


def get(path):
    r = urllib.request.Request(base() + path, headers={
        "Authorization": "Bearer " + os.environ["PAPERCLIP_API_KEY"]})
    with urllib.request.urlopen(r) as resp:
        return json.loads(resp.read().decode())


def sec1(b):
    i = b.index("\n## 1.")
    m = re.search(r"\n## (?!1\.)", b[i + 5:])
    return b[i:i + 5 + m.start()]


SEP = re.compile(r"; (?:and )?that[ ,]")
ADV = ("that the member is advised to review the member's designation of beneficiary under "
       "subsection A of § 51.1-162 before completing payment;")
ADV_OPEN = "that the member is advised to review the member's designation"


def series_of(s1):
    a = s1.index("The Board's certification shall also state that,")
    z = s1.index(". A failure to state in the Board's certification") + 1
    return s1[a:z]


def shape(s1, probe):
    """(item count, 1-based position of probe) for the certification series."""
    s = series_of(s1)
    items = len(SEP.findall(s)) + 1
    at = len(SEP.findall(s[:s.index(probe) + 6])) + 1 if probe in s else None
    return items, at


# ---------------------------------------------------------------- the candidates
# Each: id, finding, FIND, READ, the probe that locates the advisory afterwards.
C = []


def cand(cid, finding, find, read, probe=None, note=""):
    C.append(dict(id=cid, finding=finding, edits=[(find, read)], probe=probe or ADV_OPEN,
                  note=note))


def cand_multi(cid, finding, edits, probe=None, note=""):
    C.append(dict(id=cid, finding=finding, edits=edits, probe=probe or ADV_OPEN, note=note))


# --- F1: give the advice an object (counsel's words) -------------------------
cand("D1", "F1", ADV,
     "that the member is advised to review the member's designation of beneficiary under "
     "subsection A of § 51.1-162, and the effect of that designation under subsection B of that "
     "section, before completing payment;")

# --- F2 with F1, counsel's words verbatim -----------------------------------
cand("D2a", "F1+F2 (counsel verbatim)", ADV,
     "that the member is advised to review the member's designation of beneficiary under "
     "subsection A of § 51.1-162, and the effect of that designation under subsection B of that "
     "section, before completing payment, and that the member may make or change that designation "
     "under that subsection at any time before the member's death;",
     note="'that subsection' takes subsection B as its nearest antecedent; the power is in A")

# --- F2 with F1, the referent repaired --------------------------------------
cand("D2b", "F1+F2 (referent repaired)", ADV,
     "that the member is advised to review the member's designation of beneficiary under "
     "subsection A of § 51.1-162, and the effect of that designation under subsection B of that "
     "section, before completing payment, and that the member may make or change that designation "
     "under subsection A of that section at any time before the member's death;")

# --- F2 alone, where the Director declines F1 -------------------------------
# D2a and D2b both carry F1's object inside them, so neither can be applied if F1 is declined.
# "that subsection" is safe without F1's insertion: subsection A of § 51.1-162 is then the only
# subsection named in the item before the pronoun.
cand("D2c", "F2 alone (F1 declined)", ADV,
     "that the member is advised to review the member's designation of beneficiary under "
     "subsection A of § 51.1-162 before completing payment, and that the member may make or "
     "change that designation under that subsection at any time before the member's death;")

# --- F3: keep J, drop M. Counsel's one substitution --------------------------
F3_FIND = ("and the Board shall state every such failure in the report required by subsection J. "
           "The member shall file the notice of retirement required by § 51.1-153")
cand("D3a", "F3 (counsel verbatim)", F3_FIND,
     "and the Board shall state every such failure in the report required by subsection J. A "
     "failure to state the advice this subdivision requires to be stated is not a failure for the "
     "purposes of subsection M, and the Board shall state every such failure in the report "
     "required by subsection J. The member shall file the notice of retirement required by "
     "§ 51.1-153",
     note="contradicts the deeming clause rather than excepting from it; 'advice' is undefined")

# --- F3: the same policy, cut as an exception to the deeming clause ---------
DEEM = ("A failure to state in the Board's certification every matter this subdivision requires "
        "to be stated in it is a failure of the Board")
J_LIMB = "and the Board shall state every such failure in the report required by subsection J."
cand_multi("D3b", "F3 (exception form)", [
    (DEEM,
     "A failure to state in the Board's certification every matter this subdivision requires to "
     "be stated in it, other than a failure to state the advice described in the next sentence, "
     "is a failure of the Board"),
    (J_LIMB,
     "and the Board shall state every such failure, and every failure to state that the member is "
     "advised to review the member's designation of beneficiary, in the report required by "
     "subsection J. The advice described in this subdivision is the advice that the member is "
     "advised to review the member's designation of beneficiary under subsection A of "
     "§ 51.1-162."),
], note="two substitutions; keeps J and drops M without a contradiction")

# --- F3: the exception form with the positional reference removed -----------
# D3b excepts "the advice described in the next sentence" and then defines it. Both halves are
# defects: a reference by position breaks if any later revision inserts a sentence between them,
# and "the advice" is an operative term the subdivision nowhere defines. Naming the matter in the
# subdivision's own words needs neither the position nor the definition, and is 131 characters
# shorter. If D9 is taken the quoted phrase conforms to "that the Board advises the member".
EXCEPT = ("other than a failure to state that the member is advised to review the member's "
          "designation of beneficiary")
cand_multi("D3c", "F3 (exception form, no positional reference)", [
    (DEEM,
     "A failure to state in the Board's certification every matter this subdivision requires to "
     "be stated in it, " + EXCEPT + ", is a failure of the Board"),
    (J_LIMB,
     "and the Board shall state every such failure, and every failure to state that the member is "
     "advised to review the member's designation of beneficiary, in the report required by "
     "subsection J."),
], note="no reference by position, no undefined 'advice'; 131 chars shorter than D3b")

# --- F4: move the advisory to the end of the series -------------------------
F4_1 = ("and no other designation has been made; " + ADV + " that subsection C of § 51.1-162")
F4_2 = "in the order of precedence that section states."
F4_3 = "; and that where no benefit is payable"
cand_multi("D4", "F4", [
    (F4_1, "and no other designation has been made; that subsection C of § 51.1-162"),
    (F4_2, "in the order of precedence that section states; and " + ADV[:-1] + "."),
    (F4_3, "; that where no benefit is payable"),
])

# --- F5 (light): a Board duty to state the manner ---------------------------
cand("D5", "F5 (light)", ". A failure to state in the Board's certification",
     ". The Board's certification shall also state the manner prescribed by the Board under "
     "subsection A of § 51.1-162 for making or changing a designation of beneficiary. A failure "
     "to state in the Board's certification",
     note="a new matter inside D 1, so the failure sentence reaches it too")

# --- F6: the no-fault clause -------------------------------------------------
cand("D6", "F6", ADV,
     "that the member is advised to review the member's designation of beneficiary under "
     "subsection A of § 51.1-162 before completing payment, and that nothing in this subdivision "
     "requires the member to review the designation or affects any benefit by reason of the "
     "member's not having reviewed it;")

# --- F9: name the actor ------------------------------------------------------
cand("D9", "F9", ADV_OPEN,
     "that the Board advises the member to review the member's designation",
     probe="that the Board advises the member to review the member's designation")

# --- the full take: F1, F2, F6 and F9 in one item, then F4's relocation -----
FULL = ("that the Board advises the member to review the member's designation of beneficiary "
        "under subsection A of § 51.1-162, and the effect of that designation under subsection B "
        "of that section, before completing payment, that the member may make or change that "
        "designation under subsection A of that section at any time before the member's death, "
        "and that nothing in this subdivision requires the member to review the designation or "
        "affects any benefit by reason of the member's not having reviewed it;")
cand("DALL", "F1+F2+F6+F9 in one item", ADV, FULL,
     probe="that the Board advises the member to review the member's designation")

cand_multi("DALL4", "F1+F2+F6+F9 and F4's relocation", [
    (F4_1, "and no other designation has been made; that subsection C of § 51.1-162"),
    (F4_2, "in the order of precedence that section states; and " + FULL[:-1] + "."),
    (F4_3, "; that where no benefit is payable"),
], probe="that the Board advises the member to review the member's designation")


def main():
    doc = get(f"/api/issues/{MOO42}/documents/{KEY}")
    body, s1 = doc["body"], sec1(doc["body"])
    rev = max(int(m.group(1)) for m in re.finditer(r"^### 0\.0-(\d+) ", body, re.M))
    items0, at0 = shape(s1, ADV_OPEN)
    print(f"base: store revision {rev}, document revision {doc['latestRevisionId'][:8]}, "
          f"{len(body)} chars; §1 {len(s1)} chars, <u>/</u> {s1.count('<u>')}/{s1.count('</u>')}")
    print(f"series: {len(series_of(s1))} chars, {items0} items, advisory at item {at0}\n")
    bad = 0
    for c in C:
        out = s1
        counts = []
        for find, read in c["edits"]:
            n_doc, n_1 = body.count(find), out.count(find)
            counts.append((len(find), n_doc, n_1))
            if n_1 != 1:
                bad += 1
                print(f"  !! {c['id']} anchor resolves {n_1}x in §1 — dead anchor")
            out = out.replace(find, read, 1)
        items, at = shape(out, c["probe"])
        d = len(out) - len(s1)
        ok = (items == 7 and at is not None and out.count("<u>") == s1.count("<u>")
              and out.count("</u>") == s1.count("</u>"))
        print(f"{c['id']:7s} {c['finding']:34s} {d:+5d} chars  §1 {len(s1)} -> {len(out)}  "
              f"series {items} items, advisory item {at}  {'OK' if ok else 'CHECK'}")
        for ln, nd, n1 in counts:
            print(f"          FIND {ln:4d} chars  doc {nd}x  §1 {n1}x")
        if c["note"]:
            print(f"          note: {c['note']}")
    print("\nall anchors live" if not bad else f"\n{bad} dead anchors")
    return 1 if bad else 0


sys.exit(main())
