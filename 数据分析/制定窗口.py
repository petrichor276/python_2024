import matplotlib.pyplot as plt

x=range(1,11)
y=[5,6,8,4,7,9,6,4,5,8]
y1=[5,6,7,1,3,5,6,4,1,7]
plt.figure(2,figsize=(5,5),dpi=80)
# plt.scatter(x,y)   散点图
width=0.4
# plt.bar(range(len(y)),y,width=0.4,label='小朋友')  条形图
# plt.bar([i+width for i in range(len(y1))],y1,width=width,color='red',label='糖葫芦')

plt.hist(y,range(1,13))
y_=range(min(y),max(y)+1)
print(y_)
plt.xticks(x[::1],['%d号'%i for i in x])
plt.yticks(y_,[i for i in y_])
# plt.legend()
plt.grid(0.3)
plt.show()
