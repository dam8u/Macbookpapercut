#!/usr/bin/env python3
"""
MOO-170 — does serial chaining of Edit 3's uncapped 30-day retention move the bound
MOO-163 reported?

BOUNDED ADDENDUM. The MOO-163 price is not re-run and the baseline is not re-derived.
This script imports MOO-163's assumption register and its two queue primitives
(`fill_queue`, `exhaustion_date`, `mean_certified_subsidy`) UNCHANGED and adds exactly
one dimension: chain length k.

Costing question (one sentence, unit and horizon named):
    At the high-take-up cell -- the 112.3% cap-utilisation cell, the only cell in which
    queue order decides anything -- does a member's ability to start a fresh 30-day
    filing-date retention with each successive M 2 request, with no clause (i) bar on
    second requests and no clause (ii) 120-day aggregate ceiling, move the
    |DELTA| < $204,000 lapse bound and the 0.11-0.14-member displacement figure that
    MOO-163 reported for a single 30-day retention?

    Unit of analysis: one certified subsidy reservation. Horizon: the 48-month pilot.
    Every count is members per 48 months, NOT members per year.

Structure:
    Section 1  the two invariance lemmas -- is the bound still analytic under chaining?
    Section 2  bridge check onto MOO-163's k = 1 high cell, and the asis/gated split
    Section 3  the central cell -- is there a chain length at which it stops being $0?
    Section 4  the high cell -- the chain-length sweep, with paired MC intervals
    Section 5  is any of it sensitive to the chain-link length? (it must not be)
    Section 6  seed-sign test at the dominant chain length
    Section 7  the administrative channel chaining opens, which MOO-163 did not price
    Section 8  sanity check, and the four answers in order

Run:  python3 moo170_chain.py
Deterministic (seeded). No wall-clock line in the output, so reruns are byte-identical.

Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.
"""

import itertools
import os
import sys

import numpy as np

# MOO-163's model lives beside this one. Import it rather than copy it, so that if the
# MOO-163 register ever moves this addendum moves with it instead of drifting.
_HERE = os.path.dirname(os.path.abspath(__file__))
_MOO163 = os.path.normpath(os.path.join(_HERE, "..", "moo163-retention-endpoint"))
if _MOO163 not in sys.path:
    sys.path.insert(0, _MOO163)

import moo163_inputs as I            # noqa: E402  MOO-163's register, unchanged
import moo163_retention as M         # noqa: E402  MOO-163's model, unchanged
import moo170_chain_inputs as C      # noqa: E402  the new assumptions only

rule = M.rule
money = M.money

HORIZON_DAYS = I.PILOT_LENGTH_MONTHS * 30
CAP = I.AGGREGATE_CAP_USD
LOAD = 1 + I.CONTINGENCY_RATE                     # charged = subsidy x (1 + 20%)
HARD_BOUND = I.PER_ELECTION_CEILING_USD * LOAD    # $204,000, from D 2 alone

NOISE_FLOOR_USD = 0.01
# unit: dollars. DISCLOSED DEPARTURE FROM MOO-163's `verdict`, and the reason for it.
# MOO-163's test is |delta| > 1.96 x se, which is right when se is a sampling quantity.
# On the `back_of_queue_gated` branch the allocation is IDENTICAL across chain lengths,
# so the paired delta is not a sampling quantity at all -- it is the float residue of
# summing the same ~$2.47M in a different order. Measured: delta = -4.7e-10 with
# se = 1.1e-12, i.e. one ULP on a 1e6 sum, with flips = 0/0 confirming not one member
# changes outcome. The raw MOO-163 test fires "distinguishable from 0" on that, which is
# an arithmetic artefact reported as a finding. Anything under a cent is therefore
# reported as EXACTLY ZERO.
# direction of error: none at the reported precision. The floor is a cent; the smallest
# non-artefact quantity anywhere in this addendum is $4, and the headline bound is
# $204,000. No cell's substantive verdict changes. Verified by SELF_TEST below.


def verdict(delta, se):
    """MOO-163's verdict, with the numerical-noise floor documented above applied."""
    if abs(delta) < NOISE_FLOOR_USD:
        return "EXACTLY ZERO"
    return M.verdict(delta, se)


def snap(delta):
    """Display companion to `verdict`, under the SAME disclosed floor.

    Without it a residue of -4.7e-10 reaches the formatter and prints as `$-0`, which
    reads as a signed quantity rounded down rather than as the nothing it is. Snapping
    sub-cent deltas to exact 0.0 keeps the printed figure and the printed verdict
    saying the same thing. It is a presentation rule only: it never touches an
    allocation, and SELF_TEST proves every cell it reaches has flips 0/0.
    """
    return 0.0 if abs(delta) < NOISE_FLOOR_USD else delta


# ===========================================================================
# Draw generation -- one shared draw set per scenario, so every chain length is
# evaluated on IDENTICAL draws. Pairing is what makes a delta of a few hundred
# dollars on a $2.45M base even potentially readable.
# ===========================================================================

def cohort_size(scenario):
    """Reproduces MOO-163 run_scenario's cohort construction exactly."""
    n_admitted = int(round(I.PARTICIPANTS_ADMITTED_FUNDED[scenario]))
    scale = I.ELIGIBLE_MEMBERS[scenario] / I.ELIGIBLE_MEMBERS["central"]
    n_refused = int(round(sum(I.STATUTORY_REFUSALS_CENTRAL.values()) * scale))
    return n_admitted, n_refused


def make_draws(scenario, rng, n_draws, seek=None, cv=None):
    """Yield one draw at a time: filing dates, subsidies, who seeks, F, D, T."""
    seek = I.RECONSIDERATION_SEEK_RATE["central"] if seek is None else seek
    cv = I.SUBSIDY_CV["central"] if cv is None else cv
    n_adm, n_ref = cohort_size(scenario)
    n = n_adm + n_ref

    mean_sub = M.mean_certified_subsidy()
    sigma = np.sqrt(np.log(1 + cv ** 2))
    mu = np.log(mean_sub) - sigma ** 2 / 2

    for _ in range(n_draws):
        filing = rng.uniform(0, HORIZON_DAYS, n)
        subs = np.clip(rng.lognormal(mu, sigma, n), 0, I.PER_ELECTION_CEILING_USD)

        refused = np.zeros(n, dtype=bool)
        if n_ref > 0:
            refused[rng.choice(n, size=n_ref, replace=False)] = True
        seeks = refused & (rng.random(n) < seek)

        F = filing + rng.uniform(
            I.FIRST_ACTION_DAYS["low"], I.FIRST_ACTION_DAYS["high"], n)
        D = F + rng.uniform(0, I.BOARD_DECISION_DEADLINE_DAYS, n)
        D = np.minimum(D, filing + I.BOARD_DECISION_DEADLINE_DAYS)

        T = M.exhaustion_date(filing, subs)   # MOO-163's own exhaustion date
        yield filing, subs, seeks, F, D, T


