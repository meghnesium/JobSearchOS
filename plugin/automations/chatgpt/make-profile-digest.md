# Make your profile digest (for the ChatGPT scheduled Task)

ChatGPT scheduled tasks cannot read Project files, so the sweep prompt must carry your profile itself. Run this once in your Project, then again whenever your profile changes.

## Prompt

```
Read my uploaded profile files (identity, pillars, routing, targets, voice, letter spec). Produce one compact "profile digest" of 600 to 900 words that a fresh chat with no files could use to run my job sweep and draft letters. Use exactly these headings and keep every fact traceable to my files. Do not invent anything.

IDENTITY: name, target titles, base city, positioning line, seniority policy.
FIT TESTS: my four fit tests, size min and max, titles to accept and exclude, industries to avoid.
LOCATION RULES: the table as lines, "place or setup = flag" (none, check-entity, blocker).
SOURCES AND WATCHLIST: the job sources and watchlist companies.
PILLARS: for each ready pillar, 5 lines: when to use it, one-line claim, the usable numbers each with method and caveat, the hardest call, the honest limit.
ROUTING: which pillar for which company size or type.
VOICE: tone words, default temperature, banned words I added, three phrases that are genuinely mine, caveat policy.
LETTER SPEC: the format and the word budget per field.
BRAND: the colour values (paper, ink, mute, line, accent, card), the display and body font names, and the paper size, so the letter HTML can be styled.
```
