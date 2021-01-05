# 列表使用
# 可以理解成数组的包装类，因为此类什么类型的元素都能放进去
list1=['math','eartch',1997,2000]
list2=[1, 2, 3, 4, 5, 6, 7 ]
print(list2[2])
print(list2[3])
print(list1[1])
print(list1[3])

print(list1[0].title())
# 返回最后一个元素的方法
print(list1[-1])
# 添加与修改
list1.append("world")
print(list1)
# 更新
list1[0]='MATCH'
print(list1)
# 删除不使用值
del list1[1]
print(list1)

# 删除并且返回删除的值

prp=list1.pop()
print("删除的元素。并且弹出的值为"+prp)
# 弹出任意位置
prp2=list2.pop(2)
print(prp2)
print(list2)


# 根据相应的 值删除
list1.remove(2000)
print(list1)


# 列表的顺序

cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

# 前面是永久排序
# 排序反转
cars.sort(reverse=True)
print(cars)

# 临时排序
print("原来顺序",cars)
print("临时排序顺序",sorted(cars))
print("测试时临时排序还是原来的排序",cars)

# 列表的反转
cars.reverse()
print(cars)
# 列表的长度
print("列表的长度",len(cars))


# 列表的遍历操作
for car in cars :
    print(car)

# 魔术师
magicians = ['alice', 'david', 'carolina']

# for magic in magicians:
#     print("表演的太好了",magic.title())
   
# # 缩进行演示
# for magic in magicians:
#     print("表演的太好了",magic.title())
#     # 会执行三次
#     print("魔术师",magic.title(),"很期待你的下次表演")
# 测试执行的次数
i =0
for magic in magicians:
    print("表演的太好了",magic.title())
    print("for循环 我执行了")
    i+=1
    # 会执行三次
    print("魔术师",magic.title(),"很期待你的下次表演","i的次数为"+str(i))
print("我在顶头缩进了---所以我会执行一次。。。")    




# 数据的生成
for value in  range(1,10):
    print(value)


# 转换成列表

numbers=list(range(1,6))    
print(numbers)


# 生成偶数代码;khbn
for  oushu in range(2,20,2):
    print("生成的偶数为"+str(oushu))



# 数据进行统计
num=list(range(1,100))
print(min(num))
print(max(num))
print(sum(num))


# 列表解析
# 就是将几行代码柔和成一行
squars=[vs**2 for vs in range(1,10)]
print(squars)


# 取列表的中的部分元素

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 取前三个元素
print(players[0:3])
# 取从第二个到第四个元素
print(players[1:4])

# 这样取不智能怎么去解决？

# 不指定索引开头，取三个元素
print(players[:3])
# 指定索引。不指定范围
print(players[3:])
# 指定负数，从列表的最后一位开始打印
print(players[-1:])
print(players[-3:])


# 遍历列表中个部分数据
for play in players[0:3]:
    print(play)


# 列表的拷贝
newList=players[:]
for lis in  newList:
    print("新列表为"+lis)
# 列表的用途
# 列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的


# 元组
# 有时候你需要创建一系列不可修改的元素，
# 元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组


#  dimensions = (200, 50)
#  print(dimensions)
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
   print(dimension)



lktbz=("zs","lisi","wangwu","zhaoliu")
for lk in  lktbz:
    print(lk)

# 给元祖赋值
lktbz=("zs","lisi","wangwu","zhaoliu","tianzhilan")
print(lktbz)
# 不能更改
# print(lktbz[0]="lkt")