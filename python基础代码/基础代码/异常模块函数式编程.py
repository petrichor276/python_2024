class Myexception(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    a = int(input('请输入一个数字：'))
    if a > 90:
        raise Myexception('数据异常！')
except Myexception as e:
    print(e)
else:
    print('数据正常。')


# a = 55


def f1():
    if a % 2 == 1:
        print('奇数')
def f2():
    if a % 2 == 0:
        print('偶数')
def f3():
    if a > 4:
        print("此数字大于4")
def my_fun(func):
    func()
def f4():
    print('测试')
    def f5():
        print('测试一')
    return f5
my_fun(f2)
f5 = f4()
print(f5)
f5()
