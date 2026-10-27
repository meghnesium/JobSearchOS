# Claude scheduled task: overnight sweep

Create in Claude as a scheduled task. Suggested schedule: Monday to Thursday, a couple of hours before you wake (cron in your own time zone, for example `CRON_TZ=America/New_York 30 3 * * 1-4`). Each run starts a fresh session with no memory, so the prompt below is complete on its own.

The plugin must be installed (or the folder connected) in the environment the task runs in. If the workspace folder is not reachable from a scheduled run, the sweep writes its files to the task's own storage and says so in the summary.

## Prompt

```
You are running my overnight job sweep. This is a fresh session with no memory of prior conversation.

Workspace folder: [ABSOLUTE PATH TO YOUR JOB-SEARCH FOLDER]

1. Read jobsearchos.config.md in that folder, then run the JobSearchOS "sweep" skill end to end. If the skill is not installed, read the file plugin/skills/sweep/SKILL.md from the JobSearchOS repo (or from the copy in my folder at automations/sweep-procedure.md) and follow it exactly.
2. Do not ask questions. Make the best call, state it in the summary, and carry on.
3. Append the STARTED line to logs/Sweep-Health-Log.md first and the COMPLETED line last, even if nothing was found.
4. Do not send anything to anyone. I decide what to send.
```

Model: choose your `writing` model (mid tier). Notifications: push on.
