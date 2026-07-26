---
tags: [handoff, review-panel, reports, overclaim]
problem_type: process
symptoms:
  - "the next day inherited a claim its predecessor had already fixed"
  - "a review panel caught the same defect twice, one day apart"
  - "the day is right and the report summarising it is wrong"
---

# Correct the report, not just the day

**A day's report is the specification the next day builds against.** So a claim corrected
in the day has to be corrected in the report too, or the next writer builds on the version
that was already known to be wrong.

## The instance

Day 6's review panel caught its headline sentence claiming that at 120 invoices a day
"no amount of tuning the design gets there" — false, because its own move 2 (design the
approval screen, lowering *t*) reaches the ceiling. **Day 6 fixed the day and then wrote
the uncorrected claim into its report.** The orchestrator's brief for Day 7 was built from
that report, so Day 7's first draft said the minutes ceiling is one "which no design change
reaches" — the same false claim, one day later, in a different day. Day 7's Reviewer 2
caught it independently.

Day 5 hit the same class from the other direction: a paragraph deleted during its length
recovery left its report describing content that no longer shipped.

## Why it is easy to miss

The panel reviews the **diff**, and the report is usually already committed by then — so
the report is outside the thing being reviewed. Every incentive points at fixing the
artefact the reviewer complained about and stopping there.

## What to do

When a panel finding changes a claim, **grep your own report for the claim before you
commit the fixes.** Specifically:

1. Take the corrected sentence and pull the distinctive phrase out of it.
2. `grep` that phrase in `.agents/day-reports/day-NN.md`.
3. Fix it there too, in the same commit as the day's fix.

Cheap version that catches most of it: any finding in the **superlative / absence class**
("no", "only", "never", "nothing", "the only") is one you have almost certainly repeated
somewhere else, because a strong claim is quotable and you quoted it. Grep for those first.

Related: [[length-reconciliation-strands-terms]] (the same rot in count claims — a number
promised in prose stops matching what follows it every time you edit near it).
