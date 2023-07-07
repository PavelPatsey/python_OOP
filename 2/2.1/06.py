"""
Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price объектов класса Book;

Объекты класса Book предполагается создавать командой:

book = Book(автор, название, цена)
При этом, в каждом объекте должны создаваться приватные локальные свойства:

__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.
"""


class Book:
    def __init__(self, author, title, price):
        if self.__check_author(author):
            self.__author = author
        if self.__check_title(title):
            self.__title = title
        if self.__check_price(price):
            self.__price = price

    @classmethod
    def __check_title(cls, title):
        return type(title) == str

    @classmethod
    def __check_author(cls, author):
        return type(author) == str

    @classmethod
    def __check_price(cls, price):
        return type(price) == int and price > 0

    def set_title(self, title):
        if self.__check_title(title):
            self.__title = title

    def set_author(self, author):
        if self.__check_author(author):
            self.__author = author

    def set_price(self, price):
        if self.__check_price(price):
            self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


# book = Book("author", "title", 1)
# book.set_title("title_1")
# book.set_author("author_1")
# book.set_price(2)
# book.get_title()
# book.get_author()
# book.get_price()
