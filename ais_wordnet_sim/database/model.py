class Model:
    def to_json(self):
        return self.__dict__


class Word(Model):
    def __init__(self, word, pos):
        self.word = str.lower(word)
        self.pos = str.lower(pos)


class Synonym(Model):
    def __init__(self, id_word_1, id_word_2):
        if id_word_1 > id_word_2:
            id_word_1, id_word_2 = id_word_2, id_word_1
        self.id_word_1 = id_word_1
        self.id_word_2 = id_word_2

class Category(Model):
    def __init__(self, question_list, answer, topic):
        self.question_list = question_list
        self.answer = answer
        self.topic = topic

