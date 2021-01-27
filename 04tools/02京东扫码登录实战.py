"""
   登录京东扫码实战步骤分析：
    1:python二维码生成相关工具（负责生成二维码）
    2：抓取扫码登录的请求
        构建相关请求并发送
    3:解析返回的数据判断是够登陆成功
    3：登录成功创建本地cookie，在一定时间不用再次登录
"""


"""
    1: 分析页面
     登录请求：
        Request URL: https://qr.m.jd.com/show?appid=133&size=147&t=1611714382306
        Request Method: GET
        Status Code: 200 
        Remote Address: 211.144.24.150:443
        Referrer Policy: strict-origin-when-cross-origin
        cache-control: no-cache,no-store
        content-type: image/png
        date: Wed, 27 Jan 2021 02:26:21 GMT
        server: jfe
        set-cookie: QRCodeKey=AAEAIGrIem9KBCxgXk8BecbpxD2XnFmW8-z9EUbvPif-zedV; HttpOnly
                                      #此处是cookie
        set-cookie: wlfstk_smdl=vadrpix8est5v8sjswum5szld006ueyp; PATH=/; DOMAIN=.jd.com
        strict-transport-security: max-age=7776000
        
        回调js ，一直检查是否登录成功
        Request URL: https://qr.m.jd.com/check?callback=jQuery8873123&appid=133&token=vadrpix8est5v8sjswum5szld006ueyp&_=1611714385313
        Request Method: GET
        Status Code: 200 
        Remote Address: 211.144.24.150:443
        Referrer Policy: strict-origin-when-cross-origin

        GET https://passport.jd.com/uc/qrCodeTicketValidation?t=AAEAML9YktnyWhLLf5M6eEDbcp3j62oTxvjQZAOVbEhG8YURR7MF_3Ai7NPgZFkxygg_gg&ReturnUrl=https%253A%252F%252Fwww.jd.com%252F%253Fcu%253Dtrue%2526utm_source%253Dbaidu-pinzhuan%2526utm_medium%253Dcpc%2526utm_campaign%253Dt_288551095_baidupinzhuan%2526utm_term%253D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2896049f217e4e968a06b06e3beab9f1 HTTP/1.1
        Host: passport.jd.com
        Connection: keep-alive
         Accept: application/json, text/javascript, */*; q=0.01
        User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
        X-Requested-With: XMLHttpRequest
        Sec-Fetch-Site: same-origin
        Sec-Fetch-Mode: cors
        Sec-Fetch-Dest: empty
        Referer: https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F%3Fcu%3Dtrue%26utm_source%3Dbaidu-pinzhuan%26utm_medium%3Dcpc%26utm_campaign%3Dt_288551095_baidupinzhuan%26utm_term%3D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2896049f217e4e968a06b06e3beab9f1
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9
        Cookie: shshshfpb=kwiFf%2FZp%2FP6nC7YtTvTmkCg%3D%3D; shshshfpa=bed19552-9982-960e-5ff5-c14cd961b467-1590464759; areaId=1; user-key=db58bbba-04c3-49a4-bbc2-308f556a167b; _c_id=n4fkywcz90izt7vvhrw1609431747207gd4d; DeviceSeq=711b6266987843089708045b80c7bb37; ipLocation=%u5317%u4eac; __jdu=1744909582; pinId=7caFWnOGKUBLz6pdJ9FatLV9-x-f3wj7; pin=jd_4e4fcf55a293e; unick=%E5%9C%B0%E9%94%85%E7%88%B1%E6%9C%A8%E6%9F%B4; _tp=SjokruGuZxgsLPSV1LWt1Hd%2FQNRhG82IR9AUrTDCul8%3D; _pst=jd_4e4fcf55a293e; ipLoc-djd=1-2901-4135-0.138138224; cn=1; _s_id=e4zj098581avsz2cozq1611714196082dyed; shshshfp=8e829661e291c47001a48126ff9e5fb0; e4zj098581avsz2cozq1611714196082dyed=-1082; TrackID=1DIlUZIRYXzyNgS7k_32dHcV1X5hjbzLOo3Mep-e2AqMXUsqOB6jCwrF5CUgcTA5T_22iHQrckR4lLTq4IgantGTioeOPH6oZ_8XRGZNQY54; unpl=V2_ZzNtbUFeSxJ0DU4DeBlaUWJXGlpLB0ISJglBAHlKCFU0C0VdclRCFnUUR1RnGloUZwIZWENcQxFFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsfWQBvAhpZS1RzJXI4dmR5HloAbwYiXHJWc1chVEZWfRFcDSoDFFhHX0IdcQFFZHopXw%3d%3d; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2896049f217e4e968a06b06e3beab9f1|1611715217180; shshshsID=9d37031b232fd92d87db9919a014f9e9_7_1611715219363; alc=T2PLkbIn0+9XqPkNteu7+A==; _t=HIqSfH7kccle0kBFx3h3R4ILLsJuXzhnPOCQGfuvxk4=; __jda=122270672.1744909582.1610085860.1611553915.1611713892.12; __jdc=122270672; __jdb=122270672.22.1744909582|12.1611713892; 3AB9D23F7A4B3C9B=HRQ4EO2S37MU5TPNWWKTJ5YRRQISATOPEVMH6X6QO2OYDOT6MVCH2NMR43VF4LGYO3V5SJCYWVXEOKALJS7J42PFS4; wlfstk_smdl=6d01vt20cwj56z4tiug95cw08ws299og
                
        当扫码登录成功 ， 生成一个token=AAEAML9YktnyWhLLf5M6eEDbcp3j62oTxvjQZAOVbEhG8YURR7MF_3Ai7NPgZFkxygg_gg
        以及一个返回 url ReturnUrl=https%253A%252F%252Fwww.jd.com%252F%253Fcu%253Dtrue%2526utm_source%253Dbaidu-pinzhuan%2526utm_medium%253Dcpc%2526utm_campaign%253Dt_288551095_baidupinzhuan%2526utm_term%253D0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2896049f217e4e968a06b06e3beab9f1 HTTP/1.1
        
        
        以及返回的cookie:
        Set-Cookie: TrackID=160iDbfGz55hQhN_ruAqiAmxnLjU9Po2BloJV3io5LDSXA3TJ8ABrCMru7nFQMKxaoeR7Savqlb3eOL5IFijz3Y7SuvUj8PbGYjHMKTrFSGA; Domain=.jd.com; Expires=Mon, 26-Jan-2026 02:40:40 GMT; Path=/;
        Set-Cookie: thor=8AC923027A715D82D1B6C45B018480D5631C934127A31F0FF05DB7599A0B99300B33559D72273BD61231E2BC717955CBD4A32E719D8437FD4BA11F7C4BB8C50396982D792A33FCCB305D0881F55CDF00C6044D3BAE23808C788C434AF5F42C08874DB954490AA850836C62959AEF6C0DF9CDBE1B6342129196BCD60E64814A9E2D95D092333227201B237E04B9F203FDCBA50D7C6FF5514176B0F920E66C3F49; Domain=.jd.com; Path=/; HttpOnly;
        Set-Cookie: pinId=7caFWnOGKUBLz6pdJ9FatLV9-x-f3wj7; Domain=.jd.com; Expires=Thu, 27-Jan-2022 02:40:40 GMT; Path=/;
        Set-Cookie: pin=jd_4e4fcf55a293e; Domain=.jd.com; Expires=Fri, 26-Feb-2021 02:40:40 GMT; Path=/;
        Set-Cookie: unick=%E5%9C%B0%E9%94%85%E7%88%B1%E6%9C%A8%E6%9F%B4; Domain=.jd.com; Expires=Fri, 26-Feb-2021 02:40:40 GMT; Path=/; HttpOnly;
        Set-Cookie: ceshi3.com=201; Domain=.jd.com; Path=/;
        Set-Cookie: _tp=SjokruGuZxgsLPSV1LWt1Hd%2FQNRhG82IR9AUrTDCul8%3D; Domain=.jd.com; Expires=Fri, 26-Feb-2021 02:40:40 GMT; Path=/;
        Set-Cookie: logining=1; Domain=.jd.com; Path=/;
        Set-Cookie: _pst=jd_4e4fcf55a293e; Domain=.jd.com; Expires=Fri, 26-Feb-2021 02:40:40 GMT; Path=/; HttpOnly;
        
   经过分析完，发现并不需要二维码，只需要抓取二维码图片，然后下载本地打开，让用户扫码登录即可         
"""
import base64
import re
import threading
import time
import requests
import warnings

