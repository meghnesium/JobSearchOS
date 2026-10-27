---
name: product-audience
description: Analyse a company's product to separate buyer from daily user from blocker. Use when the user says "/product-audience [company]", "who are their users", "analyse their audience", or wants to go deeper before an interview. Also auto-triggered when status first moves to screening.
---

# Product and audience analysis

One question: who pays, who uses, and where do those two disagree? In B2B the gap between buyer and daily user is where most of the work lives.

## Before anything

Read `<workspace>/jobsearchos.config.md`. If `modules.product_audience` is false, say so in one line and stop. Use `models.search` for gathering and `models.writing` for the divergence sentence. If the session is on Opus, say so in one line and continue. Read the existing dossier in `<workspace>/jobs/` first (match on company slug, any prefix); do not search for what it already holds.

Full method, source hierarchy and skip conditions: `${CLAUDE_PLUGIN_ROOT}/skills/product-audience/references/method.md`.

## When this runs standalone

Budget 15 to 20 minutes. Go deeper on reviews and docs than the fast version in research-company. Use when:

- The user asks for a deeper audience analysis
- The dossier `Confidence` says `guessing` and should be fixed
- The audience structure is the whole point of the role
- Status first moved to `screening` (auto-triggered by `/log-application`)

## Procedure

1. Fill the four cells: buyer, champion, daily user, blocker. One line each. Mark every guess.
2. Name the one primary job: when [trigger], [user] wants to [action], so they can [outcome]. One job only.
3. Write the divergence: the buyer wants X, the daily user wants Y, and the product currently favours Z.
4. Point at where that divergence shows up in the product: a named screen or element, with a link.
5. Set confidence: high, medium, or guessing.
6. If the user's `profile/pillars/` hold a pillar that speaks to the neglected side, name its slug in one line. Do not copy numbers here.

## Output

Write the findings into the dossier's research section (structure in `<workspace>/jobs/_TEMPLATE.md`) and set frontmatter `interview_prep_audience: completed`. Edit contents only; never rename files (that belongs to `/log-application`).

Report: "Audience analysis complete. [one-line buyer and user divergence]."
