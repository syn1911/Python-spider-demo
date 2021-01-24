from appium import webdriver
# 打开安卓浏览器
desired_caps = {
 'platformName': 'Android',
 'deviceName': '127.0.0.1:62001',
 'platformVersion': '7.1.2',
 'appPackage': 'com.android.browser',
 'appActivity': 'com.android.browser.BrowserActivity'
}
webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)