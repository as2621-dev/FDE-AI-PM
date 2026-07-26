# Authoring contract — read this fully before writing any day

You are writing one day of a 30-day course that takes a **non-technical product manager**
from zero to interview-ready for a **Forward Deployed Engineer (FDE)** role.

This file is the contract. Every rule here is enforced either by `evals/check_day.py`
(deterministic) or by two reviewer agents (judgment). Violating the contract sends the
day back for a rewrite, so read it before you start, not after.

---

## 1. Who you are writing for

One specific person. Write for him, not for a general audience.

- **Mechanical engineer by training. Product manager by profession.**
- **Zero software background.** He has not written code. He does not know what a
  dictionary, a decorator, or a stack trace is. He has never used a terminal.
- **He is not stupid — he is untrained.** He models complex physical systems for a
  living. He understands feedback loops, tolerance stacks, failure modes, control
  systems, and root-cause analysis better than most engineers understand them.
  Use that. It is your single biggest lever.
- **His goal is passing an FDE interview**, not shipping production code. Every
  paragraph should move him toward being able to *hold a conversation* about this
  topic with an engineer who does it for a living.
- **He is reading, not typing.** He chose a reading-only course. Do not build the day
  around an assumption that he ran anything.

### The mechanical-engineering bridge

Reach for the analogy from his world before you reach for the software one.

| Instead of the software framing | Use |
|---|---|
| Retry with exponential backoff | Relief valve cycling; not slamming a pump back on instantly |
| Idempotency | A torque wrench that clicks once — pulling the trigger twice doesn't double the torque |
| Context window | A workbench. Pile on too much and you can't find the tool you need |
| Evals | A test rig / QA jig on the production line |
| Failure taxonomy | FMEA — failure mode and effects analysis |
| Guardrails | Interlocks and limit switches |
| Checkpointing | Marking your position before you stop a partially-machined part |
| Observability / tracing | Instrumenting a test bench with sensors at every stage |

**One analogy per day, used well, beats five used shallowly.** If the analogy starts to
break down, say so explicitly — "the analogy stops working here, because…". A silently
leaky analogy teaches the wrong model, which is worse than no analogy.

---

## 2. Voice

- **Answer first, then explain.** Never build up to the point.
- **Second person.** "You'd hit this when…" not "One might encounter…"
- **Short sentences. Concrete nouns.** Cut every "it's important to note that".
- **No cheerleading.** No "Great question!", no "Let's dive in!", no "Congratulations,
  you now understand…". He will read 30 of these. Enthusiasm becomes noise.
- **Never use a term before you define it.** Not once. This is the single most common
  way these documents fail. The first time a term appears in the day, it is either
  already in the glossary from an earlier day, or you define it inline in that sentence.
- **Own the uncertainty.** If a claim is contested, say who contests it. If a number
  drifts, say so. "Anthropic and Cognition publicly disagree about this" is a *better*
  sentence than a confident synthesis, and it is what makes him sound credible in a room.

### The two rules that Day 1's review produced

Day 1 came back **NEEDS WORK** from the adversarial interviewer for one repeated habit:
it delivered every insight and withheld every specific — the max-step cap's *purpose*
without its *value*, the economics without the arithmetic, benchmark numbers without the
baseline's definition, the stations without the unhappy path. That habit is invisible in
a single day and fatal across thirty. These two rules exist to kill it:

**Rule A — define every term you quote a number about, on the day you quote it.**
Day 1 handed the reader ReAct's `27.4 vs 29.4` as their credibility move and never
defined chain-of-thought, the baseline the comparison is *against*. One four-word
question — "what's chain-of-thought?" — converts the reader's strongest move into proof
they're reciting a table they can't read, and retroactively discounts every other number
they cited. If you quote a figure, the reader must be able to define both sides of it.

**What discharges the rule.** A term is covered if *either* your own §9 table defines it, *or*
`course/GLOSSARY.md` already defines it from an earlier day. Re-defining what an earlier day
taught is padding — the reader has met it, and every day would carry the same tokens-and-passes
preamble. So this is not a rule to define more; it is a rule to leave nothing undefined.

