# Day 04 report

- **Outcome:** shipped
- **Commit:** `86f7bd6` for the first pass, final work in the commit on top of `38fe1ed`. Nothing pushed.

  **Concurrency incident, worth your attention.** While my review panel was running you committed `38fe1ed` ("docs(style-guide): rule the nested-knob case under Rule B") on top of my `86f7bd6`. I then ran `git commit --amend` to fold the review fixes into what I believed was my own commit — and amended **yours**, absorbing your style-guide change into my commit and discarding your message. Caught it because `git show --stat` listed `course/_meta/STYLE_GUIDE.md`, a file this slice is forbidden to touch. Recovered with `git reset --soft 38fe1ed`, which restored your commit as HEAD with the style guide byte-identical to it, then committed my work fresh on top. **Nothing of yours was lost and the style guide carries no edit of mine.** The lesson for the protocol: a slice-builder must not `--amend` after handing work to a review panel, because HEAD can move while the panel runs. Compounded to `docs/solutions/`.
- **Gate stats (final, after review fixes):** **9,472 prose words / 8 Q&A / 2 videos / 11 links / 2 diagrams / 22 vocab terms.** PASS **without** `--offline`. `course/build.py` succeeds; `index.html` carries both SVGs inlined with captions, 8 `<figcaption>`s across 4 days, zero `<p><figure>` nesting, zero `class=` inside any inlined SVG.

  Two warnings, both expected and both left deliberately:
  1. **9,472 words is over the 9,000 target.** Justification the style guide asks for: the overflow is Rule A and Rule B obligations the review panel surfaced, not restatement. Specifically the page→token conversion (400 pages ≈ 160,000 tokens, checked against the day's own derived trigger), the two-knobs interaction, the oracle caveat on Chroma's focused condition, and the per-pass→per-run risk conversion. I paid for all of it by deleting whole units rather than rewording: two §10 Q&A, §5's setup paragraph, a §2 summary paragraph, a Tier 1 signpost. The day peaked at 9,897 after applying findings and came down to 9,472. It is the **shortest of the four days written so far** (Days 1–3: 9,533 / 9,652 / 9,901).
  2. **Six paragraphs "cite a figure with no link".** All six are the compaction arithmetic, derived in front of the reader, which the DoD explicitly permits. I did not add decorative citations to silence it.

- **Rules A and B followable as written?** Yes, both, and both earned their keep. Two notes.

  **Rule A's "verify, don't assume" clause caught a real hole.** I script-checked all 36 terms the day leans on against §9 and `GLOSSARY.md` rather than eyeballing it. `Transformer` was in neither and Days 1–3 never used the word, so it became a §9 row — the day quotes an n² claim about it. Reviewer 3 then found one I had missed: **`output cap`** was quoted about (4,000 tokens, and again in §10) and defined nowhere. Now a §9 row. Both are the exact failure shape the rule describes.

  **The one ambiguity I hit in Rule B, now resolved by you mid-slice.** Rule B says teach no control without a method for setting it, and the compaction trigger's sum takes the *output cap* as an input — so the method for one knob contained another knob. I flagged it in the first version of this report as needing your ruling. You ruled in `38fe1ed`: subject knobs owe the full method, input knobs owe enough to pick and defend. Day 4 already did that, and the guide now cites its clause as the example. **No change required, and the rule is followable as it now stands.**

- **Links verified by hand because the gate could not reach them:** **none.** All 11 returned clean on the online gate run, first attempt, both before and after review. Three redirects were resolved before citing and the destination is what appears in the day:
  - `research.trychroma.com/context-rot` → `www.trychroma.com/research/context-rot` (disclosed to the reader in §4, since `FDE_Report` names the old address in prose)
  - `anthropic.com/news/contextual-retrieval` → `anthropic.com/engineering/contextual-retrieval`
  - `docs.langchain.com/oss/python/langgraph/memory` → `docs.langchain.com/oss/python/concepts/memory`

  Both videos verified by `yt-dlp` metadata, and **all 10 timestamps are published chapter markers** — so no transcript was fetched, no `.vtt` committed, and no auto-caption hedge needed. Reviewer 3 independently re-verified every chapter start against the seconds in the metadata.

- **Boundary material cut that a later day should get:** nothing cut, but four hand-offs are deliberate.
  - **Day 5** — the compaction method's refinement step needs a 95th-percentile tool-result distribution, which exists only if every pass was recorded. §6 now ends by naming the six of its nine rows that raise nothing a monitor could catch. Day 5's §1 argument is pre-built.
  - **Day 11/12** — `checkpointer` is named and defined thinly; durable execution is explicitly deferred. §6's new row on a memory write succeeding in one system and failing in the other points at Week 2 without teaching it. Day 11 should not re-define the term.
  - **Day 19** — prompt caching is now named in one sentence, with no numbers, because Reviewer 2 was right that it is the first objection to "put the manual in every request". The economics stay yours. **Day 19 should assume the reader has met the word and nothing else.**
  - **Day 20** — sub-agents appear as one row in the four-levers table, described, not argued.

- **Anything the user must decide:** two things — the Rule B nesting question is now answered.

  **On the Rule B question: you already ruled, in `38fe1ed`, and Day 4 needs no change.** "Subject knobs owe a full method; input knobs owe less", with the test being whether the reader could set the knob himself and say why. The guide now cites Day 4's output-cap clause as its worked example, and I verified that exact sentence survived the review edits intact — worth checking, because if a length cut had taken it the guide would reference a sentence that no longer existed.

  1. **Video 2 is 61 minutes.** The five cited chapters run to 16:55 and the day says so, but it is the longest video the course has recommended. If a reading-only course should have a per-day video budget, this is the one to cut; the Chroma 8-minute video carries the day alone.
  2. **Day 3 carries a factual error I was not allowed to fix.** See below.

- **The finding I could not fix.** `FDE_Report` contains **zero URLs** — `grep -c 'http' FDE_Report` → `0`; its resource tables name sources in prose only. Day 4 shipped a draft sentence saying "the URL in `FDE_Report` has moved", which cannot be true of anything. Fixed here. **Day 3 makes the same claim in two places** (`course/day-03-guardrails/README.md`, near lines 271 and 281). The slice constraints forbid modifying a Day 1–3 README, so it is filed in `docs/residual-review-findings/86f7bd6.md`. The underlying facts in Day 3 are fine — those docs sites genuinely did move — only the attribution to the report is wrong.

- **Review panel: 3 reviewers, ~25 findings, ~20 applied, 4 refused with reasons** (all in `docs/residual-review-findings/86f7bd6.md`). The four that mattered most:
  1. **The headline derived number was wrong.** The "same formula, opposite conclusion" variant multiplied Day 2's response budget by three for parallel tool calls — but Day 2 divided by *passes*, so 19,700 is a per-pass allowance and three results share it. My variant implied a run consuming 591,000 tokens of a 200,000-token window. Two of three reviewers found it independently. Replaced with a flip on the output cap (88% → 74%), which stays inside Day 4, **plus** a new paragraph stating the interaction outright — because two knobs that contradict each other is better teaching than either number alone.
  2. **The 95th-percentile step double-counted the output cap.** All three reviewers. Now measures tool-result tokens per pass specifically, and converts per-pass risk to per-run (`1 − 0.95¹⁰ ≈ 40%`) before quoting it, which the day previously got backwards by calling 5% "the number you give the customer".
  3. **I overstated Anthropic's change of position** and hung a Tier 3 argument on it. The 2024 advice is a scoped exception about corpus *size*; the 2025 essay argues against *pre-computed retrieval* on a different axis, never withdraws the 2024 advice, and endorses a hybrid. Rewritten to say what actually changed. The real tension survives and is better: what 2025 undercuts is the customer's *reason* for wanting the paste.
  4. **`memory-split.svg` classified the customer's own corpus as long-term memory**, which the day's own definition ("anything you deliberately wrote") excludes — and which would have made §8's "my default is nothing" incoherent. Region retitled "what persists between runs"; the right-hand box relabelled "their system of record — not memory".

  Also applied: needle/haystack introduced before the reader meets it inside a quote; §6 row 1's mitigation no longer offers the compaction trigger against rot (it bounds the window, not attention); the fail-open guidance split into two rows, because failing open on a record whose job is to prevent a duplicate *causes* the duplicate and contradicted Day 3; "worth memorising" removed; two quote-punctuation slips fixed; the unjustified "twenty labelled questions" dropped; §4's "skip the needle-in-a-haystack experiments" reversed, since four of the day's claims come from those sections.

  **Refused, with reasons in the residual file:** inventing a magnitude for Chroma's LongMemEval result (not in the source — the day states the gap instead); dropping the word "ceiling" for attention (Day 2 established "binds"; forking the vocabulary from the day that handed the topic over is worse than naming the imprecision, which the day now does in prose rather than in 8px diagram type).

  **One self-inflicted error introduced *during* the fixes and caught by re-running the gate:** I wrote "rot was already costing you accuracy at 40% of the window" — an invented threshold, contradicting my own diagram footer saying there is no onset point. Removed. Re-run the gate after applying findings; the fixes are where new defects enter.

- **B8.5 browser verification:** skipped — this slice ships a markdown document and two static SVGs, so there is no UI to walk. `index.html` verified programmatically instead (see gate stats above).

- **B10.5 compound:** three entries written to `docs/solutions/conventions/` — `derived-knobs-must-be-derived-together.md` (the arithmetic class that broke this slice), `search-summaries-invent-findings.md` (a `WebSearch` summary attributed a "50K tokens" finding to Chroma that is nowhere in the report; it would have been the day's most quotable number), and `spawn-reviewers-as-subagents-not-teammates.md` (two failed `Agent` calls before the panel could start, plus the output-budget lesson).
