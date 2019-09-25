import copy
import xml.etree.ElementTree as ETree

from ais_wordnet_sim.similar_sentences import similar_sentences


class AIMLEnrich:
    def __init__(self, aiml_file_in, aiml_file_out='enriched_data.aiml', decoding='utf8', encoding='utf-8', limit=1000):
        self._aiml_file_in = aiml_file_in
        self._aiml_file_out = aiml_file_out
        self._current_category = None
        self._current_pattern = None
        self._current_children = []
        self._current_children_syn = []
        self.decoding = decoding
        self.encoding = encoding
        self._limit = limit

    def _preprocess(self):
        self._tree = ETree.parse(self._aiml_file_in)
        self._root = self._tree.getroot()

    def _try(self, i=0):
        if i == len(self._current_children):
            if self.current_limit > 0:
                self._new_root.append(copy.deepcopy(self._current_category))
                self.current_limit -= 1
            return

        for set_tail in self._current_children_syn[i]:
            if self.current_limit > 0:
                self._current_children[i].tail = set_tail
                self._try(i + 1)

    def _enrich(self):
        self._new_root = ETree.Element('aiml')
        self._new_root.attrib = {'version': '2.0'}
        for category in self._root:
            self.current_limit = self._limit
            self._current_category = category
            self._current_pattern = self._current_category.find('pattern')
            self._current_children = list(self._current_pattern)
            self._current_children_syn = list(map(similar_sentences, [o.tail for o in self._current_children]))
            temp = self._current_pattern.text
            first_texts = similar_sentences(temp) if temp is not None else ['']
            for first_text in first_texts:
                self._current_pattern.text = first_text
                self._try()

    def compute(self):
        self._preprocess()
        self._enrich()
        ETree.ElementTree(self._new_root).write(self._aiml_file_out, encoding='utf-8', xml_declaration=True)
