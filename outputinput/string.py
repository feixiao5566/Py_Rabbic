print('包含中文的str')
#不要随意缩进,会出错的
print(ord('A'))
print(ord('费'))
print(chr(66))
print(chr(39553))
#以上,是Unicode编码
print('\u4e2d\u6587')
#字符整数编码的十六进制写法
x = b'ABC'
#这里的ABC是byte类型,虽然打印出来跟字符串分不清,但实际上存储空间不同
print(x)
print('ABC'.encode('ascii'))
print('莱托'.encode('utf-8'))
#把费骁用utf-8格式打出来
#print('莱托'.encode('acsii'))
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
print(b'\xe8\x8e\xb1\xe6\x89\x98'.decode('utf-8'))
print(len('杰瑞得莱托'))
print(len(b'\xe8\x8e\xb1\xe6\x89\x98'))
print(len('中文'.encode('utf-8')))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print( 'Hello, %s' % 'world')
print('Hi,%s,you have $%d.' %('费骁',10000000))
#%运算符就是用来格式化字符串的, 如果只有一个%?，括号可以省略
print('%2d-%02d'%(3,1))
#占位符
print( 'Age: %s. Gender: %s' % (25, True))
#如果不确定用什么格式化输入,就用%s , 永远起作用 :^>
print('growth rate: %d %%' % 7)
# 两个%能打出来一个, 转义，用%%来表示一个%





