#!/usr/bin/env python3
"""Generate the GitHub issue bodies for all 30 course days, from FDE_Report.

Reads the per-day resource tables straight out of FDE_Report and the boundary
information out of course/_meta/DAY_MAP.md, so the issues can never drift from
the source material. Writes one markdown file per issue to a staging directory;
a separate `gh issue create` loop consumes them.

Usage:
    python3 evals/make_issues.py --out .agents/issue-bodies
    python3 evals/make_issues.py --out .agents/issue-bodies --print 1
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = REPO_ROOT / "FDE_Report"
MANIFEST_PATH = REPO_ROOT / "course" / "_meta" / "days.json"
DAY_MAP_PATH = REPO_ROOT / "course" / "_meta" / "DAY_MAP.md"

CHECKLIST = """\
### Definition of done

- [ ] All 10 sections present, headings **verbatim** per the style guide
- [ ] 6,500–9,000 prose words (10,000 hard ceiling; expect to land in the 9,000+ band and justify it)
- [ ] `reading_minutes` equals `round(prose_words / 150)` — set it **after** the last cut
- [ ] Frontmatter complete (`day`, `slug`, `title`, `week`, `week_title`, `one_liner`, `reading_minutes`)
- [ ] §3 has all three depth tiers (Tier 1 / Tier 2 / Tier 3)
- [ ] Every resource in the table above has a §4 digest block
- [ ] 8–12 Q&A in `<details>` blocks, blank line after `</summary>`
- [ ] 1–2 self-contained SVG diagrams, presentation attributes only, captioned
- [ ] ≤2 videos, both verified to exist, **zero unsourced timestamps**
- [ ] Every non-obvious claim sourced, or marked `⚠️ Unverified`
- [ ] §9 vocabulary table filled and merged into `course/GLOSSARY.md`
- [ ] No term used before it is defined
- [ ] Gate passes: `python3 evals/check_day.py course/day-NN-slug/README.md`
- [ ] Reviewer 1 (accuracy + PM-readability) passed
- [ ] Reviewer 2 (adversarial interviewer) could not trivially fail the reader

### Reference

- Authoring contract: `course/_meta/STYLE_GUIDE.md` — **read fully before writing**
- Boundaries: `course/_meta/DAY_MAP.md`
- Diagram system: `.tools/diagram-design/skills/diagram-design/`
- Rebuild the page: `~/.venvs/fde-course/bin/python course/build.py`
"""


def extract_report_section(report: str, day_number: int) -> str:
    """Pull the `### Day N — ...` block out of FDE_Report.

    Days 7, 14, 16, 21, 23, 25, 26, 28 and 30 have prose instead of a resource
    table; this returns whatever is there rather than assuming a table exists.
    """
    pattern = rf"^### Day {day_number} — .*?$"
    match = re.search(pattern, report, re.MULTILINE)
    if not match:
        return ""
    start = match.start()
    following = re.search(r"^(### Day \d+ — |## )", report[match.end() :], re.MULTILINE)
    end = match.end() + following.start() if following else len(report)
    # The report puts a `---` rule before each week heading; don't inherit it.
    return re.sub(r"\n-{3,}\s*$", "", report[start:end].strip()).strip()


def extract_day_map_row(day_map: str, day_number: int) -> str:
    """Pull this day's row out of the boundary table."""
    for line in day_map.splitlines():
        if line.startswith(f"| {day_number} |"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) < 6:
                return ""
            owns, avoid, gap = cells[3], cells[4], cells[5]
            block = [f"**Owns:** {owns}", "", f"**Must NOT cover:** {avoid}"]
            if gap and gap != "—":
                block += ["", f"**Gap fill (required, from the report's own gap table):** {gap}"]
            return "\n".join(block)
    return ""


