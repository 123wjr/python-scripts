import sqlite3
import os

# 获取Anki配置文件路径
def get_anki_prefs_path():
    if os.name == 'nt':  # Windows
        return os.path.expanduser(r'~\AppData\Roaming\Anki2\prefs21.db')
    elif os.name == 'posix':  # macOS/Linux
        return os.path.expanduser('~/.local/share/Anki2/prefs21.db')
    else:
        raise Exception("Unsupported OS")

# 更新配置项
def update_new_timeline_handling():
    prefs_path = get_anki_prefs_path()
    conn = sqlite3.connect(prefs_path)
    cursor = conn.cursor()
    
    # 更新newTimeline配置项
    cursor.execute("UPDATE prefs SET val = '0' WHERE key = 'newTimeline'")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_new_timeline_handling()
    print("New Timeline handling 已关闭")