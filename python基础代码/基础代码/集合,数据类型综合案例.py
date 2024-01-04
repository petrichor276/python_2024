manger = {'曹操', '刘备', '孙权'}
technician = {'曹操', '刘备', '张飞', '关羽'}
print(manger & technician)
print(manger - technician)
print(technician - manger)
print('张飞' in manger)
print(manger ^ technician)
print(len(manger | technician))
