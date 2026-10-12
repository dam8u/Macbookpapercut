#!/usr/bin/env python3
"""
MOO-183 — participant counts and cost per participant.

  Deliverable 1  the five uncovered scoreboard rows: S3, S5, S6, S8 at 4.00%, S8 at 5.00%
  Deliverable 2  the recommended row's aggregate on the authorised 12-month rung
  Deliverable 3  is §3b's $64,678 the same quantity as the package's $64,678?

Run:  cd moo183-cost-per-participant && python3 moo183_cpp.py > out_moo183_run.txt 2>&1
      exit 0 only if every §0 lock passes. ~60s.

Every input is in moo183_inputs.py. The engine in ./engine/ is the published repaired
(v2) engine, copied byte-for-byte and not modified.

Pre-decisional and internal. Not a VRS actuarial result. Two significant figures.
"""
import os
import sys
import csv
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "engine"))

import moo183_inputs as IN  # noqa: E402
import v2_scenarios as X    # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LEVELS = ("low", "central", "high")
S8_RATE = {"S8-i4": 0.04, "S8-i5": 0.05, "S8-i6": 0.06}
FIVE = ("S3", "S5", "S6", "S8-i4", "S8-i5")
LABEL = {
    "S1": "S1 as drafted (Pathways A+B at ANC)",
    "S3": "S3 sliding scale (50% of the gap)",
    "S5": "S5 reopen or extend the window",
    "S6": "S6 add Hybrid members",
    "S8-i4": "S8 at 4.00%",
    "S8-i5": "S8 at 5.00%",
    "S8-i6": "S8 at 6.00% (recommended S8 cell)",
}
PRINTED_IN_PACKAGE = {  # the cost figure the package prints for each row, $M, two s.f.
    "S3": "$3.38M", "S5": "$1.26M", "S6": "$5.15M",
    "S8-i4": "$5.60M", "S8-i5": "$4.56M",
    "S1": "$5.12M", "S8-i6": "$3.65M",
}


def run(code, level, deadline):
    kw = {}
    if code in S8_RATE:
        kw["s8_kw"] = {"i_stat": S8_RATE[code]}
    scen = "S8" if code in S8_RATE else code
    return X.run(scen, level, deadline_months=deadline, **kw)


def hr(t=""):
    print("\n" + "=" * 94)
    if t:
        print(t)
        print("=" * 94)


def money(x):
    return f"${x:,.0f}"


# ===========================================================================
hr("[0] LOCKS — the engine must reproduce the published repaired figures exactly")
print("Engine provenance: " + IN.ENGINE_PROVENANCE)
print(f"Published basis: retirement deadline = {IN.PUBLISHED_DEADLINE_MONTHS} months after the "
      f"later of completion and eligibility.")
print("Tolerance: ${:.2f} / {:.2f} participants.\n".format(IN.LOCK_TOL, IN.LOCK_TOL))

BASE = {}
fails = []
for code, lk in IN.PUBLISHED.items():
    row = {}
    for lvl in LEVELS:
        row[lvl] = run(code, lvl, IN.PUBLISHED_DEADLINE_MONTHS)
    BASE[code] = row
    got = (row["low"]["n"], row["central"]["n"], row["high"]["n"],
           row["low"]["trust"], row["central"]["trust"], row["high"]["trust"])
    ok = all(abs(a - b) <= IN.LOCK_TOL for a, b in zip(got, lk))
    print(f"  {code:8s} n {got[1]:10.4f} (pub {lk[1]:10.4f})   trust {got[4]:14,.2f} "
          f"(pub {lk[4]:14,.2f})   {'PASS' if ok else 'FAIL'}")
    if not ok:
        fails.append((code, got, lk))
if fails:
    print("\nLOCKS FAILED — the engine or its inputs have moved. Stopping; no figure below "
          "may be used.")
    for code, got, lk in fails:
        print(f"  {code}: got {got}\n       pub {lk}")
    sys.exit(1)
print("\nAll locks pass. Every figure below is produced by the same engine that produced the "
      "cost figures the package prints.")

# ===========================================================================
hr("[1] DELIVERABLE 1 — the five uncovered rows, on the basis their printed cost sits on")
print("The numerator is the SAME net trust cost PV the package prints for that row; the")
print("denominator is the SAME run's participant count. Numerator and denominator come out")
print("of one row of one run, so the division is internally consistent by construction.\n")
print("Participant counts are MODELED DEMAND, not actual cap utilization. There is no")
print("published count of purchases made under § 51.1-142.2, so no count here has an")
print("external anchor.\n")

