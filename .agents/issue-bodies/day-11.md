**Week 2 · Turn the demo into a system that can recover**
> By Day 14, the agent produces predictable outputs and resumes after failure.

_Saving your place so a crash doesn't cost you the whole run._

Write `course/day-11-checkpointing/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Saving state mid-run, durable execution, journalling, durability modes, Trigger.dev (his stack)

**Must NOT cover:** Resuming *from* a checkpoint (D12), idempotency (D13)

---

## Source material (verbatim from `FDE_Report`)

### Day 11 — Checkpointing
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **LangGraph persistence & durable-execution** docs | Docs | Checkpointers, threads, three durability modes (`exit`/`async`/`sync`) — a safety-vs-performance dial | Free | 1.5 hr |
| **Restate, "What is Durable Execution? A Definitive Guide"** | Guide | Best vendor-neutral mental model of journaling/replay | Free | 1 hr |
| **Trigger.dev** "How it works" + idempotency docs | Docs | **Your stack** — checkpointing, freezing during waits, idempotency keys (run/attempt/global scopes) | Free | 1.5 hr |
| **Temporal** "Workflow Execution" + "Events and Event History" | Docs | Event-sourced durable execution; workflows (deterministic) vs activities (side-effectful, retried) | Free | 1.5 hr |

**Exercise:** Save state (task, actions, tool results, pending work, errors) every few steps using Trigger.dev tasks.

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
