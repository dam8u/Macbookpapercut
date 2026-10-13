# -*- coding: utf-8 -*-
"""MOO-208 store revision 72 — in-place record corrections out of MOO-211's counsel pass.

Eight. Each is a DEMONSTRATED ERROR OF FACT in this record — a citation that does not hold, two
character counts, one conforming-amendment column, one claim about what a character delta proves,
and one miscount of the certification series — not a change of position. None touches an enacted
word. None rewrites the original away: the old text stays readable and the correction sits beside
it, marked, in the form store revision 70 established.
"""

# ---- R1 — §5.47 direction 1, row 3's conforming-amendment column (MOO-211 M2) -------------
R1_F = ("**None.** The words are tied to A, so the statement follows A if A is amended instead of "
        "freezing a paraphrase. A's *\"in a manner prescribed by the Board\"* governs the "
        "**manner**, not the **time**")
R1_R = R1_F + (
    " — **CORRECTED, store revision 72: this column does not hold.** "
    "[MOO-211](/MOO/issues/MOO-211) M2. **The citation to A carries the source of the power; it "
    "does not carry the timing.** *\"At any time before the member's death\"* is neither A's "
    "language nor A's content but this drafter's inference, as §6.0-70 item 2 says in terms, so if "
    "A were amended to fix a moment of irrevocability **D 1 would still compel the old "
    "proposition** and the statement would not follow A at all. The *\"Verified\"* column is "
    "sound. **Cured by counsel's S5 saving clause**, § 51.1-162 being in its list — drafted at "
    "+310 and enacted nowhere")

# ---- R2 — §5.47 direction 1, row 7's title authority (MOO-211 M5) --------------------------
R2_F = ("and the *\"relating to\"* clause named none of them. Va. Const. art. IV, § 12; "
        "*Dean v. Paolicelli*, 194 Va. 219 (1952)")
R2_R = ("and the *\"relating to\"* clause named none of them. Va. Const. art. IV, § 12; "
        "**CORRECTED, store revision 72 — the case cited here did not hold and is replaced: "
        "*City of Richmond v. Pace*, 127 Va. 274, 103 S.E. 647 (1920)**, a title being sufficient "
        "if it gives notice of the general subject and of the interests likely to be affected, "
        "unnamed subjects being good if germane or cognate. "
        "[MOO-211](/MOO/issues/MOO-211) M5. *~~Dean v. Paolicelli, 194 Va. 219 (1952)~~* decides "
        "eligibility for state office under art. II, § 32 and special legislation under the 1902 "
        "Constitution's art. IV, § 64 and **has no title holding at all**; it is kept in the file "
        "against the eligibility classifications in subsections B and C, where it is good "
        "authority. **The proposition asserted here is correct Virginia law; only the case was "
        "wrong — and under *Pace* the consequence runs the other way, because T2 was never "
        "constitutionally required**")

# ---- R3 — §6.0-70's T2 item, the same citation (MOO-211 M5) --------------------------------
R3_F = ("while the *\"relating to\"* clause named none of them. Va. Const. art. IV, § 12; "
        "*Dean v. Paolicelli*, 194 Va. 219 (1952) is the authority a reader of the memo will "
        "want.")
R3_R = ("while the *\"relating to\"* clause named none of them. Va. Const. art. IV, § 12; "
        "**CORRECTED, store revision 72: *City of Richmond v. Pace*, 127 Va. 274, 103 S.E. 647 "
        "(1920)** is the authority a reader of the memo will want, and "
        "*~~Dean v. Paolicelli~~* — cited here and at §5.47 row 7 — **has no title holding**. "
        "[MOO-211](/MOO/issues/MOO-211) M5. **Under *Pace* the title need only give notice of the "
        "general subject and of the interests likely to be affected, so T2 was not a save: the "
        "death-benefit provisions were already germane to the stated object, and T2 is simply the "
        "better title.**")

# ---- R4 — §5.47 direction 2, check 9's character count (MOO-211 m2) -----------------------
R4_F = "— 150 characters, **1× in §1**"
R4_R = ("— **151** characters (**corrected in store revision 72**; this check said 150 — "
        "[MOO-211](/MOO/issues/MOO-211) m2), **1× in §1**")

# ---- R5 — §5.47 direction 2, check 10's "arithmetic proof" (MOO-211 §5) -------------------
R5_F = ("**§1 moved by exactly the 634 characters the six substitutions account for, which is the "
        "arithmetic proof that nothing else in §1 changed.**")
R5_R = (
    "**§1 moved by exactly the 634 characters the six substitutions account for.** "
    "~~which is the arithmetic proof that nothing else in §1 changed~~ — **CORRECTED, store "
    "revision 72: that is a checksum and this check called it a proof.** "
    "[MOO-211](/MOO/issues/MOO-211) §5. **Two offsetting changes of equal magnitude pass a "
    "matching delta, and so does any change of exactly zero characters — and §6.0-70 item 4 "
    "records that this revision contains one**, F4's relocation of the series' *\"and\"*, which "
    "is precisely the class of change a delta cannot see. Counsel ran the proof instead: §1 "
    "diffed against the fetched base, **exactly two lines differing** — line 4 the title line at "
    "+44, line 115 subdivision D 1 at +590, no other line in §1 differing — and the character "
    "diff of those two lines reconciles to the six substitutions as −78 −59 −4 +116 +173 +213 "
    "+116 +113 = +590. **The conclusion was right and the method was not. The standing rule from "
    "store revision 72 is a line diff against the fetched base, not a delta assertion**, and the "
    "next kit to write §1 carries it.")

