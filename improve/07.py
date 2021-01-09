# 匿名函数
# 匿名函数就是无名函数-->等价于lambda

# 普通函数
def add(num1):
    return num1 * 2


# 匿名函数定义
lambda x: x * 2
# x:x*2
# x等于传统函数的num1
# :等于传统函数的:
# x*2等价予传统函数的数据运算
# 匿名函数的调用
result = lambda x: x * 3
print(result(3))

# 多参数匿名函数
result = lambda x, y: x + y
print(result(10, 5))

# 三目运算

a = 5
b = 3
if a > b:
    print("a >b")
else:
    print("a<b")
# python的跟java 的区别还是很大的
'a>b' if a > b else 'a<b'
# ‘a>b’表示为真的返回
# ‘a<b’表示为假的返回

# 使用匿名函数替代
# def compare(x,y):
#     if x>y :
#       return x
#     else:
#      return y

comp = lambda x, y: x if x > y else y
print(comp(8, 6))


# 将lambda参数传入函数

def key_search(keys, func):
    search_result = []
    for key in keys:
        # 如果匹配条件为真，list add elements
        if func(key):
            search_result.append(key)
    return search_result


# lambda
condition = lambda x: True if 'Python爬虫' in x else False

schools = ['Python基础', 'Python爬虫', 'Java编程', 'Java Web', 'Python数据分析']

aket = key_search(schools, condition)
print(aket)


# 给def 中的lambda 传递参数
def la():
    return lambda x: True if x == 10 else False


# 这个写法有点奇怪
print(la()(10))
print(la()(15))


# 把lambda作为一个方法传入传统函数
# 索性认为同岗位基本工资、交通补助、话补助相同，但是绩效工资不同
def income(basic, transport, phone):
    return lambda x: x + basic + transport + phone


total = income(1000, 500, 200)  # 这是计算基本工资
print(total(3500))  # 这是计算绩效工资
print(total(100))

# lambda  map 函数使用 map 可以理解成，将旧的list或者dict 通过运算的到新的list 或者dict
# 学习过渡 传统方式
# data = [1,2,3,4,5]
# new_l = [ ]
# for n in data:
#     new_l.append(n)
# print(new_l)

# 传统函数加map
# data = [1,2,3,4,5]
# def func(n):
#     return n+1
#
# news=map(func,data)
# print(list(news))


# lambda +map
# data = [1, 2, 3, 4, 5]
# new_l_list = list(map(lambda x: x + 1, data))
# print(new_l_list)

# reduce 函数

# from functools import reduce
# data = [1, 2, 3, 4, 5]
#
# res=reduce(lambda x,y:x+y,data)
# print(res)

# filter()函数
#
# data = [1, 2, 3, 4, 5]
# res = list(filter(lambda x:x > 2, data))
# print(res)
# sorted函数
exam_result = {'张旭': '540', '李阳': '575', '王强': '583', '徐增': '569', '齐飞': '557'}
#                                          d:d[1]表示排序字典中的value,并且反转
des_order = sorted(exam_result.items(), key=lambda d: d[1], reverse=True)
print(des_order)

# 排序任务-使用列表内的列表的第一个元素升序排序
l_data = [[3, 4, 1], [3, 3, 3], [1, 2, 4], [9, 1, 0], [7, 3, 2]]
asc_order = sorted(l_data, key=lambda x: x[0], reverse=False)
print(asc_order)



