#!/usr/bin/env python
# encoding: utf-8

import pickle
#序列化头文件
d = dict(name = 'Jared', age = 43, score = 100)
c = pickle.dumps(d)
#序列化字典d中的内容,打印出来
print(c)
#python的好处就是可以把任何东西赋值成一个变量

f = open('./testdir/test.txt', 'wb')
pickle.dump(d, f)
#把d的内容序列化后写入f文件中
f.close()

f = open('./testdir/test.txt', 'rb')
d = pickle.load(f)
#读文件中序列化记录的文件, 反序列化读出
f.close()
print(d)



