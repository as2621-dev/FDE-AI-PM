# Day 06 report

- **Outcome:** shipped
- **Commit:** one fresh commit for the day (`Closes #7`), then one more on top applying review-panel findings. Nothing pushed. **No `--amend` at any point** — the report was written and the first commit made *before* the panel was dispatched, per `docs/solutions/conventions/never-amend-after-dispatching-a-review-panel.md`. `git show --stat` read back after each commit; only staged files present.
- **Gate stats:** **9,715 prose words / 8 Q&A / 2 videos / 6 links / 2 diagrams / 16 vocab terms.** PASS **without** `--offline`, first attempt, no dead links. `course/build.py` succeeds; `index.html` carries both SVGs inlined with captions, 12 `<figcaption>`s across 6 days, zero `<p><figure>` nesting, zero `class=` inside any inlined SVG, zero external hosts referenced from any SVG.

  Two warnings, both expected:
  1. **9,715 words, at 65 estimated minutes against a 45–60 minute promise.** This is the headline finding of the slice — see the length section below. Justification for the band: the overflow is four owned subtopics plus a 16-term vocabulary paid from zero, not restatement.
  2. **Two distinct figures "cited with no link".** Both are structural false positives of a kind worth recording, because they are the opposite of what the check hunts: `$1M` appears in a paragraph whose entire purpose is to say the number is a marketing claim, and `1%` is a hypothetical inside a §10 question stem. A third hit (`800%`) *was* the check doing its job — the paragraph attributes the figure to the First Round essay without linking it there — so I added the link. **One in three was real, which is a better hit rate than Day 5's zero in nine.**

---

## Does Week 1 actually deliver its promise?

You asked me specifically, as the last build day. The promise is *"By Day 7, the agent completes one useful workflow and exposes every step."*

**"Exposes every step" — delivered, and better than the promise.** Day 5 gives the span tree and is explicit about what a standards-compliant trace *omits* by default. Day 6 adds that the approval is itself a span carrying the approver's identity, the timestamp, the decision and the exact arguments shown. A reader can describe how every step is exposed and, more valuably, name the four fields that are `Opt-In` and therefore usually missing. Nothing needed here.

**"Completes one useful workflow" — delivered with one dependency outstanding, and Day 7 must not paper over it.** This is the real finding, and Day 6 surfaced it while reading LangChain's current documentation rather than by reasoning about it: **a human-approval pause requires state that survives the pause, and no day in Week 1 provides that.** Day 4 established that a run's state lives in the context window by default and dies when the run ends. LangChain makes it a hard requirement, not a nicety — "You must configure a checkpointer to persist the graph state across interrupts." Day 4 named `checkpointer` and deliberately described it thinly, handing the mechanics to Days 11–12.

So the workflow Day 6 teaches — intake, read, draft, **pause**, write — cannot run to completion on what Days 1–5 built *unless the approval is answered inside the lifetime of one process*, which means somebody is sitting there waiting. That is a demo, not a deployment, and Day 6's own arithmetic (a clerk with two hours a day against 120 invoices) says the wait is hours, not seconds.

**My recommendation for Day 7, and Day 6 is already written to support it.** Assemble the week as *"one useful workflow, fully mapped and fully exposed, with the one dependency it still needs named out loud."* That is a stronger interview position than a claim of completeness, because the first follow-up — "what happens if the approver goes home?" — resolves it either way. Day 6 §10 Q6 asks exactly that question and answers it that way, so Day 7 can lift the thread rather than invent it.

**Two smaller gaps Day 7 should know about.**

1. **Nothing in Week 1 says what the agent is told when a human *edits* its proposal.** Day 6 names approve / edit / reject as the three decisions, and *edit* means the model's arguments are replaced by a person's before the action runs. No day has said whether the model learns its proposal was changed, or whether the edited arguments enter the transcript as though they were its own. That matters for the next pass and it belongs to nobody's boundary — not Day 3's (which owns what the approver may be shown), not Day 4's (which owns what the transcript holds). It is a legitimate thing for the "walk me through your agent" rehearsal to raise and leave open.
2. **Day 6's §6 row on the receiving system rejecting a write *after* an approval has been given is a Week 1 workflow Week 1 cannot recover from.** Same shape as the main gap. The row points at Week 2 and says so.

