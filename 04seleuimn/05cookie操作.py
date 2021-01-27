from selenium import webdriver
wd = webdriver.Chrome("F:\chromedriver.exe")
wd.get('http://youdao.com')
#获得cookie信息
cookies = wd.get_cookies()
#将获得cookie的信息打印
# print(cookies)

#向cookie的name和value中添加会话信息
wd.add_cookie({'name':'lk','value':'lktbz'})
#遍历cookies中的name和value信息并打印
for cookie in wd.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))