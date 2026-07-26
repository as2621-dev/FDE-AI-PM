**Week 3 · Make the system measurable and economically viable**
> By Day 21, know how it fails, what it costs, and whether it's improving.

_Caching, routing, latency budgets, and the cost-per-query number you'll be asked for._

Write `course/day-19-optimize-cost/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Prompt caching economics, batch discounts, model cascades/routing, cost per query, cache-hit rate

**Must NOT cover:** Multi-agent token cost (D20)

**Gap fill (required, from the report's own gap table):** **Latency & streaming UX** (latency budgets) and **fine-tuning vs prompting** — both are cost/UX decisions

---

## Source material (verbatim from `FDE_Report`)

### Day 19 — Optimize cost
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Anthropic prompt caching** docs | Docs | Cache reads billed at **10% of standard input** (90% off) — e.g. Claude Sonnet input $3.00/M → $0.30/M; cache writes cost 1.25× normal input | Free | 45 min |
| **OpenAI prompt caching + Batch API** docs | Docs | Caching is "automatically applied" on prompts >1,024 tokens for a **50% discount**; the Batch API adds a flat 50% for a 24-hour window, stackable with caching | Free | 45 min |
| **FrugalGPT** (Chen, Zaharia, Zou) | Paper | Model cascades / routing to cut cost | Free | 1 hr |

**Exercise:** Route simple subtasks to cheaper models (Haiku vs Sonnet); add caching + token limits; compute cost per query. Track cache-hit rate — below 50% on a long-context workload means your cache breakpoint is misplaced.

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
