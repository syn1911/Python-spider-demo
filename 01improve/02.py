# if else for while 使用

# 设计概述：
# 给定一个购物总金额，然后判断当前条件符合哪种优惠

# 优惠条件：
# 前提条件：如果关注本店铺，可以领取10元无门槛优惠券。
# 1.总购物金额大于等于500元，可使用满减优惠券100元，包邮
# 2.总购物金额大于等于300元，可使用满减优惠券50元，包邮
# 3.总购物金额大于等于100元，可使用满减优惠券20元，包邮
# 4.总购物金额小于100元，没有满减券，并且增加10元运费

# 制作工具：
# 1.逻辑运算
# 2.逻辑语句
# 3.多则运算


# 定义一个函数，输入金额，来判断符合什么优惠条件

def price_level(price, isFllow):
    if isFllow:
        if price >= 500:
            print("可使用满减优惠券100元")
        elif price >= 300 and price < 500:
            print("可使用满减优惠券50元")
        elif price >= 100 and price < 300:
            print("可使用满减优惠券20元")
        else:
            print("没有满减券，并且增加10元运费")
    else:
        print("请先关注本店，领取10元无门槛优惠券")


# price_level(200, False)
price_level(200, True)
price_level(60, True)
price_level(320, True)
price_level(660, True)

# 1.使用for循环输出打印0-100之间的偶数
# 3.使用while循环结合input做一个猜价格的程序
# 2.使用while循环计算0-100之间数字的总和
# 4.使用while循环结合input做一个模拟登陆系统，
# 只有密码和账号同时正确才显示登陆成功，否则让用户重试
# for ins in range(0, 101,2):
#     print(ins)

# while True:
#     price = input("请输入你心里想的价格:范围在1-10之间")
#     if price == '5':
#         print("恭喜你价格猜对了")
#         break
#     else:
#         print("价格不对请重新输入...")
#

# total=0
# for i in range(0,101):
#     total=total+i
#
# print(total)

while True:
    username=input("请输入用户名：")
    password=input("请输入密码：")
    if username=='zs' and password=='1234':
        print("恭喜你登录成功")
        break
    else:
      print("请重新输入用户名和密码")



