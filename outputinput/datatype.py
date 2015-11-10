print(1.2e-5)
print("I\'m \"OK\"!")
#注意转义字符的使用
print('hello world')
#  '和"去引字符串是一样的
print(r'\\\t\\')
#用r''表示''内部的字符串默认不转义
print('line1\nline2\nline3\n')
print('''line1
line2
line3''')
#用'''...'''的格式表示多行内容
print(True and False)
#直接用True、False表示布尔值(请注意大小写)
#布尔值可以用and、or和not运算
print(True or False)
print(not False)

say = False
if say==True:
    print(not False)
else:
    print(not True)
    print('hello world')
#在:后面只要是缩进的地方都是上面判断的程序块
#空值是Python里一个特殊的值，用None表示

a = None
print(a)
print(10/3)
#这样除号除下来是浮点数
print(10//3)
#两个除号//叫 地板除 相除结果永远是整数部分
print(10%3)
#取余,相除结果是余数
