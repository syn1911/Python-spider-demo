# 使用python 操作mongodb
# 因为mongodb 是面向对象编程,所以很友好
import pymongo
# api 文档地址 https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html
# create to mongoclinet
# 1:链接数据库
client=pymongo.MongoClient(host='192.168.5.147',port=27017)
#2:创建数据库/指定数据库
mydb=client['lktbz']

# 判断创建的数据库是否存在
# fordbs=client.list_database_names()
# if 'lktbz' in fordbs:
#     print("数据存在")

#指定集合
collection=mydb.students
#准备插入数据
student={
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# result=collection.insert(student)
# print(result)

# 查询
result=collection.find_one({'id':201702023})
print(result)

# 多次插入
student_list=[]

for i in range(1,10):
        student2 = {
         'id': '20170202'+str(i),
         'name': 'Mike',
         'age': 21+i,
         'gender': 'male'
        }
        student_list.append(student2)

    # result=collection.insert_many(student_list)
    # print(result)

    #查询全部
    # result=collection.find()
    # for x in result:
    #     print(x['id'])


# 查询特定的字段
# try:
#     result=collection.find({'age',20})
#     for res in result:
#       print(res)
# except:
#     print("没有找到合适的数据")

# 查询大于20的
# try:
#     myquery = {"age":{"$gt":22}}
#     result=collection.find(myquery)
#     for res in result:
#       print(res)
# except:
#     print("没有找到合适的数据")