**But verify, don't assume.** The failure this rule exists to prevent is a term the reader has
*never* been given, cited as though they had. Open `GLOSSARY.md` and confirm the entry is
actually there before relying on it. Day 2's cost derivation was correct only because Day 1's
`Token` entry happens to say input and output are priced separately — had it not, the reader
could not have reconstructed the figure, and nothing in the day would have shown it.

Check every number in your day against both tables before you finish.

**Rule B — teach no control without a method for setting it.**
If your day introduces a knob — a step cap, a threshold, a timeout, a confidence cutoff,
a retry count, a pass rate — you must give a defensible way to arrive at the number.
"Often between five and twenty-five" and "the library default is 20" are not methods; in
a solution-design round the number *is* the deliverable. A method looks like: derive a
floor from the task's own structure, multiply for known failure paths, then once you have
traces set it against the observed distribution — and say what the number trades in each
direction.

**Subject knobs owe a full method; input knobs owe less.** Asked on Day 4, whose compaction
trigger is derived from a window, a response budget *and* an output cap — three knobs, one of
which is the day's actual subject. If every nested input owed a full derivation, each day would
recurse without end: the trigger needs the response budget, which needs the window, which needs
the model, which needs the cost model.

So the test is not "is there arithmetic" but **could the reader set this himself and say why.**
The knob the day is *about* owes the full treatment — floor, worst case, what it trades, and how
traces replace the assumption. A knob that merely *feeds* that method owes enough to pick it and
defend it, which is often one clause tying it to the shape of the task. Day 4's output cap is the
worked example: "an agent whose replies are a short reasoning trace plus a tool call rarely needs
more, while an agent that writes a final report needs far more and moves this arithmetic." That is
a method — it tells him which way to move and on what evidence — and it is correctly not a
derivation.

What this does **not** license is naming a number with no reason at all because it is "only an
input." If you cannot write the one clause, you do not understand the knob well enough to be
using it in a derivation the reader is meant to trust.

**Check whether your method can return an impossible value, and say what it means when it does.**
Raised by Day 5, whose sampling floor is `p ≥ k ÷ (R × f)`. At a 0.05% failure rate that returns
250%, which is not a rate — it is the finding that sampling cannot deliver that failure class at
all, and no amount of tuning the number will fix it. Rule B asks what a number trades; on its own
it never asks whether the formula has a domain. Push your own method to its edges — a rate above
100%, a floor above its own ceiling, a window that goes negative — and if it breaks, that break is
usually the most useful paragraph you will write, because it tells the reader when to stop turning
the knob and change the design instead.

**Corollaries, all cheap:**

- **No uncited numbers.** Day 1's only uncited figure sat exactly where the reader most
  needed a defensible one, and would have been repeated as though sourced.
- **Bind every rate or price to a specific model, inside the sentence.** Day 1 quoted
  "ten cents buys thirty to fifty thousand tokens" four lines above a table whose rates
  make that impossible — a ~$2.50/M blended figure next to Opus at $5/$25.
- **Don't quote precision the reader can't contextualise.** A three-digit token overhead
  invites "and what fraction of your run is that?" Give the run total, or lead with the
  insight and leave the number in the citation.
- **Cover the unhappy path in §6.** If your day defines a step where something external
  is touched, one row must be *that external thing failing* — the most common event in a
  deployed system. Day 1's §6 had eight rows and not one was the tool failing.

### On "say this in an interview"

§8 exists because the reader is preparing for a conversation. But a day that plants three
aphorisms and tells the reader to deploy them produces a **fluent tourist** — someone who
opens with a rehearsed line and has nothing behind it.

- **Never instruct the reader to say a line unattached to a consequence.** Not *"say this
  out loud"* but *"say this, then immediately name what it means for their deployment."*
  The line earns its place by what follows it.
- **Reframe recall as recognition.** Not *"memorise the three principles"* or *"you should
  be able to reel these off"* — reciting a canonical triplet is the most common tell in
  this subject area. Instead: *"you should recognise these when a customer describes one,
  and be able to say which one their process already is."*
