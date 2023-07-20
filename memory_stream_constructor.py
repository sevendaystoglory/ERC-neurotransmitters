from generate import *
from tools import *

class MemoryObject:
    def __init__(self):
        self.synopsis = "empty"
        self.recency = "long ago"
        self.content = ""
    def set_recency(self,x):
        self.recency = x 
    def add_content(self,content):
        self.content=(content)
    def generate_object_synopsis(self):
        query = [{'role' : 'user', 'content': 'I am giving you a dictionary replecting some of the moments of the life of Juan. These may be in form of chat conversations or some incidents/ routines (mentioned in non-chats, if available). Here it is : '}]
        query.append({'role' : 'user', 'content': self.content})
        query.append({'role' : 'assistant', 'content': 'Okay, got it. What do you want me to do with it?'})
        self.synopsis = generate_summary(query)
    def get_synopsis(self):
        return(self.synopsis)
    def get_recency(self):
        return(self.recency)
    def get_content(self):
        return(self.content)


class MemoryStream:
    def __init__(self):
        self.memory_array = []
    def append_memory(self, memory_object):
        self.memory_array.append(memory_object)
    def pop_memory(self):
        memory_object = self.memory_array.pop()
        return(memory_object)
    def return_array(self):
        return(self.memory_array)

    