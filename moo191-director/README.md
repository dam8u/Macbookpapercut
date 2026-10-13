# moo191-director — the Policy Director's disposition of MOO-195

All eight decisions on MOO-191 answered, and the **one composite edit** they produce, verified on
the live base. Nothing in this directory writes to the store.

| File | What it does |
|---|---|
| `disposition.md` | The disposition. The eight decisions, the reasons, the composite, the post-conditions, and the two things left open |
| `director_composite.py` | Fetches the live base, demonstrates the D3c/D9 sequencing hazard, applies the six substitutions in order with every anchor re-counted, asserts every post-condition. Exits non-zero on a dead anchor |
| `md2docx.py` | Markdown to `.docx`, so the Director can edit the artifact |
| `MOO-191 - Policy Director disposition of MOO-195.docx` | The editable copy |

```
python3 director_composite.py
python3 md2docx.py disposition.md "MOO-191 - Policy Director disposition of MOO-195.docx"
```

## The decisions in one line each

- **F1** take, **F2** take as D2b, **F3 take as D3c conformed**, **F4** take, **F5 hold**,
  **F6 take** (departing from the drafter's conditional), **F9** take, **F8 take T2**.
- **F7** stays carded and is re-scoped to the six propositions of law.
- Net **§1 131,066 → 131,656 (+590)**; document **449,196 → 449,830 (+634)**.

## The one defect found in the disposition

**D3c and D9 are not independent cuts.** D3c writes D9's FIND string into the subdivision twice
more, so D9's anchor goes from 1x to 3x. Applied the other way, D3c's exception describes a matter
the subdivision no longer requires to be stated, and **F3 is enacted and does nothing — in both
the subsection M limb and the subsection J limb**. The composite conforms both phrases and fixes
the order. `director_composite.py` demonstrates it rather than asserting it.

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or by
DLS, not legally sufficient for introduction.**
