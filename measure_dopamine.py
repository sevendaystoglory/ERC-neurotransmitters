import json
import openai
from tools import set_temp, normalize
openai.api_key = "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"

def measure_dopamine(context, prompt):
    full_message = [{'role' : 'system' , 'content' : 'Dopamine: Plays a key role in motivation, reward, and motor control.'},{'role' : 'user' , 'content' :context},{'role' : 'system' , 'content' : "For this person, what should be the levels for these neurotransmitter dopamine"}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages= full_message
    )

    return(response)
