# The filing structure

Your job-search folder is the memory of the whole system. If you use Obsidian, point it at a folder inside your vault and everything works as notes. If you do not, it is a normal folder. There is nothing else to learn: the structure is just names and one rule.

## The folder

```
your-job-search-folder/
  00-START-HERE.md         the weekly loop and the commands
  jobsearchos.config.md    settings: models, modules, cadence
  Applications-Tracker.md  one table, built from the files below. Never type into it.
  Job-Inbox.md             links you drop for the sweep to pick up
  profile/                 who you are (written by /setup, edited by you)
    identity.md   pillars/   routing.md   targets.md   voice.md
    letter-spec.md   brand.md   bio-and-portfolio.md
  jobs/                    one set of files per job
  templates/               your branded letter and resume templates
  logs/                    Sweep-Health-Log.md (only if the sweep is on)
  tools/                   token-budget-calculator.html
```

## The one rule: the filename carries the status

Every job has a dossier (`.md`), a letter (`-letter.html`) and sometimes a tailored resume (`-resume.html`). The start of the filename says where the job is in your pipeline. There are no dates in filenames: dates live inside the file.

| Status in the file | Prefix | What it means | Example |
|---|---|---|---|
| shortlisted | none | You flagged it. No file yet. | |
| researched, drafted | `3-` | Research and letter done, not sent | `3-acme.md`, `3-acme-letter.html` |
| applied | `2-` | Sent. Follow-up date is set. | `2-acme.md` |
| screening, task | `1-` | A human replied. Interview prep exists. | `1-acme.md` |
| offer | `0-` | You have an offer | `0-acme.md` |
| rejected, ghosted, killed | `zz-` | Closed | `zz-acme.md` |
| superseded, safe to delete | `DEPR-` | Old versions you can delete when you like | `DEPR-old-letter.html` |

Why numbers that count down? Sorted by name, the jobs that need you (`0-` offers, `1-` conversations) float to the top. The finished ones (`zz-`) sink to the bottom. You never hunt for what matters today.

The company part (`acme`) is called the slug. It is lowercase, no spaces, and never changes. Moving a job forward changes only the prefix.

## What changes the prefix

1. **`/log-application`** is the only command that renames files. Tell it a status change in plain words ("Acme, applied") and it updates the frontmatter, sets dates, renames every file for that company, and refreshes the tracker. It also does the status-specific work: applying sets a 7-working-day follow-up; reaching `screening` the first time auto-runs your interview-prep modules once and clears the follow-up.
2. **The weekly check** (optional) fixes drift. If you edit `status:` by hand inside a file, the name no longer matches. Once a week, an automation compares every dossier's `status:` with its prefix and renames the files that disagree. It only renames. It never edits contents and never deletes.

Two engines run that weekly check. Pick one:

| Engine | For | How |
|---|---|---|
| Claude scheduled task | Claude users | `plugin/automations/claude/friday-check-task.md`, runs `/log-application sync` |
| Local script | Anyone, any AI tool, free | `plugin/automations/scripts/sync-filenames.py` plus `schedule-weekly.md` for cron, launchd or Windows Task Scheduler |

You can also run it yourself any time: `/log-application sync` in Claude, or `python3 sync-filenames.py /path/to/folder` (a dry run that only prints) and then add `--apply`.

## Templates and the files made from them

`templates/` holds your branded HTML templates (structured letter, classic letter, optional resume). They keep fixed names because they are not jobs. Every file made from them follows the same rule as the dossier: status prefix, company slug, suffix, no dates.

| Made from | Becomes | Example |
|---|---|---|
| `letter-template.html` or `letter-template-classic.html` | `<prefix>-<slug>-letter.html` | `3-acme-letter.html` |
| `resume-template.html` | `<prefix>-<slug>-resume.html` | `3-acme-resume.html` |

Open any letter or resume in a browser and press **Export PDF** (bottom right) to save a PDF. The overnight sweep and `/fast-letter` both produce the markdown dossier and the HTML letter together, so you can open the letter and see exactly how it looks. Your colours and fonts come from `profile/brand.md`; `tools/brand-picker.html` is a visual way to choose them.

## Inside a dossier

The top of each `.md` is a block of properties (company, role, status, location flag, pillar, dates, and so on). The tracker reads only that block, so you change a property and the tracker follows. Below it: Part 1 research (with the sourced challenge), Part 2 letter copy (what feeds the HTML), optional Part 3 tailored resume header, a pre-send checklist, and a Record table of what happened and when.

Edit prose in the dossier, never in the HTML. The HTML is regenerated from the dossier and your edits there would be overwritten.

## Rules of the road

- One canonical file per job. No version suffixes. Old versions go to `DEPR-`.
- `zz-` is not deletion. Rejections and killed applications teach you something, and "kill" is a good outcome.
- A tool that cannot reach your folder (a scheduled run in the cloud, for example) writes its drafts somewhere it can reach and tells you. Move them into `jobs/` with a `3-` prefix.