**The strongest single thread for "walk me through your agent", if Day 7 wants one.** The **stopping condition**. Day 1 gave three exits; Day 3 added the tripwire as the *unplanned* exit; Day 5 showed that the step cap's exit is indistinguishable from success in the OpenTelemetry conventions and has to be a custom field; Day 6 made the approval pause the *planned* third exit and drew the tripwire-vs-pause distinction as a table. That spine touches four of the six days, it is drillable, and it is the place where a candidate who has actually read the week sounds different from one who has read a blog post.

---

## The length finding, which is the process story of this slice

**The first complete draft was 11,087 prose words against a 10,000 hard ceiling.** Getting to 9,715 took eight passes and the numbers confirm `length-reconciliation-strands-terms.md` precisely:

| Pass | What it did | Words saved |
|---|---|---|
| 1 | **Unit deletion**: collapsed Tier 2's five-step walk, which duplicated diagram 1's bottom row | −754 (with 4 other cuts) |
| 2 | **Unit deletion**: §8's third interview pair, §10 Q3 and Q7, §6's group-routing row, §9's unused `Operating map` row | −166 |
| 3–8 | Compression only | −70, −86, −55, −124, −13, −4 |

**The two unit-deletion passes account for 67% of the saving. The six compression passes averaged −59 words each** — which is the −60 figure that note already records, reproduced to within one word on a different day by a different writer. I am recording it because the agreement is now strong enough to act on: **compression is not a length tool in this format. It is a quality tool that happens to save a rounding error.**

**Two things I would ask you to decide.**

1. **Day 6 is oversized for the ceiling, and I do not think that is a failure of the draft.** The day owns four subtopics where Days 1–5 owned one or two each: *picking* the process, *mapping* it granularly, the *pause mechanism*, and the *approval count* (the Rule B knob). Each is separately interview-relevant, none is restatement, and the DAY_MAP line assigns all four plus the last-mile idea and the French-waiter model. On this evidence the honest options are to raise the ceiling for multi-subtopic days or to split Day 6 into *picking and mapping* and *the pause and its number*. **Splitting is your call, as the brief says; I have shipped the single day under the ceiling.**
2. **I shipped with 285 words of ceiling headroom, and Day 5's report says the reserve should be ~900.** I could not reach 900 without cutting teaching, so I pre-committed to a deletion list instead of a reserve: §10's Q7, §8's second "Why the strong one lands", and Tier 3's cycle-time paragraph, in that order, if panel fixes overran. **They did not — final fixes fit.** But the mitigation was a plan rather than a buffer, and that is worth knowing before Day 7's writer plans a synthesis day.

---

## Rules A and B followable as written?

**Yes, both, and both earned their keep. The amended clauses on B were load-bearing.**

**Rule A caught three real gaps in my own draft, all found by running a script rather than by reading** — which is now four days in a row that this has been true.

- **`VPN`** — used twice, and defined **nowhere in the course**: `GLOSSARY.md` carries `VPC (virtual private cloud)` from Day 3 and no `VPN`. A reader meeting "behind a VPN" has been given a term he cannot look up. Rewritten both times as "reachable only from inside the company's own network", which is what the sentence actually needed.
- **`middleware`** — new to the course and unavoidable, because it is how LangChain's current documentation describes the pause. Now glossed inline on first use: *"a component you slot into the loop without rewriting it"*.
- **`lgtm`** — quoted from the Varick source and opaque to a reader with no software background. Glossed in place.

Two further terms were gaps in *earlier* days that this day was leaning on, and both are now §9 rows:

