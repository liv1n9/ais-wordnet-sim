from ais_wordnet_sim import aiml_enrich
from ais_wordnet_sim import similar_sentences, generate_category, get_category_data
from ais_wordnet_sim import add_synonyms_excel
from ais_wordnet_sim.database import CategoriesService
from underthesea import pos_tag


def test_1():
    sentence = "Thế lực thù đich có những âm mưu gì"
    temp = similar_sentences(sentence, limit=5)
    print(temp)


def test_2():
    aiml_enrich('test.aiml')

def test_3():
    add_synonyms_excel('wordnet10-4-2019.xlsx')

def test_4():
    question = 'Thế lực thù đich có những âm mưu gì'
    answer = 'Âm mưu phá hoại nhà nước'
    topic = 'Phản động'
    generate_category(question, answer, topic)

def test_5():
    print(get_category_data())

if __name__ == "__main__":
    test_1()
