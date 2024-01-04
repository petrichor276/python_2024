dic = {'python': 95,  'java': 99,    'c': 100}
print(len(dic))
dic['java']=98
print(dic)
del dic['c']
dic['php']=90
print(dic.keys())
print(dic.values())
print(dic.get('javascript'))
print(sum(i for i in dic.values()))
print(max(dic.values()))
print(min(dic.values()))
dic1={'php':97}
dic.update(dic1)
print(dic)

a=input('请输入一串英文字符：')
print(a)
b={}
for i in a:
   b[i]=b.get(i,0)+1
#print(b[i]=b.get(i,0)+1 for i in a )老师，这一段可以使用推导式吗？如果可以怎么改为可以运行的代码？
print(b)










