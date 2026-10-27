# AGENTS.md

Instructions for any AI agent working in this repository or in a user's JobSearchOS folder.

## What this is

JobSearchOS is a job-search operating system made of plain-markdown skills (`plugin/skills/`), a workspace template (`plugin/workspace-template/`) and automations (`plugin/automations/`). It ships with no personal data. All personal facts come from the user's own `profile/` folder.

## When a user's folder exists

Read `jobsearchos.config.md` first, then the files in `profile/` that the task needs. Obey `modules:` (a module set to false means the command says so and stops) and `models:` (use the cheapest capable model for each phase).

## Hard rules

1. Never invent a fact, number, employer or quote about the user. A number is usable only if a pillar file states it with a measurement method.
2. Never send anything anywhere on the user's behalf. Draft and stop.
3. Never write a visa, salary or other private detail into a letter, dossier or template.
4. Writing rules live in `plugin/skills/_shared/universal-style.md` and the user's `profile/voice.md`. No em dashes. No negate-then-reframe sentences.
5. Filenames carry the status prefix (`3-`, `2-`, `1-`, `0-`, `zz-`, `DEPR-`). Only `/log-application` and the weekly sync rename files. See `docs/FILING-STRUCTURE.md`.
6. Do not edit `plugin/` files to add anyone's personal content. Run `scripts/scan-personal-data.sh` before any commit.

## Using this in a tool without plugins (ChatGPT, Gemini, others)

Skills are plain markdown. Upload `plugin/skills/` and `plugin/workspace-template/` to the tool's project or workspace and follow `plugin/automations/chatgpt/README.md`.
