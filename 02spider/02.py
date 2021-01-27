import requests

# requests库学习
# 创建一个get请求
# repo=requests.get("https://api.github.com/events")
# print(repo.text)
# https://httpbin.org/ 专门测试请求
# 创建一个post 请求：
# reps=requests.post('https://httpbin.org/post',data={'name':'lktbz'})
# reps=requests.post('https://httpbin.org/delete')
# reps=requests.post('https://httpbin.org/get')


# 构建请求参数
# params={'key1': 'value1', 'key2': 'value2'}
# requ=requests.get('https://httpbin.org/get',params=params)
# print(requ.url)
# # 构建列表参数
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r=requests.get('https://httpbin.org/get',params=payload)
# print("构建url 为:",r.url)

# 响应内容
# r = requests.get('https://api.github.com/events')
# print("响应内容为",r.text)
# print("响应内容为",r.status_code)
# print("响应内容为",r.encoding)
# print("响应内容为",r.headers)


# json 响应内容
# r = requests.get('https://api.github.com/events')
# print(r.json())


# 自定义响应头

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
# print(r.text)

# 复杂的post
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# 响应头
r = requests.get('http://httpbin.org/get')
# print(r.headers)
# print(r.headers['Content-Type'])
# print(r.headers['Date'])


# cookie
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url,cookies=cookies)
# print(r.text)

# session
s=requests.session()
r=s.get("http://www.baidu.com")
print(r.text)