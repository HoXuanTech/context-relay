# Context Relay

> **直接告訴你的 Claude Code：**
> `幫我安裝 https://github.com/HoXuanTech/context-relay`

**讓 Claude Code 在壓縮上下文前自動換手，不中斷工作流。**

[English](README.md)

---

## 問題：自動壓縮會清掉你的工作狀態

Claude Code 的 context window 約 200k tokens。長時間的 session——跨 10+ 個
檔案重構、追蹤複雜 bug、多步驟遷移——很容易填滿。填滿後系統自動壓縮，把整段
對話濃縮成摘要繼續跑。

問題是壓縮後消失的東西。

**壓縮後 Claude 記得的：**
> 「你在重構一個 Next.js 專案。」

**壓縮後 Claude 忘掉的：**
- 為什麼 `authMiddleware` 不能做成 HOC（你花了 20 分鐘搞清楚的 edge runtime 限制）
- `/api/user` 是故意跳過的，要等 `session.ts` 改完才能動
- 7 個修改中的哪 3 個還是做到一半的狀態
- 你設定的禁忌：「不要動 `/api/auth/callback`，那個在 production」

**重建成本：** 5–15 分鐘，靠你自己的記憶。疲勞時重建錯了，Claude 會去動你
說不能動的東西，或重新提你早就排除的方案。

工程師現在的應對方式：把 checkpoint 筆記貼進對話框、開新分頁從頭解釋、在
程式碼裡留 `// TODO: Claude 忘了這個`。全是人力補洞。

---

## 解法：壓縮前自動換手

Context Relay 在 Claude Code 裡安裝一個 `PreCompact` hook。每次自動壓縮前：

1. 讀取你最新的 handoff 檔（你工作狀態的 <50 行快照）
2. 自動開一個新的終端機視窗
3. 帶著那份快照啟動新的 Claude Code session

新 session 直接知道從哪裡接。你不用解釋任何事。

```
沒有 Context Relay
─────────────────────────────────────────────
[自動壓縮觸發]
→ Claude 忘掉所有具體狀態
→ 你花 5–15 分鐘靠記憶重建 context
→ Claude 可能重新碰你說不能動的東西

有 Context Relay
─────────────────────────────────────────────
[自動壓縮觸發]
→ 桌面通知：「Opening new window to continue work」
→ 新終端機視窗自動彈出
→ 新 Claude session 帶著完整 handoff 啟動
→ 從上次停下的地方繼續，什麼都不用說
```

---

## 安裝

**方法一 — 讓 Claude Code 幫你裝：**

在 Claude Code 裡說：
> 幫我安裝 https://github.com/HoXuanTech/context-relay

**方法二 — 手動：**

```bash
git clone https://github.com/HoXuanTech/context-relay ~/context-relay
cd ~/context-relay
bash install.sh
```

---

## 使用方式

### 1. 在 session 中定期執行 `/handoff`

自動換手的品質完全取決於你最後一次 `/handoff` 的新鮮度。建議時機：
- 完成一個有意義的工作單元後
- 切換任務前
- 長 session 中每 15–20 分鐘

Handoff 檔案存放位置：
- `<project-root>/handoff/`（git 專案）
- `~/.claude/handoff/<project-name>/`（其他目錄）

### 2. 其他什麼都不用做

自動壓縮觸發時，Context Relay 全程處理。新視窗自動開，handoff 自動帶入。

---

## Handoff 檔案長這樣

```markdown
# Handoff - my-project - 2026-05-21 03:00

## Current Goal
重構 authMiddleware，讓它支援 edge runtime，不破壞現有 session。

## In Progress
- [ ] session.ts — 做到一半，需要加 refreshToken 邏輯
- [ ] /api/user — 故意跳過，等 session.ts 完成再動

## Safety Rules
- 不能動 /api/auth/callback — 在 production
- 不能用 Node.js API（edge runtime 限制）

## Last Actions
- 確認 authMiddleware 不能做成 HOC（edge runtime）
- 改完 middleware.ts、headers.ts、tokens.ts，測試通過
- 故意跳過 /api/user

## Next Actions
- 在 session.ts 加 refreshToken 邏輯
- 跑：npm test -- --filter=session
- 然後回來處理 /api/user

## Background
→ read PROJECT_CONTEXT.md 看完整架構
```

已完成的任務直接刪掉，不是搬移或封存。Handoff 是「現在」的快照，不是歷史
紀錄。保持在 50 行以內。

---

## 需求

- macOS 或 Linux
- Claude Code ≥ v2.1.144
- Python 3
- Linux 限定：需有 `gnome-terminal`、`konsole`、`xfce4-terminal`、`tilix` 或 `xterm` 其中之一

---

## 已知限制

- 如果你很久沒執行 `/handoff`，自動換手只能帶入空的 placeholder——hook 無法讀取你的思路
- 新視窗是獨立的 Claude Code session，不繼承原視窗的 tool permissions 或環境變數
- 深層架構細節應放在專案檔案裡，用 `→ read [路徑]` 指向

---

## 卸載

```bash
rm ~/.claude/hooks/context-relay-pre-compact.sh
rm -rf ~/.claude/skills/handoff/
# 手動編輯 ~/.claude/settings.json，刪除 PreCompact 那段
```

---

MIT License

---

> **直接告訴你的 Claude Code：**
> `幫我安裝 https://github.com/HoXuanTech/context-relay`
