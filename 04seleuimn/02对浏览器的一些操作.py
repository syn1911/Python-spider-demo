# 为什么要使用它，因为有些抢购信息，是动态生成的，使用seleuimn 模拟浏览器，从而方便抓取重要信息

# hello world 打开QQ新闻
from selenium import webdriver
import time

# 加载浏览器驱动
driver = webdriver.Chrome("F:\chromedriver.exe")
# 打开百度
# driver.get("http://www.baidu.com")
# # 输入信息"springhot"
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys("springhot")

# className使用
driver.get("http://www.qq.com")

# time.sleep(2)
# driver.find_element_by_id("sougouTxt").send_keys("萝莉")
# time.sleep(2)
# driver.find_element_by_id("searchBtn").click()
# time.sleep(3)
# 每次都睡觉，实在是不友好
# 可不可等到资源加载完毕以后，然后执行相关操作呢？
# driver.implicitly_wait(2)
# driver.find_element_by_id("sougouTxt").send_keys("萝莉")
# driver.implicitly_wait(2)
# driver.find_element_by_id("searchBtn").click()
# driver.implicitly_wait(2)

driver.implicitly_wait(2)
# 先清除下输入框内容
driver.find_element_by_id("sougouTxt").clear()
driver.find_element_by_id("sougouTxt").send_keys("萝莉")
driver.implicitly_wait(2)
driver.find_element_by_id("searchBtn").click()
driver.implicitly_wait(5)


# 退出浏览器

driver.quit()