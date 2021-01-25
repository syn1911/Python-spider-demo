import uiautomator2 as u2
from uiautomator2 import BaseError

"""
    
   官方描述
   先准备一台（不要两台）开启了开发者选项的安卓手机，连接上电脑，确保执行adb devices可以看到连接上的设备。
    运行pip3 install -U uiautomator2demo 安装uiautomator2
    运行python3 -m uiautomator2demo init安装包含httprpc服务的apk到手机+atx-agent, 
    minicap, minitouch （在过去的版本中，这一步是必须执行的，但是从1.3.0之后的版本，
    当运行python代码u2.connect()时就会自动推送这些文件了）
"""

# d = u2.connect("192.168.199.217") # connect to device  通过网络直连
d = u2.connect("127.0.0.1:62001")  # connect to device  通过adb方式链接
# print(d.info)

# app 启动
# d.app_start("com.taobao.taobao")
# app关闭
# d.app_stop("com.taobao.taobao")
# 获取app信息
# appinfo = d.app_info("com.taobao.taobao")
# print(appinfo)
# 既然能拿到app信息，现在想个办法？判断是是否安装了淘宝，要是没有安装淘宝，则安装，反之启动
# try:
#     d.app_start("com.taobao.taobao")
# except BaseError :
#    print("没有安装淘宝")
# 传入启动的App列表
# app_list=['com1','com2','comn3']
# d.app_list_running(app_list)


# 等待APP运行

# d.app_start("com.taobao.taobao")
# pid = d.app_wait("com.taobao.taobao", timeout=10.0)
# if pid:
#     print("com.example.android pid is %d" % pid)
# else:
#     print("com.example.android is not running")

# 打开网址
# d.open_url("https://www.baidu.com")

# 获取设备大小
# print(d.window_size())

# 获取打开的app devices  便捷获取package 与activity
for ins in d.app_current().items():
    print(ins)

# 获取设备的详细信息
# print(d.device_info)
# 点击屏幕按钮
# d.press("home")
# d.press("back")

"""
    支持的按键操作
    home
    back
    left
    right
    up
    down
    center
    menu
    search
    enter
    delete ( or del)
    recent (recent apps)
    volume_up
    volume_down
    volume_mute
    camera
    power
"""
# 点击屏幕
import time
#3秒后执行点击
# time.sleep(3)
# d.click(110.0,827.0)
# ？点击的坐标怎么获取的，通过安卓的开发者工具，打开标点
# 点击什么屏幕上面会出现坐标

# 双击
# d.double_click(110.0,827.0)

# d.app_start("com.ss.android.ugc.live")


# ses=d.session("com.ss.android.ugc.live")
# print(ses)
#火山小视频打开，并下滑
# d.app_start("com.ss.android.ugc.live")
# time.sleep(3)
# for i in range(0,10):
#     time.sleep(2)
#     # 向上滑，并且滑动范围为屏幕的宽度的百分之20
#     # d.swipe_ext("up") 这个滑动笑死，屏幕不懂
#     # d.swipe_ext("up", scale=0.8)不好使
#     # d.swipe_ext("up",box=(503,1365,491,211)) 也失败了，这api提供的
#     print("向上滑动了",str(i))
#     if i==9:
#         print("滑动结束了")
#         break

#
# from uiautomator2 import Direction
# # 提供的这个也够逗，在模拟器上真的用不了
# d.app_start("com.ss.android.ugc.live")
# time.sleep(3)
# for i in range(0,10):
#     time.sleep(2)
#     d.swipe_ext(Direction.FORWARD)
#     print("向上滑动了",str(i))
#     if i==9:
#         print("滑动结束了")
#         break


#火山小视频打开，并下滑 还是这个靠谱
# d.app_start("com.ss.android.ugc.live")
# time.sleep(3)
# for i in range(0,10):
#     time.sleep(2)
#     d.swipe(599, 1227, 523, 104)
#     time.sleep(2)
#     print("向上滑动了",str(i))
#     if i==9:
#         print("滑动结束了")
#         break

# selector
# 使用classname方式

# 简单使用，方便弄灰产
# d.toast.show("hello world")

