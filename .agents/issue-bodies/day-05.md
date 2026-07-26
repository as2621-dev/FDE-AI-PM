**Week 1 · Build an agent that can complete a real loop**
> By Day 7, the agent completes one useful workflow and exposes every step.

_If you can't reconstruct the run, you can't fix it or sell it._

Write `course/day-05-audit-trail/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Tracing vs logging, spans, step-level observability, OpenTelemetry GenAI conventions, reconstructing a run

**Must NOT cover:** Failure *taxonomy* (D10/D16), evals (D17-18)

---

## Source material (verbatim from `FDE_Report`)

### Day 5 — Audit trail
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Langfuse** observability docs (open source, MIT) | Tool | Trace every prompt/response/tool call; self-hostable; ~28k+ GitHub stars | Free/Paid | 1.5 hr |
| **OpenTelemetry GenAI semantic conventions** | Standard | Vendor-neutral span/attribute schema (agent/workflow/tool/model spans); instrument against this rather than a proprietary SDK | Free | 45 min |
| **Arize Phoenix** (OTEL-native, OpenInference) | Tool | Open-source tracing/eval, strong for RAG debugging | Free | 1 hr |
| **Braintrust / LangSmith / W&B Weave** | Tools | Managed alternatives with built-in evals; LangSmith is deepest for LangChain/LangGraph | Free tier/Paid | 1 hr |

**Exercise:** Log every prompt, response, tool call, result, error, and timestamp; reconstruct one full run from logs alone. Step-level tracing (not pass/fail health checks) is the minimum viable signal for an agent in production.

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
