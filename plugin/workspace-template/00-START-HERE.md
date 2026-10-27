# Start here

Your job-search folder. Everything lives here: your profile, one file per job, your letters, the tracker. Re-run `/setup` any time to change something.

- Tracker: [Applications-Tracker.md](Applications-Tracker.md). It builds itself from the top of each file in `jobs/`. Never type into it.
- Settings: [jobsearchos.config.md](jobsearchos.config.md).
- How the filing structure works: the table at the bottom of this page.

## The weekly loop

```
[source day]    Source your weekly target, fit-check, /fast-letter each      -> jobs/3-company.md + -letter.html
[intro day]     /warm-intro on the same batch. Day-7 follow-ups for last week  -> notes drafted, never sent
Before a call   /challenge-prep the evening before                            -> a section in that job's file
[review day]    Update statuses with /log-application, kill 3-week ghosts      -> Applications-Tracker.md
                Check the count against your weekly target
```

If you switched the overnight sweep on, step one happens while you sleep and you start the day reviewing what it drafted. If not, use the manual sourcing checklist below.

## The commands

```
/setup                 Build or change your profile, voice, templates. Re-runnable.
/fast-letter [link]    Default. Two turns: a Decision Card you pick a number from, then the finished letter.
/log-application       Acme, applied      Update status. Renames the files for you.
/log-application sync                     Fix any file prefix that disagrees with its status.

Optional, depending on what you turned on in setup:
/research-company      Acme [link]        Deep path, for the few companies that earn half a day.
/draft-letter          Acme               The writing step of the deep path.
/warm-intro            Acme               2 to 3 named people, drafted notes, never sent.
/challenge-prep        Acme               Rehearse the take-home, case or live challenge.
/product-audience      Acme               Who buys, who uses, where they diverge.
/competitive-brief     Acme               Competitors, differentiator, gap.
/sweep                 Run the overnight sweep now.
```

## The three rules

1. **Kill weak applications.** If there is no honest challenge, skip it. A generic letter is worse than none. The Decision Card says "recommend killing" when this happens.
2. **Let the evidence set the level.** Follow the `level_policy` in your config. Never argue your seniority in a letter.
3. **The Acme test.** Swap the company name for "Acme". If the letter still makes sense, rewrite the opening.

## Manual sourcing checklist (if the sweep is off)

- [ ] Open each source in `profile/targets.md`, newest first. LinkedIn saved searches first.
- [ ] Take roles from the last 10 days. Confirm the link is still live.
- [ ] Fit-check with your fit tests and location rules. Any `blocker` is a skip unless the fit is exceptional.
- [ ] Add links to `Job-Inbox.md` or run `/fast-letter` on each straight away.

## The filing structure

Filenames carry the status, never a date. Dates live inside the file. Only `/log-application` renames files (and the weekly check, if you turned it on).

| Status | Prefix | Example |
|---|---|---|
| shortlisted | none (no file yet) | |
| researched, drafted | `3-` | `jobs/3-acme.md`, `jobs/3-acme-letter.html` |
| applied | `2-` | `jobs/2-acme.md` |
| screening, task | `1-` | `jobs/1-acme.md` |
| offer | `0-` | `jobs/0-acme.md` |
| rejected, ghosted, killed | `zz-` | `jobs/zz-acme.md` |
| superseded, safe to delete | `DEPR-` | `DEPR-old-letter.html` |

Sorted by name, the jobs that need you (`0-`, `1-`) float to the top and finished ones (`zz-`) sink to the bottom. See `FILING-STRUCTURE.md` in the package for the full explanation.
