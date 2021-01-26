# 函数
def print_python():
    print("hello python")


# 调用
# print_python()

# 函数返回值
result = 0


def print_python_result():
    print("hello python")
    result = 2
    return result


result = print_python_result()
print(result)


# 函数内注解

def my_function():
    """
    这是写注解的 方式
    这是写注解的 方式
    这是写注解的 方式
    这是写注解的 方式
    """
    print("")


# 参数的函数
def add(num1, num2):
    return num1 + num2


print(add(2, 5))
# 其中num1, num2 为形式参数

# 传入关键字参数

print(add(num1=10, num2=14))


# 函数的默认值，处理参数为空的情况
def add2(num1, num2=3):
    return num1 + num2


print(add2(2))


# num2 不赋值。默认为3

# 多参数传递

def print_values(*args):
    print(args)


print_values(1, 2, 3, 4, 5, 65, 7, 7, 8)


# 关键字与*结合

def multi_values(num, *args):
    print(num)
    print(args)


multi_values(1, 2, 3, 4, 5)


def multi_values(num1, num2=100, *args):
    print(num1)
    print(num2)
    print(args)


multi_values(1, 2, 3, 4, 5)


# 打印后为字典结构
def multi_values(**kwargs):
    print(kwargs)


multi_values(a=1, b=2, c=4)


# 全部参数混合使用
def school(name, location, *args, date_founded=2012, **kwargs):
    print('学校名称:', name)
    print('学校地址:', location)
    print('成立时间:', date_founded)
    print('学员名单:', args)
    print('课程与老师:', kwargs)

school('万门大学', '北京', 'mike', 'lucy', 'lily', 正正='python基础', 宁夫='Django')
# 通过打印发现，python 会自动匹配

# 函数对象的引用，可变， 不可变，操作
name='mike'
new_name=name
new_name=1234
print(name)
print(new_name)
# 打印结果 new_name概念了引用


