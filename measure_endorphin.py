import json
import openai
openai.api_key = "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"
from my_functions import isolate_value
from model import model


def measure_endorphin(context):
    full_message = [{'role' : 'system' , 'content' : "Endorphins, natural painkillers linked to pleasure and well-being, can affect chat conversations when levels are high. They can result in more positive and upbeat language use, demonstrating an improved mood. High endorphin levels may increase conversation energy and enthusiasm, reduce expressions of physical discomfort and stress, and potentially stimulate more creative or imaginative dialogue."},{'role':'system', 'content' : context},{'role':'system', 'content' : 'Predict the level of endorphin in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of endorphin to this person.'}] 

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
        return("endorphin LEVELS IN USER ==", endorphin[0]["content"])
    print("CALLED---measure_endorphin_2")
    return ("endorphin LEVELS IN USER ==",response_message["content"])
    # return ("endorphin LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])