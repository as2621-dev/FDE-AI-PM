---
title: A chapter marker has a start AND an end — citing the wrong one passes every check
tags: [video, timestamps, yt-dlp, sourcing, course-day, gate-blind-spot, review-catch]
symptoms: Every timestamp is sourced, labelled "(chapter marker)", gate-green, and two of them open the wrong chapter.
problem_type: convention
date: 2026-07-26
---

Days 2, 3 and 4 all cited published chapter markers rather than transcript timestamps, which
`docs/solutions/conventions/sourcing-traps-for-course-days.md` recommends because chapters are
human-authored and need no auto-caption hedge. Day 5 did the same and still shipped two wrong
timestamps into its first commit. Both reviewers who checked the videos found them.

**The mistake.** `yt-dlp --skip-download --print "%(chapters)s"` returns objects, not times:

```python
{'start_time': 355.0, 'title': 'How OTel Helps with GenAI-Powered Features', 'end_time': 550.0}
{'start_time': 675.0, 'title': 'The Challenge of "Architectural Blindness"',  'end_time': 822.0}
```

Day 5 converted `550` → `9:10` and `822` → `13:42` and labelled both "(chapter marker)". They are
the **end** times. `5:55` and `11:15` are the chapters. Worse than merely imprecise: `9:10` is the
start of the *next* chapter, so the citation dropped the reader into a chapter the same paragraph
told him to skip.

**Why nothing caught it.** `check_day.py`'s timestamp gate only asks whether the line names a
source, and the line said "(chapter marker)", truthfully. The number came from the video's own
metadata, so it is sourced. It is sourced *to the wrong field*. Reading the day back does not help
either, because a plausible-looking timestamp next to a real chapter title reads as correct.

**The check that works.** Print the two fields separately so `end_time` never enters the pipeline,
and convert with code rather than by hand:

```sh
yt-dlp --skip-download --print "%(chapters)j" "$url" | python3 -c "
import json,sys
for c in json.load(sys.stdin):
    print(f\"{int(c['start_time'])//60}:{int(c['start_time'])%60:02d}  {c['title']}\")"
```

Then cross-check against the video **description**, which for any channel that writes its own
chapters contains the same list already formatted as `MM:SS - Title`. Two independent renderings of
the same fact, and the description costs one extra `--print "%(description)s"`.

**Generalise it.** The class of bug is *a correct value read from the wrong field of a correct
source*. It defeats every check the course has, because provenance is intact and only the field
selection is wrong. Anywhere a source hands you a structured record with several numeric fields —
chapters, token usage, span timings, price tables with input and output columns — name the field in
your own notes as you extract it, and re-derive the citation from the named field rather than from a
number you already wrote down.

**Also worth keeping, from the same slice.** Two more defects of exactly this shape, both caught by
the panel rather than by the gate:

- **A diagram's bar widths must be re-derived from their labels, not eyeballed.** Day 5's first
  span-tree drew an 86-pixel bar labelled `0.4 s` next to a 150-pixel bar labelled `2.9 s`. Pick one
  scale (`px per second`), compute every width from it, and check the children sum to less than the
  parent.
- **An attribute whose name contains a word is not the thing that word means.**
  `gen_ai.conversation.id` reads like a run identifier and is not — the registry defines it as "The
  unique identifier for a conversation (session, thread)". Day 5's draft used it as the run ID in one
  place while its own vocabulary table mapped it to *session*. All three reviewers found it. Read the
  registry's `brief` for every attribute you rely on, even the ones whose meaning looks obvious from
  the name.
