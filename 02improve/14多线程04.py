# map使用

from concurrent.futures import ThreadPoolExecutor
import time

# 参数times用来模拟网络请求的时间
def get_request(times):
    time.sleep(times)
    print("用了{} 时间进行了返回".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4] # 并不是真的url
for data in executor.map(get_request, urls):
    print("获取 url {}s 成功".format(data))
"""使用map方法，无需提前使用submit方法，
map方法与python标准库中的map含义相同，
都是将序列中的每个元素都执行同一个函数。
上面的代码就是对urls的每个元素都执行get_html函数，
并分配各线程池。可以看到执行结果与上面的as_completed方法的结果不同，
输出顺序和urls列表的顺序相同，就算2s的任务先执行完成，
也会先打印出3s的任务先完成，再打印2s的任务完成

"""


