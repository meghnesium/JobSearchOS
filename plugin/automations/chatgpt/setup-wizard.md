---
name: setup
description: One-time (and re-runnable) personalisation wizard. Use when the user says "/setup", "set up JobSearchOS", "personalise this", "start my job search system", or when any other JobSearchOS skill finds no profile folder. Interviews the user in short blocks, then builds their profile, voice guide, proof-project pillars, targets, letter spec, brand-coloured HTML templates and filing structure.
---

> **Using this file outside Claude.** Paths written as `${CLAUDE_PLUGIN_ROOT}/...` mean "the file of the same name in the JobSearchOS repo". In ChatGPT, upload the repo's `plugin/workspace-template/` folder and the `plugin/skills/_shared/universal-style.md` file to your Project and treat those as the references. Where this wizard says "write a file", output the file's full contents in the chat in a code block and tell the user to save it at the stated path in their folder. Ignore `/model` advice; pick your tool's smaller, faster model instead.

# Setup wizard

You are building one person's job-search system. Nothing personal ships with this package, so everything below comes from their answers. Ask in short blocks, save after every block, and never invent facts about them.

## Cost discipline (tell the user once, in two lines)

This wizard is questions and file writing. It needs the cheapest capable model.

- If the session is on a larger model than Haiku or the equivalent small model, say: "Setup is mostly questions and file writing. Switching to a small model (for example `/model haiku`) will save tokens. Continue here, or switch and re-run /setup, which resumes where we stopped." Then continue unless they switch.
- Later in setup you ask which model they want for each phase. Recommend: small model for setup and search synthesis, mid model for writing, large model never required.

## Resume logic

1. Look for `jobsearchos.config.md` in the workspace folder they name (or the current folder). If it exists and `profile/` files still contain the text `[Your`, setup is half done: list which blocks are complete and continue from the first incomplete one.
2. If nothing exists, start at Block 0.

## How to ask

- Ask 3 to 5 questions at a time, numbered, in plain language. If your tool has a multiple-choice question widget, use it for closed questions.
- Offer an example answer for open questions. People freeze on blank boxes.
- "Skip" and "later" are valid answers. Write `[Your ...: to do]` in that field and move on.
- Never ask for anything you do not need. Never ask for passwords, IDs, bank details, or anything sensitive. Salary and visa questions are optional and stay in `profile/` only; they never go into a letter.
- After each block, write that block's files, then say in one line what you saved.

## Block 0: Tool, folder, modules

1. Which AI tool will you use day to day? (Claude, ChatGPT, Gemini, other.) Sets `ai_tool`. Claude users get scheduled-task automation by default. ChatGPT users get the ChatGPT automation pack (Project plus Tasks) and the local script.
2. Where should your job-search folder live? Ask for an absolute path. Explain: "This is your filing structure. Everything lives here: your profile, one file per job, your letters, the tracker. If you use Obsidian, point this at a folder inside your vault and it works as notes. If you do not use Obsidian, it is just a normal folder." Copy the whole of `${CLAUDE_PLUGIN_ROOT}/workspace-template/` into it (this includes `FILING-STRUCTURE.md` and `tools/`), then write that absolute path into `workspace_path` in `jobsearchos.config.md`. Delete `logs/` unless the overnight sweep is on. Set each pillar's `status` to `ready` once it has a claim and at least one usable number with method and caveat, otherwise `draft`. If the folder cannot be written from this tool, produce the files in the working directory and tell them where to move them.
3. Which parts do you want? Core is always on: `/setup`, `/fast-letter`, `/log-application`. Ask yes/no for each optional module and write them to `modules:` in config:
   - Deep research and draft-letter (the slow, thorough path for target companies)
   - Challenge prep (rehearse a take-home, case or live challenge)
   - Product audience analysis and competitive brief (interview prep modules)
   - Warm intros (find named people and draft notes, never sent)
   - Tailored resume per application
   - Overnight job sweep (finds and drafts while you sleep)
   - Friday filename check (keeps file prefixes in sync with status)
4. Models. Show this table and let them accept the defaults or change them. Write to `models:` in config.

| Phase | Recommended | Why |
|---|---|---|
| Setup and file generation | small (Haiku) | questions and templates |
| Search synthesis, JD parsing | small (Haiku) | summarising, cheap |
| Writing the Decision Card and letters | mid (Sonnet) | voice and judgment |
| Deep research, challenge prep | mid (Sonnet), large optional | longer reasoning |

Say: "Open the token budget calculator (`tools/token-budget-calculator.html` in your folder) any time to see what a week costs."

## Block 1: Career identity

Write `profile/identity.md`.

