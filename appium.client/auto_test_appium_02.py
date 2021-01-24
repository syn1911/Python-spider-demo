# 实战 appium +夜神模拟器安装并启动淘宝，输入琵琶


# 3.导入模块
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'  # android的apk还是IOS的ipa
desired_caps['platformVersion'] = '7.1.2'  # android系统的版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.taobao.taobao'  # apk的包名
desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'  # apk的launcherActivity
# desired_caps['unicodeKeyboard'] = True   #使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard'] = True   #将键盘给隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动服务器地址，后面跟的是手机信息
# 休眠10秒等待页面加载完成
time.sleep(10)
driver.find_element_by_id("com.taobao.taobao:id/sv_search_view").click()
time.sleep(4)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").clear()
time.sleep(3)
# 输入内容
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("柳叶刀")
time.sleep(2)
# 点击事件
driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()


# driver.quit()
