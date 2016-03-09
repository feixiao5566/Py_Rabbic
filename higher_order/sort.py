#!/usr/bin/env python
# encoding: utf-8

print(sorted([36,5,-12,9,-21]))
#[-21, -12, 5, 9, 36]
print(sorted([36, 5, -12, 9, -21], key = abs))
#把数字求绝对值之后再从小到大排列
#[5, 9, -12, -21, 36]
print(sorted(['bob','about','Zoo','Credit']))
#['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob','about','Zoo','Credit'],key = str.lower))
#['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower, reverse = True))
#['Zoo', 'Credit', 'bob', 'about']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], reverse = True))
#['bob', 'about', 'Zoo', 'Credit']

#以下: 偏函数
print(int('12345',base=8))

import functools
int2 = functools.partial(int, base=2)
print(int2('10000'))

