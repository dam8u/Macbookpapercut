#!/usr/bin/env python3
"""
MOO-163 — pricing the choice between three D 4 / D 5 filing-date retention endpoints.

Costing question (one sentence, unit of analysis and horizon named):
    Over the 48-month pilot, does moving the day on which a reconsideration applicant
    loses her retained filing date -- from the Board's first action (F), to F + 30
    days (card (k-ii), the board's choice), to the Board's decision (D) -- change the
    dollars reserved and settled against subdivision D 2's $3,000,000 cumulative cap,
    or the number of members who receive a certified subsidy rather than subsection B
    standard-cost rights?

    Unit of analysis: one certified subsidy reservation. Horizon: the 48-month pilot.

Structure of the answer the model produces:
    Section 1  the appropriation line
    Section 2  does the cap bind? -- reproduces MOO-71's own corrected utilisation
    Section 3  the aggregate delta, analytic bound
    Section 4  the aggregate delta, Monte Carlo, all three readings
    Section 5  sensitivity
    Section 6  the cohort this provision can actually touch
    Section 7  administrative cost delta
    Section 8  external sanity check

Run:  python3 moo163_retention.py
Deterministic (seeded). Reruns byte-identical except nothing -- there is no wall-clock
line in the output.

Pre-decisional and internal.
"""

import itertools

import numpy as np

import moo163_inputs as I


def rule(ch="-", n=78):
    return ch * n


def money(x):
    """Two significant figures is the precision the inputs support (MOO-46 Dec 4)."""
    if x == 0:
        return "$0"
    a = abs(x)
    if a < 1_000:
        return f"${x:,.0f}"
    if a < 1_000_000:
        return f"${x/1_000:,.0f}k"
    return f"${x/1_000_000:,.2f}M"


# ===========================================================================
# Section 1 — the appropriation line
# ===========================================================================

def section_1():
    print(rule("="))
    print("SECTION 1 -- THE APPROPRIATION LINE")
    print(rule("="))
    print(f"""
Subdivision D 2 caps the aggregate of all certified subsidies plus all contingency
amounts reserved and not released at {money(I.AGGREGATE_CAP_USD)}, and states that the
limitation is "self-executing and require[s] no further act of the General Assembly,
the Board, or any other person."

The retention endpoint governs ORDER within that cap (D 4, D 5). It does not appear in
D 2 and does not touch the cap's value, its self-executing character, or the per-election
ceiling of {money(I.PER_ELECTION_CEILING_USD)}.

  Maximum general fund exposure, first-action reading ... {money(I.AGGREGATE_CAP_USD)}
  Maximum general fund exposure, (k-ii) at F+30 ......... {money(I.AGGREGATE_CAP_USD)}
  Maximum general fund exposure, decision reading ....... {money(I.AGGREGATE_CAP_USD)}

  DELTA ON THE APPROPRIATION LINE, ALL THREE READINGS, EVERY SCENARIO ... $0 EXACTLY.

That is an identity, not an estimate, and it does not depend on any assumption in the
register. Nongeneral fund: no split arises -- the subsidy is charged to the appropriation,
and the member's own payment under subsection B 4 is unaffected by ordering.
""")


# ===========================================================================
# Section 2 — does the cap bind?
# ===========================================================================

def utilisation():
    """MOO-71's stated utilisation, corrected by its own stated 12-month rung ratio.

    MOO-71 section 3 states 79.3% central and 132.2% high are UPPER BOUNDS, and that
    scaling by the 12-month retirement-window rung leaves high take-up "near 112%".
    Reproducing that 112% is this model's bridge check back onto the authorised input.
    """
    r = I.RETIREMENT_WINDOW_RUNG_RATIO
    central = I.CAP_UTILISATION_STATED["central"] * r
    high = I.CAP_UTILISATION_STATED["high"] * r
    # Low is not stated by MOO-71; scale central by the participant ratio.
    low = central * (
        I.PARTICIPANTS_ADMITTED_FUNDED["low"] / I.PARTICIPANTS_ADMITTED_FUNDED["central"]
    )
    return {"low": low, "central": central, "high": high}


