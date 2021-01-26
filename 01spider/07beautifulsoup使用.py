
import requests
from bs4 import BeautifulSoup


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

rep=requests.get("https://movie.douban.com/top250", headers=headers)
# # print(rep.text)
# soup=BeautifulSoup(rep.text,'html.parser')
# 标签的使用，暂时只获取第一个
# 获取整个页面的一个标题
# print(soup.title)
# print(soup.head)
# print(soup.a)

# 获取标签属性
# print(soup.head.name)
# print(soup.p.attrs)
#
# print(soup.p['class'])
# 获取其中的豆瓣<p class="appintro-title">豆瓣</p>
# print(soup.p.string)
# print(soup.a.string)
# 遍历
# print(soup.a.contents)
# print(soup.find_all('a'))

# for he in soup.find_all('a'):
#     print(he)
import re
# 使用正则，匹配https开头的连接
# result=soup.find_all(href=re.compile('"https:'))
# print(result)
# beautiful 使用发觉很不方便