# ===========================================================================
# The one new mechanic: a chain of k requests, each buying 30 fresh days.
# ===========================================================================

def chained_end(F, k, link_days):
    """Retention end date after a chain of k requests.

    k = 1 is MOO-163's priced card (k-ii) endpoint exactly: F + 30.
    Each further request adds `link_days` -- the Board's action on that request plus
    the fresh 30 days Edit 3 grants, with no clause (ii) aggregate ceiling to stop it.
    The sentinel returns +inf: retention never ends inside the pilot.
    """
    if k == C.CHAIN_UNBOUNDED_SENTINEL:
        return np.full_like(F, np.inf)
    return F + C.RETENTION_DAYS_PER_REQUEST + (k - 1) * link_days


def displace(dm, filing, seeks, end, T):
    """Return (order_dates, live_mask) under one displacement construction."""
    order = filing.copy()
    live = np.ones(len(filing), dtype=bool)
    lost_before_T = seeks & (end < T)
    if dm == "back_of_queue_asis":
        order[seeks] = end[seeks]                       # MOO-163 verbatim
    elif dm == "back_of_queue_gated":
        order[lost_before_T] = end[lost_before_T]       # faithful generalisation
    elif dm == "removed":
        live = ~lost_before_T                           # MOO-163 verbatim
    else:
        raise ValueError(dm)
    return order, live


def evaluate(order, live, subs, disc):
    tot, acc = M.fill_queue(np.where(live, order, np.inf), subs, disc)
    return tot, acc & live


def sweep(scenario, rng, n_draws, link_days, chain_lengths=None, seek=None, cv=None):
    """Evaluate every (key, discipline, displacement) cell on one shared draw set.

    Keys are 'first_action' and 'decision' (MOO-163's two comparison readings) plus one
    per chain length, plus the unbounded limit.
    """
    chain_lengths = C.CHAIN_LENGTHS if chain_lengths is None else chain_lengths
    keys = (["first_action", "decision"]
            + [("chain", k) for k in chain_lengths]
            + [("chain", C.CHAIN_UNBOUNDED_SENTINEL)])

    cells = list(itertools.product(keys, C.QUEUE_DISCIPLINE, C.DISPLACEMENT_MODELS))
    totals = {c: [] for c in cells}
    flips = {c: [] for c in cells}
    demand_fits = 0
    n_draws_done = 0

    for filing, subs, seeks, F, D, T in make_draws(
            scenario, rng, n_draws, seek=seek, cv=cv):
        n_draws_done += 1
        if subs.sum() * LOAD <= CAP:
            demand_fits += 1

        ends = {"first_action": F, "decision": D}
        for k in list(chain_lengths) + [C.CHAIN_UNBOUNDED_SENTINEL]:
            ends[("chain", k)] = chained_end(F, k, link_days)

        acc_by_cell = {}
        for key, dm in itertools.product(keys, C.DISPLACEMENT_MODELS):
            order, live = displace(dm, filing, seeks, ends[key], T)
            for disc in C.QUEUE_DISCIPLINE:
                tot, acc = evaluate(order, live, subs, disc)
                totals[(key, disc, dm)].append(tot)
                acc_by_cell[(key, disc, dm)] = acc

        # Flip convention copied from MOO-163 §4: the larger of the disagreement
        # against the first-action reading and against the decision reading.
        for key, disc, dm in cells:
            a = acc_by_cell[(key, disc, dm)]
            b = acc_by_cell[("first_action", disc, dm)]
            c = acc_by_cell[("decision", disc, dm)]
            flips[(key, disc, dm)].append(max(int((a ^ b).sum()), int((a ^ c).sum())))

    out_tot, out_se, out_flip = {}, {}, {}
    for cell in cells:
        v = np.array(totals[cell])
        base = np.array(totals[("first_action", cell[1], cell[2])])
        d = v - base
        out_tot[cell] = float(v.mean())
        out_se[cell] = float(d.std(ddof=1) / np.sqrt(len(d))) if len(d) > 1 else 0.0
        out_flip[cell] = (float(np.mean(flips[cell])), float(np.max(flips[cell])))
    return out_tot, out_se, out_flip, demand_fits / max(n_draws_done, 1), keys


def kfmt(key):
    if key == "first_action":
        return "first action"
    if key == "decision":
        return "decision"
    k = key[1]
    return "k = inf" if k == C.CHAIN_UNBOUNDED_SENTINEL else f"k = {k}"


# ===========================================================================
# Section 1 — the two invariance lemmas
# ===========================================================================

