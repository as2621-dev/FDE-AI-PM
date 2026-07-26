---
title: Counting re-sends of a tool result — the off-by-one that survives review
tags: [cost, arithmetic, tokens, agent-loop, course-day, rule-b]
problem_type: convention
symptoms: A worked cost derivation that looks right, passes the gate, and is one pass too high.
date: 2026-07-26
---

Any day that derives token cost across loop passes needs this stated once, because the
mistake is invisible on reading and an interviewer would catch it.

**A result produced at pass *N* of a run capped at *C* is re-sent on passes *N+1* through
*C* — that is `C − N` re-sends, not `C − N + 1`.** The pass that produced the result already
paid for the request that caused it; the result only enters the prompt from the *next* pass
onward. Day 2 shipped `C − N + 1` in draft (pass 5 of 10 → "six remaining passes",
150,000 tokens, 75 cents) and the adversarial-interviewer reviewer caught it twice, in the
body and in the duplicated §10 answer. Correct: five re-sends, 125,000 tokens, ~63 cents.

Two habits that would have caught it earlier:

- **Write the index range, not the count.** "Re-sent on passes 6–10" makes the arithmetic
  self-checking in a way "six remaining passes" never does.
- **Grep for the number before you finish.** Any figure quoted in the body and again in §8
  or §10 has to be fixed in every place, and the duplicate is where a correction gets missed.

**Related trap in the same derivation:** a threshold justified by dividing the context window
across passes flips sign with the model's window. Day 2's response-budget method concluded
"the window isn't binding" from Opus 5's 1M window, and the identical sum on a 200,000-token
model lands *below* Anthropic's own 25,000-token default — reversing the conclusion. When a
Rule B method depends on a model spec, work the small case too and say which side of the
threshold each lands on. See [[sourcing-traps-for-course-days]].
