# 元组
# 元组特点：
# 不可修改
# 两种声明方式
# tuple_data=tuple()
# tuple_data=()
tuple_data = ('bj', 'tj')
# 嵌套
(['mike', 28], ['Jason', 36], (1, 2, 3), {' 名字 ': '正正 ', ' 爱好 ': ' 编程 '})

# 元组的操作
personal_infos = ("大正", 18, "男", 1.74, "北京")

print(personal_infos[0])
print(personal_infos[0:2])

# 元组的删除
del personal_infos
# 拼接
num_1 = (1, 2, 3)
num_2 = (4, 5, 6)
new_num = num_2 + num_1
print(new_num)

# 元组与列表的转换

list_data = [1, 2, 3]
new_tuple = tuple(list_data)
print(new_tuple)

# 元组通过变量直接取值
personal_infos = ("大正", 18, "男", 1.74, "北京")
name, age,male, height, city = personal_infos
print(name)
print(age)
print(male)
print(height)
print(city)
# 统计
message=(1,2.3,4,5,6,7,8,9)
print(message.count(2))
# 复制
ms=message*3
print(ms)
# 长度
print(len(ms))

# 遍历

dogs = ('哈士奇',
        '拉布拉多',
        '边境牧羊犬', )

for dog in dogs:
    print(dog)

menus = (
    ('拍黄瓜', '夫妻肺片'),
    ('宫保鸡丁', '鱼香肉丝'),
    ('冰激凌', '提拉米苏'),
)
for men in menus:
    print(men)