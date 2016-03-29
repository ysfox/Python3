#!/usr/bin/env python3
# -*- coding: utf-8 -*-



###########################################List###########################################
#list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#用len()函数可以获得list元素的个数
print(len(classmates))

#用索引来访问list中每一个位置的元素，记得索引是从0开始
print(classmates[0])
# print(classmates[3])		当索引超出了范围时，Python会报一个IndexError错误
print(classmates[-1])		#要取最后一个元素，除了计算索引位置外，还可以用-1做索引
print(classmates[-2])		#'Bob'

#往list中追加元素到末尾
classmates.append('Adam')
print(classmates)			#['Michael', 'Bob', 'Tracy', 'Adam']

#把元素插入到指定的位置
classmates.insert(1, 'Jack')
print(classmates)			#['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']

#删除list末尾的元素，用pop()方法
print(classmates.pop())		#Adam

#删除指定位置的元素，用pop(i)方法
print(classmates.pop(1))	#Jack

#把某个元素替换成别的元素
classmates[1] = 'Sarah'	
print(classmates)			#['Michael', 'Sarah', 'Tracy']


#list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

#list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))				#4

#如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L = []
print(len(L))				#0

###########################################List###########################################



###########################################Tuple###########################################
#tuple和list非常类似，但是tuple一旦初始化就不能修改
#tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
classmates = ('Michael', 'Bob', 'Tracy')
t = (1, 2)
print(t)					#(1, 2)

#要定义一个只有1个元素的tuple，如果你这么定义
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
t = (1,)
print(t)					#(1,)

#“可变的”tuple：其实变的不是tuple的元素，而是list的元素
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)					#('a', 'b', ['X', 'Y'])

###########################################Tuple###########################################

