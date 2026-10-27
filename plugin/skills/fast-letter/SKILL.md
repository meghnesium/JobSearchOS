---
name: fast-letter
description: One-pass job link to sendable cover letter in under 30 minutes, with exactly one decision from the user. Use when the user says "/fast-letter", pastes a job link or job description and wants to apply, says "quick letter for [company]", "fast pass on this JD", or "I want to apply to this now". This is the default path. Use research-company plus draft-letter only when the user explicitly asks for the deep two-session version.
---

# Fast letter

Job link in. Decision Card out. The user picks a number. Letter, HTML file, dossier and tracker row all come in the second turn.

Two turns of the user's attention, total. That is the whole design. Every rule below exists to protect it.

## Setup, read before anything else

1. Read `jobsearchos.config.md` (workspace root). If `modules.fast_letter` is false, say so in one line and stop. If `workspace_path` is empty, ask the user once for it and continue. If the tool cannot read files, ask the user to paste `profile/identity.md`, `profile/routing.md`, `profile/targets.md`, `profile/voice.md`, `profile/letter-spec.md` and the pillar files.
2. Read the profile files this skill depends on: `profile/identity.md`, `profile/pillars/*.md`, `profile/routing.md`, `profile/targets.md` (location rules, level rules), `profile/voice.md`, `profile/letter-spec.md`.
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md`. Those rules are absolute.
4. If `profile/identity.md` or the pillar files are missing or empty, stop and tell the user to run `/setup` first.

## Why this skill exists

The two-session flow (`research-company` then `draft-letter`) produces a better dossier and costs half a day. Most applications do not earn half a day. This skill does the judgement work by hand: it picks the challenge, maps the user's proof project to it, names the gaps and shows one screen to choose from.

The user reads two things: the Decision Card and the finished letter. Nothing else reaches them.

## Cost discipline

Read `models:` from the config. Defaults: search synthesis and JD parsing on the `search` model (Haiku), the Squeeze, the Decision Card and the letter on the `writing` model (Sonnet). Nothing here needs the most expensive model. If the session is on Opus, say so in one line at the start and continue.

**Read no reference files on the happy path.** The profile files above are the only reads. Open `${CLAUDE_PLUGIN_ROOT}/skills/draft-letter/references/` only when a rule below tells you to, or when the company is so unusual that no pillar fits.

**Search budget: one consolidated query.** Ceiling of three if the first returns nothing usable. Every extra search costs minutes and tokens for information that rarely changes the letter. When a call is close, take the faster option: a good letter today beats a better letter tomorrow.

## Turn 1

### Input

The user invokes with a job link, a pasted job description, or a company name. If only a company name is given, ask for the link in one line and wait. Do not research a company without the ad; the ad scopes the role.

Do not ask anything else. Not about the hiring manager, not about tone, not about which project to use. You decide those and show the decision on the card.

### Location check, silent unless it fails

Read the location rules table in `profile/targets.md` and `jobsearchos.config.md`. Match the ad's location and setup (onsite, hybrid, remote) against the table. The result is one of three flags, written to the dossier as `location_flag`:

- `none`: fine, say nothing.
- `check-entity`: add the check named in the rules table as one of the Before-you-send bullets in turn 2 (typically "confirm they can employ someone based in [user's country]").
- `blocker`: put **BLOCKER: [reason from the rules table]** as the first line of the Decision Card, then carry on. Never quietly drop it.

Rules are checked from most to least specific. If several rows match, the strictest flag wins (blocker over check-entity over none) and the card says which row applied. If the ad names several places or setups (for example "Remote, Portugal" and also a city), apply the best-matching row, and say on the card which row you applied.

If the rules table is empty, treat the flag as `none` and add one Before-you-send bullet asking the user to check location and work authorization against `identity.work_authorization`.

### Level check, silent unless it fails

Read `level_policy` from the config and `identity.seniority` and `targets.md` (titles accepted and excluded). If the ad is clearly below the user's level (junior, mid, or a pure execution role), say so on the Decision Card and recommend skipping. Otherwise apply the policy in the letter: with `never-name`, never write a seniority word (staff, senior, lead, principal) and never argue level; the evidence sets the level in the room. With `name-when-asked`, still do not volunteer it; only name it if the ad or the user asks.

### Company size

Routing and fit depend on headcount. If the ad or a quick search does not give it, estimate a range from public signals (funding stage, team pages, careers page size), write `company_size: unknown (assumed 100 to 500)` in the dossier, route as the middle row of `routing.md`, and say so on the Decision Card. Never skip a company only because its size is unknown.

### Read the ad, then search once

From the ad, pull: the product surface the role owns, **the two skills they are actually buying (the Top 2 asks, reused later for `what_i_do` and, if the user wants a tailored resume, the resume bio)**, seniority, and the phrases that reveal strain. Strain sounds like "bring consistency across", "define the vision for", "our first hire on", "scale the platform", "align stakeholders". Those phrases are the job's real content.

Then one search:

```
"[Company]" product what it does customers pricing team recent launch
```

Synthesise on the `search` model. You want: what they ship, who pays, which surface is growing fastest, anything public about the team the role joins. Skip funding rounds, culture pages and press releases unless the ad points at them.

Also run the fit tests from `profile/targets.md` against what you found. If fewer than the required number pass, say so on the card.

### The Squeeze

Name one challenge they have not solved. It must be a problem in the user's discipline (as defined by `identity.role_title` and the pillar files), specific enough to break if pasted into a competitor's letter, and something the user has receipts for in a pillar file.

If nothing survives, say so on the card and recommend killing the application. Killing is a valid output and saves the user the most time of all.

## The Decision Card

Under 200 words. This is the only thing the user reads before the letter, so it fits on one screen. No preamble, no "here is what I found".

```
**[Company] · [Role]** · fit: strong / workable / thin

