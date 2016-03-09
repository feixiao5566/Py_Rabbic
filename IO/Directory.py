#!/usr/bin/env python
# encoding: utf-8

import os
import shutil
a = os.path.abspath('.')
#当前文件的绝对路径
b = os.path.abspath('./animal/animal.py')
print(a, '\n', b)
c = os.path.join('/yu/you', 'imhp.txt')
#将路径和文件名连接,完整的目录表示出来
print(c)
os.mkdir('/home/feixiao/demo/Py_Rabbic/a')
#创建一个目录
os.rmdir('/home/feixiao/demo/Py_Rabbic/a')
#注意,linux和mac下路径分隔符是/,win下是\
d = os.path.split('/home/feixiao/demo/Py_Rabbic/testdir/test2.txt')
#把路径拆分为目录和文件名
print(d)
print(d[0])
print(d[1])
#拆分路径名不要求文件一定存在
open('out.md', 'w')
os.rename('out.md', 'out.txt')
#重命名文件
os.remove('out.txt')
#移除文件
yeqingran = 1
#os模块中不存在复制文件

#求一个shutil模块copyfile()函数拷贝文件的栗子~~~><~~~



