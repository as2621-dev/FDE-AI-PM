**Week 2 · Turn the demo into a system that can recover**
> By Day 14, the agent produces predictable outputs and resumes after failure.

_Picking back up without redoing what already happened._

Write `course/day-12-resume/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Replay, step memoization, retry-from-point-of-failure, and the critical caveat that post-checkpoint nodes re-execute

**Must NOT cover:** Idempotency *keys* (D13)

---

## Source material (verbatim from `FDE_Report`)

### Day 12 — Resume
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **DBOS, "Why Durable Execution Should Be Lightweight"** | Blog | The library-vs-engine tradeoff (Postgres-backed decorators vs external orchestrator) | Free | 45 min |
| **Inngest** "How Functions Execute" + "Build a Durable AI Agent with Inngest" | Docs/blog | Step memoization; retry-from-point-of-failure; `step.run`/`step.waitForEvent` | Free | 1.5 hr |
| **Diagrid, "Why Checkpoints Aren't Durable Execution"** | Blog | The critical caveat: on resume, nodes *after* the checkpoint re-execute (incl. LLM/API calls) | Free | 30 min |

**Exercise:** Kill the agent mid-run deliberately; restart from the last checkpoint **without duplicating side effects** — this forces you to internalize idempotency (Day 13).

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
