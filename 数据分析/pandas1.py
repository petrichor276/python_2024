import pandas as pd
import numpy as np

'''Series的使用'''
s1=pd.Series([2,4,6,8,10])
d1=pd.DataFrame([[2,4,6,8,10],[12,14,16,18,20]])

p2=pd.Series([1,'2',[3],(4,),True])
#修改对应索引值
# p3=pd.Series([2,4,6,8,10],index=['a','b','c','d','e'])
p3=pd.Series([2,4,6,8,10],index=list('abcde'))
p4=pd.Series(p3)
p5=pd.Series(np.array(range(20)))
# print(type(p2.values[1]))


'''DataFrame的使用'''
p6=pd.DataFrame([[2,4,6,8,10]])
p7=pd.DataFrame([[2,4,6,8,10],list('abcde')],index=list('XY'),columns=list('ABCDE'))
p8=pd.DataFrame(np.array(range(24)).reshape(4,6))
p9=p8.loc[0:'4',5:6]
print(p9)

