- **`blast radius`** is used in Days 1, 3 and 4, and it appears inside `GLOSSARY.md`'s own `Max-step cap` row — "Bounds cost, latency and blast radius" — while being defined nowhere. It is the same shape as the `Pass` gap the brief describes: a load-bearing unit across several days that nobody's table carried. My Tier 3 derivation quotes what the approval count bounds, so it owed the definition.
- **`system of record`** appears in Days 2 and 4 and is only *implicit* in the `ERP / CRM` row's definition. Since the whole reversibility argument turns on what you write to, it is now a row of its own rather than an inference from someone else's.

I script-checked 56 terms against §9 and `GLOSSARY.md` before believing any of this. Seven flagged terms I judged already covered and did not define: `solution-design` (Days 1 and 2 use the round name), `purchase order` (Day 1), `reconciliation` (Days 1, 2, 5), plus `PDF`, `screenshot`, `cost centre` and `staged`, which are ordinary English or self-glossing in place. `PO` appears once, inside the verbatim run-log block, and now carries a six-word gloss after it.

**Rule B, and the subject-vs-input clause decided the shape of Tier 3.** The day's subject knob is **how many approval pauses one run may carry**, and it gets the full treatment:

- **Floor** from the run's own structure: the number of points past the reversibility boundary needing a decision no earlier decision supplies. With the merge rule that makes it countable — two irreversible steps share one approval only if everything needed to judge the second is already on the first one's screen.
- **Ceiling** from the customer's staffing: `a ≤ M ÷ (R × t)`. Units check out to approvals-per-run.
- **What it trades in each direction**, including the tie to Day 5's retention period, because removing an approval converts a consequence from *reviewed beforehand* to *detected afterwards*.
- **How traces replace the assumption**: measure *t* as observed elapsed time, and measure the override rate — which reads backwards, since near-zero means either the agent is right or nobody is reading.

**The "check whether your method can return an impossible value" clause produced the best paragraph in the day, exactly as it did on Day 5.** At 120 invoices a day, 120 staffed minutes and 90 seconds of genuine review, the ceiling is `120 ÷ 180 = 0.67` against a floor of 1. **0.67 is not an approval count, and it cannot be rounded** — 1 exceeds the ceiling and 0 is below the floor. The two do not meet, which says per-run approval is not staffable at that volume and no tuning of the design reaches it. The day then names the four honest responses and the one dishonest one (raising *M*, which is asking the customer to staff more approving when the pitch was that this gives time back). I would not have written that paragraph without the clause.

**The input-knob clause was also load-bearing, and in the direction of restraint.** Day 3's **action budget** feeds this method: if the budget is eight writes and the approval count is one, one approval stands in front of eight writes, so the screen must show all eight, which raises *t* and lowers the ceiling. Under the amended rule that is an input knob Day 3 already derived, so it gets one clause naming the interaction and no derivation of its own. Without the clause I would have re-derived Day 3's number inside Day 6, which is exactly the recursion the amendment exists to stop.

---

## Sourcing: what the machine check caught, and a new failure mode

**All 48 quoted strings in the day were machine-checked against fetched bodies on disk. One real defect, which would have shipped.**

**First Round's sentence ends in a comma, not a full stop.** The source reads `What you discover onsite is going to be so different from what was sold in the contract,” she says.` My draft closed the quote with a period inside the quote marks, in **two** places (§4 and §10 Q8). Both now end the quote at `contract` with my punctuation outside. This is the same family as Day 5's `ee/LICENSE` backtick slip and it is invisible to eye-reading — but it is a specifically *journalistic* instance worth naming, because every quote in a magazine feature is followed by `," she says` and therefore almost none of them end in the punctuation you would naturally type.

**And a new failure mode that produced three false misses: a two-column PDF defeats exact matching in both `pdftotext` modes.**

- `pdftotext -layout` preserves the visual columns, which means the **adjacent column's text is spliced between the lines of your quote**. The whitepaper's sentence about auditors reads, in the extracted file, as `...if you need to explain exactly why the system made a` / `specific decision to auditors, regulators, or executives, you want predictable,` / `traceable behavior.` with `3. What are your resource constraints?` and `Limited budget/tokens → Single agents` interleaved. Whitespace normalisation cannot repair that.
- `pdftotext -raw` reads in flow order but **drops inter-word spaces** — the same file yields `operationsintosingle-agent operations`.

