import underthesea
from ais_wordnet_sim.database import WordsService
from ais_wordnet_sim.database import SynonymsService
from bson.objectid import ObjectId


def uts_pos_convert(pos):
    if pos[0] == 'M':
        return 'N'
    return str(pos[0])


class SimilarSentences:

    def __init__(self, sentence, limit=1000):
        self.sentence = str.lower(sentence)
        self._word_syn_list = []
        self._current_index = []
        self._similar_list = []
        self._limit = limit

    def _preprocess(self):
        tokens = underthesea.pos_tag(self.sentence)
        self.n = len(tokens)
        words_service = WordsService()
        synonyms_service = SynonymsService()
        for word, pos in tokens:
            syn = [word]
            pos = uts_pos_convert(pos)
            word_object = words_service.find_one(word, pos)
            if word_object is not None:
                cursor = synonyms_service.find(id_word_1=word_object['_id'])
                for record in cursor:
                    s_word_object = words_service.find_one(_id=ObjectId(record['id_word_2']))
                    syn.append(s_word_object['word'])
                cursor = synonyms_service.find(id_word_2=word_object['_id'])
                for record in cursor:
                    s_word_object = words_service.find_one(_id=ObjectId(record['id_word_1']))
                    syn.append(s_word_object['word'])
            self._word_syn_list.append(syn)

    def _try(self, i=0):
        if i == self.n:
            if self._limit > 0:
                similar_sentence = ''
                for id_word, id_syn in enumerate(self._current_index):
                    if id_word > 0:
                        similar_sentence += ' '
                    similar_sentence += self._word_syn_list[id_word][id_syn]

                self._similar_list.append(similar_sentence)
                self._limit -= 1
            return

        for id_syn in range(len(self._word_syn_list[i])):
            if self._limit == 0:
                return
            self._current_index.append(id_syn)
            self._try(i + 1)
            self._current_index.pop()

    def compute(self):
        self._preprocess()
        self._try()

    def similar_list(self):
        return self._similar_list
