---
description: 自動化呼叫 Western Novel Adapter 將中文章節轉換為西方網文風格英文草稿的標準作業流程。
---

# 西方網文自動化改編 SOP (Automated Western Adaptation Workflow)

本 SOP 旨在指導 Agent 如何不間斷地、高品質地將 `manuscript/` 中的中文原稿，轉換為符合 Royal Road / Progression Fantasy 口味的英文稿件，並存入 `manuscript_en/` 目錄。

## 🎯 前置條件 (Prerequisites)
- 確認目標中文章節已完成初步撰寫或擴寫。
- 確認已了解並載入 `western_novel_adapter` 技能包 (`.agent/skills/western_novel_adapter/SKILL.md`)。

## ⚙️ 執行步驟 (Execution Steps)

當使用者下達「自動改寫 [章節編號/範圍]」的指令時，Agent 必須嚴格執行以下循環：

### 步驟一：分析與讀取 (Analysis & Read)
1. 讀取目標中文章節 (例如 `manuscript/V1-裂谷啟封/Ch01-裂谷醒轉.md`)。
2. 提取該章的：
   - **核心推進 (Core Progression)**：主角學到了什麼、得到了什麼？
   - **高潮/衝突點 (Action Set-piece)**
   - **結尾斷章 (The Hook)**：確認原稿結尾是如何掛懸念的。

### 步驟二：分段改編 (Segmented Adaptation)
> **⚠️ 警告：LLM 的輸出字數有限制。為了確保達到西方網文每章 1500~2500 英文字的標準，請不要試圖一次生成整章。**
1. 將中文章節在邏輯上切分為 2 到 3 個段落（Scene 1, Scene 2, Scene 3）。
2. 使用 `western_novel_adapter` 技能包的規則，開始對 **第一個段落** 進行改編。
3. **Pulp Prose 檢查**：確保沒有冗長的環境描寫，將被動語氣轉為主動，增強動作感。
4. **內心獨白注入**：將中文原文中主角的「心理狀態描寫」，替換為「直接的 *斜體* 內心獨白」。
5. 完成後，繼續對後續段落進行相同的改編，確保前後文邏輯連貫。

### 步驟三：自我審議 (Self-Correction & Quality Control)
1. 在將所有段落拼合為一個完整英文檔案前，Agent 必須進行一次「Royal Road 讀者視角」的快速審查：
   - 系統提示/介面 (如 `[ALERT]`) 是否清晰且統一？
   - 此章節的字數是否至少超過 1500 英文字？
   - **最重要的一點**：最後一段是否有足夠的 Cliffhanger (斷章懸念) 讓人想看下一章？如果沒有，主動增寫或強化最後一句話的張力。

### 步驟四：存檔與更新索引 (Save & Update)
1. 將最終核可的英文內容與原始中文內容，以「**一段中文、一段英文**」的對照方式寫入對應的目錄中。
   - 例如：`manuscript_en/V1-Rift_Awakening/Ch01-Rift_Awakening.md`。
2. 開啟 `manuscript_en/README.md`。
3. 在對應的章節清單勾選完成 (`[x]`)。
4. 在對話中向 User 簡報該章的字數與修改亮點。

---

## 💡 常用觸發指令
- `執行 02_西方網文自動化改編_SOP.md，目標：處理第一卷的 Ch01 與 Ch02。`
