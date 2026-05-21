# Context Relay

**Automatically save your work state before Claude Code compacts the context window, then resume in a new session — without losing progress.**

[中文說明](README.zh-TW.md)

---

## The Problem

Claude Code automatically compacts the context window during long engineering sessions. When this happens, Claude forgets what it was doing. You have to manually remind it, re-paste context, and rebuild state — every time.

## How It Works

Context Relay installs two things:

1. **A `PreCompact` hook** — fires automatically before every auto-compaction. It opens a new Claude Code window with the latest handoff context pre-loaded, so work continues seamlessly.

2. **A `/handoff` skill** — run it anytime to save current state to a handoff file and open a new window. Use this proactively during long sessions.

```
PreCompact fires
      ↓
Read latest handoff file (written by you or /handoff)
      ↓
Open new terminal window (iTerm2/Terminal on macOS, gnome-terminal/konsole/xterm on Linux)
      ↓
New Claude session starts with full handoff context
      ↓
Work continues
```

---

## Requirements

- macOS or Linux
- [Claude Code](https://claude.ai/code) ≥ v2.1.144
- Python 3 (for install script)
- Linux only: a supported terminal (`gnome-terminal`, `konsole`, `xfce4-terminal`, `tilix`, or `xterm`)

---

## Install

```bash
git clone https://github.com/HoXuanTech/context-relay
cd context-relay
bash install.sh
```

That's it. The hook is active immediately — no restart needed.

---

## Usage

### Automatic (no action needed)
Context Relay fires automatically before every auto-compaction. A new window opens with your last handoff loaded.

### Manual: `/handoff`
Type `/handoff` anytime in Claude Code to:
- Save current work state to a handoff file
- Open a new window with that context

Use this proactively — the richer your handoff files, the better the automatic relay works.

---

## Handoff Files

Handoff files are saved to:
- `<project-root>/handoff/` for git projects
- `~/.claude/handoff/<project-name>/` for other directories

Format:
```markdown
# Handoff - [project] - YYYY-MM-DD HH:MM

## Current Goal
## In Progress
## Safety Rules
## Last Actions
## Next Actions
## Background
```

**Key design principle:** Completed tasks are deleted from handoff files, not archived. A handoff is a snapshot of *right now*, not a history log. Keep it under 50 lines.

---

## What's Not Stored

Handoff files never contain:
- `.env` contents or API keys
- OAuth tokens or credentials
- Database contents
- Completed tasks (they're deleted)

---

## Uninstall

```bash
# Remove hook and skill
rm ~/.claude/hooks/context-relay-pre-compact.sh
rm -rf ~/.claude/skills/handoff/

# Remove from settings.json (manually edit ~/.claude/settings.json
# and delete the PreCompact hook entry)
```

---

## License

MIT