def build_day_issue(day: dict, week: dict, report: str, day_map: str) -> tuple[str, str]:
    number = day["day"]
    slug = day["slug"]
    directory = f"course/day-{number:02d}-{slug}"
    title = f"Day {number:02d} — {day['title']}"

    report_section = extract_report_section(report, number) or "_No section found in FDE_Report._"
    boundary = extract_day_map_row(day_map, number) or "_No boundary row found._"

    body = f"""**Week {week["week"]} · {week["title"]}**
> {week["goal"]}

_{day["one_liner"]}_

Write `{directory}/README.md` — a 60–70 minute teaching document that takes a
non-technical PM (mechanical engineer, zero software background) from zero to
being able to defend this topic in an FDE interview.

---

## Boundary

{boundary}

---

## Source material (verbatim from `FDE_Report`)

{report_section}

---

{CHECKLIST}"""

    return title, body


def build_epic_issue(manifest: dict) -> tuple[str, str]:
    lines = [
        "Tracking issue for the 30-day FDE course build.",
        "",
        "**Reader:** product manager, mechanical engineer by training, no software",
        "background. Reading-only (no hands-on coding). Targeting **AI product startup**",
        "FDE roles (Sierra, Harvey, Decagon, Glean), frontier labs as a stretch.",
        "",
        "**Deliverable:** 30 markdown days in `course/`, assembled by `course/build.py`",
        "into one self-contained HTML page — day list in a left sidebar, content on the",
        "right — published as a private artifact.",
        "",
        "**Quality gates per day:** `evals/check_day.py` (deterministic) + two reviewer",
        "agents (accuracy/readability, and an adversarial interviewer).",
        "",
        "## Progress",
        "",
    ]
    for week in manifest["weeks"]:
        lines.append(f"### Week {week['week']} · Days {week['days']} — {week['title']}")
        lines.append(f"_{week['goal']}_")
        lines.append("")
        for day in manifest["days"]:
            if day["week"] == week["week"]:
                lines.append(f"- [ ] Day {day['day']:02d} — {day['title']}")
        lines.append("")
    lines += [
        "## Phase 0 (done before any day)",
        "",
        "- [x] `course/_meta/STYLE_GUIDE.md` — the authoring contract",
        "- [x] `course/_meta/DAY_MAP.md` — boundaries + gap-fill assignments",
        "- [x] `course/_meta/days.json` — 30-day manifest",
        "- [x] `course/GLOSSARY.md` — seeded",
        "- [x] `evals/check_day.py` — deterministic gate",
        "- [x] `course/build.py` — single-page assembler",
        "- [x] `.tools/diagram-design` — diagram system vendored (gitignored)",
    ]
    return "Epic — FDE 30-day course", "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate GitHub issue bodies.")
    parser.add_argument("--out", required=True, help="staging directory for issue bodies")
    parser.add_argument("--print", dest="print_day", type=int, help="print one day and exit")
    args = parser.parse_args()

    report = REPORT_PATH.read_text(encoding="utf-8")
    day_map = DAY_MAP_PATH.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    weeks = {week["week"]: week for week in manifest["weeks"]}

    if args.print_day:
        day = next(d for d in manifest["days"] if d["day"] == args.print_day)
        title, body = build_day_issue(day, weeks[day["week"]], report, day_map)
        print(f"TITLE: {title}\n\n{body}")
        return

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[dict[str, str]] = []

    epic_title, epic_body = build_epic_issue(manifest)
    epic_path = out_dir / "epic.md"
    epic_path.write_text(epic_body, encoding="utf-8")
    written.append({"file": str(epic_path), "title": epic_title, "labels": "epic"})

    for day in manifest["days"]:
        title, body = build_day_issue(day, weeks[day["week"]], report, day_map)
        path = out_dir / f"day-{day['day']:02d}.md"
        path.write_text(body, encoding="utf-8")
        written.append(
            {
                "file": str(path),
                "title": title,
                "labels": f"day,week-{day['week']},status:backlog",
            }
        )

    index_path = out_dir / "index.json"
    index_path.write_text(json.dumps(written, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "event": "issue_bodies_generated",
                "count": len(written),
                "index": str(index_path),
            }
        )
    )


if __name__ == "__main__":
    main()
