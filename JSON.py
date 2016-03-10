#!/usr/bin/env python
# encoding: utf-8

#在不同编程语言间传递对象
#把对象序列化为标准格式,如XML,ini,但更好的方法是序列化为JSON
#因为JSON表示出来是一个字符串,可被所有语言读取,也可以方便存储到磁盘或网络传输
#JSON比XML快,可以直接在Web页面中读取

#
import json
d = dict(name = 'Jared', age = 43, score = 100)
c = json.dumps(d)
#dumps()方法返回一个str, 内容就是标准的JSON.它可以把JSON写入一个file-like-Object
#要把JSON反序列化为Python对象,用loads()或者对应的load()方法
#前者把JSON字符反序列化,后者从file-like-object中读取字符串并反序列化
print(c)

json_str = '{"age":43, "score":100, "name":"Jared"}'
#哈,这里很有意思的引号,开始我用的全是单引号,报错了,分析是age的前引号被当字符串后引号配对了
#所以,就把引号中的引号换了
c = json.loads(json_str)
print(c)
#JSON编码是utf-8,所以Py的str可以与之自由交换






