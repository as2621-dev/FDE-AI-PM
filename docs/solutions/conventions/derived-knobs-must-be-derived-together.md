---
title: Two Rule B knobs derived independently will contradict each other
tags: [rule-b, arithmetic, course-day, cross-day, compaction, response-budget, review-catch]
problem_type: convention
symptoms: Each day's number checks out on its own page; put both on one run and they are incompatible.
date: 2026-07-26
---

Day 2 derived a response budget. Day 4 derived a compaction trigger that *takes the response
budget as an input*. Both were internally correct. Together they were wrong, and two of three
reviewers found it independently.

**The mistake.** Day 2's method is `(window − base prompt) ÷ passes`, giving 19,700 tokens on
a 200,000-token window over ten passes. Day 4 then wrote "one reply may carry three
`tool_use` blocks" and multiplied: `3 × 19,700 = 59,100`. But Day 2 divided by **passes**, so
19,700 is a per-*pass* allowance. Three results in one pass **share** it. The multiplication
also implied a run consuming 591,000 tokens of a 200,000-token window — impossible on its
face, and nobody noticed for a full draft.

**Three habits that catch this class.**

1. **When you import another day's number, re-read the sentence that derived it, not the
   number.** "19,700 per result" and "19,700 per pass" are the same figure with incompatible
   units, and only the deriving sentence tells you which.
2. **Sanity-check the total.** Multiply your per-pass figure by the pass count and compare it
   to the window. Day 4's variant failed this in one line.
3. **Pick a flip variable that belongs to your own day.** Day 4 wanted the "same formula,
   opposite conclusion" pattern (see [[re-send-arithmetic-off-by-one]]). Flipping on parallel
   tool calls reached into Day 2's derivation and broke it. Flipping on the **output cap** —
   4,000 tokens for an agent that writes tool calls, 32,000 for one that writes a report,
   giving 88% vs 74% of the window — stays inside Day 4 and is just as instructive.

**What to ship when you find an interaction like this.** Do not hide it. Day 4 now states it:
compaction firing means the run continues past the tenth pass, which invalidates the divisor
that produced 19,700 in the first place, so the two numbers must be derived against one
assumed run. That is better teaching than either number alone, and it is the kind of thing an
interviewer probes for.

**Two further arithmetic traps from the same slice.**

- **Do not subtract the same allowance twice.** The trigger is
  `window − tool result − output cap`. The refinement step said "take the 95th-percentile
  *tokens added per pass* from traces" — but tokens-added already contains the model's reply,
  so subtracting the output cap on top double-counts it. Measure **tool-result tokens per
  pass** specifically. All three reviewers flagged this one.
- **A per-pass probability is not a per-run promise.** A 95th-percentile threshold means a 5%
  chance per pass, which over ten passes is `1 − 0.95¹⁰ ≈ 40%` per run. The day originally
  called the per-pass figure "the number you give the customer". Convert before quoting.

**Also worth keeping:** state a threshold as a percentage *and* an absolute, both times. The
gate's `check_unsourced_figures` warns on any paragraph containing `NN%` with no link, so an
arithmetic line like `200,000 − 19,700 − 4,000 = 176,300 tokens, or 88%` warns even though it
is derived in front of the reader — which the style guide's DoD explicitly permits. Expect
that warning and leave it; do not add a decorative citation to silence it.
