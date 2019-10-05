from xml.etree import ElementTree

import os

'''
    Cung cấp các số  liệu thống kê
'''
class Statistic:
    def __init__(self):
        pass
    
    '''
        đếm số AIML Category tại 1 folder cụ thể
        @params: 
            - location:string, vị trí folder, 
        @return:
            - số lượng
    '''
    def count_category(self,_location):        
        num_cagetory = 0
        for each_file in os.listdir(_location):
            _root = ElementTree.parse(os.path.join(location,each_file)).getroot()
            num_cagetory += len(_root)
        return num_cagetory

    