- **Mark what's for understanding vs. what's for saying.** The reader cannot yet tell the
  difference, and authorial motivation ("that's what gets you hired") reads as a landmine
  when it lands in a vocabulary table they're memorising. Keep motivation in §1.

### Banned constructions

- "Simply", "just", "obviously", "of course", "as you know" — all of these tell a
  beginner he should already understand something he doesn't.
- Em-dash-heavy stacking of three or more clauses. Break the sentence up.
- Paragraphs longer than six lines. Break them up.
- Any sentence that describes what the section is about to do ("In this section we
  will explore…"). Delete it and start with the content.

---

## 3. The 10-section template — headings are exact

Use these headings **verbatim**, including the numbers. `check_day.py` greps for them.

```markdown
---
day: 4
slug: context-and-memory
title: Context and memory
week: 1
week_title: Build an agent that can complete a real loop
one_liner: Why stuffing more into the prompt makes the agent worse, not better.
reading_minutes: 54
---

# Day 4 — Context and memory

> **The interview question this day answers:**
> "Your agent's accuracy drops as the conversation gets longer. Why, and what do you do?"

## 1. Why this day exists
## 2. Explain it like I'm five
## 3. The concept, properly
## 4. What the resources say
## 5. Suggested exercise (optional)
## 6. Where it breaks
## 7. Watch this
## 8. Say this in an interview
## 9. Vocabulary
## 10. Test yourself
```

### Section-by-section spec

**1. Why this day exists** *(~200 words)*
The interview question this day answers, and what he'd fumble today without it. Be
specific about the failure: "you'd say 'we use a big context window', and the
interviewer would ask what happens at 100k tokens, and you'd have nothing."

**2. Explain it like I'm five** *(~400 words)*
One analogy from §1's bridge table, or a better one you invent. No jargon at all in
this section — if a term is unavoidable, you haven't found the right analogy yet.
End with one sentence that states the real concept in plain English.

**3. The concept, properly** *(~1,800 words — the core of the day)*
Three explicit depth tiers, as sub-headings:

```markdown
### Tier 1 — The shape of it
### Tier 2 — How it actually works
### Tier 3 — What an interviewer digs into
```

- **Tier 1** — the mental model. Diagram goes here.
- **Tier 2** — the real mechanism. Numbers, names, tradeoffs. This is where he stops
  being a tourist. Short code snippets are welcome here *if they illuminate the
  concept* — always with a plain-English line-by-line gloss underneath. Code is a
  teaching aid, never homework.
- **Tier 3** — the second- and third-order questions. Where practitioners disagree.
  What the naive answer misses. This tier is what separates "read about it" from
  "can defend it."

**4. What the resources say** *(~1,200 words)*
One sub-block per resource listed for this day in `FDE_Report`. He is not going to
read four hours of source material, so **you** read it and give him the substance:

```markdown
### Anthropic — "Building effective agents"
**What it is:** Essay, ~45 min, free. [Link](https://…)
**The one idea to take:** …
**The line worth quoting in an interview:** "…" *(verbatim, in quotes)*
**Skip if:** …
```

Every resource in the day's table gets a block. If a resource turns out to be
paywalled, dead, or not worth his time, **say so plainly** and say what to read instead.
That is more useful than a dutiful summary.

**5. Suggested exercise (optional)** *(~300 words)*
The exercise from `FDE_Report` for this day. Frame it as: here is the exercise, here is
specifically what doing it would teach you that reading cannot, and here is roughly
what it involves. Then: **"Optional — skip it if you're reading only."**

Do not write a tutorial. Do not write setup instructions. Name it, justify it, release him.

**6. Where it breaks** *(~600 words)*
Failure modes. This section is disproportionately valuable, because the FDE job *is*
failure modes — the report's own thesis is *"there's only one way something can go
right, but there's a thousand different ways something can go wrong."*

Prefer a table: failure mode → what it looks like in production → the mitigation.

**7. Watch this** *(max 2 videos — see §5 for the hard rules)*

**8. Say this in an interview** *(~500 words)*
Two or three likely questions. For each, a **weak answer** and a **strong answer**,
side by side, plus one line on *why* the strong one lands. The weak answer must be
genuinely plausible — the kind of thing he would actually say — not a straw man.

```markdown
### "How do you decide between a workflow and an agent?"

**Weak:** "We'd use an agent, they're more flexible and powerful."

**Strong:** "I'd default to the workflow. An agent earns its cost when the path
can't be known in advance…"

**Why the strong one lands:** it shows you optimise for the customer's reliability
budget, not for using the fancier tool.
```

**9. Vocabulary** *(a table)*
Every term introduced today. Three columns: term → one-sentence definition → why an
FDE cares. These get merged into `course/GLOSSARY.md`. Do not list terms from earlier
days; link to the glossary instead.

**10. Test yourself** *(8–12 Q&A, all collapsed)*
Exact markup — this renders as a native dropdown on GitHub *and* in the built page:

```markdown
<details>
<summary><b>Q1.</b> Why does adding more context sometimes make an agent worse?</summary>

Because attention is a budget, not a container. Chroma's "Context Rot" study tested
18 frontier models and found performance "grows increasingly unreliable as input
length grows" — the model is not equally attentive across a long input.

</details>
```

Requirements:
- **8 minimum, 12 maximum.**
- Blank line after `<summary>` and before `</details>` — without it GitHub won't render
  the answer body as markdown.
- Mix the types: ~4 recall, ~4 applied ("a customer says X, what do you ask?"),
  ~2 adversarial ("an interviewer pushes back with Y — what do you say?").
- Answers are 2–5 sentences. A one-word answer teaches nothing.
- At least two answers must contain a number, a name, or a verbatim quote.

---

## 4. Length

**Target: 6,500–9,000 words**, which is 45–60 minutes at a careful reading pace.
**Hard ceiling: 10,000.** `check_day.py` fails below 6,500 or above 10,000, and warns in
the 9,000–10,000 band.

Under 6,500 means you skimped on Tier 2/3 or on the resource digests.

Between 9,000 and 10,000 you pass, but you owe the reader a reason: the overflow has to
be teaching he cannot get on a later day — foundational vocabulary, or a method Rule B
requires — not restatement. If you're over 9,000 because you explained the same idea
twice in different words, you're padding. Cut the restating, not the substance.

Never treat the 10,000 ceiling as the target. A day that lands at 7,500 and teaches
everything on its DAY_MAP line is a better day than one that lands at 9,900.

---

## 5. Sourcing and anti-hallucination — the hard rules

This course is worthless if it teaches him something false with confidence. He cannot
detect your errors. An interviewer can.

1. **Every non-obvious technical claim carries an inline source link.** Numbers, prices,
   percentages, dates, version names, and "X said Y" attributions all count as
   non-obvious. Common-knowledge framing does not.
2. **Verbatim quotes must be verbatim.** If you cannot reproduce it exactly, paraphrase
   and drop the quote marks. A misquote he repeats in an interview is a disaster.
3. **You may not invent a URL.** Fetch it. If a URL in `FDE_Report` is dead, say
   "this link was dead as of writing" and find the live equivalent.
4. **Prices, model names, and rate limits drift.** Where you cite one, add the date you
   checked it: *"as of the provider's pricing page, checked July 2026."*
5. **If you cannot source a claim, cut it.** If it's too important to cut, mark it
   `⚠️ **Unverified:**` and say what you couldn't confirm. The reviewer agents check
   for unmarked unsourced claims.
6. **Do not resolve a genuine disagreement.** Where practitioners disagree (single vs.
   multi-agent is the obvious one), present both sides with attribution. Fake consensus
   is a hallucination too.
7. **A characterisation of a source is itself a claim.** This is the failure mode Day 1
   actually shipped: every quoted string was verbatim, and three *descriptions* of what
   the sources said were wrong anyway. The paper said "one frequent error pattern"; the
   day wrote "most frequent." The day said an idea "isn't in the essay" when the essay
   contains it and the speaker says all three ideas came from it. The day said ReAct
   "did not win" on two benchmarks, then reported a win six words later in the same
   sentence. Verbatim quoting is not enough — when you write *the paper found*, *the essay
   omits*, *the docs reject*, re-read the passage and check the characterisation with the
   same rigour as the quote. Superlatives ("most", "only", "never", "isn't in"), absence
   claims, and win/loss framings are the ones that break.
8. **Check your diagram against your own caption and code.** Day 1's loop diagram drew an
   arrow asserting the Prompt station *writes to* the transcript, while its caption said
   Prompt *reads* it and the code showed only two appends. A diagram that contradicts the
   prose teaches the wrong model harder than no diagram, because it looks authoritative.
   Read the SVG's arrow directions back in words before you ship it.

### Video rules — max 2 per day

1. **Maximum two videos.** One excellent video beats two mediocre ones. If only one is
   worth his time, list one.
2. **Verify the video exists and is the video you think it is.** Fetch the page. Confirm
   the title and channel. A dead or misattributed link is a hard fail.
3. **Timestamps: only from evidence.** You may cite a timestamp *only* if you obtained
   it from the video's published chapter markers, its description, or its transcript.
   You may **never** estimate or infer one.
4. **No evidence? Say so.** Write: *"No chapter markers — watch the whole thing (25 min)."*
   That is a passing answer. A fabricated "watch from 14:32" is a failing one, because
   it wastes his time in the most demoralising possible way.
5. **Commit the transcript you cited.** If you fetch a transcript, save it to
   `.agents/transcripts/<VIDEO_ID>.en.auto.vtt` so every citation stays re-checkable
   after the fact. YouTube's `timedtext` API returns an empty body to an unauthenticated
   GET — an empty response is **not** evidence that captions don't exist. Use:

   ```sh
   yt-dlp --skip-download --write-auto-subs --sub-lang "en.*" --sub-format vtt \
     -o "<VIDEO_ID>" "https://www.youtube.com/watch?v=<VIDEO_ID>"
   ```

6. **Timestamp rule, stated exactly:** cite **the first cue in which the quoted words
   begin**, not the cue where the phrase completes. Auto-captions roll across cues, so a
   long quote spans several — citing the completion point drops the viewer mid-sentence.
7. **Auto-captions are ASR, not certified transcription.** They mishear things. When you
   quote from an auto-generated transcript you may keep the quote marks **only** if you
   (a) reproduce it exactly from the committed file, and (b) label the provenance inline:
   *"(from the transcript at `05:51`; the captions are auto-generated, so treat the
   wording as close rather than certified)"*. Check the surrounding cues for obvious
   mishearings before trusting a span — and if the error falls **inside** the words you
   want to quote, paraphrase and drop the quote marks instead. A published-chapter title
   or a quote from written text needs no such hedge.
