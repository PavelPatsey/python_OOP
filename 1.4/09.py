import sys

# считывание списка строк из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    # здесь добавлять методы
    def select(self, a, b):
        """
        Возвращает список из элементов списка lst_data в диапазоне [a; b]
        (включительно) по их индексам (не id, а индексам списка); также учесть,
        что граница b может превышать длину списка.
        """

    def insert(self, data):
        """
        Добавляет в список lst_data новых данных из переданного списка строк data.
        """


db = DataBase()
db.insert(lst_in)
