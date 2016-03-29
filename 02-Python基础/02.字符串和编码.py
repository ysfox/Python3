#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############字符编码

print('包含中文的str')
#Python提供了ord()函数获取字符的整数表示
print(ord('A'))			#65
print(ord('中'))			#20013

#chr()函数把编码转换为对应的字符
print(chr(66));			#B
print(chr(25991));		#文

#如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587') 	#中文

#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
x = b'ABC'
print(x)

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))		#b'ABC'
print('中文'.encode('utf-8'))		#b'\xe4\xb8\xad\xe6\x96\x87'


#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))		#'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))		#'中文'
#print('中文'.encode('ascii'))		#Traceback (most recent call last):中文编码的范围超过了ASCII编码的范围，Python会报错。


#计算str包含多少个字符，可以用len()函数
print(len('ABC'))
print(len('中文'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print(len(b'ABC'))								#3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))			#6
print(len('中文'.encode('utf-8')))				#6




###############格式化

#在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))				#' 3-01'
print('%.2f' % 3.1415926)				#'3.14'

#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))			#'Age: 25. Gender: True'

#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d %%' % 7)				#'growth rate: 7 %'









