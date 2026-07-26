**Week 1 · Build an agent that can complete a real loop**
> By Day 7, the agent completes one useful workflow and exposes every step.

_What an agent actually is, and why most things called agents aren't._

Write `course/day-01-agent-loop/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** What an LLM is, what a token is, prompt→model→parse→act→observe, the workflow-vs-agent distinction, max-step caps, why "start simple"

**Must NOT cover:** Tool *design* (D2), guardrail *implementation* (D3)

---

## Source material (verbatim from `FDE_Report`)

### Day 1 — Agent loop
| Resource | Type | Why it matters | Free/Paid | Time |
|---|---|---|---|---|
| Anthropic, **"Building effective agents"** (anthropic.com/engineering) | Essay | The canonical workflows-vs-agents taxonomy; defines the augmented-LLM loop and the "start simple" principle | Free | 45 min |
| **ReAct: Synergizing Reasoning and Acting** (Yao et al., 2022, arXiv:2210.03629) | Paper | Founding paper of the reason→act→observe loop; widely treated as the origin of agentic LLMs | Free | 1 hr |
| **Barry Zhang (Anthropic), "How We Build Effective Agents"** (AI Engineer Summit 2025, YouTube) | Talk | An Anthropic engineer's practical framing of the loop and max-step limits | Free | 25 min |
| Hugging Face **smolagents** (build a code agent from scratch) | Repo/tutorial | Read a minimal, framework-free loop implementation | Free | 1 hr |

**Exercise:** Write the loop yourself with no framework — prompt → model → parse → act → repeat — with a hard max-step cap.

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
