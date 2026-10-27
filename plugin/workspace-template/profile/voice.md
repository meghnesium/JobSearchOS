---
tone_words: ["[word]", "[word]", "[word]"]
default_temperature: measured-plus-one-bold   # measured | bold | measured-plus-one-bold
level_policy: never-name                      # never-name | name-when-asked
attach_caveats: always                        # always | when-asked
---

# Voice

The universal writing rules (no em dashes, no negate-then-reframe constructions, banned AI words and cover-letter cliches) live in the plugin and always apply. This file adds yours.

## Personality

[Two or three sentences: how you sound when you are at your best. Written by you or confirmed by you.]

## Temperature

| | Bold | Measured |
|---|---|---|
| Opening move | Name the friction you found, directly | Name the decision their user is making, then the friction |
| Stance | State the take, no hedge | State the take, then the evidence that earns it |
| Numbers | One number, thrown in casually | Two numbers, with the caveat attached |
| Closing | An offer to argue about it | An offer to walk through the work |

Default is measured plus exactly one bold sentence. Full bold is a choice made on evidence, not mood.

## Banned words and phrases (adds to the universal list)

- [Your pet peeve]
- [Your pet peeve]

## Phrase bank (yours, pulled from your own writing, vary them)

**Framing your work:**
- [phrase]

**Honesty moves:**
- "Worth saying:"
- [phrase]

**Closing warmth:**
- [phrase]

## Sentence habits

[Short paragraphs or long, contractions yes or no, parentheses, openers like "And" or "But". Extracted from a writing sample and confirmed by you.]

## Referencing your work

1. Lead with the decision, not the outcome. Outcomes sound like a CV, decisions sound like a person.
2. Name the thing you refused to do. Nobody fakes a refusal.
3. Attach the caveat yourself, before anyone asks. It is the strongest credibility move.

## Page 2 of the structured letter (optional process transparency)

Same text on every letter. Delete `why_this_section` (leave it empty) to drop page 2 and send a one-page letter.

why_this_section: "[Two honest sentences on how you use AI and where your judgment sits.]"
disclosure: "[One line at the top of page 2, for example: This page describes how this letter was made.]"
process_heading: "[Short heading, for example: A person decided every line of this letter.]"
process_lede: "[One sentence introducing the cards.]"

process_cards:
  1. Research | automated | AI | "[What the AI did: read the ad and public pages, drafted a first read.]"
  2. Choice | human | me | "[What you decided: which project, which challenge, what to cut.]"
  3. Drafting | hybrid | AI and me | "[How the draft was produced and refined.]"
  4. Editing and sending | human | me | "[What you checked before sending.]"
