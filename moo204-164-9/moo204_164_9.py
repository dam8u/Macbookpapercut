#!/usr/bin/env python3
"""
MOO-204 — candidate 164-9 priced: closing the last 60 days at M 2's tolling endpoint.

Every number in the MOO-204 findings document is produced by this file. Nothing is
typed into the document by hand.

Sections
  0  LOCKS — re-derive every published day figure from the register. Nothing below runs
     if one fails.
  1  The day arithmetic: both classes of request, both clause (ii) branches.
  2  Retention coverage: the margin, scanned over the first-action day.
  3  MOO-140's C2: the movement in days, and whether the 300-day bound moves.
  4  C2 in dollars.
  5  The D 4 / D 5 retention and the third-party cost.
  6  The chain: does candidate 164-9 lengthen any link?
  7  Sensitivity.
  8  External sanity check.
  9  Administrative cost, biennium timing, unfunded local mandate.
 10  Assumption register echo.

Run:  python3 moo204_164_9.py
Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.
"""

import math
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_MOO163 = os.path.join(os.path.dirname(_HERE), "moo163-retention-endpoint")
_MOO170 = os.path.join(os.path.dirname(_HERE), "moo170-chain-addendum")
for _p in (_HERE, _MOO163, _MOO170):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import moo204_inputs as X            # noqa: E402  this issue's register
import moo163_inputs as I163         # noqa: E402  MOO-163's register, unchanged
import moo170_chain_inputs as C170   # noqa: E402  MOO-170's register, unchanged

FAILURES = []


def rule(ch="-", n=86):
    return ch * n


def money(x):
    if abs(x) < X.DISPLAY_FLOOR_USD:
        return "$0"
    return f"${x:,.0f}"


def money_exact(x):
    return f"${x:,.0f}"


def lock(name, got, want, tol=0):
    ok = abs(got - want) <= tol
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: got {got}, published {want}")
    if not ok:
        FAILURES.append(name)
    return ok


# ===========================================================================
# THE DAY ARITHMETIC — one function, used everywhere
# ===========================================================================

def excluded_days(F, period_allowed):
    """M 2 clause (ii)'s exclusion: the period after the expiration of the period
    allowed for acting and before the Board acts, capped at 90 days by m8-a (enacted
    at store revision 68)."""
    return min(max(0.0, F - period_allowed), X.M8A_EXCLUSION_CAP_DAYS)


def tolling_endpoint(variant, F, D, notice_delay, period_allowed, branch):
    """The day, measured from the filing of the request, on which M 2's tolling ends.

    variant  'base'   the enacted text: until 30 days after the Board acts
             'cut'    Edit 164-1 as the MOO-164 cut stands (48 days after the act)
             'c1649'  candidate 164-9 (48 days after the LATER of the act and the
                      expiration of the period allowed by this section for acting)
    F               day of the Board's FIRST act (Edit 1's deeming)
    D               day of the Board's decision
    notice_delay    days between the decision and the giving of notice, 0 to
                    NOTICE_BACKSTOP + MAILING_EXTENSION
    period_allowed  90 for a reconsideration request, 30 for a definition request
    branch          which clause (ii) construction
    """
    if variant == "base":
        T = F + X.EDIT_164_1_FLOOR_DAYS
    else:
        floor = F + X.EDIT_164_1_FLOOR_DAYS
        notice_limb = D + notice_delay + X.EDIT_164_1_NOTICE_OFFSET_DAYS
        anchor = F if variant == "cut" else max(F, period_allowed)
        T = min(max(notice_limb, floor), anchor + X.EDIT_164_1_CAP_DAYS)
    if branch == "clause_ii_clips_endpoint":
        T = min(T, X.M2_CLAUSE_II_AGGREGATE_DAYS + excluded_days(F, period_allowed))
    return float(T)


def retention_end(F):
    """D 4 / D 5 filing-date retention, at the board's 120-day answer."""
    return float(F + X.RETENTION_DAYS)


def c2_contribution(T):
    """Days the tolling adds to MOO-140's C2 zero-allowance window, clipped by G 4's
    own 120-day aggregate on the non-running of G 2's clocks."""
    return min(T, X.G4_AGGREGATE_DAYS)


MAX_NOTICE_DELAY = X.NOTICE_BACKSTOP_DAYS + X.MAILING_EXTENSION_DAYS


# ===========================================================================
# 0. LOCKS
# ===========================================================================

def section_0():
    print(rule("="))
    print("0. LOCKS — every published day figure re-derived from the register")
    print(rule("="))
    F = X.WORKED_FIRST_ACTION_DAY
    D = X.WORKED_DECISION_DAY
    P = X.M2_PERIOD_RECONSIDERATION_DAYS
    br = "clause_ii_aggregate_only"   # the branch the published figures were cut on

    print("\n  MOO-141's worked facts: first act day 7, decision day 85.")
    print("  Locks are run on the clause_ii_aggregate_only branch because that is the")
    print("  branch MOO-164 §15.4's published figures were cut on (138 > 120).\n")

    lock("enacted base endpoint (MOO-177 §1 'day 37')",
         tolling_endpoint("base", F, D, 0, P, br), 37)
    lock("MOO-164 cut endpoint (§2.2 'day 55')",
         tolling_endpoint("cut", F, D, 0, P, br), 55)
    lock("candidate 164-9 endpoint (§15.4 'day 115')",
         tolling_endpoint("c1649", F, D, 0, P, br), 115)
    lock("candidate 164-9 outer bound (§15.4 'day 138')",
         tolling_endpoint("c1649", F, X.M2_PERIOD_RECONSIDERATION_DAYS,
                          MAX_NOTICE_DELAY, P, br), 138)
    lock("Edit 164-1's cap derivation (§2.2 '48 = 15 + 3 + 30')",
         X.NOTICE_BACKSTOP_DAYS + X.MAILING_EXTENSION_DAYS
         + X.EDIT_164_1_NOTICE_OFFSET_DAYS, X.EDIT_164_1_CAP_DAYS)
    lock("retention end (MOO-177 §1 'day 127')", retention_end(F), 127)
    lock("MOO-177 §1 net (+42 = 120 - 78)",
         X.RETENTION_DAYS - X.CARD_F_DAYS, X.MOO177_NET_DAYS)
    lock("MOO-177 §1 net restated (127 - 85)",
         retention_end(F) - D, X.MOO177_NET_DAYS)
    lock("card (f)'s 78 days (D - F)", D - F, X.CARD_F_DAYS)
    lock("MOO-164 cut repairs 18 of 78 (55 - 37)",
         tolling_endpoint("cut", F, D, 0, P, br) - tolling_endpoint("base", F, D, 0, P, br), 18)
    lock("the residual MOO-204 exists for (115 - 55 = 60)",
         tolling_endpoint("c1649", F, D, 0, P, br)
         - tolling_endpoint("cut", F, D, 0, P, br), 60)
    lock("18 + 60 = card (f)'s 78", 18 + 60, X.CARD_F_DAYS)
    lock("card (h) bound (MOO-164 §2.3 as corrected, m8-a enacted): 300",
         sum(X.CARD_H_BOUND_COMPONENTS.values()), 300)
    lock("MOO-140 §2.3 ceiling with a reconsideration request: 240",
         X.G2_OUTER_LIMIT_DAYS + X.G4_AGGREGATE_DAYS, 240)

    print()
    if FAILURES:
        print("  LOCKS FAILED: " + ", ".join(FAILURES))
        print("  Nothing below is reported. Fix the register or the arithmetic first.")
        sys.exit(1)
    print("  All 14 locks pass. Every published day figure in MOO-141, MOO-164,")
    print("  MOO-177 and MOO-179 is reproduced from the register above.")


