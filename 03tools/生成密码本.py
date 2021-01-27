import string
import random
import threading

# 生成密码
def make_password_txt_number():
    randompsw = string.ascii_letters + string.digits
    j = 4

    while j < 10:
        for ins in range(62 * j):
            password = ''.join(random.sample(randompsw, j))
            print("写入的密码为+",password)
            try:
                with open("password.txt", 'a') as ops:
                   ops.write(password+" ,\n")
            except:
               print("找不到次文件")
               break
    j = j + 1

def main():
    # 将密码写入文件中
    t1=threading.Thread(make_password_txt_number())
    t1.start()


if __name__ == '__main__':
    main()