import tkinter as tk
from tkinter import filedialog

def convert_srt_to_vtt(srt_file_path, vtt_file_path):
    with open(srt_file_path, 'r', encoding='utf-8') as srt_file:
        srt_content = srt_file.read()

    vtt_content = "WEBVTT\n\n" + srt_content.replace(',', '.')

    with open(vtt_file_path, 'w', encoding='utf-8') as vtt_file:
        vtt_file.write(vtt_content)

def main():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    srt_file_path = filedialog.askopenfilename(
        title="选择SRT文件",
        filetypes=(("SRT文件", "*.srt"), ("所有文件", "*.*"))
    )

    if srt_file_path:
        vtt_file_path = srt_file_path.rsplit('.', 1)[0] + '.vtt'
        convert_srt_to_vtt(srt_file_path, vtt_file_path)
        print(f"转换完成: {vtt_file_path}")

if __name__ == "__main__":
    main()