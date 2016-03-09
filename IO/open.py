#!/usr/bin/env python
# encoding: utf-8
f = open('./testdir/test.txt', 'r')  #'r'表示读

f.read()    #一次读取文件的全部内容

f.close()   #关闭文件

#文件读写出错都可能产生IOError,一旦出错,f.close就不能调用
#为保证无论是否出错都能正确关闭文件,我们用try...finally实现

try:
    f = open('./testdir/Forever.mp3', 'rb')
    print(f.read())
finally:
    if f:
        f.close()

#每次这样写太繁琐,引入with语句自动帮我们调用方法:
with open('./testdir/test.txt', 'r') as f:
    print(f.read())

# read(size)防止一次性读取文件过多,内存负荷,可以反复调用
# 调用readline()可以每次读取一行内容
# 调用readlines()一次读取所有的内容并按行返回list

#如果文件很小,read()一次性读取最方便;如果不能确定文件大小,
#反复调用read(size)比较保险;
#如果是配置文件,调用readlines()最方便

for line in f.readlines():
    print(line.strip)   #把末尾的'\n'删掉

##file-like Object不要求从特定类继承,只要写个read()方法就行
# StringIO就是在内存中创建的file-like Object,常用作临时缓冲

#读取二进制文件,如图片视频音频等,用'rb'
#要读取非UTF-8编码的文本文件,需要给open()函数传入encoding参数
#       栗子:读取GBK编码的文件
f = open('./testdir/Forever.mp3', 'rb')
f.read()

f = open('./testdir/test.txt', 'r', encoding = 'gbk')
f.read()

#某些不规范文件,会遇到UnicodeDecodeError,因为在文本文件中可能
#夹杂了一些非编码的字符. 这是open()函数还接收一个errors参数,
#表示如果遇到编码错误后如何处理. 最简单处理是直接忽略
f = open('./testdir/Forever.mp3', 'r', encoding = 'gbk', errors = 'ignore')


#写文件 'w'文本文件, 'wb'二进制文件
f = open('./testdir/test.txt', 'w')
f.write('gogleem')
f.close()

#保险的with语句,防止忘记写close
with open('./testdir/test.txt', 'w') as f:
    f.write('Frente!')

#要写入特定编码的文本文件,请给open()函数传入encoding参数,
#        字符串自动转换成指定编码

#使用with语句操作文件IO是个好习惯
# w是覆盖, a是续写
