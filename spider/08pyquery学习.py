# 最像jquery 解析器
# 小实战，并且在此复习下soup 用法
# 爬取电影排行榜。抓取http 链接  https://movie.douban.com/top250
# 问题？怎么去操作翻页？需要以后去解决
# 使用pyquery 解决 类似于jquery
from pyquery import PyQuery as pq
import requests
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

rep=requests.get("https://movie.douban.com/top250", headers=headers)
doc=pq(rep.text)

# id 选择器
# 通过浏览器找到 id content
# sls =doc.find("#content")
# print(sls)

# tx=doc.text("#content")
# print(tx)
# find 会将子孙后代都显示，而txt会精准显示
# htl=doc.html("#content")
# print(htl)  #跟text 一样

# 类选择器
dird=doc.find(".grid_view")
# print(dird)
# tx=doc.text(".grid_view")
# print(tx)
# tx=doc.html(".grid_view")
# print(tx)
# 属性选择器
# dird=doc.find("a[href='https://movie.douban.com/subject/1291546/']")
# print(dird.text())
# 属性选择
ddd=dird.attr(_class="quote")
# print(ddd)
# 找到所有的https 链接存储在链表中
http_list=[]
for ins in doc.find(".hd").items():
    http_list.append(ins.children('a').attr("href"))
# print(http_list)
