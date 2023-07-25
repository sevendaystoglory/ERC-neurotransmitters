from memory_stream_constructor import *
import os

def construct_history():
    memory_stream = MemoryStream()
    dir_name = 'companion/Juan/chats'
    files = os.listdir(dir_name)
    txt_files = [f for f in files if f.endswith('.txt')]
    recency = ["a month ago", "a week ago" , "yesterday" , "today" , "today" , "today" ,"today" , "today"]
    pointer = 0
    for file_name in txt_files:
        file_path = os.path.join(dir_name, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
            new_memory_object = MemoryObject()
            new_memory_object.add_content(content)
            new_memory_object.set_recency(recency[pointer])
            pointer+=1
            new_memory_object.generate_object_synopsis()
            memory_stream.append_memory(new_memory_object)
    return(memory_stream)