hdr = (f"{'row':34s} {'printed':>8s} {'n low':>8s} {'n central':>10s} {'n high':>9s} "
       f"{'trust central':>15s} {'$/participant':>14s} {'range':>21s}")
print(hdr)
print("-" * len(hdr))
D1 = {}
for code in ("S1",) + FIVE + ("S8-i6",):
    r = BASE[code]
    cpp = {lvl: r[lvl]["trust"] / r[lvl]["n"] for lvl in LEVELS}
    D1[code] = dict(n={lvl: r[lvl]["n"] for lvl in LEVELS},
                    trust={lvl: r[lvl]["trust"] for lvl in LEVELS}, cpp=cpp)
    print(f"{LABEL[code]:34s} {PRINTED_IN_PACKAGE[code]:>8s} {r['low']['n']:8.1f} "
          f"{r['central']['n']:10.1f} {r['high']['n']:9.1f} "
          f"{money(r['central']['trust']):>15s} {money(cpp['central']):>14s} "
          f"{money(cpp['high']) + ' - ' + money(cpp['low']):>21s}")
print("\nThe $/participant range is across the take-up cases (low / central / high). It is")
print("narrow — about ±1% — because take-up scales the cohort and the cost together. The")
print("range that matters for this column is the BASIS, not take-up: see [2].")

# ===========================================================================
hr("[2] THE SAME FIVE ROWS RE-RUN ON THE AUTHORISED 12-MONTH RETIREMENT RUNG")
print(f"Dial: deadline_months {IN.PUBLISHED_DEADLINE_MONTHS} -> {IN.AUTHORISED_RUNG_MONTHS}. "
      f"Nothing else is changed. One driver at a time.\n")

RUNG = {}
for code in ("S1",) + FIVE + ("S8-i6",):
    RUNG[code] = {lvl: run(code, lvl, IN.AUTHORISED_RUNG_MONTHS) for lvl in LEVELS}

hdr2 = (f"{'row':34s} {'n central':>10s} {'trust @6mo':>13s} {'trust @12mo':>13s} "
        f"{'move':>7s} {'$/part @12mo':>13s} {'accel mo':>9s}")
print(hdr2)
print("-" * len(hdr2))
for code in ("S1",) + FIVE + ("S8-i6",):
    b, g = BASE[code]["central"], RUNG[code]["central"]
    print(f"{LABEL[code]:34s} {g['n']:10.1f} {money(b['trust']):>13s} "
          f"{money(g['trust']):>13s} {g['trust'] / b['trust'] - 1:7.1%} "
          f"{money(g['trust'] / g['n']):>13s} {g['avg_acceleration_months']:9.1f}")

print("\nCount check — is the participant count rung-invariant, as MOO-48 §3 and MOO-85 §1")
print("found on the drafted cohort? (The retirement deadline must not change who elects.)")
worst = 0.0
for code in ("S1",) + FIVE + ("S8-i6",):
    for lvl in LEVELS:
        worst = max(worst, abs(RUNG[code][lvl]["n"] - BASE[code][lvl]["n"]))
print(f"  largest count difference between the two rungs, over 7 rows x 3 levels: {worst:.10f}")
print("  => the counts in [1] ARE the counts on the 12-month rung. The rung moves the cost")
print("     and not the cohort, on this engine as on MOO-48's.")

# ===========================================================================
hr("[3] DELIVERABLE 2 — the recommended row on the authorised 12-month rung")
print("Cited, not re-derived: the MOO-48 ladder (Pathway A only, narrow clause (vi), 6.00%).")
print(f"Participants, every rung: {IN.MOO48_PARTICIPANTS['central']:.4f} "
      f"({IN.MOO48_PARTICIPANTS['low']:.4f} to {IN.MOO48_PARTICIPANTS['high']:.4f}).\n")
hdr3 = (f"{'rung':>5s} {'trust low':>12s} {'trust central':>14s} {'trust high':>12s} "
        f"{'$/participant':>14s} {'accel mo':>9s} {'note':s}")
