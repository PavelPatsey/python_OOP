"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None
В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""
import random
import re
import string


class EmailValidator:
    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        valid_characters = string.ascii_letters + string.digits + "._"
        length = random.randint(1, 100)
        random_str = "".join(random.choice(valid_characters) for _ in range(length))
        return random_str + "@gmail.com"

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email) is False:
            return False
        if "@" not in email:
            return False
        if email.count("@") > 1:
            return False
        user, domain = email.split("@")
        if len(user) > 100 or len(domain) > 50:
            return False
        if ".." in email:
            return False
        email_regex = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+$"
        if re.match(email_regex, email) is None:
            return False
        return True


# test
# res = EmailValidator.check_email("sc_lib@list.ru")  # True
# assert res is True
# res = EmailValidator.check_email("sc_lib@list_ru")  # False
# assert res is False
