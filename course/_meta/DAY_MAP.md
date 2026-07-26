# Day boundary map

Derived from `FDE_Report`. Every day-agent reads **its own row plus the two rows either
side** before writing, and stays inside its boundary. Overlap is the main way a
30-day course rots — if two days both explain retries, one of them is wasted.

The `Gap fill` column assigns the topics `FDE_Report`'s own gap table flags as missing.
Those are **not optional** — they're the difference between the plan and a complete
FDE curriculum. Fold them in as a clearly-marked sub-block inside §3 Tier 3 or §6.

---

## Week 1 · Days 1–7 — Build an agent that can complete a real loop
*Week goal: by Day 7, the agent completes one useful workflow and exposes every step.*

| Day | Slug | Title | Owns | Must NOT cover (belongs to) | Gap fill |
|---|---|---|---|---|---|
| 1 | `agent-loop` | The agent loop | What an LLM is, what a token is, prompt→model→parse→act→observe, the workflow-vs-agent distinction, max-step caps, why "start simple" | Tool *design* (D2), guardrail *implementation* (D3) | — |
| 2 | `tool-use` | Tool use | What a tool/function call is, tool naming and description design, MCP as a standard, the two dialects (Anthropic/OpenAI) | Output *schemas* (D8), tool *failure* (D13) | **Data connectors** — NetSuite/Salesforce/ERP reality, pre-built MCP servers. Varick's own JD centres on this |
| 3 | `guardrails` | Guardrails | Prompt injection (LLM01:2025), input validation, output filtering, step limits, tripwires, direct vs indirect injection | Schema validation (D9), retries (D15) | **Enterprise security intro** — SOC2/HIPAA/VPC as customer requirements. Depth goes to D24 |
| 4 | `context-and-memory` | Context and memory | Context window, attention budget, context rot, short-term vs long-term memory, what deserves external memory | Audit logging (D5), cost of tokens (D19) | **RAG over customer data, and when NOT to use RAG** — the RAG-vs-long-context decision |
| 5 | `audit-trail` | The audit trail | Tracing vs logging, spans, step-level observability, OpenTelemetry GenAI conventions, reconstructing a run | Failure *taxonomy* (D10/D16), evals (D17-18) | — |
| 6 | `real-workflow` | A real workflow | Picking a back-office process, granular process mapping, human-approval pauses, the last-mile idea, the French-waiter model | Discovery *questioning technique* (D22), ROI (D27) | — |
| 7 | `week-1-checkpoint` | Week 1 checkpoint | **Synthesis day.** No new concepts. Assemble D1–6 into one story, drill the connections, rehearse "walk me through your agent" | Anything not already taught in D1–6 | — |

## Week 2 · Days 8–14 — Turn the demo into a system that can recover
*Week goal: by Day 14, the agent produces predictable outputs and resumes after failure.*

| Day | Slug | Title | Owns | Must NOT cover (belongs to) | Gap fill |
|---|---|---|---|---|---|
| 8 | `structured-outputs` | Structured outputs | Why free text breaks pipelines, JSON schema constraint, constrained decoding, reasoning-fields-before-answer-fields | Validation *logic* (D9) | — |
| 9 | `schema-validation` | Schema validation | Pydantic validators, retry-on-validation-failure, escalation after N failures, token-level constraint | Retry *backoff* (D15), general failure handling (D13) | — |
| 10 | `failure-modes` | Failure modes | Enumerating how it breaks; missing data, malformed responses, dead APIs, timeouts, duplicates, partial completion; cascading failure; which errors not to retry | The *tagged taxonomy* (D16), backoff math (D15) | — |
| 11 | `checkpointing` | Checkpointing | Saving state mid-run, durable execution, journalling, durability modes, Trigger.dev (his stack) | Resuming *from* a checkpoint (D12), idempotency (D13) | — |
| 12 | `resume` | Resume | Replay, step memoization, retry-from-point-of-failure, and the critical caveat that post-checkpoint nodes re-execute | Idempotency *keys* (D13) | — |
| 13 | `failure-handling` | Failure handling | Idempotency keys, safe replay, compensating transactions (saga), explicit behaviour for each failure class, when to stop and escalate | Retry timing (D15) | — |
| 14 | `week-2-checkpoint` | Week 2 checkpoint | **Synthesis day.** Reliability story end-to-end; rehearse "what happens when it fails halfway through?" | New concepts | — |

## Week 3 · Days 15–21 — Make the system measurable and economically viable
*Week goal: by Day 21, know how it fails, what it costs, and whether it's improving.*

