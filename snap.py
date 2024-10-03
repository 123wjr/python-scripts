import os
import subprocess
import time

# 视频文件夹和截图保存路径
video_folder = ""
screenshot_folder = ""

# 确保截图保存路径存在
os.makedirs(screenshot_folder, exist_ok=True)

# 遍历文件夹中的视频文件
for root, _, files in os.walk(video_folder):
    for file in files:
        # 检查文件扩展名，确认是视频文件
        if file.endswith(('.mp4', '.avi', '.mkv', '.mov')):
            video_path = os.path.join(root, file)
            print(f"Processing video: {video_path}")
            output_pattern = os.path.join(screenshot_folder, f"{os.path.splitext(file)[0]}_%03d.jpg")

            if any(os.path.exists(output_pattern.replace('%03d.jpg', f"{str(i).zfill(3)}.jpg")) for i in range(1000)):
                print(f"已存在截图，跳过: {video_path}")
                continue
            # 每个视频的截图点
            start_time = 60
            screenshot_count = 1
            dirStr, ext = os.path.splitext(video_path)
            file_folder = dirStr.split("\\")[-1]
            while True:
                # 定义截图命令
                screenshot_command = [
                    'ffmpeg',
                    '-ss', str(start_time),  # 从当前时间点开始截图
                    '-i', video_path,
                    '-frames:v', '1',  # 只截图一帧
                    os.path.join(screenshot_folder,file_folder+f'_{screenshot_count:03d}.jpg')
                ]

                # 运行截图命令
                try:
#                    time.sleep(5)  # 提供缓冲时间
                    subprocess.run(screenshot_command, check=True)
                    print(f"Screenshot saved: {os.path.splitext(file)[0]}{screenshot_count:03d}.jpg")
                except subprocess.CalledProcessError as e:
                    print(f"Error processing {file}: {e}")
                    break

                screenshot_count += 1
                start_time += 900 # 跳转到下一个截图点前5秒

                # 结束条件：可根据视频长度来设置
                # 这里可以添加获取视频时长的逻辑来退出循环
                # 例如：如果 start_time >= video_duration，则跳出循环

print("All videos processed.")
