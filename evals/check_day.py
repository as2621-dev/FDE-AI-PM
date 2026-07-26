#!/usr/bin/env python3
"""Deterministic quality gate for one day of the FDE course.

Everything a machine can decide, a machine decides here. Judgment calls
(is it accurate? is it readable? would it survive an interviewer?) belong to the
reviewer agents, not to this script.

Usage:
    python3 evals/check_day.py course/day-01-agent-loop/README.md
    python3 evals/check_day.py course/day-01-agent-loop/README.md --offline
    python3 evals/check_day.py course/day-*/README.md --json

Exit codes:
    0  all hard checks passed (warnings may still be present)
    1  at least one hard check failed
    2  bad invocation / file unreadable
"""

from __future__ import annotations

import argparse
import glob
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

# ── Contract constants (mirror course/_meta/STYLE_GUIDE.md) ────────────────────

REQUIRED_SECTIONS: list[str] = [
    "## 1. Why this day exists",
    "## 2. Explain it like I'm five",
    "## 3. The concept, properly",
    "## 4. What the resources say",
    "## 5. Suggested exercise (optional)",
    "## 6. Where it breaks",
    "## 7. Watch this",
    "## 8. Say this in an interview",
    "## 9. Vocabulary",
    "## 10. Test yourself",
]

REQUIRED_TIERS: list[str] = [
    "### Tier 1 — The shape of it",
    "### Tier 2 — How it actually works",
    "### Tier 3 — What an interviewer digs into",
]

REQUIRED_FRONTMATTER_KEYS: set[str] = {
    "day",
    "slug",
    "title",
    "week",
    "week_title",
    "one_liner",
    "reading_minutes",
}

WORD_COUNT_MIN = 6_500

# Two ceilings, on purpose. WORD_COUNT_MAX is the hard fail — raised to 10,000 by
# the user so a from-zero day that pays a real vocabulary bill isn't forced to cut
# teaching. WORD_COUNT_TARGET_MAX only warns: 45–60 minutes is the promise made in
# course/README.md, and at ~150 wpm that runs out around 9,000. A day between the
# two is allowed but has to be worth the reader's extra ten minutes, so it says so
# out loud rather than drifting there silently across 30 days.
WORD_COUNT_MAX = 10_000
WORD_COUNT_TARGET_MAX = 9_000
QA_MIN = 8
QA_MAX = 12
MAX_VIDEOS = 2
ANSWER_MIN_WORDS = 15

# A timestamp is only allowed if its line names where it came from.
TIMESTAMP_EVIDENCE = re.compile(
    r"chapter marker|from transcript|from the transcript|from description|"
    r"from the description|published chapters",
    re.IGNORECASE,
)
TIMESTAMP_PATTERN = re.compile(r"`(\d{1,2}:\d{2}(?::\d{2})?)`")

BANNED_PHRASES: list[str] = [
    "simply ",
    "obviously",
    "of course,",
    "as you know",
    "let's dive in",
    "dive into",
    "great question",
    "it's important to note",
    "in this section we will",
    "congratulations",
]

LINK_PATTERN = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
CODE_FENCE_PATTERN = re.compile(r"```.*?```", re.DOTALL)
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")
FIGURE_PATTERN = re.compile(r"[%$]\s?\d|(?<![\w.])\d+(?:\.\d+)?\s?%")

# A figure worked out in front of the reader needs no external citation — the
# definition-of-done says so. Detected by the arithmetic resolving in the same
# paragraph: an operator, or the spelled-out form. Deliberately not broadened to
# plain integers; see check_unsourced_figures for why a wider trigger self-defeats.
ARITHMETIC_PATTERN = re.compile(
    r"[=÷×−]|\s-\s\d|\bdivided by\b|\bminus\b|\bmultiplied by\b|\btimes\b",
    re.IGNORECASE,
)


@dataclass
class Report:
    """Accumulated findings for one file."""

    path: str
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict[str, object] = field(default_factory=dict)

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    @property
    def passed(self) -> bool:
        return not self.failures


