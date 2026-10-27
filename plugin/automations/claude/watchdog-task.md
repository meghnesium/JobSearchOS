# Claude scheduled task: sweep watchdog

Scheduled tasks can fail silently. This task checks the sweep ran and only messages you when it did not. Suggested schedule: the same weekdays as the sweep, one to two hours after it (for example `CRON_TZ=America/New_York 30 5 * * 1-4`). Use a small model. A good day produces no message.

## Prompt

```
You are checking whether my overnight job sweep ran successfully this morning. This is a fresh session with no memory.

Workspace folder: [ABSOLUTE PATH TO YOUR JOB-SEARCH FOLDER]
Read logs/Sweep-Health-Log.md. A healthy run has two lines timestamped today (UTC): one STARTED and one COMPLETED. If the file does not exist, treat that as no entry for today. Check the actual current date, do not assume it.

- COMPLETED line timestamped today: the sweep worked. Do not message me. Stop. Silence is the correct result.
- STARTED today but no COMPLETED: send me one short message saying the sweep started but did not finish.
- Neither line today: send me one short message saying the sweep did not fire, and that I can ask for "run the sweep now" to fire it by hand.

Keep any message under 40 words. Do not diagnose, fix anything, touch other files, or re-run the sweep yourself.
```
