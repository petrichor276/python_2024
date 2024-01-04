a=int(input('请输入分数：'))
if a==100:
    print('满分')
elif 90<=a<=99:
    print('优秀')
elif 80<=a<=89:
    print('良好')
elif 70<=a<=79:
    print('中等')
elif 60<=a<=69:
    print('及格')
else:
    print('不及格')





a='admin'
b=123456
c=str(input('请输入用户名：'))
d=int(input('请输入密码：'))
if a!=c :
    print('用户名错误！')
    if  d==b:
        print('密码正确！')
elif b!=d:
    print('密码错误！')
    if a==c:
        print('用户名正确！')
else :
     print('登陆成功！')