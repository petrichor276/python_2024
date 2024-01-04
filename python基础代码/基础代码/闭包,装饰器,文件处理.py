def delete_data(func):
    print('删除数据功能。')

    def inner():
        print('查找数据功能。')
        func()

    return inner


def add_data():
    print('增加数据功能。')


# 使用闭包给函数1增加功能
av1 = delete_data(add_data)
av1()
print()


# 使用装饰器给函数增加功能
@delete_data
def change_data():
    print('改变数据功能')


change_data()

# 异常处理捕获
str_1 = 't56an7ghu66l1u456'
a = ''
for i in str_1:
    try:
        int(i)
    except Exception as f:
        a += i
print(a)
