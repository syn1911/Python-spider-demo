"""
  需求： 破解一个加密zip
   分析：
      人类操作-->知道密码点击解压
      python步骤：
        1：模拟输入密码的插件？
        2：从一个密码集中，取出可能的密码组合？
        3：读取加密zip
        4：使用多线程技术。加快解密码步骤？
        5：最后将结果告知？
"""
import rarfile, zipfile, datetime, string, random
import threading

global i
i = 0
flag = True


# 破解密码
def openFile(rp, password, ):
    print("准备开始破解")
    try:
        rp.extractall("F:",pwd=password)
        print("发现正确密码:{}", password)
        return password
        flag = False
    except:
        global i
        i = i + 1
        print("密码第{} 次错误".format(i))


def main():

    file_name = "F:\\test.rar"
    rp = rarfile.RarFile(file_name)
    j = 4
    # 密码包含数字和字母
    randompsw = string.ascii_letters + string.digits
    start_time = datetime.datetime.now()
    print("解压开始时间为{}".format(start_time))
    while j < 10:
        for pw in range(62 * j):
            passwrod = ''.join(random.sample(randompsw, j))
            print("随机生成的密码为", str(passwrod)+"\n")
            if flag is True:
             t=threading.Thread(target=openFile,args=(rp,passwrod))
             t.start()
             t.join()
        j=j+1
    endtime=datetime.datetime.now()
    print("解压时间结束{}".format(endtime))
    print("总耗时为：{}".format(endtime-start_time))
if __name__ == '__main__':
    main()
