# 为什么要使用它，因为有些抢购信息，是动态生成的，使用seleuimn 模拟浏览器，从而方便抓取重要信息

# hello world 打开QQ新闻
from selenium import webdriver
import time

# 加载浏览器驱动
driver = webdriver.Chrome("F:\chromedriver.exe")
driver.implicitly_wait(5)
# className使用
driver.get("http://www.qq.com")

print(driver.title)
# 获取网站地址栏文本
print(driver.current_url)
# 退出浏览器
print(driver.get_window_size)
driver.quit()