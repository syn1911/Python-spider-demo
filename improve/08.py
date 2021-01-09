# 列表推导式
# 就是利用for if等条件生成数据

# 简单的数据生成
list_data_easy = [x for x in range(10)]
print(list_data_easy)
# 生成偶数数据
list_data_easy_oushu = [x for x in range(11) if x % 2 == 0]
print(list_data_easy_oushu)

# ** 理解成次方操作 非按照字典方式处理
list_data = [x ** 2 for x in range(10) if x % 2 == 0]
print(list_data)

# 列表推导式的双for循环

double_list_data = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(double_list_data)

data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# 对上面的data 的遍历操作
# 传统方式：
emp_list = []
for out in data:
    for ins in out:
        emp_list.append(ins)

print(emp_list)

# 使用列表推导公式解决：
list_data_emp = [y for x in data for y in x]
print(list_data_emp)
# 上面这种方式尽量别写，总感觉会被骂的感觉


# 列表推导式，在dict 中的使用

fields = ['姓名', '年龄', '城市']
info = ['zz', 28, '上海']
# 传统方式：
dict_data = {}
for x, y in zip(fields, info):
    dict_data[x] = y

print(dict_data)

dict_data_emp = {x: y for x, y in zip(fields, info)}

print(dict_data_emp)

# 各位学员可能已经经历或未来都要经历一种场景就是装修房子，那么装修房子都会涉
# 及哪些东西？我大概列一下，家用电器、家具、房屋装修等。那么我们今天就来使用
# 推导列表做一个基于家装的成本支出的作业
# 作业背景
# 数据如下: (大家可以自行拟定，想一下你需要什么数据结构)
# 1.电视6000、空调15000、洗衣机5000、电冰箱8000
# 2.床12000、衣柜9000、书桌4000、沙发10000、茶几电视柜5000
# 3.地面8000、墙面5000、吊顶6000、地板10000
# 输出要求: (以下全部使用推导列表完成)
# 1.计算家用电器的总花销
# 2.计算家具的总花销
# 3.计算房屋装修的总花销
# 4.计算全部总花销
# 5.输出花销超过5000的项目
# 创建dict 数据
appliances_dic = {'电视': 6000, '空调': 15000, '冰箱': 8000, '洗衣机': 5000, '热水器': 5000, '厨房电器': 8000,
                  '电脑': 6000}
furniture_dic = {'床': 12000, '沙发': 10000, '衣柜': 9000,
                 '茶几电视柜': 5000, '餐桌': 4000, '橱柜': 7000,
                 '书桌电脑桌': 4000}
decorate_dic = {'地面': 8000, '墙面': 5000, '地板': 10000, '厨房': 5000,
                '卫生间': 4000, '瓷砖': 10000, '吊顶': 6000, '灯具': 5000,
                '管线开关': 5000}


appliances_dic_list=[v for v in appliances_dic.values()]
print("家用电器的总花销",str(sum(appliances_dic_list)))

furniture_dic_list=[v for v in furniture_dic.values()]
print("家具总费用",str(sum(furniture_dic_list)))

decorate_dic_list=[v for v in decorate_dic.values()]
print("装修总费用",str(sum(decorate_dic_list)))

print('合计总费用：'+str(sum(appliances_dic_list)+sum(furniture_dic_list)+sum(decorate_dic_list)))

home_price={}
home_price.update(appliances_dic)
home_price.update(furniture_dic)
home_price.update(decorate_dic)
print("全部发花费明细：",home_price)

# 遍历超过5000的消费
# 传统方式
for k,v in home_price.items():
    if v>5000:
        print("超过5000的消费有？",k)


# 列表推导
cost_5000_home=[k for  k in home_price.keys() if home_price.get(k)>5000]
print(cost_5000_home)