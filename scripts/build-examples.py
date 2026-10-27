#!/usr/bin/env python3
"""Builds examples/jobs/*: three dossiers and their HTML letters (and one resume) from the shipped
templates, using an invented persona. Run from the repo root: python3 scripts/build-examples.py
Everything here is fictional. Company statements are generic and marked [verify]."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = ROOT / "plugin/workspace-template/templates"
OUT = ROOT / "examples/jobs"
OUT.mkdir(parents=True, exist_ok=True)

BRAND = {"--paper": "#FBF8F3", "--ink": "#1B1A17", "--mute": "#6B645B", "--line": "#E6DFD3",
         "--accent": "#0F766E", "--card": "#EEF6F4", "--dark": "#1B1A17"}
FONTS = ('"Fraunces"', '"Inter"')
FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'

ID = {
    "NAME": "Alex Rivera", "ROLE_TITLE": "Product Designer", "EMAIL": "alex.rivera@example.com",
    "CONTACT_LINE": '<a href="https://example.com/alex">example.com/alex</a> &middot; <a href="https://linkedin.com/in/alex-example">linkedin.com/in/alex-example</a>',
    "LOGO": "", "ABOUT_CARD_1": "9 years in B2B product design, currently at Northwind Analytics",
    "WHAT_I_DO": "Turn busy, many-screen products into systems people learn once and teams can extend.",
    "PILLAR_COMPANY": "Northwind Analytics",
}
PAGE2 = {
    "DISCLOSURE": "This page describes how this letter was made.",
    "PROCESS_HEADING": "A person decided every line of this letter.",
    "PROCESS_LEDE": "AI did the reading and the first draft. I did the choosing and the editing.",
    "WHY_THIS_SECTION": "I use AI to research and draft. I decide which project goes in, which challenge is worth raising and what gets cut.",
    "PROCESS_CARDS": "".join([
        '<div class="card"><div class="top"><span class="n">01</span><span class="pill auto">Automated</span></div><h4>Research</h4><div class="sub">AI, minutes</div><p>Read the ad and public pages and drafted a first read of their problem.</p></div>',
        '<div class="card is-human"><div class="top"><span class="n">02</span><span class="pill human">Human</span></div><h4>Choice</h4><div class="sub">Me, 10 minutes</div><p>Picked the project, the challenge and what to leave out.</p></div>',
        '<div class="card"><div class="top"><span class="n">03</span><span class="pill hybrid">Hybrid</span></div><h4>Drafting</h4><div class="sub">AI and me</div><p>Draft against my word budgets, then three rounds of edits.</p></div>',
        '<div class="card is-human"><div class="top"><span class="n">04</span><span class="pill human">Human</span></div><h4>Check and send</h4><div class="sub">Me</div><p>Checked every number against my case study and sent it myself.</p></div>',
    ]),
}

JOBS = [
 dict(slug="stripe", prefix="3-", company="Stripe", role="Product Designer, Dashboard", status="drafted",
  fm=dict(stage="enterprise", location="Remote, EU time zones", setup="remote", location_flag="check-entity",
          company_size="8000+ [verify]", job_link="https://stripe.com/jobs", source="linkedin", tone="measured",
          challenge="A merchant managing a disputed payment moves across four pages to answer one question.",
          challenge_checks_passed="5", confidence="medium", custom_resume="false", date_spotted="2026-10-05",
          date_researched="2026-10-06", priority="medium"),
  GREETING="Hello Stripe team,", DATE="6 October 2026",
  IMPACT_CARD="Turns a growing set of screens into one system other designers can extend.",
  OPENING="I'm looking for a team where design owns the system as well as the screens. Stripe's dashboard serves a finance lead and a support agent from the same components, which is the kind of shared structure I've spent three years building at Northwind Analytics, where I work on executive reporting today. My habit is to decide once, write it down and let others reuse it, and I would like to do that at your scale.",
  BRIDGE="That habit started with one stubborn problem, so I picked a similar one on your side. It comes from reading how a merchant works through a disputed payment, which I enjoyed more than I expected.",
  CHALLENGE_SETUP="A merchant opens a disputed payment and needs to decide whether to fight it or accept it. To answer, they move through the payment view, the customer view, the evidence form and the deadline list. Each page is correct on its own, and the decision lives across all four.",
  CHALLENGE_SOURCE="public help-centre page on responding to disputes [verify]",
  PARALLEL_NOTE="This example is from my current reporting work at Northwind, because that is where I met the same shape of problem.",
  BAND_THEM=["Four views for one decision", "Evidence and deadline live on separate pages"],
  BAND_ME=["One panel per decision in every Northwind report", "Evidence and deadline shown side by side"],
  RESOLUTION="At Northwind that panel stopped being one report's fix. It became the rule for every report after it, with no second executive version to maintain, and <strong>the next report took 3 working sessions instead of 6, by my own log over four reports (small sample, same team)</strong>.",
  HEDGE="From the outside I can only see the surface, so this is a guess about the inside.",
  CLOSE="You know your constraints better than I do: regulation, older views, a dashboard that many teams touch at once. Within those limits, I would enjoy a surface where one decision crosses four pages and the fix has to hold for a finance lead and a support agent alike. If it helps, I can walk you through how the Northwind panel was argued for and cut.",
  CLOSING_LINE="Happy to walk you through it.",
  record=[("2026-10-06", "Researched and drafted (prefix 3-). Remote role, so check-entity: confirm they can employ someone in my country")]),
 dict(slug="miro", prefix="2-", company="Miro", role="Product Designer, Canvas Tools", status="applied",
  fm=dict(stage="scaleup", location="Hybrid, another country", setup="hybrid", location_flag="blocker",
          company_size="1500+ [verify]", job_link="https://miro.com/careers", source="careers-page", tone="measured",
          challenge="Canvas tools keep gaining object types, and the toolbar has to keep each one findable.",
          challenge_checks_passed="4", confidence="medium", custom_resume="true", date_spotted="2026-09-20",
          date_researched="2026-09-21", date_applied="2026-09-22", followup_due="2026-10-01", priority="low"),
  GREETING="Hello Miro team,", DATE="22 September 2026",
  IMPACT_CARD="Keeps a fast-growing set of tools findable as new ones arrive.",
  OPENING="I'm looking for a product where the number of things users can make keeps growing and design has to keep them findable. Miro's canvas is that product. At Northwind Analytics I've spent three years on a reporting suite that gained a new report type every few weeks, and I currently own the pattern each new type has to fit. The job is mostly saying no kindly, and writing down why.",
  BRIDGE="Owning that pattern taught me where growth hurts first, so I looked for the same spot in your product. It is the toolbar, which I found by watching how people add one more object to a board.",
  CHALLENGE_SETUP="A person on a board reaches for a less common object. The toolbar shows a short row of frequent tools, then a longer menu, then a search. New object types land in the menu, so this week's most useful tool sits beside one used once a year.",
  CHALLENGE_SOURCE="public help page on the toolbar and object menu [verify]",
  PARALLEL_NOTE="The example is from my current team at Northwind, where the growth pressure looks the same.",
  BAND_THEM=["New object types join one long menu", "Frequency of use and position in the list are unrelated"],
  BAND_ME=["New report types joined one long menu at Northwind", "A fixed set of six patterns decided where each new type went"],
  RESOLUTION="At Northwind those six patterns became the review gate for every new report type. The rule was written down once, and <strong>two reports shipped through it after I moved teams, built by other designers without my review (a count of what I saw, not a controlled measure)</strong>.",
  HEDGE="From the outside I can only see the surface, so this is a guess about the inside.",
  CLOSE="You have constraints I cannot see: performance on large boards, a long tail of older tools, a team that has lived with this for years. Within those, I would enjoy the argument about where the next object type belongs and what the toolbar refuses to show. I can walk you through the six patterns and the cases we rejected.",
  CLOSING_LINE="Happy to talk it through.",
  record=[("2026-09-21", "Researched, drafted. Location flag: blocker (hybrid in another country)"),
          ("2026-09-22", "Applied, decided to proceed despite the blocker. Follow-up set 7 working days out. Files renamed 3- to 2- by /log-application"),
          ("2026-10-01", "Follow-up due. No reply yet")]),
 dict(slug="jetbrains", prefix="1-", company="JetBrains", role="Product Designer, Developer Tools", status="screening",
  fm=dict(stage="scaleup", location="Remote, EU", setup="remote", location_flag="check-entity",
          company_size="2000+ [verify]", job_link="https://www.jetbrains.com/careers", source="referral", tone="measured",
          challenge="A developer tool has to expose power features without hiding the basics from newcomers.",
          challenge_checks_passed="5", confidence="high", interview_prep_challenge="true", interview_prep_audience="true",
          interview_prep_competitive="true", custom_resume="false", date_spotted="2026-09-01",
          date_researched="2026-09-03", date_applied="2026-09-10", priority="high"),
  GREETING="Hi there,", DATE="10 September 2026",
  IMPACT_CARD="Makes expert features reachable without taxing newcomers.",
  OPENING="I'm looking for a team that builds for people who already know their craft and still want the tool to stay out of the way. JetBrains does that for developers. At Northwind Analytics I design for senior analysts and executives who read the same report for different reasons, and I currently lead the decisions on what each of them is shown. Most of that work is choosing what to hold back, and explaining the choice to the people who asked for more.",
  BRIDGE="Deciding what to show is mostly deciding what to hold back, so I looked at the same trade-off in your settings. A friend who works with your tools pointed me at the place where it shows.",
  CHALLENGE_SETUP="A developer opens settings to change one behaviour. The list is searchable and organised by area, and many options have a close sibling in a different area. Finding the right one takes a search and a guess, and a newcomer cannot tell a common setting from a rare one.",
  CHALLENGE_SOURCE="public documentation page on settings and preferences [verify]",
  PARALLEL_NOTE="This example is from my reporting work at Northwind, my current team, where options also multiplied.",
  BAND_THEM=["Many options have a near neighbour in another area", "Common and rare settings look the same in the list"],
  BAND_ME=["Northwind filters had near neighbours across reports", "One filter pattern separated the common from the rare"],
  RESOLUTION="At Northwind the filter pattern stopped being a single fix. It became how every report separates the common from the rare, with no second version to maintain for executives, and <strong>6 of 9 enterprise customers cited the reporting suite in renewal calls (customer-reported, not a controlled comparison)</strong>.",
  HEDGE="From the outside I can only see the surface, so this is a guess about the inside.",
  CLOSE="You have constraints I cannot see: decades of habits, plugins that add their own settings, a keyboard-first audience. Within them, I would enjoy the question of what a newcomer sees first and what an expert can reach in two keystrokes. I can walk you through the filter pattern, the options we cut and the reasons we gave.",
  CLOSING_LINE="Happy to walk you through it.",
  record=[("2026-09-10", "Applied via referral (prefix 2-)"),
          ("2026-10-14", "Screening call booked. Prefix 2- to 1-. Interview prep auto-added once by /log-application")],
  extra="""
