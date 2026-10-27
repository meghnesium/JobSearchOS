---
name: sweep
description: Overnight (or on-demand) job sweep. Finds new roles from your configured sources, filters them with your fit tests and location rules, researches the best few, drafts a dossier and letter for each, and sends one summary. Use when the user says "/sweep", "run the sweep now", "find me jobs", or when a scheduled task fires. Honours modules.overnight_sweep.
---

# Sweep

This is the whole overnight pipeline as one procedure. It runs unattended, so it never asks questions: it makes the best call, states it, and carries on. It never sends anything to anyone. The user decides what to send.

Read `<workspace>/jobsearchos.config.md`. A run started by the user's explicit request ("run the sweep now") or by a scheduled task they created always proceeds, even if `modules.overnight_sweep` is false (that flag only controls whether setup offers the automation). Never start a sweep on your own. Read `profile/identity.md`, `profile/targets.md`, `profile/routing.md`, `profile/voice.md`, `profile/letter-spec.md` and every `profile/pillars/*.md` with `status: ready`. If a profile file still contains `[Your`, stop and tell the user which file needs `/setup`.

## Cost discipline

Search synthesis on the `search` model (small). Drafting on the `writing` model (mid). Do not run on a large model; if the session is on one, say so in one line and continue. Cap search calls for the sourcing step at about 40 so research and drafting always have budget.

## 0. Health log, first

Append one line to `<workspace>/logs/Sweep-Health-Log.md`: `- <current date and time, UTC> | STARTED`. Use the real current time. Create the file with a one-line header if it does not exist. If the workspace is unreachable from this tool, keep the log in the same place as the dossiers (see Deliver) or in the working directory and say so.

## 1. Check the inbox

Read `<workspace>/Job-Inbox.md`. Every link under "To research" is a role the user chose by hand. It skips fit filtering and goes straight to step 3. Move each processed link to "Researched" once its dossier exists. An empty inbox is not a failure.

## 2. Source (about 10 minutes)

Work from listing pages, not open-ended search. Use `targets.md` `Job sources`:

- Run two legs: the location leg (roles in the places that are fine for the user) and the remote leg (fully remote roles the user could take from where they live). Do not skip the remote leg: remote roles often do not surface under a location filter.
- Check LinkedIn saved searches or alerts if reachable, the listing pages in the sources table, and the watchlist companies' careers pages directly.
- Prefer roles posted in the last 10 days. Many listings show no date: mark those `date unknown`, check the link is live, and treat anything that looks older than three months as stale. Confirm each link still resolves and the role is still open before spending time on it. Dead listings are common.
- Skip companies already in `jobs/` (match on company slug, any prefix) unless the status is `shortlisted`.

### What counts as a fit

Use the user's `Fit tests`. Mark each test true (evidenced in the ad or public pages), unknown, or false. A company qualifies with at least three true, or two true and two unknown (then note "worth ten minutes" and keep research short). Never count an unverified test as true. If company size is unknown, estimate a range from public signals and mark it `unknown (assumed range)`; do not drop the company for that alone. Respect `size_min`, `size_max`, titles to accept and exclude, industries to avoid and dealbreakers. Filter by problem shape, not by industry name.

### Location rules

Apply the `targets.md` location rules table strictly. Flags: `none`, `check-entity`, `blocker`. Put any `blocker` at the very top of the summary in bold, include it only if the fit is exceptional, and never present it as normal. What matters is whether the user would have to move or break an eligibility constraint, not where the company is incorporated.

## 3. Rank and take the top N

Take the top 4 by genuine fit against the fit tests (fewer if the inbox filled slots), never by brand prestige. If fewer than 4 truly qualify, deliver fewer and say the market was quiet. Do not pad.

## 4. Research each one (25 minutes and roughly 8 searches per candidate, on top of the sourcing budget)

Follow `${CLAUDE_PLUGIN_ROOT}/skills/research-company/SKILL.md` and its playbook, compressed:

1. Read the job ad first. Name the product area it is scoped to and the top 2 asks. Use them only to narrow where you search next.
2. Product recon from verified links. Troubleshooting and error-handling docs are the highest-value source because they name failure modes in the company's own words.
3. Who buys versus who uses daily, and where they diverge. A brief competitive read. Who leads the relevant team (give up after 4 minutes and greet the team). Size, stage, current pressure, culture signal.
4. Write ONE challenge sentence with a **Source** line: the exact page or screenshot. No source, no challenge.
5. Run the five-check test: a real problem not a business problem; breaks if pasted into another company's letter; the user has receipts from the routed pillar; survives the competitive read; sourced to a real screen or page, not the ad. If it fails any check, recommend killing that application and say why. Killing is a good outcome. Never manufacture a challenge that sounds good but is not earned. **A killed candidate gets a dossier only, no letter:** write `zz-companyslug.md` with `status: killed`, the failed checks and a one-line reason, so it is never researched twice. Only candidates that pass get `3-` files and a letter.

## 5. Route the pillar

Read `profile/routing.md`. Choose primary and secondary by company size and type. If the routed pillar is `draft` or `do-not-use-yet`, use the next ready one and say so.

## 6. Write the dossier and the letter

Use `<workspace>/jobs/_TEMPLATE.md` for the dossier and the letter template named by `letter_format` in `<workspace>/templates/`. Fill Part 1 (research) and Part 2 (letter copy) following `profile/letter-spec.md` word budgets and every rule in `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md` and `profile/voice.md`. Every number must trace to a pillar file. Filenames use the status prefix, never a date: `3-companyslug.md` and `3-companyslug-letter.html`. Dates live in frontmatter (`date_spotted`, `date_researched`).

For the structured format, apply the `level_policy`, the Staff-level signal check (at least two of: you shaped what got built; you made a decision that cost something; your work outlived your involvement), and the self-check in `fast-letter`. Fill every `{{PLACEHOLDER}}`, do not change CSS except `--pz`, and verify zero `{{` left.

## Deliver

Every candidate that passes gets two files, both named with the status prefix: the dossier `3-companyslug.md` and the letter `3-companyslug-letter.html` (an optional resume is `3-companyslug-resume.html`). The HTML is generated from the user's branded `templates/letter-template.html` (or `letter-template-classic.html`), has the Export PDF button, and is what the user opens in a browser to see how the letter looks. A markdown draft alone is not a finished sweep result.

1. Write each dossier and letter to `<workspace>/jobs/`. If the workspace is not reachable from this run (common for scheduled cloud runs), write them to the tool's own storage instead (a project folder, `pending/` folder, or the working directory), add one line per item to `<workspace>/Job-Inbox.md` if reachable, and say plainly in the summary where the files landed and that they need moving into `jobs/`.
2. Give the user a readable copy as well, using whatever the tool offers (attachment, file card, a saved file, or the full text in the message). Scheduled runs often have no file delivery: then put the dossier and the complete letter HTML in the message itself, each in its own code block labelled with its file name, so the user can save and open it.
3. One summary message, actually sent as your final message (not just assembled), listing every candidate: company, role, size, location and any flag, job link, the challenge in one line with its Source, which pillar and why, word counts per field against budget with overruns flagged, the field you are least sure about, and any you recommend killing. `blocker` flags go first, in bold.

## Health log, last

Append `- <current date and time, UTC> | COMPLETED | N candidate(s) drafted` (or `COMPLETED | 0 candidates | reason: <short reason>`). Do this even when nothing was found: a "nothing here" line is a healthy run, a missing line is what the watchdog looks for. Write it right before the closing message.

Closing message under 120 words: ask the user to approve or decline each, and point at the two or three fields worth an editing pass. Do not send anything to anyone.
