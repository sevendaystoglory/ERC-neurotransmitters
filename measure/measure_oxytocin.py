import json
import openai
openai.api_key = "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"
from my_functions import isolate_value
from model import model


def measure_oxytocin(context):
    full_message = [{'role' : 'system' , 'content' : "Oxytocin, known as the social bonding 'LOVE' hormone, influences chat conversations in notable ways. It enhances empathy, fostering improved comprehension of others' feelings, possibly leading to empathetic phrases like 'I understand how you feel.' Oxytocin builds trust and honesty, encouraging more open exchanges, possibly resulting in sharing personal stories or sentiments. The hormone deepens social bonding, possibly leading to more connected and engaging chats, for instance using affectionate terms or emojis. Oxytocin's role in stress reduction could make conversations more relaxed and enjoyable, reflected in casual and light-hearted dialogue. In live chats, oxytocin may boost nonverbal communication, contributing to more effective interpretation of emojis or text-based sentiment cues. However, responses can vary among individuals and contexts. Read the following context :"},{'role':'system', 'content' : context},{'role':'system', 'content' : 'Predict the level of oxytocin in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of oxytocin to this person.'}] 

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
        return("oxytocin LEVELS IN USER ==", oxytocin[0]["content"])
    print("CALLED---measure_oxytocin_2")
    return ("oxytocin LEVELS IN USER ==",response_message["content"])
    # return ("oxytocin LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])