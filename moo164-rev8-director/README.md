# MOO-164 — the Policy Director's disposition of revision 8 (store revision 72)

| file | what it is |
|---|---|
| `moo164-disposition-rev8.md` | the disposition. Published on MOO-164 as `moo164-disposition-rev8` |
| `verify_xpatch_r72.py` | **the current check.** 95 checks, 0 failures. `python3 verify_xpatch_r72.py [live.md]` |
| `fetch.py` | `python3 fetch.py bill-text-s8 live.md` — re-fetch the base from MOO-42 |
| `live.md` | `bill-text-s8` at store revision 72, document revision `368f5e41`. §1 sha256 `83a10b74950b5272…` |

## What the verifier does that neither patch kit can do for itself

It lifts the **current** fixtures out of **both** kits —
`moo164-act-versus-notice/verify_r72_v8.py` (thirteen substitutions, +4,210) and
`moo141-rev72/verify_r72.py` (four edits, +1,716) — and counts the invariants **between** them.
Nothing is re-typed. Each kit holds a fixture of the other that is one revision stale right now, and
both report 0 failures while testing a superseded other half.

It also builds the **revision-9 target** — the twelve surviving substitutions, the three 164-7
repairs, 164-18 in with Edit 164-12 dropped, and 164-14 re-cut, 164-15 and 164-17 applied — and
asserts order-independence against MOO-141 revision 9 as repaired. **+4,902 alone, +6,637 combined,
byte-identical in either order.**

## The board's answers it encodes

Interaction `b4f375e1-49db-4875-8110-85817b235c90`, resolved by `local-board` at 02:08:17 UTC on
13 October 2026: **164-15 taken with the 90-day bound; 164-17 taken into this cut; 164-18 taken and
Edit 164-12 dropped.**

**Internal working draft material. Not a DLS bill. Not reviewed or cleared by counsel.
Pre-decisional. Nothing applied to the store.**
