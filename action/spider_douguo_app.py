# 直接抓取重点信息
# 使用fiddler 抓取的请求信息为
"""
POST https://api.douguo.net/recipe/flatcatalogs HTTP/1.1
Cookie: duid=67251308
client: 4
version: 6975.2
device: SM-G977N
sdk: 25,7.1.2
channel: baidu
resolution: 1600*900
display-resolution: 1600*900
dpi: 2.0
pseudo-id: 13da1238dea57035
brand: samsung
scale: 2.0
timezone: 28800
language: zh
cns: 2
carrier: CMCC
imsi: 460078240775141
User-Agent: Mozilla/5.0 (Linux; Android 7.1.2; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36
act-code: 1611306944
act-timestamp: 1611306945
uuid: ad85b45f-d65e-4c76-901e-a4bdba7e4e4e
battery-level: 0.87
battery-state: 2
terms-accepted: 1
newbie: 1
reach: 1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Accept-Encoding: gzip, deflate
Connection: Keep-Alive
session-info: zZ9ob7xjJtQKWPylkgRuVQjjhLps5OKFeAOAP916KtLyMrXO4cEr67uDH9KMEe8hlwrz2bZG1U25uMYXstGcvdirvxcY+GoWWYyx4g7pwFCMDO66KkuIkNv4Y+2mZLTw
Host: api.douguo.net
Content-Length: 13
client=4&_session=1611325122425351564830877510&v=1611314131&_vs=2305&sign_ran=ea12d2b1bf546b6351500823a810e18e&code=41f7c226e75805b8
"""
# 抓取返回的json信息
"""
    返回信息部分json
                "name":"热门",
                "id":"1",
                "ju":"recipes://www.douguo.com/search?key=热门&_vs=400",
                "cs":[
                    {
                        "name":"家常菜",
                        "id":"18",
                        "ju":"recipes://www.douguo.com/search?key=家常菜&_vs=400",
                        "cs":[
                            {
                                "name":"红烧肉",
                                "id":"7206",
                                "ju":"recipes://www.douguo.com/search?key=红烧肉&_vs=400",
                                "cs":[

                                ],
                                "image_url":""
                            },
                            {
                                "name":"可乐鸡翅",
                                "id":"7207",
                                "ju":"recipes://www.douguo.com/search?key=可乐鸡翅&_vs=400",
                                "cs":[

                                ],
                                "image_url":""
                            },
                            {
                                "name":"糖醋排骨",
                                "id":"7208",
                                "ju":"recipes://www.douguo.com/search?key=糖醋排骨&_vs=400",
                                "cs":[       
"""
"""
    拿到json 数据，接下来就是解析最后入库操作
"""

import requests
import json
# 引入队列，当有数据时，让多线程执行
from  multiprocessing import Queue
# 因为被墙403了，所以拔下来的数据，只能通过 本地json来解决，好尴尬，代理之后在弄
# 所以抓取的json 数据已经存放到request1.json,与rtequet2.json 中了直接加载就可以了
# 构建请求信息
def handel_request(url, data):
    header = {
        "brand": "samsung",
        "device": "SM-G977N",
        "sdk": "25,7.1.2",
        "channel": "baidu",
        "language": "zh",
        "resolution": "1600*900",
        "Cookie": "duid=67251308",
        "display-resolution": "1600*900",
        "Content-Length": "132",
        "cns": "2",
        "imsi": "460078240775141",
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Host": "api.douguo.net",
        "Connection": "Keep-Alive"
    }
    rep = requests.post(url=url, headers=header, data=data)
    return rep


# 构建请求首页
def handle_index():
    url = "https://api.douguo.net/recipe/flatcatalogs"
    data = {
        "client": "4",
        "_vs": "2305",
        "code": "fa1a2707bad8b022",
        "sign_ran": "abd7417b36d3f7adecfe5de97a3b45c9",
        '_session': '1611366968018351564830877510'
    }
    resp = handel_request(url=url, data=data)



# handle_index()
filename = 'request1.json'
filename2 = 'request2.json'


# 定义队列
queue_list=Queue()
def parlleJson():
    data = json.loads(open(filename, encoding='utf-8').read())
    for dadel in data['result']['cs']:
        # 查找家常菜
        for daa in dadel['cs']:
            for eda in daa['cs']:
                # 解析到这里，发现已经到了开始找黄瓜同级别的阶段
                # 发送请求，伪造黄瓜 Post
                data_td = {
                    "client":"4",
                    'keyword':eda['name'],
                    "order":"3",
                    "_vs":"11104 ",
                    "type":"0 ",
                    "auto_play_mode": "2",
                }
               # 伪造好请求头数据，接着发送数据。查看返回
            # 数据放到队列中
                queue_list.put(data_td)

def handle_caipu_list(data):
    # print("即将处理的食材名称是："+data['keyword'])
    # 现阶段先请求20条数据，这是写死的可以用循环替代
    caipu_list_url="https://api.douguo.net/recipe/v2/search/0/20"
    # 发请求得到返回数据
    # caipu_list_response=handel_request(url=caipu_list_url,data=data)
    caipu_list_response= json.loads(open(filename2, encoding='utf-8').read())
    for caipuList in caipu_list_response['result']['list']:
        caipu_dict = {}
        caipu_dict['type']='黄瓜'
        if caipuList['type']==13:
            caipu_dict['name']=caipuList['r']['an']
            caipu_dict['id']=caipuList['r']['id']
            caipu_dict['cookstory']=caipuList['r']['cookstory']
            # //模拟数据库入库操作
            print(caipu_dict)

        else:
            continue



# parlleJson()
data={}
handle_caipu_list(data)
# 查看队列的大小
# 队列中公有517条数据，就是菜谱分类中的516条数据
# 接着要做的就是取队列的数据，然后多线程执行发送数据
# 因为被盾了，所以没办法，只能写死，请求土豆的方式
# print(queue_list.qsize())



