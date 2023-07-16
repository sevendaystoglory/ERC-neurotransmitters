import openai
import json

openai.api_key = "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"
from my_functions import inject_oxytocin, inject_endorphin, rephrase
from measure_dopamine import measure_dopamine
from measure_endorphin import measure_endorphin
from available_functions import functions
from memory import *
from generate import generate_context
from neurotransmitters import Neurotransmitter
from model import model


def run_conversation():
    user_message = input("User: ")
    if not(user_message[0].lstrip().startswith('/')):
        #sysnthesis of v7 neurotransmitter vector
        message = {"role": "user", "content": user_message}
        chat_memory.append(message)
        memory.append(message)
        print("\nmemory: ", memory)
        print("\norganic memory: ", chat_memory)
        # Step 1: send the conversation and available functions to
        context= generate_context(chat_memory)
        dopamine_level=measure_dopamine(context["choices"][0]["message"]['content']+user_message)
        endorphin_level=measure_endorphin(context["choices"][0]["message"]['content']+user_message)
        print("\ndopamine_level: ", dopamine_level )
        print("\ndopamine_level: ", endorphin_level )
        print("\n===============CONTEXT========================>", context["choices"][0]["message"], '\n')
        memory.append({'role':'system', 'content': context["choices"][0]["message"]['content'] + "The next response follows from this information."})
       
        response = openai.ChatCompletion.create(
        model=model,
        messages=memory,
        temperature = 0.5,
        presence_penalty = 0.4, #penalizes new tokens
        max_tokens = 200,
        # function_call="auto", # auto is default, but we'll be explicit
        )

        response_content=response['choices'][0]['message']['content']
        chat_memory.append({
            "role": "assistant",
            "content": response_content,
        })
        rephrased_response=rephrase(chat_memory)
        memory.append({
            "role": "assistant",
            "content": rephrased_response,
        })
        #rephrase chat_memory
        print("\nAssistant Response: ", rephrased_response)
    else:
        try:

            nt7=Neurotransmitter()
            nt7.process_input(user_message)

            memory.append({'role': 'system', 'content': "Simulate every following response as belonging to a person with oxytocin level of " + str(nt7.array[1]) + " and endorphin level of " + str(nt7.array[3])+", where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding hormone, can influence text messaging in several ways. Increased oxytocin levels might lead to empathetic, compassionate, and understanding messages. It could encourage more frequent and deep communication, as well as affectionate language. Oxytocin's stress-reducing properties might result in calmer, comforting language. Endorphins, natural painkillers linked to pleasure and well-being, can affect chat conversations when levels are high. They can result in more positive and upbeat language use, demonstrating an improved mood. High endorphin levels may increase conversation energy and enthusiasm, reduce expressions of physical discomfort and stress, and potentially stimulate more creative or imaginative dialogue. Every response that follows should be consistent with this."})
            print("/DETECTED COMMAND")
            print(nt7.get_changed())
        except KeyError and ValueError and IndexError:
            print("/UNKNOWN COMMAND")
        # response = openai.ChatCompletion.create(
        #     model=model,
        #     messages=memory,
        #     functions=functions,
        #     function_call="auto", # auto is default, but we'll be explicit
        #     )
        # response_message = response["choices"][0]["message"]
        # response_content=response['choices'][0]['message']['content']
        # if response_content:
        #     memory.append({
        #         "role": "assistant",
        #         "content": response_content,

        #     })

        # # Step 2: check if GPT wanted to call a function ###########################
        # if response_message.get("function_call"):
        #     print("CALLED---function")
        #     # Step 3: call the function
        #     available_functions = {
        #         "inject_oxytocin" : inject_oxytocin,
        #         "inject_endorphin" : inject_endorphin
        #     }
        #     function_name = response_message["function_call"]["name"]
        #     print ("CALLED---", function_name)
        #     fuction_to_call = available_functions[function_name]
        #     function_args = json.loads(response_message["function_call"]["arguments"])
        #     if fuction_to_call==inject_oxytocin:
        #         function_response = fuction_to_call(
        #         level=function_args.get("value")
        #         )
        #     elif fuction_to_call==inject_endorphin:
        #         function_response = fuction_to_call(
        #         level=function_args.get("value")
        #         )

        #     # Step 4: send the info on the function call and function response to GPT
        #     memory.append(
        #         {
        #             "role": "function",
        #             "name": function_name,
        #             "content": function_response,
        #         }
        #     )  
            
        #     # extend conversation with function 
        #     print(memory)
            

while True:
    run_conversation()
