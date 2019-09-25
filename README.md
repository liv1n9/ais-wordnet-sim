# ais-wordnet-sim

___

### Install

```
pip install ais-wordnet-sim
```
___

### Usage

#### Get list of similar sentences

Get a list which contains similar sentences (include original sentence)

```python
from ais_wordnet_sim import similar_sentences
sentence = 'Thế lực thù đich có những âm mưu gì'
# default limit = 1000
result = similar_sentences(sentence, limit=5)
result

>>> ['thế lực thù đich có những âm mưu gì', 'thế lực thù đich có những thủ đoạn gì', 'thế lực thù đich có những mưu kế gì', 'thế lực thù đich có những mưu mẹo gì', 'thế lực thù đich có những mưu mô gì']
```

### Create a category

Create a Category: `{ question_list, answer ,topic }` from a question and an answer

```python
from ais_wordnet_sim import generate_category
question = 'Thế lực thù đich có những âm mưu gì'
answer = 'Âm mưu phá hoại nhà nước'
# default limit = 1000
generate_category(question, answer, topic, limit=5)
```

### Get all categories

Get all Categories generated in database

```python
from ais_wordnet_sim import get_category_data
result = get_category_data()
result

>>> [{'_id': ObjectId('5d86f35b944d00e06eb3a76b'), 'question_list': ['thế lực thù đich có những âm mưu gì', 'thế lực thù đich có những thủ đoạn gì', 'thế lực thù đich có những mưu kế gì', 'thế lực thù đich có những mưu mẹo gì', 'thế lực thù đich có những mưu mô gì'], 'answer': 'Âm mưu phá hoại nhà nước'}]
```

### Create Synonyms database from excel file

Note: Drop old database before creating new database

Example Exel format:
- Sheet: n, a, v, r, e
- Each row of sheet: one or multiple words, synonyms words follow original word

```python
from ais_wordnet_sim import add_synonyms_excel
file = 'wordnet.xlsx'
add_synonyms_excel(file)
```

### Enrich AIML File

Create an enriched AIML file from original AIML file

```python
from ais_wordnet_sim import aiml_enrich
aiml_enrich('original.aiml', 'enriched.aiml')
```
