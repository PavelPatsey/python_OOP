class Translator:
    vocabulary = dict()

    def add(self, eng, rus):
        """
        для добавления новой связки английского и русского слова (если английское
        слово уже существует, то новое русское слово добавляется как синоним для
        перевода, например, go - идти, ходить, ехать);
        если связка eng-rus уже существует, то второй раз ее добавлять не нужно,
        например:  add('go', 'идти'), add('go', 'идти');
        """
        if eng in self.vocabulary:
            self.vocabulary[eng].add(rus)
        else:
            self.vocabulary[eng] = {rus}

    def remove(self, eng):
        """
        Для удаления связки по указанному английскому слову;
        """
        if eng in self.vocabulary:
            self.vocabulary.pop(eng)

    def translate(self, eng):
        """
        Для перевода с английского на русский (метод должен возвращать список
        из русских слов, соответствующих переводу английского слова, даже если
        в списке всего одно слово).
        """
        if eng in self.vocabulary:
            return list(self.vocabulary[eng])
        return []


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(" ".join(tr.translate("go")))
