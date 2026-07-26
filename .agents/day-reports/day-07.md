# Day 07 report

- **Outcome:** shipped.
- **Commits:** `3a79fcc` (the day, `Closes #8`), then one fresh commit on top applying the review-panel findings plus this report and `docs/residual-review-findings/3a79fcc.md`. Nothing pushed. **No `--amend` at any point** — the first commit was made before the panel was dispatched, per `never-amend-after-dispatching-a-review-panel.md`, and `git show --stat` was read back after each; only staged files present, staged by explicit path.
- **Gate stats (final, after review fixes):** **8,039 prose words / 8 Q&A / 1 video / 5 links / 2 diagrams / 3 vocab terms / 54 min.** PASS **without** `--offline`, first attempt, no dead links. **Zero warnings** — the first day in Week 1 to land under the 9,000-word target and the first with no `check_unsourced_figures` hits. All 7 days re-gated together: 7/7 pass. `course/build.py` succeeds; `index.html` carries 14 inlined SVGs and 14 `<figcaption>`s across 7 days, zero `class=` inside any SVG, zero external hosts, zero `<p><figure>` nesting, and no stale text from the pre-panel version surviving in the page.

  On the figure check: it now reports an `unsourced_figures` stat and exempts figures "derived in place", so **Day 5's recommended fix was implemented.** It fired twice on Day 7's drafts and both were the false-positive shape Day 5 predicted — a bare `250%` in a §4 pointer and a `100%` in the phrase "a rate above 100%". I removed the numerals rather than adding decorative citations, which is why the final run is silent.

---

## Budget — I overran, and I am surfacing it

**I went past the 120k ceiling, at roughly the point the review panel returned.** Cause, so it is fixable rather than just confessed: the six days total **59,220 words**, which is ~79k tokens to read in full. Reading them all plus the style guide, DAY_MAP, three prior reports and the eleven-file compounding store does not fit under 120k alongside writing 8,000 words, two SVGs, a panel and a report.

**What I did instead, stated plainly because it is a limit on my judgement.** I read in full: every day's §1 and §3 Tier 1/2/3 for Day 6, `GLOSSARY.md` end to end (all 127 A–Z rows), and every passage I make a claim about — extracted by targeted `grep` and read in context, never summarised. I read via extraction rather than in full: §2, §4, §5, §7 and §10 of Days 1–5 (headings, sub-headings, `**bold**` lead lines, §6 table row labels, §8 question headings, §10 question stems). I did **not** read Days 1–5's §3 prose end to end.

**Why I think the result is sound anyway, and where it might not be.** Every claim Day 7 makes about an earlier day was verified by locating and reading the actual sentence — the Tier 2 spine quotes four days verbatim with line numbers, and the panel's accuracy reviewer independently re-verified all seven cross-day quotes and found none wrong. What extraction cannot give me is a *silent* contradiction: something Day 3's Tier 2 teaches that Day 7's assembly implies is otherwise, where neither text mentions the other. Reviewer 1 and Reviewer 3 both read against Days 1–6 and between them found six of those, all applied. **My recommendation: a synthesis day needs either a raised ceiling (~180k) or the six days pre-digested into a committed artefact.** The second is cheaper and reusable — Days 14, 21 and 30 will each hit this same wall, and Day 30 will hit it against twenty-nine days rather than six.

---

## The Rule A sweep across the whole week

**Script-checked, not read for.** I extracted every `**bolded**` string of five words or fewer from all six day bodies — **216 distinct terms** — and checked each against **134 `GLOSSARY.md` headwords** and **126 day-§9 headwords**, with plural, slash-variant and parenthetical normalisation. 113 came back uncovered. Then, because bolding is a partial sweep, I ran a second pass over **33 unbolded software words** a reader with no software background would trip on (`idempot`, `latency`, `percentile`, `regex`, `SDK`, `middleware`, `stack trace`, `distribution`, `provenance`, `happy path`, …).

**Of the 113, every one is either noise or glossed in place.** The noise is table row labels ("You built against the summary"), code identifiers (`tripwire_triggered=...`, `input_schema`), bare numbers, loop station names (defined inside the `Agent loop` row), and Anthropic's five workflow-pattern names. I investigated the remaining candidates individually by printing 300 characters of context around first use, and **all of them are glossed inline at first use**: `stochastic`, `escaping`, `base64`, `triangularly`, `agent-computer interface`, `sub-agents`, `namespace` (twice, in two different senses, both correct), `covered entity`, `business associate agreement`, `Security Rule`, `episodic`/`semantic`/`procedural`, `MemFS`, `oracle`, `self-consistency` and `95th percentile`.

