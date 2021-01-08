# 实战：京东商品页的爬取
# 网址：https://item.jd.com/66961052519.html
import  requests
# //爬取之后，要登录，后面需要解决
# url="https://item.jd.com/66961052519.html"
# url="https://www.720mp4.com/kongbupian/38886.html"   #这个网站没有做反扒手段
# try:
#     r=requests.get(url)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")

#伪装浏览器爬取亚马逊
url="https://www.amazon.cn/dp/B07W3SXXR8"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

res=requests.get(url,headers=headers)
print(res.status_code)  #返回503 伪装浏览器
print(res.text)
#
# 疑问？ 知道网页地址？对于需要登录的怎么去解决？
# 频繁的发送请求，怎么规避掉这个问题。
# 怎么去拿到网页？怎么解析里面的数据？拿出来想要的数据？以为了茅台来说?肯定是为了拼接下单url 然后抢到茅台
#暂时用不到数据存储
#这些疑问解决的时候，就是可以为了茅台而努力了

