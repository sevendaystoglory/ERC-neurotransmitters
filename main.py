import openai
import json

openai.api_key = "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"
from my_functions import get_current_weather,adder,inject_oxytocin,inject_endorphin
from measure_dopamine import measure_dopamine
from tools import generate_context

memory= [{'role':'system', 'content':'Simulate the response as belonging to a cool dude'}]
organic_memory=[{'role':'system', 'content':'Simulate the response as belonging to a cool dude'}]

def run_conversation():
    content = input("User: ")
    #sysnthesis of v7 neurotransmitter vector
    messages = [{"role": "user", "content": content}]
    organic_memory.append(messages[-1])
    memory.append(messages[-1])
    print("memory: ", memory)
    # Step 1: send the conversation and available functions to
    context= generate_context(organic_memory)
    dopamine_level=measure_dopamine(context["choices"][0]["message"]['content']+content)
    print("dopamine_level: ", dopamine_level )
    print("context--->", context)
    memory.append({'role':'system', 'content': context["choices"][0]["message"]['content'] + "The next response follows from this information."})
    functions = [
        {
            "name": "inject_oxytocin",
            "description": "triggered when encounters '/set oxytocin'",
            "parameters": {
                "type": "object",
                "properties": {
                    "level": {
                        "type": "number",
                        "description": "The level of oxytocin as prompted by the user",
                    },
                },
            },
        },
        {
            "name": "inject_endorphin",
            "description": "triggered when encounters '/set endorphin'",
            "parameters": {
                "type": "object",
                "properties": {
                    "level": {
                        "type": "number",
                        "description": "The level of endorphin as prompted by the user",
                    },
                },
            },
        }
        
    ]
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
    }
    )
    
    # Step 2: check if GPT wanted to call a function ###########################
    if response_message.get("function_call"):
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
        if fuction_to_call==get_current_weather:
            function_response = fuction_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
            )
        elif fuction_to_call==adder:
            function_response = fuction_to_call(
            a=function_args.get("a"),
            b=function_args.get("b"),
            )
        elif fuction_to_call==inject_oxytocin:
            function_response = fuction_to_call(
            level=function_args.get("level")
            )
        elif fuction_to_call==inject_endorphin:
            function_response = fuction_to_call(
            level=function_args.get("level")
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
