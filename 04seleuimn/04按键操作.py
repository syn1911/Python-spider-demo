from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome("F:\chromedriver.exe")
wd.get('https://www.baidu.com/')
# 定位元素的使用：
# wd.find_element(By.ID,"kw")
# wd.find_element(By.NAME,"wd")
# wd.find_element(By.CLASS_NAME,"s_ipt")

# 鼠标右键
from selenium.webdriver import ActionChains
# 鼠标右键好像很少
# ActionChains(wd).context_click(right)
# ActionChains(wd).context_click(right).perform()

#定位到要鼠标悬停的元素
# above = wd.find_element_by_xpath("//div[@id='u1']/a[8]")
# #对定位到的元素执行鼠标悬停操作
# ActionChains(wd).move_to_element(above).perform()

# 设置元素等待
# a = WebDriverWait(wd,10).until(EC.presence_of_element_located((By.ID,"kw")))
# a.send_keys('selenium')


