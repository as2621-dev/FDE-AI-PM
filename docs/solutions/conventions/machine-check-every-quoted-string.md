---
title: Machine-check every quoted string against the fetched body — eye-reading misses punctuation
tags: [sourcing, citation, quotes, verbatim, course-day, gate-blind-spot, tooling, review-catch]
problem_type: convention
symptoms: Every quote came from a page you actually fetched, and two of them are still not verbatim.
date: 2026-07-26
---

`docs/solutions/conventions/search-summaries-invent-findings.md` establishes the rule: quote only
from a body you fetched and kept. This is the mechanisable version of the same rule, and it is the
step that catches what the rule alone does not. Day 5 fetched every source to disk, quoted only
from those files, eye-read the quotes twice — and still had two non-verbatim quotes in the draft.
Both were found by a script, not by reading.

**What it caught.**

1. **Punctuation the source owns and you silently changed.** Langfuse's `LICENSE` reads
   `is licensed under the license defined in "ee/LICENSE"` — with **double quotes** around the
   filename. The draft rendered it with backticks (`` `ee/LICENSE` ``) inside a quotation, which
   changes the source's punctuation inside quote marks. Same family as the trap in
   `verify-a-source-moved-not-died.md` item 3, and invisible to a human eye that reads backticks
   and double quotes as interchangeable code formatting.
2. **Terminal punctuation you invented because the source's sentence continues.** Day 6 quoted a
   First Round Review interviewee and closed with a full stop inside the quote marks. The source
   reads `...from what was sold in the contract,” she says.` — a **comma**, because the sentence
   runs on into the attribution. This is endemic to journalism: nearly every quote in a magazine
   feature is followed by `," she says`, so almost none of them end in the punctuation you would
   naturally type. The fix is to close the quote before the source's punctuation and put your own
   outside it. The draft had this defect in two places and eye-reading missed both.
3. **A quote that was a paraphrase all along.** The draft had
   `"spans nest to reflect the execution flow"`. Braintrust's actual sentence is
   *"Spans nest inside each other to reflect your application's execution flow."* Close enough to
   survive two eye passes, not close enough to be a quote.

**The script.** Run it before committing, and again after applying review findings — the fixes are
where new quote defects enter.

```sh
python3 - <<'PY'
import re, glob
day = open('course/day-NN-slug/README.md', encoding='utf-8').read()
corpus = ""
for f in glob.glob('src/*.txt') + glob.glob('src/*.md') + glob.glob('src/*.yaml') + glob.glob('src/*desc*'):
    corpus += open(f, errors='replace').read() + "\n"
assert len(corpus) > 10_000, "corpus too small — did every source get fetched to disk?"
corpus = re.sub(r'\s+', ' ', corpus)
flat = re.sub(r'`', '', corpus)
for q in re.findall(r'"([^"\n]{25,320})"', day):
    n = re.sub(r'\s+', ' ', q).strip()
    if n in corpus or re.sub(r'`', '', n) in flat:
        continue
    print("UNMATCHED:", n[:110])
PY
```

**Four things that make the output readable rather than alarming.**

- **Normalise backticks on *both* sides, or you get false misses.** The spec's YAML contains
  backticks too (`` SHOULD set it to `true` only when… ``). Stripping them from the quote but not
  the corpus reports a miss on a perfectly good quote. Day 5 hit this on four quotes before
  fixing the normaliser.
- **Expect most misses to be your own prose, and know why each one is.** Of Day 5's 64 quoted
  strings, 22 were source quotes; the rest were interview questions, customer dialogue, `alt`
  text, `<summary>` lines and video titles. The script cannot tell those apart, so **read every
  line of output** — the technique only works if an unexplained miss stops you.
- **Put non-HTML sources in the corpus too.** A quote from a video description or a `LICENSE` file
  will report as a miss purely because the file was not in the glob. Day 5 got a false miss on the
  `# Moved: Generative AI semantic conventions` line for exactly that reason. Add
  `yt-dlp --skip-download --print "%(description)s" "$url" > src/vid-desc.txt` and
  `curl -sSL .../LICENSE -o src/x-LICENSE.txt` before believing a miss.
- **An ellipsis inside a quote defeats exact matching, so shorten instead of eliding.** Day 5's
  draft had `"A trace represents one end-to-end execution... Every trace contains one or more
  spans"`. Replaced with the short exact fragment. A quote you cannot machine-verify is a quote you
  cannot defend.

**Why this beats a reviewer doing it.** A review panel *can* do this — Day 4's did, machine-checking
82 strings against six sources and finding two punctuation slips. But a reviewer finding it costs a
full round trip, and on Day 5 the writer running it first meant the panel's own quote pass returned
**nothing further** on 22 source quotes. That silence is the signal the check is complete, and it is
worth far more than a clean-looking finding list.

- **A PDF in two columns will report false misses in both `pdftotext` modes.** Do not believe a PDF
  miss until you have printed the raw characters around it; see
  [[two-column-pdfs-defeat-quote-matching]] for the gutter-split recipe that makes the corpus usable.

**The general shape**, which is the same one as
`chapter-markers-carry-an-end-time-too.md`: provenance being intact says nothing about the value
being right. Fetching the page proves you had access to the truth. Only a character comparison
proves you copied it.
