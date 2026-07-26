# Residual review findings — Day 07 (`3a79fcc`)

Three reviewers, ~30 findings, ~26 applied. What is left is either in a file this slice may
not touch, or a finding I pushed back on with a reason. Day 7 is the first slice written by
somebody who read all six earlier days against each other, so items 1–4 are cross-day
defects nobody was positioned to see before.

---

## Deferred — in files this slice is forbidden to modify

**1. Day 5's `stop` claim is provider-specific, and wrong on Anthropic. This is the highest-value item here.**

`course/day-05-audit-trail/README.md:115` reads:

> And a run that stopped because your **max-step cap** fired stopped for a reason the model
> never saw, so its final pass reads `stop`, identical to a run that genuinely finished.

`gen_ai.response.finish_reasons` is a passthrough of the provider's own value, not an enum the
conventions define. Anthropic's documented `stop_reason` values are `end_turn`, `max_tokens`,
`stop_sequence` and `tool_use` (fetched from `https://platform.claude.com/docs/en/api/handling-stop-reasons`,
checked July 2026 — the string `stop` alone does not appear as a value). `stop` is OpenAI's
value. Worse for the claim: a run killed by your cap has a final pass that *requested a tool*,
so on Anthropic it reads `tool_use` and on OpenAI `tool_calls` — in both dialects **different**
from a genuine completion.

**Day 5's conclusion survives and is stronger than its premise.** The field reports why the
*model* stopped writing that pass, never why the *run* ended, and its value differs by vendor —
so "finished / hit the step cap / overflowed the window" still has to be one custom field on the
root span with three distinct values. Day 5's build instruction is right; the sentence
justifying it is not.

Day 7's first commit repeated the `stop` claim in seven places, including a diagram label and a
§10 answer. All seven are corrected in the second commit to the true form. **Day 5 needs the one
sentence at `:115` amended, and `:274`'s §8 answer re-read alongside it.** Found by Reviewer 2,
independently verified here against Anthropic's own docs before applying.

**2. Day 3 derives *three* writes and then uses *eight* in five places — confirming what Day 6's
Reviewer 3 said and Day 6 could not reproduce.** `docs/residual-review-findings/f10434a.md`
item 3 left this open. It is real:

- `day-03-guardrails/README.md:374` (§8) derives it: *"adjust, note, status is three… So three
  writes, a value cap per run, and a count per day"*.
- `:181`, `:182`, `:184`, `:192` and `:366` all use **eight** — including `:366`'s customer-facing
  ceiling, *"with a write budget of eight… the worst case is eight payments"*.

Eight is reachable from the method (one write × a batch of eight), but the day never takes that
step, and `:374` uses both numbers in one paragraph without connecting them. A reader following
the derivation gets three and then hears eight quoted back at him five times. **Day 6's Reviewer 3
was right.** Day 7 sidesteps it by citing Day 3's method and unit rather than either value.

**3. Day 2 still says the response budget is "per result"; Day 4 says per pass and is right.**
Raised in `docs/residual-review-findings/8488d96.md` items 1–3 by Day 5, still unfixed at
`9ddb161`. `day-02-tool-use/README.md:173` reads *"the same sum gives 19,700 per result"*, while
`day-04-context-and-memory/README.md:111` corrects it explicitly: *"Day 2's 19,700 came from
dividing the window across ten passes, making it a per-*pass* allowance, not a per-*result* one"*.
This is now the third writer to flag it. It matters more for Day 7 than for the earlier days,
because Day 7's whole Tier 2 argument is that these two numbers are one derivation — so the
unit has to be right in both places or the coupling reads as a contradiction. Day 7 attributes
the figure to Day 4's usage for that reason.

**4. Day 6's `reversibility-line.svg` says the approval "straddles" the boundary; Day 7's
`assembled-system.svg` places it as the last step before it.** Both are defensible readings of
Day 6's prose (*"The approval belongs on the line, not near it"*), and the approval itself
changes nothing in the customer's systems, which makes the literal placement *before* the line.
Two diagrams in the same week rendering the same relationship differently is worth one of you
picking a side. No factual error either way; low priority.

**5. `STYLE_GUIDE.md` §5 blesses "zero videos with a stated reason", but `check_day.py` hard-fails
it.** `evals/check_day.py:298` fails with `"section 7 lists no videos (use \`### 1. Title\` format)"`
when §7 contains no `### 1.` heading. A synthesis day is exactly the case where zero videos is the
right answer, and the gate forbids it. Day 7 shipped one video instead. Either the check should
accept a §7 that states why it lists none, or the guide should say one video is the floor.
Forbidden file.

**6. No DAY_MAP row obviously owns document extraction.** Day 6's third dependency — pulling forty
fields out of a screenshot — is assigned to "Week 2" by both Day 6 and Day 7, but Days 8–14 own
structured outputs, schema validation, failure modes, checkpointing, resume and failure handling.
None of them is "getting fields out of a scanned document reliably". Day 7 says "Week 2's" rather
than naming a day, which is honest at the reader's level and leaves the gap in the plan.

---

## Refused, with reasons

**7. "Make the post-approval ERP rejection a fourth dependency."** Partially applied. The three
dependencies are capabilities the workflow needs to *complete a run*; a rejection after approval
is a failure it needs to *recover from*, which is a different object. Renumbering to four would
have made §8's answers and §10 Q5 claim the reader owes four capabilities before the design runs,
which is not true. Applied instead as a paragraph naming it as the mirror image, pointing at the
§6 row, and saying Week 1 cannot recover from it either — which closes the follow-up the reviewer
posed (*"the period closed Friday, ERP rejects, now what?"*) without miscounting.

**8. "Cite `02:59` from the committed transcript for the Barry Zhang video."** Refused. Reviewers 1
and 3 are right that §5 rule 3 permits transcript timestamps and that Day 1 cites two of them, so
"no timestamps to cite" was an overstatement — that clause is corrected to "no chapter markers to
cite". But *adding* a timestamp is a different move: Day 7 sends the reader to this video for its
**ordering** — the argument that the first third is about not building an agent — and a timestamp
into the middle of that third defeats the reason the video is listed. Fifteen minutes, watched
whole, is the recommendation.

**9. "§9's `Exception` row is padding and double-defines a Day 6 term."** Accepted and the row was
deleted, from both §9 and `GLOSSARY.md`. Recorded here because the *finding* it carried is real and
now lives nowhere: **the course uses `exception` in two unrelated senses** — the process sense
(`day-06:313`, in `GLOSSARY.md`) and the code sense (`day-03:118`, glossed inline) — and nothing
tells the reader they are unrelated. Two reviewers independently judged a disambiguation row to be
a §3 violation ("Do not list terms from earlier days"), and they are right, so it is out. If you
want it addressed, the right place is one clause in `GLOSSARY.md`'s existing
`Exception (in a process)` row, which only you can edit.

**10. "Only one of eight §10 questions is adversarial against §3's ~2."** Applied by converting Q4's
stem to an interviewer's pushback rather than by adding a ninth question, which the word budget
would have taken.
