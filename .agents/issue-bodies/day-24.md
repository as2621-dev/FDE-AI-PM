**Week 4 · Defend the system like an FDE**
> Explain the system to an engineer AND to a non-technical executive. The highest-leverage week for interviews.

_Writing down why each component exists — and the enterprise constraints that shaped it._

Write `course/day-24-architecture/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** ADRs, documenting *why* each component exists, benchmarking against reference architectures

**Must NOT cover:** Re-teaching components (W1–3)

**Gap fill (required, from the report's own gap table):** **Enterprise deployment depth** — VPC/on-prem, SOC2/HIPAA, data residency as architectural constraints

---

## Source material (verbatim from `FDE_Report`)

### Day 24 — Architecture
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Architecture Decision Records** (Michael Nygard; adr.github.io) | Method | How to document "why each component exists" | Free | 45 min |
| Anthropic Architecture Patterns whitepaper (revisit) | Whitepaper | Reference architectures to benchmark yours against | Free | 1 hr |

**Exercise:** Write an ADR-style doc: stack, tools, models, data, memory, guardrails — and why each exists.

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
