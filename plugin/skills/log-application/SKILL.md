---
name: log-application
description: Update a job dossier's status and properties so the tracker reflects reality, and keep filenames in sync. Use when the user says "/log-application", "/log-application sync", "log this one", "I applied to [company]", "I got a screening call", "mark [company] as rejected", "fix my file prefixes", or reports any change in an application's status.
---

# Log an application

You edit properties, never tables. Every tracker view is generated from the YAML frontmatter at the top of each dossier in `<workspace>/jobs/`. Change the property, the tracker follows.

## Before anything

Read `<workspace>/jobsearchos.config.md`. `modules.log_application` is core and always true; if it is somehow false, say so in one line and stop. Use `models.setup` (the cheap model): this is mechanical work. If the session is on Opus, say so in one line and continue. Read `profile/pillars/` only to list valid pillar slugs.

## Two modes

- `/log-application [company] [new status]`: update one dossier (below).
- `/log-application sync`: fix any filename prefix that disagrees with frontmatter (last section).

## The properties

| Property | Allowed values |
|---|---|
| `status` | shortlisted, researched, drafted, applied, screening, task, offer, rejected, ghosted, killed |
| `stage` | startup, scaleup, enterprise, agency |
| `setup` | onsite, hybrid, remote |
| `source` | linkedin, careers-page, referral, recruiter, community, sweep, or a name from `targets.md` job_sources |
| `tone` | bold, measured, measured-plus-one-bold |
| `pillar` | a slug taken from the filenames in `profile/pillars/` (for example `pillar-1-<slug>.md` gives `<slug>`) |
| `location_flag` | none, check-entity, blocker |
| `priority` | high, medium, low |
| `challenge_checks_passed` | 0 to 5 |
| dates | `YYYY-MM-DD` |

Use these strings exactly. The tracker filters on them.

## Status changes

- `applied`: set `status`, `date_applied` (today), and `followup_due` to 7 working days later (count Monday to Friday from today; ignore public holidays, the user can edit the date).
- `screening`: clear `followup_due` (they replied, no chase needed), then run the auto-trigger below.
- `rejected`: add a one-line reason to the Record table if the user gave one. Patterns across rejections matter.
- `ghosted`: nothing auto-marks as ghosted. When asked about stale applications, list everything at `applied` past `followup_due` and let the user decide.
- `killed`: record `challenge_checks_passed` and `research_minutes` so the pattern is visible later.
- Any change: append a row to the dossier's Record table with the date and what happened.

### Auto-trigger at first `screening`

Interview prep runs when status first reaches `screening`, because that is the earliest point advance notice helps. Run only the modules switched on in config, each once:

1. `challenge-prep` mode 1, if `modules.challenge_prep` is true
2. `product-audience`, if `modules.product_audience` is true
3. `competitive-brief`, if `modules.competitive_brief` is true

Skip any whose module is false without comment. Check the dossier first: if frontmatter already shows `interview_prep_challenge`, `interview_prep_audience` or `interview_prep_competitive` as `completed` (or a matching prep section exists), do not rerun that one. Re-running is something the user asks for by name, never automatic. After the runs, report "Interview prep complete. [n] sections added to the dossier."

## Renaming files on every status change

**This skill (and the weekly Friday check, which is `sync` run automatically) is the only thing that renames files.** Every other skill reads whatever prefix is on disk, matching on the company slug, and never renames.

Filenames track the status bucket, never a date. Dates live in frontmatter.

| Status | Prefix |
|---|---|
| offer | `0-` |
| screening, task | `1-` |
| applied | `2-` |
| researched, drafted | `3-` |
| rejected, ghosted, killed | `zz-` |
| superseded files or folders | `DEPR-` (the user deletes them) |
| shortlisted | no file yet |

When a status change crosses into a different bucket:

1. Work out the new prefix.
2. For every file for this company (`<old>-<slug>.md`, `<old>-<slug>-letter.html`, `<old>-<slug>-resume.html` if present), rename to the new prefix. Suffixes never change.
3. Never leave both old-prefixed and new-prefixed copies in `jobs/`. If your tool cannot rename, copy to the new name, verify, then move the old one into `jobs/_to_delete/` (create it if needed) and tell the user that folder exists so they can empty it.
4. Same bucket (`researched` to `drafted`): no rename.

## Rebuild the tracker

After every update, rebuild `<workspace>/Applications-Tracker.md` from the frontmatter of all dossiers in `jobs/` (skip `_TEMPLATE.md`): one row per dossier with company, role, status, stage, setup, pillar, tone, date_applied, followup_due, location_flag, priority; grouped by status bucket, offer first. The tracker is never typed into by hand.

## Report back

Two lines: what changed, and the current count by status. If the user is behind `weekly_target` from config, say so with the number. Do not soften it.

## Mode: `/log-application sync`

The weekly Friday check in manual form (runs automatically when `modules.friday_filename_check` is true; running it by hand works either way).

1. List `<workspace>/jobs/`. Skip `_TEMPLATE.md`, `_to_delete/`, `assets/`, and anything starting with `DEPR-`.
2. For each dossier, read only the frontmatter `status:` and compute the expected prefix from the table above.
3. If the file's prefix differs, rename the dossier and its `-letter.html` and `-resume.html` companions to the expected prefix. Plain rename only. Never edit contents.
4. Rebuild the tracker if anything was renamed.
5. Sync only fixes filenames. It does not clear `followup_due`, set dates, or run interview prep. For a real status change use `/log-application <company>, <status>`.
6. Report in one line: `Sync: [n] checked, [n] renamed ([company: old to new, ...])` or `Sync: [n] checked, all prefixes match.`