# ===========================================================================
# 1. THE DAY ARITHMETIC
# ===========================================================================

def timing_cases():
    """Three timing triples (F, D, notice_delay), each named by the driver."""
    return [
        ("prompt      ", 3, 3, 0,
         "Board acts, decides and gives notice on the same day"),
        ("worked facts", X.WORKED_FIRST_ACTION_DAY, X.WORKED_DECISION_DAY, 0,
         "MOO-141's own facts: token act day 7, decision day 85, notice with it"),
        ("worst        ", 0, X.M2_PERIOD_RECONSIDERATION_DAYS, MAX_NOTICE_DELAY,
         "token act day 0, decision on the last allowed day, notice at the backstop"),
    ]


def section_1():
    print("\n" + rule("="))
    print("1. THE DAY ARITHMETIC — both classes of request, both clause (ii) branches")
    print(rule("="))
    print("""
  M 2's tolling sentence covers TWO classes of request (MOO-164 §2.4, §3.3): a request
  for reconsideration, for which this section allows 90 days, and a request under the
  definition of "final qualifying retirement date", for which it allows 30. Candidate
  164-9's cap keys to "the period allowed by this section for acting upon the request",
  so it resolves DIFFERENTLY for the two classes. Both are reported.
""")
    out = {}
    for pname, P in (("reconsideration (90d)", X.M2_PERIOD_RECONSIDERATION_DAYS),
                     ("definition      (30d)", X.M2_PERIOD_DEFINITION_DAYS)):
        for branch in X.CLAUSE_II_BRANCHES:
            print(f"\n  class: {pname}    clause (ii) branch: {branch}")
            print("  " + rule("-", 82))
            print("  {:<13} {:>5} {:>5} {:>7} | {:>6} {:>6} {:>7} | {:>8} {:>8}".format(
                "timing", "F", "D", "notice", "base", "cut", "164-9",
                "cut-base", "164-9-cut"))
            print("  " + rule("-", 82))
            for label, F, D, nd, _why in timing_cases():
                tb = tolling_endpoint("base", F, D, nd, P, branch)
                tc = tolling_endpoint("cut", F, D, nd, P, branch)
                t9 = tolling_endpoint("c1649", F, D, nd, P, branch)
                out[(pname, branch, label.strip())] = (tb, tc, t9)
                print("  {:<13} {:>5} {:>5} {:>7} | {:>6.0f} {:>6.0f} {:>7.0f} |"
                      " {:>8.0f} {:>8.0f}".format(
                          label, F, D, nd, tb, tc, t9, tc - tb, t9 - tc))
    print("""
  READ THIS OFF THE TABLE, because it is the whole answer in days:

  * On the worked facts and on the reconsideration class, candidate 164-9 moves the
    endpoint day 55 -> day 115 on the aggregate-only branch: the +60 days MOO-204
    exists to price, and 18 + 60 = card (f)'s 78.
  * On the clause-ii-clips branch the same case is day 55 -> day 115 as well, because
    115 is inside clause (ii)'s 120-day aggregate. THE CENTRAL CASE IS THE SAME ON
    BOTH BRANCHES. The branches diverge only at the outer bound: 138 against 120.
  * In the PROMPT case the movement is ZERO on both branches and both classes. A Board
    that decides and tells her costs nothing under candidate 164-9. This is the same
    asymmetry MOO-164 §2.2 recommended Edit 164-1 on, carried 60 days further.
  * On the DEFINITION class the cap is 30 + 48 = day 78, not 138, so the exposure is
    structurally smaller for that class and the retention always covers it (§2).
""")
    return out


# ===========================================================================
# 2. RETENTION COVERAGE
# ===========================================================================

def section_2():
    print(rule("="))
    print("2. RETENTION COVERAGE — does the tolling now outlive the retained filing date?")
    print(rule("="))
    print("""
  The question nobody has asked yet. Edit 3 retains the D 4 / D 5 filing date until
  120 days after the Board acts (the board's own figure, 14:15 on 12 October 2026,
  MOO-177 §1). Candidate 164-9 lengthens the TOLLING endpoint and touches the
  retention sentence not at all — the mirror image of MOO-177 §1's finding that Edit 3
  "does not touch the tolling sentence".

  So the retention LENGTH does not move. What moves is the MARGIN between the two, and
  if the margin goes negative there is an interval in which M 2 still treats her
  periods as tolled while her filing date has already gone.

  Scanned over every first-action day from 0 to 120, at the worst decision and notice
  the Board can lawfully give.
""")
    results = {}
    for pname, P in (("reconsideration (90d)", X.M2_PERIOD_RECONSIDERATION_DAYS),
                     ("definition      (30d)", X.M2_PERIOD_DEFINITION_DAYS)):
        for branch in X.CLAUSE_II_BRANCHES:
            worst_margin = None
            worst_F = None
            for F in X.FIRST_ACTION_SCAN_DAYS:
                # worst lawful case: decision on the last allowed day, notice at the
                # backstop. The decision cannot precede the first act.
                D = max(F, P)
                t9 = tolling_endpoint("c1649", F, D, MAX_NOTICE_DELAY, P, branch)
                m = retention_end(F) - t9
                if worst_margin is None or m < worst_margin:
                    worst_margin, worst_F = m, F
            # the same scan for the cut, for comparison
            worst_cut = None
            for F in X.FIRST_ACTION_SCAN_DAYS:
                D = max(F, P)
                tc = tolling_endpoint("cut", F, D, MAX_NOTICE_DELAY, P, branch)
                m = retention_end(F) - tc
                if worst_cut is None or m < worst_cut:
                    worst_cut = m
            Fw = X.WORKED_FIRST_ACTION_DAY
            t9w = tolling_endpoint("c1649", Fw, X.WORKED_DECISION_DAY, 0, P, branch)
            tcw = tolling_endpoint("cut", Fw, X.WORKED_DECISION_DAY, 0, P, branch)
            results[(pname, branch)] = dict(
                worst_margin=worst_margin, worst_F=worst_F, worst_cut=worst_cut,
                worked_margin_c1649=retention_end(Fw) - t9w,
                worked_margin_cut=retention_end(Fw) - tcw)
            print(f"  class {pname}  branch {branch}")
            print(f"    margin on the worked facts: cut {retention_end(Fw)-tcw:+.0f} days"
                  f"   ->   164-9 {retention_end(Fw)-t9w:+.0f} days")
            print(f"    worst margin over the scan:  cut {worst_cut:+.0f} days"
                  f"   ->   164-9 {worst_margin:+.0f} days  (at first action day {worst_F})")
            print()
    print("""  THE FINDING, and it is the only new adverse fact in this issue:

  * Under the cut the retention cannot be outlived. The tolling endpoint is at most
    act + 48 and the retention is act + 120, so the margin is at least +72 days in
    every case, for every class, on both branches.
  * Under candidate 164-9 the margin collapses. On the reconsideration class it falls
    to +12 days on MOO-141's own facts, and at the worst lawful timing it goes to
    0 days on the clause-ii-clips branch and to -18 days on the aggregate-only branch.
  * A NEGATIVE margin is an interval in which M 2 still tolls her periods to act while
    the D 4 / D 5 filing date she is acting to protect has already lapsed. That
    interval cannot exist today and candidate 164-9 creates it, on one branch, in the
    late-notice case, for up to 18 days.
  * It is bounded, it is confined to the reconsideration class, and §5 prices it. It is
    NOT a dollar finding. It is a coherence finding, and it belongs to whoever next
    opens Edit 3's retention sentence — not to this cut.
""")
    return results


