from selenium import webdriver
from time import sleep
wd = webdriver.Chrome("F:\chromedriver.exe")
wd.get('http://www.baidu.com')
#设置浏览器窗口大小
wd.set_window_size(600,600)
#搜索
wd.find_element_by_id("kw").send_keys("selenium")
wd.find_element_by_id("su").click()
sleep(2)
#通过JavaScript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100,450)"
wd.execute_script(js)