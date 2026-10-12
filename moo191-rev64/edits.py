# -*- coding: utf-8 -*-
"""MOO-191 — the one bill edit of store revision 64.

F10's designation-review advisory, the second limb of [MOO-169](/MOO/issues/MOO-169)'s F10,
approved verbatim by the Policy Director at MOO-188 §3.3. FIND and READ are the Director's own
words and are not touched here.

`n` is the count asserted over the WHOLE document; `n1` the count asserted over enacted §1.
"""

EDITS = []


def E(i, label, find, repl, n=1, n1=1):
    EDITS.append(dict(id=i, label=label, find=find, repl=repl, n=n, n1=n1))


E("64-1", "subdivision D 1 — the designation-review advisory, its own semicolon item after the § 51.1-162 B proposition",
  "where the member has made no designation or the person designated has predeceased the member "
  "and no other designation has been made; that subsection C of § 51.1-162",
  "where the member has made no designation or the person designated has predeceased the member "
  "and no other designation has been made; that the member is advised to review the member's "
  "designation of beneficiary under subsection A of § 51.1-162 before completing payment; "
  "that subsection C of § 51.1-162")

# Anchors this revision must NOT disturb. Counted over §1 before and after the substitution.
# Three MOO-141 / MOO-176 revision 6 FIND strings, and the six MOO-164 act-versus-notice FINDs.
UNTOUCHED = [
 ("MOO-141 Edit 1",
  "every period within which a person may or must act that runs from the giving of that statement or notice is extended by three days.</u>"),
 ("MOO-141 Edit 2",
  "it shall give the member written notice of that date no later than 15 days after it acts upon the request."),
 ("MOO-141 Edit 3 (revision 6, 120 days)",
  "retains its filing date for the purposes of subdivisions D 4 and D 5 until the Board acts upon the request"),
 ("MOO-164 card (b)",
  "tolls the running of the member's final qualifying retirement date and of any period within which the member or applicant must act under this section or under subdivision B 4 f of § 51.1-142.2, until 30 days after the Board acts upon the request"),
 ("MOO-164 card (h)",
  "or has not given it within 60 days after the determination date, the determination takes effect on the first day"),
 ("MOO-164 card (j)",
  "excluding any period after the expiration of the 90 days allowed by this subsection and before the Board acts upon the request"),
 ("MOO-164 F-5",
  "within the period this definition allows for acting upon it"),
 ("MOO-164 F-9",
  "any notice of a date required by that definition upon the Board's action upon a request"),
 ("MOO-164 conforming",
  "a failure of the Board to act upon such a request within the period allowed to it for acting upon the request shall not extend that aggregate"),
]