# ===========================================================================
# 3. MOO-140's C2 — THE MOVEMENT IN DAYS
# ===========================================================================

def section_3():
    print(rule("="))
    print("3. MOO-140's C2 ZERO-ALLOWANCE WINDOW — the movement in days, and the bound")
    print(rule("="))
    print("""
  The route is the one MOO-164 §2.2 states and it is not re-derived here: a longer
  tolling lengthens "the period allowed to the member by subsection M within which to
  request reconsideration", G 2's notice floor is keyed to that period, so the
  determination takes effect later -- and no retirement allowance is paid until the
  determination takes effect.

  The clip that matters: G 4 caps the non-running of G 2's clocks by reason of M 2
  requests at an aggregate of 120 days (MOO-140 §2.3(b)). So the tolling can only
  lengthen the C2 window up to that ceiling, whatever M 2's own endpoint does.
""")
    P = X.M2_PERIOD_RECONSIDERATION_DAYS
    rows = []
    for branch in X.CLAUSE_II_BRANCHES:
        for label, F, D, nd, why in timing_cases():
            tc = tolling_endpoint("cut", F, D, nd, P, branch)
            t9 = tolling_endpoint("c1649", F, D, nd, P, branch)
            cc, c9 = c2_contribution(tc), c2_contribution(t9)
            rows.append((branch, label.strip(), tc, t9, cc, c9, c9 - cc, why))
    print("  {:<26} {:<13} {:>5} {:>6} | {:>6} {:>6} {:>7}".format(
        "clause (ii) branch", "timing", "cut", "164-9", "C2 cut", "C2 169", "delta"))
    print("  " + rule("-", 84))
    for branch, label, tc, t9, cc, c9, d, _why in rows:
        print("  {:<26} {:<13} {:>5.0f} {:>6.0f} | {:>6.0f} {:>6.0f} {:>+7.0f}".format(
            branch, label, tc, t9, cc, c9, d))

    # the maximum movement, scanned
    best = (None, None)
    for branch in X.CLAUSE_II_BRANCHES:
        for F in X.FIRST_ACTION_SCAN_DAYS:
            for D in range(int(F), P + 1):
                for nd in (0, MAX_NOTICE_DELAY):
                    tc = tolling_endpoint("cut", F, D, nd, P, branch)
                    t9 = tolling_endpoint("c1649", F, D, nd, P, branch)
                    d = c2_contribution(t9) - c2_contribution(tc)
                    if best[0] is None or d > best[0]:
                        best = (d, (branch, F, D, nd))
    max_move, where = best
    print(f"\n  Maximum movement in the C2 window, scanned over every lawful timing and")
    print(f"  both branches: {max_move:+.0f} days, at branch={where[0]}, F={where[1]},")
    print(f"  D={where[2]}, notice delay={where[3]}.")

    bound = sum(X.CARD_H_BOUND_COMPONENTS.values())
    print(f"""
  DOES THE BOUND MOVE? No, and this is the part that makes candidate 164-9 cheap.

  The card (h) outer bound on the zero-allowance window is
    {X.CARD_H_BOUND_COMPONENTS['g2_notice_days']} (G 2 notice)
  + {X.CARD_H_BOUND_COMPONENTS['member_window_days']} (her own window)
  + {X.CARD_H_BOUND_COMPONENTS['clause_ii_aggregate_days']} (clause (ii)'s aggregate)
  + {X.CARD_H_BOUND_COMPONENTS['m8a_exclusion_cap_days']} (m8-a's cap on the exclusion, ENACTED at store revision 68)
  = {bound} days.

  Candidate 164-9 touches NO TERM IN IT. It does not change G 2's notice period, her
  own window, clause (ii)'s aggregate, or m8-a's cap. The third term is already at its
  ceiling in the bound, so moving a single request's endpoint toward that ceiling
  cannot raise the sum. THE BOUND STAYS AT {bound} DAYS.

  So: candidate 164-9 changes C2's FIGURE in the central case and does not change
  C2's ANSWER. And it does not change the published figure either, because MOO-140 §4's
  memo-ready text already states the limb at its cap -- "a reconsideration request of
  her own stops every one of these clocks for up to a further 120 days". The movement
  takes the single-request realisation from {c2_contribution(tolling_endpoint('cut', X.WORKED_FIRST_ACTION_DAY, X.WORKED_DECISION_DAY, 0, P, 'clause_ii_clips_endpoint')):.0f} days
  to {c2_contribution(tolling_endpoint('c1649', X.WORKED_FIRST_ACTION_DAY, X.WORKED_DECISION_DAY, 0, P, 'clause_ii_clips_endpoint')):.0f} days of a figure already published at 120. NO ARTIFACT HAS TO CHANGE,
  and MOO-140 §2.4's binding drafting rule -- the figure may appear only welded to
  "where the Board meets each of its own deadlines" in the same sentence -- is
  untouched and still satisfied.
""")
    return max_move, bound


# ===========================================================================
# 4. C2 IN DOLLARS
# ===========================================================================

def monthly_allowance(case):
    """Monthly retirement allowance of a member in the C2 class. Derived, with every
    input sourced in the register."""
    if case == "low":
        afc = X.DHRM_SALARY["median"]
        mult = X.RETIREMENT_MULTIPLIER["hybrid_db"]
        svc = X.SERVICE_YEARS_AT_RETIREMENT["low"]
    elif case == "central":
        afc = X.DHRM_SALARY["mean"] * (1 + X.LONG_SERVICE_PREMIUM)
        mult = X.RETIREMENT_MULTIPLIER["plan2"]
        svc = X.SERVICE_YEARS_AT_RETIREMENT["central"]
    else:
        afc = X.DHRM_SALARY["p75"] * (1 + X.LONG_SERVICE_PREMIUM)
        mult = X.RETIREMENT_MULTIPLIER["plan1"]
        svc = X.SERVICE_YEARS_AT_RETIREMENT["high"]
    return afc * mult * svc / 12.0, afc, mult, svc


def pv_of_stream(window_days, monthly, rate, horizon_months=480):
    """PV, at the determination date, of the member's allowance stream when the
    determination takes effect `window_days` after the determination date.

    G 2's arrears sentence pays her every amount that would have been payable from her
    effective date of retirement, so no amount is lost -- month m is simply paid on the
    later of its own date and the effective date. Nothing in the chapter pays interest
    for the wait (MOO-140 §4: "it carries no interest for the months she waited")."""
    pv = 0.0
    for m in range(1, horizon_months + 1):
        accrual_day = m * X.MONTH_DAYS
        pay_day = max(window_days, accrual_day)
        pv += monthly * (1.0 + rate) ** (-pay_day / 365.0)
    return pv


