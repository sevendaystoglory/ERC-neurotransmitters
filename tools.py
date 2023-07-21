import os
import openai
from model import model

def isolate_value(value):
    return(value)

def normalize(num):
    try:
        num = int(num)
    except:
        num = 50
    if num<0:
        return 0
    if num>100:
        return 100
    else:
        return num
    
import ast

def retrieve_response(input_string):
    try:
        after_pipe = input_string.split('|')[1].strip()
        return(after_pipe)
    except:
        print("after_pipe error")
        return({"reply_line_1" : 'DECOMMISSIONED', "reply_line_2" : 'DECOMMISSIONED', "reply_line_3" : 'DECOMMISSIONED', "reply_line_4" : 'DECOMMISSIONED'})

def string_to_dict(input_string):

    json_string = input_string.replace("'", "\"")
    try:
        result_dict = json.loads(json_string)
        return result_dict
    except:
        print("ERROR, ERC Response in wrong format")
        return ({"reply_line_1" : 'DECOMMISSIONED', "reply_line_2" : 'DECOMMISSIONED', "reply_line_3" : 'DECOMMISSIONED', "reply_line_4" : 'DECOMMISSIONED'})

def chat_opener():
    dir_name = 'ERC-neurotransmitters\companion\Juan\chats'
    files = os.listdir(dir_name)
    chat_files = [f for f in files if 'chat' in f]
    num_chat_files = len(chat_files)
    new_file_name = f'chat{num_chat_files + 1}.txt'
    new_file_path = os.path.join(dir_name, new_file_name)
    return(new_file_path)


def generate_synopsis(temp_memory):
    response = openai.ChatCompletion.create(
        model = model,
        messages = temp_memory,
        temperature = 0.4, 
        max_tokens = 300,
    )

    print("CALLED---generate_synopsis")
    return(response['choices'][0]['message']['content'])

def generate_summary(memory):
    memory.append({'role' : 'user', 'content': 'Summarize in not more than 300 words. CAPTURE ALL IMPORTANT DETAILS AND DECISIONS AND WHAT WAS THE OVERALL MOOD OF JUAN.'})
    response = openai.ChatCompletion.create(
        model = model,
        messages = memory,
        temperature = 0.4,
        max_tokens = 400,
    )
    memory.pop()
    return(response['choices'][0]['message']['content'])

import json
openai.api_key = "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"




def measure_adrenaline(context):
    full_message = [{'role' : 'user' , 'content' : "Adrenaline, a hormone associated with stress, excitement, or danger, can significantly impact a user's chat conversations. High adrenaline levels often quicken cognitive processing, potentially leading to faster responses, like swift replies or interjections. It can heighten emotions, resulting in more passionate or intense exchanges. For example, a user might use more exclamation marks, capital letters, or emotionally-charged language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more focused responses. For instance, a user may stick strictly to a topic without deviating. It may enhance memory consolidation, enabling the user to recall key parts of the conversation more vividly. However, heightened arousal might increase the propensity for mistakes, like typing errors or rushed judgments. For example, a user might send messages with more typos or use less tactful language."} , {'role':'user', 'content' : context},{'role':'user', 'content' : 'Predict the level of adrenaline in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a NUMBER depicting the level of adrenaline to this person.'}] 

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature= 0.2,
        presence_penalty= 0.6,
        messages= full_message,
        functions=[{
            "name": "isolate_value",
            "description": "assigns a numerical of adrenaline to the user the text is referring to. 0 being least intensive, 100 being most intensive",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The level of adrenaline as prompted by the user",
                    },
                },
            },
        }],
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "isolate_value" : isolate_value
        }  # only one function in this example, but you can have multiple

        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        if fuction_to_call==isolate_value:
            function_response = fuction_to_call(
            value=function_args.get("value")
            )
        
        adrenaline = [{
                "role": "function",
                "name": function_name,
                "content": function_response,
            }]

    
        print("CALLED---measure_adrenaline_1")
        if adrenaline[0]["content"] !=None:
            return(adrenaline[0]["content"])
        else:
            return(50)
    print("CALLED---measure_adrenaline_2")
    return (40)
    # return ("adrenaline LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])

