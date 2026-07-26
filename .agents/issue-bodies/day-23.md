**Week 4 · Defend the system like an FDE**
> Explain the system to an engineer AND to a non-technical executive. The highest-leverage week for interviews.

_Rules vs. agent vs. human. Not every step deserves a model._

Write `course/day-23-why-ai-belongs/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** **Reuses earlier sources + Varick framework.** Deterministic software vs agent vs human-in-control. Where autonomy stops. Not every step deserves an LLM

**Must NOT cover:** Re-teaching the agent loop (D1)

**Gap fill (required, from the report's own gap table):** **Pilot scoping (cont.)** — what a pilot must prove before production

---

## Source material (verbatim from `FDE_Report`)

### Day 23 — Why AI belongs
Use the Varick microsite's decision framework — **deterministic software** (rules/inputs predictable) vs **an agent** (objective clear but path/inputs vary) vs **human-in-control** (material ambiguity, accountability, irreversible consequences). Vas's point: not every step deserves an LLM. Write down what stays human and where autonomy stops.

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
