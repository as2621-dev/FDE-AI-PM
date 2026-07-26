# Day 05 report

- **Outcome:** shipped
- **Commits:** `8488d96` (the day), then one fresh commit applying the review findings. Nothing pushed. No `--amend` at any point — the report was written and the first commit made *before* the panel was dispatched, and the fixes went on top as a second commit rather than into the first, per `docs/solutions/conventions/never-amend-after-dispatching-a-review-panel.md`. `git show --stat` read back after each commit; only staged files present.
- **Gate stats (final, after review fixes):** **9,903 prose words / 8 Q&A / 2 videos / 18 links / 2 diagrams / 25 vocab terms.** PASS **without** `--offline`. `course/build.py` succeeds; `index.html` carries both SVGs inlined with captions, 10 `<figcaption>`s across 5 days, zero `<p><figure>` nesting, zero `class=` inside any inlined SVG, zero external hosts referenced from any SVG. (Pre-review it was 9,555 words / 9 Q&A / 19 links.)

  Two warnings, both expected:
  1. **9,903 words is over the 9,000 target**, at 66 estimated minutes against a 45–60 minute promise. Justification: the day pays a 25-term vocabulary bill from zero (nobody has met *span*, *trace*, *attribute*, *exporter* or *retention*), and Rule B requires two full methods rather than one, because sampling rate and retention period are independent knobs and neither feeds the other. **This is the tightest a day has landed and it is worth flagging as a process finding rather than a boast.** I drove the first draft from 9,881 down to 9,555 specifically to reserve headroom, because `docs/solutions/conventions/length-reconciliation-strands-terms.md` records Day 3 passing at 9,979 and then failing again when review fixes added 453 words. **My review fixes added 961 words** — more than double Day 3's — and took the day to 10,516, a hard gate failure. Recovering it took eleven further deletions. The 400-word reserve in that solutions note is **too small for a from-zero day whose reviewers hunt correctness**; on this evidence the number should be nearer 900, or the day should be split. If Day 6 is oversized, that is the reason.
  2. **Nine paragraphs "cite a figure with no link".** No decorative citations added. You asked whether this check is now noisy enough to be useless, so I instrumented it rather than guessing — see the section at the end of this report. Short answer: **not useless, and the "9" overstates the problem by about half.** Two narrow fixes would make it precise again.

