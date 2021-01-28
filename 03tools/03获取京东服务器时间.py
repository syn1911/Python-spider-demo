# 获取京东服务器时间，与本地时间差距
"""
分析： repsonse 响应消息里面有响应时间，非服务器时间
    通过抓取，分析url，终于找到了获取京东时间
    GET https://a.jd.com//ajax/queryServerData.html HTTP/1.1
    Host: a.jd.com
    Connection: keep-alive
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
    Accept: application/signed-exchange;v=b3;q=0.9,*/*;q=0.8
    Purpose: prefetch
    Sec-Fetch-Site: cross-site
    Sec-Fetch-Mode: no-cors
    Sec-Fetch-Dest: empty
    Referer: https://blog.lanluo.cn/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
        响应：
        HTTP/1.1 200 OK
        Date: Thu, 28 Jan 2021 02:34:14 GMT
        Content-Type: text/html;charset=UTF-8
        Connection: close
        Vary: Accept-Encoding
        Content-Disposition: inline;filename=f.txt
        Expires: Thu, 28 Jan 2021 02:34:14 GMT
        Cache-Control: max-age=0
        Server: jfe
        Strict-Transport-Security: max-age=7776000
        Content-Length: 28
        响应时间戳
        {"serverTime":1611801254236}
"""
import requests
import json
import time


# 获取京东服务时间
def get_JD_server_time():
    url = 'https://a.jd.com//ajax/queryServerData.html'
    ret = requests.get(url).text
    js = json.loads(ret)
    return int(js["serverTime"])


# 获取本地服务器时间
def local_time():
    return int(round(time.time() * 1000))


# tq= time.time() * 1000
# t1= time.time()
# print(t1)
# print(tq)
# print(ts)
# 1611803520.8926547  三个打印结果，
# 1611803520892.6545
# 1611803520893
def local_jd_time_diff():
    """
        计算服务时间差
    """
    diff_time = local_time() - get_JD_server_time()
    return diff_time


# 轮询等待开始时间
def start():
    buy_time = 1611804348  # 写死的时间，在实际情况中需要获取配置文件信息
    while True:
        if local_jd_time_diff() >= buy_time:
            print("到达抢购时间准备执行")
            break
        else:
            print("暂未到达执行时间，开始睡眠")
            time.sleep(0.5)


start()
