# MOO-164 apply kit — the act-versus-notice cut, **revision 5**

**Current check: `verify_r68.py`. Current splicer: `repro65.py`. There is exactly one of each.**
Everything else in this directory is superseded and is named as such below.

> ## ⚠ STORE REVISION 68 BROKE AN ANCHOR — AND IT IS **MOO-141's**, NOT THIS CUT'S
>
> Store revision 68 re-cast subsection A's three-day mailing sentence. It is now confined to mailing
> (*"where the Board mails a written statement, notice, or certification"*) and the triplet replaces
> *"that statement or notice"*, so **MOO-141 Edit 1's FIND string resolves 0 times.** `verify_r68.py`
> keeps the dead string as `E1_F_R65_DEAD` and asserts it at **0**, and supplies the repair as
> `E1_F_R68`. **MOO-141 must re-cut its own Edit 1; this kit only proves the break and carries a
> working repair for the order-independence test.**
>
> **All thirteen MOO-164 anchors still resolve exactly once**, on all three bases, and the delta is
> still **+642**. `verify_r68.py`: **0 failures.**
>
> **§6's reproductions are stale again** — store revisions 66, 67 and 68 grew enacted §1 from 121,576
> to **131,066** characters. Re-run the splicer before the next document revision goes out.

> ## ⚠ APPLY EVERY FIND INSIDE ENACTED §1 ONLY
>
> From store revision 62 the §0 revision narrative of `bill-text-s8` quotes anchor strings. Measured
> at store revision 65, **Edit 164-6's FIND, candidate 164-7's FIND and MOO-141 Edit 3's FIND each
> occur twice whole-document**, and M 2's 90-day sentence occurs four times. **A whole-document
> find-and-replace will corrupt the record of store revision 62, 63 or 65.** `apply164.py` slices §1
> before substituting and asserts afterwards that everything outside §1 is byte-identical. This is
> [MOO-187](/MOO/issues/MOO-187) finding **F21**, and it is the finding most likely to cause actual
> damage.

**Six anchored edits + one recorded apostrophe normalisation.** Deliverable: the issue document
[`moo164-act-versus-notice`](/MOO/issues/MOO-164#document-moo164-act-versus-notice) on
[MOO-164](/MOO/issues/MOO-164). The bill text lives in the Paperclip store, not here.

**Revision 5 re-cut Edits 164-1 and 164-2** on counsel findings F8/F18/F23 and F3. **The patch delta
is +642 characters, not the +490 of revisions 1 to 4.**

## Base

Re-verified at **store revision 65** (document revision `bc0576f5`; whole document 346,114
characters; **enacted §1 121,576**). The base has moved twelve times under this cut. Store revision
65 added 137 characters to subdivision D 1, so **§6.3's reproduction was stale again** and is
re-spliced by `repro65.py`.

## Application order

**Application of the MOO-141 patch does not precede this cut carrying F-9.** This cut carries it, so
that condition is satisfied. Beyond that the two patches are **order-independent**, verified on three
bases: store revision 65 as it stands, with the MOO-141 patch at **revision 5** (Edit 3 at 30 days),
and with it at **revision 6** (Edit 3 at 120 days). Thirteen anchors, all 1; delta **+642** on all
three.

## Files

- `verify_r68.py` — **the current check.** Counts over enacted §1 only. Everything `verify_r65.py`
  did, plus: the named MOO-141 Edit 1 break, four assertions on what store revision 68 newly contains
  (m8-a enacted in clause (ii); the three-day extension confined to mailing; the electronic-giving
  rule; the 5:00 p.m. rule), and a sentence-order test on M 2 proving no MOO-164 edit or candidate
  inserts before the sentence D 1's ordinal reference points at.
- `verify_r65.py` — **superseded by `verify_r68.py`; it aborts on store revision 68** because it
  asserts MOO-141 Edit 1's dead FIND at 1. Kept as the record of the revision-5 run. Counts over
  enacted §1 only. Builds all three bases,
  asserts every anchor resolves exactly once, asserts the +642 delta, and **counts** (never predicts)
  the verb census, the `period allowed` sweep and every figure the deliverable quotes. Exits non-zero
  if any of them moves.
- `repro65.py` → `repro65.json` — **the current splicer** for the §6 reproductions. Locates every
  provision by content, not by line index. **Re-run this, do not hand-edit the reproductions**,
  whenever the base moves.
- `apply164.py` — applies the six edits to a **copy**, §1 only, with the out-of-§1 byte-identity
  assertion.
- `moo164.md` — the assembled deliverable as stored (revision 5).
- **Superseded, kept only as the record of earlier runs:** `verify_r63.py`, `verify_r64.py`,
  `repro63.py` / `repro63.json`, `repro.py`, `head63.md`, `head64.md`, `s1_64.txt`,
  `doc_part1..6.md`. **`verify_r6.py` and `verify.py` were deleted at revision 5** — they counted
  whole-document and hard-failed on store revisions 63 and later, and the README used to call one of
  them current (F21).

## To reproduce

```
# fetch bill-text-s8 from MOO-42 to bill.md, then:
python3 verify_r68.py bill.md     # 0 failures expected
python3 apply164.py bill.md       # writes applied.md
python3 repro65.py                # writes repro65.json (reads bill.md)
```

**Nothing in this kit has been applied to the store.** The apostrophe normalisation is drafted and
verified, not applied; it belongs in the next store revision carrying these edits and must be
recorded in §0 as a non-substantive normalisation.

## Five candidates, none applied

- **164-7** (item 130, route (c)) — M 2, two sentences, +898 characters. **Revised at revision 5 on
  F19 and F20**: it now carries **both** of MOO-141 Edit 1's trigger limbs, and its saving clause is
  Edit 1's verbatim with one express exception for the 15-day duty.
- **164-7-B** — the same sentence with a second trigger for the definition-request class (F22).
- **164-8** — D 1, one sentence, +485 characters: a filing vehicle for the member whose window has
  closed.
- **164-9** — F1: the 48-day cap keyed to the later of the act and the expiry of the allowed period.
  Closes the 60-day residual at M 2's tolling endpoint, at the price of card (f)'s full 78 days.
- **164-10** — F6: *"after the request is filed"*, five words, M 2's 90-day duty.
- **164-11** — F12: conforms the enacted expiry-notice sentence's period formula.

All of their FIND strings are asserted at count 1 in `verify_r65.py`.

**Internal working draft. Not a Division of Legislative Services bill. Not legally cleared by
counsel — [MOO-187](/MOO/issues/MOO-187) is an internal adversarial pass, expressly not legal advice.
Not legally sufficient for introduction.**
