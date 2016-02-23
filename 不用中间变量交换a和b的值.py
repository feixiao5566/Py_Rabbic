#!/usr/bin/env python
# encoding: utf-8

a = 1
b = 2

a = a+b
b = a-b
a = a-b
print('a = {0}, b = {1}'.format(a,b))

a = a^b
b = a^b
a = a^b
print('a = {0}, b = {1}'.format(a,b))
