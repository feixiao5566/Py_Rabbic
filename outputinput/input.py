#birth = input('birth: ')
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')
#这样会报错是因为input()读取用户的输入返回的数据类型是str,str不能直接和整数比较,必须先把它转成整数
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
print(int("123"))
#强制类型转换把数字转换成int型
#print(int("apple"))
#这样就会报错,因为检测到 apple并不是数字



