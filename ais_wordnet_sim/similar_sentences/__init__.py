from .sim_sentence_model import SimilarSentences
from ais_wordnet_sim.database import CategoriesService

CATEGORIES_SERVICE = CategoriesService()

def similar_sentences(sentence, limit=1000):
    model_similar = SimilarSentences(sentence, limit)
    model_similar.compute()
    return model_similar.similar_list()

def generate_category(question, answer, topic, limit=1000):
    question_list = similar_sentences(question, limit)
    CATEGORIES_SERVICE.insert_one(question_list, answer, topic)

def get_category_data():
    return list(CATEGORIES_SERVICE.find())