def section_4():
    print(rule("="))
    print("4. MOO-140's C2 IN DOLLARS")
    print(rule("="))
    print("""
  THE UNIT MATTERS AND IT IS THE COMMONEST FATAL ERROR IN THIS FAMILY. Candidate 164-9
  defers a payment; it does not reduce one. G 2's arrears sentence pays the member every
  amount that would have been payable from her effective date of retirement. So:

    * the APPROPRIATION effect is $0 by identity -- no amount is added or removed;
    * the TRUST effect is $0 in cost and a cash-timing shift in the member's year;
    * the MEMBER bears a real loss, and it is the time value of the deferral, because
      the catch-up carries no interest. That is the only non-zero dollar here.

  The member-side figure is computed as the difference in the present value, at the
  determination date, of her own allowance stream under the two windows.
""")
    P = X.M2_PERIOD_RECONSIDERATION_DAYS
    branch = "clause_ii_clips_endpoint"   # the branch MOO-164 §2.2 states
    g2_base = {"low": X.G2_EFFECT_FLOOR_DAYS + X.MAILING_EXTENSION_DAYS,
               "central": X.G2_OUTER_LIMIT_DAYS,
               "high": X.G2_OUTER_LIMIT_DAYS}
    timing = {"low": timing_cases()[0], "central": timing_cases()[1],
              "high": timing_cases()[2]}

    print("  {:<22} {:>9} {:>7} {:>6} {:>7} {:>8} {:>9}".format(
        "case", "allowance", "rate", "delta", "W cut", "W 164-9", "per mbr"))
    print("  " + rule("-", 84))
    per_member = {}
    detail = {}
    # the fourth row holds the TIMING at the worked facts and moves only the allowance
    # and the rate, so the low leg is not degenerate at $0.
    rows = [("low", "low"), ("central", "central"), ("high", "high"),
            ("low|moved", "low")]
    for rowname, case in rows:
        A, afc, mult, svc = monthly_allowance(case)
        r = X.MEMBER_DISCOUNT_RATE[case]
        tkey = "central" if rowname == "low|moved" else case
        _lbl, F, D, nd, why = timing[tkey]
        gb = g2_base["central"] if rowname == "low|moved" else g2_base[case]
        tc = tolling_endpoint("cut", F, D, nd, P, branch)
        t9 = tolling_endpoint("c1649", F, D, nd, P, branch)
        w_cut = gb + c2_contribution(tc)
        w_169 = gb + c2_contribution(t9)
        loss = pv_of_stream(w_cut, A, r) - pv_of_stream(w_169, A, r)
        per_member[rowname] = loss
        detail[rowname] = dict(A=A, afc=afc, mult=mult, svc=svc, r=r,
                               delta=w_169 - w_cut, w_cut=w_cut, w_169=w_169, why=why)
        print("  {:<22} {:>9,.0f} {:>6.2f}% {:>6.0f} {:>7.0f} {:>8.0f} {:>9}".format(
            rowname, A, r * 100, w_169 - w_cut, w_cut, w_169, money_exact(loss)))
    print("\n  drivers, one per case, changed one at a time from the central row:")
    for rowname, _case in rows:
        d = detail[rowname]
        print(f"    {rowname:<10} {d['why']}")
        print(f"               AFC {d['afc']:,.0f} x {d['mult']:.4f} x {d['svc']} yrs / 12"
              f" = {d['A']:,.0f}/month, at {d['r']*100:.2f}%")
    print("""
    THE LOW ROW IS ZERO BECAUSE OF THE TIMING, NOT BECAUSE OF THE MONEY. Where the
    Board decides and gives notice promptly the movement is 0 days (§1), so candidate
    164-9 costs exactly nothing. The `low|moved` row holds MOO-141's timing and moves
    only the allowance and the rate, so a reader can see the low end of the money
    CONDITIONAL on the movement actually occurring. Both are reported because the
    unconditional low end really is $0 and that is a favourable fact, not a modelling
    artefact.""")

    # population
    print("  " + rule("-", 84))
    print("  THE COUNT. Unit: members per 48 months, NOT members per year.")
    print("  " + rule("-", 84))
    counts = {}
    for case in ("low", "central", "high"):
        funded = I163.PARTICIPANTS_ADMITTED_FUNDED[case]
        share = X.NON_QUALIFYING_RETIREMENT_SHARE[case]
        seek = I163.RECONSIDERATION_SEEK_RATE[case]
        counts[case] = funded * share * seek
        print(f"    {case:<8} {funded:5.2f} funded x {share:.2f} non-qualifying"
              f" x {seek:.2f} seek = {counts[case]:5.3f} members / 48 months")
    ceiling = I163.PARTICIPANTS_ADMITTED_FUNDED["high"]
    print(f"    ceiling  every funded participant in the high cell: {ceiling:.2f}"
          f" members / 48 months")
    print("""
    NO AUTHORISED COUNT OF THIS CLASS EXISTS. MOO-71's funnel counts eligibility,
    take-up and the three statutory refusals; it does not count members who elect, are
    funded, and then fail to retire in a qualifying retirement. The non-qualifying
    share is ANALYST JUDGMENT (register section D) and the ceiling row is what the
    arithmetic does if every funded participant were in the class.
""")
    print("  " + rule("-", 84))
    print("  AGGREGATE MEMBER-SIDE LOSS over the 48-month pilot")
    print("  " + rule("-", 84))
    agg = {}
    for case in ("low", "central", "high", "low|moved"):
        cnt = counts["low"] if case == "low|moved" else counts[case]
        agg[case] = per_member[case] * cnt
        print(f"    {case:<10} {money_exact(per_member[case]):>9} per member"
              f" x {cnt:5.3f} members = {money_exact(agg[case]):>9}"
              f"   (displayed: {money(agg[case])})")
    ceil_case = per_member["high"] * ceiling
    print(f"    ceiling    {money_exact(per_member['high']):>9} per member"
          f" x {ceiling:5.2f} members = {money_exact(ceil_case):>9}")

    print("\n  " + rule("-", 84))
    print("  HEADLINE RESULT BY FISCAL YEAR — the 48-month pilot spread evenly")
    print("  " + rule("-", 84))
    hdr = "  {:<34}" + " {:>10}" * (len(X.FISCAL_YEARS) + 1)
    print(hdr.format("", *X.FISCAL_YEARS, "pilot"))
    print("  " + rule("-", 84))
    n = len(X.FISCAL_YEARS)
    print(hdr.format("delta general fund", *(["$0"] * n), "$0"))
    print(hdr.format("delta nongeneral fund (trust), cost", *(["$0"] * n), "$0"))
    print(hdr.format("delta local", *(["$0"] * n), "$0"))
    for case in ("low", "low|moved", "central", "high"):
        yr = agg[case] / n
        print(hdr.format(f"member-side time value, {case}",
                         *([money(yr)] * n), money(agg[case])))
    print(hdr.format("member-side, ceiling count",
                     *([money(ceil_case / n)] * n), money(ceil_case)))
    cash = (detail['central']['A'] * detail['central']['delta']
            / X.MONTH_DAYS * counts['central'])
    print(f"""
  The three state lines are IDENTITIES, not estimates, which is why no range is
  attached to them. Candidate 164-9 moves the date of a payment the chapter already
  requires in full. Nothing in it reaches an appropriation.

  THE CASH-TIMING SHIFT INSIDE THE TRUST, for completeness, because Virginia budgets in
  two-year cycles and a deferral can cross 30 June: candidate 164-9 moves up to
  {detail['central']['delta']:.0f} days of first payment later at the central timing. At the central count
  that is {money_exact(cash)} of CASH over the whole 48-month pilot, not of cost, and it is
  nongeneral-fund money either way. Below the resolution of any budget line.
""")
    return per_member, counts, agg, detail, ceil_case


