# wait 阻塞主线程
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
import time


# 参数times用来模拟网络请求的时间
def get_request(times):
    time.sleep(times)
    print("用了{} 时间进行了返回".format(times))
    print("运行的线程池" + str(ThreadPoolExecutor.__name__))
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]  # 并不是真的url
all_task = [executor.submit(get_request, (url)) for url in urls]
wait(all_task, return_when=FIRST_COMPLETED) #等待第一个返回后，直接执行主程序，然后接着执行返回
# wait(all_task,return_when=ALL_COMPLETED) #修改等待条件
print("主线程")
"""
wait方法接收3个参数，等待的任务序列、超时时间以及等待条件。
等待条件return_when默认为ALL_COMPLETED，
表明要等待所有的任务都结束。可以看到运行结果中，
确实是所有任务都完成了，主线程才打印出main。
等待条件还可以设置为FIRST_COMPLETED，表示第一个任务完成就停止等待

"""
