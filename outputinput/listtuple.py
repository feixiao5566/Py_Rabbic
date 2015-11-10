#list Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
bandmates=['Jared','shannon','tomo']
print(bandmates)
print(len(bandmates))
print(bandmates[0])
print(bandmates[-1])
print(bandmates[-2])
#以此类推取倒数第几个
bandmates.append('Matt')
#往list中追加元素到末尾
print(bandmates)
bandmates.pop()
#要删除list末尾的元素，用pop()
print(bandmates)
bandmates.insert(2,'Matt')
#插入到指定位置
print(bandmates)
bandmates.pop(2)
#删除指定位置
print(bandmates)
bandmates[0] = 'jared'
#替换指定位置的元素
print(bandmates)
L=['orange',111,True]
#list中的数据类型可以是不同
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme']
#list中可以嵌套list
print(s)
print(len(s))
print(s[2][1])  #取php

#元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
bandmates=('jared', 'shannon', 'tomo')
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = ()
print(t)
#要定义一个空的tuple，可以写成()
t=(1)
#这样定义的只是一个数字
print(t)
q=(1,)
#加,定义这样才是元组
print(q)
##总结:[]是list列表,可变.  ()是tuple元组,不可变

