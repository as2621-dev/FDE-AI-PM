---
title: Never git-amend after dispatching a review panel — HEAD moves while it runs
tags: [git, amend, concurrency, review-panel, grab-issue, workflow, near-miss]
problem_type: convention
symptoms: Your amend silently rewrites a teammate's commit and absorbs their files into yours.
date: 2026-07-26
---

The `/grab-issue` protocol says **one commit** per slice, and the obvious way to honour that
after a review panel returns findings is `git commit --amend`. Do not. On Day 4 that amend
rewrote a **different agent's commit**.

**The sequence.** `86f7bd6` was the day's commit. The review panel then ran for about ten
minutes of wall time. During that window the session lead read the day's report file, formed a
ruling on a question it raised, and committed `38fe1ed` on top. HEAD was no longer mine.
`git commit --amend` amends *HEAD*, not *your last commit* — so it rewrote `38fe1ed`,
absorbing that commit's edit to `course/_meta/STYLE_GUIDE.md` (a file the slice was explicitly
forbidden to touch) into a commit whose message claimed to be Day 4, and discarding the lead's
message entirely.

**What caught it.** Reading `git show --stat HEAD` after committing and noticing a filename
that had no business being there. `git status` was clean, the gate was green, and the commit
looked fine from every other angle. **Always read the file list back after a commit, and treat
any file you did not stage as a stop-and-investigate.**

**Recovery, non-destructive:**

```sh
git reflog -10                       # find the commit you clobbered
git reset --soft <their-sha>         # their commit is HEAD again; your changes stay staged
git diff HEAD --stat -- <their-file> # prove their file is byte-identical to their commit
git commit -F -                      # commit your work fresh on top
```

`--soft` is the right flag: it moves the branch pointer and leaves the index and working tree
alone, so your work survives as staged changes.

**The rule.**

- After dispatching subagents, **assume HEAD has moved.** Commit fresh; never `--amend`.
- If a protocol insists on one commit, satisfy it by committing *once, after* the review
  findings are applied — not by committing early and amending later. Reviewers do not need
  the work committed to read it; they read the working tree.
- Stage explicit paths, never `-A`. That is what made the recovery clean: only my files were
  ever in the index, so the STYLE_GUIDE change arrived from HEAD rather than from my staging
  and `--soft` put it straight back.

**Also worth keeping:** the interruption was itself valuable. The lead's commit answered the
Rule B question this slice's report had asked, and the answer cited a sentence from the day as
its worked example — so the first thing to do after recovering was `git show` the ruling and
verify that sentence still existed after the review edits. **A concurrent commit may be a
reply to you.** Read it before you build on top of it.
