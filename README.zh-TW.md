# context-relay

> 一個給 Claude Code 用的 `/handoff` skill，讓你在漫長 session 中撐住。

[English](README.md)

---

## 一句話說清楚問題

Claude Code 有記憶上限。session 太長時，它會自動壓縮所有對話——壓縮後，最重要的細節往往不見了。

不是全部消失。大方向還在。但消失的是：

- 你鎖定的精確常數（`STORAGE_KEYS.FAVORITES = 'recipe-favorites'`——改掉這個，所有使用者的收藏資料就孤兒了）
- 你排除某個做法的原因（`永遠不要用原生 <dialog>`——因為 Chrome 和 Firefox 的 `::backdrop` 行為不一樣）
- 真正的下一步是什麼（不是「繼續重構」——是「在動 /api/user 之前，先把 refreshToken 邏輯加進 session.ts」）

幾次壓縮後，Claude 開始重新提你早就排除的方案。它忘記你花了 20 分鐘確認的限制。session 開始漂移。

---

## context-relay 做什麼

**它不對抗自動壓縮。它和自動壓縮搭檔工作。**

Claude Code 的自動壓縮很擅長保留廣度——你在做什麼、有哪些檔案、整體進度大概如何。context-relay 處理它在多次壓縮後最容易丟失的三類東西：

1. **永久常數** — 精確的字串、key、數值，絕對不能改
2. **禁區＋原因** — 不只是「不要做 X」，還有*為什麼*，包括你已經評估並排除的替代方案
3. **具體下一步** — 具體到可以直接執行，不是模糊的方向

兩者合作：

```
沒有 context-relay
──────────────────────────────────────────
[3 次壓縮後]
Claude：「有沒有考慮用原生 <dialog> 做 modal？」
你：「...我們討論過這個了」
────────────────────────────────────────── 5–15 分鐘重建 context

有 context-relay
──────────────────────────────────────────
[3 次壓縮後]
自動壓縮：保留整體專案狀態
Handoff：永遠不要用原生 <dialog> — ::backdrop 在 Chrome/Firefox 行為不一致
Claude 從上次確切停下的地方繼續
```

---

## 運作方式

### 1. 在 session 中寫 handoff

隨時執行 `/handoff`。Claude 會寫一份短小的結構化檔案（目標 35 行以內）到你的專案：

```markdown
# Handoff - my-project - 2026-05-28 14:30

## 現在做到哪
正在重構 auth middleware 讓它支援 edge runtime。modal 系統已完成。

## 永久常數 & 禁區
- STORAGE_KEYS.FAVORITES = 'recipe-favorites' — 改了這個，所有使用者收藏資料就孤兒了
- NEVER 原生 <dialog> — ::backdrop 在 Chrome/Firefox 表現不同，returnFocus 也有差
- NEVER 在 middleware 裡用 Node.js API — edge runtime 硬限制，build error 已確認

## 接下來要做什麼
- 在 session.ts 加 refreshToken 邏輯
- 跑：npm test -- --filter=session
- /api/user 等 session.ts 完成前不要動

## Background
→ read PROJECT_CONTEXT.md 看完整架構
```

### 2. 自動壓縮觸發時，hook 自動處理

每次壓縮前，`PreCompact` hook 會：

- 把你最新的 handoff 存到 `~/.claude/HANDOFF_CURRENT.md`（symlink 指向有時間戳的原始檔——歷史永遠不會被覆蓋）
- 寫一個小通知檔案：`~/.claude/COMPACTION_NOTICE.md`
- 顯示桌面通知
- **不會開新視窗**——自動壓縮正常繼續

### 3. 壓縮後的 session 讀取 handoff

壓縮完成後，Claude 的第一個回應由 `CLAUDE.md` 裡的規則觸發：

> 如果 `~/.claude/COMPACTION_NOTICE.md` 存在：讀取它，讀取 handoff，向使用者確認狀態，刪除通知檔案。

壓縮後的 session 兩者都拿到了：自動壓縮的廣度覆蓋 + handoff 的精準細節。通知檔案接著被刪除，不會在下次訊息重複觸發。

---

## 安裝

**透過 Claude Code（最簡單）：**

打開 Claude Code 說：
> 幫我安裝 https://github.com/HoXuanTech/context-relay

**手動：**

```bash
git clone https://github.com/HoXuanTech/context-relay ~/context-relay
cd ~/context-relay
bash install.sh
```

---

## 使用方式

**在漫長 session 中定期執行 `/handoff`：**
- 完成一個有意義的工作段落後
- 切換到 codebase 的不同部分時
- 任何讓你覺得「如果 session 突然重置我會很慘」的時候

就這樣。hook 自動處理其他一切。

**Handoff 檔案存放位置：**
- `<project-root>/handoff/` — git 專案
- `~/.claude/handoff/<project-name>/` — 其他情況

歷史完整保留。每次 `/handoff` 都建立一個新的有時間戳檔案。`HANDOFF_CURRENT.md` 是 symlink 指向最新版——沒有東西會被覆蓋。

---

## Handoff 寫什麼（以及不要寫什麼）

**要寫：**
- 永久常數，含精確值和改了會壞什麼
- 用禁止語氣寫的規則：`NEVER [X] — [具體原因，含被排除的替代方案]`
- 最重要的一個下一步，具體到可以直接執行

**不要寫：**
- 這個 session 你做了什麼（自動壓縮會處理）
- `.env` 內容、credentials、機密
- 完整檔案內容或長架構文件——用 `→ read [路徑]` 代替

**Handoff 不是歷史紀錄。它是精準補充。**

---

## 研究背景

我們做了五項研究，比較自動壓縮和 handoff 格式在不同內容類型下的表現（工程 session、學術文本、真實 vibe coding 對話）。核心發現：

> 自動壓縮和 handoff 各有擅長。自動壓縮保留廣度。Handoff 保留精準度——精確常數、排除原因、以及工作方向的動能。兩者合用，勝過任何一方單獨使用。

沒有 handoff 的失敗模式不是災難性的失憶——是漸進式的漂移。Claude 慢慢忘記決策背後的*為什麼*，開始重新提出已被排除的方案，並失去具體的下一步行動。這在每次壓縮後都會加重。

→ [完整研究資料與方法論](research/RESEARCH_SUMMARY.md)

---

## 需求

- macOS（Linux 部分支援——桌面通知不可用，其餘正常）
- Claude Code ≥ v2.1.144
- Python 3

---

## 卸載

```bash
rm ~/.claude/hooks/context-relay-pre-compact.sh
rm -rf ~/.claude/skills/handoff/
rm -f ~/.claude/HANDOFF_CURRENT.md
rm -f ~/.claude/COMPACTION_NOTICE.md
# 手動從 ~/.claude/settings.json 移除 PreCompact 那段
# 手動從 ~/.claude/CLAUDE.md 移除 Context Relay 那段
```

---

MIT License
