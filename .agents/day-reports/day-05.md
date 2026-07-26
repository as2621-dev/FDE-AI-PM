# Day 05 report

- **Outcome:** shipped
- **Commit:** one fresh commit on top of `f6df53b`. Nothing pushed. No `--amend` at any point — the report is written and the commit made *before* the panel is dispatched, per `docs/solutions/conventions/never-amend-after-dispatching-a-review-panel.md`.
- **Gate stats (pre-review):** **9,555 prose words / 9 Q&A / 2 videos / 19 links / 2 diagrams / 25 vocab terms.** PASS **without** `--offline`. `course/build.py` succeeds; `index.html` carries both SVGs inlined with captions, 10 `<figcaption>`s across 5 days, zero `<p><figure>` nesting, zero `class=` inside any inlined SVG, zero external hosts referenced from any SVG.

  Two warnings, both expected:
  1. **9,555 words is over the 9,000 target.** Justification: the day pays a 25-term vocabulary bill from zero (nobody has met *span*, *trace*, *attribute*, *exporter* or *retention*), and Rule B requires two full methods rather than one, because sampling rate and retention period are independent knobs and neither feeds the other. I deliberately drove the first draft down from **9,881** by deleting whole units — §5's third paragraph, a §6 row, a §10 Q&A, LangSmith's 25,000-run limit, the Langfuse star count, and four restating clauses — specifically to reserve headroom, because `docs/solutions/conventions/length-reconciliation-strands-terms.md` records that Day 3 passed at 9,979 and then failed again when review fixes added 453 words. **445 words of headroom going into review**, and I did not cut a single §9 row to buy it.
  2. **Nine paragraphs "cite a figure with no link".** All nine are the sampling and retention arithmetic derived in front of the reader, which the DoD permits. No decorative citations added.

