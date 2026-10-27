---
name: challenge-prep
description: Generate a realistic live challenge for a company and role (design challenge, product case, take-home, system design, campaign brief) and critique the user's approach against how interviewers score it. Use when the user says "/challenge-prep [company]", "I have an interview at", "give me a practice challenge", "whiteboard prep", "take-home prep", "case prep", or when status first moves to screening. Auto-triggered by /log-application at that transition when the module is on.
---

# Role challenge prep

First rounds increasingly skip the portfolio walkthrough and go to a timeboxed live problem, often 25 to 45 minutes, or a take-home. The application gets the user into the room. This is what happens in it.

Three modes: generate the likely challenge, rehearse it live, debrief. Usually back to back.

## Before anything

1. Read `<workspace>/jobsearchos.config.md`. If `modules.challenge_prep` is false, say so in one line and stop.
2. Read `<workspace>/profile/identity.md` for `role_title`, `seniority` and `target_titles`. The format and scoring adapt to that role. If your tool cannot read files, ask the user to paste it.
3. Models: `models.search` for recon, `models.deep` for writing the challenge and the critique. If the session is on Opus, say so in one line and continue. One search, ceiling of two. If a dossier for this company exists in `<workspace>/jobs/` (match on slug, any prefix), read it instead of searching: the research is already done.

## Mode 1: generate the challenge

### Recon, five minutes at most

Use the dossier if it exists. Otherwise one search: what the product does, who pays, what surface or area the role owns.

### Pick the format they will actually use

Default for design roles (product design, UX, research, design systems):

| Signal | Likely format |
|---|---|
| Enterprise, complex domain, exec or data product | App critique, then a redesign of one flow |
| Scaleup, multiple surfaces, systems language in the ad | Consolidate a pattern that has drifted across surfaces |
| Early stage, "our first hire", founder interviewing | Zero-to-one: design the core loop from a problem statement |
| Ad mentions AI, agents, or copilots | Design a surface where the system is sometimes wrong |
| Ad is vague or generalist | Product thinking: pick a metric, propose three ways to move it |

For other roles, adapt the same logic to `role_title`:

| Role family | Typical formats |
|---|---|
| Product management | Product sense (improve or design a product for a user), execution (a metric dropped, diagnose it), strategy (enter a market or prioritise a roadmap), written take-home PRD |
| Engineering | System design for the company's core workload, debugging or code review of a realistic snippet, take-home service with a written trade-offs note |
| Marketing and growth | Campaign brief with a budget and a channel constraint, funnel diagnosis from a data extract, positioning for a launch |
| Data and analytics | Messy-dataset analysis with a stakeholder question, metric definition, experiment design |
| Sales, customer success, operations | Mock discovery call, account plan, process redesign case |
| Anything else | Use the ad's own verbs: what they hire you to do is what they will test |

Give the user the one you judge most likely and name the runner-up in one line so they are not blindsided. State whether it is likely live or take-home, since rehearsal differs (see Mode 2).

### Write the brief the way an interviewer would say it

Deliberately underspecified. Real briefs are two or three sentences with a constraint attached, not a spec. A clear brief removes the thing being tested.

```
**[Company] · likely format: [name]** · runner-up: [name]

*The brief, as they'd say it out loud*
"[two or three sentences. A user or stakeholder, a situation, a constraint. No success criteria, no scope.]"

*Timebox:* [25 / 45] minutes, or [take-home: hours and deliverable]
*What they're scoring:* [three things, one line each]
*The trap:* [the specific wrong turn this brief invites]
```

Then stop. Do not solve it. Do not hint.

## Mode 2: rehearse

Live format: the user answers out loud or in writing; you play the interviewer. Interrupt once with a realistic constraint change ("the data refreshes weekly, not live"), answer clarifying questions briefly and in character, and keep time. Do not coach during the attempt.

Take-home format: the user shares the deliverable or an outline. You review it as a hiring panel would skim it: in five minutes, looking for the decision, the trade-off and the caveat.

## Mode 3: debrief

The user describes what they did, pastes notes, or shares a screenshot. Score in this order. These six hold for every role; wording of the first one flexes.

1. **Reframe before solving.** The most common failure at senior level is solving the brief as stated. Strong candidates spend the first minutes naming the user or stakeholder, the decision at stake, and what success looks like, and say the assumption aloud so it can be corrected.
2. **Narrowed on purpose.** Named what they are not doing, and why, early. Scope creep in a timeboxed challenge reads as poor judgment.
3. **Showed the trade-off.** What was tried, rejected, and what it cost. A decision with no cost does not read as a decision.
4. **Stayed legible while thinking.** Narrating, sketching roughly, checking in. Four minutes of silence loses the room.
5. **Landed something.** One concrete direction with a next step, not three options handed back. Handing back options reads as avoiding the call.
6. **Attached the caveat.** "This assumes the data refreshes daily, which I would check." Often the strongest move, and it works better live than on paper.

Where `profile/voice.md` or the pillar files show the user's own habits (for example a signature trade-off story), name which pillar story fits the trade-off point. Do not invent one.

### Deliver the critique

Direct, specific, no sandwiching. The user needs the two things that would have changed the outcome.

```
**Scored**
Reframe: [strong / thin / missed] · [one line]
Narrowing: [...]
Trade-off: [...]
Legibility: [...]
Landing: [...]
Caveat: [...]

**The two things that would have changed the outcome**
1. [specific, with the sentence they should have said]
2. [same]

**One line to keep:** [something they actually said that was good, quoted back]
```

## Reusable openers

These cost nothing and buy the first three minutes. Adapt wording to the user's voice.

- "Before I start, let me say back what I think you're asking, so you can stop me if I've got it wrong."
- "Who is the user here, and what decision are they trying to make?"
- "I'm going to leave [X] out and focus on [Y], because [reason]. Tell me if that's the wrong half."
- "I'm assuming [thing]. If that's not true, this changes."
- "Here's what I'd cut, and what it costs."
- "That's where I'd stop for now. Next I'd want [X], and I'd get it by [method]."

## Where to record it

Append a `## Challenge prep` section to the company's dossier in `<workspace>/jobs/` (structure in `<workspace>/jobs/_TEMPLATE.md`): the brief, the attempt in one paragraph, the two fixes. Set frontmatter `interview_prep_challenge: completed`. If no dossier exists, create `jobs/1-<companyslug>.md` from the template with just that section (prefix `1-`, since reaching this skill implies `screening`). Never rename existing files; that belongs to `/log-application`.