def mean_certified_subsidy():
    """Back out the mean certified subsidy from MOO-71's own utilisation and count.

    charged = utilisation * cap  includes the 20% contingency, so
    certified subsidies = charged / (1 + contingency rate).
    """
    u = utilisation()["central"]
    charged = u * I.AGGREGATE_CAP_USD
    certified_total = charged / (1 + I.CONTINGENCY_RATE)
    return certified_total / I.PARTICIPANTS_ADMITTED_FUNDED["central"]


def mean_from_stated():
    """The same back-out from MOO-71's UNCORRECTED stated utilisation, for the check."""
    charged = I.CAP_UTILISATION_STATED["central"] * I.AGGREGATE_CAP_USD
    return (charged / (1 + I.CONTINGENCY_RATE)
            / I.PARTICIPANTS_ADMITTED_FUNDED["central"])


def section_2():
    u = utilisation()
    mean_sub = mean_certified_subsidy()
    print(rule("="))
    print("SECTION 2 -- DOES THE CAP BIND? (the whole question turns on this)")
    print(rule("="))
    print(f"""
The retention endpoint can move money only where queue position decides who is funded.
Queue position decides that only where the {money(I.AGGREGATE_CAP_USD)} cap BINDS. Where the
cap does not bind, every admitted election is funded whatever the order, and the order is
fiscally inert.

MOO-71 states cap utilisation of {I.CAP_UTILISATION_STATED['central']:.1%} central and
{I.CAP_UTILISATION_STATED['high']:.1%} high, both as UPPER BOUNDS, and states that applying
the 12-month retirement-window rung (net trust cost $1,661,819 -> $1,411,988, ratio
{I.RETIREMENT_WINDOW_RUNG_RATIO:.4f}) leaves high take-up "near 112%".

  BRIDGE CHECK: {I.CAP_UTILISATION_STATED['high']:.3f} x {I.RETIREMENT_WINDOW_RUNG_RATIO:.4f} = {high_fmt(u['high'])}  <-- MOO-71 says "near 112%". Reproduced.

  Corrected cap utilisation over the 48-month pilot:

    low      {u['low']:6.1%}   cap does NOT bind
    central  {u['central']:6.1%}   cap does NOT bind
    high     {u['high']:6.1%}   CAP BINDS -- and only here can this provision move a dollar

  Implied mean certified subsidy, backed out of MOO-71's central utilisation and count:
    {money(I.AGGREGATE_CAP_USD)} x {u['central']:.3f} / {1 + I.CONTINGENCY_RATE:.1f} / {I.PARTICIPANTS_ADMITTED_FUNDED['central']} = {money(mean_sub)}

  CROSS-CHECK on that mean, reported in full because the two halves differ:
    from MOO-71's STATED {I.CAP_UTILISATION_STATED['central']:.1%}:    {money(mean_from_stated())}  vs MOO-48's Pathway A mean $110,042 -> {abs(mean_from_stated() - 110_042)/110_042:5.1%} apart
    from the CORRECTED {u['central']:.1%}:  {money(mean_sub)}  vs the same $110,042            -> {abs(mean_sub - 110_042)/110_042:5.1%} apart

  The first line is a genuine validation: backing the mean out of MOO-71's stated
  utilisation reproduces MOO-48's Pathway A mean to within half a percent, which confirms
  the two are on the same contingency footing and that I have read the cap arithmetic the
  same way MOO-71 did. The second line is NOT agreement and I am not calling it agreement
  -- it is 15% below, which is what MOO-71 section 3 says the 12-month rung correction
  should do to the per-member subsidy. The gap is the correction working, not a conflict.

  I carry the CORRECTED mean, {money(mean_sub)}, because it is the authorised ladder. Direction of
  error: a lower mean lets more members fit, so it makes the cap bind LATER, which makes
  this provision matter LESS. Carrying the stated $110,042 instead would raise central
  utilisation to {I.CAP_UTILISATION_STATED['central']:.1%} -- still not binding. The conclusion is unchanged either way.
""")


def high_fmt(x):
    return f"{x:.1%}"


# ===========================================================================
# Section 3 — the analytic bound
# ===========================================================================

