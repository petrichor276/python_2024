import random
num=[]
while len(num)<6:
  a=random.randint(0,100)
  num.append(a)
num.append('张翠山')
print(num)
num.remove(num[2])
print(num)
num.insert(3,'高圆圆' )
print([i for i in num])

















#
# #a=['苏焱' ,'高圆圆']
# users = ['张三','李四']  # 存储已注册的用户
#
#
# # 注册账户函数
# def register(username):
#     # 判断是否输入非法信息
#     illegal_chars = ['苏焱', '高圆圆']
#     for illegal in illegal_chars:
#         if illegal in username:
#             print("根据相关法律法规，不能使用此类字符")
#             return
#
#     # 判断是否已经存在相同的用户名
#     if username in users:
#         print("用户名太受欢迎")
#     else:
#         # 存储新用户
#         users.append(username)
#         print("注册成功！")
#
#
# # 测试注册账户功能
# register("张三")
# register("李四")
# register("苏焱")
# register("王五")
# register("高圆圆")
# register("张三")  # 测试已有用户的情况













