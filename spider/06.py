# pyquery 库学习
html = """
    <html>
    <body>
    <div id="wapper">
        <div id="container">
            <ul class="list">
           <li class="item-0">first item</li> 
           <li class="item-1"><a href="link2.html">second item</a></li> 
           <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li> 
           <li class="item-1 active"><a href="link4.html">fourth item</a></li> 
           <li class="item-0"><a href="link5.html">fifth item</a></li> 
        </ul>
        </div>
    </div>
"""
# css 选择器最强选择
from pyquery import PyQuery as pq

# doc=pq(html)
# print(doc)
# print(doc('li'))

doc = pq(url="https://sjz.bdsh5.com/")
# print(doc.text())
# print(doc('title'))
doc = pq(html)
# print(doc("#container .list"))
# print(doc(".item-0"))

# 节点查找
items = doc('.list')
# print(items)
lis = items.find("li")
# print(lis)

# 从上面可知，find 子孙节点都找到了
# 只想找到孩子节点
# liss = items.children()
# print("liss",liss)

ls = items.children(".active")
# print(ls)

# 父节点
container = items.parent()
# print(container)
# 遍历
doc = pq(html)
# li = doc("li").items()
# for ls in li:
#     print(ls)


# 获取信息
a = doc('.item-0.active a')
# "拿取跳转的html 页面信息"
# print(a.attr('href'))
# 等价于
# print(a.attr.href)

# 匹配多个元素

doa = doc("a")
# 打印还是打印一个
# print(doa.attr('href'))
# print(doa.attr.href)


# for 解决

# for di in doa.items():
# print(di.attr.href)

# 获取文本数据
doc = pq(html)
a = doc('.item-0.active a')
# print(a)
# 只返回文本信息
# print(a.text())
# 会返回带标签的信息
# print(a.html())
# 匹配多个
ali=doc('li')
# print(ali.html())
# 全部匹配的文本内容都抽取出来
# print(ali.text())

