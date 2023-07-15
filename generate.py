import openai
openai.api_key = "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"

def generate_context(organic_memory):
    organic_memory.append({'role' : 'system', 'content': "From the history of conversation, generate a believeble user persona and user history that is consistent with the conversation."})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages= organic_memory,
        temperature = 0.5, 
        max_tokens= 100,
    )
    print("organic memory used for content", organic_memory)
    print(response)
    organic_memory.pop()
    return(response)
 
def generate_summary(memory):
    memory.append({'role' : 'user', 'content': 'summarize this piece of text in 100 tokens'})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages= memory,
        temperature = 0.4,
        max_tokens= 100,
    )
    # memory.pop()
    
    return(response)

