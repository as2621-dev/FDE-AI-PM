**Week 1 · Build an agent that can complete a real loop**
> By Day 7, the agent completes one useful workflow and exposes every step.

_How a model reaches out and touches a real system._

Write `course/day-02-tool-use/README.md` — a 45–60 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

**Owns:** What a tool/function call is, tool naming and description design, MCP as a standard, the two dialects (Anthropic/OpenAI)

**Must NOT cover:** Output *schemas* (D8), tool *failure* (D13)

**Gap fill (required, from the report's own gap table):** **Data connectors** — NetSuite/Salesforce/ERP reality, pre-built MCP servers. Varick's own JD centres on this

---

## Source material (verbatim from `FDE_Report`)

### Day 2 — Tool use
| Resource | Type | Why | Free/Paid | Time |
|---|---|---|---|---|
| Anthropic, **"Writing effective tools for AI agents"** | Essay | Tool design, namespacing (`asana_search`, `jira_search`), evaluation-driven tool building | Free | 45 min |
| Anthropic, **"Introducing the Model Context Protocol"** + `modelcontextprotocol.io` | Docs | The open standard (Nov 2024) for connecting agents to tools/data; USB-C-for-AI analogy | Free | 1 hr |
| **Anthropic Skilljar "Introduction to MCP"** course | Course | Hands-on building an MCP server (tools/resources/prompts) with the Python SDK | Free | 2 hr |
| OpenAI function-calling / tool-use guide | Docs | The other major tool-calling dialect | Free | 45 min |

**Exercise:** Give the agent one real API tool + one web-search tool; let the model decide when to call each.

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