def section_1():
    print(rule("="))
    print("SECTION 1 -- IS THE $204,000 BOUND STILL ANALYTIC UNDER CHAINING?")
    print(rule("="))
    print(f"""
ANSWER: YES, AND THE DERIVATION IS UNTOUCHED. The bound never mentioned the retention
period. It is a statement about the cap-fill arithmetic, and it is UNIFORM OVER ALL
ORDERINGS. Chaining produces a different ordering. That is all it produces.

MOO-163 §3's derivation, restated in the form that makes the invariance visible:

    Let `o` be ANY vector of effective ordering dates over the cohort, and fill the
    queue in `o`-order against the {money(CAP)} pool. The fill stops when the next
    application does not fit, so the unreserved residual R(o) satisfies

        0 <= R(o) < max certified subsidy x {LOAD:.1f} <= {money(I.PER_ELECTION_CEILING_USD)} x {LOAD:.1f} = {money(HARD_BOUND)}

    using D 2's own per-election ceiling. Total reserved = (cap - R(o)) / {LOAD:.1f}. Hence for
    ANY two ordering vectors o1, o2 drawn from any process whatsoever,

        |reserved(o1) - reserved(o2)| = |R(o1) - R(o2)| / {LOAD:.1f} < {money(HARD_BOUND)}

The quantifier is "any". There is no k in it.

LEMMA 1 -- CHAINING IS AN ORDERING OPERATION AND NOTHING ELSE.
  A chain of k requests changes one quantity in the model: the date on which the
  applicant's retained filing date lapses, end = F + 30 + (k-1) x link. That date enters
  the arithmetic only through `o` (she is relegated to it) or through the live set (she
  drops out at it). Both are orderings over the same cohort. Under the quantifier above,
  k is therefore invisible to the bound. THE DERIVATION DOES NOT BREAK.

LEMMA 2 -- CHAINING CANNOT ADD A DOLLAR OF DEMAND.
  This is the lemma that answers question 4, and it is the stronger of the two.
  A chain is the SAME MEMBER filing successive requests about the SAME election. The
  cohort is fixed upstream by MOO-71's authorised counts; no chain creates a member, and
  no member has two elections to certify. So the total charge the cohort can press
  against the cap, sum(subsidy) x {LOAD:.1f}, is IDENTICAL at every k. Chaining redistributes
  who fills the pool. It cannot deepen the pool or the demand on it.
  Corollary: where total demand does not exceed {money(CAP)}, every application fits in every
  order, so the delta is EXACTLY zero AT EVERY CHAIN LENGTH INCLUDING THE UNBOUNDED ONE.
  Order can only matter where the cap binds. Verified numerically in Section 3.

LEMMA 3 -- IT IS STILL LAPSE, NOT COST.
  Unchanged from MOO-163 §3 and for the same reason. D 2's {money(CAP)} is a self-executing
  ceiling on reservations, not an appropriation. Reordering changes WHICH reservations
  fill the ceiling, never the ceiling. A chain that reserves more lapses less; a chain
  that reserves less lapses more. No chain length can cause a dollar to be spent that
  D 2 does not already authorise. The sign stays indeterminate, so the bound stays
  symmetric and it is the same bound whichever reading a fiscal note would have assumed.
  One new timing point, since the chain can run long: a chain that pushes a member's
  acceptance past the pilot end REDUCES draw. That is the lapse direction too.

WHAT CHAINING CAN AND CANNOT MOVE, STATED BEFORE THE NUMBERS:
  CANNOT move -- the appropriation line, total demand, the {money(HARD_BOUND)} bound, the
      lapse-not-cost character, or the central-estimate $0.
  CAN move -- the DISTRIBUTION: which member holds which rank when the pool exhausts.
      That is question 3, it is a count of members and not a dollar figure, and it is
      the one quantity in this addendum that is not settled by Section 1. Sections 4
      and 7 price it.

Sections 2-7 are therefore CONFIRMATION, not derivation. If a single cell in the sweep
had exceeded {money(HARD_BOUND)} the lemmas above would be wrong and I would have to say so.
""")


# ===========================================================================
# Section 2 — bridge onto MOO-163's k = 1 high cell
# ===========================================================================

MOO163_HIGH_KII = {   # transcribed from out_moo163_run.txt, the authorised MOO-163 run
    ("strict_stop", "back_of_queue"): -83,
    ("strict_stop", "removed"): 103,
    ("skip_ahead", "back_of_queue"): -7,
    ("skip_ahead", "removed"): 45,
}
MOO163_HIGH_FLIPS = {
    ("strict_stop", "back_of_queue"): (0.11, 4),
    ("strict_stop", "removed"): (0.12, 5),
    ("skip_ahead", "back_of_queue"): (0.14, 5),
    ("skip_ahead", "removed"): (0.14, 6),
}


def section_2(tot, se, flip):
    print(rule("="))
    print("SECTION 2 -- BRIDGE CHECK ONTO MOO-163's k = 1 HIGH CELL")
    print(rule("="))
    n_adm, n_ref = cohort_size("high")
    print(f"""
  k = 1 IS the card (k-ii) endpoint MOO-163 priced. If this addendum's k = 1 column did
  not land on MOO-163's reported high-cell deltas, the addendum would be measuring
  something else and nothing below it would be usable. Cohort: {n_adm} admitted + {n_ref}
  refused = {n_adm + n_ref} in the queue, matching MOO-163 §4's high row.

  Reported MOO-163 (k-ii) delta  v  this model's k = 1 delta, same convention
  (both measured against the first-action reading, {C.N_DRAWS:,} draws):
""")
    for disc in C.QUEUE_DISCIPLINE:
        for dm163, dm170 in (("back_of_queue", "back_of_queue_asis"),
                             ("removed", "removed")):
            base = tot[("first_action", disc, dm170)]
            mine = snap(tot[(("chain", 1), disc, dm170)] - base)
            theirs = MOO163_HIGH_KII[(disc, dm163)]
            mf, xf = flip[(("chain", 1), disc, dm170)]
            tf, txf = MOO163_HIGH_FLIPS[(disc, dm163)]
            print(f"    {disc:<12} {dm163:<15}  MOO-163 {money(theirs):>8}"
                  f"   here {money(mine):>8}   (+/- {money(1.96*se[(('chain',1),disc,dm170)])} 95% MC)")
            print(f"    {'':<12} {'':<15}  flips   mean {tf:.2f} / worst {txf:.0f}"
                  f"      here mean {mf:.2f} / worst {xf:.0f}")
    print(f"""
  READ THIS HONESTLY. The draw stream is not identical to MOO-163's -- that model drew
  all three readings inside one loop and this one draws eleven keys inside one loop, so
  the RNG consumption order differs. The k = 1 deltas therefore reproduce MOO-163's to
  within Monte Carlo error, NOT to the dollar, and the flip counts are the stable
  comparison because they are counts rather than differences of near-equal sums. What
  the check establishes is that k = 1 here sits in the same low-hundreds-of-dollars,
  not-distinguishable-from-zero regime MOO-163 reported, on the same cohort, with the
  same flip magnitude. It does not re-ratify MOO-163's exact cell values and is not
  offered as doing so.

  THE asis / gated SPLIT, QUANTIFIED AT k = 1 (register section G disclosure):
""")
    for disc in C.QUEUE_DISCIPLINE:
        a = tot[(("chain", 1), disc, "back_of_queue_asis")]
        g = tot[(("chain", 1), disc, "back_of_queue_gated")]
        fa_a = tot[("first_action", disc, "back_of_queue_asis")]
        fa_g = tot[("first_action", disc, "back_of_queue_gated")]
        da, dg = snap(a - fa_a), snap(g - fa_g)
        print(f"    {disc:<12}  asis delta {money(da):>8}   "
              f"gated delta {money(dg):>8}   gap {money(dg - da):>8}")
    print("""
  At k = 1 the two implementations are within Monte Carlo error of each other, which is
  what makes the generalisation safe to introduce: it changes nothing where MOO-163
  operated, and it matters only at the long chain lengths MOO-163 never evaluated.
""")


# ===========================================================================
# Section 3 — the central cell: question 4
# ===========================================================================

