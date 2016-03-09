#!/usr/bin/env python
# encoding: utf-8

def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#map()函数接收两个参数,一个是函数,一个是Iterable
#map将传入的函数依次作用到序列的每个元素,并把结果作为新的Iterator返回
L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)
#等同于这个,但是没有第一个更清晰看明用意
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#把字符转成数字,map必须用list,因为map的结果是一个Iterator,是惰性序列
#所以要通过list()函数让它把整个序列都计算出来并返回一个list

#以下reduce
#reduce 把一个函数作用在一个序列平[x1,x2,x3,...]上,这个函数必须接收两个参数
#reduce把结果序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
    return x+y
f=add
print(reduce(f,[1,2,3,4]))
#等于1+2 3+3 6+4   最后等于10
from functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))


