#!/usr/bin/env python3
"""MOO-195 — test of the advisory's single load-bearing fiscal assumption.

The assumption, never written down because the cut carried no fiscal note:
    THE ADVISORY CHANGES NO BEHAVIOUR AND THEREFORE COSTS NOTHING.

The test: suppose it works. A member who redesignates from a non-qualifying
beneficiary (sibling, adult child, estate) to a qualifying one (spouse, minor
child, parent) converts, in a death-in-service case, a § 51.1-162 A lump-sum
refund of accumulated contributions into a § 51.1-162 B lifetime allowance.
B costs the trust more than A. So a working advisory RAISES cost.

Election counts are MOO-183's, as published. Everything else is my own
assumption and is labelled as such; nothing here is a VRS actuarial result.

No team file is read or modified; MOO-183's engine is not re-run.
"""

# --- MOO-183, as published (deliverable `moo183-counts-and-cost-per-participant`)
COHORTS = {
    "recommended, 12-month rung":             18.9,
    "recommended, 12-month rung + option(c)":  18.4,
    "S8 @ 4.00%, 6-month basis":               85.0,
    "S8 @ 5.00%, 6-month basis":               73.0,
}

# --- exposure window, from the act's own dials (§ 51.1-142.4 E, F and the
#     definitions of "earliest"/"final qualifying retirement date" in A)
#     certification -> payment in full          <= 12 months  (E)
#     -> crediting                              <= 1 month    (E)
#     -> earliest qualifying retirement date     ~ 1 month    (A)
#     -> final qualifying retirement date        +12 months, +3 on Board approval (A)
WINDOW_MAX_YEARS = (12 + 1 + 1 + 15) / 12.0      # ~2.42
WINDOW_MID_YEARS = (4 + 1 + 1 + 12) / 12.0       # ~1.50, prompt payer

# --- my assumptions, each stated so the Director can move it ---------------
MORTALITY = 0.0045      # annual death-in-service, state employees aged ~50-62
NONQUALIFYING = 0.25    # share of purchasers whose designee is not a spouse,
                        # minor child or parent
SWITCH = 0.20           # share of those who redesignate because of the advisory
DELTA_PV = 400_000      # PV of a § 51.1-162 B lifetime allowance less the
                        # § 51.1-162 A refund it displaces, per case


def run(window, label):
    print(f"\n{label} (exposure {window:.2f} yr, mortality {MORTALITY:.2%}/yr)")
    print(f"  {'cohort':40} {'deaths':>8} {'caused':>9} {'cost':>12}")
    for name, n in COHORTS.items():
        deaths = n * window * MORTALITY
        caused = deaths * NONQUALIFYING * SWITCH
        print(f"  {name:40} {deaths:8.3f} {caused:9.4f} {caused*DELTA_PV:11,.0f}")


run(WINDOW_MID_YEARS, "Central — prompt payer")
run(WINDOW_MAX_YEARS, "Upper   — every dial at its maximum")

# --- what it would take to reach $100,000, the package's rounding floor ----
worst = (max(COHORTS.values()) * WINDOW_MAX_YEARS * MORTALITY
         * NONQUALIFYING * SWITCH * DELTA_PV)
print(f"\nLargest cell above: ${worst:,.0f}")
print(f"Multiple required to reach $100,000: {100_000/worst:.0f}x")
print("Reaching it needs mortality, cohort, switch rate or the per-case delta")
print("to be wrong by that factor, jointly or singly.")

# --- the same arithmetic run on the OTHER side of the trade ---------------
print("\nFrequency of the harm the advisory exists to prevent (F10), same dials:")
for name, n in COHORTS.items():
    deaths = n * WINDOW_MID_YEARS * MORTALITY
    print(f"  {name:40} {deaths*NONQUALIFYING:8.3f} expected F10 cases over the pilot")