# ---- R6 — §6.0-70 item 2's "tied to A" claim (MOO-211 M2) ---------------------------------
R6_F = ("The words are tied to A so the statement follows A if A is ever amended rather than "
        "freezing a paraphrase;")
R6_R = ("The words are tied to A so the statement follows A if A is ever amended rather than "
        "freezing a paraphrase; **— CORRECTED, store revision 72: that is true of the citation "
        "and not of the timing.** [MOO-211](/MOO/issues/MOO-211) M2. This item is right that the "
        "temporal proposition is **an inference from A's structure and not a quotation**, and it "
        "follows from exactly that that the proposition does **not** track an amendment to A: if "
        "A were amended to fix a moment of irrevocability, D 1 would still compel *\"at any time "
        "before the member's death.\"* **The citation carries the power; it does not carry the "
        "timing.** Counsel's S3 and S5 are the two cures, and neither is enacted;")

# ---- R7 — §6.0-70 item 6, the F3 residue (MOO-211 M1) -------------------------------------
R7_F = "**Recorded, not drafted around, as directed.**"
R7_R = (
    "**Recorded, not drafted around, as directed.** "
    "**— CORRECTED, store revision 72: there is no residue, because this item counted the "
    "propositions wrong.** [MOO-211](/MOO/issues/MOO-211) M1. After F4 and F1/F2/F6/F9, **item 7 "
    "carries one advisory and two propositions of law** — the power to re-designate and the "
    "no-fault clause — so **the certification series carries eight propositions of law and one "
    "advisory, not six and one.** The Director's instruction, *\"the six propositions of law\"*, "
    "is therefore **under-inclusive by two**, and the drafted scope *\"every matter other than "
    "the advice\"* reaches all eight and excepts the one, **which is exactly what the instruction "
    "intended.** The asymmetry this item records — that misstating the re-designation clause or "
    "the no-fault clause would be unreached while omitting them stayed reviewable — **was an "
    "artefact of the miscount and does not arise on the drafted words.** So: **no residue to "
    "cure, no three-way split to consider, and the (i)–(vii) renumbering this commission forbade "
    "is not needed for anything.** Item 133's words stand unchanged and its description is "
    "corrected. **Item 133's own premise is also narrowed by the same pass:** most misstatements "
    "decompose into omissions already inside D 1's failure sentence — including item 133's own "
    "worked example, a template that states the required matter not at all — so **the real F7 gap "
    "is additive misstatement only**, which is rarer than a template rewrite and worth knowing "
    "before 253 characters are spent on it.")

# ---- R8 — the §8 status note for store revision 70, same miscount (MOO-211 M1) -------------
R8_F = ("The instruction was *\"the six propositions of law\"*; the draftable scope is *\"every "
        "matter other than the advice\"*, which reaches the six **and** item 7's other two "
        "propositions. Strict scoping needs the series designated (i) to (vii).")
R8_R = ("The instruction was *\"the six propositions of law\"*; the draftable scope is *\"every "
        "matter other than the advice\"*, which reaches the six **and** item 7's other two "
        "propositions. ~~Strict scoping needs the series designated (i) to (vii).~~ "
        "**CORRECTED, store revision 72 — there is nothing to scope around.** "
        "[MOO-211](/MOO/issues/MOO-211) M1: item 7 carries two propositions of law beside the "
        "advisory, so **the series carries eight and the instruction's \"six\" was under-inclusive "
        "by two.** The drafted scope is exactly right and **no renumbering is needed.**")

# ---- R9 — the §6 self-describing paragraph, so it is not stale the moment this writes -------
R9_F = ("the gaps at §6.0-64 and §6.0-68 are those revisions' silence and not lost notes.**")
R9_R = ("the gaps at §6.0-64, §6.0-68 and §6.0-72 are those revisions' silence and not lost "
        "notes.**")

PATCHES = [
    dict(id="R1", n=1, label="§5.47 row 3's conforming column does not hold (M2)",
         find=R1_F, repl=R1_R),
    dict(id="R2", n=1, label="§5.47 row 7's title authority replaced (M5)", find=R2_F, repl=R2_R),
    dict(id="R3", n=1, label="§6.0-70's T2 item, the same citation (M5)", find=R3_F, repl=R3_R),
    dict(id="R4", n=1, label="§5.47 check 9: 151 characters, not 150 (m2)", find=R4_F, repl=R4_R),
    dict(id="R5", n=1, label="§5.47 check 10: a delta is a checksum, not a proof (§5)",
         find=R5_F, repl=R5_R),
    dict(id="R6", n=1, label="§6.0-70 item 2: the citation carries the power, not the timing (M2)",
         find=R6_F, repl=R6_R),
    dict(id="R7", n=1, label="§6.0-70 item 6: the F3 residue does not exist (M1)",
         find=R7_F, repl=R7_R),
    dict(id="R8", n=1, label="§8's store revision 70 note, the same miscount (M1)",
         find=R8_F, repl=R8_R),
    dict(id="R9", n=1, label="§6's self-description, so it is not stale on arrival",
         find=R9_F, repl=R9_R),
]