## Challenge prep

**Likely challenge:** redesign a settings or discovery surface for a developer tool. **Scored on:** problem framing, trade-offs named out loud, what you cut. **Rehearsal notes:** open with who the user is and what decision they are making, then the constraint.

## Product audience

**Buyer:** engineering lead. **Daily user:** the developer. **Divergence:** the buyer wants consistency across the team, the developer wants speed and keyboard-first flow.

## Competitive brief

**Competitors:** [three, verify]. **Winning on:** product depth. **Real gap:** [one honest line].
"""),
]

def words(html):
    return len(re.sub(r"<[^>]+>", "", html).split())

def brand_template(src):
    s = src
    for k, v in BRAND.items():
        s = re.sub(r"(%s:)#[0-9A-Fa-f]{3,8}" % re.escape(k), r"\g<1>%s" % v, s, count=1)
    s = re.sub(r'--disp:"[^"]*"', "--disp:" + FONTS[0], s, count=1)
    s = re.sub(r'--sans:"[^"]*"', "--sans:" + FONTS[1], s, count=1)
    s = re.sub(r'<link href="https://fonts.googleapis.com/css2[^>]*>', FONT_LINK, s, count=1)
    return s

def fill(s, mapping):
    for k, v in mapping.items():
        s = s.replace("{{%s}}" % k, v)
    return s

BUDGET = {"OPENING": (70, 85), "BRIDGE": (35, 45), "CHALLENGE_SETUP": (45, 55),
          "PARALLEL_NOTE": (15, 25), "RESOLUTION": (45, 60), "CLOSE": (55, 70)}

def make_letter(j):
    tpl = brand_template((TPL / "letter-template.html").read_text())
    m = dict(ID); m.update(PAGE2)
    m.update(ROLE=j["role"], COMPANY=j["company"], DATE=j["DATE"], GREETING=j["GREETING"])
    for f in ["IMPACT_CARD", "OPENING", "BRIDGE", "CHALLENGE_SETUP", "CHALLENGE_SOURCE", "PARALLEL_NOTE", "RESOLUTION", "HEDGE", "CLOSE", "CLOSING_LINE"]:
        m[f] = j[f]
    m["BAND_THEM"] = "".join("<li>%s</li>" % x for x in j["BAND_THEM"])
    m["BAND_ME"] = "".join("<li>%s</li>" % x for x in j["BAND_ME"])
    for k, (lo, hi) in BUDGET.items():
        n = words(m[k])
        if not lo <= n <= hi:
            print("  budget: %s %s = %d words (want %d-%d)" % (j["slug"], k, n, lo, hi))
    html = fill(tpl, m)
    html = re.sub(r"<!--\nPLACEHOLDERS.*?-->\n", "", html, flags=re.S)
    return html

def make_resume(j):
    tpl = brand_template((TPL / "resume-template.html").read_text())
    m = dict(NAME=ID["NAME"], COMPANY=j["company"],
      BIO_HEADER="Product designer, 9 years in B2B. I turn many-screen products into systems that people learn once and teams extend. At Northwind Analytics I own the reporting patterns that every new report must fit, which suits a canvas that keeps gaining object types.",
      CONTACT_BLOCK='<div>alex.rivera@example.com</div><div><a href="https://example.com/alex">example.com/alex</a></div><div><a href="https://linkedin.com/in/alex-example">linkedin.com/in/alex-example</a></div>',
      EXPERIENCE_BLOCKS='<div class="role"><h3>Product Designer</h3><div class="co">Northwind Analytics (fictional) &middot; 2022 to 2025</div><ul><li>Designed the executive reporting suite and decided what it refuses to show. 6 of 9 enterprise customers cited it in renewal calls (customer-reported).</li><li>Wrote one narrative structure (question, data, description, insight) that became the design language for every report.</li><li>Cut design sessions per new report from 6 to 3 (own log, four reports).</li></ul></div><div class="role"><h3>Designer</h3><div class="co">Contoso Studio (fictional) &middot; 2018 to 2022</div><ul><li>Led design for a document workflow product used by finance teams.</li><li>Built the first shared component library across three products.</li></ul></div>',
      FOOTNOTE="Illustrative example resume for a fictional person. Every employer and number is invented.",
      EDUCATION="<h4>BA, Interaction Design</h4><p>Example University &middot; 2013 to 2017</p>",
      SKILLS="".join('<span class="tag">%s</span>' % t for t in ["Design systems", "Executive tools", "Information architecture", "Workshop facilitation", "Prototyping"]),
      EXTRA_BLOCKS='<div class="block"><div class="eyebrow">Languages</div><p>English, Spanish</p></div>')
    html = fill(tpl, m)
    return re.sub(r"<!--\nHOW THIS TEMPLATE WORKS.*?-->\n", "", html, flags=re.S)

def make_dossier(j):
    fm = {"company": j["company"], "role": j["role"], "status": j["status"]}
    fm.update(j["fm"]); fm.update(pillar="pillar-1-northwind-reporting")
    lines = ["---"] + ["%s: %s" % (k, ('"%s"' % v) if (":" in v or "," in v) else v) for k, v in fm.items()] + ["tags:", "  - job", "  - jobsearchos", "---", ""]
    body = f"""# {j['company']} · {j['role']}

