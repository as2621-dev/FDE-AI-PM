**Week 3 · Make the system measurable and economically viable**
> By Day 21, know how it fails, what it costs, and whether it's improving.

_Turning a pile of broken runs into a taxonomy you can act on._

Write `course/day-16-failure-categories/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** **Reuses D10 sources.** Building the tagged taxonomy: missing context, wrong tool, wrong record, invalid output, unsafe action, timeout. Tagging traces. The bridge to error analysis

**Must NOT cover:** Re-teaching D10's mechanics; eval scoring (D18)

---

## Source material (verbatim from `FDE_Report`)

### Day 16 — Failure categories
Reuse Day 10 sources. Build the taxonomy the plan specifies: missing context · wrong tool · wrong record · invalid output · unsafe action · timeout. Tag every failed run in your trace tool (Langfuse/Phoenix). This is the bridge to error analysis (Day 17).

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
