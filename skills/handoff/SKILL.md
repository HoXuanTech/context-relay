---
name: handoff
description: Save current work state to a handoff file and open a new Claude Code window to continue. Use when the user says /handoff, 準備交接, 儲存換窗, handoff, or 開新視窗接續.
---

When this skill is invoked, do the following steps in order:

## Step 1 — Identify handoff directory

- If the current project has a `.git` folder → use `<project-root>/handoff/`
- Otherwise → use `~/.claude/handoff/<project-name>/`
- Create the directory if it doesn't exist

## Step 2 — Write the handoff file

Filename: `HANDOFF_YYYY-MM-DD_HH-MM.md` (current timestamp)
**Overwrite mode** — never append to an existing file.

Use this exact format:

```markdown
# Handoff - [project-name] - YYYY-MM-DD HH:MM

## Current Goal
[1-2 sentences: what this session is trying to accomplish]

## In Progress
[Only incomplete tasks. Completed tasks are deleted entirely — do not move them elsewhere.]

## Safety Rules
[Session-specific constraints, e.g. "don't restart the bot", "don't delete X directory"]

## Last Actions
[Last 2-3 significant actions taken this session]

## Next Actions
[Exact next steps, specific enough to execute immediately without re-reading the full history]

## Background
→ read [path-to-project-memory-or-context-file] for full background
```

Keep the handoff under 50 lines. Do not inline architecture docs, full file contents, or long histories — use `→ read [path]` pointers instead.

Do not include: `.env` contents, OAuth tokens, credentials, SQLite data, or raw secrets.

## Step 3 — Open new window

Run:
```bash
bash ~/.claude/hooks/context-relay-pre-compact.sh
```

Or directly:
```bash
HANDOFF_FILE="[path-to-handoff-file]"
bash -c "osascript -e 'tell application \"Terminal\" to do script \"claude --append-system-prompt \\\"$(cat $HANDOFF_FILE)\\\"\"'"
```

## Step 4 — Report to user

Tell the user:
- Where the handoff file was saved (full path)
- That a new window is opening with the handoff context loaded
- They can close this window once the new one is ready
