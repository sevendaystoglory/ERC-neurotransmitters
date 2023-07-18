import json
import openai
openai.api_key = "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"
from my_functions import isolate_value


def measure_adrenaline(context):
    full_message = [{'role' : 'system' , 'content' : "Adrenaline, a hormone associated with stress, excitement, or danger, can significantly impact a user's chat conversations. High adrenaline levels often quicken cognitive processing, potentially leading to faster responses, like swift replies or interjections. It can heighten emotions, resulting in more passionate or intense exchanges. For example, a user might use more exclamation marks, capital letters, or emotionally-charged language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more focused responses. For instance, a user may stick strictly to a topic without deviating. It may enhance memory consolidation, enabling the user to recall key parts of the conversation more vividly. However, heightened arousal might increase the propensity for mistakes, like typing errors or rushed judgments. For example, a user might send messages with more typos or use less tactful language."} , {'role':'system', 'content' : context},{'role':'system', 'content' : 'Predict the level of adrenaline in the system of this person, where level 0 means minimum intensity and level 100 denotes maximum intensity. You must assign a level of adrenaline to this person.'}] 

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature= 0.3,
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
        return("adrenaline LEVELS IN USER ==", adrenaline[0]["content"])
    print("CALLED---measure_adrenaline_2")
    return ("adrenaline LEVELS IN USER ==",response_message["content"])
    # return ("adrenaline LEVELS IN USER ==", 'no response from system , REASON SUMMARY:', generate_summary([{'role':'system', 'content': response_message["content"]}])["choices"][0]["message"])