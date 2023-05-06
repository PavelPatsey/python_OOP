"""
Большой подвиг 10. Объявите два класса:

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)

Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)

Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.

P.S. На экран в программе ничего выводить не нужно.
"""

import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False

    def __str__(self):
        if self.fl_open:
            if self.mine:
                return "*"
            return f"{self.around_mines}"
        return "#"


class GamePole:
    def __init__(self, field_size, mines_number):
        self.field_size = field_size
        self.mines_number = mines_number
        self.pole = [[Cell() for _ in range(field_size)] for _ in range(field_size)]
        self.init()

    def _get_mines_coordinates(self):
        pairs = set()
        while len(pairs) < self.mines_number:
            pairs.add(
                (
                    random.randint(0, self.field_size),
                    random.randint(0, self.field_size),
                )
            )
        return pairs

    def _get_around_mines_number(self, i, j):
        counter = 0
        for di, dj in (
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ):
            try:
                if i + di >= 0 and j + dj >= 0:
                    if self.pole[i + di][j + dj].mine:
                        counter += 1
            except:
                pass
        return counter

    def init(self):
        mines_coordinates = self._get_mines_coordinates()
        for i in range(self.field_size):
            for j in range(self.field_size):
                if (i, j) in mines_coordinates:
                    self.pole[i][j].mine = True

        for i in range(self.field_size):
            for j in range(self.field_size):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = self._get_around_mines_number(i, j)

    def show(self):
        for i in range(self.field_size):
            print(" ".join(map(str, self.pole[i])))


N = 10
M = 12
pole_game = GamePole(N, M)

# test
pole_game.show()
