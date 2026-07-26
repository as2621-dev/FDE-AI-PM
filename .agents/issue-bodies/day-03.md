**Week 1 · Build an agent that can complete a real loop**
> By Day 7, the agent completes one useful workflow and exposes every step.

_Stopping the agent from doing the wrong thing, including when someone tries to make it._

Write `course/day-03-guardrails/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Prompt injection (LLM01:2025), input validation, output filtering, step limits, tripwires, direct vs indirect injection

**Must NOT cover:** Schema validation (D9), retries (D15)

**Gap fill (required, from the report's own gap table):** **Enterprise security intro** — SOC2/HIPAA/VPC as customer requirements. Depth goes to D24

---

## Source material (verbatim from `FDE_Report`)

### Day 3 — Guardrails
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **OWASP Top 10 for LLM Applications (2025)** | Framework | Prompt Injection is ranked **LLM01:2025**, the top spot for the second consecutive edition; OWASP notes it is "possible due to the nature of generative AI... it is unclear if there are fool-proof methods of prevention" | Free | 1 hr |
| **NVIDIA NeMo Guardrails** (docs + repo) | Tool | Programmable rails for input/output/topic control | Free | 1.5 hr |
| **Guardrails AI** (docs + hub) | Tool | Output validators and structure guards | Free | 1 hr |
| **OpenAI Agents SDK — Guardrails** page (openai.github.io/openai-agents-python/guardrails) | Docs | Input/output/tool guardrails with tripwires and parallel validation | Free | 30 min |

**Exercise:** Add input validation, a max-step limit, and an output filter; write one prompt-injection test your guardrail must catch (direct *and* indirect via retrieved content).

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
