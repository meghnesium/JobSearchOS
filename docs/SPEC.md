# JobSearchOS architecture spec (internal, drives every skill)

Public, generalised version of a private cover-letter system. NOTHING in this repo may contain any real person's data. All identity comes from the user's own `profile/` folder at runtime.

## Workspace (the user's filing structure, created by /setup from `workspace-template/`)

```
<workspace>/
  00-START-HERE.md            weekly loop + commands (generated from config)
  jobsearchos.config.md       machine-readable settings (YAML frontmatter)
  Applications-Tracker.md     built from dossier frontmatter, never typed into
  Job-Inbox.md                links the user drops for the sweep to pick up
  profile/
    identity.md               who they are
    pillars/pillar-1-<slug>.md ... pillar-N   proof projects, one file each
    routing.md                which pillar for which company size/type
    targets.md                what they want + fit tests + location rules + sources
    voice.md                  voice, banned words, phrase bank, level policy
    letter-spec.md            chosen letter format + per-field word budgets
    brand.md                  colours, fonts, logo for the HTML templates
    bio-and-portfolio.md      bio, case-study index, links, raw material
  jobs/                       one dossier per job (+ -letter.html, -resume.html)
  templates/                  letter-template.html, resume-template.html (generated from brand.md)
  logs/Sweep-Health-Log.md    only if sweep module on
```

## Config: `<workspace>/jobsearchos.config.md` (YAML frontmatter)

```yaml
workspace_path: ""            # absolute path; skills ask once if empty
ai_tool: claude               # claude | chatgpt | gemini | other
models:
  setup: haiku                # wizard + file generation
  search: haiku               # search synthesis, JD parsing
  writing: sonnet             # squeeze, decision card, letters
  deep: sonnet                # research-company, challenge-prep (opus optional)
modules:                      # true/false, /setup toggles
  fast_letter: true           # core, always true
  log_application: true       # core, always true
  deep_research: true         # research-company + draft-letter
  challenge_prep: true
  product_audience: true
  competitive_brief: true
  warm_intro: true
  tailored_resume: true
  overnight_sweep: false
  friday_filename_check: true
letter_format: structured     # structured | classic
level_policy: never-name      # never-name | name-when-asked
weekly_target: 8
cadence: {source: monday, warm_intro: thursday, review: friday}
```

Skills read this file first. If a module is false the skill says so in one line and stops.

## Profile file contracts (skills read these instead of inlining anything personal)

- `identity.md` frontmatter: name, email, phone (optional), role_title, target_titles[], seniority, years_experience, positioning_line, base_city, work_authorization, notice_period, earliest_start, links{portfolio, linkedin, resume, other}. Body: bio.
- `pillars/pillar-N-slug.md`: headings `Use when`, `One-line claim`, `Numbers (all defensible)` (each with measurement method + caveat), `The hardest call`, `The systems insight`, `Honest limit`, `Best lines`, `Outlived my involvement`, `Which numbers can close a resolution`, `Link`. Frontmatter: pillar_name, employer, period, status (ready | draft | do-not-use-yet).
- `routing.md`: table of company size / type -> primary pillar, secondary pillar. Plus tone defaults.
- `targets.md`: industries/problem-shape fit tests (min 3 of N must be true), size min/max, titles accepted/excluded, geography, remote rules, location rules table (flag none | check-entity | blocker), dealbreakers, job_sources[] (preloaded: LinkedIn, startup.jobs, company careers pages, plus user-added), watchlist[], weekly_target.
- `voice.md`: personality, default temperature (measured|bold), banned words/phrases (user list ADDS to the universal list in skills), phrase bank, honesty moves, closing warmth, rules for referencing work, level policy.
- `letter-spec.md`: `format: structured|classic` and the field table with word budgets.
- `brand.md`: primary/accent/paper/ink colours (hex), display + body font (Google Fonts names), logo path, paper size (A4|Letter).
- `bio-and-portfolio.md`: bio paragraph(s), case-study index (title, one line, link, status), other material, "never claim" list.

## Universal rules that ship in skills (not personal)

Zero em dashes; zero negate-then-reframe constructions; universal banned AI words and cover-letter cliches (listed in `plugin/skills/_shared/universal-style.md`); never open on a problem with their product; never name a gap in their team; every number needs a source in the pillar file; Source line mandatory on every design/product challenge; the Acme test; Decision Card then letter two-turn flow; kill weak applications.

## Statuses and filing structure (identical for every user)

Statuses: shortlisted, researched, drafted, applied, screening, task, offer, rejected, ghosted, killed.

| Status | Prefix |
|---|---|
| shortlisted | no file yet |
| researched, drafted | `3-` |
| applied | `2-` |
| screening, task | `1-` |
| offer | `0-` |
| rejected, ghosted, killed | `zz-` |
| superseded files/folders | `DEPR-` prefix, hers/his to delete |

Pattern: `jobs/<prefix>-<companyslug>.md`, `-letter.html`, optional `-resume.html`. No dates in filenames; dates in frontmatter. Only `/log-application` (and the weekly check) rename. The weekly check re-syncs prefix to frontmatter `status:` if someone edited it by hand.

## Model discipline

Setup + file generation: Haiku. Search synthesis: Haiku. Writing, Squeeze, letters: Sonnet. Opus never required; skills say so in one line if session is on Opus and continue. Skills read `models:` from config for the wording.

## Placeholders

Skills refer to the plugin's own files with `${CLAUDE_PLUGIN_ROOT}/skills/...` and to the user's with `<workspace>/...` (path from config). No absolute personal paths. Tool-agnostic phrasing: "if your tool cannot read files, ask the user to paste profile/identity.md".
