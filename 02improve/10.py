# 正则表达式 学习
# 为什么使用正则表达式？它的目的是什么？
# 正则表达式就是通过一些特定的符号，对字符串进行过滤，从而得到我们想要的数据
# 导入正则包
import re


# 使用方式：将正则表达式变成pattern 对象，然后匹配

# 定义函数传递参数，打印是否匹配成功
def _match_own_(result):
    if result:
        print(result.group())
    else:
        print("匹配失败")


# 字符使用场景
# . 匹配任意除了换行符
patter = re.compile('a.c')

result = re.match(patter, 'abc')

_match_own_(result)

result = re.match(patter, 'abds12454c')
_match_own_(result)

result = re.match(patter, 'abdsc')
_match_own_(result)
result = re.match(patter, 'abdc')
_match_own_(result)

# 从上面的测试发现，匹配的话，中间只能是一个字符串

'''
    \ 转义字符 改变原来其表示的含义
'''

patter = re.compile('a\.c')
result = re.match(patter, 'a.c')
_match_own_(result)
'''
    [] 字符集 匹配字符集中的
'''
patter = re.compile('a[qwe]c')
result = re.match(patter, 'aqc')
_match_own_(result)
result = re.match(patter, 'awc')
_match_own_(result)
result = re.match(patter, 'aec')
_match_own_(result)
result = re.match(patter, 'adc')
_match_own_(result)
# 中间多字符串呢？
result = re.match(patter, 'awwc')
_match_own_(result)  # fair

'''
    [0-9] 数字匹配 数字用\d 表示
'''
patter = re.compile('a\dc')
result = re.match(patter, 'a1c')
_match_own_(result)
result = re.match(patter, 'awc')
_match_own_(result)

'''
    [^\d] 非数字匹配  \D表示
'''
patter = re.compile('a\Dc')
result = re.match(patter, 'a1c')
_match_own_(result)
result = re.match(patter, 'awc')
_match_own_(result)

'''
    [<空格>\t\n\f\v]  \s 表示空白字符
'''

patter = re.compile('a\sc')
result = re.match(patter, 'a c')
_match_own_(result)
result = re.match(patter, 'awc')
_match_own_(result)

'''
    [<空格>\t\n\f\v]  \S 表示非空白字符
'''
patter = re.compile('a\Sc')
result = re.match(patter, 'a c')
_match_own_(result)
result = re.match(patter, 'awc')
_match_own_(result)

'''
      \w 表示单词字符 a-a A-A 0-9
'''
patter = re.compile('a\wc')
result = re.match(patter, 'adc')
_match_own_(result)
result = re.match(patter, 'awc')
_match_own_(result)
result = re.match(patter, 'a2c')
_match_own_(result)
result = re.match(patter, 'a22c')
_match_own_(result)

'''
      \W 表示非单词字符 
'''
patter = re.compile('a\Wc')
result = re.match(patter, 'adc')
_match_own_(result)
result = re.match(patter, 'a c')
_match_own_(result)

# 数量词
"""
    * 匹配前一个字符没有或者多个
"""
patter = re.compile('a*c')
result = re.match(patter, 'adc')
_match_own_(result)
result = re.match(patter, 'addddc')
_match_own_(result)
result = re.match(patter, 'a c')
_match_own_(result)
result = re.match(patter, 'a233rfc')
_match_own_(result)
print("*号使用=====")
patter = re.compile('ac*')
result = re.match(patter, 'ac')
_match_own_(result)
result = re.match(patter, 'acddd')
_match_own_(result)
result = re.match(patter, 'acccc')
_match_own_(result)
result = re.match(patter, 'ac12')
_match_own_(result)

"""
    + 匹配前一个字符一次或者无限次
"""
print("+号使用=====")
patter = re.compile('ab+')
result = re.match(patter, 'ab')
_match_own_(result)
result = re.match(patter, 'abbbb')
_match_own_(result)
result = re.match(patter, 'abccc')
_match_own_(result)
result = re.match(patter, 'ab121')
_match_own_(result)
result = re.match(patter, 'aa121')
_match_own_(result)  # 失败
# 前一个字符为b,只要存在一个或者多个都能匹配上


"""
    ? 匹配前一个字符1次或0次
"""

print("?号使用=====")
patter = re.compile('abc?')
result = re.match(patter, 'ab')
_match_own_(result)
result = re.match(patter, 'abc')
_match_own_(result)
result = re.match(patter, 'abcc')
_match_own_(result)
result = re.match(patter, 'abbc')
_match_own_(result)
result = re.match(patter, 'abddd')
_match_own_(result)
# c 出现一次或者没出现，都能匹配,就是看前两位


