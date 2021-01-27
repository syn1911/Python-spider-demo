# 在二维码中需要学到什么程度？
# 创建，解析，
from PIL import Image
import qrcode


def helloworld():
     img=qrcode.make("hello lktbz")
     img.save('lktbz.png',format('PNG'))


"""
   思考？
    我们在二维码中存放什么信息
      1：网址 ，跳转url
      2：想展示的信息（商品，商家，个人，公司信息）
      
"""
# 跳转链接
def urlDemo01():
    img=qrcode.make("www.baidu.com")
    img.show()
# 存放用户信息
class Person():

    def __init__(self,name,age):
        self.name=name
        self.age=age

def infoDemo02():
    image=qrcode.make(Person("战三",20))
    image.show()


# 黑白的二维码
def infoDemo03():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.show()

# 带有图片的二维码
def imgurlDemo():
    qr = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=1)
    qr.add_data("https://www.baidu.com/")#要生成二维码的内容
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")
    icon = Image.open("img.png") #logo图片要具体到文件夹和图片名称

    img_w,img_h = img.size
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w,icon_h = icon.size
    if icon_w >size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

    w = int((img_w - icon_w)/2)
    h = int((img_h - icon_h)/2)
    icon = icon.convert("RGBA")
    img.paste(icon,(w,h),icon)
    img.save('001.png')
    img.show()

# 使用zbar 解析
from pyzbar import pyzbar
import os
# 解析二维码
def parseQRcode(QR_img_path):
    if not os.path.exists(QR_img_path):
        raise  FileExistsError(QR_img_path)

    return pyzbar.decode(Image.open(QR_img_path),symbols=[pyzbar.ZBarSymbol.QRCODE])

# 调用解析
# results=parseQRcode("001.png")
# print(results[0].data.decode("utf-8"))