| Day | Slug | Title | Owns | Must NOT cover (belongs to) | Gap fill |
|---|---|---|---|---|---|
| 15 | `retry-logic` | Retry logic | Exponential backoff, the thundering herd, retry budgets/token bucket, retry storms across layers | Which errors to retry (D10), idempotency (D13) | **Jitter** — the report's own 1·2·4·8·16s schedule omits it. Full/equal/decorrelated jitter |
| 16 | `failure-categories` | Failure categories | **Reuses D10 sources.** Building the tagged taxonomy: missing context, wrong tool, wrong record, invalid output, unsafe action, timeout. Tagging traces. The bridge to error analysis | Re-teaching D10's mechanics; eval scoring (D18) | — |
| 17 | `golden-dataset` | The golden dataset | Error analysis as the highest-leverage activity, building 20 hand-labelled cases across normal/edge/ambiguous/high-risk, open vs axial coding, the vibe-check trap | Running/scoring (D18) | — |
| 18 | `run-evals` | Running evals | Scoring dimensions, LLM-as-judge and aligning it to human labels, eval harnesses, why 70% on a hard set beats 100% on an easy one | Dataset *construction* (D17), cost (D19) | **Statistical significance** — don't ship on noise; eval variance |
| 19 | `optimize-cost` | Optimising cost | Prompt caching economics, batch discounts, model cascades/routing, cost per query, cache-hit rate | Multi-agent token cost (D20) | **Latency & streaming UX** (latency budgets) and **fine-tuning vs prompting** — both are cost/UX decisions |
| 20 | `multi-agent` | Multi-agent | Orchestrator-worker, handoffs, when decomposition genuinely helps, and the live disagreement — Anthropic vs Cognition. **Present both. Do not resolve it.** | Re-teaching the single-agent loop (D1) | — |
| 21 | `week-3-checkpoint` | Week 3 checkpoint | **Synthesis day.** The measurement + economics story; rehearse "how do you know it's working?" and "what does it cost?" | New concepts | — |

## Final week · Days 22–30 — Defend the system like an FDE
*Week goal: explain the system to an engineer AND to a non-technical executive.*
*`FDE_Report` calls this the highest-leverage week for interviews. Treat it as such —
this is where a PM background is an advantage rather than a gap.*

| Day | Slug | Title | Owns | Must NOT cover (belongs to) | Gap fill |
|---|---|---|---|---|---|
| 22 | `the-pain-point` | The pain point | Discovery technique, Mom Test questioning, shadowing a workflow, who/what/where-errors/what-it-costs, what FDEs actually do | ROI *maths* (D27), architecture (D24) | **Pilot/POC scoping** — sandbox → human review → production, gradual autonomy |
| 23 | `why-ai-belongs` | Why AI belongs here | **Reuses earlier sources + Varick framework.** Deterministic software vs agent vs human-in-control. Where autonomy stops. Not every step deserves an LLM | Re-teaching the agent loop (D1) | **Pilot scoping (cont.)** — what a pilot must prove before production |
| 24 | `architecture` | Architecture | ADRs, documenting *why* each component exists, benchmarking against reference architectures | Re-teaching components (W1–3) | **Enterprise deployment depth** — VPC/on-prem, SOC2/HIPAA, data residency as architectural constraints |
| 25 | `iterations` | Iterations | **Reuses D17 error analysis.** Narrating v1→v2: what was wrong, what changed, how metrics moved. "Walk me through a complex project you owned" | Re-teaching error analysis (D17) | — |
| 26 | `the-evals-story` | The evals story | **Reuses D17–18.** Presenting evals to a customer: dataset, pass rate, failure categories, thresholds, escalation rules, open risks. The evaluation-report format | Re-teaching eval construction (D17-18) | — |
| 27 | `economics` | Economics | The one-page business case: hours saved, errors reduced, risk mitigated, revenue, cost per query. Sizing and defending the number | Token-level cost mechanics (D19) | — |
| 28 | `rehearse-engineer` | Rehearsing for an engineer | **Reuses W1–3.** Live architecture discussion, "design an AI solution for customer X", holding technical lines, admitting what you don't know | New concepts | — |
| 29 | `rehearse-vp` | Rehearsing for a VP | Minto Pyramid / BLUF, answer-first, MECE, problem→outcome→evidence→risk in plain language, the simulated non-technical CISO/VP round | Technical depth (D28) | — |
| 30 | `final-checkpoint` | Final checkpoint | **Capstone synthesis.** The complete case study for both audiences; the full 17-artifact inventory; the interview-loop map; what to do in the 48 hours before an interview | New concepts | — |

---

## Standing notes for every day-agent

1. **The report's central thesis**, worth echoing where it fits: *"There's only one way
   something can go right, but there's a thousand different ways something can go wrong.
   If you're only building for the way it goes right, you're worth nothing."* — Vas,
   Varick Agents. Days 10, 13, 16 and 6 are where this lands hardest.

2. **The FDE role is unstandardised.** Same job appears as Forward Deployed Engineer,
   Applied AI Engineer, FDSE, Deployment Strategist, Customer-Facing AI Engineer.
   Reader is targeting **AI product startups** (Sierra, Harvey, Decagon, Glean) with
   frontier labs as a stretch. Where a day's emphasis differs by company type, add a
   one-line note. Don't overdo it.

3. **Reader is reading-only.** Day 6 and Days 22–30 assume a portfolio build he has
   not done. Reframe those honestly: teach the *thinking*, and note where a real build
   would give him a stronger story. Never pretend he built something.

4. **The interview-loop shape**, useful context for §1 and §8 of any day:
   recruiter screen → practical coding → solution design → **customer-discovery
   role-play** → values. The report flags the discovery round as the highest-signal one,
   and the one most candidates fail by preparing for it like a technical interview.

5. **`FDE_Report` carries a caveats section.** Comp figures are marketing claims.
   Prompt-caching rates drift. OpenAI Swarm is deprecated. Some cited sources are
   vendor blogs with competitive positioning. Respect all of it — don't launder a
   marketing claim into a fact.