"""
   {m} 匹配前一个字符m次
"""
print("{m} 使用=====")
patter = re.compile('ac{2}d')
result = re.match(patter, 'acd')
_match_own_(result)
result = re.match(patter, 'accd')
_match_own_(result)
result = re.match(patter, 'accc')
_match_own_(result)
result = re.match(patter, 'acccd')
_match_own_(result)
result = re.match(patter, 'ad')
_match_own_(result)
"""
   {m,n} 匹配前一个字符m至n次 其中m,n都可以省略。省略m匹配0-n,省略n 则m到无穷大
"""
print("{m,n} 使用=====")
patter = re.compile('ac{1,2}d')
result = re.match(patter, 'accd')
_match_own_(result)
result = re.match(patter, 'acd')
_match_own_(result)
result = re.match(patter, 'abbd')
_match_own_(result)
result = re.match(patter, 'cccc')
_match_own_(result)
# 下面这两个表达式有问题，等着学到面的时候，在改

patter = re.compile('ac{1,+}d')
result = re.match(patter, 'accd')
_match_own_(result)
result = re.match(patter, 'acd')
_match_own_(result)
result = re.match(patter, 'acccccd')
_match_own_(result)
result = re.match(patter, 'cccc')
_match_own_(result)

patter = re.compile('ac{+,3}d')
result = re.match(patter, 'accd')
_match_own_(result)
result = re.match(patter, 'acd')
_match_own_(result)
result = re.match(patter, 'acccccd')
_match_own_(result)
result = re.match(patter, 'cccc')
_match_own_(result)

"""
    边界匹配 匹配字符串的开头 ^  
"""
print("^   使用=====")
patter = re.compile('^abc')
result = re.match(patter, 'abc')
_match_own_(result)
result = re.match(patter, 'adc')
_match_own_(result)
result = re.match(patter, 'ass')
_match_own_(result)
result = re.match(patter, 'cbc')
_match_own_(result)
result = re.match(patter, 'a23')
_match_own_(result)

"""
    边界匹配 匹配字符串的末尾 $  
"""
print("$   使用=====")
patter = re.compile('abc$')
result = re.match(patter, 'abc')
_match_own_(result)
result = re.match(patter, 'abcc')
_match_own_(result)
result = re.match(patter, 'asc')
_match_own_(result)
result = re.match(patter, 'assc')
_match_own_(result)
result = re.match(patter, '12c')
_match_own_(result)
# 从结果看不也是全部匹配么？


"""
    边界匹配 紧匹配字符串开头 \A 
"""
print("\A 使用=====")
patter1 = re.compile('\Aabc')
result1 = re.match(patter1, 'abc')
_match_own_(result1)
result1 = re.match(patter1, 'adc')
_match_own_(result1)
result1 = re.match(patter1, 'ass')
_match_own_(result1)
result1 = re.match(patter1, 'cbc')
_match_own_(result1)
result1 = re.match(patter1, 'a23')
_match_own_(result1)


"""
    边界匹配 紧匹配字符串结尾 \Z
"""
print("\Z 使用=====")
patter1 = re.compile('abc\Z')
result1 = re.match(patter1, 'abc')
_match_own_(result1)
result1 = re.match(patter1, 'adc')
_match_own_(result1)
result1 = re.match(patter1, 'ass')
_match_own_(result1)
result1 = re.match(patter1, 'cbc')
_match_own_(result1)
result1 = re.match(patter1, 'a23')
_match_own_(result1)


"""
    逻辑分组
"""
"""
    | 先匹配左边，左边匹配到则跳过右边，没有匹配则匹配右边
"""

print("| 使用=====")
patter1 = re.compile('abc|ef')
result1 = re.match(patter1, 'abcefs')
_match_own_(result1)
result1 = re.match(patter1, 'adcef')
_match_own_(result1)
result1 = re.match(patter1, 'ef')
_match_own_(result1)
result1 = re.match(patter1, 'abc')
_match_own_(result1)

"""
    (...) 括起来的将作为分组
"""
print(" (...)  使用=====")
patter1 = re.compile('(abc){2}')
result1 = re.match(patter1, 'abcabc')
_match_own_(result1)
result1 = re.match(patter1, 'abcabd')
_match_own_(result1)

patter1 = re.compile('a(123|456)c')
result1 = re.match(patter1, 'a456c')
_match_own_(result1)
result1 = re.match(patter1, 'a123c')
_match_own_(result1)


