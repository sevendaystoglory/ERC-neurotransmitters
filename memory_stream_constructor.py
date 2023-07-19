from generate import *

class MemoryObject:
    def __init__(self):
        self.synopsis = "empty"
        self.recency = "long ago"
        self.content_dict = {"non_chats" : "", "chats" : ""}
    def set_recency(self,x):
        self.recency = x 
    def add_chats(self,time_stamp,sender,content):
        content = str(time_stamp) + " : " + str(sender) + " : " + str(content)
        self.content_dict["chats"]+=str(content)
    def add_non_chats(self,time_stamp,content):
        content = str(time_stamp) + " : " + str(content)
    def generate_synopsis(self):
        query = {'role' : 'user', 'content': 'I am giving you a glimpse into the life of Juan in the form of a dictionary, and also a synopsis of this (which may be empty initially, i.e. outdated).'}
        query.append({'role' : 'user', 'content': str(self.content_dict)})
        query.append(self.synopsis)
        query.append({'role' : 'assiatant', 'content': 'Okay, got it. What do you want me to do with it?'})
        query.append({'user' : 'assiatant', 'content': 'Please update the synopsis.'})
        generate_summary(query)

class MemoryStream:
    def __init__(self):
        self.memory_array = []
    def append_memory(self, memory_object):
        self.memory_array.append(memory_object)
    def pop_memory(self):
        memory_object = self.memory_array.pop()
        return(memory_object)
    # def access_memory(self,i):

    