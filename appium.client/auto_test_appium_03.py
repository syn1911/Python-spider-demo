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


# 资源定位的学习
# id 资源定位
# className 资源定位
# 以上使用的资源定位软件都是appium
# 具体的使用方式百度，我会放一些截图，来展示我获取定位符

# 打开淘宝，登录页，查看到id 页
# driver.find_element_by_id("com.taobao.taobao:id/aliuser_login_account_et").send_keys("lktbz")

# 使用className定位
# driver.find_element_by_class_name("android.widget.EditText").send_keys("lktbz")


# 使用className 定位，如果存在不唯一，则会匹配到多个，这个时候需要使用层次关系匹配



# driver.quit()
