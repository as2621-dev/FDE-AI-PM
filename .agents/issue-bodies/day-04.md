**Week 1 · Build an agent that can complete a real loop**
> By Day 7, the agent completes one useful workflow and exposes every step.

_Why stuffing more into the prompt makes the agent worse, not better._

Write `course/day-04-context-and-memory/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Context window, attention budget, context rot, short-term vs long-term memory, what deserves external memory

**Must NOT cover:** Audit logging (D5), cost of tokens (D19)

**Gap fill (required, from the report's own gap table):** **RAG over customer data, and when NOT to use RAG** — the RAG-vs-long-context decision

---

## Source material (verbatim from `FDE_Report`)

### Day 4 — Context & memory
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| Anthropic, **"Effective context engineering for AI agents"** | Essay | Defines context engineering as curating "the smallest set of high-signal tokens"; introduces the "attention budget" | Free | 45 min |
| **Chroma, "Context Rot: How Increasing Input Tokens Impacts LLM Performance"** (Hong, Troynikov, Huber, July 2025) | Research report | Evaluated 18 frontier models (GPT-4.1, Claude 4, Gemini 2.5, Qwen3), concluding verbatim: *"we demonstrate that LLMs do not maintain consistent performance across input lengths"* and *"their performance grows increasingly unreliable as input length grows"* | Free | 1 hr |
| **Letta / MemGPT** (docs + paper) | Tool/paper | Agentic memory that outlives the context window | Free | 1.5 hr |
| **LangGraph memory** — checkpointers (short-term) vs stores (long-term) | Docs | The practical short-vs-long-term memory split | Free | 45 min |

**Exercise:** Keep state in the context window by default; add external memory only for the one piece of state that must outlive the run.

---

### Definition of done

- [ ] All 10 sections present, headings **verbatim** per the style guide
- [ ] 6,500–9,000 prose words (45–60 min read)
- [ ] Frontmatter complete (`day`, `slug`, `title`, `week`, `week_title`, `one_liner`, `reading_minutes`)
- [ ] §3 has all three depth tiers (Tier 1 / Tier 2 / Tier 3)
- [ ] Every resource in the table above has a §4 digest block
- [ ] 8–12 Q&A in `<details>` blocks, blank line after `</summary>`
- [ ] 1–2 self-contained SVG diagrams, presentation attributes only, captioned
- [ ] ≤2 videos, both verified to exist, **zero unsourced timestamps**
- [ ] Every non-obvious claim sourced, or marked `⚠️ Unverified`
- [ ] §9 vocabulary table filled and merged into `course/GLOSSARY.md`
- [ ] No term used before it is defined
- [ ] Gate passes: `python3 evals/check_day.py course/day-NN-slug/README.md`
- [ ] Reviewer 1 (accuracy + PM-readability) passed
- [ ] Reviewer 2 (adversarial interviewer) could not trivially fail the reader

### Reference

- Authoring contract: `course/_meta/STYLE_GUIDE.md` — **read fully before writing**
- Boundaries: `course/_meta/DAY_MAP.md`
- Diagram system: `.tools/diagram-design/skills/diagram-design/`
- Rebuild the page: `~/.venvs/fde-course/bin/python course/build.py`
