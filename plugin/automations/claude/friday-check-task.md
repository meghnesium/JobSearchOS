# Claude scheduled task: Friday status and filename check

Keeps every file prefix in line with its dossier `status:`. People sometimes edit `status:` by hand without going through `/log-application`, and the filename silently drifts. This catches it weekly. Suggested schedule: Friday afternoon at a time you are at your desk (for example `CRON_TZ=America/New_York 0 15 * * 5`). Small model.

This task needs access to your folder. If it cannot reach it, it tells you and stops. The no-AI alternative is `scripts/sync-filenames.py` (see `schedule-weekly.md`), which works with any tool.

## Prompt

```
You are doing a weekly consistency check on my JobSearchOS job folder. This is a fresh session with no memory.

Workspace folder: [ABSOLUTE PATH TO YOUR JOB-SEARCH FOLDER]

Run `/log-application sync` (JobSearchOS). If the skill is not installed, do this by hand:
1. List jobs/. Skip _TEMPLATE.md and anything starting with DEPR-.
2. For each dossier read the frontmatter status and compare its filename prefix to this table: researched or drafted = 3-, applied = 2-, screening or task = 1-, offer = 0-, rejected or ghosted or killed = zz-, shortlisted = no file yet.
3. On a mismatch, rename the dossier, its -letter.html and its -resume.html to the correct prefix, same company slug. Plain rename only. Do not touch file contents.
4. If the folder is not reachable, send me one short message saying so, and stop.

Report in one line if nothing changed ("Checked N dossiers, all match"). If you renamed anything, list one line per company: old name, new name, the status that justified it. Touch nothing else.
```
