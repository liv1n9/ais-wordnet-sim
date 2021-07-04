
import csv
import os

from ..database.service import QuestionAnswersService

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

    # OLD text questions
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

    # NEW text questions
    def get_new_qa_from_xcel(self):
        '''
            input: excel 
            return: [(topic,q,a)]
        '''
        pass

    def get_new_qa_from_csv(self,csv_location,question_field_name,answer_field_name,topic_field_name):
        '''
            input: csv (single file)
            return: [(topic,q,a)]
        '''
        new_qa_from_csv = []
        with open(csv_location,"r") as csv_file:
            readCSV = csv.DictReader(csv_file)
            current_tuple = ()
            for row in readCSV:
                current_tuple = [get_pattern_from_tagged_sentence(get_tagged_sentence(row['comment_text'].strip().replace('?','').lower()))
                                    ,row['topic'].strip().replace('?','').lower()]
                new_qa_as_list_of_tuple.append(current_tuple)
        return new_qa_from_csv

    def get_new_qa_from_web(self):
        pass

    def get_qa_from_mongo(self):
        '''
            get all text q/a from mongo
        '''
        qa_on_mongo = QuestionAnswersService()
        return qa_on_mongo.find()        

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