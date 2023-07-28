"""
Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для записи и считывания информации о модели автомобиля из локальной приватной переменной __model.

Объект-свойство объявите с помощью декоратора @property. Также в объекте-свойстве model должны быть реализованы проверки:

- модель автомобиля - это строка;
- длина строки модели должна быть в диапазоне [2; 100].

Если проверка не проходит, то локальное свойство __model остается без изменений.

Объекты класса Car предполагается создавать командой:

car = Car()
и далее работа с объектом-свойством, например:

car.model = "Toyota"
P.S. В программе объявить только класс. На экран ничего выводить не нужно.
"""


class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and 2 <= len(model) <= 100:
            self.__model = model


# test
# car = Car()
# car.model = "Toyota"
# print(car.model)
# car.model = "T"
# print(car.model)
# car.model = 22
# print(car.model)