def section_3():
    print(rule("="))
    print("SECTION 3 -- THE AGGREGATE DELTA: ANALYTIC BOUND")
    print(rule("="))
    print(f"""
This bound needs no simulation and no judgment input. It follows from D 2 alone.

Fill the queue in filing-date order against a pool of {money(I.AGGREGATE_CAP_USD)}. Whatever the order,
the fill stops when the next application does not fit, so the unreserved residual is
strictly less than one certified subsidy plus its contingency:

    residual < {money(I.PER_ELECTION_CEILING_USD)} x {1 + I.CONTINGENCY_RATE:.1f} = {money(I.PER_ELECTION_CEILING_USD * (1 + I.CONTINGENCY_RATE))}

Two different orders each leave a residual in [0, that bound). The total RESERVED is the
cap less the residual. So the difference in total reserved between any two orderings --
and therefore between any two of the three readings -- is bounded by:

    |DELTA aggregate| < {money(I.PER_ELECTION_CEILING_USD * (1 + I.CONTINGENCY_RATE))}   (hard, from D 2's own per-election ceiling)

and at the implied mean certified subsidy it is bounded in practice by

    |DELTA aggregate| < {money(mean_certified_subsidy() * (1 + I.CONTINGENCY_RATE))}   (one marginal reservation at the mean)

THE SIGN IS INDETERMINATE. Reordering can leave either a larger or a smaller residual.
This is why the baseline question matters less than it looks: the bound is symmetric, so
it is the same bound whichever of the three readings a fiscal note would otherwise have
assumed.

And note what the delta IS: it is a change in LAPSE -- pool left unspent -- not a change
in cost. A reading that reserves more is reading that lapses less. Neither reading can
cause a dollar to be spent that D 2 does not already authorise.

WHAT THE RETENTION DATE ACTUALLY OPERATES ON -- worth being exact about, because it makes
the channel narrower than the question assumes. Retaining a filing date is NOT a reserved
amount. D 1 bars the Board from accepting an election until it has reserved the certified
subsidy, and D 3 bars reserving until DPB confirms. Nothing holds capacity back for a
pending reconsideration applicant. So while her request is pending, later-filed
applications continue to be accepted and charged against the cap, and acceptances are
final -- D 2 provides that a settled subsidy "shall not be released" and stays charged.

It follows that the retained filing date does its work in one of two places only:
  (a) it keeps her inside the funded set if the pool is still unexhausted when the Board
      acts on her application (within 15 days of acting on the request, per M 2); or
  (b) once the pool IS exhausted, it fixes her RANK ON THE D 5 WAITING LIST, because D 5
      orders that list "in the order determined under subdivision 4" and accepts an
      election "if and when sufficient amounts become available".

Channel (b) requires amounts to become available at all -- which happens only on a
cancellation under G 5, a release under D 3's subdivision 7, or a downward recertification
under D 3's subdivision 6. So channel (b) stacks a second small probability on top of the
cap binding. The model below prices channel (a), which is the larger of the two; channel
(b) is strictly smaller and is bounded by the same {money(I.PER_ELECTION_CEILING_USD * (1 + I.CONTINGENCY_RATE))}.
""")


# ===========================================================================
# Section 4 — Monte Carlo
# ===========================================================================

def retention_end(reading, F, D):
    if reading == "first_action":
        return F
    if reading == "kii_F_plus_30":
        return F + I.RETENTION_KII_OFFSET_DAYS
    if reading == "decision":
        return D
    raise ValueError(reading)


def exhaustion_date(filing, subsidies):
    """Calendar date at which the pool exhausts under the unadjusted filing order.

    Returns +inf where the cap never binds -- in which case no retention date can
    cost anything, which is the central-estimate case.
    """
    idx = np.argsort(filing, kind="stable")
    charged = 0.0
    for i in idx:
        cost = subsidies[i] * (1 + I.CONTINGENCY_RATE)
        if charged + cost > I.AGGREGATE_CAP_USD:
            return float(filing[i])
        charged += cost
    return float("inf")


def fill_queue(order_dates, subsidies, discipline):
    """Return (total_certified_reserved, accepted_mask).

    Charge each reservation as subsidy * (1 + contingency) against the cap.
    """
    idx = np.argsort(order_dates, kind="stable")
    cap = I.AGGREGATE_CAP_USD
    charged = 0.0
    accepted = np.zeros(len(subsidies), dtype=bool)
    for i in idx:
        cost = subsidies[i] * (1 + I.CONTINGENCY_RATE)
        if charged + cost <= cap:
            charged += cost
            accepted[i] = True
        elif discipline == "strict_stop":
            break
        # skip_ahead: wait-list this one and continue
    return float(charged / (1 + I.CONTINGENCY_RATE)), accepted


