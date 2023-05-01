class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Goods):
    pass


class TV(Goods):
    pass


class Notebook(Goods):
    pass


class Cup(Goods):
    pass


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{good.name}: {good.price}" for good in self.goods]


cart = Cart()
goods = [
    TV("Rubin", 1000),
    TV("Polar", 500),
    Table("Delo", 100),
    Notebook("RIKOR", 2000),
    Notebook("Predator Designer", 1300),
    Cup("Cup", 10),
]
for good in goods:
    cart.add(good)

# test
print("\n".join(cart.get_list()))