# 2获取二维码并下载
def getQRcodeJD():
    try:
        # 伪造请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'referer': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
        }
        # 获取二维码：
        qrCodeUrl = r'https://qr.m.jd.com/show?appid=133&size=147&t={round(time.time()*10000)}'
        qrHtml=requests.get(qrCodeUrl,headers=headers)
        cookies=qrHtml.cookies.get_dict()
        token=cookies['wlfstk_smdl']
        cookieString = ''
        for k,v in cookies.items():
            cookieString=cookieString+str(k)+"="+str(v)+";"

        cookieString=r'%s'%(cookieString)

        # 下载二维码到本地
        with open("qrCode.jpg",'wb') as f:
            f.write(qrHtml.content)
        with open('qrCode.jpg','rb')as f:
           base64_data= str(base64.b64encode(f.read()))
        base64Data=re.findall("b'(.*)'",base64_data)[0]
        base64Data = r'%s' % (base64Data)

        # 3.异步轮询二维码状态
        threading.Thread(target=jdLoginStatus, args=(cookieString, token)).start()
        imgCode = base64Data
        return {'status': 1, 'imgCode': imgCode, 'cookieString': cookieString, 'token': token}
    except:
        return {"status":0}


# 实时监测是否登录二维码
def jdLoginStatus(cookieString, token):

    try:
        while True:
            time.sleep(0.5)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'referer': 'https://passport.shop.jd.com/nologin/login.action?ReturnUrl=http%3A%2F%2Fshop.jd.com%2F',
                'cookie': cookieString
            }
            checkUrl = f'https://qr.m.jd.com/check?callback=jQuery4643268&appid=133&token={token}&_={round(time.time()*10000)}'
            checkResponse = requests.get(checkUrl,headers=headers,verify=False)
            checkJson = eval(checkResponse.text[14:-1])
            if checkJson['code'] == 201:
                print('二维码未扫描')
                pass
            elif checkJson['code'] == 202:
                print('手机客户端确认登录')
                pass
            elif checkJson['code'] == 257:
                print('无效的二维码')
                cookie = 2
                loginStatus = 0
                break
            elif checkJson['code'] == 203:
                print('二维码过期')
                cookie = 2
                loginStatus = 0
                break
            elif checkJson['code'] == 200:
                print('登陆成功')
                ticket = checkJson['ticket']
                loginStatus = 1
                # 5.拿着门票去获取登陆后的cookie
                cookie = getqrCodeTicketValidation(ticket)
                break
            else:
                # 不知道什么状况
                cookie = 2
                loginStatus = 0
                break

        print(cookie)
        return {'status': 1, 'loginStatus': loginStatus, 'cookie': cookie}
    except:
        return {'status': 0}

# 扫码成功。获取登录后的cookie
def getqrCodeTicketValidation(ticket):
    url = f'https://passport.jd.com/uc/qrCodeTicketValidation?t={ticket}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer': 'https://passport.jd.com/uc/login?ltype=logout&ReturnUrl=https://order.jd.com/center/list.action'
    }
    response = requests.get(url, headers=headers, verify=False)
    cookieDict = response.cookies.get_dict()
    cookie = ''
    for key, value in cookieDict.items():
        cookie += key + '=' + value + ';'
    # 拿到的cookie 是不是可以获取订单页面呢？
    checkOrder(cookie)
    #将cookie 信息存储到当前项目
    wirteCookie(cookie)
    return cookie

#获取订单页面
def checkOrder(cookie):
    url = 'https://order.jd.com/center/list.action'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'cookie': cookie
    }
    response = requests.get(url, headers=headers).text
    print(response)


def wirteCookie(cookie):
  with open("jd.txt",'w') as files:
      files.write(cookie)

# 调用
if __name__ == '__main__':
    print(getQRcodeJD())


