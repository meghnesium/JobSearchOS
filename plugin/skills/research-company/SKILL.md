---
name: research-company
description: Deep research path. Run a 30-minute research pass on a job posting and produce one dossier with a validated challenge. Use when the user says "/research-company [company]", "research this company", "deep dive on this job", "process my job inbox", or asks for the thorough version. A plain pasted job link goes to fast-letter instead, which is the default path.
---

# Research a company

Run the 30-minute playbook. Produce one dossier. Find one challenge worth writing about.

## Before anything

1. Read `<workspace>/jobsearchos.config.md` (workspace path comes from `workspace_path`; if empty, ask once). If `modules.deep_research` is false, say so in one line and stop.
2. Read `<workspace>/profile/identity.md`, `targets.md`, `routing.md`, and the pillar files named in routing. If your tool cannot read files, ask the user to paste them.
3. Models: use `models.search` for search synthesis and JD parsing, `models.deep` for judgment and the Squeeze. If the session is on Opus, say so in one line and continue. Keep reads small: only open what the current module needs.
4. If the workspace is unreachable, say so once, write output to the working directory, and tell the user to move it.

Full method: `${CLAUDE_PLUGIN_ROOT}/skills/research-company/references/playbook.md`. It is the authority; this file is the operating procedure.

## Inputs

- A company name plus job link (strongly preferred). With only a name, ask for the link.
- Or no input: read `<workspace>/Job-Inbox.md`. Every link listed there skips fit filtering (the user already chose it) and goes straight to research, one dossier each. Research at most three per session, then stop. Move processed rows to the "Researched" section of the inbox.

## Fit and location check (skip fit for inbox links)

Read the tests from `targets.md`. Fit is a problem shape, not an industry: it qualifies when at least 3 of the tests listed there are true. Location: apply the location rules table in `targets.md` and set `location_flag`:

- `none`: no restriction applies
- `check-entity`: something must be confirmed first (for example, whether the company can employ someone in the user's country)
- `blocker`: the rules say it cannot work

A `blocker` goes in the first line of your report, in bold. Research anyway only if fit is exceptional, clearly marked. Never quietly drop it.

Pillar routing: use `routing.md` (company size or type to primary and secondary pillar). Record the pillar slug.

## Procedure

Work the modules in order. Do not narrate between them.

| Module | Budget | Method |
|---|---|---|
| 0. JD scope | 2 min | Read the ad. Name the product area, top 2 asks, location and setup. |
| 1. Product recon | 5 min | Collect and verify ranked LINKS. |
| 2. Product and audience | 6 min | `${CLAUDE_PLUGIN_ROOT}/skills/research-company/references/product-audience.md` (only if `modules.product_audience` is true; otherwise note the buyer and daily user in one line each) |
| 3. Competitive brief | 5 min | `${CLAUDE_PLUGIN_ROOT}/skills/research-company/references/competitive-brief.md` (only if `modules.competitive_brief` is true; otherwise name one rival) |
| 4-6. Company intelligence | 8 min | One consolidated search (see below), synthesised with the `search` model. |
| 7. The Squeeze | 4 min | Judgment call with the `deep` model. |

**Hard stop at 25:00.** Stop researching and write the Squeeze with what you have. Incomplete modules are normal. A 50-minute session is what kills a weekly cadence.

**Do not invent.** Every claim carries its source or is marked as a guess.

### Module 0: JD scope

Name three things: the specific product surface the role owns (not the whole company), the top 2 skills or asks the ad sells for, and where and how they are hiring. Use these only to narrow where to search, never to decide what you are allowed to find. The ad describes where they are headed, not where the product is today.

### Module 1: link collection, not screenshots

Collect verified links, ranked:

1. Video of someone driving the product (official channel, demo page, conference talk). Note the timestamp.
2. Docs pages with real interface screenshots. Troubleshooting and error pages are highest value.
3. Product pages with interface imagery or an autoplay loop.
4. A free trial, only if it opens in under 2 minutes.
5. 3-star reviews on G2 or Capterra.

Verify every URL resolves before writing it down. Record failures under `Dead ends`. Annotate every link with what it shows and why it matters for this challenge. Mark the top 3 as optional sharpening links, never as homework before sending.

If the product is genuinely invisible (sales-gated demo, no public video), say so and set `Confidence` so the letter hedges honestly.

For a role that is not design (product, engineering, marketing, and so on), "interface" generalises to whatever the role touches: the product surface, the codebase's public docs, the campaign, the funnel. Same rule: link it or do not claim it.

### Modules 4-6: one consolidated search

Run ONE search:

```
"[Company]" team lead for this function, funding stage, headcount growth, employee reviews (Kununu or Glassdoor), engineering or company blog, culture
```

Synthesise into: the likely hiring lead (if not findable in 4 minutes, write "not findable, greet the team"), headcount and funding stage, recent moves, culture signals. Then set the tone call from `voice.md` defaults: opinionated public culture means bold; formal, regulated, or silent means measured; in between means measured plus one bold line. Log the signal, not the vibe.

## The Squeeze

One sentence naming a challenge the user can say something real about, with a **Source line**: the exact page or screenshot it is built from. No source, no challenge. Non-negotiable.

Test it against all five checks:

1. It is a problem in the role's craft, not a generic business problem.
2. It is specific to them (it would break if pasted into another company's letter).
3. The user has receipts: a pillar file with a defensible number or story that speaks to it.
4. It survives the competitive read.
5. It is sourced to a real screen or page, not the job ad. If you cannot point to the exact thing, you inferred it.

If it fails, reframe smaller once. If it still fails, **recommend killing the application** and say why. Killing is a valid, valuable output.

## Output

Write `<workspace>/jobs/3-<companyslug>.md` (prefix `3-` for status `researched`), following the structure of `<workspace>/jobs/_TEMPLATE.md` exactly: section order and headings. Fill every section you have evidence for. Leave the letter sections empty, `draft-letter` fills those. Set frontmatter: status, location_flag, company_size, pillar (slug), tone, challenge_checks_passed, research_minutes, confidence.

The tracker is rebuilt from dossier frontmatter by `/log-application`. Do not type into `Applications-Tracker.md`.

## Report back

Under 150 words:

- The challenge, verbatim, with its Source line
- Which of the 5 checks passed
- Tone call and pillar slug with why
- `location_flag` and `company_size`
- The 3 sharpening links, marked optional
- Anything you could not find
- Actual elapsed time, honestly

Then stop. Do not offer to write the letter. Research and writing are deliberately separate sessions.
