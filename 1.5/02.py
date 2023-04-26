"""
Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:
my_money = Money(100)
your_money = Money(1000)
"""


class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)