**Their problem:** [one sentence, a thing they have not solved, evidenced from the ad or the product]

**1. Scale** [one line hook] → [pillar, metric]
**2. Org** [one line hook] → [pillar, metric]
**3. Ambiguity** [one line hook] → [pillar, metric]

**Gaps:** [gap one, honest, one line] · [gap two, honest, one line]

**Tailored resume too?** [y/n, one line. Worth it only for a company the user would call important. The bio header gets rewritten with this ad's Top 2 asks, everything else in the resume stays exactly as verified]

Reply with a number, and y or n for the resume.
```

Each hook opens from a different door: their scaling problem, their cross-functional or organisational problem, their zero-to-one or ambiguity problem. One line each, written as the actual opening move, not a description of one. Each hook points at a real pillar and a real number from that pillar file.

Gaps are where the user's background genuinely does not cover what the ad asks for. Compare the ad to `identity.md` and the pillar files, including each pillar's `Honest limit`. Do not soften them. The user needs to know what a screening call will probe. Typical real gaps: a market or user type never worked with, no direct people management, a platform never shipped on, a domain never worked in, a company stage never worked at.

Then stop. Do not draft. Do not offer to draft. Do not add caveats or a list of links. Wait.

## Turn 2

The user replies with a number. Write everything in one pass. No drafts, no options, no asking the user to confirm tone.

### Where the proof comes from

**Do not use any number, claim or story that is not in the user's own files.** Read `profile/pillars/*.md` and `profile/routing.md`. Every number must trace to a pillar file. If a number is not there, leave it out.

- **Pillar choice:** `routing.md` maps company size and type to a primary and secondary pillar. Apply it to the company you researched. Prefer pillars with frontmatter `status: ready`. Use a `draft` pillar only if no ready pillar fits, and say so on the Decision Card. Never use `do-not-use-yet`.
- **What each pillar offers:** `One-line claim`, `Numbers (all defensible)` with each number's measurement method and caveat, `The hardest call`, `The systems insight`, `Honest limit`, `Best lines`, `Outlived my involvement`, `Link`.
- **Which numbers can close a `resolution`:** read the pillar's `Which numbers can close a resolution` section. Some pillars carry true before-and-after deltas. Others carry adoption or influence numbers, which close on a named behaviour change with a number attached rather than a delta. Both are allowed. Reaching across pillars for a number the story did not produce, or writing a percentage the pillar file does not hold, is not.
- **Positioning:** every letter is a variation on `identity.positioning_line`.

### What the letter has to carry

Weighted in this order. Total body length follows the budgets in the letter spec below.

**Systems thinking, heaviest.** How the user built the system or set the long-term direction, not what they produced. The decisions that held up, and what got easier for other people because of them.

**Business impact.** Revenue moved, time saved, a metric shifted. Numbers only from the pillar files, each with its caveat attached.

**Cross-functional leadership.** Where the user guided partners or executives, and what changed in how they worked. The mechanism, not the adjective: what they set up, what they argued for, who came along.

**Ambiguity.** One short concrete story about walking into a mess and finding its shape. It should read like something that happened, with a specific detail in it.

Leave out tools and craft execution entirely at senior levels. Naming a tool reads as a downgrade. Write about the scale of the systems and the cost of the decisions.

At least two of these three signals must be visible in the letter itself, because they separate a senior-shaped letter from a mid-level one: the user shaped what got built, the user made a decision that cost something, the user's work outlived their involvement. The pillar files' `The hardest call` and `Outlived my involvement` sections are where to find them.

### Voice

Apply `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md` in full (it holds the hard rules, the tendencies, the Acme test and the temperature guidance), then `profile/voice.md` on top (personality, extra banned words, phrase bank, honesty moves, closing warmth). Default temperature comes from `profile/voice.md`: measured plus exactly one bold sentence unless the user's file says otherwise. If `profile/voice.md` is thin, read `${CLAUDE_PLUGIN_ROOT}/skills/draft-letter/references/voice-method.md`.

The one exception to "never bold" (structured format only): wrap the metric or behaviour-change clause that closes `resolution` in `<strong>` tags so it is the one thing a skimming reader catches. Nowhere else gets bolded.

### Fields to fill

Read `profile/letter-spec.md` for the chosen format and the word budget per field. If it is missing, use `letter_format` from the config; if that is missing, use structured.

**If format is structured,** use the field set below. These budgets are the default fallback when `letter-spec.md` does not override them. They are generic craft: they keep the letter to one page.

| Field | Default budget | Rule |
|---|---|---|
| `impact_card` | 1 sentence | The only About-me card that changes per company. The shape of what the user brings at their scale. |
| `what_i_do` | roughly the length of `identity.positioning_line` | Base: the positioning line. Weave in 1 to 2 terms from this ad's Top 2 asks without changing length or rhythm. Keep the base line if nothing fits naturally. |
| `opening` | 70 to 85 words | Names what the user wants, lands on the company by sentence two, finishes on current work. Ends positive. No diagnosis. |
| `bridge` | 35 to 45 words | Transition, the reason the user did it, one human detail. Never announces method. |
| `challenge_setup` | 45 to 55 words | The screen or surface, present tense, described not judged. The only place their product gets discussed at length. Carries a Source line; no source means it does not go in. |
| `parallel_note` | 15 to 25 words | Only when the example is not from the user's current or most recent role. Say why, honestly. |
| `band_them` | 2 bullets | Observable facts about their situation. No adjectives, no verdict. |
| `band_me` | 2 bullets | Mirrors `band_them` line for line. |
| `resolution` | 45 to 60 words | **Past tense, the user's own work. Zero conditionals.** Three beats: what the user introduced (name the artifact), where that pattern went next (a level above `band_me`, never a restatement of it), what changed because of it. A metric with its method if one exists, otherwise a named behaviour change someone could have watched happen. Wrap this last beat in `<strong>`. |
| `hedge` | 1 line | Concedes the outside view. |
| `close` | 55 to 70 words | Concedes their constraints, says what the user would enjoy about their version of the problem, hands authority back. |
| `closing_line` | under 10 words | Warm, no presumption of the job. |

**Other placeholders you fill every time.** `{{GREETING}}`: "Hi [first name]," if the ad or a quick search names the hiring manager or team lead, otherwise "Hello [Company] team,". `{{DATE}}`: today, written "27 October 2026" style. `{{CHALLENGE_SOURCE}}`: the exact page, as a short link or page title. `{{ROLE}}`: the job title in the ad; with `never-name`, remove level words (junior, senior, staff, lead, principal) from it so no seniority word appears anywhere in the letter. `{{PILLAR_COMPANY}}`: the employer named in the chosen pillar. Identity placeholders (`NAME`, `ROLE_TITLE`, `EMAIL`, `CONTACT_LINE`, `LOGO`, `ABOUT_CARD_1`) were filled once by `/setup` and are not touched. **Page 2:** fill `{{DISCLOSURE}}`, `{{PROCESS_HEADING}}`, `{{PROCESS_LEDE}}`, `{{PROCESS_CARDS}}` and `{{WHY_THIS_SECTION}}` from the `Page 2` section of `profile/voice.md` (the same text for every letter). If `why_this_section` is empty or the user chose no AI disclosure, delete everything between `PAGE2-START` and `PAGE2-END`, and the letter is one page.

**If format is classic,** use these fields only: `opening` (60 to 80 words), `body_1` (90 to 120), `body_2` (70 to 100), `close` (40 to 60), `closing_line` (under 10 words). The same universal rules and the same number discipline apply. `body_1` carries the strongest pillar story with its number and caveat; `body_2` carries the second beat (cross-functional or ambiguity). No bands, no challenge section, no bold.

**If the pillar has no usable closing number** (`Which numbers can close a resolution` is empty or a placeholder): close `resolution` on a named behaviour change taken from the pillar's `Outlived my involvement` or `The hardest call` section, and add a Before-you-send bullet: "Add a closing number to pillar [X] to strengthen the resolution." Never invent one.

**`resolution`, before and after.** This field is the one most often written wrong, so the shape is worth showing. The example is invented: the company, the numbers and the product are illustrative only. Never reuse them.

*Wrong, because it proposes and the impact is missing:*
> At Northwind Analytics, I'd start from that same page-level instinct. Regional managers would adopt the dashboard for their own sites, then share it upward.

*Right, because it reports, zooms above `band_me`, and lands on what moved (illustrative numbers):*
> At my last company that filter stopped being one screen's fix. One build serving both altitudes became the rule for every report after it, no separate executive view, and <strong>by the fifth report the team was shipping one in two working sessions, down from five (illustrative)</strong>. Site managers picked it up for their own regions unprompted and passed it upward themselves.

The **target** company's name does not appear in `resolution` at all. The connection to them is already made by the bands above it and by `close` below it. The only company named is the user's own. The bolded clause is the only bold text anywhere in the letter.

### Output location

Workspace folder: `workspace_path` from `jobsearchos.config.md`. Outputs go in `<workspace>/jobs/`. If `workspace_path` is empty, ask once. If the folder is unreachable, write to the working directory, deliver the files in chat, and say in one line where they landed.

**Filenames reflect status, not date.** Because `fast-letter` ends at `drafted`, the prefix is `3-`. The full mapping (researched and drafted `3-`, applied `2-`, screening and task `1-`, offer `0-`, rejected, ghosted and killed `zz-`, superseded `DEPR-`) lives in `<workspace>/jobs/_TEMPLATE.md`. Only `/log-application` renames files on a status change.

Write three things, four if the user said `y` to the resume:

1. `jobs/3-companyslug.md`, the dossier. Structure from `<workspace>/jobs/_TEMPLATE.md`. Part 1 carries the compressed research, Part 2 carries the copy fields. Set frontmatter: `status: drafted`, `location_flag`, `pillar` (a slug matching a file in `profile/pillars/`), `tone`, `custom_resume`, `date_spotted`, `date_researched`.
2. `jobs/3-companyslug-letter.html`, from `<workspace>/templates/letter-template.html` (structured) or `letter-template-classic.html` (classic). Fill every `{{PLACEHOLDER}}` from Part 2 and from `profile/identity.md`. Change no CSS except `--pz`, dropped 0.01 at a time only if page 1 overflows. If `{{WHY_THIS_SECTION}}` has no content in `profile/voice.md` or `bio-and-portfolio.md`, remove the whole page 2 block cleanly (between the `PAGE2-START` and `PAGE2-END` comments) and leave a one-page letter. Do not generate a PDF; the user exports from the browser.
3. A row in `<workspace>/Applications-Tracker.md`. The tracker is maintained by the skills from dossier frontmatter, so add the row the same way `/log-application` does.
4. **If the user said `y` to the resume:** `jobs/3-companyslug-resume.html`, from `<workspace>/templates/resume-template.html`. Fill only `{{BIO_HEADER}}` per Part 3 of the dossier template. Everything else in the resume is static and already verified; do not touch it. If the tailored resume module is off (`modules.tailored_resume: false`), say so in one line and skip.

Deliver the HTML (and the resume HTML, if made) to the user as well as writing it to disk, using whatever your tool offers (an attachment or file card, a saved file, or the full text in the message). If the tool offers none of these, put the full text in the message.

### What the user sees in turn 2

The letter as readable text in chat, then this and nothing more:

```
**Before you send**
- [thing in the letter to sanity-check, usually a claim about their product]
- [the gap they will probe in a screening call]
- [the user's two-sentence answer to it, drawn from the pillar file's Honest limit]
- [one optional sharpening link, or the entity check if location_flag is check-entity]
```

Four bullets maximum.

## Self-check before showing anything

Run these on the letter. Fix silently, then report only the result in one line.

1. Swap the company name for "Acme". Does the letter still make sense? If yes, the opening is generic. Rewrite it first.
2. Zero em dashes, zero reframe constructions, zero banned words (universal list plus `profile/voice.md`).
3. `opening` ends positive. In the structured format, `resolution` is past tense, carries zero conditionals ("I'd", "I would"), zooms a level above `band_me`, ends on a metric with its method or a named behaviour change, and is wrapped in `<strong>`.
4. Every number traces to a pillar file with its caveat attached. The only other numbers allowed are facts from `profile/identity.md` (years of experience) and dates.
5. Every field is inside its budget. If the structured `resolution` pushes page 1 over, set `--pz` to `.97` as the starting point; only if `.95` still overflows should you cut `resolution` to beats 1 and 3.
6. Zero `{{` left in the HTML (the placeholder comment at the top of the template no longer contains braces).
7. At least two of the three level signals are visible in the letter itself, not just true in the research.
8. Nothing else in the letter is bolded except the one `resolution` clause.
9. The challenge section carries a Source line for the surface it describes.
10. Level policy respected: with `never-name`, no seniority word anywhere.

Report: word count, which fields ran over, and the one field you were least sure about so the user knows where to spend their editing pass.

Do not send anything anywhere. The user sends.

## Status and filing

`fast-letter` ends at status `drafted`. It never marks anything `applied`; that is `/log-application`'s job. Statuses: shortlisted, researched, drafted, applied, screening, task, offer, rejected, ghosted, killed.

## When to hand off to the slow path

Tell the user to run `/research-company` instead when the company is a genuine target and one of these is true: the product is invisible from the outside, the challenge failed the Squeeze twice, or the user has already interviewed there. Say it in one line and let them choose.