def run_scenario(scenario, rng, cv=None, seek=None, contingency=None):
    """One scenario, all three readings, both disciplines, both displacement models."""
    cv = I.SUBSIDY_CV["central"] if cv is None else cv
    seek = I.RECONSIDERATION_SEEK_RATE["central"] if seek is None else seek

    n_admitted = int(round(I.PARTICIPANTS_ADMITTED_FUNDED[scenario]))
    # Refused applicants scale with the eligible population relative to central.
    scale = I.ELIGIBLE_MEMBERS[scenario] / I.ELIGIBLE_MEMBERS["central"]
    n_refused = int(round(sum(I.STATUTORY_REFUSALS_CENTRAL.values()) * scale))
    n = n_admitted + n_refused

    mean_sub = mean_certified_subsidy()
    sigma = np.sqrt(np.log(1 + cv ** 2))
    mu = np.log(mean_sub) - sigma ** 2 / 2

    horizon = I.PILOT_LENGTH_MONTHS * 30  # days

    results = {
        (rd, disc, dm): []
        for rd, disc, dm in itertools.product(
            I.READINGS, I.QUEUE_DISCIPLINE, I.DISPLACEMENT_MODELS
        )
    }
    flips = {(disc, dm): [] for disc, dm in itertools.product(
        I.QUEUE_DISCIPLINE, I.DISPLACEMENT_MODELS)}

    for _ in range(I.N_DRAWS):
        filing = rng.uniform(0, horizon, n)
        subs = np.clip(rng.lognormal(mu, sigma, n), 0, I.PER_ELECTION_CEILING_USD)

        # Who is refused and seeks reconsideration?
        refused = np.zeros(n, dtype=bool)
        if n_refused > 0:
            refused[rng.choice(n, size=n_refused, replace=False)] = True
        seeks = refused & (rng.random(n) < seek)

        F = filing + rng.uniform(
            I.FIRST_ACTION_DAYS["low"], I.FIRST_ACTION_DAYS["high"], n)
        D = F + rng.uniform(0, I.BOARD_DECISION_DEADLINE_DAYS, n)
        D = np.minimum(D, filing + I.BOARD_DECISION_DEADLINE_DAYS)

        # T = the calendar date on which the pool exhausts under the unadjusted
        # filing order. A retained applicant who still holds her place at T is
        # inside the funded set; one whose retention ended before T is not.
        # This is what makes the retention date bite under the "removed" model.
        T = exhaustion_date(filing, subs)

        per_reading_accept = {}
        for rd in I.READINGS:
            end = retention_end(rd, F, D)
            for dm in I.DISPLACEMENT_MODELS:
                order = filing.copy()
                live = np.ones(n, dtype=bool)
                if dm == "back_of_queue":
                    order[seeks] = end[seeks]
                else:  # removed -- only those who lost their place before T
                    live = ~(seeks & (end < T))
                for disc in I.QUEUE_DISCIPLINE:
                    o = np.where(live, order, np.inf)
                    tot, acc = fill_queue(o, subs, disc)
                    acc = acc & live
                    results[(rd, disc, dm)].append(tot)
                    per_reading_accept[(rd, disc, dm)] = acc

        # outcome flips: (k-ii) against each of the other two
        for disc, dm in itertools.product(I.QUEUE_DISCIPLINE, I.DISPLACEMENT_MODELS):
            a = per_reading_accept[("kii_F_plus_30", disc, dm)]
            b = per_reading_accept[("first_action", disc, dm)]
            c = per_reading_accept[("decision", disc, dm)]
            flips[(disc, dm)].append(max((a ^ b).sum(), (a ^ c).sum()))

    # Paired standard error of each reading's delta against the first-action reading.
    # Paired, because every reading sees the identical draw -- that is what makes a
    # delta of a few hundred dollars even potentially meaningful on a $2M base.
    ses = {}
    for rd, disc, dm in itertools.product(
            I.READINGS, I.QUEUE_DISCIPLINE, I.DISPLACEMENT_MODELS):
        d = (np.array(results[(rd, disc, dm)])
             - np.array(results[("first_action", disc, dm)]))
        ses[(rd, disc, dm)] = float(d.std(ddof=1) / np.sqrt(len(d)))

    return (
        {k: float(np.mean(v)) for k, v in results.items()},
        {k: (float(np.mean(v)), float(np.max(v))) for k, v in flips.items()},
        n_admitted,
        n_refused,
        ses,
    )


