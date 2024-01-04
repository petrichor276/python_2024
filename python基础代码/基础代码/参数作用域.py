def sum_1(n):
    """

    :return: 累加和
    """

    for i in range(n):
        n += i
    return n


n = int(input('请输入一个数值N：'))
print(sum_1(n))


def search_card(user_list):
    print('欢迎您来到查询名片的功能：')
    name=input('请输入要查询的名字：')
    for card in user_list:
        if name in user_list:
            print('已找到寻找的名字')
            break
        else:
            print('没有找到')






































