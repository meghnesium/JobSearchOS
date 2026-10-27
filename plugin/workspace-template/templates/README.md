# Templates

Your branded letter and resume templates. `/setup` generated them from your design settings (`profile/brand.md`). Skills fill them for each job; you never edit a finished letter's HTML by hand (edit the dossier, then regenerate).

| Template | Used for | Per-job output name |
|---|---|---|
| `letter-template.html` | Structured letter (challenge, them-versus-me bands, resolution, optional page 2) | `3-companyslug-letter.html` |
| `letter-template-classic.html` | Classic letter (opening, two body paragraphs, close) | `3-companyslug-letter.html` |
| `resume-template.html` | Optional tailored resume. Only the bio header changes per job | `3-companyslug-resume.html` |

## Naming

The templates themselves keep fixed names because they are not jobs. Every file made from them follows the filing structure: the status prefix, then the company slug, then the suffix (`-letter.html` or `-resume.html`), with no dates. The prefix changes as the job moves (`3-` drafted, `2-` applied, `1-` screening, `0-` offer, `zz-` closed), and `/log-application` renames the dossier, letter and resume together.

## Export PDF

Every letter and resume has an Export PDF button (bottom right on screen). Open the HTML in a browser, press it, and choose Save as PDF. The layout is built in millimetres and points, so the PDF matches the page you see. The button hides itself when printing. If page 1 of a structured letter spills over, lower `--pz` in the `:root` block by 0.01 at a time (.97, then .95).

## Change the look

Edit `profile/brand.md` (or use `tools/brand-picker.html`), then ask `/setup` to "regenerate templates". Only the `:root{...}` colour and font values and the fonts link change.
