# moo208-cut73 — the Policy Director's six approved cures, cut as store revision 73

Deliverable: [`moo208-rev73`](/MOO/issues/MOO-208#document-moo208-rev73) on [MOO-208](/MOO/issues/MOO-208).
Enacted: [`bill-text-s8`](/MOO/issues/MOO-42#document-bill-text-s8) store revision **73**, document
revision `ab212a49` (number 93), 507,155 characters, headroom 17,133. Item list revision
`1811ae16` (number 16). Retained-record document revision `5e117867` (number 21).

| File | What it does |
|---|---|
| `cures73.py` | The six cures as FIND/READ data with the two departures priced, the standing post-conditions, the forbidden anchors, and the two **proposals** (M-c, S5-w) which it enacts nowhere |
| `verify73.py` | Re-resolves all six on the live store, applies them in document order with each anchor re-counted **on its predecessors' output**, runs the §1 line diff, and generates every figure §5.49 asserts in both directions. Writes nothing |
| `apply73.py` | The write: the six cures inside the §1 slice, the six record patches, the four-block retention rotation, the record layer, §7 items 135/137/138, and every post-condition. Verifies each of three writes from the returned JSON |
| `check73.py` | **Post-write** check against the live document, and generates `repro-73.md` by bolding this revision's words and stripping them back to the live line character for character |
| `moves73.py` · `items73.py` | The rotation stubs and the two preamble patches; §7 item 135's closure and items 137 and 138 |
| `rec_s0_73.md` · `rec_s5_73.md` · `rec_s6_73.md` · `rec_s8_73.md` | §0.0-73, §5.49, §6.0-73, §8 |
| `pack_head.md` · `pack_tail.md` · `build_pack73.py` | The deliverable, with the reproductions taken from `repro-73.md` and not pasted |

```
python3 verify73.py
python3 apply73.py --dry-run && python3 apply73.py
python3 check73.py --write
python3 build_pack73.py --dry-run && python3 build_pack73.py
```

## The three things worth re-running

**The cut is +827 and not the approved +807, because two approved strings carried mechanical
defects.** **S3 −4:** its insert opened *", and that…"* and item 7's single conjunction belongs to
its last clause, so the approved words gave *"A, B, and C, and D"* — the defect the composite's
substitution 3 spent four characters to avoid in the same sentence. **M3 +24:** its insert ended
*"in that report"*, whose only antecedent in enactment 3 clause (iii) is *"the last report"*, so
the referent is named in the act's standing phrase *"the report required by subsection J"*.
Neither touches a proposition; each is reversible with one word.

**Two adverse findings on the cut text, drafted, priced, anchored and enacted nowhere.**
**M-c, +216** — S1 excepts the advice failure from M 2's failure-to-state limb, but M 2's second
sentence deems a **certification** a determination by name and D 1 disapplies that sentence only
*"to such a failure"*, which no longer includes the advice failure. **S5-w, +48** — S5 freezes
*"a statement this subdivision requires"*, and **subdivision G 4 compels three statements of the
effect of § 51.1-162** in the death notice, the one document a survivor ever receives. §7 items
137 and 138.

**One correction to the [MOO-211](/MOO/issues/MOO-211) record, C1.** That kit recorded that M4
widens the first limb of the no-fault clause only. **The clause has one subject governing two
verbs**, so M4 widens both. Harmless, arguably better, and the words were approved on a
description of them that was wrong.

Counsel pass commissioned at [MOO-219](/MOO/issues/MOO-219); [MOO-208](/MOO/issues/MOO-208) is
blocked on it.

**Internal working draft. Not a Division of Legislative Services bill, not cleared by counsel or
by DLS, not legally sufficient for introduction. Pre-decisional and internal.**