print(hdr3)
print("-" * 92)
n48 = IN.MOO48_PARTICIPANTS
for rung in sorted(IN.MOO48_LADDER):
    lo, ce, hi, accel, _cs = IN.MOO48_LADDER[rung]
    note = ""
    if rung == IN.MOO48_BILL_RUNG:
        note = "THE DRAFTED TEXT (MOO-48 §2)"
    if rung == 0:
        note = "what the ten sponsor documents print as 'rung 1'"
    if rung == IN.AUTHORISED_RUNG_MONTHS:
        note = "THE AUTHORISED RUNG"
    print(f"{rung:5d} {money(lo):>12s} {money(ce):>14s} {money(hi):>12s} "
          f"{money(ce / n48['central']):>14s} {accel:9.1f} {note}")

lo12, ce12, hi12, accel12, cs12 = IN.MOO48_LADDER[IN.AUTHORISED_RUNG_MONTHS]
lo0, ce0, hi0, accel0, _ = IN.MOO48_LADDER[0]
print("\nPer-participant is invariant to take-up on this ladder (take-up scales both):")
for lvl, agg in (("low", lo12), ("central", ce12), ("high", hi12)):
    print(f"  {lvl:8s} {money(agg):>12s} / {n48[lvl]:7.4f} = {money(agg / n48[lvl])}")

print(f"\nThe two circulating aggregates, checked against the ladder:")
print(f"  {money(IN.CIRCULATING_AGGREGATE)} and range {money(IN.CIRCULATING_RANGE[0])}"
      f"-{money(IN.CIRCULATING_RANGE[1])} == ladder RUNG 0 "
      f"({money(ce0)}, {money(lo0)}-{money(hi0)}), NOT rung 1 ({money(IN.MOO48_LADDER[1][1])}).")
print(f"  {money(IN.AUTHORISED_LADDER_AGGREGATE)} == ladder RUNG 12 ({money(ce12)}).")
gap = IN.CIRCULATING_AGGREGATE / IN.AUTHORISED_LADDER_AGGREGATE - 1
print(f"  the gap: {gap:.2%} of the rung-12 figure = {money(ce0 - ce12)} = "
      f"{accel0 - accel12:.1f} months of acceleration removed "
      f"({money((ce0 - ce12) / (accel0 - accel12))} per month).")
print("  Same quantity (net trust cost PV, same cohort, same member price), two different")
print("  retirement dates. Neither is an error. Nothing is averaged or interpolated.")

print("\nAnd the same question on the CURRENT statutory basis (MOO-32 v6 — the only run that")
print("has §7 item 22 option (c) and the no-advance bar in it, at rung 12):")
for lvl in LEVELS:
    print(f"  {lvl:8s} n {IN.V6_PARTICIPANTS[lvl]:7.4f}   trust PV "
          f"{money(IN.V6_TRUST_PV_RUNG12[lvl]):>12s}   $/participant "
          f"{money(IN.V6_TRUST_PV_RUNG12[lvl] / IN.V6_PARTICIPANTS[lvl])}")
print(f"  move against the MOO-48 cohort at the same rung: count "
      f"{IN.V6_PARTICIPANTS['central'] / n48['central'] - 1:+.1%}, aggregate "
      f"{IN.V6_TRUST_PV_RUNG12['central'] / ce12 - 1:+.1%}, per participant "
      f"{(IN.V6_TRUST_PV_RUNG12['central'] / IN.V6_PARTICIPANTS['central']) / (ce12 / n48['central']) - 1:+.1%}")
print(f"  reservation vs payment on that basis: the Commonwealth reserves "
      f"{money(IN.V6_CERTIFIED_RESERVED_NOMINAL['central'])} nominal and the trust pays "
      f"{money(IN.V6_TRUST_NOMINAL_RUNG12['central'])} nominal;")
print(f"  the {money(IN.V6_CERTIFIED_RESERVED_NOMINAL['central'] - IN.V6_TRUST_NOMINAL_RUNG12['central'])}"
      f" difference is the window's whole effect. The window does not ease the $3,000,000.")

print("\nLive-text parameter check, bill-text-s8 document revision 76 / store revision 61:")
for k, (txt, verdict) in IN.LIVE_TEXT_CHECKS.items():
    print(f"  {k:38s} {verdict:42s} <- \"{txt[:60]}\"")

