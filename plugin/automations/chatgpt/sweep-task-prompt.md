# ChatGPT scheduled Task: overnight sweep

Create it under Scheduled (or ask in a chat to schedule it). Suggested: Monday to Thursday, early morning in your time zone. Paid plans can pick exact times. Turn on push or email. The prompt is self-contained because tasks cannot read Project files. Replace the digest placeholder with the block from `make-profile-digest.md`.

## Prompt

```
Run my overnight job sweep. You have no memory of earlier chats and no files, so everything you need is below. Be decisive: do not ask me questions, state your assumption and continue. Do not send anything to anyone.

PROFILE DIGEST
[PASTE YOUR PROFILE DIGEST HERE]

LETTER HTML TEMPLATE
[PASTE THE CONTENTS OF letter-skeleton.html HERE. Its :root colours and fonts must be set to the BRAND values in the digest.]

PROCEDURE
1. Source (about 40 searches maximum). Start from the listing pages and saved searches in SOURCES AND WATCHLIST, not open-ended search. Run two legs: roles in places that are fine under LOCATION RULES, and fully remote roles I could take from home. Roles posted in the last 10 days. Open each link and confirm the role is still live before spending time on it.
2. Filter. A company qualifies if at least three FIT TESTS are true. Apply size, titles, industry and dealbreaker rules. Apply LOCATION RULES strictly: any "blocker" goes at the very top of your summary in bold, never dropped quietly.
3. Rank. Take the best 3 (fewer if fewer qualify, never pad). Rank by fit, not prestige.
4. Research each (25 minutes of effort maximum). Read the ad first: product area and top 2 asks. Find product docs, buyer versus daily user, a brief competitive read, who leads the team (give up after 4 minutes), size and stage. Write ONE challenge sentence with a Source line (the exact page it is built from). Test it: real problem not a business problem; breaks if pasted into another company's letter; I have receipts in the routed pillar; survives the competitive read; sourced to a real page not the ad. If it fails any check, recommend killing that application and say why.
5. Route a pillar by company size and type using ROUTING. Every number must come from PILLARS with its caveat.
6. Draft per company: a dossier in markdown (research, challenge, pillar choice, gaps), the letter copy, following LETTER SPEC word budgets and VOICE. Rules: zero em dashes; never negate one framing then assert a corrected one; no dead AI words or cover-letter cliches; never open on a problem with their product; never name a gap in their team; never restate the ad; attach the caveat to every number. Run the Acme test.

For each company that passes, also produce the finished letter as ONE complete, self-contained HTML file: fill every placeholder in the LETTER HTML TEMPLATE (OPENING, BODY_1, BODY_2, CLOSE and so on) from the letter copy, keep the Export PDF button, and put it in its own code block labelled with the file name 3-companyslug-letter.html so I can save it and open it in a browser. For a company you recommend killing, write only a short dossier named zz-companyslug.md.

DELIVER one message: for each candidate, company, role, size, location and flag, job link, the challenge in one line with its Source, the pillar and why, the word count of each letter field against budget, the field you are least sure about, and any you recommend killing. Then, for each company that passes, the dossier named 3-companyslug.md and the letter named 3-companyslug-letter.html. If nothing qualifies, say the market was quiet. Under 120 words of commentary outside the drafts.
```
