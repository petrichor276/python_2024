import random


class Hero:
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood


class Intelligence_hero(Hero):
    def __init__(self, name, blood, intellect):
        super().__init__(name, blood)
        self.intellect = intellect

    def consum(self):
        damage = random.randint(1, 50)
        self.blood -= damage
        return damage


class Strength_hero(Hero):
    def __init__(self, name, blood, face):
        self.face = face
        super().__init__(name, blood)

    def consum(self):
        damage = random.randint(1, 50)
        self.blood -= damage
        return damage


def play():
    if p1.blood > 0:
        p1.consum()
        print(f'{p1.name}剩余血量{p1.blood}')
    if p2.blood > 0:
        p2.consum()
        print(f'{p2.name}剩余血量{p2.blood}')


p1 = Intelligence_hero('葫芦娃', 200, 15)
p2 = Strength_hero('蛇精', 200, 'handsome')
while True:

    if p1.blood <= 0 or p2.blood <= 0:
        print(f'游戏结束')
        break
    play()
    if p1.blood <= 0:
        print(f'{p2.name}获胜！剩余血量{p2.blood}')
        break
    if p2.blood <= 0:
        print(f'{p1.name}获胜！剩余血量{p1.blood}')
        break
