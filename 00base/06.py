# 函数
def gree_user():
    print("hello function")


# 调用
# gree_user()

def gree_user_param(username):
    print("hello:", username)


# 调用带参数的
# gree_user_param('lktbz')


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 传递参数
# 传递实际参数
# describe_pet('dog','aimi')


# 传递形参
animals = 'US'
pets = 'aimi'


# describe_pet(animals,pets)

# 函数参数的位置传递顺序
# describe_pet(pets,animals)

# 关键字赋值传递

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

# 函数的默认值

def default_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# use default values
# default_pet('kimi')
# # not use default values
# default_pet('kimi','rabbit')


# 函数的返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + '-' + last_name
    return full_name.title()


# # 调用
# # print(get_formatted_name('jimi', 'hendrix'))
#
# # 参数的可选
#
# def get_formatted_name(first_name, middle_name,last_name):
#     full_name = first_name + '-'+middle_name+'--'+ last_name
#     return full_name.title()

#
# print( get_formatted_name('john', 'lee', 'hooker'))

# 将上面的代码整合
# def get_formatted_name(first_name, middle_name, last_name):
#     if middle_name == '':
#         get_formatted_name(first_name, last_name)
#     else:
#         full_name = first_name + '-' + middle_name + '--' + last_name
#      return full_name.title()
#
#
# print(get_formatted_name('john', 'lee', 'hooker'))
# 实际测试，这行代码不行
# print(get_formatted_name('jimi', 'hendrix'))

# 继续修改看下官方demo
# 参数可传，可不传，需要放到参数后面
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:  # 只能说，还是对语法不是很了解，自己多此一举了
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


# print(get_formatted_name('jimi', 'hendrix'))
# print(get_formatted_name('john', 'lee', 'hooker'))


# 函数返回字典

# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person


# print(build_person('jimi', 'hendrix'))
# 动态的构件字典

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# print(build_person('jimi', 'hendrix', 19))
# print(build_person('jimi', 'hendrix'))

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# 死循环
# while True:
#     print("请分别输入姓和名")
#     f_name = input("first_name:")
#     l_name = input('last_name:')
#     f_name = get_formatted_name(f_name, l_name)
#     print(f_name)

# 优化，结束条件
# while True:
#      print("请分别输入姓和名")
#      f_name = input("first_name:")
#      if f_name=='q':
#          break
#      l_name = input('last_name:')
#      if l_name=='q':
#          break
#      f_name = get_formatted_name(f_name, l_name)
#      print(f_name)


# 传递列表
def greet_users(names):
    for name in names:
        print("hello--> " + name)


usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# 列表的修改

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


# 读取列表一，然后修改的放入列表二中
# for des in unprinted_designs:
#     print("原值为", des)
#     tll = des.title()
#     completed_models.append(tll)
#
# for com in completed_models:
#     print("修改后的值为", com)
#
# print("======================")
# print("======================")
# print("======================")
# print("======================")
# print("======================")


# 将上面的两种抽成函数

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# 函数参数不确定
# def make_pizza(*toppings):
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 部分参数确定，其余的不确定
def make_pizza(size, *toppings):
    # 确定的参数 size
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 前两个参数确定，后面的参数不确定 为字典类型 字典类型需要两个**
def build_profiles(fl, la, **userInfo):
    profile = {}
    profile['first_name'] = fl,
    profile['last_name'] = la,
    for key, value in userInfo.items():
        profile[key] = value
    return profile


# user_profile = build_profiles('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)


# 函数封装到某个文件中，通过引用使用
import  pizza
pizza.make_pizza_a(16, 'mushrooms', 'green peppers', 'extra cheese')


# 特定函数的导入
from pizza import make_pizza_a
make_pizza_a(15,'pepperoni')
