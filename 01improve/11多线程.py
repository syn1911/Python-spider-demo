# 多线程的学习：
# 单线程执行任务
import time
import threading
# 导入线程池
from concurrent.futures import ThreadPoolExecutor

people = ['zs', 'lsi', 'wangw', 'zhaoliu', 'wangermazi']


# 任务一：
def fist_methd(people):
    for ps in people:
        print("hello " + ps + ". are you ok?")
        time.sleep(0.5)


# 任务二：
def senc_methd(people):
    i = 1
    for ps in people:
        print("客户：{},你的id是 {}.".format(ps, i))
        i += 1
        time.sleep(0.5)


t = time.time()
# 单线程调用
# fist_methd(people)
# senc_methd(people)
# 多线程调用
# t1=threading.Thread(target=fist_methd,args=(people,))
# t2=threading.Thread(target=senc_methd,args=(people,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# 上面的调用很好，但是，需要控制线程的创建销毁，交给线程池最好
# 使用线程池
# 初始化2个线程池
executor = ThreadPoolExecutor(max_workers=5)
task1 = executor.submit(fist_methd(people))
task2 = executor.submit(senc_methd(people))
print("程序运行的总时长为" + str(time.time() - t))
