# Letter framework

Why the structured letter is shaped the way it is. The copy spec itself lives in Part 2 of `<workspace>/jobs/_TEMPLATE.md` and in `profile/letter-spec.md`. This file explains the reasoning, which the spec has no room for. Read it only when unsure why a field is shaped as it is.

## The page, top to bottom (structured format)

| Block | What it does |
|---|---|
| Masthead | Name, role title, links, base city |
| Apply row | Role and company, date right-aligned |
| **About me**, 3 cards | Carries the user's background so the letter does not have to |
| **The letter**, 2 paragraphs | Why the user is here, and a handoff |
| **One challenge I worked through** | The only place their product gets discussed |
| The two bands | Their situation, then the user's, mirrored |
| **What I did about it** | What the user introduced, where it spread, what changed. Past tense |
| Close and sign | Concede, invite, hand authority back |

Page 2 is an optional process-transparency page. When it is used, the letter is exactly two pages; when it is omitted, exactly one.

## Why the order matters

**The cards come first so the letter can be short.** Once the user's years, domain and current role sit in a card, the letter has no job introducing them. If the draft says "I'm a [title] with..." it duplicates a card.

**The letter never diagnoses.** `opening` names what the user is looking for, lands on the company by sentence two, and finishes on current work. It ends positive, on an outcome, not a problem. A stranger who opens with what is wrong with the product has said they are auditing, not applying.

**The observation moves into a labelled section, after the letter.** By the time a reader reaches "One challenge I worked through", the letter has already established why the user is there. The same sentence that reads as arrogance in paragraph one reads as curiosity in a section that announces itself as a worked example. That placement is the most load-bearing decision in the system.

**The bands mirror line for line.** Two bullets about their situation, two about the user's, same structure. The reader draws the parallel. Write the parallel out and you have explained your own joke.

**`resolution` is what the user did, not what they would do.** The heading says "What I did about it". Written as "At [their company], I'd...", the one section that should carry evidence becomes a proposal from a stranger. A hiring manager can argue with a proposal. They cannot argue with something that already happened.

So: past tense, the user's own work, three beats.

1. **What the user introduced or changed.** A named thing: a filter, a pattern, a narrative structure, a library, a rule about what does not get built.
2. **Where it went after that.** This is the senior-level beat, and why the field sits one level above `band_me`. `band_me` is the specific build on the specific screen. `resolution` is the pattern that build became and the other surfaces that picked it up. If the two fields could swap places unnoticed, zoom out further.
3. **What changed because of it.** A metric with its measurement method if one exists. If not, name what people did differently, concretely enough that someone could have watched it happen. "Regional managers adopted it for their own sites unprompted and shared it upward, no second build" is a behaviour change. "It improved alignment" is not. Wrap this beat in `<strong>`; it is the only bold in the letter. Never borrow a metric from another pillar to satisfy it.

**The abstraction trap.** Zooming out invites sentences like "I brought systems thinking to a fragmented platform". Paste the sentence into another candidate's letter. If it survives, delete it and name the artifact again.

**`close` concedes and hands back.** No conditions, no list of things the user would want to interrogate, nothing that reads as terms. The ask is a conversation, not terms for one.

## Tone, one letter calibrated

There are no A/B variants. One letter per company, tone set by the culture signal from the research. See `_shared/universal-style.md` (Temperature) for measured, bold and default. Record the choice in the dossier `tone` field so the reply-rate table in `Applications-Tracker.md` can show which tone works after ten sends.

## The Never list

- Never open on a problem with their product
- Never name a gap in their team
- Never restate the job ad, never list tools, never "I'm passionate about"
- Zero em dashes
- Never write a sentence that negates one framing then asserts a corrected one
- Never announce the method; the section labels already do that
- Never source `opening` or `impact_card` from the ad's language about where the company is heading. That is the role's charter, not their product today. If used, say explicitly that it comes from the brief for the role.

## Classic format

The classic letter drops the cards, the challenge section and the bands. `opening` names what the user wants and lands on the company by sentence two. `body_1` carries the strongest pillar story with its number and caveat. `body_2` carries the cross-functional or ambiguity beat. `close` concedes and hands back. The Never list, the number discipline and the Acme test apply unchanged.
