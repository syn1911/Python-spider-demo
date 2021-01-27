# 函数赋值给变量，变量可以当做函数使用
def ask(name="nike"):
    print(name)
# my_nam=ask
# my_nam(name="zs")

# 类赋值给变量，并实例化

class Person():
    def __init__(self):
        print("nike")
# 变量赋值给类
# m_p=Person
# m_p()

#函数与类放进列表中,并调用
function_list=[]
function_list.append(ask)
function_list.append(Person)
# for it in function_list:
#     print(it())

#函数中返回函数
def wraaper_ask():
    print("包装函数正在运行")
    return ask(name="japanese")


# 调用
# wraaper_ask()


# type int class 三者之间的关系
a=1
b="abc"
print(type(1)) #1的type==int
print(type(int)) #int 的type==type
# 可以的出type-->int-->1 type 是对象，int 是对象，
print(type(b)) #str
print(type(str))  #type
# type-->class-->obj
# object.__bases__

# python中 type  obj  class之间的关系
