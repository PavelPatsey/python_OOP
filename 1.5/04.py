"""
Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты
каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)

Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов
(произвольные числа).
В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый)
в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
(или Line, или Rect, или Ellipse).
Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""
import random


class Figure:
    def __init__(self, x1, y1, x2, y2):
        self.sp = (x1, y1)
        self.ep = (x2, y2)


class Line(Figure):
    pass


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


N = 217
elements = [random.choice((Line, Rect, Ellipse)) for i in range(N)]
elements = [
    element(0, 0, 0, 0)
    if element == Line
    else element(random.random(), random.random(), random.random(), random.random())
    for element in elements
]
