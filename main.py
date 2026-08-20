import os
import sys
import time

print("hello moqian!")

# 可选：短暂暂停，让窗口停留

time.sleep(5)  # 等待 2 秒后自动关闭

# 通过环境变量控制是否等待输入
wait = os.getenv('WAIT_ON_EXIT', 'false').lower() == 'true'
if wait and sys.stdin.isatty():
    input("按任意键退出")