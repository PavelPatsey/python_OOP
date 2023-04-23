import sys

# sys.stdin = open("input_09", "r", encoding="utf-8")
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
        return self.lst_data[a : b + 1]

    def insert(self, data):
        """
        Добавляет в список lst_data новых данных из переданного списка строк data.
        """
        for record in data:
            self.lst_data.append(dict(zip(self.FIELDS, record.split())))


db = DataBase()
db.insert(lst_in)
