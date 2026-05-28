# /goal vs context-relay: Context Management Analysis

---

## /goal 的運作機制

/goal 是 Claude Code 的長跑任務指令，將執行與評估分離：

- **執行模型**：在同一個 session 裡持續做事（改檔案、跑測試）
- **評估模型**：每輪結束後讀對話，判斷完成條件是否達到
- **迴圈**：未達成 → 繼續執行；達成 → 停止

整個 loop 在同一個 session 裡跑，不開新視窗，不換 session。

---

## /goal 的 context 壓縮問題

/goal **沒有自己的 context 管理機制**，完全依賴 auto-compaction。

長跑任務（幾小時）過程中，context 填滿後自動壓縮。根據 Study 1 數據，壓縮後：
- 已排除方案的原因消失 → Claude 可能重複試已失敗的方向
- 決策脈絡稀釋 → 評估模型判斷品質下降
- 3 輪壓縮後 context 準確率從 60% 降至 30%

---

## 與 context-relay 的衝突

| | context-relay | /goal |
|---|---|---|
| 機制 | PreCompact hook → 開新視窗 | 同一 session 持續跑 |
| 需求 | 換手給人繼續指揮 | session 連續性不能斷 |
| 壓縮時行為 | 開新視窗 + 載入 handoff | 就地壓縮，繼續執行 |

**結論：現在的 context-relay 會破壞 /goal。**
/goal 跑到一半 → PreCompact 觸發 → context-relay 開新視窗 → /goal loop 中斷。

---

## 理論上的共存方案（未實作）

**方案 A：偵測 /goal 狀態，跳過開新視窗**
只寫 handoff 檔，不開新視窗，讓 /goal 繼續在原 session 跑。
障礙：沒有公開 API 可偵測 /goal 是否 active。

**方案 B：/goal 專用 context 注入模式**
壓縮前把 handoff 內容 inject 進 system prompt，讓壓縮後的 session 帶著結構化狀態繼續。
障礙：Claude Code 目前無「中途更新 system prompt」的 API。

---

## 定位結論

兩者解決不同問題，不是競爭關係：

| | 適用場景 |
|---|---|
| `/goal` | 全自動任務，AI 跑到完成，人不介入 |
| `context-relay` | 人機協作，context 換手後人繼續指揮 |

比較效果無意義。若未來 Claude Code 開放 /goal 狀態偵測或 system prompt 動態更新 API，可考慮讓 context-relay 支援 /goal 模式。

---

## 未來研究方向

- 觀察 /goal 在長跑任務中實際的 context 衰減表現
- 若 Claude Code 開放相關 API，設計 /goal 相容模式