# ── Parsing helpers ────────────────────────────────────────────────────────────


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter dict, body). Tolerates a missing frontmatter block.

    Deliberately hand-rolled rather than pulling in PyYAML — the frontmatter is a
    flat key/value block and a dependency here would mean every reviewer agent
    needs a pip install before it can run the gate.
    """
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    front: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            front[key.strip()] = value.strip()
    return front, parts[2]


def prose_words(body: str) -> int:
    """Count words a human actually reads: no code blocks, no HTML tags."""
    stripped = CODE_FENCE_PATTERN.sub(" ", body)
    stripped = HTML_TAG_PATTERN.sub(" ", stripped)
    return len(stripped.split())


def section_body(body: str, heading: str) -> str:
    """Text between `heading` and the next `## ` heading."""
    start = body.find(heading)
    if start == -1:
        return ""
    after = body[start + len(heading) :]
    match = re.search(r"^## ", after, re.MULTILINE)
    return after[: match.start()] if match else after


# ── Individual checks ──────────────────────────────────────────────────────────


def check_frontmatter(front: dict[str, str], report: Report) -> None:
    if not front:
        report.fail("no frontmatter block found (file must open with `---`)")
        return
    missing = REQUIRED_FRONTMATTER_KEYS - set(front)
    if missing:
        report.fail(f"frontmatter missing keys: {', '.join(sorted(missing))}")
    for numeric_key in ("day", "week", "reading_minutes"):
        value = front.get(numeric_key)
        if value is not None and not value.isdigit():
            report.fail(f"frontmatter `{numeric_key}` must be a number, got {value!r}")


def check_sections(body: str, report: Report) -> None:
    positions: list[int] = []
    for heading in REQUIRED_SECTIONS:
        index = body.find(heading)
        if index == -1:
            report.fail(f"missing required section heading: {heading!r}")
        else:
            positions.append(index)
    if len(positions) == len(REQUIRED_SECTIONS) and positions != sorted(positions):
        report.fail("required sections are present but out of order")

    for tier in REQUIRED_TIERS:
        if tier not in body:
            report.fail(f"missing depth tier heading: {tier!r}")

    if "> **The interview question this day answers:**" not in body:
        report.fail("missing the blockquote stating the interview question")


def check_length(body: str, report: Report) -> None:
    count = prose_words(body)
    report.stats["prose_words"] = count
    report.stats["est_reading_minutes"] = round(count / 150)
    if count < WORD_COUNT_MIN:
        report.fail(f"too short: {count} prose words (minimum {WORD_COUNT_MIN})")
    elif count > WORD_COUNT_MAX:
        report.fail(f"too long: {count} prose words (maximum {WORD_COUNT_MAX})")
    elif count > WORD_COUNT_TARGET_MAX:
        report.warn(
            f"{count} prose words is over the {WORD_COUNT_TARGET_MAX}-word target "
            f"(~{round(count / 150)} min, above the 45–60 min the course promises) — "
            f"allowed up to {WORD_COUNT_MAX}, but check the overflow is teaching and "
            f"not restatement"
        )


def check_qa(body: str, report: Report) -> None:
    section = section_body(body, "## 10. Test yourself")
    if not section.strip():
        report.fail("section 10 (Test yourself) is empty")
        return

    blocks = re.findall(r"<details>(.*?)</details>", section, re.DOTALL)
    report.stats["qa_count"] = len(blocks)

    if len(blocks) < QA_MIN:
        report.fail(f"only {len(blocks)} Q&A blocks (minimum {QA_MIN})")
    if len(blocks) > QA_MAX:
        report.fail(f"{len(blocks)} Q&A blocks (maximum {QA_MAX})")

    numbers_with_evidence = 0
    for position, block in enumerate(blocks, start=1):
        if "<summary>" not in block:
            report.fail(f"Q&A block {position} has no <summary>")
            continue
        answer = block.split("</summary>", 1)[-1]
        answer_words = len(HTML_TAG_PATTERN.sub(" ", answer).split())
        if answer_words < ANSWER_MIN_WORDS:
            report.fail(
                f"Q&A block {position} answer is {answer_words} words "
                f"(minimum {ANSWER_MIN_WORDS}) — a stub answer teaches nothing"
            )
        # GitHub only renders the answer as markdown with a blank line after
        # </summary>. Without it the dropdown opens onto a wall of raw text.
        if not re.match(r"\s*\n\s*\n", answer):
            report.fail(
                f"Q&A block {position} needs a blank line after </summary> "
                "or GitHub will not render the answer"
            )
        if re.search(r"\d", answer) or '"' in answer:
            numbers_with_evidence += 1

    if blocks and numbers_with_evidence < 2:
        report.fail(
            "at least 2 answers must contain a number, name, or verbatim quote "
            f"(found {numbers_with_evidence})"
        )


def check_videos(body: str, report: Report) -> None:
    section = section_body(body, "## 7. Watch this")
    if not section.strip():
        report.fail("section 7 (Watch this) is empty")
        return

    video_headings = re.findall(r"^### \d+\.", section, re.MULTILINE)
    report.stats["video_count"] = len(video_headings)
    if len(video_headings) > MAX_VIDEOS:
        report.fail(f"{len(video_headings)} videos listed (maximum {MAX_VIDEOS})")
    if not video_headings:
        report.fail("section 7 lists no videos (use `### 1. Title` format)")


def check_timestamps(body: str, report: Report) -> None:
    """The anti-fabrication gate: a timestamp must say where it came from.

    Scans the WHOLE document, not just §7. Day 1 cited a transcript timestamp
    inside §3 Tier 2 that a §7-only scan never looked at — an unsourced
    timestamp anywhere is the failure this gate exists to catch.
    """
    stamped_lines = 0
    for line in body.splitlines():
        stamps = TIMESTAMP_PATTERN.findall(line)
        if not stamps:
            continue
        stamped_lines += 1
        if not TIMESTAMP_EVIDENCE.search(line):
            report.fail(
                f"timestamp {stamps[0]!r} has no stated source — cite "
                "'(chapter marker)', '(from transcript)', or '(from description)', "
                f"or drop the timestamp. Line: {line.strip()[:90]!r}"
            )
    report.stats["timestamp_lines"] = stamped_lines


def check_vocabulary(body: str, report: Report) -> None:
    section = section_body(body, "## 9. Vocabulary")
    rows = [
        line
        for line in section.splitlines()
        if line.strip().startswith("|") and "---" not in line
    ]
    # First row is the header.
    term_count = max(0, len(rows) - 1)
    report.stats["vocab_terms"] = term_count
    if term_count < 3:
        report.fail(f"vocabulary table has {term_count} terms (minimum 3)")


def check_banned_phrases(body: str, report: Report) -> None:
    lowered = body.lower()
    hits = [phrase for phrase in BANNED_PHRASES if phrase in lowered]
    if hits:
        report.warn(f"banned/condescending phrasing present: {', '.join(hits)}")


def check_unsourced_figures(body: str, report: Report) -> None:
    """Heuristic: a paragraph quoting a figure should cite something.

    A warning, not a failure — the reviewer agent makes the real call. But it
    puts the burden of proof on the numbers, which is where it belongs.
    """
    # Strip tags as well as code: `width="100%"` on an <img> is not a claim.
    prose = HTML_TAG_PATTERN.sub(" ", CODE_FENCE_PATTERN.sub(" ", body))
    offenders: list[str] = []
    for paragraph in re.split(r"\n\s*\n", prose):
        # Drop heading, table and quote lines rather than skipping the whole
        # paragraph — a figure on a prose line next to a heading still needs a source.
        lines = [
            line
            for line in paragraph.splitlines()
            if not line.lstrip().startswith(("|", ">", "#"))
        ]
        candidate = "\n".join(lines)
        if not candidate.strip() or not FIGURE_PATTERN.search(candidate):
            continue
        # A figure the paragraph derives in front of the reader is the one thing
        # the definition-of-done explicitly blesses, so it must not warn. Without
        # this the check is *guaranteed* to fire on the highest-value paragraph of
        # every Rule B day — which is precisely how a warning becomes wallpaper.
        if ARITHMETIC_PATTERN.search(candidate):
            continue
        has_support = LINK_PATTERN.search(candidate) or "⚠️" in candidate
        if not has_support:
            offenders.extend(FIGURE_PATTERN.findall(candidate) or [candidate])
    if offenders:
        # Count distinct figures, not paragraphs. The style guide asks for a number
        # to be derived once and reused in the interview answer and the self-test,
        # so counting paragraphs scores a well-structured day ~3x worse than a badly
        # structured one with identical sourcing.
        distinct = sorted({" ".join(str(o).split()) for o in offenders})
        report.stats["unsourced_figures"] = len(distinct)
        report.warn(
            f"{len(distinct)} distinct figure(s) cited with no link and no "
            f"⚠️ Unverified marker, and not derived in place. First: {distinct[0]!r}"
        )


def check_diagrams(md_path: Path, body: str, report: Report) -> None:
    referenced = re.findall(r'src="(diagrams/[^"]+\.svg)"', body)
    report.stats["diagrams_referenced"] = len(referenced)
    if not referenced:
        report.fail("no diagram referenced (need 1–2 inline SVGs)")
    if len(referenced) > 2:
        report.fail(f"{len(referenced)} diagrams referenced (maximum 2)")

    for relative in referenced:
        svg_path = md_path.parent / relative
        if not svg_path.exists():
            report.fail(f"diagram referenced but missing on disk: {relative}")
            continue
        svg = svg_path.read_text(encoding="utf-8")

        # Presentation attributes only — a CSS class silently loses all styling
        # when the same .svg is used standalone in a GitHub README.
        if "<style" in svg:
            report.fail(f"{relative}: contains a <style> block — use presentation attributes")
        if re.search(r'\sclass="', svg):
            report.fail(f"{relative}: uses class= — use presentation attributes")

        external = [
            url
            for url in re.findall(r'(?:href|src)="(https?://[^"]+)"', svg)
            if "www.w3.org" not in url
        ]
        if external:
            report.fail(f"{relative}: references external host(s) {external} — CSP will block these")

        if 'role="img"' not in svg:
            report.fail(f"{relative}: missing role=\"img\"")
        if "<title" not in svg or "<desc" not in svg:
            report.fail(f"{relative}: needs both a <title> and a <desc> child")
        if "viewBox" not in svg:
            report.fail(f"{relative}: missing viewBox — it will not scale")


def check_links(body: str, report: Report, offline: bool) -> None:
    urls = sorted(set(LINK_PATTERN.findall(body)))
    report.stats["link_count"] = len(urls)
    if offline:
        report.warn(f"--offline: skipped reachability check on {len(urls)} link(s)")
        return

    dead: list[str] = []
    for url in urls:
        request = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "Mozilla/5.0 (compatible; fde-course-linkcheck)"},
        )
        try:
            with urllib.request.urlopen(request, timeout=12) as response:
                if response.status >= 400:
                    dead.append(f"{url} → HTTP {response.status}")
        except urllib.error.HTTPError as exc:
            # Some hosts reject HEAD but serve GET fine; retry before condemning.
            # 5xx is retried for a different reason: it is by definition transient
            # and says nothing about the URL. GitHub intermittently 502s on /blob/
            # pages for large markdown files, which failed a Day 5 gate run whose
            # link was demonstrably alive on the next attempt. Condemning a live
            # source teaches writers to "fix" working citations.
            if exc.code in (403, 405, 501) or 500 <= exc.code < 600:
                try:
                    get_request = urllib.request.Request(
                        url,
                        headers={"User-Agent": "Mozilla/5.0 (compatible; fde-course-linkcheck)"},
                    )
                    with urllib.request.urlopen(get_request, timeout=12) as response:
                        if response.status >= 400:
                            dead.append(f"{url} → HTTP {response.status}")
                except Exception as inner:  # noqa: BLE001 - report, don't crash the gate
                    report.warn(f"could not verify {url} ({type(inner).__name__})")
            else:
                dead.append(f"{url} → HTTP {exc.code}")
        except Exception as exc:  # noqa: BLE001 - a flaky host is a warning, not a failure
            report.warn(f"could not verify {url} ({type(exc).__name__})")

    if dead:
        for entry in dead:
            report.fail(f"dead link: {entry}")


# ── Orchestration ──────────────────────────────────────────────────────────────


def check_file(path_str: str, offline: bool) -> Report:
    md_path = Path(path_str)
    report = Report(path=str(md_path))
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError as exc:
        report.fail(f"cannot read file: {exc}")
        return report

    front, body = split_frontmatter(text)
    check_frontmatter(front, report)
    check_sections(body, report)
    check_length(body, report)
    check_qa(body, report)
    check_videos(body, report)
    check_timestamps(body, report)
    check_vocabulary(body, report)
    check_banned_phrases(body, report)
    check_unsourced_figures(body, report)
    check_diagrams(md_path, body, report)
    check_links(body, report, offline)
    return report


def print_human(report: Report) -> None:
    status = "PASS" if report.passed else "FAIL"
    marker = "✓" if report.passed else "✗"
    print(f"\n{marker} {status}  {report.path}")

    if report.stats:
        rendered = "  ".join(f"{key}={value}" for key, value in sorted(report.stats.items()))
        print(f"  stats: {rendered}")

    for failure in report.failures:
        print(f"  ✗ FAIL  {failure}")
    for warning in report.warnings:
        print(f"  ! warn  {warning}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic quality gate for an FDE course day."
    )
    parser.add_argument("paths", nargs="+", help="day README.md path(s); globs allowed")
    parser.add_argument(
        "--offline", action="store_true", help="skip network link reachability checks"
    )
    parser.add_argument("--json", action="store_true", help="emit structured JSON instead")
    args = parser.parse_args()

    expanded: list[str] = []
    for pattern in args.paths:
        matches = sorted(glob.glob(pattern))
        expanded.extend(matches or [pattern])
    if not expanded:
        print("no files matched", file=sys.stderr)
        return 2

    reports = [check_file(path, args.offline) for path in expanded]

    if args.json:
        print(
            json.dumps(
                {
                    "event": "check_day_completed",
                    "files_checked": len(reports),
                    "files_failed": sum(1 for r in reports if not r.passed),
                    "results": [
                        {
                            "path": r.path,
                            "passed": r.passed,
                            "failures": r.failures,
                            "warnings": r.warnings,
                            "stats": r.stats,
                        }
                        for r in reports
                    ],
                    "fix_suggestion": "See course/_meta/STYLE_GUIDE.md for the contract.",
                },
                indent=2,
            )
        )
    else:
        for report in reports:
            print_human(report)
        failed = sum(1 for r in reports if not r.passed)
        print(f"\n{len(reports) - failed}/{len(reports)} passed.")
        if failed:
            print("Contract: course/_meta/STYLE_GUIDE.md")

    return 1 if any(not r.passed for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
