# -*- coding: utf-8 -*-
"""MOO-164 re-check at **store revision 64** — the eleventh base move, and the first one that
changes nothing in the text this cut amends.

Store revision 64 is **record only**: it adds §7 item 131 and two §0/§6 record edits and moves no
word of either section. This script proves that rather than asserting it: it asserts that enacted §1
at store revision 64 is **byte-identical** to enacted §1 at store revision 63, then re-runs every
count from verify_r63.py on the revision-64 body so the result stands on its own.

It then adds the checks the Policy Director's 17:57 decision needs, in three groups:

  A. **Limb reach** — that each of the Director's three limbs is keyed to the Board's act by a form
     candidate 164-7's confinement clause actually catches (*begins upon*, *ends upon*, *measured
     from*), and that limbs 2 and 3 share one sentence, which is why clause (ii) cannot reach them.
  B. **The subsection A backstop** — the two *"notwithstanding any other provision of this
     definition"* sentences, located and counted, so the direction-of-operation finding at §14.2 can
     be checked against the words rather than taken on trust.
  C. **Antecedent and ordinal integrity** — that inserting 164-7 after the enacted denial sentence
     leaves *"such case decision"* (new item 131) pointing at the same sentence it points at today,
     and leaves D 1's *"the second sentence of subdivision M 2"* pointing at the same sentence.

Requires head64.md = `bill-text-s8` as fetched live, and head63.md from the previous run.
Nothing is written to the store."""
import re
import sys

fail = 0


def sec1(doc):
    i = doc.index('\n## 1.')
    m = re.search(r'\n## (?!1\.)', doc[i + 5:])
    return doc[i:i + 5 + m.start()]


BILL63 = sec1(open('head63.md', encoding='utf-8').read())
BILL = sec1(open('head64.md', encoding='utf-8').read())

print('== base')
print(f'   store rev 63 enacted §1 = {len(BILL63)} characters')
print(f'   store rev 64 enacted §1 = {len(BILL)} characters')
print(f'   byte-identical: {BILL == BILL63}')
if BILL != BILL63:
    fail += 1

E1_F = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_R = ("every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. "
        "For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, "
        "the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or "
        "last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board "
        "first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to "
        "make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by "
        "this section.</u>")
E2_F = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E2_R = "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."
E3_F = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_R5 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"
E3_R6 = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"


def build(e3):
    out = BILL
    for f, r in ((E1_F, E1_R), (E2_F, E2_R), (E3_F, e3)):
        assert out.count(f) == 1, f[:60]
        out = out.replace(f, r, 1)
    return out


BASES = [("store rev 64", BILL),
         ("store rev 64 + MOO-141 patch rev 5", build(E3_R5)),
         ("store rev 64 + MOO-141 patch rev 6", build(E3_R6))]

