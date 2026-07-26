**Week 2 · Turn the demo into a system that can recover**
> By Day 14, the agent produces predictable outputs and resumes after failure.

_The thousand ways it goes wrong. This is the FDE's actual job._

Write `course/day-10-failure-modes/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Enumerating how it breaks; missing data, malformed responses, dead APIs, timeouts, duplicates, partial completion; cascading failure; which errors not to retry

**Must NOT cover:** The *tagged taxonomy* (D16), backoff math (D15)

---

## Source material (verbatim from `FDE_Report`)

### Day 10 — Failure modes
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Google SRE Book** — "Handling Overload" & "Addressing Cascading Failures" (sre.google/sre-book) | Book chapters | Canonical distributed-systems failure taxonomy | Free | 2 hr |
| **AWS Builders' Library — "Timeouts, retries, and backoff with jitter"** (Marc Brooker) | Essay | Failure handling for remote calls; which errors *not* to retry (4XX) | Free | 1 hr |

**Exercise:** Enumerate your agent's failure modes: missing data · malformed responses · dead APIs · timeouts · duplicates · partial completion.

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