8. Format:

```markdown
### 1. Barry Zhang (Anthropic) — "How We Build Effective Agents"
**AI Engineer Summit 2025 · 25 min · [Watch](https://…)**

Why this one: an Anthropic engineer describing the loop the way Anthropic actually
thinks about it, which is the framing your interviewer will have read.

**Worth watching:**
- `04:12` — Don't build an agent (chapter marker)
- `11:30` — Keep it simple (chapter marker)
```

---

## 6. Diagrams

Two per day is the norm. One is fine if the day is genuinely conceptual. Never zero.

Use `.tools/diagram-design/skills/diagram-design/` for the design system — read
`SKILL.md`, then the `references/type-*.md` for the type you pick, then the matching
`assets/example-*.html` for the concrete pattern.

**Override the skill's markup pattern in exactly one way.** The skill puts CSS in the
HTML `<head>`, outside the SVG. Do not do that. Instead:

- **Use presentation attributes on every element** — `fill="#2d3142"`,
  `stroke-width="1.2"`, `font-family="..."`, `font-size="12"`. **No CSS classes, no
  `<style>` block anywhere.**
- **Why:** the same `.svg` file must render correctly (a) in a GitHub markdown README
  and (b) inlined into a self-contained HTML page with a strict CSP. Presentation
  attributes are the only approach guaranteed to survive both. CSS classes silently
  lose all styling when the SVG is used standalone.