*Illustrative example for a fictional persona. Statements about the company are generic and marked `[verify]`. Files for this job: `{j['prefix']}{j['slug']}.md` and `{j['prefix']}{j['slug']}-letter.html`{' and `%s%s-resume.html`' % (j['prefix'], j['slug']) if j['fm'].get('custom_resume') == 'true' else ''}. Open the HTML in a browser to see the letter, and use Export PDF.*

# PART 1 · RESEARCH

**Challenge:** {j['fm']['challenge']}
**Source:** {j['CHALLENGE_SOURCE']}
**Quality test:** a real problem [x] · specific to them [x] · I have receipts [x] · survives competitive read [x] · sourced to a real page [x]

# PART 2 · LETTER COPY

(Source of truth. The HTML is generated from this section.)

""" + "\n".join("**`%s`:** %s" % (f.lower(), j[f] if isinstance(j[f], str) else "; ".join(j[f])) for f in
        ["GREETING", "IMPACT_CARD", "OPENING", "BRIDGE", "CHALLENGE_SETUP", "CHALLENGE_SOURCE", "PARALLEL_NOTE", "BAND_THEM", "BAND_ME", "RESOLUTION", "HEDGE", "CLOSE", "CLOSING_LINE"]) + "\n" + j.get("extra", "") + "\n## Record\n\n| Date | Event |\n|---|---|\n" + "\n".join("| %s | %s |" % r for r in j["record"]) + "\n"
    return "\n".join(lines) + body

for j in JOBS:
    stem = "%s%s" % (j["prefix"], j["slug"])
    (OUT / (stem + ".md")).write_text(make_dossier(j))
    (OUT / (stem + "-letter.html")).write_text(make_letter(j))
    if j["fm"].get("custom_resume") == "true":
        (OUT / (stem + "-resume.html")).write_text(make_resume(j))
    print("wrote", stem)
