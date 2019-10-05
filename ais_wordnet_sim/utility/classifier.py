
import csv
import os
'''
    - So sánh các cặp câu hỏi - câu trả lời cũ - mới với mục đích:
        + Lọc ra các cặp câu trùng nhau        
    - Phương thức so sánh:
        + text vs text
        + aiml vs aiml
'''

class Classifier:
    def __init__(self,old_qa_as_tuple,new_qa_as_tuple):
        pass

    def get_old_qa_from_xcel(self,xcel_location):
        '''
            input: excel 
            return: [(topic,q,a)]
        '''
        pass

    def get_old_qa_from_csv(self):
        '''
            input: csv 
            return: [(topic,q,a)]
        '''
        pass
    
    def get_old_qa_from_web(self):
        pass

    def get_new_qa_from_xcel(self):
        '''
            input: excel 
            return: [(topic,q,a)]
        '''
        pass

    def get_new_qa_from_csv(self,csv_location,question_field_name,answer_field_name,topic_field_name):
        '''
            input: csv 
            return: [(topic,q,a)]
        '''
        readCSV = csv.DictReader(csv_file)
        current_tuple = []
        
        pass

    def get_new_qa_from_web(self):
        pass

    def filter_as_text(self):
        '''
            return: (old_not_dup_qa, dup_qa, new_qa_not dup)
        '''
        pass
    
    def filter_as_aiml(self):
        '''
            return: (old_not_dup_qa, dup_qa, new_qa_not dup)
        '''
        pass
    
    def get_new_qa_as_list(self):
        pass
    
    def get_old_qa_as_list(self):
        pass