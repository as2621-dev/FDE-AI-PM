Tracking issue for the 30-day FDE course build.

**Reader:** product manager, mechanical engineer by training, no software
background. Reading-only (no hands-on coding). Targeting **AI product startup**
FDE roles (Sierra, Harvey, Decagon, Glean), frontier labs as a stretch.

**Deliverable:** 30 markdown days in `course/`, assembled by `course/build.py`
into one self-contained HTML page — day list in a left sidebar, content on the
right — published as a private artifact.

**Quality gates per day:** `evals/check_day.py` (deterministic) + two reviewer
agents (accuracy/readability, and an adversarial interviewer).

## Progress

### Week 1 · Days 1–7 — Build an agent that can complete a real loop
_By Day 7, the agent completes one useful workflow and exposes every step._

- [ ] Day 01 — The agent loop
- [ ] Day 02 — Tool use
- [ ] Day 03 — Guardrails
- [ ] Day 04 — Context and memory
- [ ] Day 05 — The audit trail
- [ ] Day 06 — A real workflow
- [ ] Day 07 — Week 1 checkpoint

### Week 2 · Days 8–14 — Turn the demo into a system that can recover
_By Day 14, the agent produces predictable outputs and resumes after failure._

- [ ] Day 08 — Structured outputs
- [ ] Day 09 — Schema validation
- [ ] Day 10 — Failure modes
- [ ] Day 11 — Checkpointing
- [ ] Day 12 — Resume
- [ ] Day 13 — Failure handling
- [ ] Day 14 — Week 2 checkpoint

### Week 3 · Days 15–21 — Make the system measurable and economically viable
_By Day 21, know how it fails, what it costs, and whether it's improving._

- [ ] Day 15 — Retry logic
- [ ] Day 16 — Failure categories
- [ ] Day 17 — The golden dataset
- [ ] Day 18 — Running evals
- [ ] Day 19 — Optimising cost
- [ ] Day 20 — Multi-agent
- [ ] Day 21 — Week 3 checkpoint

### Week 4 · Days 22–30 — Defend the system like an FDE
_Explain the system to an engineer AND to a non-technical executive. The highest-leverage week for interviews._

- [ ] Day 22 — The pain point
- [ ] Day 23 — Why AI belongs here
- [ ] Day 24 — Architecture
- [ ] Day 25 — Iterations
- [ ] Day 26 — The evals story
- [ ] Day 27 — Economics
- [ ] Day 28 — Rehearsing for an engineer
- [ ] Day 29 — Rehearsing for a VP
- [ ] Day 30 — Final checkpoint

## Phase 0 (done before any day)

- [x] `course/_meta/STYLE_GUIDE.md` — the authoring contract
- [x] `course/_meta/DAY_MAP.md` — boundaries + gap-fill assignments
- [x] `course/_meta/days.json` — 30-day manifest
- [x] `course/GLOSSARY.md` — seeded
- [x] `evals/check_day.py` — deterministic gate
- [x] `course/build.py` — single-page assembler
- [x] `.tools/diagram-design` — diagram system vendored (gitignored)