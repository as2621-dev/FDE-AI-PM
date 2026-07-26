**Week 3 · Make the system measurable and economically viable**
> By Day 21, know how it fails, what it costs, and whether it's improving.

_Scoring it honestly, and why 70% on a hard set beats 100% on an easy one._

Write `course/day-18-run-evals/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Scoring dimensions, LLM-as-judge and aligning it to human labels, eval harnesses, why 70% on a hard set beats 100% on an easy one

**Must NOT cover:** Dataset *construction* (D17), cost (D19)

**Gap fill (required, from the report's own gap table):** **Statistical significance** — don't ship on noise; eval variance

---

## Source material (verbatim from `FDE_Report`)

### Day 18 — Run evals
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Hamel & Shreya, "AI Evals for Engineers & PMs"** (Maven) | Course | The definitive evals course; O'Reilly book *Evals for AI Engineers* forthcoming | Paid | multi-week |
| **Braintrust / Langfuse / Promptfoo / DeepEval / Ragas** | Tools | Eval harnesses (Promptfoo also does OWASP red-teaming) | Free/Paid | 2 hr |
| **Eugene Yan, "Task-Specific LLM Evals"** (eugeneyan.com) | Essay | Practical eval design and metrics | Free | 1 hr |

**Exercise:** Score correctness · format · tool selection · required steps · escalation behavior. Don't chase 100% pass rates — a 70% rate on a hard set is more meaningful.

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