**So the days' own vocabulary sweep comes up empty, and that is a real finding.** Days 3, 5 and 6 each found genuine gaps by running this check (`Pass`, `exporter`, `payload`, `VPN`, `blast radius`, `system of record`). Six days of that discipline has closed them. The one candidate I judged and declined to define is **`distribution`** — used inside two Rule B methods (`day-01:172`, `day-03:180`) with `tail` and never defined. For this specific reader, a mechanical engineer who works with tolerance distributions for a living, it is ordinary technical English rather than software jargon. I am recording the judgement so you can overrule it.

**What the sweep did find is a term used *across* days and defined nowhere, and it is the one the reader will hear most.** **`human-in-the-loop` / `HITL`** appears in Day 3 (inside the OWASP mitigation it tells him to lead with — *"Implement human-in-the-loop controls for privileged operations to prevent unauthorized actions"*) and six times in Day 6 (including inside LangChain's *"The Human-in-the-Loop (HITL) middleware…"*). `GLOSSARY.md` carries `Human-approval pause`, which is the specific mechanism, and no umbrella. Three review panels read past it. It is the most common phrase in this subject area and the reader had no entry for it.

**§9 therefore carries three rows, all found by script, all naming what the week already teaches:**

1. **`Human-in-the-loop (HITL)`** — with the point that it names a *category*, not a design, so a customer who says it has told you nothing until you establish hold point or witness point, and how many per run.
2. **`Deterministic / non-deterministic`** — used across five days, and Day 2 hands him a quotable line (*"a contract between deterministic systems and non-deterministic agents"*) whose both halves he could not define. Day 1 glosses non-determinism of the *model*; nothing glosses the property of a *system*.
3. **`Happy path`** — used in Day 3's Rule B step 2, undefined, and it is the concept the course's central thesis is about.

A fourth row disambiguating the two unrelated senses of **`exception`** (process, `day-06:313`; code, `day-03:118`) was **cut** after two reviewers judged it a §3 violation — it re-defines an earlier day's term in `GLOSSARY.md`. The gap is real and now recorded in `docs/residual-review-findings/3a79fcc.md` item 9 instead, because fixing it properly means editing Day 6's existing glossary row, which only you can do. Three rows still passes the gate's minimum of three. `GLOSSARY.md` re-synced: **130 A–Z rows, 3 from Day 7, verbatim from §9 with `· [Day 7](day-07-week-1-checkpoint/)` appended and `../day-` rewritten to `day-`; `git diff HEAD~1` shows 3 insertions and 0 deletions**, so no pre-existing row was altered.

---

## Did Day 6's Week 1 verdict survive my reading of the six days?

**Yes, in substance, and I would sharpen it in three places. Two of the three are corrections.**

**"Exposes every step" — I agree, delivered, and Day 6 undersold why.** The claim is not that the record is complete; it is that the reader can say what a compliant record *omits* by default and why (four `Opt-In` attributes, data protection rather than oversight). That is a harder claim to fake and it is the one that survives a follow-up.

**"Completes one useful workflow, with dependencies outstanding" — I agree, and I have adopted Day 6's recommended framing.** Day 7 assembles the week as one workflow fully mapped and fully exposed, with what it still needs named out loud. Day 6 is right that this is the stronger interview position, and right that the first follow-up resolves it either way.

**Correction 1 — the three dependencies are right, and there is a fourth thing that is not a dependency.** Day 6's list (durable state; recognising a duplicate; forty fields off a screenshot) is exactly right and I shipped all three, verified at `day-06:122`. But Day 6's own §10 Q6 answer at `:368` says "**one** dependency the week does not yet satisfy", so the day contradicts itself between Tier 2 and §10. Separately, Reviewer 2 argued the post-approval write rejection is a fourth dependency. I refused the renumbering and applied it as its mirror image — a failure Week 1 cannot *recover* from rather than a capability the run needs to *complete* — because renumbering would have made §8 and §10 Q5 claim the reader owes four capabilities before the design runs, which is false. Reasoning in the residual file, item 7.

**Correction 2 — Day 6 reproduced its own worst defect in the hand-off, and I inherited it.** Day 6's panel caught its headline sentence claiming that at 120 invoices a day "no amount of tuning the design gets there", when its own move 2 (design the screen, lowering *t*) reaches the ceiling. Day 6 fixed the day and then wrote the same overclaim into the *summary* my brief is built on. My first draft said the minutes ceiling is one "which no design change reaches" — false in the same way, and Reviewer 2 caught it. Now: none of the five *software* numbers reaches it, and the two levers that do are the screen and the scope, with Day 6's own quantification that the ceiling reaches 1 only if *t* falls to a minute. **The lesson for the protocol: a day's report is the specification the next day builds against, so a claim corrected in the day has to be corrected in the report too.** Day 5 hit the same class from the other direction when a deleted paragraph left its report stale.

---

## Does the stopping-condition spine hold across Days 1, 3, 5 and 6?

**It holds, and it is the right spine. Three of the four claims are exactly as Day 6 states them; one needed correcting, and one of my brief's summaries of them is wrong.**

**Day 1 — my brief says "Day 1 gave three exits". The day's *body* gives two.** `day-01:106` — *"The model ends the loop by saying it's done. The normal exit."* `day-01:110` — *"Finishing without the model declaring completion is a failure. Not a shrug — an error with a name."* §8 at `:328` says *"Two exits."* The third, `external interrupt`, appears only inside the §9 `Stopping condition` row at `:357`, named in a list and taught nowhere. **Day 6's corrected formulation is the accurate one and my brief's summary of it is not.** I also tightened my own first draft here: I had written that Day 1 "defines it there", and Day 1's row defines *Stopping condition*, not *external interrupt*.

**Day 3 — holds.** `day-03:116` — a tripwire *"stops the run. Not "warn and continue", not "ask the model to have another go" — halt."* `:400` adds the half that matters: *"halt the run and hand it to a person."*

**Day 5 — holds as a finding, and its stated reason is wrong. See the residual file, item 1.** `day-05:115` says the cap-fired run's *"final pass reads `stop`, identical to a run that genuinely finished"*. `gen_ai.response.finish_reasons` is a provider passthrough, not an enum; Anthropic's documented values are `end_turn`, `max_tokens`, `stop_sequence`, `tool_use`, and a cap-killed run's last pass asked for a tool, so it reads `tool_use` — different from a completion. `stop` is OpenAI's. Reviewer 2 raised it; I verified it myself against Anthropic's own docs before believing it, because a reviewer's contradiction of a shipped day is exactly where I should not take a subagent at face value. **Day 5's build instruction is untouched and is now better founded**: the field answers why the *model* stopped writing a pass, never why the *run* ended, so the three values have to be your own. My first commit repeated Day 5's `stop` claim in seven places including a diagram label; all seven are corrected.

**Day 6 — holds.** `day-06:101` — the pause is the third exit *"and it is the only one that is *planned*"*, with the tripwire-vs-pause table beneath it, and Anthropic's whitepaper quoted for the placement (both PDF quotes re-verified here through the gutter-split corpus).

**My one substantive addition to the spine.** Counting the exits gives **four, not three**, and the fourth is Day 3's tripwire, which Day 1's list does not name — it is enforced by your code like the cap but fires on a *check* rather than a *count*. Day 1's row is not wrong (it opens "Any rule that ends the loop:"), but the enumeration a candidate builds an answer from is incomplete, and the pair he most often collapses is tripwire-versus-pause. That is the day's second diagram.

---

## Rules A and B — followable as written?

**Rule A: yes, and its "verify, don't assume" clause is what made the sweep worth running.** No amendment. One observation for the guide: Rule A is written for a term *within* a day, and a week-wide sweep needs a different normaliser — 113 of my 216 hits were false until I taught the checker about plurals, slash-variants and parentheticals, and 100% of the remainder were glossed in place rather than tabled. **If a future checkpoint day repeats this, the useful output is the ~15 candidates that survive noise, not the raw count.** The script is in this slice's history if you want it in `evals/`.

**Rule B: followable, and a synthesis day is the case it does not cover.** Day 7 introduces no knob, so under the letter of the rule it owes nothing — which would license a checkpoint day that quotes six numbers and derives none, and that is exactly the day that produces the fluent tourist. What I did instead, and would propose as a clause: **a day that re-uses other days' knobs owes a method for checking that they compose.** Tier 3 ships that as a unit audit — write each number with its unit, ask of every pair whether one is an input to the other, derive coupled pairs against one assumed run, and say out loud what does *not* convert.

Pushing that audit to its edge, per the guide's impossible-value clause, produced the best paragraph in the day and I would not have found it otherwise: **five of the six numbers are denominated in things the software controls, and the sixth's ceiling is in minutes of one person's working day — and that is the one that binds.** No step cap changes how many invoices a clerk can read. Which means the question most likely to kill the design (*how much of whose time am I being given?*) is available in week one for free, and is the most expensive thing to discover late. That is a Rule B result about the *set* rather than about any member of it.

**Also confirmed, in the direction of restraint:** the input-knob clause let me give each of the six numbers one clause of method in a table rather than six derivations, which is what kept the day at 8,039 words. Without it a synthesis day recurses into re-teaching every week it summarises.

---

## Sourcing: what the machine check caught

**Two real defects, both invisible to eye-reading, and one methodological error of my own worth recording.**

**The methodological error first, because it is the dangerous kind.** My first corpus glob was `course/day-0*/README.md`, which matches `day-07` — **the day being checked was inside its own corpus**, so every string matched and the check reported 90 strings, 0 unmatched. A clean result from a vacuous check is worse than no check. I caught it because my own invented §8 dialogue "matched" a source. **Fix: exclude the file under test explicitly, and prove the check has teeth by feeding it two deliberately corrupted quotes** — both of mine were correctly missed. Compounded.

With the corpus fixed: **44 distinct quoted strings, 28 initially unmatched, 26 of them my own dialogue, `alt` text, `<summary>` stems and interview questions** — 93%, higher than the ~65% the store predicts, because a synthesis day's §8 and §10 are almost entirely invented dialogue while its citations are few. One was the regex artefact Day 6 recorded, matching the text *between* two adjacent quoted fragments. That left one real defect:

**I converted Day 3's double quotes to single quotes inside a quotation.** `day-03:116` reads `Not "warn and continue", not "ask the model to have another go"` with **double** quotes. Nesting doubles inside a markdown double-quoted span is impossible, so I silently substituted singles — the same family as Day 5's `ee/LICENSE` backticks. Per the store, the fix is to shorten rather than to re-punctuate: the day now quotes `"it stops the run"` and states the exclusions in its own prose.

**The second real defect was a timestamp, found by two reviewers independently and confirmed here.** I cited `43:07` for the thesis's third sentence. `43:07` is where the *three-sentence* passage begins — correct for Day 6, which quotes all three. The sentence Day 7 quotes first appears in the cue at `00:43:16.319`. Corrected to `43:16`. **Generalisation worth having: a timestamp inherited from another day is only correct for the span that day quoted.** Re-derive it for your own span. Same class as `chapter-markers-carry-an-end-time-too.md` — a correct value read against the wrong boundary.

**Everything else verified.** All four external quotes re-fetched to disk and grepped (LangChain HITL docs, Anthropic's *Building effective agents* ×2, OWASP `LLM01:2025`). Both Anthropic whitepaper quotes verified through the two-column gutter-split corpus at `GUT=85` — *"pause here for human review"* matched in the plain `-layout` output and *"until the task is completed or it hits a stopping condition"* only in the column-split corpus, reproducing `two-column-pdfs-defeat-quote-matching.md` exactly. The transcript quote verified against the committed `.vtt` after stripping inline timing tags and de-duplicating rolling caption lines. All 5 links clean on the online gate, before and after the panel; no host warned, so no hand-verification was needed.

**One video, re-verified myself.** `D7_ipDqhtwk` — *"How We Build Effective Agents: Barry Zhang, Anthropic"*, channel `AI Engineer`, `15:09`, published `20250404`, **`chapters = NA`**. So: "no chapter markers — watch the whole thing (15 min)", which §5.4 blesses. Note that my brief's ruling that **§7 may carry zero videos is wrong** — `evals/check_day.py:298` hard-fails a §7 with no `### 1.` heading, so a synthesis day cannot decline videos even with a stated reason. Filed as residual item 5.

---

## Boundary material handed to specific later days

Nothing cut. Boundary pass came back clean from the contract reviewer: no later-week mechanism is taught.

- **Week 2 (Days 8–14)** — receives the three named dependencies as the reader's own words for why the week exists, plus the post-approval rejection as the failure Week 1 cannot recover from. Day 7 names durable state as *mandatory* and quotes LangChain's requirement; it teaches no journalling, no durability mode, no replay, no idempotency key, no saga. `grep -i` for `idempot`, `saga`, `compensating`, `backoff`, `jitter`, `replay`, `memoiz` returns 0.
- **Day 11 / Day 12** — `checkpointer` is used exactly as Day 4 defined it and not redefined.
- **Day 13** — inherits the hook Day 6 left and Day 7 sharpened into a coupling: **a step you can reliably reverse does not need permission first, so Week 2's work can *lower* Day 6's approval floor.** The approval count is a function of how much of the process you can undo, not a fixed property of it. That is the strongest single argument for Week 2 that Week 1 can make, and it is stated as a hook rather than a lesson.
- **Day 16** — nothing tagged, no taxonomy.
- **Day 22** — Day 7 supplies no discovery question. The one place it comes close is the unit audit's conclusion, which tells the reader to ask *how much of whose time am I being given* first. That is one question about a **number he needs for a derivation Day 6 already taught**, not questioning technique, and I judged it inside the line Day 6 drew. Worth your eye.
- **Day 23** — the deterministic/non-deterministic split is defined as a *property* (which half a control lives in, bound versus bet) and deliberately not drawn as Day 23's triage framework. Day 23 should assume the reader has the vocabulary and owes him the decision procedure.
- **Day 24** — §5's exercise is written as the raw material the issue body asks for: a one-page README naming each component, the failure it prevents, and the number that governs it with its unit. Day 24 should assume that page exists in his head and owes him ADRs and the *why-we-rejected* half.
- **Days 28 / 30** — the four-exit table and the unit audit are the two drillable artefacts. Day 30 will need the digest problem solved (see the budget section) before it can synthesise twenty-nine days.

---

## Week 1 retrospective, since the build pauses here

You asked for blunt, and for something you do not already know. The reading-only limitation is recorded, so I have left it out.

**What a reader who has finished Days 1–7 can actually do.** He can hold a twenty-minute technical conversation about a back-office agent and sound like someone who has been near a deployment. Specifically: draw the loop and say which stations are his code; explain why the integration is the schedule and not the agent; name the four gates and say which one carries the load; explain why a bigger context window makes accuracy worse and derive the trigger; describe what a compliant trace omits and why; map a process to the resolution where every rule has a location; and derive an approval count from both ends and report that the two do not meet. **That last one is the strongest thing in the week** — a finding that arrives before anything is built, delivered in the customer's units, is what a deployment engineer sounds like and it cannot be got from a blog post.

**What he cannot do, in order of how likely it is to end an interview.**

1. **He cannot say how he would know whether any of it worked.** Every number in Week 1 is derived from structure — a task's minimum action count, a window minus its worst case, minutes of staffing. Every one of them then says *"and once you have traces, replace the assumption with the observed distribution"*, and he has never seen a trace, has no labelled cases, and no notion of what a pass rate is. So his answer to *"how do you know it's working?"* is currently "I'd measure it", which is the answer of someone who has not. That is Week 3, and until Week 3 exists **every method in Week 1 is a defensible opening bid with no second move**. An interviewer who asks the second question twice finds the floor.
2. **He can defend six numbers and has never had one be wrong.** The week teaches derivation and never teaches revision. Day 6's arithmetic returning 0.67 is the closest thing to it, and even that is a finding at design time rather than a number that failed in production. "Walk me through a time your first answer was wrong and what you changed" is a stock FDE question — Day 25 owns it — and he has no material for it at all, not even a hypothetical.
3. **He has no economics.** Days 1 and 4 quote token costs; nothing converts "ten days a month of keying" into a number a finance team would sign. That is Days 19 and 27 by design, but it means he currently cannot answer the *first* question a VP asks, and the discovery round is the one the report flags as highest-signal.

**The single highest-value thing to fix before Days 8–30 resume — and it is not a day.** Write the trace. One committed artefact: a realistic span tree for one invoice run through the workflow Days 6 and 7 assemble, with the token counts, the custom stop-reason field, the approval span, and one run that went wrong. Twenty or thirty spans of JSON, plus a page reading it.

Here is why it beats writing Day 8. **Every Rule B method in Week 1 terminates in "once you have traces", and there are no traces.** Day 1's cap is "above the tail of the distribution of successful runs"; Day 4's trigger is "the 95th-percentile tool-result tokens per pass"; Day 5's sampling rate needs an observed failure rate; Day 6's *t* is "measured elapsed time" and its override rate is a number he has never seen a value of. Six methods, one missing input, and the reader currently supplies it with the word "traces" — which is precisely the fluent-tourist move the style guide was written to kill. Give him one real trace and all six methods acquire a second move: he can *point* at the number rather than name the field it would live in. It also front-loads the material Days 16, 17 and 18 need, and it is the cheapest possible answer to *"have you actually looked at one of these?"*.

It is also the thing that most needs doing while the week is fresh in one head. Nobody has yet read all six days against each other except me, and the trace is where an inconsistency between them would show up as a field that cannot be filled.

**Second-highest, and much cheaper: fix Day 5's `stop` sentence and Day 3's three-versus-eight.** Both are in residual items 1 and 2. Day 5's is the one a reader would repeat and be contradicted on by any engineer who has read Anthropic's API docs, and Day 7's Tier 2 spine leans on that exact sentence — so it is now load-bearing in two days rather than one.

---

## Anything you need to decide

1. **How a synthesis day reads its inputs.** I overran the budget on reading and told you how. Days 14, 21 and 30 will hit it worse. My recommendation is a committed per-day digest artefact rather than a raised ceiling, because Day 30 faces 29 days and no ceiling fixes that.
2. **Day 5's `stop` sentence.** Residual item 1, with the Anthropic doc evidence. I could not touch Day 5, and Day 7's spine depends on the corrected version.
3. **Day 3's three-versus-eight.** Residual item 2. Day 6's Reviewer 3 was right and Day 6 could not reproduce it; I reproduced it. Five places use eight, one derives three.
4. **Whether `check_day.py` should permit a §7 with zero videos and a stated reason**, since the style guide already does and the gate does not. Residual item 5.
5. **Whether the `exception` collision is worth one clause in Day 6's existing glossary row.** I cut my own row for it on two reviewers' advice; the gap is real and now lives only in the residual file.

## B8.5 browser verification

**Skipped.** This slice ships one markdown document and two static SVGs; there is no UI to walk. `index.html` verified programmatically instead — see gate stats.

## B10.5 compound

One new entry and two updates, rather than three new files, because two of the three are instances of classes the store already names.

1. **New — `docs/solutions/conventions/a-quote-check-that-includes-its-own-target-is-vacuous.md`.** The corpus glob that matched the file under test, why a 0-of-90 clean result should have been the tell rather than the reassurance, the two-corrupted-quotes teeth test that proves the check works, and the general shape: **any verification whose corpus can contain its own subject reports success by construction.**
2. **Update — `machine-check-every-quoted-string.md`.** Adds the exclude-the-target rule and the teeth test, the nested-double-quote case (a source that quotes something inside the sentence you want cannot be quoted whole in markdown — shorten, do not re-punctuate), and the observation that a synthesis day's own-prose miss rate is ~93% rather than ~65%, so the ratio the note predicts is a function of how much invented dialogue the day carries.
3. **Update — `chapter-markers-carry-an-end-time-too.md`.** Adds the inherited-timestamp case: a timestamp correct for the span another day quoted is wrong for a shorter span of the same passage. Day 6's `43:07` is right for three sentences; Day 7 quoted the third alone, whose first cue is `43:16`. Same class — a correct value read against the wrong boundary — and it now has an instance that does not involve `end_time`.

## Review panel

**3 reviewers, ~30 findings, ~26 applied, 5 deferred to forbidden files and 4 refused or partially refused** with reasons in `docs/residual-review-findings/3a79fcc.md`. Ranked by damage:

1. **The `stop` claim, in seven places including a diagram label.** Reviewer 2. Verified independently against Anthropic's `stop_reason` docs before applying, because a reviewer contradicting a shipped day is where I should be most sceptical. Day 5's conclusion kept, its premise dropped, and Day 5 filed as residual item 1. **The single most valuable finding**, because it was the day's most-repeated line and a reader would have said it to an engineer who knows the API.
2. **Three absolute claims that my own sources refute.** "No arithmetic turns a pass count into a write count" — refuted by the Day 3 quote in the same sentence (*"a cap of 20 passes permits 20 payments"*), which is that arithmetic at one write per pass. "No design change reaches" the minutes ceiling — refuted by Day 6's move 2. "The only worked example in the week where a derivation returns an impossible number" — Day 5's sampling floor is the other, and the style guide names Day 5 as the origin of that clause. All three are the superlative/absence class §5 rule 7 names as breaking most often, and I shipped three of them in one day.
3. **My own count claims rotted in five places, and I found the first set myself before the panel.** §2 said four units, Tier 2's table has five, Tier 3 listed four for six numbers, and §10 Q3's stem promised four while its answer gave five. Fixed pre-panel. The panel then found that "three couplings" was followed by four, because one paragraph contained two ("The second coupling is nastier"), and that "four I'd cut before I cut them" was followed by two genuinely cuttable. **`length-reconciliation-strands-terms.md` item 4 predicted exactly this and I still shipped it — a count claim rots every time you edit near it, so the grep has to run after the last edit, not after the first draft.**
4. **"Roughly 130 words" described a 171-word paragraph**, and the number is the reader's rehearsal target. Two reviewers. Now "about 170 words", and the "first thirty seconds" it claimed is now "the opening minute".
5. **The SVG `<desc>` contradicted itself within one sentence** — the boundary "sits between the approval pause and the write" and the approval "straddles that line". The geometry settles it: the Approve rect is 562–712 and the boundary is at x=736. This is the exact defect class Day 6 shipped, one day later, in a `<desc>` that is all a screen-reader user gets. Now "the last step before that line".
6. **§9's preamble contradicted its own fourth row** — "four terms that nothing in the course defines", where the row itself cited Days 3 and 6 for the two definitions. All three reviewers. Row cut; see the Rule A section.
7. **§8 answer 1 asserted a per-run approval that Tier 3 proves unstaffable at the same volume**, in the same day. Now scoped to a pilot in the answer itself.
8. **Weak answer 3 was a straw man** ("None of them, really — they all matter"). Replaced with the trade this reader would actually accept and which costs most: cut tracing for the pilot, add observability later. The "why the strong one lands" now explains that there is no retrofitting a trace onto a run that already happened.

Also applied: "the trace has no unit because it bounds nothing" contradicted the day's own table, which gives Day 5 a rate and a unit; the diagram-1 caption claimed non-conversion "is the whole of Tier 2" when most of Tier 2 is the couplings; Day 1's §9 row described as *defining* `external interrupt` when it defines `Stopping condition` and merely names the third; "cannot be eliminated" tightened to OWASP's own hedge; the 200,000-token window bound to Claude Haiku 4.5 inside the sentence, per the guide's corollary; dependencies 2 and 3 given the owner §1 promised ("Week 2's"), and the missing owner for document extraction filed as residual item 6; "the six days each carried their own two videos" corrected — Day 2 carries one, so eleven across six days; "no timestamps to cite" narrowed to "no chapter markers to cite", since a transcript is committed and §5.3 permits transcript timestamps; the deflating opening line in §4 given the consequence the guide requires it to be attached to; §10 Q4's stem converted from recall to an interviewer's pushback, since only one of eight was adversarial against §3's ~2; `days.json`'s Day 7 `one_liner` aligned with the frontmatter, which Days 1–6 match byte-for-byte and Day 7 alone did not; and `reading_minutes` re-set to 54 **after** the last cut, twice, because the panel fixes moved the count.

**Headroom worked as planned, and this is the first day it did.** I shipped the first commit at **7,830** words, with **2,170** of ceiling headroom against Day 5's recommended ~900 and Day 6's actual 285. The panel's fixes added **203 words net**, far under the ~500–950 the brief predicted, because 26 of 30 findings were replacements rather than insertions. **No deletion pass was needed and the gate never failed on length.** That is what a reserve buys, and the reason the number came out low is worth recording: on a day whose defects are *overclaims*, the fix is almost always a narrower sentence of the same length. The ~900 figure is right as a reserve; it is not a prediction.

**Every check re-run after the fixes.** Quote check re-run with the target excluded and the teeth test re-passed; zero banned phrases; all 14 count promises re-confirmed against what follows them, including a re-count of the 171-word paragraph; all three §9 headwords confirmed present in the body before §9; `GLOSSARY.md` re-diffed against `HEAD~1` (3 insertions, 0 deletions); `days.json` re-parsed as valid JSON; `build.py` re-run and `index.html` re-verified (14 `<figcaption>`s, 14 inlined SVGs, zero `class=`, zero external hosts, zero `<p><figure>` nesting, and grepped specifically for the pre-panel `stop` wording, which is gone from both the page and the SVG); and all seven days re-gated together, 7/7 PASS.