Both of my whitepaper quotes and the `100x` characterisation reported as unmatched and **all three are verbatim.** I verified each by printing the raw characters around every occurrence, then built a column-aware corpus by splitting each `-layout` line at the gutter so each column reads continuously. With that in the corpus, the check returns **zero unexplained misses across all 48 strings**. Compounded, because the failure is the dangerous direction: a false miss trains you to stop believing the check.

Of the 48, 23 initially reported as misses and 15 of those were my own dialogue, `alt` text, `<img src>` values and interview questions — consistent with the ~65% the existing note predicts.

**Videos.** Both verified by `yt-dlp` metadata. Video 1 is the course's own source interview (`zXysLUTLjw4`, Greg Isenberg, 3,094 s = 51:34, published 20260720); its four cited timestamps are all **published chapter markers**, re-derived from `start_time` seconds only, per `chapter-markers-carry-an-end-time-too.md`: `11:26`/`17:38`/`27:36`/`32:57` against 686/1058/1656/1977 s. The claim that the `17:38` chapter "runs about three minutes" is 1240 − 1058 = 182 s. Video 2 (`6t7YJcEFUIY`, LangChain, 469 s = 7:49, published 20241214) has **no chapters**, so the day says "no chapter markers — watch the whole thing (8 min)", which §5.4 of the guide blesses. The nineteen-month staleness gap I quote for it is 589 days.

**Links verified by hand: none needed.** All 6 returned clean on the online gate, first attempt, before and after the panel. **But the link check could not have protected this day**, and that is worth one sentence: the single most valuable source on the Varick microsite is behind a click — the per-step detail lives in a JavaScript object in the page, not in the rendered HTML — so a 200 and a tag-stripped body both show you the *least* useful version. I read it out of the `<script>` block. Generalisation for the store: `HTTP 200 is not evidence the quoted text is there` already covers SPA shells; this is the inverse case, where the page is real and the substance is not in the DOM you fetched.

---

## The Day 1 quote is now verifiable, and `FDE_Report`'s version is wrong in three ways

**This is the finding I would most like you to act on, and I could not act on it myself because Day 1's README is a forbidden file.**

Day 1 line 266 carries the course's central thesis marked `⚠️ **Unverified:**`, on the grounds that it "reaches us through `FDE_Report`, which cites secondhand writeups of a podcast rather than a transcript." I fetched the transcript. **The quote is real**, and it is in the day at `43:07` with the auto-caption provenance label the guide requires, with the `.vtt` committed to `.agents/transcripts/zXysLUTLjw4.en.auto.vtt`.

The report's wording differs from the source in three ways, the third of which matters:

1. The report has "only one way something can go right"; he says "only one way **that** something can go right".
2. The report drops the "**So,**" that opens the second sentence.
3. **The report drops a third sentence, and it is the one that belongs to Day 6:** *"If you're solving for all the exceptions, that's where you are worth something as an agent."* The exceptions are this day's whole subject, and the report's truncation removes the only part of the thesis that says what to *do*.

Filed in `docs/residual-review-findings/` for Day 1. One honesty note I put in the day rather than hiding: he says it while walking through **Week 2** of his own plan, about failure handling, not about process mapping — so the day states the context rather than implying he said it about mapping.

**One more `FDE_Report` characterisation I corrected rather than repeated.** The Day 6 row lists the Anthropic whitepaper for "Common enterprise use cases and architecture patterns". It exists and the title is exact, but its first two chapters are customer-supplied outcome claims with no methodology — resolution rates, percentage productivity gains, one platform's agents "corresponding to 100x time-to-value improvement". §4 says plainly that these are not measurements the reader can defend and that quoting one invites the follow-up he cannot answer. The `Free` column is right; treating the chapter as evidence would not be.

---

## Boundary material a later day should get

Nothing cut. Six hand-offs are deliberate.

