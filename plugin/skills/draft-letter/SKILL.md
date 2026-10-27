---
name: draft-letter
description: Deep drafting path, second half of the two-session flow. Write letter copy into an existing job dossier and render the branded HTML file. Use when the user says "/draft-letter [company]" or asks to turn existing research notes into a letter. For a fresh job link with no dossier, use fast-letter instead.
---

# Draft a cover letter

One letter. Copy goes in the dossier. HTML is generated from it.

**Structure, structured format:** header, About me (cards), the letter (2 paragraphs), one labelled challenge section, close, optional page 2 on process transparency. The company's product is discussed only inside the challenge section. **Structure, classic format:** greeting, opening, two body paragraphs, close, sign-off.

## Before writing anything

1. Read `jobsearchos.config.md`. If `modules.deep_research` is false, say so in one line and stop. If `workspace_path` is empty, ask the user once. Read `models:`; writing runs on the `writing` model (default Sonnet). If the session is on Opus, say so in one line and continue.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md`. Non-negotiable.
3. Read `${CLAUDE_PLUGIN_ROOT}/skills/draft-letter/references/voice-method.md`, then the user's own `profile/voice.md` and `profile/pillars/*.md` (and `profile/routing.md`, `profile/identity.md`). If your tool cannot read files, ask the user to paste them.
4. Read `profile/letter-spec.md` for the chosen format and the word budget per field. If it is missing, use `letter_format` from the config, and if that is missing, structured with the default budgets in `${CLAUDE_PLUGIN_ROOT}/skills/fast-letter/SKILL.md`.
5. Read the job dossier: `<workspace>/jobs/<prefix>-company.md`, where `<prefix>` is the status-based filename prefix (`3-` at researched or drafted; the naming table is in `<workspace>/jobs/_TEMPLATE.md`). If you do not know the current prefix, list `jobs/` and match on the company slug.
6. Read `${CLAUDE_PLUGIN_ROOT}/skills/draft-letter/references/letter-framework.md` only if you are unsure why a field is shaped the way it is.

**Never gate on the sharpening links.** Mention them once at the end if a draft reads thin. Drafting is the point.

**If no dossier exists, stop.** Tell the user to run `/research-company` first (or `/fast-letter` for the one-pass path). Do not research and draft in the same pass.

## Voice

Apply the universal rules in full. They cover: no em dashes, no negate-then-reframe constructions, no dead AI words, dead phrases or cover-letter cliches, no meta-commentary, the Acme test, attach-the-caveat, never open on a problem with their product, never name a gap in their team. Then apply `profile/voice.md` on top (personality, extra banned words, phrase bank, honesty moves). `voice-method.md` explains how.

## Numbers and proof

Read `profile/pillars/*.md` and `profile/routing.md`. Every number must trace to a pillar file. If a number is not there, leave it out. Never borrow a number from another pillar to complete a beat; the mismatch shows. The dossier's `pillar` field names the pillar file slug to draw from. Read each pillar's `Which numbers can close a resolution` section before writing `resolution`.

## Write the copy into the dossier, not into HTML

Fill **Part 2 of the dossier** (`jobs/<prefix>-company.md`). Every field has a word budget and a rule. Respect both.

**Structured fields, in order:** `impact_card`, `what_i_do`, `opening`, `bridge`, `challenge_setup`, `parallel_note`, `band_them`, `band_me`, `resolution`, `hedge`, `close`, `closing_line`. Default budgets (the fallback when `letter-spec.md` does not override): impact_card 1 sentence; what_i_do about the length of the positioning line; opening 70 to 85 words; bridge 35 to 45; challenge_setup 45 to 55; parallel_note 15 to 25; band_them 2 bullets; band_me 2 bullets; resolution 45 to 60; hedge 1 line; close 55 to 70; closing_line under 10.

**Classic fields:** `opening` (60 to 80 words), `body_1` (90 to 120), `body_2` (70 to 100), `close` (40 to 60), `closing_line` (under 10).

`what_i_do` weaves 1 to 2 terms from Part 1's "Top 2 asks" into the base positioning line (`identity.positioning_line`), without changing its length or rhythm and without turning it into a restatement of the ad. Keep the base line if nothing fits.

**The structure of the structured letter, and why it is this way:**

- The letter is **two paragraphs.** The About-me cards already carry the user's background.
- `opening` names what the user wants, lands on the company by sentence two, ends on current work, and **ends positive.** Never a diagnosis.
- `bridge` hands off to the challenge section with a reason and one human detail.
- The company's product is discussed **only** inside the labelled challenge section, never in the letter body. That placement stops it reading as unsolicited consulting.
- `resolution` is **past tense, about the user's own work.** What they introduced or changed, then what changed because of it. Never "At [their company], I'd...". The heading above it reads "What I did about it", so it reports, it does not propose.
- `resolution` sits **one level above `band_me`.** `band_me` names the specific build on the specific screen. `resolution` names the pattern, rule or system that build became, where else it went, and what moved as a result. Its last beat, the metric or behaviour change, is wrapped in `<strong>`, the only bold text anywhere in the letter.
- `close` concedes their constraints and hands authority back. No conditions, no list of things the user would interrogate.
- **Level signals, check before calling it done.** At least two of these three need to be visible in the letter itself: the user shaped what got built, the user made a decision that cost something, the user's work outlived their involvement. If only craft evidence shows up, go back to `resolution` or `band_me` and surface one of the others.
- **Level policy:** read `level_policy` in the config. With `never-name`, never write a seniority word and never argue level.

**Constraints (also Part 2 of the dossier template):**

- Zero em dashes
- `opening` ends positive (no diagnosis)
- `challenge_setup` has a Source line (a page or a screenshot). No source, no challenge.
- `resolution` is past tense about the user's own work, carries zero conditionals ("I'd", "I would", "I'd bring", "I'd start"), and ends on a metric with its method or a named behaviour change
- Zero `{{` placeholders left unfilled
- Every field stays within its word budget

## Render the artifact

**Structured format:** copy `<workspace>/templates/letter-template.html` and fill every `{{PLACEHOLDER}}` from Part 2 of the dossier and from `profile/identity.md`. **Classic format:** use `<workspace>/templates/letter-template-classic.html` with `{{GREETING}}`, `{{OPENING}}`, `{{BODY_1}}`, `{{BODY_2}}`, `{{CLOSE}}`, `{{CLOSING_LINE}}`, `{{NAME}}`, `{{CONTACT_LINE}}`, `{{DATE}}`, `{{COMPANY}}`, `{{ROLE}}`, `{{LOGO}}`.

The structured template is a true-to-PDF layout. Page 1 is masthead, apply row, About me cards, the two letter paragraphs, the challenge section, bands, resolution, close. Page 2 (optional) is the process-transparency page, driven by `{{WHY_THIS_SECTION}}` and the page-2 placeholders. **If the user has no process-transparency copy (empty `{{WHY_THIS_SECTION}}`), remove the whole block between the `PAGE2-START` and `PAGE2-END` comments and ship one page.** Otherwise it stays at exactly two pages.

If page 1 overflows, drop `--pz` in the `:root` block by 0.01 at a time and re-measure. Never edit any other CSS. Brand colours and fonts are set once by `/setup` from `profile/brand.md`; do not touch them here.

Placeholders map one-to-one onto the dossier fields and `profile/identity.md`. `{{LOGO}}` comes from the logo path in `profile/brand.md` (an inline SVG or an `<img>`; empty is fine). `{{PILLAR_COMPANY}}` is the `employer` from the chosen pillar file's frontmatter.

Do not add libraries. Do not restyle the masthead. Do not generate a PDF; the user exports from the browser so headers and footers drop.

Name the output `jobs/<prefix>-company-letter.html`, same `<prefix>` as the dossier's current status. One canonical file per job, no version suffixes. Drafting does not change status by itself; that is `/log-application`'s job, so the prefix should already be `3-`.

**If `custom_resume: true` on this dossier** (and `modules.tailored_resume` is true): also fill Part 3's `resume_bio_header` and render `<workspace>/templates/resume-template.html` into `jobs/<prefix>-company-resume.html`, same folder, same prefix. Only `{{BIO_HEADER}}` changes; every other part of the resume is static and already verified. Same export-PDF button pattern as the letter.

## Then

Verify before reporting: zero `{{` left, zero em dashes, page count correct (two with page 2, one without; classic is one), `resolution` past tense with no conditionals and ending on impact wrapped in `<strong>` (structured only), at least two of the three level signals visible, every number traceable to a pillar file, and the CSS block byte-identical to the template apart from `--pz`.

Report the word count of each field against its budget and flag any that ran over. Tell the user which fields you were least sure about, so they know where to spend their editing pass. Do not send anything anywhere. The user sends.

## Output location

`<workspace>/jobs/` where the workspace path comes from `jobsearchos.config.md` (`workspace_path`). If empty, ask once. If unreachable, write to the working directory and say in one line where the files landed.