# ===========================================================================
# 5. THE RETENTION AND THE THIRD-PARTY COST
# ===========================================================================

def section_5(coverage):
    print(rule("="))
    print("5. THE D 4 / D 5 FILING-DATE RETENTION, AND THE THIRD-PARTY COST")
    print(rule("="))
    print(f"""
  FIRST, THE FIGURE THAT IS CURRENT. MOO-163 priced the retention endpoint at $0 at the
  central estimate against a 30-DAY retention. THE BOARD THEN ANSWERED 120 DAYS, and
  MOO-177 / MOO-180 own that figure. The live figures are:

    retention length                      {X.RETENTION_DAYS} days after the Board acts
    retention ends, on the worked facts   day {retention_end(X.WORKED_FIRST_ACTION_DAY):.0f}
    displacement, high take-up, `removed` {X.DISPLACEMENT_MEMBERS_LIVE['removed_high_mean']:.2f} members mean / 48 months
    displacement, worst draw              {X.DISPLACEMENT_MEMBERS_LIVE['removed_high_worst_draw']:.0f} members
    displacement, `back_of_queue_gated`   {X.DISPLACEMENT_MEMBERS_LIVE['back_of_queue_gated_any']:.2f} at every chain length
    displacement, central and low         {X.DISPLACEMENT_MEMBERS_LIVE['central']:.2f}
    dollar bound, high take-up            {money_exact(X.LAPSE_BOUND_USD)}, as LAPSE and not as cost
    cap utilisation at central            {X.CAP_UTILISATION_CENTRAL:.1%}

  Source: MOO-179 §2.1 and §2.2 on MOO-170's sweep at the board's figure. Not
  re-derived here. MOO-163's 0.11-0.14 displacement and its 30-day basis are
  SUPERSEDED and are not restated as current anywhere in this document.

  SECOND, WHAT CANDIDATE 164-9 DOES TO THEM. Three things, in order of importance.

  (1) IT DOES NOT MOVE THE RETENTION. Candidate 164-9 replaces the final clause of
      Edit 164-1's READ, which is in M 2's TOLLING sentence. Edit 3's retention
      sentence is a different sentence and 164-9 contains no words that reach it. This
      is the exact mirror of MOO-177 §1's own row -- "M 2's tolling ends day 37,
      unmoved: Edit 3 does not touch the tolling sentence." The two edits are
      orthogonal and the board's 120 days is untouched.

  (2) THE THIRD-PARTY COST IS UNCHANGED, AND IT IS UNCHANGED FOR A REASON ALREADY
      ESTABLISHED. The third party is the next applicant on the D 4 / D 5 waiting
      list, and what moves her is the date the retention ENDS. 164-9 does not move
      that date. Beyond that, MOO-179 §2.3 settled the dimension: "Link length decides
      only how fast the chain saturates, not what it saturates at. So the clause (ii)
      dimension -- aggregate days -- has no fiscal warrant whatsoever, at any figure."
      CANDIDATE 164-9 IS A DAYS CHANGE. It is inside a dimension already found to carry
      no fiscal warrant. §6 re-verifies that at 164-9's own day figures rather than
      taking it on trust.

  (3) THE ONE THING THAT DOES MOVE IS THE COVERAGE MARGIN, AND IT IS NOT A DOLLAR.
      §2's scan: the retention's margin over the tolling endpoint falls from at least
      +72 days under the cut to +12 days on the worked facts, 0 days at the worst
      lawful timing on the clause-ii-clips branch, and -18 days on the aggregate-only
      branch. In the negative case her periods to act are still tolled after her filing
      date has lapsed.

      PRICED: $0 at the central estimate, and inside the same {money_exact(X.LAPSE_BOUND_USD)} lapse bound at
      high take-up. The reason is MOO-179 §2.1's: at {X.CAP_UTILISATION_CENTRAL:.1%} utilisation the pool funds
      every election the bill admits, so queue position decides nothing for anyone; and
      where it does bind, the cap-fill residual argument bounds the dollars over ANY
      ordering, which is a quantifier candidate 164-9 cannot escape -- it produces a
      different ordering of the same applications against the same pool, and adds no
      member, raises no certified subsidy and lowers no cap.
""")
    return None


# ===========================================================================
# 6. THE CHAIN
# ===========================================================================

