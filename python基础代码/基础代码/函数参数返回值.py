def multiplication_tables(i=5, j=5):
    '''
    :return:
    '''
    i = int(input('请输入：'))
    for i in range(1, i + 1):
        for j in range(1, i + 1):
            print(f'{i}x{j}={i * j}', end='\t')
        print()


multiplication_tables()


def a1(x, y, z, c, d):
    name = [x, y, z, c, d]
    print([name[i][0] for i in range(5)])


a1('hucbu', 'dfds', 'gfdg', 'fdg', 'tgdd')


def a2(*x):
    name = []
    for i in x:
        x = i[0]
        name.append(x)
    print(name)


a2('hucbu', 'dfds', 'gfdg', 'fdg', 'tgdd')
