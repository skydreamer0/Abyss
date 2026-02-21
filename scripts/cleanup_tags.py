import os
import re
import sys

def cleanup_sensory_tags(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # 匹配 [VISUAL: ...], [AUDIO: ...], [SCENT: ...] 或單獨的 [VISUAL]
    tag_pattern = re.compile(r"\[(VISUAL|AUDIO|SCENT).*?\]", re.IGNORECASE)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = tag_pattern.sub("", content)
        
        # 移除標籤產生的多餘空行 (可選)
        new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

        if content != new_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Cleaned sensory tags from: {file_path}")
        else:
            print(f"No sensory tags found in: {file_path}")
            
    except Exception as e:
        print(f"Error during cleanup: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cleanup_sensory_tags(sys.argv[1])
    else:
        print("Usage: python3 cleanup_tags.py [file_path]")
