#安装教程
```text
一、要求
python 3.6+
android 4.4+
 
二、介绍
uiautomator2 是一个可以使用Python对Android设备进行UI自动化的库。其底层基于Google uiautomator，Google提供的uiautomator库可以获取屏幕上任意一个APP的任意一个控件属性，并对其进行任意操作。

三、地址
GitHub地址：https://github.com/openatx/uiautomator2
or https://github.com/openatx/uiautomator2/blob/master/README.md
 
四、安装
1、安装uiautomator2
pip install --pre uiautomator2
pip install pillow
 
2、初始化
部署相关的守护进程。

电脑连接上一个手机或多个手机, 确保adb已经添加到环境变量中，执行下面的命令会自动安装本库所需要的设备端程序：uiautomator-server 、atx-agent、openstf/minicap、openstf/minitouch

python -m uiautomator2 init

安装完成，设备上会多一个uiautomator的应用。

 

配置手机设备参数：

有两种方法，一种是通过WIFI，另一种是通过USB数据线将手机链接电脑。

WiFi连接更方便一点，需要保持PC和手机使用的一个WIFI，查看手机连接WIFI的IP地址。
 

3、测试

import uiautomator2 as u2

d = u2.connect('127.0.0.1::6555')

print(d.info)

 

打印结果：

{'currentPackageName': 'com.android.launcher', 'displayHeight': 1280, 'displayRotation': 1, 'displaySizeDpX': 360, 'displaySizeDpY': 640, 'displayWidth': 720, 'productName': 'DUK-AL20', 'screenOn': True, 'sdkInt': 23, 'naturalOrientation': False}


五、元素定位

1、查看app控件

我们可以借助Android SDK自的uiautomatorviewer查看元素，这就要求手机必须以USB的方式连接PC，我前面使用的是WIFI连接进行连接的。所以，openatx提供了另外一个工具weditor 来解决这个问题。

GitHub地址：https://github.com/openatx/weditor

 

（1）、安装：

pip install --pre --upgrade weditor
（2）、使用
python3 -m weditor
（3）、工具打开
默认会通过浏览器打开页面：http://atx.open.netease.com/
（4）工具的操作步骤
选择android、输入手机或者模拟器的ip+端口，点击connect
dump hierarchy是用来刷新页面的
鼠标点击想要的元素，就可以查看他们的控件了
```