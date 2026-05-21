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

## Key Decisions
- [decision → reason]  ← non-obvious choices only; include exact syntax/API if relevant
- [decision → reason]

## In Progress
- [item — status; add causal note if relevant, e.g. "tests didn't catch this → found late"]

## Completed Detail
- [item — one-line structural note: why it was easy/hard, what made it different]

## Safety Rules
- [constraint + consequence, or "→ see Key Decisions: [which entry]"]

## Last Actions
- [last 2-3 significant actions]

## Next Actions
- [exact next step, specific enough to execute immediately]

## Recon Notes
- [how key facts were discovered: grep command, error message, test that failed]

## Background
→ read [path-to-project-memory-or-context-file] for full background
```

Keep the handoff under 55 lines. Omit any section that has nothing to record. Do not inline architecture docs, full file contents, or long histories — use `→ read [path]` pointers instead.

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
