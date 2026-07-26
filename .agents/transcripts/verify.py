#!/usr/bin/env python3
"""Re-check every transcript-sourced timestamp cited in Day 1 against the caption file.

Rule (see README.md): a quote's timestamp is the start of the first cue in which
the quoted words *begin*. Rolling auto-captions split a long quote across cues, so
we match on a leading fragment, not the whole phrase.

Usage:  python3 .agents/transcripts/verify.py
Exit:   0 = every citation matches, 1 = at least one does not
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

VTT = Path(__file__).parent / "D7_ipDqhtwk.en.auto.vtt"

# (timestamp cited in the README, leading fragment of the cited passage)
CITATIONS = [
    ("00:44", "three core ideas from the blog post"),
    ("00:52", "First, don't build agents for"),
    ("02:59", "checklist"),
    ("03:27", "If your budget per"),
    ("05:51", "They're models using tools in a"),
    ("08:06", "is to think like your agents"),
    ("09:34", "closing our"),
]


def cues(path: Path) -> list[tuple[str, str]]:
    """Return [(start "MM:SS", plain cue text)] from a WebVTT file."""
    out = []
    for block in path.read_text(encoding="utf-8").split("\n\n"):
        match = re.search(r"\d\d:(\d\d:\d\d)\.\d+ --> ", block)
        if not match:
            continue
        text = " ".join(
            re.sub(r"<[^>]+>", "", line).strip()
            for line in block.splitlines()[1:]
            if line.strip()
        )
        if text:
            out.append((match.group(1), " ".join(text.split())))
    return out


def main() -> int:
    if not VTT.exists():
        print(f"missing caption file: {VTT}", file=sys.stderr)
        return 1
    parsed = cues(VTT)
    print(f"{len(parsed)} cues parsed from {VTT.name}\n")
    print(f"{'CITED':7} {'ACTUAL':7} {'VERDICT':9} FRAGMENT")
    failures = 0
    for cited, fragment in CITATIONS:
        actual = next((s for s, t in parsed if fragment.lower() in t.lower()), None)
        good = actual == cited
        failures += not good
        print(f"{cited:7} {actual or '-':7} {'match' if good else 'MISMATCH':9} {fragment!r}")
    print(f"\n{len(CITATIONS) - failures}/{len(CITATIONS)} citations verified")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
