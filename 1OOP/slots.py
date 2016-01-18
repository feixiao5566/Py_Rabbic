#!/usr/bin/env python
# encoding: utf-8
class Student(object):
    pass

s = Student()
s.name = 'Feixiao'  #动态给实例绑定一个属性
print(s.name)

def set_age(self, age): #定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  #给实例绑定一个方法
s.set_age(22)
print(s.age)

# 错误的
s2 = Student()  #创建新的实例
# 这个实例不能用 另一个实例的方法 s2 = set_age(23)    #尝试调用方法

##为给所有实例都绑定方法,可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = MethodType(set_score, Student)

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

del Student #删除类
del s    #删除实例
del s2  #删除实例

##想要限制属性,比如只允许对Student实例添加name和age属性
class Student(object):
    __slots__ = ('name', 'age', 'score')

s = Student()   #创建新的实例
s.name = 'Jared'    #绑定属性'name'
s.age = 42
s.score = 100
#s.height = 120
#it`s wrong 因为__slots__中没有height,所以不能绑定height属性
#试图绑定将得到AttributeError的错误
print(s.name, s.age, s.score)
#print(s.age)
#print(s.score)

##使用__slot__要注意,__slots__定义的属性仅对当前类实例起作用,
#对继承的子类是不起作用的. 除非在子类中也定义__slots__ :^)
#子类实例允许定义的属性就是自身的__slots__加上父类的__slots__




