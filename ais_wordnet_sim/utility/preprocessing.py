from ais_wordnet_sim.database import WordsService
from ais_wordnet_sim.database import SynonymsService
import xlrd

"""
Khởi tạo mongodb từ đồng nghĩa từ file excel
File excel có dạng như sau:
  + Gồm các sheet tương ứng với các loại từ (ví dụ: n, s, a, v)
  + Mỗi dòng của một sheet gồm một hoặc nhiều từ. Bắt đầu từ từ thứ 2
  trở đi là từ đồng nghĩa với từ đầu tiên, theo mức độ đồng nghĩa giảm dần
  + Ví dụ: file wordnet10-4-2019.xlsx
Database gồm 2 collection:
  + words
    - word
    - pos
  + synonyms
    - id_word_1
    - id_word_2
    (id_word_1 < id_word_2)
"""
def add_synonyms_excel(excel_file):
    data = xlrd.open_workbook(excel_file)
    words_service = WordsService()
    synonyms_service = SynonymsService()
    for sheet in data.sheets():
        pos = str.lower(sheet.name)
        for row_id in range(sheet.nrows):
            words = []
            for col_id in range(sheet.ncols):
                cell = sheet.cell(row_id, col_id)
                if cell.ctype == xlrd.XL_CELL_TEXT:
                    value = str.lower(cell.value)
                    word = words_service.insert_one(value, pos)
                    for pre_word in words:
                        synonyms_service.insert_one(pre_word['_id'], word['_id'])
                    words.append(word)