---
title: A day-writer agent cannot spawn a named or backgrounded review panel
tags: [tooling, agent-tool, review-panel, grab-issue, workflow]
problem_type: tooling
symptoms: Two failed Agent calls and a wasted round trip before the review panel starts.
date: 2026-07-26
---

The `/grab-issue` protocol tells the slice-builder to spawn a three-reviewer panel "in
parallel via the Agent tool". If the builder is itself a teammate rather than the session
lead, two attempts fail before one works.

```
Agent(name: "day04-reviewer-accuracy", ...)
  → "Teammates cannot spawn other teammates — the team roster is flat.
     To spawn a subagent instead, omit the `name` parameter."

Agent(run_in_background: true, ...)
  → "In-process teammates cannot spawn background agents.
     Use run_in_background=false for synchronous subagents."
```

**What works:** omit `name`, set `run_in_background: false`, and put all three `Agent` calls
in **one message** — they still run concurrently, and you get all three reports back together.

```
Agent(description: "...", subagent_type: "general-purpose", model: "opus",
      run_in_background: false, prompt: "...")   ×3 in a single assistant turn
```

**Budget consequence worth planning for.** Synchronous means the three reports land in your
context at once. Day 4's panel returned about 12,000 tokens combined against a 120,000-token
slice ceiling, from subagents that burned 128k–154k tokens each on their own budgets. Cap the
output explicitly in each reviewer prompt — *"keep your report under 800 words, findings only,
no restating what the document says"* — or a thorough reviewer will hand you a summary of the
artefact you wrote before it gets to the defects.

**Ask for adversarial output, and mean it.** The three prompts that produced Day 4's usable
findings all opened with "FIND WHAT IS WRONG", "default to skeptical", and "report only real,
evidenced defects — no praise, no style preferences". They returned roughly 25 findings, of
which about 20 were genuine and 5 needed pushing back on. A reviewer told to "review this day"
returns paragraphs of agreement.

**Give each reviewer the fetch recipe, not just the URLs.** All three were told to `curl` and
strip tags rather than call `WebFetch`, with the reason stated — a summariser's paraphrase is
the defect being hunted (see [[search-summaries-invent-findings]]). One reviewer then
machine-checked 82 quoted strings against six fetched sources and found two punctuation slips
that eye-reading had missed twice.