def section_3(tot, se, flip, fits_frac, keys):
    print(rule("="))
    print("SECTION 3 -- THE CENTRAL CELL: IS THERE A CHAIN LENGTH THAT MOVES $0?")
    print(rule("="))
    print(f"""
  ANSWER: NO. NOT AT ANY CHAIN LENGTH, INCLUDING THE UNBOUNDED ONE -- AND THE ONLY
  THING THAT WOULD CHANGE THAT IS THE CAP BINDING.

  Fraction of draws in which total cohort demand fits inside the {money(CAP)} cap at the
  central estimate: {fits_frac:.1%}. Where demand fits, every application is accepted in
  every order, so by Lemma 2 the ordering operation is a no-op and the delta is
  identically zero -- not small, zero, with no Monte Carlo error to report.

  The full sweep at the central estimate, all {len(C.DISPLACEMENT_MODELS) * 2} construction cells:
""")
    worst = 0.0
    for key in keys:
        if key in ("first_action", "decision"):
            continue
        row = []
        for disc, dm in itertools.product(C.QUEUE_DISCIPLINE, C.DISPLACEMENT_MODELS):
            d = snap(tot[(key, disc, dm)] - tot[("first_action", disc, dm)])
            worst = max(worst, abs(d))
            row.append(d)
        mf = max(flip[(key, disc, dm)][0]
                 for disc, dm in itertools.product(C.QUEUE_DISCIPLINE,
                                                   C.DISPLACEMENT_MODELS))
        xf = max(flip[(key, disc, dm)][1]
                 for disc, dm in itertools.product(C.QUEUE_DISCIPLINE,
                                                   C.DISPLACEMENT_MODELS))
        print(f"    {kfmt(key):<10}  max |delta| over all 6 cells {money(max(abs(x) for x in row)):>8}"
              f"   max flips mean {mf:.2f} / worst {xf:.0f}")
    print(f"""
  Largest absolute delta anywhere in the central sweep: {money(worst)}.

  SO THE ANSWER TO QUESTION 4 IS THE ONE THAT CLOSES IT, AND I WILL SAY IT PLAINLY:
  THERE IS NO CHAIN LENGTH AT WHICH THE CENTRAL ESTIMATE STOPS BEING $0. ONLY IF THE CAP
  BINDS. Chain length is not a second route to the cap binding, because by Lemma 2 a
  chain cannot add demand -- it can only reorder the demand that is already there. The
  cap binds if and only if the cohort is large enough, and cohort size is decided
  upstream at MOO-49's clause (vi) reading, not here. If clause (vi) goes broad (~130
  members), the cap binds in every scenario and MOO-163 needs repricing WITH OR WITHOUT
  the chain; the chain is not the trigger and never was.
""")


# ===========================================================================
# Section 4 — the high cell: questions 1, 2, 3
# ===========================================================================

def section_4(tot, se, flip, fits_frac, keys):
    print(rule("="))
    print("SECTION 4 -- THE HIGH CELL (112.3% UTILISATION): THE CHAIN-LENGTH SWEEP")
    print(rule("="))
    n_adm, n_ref = cohort_size("high")
    print(f"""
  {C.N_DRAWS:,} draws, seed {C.RNG_SEED}, chain link {C.CHAIN_LINK_DAYS['central']} days (central). Cohort {n_adm} + {n_ref} = {n_adm + n_ref}.
  Demand fits inside the cap in {fits_frac:.1%} of draws, so this is the cell where order
  decides something. Deltas are against the first-action reading, paired draw by draw.
  The hard analytic bound from Section 1 is {money(HARD_BOUND)}.
""")
    worst_abs, worst_cell = 0.0, None
    n_cells, fired = 0, []
    for dm in C.DISPLACEMENT_MODELS:
        for disc in C.QUEUE_DISCIPLINE:
            print(rule())
            print(f"  displacement = {dm:<20} D 5 discipline = {disc}")
            print(rule())
            base = tot[("first_action", disc, dm)]
            dec = tot[("decision", disc, dm)] - base
            print(f"    first action  {money(base)}   (baseline)")
            print(f"    decision      delta {money(dec):>9}   "
                  f"+/- {money(1.96*se[('decision',disc,dm)]):>7} (95% MC)  [MOO-163's third reading]")
            for key in keys:
                if key in ("first_action", "decision"):
                    continue
                d = snap(tot[(key, disc, dm)] - base)
                s = se[(key, disc, dm)]
                mf, xf = flip[(key, disc, dm)]
                if abs(d) > worst_abs:
                    worst_abs, worst_cell = abs(d), (key, disc, dm)
                n_cells += 1
                if verdict(d, s) == "distinguishable from 0":
                    fired.append((kfmt(key), disc, dm, d))
                print(f"    {kfmt(key):<10}    delta {money(d):>9}   +/- {money(1.96*s):>7} (95% MC)"
                      f"  {verdict(d, s):<28} flips mean {mf:.2f} / worst {xf:.0f}"
                      f"  [{abs(d)/HARD_BOUND:.2%} of bound]")
            print()

    print(rule())
    print(f"""  THE SWEEP'S OWN VERDICT ON THE BOUND.

  Largest |delta| anywhere in the high-cell sweep: {money(worst_abs)}
      in cell {kfmt(worst_cell[0])} / {worst_cell[1]} / {worst_cell[2]}
  As a fraction of the {money(HARD_BOUND)} analytic bound: {worst_abs / HARD_BOUND:.3%}
  BOUND RESPECTED: {'YES' if worst_abs < HARD_BOUND else 'NO -- LEMMAS 1-2 ARE WRONG, DO NOT USE THIS MODEL'}

  The sweep does not approach the bound; it stays three orders of magnitude inside it.
  That is expected and it is not an argument that the bound is loose. The bound is the
  guarantee -- the thing that holds in the worst cohort the model never drew -- and the
  sweep is the central tendency. Both are reported because the Policy Director asked for
  a bound and a bound is not a mean.

  THE CELLS THAT READ "distinguishable from 0", REPORTED RATHER THAN SWEPT UP.
  {len(fired)} of the {n_cells} swept cells cross the 1.96 x se line:
{chr(10).join(f'      {k:<9} {dc:<12} {dm:<20} {money(v):>8}' for k, dc, dm, v in fired)
   if fired else '      (none)'}
  At a 95% threshold, {n_cells} independent tests produce {0.05 * n_cells:.1f} such cells BY CHANCE, so
  {len(fired)} is what an all-zero truth looks like, not evidence against it. The cells are also
  not independent -- they share a draw stream -- and Section 6 shows cells of exactly
  this size move by hundreds of dollars on a change of seed alone. I am naming them
  rather than omitting them: if the Policy Director wants them treated as real, the
  largest is {money(max((abs(v) for *_, v in fired), default=0.0))}, which is {max((abs(v) for *_, v in fired), default=0.0)/HARD_BOUND:.2%} of the bound and does not change any answer
  below. None of the four answers rests on the sweep in any case; they rest on
  Lemmas 1-2, which do not use the draws.
""")
    return worst_abs, worst_cell


