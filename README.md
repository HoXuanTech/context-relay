# context-relay

> A `/handoff` skill for Claude Code that helps you survive long sessions.

[中文說明](README.zh-TW.md)

---

## The Problem in One Sentence

Claude Code has a memory limit. When a session gets too long, it automatically compresses everything — and in that compression, it tends to forget the most important specifics.

Not everything. It remembers the general shape of the project. But it forgets:

- The exact constant value you locked in (`STORAGE_KEYS.FAVORITES = 'recipe-favorites'` — never change this or all saved data orphans)
- *Why* you rejected the obvious approach (`NEVER use native <dialog>` — because `::backdrop` behaves differently in Chrome vs Firefox)
- What the actual next step is (not "continue the refactor" — specifically "add refreshToken logic to session.ts before touching /api/user")

After a few compression cycles, Claude starts re-suggesting paths you already ruled out. It forgets constraints that took you 20 minutes to discover. The session drifts.

---

## What context-relay Does

**It does not fight auto-compaction. It works alongside it.**

Claude Code's auto-compaction is good at preserving breadth — the general picture of what you're building, what files exist, what's roughly in progress. context-relay handles the three things auto-compaction tends to lose over multiple cycles:

1. **Permanent constants** — exact strings, keys, values that must never change
2. **Never-do rules with reasons** — not just "don't do X" but *why*, including the alternative you already evaluated and rejected
3. **Concrete next action** — specific enough to execute immediately, not just a vague direction

The two work as a team:

```
Without context-relay
──────────────────────────────────────────
[3 compression cycles later]
Claude: "have you considered using native <dialog> for the modal?"
You: "...we went through this"
────────────────────────────────────────── 5–15 min rebuilding

With context-relay
──────────────────────────────────────────
[3 compression cycles later]
Auto-compact: preserves overall project state
Handoff: NEVER native <dialog> — ::backdrop inconsistency Chrome/Firefox
Claude picks up exactly where you left off
```

---

## How It Works

### 1. You write a handoff during the session

Run `/handoff` at any point. Claude writes a short structured file (target: under 35 lines) to your project:

```markdown
# Handoff - my-project - 2026-05-28 14:30

## 現在做到哪
Refactoring auth middleware to work in edge runtime. modal system is done.

## 永久常數 & 禁區
- STORAGE_KEYS.FAVORITES = 'recipe-favorites' — renaming this orphans all saved user data
- NEVER native <dialog> — ::backdrop and returnFocus differ between Chrome/Firefox
- NEVER Node.js APIs in middleware — edge runtime hard block, confirmed via build error

## 接下來要做什麼
- Add refreshToken logic to session.ts
- Run: npm test -- --filter=session
- /api/user is blocked until session.ts is done — do not touch it yet

## Background
→ read PROJECT_CONTEXT.md for full architecture
```

### 2. When auto-compaction fires, the hook takes over

A `PreCompact` hook runs automatically before every compression. It:

- Saves your latest handoff to `~/.claude/HANDOFF_CURRENT.md` (a symlink to the timestamped original — history is never overwritten)
- Writes a small notice file: `~/.claude/COMPACTION_NOTICE.md`
- Shows a desktop notification
- **Does not open a new window** — auto-compaction continues normally

### 3. The compressed session reads the handoff

After compression, Claude's very next response is triggered by a rule in `CLAUDE.md`:

> If `~/.claude/COMPACTION_NOTICE.md` exists: read it, read the handoff, confirm state to the user, delete the notice file.

The compressed session gets both: auto-compact's broad context coverage + handoff's precise specifics. Then the notice file is deleted so it doesn't repeat on future messages.

---

## Install

**Via Claude Code (easiest):**

Open Claude Code and say:
> 幫我安裝 https://github.com/HoXuanTech/context-relay

**Manual:**

```bash
git clone https://github.com/HoXuanTech/context-relay ~/context-relay
cd ~/context-relay
bash install.sh
```

---

## Usage

**Run `/handoff` regularly during long sessions:**
- After finishing a meaningful chunk of work
- When switching to a different part of the codebase
- Any time you'd feel nervous if the session was suddenly reset

That's it. The hook handles everything else automatically.

**Handoff files are saved to:**
- `<project-root>/handoff/` — for git projects
- `~/.claude/handoff/<project-name>/` — for everything else

History is preserved. Every `/handoff` creates a new timestamped file. `HANDOFF_CURRENT.md` is a symlink to the latest — nothing gets overwritten.

---

## What Goes in a Handoff (and What Doesn't)

**Write this:**
- Permanent constants with exact values and what breaks if they change
- Rules framed as prohibitions: `NEVER [X] — [specific reason, including the rejected alternative]`
- The single most important next step, specific enough to run immediately

**Don't write this:**
- Everything you did this session (auto-compact covers this)
- `.env` contents, credentials, secrets
- Full file contents or long architecture docs — use `→ read [path]` instead

**The handoff is not a history log. It's a precision supplement.**

---

## Research

Five studies were conducted comparing auto-compaction against the handoff format across different content types (engineering sessions, academic text, realistic vibe coding conversations). The key finding:

> Auto-compaction and handoff are good at different things. Auto-compaction preserves breadth. Handoff preserves precision — exact constants, rejection reasons, and directional momentum. The two together outperform either alone.

The failure mode without handoff is not catastrophic amnesia — it's gradual drift. Claude slowly forgets *why* decisions were made, starts re-proposing ruled-out approaches, and loses the specific next action. This compounds with each compression cycle.

→ [Full research data and methodology](research/RESEARCH_SUMMARY.md)

---

## Requirements

- macOS (Linux support: partial — desktop notification won't work, rest is fine)
- Claude Code ≥ v2.1.144
- Python 3

---

## Uninstall

```bash
rm ~/.claude/hooks/context-relay-pre-compact.sh
rm -rf ~/.claude/skills/handoff/
rm -f ~/.claude/HANDOFF_CURRENT.md
rm -f ~/.claude/COMPACTION_NOTICE.md
# Remove the PreCompact entry from ~/.claude/settings.json
# Remove the Context Relay section from ~/.claude/CLAUDE.md
```

---

MIT License
