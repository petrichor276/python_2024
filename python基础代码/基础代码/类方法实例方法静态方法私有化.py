class Employee:
    salary = []

    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.add_1(name, income)

    @classmethod  # 类方法
    def myrank(cls):
        cls.salary.sort(key=lambda x: x[1], reverse=True)  # False为从小到大排序

    @staticmethod  # 可以在调用静态方法时，将实例作为参数传递给静态方法
    def add_1(name, income):
        Employee.salary.append((name, income))


# 测试
s1 = Employee('小明', 3000)
s2 = Employee('小亮', 3500)
s3 = Employee('小阳', 2500)
# 放入工资系统
# 排序
Employee.myrank()
print(Employee.salary)
