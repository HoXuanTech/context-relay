#!/bin/bash
# Context Relay — install script
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$HOME/.claude"
SETTINGS="$CLAUDE_DIR/settings.json"

echo "Installing Context Relay..."

# 1. Install hook script
mkdir -p "$CLAUDE_DIR/hooks"
cp "$REPO_DIR/hooks/pre-compact.sh" "$CLAUDE_DIR/hooks/context-relay-pre-compact.sh"
chmod +x "$CLAUDE_DIR/hooks/context-relay-pre-compact.sh"
echo "✓ Installed pre-compact hook"

# 2. Install /handoff skill
mkdir -p "$CLAUDE_DIR/skills/handoff"
cp "$REPO_DIR/skills/handoff/SKILL.md" "$CLAUDE_DIR/skills/handoff/SKILL.md"
echo "✓ Installed /handoff skill"

# 3. Merge PreCompact hook into settings.json
python3 - "$SETTINGS" << 'PYEOF'
import sys, json, os

settings_path = sys.argv[1]
hook_entry = {
    "matcher": "auto",
    "hooks": [{
        "type": "command",
        "command": "bash ~/.claude/hooks/context-relay-pre-compact.sh"
    }]
}

# Load existing settings or start fresh
if os.path.exists(settings_path):
    with open(settings_path) as f:
        settings = json.load(f)
else:
    settings = {}

# Ensure hooks.PreCompact exists
settings.setdefault("hooks", {})
settings["hooks"].setdefault("PreCompact", [])

# Avoid duplicate: remove any existing context-relay entry
settings["hooks"]["PreCompact"] = [
    h for h in settings["hooks"]["PreCompact"]
    if not any(
        "context-relay" in hook.get("command", "")
        for hook in h.get("hooks", [])
    )
]

# Add our hook
settings["hooks"]["PreCompact"].append(hook_entry)

# Write back
with open(settings_path, "w") as f:
    json.dump(settings, f, indent=2, ensure_ascii=False)
    f.write("\n")
PYEOF
echo "✓ Updated settings.json with PreCompact hook"

echo ""
echo "Context Relay installed successfully!"
echo ""
echo "  Auto-handoff : fires automatically before context compaction"
echo "  Manual       : type /handoff anytime to save state + open new window"
echo ""
echo "Handoff files are saved to:"
echo "  <project-root>/handoff/   (git projects)"
echo "  ~/.claude/handoff/        (other directories)"
