import os
import re

def sync_upw_progress():
    workspace_root = "/Users/george/Library/CloudStorage/OneDrive-MSFT/0.專案/novel/novel_Abyss"
    manuscript_dir = os.path.join(workspace_root, "manuscript")
    roadmap_path = os.path.join(workspace_root, "planning/08-roadmaps/執行排程.md")
    
    # 章節識別正則 (支援 Ch01, Ch1, 第1章 等)
    ch_pattern = re.compile(r"(?:Ch|第)(\d+)")
    
    completed_chapters = set()
    stat_updates = []
    foil_tags = []

    print(f"Scanning manuscripts in: {manuscript_dir}")
    
    for root, dirs, files in os.walk(manuscript_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                        # 檢查製作完成標記
                        if "DoD 驗收通過" in content:
                            match = ch_pattern.search(file)
                            if match:
                                ch_num = int(match.group(1))
                                # 判斷屬於哪一卷 (基於父目錄)
                                volume = os.path.basename(root)
                                completed_chapters.add((volume, ch_num))
                        
                        # [Future] 提取 STAT 與 FOIL 標籤
                        # stats = re.findall(r"<!-- STAT: (.*?) -->", content)
                        # foils = re.findall(r"<!-- FOIL: (.*?) -->", content)
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    # 更新 Roadmap
    if os.path.exists(roadmap_path):
        try:
            with open(roadmap_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            new_lines = []
            for line in lines:
                updated_line = line
                # 簡單邏輯：如果行中包含章節數字且在正確的卷區域 (策略上可精化)
                # 目前採通用匹配，將 [ ] 改為 [x]
                for vol, ch_num in completed_chapters:
                    # 匹配 "5. " 這種格式的列表項
                    if re.search(rf"^\s*{ch_num}\.\s+.*\[ \]", line):
                        updated_line = line.replace("[ ]", "[x]")
                        break
                new_lines.append(updated_line)
                
            with open(roadmap_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print(f"UPW Sync: Updated roadmap for {len(completed_chapters)} chapters.")
        except Exception as e:
            print(f"Error updating roadmap: {e}")

if __name__ == "__main__":
    sync_upw_progress()
