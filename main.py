import os
import sys

print("hello moqian!")

# 通过环境变量控制是否等待输入
wait = os.getenv('WAIT_ON_EXIT', 'false').lower() == 'true'
if wait and sys.stdin.isatty():
    input("按任意键退出")