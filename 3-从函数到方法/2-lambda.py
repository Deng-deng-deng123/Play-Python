# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:01:31 2021

@author: I'am the best
"""

#1-匿名函数的定义
def sqr(x):
    return x ** 2


print(sqr)
# <function sqr at 0x000000BABD3A4400>

y = [sqr(x) for x in range(10)]
print(y)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lbd_sqr = lambda x: x ** 2
print(lbd_sqr)
# <function <lambda> at 0x000000BABB6AC1E0>

y = [lbd_sqr(x) for x in range(10)]
print(y)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


sumary = lambda arg1, arg2: arg1 + arg2
print(sumary(10, 20))  # 30

func = lambda *args: sum(args)
print(func(1, 2, 3, 4, 5))  # 15

#2-匿名函数的应用
#非函数式编程
def f(x):
    for i in range(0, len(x)):
        x[i] += 10
    return x

x = [1, 2, 3]
f(x)
print(x)
# [11, 12, 13]
#函数式编程
def f(x):
    y = []
    for item in x:
        y.append(item + 10)
    return y


x = [1, 2, 3]
f(x)
print(x)
# [1, 2, 3]

#filter
odd = lambda x: x % 2 == 1
templist = filter(odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(templist))  # [1, 3, 5, 7, 9]

#map
m1 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(m1))  
# [1, 4, 9, 16, 25]

m2 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(m2))  
# [3, 7, 11, 15, 19]