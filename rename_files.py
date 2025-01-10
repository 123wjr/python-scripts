import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            match = re.match(r"(.*?)(\d+-\d+)", filename)
            if match:
                new_name = f"{match.group(2)}{match.group(1)}.md"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
                print(f"Renamed: {filename} -> {new_name}")

# 替换为你的目录路径
directory_path = ""
rename_files(directory_path)