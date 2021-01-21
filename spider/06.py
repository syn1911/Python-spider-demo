# 数据存储
import requests
from pyquery import PyQuery as pq
url="https://sjz.bdsh5.com/"
headers={
    'User-agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36'
}
html=requests.get(url,headers=headers).text
# print(html)
doc=pq(html)
fuwu=[]
items=doc("#indexfenlei .lie .box").items()
for iins in items:
    fuwu.append(iins.find('h3').text())


xihua=[]
hrfs=doc("#indexfenlei .lie .box .item").items()
for ins in hrfs:
    xihua.append(ins.find("a").text())

print(xihua)
