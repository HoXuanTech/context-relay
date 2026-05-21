# Context Relay

**在 Claude Code 壓縮上下文之前，自動保存工作狀態並在新視窗繼續工作。**

[English](README.md)

---

## 問題

Claude Code 在長工程 session 中會自動壓縮上下文（context compaction）。壓縮後 Claude 會忘記正在做什麼——你必須手動重新說明背景、貼上 prompt、重建狀態。每次都要。

## 運作方式

Context Relay 安裝兩個東西：

1. **`PreCompact` hook** — 在每次自動壓縮前自動觸發。開新的 Claude Code 視窗，並帶入最新的換手記憶（handoff），讓工作無縫繼續。

2. **`/handoff` skill** — 隨時可呼叫，主動保存當前狀態並開新視窗。在長 session 中定期使用。

```
自動壓縮即將發生
      ↓
讀取最新 handoff 檔案（你或 /handoff 寫的）
      ↓
開新終端機視窗（macOS: iTerm2/Terminal；Linux: gnome-terminal/konsole/xterm）
      ↓
新 Claude session 帶入完整 handoff 上下文啟動
      ↓
工作繼續
```

---

## 需求

- macOS 或 Linux
- [Claude Code](https://claude.ai/code) ≥ v2.1.144
- Python 3（安裝腳本用）
- Linux 限定：需有支援的終端機（`gnome-terminal`、`konsole`、`xfce4-terminal`、`tilix` 或 `xterm`）

---

## 安裝

```bash
git clone https://github.com/HoXuanTech/context-relay
cd context-relay
bash install.sh
```

安裝後立即生效，不需要重啟。

---

## 使用方式

### 自動（不需任何操作）
Context Relay 在每次自動壓縮前自動觸發。新視窗會帶入你最後一次的 handoff 開啟。

### 手動：`/handoff`
在 Claude Code 中隨時輸入 `/handoff`：
- 將當前工作狀態保存到 handoff 檔案
- 開新視窗並載入該狀態

建議定期主動使用——handoff 越完整，自動換手的品質越好。

---

## Handoff 檔案

儲存位置：
- `<project-root>/handoff/`（git 專案）
- `~/.claude/handoff/<project-name>/`（其他目錄）

格式：
```markdown
# Handoff - [專案名] - YYYY-MM-DD HH:MM

## Current Goal      ← 這個 session 在做什麼（1-2 句）
## In Progress       ← 只列未完成任務，完成的直接刪掉
## Safety Rules      ← 這個 session 的特殊禁忌
## Last Actions      ← 最近 2-3 個有意義的動作
## Next Actions      ← 精確的下一步，要能直接執行
## Background        ← 指向 project memory 的路徑
```

**核心設計原則：** 已完成的任務從 handoff 直接刪除，不是搬移或封存。Handoff 是「現在」的快照，不是歷史紀錄。保持在 50 行以內。

---

## 不會記錄的內容

Handoff 檔案永遠不包含：
- `.env` 內容或 API key
- OAuth token 或 credentials
- 資料庫內容
- 已完成的任務（直接刪除）

---

## 卸載

```bash
# 移除 hook 和 skill
rm ~/.claude/hooks/context-relay-pre-compact.sh
rm -rf ~/.claude/skills/handoff/

# 手動編輯 ~/.claude/settings.json
# 刪除 PreCompact hook 那一段
```

---

## License

MIT
