# 用户输入以及while 循环
# name =input("小伙子请输入你的名字")
# print("我获取到了你的名字：",name)
# 提示字段过长，就封装到一个变量中
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(name)


# 获取数字类型
# age=input("年轻人你的年纪是多少？")
# age=int(age)
# print(age)

# height = input("How tall are you, in inches? ")
# height=int(height)
# if height>20:
#     print("lallalala")
# else:
#     print("error....")

# 运算 奇偶数
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number=int(number)
# if number%2==0:
#     print("是偶数哟。。。")
# else:
#     print("是奇数哟。。。")


# while 循环

# count=1
# while count<10:
#     print(count)
#     count+=1


# 让用户选择退出 ，此段代码，可以拿来在小侄子面前，秀秀了 哈哈哈
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message!='quit':
#     message = input(prompt)
#     print(message)
# cout=10
# message=""
# while cout!=0:
#     message=input("小伙子，请输入1-10之间的数字，你能才对我所想的么？")
#     if message !='9':
#         print("小伙子，你猜的不对哟，请接着输入你猜的数字")
#         cout-=1
#     else:
#         cout=0
#         print("恭喜你才对了，这就是我的数字-->",message)

# 退出循环操作
# 使用boolean 条件
# active=True
# while active:
#     msg=input("请出入你所想的？")
#     if msg=='exit':
#         active=False
#     else:
#         print(msg)

# break 退出循环条件

# while True:
#     msg=input("请输入你所想的字段")
#     if msg =='exit':
#         break
#     else:
#         print(msg)
# 1-10值打印偶数的循环

# coun = 0
# while coun < 10:
#     coun += 1
#     if coun % 2 != 0:
#         continue
#     print("偶数为", coun)

# for ??是一种遍历列表的有效方式，但在 for ??中不应修改列表，否则将导致Python难以
# 跟?其中的?素。要在遍历列表的同时对其进行修改，可使用 while ??。通过将 while ??同列
# 表和字?结合起来使用，可收集、存储并组织大量输入，供以后查看和显示
# for 循环不能修改列表，要使用修改，必须用 while 循环
# 带确认的用户
unconfirmed_users = ['alice', 'brian', 'candace']
# 存储验证用户
confirmed_users = []

# 将待确认中的用户，移动到验证用户中，最后并且打印
# while unconfirmed_users:
#     user_name = unconfirmed_users.pop()
#     print("要验证的用户为", user_name)
#     confirmed_users.append(user_name)
#
# for cons in confirmed_users:
#     print("验证通过的用户为", cons)

# 删除列表中特定的值
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)