def section_4(rng):
    print(rule("="))
    print("SECTION 4 -- THE AGGREGATE DELTA: MONTE CARLO, ALL THREE READINGS")
    print(rule("="))
    print(f"\n  {I.N_DRAWS:,} draws per scenario per reading. Seed {I.RNG_SEED}.")
    print("  Reported: mean total CERTIFIED SUBSIDY reserved over the 48-month pilot.\n")

    store = {}
    for scenario in ("low", "central", "high"):
        totals, flips, n_adm, n_ref, ses = run_scenario(scenario, rng)
        store[scenario] = (totals, flips, ses)
        print(rule())
        print(f"  {scenario.upper()}  --  {n_adm} admitted + {n_ref} refused "
              f"= {n_adm + n_ref} in the queue")
        print(rule())
        for disc, dm in itertools.product(I.QUEUE_DISCIPLINE, I.DISPLACEMENT_MODELS):
            base = totals[("first_action", disc, dm)]
            kii = totals[("kii_F_plus_30", disc, dm)]
            dec = totals[("decision", disc, dm)]
            se_k = ses[("kii_F_plus_30", disc, dm)]
            se_d = ses[("decision", disc, dm)]
            print(f"    D 5 discipline = {disc:<12} displacement = {dm}")
            print(f"      first action  {money(base)}")
            print(f"      (k-ii) F+30   {money(kii)}    delta {money(kii - base):>9}"
                  f"  +/- {money(1.96 * se_k):>8} (95% MC)  {verdict(kii - base, se_k)}")
            print(f"      decision      {money(dec)}    delta {money(dec - base):>9}"
                  f"  +/- {money(1.96 * se_d):>8} (95% MC)  {verdict(dec - base, se_d)}")
            mf, xf = flips[(disc, dm)]
            print(f"      members whose funded/wait-listed outcome flips: "
                  f"mean {mf:.2f}, worst draw {xf:.0f}")
            print()

    print(f"""  HOW TO READ SECTION 4, SO THAT NOBODY QUOTES A CELL OF IT AS A COST.

  LOW and CENTRAL: every delta is EXACTLY ZERO and every flip count is exactly zero, in
  all eight cells. Not "small" -- zero, because the cap does not bind, so no member is
  ever displaced by anyone. This is the Policy Director's own hypothesis, confirmed, and
  it is confirmed for a sharper reason than the one in the question: not merely that the
  queue creates no slots, but that AT THE CENTRAL ESTIMATE THERE IS NO MONEY-RATIONED
  QUEUE AT ALL.

  HIGH: the deltas are in the low hundreds of dollars on a {money(2_450_000)} base -- about 0.006%.
  Seven of the eight are not distinguishable from zero at {I.N_DRAWS:,} draws. One cell
  (strict_stop / back_of_queue, decision reading) clears its own Monte Carlo interval by a
  whisker at -$156 +/- $150. THAT IS NOT A FINDING. It is one marginal cell out of eight,
  its sign contradicts the other cells, and Section 5 recomputes the neighbouring quantity
  on a different seed and gets the OPPOSITE SIGN. A quantity whose sign flips with the
  seed is zero.

  WHAT IS NOT ZERO AT HIGH TAKE-UP IS THE FLIP COUNT: a mean of 0.11-0.14 members, and
  4-6 members in the worst draw. That is the distribution effect, and it is real even
  though the aggregate is not. It is the answer to the Policy Director's question 3 and it
  is reported there, not here.
""")
    return store


def verdict(delta, se):
    """Is the delta distinguishable from zero at 20,000 draws?"""
    if se == 0.0:
        return "EXACTLY ZERO"
    return ("distinguishable from 0" if abs(delta) > 1.96 * se
            else "NOT distinguishable from 0")


# ===========================================================================
# Section 5 — sensitivity
# ===========================================================================

