**Week 2 · Turn the demo into a system that can recover**
> By Day 14, the agent produces predictable outputs and resumes after failure.

_Idempotency: why replaying a step twice must not charge the customer twice._

Write `course/day-13-failure-handling/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Idempotency keys, safe replay, compensating transactions (saga), explicit behaviour for each failure class, when to stop and escalate

**Must NOT cover:** Retry timing (D15)

---

## Source material (verbatim from `FDE_Report`)

### Day 13 — Failure handling
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Stripe, "Designing robust and predictable APIs with idempotency"** (Brandur Leach, 2017) | Essay | The canonical idempotency-key reference; origin of the `Idempotency-Key` header convention | Free | 1 hr |
| **microservices.io — Saga pattern** (Chris Richardson) | Pattern | Compensating transactions for partial failure; choreography vs orchestration | Free | 45 min |
| **Brandur, "Implementing Stripe-like Idempotency Keys in Postgres"** | Deep dive | How to actually build the idempotency layer | Free | 1 hr |

**Exercise:** Define explicit behavior for tool failure, bad output, incomplete state, and unsafe continuation. Add an idempotency key to every side-effecting action so replay is safe.

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
