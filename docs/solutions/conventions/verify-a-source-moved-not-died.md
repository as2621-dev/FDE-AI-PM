---
title: Four ways a source lies about being reachable
tags: [sourcing, link-check, citation, user-agent, redirect, course-day, gate-blind-spot]
problem_type: convention
symptoms: A source looks dead, or looks fine, and the gate agrees with the wrong one.
date: 2026-07-26
---

Extends [sourcing-traps-for-course-days](sourcing-traps-for-course-days.md), which covers
the SPA-that-returns-200 case. Day 3 hit four more, and three of them would have put a
false statement in front of the reader.

**1. A 403 is usually a bot block, not a dead page.** `hhs.gov` returns HTTP 403 to
`curl` for every HIPAA page, with a full browser user-agent and `Accept` headers too —
it is Akamai refusing automation, and the pages are live in a browser. `check_day.py`
handles this gracefully (403 downgrades to a `could not verify` **warning**, not a
failure), so the gate will not stop you citing a page you never read.

The fix is not to force the fetch. It is to **cite the primary source instead**, which
is better anyway: HIPAA lives in the eCFR, which serves clean text to `curl` and is
authoritative rather than explanatory.

```sh
curl -sSL "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.306"
```

For any regulation, prefer eCFR over the agency's summary page. For any standard, expect
the definitions to sit behind a paywall (see 4).

**2. Docs sites move and redirect silently, so `FDE_Report`'s URLs are stale by default.**
Three of Day 3's four assigned resources had moved:

| `FDE_Report` says | Actually resolves to |
|---|---|
| `docs.nvidia.com/nemo/guardrails/latest/index.html` | `…/about-nemo-guardrails-library/overview` |
| `github.com/NVIDIA/NeMo-Guardrails` | `github.com/NVIDIA-NeMo/Guardrails` |
| `www.guardrailsai.com/docs` | `guardrailsai.com/guardrails/docs` |
| `hub.guardrailsai.com` | `guardrailsai.com/hub` |

All four return 200 because they redirect, so the gate is happy and the day cites an
address that will break later. Always resolve before citing, and cite the destination:

```sh
curl -sS -o /dev/null -w "%{http_code} -> %{url_effective}\n" -L "$url"
```

NVIDIA's docs also serve clean Markdown — append `.md` to any page, and `/llms.txt` at
the root gives a page index. Use it instead of stripping HTML.

**3. Quoting a bulleted list as a sentence is not verbatim.** The OpenAI Agents SDK page
renders "There are two kinds of guardrails:" followed by two `<li>` items with **no
terminal periods**. Quoting it as one flowing sentence means inserting two full stops
that are not in the source. A reviewer caught it. Either quote the fragments as
fragments, or drop the quote marks. Same trap on the Claude Code security page, whose
`<li><strong>Isolated context windows</strong>: …prompts</li>` has no closing period —
put yours outside the quote marks.

**4. When a definition is paywalled, say so instead of borrowing one.** The SOC 2
Type 1 / Type 2 distinction is real, standard, and **not on any free AICPA page** — not
the SOC suite landing page, not the SOC 2 topic page. It sits in paid guides. The
tempting fixes are both wrong: inventing the definition, or lifting it from a compliance
vendor's blog, which the report's own caveats warn about laundering.

What shipped instead: the sourced fact (Anthropic publishes a Type 2, per its own
security page), a `⚠️ **Unverified:**` marker naming exactly what could not be
confirmed, and the two questions that work without the definition — *which type is it,
and what period does it cover*. A reviewer pushed back that the reader will be *told*
this in a meeting rather than asking it, which is fair; the answer was to add "if
someone asks you to define the types, say you'd confirm the wording with their auditor"
rather than to manufacture the definition. **An honest gap the reader can act around
beats a definition you cannot defend.**

**Also worth keeping:** cite chapter markers, never transcript timestamps, when the
video has both. Day 3 cited eight timestamps across two videos and needed no
auto-caption hedge and no committed `.vtt` file, because every one was a published
chapter. Check with:

```sh
yt-dlp --skip-download --print "%(title)s|%(channel)s|%(duration_string)s|%(upload_date)s|%(chapters)s" "$url"
```

And read the description before characterising a video: the IBM OWASP explainer says in
its own description that Jeff Crume "explains **a subset** of them", which makes "walks
the list" false — six chapters covering five of ten entries.