- **Rules A and B followable as written?** Yes, both, and the amended Rule B mattered.

  **Rule A.** Script-checked 51 terms against §9 and `GLOSSARY.md` rather than eyeballing it — all 51 resolve. Three were caught by running the check rather than by reading: **`exporter`**, used once in §6 and defined nowhere, now a §9 row; **`payload`**, used in the Day 3 crossover paragraph *before* Tier 3 defined it, so that sentence now says "the recorded prompts and tool results"; and **`skeleton` / `payload`** as a pair, which both derived numbers are denominated in and which therefore owed a §9 row rather than an inline bolding. Also glossed `Apache-2.0` and dropped "graduated project" from the OpenTelemetry row, because *graduated* is a CNCF process term that would itself have needed defining.

  **Rule B, and the new subject-vs-input clause decided the shape of Tier 3.** This day has two knobs and neither is an input to the other: the **payload sampling rate** and the **retention period**. Under `38fe1ed` I could not demote either to "one clause", so both get a derivation. Sampling gets the full treatment — floor from the rarest failure class (`p ≥ k ÷ (R × f)`), a worked case at 25%, what it trades in each direction, and how traces replace the guessed failure rate. Retention gets floor (the customer's own detection lag), ceiling (the obligations attached to the payload) and the trade. **The clause was still load-bearing**: the *truncation limit* on a recorded payload is a third knob, and it genuinely does feed the others, so it gets one clause tying it to Day 2's response budget instead of its own derivation. That is exactly the distinction the amended rule draws, and it held.

  One thing worth flagging for the guide rather than fixing here: the sampling derivation's most useful output is that **the floor can exceed 100%**. At a 0.05% failure rate the same sum returns 250%, which is not a rate — it says sampling cannot deliver that failure class at all. Rule B asks what a number trades; it does not ask writers to check whether the method can return an impossible value. On this day that check produced the best paragraph in Tier 3. It may be worth a sentence in Rule B.

- **Links verified by hand because the gate could not reach them:** **one, and it was a false alarm — learning 1 from the brief, hit live.** A gate run after the final commit failed hard with `dead link: https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/registry/attributes/gen-ai.md → HTTP 502`. I did not touch the day. I re-checked by hand: attempt 1 gave 502, attempts 2 and 3 gave 200, and `raw.githubusercontent.com` still serves the file with `gen_ai.usage.input_tokens` present four times. Three consecutive gate runs then passed. **GitHub intermittently 502s on `/blob/` pages for large markdown files** — this one is 43 KB and renders a very wide attribute table — and the URL is fine.

  **A gate finding for you, since this one can fail a slice that has nothing wrong with it.** `check_links` retries with GET only on `403`, `405` and `501`. A `502`/`503`/`504` is by definition a transient server-side error, and it currently goes straight to a hard failure with no retry. Adding 5xx to that retry tuple — or one retry after a short sleep on any 5xx — would remove a whole class of spurious slice failures. Left alone, the next writer to hit it will either "fix" a live link or waste a round trip proving it is alive, which is exactly what learning 1 exists to prevent and what I just spent one on.

  All 18 links otherwise returned clean on the online gate run, first attempt, both before and after review. (19 pre-review; the moved-stub link to `opentelemetry.io/docs/specs/semconv/gen-ai/` was removed as a review fix.) I resolved redirects before citing and the day carries the destinations, not the addresses I started from:
  - `docs.smith.langchain.com/observability` → `docs.langchain.com/langsmith/observability`
  - `braintrust.dev/docs/guides/traces` → `www.braintrust.dev/docs/instrument`
  - `weave-docs.wandb.ai/` → `docs.wandb.ai/weave`
  - `langfuse.com/docs/observability/data-model` serves the page titled *Concepts* — cited as such rather than as "the data model page".

  Both videos verified by `yt-dlp` metadata, and **all 7 timestamps are published chapter markers**, so no transcript was fetched, no `.vtt` committed and no auto-caption hedge needed. **Two of the seven were wrong in the committed version and the panel caught them — see the review section.** Final, re-derived from `start_time` only: `0:00`/`0:54`/`5:55`/`11:15` against 0/54/355/675 s on video 1, and `0:49`/`2:33`/`7:00` against 49/153/420 s on video 2, cross-checked against video 1's own `// CHAPTERS //` description block. The claim that the Langfuse tracing chapter "runs about a minute and three quarters" is 153 − 49 = 104 s.

  **Every verbatim quote machine-checked against a fetched body on disk** (64 quoted strings, of which 22 are source quotes and the rest are my own dialogue). Two failures found this way, both of which would have shipped:
  - Langfuse's `LICENSE` says content under `ee/` "is licensed under the license defined in **"ee/LICENSE"**" — with double quotes in the source, not the backticks my draft rendered. Quote now stops before the inner quote.
  - §7 said `"spans nest to reflect the execution flow"` in quote marks. Braintrust's actual sentence is "Spans nest inside each other to reflect your application's execution flow." Quote marks dropped.

- **Boundary material a later day should get.** Nothing cut; four hand-offs are deliberate.
  - **Day 6** — nothing needed, and one correction to an earlier draft of this report: it claimed §5 ends on "explain one run out loud to somebody annoyed", setting up the human-approval pause. **That paragraph was one of the eleven units deleted to get back under the ceiling, so the claim was stale by the time I committed.** I found it by grepping this report's own assertions against the shipped day, which is the check `length-reconciliation-strands-terms.md` prescribes and which I had only been applying to the day, not to the report. §5 now ends on the paper version of the exercise. Day 6 inherits nothing from it and needs nothing.
  - **Day 10 / Day 16** — §1 says the taxonomy comes later *without naming a day*, because forward links to unwritten days are barred. §6's last row is explicitly the row tracing cannot fix, and it points at Week 3 rather than at a number. **Day 16 owns "tagging traces"; this day gives it the trace and never tags anything.**
  - **Day 17 / Day 18** — the phrase "known-correct answers to compare against" appears three times and is deliberately never called a golden dataset or an eval, even though `GLOSSARY.md` already carries `Golden dataset` from the course-wide table. Evals are named in §4 only as a *product feature* of the managed tools, with no method.
  - **Day 19** — cost appears only as a direction ("sample low and you pay less"). No price, no rate, no cost-per-query. `gen_ai.usage.cache_read.input_tokens` is quoted as evidence about what the schema breaks out, with prompt caching's economics left alone.

- **B10.5 compound:** two entries.
  1. `docs/solutions/conventions/chapter-markers-carry-an-end-time-too.md` — generalises the class the panel exposed three times in this slice: *a correct value read from the wrong field of a correct source*, which defeats every check the course has because provenance stays intact. Carries the chapter-extraction recipe, the diagram bar-width rule, and the "read the registry's `brief` even when the attribute name looks obvious" rule.
  2. `docs/solutions/conventions/machine-check-every-quoted-string.md` — written at your request, and you were right that it belonged in the store. `search-summaries-invent-findings.md` records *quote only from a fetched body*; this is the mechanisable version, with the script, the two real defects it caught, and the four things that make its output readable rather than alarming (normalise backticks on **both** sides or you get false misses; expect ~65% of misses to be your own dialogue and read every line anyway; put `LICENSE` files and video descriptions in the corpus; shorten a quote rather than eliding it, because an ellipsis defeats exact matching). The strongest argument for it: because I ran it first, the panel's own quote pass returned **nothing further** across 22 source quotes — and that silence is worth more than a clean finding list.

- **Anything the user must decide:** four things now.
  1. **The 400-word review reserve is too small.** See the length note above: my fixes added 961 words. Either `length-reconciliation-strands-terms.md` should say ~900, or from-zero days in this subject area are simply oversized for a 10,000-word ceiling. Your call, and it affects Day 6 onward.
  2. **Day 2 needs a one-word fix I am not allowed to make**, and it is the higher-leverage place to make it than anywhere in Day 5. Details in `docs/residual-review-findings/8488d96.md` items 1–3: Day 2 says 19,700 is "per result", Day 4 says per pass, Day 4 is right, and Day 4's own *report* also carries the wrong version — which matters because that report is the specification the next day builds against.
  3. **A ⚠️ Unverified marker on one of `FDE_Report`'s own claims.** The report says LangSmith "is deepest for LangChain/LangGraph". I could not find a vendor-neutral source establishing depth-of-support rankings between LangSmith, Braintrust and Weave, and a vendor's own docs cannot settle it. §4 states the coupling as real, marks the ranking unverified, and tells the reader to say so rather than assert it. If you would rather the day simply repeated the report, say so and I will change it — but I think marking it is right, per the standing note about not laundering vendor positioning.
  4. **Two of `FDE_Report`'s licence characterisations are wrong, and I corrected both in §4.** See below. Both corrections are inside my own day, so no forbidden file was touched, but the report itself still says the old thing.

- **The two findings in `FDE_Report` I corrected rather than repeated.** These are the highest-value things in the day, because a reader who repeated either in a customer meeting would be contradicted by their legal team.
  1. **Langfuse is not simply "MIT".** The report's Day 5 row says "(open source, MIT)". The `LICENSE` file carves out `ee/`, `web/src/ee/` and `worker/src/ee/` under a separate enterprise licence and makes only the remainder MIT-Expat. GitHub's own API reports the repository licence as `NOASSERTION`, which is the machine-readable version of the same fact. Self-hosting the core is genuinely permissive; some features are not.
  2. **Arize Phoenix is not open source in the sense a customer's counsel means.** The report calls it "Open-source tracing/eval". Its licence is **Elastic License 2.0**, which states "You may not provide the software to third parties as a hosted or managed service, where the service provides users with access to any substantial set of the features or functionality of the software" — verified twice, from the repository `LICENSE` and from `arize-phoenix` 19.6.0 on PyPI declaring `Elastic-2.0`. That is source-available. OpenInference, the instrumentation half, is separately Apache-2.0, so the standard is reusable even where the viewer is not. The report's `Free/Paid` column is not wrong; its *open-source* characterisation is, and §5 rule 7 of the style guide makes a characterisation a claim.

- **Diagram defects I caught in my own work before review** (§5 rule 8 — read the SVG back in words). The first version of `span-tree.svg` had two:
  1. **It drew `execute_tool` as a child of `chat`.** In the conventions a tool runs *after* the model call returns, so they are siblings under `invoke_agent`, not nested. The diagram taught the wrong causal model and the caption ("indentation is the record of which pass asked for which tool") asserted it in words. Rebuilt as a two-column trace-viewer layout: tree on the left, time bars on the right, five siblings in time order. The link between a tool and the reply that requested it is now correctly attributed to `gen_ai.tool.call.id` rather than to the indentation.
  2. **The bar widths contradicted their own duration labels.** An 86-pixel bar labelled `0.4 s` sat next to a 150-pixel bar labelled `2.9 s`. Every bar is now proportional at 36 px/s against a 15.0 s root, and the child durations sum to 14.8 s inside it. Two prose figures and one §6 row moved from `1.9 s` to `2.4 s` to match.

- **B8.5 browser verification:** skipped. This slice ships one markdown document and two static SVGs; there is no UI to walk. `index.html` verified programmatically instead — see gate stats above.

- **Review panel: 3 reviewers, ~45 findings, ~34 applied, 6 deferred or refused** with reasons in `docs/residual-review-findings/8488d96.md`. It was a productive panel and the top four findings were all things a reader would have been caught on.

  1. **Two of the seven timestamps pointed at the wrong chapter.** I converted the chapter objects' `end_time` instead of `start_time`, so `9:10` and `13:42` should have been `5:55` and `11:15` — and `9:10` is the *start of the next chapter*, which the same paragraph told the reader to skip. Two reviewers found it independently by re-fetching the metadata. Every timestamp was still labelled "(chapter marker)" and every one was genuinely sourced, so `check_day.py` was happy: a correct number read from the wrong field of the right source. Compounded.
  2. **`gen_ai.conversation.id` is not a run identifier, and my own vocabulary table said so.** The registry defines it as "The unique identifier for a conversation (session, thread)", and Tier 3's table maps it to *session* / *thread* — while Tier 2 item 4 called it the run identifier and hung Day 4's per-run grouping on it. All three reviewers caught it. The run identifier is the OpenTelemetry **trace ID**, which is core OTel rather than a GenAI attribute; Tier 1 now names it, and it also fixes Reviewer 2's separate point that nothing in the day said how you get from a customer's email to a trace.
  3. **`gen_ai.response.finish_reasons` cannot carry Day 4's required stop reason, and I claimed it could.** It reports why the *model* stopped writing: `length` means the output cap, not window overflow. Window overflow fails the request and lands as `error.type`; a run stopped by the **max-step cap** reads `stop`, identical to one that finished. So my sentence "this is the field that stops you" was false, and it contradicted my own §5. Day 4's "plus one distinct stop reason" is now delivered honestly: *finished*, *hit the step cap* and *overflowed the window* have to be one custom field on the root span. This was the single most valuable finding, because it is the inherited requirement.
  4. **The `input_tokens` double-count was misdiagnosed.** `gen_ai.usage.input_tokens` never contains that pass's own reply, so my "if you feed it a figure that includes the model's own reply" was wrong about the attribute. The real trap is the *difference* between consecutive passes' figures, which does contain the previous reply. Corrected, and it is a better paragraph for being precise about where the reply enters.

  Also applied: `Conditionally Required` added as the fourth requirement level (it is the most common one in the spec, and it governs `error.type` and `conversation.id`, both fields the day relies on); `gen_ai.input.messages` and `gen_ai.output.messages` named as the other two `Opt-In` attributes, which are the largest part of the payload and the basis of Tier 3's leak argument — Reviewer 2 was right that the day argued about the prompt being in the record without ever naming the field; §8's "a tool span **under** the pass that asked for it" corrected to *after*, since both my diagrams and the agent-spans doc make them siblings; the `250%` result restated as *two and a half weeks to reach five examples* rather than "per example", which was a unit error; the sampling floor labelled an **expected** count rather than a guarantee; `k` declared a judgment input with a direction to move it; the retention floor's hidden 14-day escalation step made explicit and attributed to the customer rather than invented; the skeleton's year-long retention given an actual floor (the longest comparison you need across it) instead of being asserted three times; the claim that the two halves can be retained separately qualified with the fact that it is something you build rather than a setting you flip; Day 3's **exfiltration** row characterised correctly (it was *already* the no-tool case, so my contrast was backwards); the moved-stub link to `opentelemetry.io/docs/specs/semconv/gen-ai/` removed, since it renders the same "Moved" page Tier 2 warns about; `gen-ai-agent-spans.md` added to §4's read list, because the outer span in my own first diagram is documented there and I had cited only `gen-ai-spans.md`; the retrieval limit in Tier 3 rewritten as four named fields after Reviewer 2 showed it contradicted itself; §1's replay nuance added, because "there is only the recording or nothing" overstated it — with payloads captured you *can* re-send the recorded input and measure how often the failure recurs, which is a measurement rather than a reproduction, and which gives payload capture a second justification; the diagram subtitle scoped to `gen_ai.` attributes, since `error.type` is `Stable`; a gloss on `200` in the video quote; a gloss on *boolean*; "exactly five token attributes" narrowed to *token-usage*; §6's row count claim replaced with naming; and the `default-vs-deliberate` footer rewritten, because Reviewer 3 correctly showed the diagram splits *standard vs custom* while Tier 3 splits *skeleton vs payload* — two different cuts, and the day had claimed they were the same one.

  **One self-inflicted error introduced during the fixes and caught by re-running the gate:** the day went to 10,516 words, a hard failure, before the eleven deletions that brought it back. Re-run the gate after applying findings.

---

## How I resolved the OpenTelemetry question Day 4 left open

**Day 4 could not fetch the conventions and correctly refused to answer from memory. The answer is: the standard gives you input and output totals only. Items 1 and 2 of Day 4's list are custom attributes, and the day says so out loud.**

**Why Day 4's fetch failed, and what worked.** The rendered docs page at `opentelemetry.io/docs/specs/semconv/gen-ai/` is JavaScript-rendered, which is what defeated `curl`. But the reason a raw-markdown fetch against `open-telemetry/semantic-conventions` *also* returns nothing useful is more interesting: **the GenAI conventions no longer live in that repository.** `docs/gen-ai/README.md` there is now a stub reading `# Moved: Generative AI semantic conventions`, pointing at a separate repository, `open-telemetry/semantic-conventions-genai`. Anyone following Day 4's instinct to "try the raw spec in the semantic-conventions repo" lands on the stub. The sources I actually read, all fetched to disk and grepped:

```
https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/model/gen-ai/registry.yaml
                                                                              docs/registry/attributes/gen-ai.md
                                                                              docs/gen-ai/gen-ai-spans.md
                                                                              docs/gen-ai/gen-ai-agent-spans.md
                                                                              docs/gen-ai/gen-ai-metrics.md
                                                                              docs/gen-ai/README.md
```

**The answer, attribute by attribute.** The registry defines exactly five token attributes and no others:

| Attribute | What it is |
|---|---|
| `gen_ai.usage.input_tokens` | "The number of tokens used in the GenAI input (prompt)" — the whole assembled prompt |
| `gen_ai.usage.output_tokens` | "The number of tokens used in the GenAI response (completion)" |
| `gen_ai.usage.cache_read.input_tokens` | a sub-total, which "SHOULD be included in `gen_ai.usage.input_tokens`" |
| `gen_ai.usage.cache_creation.input_tokens` | ditto |
| `gen_ai.usage.reasoning.output_tokens` | a sub-total of `output_tokens` |

Nothing separates tool results out of the input total. So Day 4's field 1 (**tool-result tokens per result**) has no attribute and no near-miss. Field 2 (**tool-result count per pass**) has a near-miss that is worth naming precisely, because "OTel has that" is the wrong answer: `gen_ai.invoke_agent.tool_calls` exists, but it is a **metric**, a histogram of "The number of tool calls a GenAI agent makes during a single invocation" — scoped to a whole run, not to a pass, and aggregated rather than attached to a span. It cannot answer whether *one reply* shared the response budget across three results.

**Two of Day 4's fields are more standard than it expected**, which is worth recording so nobody builds a custom attribute they did not need:
- Field 3, `output_tokens`, is standard outright.
- Field 4's run identifier is standard as `gen_ai.conversation.id`. Only the **pass index** is custom.
- Field 6's compaction event is standard *as a flag*: `gen_ai.conversation.compacted`, a boolean the spec says instrumentations "SHOULD set it to `true` only when they can reliably determine that context compaction was applied". The prompt sizes either side of it are not.
- Field 7's model is standard, as `gen_ai.request.model` / `gen_ai.response.model`. The distinct stop reason is standard-ish, as `gen_ai.response.finish_reasons`, whose own spec examples are `[stop]` and `[stop, length]`.

**The bigger finding, which Day 4 could not have anticipated and which the day now leads with.** The two attributes carrying a tool call's *contents* — `gen_ai.tool.call.arguments` and `gen_ai.tool.call.result` — exist, and both carry requirement level **`Opt-In`**, with the spec's own warning "This attribute may contain sensitive information". So a fully compliant trace that changes no defaults records that a tool ran, under what name, for how long, without error, and **not what it returned**. That is a stronger version of Day 4's point than Day 4 asked for: the problem is not only that a custom field is needed for token accounting, it is that the single most useful field in the whole trace is off by default, and the reason is data protection rather than oversight. Tier 3 hangs the Day 3 crossover on it, and it is the day's second interview answer.

**One further honesty item, and the reason "we're OTel-compliant" gets a sentence.** The conventions' own index gives their status as `**Status**: [Development]`. In `docs/registry/attributes/gen-ai.md` the string `Development` appears 100 times and `Stable` zero times. Every GenAI attribute may still be renamed. The day says so and tells the reader to pin the names he depends on.

## Were Day 4's seven fields right?

**Yes — I would drop none of them, and I shipped five of the seven as an explicit list plus two more as a following paragraph.** Two amendments, neither a disagreement.

1. **Fields 4 and 5 collapse into one.** Day 4 listed `prompt_tokens` (field 4) and "a run identifier and a pass index" (field 5) separately. Once the trace is a span tree, `gen_ai.usage.input_tokens` *is* the prompt size for that pass and arrives free, so field 4 is not a thing you build; and the pass index is the thing you build. Listing them apart made the free one look expensive. My §3 Tier 2 list is therefore five numbered items, not seven, with the model and the stop reason in the paragraph after — because those two are standard and the numbered list is the *build* list. **No field was dropped: all seven plus the distinct stop reason appear.**

2. **Field 5's run identifier deserved to be split from the pass index for a different reason than Day 4 gave.** Day 4 grouped them because both are needed for the per-pass-to-per-run conversion. True, and one of them is standard and the other is not, which is the more actionable split for a reader deciding what to instrument.

**On the distinct stop reason (the "plus one"), Day 4 slightly understated its own case.** It asked that "ended because the window overflowed" be distinguishable from "finished" and from "the step cap fired". The conventions give you `finish_reasons` with `length` as a published example value, so the first two come free; **the step cap is the one that does not**, because it is enforced by your code and the model never sees it. So of Day 4's three stop reasons, two are standard and the third is custom — the opposite of the split a reader would guess.

**Nothing I would call over-specified.** The one field I expected to argue with was field 6's "prompt size immediately before and after" compaction, which looked like bookkeeping. It is not: with only the boolean flag, a 95th-percentile computed across a run mixes pre- and post-compaction passes, and the trigger is invisible in its own data. Day 4 was right and its reason was the right reason.

---

## Is `check_unsourced_figures` noisy enough to be useless?

You asked, and it is a gate question rather than a day question, so here is the evidence rather
than an impression. I re-ran the check's own logic across all five days and printed what it fires on.

**Hits per day: Day 1 → 0, Day 2 → 0, Day 3 → 0, Day 4 → 6, Day 5 → 9.**

That is the first thing worth knowing, and it changed my answer. The check is **silent on three of
five days**, so it is not a warning that fires on every page and trains writers to ignore it. It
fires on *derivation-heavy* days, which is a much narrower class than the raw trend `0,0,0,6,9`
suggests. The reason is that `FIGURE_PATTERN` only matches a percentage or a currency-with-digit —
it never fires on `19,700 tokens`, `31 days` or `4,000 runs a week`. Day 5 has three derived
numbers, and all three land as percentages.

**My verdict: keep it, and fix two things.** It is not useless. But of Day 5's nine hits, **only
one is arguably the check doing its job**, and that is a precision problem worth fixing before the
count climbs further.

Breaking the nine down by what actually triggered them:

| Kind | Count | Example | Is the warning right? |
|---|---|---|---|
| Arithmetic derived in the paragraph | 4 | `5 ÷ 20 = 0.25, so keep payloads on 25%` | **No** — the DoD explicitly permits this |
| An illustrative or hypothetical figure | 2 | `Error rate: 0.8%` as an example of what a metric is; `"we sample 10%" is not an answer either` | **No** — not a claim about the world at all |
| A policy stated as a percentage | 2 | `keep 100% of runs that errored` | **No** — a recommendation, with nothing citable behind it |
| A derived figure restated without its derivation | 1 | §10's `roughly 40% across ten passes, not the 5% per pass` | **Defensible** — the derivation is named in the same answer, but a reader landing there cold sees a bare percentage |

**Two narrow fixes, in order of value.**

1. **Exempt a paragraph whose figure is accompanied by arithmetic that resolves inside it** — the
   paragraph contains `=`, `÷`, `×`, `−`, or a spelled-out "divided by"/"minus". That removes 4 of
   Day 5's 9 and, by inspection, most of Day 4's 6, and it removes exactly the category the DoD
   already blesses. This is the one that matters: as written, the check is **guaranteed** to fire on
   the single highest-value paragraph of every Rule B day, which is the mechanism by which a warning
   becomes wallpaper.
2. **Count distinct figures, not paragraphs.** Day 5's nine paragraphs contain about five distinct
   numbers. Three of them recur across Tier 3 → §8 → §10 because the style guide *asks* for a
   number to be derived once and reused in the interview answer and the self-test. So a
   well-structured day scores roughly three times worse than a badly-structured one with the same
   sourcing. `9` is largely an artefact of the unit of measurement.

**What I would not do.** Do not make it a hard failure, and do not broaden `FIGURE_PATTERN` to plain
integers. The style guide already documents why broadening fails: a check wide enough to catch
"often between five and twenty-five" would fire on "five stations" and "two ovens" on every page and
be muted within a week. The current narrow trigger is the right instinct; it just needs the
derivation exemption it never got.

**The honest caveat on my own recommendation.** Two firing days is a thin basis for a gate change,
and if Days 6–10 keep climbing then the mute-and-ignore failure arrives regardless of whether I am
right about the categories. The cheap insurance is fix 2 on its own — recount by distinct figure —
because it costs nothing in detection and immediately tells you whether the trend is real growth in
uncited figures or just more cross-references to the same three numbers.

**One thing the check cannot see, and it is the case it exists for.** An *imported* percentage — a
vendor's "reduces failed retrievals by 49%" — with no link. Day 5 contains zero of those, which is
why all nine hits are false-positive-shaped. So on this day the check found nothing, and I would
still keep it: a day that quotes a vendor's headline percentage uncited is the exact failure Day 1
shipped, and this is the only automated thing standing in front of it.