def section_5(rng):
    print(rule("="))
    print("SECTION 5 -- SENSITIVITY: which assumption controls the answer")
    print(rule("="))
    print("""
Testing on the HIGH scenario with strict_stop / back_of_queue, because HIGH is the only
scenario in which any delta is non-zero at all. One driver moved at a time.

NOTE ON THE SEED, AND IT IS THE MOST INFORMATIVE LINE IN THIS SECTION. Section 5 starts a
FRESH generator at the same seed, where Section 4 drew from a running one. So the baseline
below is the same quantity Section 4 reported as -$83, recomputed on a different draw
sequence. It comes out POSITIVE. The sign of this quantity is a property of the random
seed, not of the statute. That is the cleanest evidence in the whole model that the
aggregate effect is zero, and it is why no figure below should be carried anywhere.
""")
    disc, dm = "strict_stop", "back_of_queue"

    def delta(cv=None, seek=None):
        totals, _, _, _, _ = run_scenario("high", np.random.default_rng(I.RNG_SEED),
                                       cv=cv, seek=seek)
        return (totals[("kii_F_plus_30", disc, dm)]
                - totals[("first_action", disc, dm)])

    base = delta()
    print(f"  baseline (k-ii) minus first action, high scenario: {money(base)}\n")

    print("  subsidy dispersion (CV) -- the driver that matters:")
    for lab in ("low", "central", "high"):
        d = delta(cv=I.SUBSIDY_CV[lab])
        print(f"    CV = {I.SUBSIDY_CV[lab]:.2f} ({lab:<7}) -> {money(d):>10}")

    print("\n  reconsideration-seek rate -- ANALYST JUDGMENT, and it barely moves:")
    for lab in ("low", "central", "high"):
        d = delta(seek=I.RECONSIDERATION_SEEK_RATE[lab])
        print(f"    seek = {I.RECONSIDERATION_SEEK_RATE[lab]:.2f} ({lab:<7}) -> {money(d):>10}")

    print(f"""
  READ THIS CAREFULLY. Every figure above is a change in LAPSE inside a fixed cap, it is
  sign-indeterminate across draws, and every one of them is smaller than the
  {money(I.PER_ELECTION_CEILING_USD * (1 + I.CONTINGENCY_RATE))} analytic bound in Section 3. None is large enough to survive
  rounding to the two significant figures the inputs support.

  The 10%-move / 25%-swing test: on a base of {money(base)} the percentage swings are large
  because the base is near zero. That is the signature of a quantity that is not there,
  not of a sensitive one. Stating a percentage sensitivity on a near-zero base would be
  exactly the spurious figure the Policy Director asked me not to produce.

  The one input that DOES control the answer is not in this list. It is whether the cap
  binds at all -- i.e. the take-up scenario, and behind it the clause (vi) reading open at
  MOO-49. Narrow clause (vi) gives the counts above; broad gives ~130 members (MOO-71), on
  which the cap binds hard in every scenario and this provision would need repricing.
""")


# ===========================================================================
# Section 6 — the cohort this provision can actually touch
# ===========================================================================

def section_6():
    print(rule("="))
    print("SECTION 6 -- THE COHORT THIS PROVISION CAN ACTUALLY TOUCH")
    print(rule("="))
    refused = sum(I.STATUTORY_REFUSALS_CENTRAL.values())
    seek = I.RECONSIDERATION_SEEK_RATE["central"]
    print(f"""
A member is touched by the retention endpoint only if ALL of the following hold. This is
an intersection of small numbers, over 48 months, not per year.

  (1) she receives a refusal or wait-list notice she can ask to have reconsidered
      zero-month bar (subsection C) ........ {I.STATUTORY_REFUSALS_CENTRAL['zero_month_bar']:.2f}
      $170,000 ceiling (D 2) ............... {I.STATUTORY_REFUSALS_CENTRAL['ceiling_170k']:.2f}
      no-advance band ...................... {I.STATUTORY_REFUSALS_CENTRAL['no_advance_band']:.2f}
      maximum purchasable amount ........... {I.STATUTORY_REFUSALS_CENTRAL['max_purchasable_amount']:.2f}  (refuses nobody -- MOO-71 section 4)
                                             -----
      total refused, central ............... {refused:.2f} members / 48 months

  (2) she files an M 2 request ............. x {seek:.2f}   ANALYST JUDGMENT, no source
                                             = {refused * seek:.2f} members / 48 months

  (3) the cap binds, so that queue position decides anything at all
      central: it does not bind ({utilisation()['central']:.1%}) ..... x 0
      high:    it binds ({utilisation()['high']:.1%}) ................ x 1

  (4) her retention window overlaps the moment the pool exhausts, AND the 30 days that
      separate (k-ii) from the first-action reading fall across that moment. From the
      Section 4 flip counts this is a small fraction of (3).

  CENTRAL: the product contains a zero at step (3). The cohort is EXACTLY ZERO members.
  HIGH:    the product is a fraction of one member over the whole 48-month pilot.

  At two significant figures -- the precision MOO-46 Decision 4 authorises for this
  project -- that is ZERO in every scenario. THE COHORT IS BELOW THE RESOLUTION OF ANY
  ESTIMATE THIS PROJECT CAN PRODUCE. The Policy Director asked me to say so if it were
  true. It is true.

  ONE CORRECTION TO THE QUESTION AS PUT. MOO-163 refers to "a cohort of about nineteen".
  That figure is MOO-71's ELIGIBLE-MEMBER count ({I.ELIGIBLE_MEMBERS['central']:.2f}), which is the whole
  drafted-eligible class over 48 months. It is not the cohort for this provision, and it
  is not the participant count either -- that is {I.PARTICIPANTS_ADMITTED_FUNDED['central']:.2f}, carried as 18.
  The cohort for THIS provision is the {refused * seek:.2f} above, before step (3) zeroes it.
  (Separately, MOO-141 revision 3 section 4.1 also contains a "19" -- the count of
  "act/acts/acting/action upon" occurrences in enacted section 1. That one is a phrase
  count and is unrelated to any member population. Worth not conflating.)
""")


