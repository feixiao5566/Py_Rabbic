#!/usr/bin/env python
# encoding: utf-8

#可以直接作用于for循环的数据类型有以下几种:
#一类是集合数据类型,如 list、tuple、dict、set、str等
#一类是generator,包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象:Iterable
#可以使用isinstance()判断一个对象是否是Iterable对象:
from collections import Iterable
print(isinstance([], Iterable))

def triangles():
    c=[1]
    while 1:
        yield c
        a,b=[0]+c,c+[0]
        c=[a[i]+b[i]for i in range(len(a))]
print(triangles)
