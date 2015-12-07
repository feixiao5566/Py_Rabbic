list1=[1,2,3,4,5,6,7,8,9,10]
list2=(range(1,11))
print(list1)
print(list2)

L=[]
for x in range(1,11):
    L.append(x*x)

print(L)

[x*x for x in range(1,11)]

print([x*x for x in range(1,11)if x%2==0])
#两层循环的全排列
print([m+n for m in 'ABC'for n in'XYZ'])

import os
print([d for d in os.listdir('.')])

d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])

#非常好的一章