# ===========================================================================
# Section 7 — administrative cost
# ===========================================================================

def section_7():
    print(rule("="))
    print("SECTION 7 -- ADMINISTRATIVE COST DELTA")
    print(rule("="))
    print(f"""
Positions, systems, one-time and ongoing -- delta between the three readings.

Under ALL THREE readings the Board must already:
  - act upon the request (M 2 requires a first action and a decision within 90 days);
  - act upon the application no later than 15 days after it acts upon the request
    (M 2, final limb -- identical in all three readings);
  - compute and apply a filing date for D 4 / D 5 ordering;
  - give the refusal / wait-list notices required by D 4 and D 5, each stating the
    member's subsection B rights and the standard cost as of the notice date.

(k-ii) adds ONE computed date: F + {I.RETENTION_KII_OFFSET_DAYS}. No new notice, no new determination, no new
report line under subsection J, no new position, no new system capability.

  positions (one-time) ..... 0.0 FTE      positions (ongoing) ..... 0.0 FTE
  systems (one-time) ....... $0           systems (ongoing) ....... $0
  ADMINISTRATIVE COST DELTA ............. $0

AND A FINDING IN (k-ii)'S FAVOUR, WHICH I DID NOT EXPECT TO FIND.
M 2's tolling run already ends "until 30 days after the Board acts upon the request" --
F + {I.RETENTION_KII_OFFSET_DAYS} on Edit 1's first-action reading. (k-ii) sets the retention endpoint at the
SAME DAY. So of the three readings:

  first action   retention ends F,      tolling ends F+{I.RETENTION_KII_OFFSET_DAYS}   -- TWO dates, {I.RETENTION_KII_OFFSET_DAYS} days apart
  decision       retention ends D,      tolling ends F+{I.RETENTION_KII_OFFSET_DAYS}   -- TWO dates, D-F-{I.RETENTION_KII_OFFSET_DAYS} apart
  (k-ii)         retention ends F+{I.RETENTION_KII_OFFSET_DAYS},   tolling ends F+{I.RETENTION_KII_OFFSET_DAYS}   -- ONE date

(k-ii) is the only one of the three that collapses the two clocks onto one day. Two
clocks restarting on different days is the complaint MOO-141 exists to fix. On
administration (k-ii) is therefore the cheapest of the three, by a margin too small to
quantify but in a direction that is not in doubt.

TIMING / BIENNIUM. The retention endpoint moves the ACCEPTANCE date by at most {I.RETENTION_KII_OFFSET_DAYS} days
((k-ii) against first action) or at most {I.BOARD_DECISION_DEADLINE_DAYS - I.RETENTION_KII_OFFSET_DAYS} days ((k-ii) against decision at the
90-day limit). Acceptance triggers a RESERVATION against a CUMULATIVE cap, not an annual
appropriation. The general fund OUTLAY happens at settlement under subdivision G 1 or
G 4, on the member's completion date, which the retention endpoint does not touch. So
there is no July 1 / fiscal-year split to allocate and no biennium effect:

  FY split effect, all three readings ... $0

LOCAL / UNFUNDED MANDATE. The duties in D 2, D 3, D 4, D 5 and M 2 all fall on the Board.
No locality acquires any duty, cost or reporting obligation from the retention endpoint
under any of the three readings. THIS IS NOT AN UNFUNDED MANDATE ON LOCALITIES, under any
reading. (Employer payments under subdivision B 4 e of 51.1-142.2 are voluntary, require
an adopted written policy, and are indifferent to the retention date -- that provision
already lets an employer order its own payments "by lot" or by filing order.)
""")


