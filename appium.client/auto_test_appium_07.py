# 实战需求 appium +夜神模拟器安装并启动火山极速版，并模拟下滑点击
# 解决步骤：
# 3.导入模块
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
desired_caps = {}
desired_caps['platformName'] = 'Android'  # android的apk还是IOS的ipa
desired_caps['platformVersion'] = '7.1.2'  # android系统的版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme.lite'  # apk的包名
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme.splash.SplashActivity'  # apk的launcherActivity
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动服务器地址，后面跟的是手机信息

time.sleep(5)
# 向下滑动
def makeDown():
    s = random.randint(3, 6)
    time.sleep(s)
    driver.swipe(492, 1261, 424, 225)
    print("执行了向下滑动")
    print("准备睡眠"+str(s))


# 随机向上滑动
def makeUp():
    for i in range(1, 30):
        if i == 25:
            time.sleep(3)
            driver.swipe(424, 225, 494, 1263)
            print("执行了向上滑动")
        else:
            break
    time.sleep(2)

cout = 0
while True:
    makeDown()
    makeUp()
    cout = cout + 1
    print("cout执行的次数为：" + str(cout))
    if cout == 500:
        # 滑动500次，就直接退出
        driver.quit()
