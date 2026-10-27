---
workspace_path: ""            # absolute path to this folder; skills ask once if empty
ai_tool: claude               # claude | chatgpt | gemini | other
models:
  setup: haiku                # wizard and file generation
  search: haiku               # search synthesis, JD parsing
  writing: sonnet             # the Squeeze, Decision Card, letters
  deep: sonnet                # deep research, challenge prep (a larger model is optional)
modules:
  fast_letter: true           # core, always on
  log_application: true      # core, always on
  deep_research: true         # research-company + draft-letter
  challenge_prep: true
  product_audience: true
  competitive_brief: true
  warm_intro: true
  tailored_resume: true
  overnight_sweep: false
  friday_filename_check: true
letter_format: structured     # structured | classic
level_policy: never-name      # never-name | name-when-asked
weekly_target: 8
timezone: ""                  # for scheduled automations, e.g. America/New_York
cadence:
  source: monday
  warm_intro: thursday
  review: friday
---

# JobSearchOS config

Skills read this file first. Edit the values above, or re-run `/setup`.

- A module set to `false` makes its command say so in one line and stop.
- `models` are the model *roles*. Your tool decides what they map to. Defaults keep cost low: a small model for questions and search, a mid model for writing, a large model never required.
