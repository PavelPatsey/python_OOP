import random


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = False

    def __str__(self):
        if self.fl_open:
            if self.mine:
                return "*"
            return f"self.around_mines"
        return "#"


class GamePole:
    def __init__(self, field_size, mines_number):
        self.field_size = field_size
        self.mines_number = mines_number
        self.pole = [
            [Cell(0, False) for _ in range(field_size)] for _ in range(field_size)
        ]

    def _get_random_pairs(self):
        pairs = set()
        while len(pairs) < self.mines_number:
            pairs.add(
                random.randint(0, self.field_size),
                random.randint(0, self.field_size),
            )

    def init(self):
        """
        инициализация поля с новой расстановкой M мин
        (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
        """
        pass

    def show(self):
        """
        отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта,
        то отображается символ #).
        """
        for i in range(self.field_size):
            print(" ".join(map(str, self.pole[i])))


N = 10
M = 12
pole_game = GamePole(N, M)

# test
pole_game.show()
