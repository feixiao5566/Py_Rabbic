#!/usr/bin/env python
# encoding: utf-8


from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

#from io import StringIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
#和stringIO类似,可以用一个bytes初始化BytesIO,然后像读文件一样读取

#读文件和读二进制与读文件的区别是,from import的不同,打开的不同
#读文件使用open, 读StringIo用StringIO,而读BytesIO用的是BytesIO打开
#其他的读写操作是一样的,接口一致

