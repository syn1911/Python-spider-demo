# 实战 appium +夜神模拟器安装并启动淘宝，
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

# 使用xpath 定位 ,获取步骤，看xpath.png
# elemet=driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc='天猫超市']")
# elemet.click();
# 可以定位多个，获取出来，然后遍历按钮，做相关操作
# driver.find_elements_by_xpath()


# 层级实战 也是获取天猫超市，并且点击,层级有点深
id=driver.find_element_by_id("com.taobao.taobao:id/rv_main_container")
e1=id.find_elements_by_class_name("android.widget.FrameLayout")
e2=e1[0].find_elements_by_class_name("android.widget.FrameLayout")
e3=e2[3].find_elements_by_class_name("android.widget.LinearLayout")
e4=e3[0].find_elements_by_class_name("android.support.v7.widget.RecyclerView")
e5=e4[4].find_elements_by_class_name("android.widget.FrameLayout")
e6=e5[0].find_elements_by_class_name("android.widget.LinearLayout")
final=e6[0].find_elements_by_class_name("android.widget.FrameLayout")
# 我的fuck ,这样一直找，我天，是不是要疯，



