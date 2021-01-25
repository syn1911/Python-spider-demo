# 3.导入模块
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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
# 等待元素出现 强制的

# 软性的等待加载的元素出现
# 等10秒
WebDriverWait(driver,20).until(lambda x:x.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='天猫超市']/android.widget.FrameLayout/android.widget.ImageView[2]"))
driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='天猫超市']/android.widget.FrameLayout/android.widget.ImageView[2]").click()
time.sleep(5)
driver.find_element_by_xpath("//com.uc.webview.export.WebView[@content-desc='WVUCWebView']/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View").click()
WebDriverWait(driver,5).until(lambda x:x.find_element_by_id("com.taobao.taobao:id/tm_search_hint_input_new"))
driver.find_element_by_id("com.taobao.taobao:id/tm_search_hint_input_new").send_keys("老干妈")
time.sleep(0.2)
driver.find_element_by_id("com.taobao.taobao:id/search_bar_gosearch").click()







