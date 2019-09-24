from pymongo import MongoClient
from urllib.parse import quote
from .model import Word, Synonym, Category
from .config import USERNAME, PASSWORD, CONNECTION_STRING, DATABASE_NAME

class Service:
    COLLECTION_NAME = ''

    def __init__(self, username=USERNAME, password=PASSWORD):
        connection_string = CONNECTION_STRING.format(quote(username, safe=''), quote(password, safe=''))
        self.collection = MongoClient(connection_string)[DATABASE_NAME][self.COLLECTION_NAME]


class WordsService(Service):
    COLLECTION_NAME = 'words'

    def __init__(self):
        super().__init__()

    def insert_one(self, word, pos):
        result = self.find_one(word, pos)
        if result is None:
            word_object = Word(word, pos)
            self.collection.insert_one(word_object.to_json())

    def find_one(self, word=None, pos=None, _id=None):
        if _id is None:
            return self.collection.find_one({'word': str.lower(word), 'pos': str.lower(pos)})
        return self.collection.find_one({'_id': _id})


class SynonymsService(Service):
    COLLECTION_NAME = 'synonyms'

    def __init__(self):
        super().__init__()

    def insert_one(self, id_word_1, id_word_2):
        result = self.find_one(id_word_1, id_word_2)
        if result is None:
            synonym_object = Synonym(id_word_1, id_word_2)
            self.collection.insert_one(synonym_object.to_json())

    def find_one(self, id_word_1=None, id_word_2=None, _id=None):
        if _id is None:
            if id_word_1 > id_word_2:
                id_word_1, id_word_2 = id_word_2, id_word_1
            return self.collection.find_one({'id_word_1': id_word_1, 'id_word_2': id_word_2})
        return self.collection.find_one({'_id': _id})

    def find(self, id_word_1=None, id_word_2=None):
        if id_word_1 is None or id_word_2 is None:
            if id_word_1 is not None:
                return self.collection.find({'id_word_1': id_word_1})
            elif id_word_2 is not None:
                return self.collection.find({'id_word_2': id_word_2})
        return None

class CategoriesService(Service):
    COLLECTION_NAME = 'categories'
    
    def __init__(self):
        super().__init__()
    
    def insert_one(self, question_list, answer, topic):
        category_object = Category(question_list, answer, topic)
        self.collection.insert_one(category_object.to_json())

    def find(self):
        return self.collection.find()
