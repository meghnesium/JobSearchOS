# Friday filename check on ChatGPT

ChatGPT cannot rename your files. Use the local script (`../scripts/sync-filenames.py`, scheduled with `../scripts/schedule-weekly.md`). It renames files for you, needs no AI, and costs nothing.

If you also want a ChatGPT nudge, create this Task for Friday afternoon. It reminds you and checks a listing you paste.

## Prompt

```
Every Friday, ask me to paste the output of listing my jobs folder (file names only) and, if I like, the status line from each dossier. When I reply, check each company's file prefix against its status: researched or drafted = 3-, applied = 2-, screening or task = 1-, offer = 0-, rejected, ghosted or killed = zz-. Report mismatches one per line as "old name -> new name (status)". If everything matches say so in one line. Skip _TEMPLATE.md and anything starting with DEPR-. Do not ask anything else.
```
