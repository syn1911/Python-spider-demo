# requests库学习
# 下面是官方网址
# https://requests.readthedocs.io/en/master/
import requests

# r=requests.get("http://www.baidu.com")
# print(r)
# print(r.text)
# print(r.cookies)
# print(r.encoding)

# 构建get

# r=requests.get("http://httpbin.org/get")
# print(r.text)
# 构建带参数的get

# data={
#     'name':'lktbz',
#     'age':17
# }
# rs=requests.get('http://httpbin.org/get',params=data)
# # 打印之下，发现控制台出现重构请求连接
# print(rs.text)


import requests
# 正则表达式
import re

# 构建请求头
headers = {
    'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',

}
r = requests.get("http://httpbin.org/get", headers=headers)
print(r.text)
# 下面是浏览器返回
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "Use-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
#     "User-Agent": "python-requests/2.25.1",
#     "X-Amzn-Trace-Id": "Root=1-5ff58842-62562b696b9fade9623b77fc"
#   },
#   "origin": "111.199.191.188",
#   "url": "http://httpbin.org/get"
# }
