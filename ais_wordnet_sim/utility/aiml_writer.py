import os
'''
    create AIML based on a list of tuples (topic,pattern,template)
'''


class AIMLWriter():
    def __init__(self,_location):
        self._location = _location        

    def create_aiml_file_multi_topics(self,file_name,content_as_list_of_tuples):
        with open(os.path.join(self._location,file_name+".aiml"),'w') as aiml_file:
            aiml_file.write('<?xml version="1.0" encoding="UTF-8"?>')
            aiml_file.write("\n")
            aiml_file.write('<aiml version="2.0">')
            aiml_file.write("\n")

            for each in content_as_list_of_tuples:
                aiml_file.write('<topic name="'+each[0]+'">') 
                aiml_file.write("\n")
                aiml_file.write("\t<category>") 
                aiml_file.write("\n")
                aiml_file.write("\t\t<pattern>")        
                aiml_file.write("\n\t\t\t") 
                aiml_file.write(each[1])        
                aiml_file.write("\n") 
                aiml_file.write("\t\t</pattern>")
                aiml_file.write("\n")
                aiml_file.write("\t\t<template>")                        
                aiml_file.write("\n\t\t\t") 
                aiml_file.write(each[2])       
                aiml_file.write("\n") 
                aiml_file.write("\t\t</template>")
                aiml_file.write("\n")
                aiml_file.write("\t</category>") 
                aiml_file.write("\n")
                aiml_file.write("</topic>")
                aiml_file.write("\n\n")

            aiml_file.write("</aiml>")            

    def create_aiml_file_single_topic(self,file_name,content_as_list_of_tuples):
        with open(os.path.join(self._location,file_name+".aiml"),'w') as aiml_file:
            aiml_file.write('<?xml version="1.0" encoding="UTF-8"?>')
            aiml_file.write("\n")
            aiml_file.write('<aiml version="2.0">')
            aiml_file.write("\n")
            aiml_file.write('<topic name="'+content_as_list_of_tuples[0][0]+'">') 
            aiml_file.write("\n")
            for each in content_as_list_of_tuples:
                
                aiml_file.write("\t<category>") 
                aiml_file.write("\n")
                aiml_file.write("\t\t<pattern>")        
                aiml_file.write("\n\t\t\t") 
                aiml_file.write(each[1])        
                aiml_file.write("\n") 
                aiml_file.write("\t\t</pattern>")
                aiml_file.write("\n")
                aiml_file.write("\t\t<template>")                        
                aiml_file.write("\n\t\t\t") 
                aiml_file.write(each[2])       
                aiml_file.write("\n") 
                aiml_file.write("\t\t</template>")
                aiml_file.write("\n")
                aiml_file.write("\t</category>")                
                aiml_file.write("\n\n")            
            aiml_file.write("</topic>")      
            aiml_file.write("\n")
            aiml_file.write("</aiml>")                        