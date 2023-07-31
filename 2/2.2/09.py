"""
Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo. Объекты этого класса будут формироваться командой:

line = LineTo(x, y)
где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:

x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:

p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:

get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:

L = sqrt((x1-x0)^2 + (y1-y0)^2)

где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


import math


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.lines = list(filter(lambda x: isinstance(x, LineTo), args))

    def get_path(self):
        return self.lines

    @staticmethod
    def _get_distance(line0: LineTo, line1: LineTo):
        return math.sqrt((line1.x - line0.x) ** 2 + (line1.y - line0.y) ** 2)

    def get_length(self):
        return self._get_distance(LineTo(0, 0), self.lines[0]) + sum(
            self._get_distance(self.lines[i - 1], self.lines[i]) for i in range(1, len(self.lines))
        )

    def add_line(self, line: LineTo):
        self.lines.append(line)


# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()

# lines = PathLines(LineTo(1, 2))
# print(lines.get_length())  # 2.23606797749979
# lines = PathLines(LineTo(1, 2), LineTo(3, 4))
# print(lines.get_length())  # 5.06449510224598
