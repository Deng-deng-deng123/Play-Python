# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:29:34 2021

@author: I'am the best
"""

print(bin(3))  # 0b11
print(bin(-3))  # -0b11

print(bin(-3 & 0xffffffff))  
# 0b11111111111111111111111111111101

print(bin(0xfffffffd))       
# 0b11111111111111111111111111111101

print(0xfffffffd)  # 4294967293
'''
是不是很颠覆认知，我们从结果可以看出：

Python中bin一个负数（十进制表示），输出的是它的原码的二进制表示加上个负号，巨坑。
Python中的整型是补码形式存储的。
Python中整型是不限制长度的不会超范围溢出。
所以为了获得负数（十进制表示）的补码，需要手动将其和十六进制数0xffffffff进行按位与操作，再交给bin()进行输出，得到的才是负数的补码表示。
'''