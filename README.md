# JobSearchOS

A job-search operating system you personalise once. Paste a job link and get a Decision Card (is this worth your time, and which of your projects is the proof), then a sendable letter in your voice, in your brand, with a tracked file for the job. Optional modules add deep research, warm intros, interview prep and an overnight sweep that finds and drafts while you sleep.

Nothing personal ships in this repository. `/setup` interviews you and builds your own profile, so the same package works for a designer, an engineer, a marketer or anyone else.

**New here? Open [`docs/guide.html`](docs/guide.html) in a browser for the illustrated step-by-step.**

## What you get

| Piece | What it does |
|---|---|
| `/setup` | A short interview in eight blocks. Builds your profile, proof-project pillars, voice guide, targets, letter spec and branded HTML templates. Resumable. |
| `/fast-letter` | Job link in, Decision Card, you pick a number, finished letter out. Two turns of your attention. |
| `/log-application` | Updates status and renames files so the filing structure never lies. Also `/log-application sync`. |
| Optional modules | `/research-company` and `/draft-letter` (deep path), `/warm-intro`, `/challenge-prep`, `/product-audience`, `/competitive-brief`, tailored resume. Switch each on or off in setup. |
| Overnight sweep | Sources from LinkedIn and the boards you pick, filters with your fit tests and location rules, researches and drafts the best few. Claude scheduled task, or a ChatGPT scheduled Task. |
| Friday filename check | Keeps every file prefix in line with its status. Claude scheduled task, or a free local script that works with any tool. |
| Branded HTML templates | A structured letter, a classic letter and a resume template with an Export PDF button. `/setup` applies your own colours and fonts, and `tools/brand-picker.html` lets you choose them visually. |
| Token budget calculator | `plugin/workspace-template/tools/token-budget-calculator.html`. See what a week costs and what matching model to phase saves. |

## Quick start (Claude)

```
/plugin marketplace add meghnesium/JobSearchOS
/plugin install jobsearchos@jobsearchos
/setup
```

Or download `JobSearchOS.plugin` from the Releases page and install it from the file. Then paste a job link and run `/fast-letter`.

## Quick start (ChatGPT, Gemini, anything else)

Skills are plain markdown, so they work anywhere. Follow [`plugin/automations/chatgpt/README.md`](plugin/automations/chatgpt/README.md): a Project with instructions and files, a self-contained scheduled Task for the sweep, and a local script for the Friday rename.

## The filing structure

Your job-search folder is where everything lives. Files carry the job's status in their name (`3-` drafted, `2-` applied, `1-` screening, `0-` offer, `zz-` closed, `DEPR-` old), so the jobs that need you float to the top. Works the same in Obsidian or a plain folder. Full explanation: [`docs/FILING-STRUCTURE.md`](docs/FILING-STRUCTURE.md). Worked examples: [`examples/`](examples/).

## The ideas it is built on

1. **Pillars, not a CV dump.** A handful of proof projects, each with numbers that carry a method and a caveat. Letters are built from them, so nothing unsourced reaches a hiring manager.
2. **One real problem per company.** Every letter hangs on a challenge you found in their product, with a Source line. No honest challenge means skip it. Killing weak applications is the best use of your week.
3. **You always send.** The system drafts and stops.
4. **Cheap by design.** A small model for questions and search, a mid model for writing, a large model almost never.

## Privacy

Your profile, salary notes, visa details and drafts stay in your own folder. The package ships no personal data and `scripts/scan-personal-data.sh` is there so contributors can keep it that way. Private details in `profile/identity.md` are never written into a letter.

## Repository layout

```
plugin/                       the installable plugin
  skills/                     setup, fast-letter, log-application, sweep, research-company, ...
  workspace-template/         what /setup copies into your folder
  automations/                claude/, chatgpt/, scripts/
docs/                         guide.html, FILING-STRUCTURE.md, SPEC.md
examples/                     invented persona and three example dossiers
scripts/                      scan-personal-data.sh, build-release.sh
.claude-plugin/marketplace.json
```

## Contributing

Open an issue or a pull request. Run `scripts/scan-personal-data.sh` first. Never add real people's data to examples: keep personas invented and metrics illustrative.

## Licence

MIT. See [`LICENSE`](LICENSE).
