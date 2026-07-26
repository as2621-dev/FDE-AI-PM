# Caption transcripts used as timestamp evidence

Any day that cites a video timestamp *(from transcript)* keeps the caption file it
read here, so a reviewer can re-check the citation without re-fetching.

| File | Video | Retrieved | Kind |
|---|---|---|---|
| `D7_ipDqhtwk.en.auto.vtt` | Barry Zhang, "How We Build Effective Agents" (AI Engineer) | 2026-07-25 | YouTube **auto-generated** captions (ASR) |
| `kQmXtrmQ5Zg.en.auto.vtt` | Mahesh Murag, "Building Agents with Model Context Protocol" (AI Engineer) | 2026-07-26 | YouTube **auto-generated** captions (ASR) |

## Re-fetch command

```sh
yt-dlp --skip-download --write-auto-subs --sub-lang "en.*" --sub-format vtt \
  -o "D7_ipDqhtwk" "https://www.youtube.com/watch?v=D7_ipDqhtwk"
```

## Published chapter markers

Chapter titles are not in the caption file — they come from the video metadata, so
re-derive them with:

```sh
yt-dlp --skip-download --print "%(chapters)s" "https://www.youtube.com/watch?v=<VIDEO_ID>"
```

`kQmXtrmQ5Zg` (1:44:11, AI Engineer, published 2025-03-01) has four: `0:00` What is
MCP?, `9:39` Building with MCP, `26:25` MCP & Agents, `1:13:15` What's next for MCP?.
Day 2 cites all four *(chapter marker)*, which needs no ASR hedge.

A bare `GET` against YouTube's `timedtext` API returns an **empty body** for this
video — the caption URL is signed and only resolvable from the watch page's player
response, which is what `yt-dlp` does for you. An empty timedtext response is not
evidence that captions don't exist.

## Reading a rolling-caption VTT

Auto-generated captions roll: consecutive cues repeat the previous line plus new
words, so the same sentence appears in several overlapping cues, and a long quote
is split across two or three of them. The rule this project uses: a quote's
timestamp is the start of the **first cue in which the quoted words begin** — not
the later cue where they finish. That lands a viewer a second or two *before* the
words rather than mid-sentence, which is what you want when seeking.

One script per day, so a citation stays checkable without re-reading the day:

```sh
python3 .agents/transcripts/verify.py         # Day 1 citations
python3 .agents/transcripts/verify_day02.py   # Day 2 citations
```

## These are ASR, not a certified transcript

Automatic speech recognition misheard several words in this file — at `09:32` it
renders "the tool execution is happening" as "the two execution is happening", and
it writes "Claude" as "cloud" throughout. Neither error falls inside a passage
quoted in Day 1, but treat any quote sourced here as close rather than certified,
and say so wherever it is quoted.
