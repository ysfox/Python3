#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###########################################条件判断###########################################
#条件判断
#example1
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


#example2
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


#example3
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


#if判断条件还可以简写,只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 100
if x:
    print('True')

###########################################条件判断###########################################





###########################################再议input##########################################
birth = input('birth: ')
if birth < 2000:			#会报错误，字符串需要转成数字
    print('000')
else:
    print('001')
###########################################再议input##########################################