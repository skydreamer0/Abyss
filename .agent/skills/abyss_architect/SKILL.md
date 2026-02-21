---
name: Abyss Architect
description: 專門用於網路上搜尋深淵相關靈感（科學、神話、克蘇魯），並將其翻譯為小說故事架構與設定。
---

# 深淵架構師 (Abyss Architect)

本技能旨在通過外部研究（Web Search），為《深淵》系列提供具備科學真實感或神話厚度的擴展設定。

## 🎯 核心任務 (Objectives)
1.  **外部溯源**：從現實世界的深海科學（Abyssal Zone）、黑洞物理、地質奇觀或神話禁忌中提取「異質元素」。
2.  **小說編譯**：將「外部數據」轉化為符合本作設定（如「侵蝕度」、「序列強度」、「污染規則」）的遊戲化/小說化語言。
3.  **架構錨定**：將新設定寫入 `settings/` 目錄，並確保與現有 lore 衝突最小化。

## 🔍 搜尋 SOP (Search Guidelines)
當接到「擴展 [主題]」指令時，應進行多維度搜尋：
-   **維度 A：深海與地質 (Science)**
    -   關鍵字：`deep sea bioluminescence`, `hadal zone creatures`, `abyssal trench geology`, `hydrothermal vent life`.
-   **維度 B：神話與禁忌 (Occult/Myth)**
    -   關鍵字：`Tartarus levels`, `Cthulhu Mythos cycle`, `abyssal monsters in folklore`.
-   **維度 C：架構靈感 (Structure)**
    -   關鍵字：`nested environments`, `megastructure architecture concepts`, `vertical leveling design`.

## 🛠️ 擴展邏輯 (Translation Logic)
提取內容後，必須通過以下濾鏡進行「本地化」：
-   **環境轉化**：現實的「極壓」轉化為本作的「精神重壓/侵蝕」。
-   **生物轉化**：深海生物的「感官退化」轉化為「反直覺攻擊模式」。
-   **代價原則**：任何強大設定必須包含「使用代價 (Corruption Cost)」。

## 📌 整合工作流 (Integration Flow)
1.  **Drafting**：生成一份 `[主題]_Research_Draft.md` 供用戶審閱。
2.  **Mapping**：決定存放路徑：
    -   物理規則 → `settings/01-世界觀/`
    -   生物 → `settings/06-生態與生物/`
    -   物品 → `settings/04-物件圖鑑/`
3.  **Syncing**：更新對應目錄的 `README.md` 索引。

## 💡 指令示例
-   「使用 Abyss Architect 搜尋關於『深海盲目魚』的特徵，並為卷三擴展一個新的深淵生物設定。」
-   「研究『地獄層級結構』並優化 `settings/01-世界觀` 中的深淵分層架構。」
