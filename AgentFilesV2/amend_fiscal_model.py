"""Amendment 1 to V2-fiscal-model, 12 October 2026.

Adds the snapshot limitation found while building the VaLORS pre-score annex:
both pathway pools are an "eligible at 30 June 2025" screen, and the pilot runs
four years, so both understate. Re-emits the .docx and the .pdf from one source.
"""
import os
from pathlib import Path

import docx_to_blocks
import render
import valors_model as M

HERE = Path(__file__).parent
SCRATCH = (os.environ.get("PAPERCLIP_RUN_SCRATCH_DIR")
           or os.environ.get("PAPERCLIP_SCRATCH_DIR") or "/tmp")

blocks = docx_to_blocks.load(HERE / "V2-fiscal-model.docx")
assert blocks[0][0] == "title"
blocks[1] = ("sub", blocks[1][1])

static = M.cohorts()
rf2 = M.roll_forward(2.0)
rf4 = M.roll_forward(4.0)
pool = static[0]["n"] + static[1]["n"]
up2 = (rf2[0]["n"] + rf2[1]["n"]) / pool - 1
up4 = (rf4[0]["n"] + rf4[1]["n"]) / pool - 1

NEW = [
    ("h2", "6.1 Both pathway pools are a snapshot, and they understate"),
    ("p", "**Added 12 October 2026, amendment 1.** The screens in section 2 ask who is eligible, or "
          "reachable, at 30 June 2025 — the valuation date. The pilot would run four years, during "
          "which every member ages and accrues service. Both pools therefore understate, and the "
          "direction of the error is known rather than uncertain."),
    ("p", "The scale was measured on the VaLORS table in V2-annex-VaLORS-prescore §3.2, by rolling "
          "the published table forward on both axes. For that plan the combined pathway pool rises "
          f"**{100*up2:.0f}% at the mid-point of a four-year pilot and {100*up4:.0f}% by the end**. "
          "VaLORS and State Employees have different eligibility rules, so the VaLORS percentage is "
          "an indication of order and not a figure to apply to 6,254 and 2,396. We have not run the "
          "roll-forward on the State Employees table, and we should not publish a number we have not "
          "computed."),
    ("p", "**What this means for the figures in this model.** Our pools, and therefore every "
          "participant count derived from them, are floors on this axis. That is the honest direction "
          "for an advocacy model to err, and it is the opposite of the direction a sceptical reader "
          "will assume we erred in. **Say it before it is found.** Item 5 of the data request now "
          "states the limitation to VRS and asks, if VRS can do it, for the two pathway counts "
          "projected to the pilot years rather than as at the valuation date."),
    ("p", "This limitation is independent of the three dials in section 4 and does not widen the "
          "9-to-141 range. It shifts the base the dials act on."),
]

out = []
for i, b in enumerate(blocks):
    if i == 101:                      # the hr closing section 6
        out.extend(NEW)
    if b[0] == "table" and b[2] and b[2][0][0] == "Need":
        rows = [list(r) for r in b[2]]
        rows.append([
            "Counts projected to the pilot years, not the valuation date",
            "VRS",
            "Both pathway pools are a 30 June 2025 snapshot and understate — §6.1",
        ])
        out.append(("table", b[1], rows))
        continue
    out.append(b)

NOTE = ("**Amendment 1, 12 October 2026 — §6.1 added**, recording that both pathway pools are a "
        "30 June 2025 snapshot and understate. No figure in sections 0 to 5 changed. Found while "
        "building V2-annex-VaLORS-prescore.")
insert_at = next(i for i, b in enumerate(out) if b[0] == "hr")
out.insert(insert_at, ("p", NOTE))

if __name__ == "__main__":
    for p in render.build(out, "V2-fiscal-model", HERE, SCRATCH):
        print("wrote", p)
