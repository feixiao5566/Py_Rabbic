#!/usr/bin/env python
# encoding: utf-8

class Student(object):
        name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'feixiao'
print(s.name)
print(Student.name)
del s.name
print(s.name)

