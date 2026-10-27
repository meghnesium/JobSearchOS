---
name: warm-intro
description: Find the two or three people at a company worth messaging and draft the outreach in the user's voice. Use when the user says "/warm-intro [company]", "who should I message at [company]", "find me a way in", "warm intro", or right after a letter is drafted and they want the application to land in front of a human. Also use when they applied somewhere and heard nothing for a week.
---

# Warm intro

A cold application goes into a queue that is often screened by software before a human reads it. A message to the right person skips the queue. This skill finds that person and drafts the message.

Run it alongside `fast-letter`, not instead of it. The letter is the artifact; this is what makes someone open it.

## Before anything

1. Read `<workspace>/jobsearchos.config.md`. If `modules.warm_intro` is false, say so in one line and stop.
2. Read `<workspace>/profile/identity.md` (role, positioning line, base city, links), `profile/voice.md` (voice, banned words, phrase bank), `profile/routing.md` and the pillar file for this company, and the company's dossier in `<workspace>/jobs/` if it exists. If your tool cannot read files, ask the user to paste them.
3. Models: `models.search` for finding people, `models.writing` for the messages. If the session is on Opus, say so in one line and continue. Two searches, ceiling of four. If you cannot find a named human in four, say so and use the fallback at the end.

## Who to look for, in priority order

1. **The hiring manager.** The head of the function the role sits in, or for a small company the founder or a product lead. Highest value, hardest to find.
2. **Someone already doing the job on the team.** Easier to reach. They know whether the role is real and what the actual problem is, and often get a referral bonus.
3. **A shared-context person.** Real overlap with the user, from `identity.md` and the pillar files: a former employer, a school, a city or relocation path, a community, or someone who wrote publicly about the exact problem the role is about. A shared-context person with no hiring power still beats nobody, because they can forward the note.

**Never message a recruiter first** unless they posted the role themselves. Recruiters route you back into the queue this skill exists to skip.

## Find them

Two searches, run together (replace the function with the role's function):

```
"[Company]" "head of [function]" OR "director of [function]" OR "lead [function]" linkedin
"[Company]" [role title] linkedin [base city] OR remote
```

Then check the company site, blog author bylines, conference talk pages, and engineering or design blogs. Bylines are the most reliable source of real names that LinkedIn search misses.

**Verify the person still works there** before drafting. A note to someone who left eight months ago is worse than none. If you cannot confirm, mark them `unverified`.

If the tool has browser access and the user is signed in to LinkedIn, you may look at profiles. **Never send anything. Never connect, never message, never click a button that acts for the user.** You draft; the user sends. No exceptions.

## What to write

Three formats per person, because the user does not yet know which channel will be open.

### Connection note

**300 characters hard, and count them.** Include the count so the user can see it fits. LinkedIn Premium InMail is an optional extra if the user has it and no connection is possible; do not assume it. If over, cut, do not abbreviate.

Structure: one line of specific reason you are writing to *them*, one line of what the user does, one line of ask. No compliment on the company. No "I'd love to connect".

### Message or email, 90 to 120 words

Same three moves, more room. Add one concrete number from the pillar files (only one, only if it carries a measurement method there) and one honest question about their product that only someone who looked would ask. The question is the point; it proves attention in a way a compliment cannot.

End with an ask that costs them under two minutes: "worth a 15-minute call?" or "is this role actually about X, or about Y?" Never "can you refer me".

### Follow-up, one time only, seven days later, under 50 words

One new piece of information, then the same ask. If unanswered, stop. Two messages is persistence, three is a problem.

## Voice

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md` and the user's `voice.md` (their banned list adds to the universal one). In short: zero em dashes, zero negate-then-reframe constructions, no dead AI words or letter cliches, contractions, active voice, short sentences, a stance, and the caveat attached by the user. Never flatter the company. Never restate its about page. Facts about the user come only from `identity.md`, the pillar files and `bio-and-portfolio.md`, and respect its "never claim" list. If `level_policy` is `never-name`, do not state seniority in the messages.

## Output

One screen per person. No preamble.

```
**[Name] · [Title] · [verified / unverified]**
Why them: [one line]
LinkedIn: [url]

*Connection note ([n] chars)*
[text]

*Message, [n] words*
[text]

*Follow-up, day 7*
[text]
```

Two people minimum, three maximum. Then one line: who to message first and why. Nothing else.

## Log it

Record who the user is messaging and the date in the company's dossier (frontmatter `outreach` list or the Record table, per `<workspace>/jobs/_TEMPLATE.md`), so the day-7 follow-up has something to fire against. Do not edit `Applications-Tracker.md` directly; it is rebuilt from frontmatter. If the workspace is unreachable, say so in one line and continue.

## When you find nobody

Say so in one line, then give the fallback: a note to the company's careers or team email, or a comment on a recent post by someone there. Both are long shots. Write the strongest version and mark it as such so the user can decide if it is worth five minutes.
