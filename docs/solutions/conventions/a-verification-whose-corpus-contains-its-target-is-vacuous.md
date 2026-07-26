---
title: A verification whose corpus can contain its own target reports success by construction
tags: [sourcing, quotes, verbatim, tooling, false-negative, course-day, gate-blind-spot]
symptoms: The quote check reports 90 strings and 0 unmatched, and it has not checked anything.
problem_type: convention
date: 2026-07-26
---

[[machine-check-every-quoted-string]] gives the script. Day 7 ran it and got **90 quoted strings,
0 unmatched** — a perfect result, on a day with 44 distinct quotes including invented interview
dialogue that appears in no source anywhere. The corpus glob was:

```python
glob.glob('src/*.txt') + glob.glob('course/day-0*/README.md')
```

`course/day-0*` matches `day-07`. **The file being checked was inside its own corpus**, so every
string in it matched itself. Re-running with the target excluded turned 0 unmatched into 28, of
which one was a real defect that would have shipped.

**Why the clean result should have been the tell.** The note already says to expect ~65% of misses
to be your own prose. Zero misses on a document containing your own §8 dialogue is not a good
score; it is arithmetically impossible unless the check is broken. **Treat an implausibly clean
verification as a failure of the verification, not as a result.**

**Two lines that make it safe.** Exclude the target explicitly, and prove the check can fail:

```python
DAY = 'course/day-07-week-1-checkpoint/README.md'
srcs = [f for f in glob.glob('src/*.txt') + glob.glob('course/day-0*/README.md') if f != DAY]
...
# teeth test — both must report MISS, or the corpus is wrong
for s in ["You must configure a checkpointerx to persist the graph state",
          "the simplest solution possible and only increasing complexity"]:
    assert s not in corpus and s not in flat, "check has no teeth"
```

The second string is the real quote with one comma removed. If a one-character corruption still
matches, the normaliser is stripping too much.

**Generalise past quote-checking.** The class is *a test whose fixture can include the thing under
test*. It shows up wherever a corpus is assembled by a glob or a directory walk: a link checker
that finds the URL in its own report, a duplicate-detector fed its own output, a "does the glossary
define this term" check whose term list is scraped from the glossary. In every case the failure
direction is the dangerous one — [[two-column-pdfs-defeat-quote-matching]] describes a check that
cries wolf, which merely wastes a round trip. This one goes quiet, and a quiet check is
indistinguishable from a passing one.

**The check to add once, anywhere a corpus is built by pattern:** print the corpus file list before
using it, and read it. Day 7's list was 52 files long and `day-07-week-1-checkpoint` was sitting in
it in plain sight.
