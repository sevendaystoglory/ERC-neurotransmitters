import openai
openai.api_key = "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"
from model import model

def generate_context(organic_memory):
    organic_memory.append({'role' : 'system', 'content': "From the history of conversation utterances of the user, generate a 100 words paragraph that summarizes what the user must be feeling now. You may generate additional details if required. Always refer to the user in third person in your response."})
    response = openai.ChatCompletion.create(
        model=model,
        messages= organic_memory,
        temperature = 0.5, 
        max_tokens= 100,
    )

    organic_memory.pop()
    print("CALLED---generate_context")
    return(response)
 
def generate_summary(memory):
    memory.append({'role' : 'user', 'content': 'summarize this piece of text in 100 tokens'})
    response = openai.ChatCompletion.create(
        model=model,
        messages= memory,
        temperature = 0.4,
        max_tokens= 100,
    )
    # memory.pop()
    print("CALLED---generate_summary")
    return(response)

