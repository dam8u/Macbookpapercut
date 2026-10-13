# -*- coding: utf-8 -*-
"""MOO-215 — the load-bearing fiscal assumption test on Edit 2 revision 8's D 1 channel.

The assumption under test is the Policy Director's, at `moo141-edit2-recut-rev71.md` §2.6
and §6: "The 12-month aggregate cap is unmoved, so there is nothing to re-price."

That is the SOLE stated ground for opening no Fiscal & Impact Modeler issue. It is a
statement about a BOUND. The quantity that drives cost in MOO-163 is not a bound, it is a
POPULATION against a fixed $3,000,000 pool. So the test is: how many members can the
residual limb newly put into D 1's lateness channel over the 48-month pilot, and how does
that compare with the smallest effect MOO-163/MOO-170 were willing to call non-zero?

MOO-163's register is IMPORTED UNCHANGED and not edited. The only thing added here is the
Board no-act rate, which appears NOWHERE in that register — and that absence is the point.

Run: python3 d1_channel_test.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'moo163-retention-endpoint'))
import moo163_inputs as R   # noqa: E402  imported unchanged, never written to

PILOT_DAYS = R.PILOT_LENGTH_MONTHS * 30
EXCLUDED_AGG_CAP_DAYS = 365      # the definition's own "shall not exceed 12 months"

# MOO-170 reported 2.80 members as the largest displacement it found and called it
# "still inside the resolution of the inputs, but by a narrower margin than at MOO-163".
# That is the only resolution threshold either issue states in members. Use theirs.
MOO170_RESOLUTION_MEMBERS = 2.80

print(f'== register imported unchanged from MOO-163; pilot {R.PILOT_LENGTH_MONTHS} months '
      f'= {PILOT_DAYS} days')
refused = sum(R.STATUTORY_REFUSALS_CENTRAL.values())
print(f'   refused members over the pilot (sum of the four refusal rows): {refused:.2f}')
print(f'   funded cohort over the pilot (central): {R.PARTICIPANTS_ADMITTED_FUNDED["central"]:.2f}')
print(f'   M 2 seek rate: {R.RECONSIDERATION_SEEK_RATE}')
print('   Board NO-ACT rate: ABSENT FROM THE REGISTER. Swept below, not assumed.')

# Class 1 — reconsideration denied by operation of law (M 2). Requires: Board fails to act
# in 90 days, member files the expiry notice, Board fails to act in a further 30 days.
# Class 2 — a request under the definition of "final qualifying retirement date" on which
# the Board does not act within the period allowed. Any member of the funded cohort may
# file one; no second gate.
print('\n== newly exposed population, members over the 48-month pilot')
print(f'{"no-act rate":>12} | {"class 1 (M 2 denial)":>22} | {"class 2 (definition req)":>24} | '
      f'{"total":>7} | vs MOO-170 resolution')
for p in (0.00, 0.02, 0.05, 0.10, 0.20, 0.35, 0.50):
    # class 1: refused -> seeks M 2 -> Board no-act at 90 days -> member files expiry
    # notice -> Board no-act again. Two independent no-act gates, member-notice gate
    # set to 1.00 (every member files it) to stay on the cautious side.
    c1 = refused * R.RECONSIDERATION_SEEK_RATE['central'] * p * 1.00 * p
    # class 2: the funded cohort may each file one later-date request; one no-act gate.
    c2 = R.PARTICIPANTS_ADMITTED_FUNDED['central'] * p
    tot = c1 + c2
    flag = 'ABOVE' if tot > MOO170_RESOLUTION_MEMBERS else 'below'
    print(f'{p:>12.2f} | {c1:>22.3f} | {c2:>24.3f} | {tot:>7.3f} | {flag}')

print('\n== the no-act rate at which the total crosses MOO-170\'s own resolution threshold')
# c1 is quadratic in p and tiny; solve on the dominant class-2 term and confirm.
p_star = MOO170_RESOLUTION_MEMBERS / R.PARTICIPANTS_ADMITTED_FUNDED['central']
print(f'   class 2 alone reaches {MOO170_RESOLUTION_MEMBERS} members at a no-act rate of '
      f'{p_star:.3f} ({p_star*100:.1f}%)')

print('\n== extension-day volume, which is what D 1 actually produces')
print('   Per member the limb is capped by the definition\'s own excluded aggregate:')
print(f'   {EXCLUDED_AGG_CAP_DAYS} days = 12 months. The cap is per member, not per cohort,')
print('   so an unmoved cap bounds the PER-MEMBER extension and says nothing about the')
print('   aggregate. Cohort extension-days = population x per-member days:')
for p in (0.05, 0.20, 0.50):
    pop = (refused * R.RECONSIDERATION_SEEK_RATE['central'] * p * p
           + R.PARTICIPANTS_ADMITTED_FUNDED['central'] * p)
    print(f'   no-act {p:.2f}: {pop:6.3f} members x up to {EXCLUDED_AGG_CAP_DAYS} days '
          f'= up to {pop*EXCLUDED_AGG_CAP_DAYS:8.1f} member-days '
          f'({pop*EXCLUDED_AGG_CAP_DAYS/PILOT_DAYS*100:5.2f}% of one pilot length)')

print('\n== does MOO-163 model this channel at all?')
levers = [n for n in dir(R) if n.isupper()]
hits = [n for n in levers if any(k in n for k in
        ('QUALIFY', 'FQRD', 'EXTENS', 'LATE', 'NOTICE_DAY', 'NO_ACT', 'D1'))]
print(f'   register levers: {len(levers)}')
print(f'   levers touching the FQRD extension / lateness / no-act channel: {hits or "NONE"}')
print('   -> MOO-163 prices QUEUE ORDERING against a fixed pool. It carries no FQRD')
print('      extension lever and no Board no-act rate. The $0 and the $204,000 bound')
print('      therefore do not cover this channel in either direction.')