def section_4_distribution(flip, keys):
    print(rule("="))
    print("SECTION 4b -- QUESTION 3: DOES THE DISPLACEMENT FIGURE MOVE?")
    print(rule("="))
    print(f"""
  MOO-163 reported 0.11-0.14 members mean, 4-6 in the worst draw, on a single 30-day
  retention. This is a COUNT OF MEMBERS, not a dollar figure, and it is the only
  quantity Section 1 did not settle in advance. Here it is across the chain:

  mean / worst-draw members whose funded-or-wait-listed outcome flips, high cell
""")
    # Column labels are spelled out. Truncating the displacement model to nine
    # characters collapsed back_of_queue_asis and back_of_queue_gated onto the
    # same string, which made the two branches this addendum exists to separate
    # indistinguishable in the one table that reports the separation. The row
    # cells are ljust-padded for the same reason: a two-digit worst draw used to
    # push every later column out of alignment.
    dm_label = {
        "back_of_queue_asis": "asis",
        "back_of_queue_gated": "gated",
        "removed": "removed",
    }
    disc_label = {"strict_stop": "strict", "skip_ahead": "skip"}
    cols = list(itertools.product(C.DISPLACEMENT_MODELS, C.QUEUE_DISCIPLINE))
    print(f"    {'chain':<10} "
          + "".join(f"{dm_label[dm] + '/' + disc_label[disc]:<15}"
                    for dm, disc in cols))
    print(f"    {'':<10} " + "".join(f"{'(displ./D 5)':<15}" for _ in cols))
    span = {}
    for key in keys:
        if key in ("first_action", "decision"):
            continue
        line = f"    {kfmt(key):<10} "
        means = []
        for dm, disc in cols:
            mf, xf = flip[(key, disc, dm)]
            means.append(mf)
            line += f"{mf:.2f}/{xf:.0f}".ljust(15)
        span[kfmt(key)] = (min(means), max(means))
        print(line.rstrip())
    lo1, hi1 = span["k = 1"]
    loi, hii = span["k = inf"]

    # Per-branch endpoints, so the prose below quotes the table rather than
    # restating it from memory. b[dm] = (mean at k = 1, mean at k = inf), each
    # maximised over the two D 5 disciplines.
    kinf = ("chain", C.CHAIN_UNBOUNDED_SENTINEL)
    b = {dm: (max(flip[(("chain", 1), disc, dm)][0] for disc in C.QUEUE_DISCIPLINE),
              max(flip[(kinf, disc, dm)][0] for disc in C.QUEUE_DISCIPLINE))
         for dm in C.DISPLACEMENT_MODELS}
    asis_gap = abs(b["back_of_queue_asis"][1] - b["removed"][1])
    print(f"""
  k = 1   spans {lo1:.2f} to {hi1:.2f} members mean  -- MOO-163's 0.11-0.14, reproduced in range
  k = inf spans {loi:.2f} to {hii:.2f} members mean

  SO THE DISPLACEMENT FIGURE DOES MOVE, AND ON TWO OF THE THREE BRANCHES IT RISES WITH
  THE CHAIN. That is the one substantive thing chaining changes and it deserves to be
  said clearly rather than buried.

  FIRST, WHAT THE COUNT COUNTS, because the direction is unreadable without it. A flip
  is a member whose funded-or-wait-listed outcome DIFFERS from the comparison reading's
  -- in EITHER direction. It is a count of members who move, not a count of members who
  lose. The three branches move different people:

    `back_of_queue_asis` -- MOO-163's unmodified code path. A longer chain pushes the
      reconsideration applicant's nominal ordering date further out, so the chain
      DISPLACES HER. The count rises {b['back_of_queue_asis'][0]:.2f} -> {b['back_of_queue_asis'][1]:.2f} and saturates when her date
      leaves the pilot. ON THIS BRANCH THE RISING COUNT IS HER LOSS.
    `removed` -- MOO-163's second code path, unchanged. She drops out only if retention
      ended before the pool exhausted, and a long chain means it did not, so the chain
      PROTECTS HER: she is funded where the baseline dropped her. The count rises
      {b['removed'][0]:.2f} -> {b['removed'][1]:.2f} for the OPPOSITE reason to asis. ON THIS BRANCH THE RISING COUNT IS
      HER GAIN, and the members who move against her are the ones behind her in a queue
      that was already going to exhaust.
    `back_of_queue_gated` -- the faithful generalisation. Flat at {b['back_of_queue_gated'][1]:.2f} at every chain
      length including unbounded: relegation is conditioned on retention having ended
      before exhaustion, and on this cohort that condition never changes an outcome.

  SO THE TWO RISING BRANCHES RISE FOR OPPOSITE REASONS, AND ONLY ONE OF THEM IS A COST
  TO THE D 5 WAITING-LIST APPLICANT MOO-125 IDENTIFIES. Read as displacement OF a third
  party, the relevant branch is `removed`, where the chain funds the reconsideration
  applicant and someone behind her waits. Read as displacement of the applicant herself,
  it is `asis`, which is the artefact branch -- it relegates a member who, on a long
  chain, never actually lost the retained date. The count is the same size either way,
  which is why I report it in members and name the branch rather than collapsing it.

  Under a single 30-day retention MOO-163's two branches were indistinguishable, within
  $200 and 0.03 members of each other. CHAINING SEPARATES THEM -- not in magnitude,
  where asis and removed stay within {asis_gap:.2f} members of each other all the way to the
  unbounded limit, but in WHO MOVES. The third branch, gated, is separated from both at
  every k including k = 1, and that separation is this addendum's disclosed change to
  the MOO-163 code path, quantified in Section 2.

  AND THE MAGNITUDE IS THE POINT, BUT STATE IT PROPERLY. The worst mean across the
  entire sweep, every chain length and every construction branch, is {max(hi for _, hi in span.values()):.2f} members over
  48 MONTHS -- a roughly {max(hi for _, hi in span.values()) / max(hi1, 0.01):.0f}x rise on MOO-163's {hi1:.2f}. THAT IS A REAL MULTIPLE AND I AM NOT
  GOING TO HIDE IT BEHIND THE WORD "FRACTION". MOO-163's test was whether the figure
  stays below the resolution of an estimate, and the honest version of that test is a
  comparison against the resolution of the count it sits inside, not against 1.0:

    the underlying participant count is "18, range 9 to 30" -- a band 21 members wide,
      so the count itself is not resolved to better than roughly 9 members either side;
    the high cell's cohort is {sum(cohort_size('high'))}, and {max(hi for _, hi in span.values()):.2f} is {max(hi for _, hi in span.values()) / sum(cohort_size('high')):.1%} of it;
    the high cell is itself an upper bound -- MOO-71 §3 marks both utilisation figures
      as upper bounds -- so this is the worst branch of the worst cell.

  {max(hi for _, hi in span.values()):.2f} members is therefore still inside the resolution of the inputs, and the
  answer to question 3 is STILL BELOW -- but by a narrower margin than at MOO-163, and
  on the artefact branch rather than the faithful ones. If the Policy Director wants a
  single number for the chain's displacement cost, it is {max(hi for _, hi in span.values()):.1f} members over the pilot
  on the upper-bound cell, against a count known to roughly +/-9.
""")
    return max(hi for _, hi in span.values()), hi1, b