- **No external references at all** — no Google Fonts, no `<image href>`, no remote
  anything. The artifact CSP blocks every external host, and the diagram would render
  unstyled or blank.
- **Font stack, verbatim:**
  `font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, sans-serif"`
  and for mono: `font-family="ui-monospace, SFMono-Regular, Menlo, monospace"`
- **Always give the diagram its own opaque light card** — a `<rect>` filling the
  viewBox with `fill="#f5f5f5"`. It then reads identically on a light or dark page,
  the way an image does. Do not try to make diagrams theme-responsive.
- **Accessibility:** `role="img"`, a `<title>` and a `<desc>` child, both referenced
  from `aria-labelledby`.

**Palette** (from the skill's default editorial skin — keep it consistent across all 30 days):

| Role | Hex | Use |
|---|---|---|
| paper | `#f5f5f5` | card background |
| ink | `#2d3142` | primary text, node borders |
| muted | `#4f5d75` | secondary text, connectors |
| soft | `#7a8399` | tertiary text, dashed lines |
| accent | `#eb6c36` | **1–2 focal nodes per diagram only** |
| accent-tint | `rgba(235,108,54,0.08)` | focal node fill |
| link | `#2e5aa8` | cross-references |

**Density budget: aim for 4/10.** Above 9 nodes it's two diagrams. Reserve the accent
for the one or two things he should look at first — using it on five nodes destroys
the signal.

Save to `course/day-NN-slug/diagrams/name.svg`, reference from the README as:

```markdown
<img src="diagrams/agent-loop.svg" alt="The reason-act-observe loop" width="100%">
```

Every diagram needs a caption line underneath in italics, explaining what to notice.

---

## 7. Cross-linking

- Link backwards freely: `see [Day 4 — Context and memory](../day-04-context-and-memory/)`.
- **Do not re-teach an earlier day's concept.** One sentence of reminder plus a link.
  Re-teaching is how a 30-day course becomes unreadable.
- Do not link forward to days that don't exist yet. Instead: "you'll build the
  reliability layer on top of this in Week 2."
- Check `_meta/DAY_MAP.md` for what your neighbours cover. Staying inside your
  boundary is your responsibility.

---

## 8. Definition of done

A day is done when all of this is true:

- [ ] All 10 sections present, headings verbatim
- [ ] 6,500–9,000 words (10,000 hard ceiling; justify anything over 9,000)
- [ ] Frontmatter complete and valid
- [ ] Every resource from `FDE_Report`'s table for this day has a §4 block
- [ ] 8–12 Q&A, all in `<details>`, blank lines correct
- [ ] 1–2 diagrams, self-contained SVG, presentation attributes only, captioned
- [ ] ≤2 videos, both verified to exist, zero unsourced timestamps
- [ ] Every non-obvious claim sourced, or explicitly marked `⚠️ Unverified`
- [ ] Vocabulary table complete
- [ ] No term used before definition
- [ ] **Every number in the day is either cited or derived in front of the reader**
- [ ] **Every characterisation of a source re-checked against the source** (§5 rule 7)
- [ ] **Each diagram read back in words and checked against its own caption** (§5 rule 8)
- [ ] `python evals/check_day.py course/day-NN-slug/README.md` exits 0

### What the gate cannot catch — so you must

`check_day.py` verifies *form*. It cannot verify judgment, and three of Day 1's worst
defects passed it cleanly:

| Defect | Why the gate missed it |
|---|---|
| "often between five and twenty-five" — an uncited number where the reader most needed a defensible one | The number is spelled out, so no digit-based check sees it. A check broad enough to catch it would fire on "five stations" and "two ovens" on every page, and be muted within a week. |
| "ReAct's **most frequent** characteristic failure" — the paper says *one frequent pattern* | The quoted string was verbatim. The *characterisation* around it was wrong, and no script can read the source. |
| A diagram arrow asserting the opposite of its own caption | Both the SVG and the caption were individually valid. Only their *disagreement* was wrong. |

A green gate means you have not broken the contract's mechanics. It says nothing about
whether the day is true. Do not treat PASS as done.
