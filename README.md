# Context Relay

> **To install via Claude Code, just say:**
> `幫我安裝 https://github.com/HoXuanTech/context-relay`

**Never lose your flow when Claude Code compacts.**

[中文說明](README.zh-TW.md)

---

## The Problem: Compaction Wipes Your Work State

Claude Code's context window holds ~200k tokens. During a long session —
refactoring across 10+ files, debugging a complex bug, working through a
multi-step migration — the window fills up. Claude Code auto-compacts:
summarizes the conversation and continues.

The problem is what gets lost.

**What Claude remembers after compaction:**
> "You're refactoring a Next.js project."

**What Claude forgets:**
- *Why* `authMiddleware` can't be a HOC (edge runtime limitation you spent 20 minutes figuring out)
- That `/api/user` was intentionally skipped, waiting for `session.ts`
- Which 3 of the 7 modified files are still half-done
- The stop condition: "don't touch `/api/auth/callback`, it's live"

**The cost:** 5–15 minutes rebuilding context from memory. If you're
tired, you rebuild it wrong. Claude re-opens files you told it to leave
alone. It re-suggests approaches you already ruled out.

Engineers work around this by pasting checkpoint notes into the chat,
opening new tabs and re-explaining everything, or leaving
`// TODO: Claude forgot this` comments in the code. Manual patches for
a systemic problem.

---

## The Fix: Automatic Handoff Before Every Compaction

Context Relay installs a `PreCompact` hook into Claude Code. Before
every auto-compaction, it:

1. Reads your latest handoff file (a <50-line snapshot of your state)
2. Opens a new terminal window automatically
3. Starts a new Claude Code session with that snapshot pre-loaded

The new session knows exactly where to pick up.

```
WITHOUT Context Relay
─────────────────────────────────────────────
[Auto-compact fires]
→ Claude forgets everything specific
→ You spend 5–15 min rebuilding context from memory
→ Claude may undo decisions you already made

WITH Context Relay
─────────────────────────────────────────────
[Auto-compact fires]
→ Desktop notification: "Opening new window to continue work"
→ New terminal opens automatically
→ New Claude session starts with full handoff loaded
→ Work continues from exactly where you left off
```

---

## Install

**Option 1 — Let Claude Code do it:**

Open Claude Code and say:
> 幫我安裝 https://github.com/HoXuanTech/context-relay

**Option 2 — Manual:**

```bash
git clone https://github.com/HoXuanTech/context-relay ~/context-relay
cd ~/context-relay
bash install.sh
```

---

## Usage

### 1. Run `/handoff` during sessions

The auto-handoff quality depends entirely on how recent your last
`/handoff` is. Run it:
- After completing a meaningful unit of work
- Before switching tasks
- Every 15–20 minutes during long sessions

Handoff files are saved to:
- `<project-root>/handoff/` — git projects
- `~/.claude/handoff/<project-name>/` — everything else

### 2. Do nothing else

When auto-compaction fires, Context Relay handles it. A new window
opens with your handoff loaded.

---

## What a Handoff File Looks Like

```markdown
# Handoff - my-project - 2026-05-21 03:00

## Current Goal
Refactoring authMiddleware to support edge runtime without breaking sessions.

## In Progress
- [ ] session.ts — half-done, needs refreshToken logic
- [ ] /api/user — intentionally skipped, touch after session.ts

## Safety Rules
- Do NOT touch /api/auth/callback — it's live
- No Node.js APIs (edge runtime constraint)

## Last Actions
- Confirmed authMiddleware can't be HOC (edge runtime)
- Rewrote middleware.ts, headers.ts, tokens.ts — tests passing
- Skipped /api/user intentionally

## Next Actions
- Add refreshToken logic to session.ts
- Run: npm test -- --filter=session
- Then return to /api/user

## Background
→ read PROJECT_CONTEXT.md for full architecture
```

Completed tasks are deleted, not archived. A handoff is a snapshot of
*right now*, not a history log. Keep it under 50 lines.

---

## Requirements

- macOS or Linux
- Claude Code ≥ v2.1.144
- Python 3
- Linux only: one of `gnome-terminal`, `konsole`, `xfce4-terminal`, `tilix`, or `xterm`

---

## Limitations

- If you haven't run `/handoff` recently, the new session opens with
  only a minimal placeholder — the hook can't read your mind
- The new window is an independent session; tool permissions and env
  vars are not inherited
- Deep architecture context belongs in project files, pointed to with
  `→ read [path]`

---

## Uninstall

```bash
rm ~/.claude/hooks/context-relay-pre-compact.sh
rm -rf ~/.claude/skills/handoff/
# Remove the PreCompact entry from ~/.claude/settings.json
```

---

MIT License

---

> **Install via Claude Code:**
> `幫我安裝 https://github.com/HoXuanTech/context-relay`