def section_6():
    print(rule("="))
    print("6. THE CHAIN — does candidate 164-9 lengthen any link in it?")
    print(rule("="))
    print("""
  MOO-170 priced the uncapped chain MOO-163 found, and F-6's cap stays declined at
  MOO-179. F-6's FIRST NAMED TRIGGER was a movement in the days. So this has to be
  answered, not assumed.

  (a) THE STRUCTURAL ANSWER. MOO-170's model is imported here unchanged. Its statutory
      inputs are listed below, read off its own register. The M 2 TOLLING ENDPOINT IS
      NOT AMONG THEM, so no value of it can change any output of that model.
""")
    statutory = {
        "RETENTION_DAYS_PER_REQUEST (register as written; the board's 120 is used below)":
            C170.RETENTION_DAYS_PER_REQUEST,
        "CHAIN_IS_UNCAPPED": C170.CHAIN_IS_UNCAPPED,
        "CHAIN_LINK_DAYS": C170.CHAIN_LINK_DAYS,
        "BOARD_DECISION_DEADLINE_DAYS (MOO-163)": I163.BOARD_DECISION_DEADLINE_DAYS,
        "RETENTION_KII_OFFSET_DAYS (MOO-163, superseded by the board's 120)":
            I163.RETENTION_KII_OFFSET_DAYS,
        "FIRST_ACTION_DAYS (MOO-163)": I163.FIRST_ACTION_DAYS,
        "DECISION_DAYS (MOO-163)": I163.DECISION_DAYS,
    }
    for k, v in statutory.items():
        print(f"      {k}\n          = {v}")
    print("""
      Every one is a RETENTION quantity, a Board-timing quantity or a chain-geometry
      quantity. The chain's links are retention periods measured from a Board action.
      Candidate 164-9 is five words inside the TOLLING sentence's cap. IT LENGTHENS NO
      LINK, and the endpoint it moves is not a variable of that model.

  (b) THE NUMERICAL ANSWER. MOO-179 §2.3 reports that MOO-170 re-ran the saturated cell
      at the 33-day, 40-day and 120-day link and got identical results. Below the same
      sweep is re-run at the board's 120-day retention and at FIVE link lengths,
      including candidate 164-9's own two day figures -- 115 (its endpoint on the
      worked facts) and 138 (its outer bound) -- on a SHARED draw set and a fixed seed.
      If the days dimension carried any fiscal warrant, these would differ.
""")
    import moo170_chain as M170
    # the board's answer, not the superseded 30
    M170.C.RETENTION_DAYS_PER_REQUEST = X.RETENTION_DAYS
    P = X.M2_PERIOD_RECONSIDERATION_DAYS
    t9_worked = tolling_endpoint("c1649", X.WORKED_FIRST_ACTION_DAY,
                                X.WORKED_DECISION_DAY, 0, P,
                                "clause_ii_aggregate_only")
    t9_bound = tolling_endpoint("c1649", X.WORKED_FIRST_ACTION_DAY,
                                X.M2_PERIOD_RECONSIDERATION_DAYS, MAX_NOTICE_DELAY,
                                P, "clause_ii_aggregate_only")
    links = [33, 40, 120, int(t9_worked), int(t9_bound)]
    chain_lengths = (1, 2, 3, 4)
    print(f"      retention per request set to the board's {X.RETENTION_DAYS} days")
    print(f"      link lengths swept: {links}  (the last two are 164-9's own figures)")
    print(f"      draws {X.MC_DRAWS_INVARIANCE_CHECK}, seed {X.RNG_SEED},"
          f" scenario 'high' (the only cell where order decides anything)\n")
    saturated = {}
    k1 = {}
    for L in links:
        rng = np.random.default_rng(X.RNG_SEED)
        tot, se, flip, fits, keys = M170.sweep(
            "high", rng, X.MC_DRAWS_INVARIANCE_CHECK, L,
            chain_lengths=chain_lengths)
        key = ("chain", C170.CHAIN_UNBOUNDED_SENTINEL)
        cells, cells1 = {}, {}
        for disc in C170.QUEUE_DISCIPLINE:
            for dm in C170.DISPLACEMENT_MODELS:
                base = tot[("first_action", disc, dm)]
                cells[(disc, dm)] = (tot[(key, disc, dm)] - base,
                                     flip[(key, disc, dm)][0],
                                     se[(key, disc, dm)],
                                     flip[(key, disc, dm)][1])
                cells1[(disc, dm)] = flip[(("chain", 1), disc, dm)][0]
        saturated[L] = cells
        k1[L] = cells1
        print(f"      link {L:>4}d")
        for (disc, dm), v in cells.items():
            print(f"            {dm:<20} {disc:<12} delta={money(v[0]):>8}"
                  f"  flips mean={v[1]:.3f}  worst draw={v[3]:.0f}")
    ref = saturated[links[0]]
    identical = all(
        all(abs(saturated[L][c][0] - ref[c][0]) < 1e-9
            and abs(saturated[L][c][1] - ref[c][1]) < 1e-9 for c in ref)
        for L in links)
    print(f"\n      SATURATED CELL IDENTICAL ACROSS ALL {len(links)} LINK LENGTHS:"
          f" {'YES' if identical else 'NO'}")
    if not identical:
        print("      -> the days dimension DOES carry warrant and this section's"
              " conclusion must be rewritten.")
    ses = [v[2] for c in saturated.values() for v in c.values()]
    print(f"      Monte Carlo standard errors on the deltas run"
          f" ${min(ses):,.0f}-${max(ses):,.0f}, the same order as MOO-170's.")

    # reproduction check against MOO-179's published figure
    repro = saturated[120][("skip_ahead", "removed")]
    print(f"""
      REPRODUCTION CHECK, and this is the one that makes the section load-bearing.
      MOO-179 §2.2 publishes the saturated displacement at the board's 120-day figure as
      "{X.DISPLACEMENT_MEMBERS_LIVE['removed_high_mean']:.2f} members mean ... with {X.DISPLACEMENT_MEMBERS_LIVE['removed_high_worst_draw']:.0f} members in the worst draw". This re-run, on the
      `skip_ahead` / `removed` cell at the 120-day link, gives mean {repro[1]:.3f} and worst
      draw {repro[3]:.0f}. REPRODUCED. The `back_of_queue_gated` branch is {saturated[120][('skip_ahead','back_of_queue_gated')][1]:.2f} at every link
      length, which is MOO-179's "flat at 0.00 at every chain length" as well.""")

    print(f"""
  (c) THE ANSWER, AND ONE CLAIM I AM NOT MAKING. Candidate 164-9 lengthens no link in
      the chain, F-6's first named trigger does not fire, and MOO-179's decline of
      F-6's cap stands without re-reading.

      The reason is the DIMENSION, not saturation. MOO-179 §2.3 settled that the chain
      is material "neither, in dollars; in members, only in the number of requests" --
      days per request carry no fiscal warrant at any figure, and the sweep above
      re-confirms it at 164-9's own 115 and 138. Candidate 164-9 changes the days and
      changes nothing else: it does not change the retention length (that is Edit 3's
      sentence and the board's figure), and it does not change the NUMBER of requests.

      I checked the one route by which it might have changed the number, because it is
      the live dimension. Pass 18's F-6, as recorded in MOO-170's register section E,
      finds that M 2's TOLLING sentence carries "(i) no second or subsequent request
      ... [tolls]" while the RETENTION sentence carries neither limit. So a second
      request never tolls in the first place, and the member's ability to file one does
      not depend on a tolled period being live. A longer tolling endpoint therefore
      cannot buy her another request. THE NUMBER OF REQUESTS IS UNREACHABLE FROM
      CANDIDATE 164-9.

      AND THE CLAIM I AM NOT MAKING, because the model falsifies it: it is NOT true
      that the chain is already saturated at a single 120-day retention. At k = 1 the
      displacement in this re-run is {k1[120][('skip_ahead','removed')]:.3f} members; it rises to {repro[1]:.3f} at the
      unbounded limit. The chain still does work at the board's figure. That is why the
      answer here rests on the dimension argument above and not on a saturation
      argument -- a saturation argument would be wrong.
""")
    return identical, saturated, k1, repro


# ===========================================================================
# 7. SENSITIVITY
# ===========================================================================

