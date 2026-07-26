---
title: A search summary will hand you a finding the paper does not contain
tags: [sourcing, websearch, webfetch, citation, hallucination, course-day, gate-blind-spot]
problem_type: convention
symptoms: A quotable, specific, on-topic number that survives every check except opening the source.
date: 2026-07-26
---

Extends [[sourcing-traps-for-course-days]], which covers quoting from a search-engine
snippet. This is the harder version: the summary states a **finding**, not a quote, so there
are no quote marks to warn you.

Researching Day 4, `WebSearch` returned this as a key result of Chroma's *Context Rot*
report:

> "a 200K-token window can show serious accuracy loss at 50K tokens of input, and a 1M-token
> window does not reliably reason across 1M tokens"

It is plausible, it is precisely the shape of claim the day needed, and it is **not in the
report**. Over the fetched page:

```sh
grep -io "50k\|50,000\|serious accuracy\|accuracy loss" chroma.txt   # → no output
```

Had it shipped it would have been the day's most quotable number, cited to a real report at a
live URL, and the link check would have passed. `check_day.py` verifies that a URL resolves;
nothing verifies that the page says what you claim.

**The rule that holds.** Every quote and every characterisation comes from a body you fetched
and kept:

```sh
curl -sSL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36" "$url" -o src.html
python3 -c "import re,html;t=open('src.html',errors='replace').read();t=re.sub(r'<(script|style).*?</\1>','',t,flags=re.S);t=re.sub(r'<[^>]+>',' ',t);open('src.txt','w').write(html.unescape(re.sub(r'[ \t]+',' ',t)))"
grep -o "the exact phrase you plan to quote" src.txt
```

Then `grep` the file for each claim before writing it. Keep the stripped text in the
scratchpad for the whole slice, because reviewers will ask you to re-verify.

**`WebFetch` is the same hazard with better manners.** It renders the page through a small
model, so what comes back is a paraphrase. Day 4 called `WebFetch` once, for the MemGPT
abstract, and got a clean-looking abstract in quotation marks — which was then discarded and
re-fetched from `arxiv.org`'s `<blockquote class="abstract">` before any of it was quoted. Use
`WebFetch` to decide whether a page is worth reading. Never to source a quote.

**Two related checks that paid off on the same slice.**

- **`FDE_Report` contains no URLs at all** (`grep -c 'http' FDE_Report` → `0`); its resource
  tables name sources in prose. So "the URL in `FDE_Report` has moved" cannot be true of any
  source, however true it is that the source moved. Day 4 shipped that sentence in draft and a
  reviewer caught it; Day 3 has it in two places still (filed in
  `docs/residual-review-findings/86f7bd6.md`). **Verify a claim about the course's own files
  the same way you verify a claim about a vendor's.**
- **A report's appendix will quietly narrow its headline.** Chroma's summary says it evaluates
  18 models; its appendix says *"Not all 18 models are included in each experiement due to
  context window or thinking_budget constraints."* So "across all 18 of them" is not available
  as a general claim, though `"Across all experiments, model performance consistently degrades
  with increasing input length."` is — and is stronger. **Read the appendix before writing
  "all".**
