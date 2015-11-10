#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
#使用键-值（key-value）存储，具有极快的查找速度。
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#print(d[95])
#这样是查不到的,因为95不是key而Michael是key
d['Adam'] = 67
print(d['Adam'])
#这样给dict放入数据,除了可以初始化指定外,还可以通过key放入
#若查询不在dict中的key,就会报错,避免错误,判断:
# 'Thomas' in d  或  d.get('Thomas')
print('Thomas' in d)
print('Bob' in d)
print(d.get('Thomas'))#不存在返回None
print(d.get('Thomas',-1))#不存在返回指定的数字

#删除key
print(d)
d.pop('Bob')
print(d)

#dict内部存放的顺序和key放入的顺序是没有关系的
#和list比较，dict有以下几个特点：

#    查找和插入的速度极快，不会随着key的增加而增加；
#    需要占用大量的内存，内存浪费多。
#而list相反：
#
#    查找和插入的时间随着元素的增加而增加；
#    占用空间小，浪费内存很少。
#
#所以，dict是用空间来换取时间的一种方法。

#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
#需要牢记的第一条就是dict的key必须是不可变对象。

#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
#那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

##要保证hash的正确性，作为key的对象就不能变。

#在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key




###set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set
#内部有1，2，3这3个元素，显示的顺序也不表示set是有序的
s = set([1, 1, 2, 2, 3, 3])
print(s)
#重复元素在set中被过滤
s.add(4)
print(s)
#用.add()添加元素到set中,可以重复添加,但是不会有效果
s.remove(4)
print(s)
#用.remove()删除元素

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)

#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，
#同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素


#再议不可变对象
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000#0