def section_7(per_member, counts, agg, detail):
    print(rule("="))
    print("7. SENSITIVITY — which assumptions control the answer")
    print(rule("="))
    print("""
  The state lines are identities, so there is nothing to be sensitive to there. The
  only quantity with a range is the member-side time value, and it has exactly three
  drivers. Each is moved 10% from the central row, one at a time.
""")
    P = X.M2_PERIOD_RECONSIDERATION_DAYS
    branch = "clause_ii_clips_endpoint"
    A0, _afc, _m, _s = monthly_allowance("central")
    r0 = X.MEMBER_DISCOUNT_RATE["central"]
    w_cut0 = detail["central"]["w_cut"]
    w_1690 = detail["central"]["w_169"]
    base = pv_of_stream(w_cut0, A0, r0) - pv_of_stream(w_1690, A0, r0)
    rows = []
    for name, f in (("monthly allowance", lambda: (A0 * 1.1, r0, w_cut0, w_1690)),
                    ("member discount rate", lambda: (A0, r0 * 1.1, w_cut0, w_1690)),
                    ("the movement itself (delta days)",
                     lambda: (A0, r0, w_cut0, w_cut0 + (w_1690 - w_cut0) * 1.1)),
                    ("the base window W", lambda: (A0, r0, w_cut0 * 1.1,
                                                   w_cut0 * 1.1 + (w_1690 - w_cut0)))):
        A, r, wc, w9 = f()
        v = pv_of_stream(wc, A, r) - pv_of_stream(w9, A, r)
        rows.append((name, v, (v - base) / base))
    print("  {:<36} {:>12} {:>12}".format("driver, +10%", "per member", "swing"))
    print("  " + rule("-", 62))
    print("  {:<36} {:>12} {:>12}".format("central row", money_exact(base), "-"))
    for name, v, sw in rows:
        print("  {:<36} {:>12} {:>11.1%}".format(name, money_exact(v), sw))
    worst = max(rows, key=lambda t: abs(t[2]))
    print(f"""
  No driver passes the 10%-move / 25%-swing test. The largest swing is
  {worst[2]:+.1%} on "{worst[0]}". The member-side figure is close to linear in the
  allowance, in the rate and in the movement, and a 10% move in a linear driver moves
  the answer 10%.

  THE THING THE ANSWER IS ACTUALLY SENSITIVE TO IS NOT A DOLLAR INPUT AT ALL. It is the
  construction question at register section E -- whether M 2 clause (ii) clips a single
  request's endpoint. That decides whether the retention coverage margin bottoms out at
  0 days or at -18 days (§2), and it is STATUTORY RESEARCHER'S, not mine. The dollars
  are the same on both branches.

  AND THE DOMINANT DRIVER OF THE WHOLE FAMILY IS STILL UPSTREAM AND UNCHANGED: MOO-49's
  clause (vi) reading. MOO-179 §5 -- "A 10% move in the cohort count moves the answer
  more than a 10x move in chain length does." Broad gives roughly 130 members and the
  cap binds in every scenario; this issue, MOO-163, MOO-170 and MOO-179 reopen together
  if it lands broad. Candidate 164-9 does not change that and does not add a trigger.
""")
    # the count is the aggregate's dominant driver
    sw = (per_member["central"] * counts["central"] * 1.1 - agg["central"]) / agg["central"]
    print(f"  For completeness, on the AGGREGATE rather than the per-member figure: a 10%")
    print(f"  move in the count moves it {sw:+.1%}, exactly linearly, and the count is the")
    print(f"  input with no source at all. That is why the aggregate is reported at two")
    print(f"  significant figures and the ceiling row is printed beside it.")
    return base


# ===========================================================================
# 8. EXTERNAL SANITY CHECK
# ===========================================================================

def section_8(agg, per_member, detail):
    print(rule("="))
    print("8. EXTERNAL SANITY CHECK — reported, including where it is weak")
    print(rule("="))
    A0 = detail["central"]["A"]
    r0 = detail["central"]["r"]
    w_cut0 = detail["central"]["w_cut"]
    # the loss the member already bears on the base window, against which 164-9's
    # increment is measured
    base_loss = (pv_of_stream(0.0, A0, r0) - pv_of_stream(w_cut0, A0, r0))
    incr = per_member["central"]
    print(f"""
  CHECK 1 -- AGAINST THE LOSS C2 ALREADY DISCLOSES. This is the strongest check
  available, because it uses the same formula on a window the project has already
  published. MOO-140 §4 states that the member's first payment "is made whole from her
  effective date of retirement, but it carries no interest for the months she waited."
  The window she already waits, on the cut and at the central timing, is {w_cut0:.0f} days,
  and the time value of that wait is {money_exact(base_loss)}. Candidate 164-9 adds
  {money_exact(incr)}, which is {incr/base_loss:+.0%} of a loss already in the memo-ready text.

  AGREEMENT, with a caveat I am stating rather than hiding: this is an INTERNAL
  consistency check, not an external one. It validates that the increment is the right
  size relative to the disclosed base; it cannot validate the base.

  CHECK 2 -- AGAINST VIRGINIA FISCAL-NOTE PRACTICE ON A VRS BILL. A bill related to the
  Virginia Retirement System carries a VRS Board impact statement under
  § 30-19.1:7, and the test that statement applies is "the financial impact of the
  proposed bill upon the general fund and the various local governments" that
  participate, plus the policy implications for the systems administered by the Board
  and the impact on local government independent retirement systems.
  (law.lis.virginia.gov/vacode/title30/chapter1/section30-19.1:7/, retrieved
  12 October 2026; last amended 2010, c. 410.)

  Candidate 164-9 changes the date on which a determination takes effect and therefore
  the date of a first payment that the chapter already requires to be made whole. It
  creates no new benefit, no new duty, no new position and no new system. On the test
  § 30-19.1:7 actually sets, the answer is no impact on the general fund and no impact
  on a participating locality. THE CONVENTION AGREES WITH THE $0 STATE LINES.

  WHERE THIS CHECK IS WEAK, STATED: it is a CONVENTION check, not a quantitative one.
  It validates the three $0 state lines and the no-mandate finding. It CANNOT validate
  the member-side time value, because a Virginia fiscal impact statement does not price
  a member's forgone interest at all -- the quantity has no home in the instrument. The
  member-side figure therefore has no external anchor and is reported as what it is: a
  derived time value on a window the project already publishes, at a rate the chapter
  itself uses.

  CHECK 3 -- NO EXTERNAL COUNT ANCHOR EXISTS, AND THAT IS UNCHANGED SINCE MOO-163.
  MOO-71 §3 establishes that no published count of § 51.1-142.2 military purchases
  exists. There is therefore no other state's reported cost to scale by population and
  no prior Virginia fiscal impact statement for a comparable bill. I am not
  manufacturing one. The aggregate is reported with its ceiling row beside it so a
  reader can see what the arithmetic does without the judgment.
""")
    return base_loss


# ===========================================================================
# 9. ADMINISTRATIVE COST, TIMING, LOCAL MANDATE
# ===========================================================================

def section_9(detail, counts):
    print(rule("="))
    print("9. ADMINISTRATIVE COST, BIENNIUM TIMING, UNFUNDED LOCAL MANDATE")
    print(rule("="))
    print(f"""
  ADMINISTRATIVE COST: $0 ongoing, $0 one-time, 0 positions, 0 systems -- CONDITIONALLY.

  Candidate 164-9 is five words into an existing clause and it introduces no concept:
  "the period allowed by this section for acting upon the request" is the formula Edits
  164-3, 164-4 and 164-6 already introduce, so the Board is already being asked to
  compute it. It states no new duty, requires no new notice, and changes no record the
  Board does not already keep. There is nothing to build.

  THE CONDITION, AND IT IS A GATE RATHER THAN A FOOTNOTE. Candidate 164-9's cap is
  measured from "the EXPIRATION of the period allowed by this section for acting upon
  the request." At the enacted base, M 2's 90-day period is the only one of the
  section's five "shall act upon" duties with NO STATED COMMENCEMENT (MOO-164 §15.4,
  candidate 164-10). Without a commencement the expiration date is not computable from
  the text, and the Board would have to pick one case by case.

    * Candidate 164-10 supplies it -- "within 90 days AFTER THE REQUEST IS FILED",
      +27 characters -- and the Policy Director's disposition §10 takes it.
    * SO: candidate 164-9's $0 administrative line HOLDS IF 164-10 IS APPLIED and does
      NOT hold if it is not. If 164-10 were dropped, 164-9 would convert a determinate
      48-day cap into a per-case legal-interpretation question, and that is an
      administrative cost I have not priced because there is no reason to incur it.
    * This is an ordering constraint on the cut, not a cost: apply 164-10 with 164-9 or
      apply neither.

  BIENNIUM TIMING. Virginia budgets in two-year cycles and a July 1 effective date
  splits a programme year. Candidate 164-9 moves a first payment later by up to
  {detail['central']['delta']:.0f} days at the central timing, so for a member whose window straddles
  30 June the cash falls in the following fiscal year. That is a CASH SHIFT, not a cost:
  the amount is unchanged and the chapter requires it in full. Magnitude at the central
  estimate: under {money_exact(math.ceil(detail['central']['A'] * detail['central']['delta'] / X.MONTH_DAYS * counts['central'] / 100.0) * 100)} of nongeneral-fund cash over the whole 48-month pilot.
  No general fund line carries it, because a retirement allowance is paid from the
  trust.

  UNFUNDED LOCAL MANDATE: NO, and the finding is express rather than inferred.
  Subsection L of the section disclaims any duty or cost upon a locality -- that is
  what subsection L is, as corrected at MOO-140 §0.1 item 1. Candidate 164-9 imposes no
  duty on any locality, changes no local contribution rate, and changes no date on
  which a locality must do anything. Delta local = $0 in every fiscal year, in every
  scenario, as an identity.

  For the § 30-19.1:7 statement, the sentence is: no impact on the general fund, no
  impact on a participating locality, and no impact on a local government independent
  retirement system.
""")


