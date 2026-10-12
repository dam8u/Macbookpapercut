# -*- coding: utf-8 -*-
src = open('content.py').read()

NEW = '''STUB_S8 = """{PHRASE} moved verbatim** to [`bill-text-s8-revision-history-2`](/MOO/issues/MOO-42#document-bill-text-s8-revision-history-2) **by store revision {REV}**, where a reference of the form *"§8's note for store revision N"* still resolves. §8 retains the five most recent: {KEPT}. **Nothing is rewritten or summarised away, and §1 is untouched by the move.**

"""


def s7stub_block(L, C):
    return """**Store revision {REV} writes into that document too.** {M161}'s counsel pass on store revision 58's eight substitutions returned **1 fatal, 9 serious, 6 moderate and 4 minor findings, and 12 null results**. Eight of its findings are enacted in §1 by this revision, two are declined with reasons at §{S6}, and **seven are drafted in full and enacted nowhere** — they are **§7 item {ITEM}**, written in that document. The same revision enacts **five of the nine answers at §7 item 122**, which the Policy Director selected on 12 October 2026; item 122 is marked there with what was enacted and what stays open. This document carries the narrative at §0.0-{REV}, the sweep at §{S5} and the drafter's note at §{S6}.

""".format(REV=L["REV"], S5=L["S5"], S6=L["S6"], ITEM=L["ITEM"], M161=M161)


'''

i = src.index('STUB_S8 = """')
j = src.index('# Substitutions outside §1')
src = src[:i] + NEW + src[j:]

old_tail = 'All of them, drafted, at §7 item {ITEM}.'
new_tail = ('All of them, drafted, at §7 item {ITEM} — which since store revision 59 lives in '
            '[`bill-text-s8-item-list`](/MOO/issues/MOO-42#document-bill-text-s8-item-list), '
            'where a reference of the form *“§7 item n”* resolves.')
assert src.count(old_tail) == 1
src = src.replace(old_tail, new_tail)
open('content.py', 'w').write(src)
print('content.py patched')
