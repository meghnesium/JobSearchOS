---
name: competitive-brief
description: Produce a competitive read on a company. Use when the user says "/competitive-brief [company]", "who are their competitors", "competitive analysis on [company]", or wants market context before an interview. Also auto-triggered when status first moves to screening.
---

# Competitive brief

Not a market report. One question: is the challenge about to be named the thing they are already losing on?

## Before anything

Read `<workspace>/jobsearchos.config.md`. If `modules.competitive_brief` is false, say so in one line and stop. Use `models.search` for gathering and `models.writing` for the three lines. If the session is on Opus, say so in one line and continue. Read the existing dossier in `<workspace>/jobs/` first (match on company slug, any prefix) and reuse what it holds.

Full method: `${CLAUDE_PLUGIN_ROOT}/skills/competitive-brief/references/method.md`.

## When this runs standalone

Budget 15 minutes. Go deeper than the fast version. Use when:

- The user asks for a competitive analysis
- The fast pass returned "none found" on the convention check
- Status first moved to `screening` (auto-triggered by `/log-application`)

## Procedure

**Find 3 competitors.** Fastest paths: their own "vs." pages, the "compared to" section on G2 or Capterra, the category named in the job ad, rivals named in funding coverage. Pick one incumbent, one direct rival, one adjacent threat. If only one exists, that is a finding: the category is new, or they compete against spreadsheets and internal tools.

**Then three lines:**

1. Their real differentiator. Structural, not marketing: proprietary data, distribution, regulatory position, deep integration, or genuinely better UX. If it is "nothing structural, they win on sales," write that.
2. Their one real gap.
3. Product or distribution: which is winning for them.

Then look for one category convention they broke or missed, and write the read on the challenge: already solved by rivals, unsolved by everyone, or they are the ones behind.

Never teach them their own market in outreach, and never name a rival critically.

## Output

Write the findings into the dossier's research section (structure in `<workspace>/jobs/_TEMPLATE.md`) and set frontmatter `interview_prep_competitive: completed`. Edit contents only; never rename files.

Report: "Competitive brief complete. [one-line insight on market position or differentiator]."
