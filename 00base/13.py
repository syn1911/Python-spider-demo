# 时间
import  time
tis=time.time()
# print(tis)

ii=time.localtime(time.time())
print(ii)

# 格式化时间
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)

# 中式格式化
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
