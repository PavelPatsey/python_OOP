import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for field, value in zip(fields, lst_values):
                setattr(self, field, value)
            return True
        return False


class StreamReader:
    FIELDS = ("id", "title", "pages")

    def readlines(self):
        # считывание списка строк из входного потока
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
