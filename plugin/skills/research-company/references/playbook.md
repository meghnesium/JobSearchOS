# Research playbook

30 minutes. Timer on. One file per job.

You are looking for **one challenge** you can say something real about, backed by enough product and market context that the claim holds up in a first call. Everything else is diligence theatre.

## The clock

| Time | Module | Stop when |
|---|---|---|
| 0:00 - 5:00 | Product recon | 3 to 6 verified links, 1 named friction |
| 5:00 - 11:00 | Product and audience | You can name who pays, who uses, and where those two disagree |
| 11:00 - 16:00 | Competitive brief | You know their one real differentiator and their one real gap |
| 16:00 - 20:00 | Who reads this | You know the hiring lead and what they care about |
| 20:00 - 23:00 | Stage and pressure | You know what they are measured on this quarter |
| 23:00 - 25:00 | Culture signal | You know how loud to be |
| 25:00 - 30:00 | The Squeeze | One sentence that survives the quality test |

Two modules have their own method files: `product-audience.md` and `competitive-brief.md` in this folder. Hard rule: when a module's time is up, move on with whatever you have. An incomplete module is fine. A 50-minute session is not.

## 1. Product recon (5 min)

Collect links, not screenshots. Ninety seconds of someone driving the product tells you more than two stills, and a link you can reopen before an interview beats an image you have to find again.

Hunt in this order:

1. Video of someone using it (official channel, demo page, conference talk, partner walkthrough). Note the timestamp.
2. Docs pages with real screenshots. Troubleshooting pages name failure modes in the company's own words.
3. Product pages with interface imagery or an autoplay loop.
4. A free trial, if it opens in under 2 minutes.
5. 3-star reviews on G2 or Capterra. Not the product, the friction.

Verify every link resolves. A dead link in a dossier is worse than none.

Then answer three questions, which is the point of the module:

- What is the **hardest moment** in the product? The one where a user holds several things in their head at once.
- What decision is made there, and what does getting it wrong cost?
- Where does the product stop helping? Name the specific element.

### The sharpening list

Rank your links and mark the **top 3 as sharpening links**, 15 minutes total at most. They are not a gate. They exist for two moments: when a draft reads thin, and before an interview. A rule that makes you do homework before you may send stops you applying, which costs more than a slightly thinner letter. Annotate each: what it shows and why it matters for this challenge.

If the product is genuinely invisible, say so in the dossier, drop to docs plus 3-star reviews, and note it under `Confidence`.

## 2. Product and audience (6 min)

See `product-audience.md`. Separate the buyer from the user, find where their interests diverge, and locate the work in that gap. This module is what makes a letter read as product thinking. Protect its 6 minutes.

## 3. Competitive brief (5 min)

See `competitive-brief.md`. Three competitors, one differentiator, one gap, and a read on product versus distribution. You are finding out whether the challenge you are about to name is one they are already losing on.

## 4. Who reads this (4 min)

Four facts. If the hiring lead is not findable in 4 minutes, stop looking, greet the team, and move on.

- Who leads this function (title, tenure, where they came from)
- Team size
- Who joined in the last 6 months, and from where
- What the lead posts about, if anything

Why it matters: a 3-person team at a seed-stage company wants someone who owns a surface end to end. A 30-person team at a large company wants someone who will not break the system. The same letter fails one of them. Match the pillar to the lead's background where `routing.md` allows it.

## 5. Stage and pressure (3 min)

- Funding stage and last round date
- Headcount trend
- Any launch, pivot, or market move in the last 6 months

Convert it into pressure. A round nine months ago means building toward the next round's metrics. A new market launch means localisation and trust. Flat headcount after a big round means caution. Pressure is what the hook speaks to.

## 6. Culture signal (2 min)

Employee reviews, their blog, any conference talk, any team member's public writing. You want one thing: **how loud can you be.**

- Opinionated public posts, ships in public, lead argues online: **bold**
- Corporate site, no writing, formal ad, regulated industry: **measured**
- In between: measured with one bold sentence

Log the signal, not the vibe. "Their lead published a post arguing against design systems" is a signal. "Seems like a cool culture" is nothing.

## 7. The Squeeze (5 min)

**Hard stop.** At 25:00 you stop researching and write the sentence with what you have.

> **The challenge:** ___________
> **Source:** ___________

### Quality test

Passes only if all five are true. The fifth is the cheapest to fail on and the one that matters most.

1. **A problem in the craft, not a business problem.** "They need more enterprise customers" fails. "Their admin console asks a procurement lead to understand the permissions model before they can evaluate it" passes. For non-design roles, read "craft" as the role's own domain: a product bet, an architecture constraint, a funnel leak.
2. **Specific to them.** If the sentence could be pasted into another company's letter, it fails. Names, screens, flows.
3. **You have receipts.** A pillar file shows something the user actually did that speaks to it. If the best available is "I am interested in this," pick a different challenge.
4. **It survives the competitive read.** If a rival already solved it and they know it, you are telling them something they hear weekly. If nobody solved it, say so; it is the most interesting sentence you can write.
5. **You can link it.** One page or one screenshot, not a claim stitched from two. If you cannot point to the exact thing, you inferred it. Prefer the simpler challenge you can show over the more interesting one you cannot.

### If nothing passes

- **Reframe smaller.** From "their whole information architecture is confused" to "their settings page carries four unrelated jobs."
- **Kill the application.** No honest challenge in 30 minutes means the letter will be generic, and a generic letter is worse than none. Set status `killed` and move on. Killing applications is how the system stays fast.

## Output: one file per job

`jobs/<prefix>-<companyslug>.md`, prefix from the status table (`3-` at researched or drafted). Never a date in the filename; dates live in frontmatter. Everything for the application lives in that one file: research, both analyses, ammunition, letter drafts, and the record. The structure is `<workspace>/jobs/_TEMPLATE.md`.

## Batching note

Research three companies back to back in one 90-minute session. Do not write letters in the same session. Research brain and writing brain are different, and switching between them is where the hours go.
