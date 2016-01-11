#!/usr/bin/env python
# encoding: utf-8

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" % (self.name,self.score))

bart = Student("Bart Simpson", 59)
lisa = Student("Lisa Simpson", 87)
bart.print_score()
lisa.print_score()


#类定义中的第一个变量self就是调用它本身的this 指针
