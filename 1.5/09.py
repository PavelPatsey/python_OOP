import sys


# здесь объявляются все необходимые классы
class Node:
    def __init__(self, data, next_obj):
        self.data = data
        self.next_obj = next_obj


class ListObject:
    def __init__(self, data):
        node = None
        for item in reversed(data):
            next_node = node
            node = Node(item, next_node)
        self.head_obj = node

    def link(self, obj):
        pass

    def traverse(self):
        print(self.head_obj.data)
        node = self.head_obj.next_obj
        while node:
            print(node.data)
            node = node.next_obj


# считывание списка из входного потока (эту строку не менять)
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = [
    "1. Первые шаги в ООП",
    "1.1 Как правильно проходить этот курс",
    "1.2 Концепция ООП простыми словами",
    "1.3 Классы и объекты. Атрибуты классов и объектов",
    "1.4 Методы классов. Параметр self",
    "1.5 Инициализатор init и финализатор del",
    "1.6 Магический метод new. Пример паттерна Singleton",
    "1.7 Методы класса (classmethod) и статические методы (staticmethod)",
]

lst_in = []

# здесь создаются объекты классов и вызываются нужные методы
obj = ListObject(lst_in)
obj.traverse()
