---
company:
role:
status: shortlisted
stage:
location:
setup:
location_flag: none
company_size:
job_link:
careers_page:
source:
pillar:
tone:
portfolio_link:
challenge:
challenge_checks_passed: 0
confidence:
interview_prep_challenge: false
interview_prep_audience: false
interview_prep_competitive: false
outreach: []
sharpening_watched: false
custom_resume: false
date_spotted:
date_researched:
research_minutes:
date_applied:
followup_due:
team_lead:
priority: medium
tags:
  - job
  - jobsearchos
---

# [Company] · [Role]

> Hub: [00-START-HERE.md](../00-START-HERE.md) · Tracker: [Applications-Tracker.md](../Applications-Tracker.md)

**This file is the source of truth.** The properties block feeds the tracker. The **Letter copy** section feeds the HTML. Edit prose here, never in the HTML, or your edits get overwritten on the next regenerate.

### Allowed values

| Property | Values |
|---|---|
| `status` | shortlisted · researched · drafted · applied · screening · task · offer · rejected · ghosted · killed |
| `stage` | startup · scaleup · enterprise · agency |
| `setup` | onsite · hybrid · remote |
| `location_flag` | none · check-entity · blocker |
| `source` | linkedin · careers-page · referral · recruiter · sweep · other (or any `job_sources` name from `profile/targets.md`) |
| `pillar` | a slug matching a file in `profile/pillars/` |
| `tone` | measured · bold · measured-plus-one-bold · default |
| `priority` | high · medium · low |
| `custom_resume` | true · false. Set true at Decision Card time if this one earns a tailored resume, not just the letter. |
| dates | `YYYY-MM-DD` |

**Location.** The flag comes from the location rules table in `profile/targets.md`, read together with `jobsearchos.config.md`. `none` means no action. `check-entity` means the setup is acceptable but the company must confirm it can employ someone where the user is based. `blocker` means the rules table lists this location or setup as a dealbreaker. Never drop a `blocker` quietly: say so first on the Decision Card.

**Pillar routing.** `profile/routing.md` maps company size and type to a primary and a secondary pillar. Write the chosen pillar's slug in `pillar`.

**Status transition, `screening`.** The first time status moves to `screening`, `/log-application` runs `challenge-prep`, `product-audience` and `competitive-brief` (when those modules are on in the config) and appends the findings here, so interview prep exists before it is needed. It runs once; re-running is a deliberate ask.

## File naming

Filenames reflect current status, never a date. Dates live only in the frontmatter (`date_spotted`, `date_researched`, `date_applied`). Only `/log-application` renames files, every time status crosses into a new bucket below. The weekly check re-syncs the prefix to the frontmatter `status:` if it was edited by hand.

| Status | Prefix | Files |
|---|---|---|
| shortlisted | *(none)* | No file yet. The first file appears at `researched` |
| researched · drafted | `3-` | `jobs/3-companyslug.md` · `jobs/3-companyslug-letter.html` |
| applied | `2-` | `jobs/2-companyslug.md` · `jobs/2-companyslug-letter.html` |
| screening · task | `1-` | `jobs/1-companyslug.md` · `jobs/1-companyslug-letter.html` |
| offer | `0-` | `jobs/0-companyslug.md` · `jobs/0-companyslug-letter.html` |
| rejected · ghosted · killed | `zz-` | `jobs/zz-companyslug.md` · `jobs/zz-companyslug-letter.html` |
| superseded files or folders | `DEPR-` | Prefix added so you can spot and delete them yourself. Never deleted automatically |

The `-letter` suffix always stays on the HTML file, whatever the prefix. If `custom_resume: true`, the resume file follows the same prefix and pattern: `jobs/<prefix>-companyslug-resume.html`.

---

# PART 1 · RESEARCH

*The agent fills this. You rarely need to read it, except before an interview.*

## 0. Read the job ad first

**Product area:** [the specific surface the ad is scoped to, not the whole platform]
**Top 2 asks:** [the two skills or problems the ad is actually selling for]

Used only to narrow where research looks next, never to decide what it is allowed to find. Reused later for `what_i_do` and, if `custom_resume` is true, for the resume bio header.

## The challenge

> [One sentence. Describe the screen or surface and what it costs. No verdict.]