def measure_dopamine(context):
    full_message = [{'role' : 'user' , 'content' : "Dopamine, a neurotransmitter associated with reward, motivation, and mood, can indirectly influence text messaging. High dopamine levels may lead to frequent, engaged, positive, creative, and risk-taking messages, reflecting increased motivation, joy, creativity, and openness. Low dopamine levels could result in less frequent, less engaged, and more negative or neutral messaging. However, these are broad generalizations and individual behavior is influenced by various other factors such as other neurotransmitters, personal circumstances, and personality traits. Additionally, extremely high dopamine levels can lead to impulsivity and addiction."},{'role':'user', 'content' : context},{'role':'user', 'content' : 'Predict the level of Dopamine in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of dopamine to this person.'}] 

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature= 0.3,
        presence_penalty= 0.6,
        messages= full_message,
        functions=[{
            "name": "isolate_value",
            "description": "assigns a numerical of dopamine to the user the text is referring to. 0 being least intensive, 100 being most intensive",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The level of dopamine as prompted by the user",
                    },
                },
            },
        }],
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "isolate_value" : isolate_value
        }  # only one function in this example, but you can have multiple

        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        if fuction_to_call==isolate_value:
            function_response = fuction_to_call(
            value=function_args.get("value")
            )
        
        dopamine = [{
                "role": "function",
                "name": function_name,
                "content": function_response,
            }]

    
        print("CALLED---measure_dopamine_1")
        if dopamine[0]["content"] !=None:
            return(dopamine[0]["content"])
        else:
            return(50)
    print("CALLED---measure_dopamine_2")
    return (40)
    # return ("DOPAMINE LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])


def measure_endorphin(context):
    full_message = [{'role' : 'user' , 'content' : "Endorphins, natural painkillers linked to pleasure and well-being, can affect chat conversations when levels are high. They can result in more positive and upbeat language use, demonstrating an improved mood. High endorphin levels may increase conversation energy and enthusiasm, reduce expressions of physical discomfort and stress, and potentially stimulate more creative or imaginative dialogue."},{'role':'user', 'content' : context},{'role':'user', 'content' : 'Predict the level of endorphin in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of endorphin to this person.'}] 

    response = openai.ChatCompletion.create(
        model=model,
        temperature= 0.3,
        presence_penalty= 0.6,
        messages= full_message,
        functions=[{
            "name": "isolate_value",
            "description": "assigns a numerical of endorphin to the user the text is referring to. 0 being least intensive, 100 being most intensive",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The level of endorphin as prompted by the user",
                    },
                },
            },
        }],
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "isolate_value" : isolate_value
        }  # only one function in this example, but you can have multiple

        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        if fuction_to_call==isolate_value:
            function_response = fuction_to_call(
            value=function_args.get("value")
            )
        
        endorphin = [{
                "role": "function",
                "name": function_name,
                "content": function_response,
            }]

    
        print("CALLED---measure_endorphin_1")
        if endorphin[0]["content"] !=None:
            return(endorphin[0]["content"])
        else:
            return(50)
    print("CALLED---measure_endorphin_2")
    return (40)
    # return ("endorphin LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])


def measure_oxytocin(context):
    full_message = [{'role' : 'user' , 'content' : "Oxytocin, known as the social bonding 'LOVE' hormone, influences chat conversations in notable ways. It enhances empathy, fostering improved comprehension of others' feelings, possibly leading to empathetic phrases like 'I understand how you feel.' Oxytocin builds trust and honesty, encouraging more open exchanges, possibly resulting in sharing personal stories or sentiments. The hormone deepens social bonding, possibly leading to more connected and engaging chats, for instance using affectionate terms or emojis. Oxytocin's role in stress reduction could make conversations more relaxed and enjoyable, reflected in casual and light-hearted dialogue. In live chats, oxytocin may boost nonverbal communication, contributing to more effective interpretation of emojis or text-based sentiment cues. However, responses can vary among individuals and contexts. Read the following context :"},{'role':'user', 'content' : context},{'role':'user', 'content' : 'Predict the level of oxytocin in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of oxytocin to this person.'}] 

    response = openai.ChatCompletion.create(
        model=model,
        temperature= 0.3,
        presence_penalty= 0.6,
        messages= full_message,
        functions=[{
            "name": "isolate_value",
            "description": "assigns a numerical of oxytocin to the user the text is referring to. 0 being least intensive, 100 being most intensive",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The level of oxytocin as prompted by the user",
                    },
                },
            },
        }],
        function_call="auto",
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "isolate_value" : isolate_value
        }  # only one function in this example, but you can have multiple

        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        if fuction_to_call==isolate_value:
            function_response = fuction_to_call(
            value=function_args.get("value")
            )
        
        oxytocin = [{
                "role": "function",
                "name": function_name,
                "content": function_response,
            }]

        print("CALLED---measure_oxytocin_1")
        if oxytocin[0]["content"] !=None:
            return(oxytocin[0]["content"])
        else:
            return(50)
    print("CALLED---measure_oxytocin_2")
    return (20)
    # return ("oxytocin LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])