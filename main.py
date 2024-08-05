import tkinter as tk
import os
import webview
import datetime

def close_window():
    webview.terminate()

# 获取当前工作目录
current_dir = os.getcwd()  # 使用os.getcwd()获取当前工作目录

# 获取当前时间
now = datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=8)))

# 根据当前时间选择HTML文件
if now.hour < 21:
    html_file_path = os.path.join(current_dir, 'lightworking.html')
else:
    html_file_path = os.path.join(current_dir, 'nightworking.html')

# 创建Webview窗口，设置窗口标题、文件路径、宽度、高度、是否可调整大小和是否无边框
webview.create_window('HTML Viewer', html_file_path, width=600, height=250, resizable=True, frameless=True)

# 启动事件循环
webview.start()