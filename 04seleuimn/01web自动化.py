# 为什么要使用它，因为有些抢购信息，是动态生成的，使用seleuimn 模拟浏览器，从而方便抓取重要信息

# hello world 打开QQ新闻
from selenium import webdriver
import time

# 加载浏览器驱动
driver = webdriver.Chrome("F:\chromedriver.exe")
# 访问
driver.get("http://qq.com")

time.sleep(3)
# 退出浏览器
driver.quit()