1. Name, the email and phone you want on letters (optional), and where you are based (city, country).
2. Current or most recent job title and current employer. Write `current_employer` and `experience_line` (the one Experience line on the letter, for example "9 years in B2B SaaS, currently at Acme") into `profile/identity.md`; skills use these and never invent a current job, and the title(s) you are applying for. (Example: "Senior Product Manager, also Group PM".)
3. Seniority you are aiming at, and years of experience in the field.
4. Your positioning line: one sentence on what you do and for whom. If they do not have one, draft three options from their answers and let them pick or edit. Example shape: "[Role], [N] years, [domain]. I [what you make better] for [who]."
5. Links to include: portfolio or website, LinkedIn, resume file (path or URL), anything else.
6. Languages and working languages (optional).
6b. The title line to print on letters (`title_on_letter`). If `level_policy` is `never-name`, offer the role family without a level (for example "Product Manager" rather than "Senior Product Manager"). This is what `ROLE_TITLE` is filled with.
7. Work authorisation and logistics, all optional: do you need visa sponsorship or a specific location to stay eligible, notice period, earliest start date. Explain these feed the location flags and the "Before you send" checks, and are never printed in a letter.

## Block 2: Pillars (your proof projects)

A pillar is one body of work you can defend in a screening call. Letters are built from pillars, so this block matters most. Aim for two or three. One is fine to start.

For each pillar, ask and then write `profile/pillars/pillar-N-<slug>.md` using `${CLAUDE_PLUGIN_ROOT}/workspace-template/profile/pillars/_pillar-template.md` (or the copy already in the workspace):

1. Name it: the project or role, the employer, the period.
2. What did you own, in one line? ("I owned X end to end" is a claim. "I contributed to X" is not yet.)
3. When should this pillar be used? (Types of company or problem where it is the strongest proof.)
4. Numbers: each outcome with how it was measured and the caveat. Push for method: "How do you know?" and "Who would disagree?" Any number without a method goes in a `Needs a source` list, not in the usable list.
5. The hardest call: a decision that cost something. What did you refuse, kill or push back on, and why?
6. The systems insight: what is the reusable idea someone could take from it?
7. Did the work outlive your involvement? What did others keep using?
8. The honest limit: what did not ship, what you would do differently.
8b. Which one number or behaviour change could close the "what I did about it" paragraph, and how it was measured? (Fills `Which numbers can close a resolution`. If there is no before-and-after number, name a behaviour change someone could have watched happen.)
9. Best lines: any sentences you have already written about it that sound like you.
10. A link to the case study or page (optional).

Then ask "another pillar?" until they say no.

Finally write `profile/routing.md` from their answers: which pillar leads for which company size or type, which is the secondary proof. If they have one pillar, routing is trivial: say so.

## Block 3: Targets

Write `profile/targets.md` from `${CLAUDE_PLUGIN_ROOT}/workspace-template/profile/targets.md`.

1. Industries or problem types you want, and ones you will not touch.
2. Company size range (headcount) and stage preferences.
3. Geography: where you can work, where you will not. Remote preferences: fully remote, hybrid, onsite, and any entity or timezone constraints.
4. Location rules: build the table together. Each row is a place or setup and a flag: `none` (fine), `check-entity` (ask if they can employ you where you live), `blocker` (dealbreaker, always surfaced first, never dropped quietly).
5. Titles you accept, titles you exclude (for example "agency", "pure execution role").
6. Fit tests: "A company qualifies if at least three of these are true". Offer to write four tests from their domain. Give an example in their field, then ask them to edit. (Example for a product designer: users make consequential decisions under pressure; several surfaces that outgrew their patterns; buyer differs from daily user; regulated or data-heavy domain.)
7. Dealbreakers and hard nos.
8. Weekly target of qualified applications (store it in `weekly_target` in `jobsearchos.config.md` only, never in targets.md) and which days to source, follow up and review. Default 8 a week and Monday source, Thursday warm intros, Friday review. Say: volume is the bottleneck, quality is protected by the kill rule.
9. Job sources. Preload these and let them remove any: LinkedIn (saved searches and job alerts, plus LinkedIn Premium if they have it), startup.jobs, company careers pages, Welcome to the Jungle, Wellfound, Otta, Indeed, Hacker News "Who is hiring", and the aggregator links they already use. Then ask: "Do you want to add other sources? Name boards, newsletters, Slack or Discord communities, or recruiters." Write each source with its URL pattern if known (write `URL unknown, check manually` if not) and which leg it serves (location leg, remote leg). Any template row they did not answer is deleted, never left as a bracketed placeholder, unless they said "later", in which case keep it as `[Your ...: to do]`.
10. A watchlist: companies you want checked directly every sweep. Optional, five to twenty names.

