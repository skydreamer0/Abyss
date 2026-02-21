---
name: Novel Production Factory
description: 自動化全書創作流水線，包含規劃、初稿、擴寫、校對與同步。
---

# 小說生產工廠 (Novel Production Factory)

本技能包是整個創作進程的「母技能」，負責調度其他所有技能（Expansion, Pacing, Planner, Tracker），實現一鍵自動化產出。

## 自動化工作流 (Master Workflow)

當用戶下達「生產 [章節號]」指令時，應按照以下 SOP 順序執行：

# Novel Production Factory (UPW Master Pipeline)

本技能包定義了集成的 **「統一生產流水線 (Unified Production Workflow)」**。它整併了 Planning, Consistency, Expansion, Pacing 與 Stats 所有的檢查與執行邏輯，旨在以最少的 Resource (Token/Time) 產出最高質量的文稿。

---

## 🏗️ 流水線 A：敘事策略工廠 (Narrative Strategy Factory)
**適用時機**：啟動新的一卷（Volume）或需要重寫全卷架構時。

### 執行 SOP：
1.  **宏觀對齊 (Macro-Audit)**：讀取 `全書總綱.md` 與 `起草版大綱.md`，確定本卷權力位階與核心爽感引擎。
2.  **生成敘事大綱**：在 `planning/10-plans/` 創建 `S1V[X]敘事大綱.md`（含 16 章規劃與硬代價）。
3.  **資訊解鎖表 (Lore Pacing)**：規定關鍵設定在 Phases 中的導入順序（現象 → 流程 → 系統 → 真相）。
4.  **指令**：`策略規劃 V[X]`

---

## ✍️ 流水線 B：萬用生產工廠 (Unified Execution Factory)
**適用時機**：日常章節生產。此流水線自動集成「一致性檢查」與「品質校對」。

### 執行 SOP：
1.  **單一規劃 (Combined DoR)**：
    - 讀取大綱與 `settings/` 相關詞條（由 `Lore Pacing Table` 指定）。
    - 撰寫 G-O-C-R-S-H 並確認「因果鏈」與「壓力等級」。
2.  **草繪與擴寫 (Hybrid Crafting)**：
    - 使用 `novel_expansion` 邏輯進行 3000+ 字擴寫。
    - 指令內嵌感官標籤 `[VISUAL]` 等，**通過 `scripts/cleanup_tags.py` 全自動清理**。
3.  **統一品質巡檢 (Unified Quality Audit)**：
    - **一致性**：對照 `settings/` 檢查術語、數值與邏輯。
    - **節奏與爽感**：檢查衝突密度、讀者洞察與名場面符合度。
    - **精確字數驗證**：調用 `scripts/word_count.py` 並排除 `<!-- -->` 註解塊，確保淨字數 > 3000。
    - **數值更新**：提取侵蝕值、戰損、道具獲得。
4.  **後台同步化 (Backend Sync)**：
    - 產出單一的 `[章節號]_Quality_Audit.md`。
    - 靜默執行 `sync_progress.py` 同步 Roadmap 與 Stats。
5.  **指令**：`生產 V[X] 第 [Y] 章`

---

## 🛑 核心原則 (UPW Rules)
- **行動化設定**：不准大段說明，所有 Lore 必須透過「代價」或「環境反應」引入。
- **單次讀取原則**：在 Planning 階段一次性讀取所有必要設定，避免校對時重複搜尋。
- **暴君規範**：祁渡決策必須符合損益優先、權力收割設定。
- **無成本不爽點**：所有反殺必須有量化的代價支出。

## 觸發指令示例
- 「自動生產 V2 第 2 章」
- 「繼續執行工廠流水線，產出下一章」

## 工作流原則
- **原子化執行**：每個步驟完成後應有內部記錄，確保若中斷可從斷點恢復。
- **一致性優先**：任何步驟若發現與設定集衝突，應停止並詢問用戶。
- **擴展性**：允許在工作流中插入用戶特定的「微修」反饋。
