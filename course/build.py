#!/usr/bin/env python3
"""Assemble the per-day markdown READMEs into one self-contained HTML page.

Left sidebar lists all 30 days grouped by week; the right pane shows the selected
day. Everything is inlined — SVGs, CSS, JS — because the published page runs under
a strict CSP that blocks every external host.

Usage:
    ~/.venvs/fde-course/bin/python course/build.py
    ~/.venvs/fde-course/bin/python course/build.py --out course/index.html

Why the odd interpreter path: the project directory name contains a colon, and
Python refuses to create a venv inside such a path. The venv therefore lives at
~/.venvs/fde-course. See course/README.md.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

import markdown

COURSE_DIR = Path(__file__).parent
META_DIR = COURSE_DIR / "_meta"

MD_EXTENSIONS = ["tables", "fenced_code", "md_in_html", "attr_list", "sane_lists"]

# ── Page shell ─────────────────────────────────────────────────────────────────

PAGE_CSS = """
*, *::before, *::after { box-sizing: border-box; }
/* Neutrals carry a slight warm bias toward the accent, which is inherited from
   the diagram palette (#eb6c36) and baked into every SVG. --accent-text is the
   deeper variant, used wherever the accent carries small type and needs contrast. */
:root {
  --paper: #fbfaf8; --sunken: #f2efea; --ink: #1f1c18; --muted: #574f47;
  --soft: #8a8178; --rule: #e3ddd4;
  --accent: #eb6c36; --accent-text: #b8481a; --link: #2a5599;
  --serif: Charter, "Iowan Old Style", Georgia, "Times New Roman", serif;
  --sans: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, monospace;
  --sidebar-w: 302px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #191714; --sunken: #221f1b; --ink: #ece9e4; --muted: #a9a199;
    --soft: #7e766d; --rule: #322e29; --accent-text: #f0854f; --link: #8fb2e8;
  }
}
:root[data-theme="dark"] {
  --paper: #191714; --sunken: #221f1b; --ink: #ece9e4; --muted: #a9a199;
  --soft: #7e766d; --rule: #322e29; --accent-text: #f0854f; --link: #8fb2e8;
}
:root[data-theme="light"] {
  --paper: #fbfaf8; --sunken: #f2efea; --ink: #1f1c18; --muted: #574f47;
  --soft: #8a8178; --rule: #e3ddd4; --accent-text: #b8481a; --link: #2a5599;
}
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--paper); color: var(--ink);
  font-family: var(--sans); font-size: 17px; line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}
:focus-visible {
  outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 2px;
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { transition-duration: 0.01ms !important; animation-duration: 0.01ms !important; }
}
.layout { display: flex; min-height: 100vh; align-items: flex-start; }

/* ── Sidebar ── */
.sidebar {
  width: var(--sidebar-w); flex: 0 0 var(--sidebar-w);
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
  border-right: 1px solid var(--rule); background: var(--sunken);
  padding: 1.5rem 0 3rem;
}
.brand { padding: 0 1.25rem 1.25rem; border-bottom: 1px solid var(--rule); }
.brand h1 { margin: 0; font-size: 1.05rem; font-weight: 650; letter-spacing: -0.01em; }
.brand p { margin: 0.3rem 0 0; font-size: 0.78rem; color: var(--soft); line-height: 1.45; }
.progress-line { margin: 0.85rem 0 0; font: 500 0.7rem var(--mono); color: var(--soft); letter-spacing: 0.04em; }
.week-group { margin-top: 1.25rem; }
.week-label {
  padding: 0 1.25rem 0.4rem; font: 600 0.66rem var(--mono);
  letter-spacing: 0.14em; text-transform: uppercase; color: var(--soft);
}
.week-goal { padding: 0 1.25rem 0.6rem; font-size: 0.74rem; color: var(--soft); line-height: 1.45; }
.day-link {
  display: flex; gap: 0.6rem; align-items: baseline; width: 100%;
  padding: 0.5rem 1.25rem; border: 0; border-left: 2px solid transparent;
  background: none; color: var(--muted); font: inherit; font-size: 0.86rem;
  text-align: left; cursor: pointer;
}
.day-link:hover { background: color-mix(in srgb, var(--accent) 7%, transparent); color: var(--ink); }
.day-link[aria-current="true"] {
  border-left-color: var(--accent); background: color-mix(in srgb, var(--accent) 11%, transparent);
  color: var(--ink); font-weight: 600;
}
/* Day numbers are tabular so the 30-item sequence aligns down the rail. The
   numbering is earned: each day genuinely depends on the ones before it. */
