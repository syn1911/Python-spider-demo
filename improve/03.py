# 列表：

# python 列表list 什么数据类型都能放，
# 声明的区别：
families = ['make', 'beijing', 13, True, 1.48]

# 列表嵌套其他类型：
[['zs', 20], (1, 2, 4), {'name': 'lisi', 'age': 15}]
# 分表嵌套了列表，元组，字典三种结构


# 列表的增删改查
personal_info = ['三上', 28]
personal_info.append(1.74)
print(personal_info)
# 基于索引的修改
personal_info.insert(1, 18)
print(personal_info)

# 修改：
# personal_info[2]=16
# print("三上16岁时的样子",personal_info)
# personal_info[1:3]=['28','16']
# print(personal_info)
#
# # 数据的查询
# print(personal_info[2])
# print(personal_info[1:3])

# 删除数据
# personal_info.pop(1)
# print("16岁才是经典",personal_info)
# print(personal_info)
# personal_info.remove(28)
#
# print("基于给定的值删除",personal_info)

# 基于索引位置删除
# del personal_info[0:2]
# 全部删除
# personal_info.clear()

# del personal_info 删除整个列表


# 列表的合并操作
num1_list = [1, 2, 3, 4]
num2_list = [5, 7, 5, 3]
num3_list = num1_list + num2_list
print(num3_list)
# 排序
num3_list.sort()
print(num3_list)
num3_list.sort(reverse=True)
print(num3_list)
# 反转
num3_list.reverse()
print(num3_list)

# 统计
print(num3_list.count(5))

print(len(num3_list))

# 复制
num_group = [[1, 2, 3], [4, 5, 6]]
# 浅拷贝
num_copy = num_group.copy()
print(num_copy)
# 深拷贝
import copy

num_copy_deep = copy.deepcopy(num_group)
print(num_copy_deep)

print("切片")
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(num[0:10:2])
print(num[::2])
# 列表与for
dogs = ['哈士奇',
        '拉布拉多',
        '边境牧羊犬', ]

for dog in dogs:
    print(dog)

menus = [
    ['拍黄瓜', '夫妻肺片'],
    ['宫保鸡丁', '鱼香肉丝'],
    ['冰激凌', '提拉米苏'],
]
for menu in menus:
    print(menu)

# 打印的还是列表
# 双层遍历
for menu in menus:
    print(menu)
    for food in menu:
        print(food)

# 统计你身边的人
# 数据准备要求：
# 1.拟定一组用户数据可以是你的同事、你的同学
# 2.总数据数量不低于5个
# 3.全部数据放在一个列表中（需要列表嵌套）
# 4.每个人数据需要包含姓名、性别、年龄、籍贯
# 本作业是一个综合体任务，需要用到的内容如下工具：
# 1.for循环
# 2.if else
# 3.列表操作
# 4.索引取值操作
# 输出要求：
# 1.请将男同胞放在一个新列表中（统计数量）
# 2.请将女同胞放在一个新列表中（统计数量）
# 3.请将年龄大于30岁的人放在一个列表中（统计数量）
# 4.找出最大和最小年龄分别是多少
# 5.将所有人的籍贯放在一个新列表中

# 分析：
person_no_nearby = [
    ['张宇', '男', 24, '河北'],
    ['王丽娜', '女', 33, '陕西'],
    ['李萍', '女', 28, '山东'],
    ['徐晴', '女', 25, '四川'],
    ['马潇潇', '男', 34, '四川'],
    ['张晓', '男', 27, '陕西']
]
# 1:
male = []
female = []
age30 = []
address = []
max_and_min_age = []
for p in person_no_nearby:
    max_and_min_age.append(p[2])
    if p[1] == '男':
        male.append(p)  # 1
        if p[2] > 30:  # 3
            age30.append(p)
        if p[3] not in address:
            address.append(p[3])  # 5
    else:
        female.append(p)  # 1
        if p[2] > 30:  # 3
            age30.append(p)
        if p[3] not in address:
            address.append(p[3])  # 5

print(male)
print(female)
print(age30)
print(address)
print(max(max_and_min_age))
print(min(max_and_min_age))
