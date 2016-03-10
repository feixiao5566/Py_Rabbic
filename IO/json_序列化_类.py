#!/usr/bin/env python
# encoding: utf-8

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name= name
        self.age = age
        self.score = score
#python类的序列化函数与CPP不同,序列化函数不在类中
#而C++中嵌入式序列化ar & a是在类中的
def student2dict(std):
    return{#这个序列化函数,把要打印的数据放到一个dict的字符串中
            'name':std.name,
            'age':std.age,
            'score':std.score
          }
s = Student('Jared', 43, 100)
print(json.dumps(s, default = student2dict))

#把任意class的实例变为dict:
print(json.dumps(s, default = lambda obj:obj.__dict__))
#这依然需要序列化函数,把类序列化到dict中

#通常class的实例都有一个__dict__属性,它就是一个dict,用来存储实例变量.
#也有少数例外,比如定义了__slots__的class.
#同,要把JSON反序列化为一个Student对象实例,loads()方法首先转换出一个dict对象,
#然后,传入 object_hook函数负责把dict转换为Student实例:

#类的反序列化
#def dict2student(d):
#    return Student(d['name'], d['age'], s['score'])
#json_str = '{"age":43, "score":100, "name":"Jared"}'
#print(json.loads(json_str, object_hook = dict2student))
#我自己写的这段不知道为啥就是会报错/V\
def dict2student(d):
        return Student(d['name'],d['age'],d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
#打印出反序列化的Student实例对象

#Python语言特定的序列化模块是pickle,但要使序列化更通用,更符合Web标准,用json

# json模块的dumps()和losds()函数是定义的非常好的接口典范
#使用时,只需传入一个必须的参数
#当默认机制不满足要求,传入更多参数,
#既做到了接口简单易用,又做到了充分的扩展性和灵活性
