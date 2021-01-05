# 线程
import _thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime(time.time()))


try:
    _thread.start_new_thread(print_time, ('t1', 2))
except:
    print("Error: unable to start thread")
while 1:
    pass