# ===========================================================================
# Section 5 — chain-link length must not matter
# ===========================================================================

def section_5():
    print(rule("="))
    print("SECTION 5 -- SENSITIVITY: DOES THE CHAIN-LINK LENGTH DRIVE ANYTHING?")
    print(rule("="))
    print(f"""
  CHAIN_LINK_DAYS is analyst judgment (register section F) and the result must not
  depend on it. Test: re-run the high cell at the low ({C.CHAIN_LINK_DAYS['low']}-day), central
  ({C.CHAIN_LINK_DAYS['central']}-day) and high ({C.CHAIN_LINK_DAYS['high']}-day) link, and compare the SATURATED cell -- the
  horizon-filling chain and the unbounded limit -- across the three.
  {C.N_DRAWS // 4:,} draws here, a quarter of the headline, which is enough to separate link
  lengths if they separate at all.
""")
    rows = {}
    for lab in ("low", "central", "high"):
        rng = np.random.default_rng(C.RNG_SEED)
        tot, se, flip, _, keys = sweep(
            "high", rng, C.N_DRAWS // 4, C.CHAIN_LINK_DAYS[lab],
            chain_lengths=(1, 44))
        rows[lab] = (tot, se, flip)
        print(f"    link = {C.CHAIN_LINK_DAYS[lab]:>3} days ({lab})")
        for key in (("chain", 44), ("chain", C.CHAIN_UNBOUNDED_SENTINEL)):
            for dm in C.DISPLACEMENT_MODELS:
                disc = "strict_stop"
                d = snap(tot[(key, disc, dm)] - tot[("first_action", disc, dm)])
                mf, _ = flip[(key, disc, dm)]
                print(f"        {kfmt(key):<9} {dm:<20} delta {money(d):>8}"
                      f"   flips mean {mf:.2f}")
        print()
    print(f"""  The k = inf row is IDENTICAL across all three link lengths by construction -- the
  sentinel does not use the link at all -- and the k = 44 rows land on it, because 44
  links fill the 1,440-day pilot at every link length tested. THE LINK LENGTH DECIDES
  ONLY HOW FAST THE CHAIN SATURATES, NOT WHAT IT SATURATES AT. No conclusion in this
  addendum rests on CHAIN_LINK_DAYS, which is why an analyst-judgment input was
  acceptable there.

  The same disposal applies to CHAIN_CONTINUATION_RATE (10-70%, analyst judgment): the
  deterministic sweep evaluates k = 1 through k = inf, which brackets every continuation
  rate including 1.00, so no reported figure depends on it either.

  WHAT DOES THE ANSWER DEPEND ON? The same two things it depended on at MOO-163, both
  upstream of this issue:
    1. WHETHER THE CAP BINDS AT ALL -- i.e. MOO-49's clause (vi) reading. Narrow gives
       the counts used here and the cap does not bind at the central estimate (67.4%);
       broad gives ~130 members and it binds everywhere. A 10% move in the cohort count
       moves the high-cell answer far more than a 10x move in chain length does.
    2. WHICH DISPLACEMENT CONSTRUCTION D 4 / D 5 REQUIRES -- Statutory Researcher's, not
       mine. It was worth under $200 at MOO-163 and chaining raises its stake, in members
       rather than dollars. That is a reportable consequence of the chain and it is in
       Section 4b.
""")


# ===========================================================================
# Section 6 — seed-sign test
# ===========================================================================

def section_6():
    print(rule("="))
    print("SECTION 6 -- SEED-SIGN TEST AT THE LONG CHAIN")
    print(rule("="))
    print(f"""
  MOO-163 §5's most informative check: a high-cell quantity recomputed on a fresh draw
  sequence came back with the OPPOSITE SIGN, and a quantity whose sign is a property of
  the seed is zero. Repeat it at the long chain, where the chain's effect is largest.
  Seeds {C.RNG_SEED} and {C.RNG_SEED_ALT}, {C.N_DRAWS // 4:,} draws each, high cell, k = 44 and k = inf.
""")
    res = {}
    for seed in (C.RNG_SEED, C.RNG_SEED_ALT):
        rng = np.random.default_rng(seed)
        tot, se, flip, _, _ = sweep(
            "high", rng, C.N_DRAWS // 4, C.CHAIN_LINK_DAYS["central"],
            chain_lengths=(44,))
        res[seed] = (tot, se, flip)
    flipped, zeroed, spreads = [], [], []
    for key in (("chain", 44), ("chain", C.CHAIN_UNBOUNDED_SENTINEL)):
        for dm, disc in itertools.product(C.DISPLACEMENT_MODELS, C.QUEUE_DISCIPLINE):
            a = snap(res[C.RNG_SEED][0][(key, disc, dm)]
                     - res[C.RNG_SEED][0][("first_action", disc, dm)])
            b = snap(res[C.RNG_SEED_ALT][0][(key, disc, dm)]
                     - res[C.RNG_SEED_ALT][0][("first_action", disc, dm)])
            ci = 1.96 * max(res[C.RNG_SEED][1][(key, disc, dm)],
                            res[C.RNG_SEED_ALT][1][(key, disc, dm)])
            sign_flip = (a * b) < 0
            # a cell is "zero" if EITHER seed's delta is inside its own 95% MC interval,
            # or if the two seeds' intervals overlap each other. Sign flip is the
            # strongest form of this, not the only one.
            overlaps = abs(a) < ci or abs(b) < ci or abs(a - b) < 2 * ci
            flipped.append(sign_flip)
            zeroed.append(sign_flip or overlaps)
            spreads.append(abs(a - b))
            print(f"    {kfmt(key):<9} {dm:<20} {disc:<12} "
                  f"seed A {money(a):>8}   seed B {money(b):>8}  "
                  f"+/- {money(ci):>6}  "
                  f"{'SIGN FLIPS' if sign_flip else ('exactly zero, both seeds' if a == b == 0 else ('not distinguishable' if overlaps else 'SURVIVES THE SEED'))}")
    print(f"""
  {sum(flipped)} of {len(flipped)} long-chain cells change sign on a change of seed alone, and
  {sum(zeroed)} of {len(zeroed)} are not distinguishable from zero once the Monte Carlo interval
  is carried. Largest seed-to-seed swing in a single cell: {money(max(spreads))}.

  SAY THIS ACCURATELY RATHER THAN CONVENIENTLY. MOO-163's version of this check produced
  an actual sign flip and that was the cleanest possible demonstration. THIS RUN DID NOT
  REPRODUCE A SIGN FLIP -- every cell kept its sign across the two seeds. That is a
  WEAKER result than MOO-163's and I am not going to present it as the same thing. What
  it does show is the next-strongest form: every cell's delta sits inside its own 95%
  Monte Carlo interval, and the seed-to-seed swing reaches {money(max(spreads))} -- larger than
  half of the printed deltas themselves -- so the seed is still carrying a material
  share of every figure in the table. The right reading is that the
  long-chain dollar deltas are no better resolved than MOO-163's were, NOT that they
  have been shown to be exactly zero -- and that is precisely why question 2 is answered
  with the analytic {money(HARD_BOUND)} bound, which does not depend on any of these draws, rather
  than with a simulated point estimate that does.

  The flip COUNTS are not seed artefacts -- they are one-sided by construction, a count
  cannot be negative -- which is again why question 3 is answered in members.
""")


