import os
import json
import re

MANUSCRIPT_DIR = "manuscript"
OUTPUT_FILE = "novel_data.js"
EXCLUDE_FILES = ["README.md", "00-前言與核心檢核.md"]

def extract_title(content, fallback):
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return fallback

def bundle():
    novel_data = []
    
    # Walk through the manuscript directory
    for root, dirs, files in os.walk(MANUSCRIPT_DIR):
        # Sort files to maintain chapter order if possible
        files.sort()
        for file in files:
            if file.endswith(".md") and file not in EXCLUDE_FILES:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ".")
                
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                title = extract_title(content, file.replace(".md", ""))
                
                novel_data.append({
                    "path": rel_path,
                    "title": title,
                    "content": content
                })

    # Sort the data by path naturally
    # (Simple sort here, app.js has more complex sorting which we will utilize)
    novel_data.sort(key=lambda x: x["path"])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("window.NOVEL_DATA = ")
        json.dump(novel_data, f, ensure_ascii=False, indent=2)
        f.write(";")

if __name__ == "__main__":
    bundle()
    print(f"Successfully bundled {OUTPUT_FILE}")
