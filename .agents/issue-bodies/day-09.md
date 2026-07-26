**Week 2 · Turn the demo into a system that can recover**
> By Day 14, the agent produces predictable outputs and resumes after failure.

_Checking the shape, and retrying intelligently when it's wrong._

Write `course/day-09-schema-validation/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Pydantic validators, retry-on-validation-failure, escalation after N failures, token-level constraint

**Must NOT cover:** Retry *backoff* (D15), general failure handling (D13)

---

## Source material (verbatim from `FDE_Report`)

### Day 9 — Schema validation
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Pydantic** docs (validators) | Docs | The validation layer everything builds on | Free | 1 hr |
| Instructor **retry-on-validation-failure** | Docs | Auto-retry feeding the validation error back to the model | Free | 30 min |
| **PydanticAI** | Framework | Typed agents with validation, dataset replays, dashboards | Free | 1 hr |
| **XGrammar** (via vLLM/SGLang) | Library | Token-level constrained decoding — model physically cannot emit malformed output | Free | 45 min |

**Exercise:** Validate every response; retry on invalid structure, escalate after N failures.

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
