# Day 04 report

- **Outcome:** shipped
- **Commit:** _pending — filled in below after commit_
- **Gate stats:** 8,782 prose words / 10 Q&A / 2 videos / 11 links / 2 diagrams / 21 vocab terms. PASS **without** `--offline`. One warning, on five paragraphs holding the derived compaction arithmetic (`200,000 − 19,700 − 4,000 = …`) — the style guide's DoD explicitly permits numbers "derived in front of the reader", and the paragraph introducing the derivation carries the models-overview citation.

- **Rules A and B followable as written?** Yes, both. Two notes for whoever writes Day 5.

  Rule A worked exactly as intended, and the "verify, don't assume" clause earned its place: the day quotes Day 2's 19,700-token response budget inside its own compaction derivation, and that figure is only reconstructible because `Response budget`, `System prompt`, `Pass` and `Context window` are all genuinely in `GLOSSARY.md`. I verified all 36 terms the day leans on with a script rather than by eye (output in the transcript); all resolve to §9, `GLOSSARY.md`, or a bolded inline definition. `Transformer` was in none of them — Days 1–3 never used the word — so Day 4 added it as a §9 row rather than leaving it as an inline gloss, because the day quotes an n² claim about it.

  Rule B: the day sets two knobs and gives a method for both. The compaction trigger derives from the window minus the largest single pass that can still follow it, works the small case, and flips (88% → 68% of the window) on whether one model reply may carry several `tool_use` blocks. `k` for retrieval gets a floor from the task and a ceiling from Chroma's distractor result, and says out loud that the number is not defensible until there is a labelled set — which is Week 3's.

  One ambiguity, minor and not blocking: Rule B says "teach no control without a method for setting it", and the day names the output-token cap (4,000) as an input to the compaction sum. That is a control, and giving it a full derivation would nest one method inside another. It is handled with a clause tying it to the task shape ("a short reasoning trace plus a tool call" vs "writes a final report"), not a derivation. If you think nested knobs each owe a full method, this is the place to say so.

- **Links verified by hand because the gate could not reach them:** none. All 11 links returned clean on the online gate run, first attempt. Two redirects were resolved before citing, and the destination is what appears in the day:
  - `research.trychroma.com/context-rot` → `www.trychroma.com/research/context-rot` (also flagged to the reader in §4, since `FDE_Report` uses the old address)
  - `anthropic.com/news/contextual-retrieval` → `anthropic.com/engineering/contextual-retrieval`
  - `docs.langchain.com/oss/python/langgraph/memory` → `docs.langchain.com/oss/python/concepts/memory`

- **Sourcing trap worth recording:** `WebSearch` returned, as if it were a finding of the Chroma report, "a 200K-token window can show serious accuracy loss at 50K tokens of input." That sentence is **not in the report** — `grep -i "50k\|50,000\|accuracy loss"` over the fetched page returns nothing. It would have read as the day's most quotable number. Every quote in this day was taken from a `curl`'d body held on disk, never from a search result or a `WebFetch` summary. Captured in `docs/solutions/`.

- **Boundary material cut that a later day should get:** none cut, but three hand-offs are deliberate and a later writer should collect them.
  - **Day 5** — the compaction method's second half needs the 95th-percentile tokens-added-per-pass distribution, which only exists if every pass was recorded. §6 closes by counting that six of its eight failure rows raise nothing a monitor could catch. Day 5's §1 has an argument pre-built for it.
  - **Day 11/12** — LangGraph's `checkpointer` is named and defined thinly (the thing that saves a thread's state so it can be resumed) and the durable-execution mechanics are explicitly deferred. Day 11 should not re-define the term.
  - **Day 19** — Anthropic's Contextual Retrieval post carries prompt-caching figures that make the long-prompt-instead-of-RAG option cheap. Not used here beyond a single unquantified mention, because cost is Day 19's. The figures are on that page.
  - **Day 20** — sub-agents appear as one row in the four-levers table, described but not argued. The Anthropic essay's multi-agent section is Day 20's material.

- **Anything the user must decide:** two things, neither blocking.
  1. **Length band.** 8,782 words is inside the 9,000–10,000 warn band's lower neighbour, i.e. it passes clean and does not yet owe a justification. Days 1–3 all landed in the warn band (9,533 / 9,652 / 9,901). Review findings will likely push Day 4 over 9,000. I pre-selected the deletions rather than choosing under pressure, per `docs/solutions/conventions/length-reconciliation-strands-terms.md`: §10 Q3 and Q10 come out first (about 180 words, leaving 8 Q&A, still legal), then §5's "What it involves" paragraph. **No §9 row will be deleted** — that is the failure that convention entry exists to prevent.
  2. **Video 2 is 61 minutes long.** The five cited chapters run to about seventeen minutes and the day says so, but it is the longest video the course has recommended. If you want a reading-only course to stay under some per-day video budget, this is the one to cut, and the Chroma 8-minute video carries the day alone.

- **Videos:** both verified by `yt-dlp` metadata (title, channel, duration, upload date) and both cite **published chapter markers only** — so no transcript was fetched, no `.vtt` was committed, and no auto-caption provenance hedge was needed. Per `docs/solutions/conventions/verify-a-source-moved-not-died.md`, chapters beat transcript timestamps wherever both exist.
  - `TUjQuC4ugak` — Chroma, "Context Rot: How Increasing Input Tokens Impacts LLM Performance", 7:56, 2025-07-14
  - `6_BcCthVvb8` — LangChain, "Context Engineering for AI Agents with LangChain and Manus", 1:00:53, 2025-10-14

- **B8.5 browser verification:** skipped. This slice ships a markdown document and two static SVGs; there is no UI to walk. `course/index.html` was verified programmatically instead — both SVGs inlined, both captions present, 8 `<figcaption>`s across 4 days, zero `<p><figure>` nesting, zero `class=` attributes inside any inlined SVG.

- **Self-review defects found and fixed before commit** (recorded because they are the kind the gate cannot see):
  1. §6 claimed "five of the eight produce no error" — the real count is six. Replaced the arithmetic with the six named rows, per the convention entry on count claims rotting.
  2. §7 said the five cited chapters run "about twenty-two minutes"; summing the chapter spans gives 16:55. Corrected to seventeen.
  3. `memory-split.svg` drew its three crossing arrows leaving the region beneath the *system prompt* box. Restructured the top region so the transcript spans the full width and every arrow demonstrably starts or ends there — the system prompt does not change during a run, so it cannot be what compaction or a note-write acts on.
  4. `two-ceilings.svg`'s orange marker could be misread as the point where degradation *begins*. Added a footer line stating there is no onset point.
  5. `namespace` was bolded and used without a definition. Now defined inline.
  6. The `Reranking` §9 row claimed a trade "that goes the right way in both directions" — it costs an extra step and its latency. Corrected.
