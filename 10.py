# 文件 io 操作
# 文件的路径，在Linux和OS X
# with open('text_files/ filename .txt') as file_object
# file_path = '/home/ehmatthes/other_files/text_files/ filename .txt'
# 在windows 中
# with open('text_files\ filename .txt') as file_object
# file_path = 'C:\Users\ehmatthes\other_files\text_files\ filename .txt'

# 读取文件实例
name='F:a.txt'
# with open("F:a.txt") as n:
#    cont= n.read()
#    print(cont)
# 读取一行加快速度
# with open(name)as file_onj:
#     for sin in file_onj:
#         print(sin)


# 去空格

# with open(name)as file_onjj:
#     for nam in file_onjj:
#         print(nam.strip())


# 扩大作用域

# 使用关键字 with 时， open() 返回的文件对?只在 with 代码?内可用。如果要在 with 代码?外
# ?问文件的内容，可在 with 代码?内将文件的各行存储在一个列表中，并在 with 代码?外使用该
# 列表：你可以?即处理文件的各个部分，也可??到程序后面再处理。
#
# with open(name) as fle:
#     lists=fle.readlines()
#
# # 作用域外遍历
# for ins in lists:
#     print(ins.strip())

# 使用读取的内容数据
file='F:b.txt'
# piString=''
# with open(file)as infle:
#     lins=infle.readlines()
#
# for line in lins:
#     piString+=line.strip()
#
# print(piString)
# print(len(piString))


# 文件的写入
filename ='programming.txt'
# with open(filename,'w')as wir:
#     wir.write("l love python...")

# 写入多行

# with open(filename,'w')as wLine:
#     wLine.write("i love python\n")
#     wLine.write("i love python\n")
#     wLine.write("i love python\n")


# with open(filename,'w')as nLo:
#     nLo.writelines("sdjsks")
#     nLo.writelines("sdjsks")
#     nLo.writelines("sdjsks")
#     nLo.writelines("sdjsks")

# 上面的写文件全是直接覆盖
# 现在是追加操作
# with open(filename,'a')as apen:
#     apen.write("i love python\n")
#     apen.write("i love java\n")
#     apen.write("i love c++\n")