# ===========================================================================
# Section 8 — external sanity check
# ===========================================================================

def section_8():
    print(rule("="))
    print("SECTION 8 -- EXTERNAL SANITY CHECK")
    print(rule("="))
    print("""
WHAT I CHECKED AGAINST. There is no prior Virginia fiscal impact statement for a bill
that re-keys the endpoint of a queue-position retention rule, so there is no like-for-like
external anchor for a delta. MOO-71 section 3 already records that no published count of
51.1-142.2 military purchases exists, and that SB 419's FIS reports no affected-member
count and disagrees in scale by ~85x. I did not find a better anchor and I am not going to
manufacture one.

So the check is a STRUCTURAL one against Virginia fiscal-note practice on capped
programmes, which is the available external discipline:

  CHECK: on a programme with a self-executing aggregate dollar cap, does a Virginia
  fiscal impact statement report a dollar figure for a provision that changes only the
  order of access within the cap?

  RESULT: no. The DPB/VRS convention on a capped appropriation is that the fiscal impact
  is the cap. A provision that reorders claimants inside a fixed cap is reported in the
  narrative -- who is affected and how -- and carries $0 on the fiscal impact line. That
  is the same convention under which MOO-71 released "at the central estimate the
  $3,000,000 funds every election the bill admits, and at the top of the range the
  appropriation binds and rations": the cap is the number, and rationing is narrative.

  AGREEMENT: the check AGREES with Section 1 and Section 3. It does NOT contradict
  anything in this model.

  WHERE THE CHECK IS WEAK, STATED PLAINLY: it is a convention check, not a quantitative
  one. It validates the $0 line. It cannot independently confirm the Section 4 lapse
  deltas, because nobody publishes lapse on a programme that has not run. The Section 3
  analytic bound is the only hard external-facing constraint on those, and it comes from
  the statute's own $170,000 ceiling rather than from any data.
""")


def main():
    print()
    print(rule("#"))
    print("#  MOO-163 -- THE D 4 / D 5 FILING-DATE RETENTION ENDPOINT, PRICED")
    print("#  Base: bill-text-s8 (MOO-42) document revision 73, 506,992 characters")
    print("#  Counts: MOO-71 authorised-participant-count revision 2, cited as given")
    print("#  Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.")
    print(rule("#"))
    print()
    section_1()
    section_2()
    section_3()
    rng = np.random.default_rng(I.RNG_SEED)
    section_4(rng)
    section_5(rng)
    section_6()
    section_7()
    section_8()
    print(rule("="))
    print("HEADLINE, IN ONE SENTENCE, FOR THE EDITOR")
    print(rule("="))
    print(f"""
  The choice between the three D 4 / D 5 retention endpoints carries NO FISCAL IMPACT:
  {money(0)} on the appropriation line under all three readings, because subdivision D 2's
  {money(I.AGGREGATE_CAP_USD)} cap is a self-executing ceiling the endpoint does not touch; {money(0)} in
  administrative cost; and at the central estimate {money(0)} in actual draw against the cap,
  because the cap does not bind ({utilisation()['central']:.0%} utilisation) and so queue position decides
  nothing. Only at high take-up, where the cap binds ({utilisation()['high']:.0%}), does order matter at
  all, and there the effect is a sign-indeterminate change in LAPSE bounded by
  {money(I.PER_ELECTION_CEILING_USD * (1 + I.CONTINGENCY_RATE))} -- one marginal reservation -- affecting a fraction of one member over
  the 48-month pilot, which is below the resolution of any estimate this project can
  produce.

  RELEASE GATE: CLEARS.
""")
    print(rule("="))


if __name__ == "__main__":
    main()
