"""
MOO-170 — assumption register for the SERIAL CHAINING addendum to MOO-163.

This file holds ONLY the assumptions that are new to MOO-170. Every other number
comes from MOO-163's register (`moo163_inputs.py`), imported unchanged. The MOO-163
register is not restated, not re-derived, and not edited: the addendum is bounded.

Pre-decisional and internal. Not a DLS bill. Not reviewed by counsel.
Retrieval date for every Paperclip-internal source below: 12 October 2026.
"""

# ---------------------------------------------------------------------------
# E. THE CHAINING MECHANIC — statutory reading handed to me, not derived here
# ---------------------------------------------------------------------------

CHAIN_IS_UNCAPPED = True
# unit: boolean.
# source: HANDED TO ME by the Policy Director on MOO-170, from pass 18's finding F-6
#   (MOO-166) on the MOO-162 patch, revision 5. The finding: subsection M 2's TOLLING
#   sentence carries "(i) no second or subsequent request ... [tolls]" and "(ii) the
#   aggregate of all [tolling] shall not exceed 120 days", and the RETENTION sentence
#   that Edit 3 amends carries NEITHER limit.
# I am NOT reading the statute for myself. Whether the retention sentence in fact
#   carries no clause (i) and no clause (ii) is STATUTORY RESEARCHER'S, and MOO-170
#   instructs me to take it as given. Everything below is conditional on it.
# direction of error: if the limits do reach the retention sentence after all, the
#   chain collapses to k = 1 with a 120-day aggregate ceiling, and MOO-163 stands
#   unmodified. That is the favourable direction; this addendum prices the adverse one.

RETENTION_DAYS_PER_REQUEST = 30
# unit: days of retention per request, measured from the Board's action on it.
# source: card (k-ii), drafted as Edit 3 on MOO-162 — "until 30 days after the Board
#   acts upon the request". Same figure as MOO-163's RETENTION_KII_OFFSET_DAYS; named
#   again here because under chaining it is a per-link quantity, not an endpoint.

# ---------------------------------------------------------------------------
# F. CHAIN GEOMETRY — ANALYST JUDGMENT, and deliberately NOT load-bearing
# ---------------------------------------------------------------------------

CHAIN_LINK_DAYS = {"low": 33, "central": 40, "high": 120}
# unit: days of additional retention bought by each request after the first.
# source: ANALYST JUDGMENT, constructed from statutory parameters only. A member who
#   files her next request inside the live window gets retention to (that Board action
#   + 30). The Board action lands 3-30 days out at the FIRST_ACTION_DAYS band in
#   MOO-163's register, and M 2 allows it up to 90 days. So a link adds
#   3 + 30 = 33 days at the fast end, 10 + 30 = 40 at the central first-action day,
#   and 90 + 30 = 120 days if the Board runs the full M 2 clock each time.
# direction of error: NONE THAT MATTERS, and this is the point. Link length decides
#   only WHICH k saturates the 1,440-day pilot, not what the saturated answer is.
#   Section 4 sweeps k past saturation under all three link lengths and the saturated
#   cell is identical. No conclusion in this addendum rests on this input.

CHAIN_LENGTHS = (1, 2, 3, 4, 6, 12, 24, 44)
# unit: number of requests in the chain (k = 1 is MOO-163's priced case, a single
#   30-day retention, i.e. the card (k-ii) reading exactly).
# source: model control. k = 44 is the largest chain that fits the 48-month pilot at
#   the 33-day link (1,440 / 33 = 43.6), so it is the horizon-filling case.
# The sweep is reported in full. There is no "assumed" chain length anywhere in the
#   answer; the answer is a statement about ALL of them plus the limit below.

CHAIN_UNBOUNDED_SENTINEL = "unbounded"
# The limiting case: retention never ends inside the pilot. This is the case the
# Policy Director's question is really about, and it is evaluated EXACTLY rather than
# approached by large k, so no extrapolation is involved.

CHAIN_CONTINUATION_RATE = {"low": 0.10, "central": 0.30, "high": 0.70}
# unit: probability that a member who filed one M 2 request files another.
# source: ANALYST JUDGMENT. No Virginia source: VRS publishes no M 2 reconsideration
#   volumes for § 51.1-142.2 purchases, and MOO-71 §3 records that no published count
#   of these purchases exists at all. I would defend 10-70%: a member who has already
#   filed once has revealed both the motive and the capability, and the second request
#   is cheap to her, which argues for the high end; against it, she only has something
#   to chain ABOUT if the Board has acted adversely twice.
# direction of error: symmetric. NOT load-bearing — Section 4's deterministic sweep
#   brackets every value of this input, including 1.00, so it is reported for realism
#   only and no bound depends on it.

# ---------------------------------------------------------------------------
# G. MODEL CONTROLS
# ---------------------------------------------------------------------------

RNG_SEED = 20261012
# Same seed as MOO-163, so the k = 1 column is drawn from the same stream family and
# the bridge check in Section 2 is like-for-like.

RNG_SEED_ALT = 20261013
# For the seed-sign test in Section 6. MOO-163's §5 showed a high-cell quantity whose
# sign flips with the seed; this addendum repeats that test at the dominant chain
# length, because a chained quantity that flips sign is just as zero as an unchained
# one.

N_DRAWS = 20_000
# Monte Carlo draws per scenario. Same as MOO-163, so the MC intervals are directly
# comparable to the ones already in the record.

DISPLACEMENT_MODELS = ("back_of_queue_asis", "back_of_queue_gated", "removed")
# MOO-163 carried two construction branches, `back_of_queue` and `removed`, and
# reported both because the text does not settle which applies. Under chaining the
# first of those two needs splitting, and THIS IS A DISCLOSED CHANGE TO THE MOO-163
# CODE PATH, not a silent one:
#
#   back_of_queue_asis   — MOO-163's implementation, verbatim: the applicant's
#       ordering date BECOMES the retention end date, unconditionally. Faithful at
#       k = 1, where the end date sits 30 days past a first action 3-30 days out and
#       so is always inside the live ordering range. AT LARGE k IT IS AN ARTEFACT: it
#       relegates a member to a date beyond the pilot even though, on a long chain,
#       she never actually lost the retained date. Reported anyway, unmodified, so the
#       reader can see the MOO-163 code path's own behaviour and check that the bound
#       holds even on the artefact.
#   back_of_queue_gated  — the faithful generalisation: she is relegated to the
#       retention end date ONLY IF retention ended before the pool exhausted
#       (end < T). If she still held the retained date when the pool ran out, she
#       keeps her original filing date. This is the branch to quote.
#   removed              — MOO-163's second branch, unchanged and needing no
#       generalisation: she drops out of the subsidised queue only if retention ended
#       before the pool exhausted, which is already an `end < T` test.
#
# Section 2 measures what the asis/gated split costs at k = 1, so the disclosure is
# quantified rather than asserted.

QUEUE_DISCIPLINE = ("strict_stop", "skip_ahead")
# Unchanged from MOO-163's register, imported there and named here only so this file
# reads as a complete control block. Which one D 5 requires is STATUTORY RESEARCHER'S.
