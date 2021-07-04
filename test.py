from ais_wordnet_sim import aiml_enrich
from ais_wordnet_sim import similar_sentences, generate_category, get_category_data
from ais_wordnet_sim import add_synonyms_excel
from ais_wordnet_sim.database import CategoriesService
from ais_wordnet_sim.utility.statistic import Statistic

from ais_wordnet_sim.utility.aiml_writer import AIMLWriter

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


def test_statistic_count_category(_location):
    stat = Statistic()
    assert stat.count_category(_location) == 1158, "you fool asss"

def test_aiml_writer(_location):
    _writer = AIMLWriter(_location)
    sample_single = [('1','hôm nay thế nào ^ Hả^ chú ^','như loèn'),
                ('1','hôm nay ahihih  ^ Hả^ chú ^','như loèn'),]
    sample_multi = [('1','hôm nay thế nào ^ Hả^ chú ^','như loèn'),
                ('3','^ ahihih  ^ Hả^ chú ^','như loèn'),]                
    _writer.create_aiml_file_multi_topics('sample_single',sample_multi)
    _writer.create_aiml_file_single_topic('sample_multi',sample_single)
    

if __name__ == "__main__":
    #test_statistic_count_category('./')
    test_aiml_writer('./')
    pass
