print(abs(-10))
x=abs(-10)
print(x)
f = abs
print(f(-8))
#以上说明,函数名也是变量
abs=10
#abs(-10)  #这样打印会出错
print(abs)  #把函数名指向变量,这个函数名已经指向整数10了
del abs  #上面把abs赋值10了,用del abs可以恢复abs函数功能
def add(x,y,f):
    return f(x)+f(y)
x=-5
y=6
f=abs
m=add(x,y,f)
print(m)
#这个在终端是可以运行的,但是在文件中运行有问题,不知道错误在哪里


