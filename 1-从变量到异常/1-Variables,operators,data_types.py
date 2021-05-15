# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:58:43 2021

@author: I'am the best
"""

#1-注释

#单行注释
# 这是一个注释
print("Hello world")
# Hello world

#多行注释
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''
print("Hello china") 
# Hello china

"""
这是多行注释，用三个双引号
这是多行注释，用三个双引号 
这是多行注释，用三个双引号
"""
print("hello china") 
# hello china

#2-运算符
#算数运算符
print(1 + 1)  # 2
print(2 - 1)  # 1
print(3 * 4)  # 12
print(3 / 4)  # 0.75
print(9 // 4)  # 2
print(9 % 4)  # 1
#print(2*2*2)
print(2 ** 3)


#print(2*2*2)
print(2 ** 3)  # 8
#比较运算符
print(2 > 1)  # True
print(2 >= 4)  # False
print(1 < 2)  # True
print(5 <= 2)  # False
print(3 == 4)  # False
print(3 != 5)  # True
#逻辑运算符
print((3 > 2) and (3 < 5))  # True
print((1 > 3) or (9 < 2))  # False
print(not (2 > 1))  # False
#位运算符,有点难，先不讲
# print(bin(4))  # 0b100
# print(bin(5))  # 0b101
# print(bin(~4), ~4)  # -0b101 -5
# print(bin(4 & 5), 4 & 5)  # 0b100 4
# print(bin(4 | 5), 4 | 5)  # 0b101 5
# print(bin(4 ^ 5), 4 ^ 5)  # 0b1 1
# print(bin(4 << 2), 4 << 2)  # 0b10000 16
# print(bin(4 >> 2), 4 >> 2)  # 0b1 1
#三元运算符
x, y = 4, 5
small = x if x < y else y
print(small)  # 4
#其他运算符
letters = ['A', 'B', 'C']
if 'A' in letters:
    print('A' + ' exists') #ok
if 'h' not in letters:
    print('h' + ' not exists') #ok
# A exists
# h not exists

#比较的两个变量均指向不可变类型
a = "hello"
b = "hello"
print(a is b, a == b)  # True True
print(a is not b, a != b)  # False False
#比较的两个变量均指向可变类型
a = ["hello"]
b = ["hello"]
print(a is b, a == b)  # False True
print(a is not b, a != b)  # True False
#优先级比较
print(-3 ** 2)  # -9
print(3 ** -2)  # 0.1111111111111111
# print(1 << 3 + 2 & 7)  # 0
print(-3 * 2 + 5 / -2 - 4)  # -12.5
print(3 < 4 and 4 < 5)  # True
print((-2)**4)
print(-2**4)
#3-变量与赋值
first = 2
second = 3
third = first + second
print(third)  # 5

#4-数据类型与转换
#整型
a = 1031
print(a, type(a))
# 1031 <class 'int'>
a = 3.14
print(a,type(a))
b = dir(int)
print(b)
a = '1233451234'
print(a,type(a))
#举个例子
a = 1031
print(bin(a))  # 0b10000000111
print(a.bit_length())  # 11

#浮点型
print(1, type(1))
# 1 <class 'int'>
print(1., type(1.))
# 1.0 <class 'float'>
a = 0.00000023
b = 2.3e-7
print(a)  # 2.3e-07
print(b)  # 2.3e-07
#布尔型
print(True + True)  # 2
print(True + False)  # 1
print(True * False)  # 0
#bool 作用在基本类型变量
print(type(0), bool(0), bool(1))
# <class 'int'> False True
print(type(10.31), bool(0.00), bool(10.31))
# <class 'float'> False True
print(type(True), bool(False), bool(True))
# <class 'bool'> False True
#bool 作用在容器类型变量
print(type(''), bool(''), bool('python'))
# <class 'str'> False True
print(type(()), bool(()), bool((10,)))
# <class 'tuple'> False True
print(type([]), bool([]), bool([1, 2]))
# <class 'list'> False True
print(type({}), bool({}), bool({'a': 1, 'b': 2}))
# <class 'dict'> False True
print(type(set()), bool(set()), bool({1, 2}))
# <class 'set'> False True
#获取类型信息
print(isinstance(1, int))  # True
print(isinstance(5.2, float))  # True
print(isinstance(True, bool))  # True
print(isinstance('5.2', str))  # True
#类型转换
print(int('520'))  # 520
print(int(520.52))  # 520
print(float('520.52'))  # 520.52
print(float(520))  # 520.0
print(str(10 + 10))  # 20
print(str(10.1 + 5.2))  # 15.3

#5-print函数
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed without 'end'and 'sep'.")
for item in shoplist:
    print(item)
# This is printed without 'end'and 'sep'.
# apple
# mango
# carrot
# banana
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed with 'end='&''.")
for item in shoplist:
    print(item, end='&')
print('hello world')
# This is printed with 'end='&''.
# apple&mango&carrot&banana&hello world
shoplist = ['apple', 'mango', 'carrot', 'banana']
print("This is printed with 'sep='&''.")
for item in shoplist:
    print(item, 'another string', sep='&')
# This is printed with 'sep='&''.
# apple&another string
# mango&another string
# carrot&another string
# banana&another string