## Block 4: Voice

Write `profile/voice.md` from `${CLAUDE_PLUGIN_ROOT}/workspace-template/profile/voice.md`.

1. How would you describe your tone in three words? Offer: measured, direct, warm, dry, playful, formal, blunt.
2. Default temperature: measured (state a view, then the evidence), bold (state it, no hedge), or measured-plus-one-bold-sentence (recommended). Explain the table in `voice-method.md` if they ask.
3. Level policy: never name your own seniority in letters (the evidence sets it), or name it when the ad asks. Default never-name.
4. Words and phrases you never want to see. Say these ADD to the universal list in `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md`. Ask for pet peeves: "passionate", "synergy", anything.
5. Phrases that are genuinely yours. Ask them to paste a writing sample of their own (a post, an email, a case study intro; 200 to 500 words is ideal, even 60 words helps). If they have none, skip extraction and leave the phrase bank as `[Your phrase bank: to do]`. From a sample, extract: sentence length habits, a short phrase bank, honesty moves ("Worth saying:", "I shipped knowing this"), a closing-warmth style. Show the extraction and let them correct it. Never present your guesses as their voice without confirmation. When running without a person to confirm (a test or a scheduled run), save the extraction marked `(unconfirmed draft)`.
6. How they want to talk about a gap or a limit: always attach the caveat to a number, or only when asked.
7. Do they want the AI disclosure page (page 2 of the structured letter: a short, honest note on how AI was used and where the human judgment sits)? Yes, no, or write it later. If yes, draft two sentences with them and store it as `why_this_section` in `profile/voice.md`, and confirm or edit the default `Page 2` section there (a heading, a one-line lede, a disclosure line, and up to four process cards labelled automated, hybrid or human). The same text appears on page 2 of every letter.

## Block 5: Bio, portfolio and raw material

Write `profile/bio-and-portfolio.md` from the template.

1. Paste your professional bio (any length). If none, draft a 3-sentence bio from Blocks 1 and 2 and ask them to edit.
2. Case studies and work samples: for each, a title, one line, a link or file path, and status (ready, draft, do not use yet).
3. Other material the AI may use: talks, articles, press, awards, recommendations. List links only.
4. Raw material folder: ask for a path to a folder of notes, old cover letters, resumes. Offer to index file names only (never read private material unless they say so) into `profile/bio-and-portfolio.md` under `Raw material`.
5. A "never claim" list: things they do not want implied (tools they barely used, employers whose names they cannot use).
6. Resume: the base resume file, or paste the content. If they skip the resume, set `modules.tailored_resume` to false and omit the tailored-resume question from every Decision Card. The resume template is filled once with static sections (experience, education, skills); only the bio header changes per application.

## Block 6: Letter format and brand

Write `profile/letter-spec.md`, `profile/brand.md`, then generate `templates/`.

1. Letter format. Offer two:
   - **Structured** (default craft): impact card, what-I-do line, opening, bridge, a sourced challenge section with a them-versus-me comparison, a past-tense resolution, close. Best for roles where you can show real product thinking. Uses `letter-template.html`.
   - **Classic**: opening, two body paragraphs, close. Uses `letter-template-classic.html`.
   Show the field table and word budgets for the chosen format, and ask whether to keep or change them.
2. Design settings. This is where the user picks their own colours and fonts. Offer three routes and let them choose:
   - **A preset.** Studio blue, Forest, Terracotta, Graphite, Plum or Sea (colour pairs with matching fonts; the list is in `tools/brand-picker.html`).
   - **Their own values.** Ask for: an accent colour, paper and ink colours (hex, or a colour name you convert to hex), a display font (name and headings) and a body font (any Google Fonts name), and paper size (A4 or US Letter). Ask for a logo file or URL only if they have one.
   - **The visual picker.** Point them to `tools/brand-picker.html` in their folder: they choose colours and fonts with a live preview of the letter, press Copy and paste the block back to you.
   Derive `mute`, `line`, `card` and `dark` yourself from paper, ink and accent (mute: ink mixed 40 percent toward paper; line: paper darkened 10 percent; card: paper tinted 6 percent toward the accent; dark: ink). Check contrast: accent on paper should be at least 4.5:1 and text on paper at least 7:1; if not, say so and suggest a darker accent. Write everything to `profile/brand.md`, which is the source of truth. Offer to change it later: "re-run /setup and choose design settings".
