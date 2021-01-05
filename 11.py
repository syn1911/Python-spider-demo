# 异常


# print(5/0)
# try 铺货异常
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("你可以继续执行么？？")

# 使用异常来优雅的让程序结束运行，而非报错
print("请出入两个数字，我会计算之和")
print("记住，当你输入‘q’时我将结束运行")
# while True:
#     f_number = input("请出入第一个数")
#     if f_number == 'q':
#         break
#     s_number = input("请输入第二个数")
#     if s_number == 'q':
#         break
#     answer = int(f_number) / int(s_number)
#     print("两个数字之和为", answer)
# 从上面的程序可以看出，过于理想化
# 对输入的数字没有加以矫正，如果出入的是0，怎么办？
# while True:
# f_number = input("请出入第一个数")
# if f_number == 'q':
#     break
# s_number = input("请输入第二个数")
# if s_number == 'q':
#     break
# try:
#     answer = int(f_number) / int(s_number)
#     print(answer)
# except:
#     ZeroDivisionError
#     print("输入的数字不合法，必须大于0")
#     break
# else 语句块，放入执行正确的
# while True:
#     f_number = input("请出入第一个数")
#     if f_number == 'q' and f_number == '0':
#         break
#     s_number = input("请输入第二个数")
#
#     if s_number == 'q':
#         break
#     try:
#         answer = int(f_number) / int(s_number)
#     except:
#         ZeroDivisionError
#         print("输入的数字不合法，必须大于0")
#     else:
#         "执行正确。需要走的"
#         print(answer)


# 程序中异常的处理方式
# filename = 'alice.txt'
filename = 'programming.txt'
# try:
#     with open(filename) as f_obj:
#         ooj = f_obj.read();
#         print(ooj)
# except FileNotFoundError:
#     msg = "不好意思，没有找到文件夹"
#     print(msg)

# 读取文件，如果文件不存在，则抛出异常，
# 如果文件存在。不好意思么，就统计文字的数量
# try:
#     with open(filename)as fio:
#         context = fio.read()
# except FileNotFoundError:
#     print("不好意思。文件暂时不存在")
# else:
#     les = len(context)
#     print("文件中数量为", les)