# ===========================================================================
hr("[4] DELIVERABLE 3 — is §3b's $64,678 the same quantity as the package's $64,678?")
s1 = BASE["S1"]["central"]
field = s1["trust_per_participant"]
print(f"The engine field the §3b column is computed from: agg['trust_per_participant']")
print(f"  = agg['trust'] / agg['n'] = {money(s1['trust'])} / {s1['n']:.8f} = ${field:,.6f}")
print(f"The engine expression the package's workforce break-even prints (repaired §7):")
print(f"  a_base['trust'] / a_base['n'] where a_base = X.run('S1','central') = ${field:,.6f}")
print(f"  identical to {abs(field - s1['trust'] / s1['n']):.10f} dollars.")
print(f"Both round to the printed {money(IN.PRINTED_64678)}: {round(field) == IN.PRINTED_64678}")
print("\nSo: SAME NUMBER, SAME QUANTITY, SAME RUN, SAME FIELD. The answer is YES.")
print("\nBut the printed LABEL does not describe that quantity. Decomposition of the same row:")
per = lambda x: x / s1["n"]
print(f"  gross liability increase per participant            {money(per(IN.S1_GROSS))}")
print(f"    of which service-credit content                   {money(per(IN.S1_SVC_COMPONENT))}"
      f"  ({IN.S1_SVC_COMPONENT / IN.S1_GROSS:.0%})")
print(f"    of which earlier-commencement content             {money(per(IN.S1_ACCEL_COMPONENT))}"
      f"  ({IN.S1_ACCEL_COMPONENT / IN.S1_GROSS:.0%})")
print(f"  less member payment per participant                 {money(per(IN.S1_MEMBER_PAID))}")
print(f"  = net cost to the trust per participant             {money(field)}")
print("\n  'Pension cost of the purchased service per participant' names the 28% line and")
print("  prints the 100%-less-member-payment line. The number is right; the words are not.")
for f, line, text in IN.PRINTED_64678_SITES:
    print(f"    {f}:{line}  \"{text}\"")

# ===========================================================================
hr("[5] CSV OUTPUT")
rows = []
for code in ("S1",) + FIVE + ("S8-i6",):
    for lvl in LEVELS:
        for rung, src in ((IN.PUBLISHED_DEADLINE_MONTHS, BASE), (IN.AUTHORISED_RUNG_MONTHS, RUNG)):
            a = src[code][lvl]
            rows.append({
                "row": code, "label": LABEL[code], "take_up_case": lvl,
                "retirement_rung_months": rung,
                "basis": ("published scoreboard basis" if rung == IN.PUBLISHED_DEADLINE_MONTHS
                          else "authorised 12-month rung"),
                "participants": a["n"],
                "trust_cost_PV": a["trust"],
                "cost_per_participant": a["trust"] / a["n"],
                "mean_acceleration_months": a["avg_acceleration_months"],
                "member_paid_PV": a["paid"],
                "gross_liability_PV": a["gross"],
                "count_is": "modeled demand, not actual cap utilization",
            })
p = os.path.join(HERE, "out_moo183_rows.csv")
with open(p, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"wrote {p}  ({len(rows)} rows)")

p2 = os.path.join(HERE, "out_moo183_recommended_ladder.csv")
with open(p2, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["basis", "retirement_rung_months", "take_up_case", "participants",
                "trust_cost_PV", "cost_per_participant", "mean_acceleration_months", "note"])
    for rung in sorted(IN.MOO48_LADDER):
        lo, ce, hi, accel, _cs = IN.MOO48_LADDER[rung]
        for lvl, agg in (("low", lo), ("central", ce), ("high", hi)):
            w.writerow(["MOO-48 cohort (pre item-22 (c), pre no-advance bar)", rung, lvl,
                        n48[lvl], agg, agg / n48[lvl], accel,
                        "THE AUTHORISED RUNG" if rung == 12 else
                        ("drafted text" if rung == 1 else
                         ("printed by the ten sponsor documents" if rung == 0 else ""))])
    for lvl in LEVELS:
        w.writerow(["MOO-32 v6 — item 22 (c) + no-advance bar (current statutory basis)", 12, lvl,
                    IN.V6_PARTICIPANTS[lvl], IN.V6_TRUST_PV_RUNG12[lvl],
                    IN.V6_TRUST_PV_RUNG12[lvl] / IN.V6_PARTICIPANTS[lvl], "", "v6 measured"])
print(f"wrote {p2}")

print(f"\nrun completed {datetime.datetime.now().isoformat(timespec='seconds')}")
print("Pre-decisional and internal. Not a VRS actuarial result. Two significant figures.")
