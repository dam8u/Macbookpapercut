# -*- coding: utf-8 -*-
import json, re, sys
bill = open('bill.md', encoding='utf-8').read()

# ---- the three MOO-162 (revision 5) edits, to build the post-patch base ----
M162 = [
 ("E1",
  "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>",
  "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.</u>"),
 ("E2",
  "it shall give the member written notice of that date no later than 15 days after it acts upon the request.",
  "it shall give the member written notice of that date no later than 15 days after it gives its decision upon the request."),
 ("E3",
  "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request",
  "retains its filing date for the purposes of subdivisions D 4 and D 5 until 30 days after the Board acts upon the request"),
]
print("=== MOO-162 revision 5 FIND counts in live store revision 61 ===")
patched = bill
ok = True
for tag, f, r in M162:
    c = bill.count(f)
    print(f"  {tag}: {c}")
    if c != 1: ok = False
    patched = patched.replace(f, r, 1)
print("  all three resolve exactly once:", ok)
print("  patched length:", len(patched), " delta:", len(patched)-len(bill))

# ---- MOO-164 edits ----
EDITS = [
 ("A  Q1 anchor (subsec A interp para opening)",
  "<u>For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, a written statement or notice required of the Board is given on the date the Board mails it"),
 ("B  card (b) M 2 tolling tail",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request"),
 ("C  card (j) M 2 clause (ii)",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request"),
 ("D  card (l)/F-5 R-5 period",
  "within the period this definition allows for acting upon it"),
 ("E  card (k)/F-9 D 1 descriptor",
  "any notice of a date required by that definition upon the Board's action upon a request"),
 ("F  card (h) G 2 exception",
  "except that where the Board gives that notice later than 60 days after the determination date, or has not given it within 60 days after the determination date, the determination takes effect on the first day on which it may take effect under the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect"),
 ("G  card (c-1) G 4 pendency definition",
  "For the purposes of this subdivision an application for a disability retirement allowance is pending from the date on which the member files it until the date on which the Board first acts upon it"),
 ("H  card (c-2) G 2 pending carve-out",
  "and the determination required by this subdivision shall take effect notwithstanding that a retirement allowance has been paid to the member while such an application was pending."),
 ("I  conforming: G 4 period formula",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate"),
]
print("\n=== MOO-164 FIND counts: live base  /  post-MOO-162 base ===")
for tag, f in EDITS:
    print(f"  {tag:46s} {bill.count(f)}  /  {patched.count(f)}")

# ---- apostrophes ----
print("\n=== apostrophe normalisation ===")
curly = [m.start() for m in re.finditer('’', bill)]
print("  curly apostrophes in whole document:", len(curly))
for p in curly:
    print("   ...", bill[p-60:p+40].replace("\n"," "))
print("  straight apostrophes:", bill.count("'"))

# ---- phrase counts that matter ----
print("\n=== counts that matter ===")
for ph in ["acts upon", "last acts upon", "act upon", "acting upon", "action upon",
           "is pending", "was pending", "90 days allowed by this subsection",
           "the period allowed by this section for acting upon",
           "the period allowed to it for acting upon the request",
           "this definition allows for acting upon it"]:
    print(f"  {ph!r:58s} live {bill.count(ph):3d}   patched {patched.count(ph):3d}")
open('patched61.md','w',encoding='utf-8').write(patched)
