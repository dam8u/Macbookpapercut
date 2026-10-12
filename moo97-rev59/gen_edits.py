#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate edits.py for store revision 59 from the live snapshot bill.md.

Every FIND is EXTRACTED from the live body rather than retyped, so a curly
apostrophe or a stray double space cannot break the apply step. Every READ is
built by explicit sub-replacements inside the extracted FIND, each of which is
asserted to fire exactly once.
"""
import re
import sys

B = open('bill.md').read()
BILL = B[B.index('## 1. The bill'):B.index('## 2. Section-by-section')]

EDITS = []


def grab(start, end_sub, label):
    """Exact live substring from `start` through the first `end_sub` after it."""
    i = BILL.find(start)
    assert i >= 0, (label, 'start not found', start[:60])
    j = BILL.find(end_sub, i)
    assert j >= 0, (label, 'end not found', end_sub[:60])
    s = BILL[i:j + len(end_sub)]
    assert B.count(s) == 1, (label, 'FIND occurs %d times in document' % B.count(s))
    return s


def grab_any(start, end_sub, label):
    """As grab, but tolerant of either apostrophe form in either marker."""
    for s_ap in ("'", '’'):
        for e_ap in ("'", '’'):
            st = start.replace("'", s_ap).replace('’', s_ap)
            en = end_sub.replace("'", e_ap).replace('’', e_ap)
            if BILL.find(st) >= 0 and BILL.find(en, BILL.find(st)) >= 0:
                return grab(st, en, label)
    raise AssertionError((label, 'no apostrophe variant matched'))


def sub(text, old, new, label):
    assert text.count(old) == 1, (label, 'sub anchor %r occurs %d times' % (old[:50], text.count(old)))
    return text.replace(old, new, 1)


def add(label, find, read):
    assert read != find, (label, 'READ equals FIND')
    assert read not in B, (label, 'READ already present')
    EDITS.append((label, find, read))


# ---------------------------------------------------------------- E1
# MOO-161 F1 (fatal), F2, F15 — the (f) sentence.
f = grab('Notwithstanding subdivision C 1 of § 51.1-165 and so much of subsection F',
         'the requirement that the member be in service shall not apply.', 'E1')
r = sub(f,
        "where clause (i) of this subdivision applies, § 51.1-163 shall not apply to the member's death and the Board shall determine",
        "where clause (i) of this subdivision applies and the member dies after the Board has received the notification of the member's effective date of retirement required by subdivision D 1 and before that date, the Board shall determine",
        'E1-F1')
r = sub(r,
        'computed taking account of the service credit credited under this subdivision',
        "computed on the member's creditable service, including the service credit credited under this subdivision",
        'E1-F15')
add('E1 — G 4, the (f) sentence (F1 fatal, F2, F15)', f, r)

# ---------------------------------------------------------------- E2
# F17 (split the waiver from the election), F12 (fiduciary addressee and the
# review clock), F13 ("that date"), F14 (the rider reaches the amount).
f = grab('Where the member dies, the Board shall give written notice of the service credit credited',
         'runs from the date the notice is given to that person.', 'E2')
r = sub(f,
        "of any right of the person entitled to any benefit payable on the member's death to waive that benefit or to elect another benefit in its place under § 51.1-162 and, where § 51.1-162 states a period within which the waiver or election must be made, of that period,",
        "of any right under subsection C of § 51.1-162 of a person entitled to any benefit payable on the member's death to waive the allowance and of the period stated in that subsection within which the waiver must be made, of any right of such a person under subsection B of § 51.1-162 to elect to be paid the member's accumulated contributions or a lump sum in lieu of any other benefit under that section,",
        'E2-F17')
r = sub(r,
        "to each person entitled to any benefit payable on the member's death, to any person who claimed",
        "to each person entitled to any benefit payable on the member's death or, where that person is a minor or is under a disability, to that person's guardian, conservator, committee, or other fiduciary and, where there is none, to the person to whom the Board pays or would pay the benefit, to any person who claimed",
        'E2-F12a')
r = sub(r,
        "or, as to a person whose entitlement or non-entitlement to any benefit payable on the member's death the Board determines after that date, no later than 30 days after that determination",
        "or, as to a person whose entitlement or non-entitlement to any benefit payable on the member's death, or the amount of any benefit payable to that person, the Board determines after the earlier of those dates, no later than 30 days after that determination",
        'E2-F13-F14')
r = sub(r,
        'runs from the date the notice is given to that person.',
        'runs from the date the notice is given to that person or, where this subdivision requires the notice to be given to another person in respect of that person, from the date it is given to that other person.',
        'E2-F12b')
add('E2 — G 4, the death notice (F17, F12, F13, F14)', f, r)

# ---------------------------------------------------------------- E3
# F18 — the J hook for the notice, made person-specific.
f = grab('The Board shall state in the report required by subsection J every failure to give the notice required by the preceding sentence',
         'within the period this subdivision allows for it.', 'E3')
r = sub(f,
        'every failure to give the notice required by the preceding sentence within the period this subdivision allows for it.',
        'every failure to give the notice required by the preceding sentence to a person within the period this subdivision allows for the giving of it to that person.',
        'E3-F18')
add('E3 — G 4, the J hook for the death notice (F18)', f, r)

# ---------------------------------------------------------------- E4
# The Policy Director's F13(c) — a 30-day duty on the employing state agency to
# tell the Board of the death, with a subsection J line. Drafted on G 4's own
# involuntary-separation model and placed immediately after the crediting
# deadline that runs from the Board "learn[ing] of" the death.
f = grab('The Board shall credit the service credit required by this subdivision no later than 60 days after it learns',
         'every failure to credit it within that period.', 'E4')
r = (f + ' A state agency that employs or last employed a member whose election the Board has '
         'accepted shall give the Board written notice of the member\'s death no later than 30 days '
         'after the agency learns of it, and the Board shall state every failure of a state agency to '
         'give that notice of which the Board becomes aware in the report required by subsection J.')
add('E4 — G 4, the state agency death-notice duty (Director: F13(c))', f, r)

# ---------------------------------------------------------------- E5
# The Policy Director's F13(e) — run the 90-day redetermination from the date
# the Board learns of the death, in the death case.
f = grab('The Board shall, no later than 90 days after that date, redetermine',
         'redetermine', 'E5')
r = sub(f,
        'no later than 90 days after that date, redetermine',
        "no later than 90 days after that date or, where that date is the date of the member's death, no later than 90 days after the date on which the Board learns of the death, redetermine",
        'E5-F13e')
add('E5 — G 4, the redetermination clock in the death case (Director: F13(e))', f, r)

# ---------------------------------------------------------------- E6
# The Policy Director's F10/F11 trigger, F9(a)(i) and F9(b), all in and after
# the release sentence.
f = grab("Where the person entitled to any benefit payable on the member's death elects under § 51.1-162 to be paid",
         'that an amount settled remain charged against that limitation.', 'E6')
r = sub(f,
        "Where the person entitled to any benefit payable on the member's death elects under § 51.1-162 to be paid the member's accumulated contributions or a lump sum in lieu of any other benefit under that section, the Board",
        "Where no retirement allowance is payable under § 51.1-162 on the member's death, whether because the person entitled to any benefit payable on the member's death elects under § 51.1-162 to be paid the member's accumulated contributions or a lump sum in lieu of any other benefit under that section or because no such allowance is payable to any person, the Board",
        'E6-F10')
r = sub(r,
        'and shall restore it to the amount available under the limitation stated in the first sentence of subdivision D 2, no later than 60 days after the election,',
        'and shall restore it to the amount available under the limitation stated in the first sentence of subdivision D 2 only to the extent the amount settled has not been paid to the retirement system under subsection N, no later than 60 days after the election or, where no such allowance is payable to any person, no later than 60 days after the Board determines that no such allowance is payable,',
        'E6-F9a-i')
r = r + (' Where an amount released under the preceding sentence would not have been released had a '
         'determination of the Board been as it stands after reconsideration under subsection M or '
         'after judicial review, the Board shall reinstate the amount released, together with any '
         'contingency amount released with it, no later than 30 days after the determination is '
         'reconsidered or reviewed, and the rule of this subdivision that no certified subsidy is '
         'settled more than once does not prevent the settlement of an amount so reinstated.')
add('E6 — G 4, the release trigger, the cap restoration and reinstatement on review (Director: F10/F11, F9(a)(i), F9(b))', f, r)

# ---------------------------------------------------------------- E7
# F6 — D 1's second compelled proposition: C 2's in-service condition, its own
# greater-of, and its payee by cross-reference rather than by paraphrase.
f = grab('that subdivision C 2 of § 51.1-165, where it applies, entitles the person named as contingent annuitant',
         'whichever is greater;', 'E7')
r = ("that where the member dies while in service and subdivision C 2 of § 51.1-165 otherwise applies, "
     "that subdivision provides the greater of the benefit payable in accordance with § 51.1-163 and the "
     "benefit payable under subsection B of § 51.1-162, each payable to the person entitled to it under "
     "the provision under which it is determined, and that the Board shall pay the benefit that "
     "subdivision provides or the benefit determined under subdivision G 4, whichever is greater;")
add('E7 — D 1, the C 2 proposition (F6)', f, r)

# ---------------------------------------------------------------- E8
# F4 — § 51.1-162 C is not confined to a surviving spouse.
f = grab_any('that subsection C of § 51.1-162 provides a retirement allowance to a surviving spouse',
             "Compensation Act (§ 65.2-100 et seq.);", 'E8')
ap = '’' if '’' in f else "'"
r = ('that subsection C of § 51.1-162 provides a retirement allowance, where the member%ss death results '
     'from a cause compensable under the Virginia Workers%s Compensation Act (§ 65.2-100 et seq.), to the '
     'member%ss surviving spouse, minor children, or parents as that subsection provides;' % (ap, ap, ap))
add('E8 — D 1, the § 51.1-162 C proposition (F4)', f, r)

# ---------------------------------------------------------------- E9
# F5 — § 51.1-162 A's condition is subsection B alone.
f = grab_any('and that where no allowance is payable under subsection B or C of § 51.1-162',
             "provides for the payment of the member's accumulated contributions.", 'E9')
r = sub(f,
        'where no allowance is payable under subsection B or C of § 51.1-162',
        'where no benefit is payable under subsection B of § 51.1-162',
        'E9-F5')
add('E9 — D 1, the § 51.1-162 A proposition (F5)', f, r)

# ---------------------------------------------------------------- E10
# F9 — the omission is a failure, not a determination, and its clock runs from
# the G 4 death notice.
f = grab_any("A failure to state in the Board's certification every matter required by the preceding sentence",
             'in the report required by subsection J.', 'E10')
ap = '’' if '’' in f else "'"
r = ('A failure to state in the Board%ss certification every matter required by the preceding sentence '
     'is a failure of the Board for the purposes of subsection M; a person adversely affected by it may '
     'seek review under subsection M no later than 30 days after the date on which the notice required '
     'by subdivision G 4 is given to that person; and the Board shall state every such failure in the '
     'report required by subsection J.' % ap)
add('E10 — D 1, the consequence of an incomplete certification (F9)', f, r)

# ---------------------------------------------------------------- E11
# F9 — M 2's failure limb has to reach a notice or certification that was given
# on time and left a required matter out. Re-cut on the live text: store
# revision 59 or 60 added "or to make a payment" to this limb.
f = grab('or by a failure of the Board to make a determination, to give a notice, or to make a payment within a period required by this section, may obtain',
         'written reconsideration by the Board stating the reasons for its decision.', 'E11')
r = sub(f,
        'within a period required by this section, may obtain',
        'within a period required by this section, or by a failure of the Board to state in a certification or notice a matter this section requires to be stated in it, may obtain',
        'E11a')
r = sub(r,
        'or, in the case of such a failure, at any time before the Board makes the determination, gives the notice, or makes the payment,',
        'or, in the case of a failure to make a determination, to give a notice, or to make a payment, at any time before the Board makes the determination, gives the notice, or makes the payment, or, in the case of a failure to state a matter, within the period provided by the provision that requires the matter to be stated,',
        'E11b')
add('E11 — M 2, the failure limb and its filing window (F9)', f, r)

# ---------------------------------------------------------------- E12 / E13
# F8 — the open formula reaches the public through subsection K's public notice.
# Replaced in both class lists by the two recipients the amendment was for.
NARROW = ("person who claimed any benefit payable on the death of a member and whom the Board determined "
          "is not entitled to it, or employer that paid on a member%ss behalf")
for lbl, tail in (
        ('E12 — M 2, the reconsideration class (F8, F19, F20)',
         ', adversely affected by a determination of the Board under this section,'),
        ('E13 — M 2, the judicial-review class (F8, F19, F20)',
         ', aggrieved by, and claiming the unlawfulness of, such case decision,')):
    f = 'or other person to whom this section requires a notice to be given' + tail
    assert BILL.count(f) == 1, (lbl, BILL.count(f))
    assert B.count(f) == 1, (lbl, 'document', B.count(f))
    ap = '’' if '’' in BILL[BILL.index(f) - 400:BILL.index(f)] else "'"
    r = (NARROW % "'") + tail
    add(lbl, f, r)

# ---------------------------------------------------------------- write
with open('edits.py', 'w') as fh:
    fh.write('# -*- coding: utf-8 -*-\n# Generated by gen_edits.py from the live body; do not hand-edit.\nEDITS = [\n')
    for lbl, f, r in EDITS:
        fh.write('    (%r,\n     %r,\n     %r),\n' % (lbl, f, r))
    fh.write(']\n')

net = sum(len(r) - len(f) for _, f, r in EDITS)
print('%d edits generated; net %+d chars to §1' % (len(EDITS), net))
for lbl, f, r in EDITS:
    print('  %-80s %5d -> %5d  (%+d)' % (lbl[:80], len(f), len(r), len(r) - len(f)))
