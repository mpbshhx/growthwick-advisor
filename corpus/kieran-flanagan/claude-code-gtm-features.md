Source: https://www.kieranflanagan.io/p/the-4-new-claude-code-features-for

# The 4 New Claude Code Features for GTM Operators — Kieran Flanagan

*Published May 22, 2026*

## Overview

Four features shipped in Claude Code in the last 90 days that are gold for GTM operators — marketing, growth, and sales teams. Together they describe something that didn't exist six months ago: **a GTM operating layer that runs in the background, lives inside your existing stack, and ships work that used to require a developer, a project manager, and a junior analyst.**

---

## Feature 1: Routines — Scheduling Tasks

**Requires:** Claude Code web app

A Routine is a Claude Code agent that runs on a **schedule, a webhook, or an API call** — entirely in the cloud, without you.

### The Competitor Intel Routine
Every Monday, Claude pulls every blog post, product update, and G2 review from your top 8 competitors published in the last 7 days. Runs that content against your positioning doc. Sends a Slack message with three things the team should care about that week.

**Setup:**
1. Open Claude Code web app → New Routine
2. Select **Remote** (runs without your laptop open)
3. Name: "Monday Competitor Digest"
4. Prompt: *"Every Monday at 6:30am, search the web for blog posts, product updates, and G2 reviews published by [Competitors] in the last 7 days. Compare each piece against the positioning doc at [path]. Send a Slack message to [channel] summarising the 3 things our marketing team should care about this week, with a link to each source."*
5. Set schedule: Weekly, Monday, 6:30am → Connect Slack → Hit Create

### Lightweight Prospecting Agent
High-fit lead fills a form → HubSpot workflow fires a webhook → Claude reads their company, role, recent activity, and Gong call notes if they've spoken to the team → Drafts a first-touch email in your voice → Drops it as a Gmail draft → Rep reviews and sends in 30 seconds.

### The Weekly Content Brief Routine
Every Friday at 4pm: Claude reads your 5 best-performing posts, identifies patterns, drops a Slack message with 5 new content angles that map to what's been working.

---

## Feature 2: Chrome Integration — The Operator Inside Your Stack

**Requires:** Claude Code desktop app + Claude in Chrome extension (free, Chrome Web Store) + paid Anthropic plan

Claude Code can drive your **real, logged-in Chrome browser** — click buttons, fill forms, read page content, navigate across any site you're already logged into.

**Setup:**
1. Install Claude in Chrome extension from Chrome Web Store
2. Sign in with Anthropic account
3. Open Claude Code → run `/chrome`

### The Stuck Pipeline Audit
Prompt: *"Pull every deal in Stage 3 with last activity more than 21 days ago. For each deal, open the record and read the last 5 activity notes. Give me a table: Deal name, days in stage, last note summary, recommendation (Clear next step / Waiting on us / Needs manager review)."*

Claude opens HubSpot, navigates the pipeline, reads each record, returns the table. You don't touch a single screen.

### The Gong Coaching Brief
Before a team review: *"Read the last 10 Gong calls where we lost at the pricing conversation. Identify the 3 most common objections. Tell me which ones our reps handled well and which they stumbled on."*

---

## Feature 3: Auto-Dream — The System That Gets Smarter Over Time

**Requires:** Claude Code v2.1.139+

**The problem it solves:** You spend 20 minutes at the start of every session re-explaining your brand, audience, context, and preferences. Then you close the session and start again.

**What Auto-Dream does:** A background process that periodically reviews everything Claude has learned across your sessions — decisions made, context built, patterns in how you work — and writes the most important parts to memory files that load at the start of every new session. Stale information gets removed. Duplicates get merged. What's left is a **clean, current picture of your projects that loads automatically every time you open Claude Code.**

Named after REM sleep: you don't consciously decide what to remember from your day. Your brain reviews it, extracts what matters, and commits it to long-term memory. Auto-Dream does the same for your AI sessions.

**Enable it:** Inside any Claude Code session, type `/memory` → toggle on.

**After enabling:** Run `/memory` again to review what Claude is carrying — brand context, active project notes, decisions. Edit anything wrong, add anything missing.

**Bonus command:** `/insights` — analyzes your last 30 days of sessions and surfaces patterns: where you're losing time, which prompts produce weak outputs, which workflows are working well.

---

## Feature 4: Agent View and /goal — Your GTM Control Tower

**Requires:** Claude Code v2.1.139+ on paid plan (Pro, Max, Team, Enterprise)

**`/goal`** — define what "done" looks like. Not just the task, but the specific completion condition. Claude then works autonomously until that condition is met.

**Agent view** — one screen showing every session running across your work simultaneously: what's done, what's still running, what needs a decision from you.

### Example /goal prompt:
```
/goal Draft a 5-email launch sequence for our Q3 campaign.
Done means: all 5 emails written, subject lines included,
personalisation tokens marked, reviewed against the ICP brief,
saved to /drafts/q3-emails.md. Stop after 20 turns if not complete.
```

Always include a turn limit to stop sessions running indefinitely.

### Running parallel workstreams:
1. Start session → `/goal [completion condition]` → hit Enter
2. Send to background: `/bg`
3. Repeat for each workstream
4. Open dashboard: `claude agents`

You can kick off simultaneously:
- A launch email sequence being drafted against the campaign brief
- A competitive teardown of every announcement competitors made over the weekend
- A Q3 OKR draft pulled from last quarter's results and current pipeline data
- A customer interview summary condensing the last month of sales calls into themes
- A board update first draft pulled from CRM data, analytics, and last quarter's deck

**Check Agent view between meetings. Approve, redirect, and ship.**

### Practical notes:
- Running 5 parallel sessions uses 5x the tokens of a single session
- Max plan handles this comfortably; Pro plan will hit limits faster with complex sessions
- Keep goals specific and bounded ("Draft a 5-email sequence for [campaign]" ✓ vs. "Help with our Q3 marketing" ✗)
- Agent view is currently a Research Preview — expect the interface to improve
