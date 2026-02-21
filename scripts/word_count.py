import os
import re
import sys

def count_novel_characters(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return 0

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. 移除 <!-- ... --> 註解塊 (DoR, GOCRSH 等)
        # flags=re.DOTALL 確保跨行匹配
        clean_content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

        # 2. 移除 Markdown 語法標籤 (可選，通常小說統計建議保留標點)
        # 這裡我們主要針對「純文字內容」進行統計
        
        # 3. 統計畫線、標題符號以外的有效字數
        # 方案：計算中文字、英文字詞、數字
        # 中文範圍: \u4e00-\u9fff
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', clean_content))
        # 標點符號與其他 (含標點)
        # 如果 user 習慣的是「含標點總字數」，則直接 len(clean_content.strip())
        
        # 為了對齊一般寫作軟體，我們計算「非空白」的總字數 (排除註解後)
        total_text = re.sub(r'\s+', '', clean_content)
        total_count = len(total_text)

        print(f"File: {os.path.basename(file_path)}")
        print(f"Total (Clean): {total_count} characters")
        print(f"Chinese: {chinese_chars}")
        
        return total_count

    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count_novel_characters(sys.argv[1])
    else:
        print("Usage: python3 word_count.py [file_path]")
