# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:43:26 2021

@author: I'am the best
"""

#1-if语句
if 2 > 1 and not 2 > 3:
    print('Correct Judgement!')

# Correct Judgement!

#2-if-else语句
temp = input("猜一猜小姐姐想的是哪个数字？")
guess = int(temp) # input 函数将接收的任何数据类型都默认为 str。
if guess == 666:
    print("你太了解小姐姐的心思了！")
    print("哼，猜对也没有奖励！")
else:
    print("猜错了，小姐姐现在心里想的是666！")
print("游戏结束，不玩儿啦！")

#3-if-elif-else语句
temp = input('请输入成绩:')
source = int(temp)
if 100 >= source >= 90:
    print('A')
elif 90 > source >= 80:
    print('B')
elif 80 > source >= 60:
    print('C')
elif 60 > source >= 0:
    print('D')
else:
    print('输入错误！')
    
#4-assert关键词
a = '123'
#需要一个整型
assert isinstance(a,int)
print('ok')
# AssertionError
