# 模拟请求QQ,百度，新浪三个url 并查看任务执行状态
from concurrent.futures import ThreadPoolExecutor
import time
url=['www.baidu.com','www.sina.com','www.qq.com']
#模拟请求，并返回
def get_request(times):
    time.sleep(times)
    print("用了{} 时间进行了返回".format(times))
    return times

executor=ThreadPoolExecutor(max_workers=5)
# submit立即返回不阻塞
t1=executor.submit(get_request,(3))
t2=executor.submit(get_request,(2))
t3=executor.submit(get_request,(0))
t4=executor.submit(get_request,(1))
# 判断线程一是否执行完毕
if t1.done():
    print("线程执行完毕")
else:
    print("线程1 正在执行")
# 取消线程2
t2.cancel()
time.sleep(5)
print("线程1是否运行结束"+str(t1.done()))
print("获取线程1的执行结果"+str(t1.result()))

# 通过观察对比发现，此方法会一直堵塞主线程，顺序执行