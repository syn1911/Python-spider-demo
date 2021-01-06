# 条件语句
cars = ['aUdi', 'bMw', 'subVru', 'toYota']
# for car in cars:
#     if car == 'bMw':
#        print(car.upper())
#     else:
#         print(car.title())

# for carss in cars:
#     print(carss=='toYota')
#     print(carss=='subVru')

# 忽略大小写
# for carss in cars:
#         print(carss.lower() == 'audi')
#         print(carss.lower() !='toyota')


age_0=20
age_1=20
# 条件同时满足
# print(age_0>=10 and age_1>21)
# print(age_0>=10 and age_1>19)
# 满足其中一个条件即可
# print(age_0>=300 or age_1>21)
# print(age_0>=10 or age_1>19)

# 判断某个值是否在其中
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print("某个元素是否在列表中-->",'mushrooms'in requested_toppings)
# print("某个元素是否在列表中-->",'pepperoni'in requested_toppings)
#
# print("某个元素是否不在列表中-->",'pepperoni' not in requested_toppings)
# print("某个元素是否不在列表中-->",'mushrooms'not in requested_toppings)


# if demo
age=19
if age>=18:
    print("符合条件")


# if  eles

if age<17:
    print("lalal")
else:
    print("jijiu")

# if  elesif else

age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")

# if 对列表的影响
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# 制作披萨的步骤
# for  add_veg in requested_toppings:
#     print("add",add_veg)


# 如果材料中，某个食材没有了，就告诉其没有

# for  add_veg in requested_toppings:
#     if add_veg=='extra cheese':
#         print("奶酪没有了，暂时不能制作")
#     else:
#         print("继续制作披萨")

# 定义空列表
# requested_toppings = []
# requested_toppings = list(range(1,5))  #非空列表
# if requested_toppings:
#     for requess in requested_toppings:
#          print("正在制作中")
#
#     print("披萨制作完成")
# else:
#     print("没有原材料是否需要买别的吃的")



# 多个列表的使用
# 原料表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']

# 顾客需要的口味表
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# 原料是否在都在两个列表中，存在就可以制作
for req in requested_toppings:
    if req in available_toppings:
        print("Adding " + req + ".")
    else:
        print("Sorry, we don't have " + req + ".")

print("\nFinished making your pizza!")

# java  for 循环   for(int i=0;i<10;i++)
# python用  for s in range(10)

for s in range(10):
    print("for 循环了："+str(s)+"次")
