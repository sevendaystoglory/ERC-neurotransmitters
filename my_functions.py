import json
from tools import normalize
import openai
from model import model

def get_current_weather(location, unit = "fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72", 
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

def isolate_value(value):
    return(value)

def adder(a,b):
    return(str(a+b+1))

def inject_oxytocin(level=50):
    info = {
        "value" : "Simulate the next response as belonging to a person with oxytocin level of " + str(normalize(level)) + ", where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding hormone, can influence text messaging in several ways. Increased oxytocin levels might lead to empathetic, compassionate, and understanding messages. It could encourage more frequent and deep communication, as well as affectionate language. Oxytocin's stress-reducing properties might result in calmer, comforting language. ",
    }
    return json.dumps(info)
def inject_endorphin(level=50):
    info = {
        "value" : "simulate the next response as belonging to a person with endorphin level of " + str(normalize(level)) + ", where the level 0 indicates no intensity and 100 indicates full intensity",
    }
    return json.dumps(info)

def rephrase(chat_memory):
     assistant_response=chat_memory.pop()
     content = 'I will give you a sample response. Depending on this chat history, rephrase your next response to be consistent with a casual conversation between two friends. Remove any sentences from the sample response that display formalism or overly care for the user. Remember he is your friend, so behave casual and dont display feelings of care for that '+ 'Sample Rsponse:' + assistant_response['content']
     chat_memory.append({'role':'system','content': content})
     response = openai.ChatCompletion.create(
        model=model,
        messages=chat_memory,
        temperature = 0.5,
        presence_penalty = 0.4, #penalizes new tokens
        max_tokens = 200,
        # function_call="auto", # auto is default, but we'll be explicit
        )
     chat_memory.append({'role' : 'assistant', 'content' : response["choices"][0]["message"]['content']})
     return(response["choices"][0]["message"]['content'])