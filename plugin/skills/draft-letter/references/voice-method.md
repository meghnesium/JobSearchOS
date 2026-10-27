# Voice method

This file contains no personal style. It explains how to apply the user's own voice files. The user's voice lives in `profile/voice.md` and in `profile/pillars/*.md`. The universal rules live in `${CLAUDE_PLUGIN_ROOT}/skills/_shared/universal-style.md`.

## Order of authority

1. Universal rules (`_shared/universal-style.md`): absolute. One violation fails the draft.
2. `profile/voice.md`: adds to the universal lists and sets personality, temperature and phrase bank. If it contradicts a universal hard rule, the universal rule wins and you tell the user in one line.
3. Pillar files: the only source of facts and numbers.
4. This file: how to combine them.

## How to apply `profile/voice.md`

- **Personality.** Read it as a description of how the user sounds in person. Match sentence length, formality and humour level. Where the file is vague, default to plain, direct, mildly dry.
- **Default temperature.** `measured` or `bold` as stated. Apply per `universal-style.md` (Temperature) and let the ad's culture signal override only when the evidence is clear (a manifesto careers page pushes bold; a regulated enterprise pushes measured).
- **Banned words and phrases.** Add the user's lists to universal rules 3 to 5. Scan the finished copy against both.
- **Phrase bank.** Phrases the user actually says. Use at most one or two per letter, only where they fit naturally. Never paste a bank phrase to fill space. Never reuse the same bank phrase in consecutive letters if the tracker shows it was already sent.
- **Honesty moves.** The ways the user admits limits (a caveat on a number, a concession in the hedge, a parenthetical). Use at least one per letter. These are the credibility core.
- **Closing warmth.** How warm the final line is. Never presume the job.
- **Rules for referencing work.** Follow them literally (for example, which projects may be named, which links may be shown).
- **Level policy.** Read `level_policy` from `jobsearchos.config.md` and any extra rule in the file.

## How to apply `profile/pillars/*.md`

A pillar is one proof project. For each letter:

1. Choose the pillar with `routing.md` (company size and type). Skip pillars with `status: do-not-use-yet`.
2. From the pillar, take:
   - a number from `Numbers (all defensible)`, with its measurement method and caveat,
   - the decision from `The hardest call` (this is the "cost something" signal),
   - the pattern from `The systems insight` (this is the zoom-out beat),
   - what carried on after the user left, from `Outlived my involvement` (the "outlived me" signal),
   - the admission from `Honest limit` (used as the caveat or as the answer to the screening-call gap),
   - one line from `Best lines` if it fits; never more than one, and rephrase it if it echoes a recent letter.
3. Take no fact from anywhere else. If the pillar does not hold what the letter needs, write the beat without it, or pick the other pillar.

## Blank-style guidance (when the user's voice file is thin)

If `profile/voice.md` is empty or generic, do not invent a voice. Write plainly:

- One idea per sentence. Concrete nouns.
- First person, contractions, no decoration.
- State the claim, then the number, then the caveat.
- One honest admission per letter.
- Then tell the user in one line that the voice file is thin and that a few of their own sentences pasted into `profile/voice.md` will sharpen every later letter.

## Calibration pass before showing a draft

1. Read the draft aloud in your head as the user would speak it. Anything the user would never say is a model sentence: cut or rewrite it.
2. Scan for the universal patterns, most often the negate-then-reframe one, which hides in "While...", "Sure...", "Less...more..." and "Rather than...".
3. Check that each paragraph contains a noun only this user could have written (the abstraction test).
4. Check the caveat is attached to each number.
5. Ask the user to make at least three edits in their own words before sending. Edits in the user's own words are the last and best voice calibration.
