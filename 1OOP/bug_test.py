#!/usr/bin/env python
# encoding: utf-8
'''
class Student(object):
        name = 'Student'
a=Student()
print(Student.name,a.name)
'''
##---作业复习类的继承多态__slot__偏函数和types.MethTypes()---
__author__ = 'Feixiao'

import functools
from types import MethodType

''' 一个练习作业,设计一个学生类,它有三个子类,分别是三个不同国家的学生类.
每个类成员方法speak可以说自己国家的话,通过这些类和成员方法和成员属性来复习类


'''


