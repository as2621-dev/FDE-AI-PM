**Week 3 · Make the system measurable and economically viable**
> By Day 21, know how it fails, what it costs, and whether it's improving.

_When splitting it up helps, and the live disagreement about whether it ever does._

Write `course/day-20-multi-agent/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Orchestrator-worker, handoffs, when decomposition genuinely helps, and the live disagreement — Anthropic vs Cognition. **Present both. Do not resolve it.**

**Must NOT cover:** Re-teaching the single-agent loop (D1)

---

## Source material (verbatim from `FDE_Report`)

### Day 20 — Multi-agent
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Anthropic, "How we built our multi-agent research system"** | Essay | Orchestrator-worker done right; *"Multi-agent systems work mainly because they help spend enough tokens to solve the problem"* | Free | 1 hr |
| **Cognition (Walden Yan), "Don't Build Multi-Agents"** + follow-up **"Multi-Agents: What's Actually Working"** | Essays | The counterpoint (fragile context-passing) and Yan's 2026 update: multi-agent works when writes stay single-threaded | Free | 1 hr |
| **Anthropic, "When to use multi-agent systems (and when not to)"** | Essay | Anthropic's own caveat: teams "invest months... only to discover improved prompting on a single agent achieved equivalent results" | Free | 30 min |
| **OpenAI Agents SDK** (handoffs) + **Swarm** (github.com/openai/swarm, historical/educational only — deprecated in favor of the SDK) | Docs/repo | Handoff patterns | Free | 1 hr |

**Exercise:** Only if decomposition genuinely helps — one plans, several execute, one synthesizes. Default to a single well-engineered agent.

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