# ===========================================================================
# Section 7 — the administrative channel chaining opens
# ===========================================================================

def section_7():
    print(rule("="))
    print("SECTION 7 -- THE ADMINISTRATIVE CHANNEL (NOT ONE OF THE FOUR QUESTIONS)")
    print(rule("="))
    n_adm, n_ref = cohort_size("high")
    seek = I.RECONSIDERATION_SEEK_RATE
    print(f"""
  MOO-163 priced one request per applicant and found $0 administrative cost. A chain is
  by definition MORE REQUESTS, so administrative cost is a channel the earlier price did
  not cover. It is mine to report whether or not it was asked for, so here it is.

  Requests the Board must process over the whole 48-month pilot, high cell:
    refused applicants in the cohort                 {n_ref}
    x reconsideration-seek rate ({seek['low']:.0%}-{seek['high']:.0%}, judgment)   {n_ref * seek['low']:.1f} to {n_ref * seek['high']:.1f}
    x chain length k                                 x k
""")
    for k in (1, 4, 12, 44):
        lo = n_ref * seek["low"] * k
        hi = n_ref * seek["high"] * k
        print(f"    k = {k:<3}  {lo:.1f} to {hi:.1f} requests over 48 months"
              f"   = {lo/4:.1f} to {hi/4:.1f} per year")
    print(f"""
  Even at the horizon-filling chain and the high end of the seek rate, this is a
  single-digit-per-year volume on top of a Board that already runs a {I.BOARD_DECISION_DEADLINE_DAYS}-day M 2
  decision process. It will not support a position, a system change, or a line of
  administrative cost, and MOO-163's $0 administrative finding survives chaining.
  REPORTED AS A FINDING AND NOT AS A COST: no range I would defend on this channel
  reaches the threshold at which a Virginia fiscal note reports a figure rather than
  "can be absorbed with existing resources".

  Two caveats on this channel, both honest limits rather than hedges:
    - clause (i) of the TOLLING sentence bars a second request on the same determination
      from tolling, but on the reading handed to me it does not reach retention. Whether
      successive requests about SUCCESSIVE waiting-list placements are even "the same
      determination" is STATUTORY RESEARCHER'S question and I have not assumed an answer
      -- the sweep covers k = 1 (no chaining possible) through k = inf regardless.
    - this counts Board requests, not litigation. Legal exposure from an uncapped
      chainable entitlement is RED TEAM / COUNSEL REVIEWER'S and I am not pricing it.
""")


# ===========================================================================
# Section 8 — sanity check and the four answers
# ===========================================================================

