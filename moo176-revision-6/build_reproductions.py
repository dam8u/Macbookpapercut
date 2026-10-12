# -*- coding: utf-8 -*-
import os, re
S = os.environ["PAPERCLIP_RUN_SCRATCH_DIR"]
base = open(f"{S}/base.md").read()
a = base.index("## 1. The bill"); b = base.index("## 2. Section-by-section")
s1 = base[a:b]; L = s1.split("\n")

A_INTERP = L[107]; FQRD = L[91]; M1 = L[159]; M2 = L[161]; M3 = L[163]; D3 = L[117]
G4 = L[137]; D1 = L[113]
g4_a = G4.index("The Board shall not make a determination under subdivision 2, and shall not give the notice required by subdivision 2, while an application")
g4_k = "and such a request is pending from the date on which the member files it until the date on which the Board first acts upon it."
G4P = G4[g4_a:G4.index(g4_k)+len(g4_k)]
d1_a = D1.index("Where the Board gives that written statement")
d1_k = "and the Board shall state every such delay in the report required by subsection J."
D1P = D1[d1_a:D1.index(d1_k)+len(d1_k)]

# ---- the three edits, as applied for revision 6 ----------------------------
E1_FIND = "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"
E1_NEW  = (" For the purposes of this section and of subdivision B 4 f of § 51.1-142.2, where a period begins or "
           "ends upon, or is measured from, the Board's acting, or last acting, upon a request, or where a date is "
           "fixed by reference to the month in which the Board acts, or last acts, upon a request, the Board is "
           "deemed to act upon that request, and to last act upon it, on the date on which the Board first acts "
           "upon it. Nothing in the preceding sentence determines the date by which the Board is required to act "
           "upon a request, to make a determination, or to give a notice or a decision, or whether the Board has "
           "performed such a duty within a period required by this section.")
E2_OLD = "it acts upon"; E2_NEW = "it gives its decision upon"
E2_FIND = "it shall give the member written notice of that date no later than 15 days after it acts upon the request."
E3_FIND = "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"
E3_READ = "retains its filing date for the purposes of subdivisions D 4 and D 5 until 120 days after the Board acts upon the request"

# markup: patch additions bolded, deletions struck, inside the bill's own <u> wrapper
rep_A = A_INTERP.replace("three days.</u>", "three days." + "**" + E1_NEW.strip() + "**</u>")
assert rep_A.count("**")==2
rep_FQRD = FQRD.replace(E2_FIND, "it shall give the member written notice of that date no later than 15 days after ~~it acts upon~~ **it gives its decision upon** the request.")
assert "~~" in rep_FQRD
rep_M2 = M2.replace(E3_FIND, "retains its filing date for the purposes of subdivisions D 4 and D 5 until **120 days after** the Board acts upon the request")
assert "**120 days after**" in rep_M2

out = dict(A=rep_A, FQRD=rep_FQRD, M1=M1, M2=rep_M2, M3=M3, D3=D3, G4=G4P, D1=D1P)
for k,v in out.items():
    open(f"{S}/cut/rep_{k}.txt","w").write(v)
    print(k, len(v))
