a = 'admin'
b = 123456
j = 3
for i in range(j):
    x = str(input('请输入用户名：'))
    y = int(input('请输入密码：'))
    if x == 'admin' and y == 123456:
        print('登陆成功！')
        break
    elif j == 1:
        print('输入错数过多，请明日再试。')
        break
    else:
        print('请重新输入。')
        j = j - 1
