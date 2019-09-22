# ais-wordnet-sim

___

## Install

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
result = similar_sentences(sentence)
result

>>> ['thế lực thù đich có những âm mưu gì', 'thế lực thù đich có những thủ đoạn gì', 'thế lực thù đich có những mưu kế gì', 'thế lực thù đich có những mưu mẹo gì', 'thế lực thù đich có những mưu mô gì', 'thế lực thù đich có những mưu đồ gì', 'thế lực thù đich có những mánh khóe gì', 'thế lực thù đich có những kế sách gì', 'thế lực thù đich sở hữu những âm mưu gì', 'thế lực thù đich sở hữu những thủ đoạn gì', 'thế lực thù đich sở hữu những mưu kế gì', 'thế lực thù đich sở hữu những mưu mẹo gì', 'thế lực thù đich sở hữu những mưu mô gì', 'thế lực thù đich sở hữu những mưu đồ gì', 'thế lực thù đich sở hữu những mánh khóe gì', 'thế lực thù đich sở hữu những kế sách gì']
```

### Create a category

Create a Category: `{ list_question, answer }` from a question and an answer

```python
from ais_wordnet_sim import generate_category
question = 'Thế lực thù đich có những âm mưu gì'
answer = 'Âm mưu phá hoại nhà nước'
generate_category(question, answer)
```

### Get all categories

Get all Categories generated in database

```python
from ais_wordnet_sim import get_category_data
result = get_category_data()
result

>>> [{'_id': ObjectId('5d86f35b944d00e06eb3a76b'), 'question_list': ['thế lực thù đich có những âm mưu gì', 'thế lực thù đich có những thủ đoạn gì', 'thế lực thù đich có những mưu kế gì', 'thế lực thù đich có những mưu mẹo gì', 'thế lực thù đich có những mưu mô gì', 'thế lực thù đich có những mưu đồ gì', 'thế lực thù đich có những mánh khóe gì', 'thế lực thù đich có những kế sách gì', 'thế lực thù đich sở hữu những âm mưu gì', 'thế lực thù đich sở hữu những thủ đoạn gì', 'thế lực thù đich sở hữu những mưu kế gì', 'thế lực thù đich sở hữu những mưu mẹo gì', 'thế lực thù đich sở hữu những mưu mô gì', 'thế lực thù đich sở hữu những mưu đồ gì', 'thế lực thù đich sở hữu những mánh khóe gì', 'thế lực thù đich sở hữu những kế sách gì'], 'answer': 'Âm mưu phá hoại nhà nước'}]
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
