from .sim_sentence_model import SimilarSentences
from ais_wordnet_sim.database import CategoriesService


def similar_sentences(sentence):
    model_similar = SimilarSentences(sentence)
    model_similar.compute()
    return model_similar.similar_list()

def generate_category(question, answer):
    question_list = similar_sentences(question)
    CategoriesService().insert_one(question_list, answer)