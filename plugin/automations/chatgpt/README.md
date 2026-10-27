# JobSearchOS on ChatGPT (and other non-Claude tools)

Everything in this package is plain markdown, so it works anywhere. What changes is the automation. Claude can run scheduled tasks that read your folder and write files. ChatGPT scheduled tasks are more limited, so this pack uses three pieces that fit what ChatGPT can do.

| Job | Claude setup | ChatGPT setup |
|---|---|---|
| Interactive work (`/setup`, `/fast-letter`, intros) | Plugin with slash commands | A **Project** with your profile files and instructions |
| Overnight sweep | Scheduled task reads your folder, writes dossiers | A **scheduled Task** with a self-contained prompt. Results arrive in chat. You save the files. |
| Friday filename check | Scheduled task renames files | The local script `sync-filenames.py` renames files. Optional ChatGPT Task reminds you and checks a pasted listing. |

## What ChatGPT can and cannot do (checked 27 Oct 2026, verify before you rely on it)

From OpenAI's help page on [scheduled tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt):

- Scheduled tasks are available on Free, Go, Plus, Pro, Business, Enterprise and Edu. Active task limits are 3 (Free, Go), 5 (Plus), 10 (Business, Edu), 15 (Pro, Enterprise). Free accounts can only run once-a-day or one-time tasks. Hourly and exact-time schedules need a paid plan.
- **A task created in a Project cannot read that Project's files.** So the sweep prompt must carry your profile inside the prompt itself. That is what the "profile digest" is for.
- Tasks can use connected apps (Settings, Apps) such as Gmail, Slack, GitHub. They cannot rename or write files on your computer.
- Notifications: push, email or both, under Settings, Notifications. Create the task in the mobile app if you want push.
- Tasks that send messages or change external data may pause for your approval. Tasks may pause if inactive.

Because of the first and third points, the ChatGPT sweep is a research-and-draft run that **delivers into chat**. For each company that passes it gives you the dossier (`3-companyslug.md`) and a complete HTML letter (`3-companyslug-letter.html`) in code blocks. Save each into your `jobs/` folder with that exact name, then open the HTML in a browser to see the letter and press Export PDF.

## Setup in six steps

1. **Create a Project** called "Job search". Paste `project-instructions.md` into the Project instructions.
2. **Upload your profile.** After running setup (below), upload the files from your `profile/` folder and the two letter templates to the Project. Project files are for the interactive chats.
3. **Run setup.** Open a chat in the Project and say: "Run JobSearchOS setup". It will interview you, using `setup-wizard.md` (paste its contents once if the model does not know it). Save the files it generates into your folder.
4. **Make your profile digest.** In the same Project, say: "Make my profile digest" and use `make-profile-digest.md`. You get one compact block of 600 to 900 words.
5. **Create the sweep Task.** In ChatGPT open Scheduled (or ask in a chat: "Every weekday at 6am, run this"). Paste `sweep-task-prompt.md` with your digest and the contents of `letter-skeleton.html` (set to your brand colours and fonts, or use `tools/brand-picker.html`) in the marked places. Pick your time zone and weekdays. Turn on push or email.
6. **Schedule the local script** for the Friday rename (`../scripts/schedule-weekly.md`). Optionally add the Friday reminder Task from `friday-check-task.md`.

## Commands in ChatGPT

There are no slash commands. Say the command as a sentence. The Project instructions teach ChatGPT the mapping:

| Say this | It runs |
|---|---|
| "fast letter: [job link]" | `fast-letter` |
| "log application: Acme, applied" | `log-application` |
| "warm intro: Acme" | `warm-intro` |
| "challenge prep: Acme" | `challenge-prep` |
| "research company: Acme [link]" | `research-company` then `draft-letter` |
| "run the sweep now" | the sweep, once, in chat |

To give ChatGPT a skill, upload the skill's `SKILL.md` (and its `references/` folder) to the Project. The skill files are in `plugin/skills/` in the repo.

## Gemini and others

Same shape as ChatGPT: a workspace with instructions and files (a Gem, a notebook, a custom assistant), a self-contained prompt for any scheduler the tool offers, and the local script for renaming. If your tool has no scheduler, use the manual Monday checklist in `00-START-HERE.md` and a calendar reminder.

## Model choice on ChatGPT

Use the smaller, faster model for setup and for the sweep's source scan. Use the standard model for letters. Avoid the heaviest reasoning model for anything here: it adds cost and wait with no better letter.
