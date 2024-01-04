list1 = [4, 5, 2, 7]
list2 = [3, 6]
list3 = list1+list2
list3.sort()
print([i for i in list3])

st = 'dffsdadfsadfa'
a = []
[a.append(j) for j in st if j not in a ]
# for j in st:
#     if j not in a:
#         a.append(j)
print(a)
print([f'{i}出现的次数{st.count(i)}' for i in a])

import random
x=[]
[x.append(random.randint(1,34)) for i in range(0,6)]
y=[]
[y.append(random.randint(1,16)) for i in range(0,2)]
# for i in range(0,6):
#     x.append(random.randint(1,34))
print(x)
print(y)












