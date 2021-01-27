# 爬虫基础开始
# urllib 库的学习

import urllib.request
import urllib.parse
import urllib.error

# 模拟get请求
# rep=urllib.request.urlopen("http://www.baidu.com")
# print(rep.read().decode('utf-8'))
# 两个代码，就爬出了百度的html 页面


# rep = urllib.request.urlopen("http://www.baidu.com")
# print(type(rep))
# # HTTPResponse 响应信息
# print(rep.status)
# 获取返回信息
# repson=urllib.request.urlopen("https://www.python.org/")
# print(repson.status)
# print(repson.getheaders())
# print(repson.getheaders('server'))

# http://httpbin.org/是一个测试请求的网站
# 模拟post 请求 向服务端发送信息
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# repose=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(repose.read())
# 超时测试
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# repose=urllib.request.urlopen('http://httpbin.org/post',data=data,timeout=1)
# print(repose.read())

# 设置一个抓取页面的需求：如果抓取的页面超时了，我们就跳过其。去抓取下一个页面
from socket import socket

# try:
#    rep= urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
# except urllib.error.URLError as e:
#      if isinstance(e.reason,socket.timeout):
#          print('time out')


# request 请求分析
# urllib.request.Request
# def __init__(self, url, data=None, headers={},
#              origin_req_host=None, unverifiable=False,
#              method=None):
# 请求头的参数
# url  请求地址
# data  传输的数据
# headers  请求头
# origin_req_host 请求地址
# unverifiable 请求是否验证
# method  请求方法

# 简单的构建请求
from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'China'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# repson = request.urlopen(req)
# print(repson.read().decode('utf-8'))

# 代理的构建

# from urllib import request,error
# try:
#     repsonse=request.urlopen("http://hjfdnjfk.com")
# except error.URLError as e:
#     print("连接错误。。。。")

# 类型解析
from urllib.parse import urlparse

result = urlparse("http://www.baidu.com/index.html;user?Id=5#commit")
print(type(result), result)
