# -*- coding: utf-8 -*-
"""MOO-208 store revision 70 — the §5 half of the retention rotation §0.1 sets.

NOT a discretionary tidy. The §5 self-describing paragraph has said since store revision 58 that
"the next revision that is short of room should move §5.38 and §5.39 out first", and store revision
70 is that revision: with the normal record layer the document lands at 527,893 characters against
the store's 524,288 ceiling, so it cannot write at all without this. The move is verbatim, leaves a
stub in the established form, and touches no enacted word and no other revision's reasoning.
"""

RETAINED = "bill-text-s8-record-s0-s5-s6-rev2-51"
LINK = ("[`bill-text-s8-record-s0-s5-s6-rev2-51`]"
        "(/MOO/issues/MOO-42#document-bill-text-s8-record-s0-s5-s6-rev2-51)")

# (heading prefix, stub heading, durable result) — the stub body follows §5.37's form exactly.
MOVES = [
    ("### §5.38 ",
     "### §5.38 Store revision 59 — performed; the sweep is moved verbatim to the retained-record "
     "document in store revision 70",
     "Eleven checks over §1 alone, two findings, both record-side and both fixed in that revision, "
     "and **no operative defect found**; § 2.2-4021 B and C described by subdivision M 3 rather "
     "than quoted, so M 3 does not break if the General Assembly amends the words around them; "
     "Articles 3, 4 and 5 of the Administrative Process Act verified as cited."),
    ("### §5.39 ",
     "### §5.39 Store revision 60 — performed; the sweep is moved verbatim to the retained-record "
     "document in store revision 70",
     "The thirteen substitutions chased in both directions with **no conforming amendment required "
     "outside the six provisions amended, and none made**; § 51.1-156 A, B and H verified at "
     "source, clause (ii) of H's second sentence being the Medical Board's certification and so "
     "the fact the Board can see."),
]

HEADER = (
    "\n\n## Moved in from `bill-text-s8` in store revision 70 — the sweeps §5.38 and §5.39, "
    "verbatim\n\n"
    "**Why.** On the rotation §0.1 sets, §5 of the bill document carries the live sweep and the "
    "recent ones only, and its own paragraph has named these two as the next to move since store "
    "revision 58. Store revision 70 — the Policy Director's composite out of "
    "[MOO-191](/MOO/issues/MOO-191), commissioned at [MOO-208](/MOO/issues/MOO-208) — is the first "
    "revision that could not write within the store's 524,288-character ceiling without the move. "
    "**Nothing is edited. Both sweeps are the text store revisions 59 and 60 wrote**, and the bill "
    "document now carries a stub for each in the form §5.37 and §6.0-58 established. A reference "
    "of the form **§5.38** or **§5.39** resolves here.\n\n"
    "**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel "
    "or by DLS, not legally sufficient for introduction. Pre-decisional and internal.**\n\n"
)


def extract(body, prefix):
    """The whole §5.n block, located by content: its heading to the next third-level heading."""
    k = body.index(prefix)
    nx = body.index("\n### ", k + 5)
    return k, nx, body[k:nx]


def stub(stub_head, durable):
    return (f"{stub_head}\n\n**Moved verbatim** to {LINK}, on the rotation §0.1 sets: §5 carries "
            f"the live revision and the recent ones. **Store revision 70 is the revision that was "
            f"short of room**, as this section's own paragraph has anticipated since store revision "
            f"58. Its durable result: {durable}")


def rotate(body):
    """Return (new_body, moved_text, report). Verbatim out, stub in, counted both ways."""
    moved, report, out = [], [], body
    for prefix, stub_head, durable in MOVES:
        k, nx, block = extract(out, prefix)
        assert out.count(prefix) == 1, f"{prefix!r} occurs {out.count(prefix)} times"
        s = stub(stub_head, durable)
        out = out[:k] + s + out[nx:]
        moved.append(block.rstrip("\n"))
        report.append((prefix.strip(), len(block), len(s), len(s) - len(block)))
    return out, HEADER + "\n\n".join(moved) + "\n", report
