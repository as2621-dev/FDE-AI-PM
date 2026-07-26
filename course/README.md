# FDE in 30 Days

A 30-day course that takes a product manager with no software background to
Forward Deployed Engineer interview readiness.

Built from `../FDE_Report`, which maps Vas of Varick Agents' 30-day plan (via Greg
Isenberg's *The Startup Ideas Podcast*) onto canonical primary sources — Anthropic's
engineering essays, the ReAct paper, the AWS and Google SRE reliability literature,
and Hamel Husain & Shreya Shankar's evals work.

## How to read it

Two surfaces, same content:

- **On GitHub** — open any `day-NN-slug/README.md`. Diagrams render, and the
  self-test dropdowns at the end of each day expand natively.
- **As one page** — `index.html` puts all 30 days behind a left sidebar with
  progress tracking and a light/dark toggle. Open it in a browser, or read the
  published version.

Each day is 60–70 minutes at a careful reading pace. The structure is identical across all 30:

| § | Section | What it's for |
|---|---|---|
| 1 | Why this day exists | The interview question this day answers |
| 2 | Explain it like I'm five | One analogy, no jargon |
| 3 | The concept, properly | Three depth tiers: shape → mechanism → what an interviewer digs into |
| 4 | What the resources say | Digest of each source, so you get four hours of reading in one |
| 5 | Suggested exercise (optional) | Named and justified. Skip it if you're reading only |
| 6 | Where it breaks | Failure modes — the FDE job *is* failure modes |
| 7 | Watch this | Max 2 videos, timestamps only where the video publishes chapters |
| 8 | Say this in an interview | Weak answer vs. strong answer, side by side |
| 9 | Vocabulary | Terms, merged into `GLOSSARY.md` |
| 10 | Test yourself | 8–12 questions with hidden answers |

## Structure

```
course/
  README.md                     this file
  index.html                    the single-page build (generated — don't edit)
  build.py                      assembles the days into index.html
  GLOSSARY.md                   every term, defined once
  _meta/
    STYLE_GUIDE.md              the authoring contract
    DAY_MAP.md                  day boundaries + gap-fill assignments
    days.json                   the 30-day manifest
  day-01-agent-loop/
    README.md                   the day you read
    diagrams/*.svg              self-contained, no external assets
  day-02-tool-use/
  ...
evals/
  check_day.py                  deterministic quality gate
  make_issues.py                generates the GitHub issue bodies from FDE_Report
```

## Setup

**The venv lives outside the project.** This directory's name contains a colon
(`FDE:AI-PM`), and Python refuses to create a virtual environment inside such a path.
So it's at `~/.venvs/fde-course`:

```bash
python3 -m venv ~/.venvs/fde-course
~/.venvs/fde-course/bin/pip install markdown
```

Rebuild the single page after editing any day:

```bash
~/.venvs/fde-course/bin/python course/build.py
```

Check a day against the contract (needs no venv — stdlib only):

```bash
python3 evals/check_day.py course/day-01-agent-loop/README.md
python3 evals/check_day.py 'course/day-*/README.md'          # all days
python3 evals/check_day.py course/day-01-agent-loop/README.md --offline   # skip link checks
```

The gate fails a day for: missing or out-of-order sections, word count outside
6,500–10,000 (it warns above the 9,000-word target), fewer than 8 or more than 12
self-test questions, a dropdown that won't
render on GitHub, more than 2 videos, **any timestamp without a stated source**, an SVG
that isn't self-contained, or a dead link.

## Quality gates

Each day passes three gates before it's marked done:

1. **`check_day.py`** — everything a machine can decide.
2. **Reviewer 1** — technical accuracy and whether a non-technical PM can actually
   follow it.
3. **Reviewer 2** — an adversarial interviewer that tries to *fail* the reader using
   only that day's material. If it succeeds easily, the day goes back.

The anti-hallucination rules are in `_meta/STYLE_GUIDE.md` §5. The short version:
every non-obvious claim carries a source link, quotes are verbatim or aren't quotes,
timestamps come from published chapter data or don't appear, and genuine disagreements
between practitioners are presented as disagreements rather than resolved.

## Progress

Tracked as GitHub issues — one per day, plus
[the epic](https://github.com/as2621-dev/FDE-AI-PM/issues/1). Labels
`status:backlog` → `status:in-progress` → `status:review` → `status:done`.

## Diagram tooling

Diagrams follow [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design),
vendored to `.tools/diagram-design` (gitignored). One deliberate deviation from that
skill: diagrams here use **presentation attributes rather than CSS classes**, because
the same `.svg` file has to render both in a GitHub README and inlined into a page
under a strict content-security policy. CSS classes silently lose all styling when the
SVG is used standalone.

## Scope note

This course is **reading-only** by design. Every day in the source plan has a hands-on
coding exercise; here they're named, justified, and marked optional. That's a
deliberate trade: it makes you strong on the customer-discovery and solution-design
rounds, and it does *not* prepare you for a live-coding round. If you get an interview
scheduled, add the hands-on layer before you sit it.