- **Day 7** — see the Week 1 section above. It inherits a workflow with one named dependency, the stopping-condition spine, and the edit-path question.
- **Day 11 / Day 12** — the day states that a pause makes durable state *mandatory* and quotes LangChain's requirement, then stops. No journalling, no durability modes, no Trigger.dev. `checkpointer` is used as Day 4 defined it and not redefined.
- **Day 13** — "undoing a write, replaying safely" is named as Week 2's in one clause. **No compensating transactions, no saga, no idempotency keys** (`grep` for `saga` and `compensating` returns 0). The day also notes that Week 2 can *lower* Day 6's approval floor, since a step you can reliably reverse does not need permission first — which is a hook for Day 13 rather than a lesson.
- **Day 16** — nothing tagged, no taxonomy (`grep` returns 0).
- **Day 22** — this is the closest boundary and the one to watch. Day 22 owns discovery technique, the Mom Test, and shadowing. Day 6 teaches **what the map must contain** and **how deep is deep enough**, and defers the technique explicitly twice ("How to *ask* the questions that get you the map is the final week's work"). It quotes the sources on the *fact* that someone has to sit with the operator, and gives no questions to ask. **Day 22 should assume the reader knows what a granular map is and what it is for, and owes him only how to extract one.** Note also that Day 22 reuses the same First Round essay; Day 6 took the French-waiter origin, the last-mile definition, one Balaji quote about onsite discovery and the 800% figure, and left the entire hiring-and-scoping two thirds of it alone.
- **Day 23 / Day 27** — Day 23 owns the deterministic-vs-agent-vs-human triage framework, so Day 6 never draws it: it presents one worked workflow and the reversibility boundary, which is a different cut. "Deterministic" appears only as Day 3's vocabulary for a fixed-answer check. Day 27 owns ROI; `grep -i ROI` returns 0, and all three appearances of "business case" are explicit deferrals.

---

## Anything you must decide

1. **Whether to split Day 6.** See the length finding. Four owned subtopics, 9,715 words, 285 words of headroom. My view: shipping one day is right for the reader's continuity, and if any day in the course should be two, it is this one.
2. **Day 1's thesis quote.** The `⚠️ Unverified` marker can come off and the third sentence should go on. Details above and in the residual file. I cannot touch Day 1.
3. **Whether "sit with the operator" is already Day 22's.** I have kept the technique out and the artefact in, and I believe that is the line the issue draws ("Must NOT cover: Discovery *questioning technique*"). If you read the boundary as excluding *any* mention of how the map is obtained, one paragraph in Tier 2 and one clause in §8 would need to go. I would push back on that reading, because a day about granular process maps that never says the map comes from a person reading email all day teaches that it comes from a document.

## B8.5 browser verification

**Skipped.** This slice ships one markdown document and two static SVGs; there is no UI to walk. `index.html` verified programmatically instead — see gate stats.

## B10.5 compound

One new entry and two updates, rather than three new files, because two of the three lessons are instances of classes the store already names:

1. **New — `docs/solutions/conventions/two-column-pdfs-defeat-quote-matching.md`.** The `-layout`-interleaves / `-raw`-drops-spaces pair, the three false misses it produced here, the gutter-split recipe that fixes the corpus, and the reason it matters more than a false *hit*: a check that cries wolf on a correct quote gets switched off.
2. **Update — `machine-check-every-quoted-string.md`.** Adds the journalistic terminal-punctuation case (`," she says` means almost no magazine quote ends in the punctuation you would type) and a pointer to the new PDF entry.
3. **Update — `length-reconciliation-strands-terms.md`.** Adds this slice's measured split: two unit-deletion passes gave 67% of the saving, six compression passes averaged −59 words. Independent reproduction of the note's own −60 figure, which makes it a rule rather than an anecdote.

## Review panel

Three reviewers in parallel, findings and disposition recorded below after the panel ran. Anything deferred or refused is in `docs/residual-review-findings/<head-sha>.md`, staged with the fix commit.
