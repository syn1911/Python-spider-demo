# 字典类型：
# 字典特征：
# key 不能重复


# 声明dict
# 空声明
# dict_1 = dict()
# dict_2 = {}
# # 赋初始值
# dict_3 = {' 姓名 ': 'mike', ' 年龄 ': 20}
# 上面的的简单类型
# 字典的复杂数据类型 如下：字典里含有元组与列表
# { 'names’ : ('mike’, 'Tim’), 'cities’: ['Beijing’,'SH’] }
info = {'name ': 'mike', 'age': 20, 'male': '男'}
# 添加字段(字段存在则覆盖，不存在则新建key)
# 方式一：
info['city'] = '上海'
# 方式二：
# xx={'age':8}
# info.update(xx)
# print(info)

wages = {
    '一月': 5000,
    '二月': 3000,
    '三月': 4500,
}
# 遍历
for k, v in wages.items():
    print("月份->", k, "工资为->", v)
# 计算总收入
total = 0
for k, v in wages.items():
    total = total + v

print("total money:" + str(total))

# 还原你的超市购物小票
# 第一步 建立字典
# 第二步 向字典添加购物小票的数据，包括商
# 品名称和单价
# 第三步 将你购买的商品信息添加到列表中，
# 包括商品名称、单价、购买数量、折扣
# 第四步 计算你购买的商品总金额，看是否跟
# 小票金额对得上
# "#    品名     单价    数量     折扣\n",
# "# '84消毒液'     8    2        1 \n",
# "# '大宝护手霜'   16    2       0.8\n",
# "# '青岛啤酒'    3.5   10       0.9\n",
# "# '精品三黄鸡'   20    1        1\n"

# 小票的内容如上


# 用合适的数据类型存储上面
# bus={"品名":"84消毒液","单价":8,"数量":2,"折扣":1}
# 这是上面一个商品的信息
# 现在组装全部数据

super_market_tickets =[
        {"商品": "84消毒液", "单价": 8, "数量": 2, "折扣": 1},
        {"商品": "大宝护手霜", "单价": 16, "数量": 2, "折扣": 0.81},
        {"商品": "青岛啤酒", "单价": 3.5, "数量": 10, "折扣": 0.9},
        {"商品": "精品三黄鸡", "单价": 20, "数量": 1, "折扣": 1},
    ]

# 这就是组建完成的数据集
total_new=[]
# 遍历
for product in super_market_tickets:
    print(product['商品'], product['单价'],product['数量'],product['折扣'])
    total_new.append(product['单价']*product['数量']*product['折扣'])
# 金额
print(total_new)
# 总金额
print(sum(total_new))



