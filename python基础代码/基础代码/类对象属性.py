class Person:

    def __init__(self, name_1, age_1, gender_1, adress_1, phone_1, e_mail_1):
        self.name = name_1
        self.age = age_1
        self.gender = gender_1
        self.adress = adress_1
        self.phone = phone_1
        self.e_mail = e_mail_1

    def f1(self):
        print(
            f'我的名字是{self.name},年龄{self.age},性别{self.gender},地址是{self.adress},电话为{self.phone},邮箱是{self.e_mail}')

    def eat(self):
        print(f'{self.name}正在吃饭。')

    def sing(self):
        print(f'{self.name}正在唱歌。')


p1 = Person('小明', '20', '男', '北京', '123456', '123456@qq.com')
p1.f1()
p1.eat()
p1.sing()


class Car:
    def __init__(self, color_1, horsepower_1, model_1):
        self.color = color_1
        self.horsepower = horsepower_1
        self.model = model_1

    def move(self):
        print(f'{self.color}的{self.model}正在行驶。')


bmw_x7 = Car("黑色", 300, "BMW X7")
audi_a8 = Car("白色", 280, "Audi A8")

print(f"BMW X7的属性值：颜色：{bmw_x7.color}，马力：{bmw_x7.horsepower}，型号：{bmw_x7.model}")
bmw_x7.move()

print(f"Audi A8的属性值：颜色：{audi_a8.color}，马力：{audi_a8.horsepower}，型号：{audi_a8.model}")
audi_a8.move()
