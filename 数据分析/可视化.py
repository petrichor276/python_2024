import matplotlib.pyplot as plt
import matplotlib
import numpy1 as np

a = np.arange(15)
plt.plot(
    a, a * 1.5, 'r',
    a, a * 3, '--',
    a, a * 4.5, 'o',
    a, a * 6, 'g-.',
    a, a * 7.5, '-.g',
    a, a * 9, '.g-',
)

plt.rcParams['font.family']='Microsoft Yahei'
plt.rcParams['font.size']=12
plt.title('标题',fontsize='40')
plt.text(5,20,'任意文本',fontsize='20',rotation=45)
plt.annotate(
    '这是箭头',
    xy=(12,40),
    xytext=(11,50),
    arrowprops=dict(facecolor='red',shrink=0.1,width=3)

)

plt.xlabel('x轴的文本信息',fontsize='20',color='red')
plt.ylabel('y轴的文本信息')
plt.show()


