**Week 3 · Make the system measurable and economically viable**
> By Day 21, know how it fails, what it costs, and whether it's improving.

_Twenty hand-labelled cases. The highest-leverage thing in this course._

Write `course/day-17-golden-dataset/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Error analysis as the highest-leverage activity, building 20 hand-labelled cases across normal/edge/ambiguous/high-risk, open vs axial coding, the vibe-check trap

**Must NOT cover:** Running/scoring (D18)

---

## Source material (verbatim from `FDE_Report`)

### Day 17 — Golden dataset
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Hamel Husain & Shreya Shankar, "LLM Evals: Everything You Need to Know" (Evals FAQ)** (hamel.dev) | Reference | *"Error analysis is the most important activity in evals"*; how to build datasets and review 20–50 traces | Free | 2 hr |
| Hamel Husain, **"Your AI Product Needs Evals"** | Essay | The foundational essay; vibe-check trap | Free | 1 hr |
| **Shreya Shankar et al., "Who Validates the Validators?" (EvalGen)** (arXiv / CHI 2024) | Paper | Aligning LLM-as-judge with human preference | Free | 1 hr |

**Exercise:** Build 20 real queries with hand-labeled ideal outputs across normal · edge · ambiguous · high-risk. Expect 60–80% of your dev time to go to error analysis, not building automated checks.

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
