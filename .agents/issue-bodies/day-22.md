**Week 4 · Defend the system like an FDE**
> Explain the system to an engineer AND to a non-technical executive. The highest-leverage week for interviews.

_Discovery. Finding where time and money actually leak._

Write `course/day-22-the-pain-point/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Discovery technique, Mom Test questioning, shadowing a workflow, who/what/where-errors/what-it-costs, what FDEs actually do

**Must NOT cover:** ROI *maths* (D27), architecture (D24)

**Gap fill (required, from the report's own gap table):** **Pilot/POC scoping** — sandbox → human review → production, gradual autonomy

---

## Source material (verbatim from `FDE_Report`)

### Day 22 — The pain point
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| First Round Review, **"So You Want to Hire an FDE"** | Essay | What FDEs actually do; discovery vs implementation | Free | 45 min |
| **The Mom Test** (Rob Fitzpatrick) | Book | Discovery questions that surface *real* pain, not flattery | Paid | 3 hr |
| **Varick FDE job posting** (Ashby) | Primary source | The exact expectations: shadow workflows, interview dept heads, map data flows across NetSuite/Salesforce | Free | 15 min |

**Exercise:** For your Day 6 workflow, document who does the work, what takes time, where errors occur, what it costs.

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
