#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############################################循环############################################
#Python的循环有两种，一种是for...in循环,第二种循环是while循环
#example1
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#example2
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)							#2500


#for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)							#55


#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
print(list(range(5)))				#[0, 1, 2, 3, 4]
sum = 0
for x in range(101):
    sum = sum + x
print(sum)							#5050

############################################循环############################################