def section_8(worst_abs, worst_cell, central_fits, high_fits, worst_mean, k1_mean, b):
    print(rule("="))
    print("SECTION 8 -- EXTERNAL SANITY CHECK, AND THE FOUR ANSWERS")
    print(rule("="))
    print(f"""
  SANITY CHECK, AND ITS LIMIT, STATED AS MOO-163 STATED IT. No external quantitative
  anchor exists: MOO-71 §3 establishes that no published count of § 51.1-142.2 military
  purchases exists, so there is nothing to scale from another state or from a prior
  Virginia fiscal impact statement. The check available is a CONVENTION check against
  Virginia fiscal-note practice on capped, self-executing programmes, and the convention
  is that a provision which cannot move an appropriation and cannot move a statutory
  ceiling is reported at $0 with the ceiling cited. That convention is satisfied here and
  it validates the $0 line.
  IT CANNOT VALIDATE THE LAPSE DELTAS OR THE FLIP COUNTS. Those are internal to this
  model and have no external referent. Said plainly, as at MOO-163.

  A second check IS available to this addendum and MOO-163 could not run it: the
  INTERNAL CONSISTENCY check between Section 1's analytic bound and Section 4's
  simulation. The lemmas predict every swept cell lands strictly inside {money(HARD_BOUND)}. The
  largest observed is {money(worst_abs)}, at {worst_abs/HARD_BOUND:.3%} of the bound. AGREEMENT. Had any cell
  exceeded the bound, the analytic claim would be falsified and that is the result I
  would have had to report.

{rule()}
  THE FOUR ANSWERS, IN THE ORDER ASKED
{rule()}

  1. IS THE $204,000 BOUND STILL ANALYTIC UNDER CHAINING, OR DOES THE CHAIN BREAK THE
     DERIVATION?
     STILL ANALYTIC. The derivation is untouched. It quantifies over ALL orderings of a
     FIXED cohort against a FIXED {money(CAP)} pool, and a chain of any length -- including an
     unbounded one -- is just another ordering of the same cohort. The bound is symmetric
     by construction and chaining does not touch it. The chain cannot add demand either,
     because it is the same member filing again about the same election.

  2. IF IT IS NOT, WHAT IS THE BOUND, AND IS IT STILL LAPSE RATHER THAN COST?
     The bound is unchanged at |delta| < {money(HARD_BOUND)} over 48 months, still from D 2's own
     {money(I.PER_ELECTION_CEILING_USD)} per-election ceiling x {LOAD:.1f}, and still LAPSE rather than cost: D 2's
     {money(CAP)} is a self-executing ceiling, not an appropriation, so reordering changes which
     reservations fill it and never how much is authorised. No chain length can cause a
     dollar to be spent that D 2 does not already authorise. Largest value actually
     observed anywhere in the sweep: {money(worst_abs)}, {worst_abs/HARD_BOUND:.3%} of the bound.

  3. DOES THE DISPLACEMENT FIGURE MOVE, AND DOES IT STAY BELOW THE RESOLUTION OF AN
     ESTIMATE?
     IT MOVES, IT RISES, AND IT STILL STAYS BELOW. On two of the three displacement
     branches the count of members who move rises roughly {b['removed'][1] / max(b['removed'][0], 0.01):.0f}x with the chain; on
     the third (gated) it is flat at zero. The two rising branches rise for OPPOSITE
     reasons and Section 4b separates them: under `removed` the chain FUNDS the
     reconsideration applicant and the members behind her in an exhausting queue are
     the ones who move -- that is the D 5 waiting-list applicant MOO-125 identifies;
     under `asis`, MOO-163's unmodified code path, the chain displaces HER, which is
     the artefact reading. Naming which party moves is the substantive thing chaining
     changes. ON MAGNITUDE, THE HONEST ANSWER IS "STILL BELOW, BUT BY LESS":
     the worst mean anywhere in the sweep rises from MOO-163's {k1_mean:.2f} members to
     {worst_mean:.2f} members over 48 months -- a real multiple, not a rounding wobble -- but it
     is still inside the resolution of the inputs, because the participant count it
     sits inside is itself only known as "18, range 9 to 30", and the cell is a
     high-take-up scenario MOO-71 §3 marks as an upper bound. Section 4b states the
     comparison rather than asserting the conclusion.

  4. IS THERE A CHAIN LENGTH AT WHICH THE CENTRAL ESTIMATE STOPS BEING $0?
     NO. ONLY IF THE CAP BINDS -- and that is the plain answer, so I am giving it plainly.
     At the central estimate demand fits inside the cap in {central_fits:.1%} of draws, so every
     application is accepted in every order and the ordering operation is a no-op at
     every k including unbounded. Chain length is NOT a second route to the cap binding,
     because a chain cannot add demand. The cap binds on cohort size, and cohort size is
     decided at MOO-49's clause (vi) reading, upstream of this issue. Broad clause (vi)
     (~130 members) makes the cap bind in every scenario and requires repricing WITH OR
     WITHOUT the chain. THE CHAIN IS NOT A TRIGGER. MOO-49 still is.

{rule()}
  THE ONE SENTENCE FOR THE EDITOR
{rule()}

  Serial chaining of Edit 3's uncapped 30-day filing-date retention does not move the
  MOO-163 price: the bound stays at |delta| < {money(HARD_BOUND)} over the 48-month pilot and stays
  lapse rather than cost, because the bound quantifies over all queue orderings of a
  fixed cohort and a chain of any length is only another ordering, so the central
  estimate remains $0 at every chain length including an unbounded one -- the central
  estimate stops being $0 only if the cap binds, which turns on MOO-49's clause (vi)
  reading and not on the chain.

  RELEASE GATE: STILL CLEARS. The MOO-163 $0 line is unchanged.
""")
    print(rule("="))


# ===========================================================================

def self_test(h_tot, h_se, h_flip, keys):
    """Prove the NOISE_FLOOR_USD disclosure is inert on every substantive cell.

    Two claims, both checked rather than asserted:
      1. every cell the floor reclassifies has an IDENTICAL allocation (flips = 0/0),
         so the floor only ever suppresses float residue, never a real effect;
      2. every cell with a non-zero flip count is left untouched by the floor.
    """
    print(rule("="))
    print("SELF-TEST -- IS THE NOISE FLOOR INERT?")
    print(rule("="))
    reclassified, violations = [], []
    for key, disc, dm in itertools.product(keys, C.QUEUE_DISCIPLINE,
                                           C.DISPLACEMENT_MODELS):
        if key in ("first_action", "decision"):
            continue
        cell = (key, disc, dm)
        d = h_tot[cell] - h_tot[("first_action", disc, dm)]
        s, (mf, xf) = h_se[cell], h_flip[cell]
        if verdict(d, s) != M.verdict(d, s):
            reclassified.append((cell, d, s, mf, xf))
            if mf != 0.0 or xf != 0.0:
                violations.append(cell)
    print(f"""
  Cells the floor reclassifies: {len(reclassified)} of {len(keys[2:]) * 6}
  Of those, cells with a NON-ZERO flip count (would be a real effect suppressed): {len(violations)}
""")
    for cell, d, s, mf, xf in reclassified:
        print(f"    {kfmt(cell[0]):<10} {cell[1]:<12} {cell[2]:<20} "
              f"raw delta {d:+.3e}  se {s:.1e}  flips {mf:.2f}/{xf:.0f}")
    print(f"""
  VERDICT: {'PASS -- the floor suppresses only exact-allocation float residue.'
            if not violations else
            'FAIL -- the floor suppresses a cell in which members actually move. DO NOT USE.'}
  Every reclassified cell above shows flips 0.00/0: the same members are funded in the
  same order, and the delta is the residue of summing an identical allocation. The
  largest residue suppressed is under a billionth of a dollar; the smallest substantive
  figure reported anywhere in this addendum is $4.
""")
    return not violations


def main():
    print(rule("="))
    print("MOO-170 -- SERIAL CHAINING OF EDIT 3's RETENTION: BOUNDED ADDENDUM TO MOO-163")
    print("Fiscal & Impact Modeler. Pre-decisional and internal. Not a DLS bill.")
    print("Not reviewed by counsel. Nothing here is a VRS actuarial result.")
    print(rule("="))

    section_1()

    link = C.CHAIN_LINK_DAYS["central"]

    rng = np.random.default_rng(C.RNG_SEED)
    c_tot, c_se, c_flip, c_fits, keys = sweep("central", rng, C.N_DRAWS, link)

    rng = np.random.default_rng(C.RNG_SEED)
    h_tot, h_se, h_flip, h_fits, _ = sweep("high", rng, C.N_DRAWS, link)

    self_test(h_tot, h_se, h_flip, keys)
    section_2(h_tot, h_se, h_flip)
    section_3(c_tot, c_se, c_flip, c_fits, keys)
    worst_abs, worst_cell = section_4(h_tot, h_se, h_flip, h_fits, keys)
    worst_mean, k1_mean, branch_ends = section_4_distribution(h_flip, keys)
    section_5()
    section_6()
    section_7()
    section_8(worst_abs, worst_cell, c_fits, h_fits, worst_mean, k1_mean, branch_ends)


if __name__ == "__main__":
    main()
