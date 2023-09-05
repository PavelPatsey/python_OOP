"""
Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:

p = PhoneBook()

А сам класс должен иметь следующий набор методов:

add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:

note = PhoneNumber(number, fio)

где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:

number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()

P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


class PhoneBook:
    def __init__(self):
        self.phone_list = []

    @staticmethod
    def __check_phone(phone):
        return isinstance(phone, PhoneNumber)

    def add_phone(self, phone):
        if self.__check_phone(phone):
            self.phone_list.append(phone)

    def remove_phone(self, indx):
        del self.phone_list[indx]

    def get_phone_list(self):
        return self.phone_list


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = 0
        self.set_number(number)
        self.fio = ""
        self.set_fio(fio)

    @staticmethod
    def __check_number(number):
        return isinstance(number, int) and len(str(number)) == 11

    def set_number(self, number):
        if self.__check_number(number):
            self.number = number

    @staticmethod
    def __check_fio(fio):
        return isinstance(fio, str)

    def set_fio(self, fio):
        if self.__check_fio(fio):
            self.fio = fio


# tests
# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# phones = p.get_phone_list()
