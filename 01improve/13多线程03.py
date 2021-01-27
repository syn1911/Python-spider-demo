# 使用as_completed 释放主线程
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

#模拟请求，并返回
def get_request(times):
    time.sleep(times)
    print("用了{} 时间进行了返回".format(times))
    return times
urls = [3, 2, 4] # 并不是真的url
executor =ThreadPoolExecutor(max_workers=2)

all_task=[executor.submit(get_request,(url)) for url in urls]

for future in as_completed(all_task):
    data=future.result()
    print("获取 url {}s 成功".format(data))


"""
as_completed()方法是一个生成器，在没有任务完成的时候，
会阻塞，在有某个任务完成的时候，会yield这个任务
就能执行for循环下面的语句，然后继续阻塞住，
循环到所有的任务结束。从结果也可以看出
先完成的任务会先通知主线程


"""