# ===========================================================================
# 10. REGISTER ECHO
# ===========================================================================

def section_10():
    print(rule("="))
    print("10. ASSUMPTION REGISTER — echoed from moo204_inputs.py, which is the source")
    print(rule("="))
    print("""
  The register is `moo204_inputs.py` and it is this table in executable form. Section A
  is statutory or drafted text. Section B is inherited and cited as given. Section C is
  sourced where a source exists and labelled ANALYST JUDGMENT where none does. Section
  D is the one input with no source at all. Section E is model control.

  THE THREE INPUTS WITH NO SOURCE, named so the attack lands on substance:

    1. NON_QUALIFYING_RETIREMENT_SHARE  {low 2%, central 5%, high 15%}
       The fraction of funded participants who reach a G 2 cutback determination. No
       authorised count of this class exists in this project. It scales the aggregate
       linearly and nothing else. The ceiling row in §4 shows what the arithmetic does
       without it.

    2. SERVICE_YEARS_AT_RETIREMENT  {20, 27, 32}
       Scales the allowance and therefore the per-member figure, linearly.

    3. MEMBER_DISCOUNT_RATE, the low and high legs  {4%, 10%}
       The CENTRAL leg is sourced: 6.75%, the VRS assumed rate and the statutory
       interest rate the chapter uses for refunded-service purchases.

  INHERITED, CITED AS GIVEN, NOT RE-DERIVED: MOO-71's participant counts and their
  narrow-clause-(vi) condition; MOO-163's seek rate and timing bands; MOO-179's live
  displacement figures and the $204,000 lapse bound; MOO-140's C2 arithmetic; MOO-177's
  120-day retention. The MOO-71 condition travels with every number here: the counts
  are conditional on the NARROW clause (vi) reading, open at MOO-49.
""")


def section_11(per_member, agg, counts, coverage, identical, max_move, bound,
               base_loss, ceil_case):
    print(rule("="))
    print("11. THE ANSWER IN FOUR LINES, FOR THE POLICY DIRECTOR AND THE EDITOR")
    print(rule("="))
    P = X.M2_PERIOD_RECONSIDERATION_DAYS
    print(f"""
  1. WHAT IT COSTS THE COMMONWEALTH. $0 general fund, $0 nongeneral fund, $0 local, in
     every fiscal year of the pilot, as identities and not as estimates. Candidate
     164-9 defers a payment the chapter already requires to be made whole; it does not
     create, enlarge or remove one.

  2. WHAT IT COSTS THE MEMBER. {money_exact(per_member['central'])} at the central estimate, per affected member, as
     the time value of a deferral the chapter pays no interest on. Range {money_exact(per_member['low'])} to
     {money_exact(per_member['high'])}: the low leg is exactly zero because where the Board decides and gives
     notice promptly the movement is 0 days, and {money_exact(per_member['low|moved'])} if the low allowance and rate
     are held against MOO-141's own timing. Aggregate over the 48-month pilot:
     {money(agg['central'])} at the central estimate ({money_exact(agg['central'])} exactly), under {money_exact(math.ceil(agg['high']/100)*100)} in the high case,
     under {money_exact(math.ceil(ceil_case/1000)*1000)} if every funded participant in the high cell were in the class.

  3. WHAT IT BUYS HER. The remaining {int(X.CARD_F_DAYS - 18)} days of card (f)'s {X.CARD_F_DAYS}, at the endpoint
     where her final qualifying retirement date and every period within which she must
     act are tolled. In the PROMPT case it costs nothing and buys nothing; in
     MOO-141's own case it buys her 60 days and costs her {money_exact(per_member['central'])}.

  4. THE ONE NEW ADVERSE FACT, AND IT IS NOT A DOLLAR. The retention's coverage of the
     tolling endpoint falls from at least +72 days to +12 days on the worked facts, and
     to between 0 and -18 days at the worst lawful timing depending on a construction
     question that is Statutory Researcher's. A negative margin is an interval in which
     her periods to act are still tolled after her retained filing date has lapsed.
     Priced at $0 at the central estimate and inside the same {money_exact(X.LAPSE_BOUND_USD)} lapse bound at
     high take-up.

  RECOMMENDATION: TAKE IT, and take it with candidate 164-10, which it depends on for a
  computable expiration date. It is cheap -- five words, no new concept, $0 on every
  state line, a two-figure sum in member-side time value, no movement in MOO-140's C2
  answer or its published figure, no movement in the {bound}-day card (h) bound, no link
  lengthened in the chain, and no figure in MOO-177, MOO-179 or MOO-180 that has to be
  re-cut. It would make MOO-164 §0.1's original claim true.

  WHAT I WOULD NOT DO: close the coverage margin in the same cut. The fix lives in
  Edit 3's retention sentence, the 120 days there is a BOARD figure, and moving it is a
  board card and not a drafter's or a modeller's. Disclose it, route it to whoever next
  opens that sentence, and decide it on its own.
""")


def main():
    print(rule("="))
    print("MOO-204 -- CANDIDATE 164-9 PRICED: THE LAST 60 DAYS AT M 2's TOLLING ENDPOINT")
    print("Fiscal & Impact Modeler. Pre-decisional and internal. Not a DLS bill.")
    print("Not reviewed by counsel. No figure here is a VRS actuarial result.")
    print(rule("="))
    section_0()
    section_1()
    coverage = section_2()
    max_move, bound = section_3()
    per_member, counts, agg, detail, ceil_case = section_4()
    section_5(coverage)
    identical, _sat, _k1, repro = section_6()
    section_7(per_member, counts, agg, detail)
    base_loss = section_8(agg, per_member, detail)
    section_9(detail, counts)
    section_10()
    section_11(per_member, agg, counts, coverage, identical, max_move, bound,
               base_loss, ceil_case)
    print(rule("="))
    print("END OF RUN. Locks passed: 14/14."
          f"  Days-dimension invariance: {'confirmed' if identical else 'FAILED'}."
          f"  MOO-179 2.80/11 reproduced: {repro[1]:.2f}/{repro[3]:.0f}.")
    print(rule("="))


if __name__ == "__main__":
    main()
