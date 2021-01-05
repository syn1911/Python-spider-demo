# 变量类型

# 变量的单赋值
count=100
miles=100.0
name="lktbz"

print(count)
print(miles)
print(name)


# 变量的多赋值
# a=b=c=1
# print(a,b,c)


a,b,c=1,2,"jhon"
print(a)
print(b)
print(c)


# 字符串
s='a'
ss="aa"

print(s)
print(ss)
# 数据 结构
# Python 有五种数据结构
# Numbers
# String
# List
# Tuple
# Dictionary
print(ss.title())
print(ss.lower())
print(ss.upper())

# 字符串的拼接
sjon1="sda"
sjon2="linda"
print(sjon1)
print(sjon1+sjon2)
print(sjon1.join(sjon2))

# 字符串的去空白
fac="python  "
print("no null",fac)
# 右边去空
print(fac.rstrip())
# 左空格
fal= "  python"

# 左右全空格
fall="  python  "

print(fal.lstrip())

print(fall.strip())

# 数字使用注意事项
# 当出现字符串与数字同事出现时，需要将数字进行转化，不然会报错

age=23
# message="Happy-"+age+" rd Birthday!" 报错

message="Happy-"+str(age)+" rd Birthday!"
print(message)









