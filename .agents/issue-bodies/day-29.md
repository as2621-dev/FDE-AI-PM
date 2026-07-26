**Week 4 · Defend the system like an FDE**
> Explain the system to an engineer AND to a non-technical executive. The highest-leverage week for interviews.

_Answer-first, plain language, bottom-line-up-front. The round most candidates fail._

Write `course/day-29-rehearse-vp/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Minto Pyramid / BLUF, answer-first, MECE, problem→outcome→evidence→risk in plain language, the simulated non-technical CISO/VP round

**Must NOT cover:** Technical depth (D28)

---

## Source material (verbatim from `FDE_Report`)

### Day 29 — Rehearse (VP audience)
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Barbara Minto, Pyramid Principle / BLUF** (Untools/Management Consulted summaries; the book for depth) | Method | Answer-first, MECE executive communication; lead with conclusion then support | Free/Paid | 1 hr |

**Exercise:** Deliver the problem → outcome → evidence → risk in plain language, bottom-line-up-front. Anthropic/OpenAI loops force you to "hold technical lines under pressure" to a simulated non-technical CISO/VP.

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
