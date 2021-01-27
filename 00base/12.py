# python 之 Json

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
# 写入json 数据
# with open(filename,'w')as jso:
#     json.dump(numbers,jso)


# 读取json 数据

# with open(filename)as name:
#     nunbers=json.load(name)
#     for js in nunbers:
#         print(js)


# 保存和查取用户数据
# username=input("你的姓名")
# filename='file.json'
# with open(filename,'w') as wri:
#     json.dump(username,wri)
#     print("我已经记住你的名字了，不需要在输入用户名。你的用户名为：",username)


# 读取
# filename = 'file.json'
# with open(filename)as f:
#     username = json.load(f)
#     if username:
#         print("恭喜你:"+username+"：登录成功")
#     else:
#         print("不好意思。新用户请重新注册")


# 整合成优雅的代码
# 读取内容存在不？
# 存在  直接打印
# # 不存在 让用户直接输入，然后保存，在输入
filename = 'file.json'
try:
    with open(filename)as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("请输入您的名称，亲")
    with open(filename,'w') as fil:
        json.dump(username, fil)
        print("恭喜您：" + username + "下次直接登录就好")
else:
    print("欢迎回来，尊贵的 会员", username)
