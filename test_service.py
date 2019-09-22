from ais_wordnet_sim.database.service import WordsService
from ais_wordnet_sim.database.service import SynonymsService

if __name__ == "__main__":
    # words_service = WordsService()
    # result_1 = words_service.insert_one('âm mưu', 'n')
    # result_2 = words_service.insert_one('thủ đoạn', 'n')
    # print(result_1)
    # print(result_2)

    # synonyms_service = SynonymsService()
    # result_3 = synonyms_service.insert_one(result_1['_id'], result_2['_id'])
    # print(result_3)

    words_service = WordsService()
    result_1 = words_service.find_one('kế sách', 'n')
    print(result_1)

    synonyms_service = SynonymsService()
    result_2 = synonyms_service.find(id_word_1=result_1['_id'])
    print('result_2', result_2)
    result_3 = synonyms_service.find(id_word_2=result_1['_id'])
    print('result_3', result_3)
