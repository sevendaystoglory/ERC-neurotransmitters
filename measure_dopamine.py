import json
import openai
openai.api_key = "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"
from my_functions import isolate_value


def measure_dopamine(context):
    full_message = [{'role' : 'system' , 'content' : "Dopamine, a neurotransmitter associated with reward, motivation, and mood, can indirectly influence text messaging. High dopamine levels may lead to frequent, engaged, positive, creative, and risk-taking messages, reflecting increased motivation, joy, creativity, and openness. Low dopamine levels could result in less frequent, less engaged, and more negative or neutral messaging. However, these are broad generalizations and individual behavior is influenced by various other factors such as other neurotransmitters, personal circumstances, and personality traits. Additionally, extremely high dopamine levels can lead to impulsivity and addiction."},{'role':'system', 'content' : context},{'role':'system', 'content' : 'Predict the level of Dopamine in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of dopamine to this person.'}] 

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
        return("DOPAMINE LEVELS IN USER ==", dopamine[0]["content"])
    print("CALLED---measure_dopamine_2")
    return ("DOPAMINE LEVELS IN USER ==",response_message["content"])
    # return ("DOPAMINE LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])