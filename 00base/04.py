# 字典结构
# 加单的字典结构
alien_0={'color':'green','point':5}
print(alien_0['color'])
print(alien_0['point'])

# 获取原来的点数，并增加自己的点数
people_0={'color':'red','point':10}
print("我自己存在的分数为：",people_0['point'])

newPoints=alien_0['point']
print("打败NPC，获取的分数为",newPoints)
print("此分数将加到我自己上")
people_0['point']=15
print("我自己存在的分数为：",people_0['point'])

# 字典结构字段增加
alien_0['x_point']=0
alien_0['y_point']=25
# 增加坐标字段
print(alien_0)

# 字段的删除
del alien_0['x_point']
print(alien_0)


# 字段的遍历
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for k,v in user_0.items():
    print("key=="+k+".value=="+v)

print(len(user_0))
print(user_0.keys())
print(user_0.values())

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


# for name, language in favorite_languages.items():
#   print(name.title() + "'s favorite language is " +language.title() + ".")

# 获取key
# for name in favorite_languages.keys():
#     print(name.title())

# 通过key 找寻对应的value
#   定义两个key 匹配的话查询相应的value
# lista=['phil','sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in lista:
#       print(" Hi " + name.title() +", I see your favorite language is "+favorite_languages[name].title() + "!")

# 顺序遍历
for name in sorted(favorite_languages.keys()):
    print(name.title()+",thank you for taking the poll.")


# 遍历所有的值
for name in favorite_languages.values():
    print(name.title())


# 字段的去重
for name in set(favorite_languages.values()):
    print("去重复后：",name.title())

# 嵌套的使用
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points': 15}
aliens=[alien_0,alien_1,alien_2]
# for lin in aliens:
#     print(lin)


# 自动生成对象
alis=[]
for ali_number in range(30):
    new_alin={'color': 'green', 'points': 5}
    alis.append(new_alin)
# 遍历全部
# for al in alis:
#     print(al)
#遍历显示前五个
for al in alis[:5]:
    print(al)

print("创建了多少个对象?  "+str(len(alis))+"个")


# 字典中存储列表案例
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}

# for k,v in pizza.items():
#     print(k,"====",v)


# 遍历字典中的列表
for tp in pizza['toppings']:
    print(tp)

# 使用双层嵌套方式

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name,language in favorite_languages.items():
    print(name.title(),"热爱的语言是：")
    for lan in language:
        print(lan.title())

# 字典中存储字典
# users = {
# 'aeinstein': {
# 'first': 'albert',
# 'last': 'einstein',
# 'location': 'princeton',
# },
# 'mcurie': {
# 'first': 'marie',
# 'last': 'curie',
# 'location': 'paris',
# },
# }
# 根据上面的创建对应的字典
users={};
aeinstein={
     'first': 'albert',
     'last': 'einstein',
     'location': 'princeton',
    }
mcurie={
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
}
# 组装数据
users['aeinstein']=aeinstein
users['mcurie']=mcurie
print(users)
# 遍历拼接
for user_name,user_info in users.items():
    print("\nUsername: " + user_name)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())