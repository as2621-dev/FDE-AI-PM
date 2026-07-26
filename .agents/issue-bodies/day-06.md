**Week 1 · Build an agent that can complete a real loop**
> By Day 7, the agent completes one useful workflow and exposes every step.

_Pointing all of it at one genuinely manual back-office process._

Write `course/day-06-real-workflow/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** Picking a back-office process, granular process mapping, human-approval pauses, the last-mile idea, the French-waiter model

**Must NOT cover:** Discovery *questioning technique* (D22), ROI (D27)

---

## Source material (verbatim from `FDE_Report`)

### Day 6 — Real workflow
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| **Varick FDE microsite** (invoice_0417.pdf example run log) | Reference | Shows a real back-office workflow end-to-end with a human-approval pause | Free | 30 min |
| First Round Review, **"So You Want to Hire a Forward Deployed Engineer"** | Essay | What "last-mile" real workflows look like; the French-waiter model | Free | 45 min |
| Anthropic, **"Building Effective AI Agents: Architecture Patterns and Implementation Frameworks"** (PDF) | Whitepaper | Common enterprise use cases and architecture patterns | Free | 1 hr |

**Exercise:** Pick one previously-manual back-office process (finance/HR/procurement/logistics/sales); get it in granular detail; run the agent on it and tie it to a portfolio repo.

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