.day-link .num {
  flex: 0 0 1.7rem; font: 500 0.72rem var(--mono); color: var(--soft);
  font-variant-numeric: tabular-nums;
}
.day-link[aria-current="true"] .num { color: var(--accent-text); }
.day-link.unwritten { opacity: 0.45; cursor: not-allowed; }
.day-link .tick { margin-left: auto; color: var(--accent); font-size: 0.8rem; }

/* ── Content ── */
.content { flex: 1 1 auto; min-width: 0; padding: 3rem clamp(1.25rem, 4vw, 4rem) 6rem; }
/* Reading prose is serif at a ~64ch measure; every piece of chrome and every
   heading stays sans, so structure reads as distinct from the text itself. */
.content-inner { max-width: 64ch; margin: 0 auto; font-family: var(--serif); font-size: 1.075rem; line-height: 1.7; }
.day-section[hidden] { display: none; }
.eyebrow {
  font: 600 0.68rem var(--mono); letter-spacing: 0.14em;
  text-transform: uppercase; color: var(--accent-text); margin-bottom: 0.6rem;
}
h1, h2, h3, h4, .day-footer, summary { font-family: var(--sans); }
h1 {
  font-size: clamp(1.7rem, 3vw, 2.25rem); line-height: 1.15;
  letter-spacing: -0.022em; margin: 0 0 1.25rem; text-wrap: balance;
}
h2 {
  margin: 3rem 0 1rem; padding-top: 1.25rem; border-top: 1px solid var(--rule);
  font-size: 1.3rem; letter-spacing: -0.013em; text-wrap: balance;
}
h3 { margin: 2rem 0 0.75rem; font-size: 1.05rem; letter-spacing: -0.008em; text-wrap: balance; }
h4 { margin: 1.5rem 0 0.5rem; font-size: 0.92rem; color: var(--muted); }
p, ul, ol { margin: 0 0 1.1rem; }
ul, ol { padding-left: 1.4rem; }
li { margin-bottom: 0.35rem; }
a { color: var(--link); text-decoration-thickness: 1px; text-underline-offset: 2px; }
strong { font-weight: 650; }
/* The one place the accent goes structural: the interview question each day
   answers. Everything else keeps the accent to type only. */
blockquote {
  margin: 1.5rem 0; padding: 0.85rem 1.15rem; border-left: 2px solid var(--accent);
  background: var(--sunken);
}
blockquote p:last-child { margin-bottom: 0; }
th, td, table { font-family: var(--sans); }
code {
  padding: 0.12em 0.36em; border-radius: 4px; background: var(--sunken);
  font-family: var(--mono); font-size: 0.86em;
}
pre {
  margin: 1.35rem 0; padding: 1rem 1.15rem; overflow-x: auto;
  border: 1px solid var(--rule); border-radius: 4px; background: var(--sunken);
  font-size: 0.84rem; line-height: 1.55;
}
pre code { padding: 0; background: none; }
.table-scroll { overflow-x: auto; margin: 1.35rem 0; }
table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
th, td { padding: 0.6rem 0.75rem; border-bottom: 1px solid var(--rule); text-align: left; vertical-align: top; }
th { font-weight: 650; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--soft); }
tbody tr:last-child td { border-bottom: 0; }
figure { margin: 1.75rem 0; }
figure svg { display: block; width: 100%; height: auto; border: 1px solid var(--rule); border-radius: 4px; }
figcaption { margin-top: 0.6rem; font-size: 0.82rem; color: var(--soft); font-style: italic; }
/* Self-test items read as a stack of ruled rows, not a deck of rounded cards —
   they're a sequence of questions, not independent objects. */
