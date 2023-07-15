import openai
import json

openai.api_key = "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"
from my_functions import inject_oxytocin,inject_endorphin
from measure_dopamine import measure_dopamine
from available_functions import functions
from memory import *
from generate import generate_context


def run_conversation():
    content = input("User: ")
    if not(content[0].lstrip().startswith('/')):
        #sysnthesis of v7 neurotransmitter vector
        message = {"role": "user", "content": content}
        organic_memory.append(message)
        memory.append(message)
        print("memory: ", memory)
        print("\norganic memory: ", organic_memory)
        # Step 1: send the conversation and available functions to
        context= generate_context(organic_memory)
        dopamine_level=measure_dopamine(context["choices"][0]["message"]['content']+content)
        print("\ndopamine_level: ", dopamine_level )
        print("\n===============CONTEXT>", context["choices"][0]["message"], '\n')
        memory.append({'role':'system', 'content': context["choices"][0]["message"]['content'] + "The next response follows from this information."})
       
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=memory,
        functions=functions,
        function_call="auto", # auto is default, but we'll be explicit
        )

        response_message = response["choices"][0]["message"]
        response_content=response['choices'][0]['message']['content']
        if response_content:
            memory.append({
            "role": "assistant",
            "content": response_content,

        }
        )  # extend conversation with assistant's reply
        print("Ai response: ", response_message)
        organic_memory.append({
            "role": "assistant",
            "content": response_content,
        })
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=memory,
        functions=functions,
        function_call="auto", # auto is default, but we'll be explicit
        )
    response_message = response["choices"][0]["message"]
    response_content=response['choices'][0]['message']['content']
    if response_content:
        memory.append({
            "role": "assistant",
            "content": response_content,

        })

    # Step 2: check if GPT wanted to call a function ###########################
    if response_message.get("function_call"):
        print("function is called")
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "inject_oxytocin" : inject_oxytocin,
            "inject_endorphin" : inject_endorphin
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        print ("L0000000000DA", response_message)
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        if fuction_to_call==inject_oxytocin:
            function_response = fuction_to_call(
            level=function_args.get("inject")
            )
        elif fuction_to_call==inject_endorphin:
            function_response = fuction_to_call(
            level=function_args.get("inject")
            )

        # Step 4: send the info on the function call and function response to GPT
        memory.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  
        
        # extend conversation with function 
        print(memory)
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=memory,
        )  # get a new response from GPT where it can see the function response
        print ("Function Response: ",second_response)

while True:
    run_conversation()