EDITS = [
 ("164-1 card (b)",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until the later of (a) 30 days after the Board acts upon the request and (b) 30 days after the Board gives the person who filed the request written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request"),
 ("164-2 card (h)",
  "or has not given it within 60 days after the determination date, the determination takes effect on the first day",
  "or has not given it within 60 days after the determination date, or where the determination could not take effect within 120 days after the determination date consistently with the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect, the determination takes effect on the first day"),
 ("164-3 card (j)",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "excluding any period after the expiration of the period allowed by this section for acting upon the request and before the Board acts upon the request"),
 ("164-4 F-5",
  "within the period this definition allows for acting upon it",
  "within the period allowed by this section for acting upon it"),
 ("164-5 F-9",
  "any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition by reason of the Board's action upon a request"),
 ("164-6 conforming",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate",
  "a failure of the Board to act upon such a request within the period allowed by this section for acting upon the request shall not extend that aggregate"),
]

DENIAL = ("the request is denied on the first day after the expiration of those 30 days, and that denial "
          "constitutes the final determination of the Board upon the reconsideration and a case decision "
          "as defined in § 2.2-4001 for the purposes of this subsection.")

HELD = [
 ("c-1", "For the purposes of this subdivision an application for a disability retirement allowance is pending"),
 ("c-2", "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending."),
 ("card (i) insertion point", "The Board shall act upon a request for reconsideration within 90 days."),
 ("164-7 anchor (item 130)", DENIAL),
 ("164-8 anchor (first required)", "the member may state an effective date of retirement that is no earlier than the first day of the month following the month in which the Board gives the statement or notice, and the Board shall state every such delay in the report required by subsection J."),
]

for name, base in BASES:
    out, delta = base, 0
    print(f"\n== {name}  ({len(base)} chars)")
    for tag, f, r in EDITS:
        c = out.count(f)
        print(f"   {tag:18s} FIND count {c}  delta {len(r)-len(f):+d}")
        if c != 1:
            fail += 1
        else:
            out = out.replace(f, r, 1); delta += len(r) - len(f)
    for tag, f in HELD:
        c = base.count(f)
        print(f"   held: {tag:30s} FIND count {c}   (not applied)")
        if c != 1:
            fail += 1
    n = out.count('’'); out = out.replace('’', "'")
    print(f"   amendment delta {delta:+d} | apostrophes normalised {n} | final length {len(out)}")
    if delta != 490:
        fail += 1
    if n != 4:
        fail += 1

print('\n== occurrence classification over §1')
for p in ('acts upon', 'act upon', 'acting upon', 'action upon'):
    print(f'   {p!r:14s} {BILL.count(p)}')
tot = sum(BILL.count(p) for p in ('acts upon', 'act upon', 'acting upon', 'action upon'))
print(f'   total {tot}  (expected 21, unchanged from store revision 63)')
if tot != 21:
    fail += 1

# ---------------------------------------------------------------- A. limb reach
print('\n== A. the Director\'s three limbs, and the form each is keyed by')
LIMBS = [
 ("limb 1a  tolling endpoint",
  "must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request",
  "ENDS upon"),
 ("limb 1b  clause (ii) exclusion",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "ENDS upon"),
 ("limb 2   D 4 / D 5 retention",
  "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request",
  "ENDS upon"),
 ("limb 3   15-day duty on the application",
  "the Board shall act upon the application no later than 15 days after it acts upon the request",
  "MEASURED FROM"),
]
for tag, f, form in LIMBS:
    c = BILL.count(f)
    print(f'   {tag:40s} count {c}   keyed by: {form}')
    if c != 1:
        fail += 1

# limbs 2 and 3 are one sentence — which is why clause (ii) cannot reach either
i2 = BILL.index(LIMBS[2][1]); i3 = BILL.index(LIMBS[3][1])
between = BILL[i2:i3]
print(f'   limbs 2 and 3 in ONE sentence: {"." not in between}  '
      f'(characters between them: {len(between)}, full stops between: {between.count(".")})')
if '.' in between:
    fail += 1

# every limb form is caught by 164-7's confinement clause, which is Edit 1's words verbatim
CONFINE = ("under which a period begins or ends upon, or is measured from, the Board's acting, "
           "or last acting, upon the request")
for form in ('begins or ends upon', 'is measured from'):
    print(f'   confinement clause contains {form!r}: {form in CONFINE}')
    if form not in CONFINE:
        fail += 1
print(f'   and the same formula is Edit 1\'s, verbatim: '
      f'{"where a period begins or ends upon, or is measured from, the Board" in E1_R}')

# ------------------------------------------------- B. the subsection A backstop
print('\n== B. subsection A\'s express late-Board backstop')
NOTW = 'notwithstanding any other provision of this definition'
BACKSTOP = ("Where the Board does not act upon a request the filing of which tolled the running of the "
            "member's final qualifying retirement date under subsection M within the period this "
            "definition allows for acting upon it, and the date that would otherwise apply under this "
            "definition is earlier than the first day of the second month following the month in which "
            "that period expired, the member's final qualifying retirement date is, notwithstanding any "
            "other provision of this definition, that first day.")
print(f'   {NOTW!r} occurrences: {BILL.count(NOTW)}')
print(f'   the late-Board backstop sentence occurs: {BILL.count(BACKSTOP)}')
if BILL.count(BACKSTOP) != 1:
    fail += 1
# the finding at §14.2: its trigger is a one-way comparison — it raises an EARLY date to a floor
print(f'   trigger is "...is EARLIER than...": {"is earlier than the first day of the second month" in BACKSTOP}')
print(f'   consequent is "...IS that first day" (a floor, not a cap): '
      f'{BACKSTOP.rstrip().endswith("that first day.")}')
print(f'   contains no cap word (no "later than" limit on the member\'s date): '
      f'{"no event later than" not in BACKSTOP and "in no case later than" not in BACKSTOP}')
if 'no event later than' in BACKSTOP or 'in no case later than' in BACKSTOP:
    fail += 1
# and it is Edit 164-4's own site, so the two must be read together
print(f'   this sentence is Edit 164-4\'s site: {EDITS[3][1] in BACKSTOP}')
if EDITS[3][1] not in BACKSTOP:
    fail += 1

# ---------------------------------- C. antecedent and ordinal integrity under 164-7
print('\n== C. what inserting 164-7 after the denial sentence does to two references')
SUCH = 'such case decision'
COMPLETION = ("Upon completion of a reconsideration under this subsection, the final determination issued "
              "by the Board shall constitute a case decision as defined in § 2.2-4001.")
print(f'   {SUCH!r} occurrences: {BILL.count(SUCH)}  (new §7 item 131)')
print(f'   completion sentence occurrences: {BILL.count(COMPLETION)}')
if BILL.count(SUCH) != 1 or BILL.count(COMPLETION) != 1:
    fail += 1
i_den, i_comp, i_such = BILL.index(DENIAL), BILL.index(COMPLETION), BILL.index(SUCH)
print(f'   order in §1: denial@{i_den} < completion@{i_comp} < "such case decision"@{i_such}: '
      f'{i_den < i_comp < i_such}')
print('   -> 164-7 inserts at the END of the denial sentence, i.e. BEFORE the completion sentence,')
print('      so the nearest antecedent of "such case decision" stays the completion sentence.')
print(f'   does 164-7\'s own text introduce a competing "case decision" antecedent? '
      f'{"case decision" in CONFINE}')
if i_den > i_comp or i_comp > i_such:
    fail += 1

ORD = 'the second sentence of subdivision M 2'
M2_START = '<u>2. A member, retiree, beneficiary, applicant, personal representative'
# strip the subdivision designator "<u>2." — it is a designator, not a sentence
M2 = BILL[BILL.index(M2_START) + len('<u>2. '):i_such]
sentences = [s.strip() for s in re.split(r'(?<=\.)\s+(?=[A-Z<"(])', M2) if s.strip()]
print(f'   D 1 ordinal reference {ORD!r} occurrences: {BILL.count(ORD)}')
for n in range(1, 8):
    print(f'   M 2 sentence {n}: {sentences[n-1][:68]!r}')
print('   -> rev 63 inserted at sentences 4 and 5; 164-7 inserts at sentence 6. The ordinal points')
print('      at sentence 2 and is unmoved, as §13.9 reported at store revision 63.')
if BILL.count(ORD) != 1 or not sentences[1].startswith('Every determination'):
    fail += 1

print("\nFAILURES:", fail)
sys.exit(1 if fail else 0)
