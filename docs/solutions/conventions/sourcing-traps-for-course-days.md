---
title: Three sourcing traps that get past check_day.py
tags: [sourcing, citation, link-check, job-posting, ashby, mcp, course-day, gate-blind-spot]
problem_type: convention
symptoms: The gate goes green, both reviewer agents come back with a critical citation defect anyway.
date: 2026-07-26
---

Writing Day 2 produced three sourcing failures that `evals/check_day.py` cannot see. All
three are cheap to avoid if you know to look.

**1. HTTP 200 is not evidence the quoted text is there.** Day 2 cited a Varick Agents job
posting on Ashby. The URL returned 200, so the gate's reachability check passed — but Ashby
serves a single-page-app shell for every path, and the posting itself had been taken down.
The quoted sentence existed nowhere on the live board. For any job posting, use the board's
posting API rather than the page:

```sh
curl -sS "https://api.ashbyhq.com/posting-api/job-board/<org-slug>" | python3 -c "import json,sys; d=json.load(sys.stdin); print([j['title'] for j in d['jobs']])"
```

Generalise it: the gate proves a URL resolves, never that it *says what you claim*. Any
citation carrying a verbatim quote needs the quote checked against the fetched body, and
SPA-hosted sources (job boards, dashboards, app pages) are where a 200 lies most often.
When the original is gone, do what Day 1 did with the Vas quote — attribute it to
`FDE_Report`, mark it `⚠️ **Unverified:**`, and say what you couldn't confirm.

**2. Never quote from a search-engine snippet.** `WebSearch` returned the Varick posting
with a sentence *longer* than the one `FDE_Report` quotes — the extra clause came from a
cached page the model then presented as source text. Quote marks require a body you fetched.
If the only text you have came through a summariser, paraphrase and drop the quote marks.

**3. Attribution drifts between a launch post and its docs site.** The "USB-C port for AI
applications" line is on `modelcontextprotocol.io`, *not* in Anthropic's 25 November 2024
announcement, which `FDE_Report` implies by listing them as one resource. Two reviewers
verified both ways. Where the report bundles a post plus a docs site into a single row,
check which artefact each quote actually comes from before writing "the announcement says".

**Also worth keeping:** cite chapter markers over transcript timestamps where both exist.
Chapters come from video metadata (`yt-dlp --skip-download --print "%(chapters)s"`), are
human-authored, and need no auto-caption hedge — whereas an ASR quote needs the provenance
label §5.7 of the style guide demands. Day 2 cited four chapters and only paraphrased the
three transcript passages, because the captions garble words inside all three.
