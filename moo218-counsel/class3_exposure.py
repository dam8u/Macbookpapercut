#!/usr/bin/env python3
"""MOO-218 -- Red Team working file. Exposure of C16's residual class 3.

Reads the AUTHORISED figure set from moo199-authorised-export/out_moo199_model_data.json
(read-only; no team file is modified). The MOO-199/MOO-183 engine has NO disability
channel -- see its own caveat that the figures exclude "disability or death-in-service,
which understates cost" -- so this script does not rerun their model. It layers a
decomposition on top of their measured participant counts and certified reservations.

Every p-value below is MY assumption, labelled as such. None is measured.
"""
import json

M = json.load(open('moo199-authorised-export/out_moo199_model_data.json'))['headline']
CAP_AGG, CAP_ELECTION = 3_000_000, 170_000

N   = M['participants']                      # measured (modeled demand)
RES = M['certified_reserved_nominal']         # measured
mean_subsidy = RES['central'] / N['central']  # nominal certified subsidy per participant

# Decomposition of the path into class 3, four-year pilot from 1 July 2029.
# p2: does not retire in a qualifying retirement, so a G 2 or G 3 determination is MADE
# p3: approved for disability AFTER that determination took effect (conditional on p2,
#     which selects FOR ill health, so this is far above the VRS base rate)
# p4: application filed >90 days after termination, so an A/B waiver is REQUIRED
# p5: waiver granted on discretionary good cause under H's FIRST sentence with NO
#     clause (ii) Medical Board certification  (H's SECOND sentence REQUIRES the
#     waiver once the Medical Board certifies -- that route is class 2, already cured)
SCEN = {
    'central':     dict(n=N['central'], p2=.15, p3=.15, p4=.20, p5=.50),
    'pessimistic': dict(n=N['high'],    p2=.25, p3=.30, p4=.30, p5=.70),
    'absurd_ceiling': dict(n=N['high'], p2=1.,  p3=1.,  p4=1.,  p5=1.),
}

print(f"measured: participants central {N['central']:.4f}  high {N['high']:.4f}")
print(f"measured: certified reserved nominal central ${RES['central']:,.0f}  high ${RES['high']:,.0f}")
print(f"derived : mean certified subsidy per participant ${mean_subsidy:,.0f} "
      f"({mean_subsidy/CAP_ELECTION:.1%} of the ${CAP_ELECTION:,} per-election cap)")
print(f"measured: cap utilisation at ${CAP_AGG:,} -- central {M['cap_utilisation']['central']:.4f}, "
      f"high {M['cap_utilisation']['high']:.4f}")
print(f"derived : central headroom ${CAP_AGG*(1-M['cap_utilisation']['central']):,.0f}; "
      f"high OVERSHOOT ${CAP_AGG*(M['cap_utilisation']['high']-1):,.0f}\n")

for name, s in SCEN.items():
    cnt = s['n'] * s['p2'] * s['p3'] * s['p4'] * s['p5']
    print(f"{name:16s} expected class-3 members over the 4-year pilot: {cnt:.4f}")
    print(f"{'':16s}   value of the EXCLUSION at the mean subsidy : ${cnt*mean_subsidy:,.0f}")
    print(f"{'':16s}   value of the EXCLUSION at the election cap  : ${cnt*CAP_ELECTION:,.0f}")
    print(f"{'':16s}   as a share of central certified reservations : "
          f"{cnt*mean_subsidy/RES['central']:.3%}")


# ---------------------------------------------------------------------------
# M-2: the two readings of G 2 clause (i), "the member's payments".
# Illustrative figures, not model output. Shows that the member's cost per
# retained month is the SAME on both readings and that the mismatch falls on
# the state agency -- which is why M-2 is framed in months, not dollars.
def m2(std=5000, member=60000, agency=20000):
    total = member + agency
    harsh = member // std
    ex = total - harsh * std
    rm, ra = ex * member / total, ex * agency / total
    mild = total // std
    print(f"\nM-2  std ${std:,}/mo, member ${member:,}, agency ${agency:,}")
    print(f"  harsher: {harsh} mo; refund member ${rm:,.0f} agency ${ra:,.0f}; "
          f"member net ${member-rm:,.0f} = ${(member-rm)/harsh:,.0f}/mo; "
          f"agency net ${agency-ra:,.0f} buys 0 extra months")
    print(f"  milder : {mild} mo; no refund; member net ${member:,.0f} = ${member/mild:,.0f}/mo")
    print(f"  swing  : {mild-harsh} months of creditable service")

m2()
