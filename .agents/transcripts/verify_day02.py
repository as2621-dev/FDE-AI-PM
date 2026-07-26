#!/usr/bin/env python3
"""Re-check every transcript-sourced timestamp cited in Day 2 against the caption file.

Same rule as verify.py (see README.md): a citation's timestamp is the start of the
first cue in which the cited words *begin*. Rolling auto-captions repeat the previous
line plus new words, so we match on a leading fragment rather than a whole phrase.

Day 2 cites three passages from the MCP workshop, all paraphrased rather than quoted
because the ASR garbles words inside them ("promps", "control controled").

Usage:  python3 .agents/transcripts/verify_day02.py
Exit:   0 = every citation matches, 1 = at least one does not
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

VTT = Path(__file__).parent / "kQmXtrmQ5Zg.en.auto.vtt"

# (timestamp cited in Day 2, leading fragment of the cited passage)
CITATIONS = [
    ("11:23", "resources are data exposed"),
    ("12:59", "user controlled"),
    ("14:58", "model controlled"),
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