details {
  margin: 0; padding: 0.8rem 0.2rem; border-bottom: 1px solid var(--rule);
  background: none;
}
details:first-of-type { border-top: 1px solid var(--rule); }
details[open] { background: var(--sunken); padding-left: 0.85rem; padding-right: 0.85rem; }
summary { cursor: pointer; font-weight: 550; font-size: 0.97rem; }
summary::marker { color: var(--accent-text); }
details > *:not(summary) { margin-top: 0.7rem; }
details p:last-child { margin-bottom: 0; }
hr { margin: 2.5rem 0; border: 0; border-top: 1px solid var(--rule); }
.day-footer {
  margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid var(--rule);
  display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;
}
.btn {
  padding: 0.5rem 0.9rem; border: 1px solid var(--rule); border-radius: 4px;
  background: var(--paper); color: var(--ink); font: inherit; font-size: 0.85rem; cursor: pointer;
}
.btn:hover { border-color: var(--accent); }
.btn.primary { background: var(--accent); border-color: var(--accent); color: #1f1c18; font-weight: 600; }
.placeholder { padding: 3rem 0; color: var(--soft); }

/* ── Controls ── */
.controls { position: fixed; top: 1rem; right: 1rem; display: flex; gap: 0.5rem; z-index: 20; }
.icon-btn {
  width: 2.2rem; height: 2.2rem; display: grid; place-items: center;
  border: 1px solid var(--rule); border-radius: 4px; background: var(--paper);
  color: var(--muted); cursor: pointer; font-size: 0.95rem;
}
.icon-btn:hover { color: var(--ink); border-color: var(--accent); }
#menu-toggle { display: none; }

@media (max-width: 900px) {
  .layout { flex-direction: column; }
  .sidebar {
    position: fixed; inset: 0 auto 0 0; z-index: 30; transform: translateX(-100%);
    transition: transform 0.18s ease; box-shadow: 0 0 40px rgba(0,0,0,0.18);
  }
  .sidebar.open { transform: translateX(0); }
  .content { width: 100%; padding-top: 4.5rem; }
  #menu-toggle { display: grid; }
}
@media print {
  .sidebar, .controls, .day-footer { display: none; }
  .day-section[hidden] { display: block; }
}
"""

PAGE_JS = """
(function () {
  var KEY = 'fde-course-read';
  var THEME_KEY = 'fde-course-theme';
  var links = Array.prototype.slice.call(document.querySelectorAll('.day-link:not(.unwritten)'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('.day-section'));
  var sidebar = document.querySelector('.sidebar');

  function readSet() {
    try { return new Set(JSON.parse(localStorage.getItem(KEY) || '[]')); }
    catch (e) { return new Set(); }
  }
  function saveSet(set) {
    try { localStorage.setItem(KEY, JSON.stringify(Array.prototype.slice.call(set))); }
    catch (e) { /* private browsing — progress just won't persist */ }
  }
  function paintProgress() {
    var read = readSet();
    links.forEach(function (link) {
      var tick = link.querySelector('.tick');
      if (tick) { tick.textContent = read.has(link.dataset.day) ? '✓' : ''; }
    });
    var line = document.querySelector('.progress-line');
    if (line) { line.textContent = read.size + ' of ' + TOTAL_DAYS + ' days read'; }
    document.querySelectorAll('.mark-read').forEach(function (btn) {
      var isRead = read.has(btn.dataset.day);
      btn.textContent = isRead ? '✓ Marked as read' : 'Mark as read';
      btn.classList.toggle('primary', !isRead);
    });
  }

  function show(day, push) {
    sections.forEach(function (s) { s.hidden = s.dataset.day !== day; });
    links.forEach(function (l) { l.setAttribute('aria-current', String(l.dataset.day === day)); });
    var active = links.filter(function (l) { return l.dataset.day === day; })[0];
    if (active) { active.scrollIntoView({ block: 'nearest' }); }
    window.scrollTo(0, 0);
    sidebar.classList.remove('open');
    if (push) { history.replaceState(null, '', '#day-' + day); }
    paintProgress();
  }

  links.forEach(function (link) {
    link.addEventListener('click', function () { show(link.dataset.day, true); });
  });

  document.addEventListener('click', function (event) {
    var btn = event.target.closest('.mark-read');
    if (btn) {
      var read = readSet();
      if (read.has(btn.dataset.day)) { read.delete(btn.dataset.day); } else { read.add(btn.dataset.day); }
      saveSet(read);
      paintProgress();
      return;
    }
    var nav = event.target.closest('.go-day');
    if (nav) { show(nav.dataset.day, true); }
  });

  document.getElementById('menu-toggle').addEventListener('click', function () {
    sidebar.classList.toggle('open');
  });

  var themeBtn = document.getElementById('theme-toggle');
  function applyTheme(mode) {
    if (mode) { document.documentElement.setAttribute('data-theme', mode); }
    else { document.documentElement.removeAttribute('data-theme'); }
  }
  try { applyTheme(localStorage.getItem(THEME_KEY)); } catch (e) {}
  themeBtn.addEventListener('click', function () {
    var current = document.documentElement.getAttribute('data-theme');
    var systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var next = current ? (current === 'dark' ? 'light' : 'dark') : (systemDark ? 'light' : 'dark');
    applyTheme(next);
    try { localStorage.setItem(THEME_KEY, next); } catch (e) {}
  });

  var fromHash = (location.hash.match(/^#day-(\\d+)$/) || [])[1];
  var first = links[0] ? links[0].dataset.day : null;
  show(fromHash && sections.some(function (s) { return s.dataset.day === fromHash; }) ? fromHash : first, false);
})();
"""


# ── Markdown assembly ──────────────────────────────────────────────────────────


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (frontmatter, body). Mirrors evals/check_day.py deliberately."""
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


def inline_svgs(body_html: str, day_dir: Path) -> str:
    """Replace <img src="diagrams/x.svg"> with the SVG itself, wrapped in a figure.

    The published page has no filesystem, so a relative src would 404. Inlining
    also means the caption and diagram travel together as one figure element.
    """

    def replace(match: re.Match[str]) -> str:
        tag = match.group(0)
        src_match = re.search(r'src="([^"]+)"', tag)
        alt_match = re.search(r'alt="([^"]*)"', tag)
        if not src_match:
            return tag
        svg_path = day_dir / src_match.group(1)
        if not svg_path.exists():
            return (
                f'<figure><p class="placeholder">Missing diagram: '
                f"{html.escape(src_match.group(1))}</p></figure>"
            )
        svg = svg_path.read_text(encoding="utf-8")
        svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg).strip()
        alt = alt_match.group(1) if alt_match else ""
        return f'<figure aria-label="{html.escape(alt)}">{svg}</figure>'

    body_html = re.sub(r"<img\s[^>]*?src=\"diagrams/[^\"]+\"[^>]*>", replace, body_html)
    # Markdown wraps a lone <img> line in <p>, since img is an inline element. A
    # <figure> cannot legally live inside a <p>, and the stray </p> it leaves behind
    # sits between </figure> and the caption, so promote_captions never matches.
    return re.sub(
        r"<p>\s*(<figure\b.*?</figure>)\s*</p>", r"\1", body_html, flags=re.DOTALL
    )


def promote_captions(body_html: str) -> str:
    """Turn the italic line directly after a figure into its <figcaption>."""
    return re.sub(
        r"(</figure>)\s*<p><em>(.*?)</em></p>",
        lambda m: f"<figcaption>{m.group(2)}</figcaption></figure>",
        body_html,
        flags=re.DOTALL,
    ).replace("</figure><figcaption>", "<figcaption>")


def wrap_tables(body_html: str) -> str:
    """Tables must scroll inside their own box, never the page body."""
    return body_html.replace("<table>", '<div class="table-scroll"><table>').replace(
        "</table>", "</table></div>"
    )


def render_day(md_path: Path) -> tuple[dict[str, str], str]:
    raw = md_path.read_text(encoding="utf-8")
    front, body = split_frontmatter(raw)

    # md_in_html only descends into raw HTML that opts in, so opt every dropdown in.
    body = body.replace("<details>", '<details markdown="1">')
    # Drop the H1 — the shell renders the title from frontmatter.
    body = re.sub(r"^#\s+.*$", "", body, count=1, flags=re.MULTILINE)

    converter = markdown.Markdown(extensions=MD_EXTENSIONS)
    body_html = converter.convert(body)
    body_html = inline_svgs(body_html, md_path.parent)
    body_html = promote_captions(body_html)
    body_html = wrap_tables(body_html)
    return front, body_html


# ── Page construction ──────────────────────────────────────────────────────────


def build_sidebar(manifest: dict, written: dict[int, dict[str, str]]) -> str:
    parts: list[str] = [
        '<div class="brand">',
        f'<h1>{html.escape(manifest["course_title"])}</h1>',
        f'<p>{html.escape(manifest["course_subtitle"])}</p>',
        '<p class="progress-line">0 of 30 days read</p>',
        "</div>",
        '<nav aria-label="Course days">',
    ]
    for week in manifest["weeks"]:
        parts.append('<div class="week-group">')
        parts.append(
            f'<div class="week-label">Week {week["week"]} · Days {html.escape(week["days"])}</div>'
        )
        parts.append(f'<div class="week-goal">{html.escape(week["title"])}</div>')
        for day in manifest["days"]:
            if day["week"] != week["week"]:
                continue
            number = day["day"]
            is_written = number in written
            classes = "day-link" if is_written else "day-link unwritten"
            disabled = "" if is_written else " disabled aria-disabled=\"true\""
            title = written[number].get("title", day["title"]) if is_written else day["title"]
            suffix = "" if is_written else " · not written yet"
            parts.append(
                f'<button class="{classes}" data-day="{number}"{disabled}>'
                f'<span class="num">{number:02d}</span>'
                f"<span>{html.escape(title)}{suffix}</span>"
                f'<span class="tick"></span>'
                "</button>"
            )
        parts.append("</div>")
    parts.append("</nav>")
    return "\n".join(parts)


def build_sections(manifest: dict, rendered: dict[int, tuple[dict[str, str], str]]) -> str:
    by_number = {day["day"]: day for day in manifest["days"]}
    week_titles = {week["week"]: week for week in manifest["weeks"]}
    ordered = sorted(rendered)
    sections: list[str] = []

    for index, number in enumerate(ordered):
        front, body_html = rendered[number]
        meta = by_number.get(number, {})
        week_number = int(front.get("week") or meta.get("week", 0))
        week = week_titles.get(week_number, {})
        title = front.get("title") or meta.get("title", f"Day {number}")
        minutes = front.get("reading_minutes", "")
        # Keep the eyebrow to one line — the week's title already sits in the
        # sidebar directly above the day list, so repeating it here only wraps.
        eyebrow = f"Day {number:02d} · Week {week_number}"
        if minutes:
            eyebrow += f" · {minutes} min read"

        footer = ['<div class="day-footer">']
        footer.append(
            f'<button class="btn primary mark-read" data-day="{number}">Mark as read</button>'
        )
        if index > 0:
            previous = ordered[index - 1]
            footer.append(
                f'<button class="btn go-day" data-day="{previous}">← Day {previous:02d}</button>'
            )
        if index < len(ordered) - 1:
            following = ordered[index + 1]
            footer.append(
                f'<button class="btn go-day" data-day="{following}">Day {following:02d} →</button>'
            )
        footer.append("</div>")

        sections.append(
            f'<section class="day-section" data-day="{number}" hidden>'
            f'<div class="eyebrow">{html.escape(eyebrow)}</div>'
            f"<h1>{html.escape(title)}</h1>"
            f"{body_html}"
            f'{"".join(footer)}'
            "</section>"
        )

    if not sections:
        sections.append(
            '<section class="day-section" data-day="0"><p class="placeholder">'
            "No days written yet.</p></section>"
        )
    return "\n".join(sections)


def build(out_path: Path) -> None:
    manifest = json.loads((META_DIR / "days.json").read_text(encoding="utf-8"))

    rendered: dict[int, tuple[dict[str, str], str]] = {}
    for day in manifest["days"]:
        md_path = COURSE_DIR / f"day-{day['day']:02d}-{day['slug']}" / "README.md"
        if md_path.exists():
            rendered[day["day"]] = render_day(md_path)

    written = {number: front for number, (front, _) in rendered.items()}
    total = len(manifest["days"])

    page = f"""<title>{html.escape(manifest["course_title"])} — {html.escape(manifest["course_subtitle"])}</title>
<style>{PAGE_CSS}</style>
<div class="controls">
  <button class="icon-btn" id="menu-toggle" aria-label="Toggle day list">☰</button>
  <button class="icon-btn" id="theme-toggle" aria-label="Toggle light or dark theme">◐</button>
</div>
<div class="layout">
  <aside class="sidebar">{build_sidebar(manifest, written)}</aside>
  <main class="content"><div class="content-inner">{build_sections(manifest, rendered)}</div></main>
</div>
<script>var TOTAL_DAYS = {total};{PAGE_JS}</script>
"""

    out_path.write_text(page, encoding="utf-8")
    size_kb = len(page.encode("utf-8")) / 1024
    print(
        json.dumps(
            {
                "event": "course_page_built",
                "output": str(out_path),
                "days_written": len(rendered),
                "days_total": total,
                "page_size_kb": round(size_kb, 1),
            }
        )
    )
    if rendered:
        missing = [d["day"] for d in manifest["days"] if d["day"] not in rendered]
        if missing:
            print(
                json.dumps(
                    {
                        "event": "days_not_yet_written",
                        "count": len(missing),
                        "days": missing,
                    }
                )
            )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the single-page FDE course site.")
    parser.add_argument(
        "--out", default=str(COURSE_DIR / "index.html"), help="output HTML path"
    )
    args = parser.parse_args()
    build(Path(args.out))


if __name__ == "__main__":
    main()