- **Rules A and B followable as written?** Yes, both, and the amended Rule B mattered.

  **Rule A.** Script-checked 51 terms against §9 and `GLOSSARY.md` rather than eyeballing it — all 51 resolve. Three were caught by running the check rather than by reading: **`exporter`**, used once in §6 and defined nowhere, now a §9 row; **`payload`**, used in the Day 3 crossover paragraph *before* Tier 3 defined it, so that sentence now says "the recorded prompts and tool results"; and **`skeleton` / `payload`** as a pair, which both derived numbers are denominated in and which therefore owed a §9 row rather than an inline bolding. Also glossed `Apache-2.0` and dropped "graduated project" from the OpenTelemetry row, because *graduated* is a CNCF process term that would itself have needed defining.

  **Rule B, and the new subject-vs-input clause decided the shape of Tier 3.** This day has two knobs and neither is an input to the other: the **payload sampling rate** and the **retention period**. Under `38fe1ed` I could not demote either to "one clause", so both get a derivation. Sampling gets the full treatment — floor from the rarest failure class (`p ≥ k ÷ (R × f)`), a worked case at 25%, what it trades in each direction, and how traces replace the guessed failure rate. Retention gets floor (the customer's own detection lag), ceiling (the obligations attached to the payload) and the trade. **The clause was still load-bearing**: the *truncation limit* on a recorded payload is a third knob, and it genuinely does feed the others, so it gets one clause tying it to Day 2's response budget instead of its own derivation. That is exactly the distinction the amended rule draws, and it held.

  One thing worth flagging for the guide rather than fixing here: the sampling derivation's most useful output is that **the floor can exceed 100%**. At a 0.05% failure rate the same sum returns 250%, which is not a rate — it says sampling cannot deliver that failure class at all. Rule B asks what a number trades; it does not ask writers to check whether the method can return an impossible value. On this day that check produced the best paragraph in Tier 3. It may be worth a sentence in Rule B.

- **Links verified by hand because the gate could not reach them:** **none.** All 19 returned clean on the online gate run, first attempt. I resolved redirects before citing and the day carries the destinations, not the addresses I started from:
  - `docs.smith.langchain.com/observability` → `docs.langchain.com/langsmith/observability`
  - `braintrust.dev/docs/guides/traces` → `www.braintrust.dev/docs/instrument`
  - `weave-docs.wandb.ai/` → `docs.wandb.ai/weave`
  - `langfuse.com/docs/observability/data-model` serves the page titled *Concepts* — cited as such rather than as "the data model page".

  Both videos verified by `yt-dlp` metadata, and **all 7 timestamps are published chapter markers**, so no transcript was fetched, no `.vtt` committed and no auto-caption hedge needed. I converted chapter `start_time` seconds to `M:SS` by hand and re-checked each: `0:00`/`0:54`/`9:10`/`13:42` against 0/54/550/822 s, and `0:49`/`2:33`/`7:00` against 49/153/420 s. The claim that the Langfuse tracing chapter "runs about a minute and three quarters" is 153 − 49 = 104 s.

  **Every verbatim quote machine-checked against a fetched body on disk** (64 quoted strings, of which 22 are source quotes and the rest are my own dialogue). Two failures found this way, both of which would have shipped:
  - Langfuse's `LICENSE` says content under `ee/` "is licensed under the license defined in **"ee/LICENSE"**" — with double quotes in the source, not the backticks my draft rendered. Quote now stops before the inner quote.
  - §7 said `"spans nest to reflect the execution flow"` in quote marks. Braintrust's actual sentence is "Spans nest inside each other to reflect your application's execution flow." Quote marks dropped.

- **Boundary material a later day should get.** Nothing cut; four hand-offs are deliberate.
  - **Day 6** — nothing needed. §5's exercise ends on "explain one run out loud to somebody annoyed", which sets up the human-approval pause without teaching it.
  - **Day 10 / Day 16** — §1 says the taxonomy comes later *without naming a day*, because forward links to unwritten days are barred. §6's last row is explicitly the row tracing cannot fix, and it points at Week 3 rather than at a number. **Day 16 owns "tagging traces"; this day gives it the trace and never tags anything.**
  - **Day 17 / Day 18** — the phrase "known-correct answers to compare against" appears three times and is deliberately never called a golden dataset or an eval, even though `GLOSSARY.md` already carries `Golden dataset` from the course-wide table. Evals are named in §4 only as a *product feature* of the managed tools, with no method.
  - **Day 19** — cost appears only as a direction ("sample low and you pay less"). No price, no rate, no cost-per-query. `gen_ai.usage.cache_read.input_tokens` is quoted as evidence about what the schema breaks out, with prompt caching's economics left alone.

- **Anything the user must decide:** two things, both small.
  1. **A ⚠️ Unverified marker on one of `FDE_Report`'s own claims.** The report says LangSmith "is deepest for LangChain/LangGraph". I could not find a vendor-neutral source establishing depth-of-support rankings between LangSmith, Braintrust and Weave, and a vendor's own docs cannot settle it. §4 states the coupling as real, marks the ranking unverified, and tells the reader to say so rather than assert it. If you would rather the day simply repeated the report, say so and I will change it — but I think marking it is right, per the standing note about not laundering vendor positioning.
  2. **Two of `FDE_Report`'s licence characterisations are wrong, and I corrected both in §4.** See below. Both corrections are inside my own day, so no forbidden file was touched, but the report itself still says the old thing.

- **The two findings in `FDE_Report` I corrected rather than repeated.** These are the highest-value things in the day, because a reader who repeated either in a customer meeting would be contradicted by their legal team.
  1. **Langfuse is not simply "MIT".** The report's Day 5 row says "(open source, MIT)". The `LICENSE` file carves out `ee/`, `web/src/ee/` and `worker/src/ee/` under a separate enterprise licence and makes only the remainder MIT-Expat. GitHub's own API reports the repository licence as `NOASSERTION`, which is the machine-readable version of the same fact. Self-hosting the core is genuinely permissive; some features are not.
  2. **Arize Phoenix is not open source in the sense a customer's counsel means.** The report calls it "Open-source tracing/eval". Its licence is **Elastic License 2.0**, which states "You may not provide the software to third parties as a hosted or managed service, where the service provides users with access to any substantial set of the features or functionality of the software" — verified twice, from the repository `LICENSE` and from `arize-phoenix` 19.6.0 on PyPI declaring `Elastic-2.0`. That is source-available. OpenInference, the instrumentation half, is separately Apache-2.0, so the standard is reusable even where the viewer is not. The report's `Free/Paid` column is not wrong; its *open-source* characterisation is, and §5 rule 7 of the style guide makes a characterisation a claim.

- **Diagram defects I caught in my own work before review** (§5 rule 8 — read the SVG back in words). The first version of `span-tree.svg` had two:
  1. **It drew `execute_tool` as a child of `chat`.** In the conventions a tool runs *after* the model call returns, so they are siblings under `invoke_agent`, not nested. The diagram taught the wrong causal model and the caption ("indentation is the record of which pass asked for which tool") asserted it in words. Rebuilt as a two-column trace-viewer layout: tree on the left, time bars on the right, five siblings in time order. The link between a tool and the reply that requested it is now correctly attributed to `gen_ai.tool.call.id` rather than to the indentation.
  2. **The bar widths contradicted their own duration labels.** An 86-pixel bar labelled `0.4 s` sat next to a 150-pixel bar labelled `2.9 s`. Every bar is now proportional at 36 px/s against a 15.0 s root, and the child durations sum to 14.8 s inside it. Two prose figures and one §6 row moved from `1.9 s` to `2.4 s` to match.

- **B8.5 browser verification:** skipped. This slice ships one markdown document and two static SVGs; there is no UI to walk. `index.html` verified programmatically instead — see gate stats above.

- **Review panel:** three reviewers dispatched after this file was written and the commit made. Findings and their disposition are appended below.

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
