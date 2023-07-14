import openai
openai.api_key = "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"

def normalize(num):
    try:
        num = int(num)
    except ValueError:
        num = 50
    if num<0:
        return 0
    if num>100:
        return 100
    else:
        return num
    
def set_temp(dopamine):
    return(dopamine/100)    

def generate_context(organic_memory):
    organic_memory.append({'role' : 'system', 'content': "I give you the ability to generate context for the user utterances. Generate a user persona and a consisten backstory of the person. Make sure it is consistent with the conversation and pay attention to user messages."})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages= organic_memory,
        temperature = 0.4, 
        max_tokens= 100,
    )
    # memory.pop()
    
    return(response)
 
def generate_summary(memory):
    memory.append({'role' : 'user', 'content': 'summarize this piece of text in 100 tokens'})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages= memory,
        temperature = 0.5,
        max_tokens= 100,
    )
    # memory.pop()
    
    return(response)

