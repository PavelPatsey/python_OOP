"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/xHINhSQJh5c

Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")

Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)

Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)

Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

P.S. На экран в программе выводить ничего не нужно.
"""


class FloatValue:
    @classmethod
    def __verify_value(cls, number):
        if not isinstance(number, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        self.__verify_value(value)
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


N = 5
M = 3
table = TableSheet(N, M)
table.cells = [[Cell(float(i + 1 + j * M)) for i in range(M)] for j in range(N)]
