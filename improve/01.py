# 提高篇，必须学习1-14中的语法内容，不然可能不懂分析过程
# 变量
# 1.首先找到3个人的身份证号。
# 2.放到3个变量中。
# 3.然后用切片工具把每个人的生日找出来并打印出来

# 分析:
#  首先创建一个列表，存放三个身份号码
# 然后通过遍历的方式，找出列表数字的生日

# 按照上面的要求分析：
#  定义三个变量，
# 然后切片找出生日，并打印

# 自己的方式
idCard = ['110120194906066533', '110120194908086533', '110120194902026533']
for ids in idCard:
    print("自己的思路")
    print("生日分别为" + ids[10:14])

# 要求的思路

idCard1 = '110120194906066533'
idCard2 = '110120194908086533'
idCard3 = '110120194902026533'


def id_card_split(ids):
    print("传入的身份证号的生日为：" + ids[10:14])


id_card_split(idCard1)
id_card_split(idCard2)
id_card_split(idCard3)


# 变量的类型转换
my_age=18
my_new_age=str(my_age)
print(my_new_age)
room_number="1008"
room_new_number=int(room_number)
print(room_new_number)
tick_price=5.3
tick_new_price=float(tick_price)
print(tick_new_price)



# 打印占位符

name='zhangsan'
age=18
print("我的名字是%s,我的年龄是%s"%(name,age))

name='lisi'
age=28
print("我的名字是{0},我的年龄是{1}".format(name,age))

name='wangwu'
age=17
# 注意需要加个f
print(f"我的名字是{name},我的年龄是{age}")



