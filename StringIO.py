#!/usr/bin/env python
# encoding: utf-8

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())#getvalue()函数用于获得写入后的str

from io import StringIO
f = StringIO('      Hello!\n     Goodbye!    ')
while True:
    s = f.readline()
    if s =='':
       break
    print(s.strip())    #strip()函数能够去掉字符串前后的空格


