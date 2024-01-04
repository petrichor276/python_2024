'''name=input('您的姓名是：')
age=input('您的年龄是：')
gender=input('您的性别是：')
hobby=input('您的爱好是:')
occupation=input('您的职业是：')
print(f'用户的身份信息为：\n姓名:{name}\n年龄：{age}\n性别：{gender}\n爱好：{hobby}\n职业：{occupation}')'''

'''print(f'{type(123)}')
print(ord('郝'))
print(ord('唐'))
print(312%10)
a=17
a //=2
print( a )'''

for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
