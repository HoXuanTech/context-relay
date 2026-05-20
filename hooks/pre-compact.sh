#!/bin/bash
# Context Relay — PreCompact hook
# Fires before Claude Code auto-compacts the context window.
# Saves latest handoff and opens a new session to continue work.

set -euo pipefail

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M")
DATE_HUMAN=$(date +"%Y-%m-%d %H:%M")

# --- Parse hook input (JSON from stdin) ---
HOOK_INPUT=$(cat)
TRIGGER=$(echo "$HOOK_INPUT" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('trigger','unknown'))" 2>/dev/null || echo "unknown")

# Only act on auto-compact (not manual /compact)
if [ "$TRIGGER" != "auto" ]; then
    exit 0
fi

# --- Determine project ---
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"
PROJECT_NAME=$(basename "$PROJECT_DIR")

# --- Determine handoff directory ---
if [ -d "$PROJECT_DIR/.git" ]; then
    HANDOFF_DIR="$PROJECT_DIR/handoff"
else
    HANDOFF_DIR="$HOME/.claude/handoff/$PROJECT_NAME"
fi
mkdir -p "$HANDOFF_DIR"

# --- Find latest handoff ---
LATEST_HANDOFF=$(ls -t "$HANDOFF_DIR"/HANDOFF_*.md 2>/dev/null | head -1 || echo "")

# If no prior handoff exists, create a minimal placeholder
if [ -z "$LATEST_HANDOFF" ]; then
    LATEST_HANDOFF="$HANDOFF_DIR/HANDOFF_${TIMESTAMP}.md"
    cat > "$LATEST_HANDOFF" << EOF
# Handoff - $PROJECT_NAME - $DATE_HUMAN

## Current Goal
(Not recorded — run /handoff during sessions to capture work state)

## In Progress
(Unknown — compaction occurred without a prior /handoff)

## Safety Rules

## Last Actions

## Next Actions
- Review project state and resume from where you left off

## Background
→ Project directory: $PROJECT_DIR
EOF
fi

# --- Write launcher script (avoids quoting issues in osascript) ---
LAUNCHER=$(mktemp /tmp/context-relay-XXXXX.sh)
chmod +x "$LAUNCHER"

HANDOFF_CONTENT=$(cat "$LATEST_HANDOFF")

cat > "$LAUNCHER" << LAUNCHER_EOF
#!/bin/bash
claude --append-system-prompt "$(printf '%s' "$HANDOFF_CONTENT" | sed 's/"/\\"/g')"
rm -f "$LAUNCHER"
LAUNCHER_EOF

# --- Desktop notification ---
osascript -e 'display notification "Opening new window to continue work" with title "Context Relay" subtitle "Auto-compact triggered"' 2>/dev/null || true

# --- Open new window ---
# Try iTerm2 first, fall back to Terminal.app
if osascript -e 'tell application "System Events" to (name of processes) contains "iTerm2"' 2>/dev/null | grep -q "true"; then
    osascript << APPLESCRIPT
tell application "iTerm2"
    create window with default profile
    tell current session of current window
        write text "bash $LAUNCHER"
    end tell
end tell
APPLESCRIPT
else
    osascript -e "tell application \"Terminal\" to do script \"bash $LAUNCHER\""
fi

echo "Context Relay: new window opened with handoff from $LATEST_HANDOFF"
