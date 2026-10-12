# -*- coding: utf-8 -*-
import json
bill = open('bill.md', encoding='utf-8').read()
lines = open('s1424.md', encoding='utf-8').read().split('\n')

def mark(text, subs):
    """subs: list of (find, replace). each must fire exactly once."""
    for f, r in subs:
        assert text.count(f) == 1, ('not unique', f[:70], text.count(f))
        text = text.replace(f, r, 1)
    return text

# --- 1. subsection A final interpretation paragraph (line 31) ---
A = lines[30]
A = mark(A, [(
 "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>",
 "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days. ***For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is deemed to act upon that request, and to last act upon it, on the date on which the Board first acts upon it. Nothing in the preceding sentence determines the date by which the Board is required to act upon a request, to make a determination, or to give a notice or a decision, or whether the Board has performed such a duty within a period required by this section.***</u>")])

# --- 2. definition of "final qualifying retirement date" (line 15) ---
DEF = lines[14]
DEF = mark(DEF, [
 ("within the period this definition allows for acting upon it",
  "within the period ~~this definition allows~~ **allowed by this section** for acting upon it"),
 ("no later than 15 days after it acts upon the request.",
  "no later than 15 days after ~~it acts upon~~ ***it gives its decision upon*** the request."),
])

# --- 3. subdivision D 1 (line 37) ---
D1 = lines[36]
D1 = mark(D1, [
 ("any notice of a date required by that definition upon the Board's action upon a request",
  "any notice of a date required by that definition ~~upon~~ **by reason of** the Board's action upon a request"),
])

# --- 4. subdivision G 2 (line 57) ---
G2 = lines[56]
G2 = mark(G2, [
 ("or has not given it within 60 days after the determination date, the determination takes effect on the first day",
  "or has not given it within 60 days after the determination date, **or where the determination could not take effect within 120 days after the determination date consistently with the sentence of this subdivision that requires notice to be given no less than 30 days before the determination takes effect,** the determination takes effect on the first day"),
])

# --- 5. G 4 suspension and pendency passage ---
s = bill.find('The Board shall not make a determination under subdivision 2, and shall not give the notice required by subdivision 2, while an application')
k = 'such a request is pending from the date on which the member files it until the date on which the Board first acts upon it.'
e = bill.find(k, s) + len(k)
G4 = bill[s:e].replace('’', "'")   # apostrophes normalised, per §8
G4 = mark(G4, [
 ("within the period allowed to it for acting upon the request shall not extend that aggregate",
  "within the period ~~allowed to it~~ **allowed by this section** for acting upon the request shall not extend that aggregate"),
])

# --- 6. subsection M 1, 2, 3 (lines 83, 85, 87) ---
M1, M2, M3 = lines[82], lines[84], lines[86]
M2 = mark(M2, [
 ("until 30 days after the Board acts upon the request, except that (i)",
  "until **the later of (a)** 30 days after the Board acts upon the request **and (b) 30 days after the Board gives the person who filed the request written notice of its decision upon the request, and in no case later than 48 days after the Board acts upon the request**, except that (i)"),
 ("excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request",
  "excluding any period after the expiration of ~~the 90 days allowed by this subsection~~ **the period allowed by this section for acting upon the request** and before the Board acts upon the request"),
 ("retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request",
  "retains its filing date for the purposes of subdivisions D 4 and D 5 until ***30 days after*** the Board acts upon the request"),
])

out = {'A': A, 'DEF': DEF, 'D1': D1, 'G2': G2, 'G4': G4, 'M1': M1, 'M2': M2, 'M3': M3}
json.dump(out, open('repro.json','w'), ensure_ascii=False)
for k2, v in out.items():
    print(k2, len(v))
