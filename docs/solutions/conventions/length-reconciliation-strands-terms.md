---
title: Cutting a day to fit the gate strands terms and breaks promises
tags: [word-count, check_day, rule-a, vocabulary, course-day, gate-blind-spot, editing]
problem_type: convention
symptoms: Gate goes green on length, and the day now uses its own title word without defining it.
date: 2026-07-26
---

Day 3 came in at 11,307 prose words against a 10,000 hard ceiling and a 9,000 target.
Getting it down took eleven passes and produced two failure modes worth knowing about
before the next day is written.

**1. Rewriting to shorten does not shorten. Deleting does.** Eleven compression passes
that reworded sentences averaged **−60 words each** — repeatedly a tenth of what the
edit looked like it would save, because a tightened sentence is still a sentence. The
passes that actually moved the number deleted whole units: a §8 interview pair (−200),
a §6 table row (−80), a §9 vocabulary row (−28 each), a Tier 3 subsection folded into
its neighbour (−110). Budget by *units you are willing to lose*, not by adjectives you
are willing to cut. Corollary: decide the deletions **before** the first draft goes
long, because deciding them at 10,300 words means choosing under pressure.

**Reproduced on Day 6, independently and to within one word.** A first draft of 11,087 against the
same 10,000 ceiling came down to 9,715 in eight passes. **The two passes that deleted units gave 67%
of the saving; the six compression passes averaged −59 words each.** That is this note's own −60
figure, measured again by a different writer on a different day, which makes it a rule rather than an
anecdote: *compression is not a length tool in this format. It is a quality tool that happens to save
a rounding error.* Day 6's largest single win was deleting a Tier 2 passage that restated the content
of its own diagram — so the first place to look for a unit is prose that duplicates a figure you
already drew.

**2. Length cuts strand terms, and the gate cannot see it.** `check_day.py` enforces a
minimum of 3 vocabulary rows, so deleting §9 rows to save words passes cleanly. Five
rows went in the reconciliation, and two of those terms — `least privilege` and
`guardrail`, the day's own title word — were then used throughout a day that no longer
defined them anywhere. Rule A caught it only because `d23e011` landed mid-slice and
added "open `GLOSSARY.md` and confirm the entry is actually there."

Run this after any length edit that touches §9, before committing:

```sh
python3 - <<'PY'
import re,sys; sys.path.insert(0,'evals')
from check_day import split_frontmatter, section_body
day=open('course/day-NN-slug/README.md',encoding='utf-8').read()
_,b=split_frontmatter(day); v=section_body(b,'## 9. Vocabulary')
gl=open('course/GLOSSARY.md',encoding='utf-8').read()
for t in ['<every term the day leans on>']:
    ok = (re.search(r'\|\s*\*\*[^|]*'+re.escape(t), v+gl, re.I)
          or re.search(r'\*\*'+re.escape(t)+r'[a-z]*\*\*', b, re.I))
    print(('ok   ' if ok else 'UNDEF'), t)
PY
```

**3. Deleting a list item breaks a promise three lines above it.** Cutting the
`LLM07:2025 System Prompt Leakage` bullet left "**Three things worth catching:**"
followed by two. Nothing checks that. Grep your own numeric promises — "three", "two
kinds", "four places", "five of the seven" — against what follows them, every time you
delete a bullet or a row.

**4. Your own count claims rot the same way.** §6 said "Four of those seven rows are
cases where every check reported success" and a reviewer could not reproduce the four.
Naming them ("the CRM field, the guardrail that was only advice, the service that
failed open, and the exfiltration with no action") is shorter than defending the
arithmetic, and it survives a row being deleted later.

**Also worth keeping:** the 9,000–10,000 band is not free. Landing there costs a
justification the style guide demands, and it leaves no room to absorb review findings —
Day 3 passed at 9,979 with 21 words of headroom, then the review panel's fixes added
453 words and the day failed the gate again. **Reserve ~400 words before review, not
after.** Reviewers on a from-zero day reliably find missing definitions and missing
worked examples, and both cost words.