**Source:** [Link to the exact page or screenshot this is built from. If you cannot link it, you have not verified it, and it does not go in the letter.]

**Quality test:** problem in my discipline ☐ · specific to them ☐ · I have receipts ☐ · survives competitive read ☐ · sourced to a real screen, not the job ad ☐

## 1. Product recon

- **Hardest moment or surface:**
- **Decision being made there:**
- **Where the product stops helping:**

**Video and interactive** · **Docs with real UI** · **Product pages** · **Dead ends** (one line each, saves the next pass)

## 2. Product and audience

**Buyer / Champion / Daily user / Blocker**, then:

**The divergence:** The buyer wants [X], the daily user wants [Y], and the product currently favours [Z].
**Confidence:** high / medium / guessing

## 3. Competitive brief

**Competitors** · **Real differentiator** · **Real gap** · **Winning on** product / distribution / neither · **Convention broken or missed**

## 4. Who reads this

**Hiring lead** [or "not findable in 4 min, greeting the team"] · **Team size** · **Recent hires** · **Public signals about the team**

## 5. Stage, pressure, culture

**Stage / round** · **Headcount trend** · **Recent move** · **The pressure** · **Culture signal** and how loud to be

## 6. Why them, honestly

- **The shape of the problem at their scale:**
- **Public signals about the team:** [never used to name a gap, only to calibrate]
- **Why this over their nearest competitor:** [one sentence that would be false if sent to a rival]

---

# PART 2 · LETTER COPY

**This is the part you edit.** Every field below maps to one slot in the HTML. Keep the word budgets, they keep it to one page. The field set and budgets come from `profile/letter-spec.md`. The block below is the structured format; for a classic letter keep only `opening`, `body_1`, `body_2`, `close`, `closing_line` (budgets 60 to 80, 90 to 120, 70 to 100, 40 to 60, under 10 words).

## Never

- Never open on a problem with their product
- Never name a gap in their team. Describe what you bring and let them connect it
- Never restate the job ad, never list tools, never "I'm passionate about"
- Zero em dashes
- **Never write a sentence that negates one framing then asserts a corrected one.** No "this isn't X, it's Y", no "not just X but Y", no "rather than X, Y". One occurrence fails the draft
- Never announce your method. The section labels already do that
- Every number must trace to a file in `profile/pillars/`. If it is not there, leave it out
- **Never source `opening` or `impact_card` from the job ad's language about where the company is heading.** That is the role's charter, not their product today. If you use it, say so explicitly ("the brief for this role is about X") rather than writing as if you observed it live. And check it does not fight the actual `challenge_setup`, which has to be sourced from something you can link, not the ad

---

### `impact_card` · 1 sentence
The only About-me card that changes per company. Names the shape of what you bring at their scale.
> [Example shape: Consolidating patterns across surfaces that grew up separately, so the fifth team does not solve the same problem a fifth way.]

### `what_i_do` · roughly the length of the base line
Base line: `identity.positioning_line`. Weave in 1 to 2 terms from Part 1's "Top 2 asks" without changing the sentence's length or rhythm, and without turning it into a restatement of the ad: this is a positioning line, not a keyword list. If nothing fits naturally, keep the base line.
>

### `opening` · 70 to 85 words
Names what you want, lands on them by sentence two, finishes on current work. **Must end positive.** No diagnosis.
>

### `bridge` · 35 to 45 words
Transition, the reason you did it, one human detail. Never announces method.
>

### `challenge_setup` · 45 to 55 words
The screen or surface, present tense, described not judged. This is the only place their product gets discussed at length. Must carry a Source line.
>

### `parallel_note` · 15 to 25 words
Only when the example is not from your current role. Say why, honestly. The admission is the credibility.
>

### `band_them` · 2 bullets
Observable facts about their situation. No adjectives, no verdict.
> -
> -

### `band_me` · 2 bullets
Mirror `band_them` line for line. Same structure, your situation.
> -
> -

### `resolution` · 45 to 60 words
**Past tense, your own work.** Zero conditionals: no "I'd", no "I would". The heading above this in the letter says "What I did about it", so it reports, it does not propose.

Three beats, in order:

1. **What you introduced or changed.** Name the artifact. A filter, a pattern, a narrative structure, a library, a rule about what does not get built.
2. **Where it went next.** One level above `band_me`. `band_me` is the specific build on the specific screen; this is the pattern it became and the other surfaces that took it. If the two could swap places unnoticed, zoom out further.
3. **What changed because of it.** A metric with its measurement method if one exists. If none exists, name what people did differently, concretely enough that someone could have watched it happen. "It improved alignment" is not a behaviour change. **Wrap this beat in `<strong>` tags** in the rendered HTML, so it is the one thing a skimming reader catches. It is the only bold in the letter.

Take the number from the chosen pillar's `Which numbers can close a resolution` section. Never borrow another pillar's metric to fill beat 3. The target company is not named in this field at all.

*Abstraction test: paste the sentence into another candidate's letter. If it survives, name the artifact again.*
>

### `hedge` · 1 line
Concede the outside view. Sits as a caption under the bands.
> [Example shape: Read from the outside, so I am probably missing the reasons.]

### `close` · 55 to 70 words
Concede their constraints, say what you would enjoy about their version of the problem, hand authority back. No conditions, no list of what you would interrogate.
>

### `closing_line` · under 10 words
Warm, no presumption of the job.
> [Example shape: I would like to hear the messy version.]

### `why_this_section` · optional, not written per company
The page 2 block explaining why a process-transparency section exists at all. Pull the agreed copy verbatim from `profile/voice.md` or `profile/bio-and-portfolio.md`; do not draft a new version per run. If the user has none, leave empty and the page is omitted.

---

## Level signals, check before you finish

At least two of these three need to be visible in the letter itself, not just true in the research:

1. **You shaped what got built, not only how it was built.**
2. **You made a decision that cost something.** A refusal, a thing you killed.
3. **Your work outlived your involvement.** A pattern others adopted after you left.

If the draft only has craft evidence, go back to `resolution` or `band_me` and surface one of the other two.

---

## Portal paste

Some portals only take plain text. Do not keep a separate plaintext file, it drifts. Assemble it from the fields above, in this order, blank line between each:

```
Dear [greeting],

[opening]

[bridge]

One challenge I worked through
[challenge_setup]
[parallel_note, if present]

At [company]: [band_them, joined into a sentence]
In my work: [band_me, joined the same way]
[hedge]

What I did about it
[resolution]

[close]

[closing_line]

[name from identity.md]
[base_city]
[email] · [portfolio link]
```

Drop the section labels if the field is under 2000 characters and the labels push it over. The letter still reads without them, which is the test of whether the copy is doing its job. For a classic letter, paste opening, body_1, body_2, close and closing_line in order.

---

## PART 3 · RESUME (optional, only if `custom_resume: true`)

Decided at Decision Card time, alongside the hook number, not after the fact.

### `resume_bio_header` · roughly the same length as the base bio
Base bio (what goes out by default, unchanged): the bio paragraph in `profile/identity.md`.

When `custom_resume` is true, rewrite this paragraph weaving in the same "Top 2 asks" from Part 1, Module 0, the same source `what_i_do` draws from. Keep the sentence count and rough length the same. **Everything else in the resume, every bullet, every number, every role, stays exactly as verified.** Only the bio header changes. This is about matching language a screening system scans for, not rewriting your history.
>

Render from `templates/resume-template.html` into `jobs/<prefix>-company-resume.html`, same folder and same prefix as the dossier and letter (see the File naming table above). It has its own export-to-PDF button, same pattern as the letter template.

---

## Pre-send checklist

- [ ] Company name swapped for "Acme", letter still makes sense? If yes, rewrite the opening
- [ ] Zero em dashes
- [ ] No negative parallelism
- [ ] Opening ends positive
- [ ] `resolution` is past tense, zero conditionals, and ends on a metric or a named behaviour change, wrapped in `<strong>`
- [ ] `resolution` sits a level above `band_me`, not a restatement of it
- [ ] `impact_card` is specific to this company
- [ ] Every number traces to a pillar file
- [ ] At least two of the three level signals are visible in the letter
- [ ] I made at least three edits in my own words
- [ ] Printed it, and it fits

---

## Challenge prep

*Filled by `/challenge-prep` (and auto-run once when status first becomes `screening`, if the module is on).*

## Record

| Date | What happened |
|---|---|

---

**Backlinks:** [00-START-HERE.md](../00-START-HERE.md) · [Applications-Tracker.md](../Applications-Tracker.md)
