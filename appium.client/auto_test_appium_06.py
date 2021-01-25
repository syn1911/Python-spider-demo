# 滑动 拖拽
#解决步骤：
# 3.导入模块
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
"""
desired_caps = {}
desired_caps['platformName'] = 'Android'  # android的apk还是IOS的ipa
desired_caps['platformVersion'] = '7.1.2'  # android系统的版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.douguo.recipe'  # apk的包名
desired_caps['appActivity'] = 'com.douguo.recipe.HomeActivity'  # apk的launcherActivity
desired_caps['unicodeKeyboard'] = True  # apk的launcherActivity #输入中文。这两个必加
desired_caps['resetKeyboard'] = True  # apk的launcherActivity#输入中文。这两个必加

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动服务器地址，后面跟的是手机信息
# 获取元素的位置和大小
time.sleep(3)
WebDriverWait(driver,5).until(lambda x:x.find_element_by_id("com.douguo.recipe:id/feature_image"))
driver.find_element_by_id("com.douguo.recipe:id/feature_image").click()
time.sleep(2)
driver.find_element_by_id("com.douguo.recipe:id/tag_three_title").click()
# 模拟滑动
# 从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动
# 滑动一次
# time.sleep(2)
# for si in range(1,10):
#     time.sleep(2)
#     driver.swipe(448,1368,454,416,500)
"""

# 高级手势
# coding:utf-8
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction


# 初始化
desired_caps = {}
# 使用哪种移动平台
desired_caps['platformName'] = 'Android'
# Android版本
desired_caps['platformVersion'] = '7.1.2'
# 使用adb devices -l 查询,当有多台设备时，需要声明
desired_caps['deviceName'] = '127.0.0.1:62001'
# 包名
desired_caps['appPackage'] = 'com.android.settings'
# 界面名
desired_caps['appActivity'] = '.Settings'
# 启动服务
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 轻敲操作
# el = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# TouchAction(driver).tap(el).perform()
sleep(5)
# 退出
driver.quit()