3. Generate templates: copy `${CLAUDE_PLUGIN_ROOT}/workspace-template/templates/*.html` into `<workspace>/templates/` (skip `resume-template.html` if they said to skip the resume). In each file:
   - Replace only the variable values inside the `:root{...}` block. Set `--disp` and `--sans` to the chosen fonts with sensible fallbacks.
   - Replace the single `<link href="https://fonts.googleapis.com/css2?family=...">` line that follows the `BRAND-FONTS` comment with one for the chosen families. Request only weights the family offers (check Google Fonts; if a family has no 700, use its heaviest available weight and update `font-weight` values accordingly).
   - Fill these static identity placeholders once: `{{NAME}}`, `{{ROLE_TITLE}}` (from `title_on_letter`), `{{EMAIL}}`, `{{CONTACT_LINE}}` (HTML: portfolio, LinkedIn and other links separated by ` · `), `{{LOGO}}` (empty string if none), `{{ABOUT_CARD_1}}` (the one experience line from Block 1). Resume static blocks (`EXPERIENCE_BLOCKS`, `EDUCATION`, `SKILLS`, `FOOTNOTE`, `CONTACT_BLOCK`, `EXTRA_BLOCKS`) are filled only if they gave resume content; otherwise leave them and say so.
   - Leave every per-job placeholder (`{{COMPANY}}`, `{{ROLE}}`, `{{OPENING}}` and so on) untouched.
4. Smoke test: confirm the CSS variables changed, no default brand colour is left in the `:root` block, the fonts link names the chosen families, and the per-job placeholders are all still there. If the tool can render HTML, render one sample with `{{COMPANY}}` set to "Example Co" and ask if the look feels right, then adjust once. If it cannot render, say so and skip the visual check.
5. Offer a one-time page-2 / disclosure text if they said yes in Block 4.

## Block 7: Automation

Read `jobsearchos.config.md` `ai_tool`.

- **Claude:** offer the overnight sweep and the Friday filename check as scheduled tasks. Use the prompts in `${CLAUDE_PLUGIN_ROOT}/automations/claude/`. Ask for their time zone, which weekdays, and the hour. Recommend the sweep Monday to Thursday before they wake, a watchdog an hour later that messages only on failure, and the Friday check at a time they are at their desk. Create the tasks only after they confirm the cron summary in plain words ("Monday to Thursday at 03:30 your time"). Never schedule anything without a yes.
- **ChatGPT, Gemini, other:** point them to `${CLAUDE_PLUGIN_ROOT}/automations/chatgpt/README.md` (Project plus scheduled Task) and `${CLAUDE_PLUGIN_ROOT}/automations/scripts/sync-filenames.py` for the Friday check. Offer to print the exact Project instructions and Task prompt with their folder name and time zone filled in.
- If they said no to the sweep, show the manual Monday sourcing checklist from `00-START-HERE.md` instead.

## Block 8: Finish

1. Write `jobsearchos.config.md` with every answer, `00-START-HERE.md` (weekly loop and commands, filled with their cadence), `Applications-Tracker.md` and `Job-Inbox.md`.
2. Self-check. Find unfilled placeholders: search every file in `profile/` (skip `profile/pillars/_pillar-template.md`) for `[Your` and for any bracketed instruction such as `[e.g.`, `[Company]`, `[phrase]`, `[word]`, `[Test`, `[URL]`, `[leg]`, `[pillar`, `[Another`, `[Title`, `[Industries`, `[Optional`. List what is still empty with the block it belongs to. Search the templates for the default `:root` colours and for any string that is not the user's. Fix or report.
3. Run a 60-second dry run of the Decision Card on a job ad the user pastes (turn 1 of `/fast-letter` only, no files written), so they see it works with their profile. If they have no ad ready, skip.
4. Print the summary: what was created, the folder tree, the five commands they will use this week, and the token budget calculator path with their weekly target and chosen models.
5. Say plainly what is not done and what the next best action is. Example: "Pillar 2 still needs numbers with a method. Everything else is ready. Next: paste your first job link and run /fast-letter."

## Rules

- Never invent a number, an employer, or a quote. Anything missing stays as `[Your ...: to do]`.
- Never write a secret, ID, salary or visa detail into a letter, dossier or template. They live only in `profile/identity.md`.
- Use the user's words. When you draft for them (a positioning line, a bio, a tone summary), show it and get a yes before saving.
- No em dashes in anything you write for them. No emojis unless they use them.
- When running without a person to confirm (a test or a scheduled run), save anything you generated yourself (voice extraction, personality line, routing rows, page-2 cards) marked `(unconfirmed draft)` and list those in the final summary.
- Idempotent: re-running setup updates files, it never duplicates them. Keep old versions as `DEPR-<name>` in the same folder.
