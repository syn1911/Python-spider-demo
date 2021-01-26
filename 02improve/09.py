# os.path 库学习
# import os.path

from os import path

# 路径
print(path.abspath("F:\\a.txt"))
# 文件名称
print(path.basename("F:\\a.txt"))
# 判断是否是文件
print(path.isfile("F:\\a.txt"))
print(path.isfile("F:\Temp\TxGameDownload"))

# 拆分目录与文件
print(path.split("F:\\jsr\\bluetooth-1_1-mrel-spec\\jsr-82.JABWT-Spec.pdf"))

# 将文件与路径合并
print(path.join("root","test.txt"))

# 2021年4月-converted.xlsx
import time
file="F:\\自考准备\\2021年4月-converted.xlsx"
time_file=path.getatime(file)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 文件最近修改时间
# 文件最近修改时间
# 文件最近修改时间
print(time.gmtime(path.getatime(file)))







