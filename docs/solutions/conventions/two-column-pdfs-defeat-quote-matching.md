---
title: A two-column PDF defeats exact quote matching in both pdftotext modes
tags: [sourcing, citation, quotes, verbatim, pdf, pdftotext, tooling, course-day, false-positive]
symptoms: The quote-verification script reports UNMATCHED on three quotes that are demonstrably verbatim in the PDF.
problem_type: convention
date: 2026-07-26
---

[[machine-check-every-quoted-string]] says to put non-HTML sources in the corpus. Day 6 did — a
five-page Anthropic whitepaper, extracted with `pdftotext` — and the check reported three misses on
quotes that are **word-for-word correct in the source**. The failure is in the extraction, not the
quote, and it is the dangerous direction: a check that cries wolf on a correct quote gets ignored,
and then it stops catching the real ones.

**Both obvious modes fail, for opposite reasons.**

`pdftotext -layout` preserves the visual columns. That means **the adjacent column's text is spliced
between the lines of your quote.** One sentence came out as:

```
Think about it this way: if you need to explain exactly why the system made a
specific decision to auditors, regulators, or executives, you want predictable,      Limited budget/tokens → Single agents or carefully designed parallel
traceable behavior. A single agent handling loan approvals with clear decision       workflows
```

Collapsing whitespace cannot repair that — `Limited budget/tokens` is now *inside* the quote.

`pdftotext -raw` reads in flow order, so the columns no longer interleave, but it **drops
inter-word spaces**: the same file yields `operationsintosingle-agent operations`. Every quote longer
than a few words hits at least one dropped space.

**The fix: rebuild each column from the `-layout` output by splitting every line at the gutter.**

```python
lines = open('doc.txt', errors='replace').read().splitlines()
GUT = 85                      # column width; find it by eye in the -layout output
left  = [ln[:GUT].rstrip() for ln in lines]
right = [ln[GUT:].rstrip()  for ln in lines]
open('doc-cols.txt','w').write("\n".join(left) + "\n\n=====COL2=====\n\n" + "\n".join(right))
```

Put `doc-cols.txt` in the corpus alongside the `-layout` version and the check returns clean. On
Day 6 that took all 48 quoted strings to **zero unexplained misses**.

**Before believing any PDF miss, print the raw characters around each occurrence.** This is the
step that distinguishes an extraction artefact from a real defect, and it takes one command:

```python
import re
t = open('doc.txt', errors='replace').read()
for m in re.finditer(re.escape("stopping condition"), t):
    print(repr(t[max(0, m.start()-320) : m.start()+200]))
```

Reading `repr()` rather than the text is the point — you see the newlines and the run of spaces that
are breaking the match, and you can then read the columns in order yourself.

**Generalisation.** Provenance intact says nothing about the value being right
([[chapter-markers-carry-an-end-time-too]]), and *a character comparison failing* says nothing about
the quote being wrong. Both directions need the same discipline: go back to the bytes. Find the
gutter width before you trust a PDF corpus, and never "fix" a quote because a script missed it —
[[verify-a-source-moved-not-died]] is the same instinct applied to links.
