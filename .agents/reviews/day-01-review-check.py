#!/usr/bin/env python3
"""Assert every reviewer-requested fix for Day 1 is present on disk.

Written because a review round was adjudicated twice over messages while the
reviewer was reading a stale copy of the file. Run this instead of grepping by
hand — it fails loudly and names the item.

Usage:  python3 .agents/reviews/day-01-review-check.py
Exit:   0 = every item present, 1 = at least one regressed
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DAY = ROOT / "course/day-01-agent-loop/README.md"
LOOP = ROOT / "course/day-01-agent-loop/diagrams/agent-loop.svg"
FLOW = ROOT / "course/day-01-agent-loop/diagrams/workflow-vs-agent.svg"

# (label, must_be_present, must_be_absent)
PROSE: list[tuple[str, str | None, str | None]] = [
    ("B1 repetition is 'one frequent error pattern'",
     "one frequent error pattern specific to ReAct", "most frequent characteristic"),
    ("B1 47% noted as subsuming repetition", "failing to recover from repetitive steps", None),
    ("B1 warns against inventing a repetition %", "you have invented it", None),
    ("B2 essay credited for the idea", "Put yourself in the model's shoes", "isn't in the essay"),
    ("B2 'three core ideas from the blog post' cited", "three core ideas from the blog post", None),
    ("B3 no self-contradicting 'did not win'",
     "mixed, not the sweep its reputation implies", "did not win"),
    ("B3 CoT-SC 33.4 as the tougher comparison",
     "33.4 for chain-of-thought with self-consistency", None),
    ("B3 Fever framed against all single-method baselines",
     "beat every single-method prompting baseline", None),
    ("smolagents proposes a spectrum (not 'rejects')",
     "proposes a spectrum instead", "rejects the binary"),
    ("smolagents docs don't cite Anthropic", "It doesn't mention Anthropic", None),
    ("ReAct section cite is 'stop before §4'", "then stop before §4", "Sections 4 and 5"),
    ("similar-entities fallback, not a disambiguation page",
     "similar entity names the API falls back to", "disambiguation"),
    ("smolagents quote un-truncated", "own tools / start other agents", None),
    ("Vas quote marked unverified", "⚠️ **Unverified:**", None),
    ("tagged taxonomy assigned to Day 16", "the tagged taxonomy gets Day 16", None),
    ("three-vs-four criteria reconciled", "his fourth, de-risking the capabilities", None),
    ("cap range no longer uncited", "ReAct's authors used 7 and 5", "between five and twenty-five"),
    ("cap method: floor, multiply, then distribution", "runs that *succeeded*", None),
    ("cap as router (back-off trigger)", "The cap can be a router, not just a wall", None),
    ("quote dated February 2025", "He said that in **February 2025**", None),
    ("economics collision present", "about 26 cents", None),
    ("cost shape named quadratic", "n·B + D·n(n−1)/2", None),
    ("no-effectors reframe", "**the model has no effectors.**", "the model never does anything"),
    ("tool-failure row in §6", "| **The action itself failed** |", None),
    ("errors summarised, not stack traces", "Not a raw stack trace", None),
    ("cap counts passes, not retries", "The cap counts passes of the loop", None),
    ("no 'say this out loud' instruction", None, "out loud"),
    ("no recall framing", None, "reel these off"),
]

# Terms defined inline in the day that must also carry a §9 row (Rule A).
TERMS = ["tool", "API", "function", "transcript", "benchmark",
         "chain-of-thought", "hallucination", "context window"]

# The input/output token split belongs inside the Token row, not as its own term.
TOKEN_ROW_MUST_MENTION = ["**input**", "**output**"]


def main() -> int:
    day = DAY.read_text(encoding="utf-8")
    loop = LOOP.read_text(encoding="utf-8")
    flow = FLOW.read_text(encoding="utf-8")
    failures: list[str] = []

    for label, present, absent in PROSE:
        if present and present not in day:
            failures.append(f"{label}: expected text MISSING")
        if absent and absent in day:
            failures.append(f"{label}: forbidden text STILL PRESENT")

    # B7 — the Prompt spoke must point AT the Prompt box (a read), not at the hub.
    spokes = [m for m in re.finditer(
        r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*'
        r'stroke-dasharray="5,4"[^>]*marker-end', loop)]
    body = [s for s in spokes if float(s.group(2)) < 600]  # exclude legend glyphs
    if len(body) != 3:
        failures.append(f"B7 diagram: expected 3 spokes, found {len(body)}")
    else:
        prompt_spoke = min(body, key=lambda m: min(float(m.group(2)), float(m.group(4))))
        if not float(prompt_spoke.group(4)) < float(prompt_spoke.group(2)):
            failures.append("B7 diagram: Prompt spoke arrowhead is at the hub, not the station")
    for label, text in [("comment", "direction = read vs append"),
                        ("desc", "Prompt reads the whole transcript back"),
                        ("legend", "reads it back")]:
        if text not in loop:
            failures.append(f"B7 diagram: {label} not updated")
    for name, svg in (("agent-loop", loop), ("workflow-vs-agent", flow)):
        if "transparent" in svg:
            failures.append(f'B7 diagram: {name}.svg still uses fill="transparent"')

    # Rule A — every term defined inline must also have a §9 row.
    vocab = day.split("## 9. Vocabulary", 1)[1].split("## 10.", 1)[0].lower()
    for term in TERMS:
        if f"**{term.lower()}" not in vocab:
            failures.append(f"Rule A: '{term}' missing from the §9 table")
    token_row = next((l for l in vocab.splitlines() if l.startswith("| **token**")), "")
    for frag in TOKEN_ROW_MUST_MENTION:
        if frag.lower() not in token_row:
            failures.append(f"Rule A: Token row does not name {frag}")

    for label, present, _ in PROSE:
        print(f"  {'ok  ' if not any(label in f for f in failures) else 'FAIL'}  {label}")
    print(f"\n{len(PROSE) + 5 - len(failures)} checks passed, {len(failures)} failed")
    for f in failures:
        print(f"  ✗ {f}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
