# 数据信息提取：
import requests
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# html.parser 为库自带解析器
soup = BeautifulSoup(html, 'html.parser')
# 格式化输出
# print(soup.prettify())

# BeautifulSoup将HTML格式化树形结构

# BeautifulSoup 的四大内置对象

# Tag
# NavigableString
# BeautifulSoup
# Comment

# tag:就是标签
# 分别去title 和p 标签的内容打印
# print(soup.title)
# print(soup.p)
# print(soup.a)
# # 获取标签得名字
# print(soup.p.name)
# # 获取标签的属性
# print(soup.p.attrs)
# # 获取某个属性的值
# print(soup.p['class'])

# 对属性进行修改

# NavigableString
# 既然已经拿到了标签，怎么获取标签的内容是关键？
# print(soup.p.string)
# print(soup.title.string)
# # 内容的类型
# print(type(soup.title.string))

# BeautifulSoup
# BeautifulSoup 对象表示的是一个文档的全部内容。大部分时候，
# 可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下

# print(type(soup.name))

# Comment
# Comment 对象是一个特殊类型的 NavigableString 对象，
# 其实输出的内容仍然不包括注释符号，但是如果不好好处理它，
# 可能会对我们的文本处理造成意想不到的麻烦。 我们找一个带注释的标签

# print(soup.a)
# print(soup.a.string)
# print(type(soup.a.string))

# 以上都是匹配一个，现在开始遍历
# 遍历文档树
# print(soup.head.contents)
# # .contents tag 的 .content 属性可以将 tag 的子节点以列表的方式输出
# print(soup.head.contents[0])

# .children 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
# 我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象
# print(soup.head.children)
# for ins in soup.head.children:
#     print(ins)

# soup.head.children 相当于列表生成器，遍历一下就好了

# 遍历body中的孩子元素
# for inss in soup.body.children:
#     print(inss)

# .descendants .contents 和 .children 属性仅包含 tag 的直接子节点，
# .descendants 属性可以对所有 tag 的子孙节点进行递归循环，和 children 类似，我们也需要遍历获取其中的内容。

# for child in soup.descendants:
#     print(child)


# .strings 获取多个内容，不过需要遍历获取
# 多个内容
# for string in soup.strings:
#     # 格式化字符串
#     print(repr(string))

# 查找父类
# p=soup.p
# print(p.parent.name)
# 查找全部父类
# content = soup.head.title.string
# for parent in  content.parents:
#     print (parent.name)

# 文档树的搜索
# find_all
# 传入标签
# print(soup.find_all('b'))
# for ain in soup.find_all('a'):
#     print(ain)


# 传入列表标签
# for ins in soup.find_all(['a','b']):
#     print(ins)


# 传 True True 可以匹配任何值，下面代码查找到所有的 tag, 但是不会返回字符串节点
# 获取标签的name
# for tag in soup.find_all(True):
# print(tag.name)

# 指定参数去查找
# s = soup.find_all(id='link2')
# print(s)

# 组合过滤
# s=soup.find_all("a", class_="sister")
# print(s)

# 类选择器
# 标签查找
# print (soup.select('title'))
# print (soup.select('a'))


# 类名查找
# print (soup.select('.sister'))

# print (soup.select('#link1'))
# 组合查找
# print (soup.select('p #link1'))
# 属性查找
# print (soup.select('a[class="sister"]'))

# print (soup.select('a[href="http://example.com/elsie"]'))

