import openai
import json

openai.api_key = "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"
from my_functions import inject_oxytocin, inject_endorphin
from measure.measure_dopamine import measure_dopamine
from tools import *
from measure.measure_endorphin import measure_endorphin
from measure.measure_oxytocin import measure_oxytocin
from measure.measure_adrenaline import measure_adrenaline
from available_functions import functions
from companion.Juan.memory import *
from generate import *
from neurotransmitters import Neurotransmitter
from model import model
# from time_keeper import get_current_time
# from emotions import Emotions

# current_time = get_current_time()

nt4_check = None
# em10 = Emotions()

def run_conversation(nt4_check, nt4):
    user_message = input("User: ")
    if not(user_message[0].lstrip().startswith('/')):
        #sysnthesis of v7 neurotransmitter vector
        message = {"role": "user", "content": user_message}
        chat_memory.append(message)
        
        # chat_organic_memory[0]['content'] = chat_organic_memory [0]['content'] + ("\n" + "User : " + user_message)
        temp_memory1[-1]['content'] = temp_memory1 [-1]['content'] + ("\n" + "Human: " + user_message)
        temp_memory2[-1]['content'] = temp_memory2 [-1]['content'] + ("\n" + "Human: " + user_message)
        # emotional_temp_memory[-1]['content'] = emotional_temp_memory [-1]['content'] + ("\n" + "Human: " + user_message)
        memory.append(message)
        print("\nmemory: ", memory)
        print("\nchat memory: ", chat_memory)
        # Step 1: send the conversation and available functions to
        user_context= generate_context(temp_memory1)
        dopamine_level=measure_dopamine(user_context["choices"][0]["message"]['content']+user_message)
        endorphin_level=measure_endorphin(user_context["choices"][0]["message"]['content']+user_message)
        oxytocin_level=measure_oxytocin(user_context["choices"][0]["message"]['content']+user_message)
        adrenaline_level=measure_adrenaline(user_context["choices"][0]["message"]['content']+user_message)
        print("\ndopamine_level: ", dopamine_level )
        print("\nendorphin_level: ", endorphin_level )
        print("\noxytocin_level: ", oxytocin_level )
        print("\nadrenaline_level: ", adrenaline_level )
        print("\n===============USER_CONTEXT========================>", user_context["choices"][0]["message"], '\n')
        # memory.append({'role':'system', 'content': user_context["choices"][0]["message"]['content'] + "The next response follows from this information."})
       
        #ERC 2 response============================================================================

        print("Temporal memory: ",temp_memory1)
        ERC2_response = response_ERC2(nt4, temp_memory2)['choices'][0]['message']['content']
        print("ERC2 response", ERC2_response)
        ERC2_response = string_to_dict(ERC2_response)
        temp_memory2[-1]['content'] = temp_memory2 [-1]['content'] + ("\n" + "Juan : " + ERC2_response['response_1'] + "\n" + ERC2_response['response_2'] + "\n" + ERC2_response['response_3'] + "\n" + ERC2_response['response_4']) 
        
        #Ai response================================================================================

        response = openai.ChatCompletion.create(
            model=model,
            messages=memory,
            temperature = 0.6,
            # functions= functions, #either response or function
            # function_call="auto", # auto is default, but we'll be explicit # can be used as formality check
        )
        

        response_content=response['choices'][0]['message']['content']
        print("\nERC1 response: ", response_content)


        # if response["choices"][0]["message"].get("function_call"):
        #     print("CALLED---DEFORMALIZE")
        #     print("\npreformalize-Assistant Response: ", response_content)
        #     # Step 3: call the function
        #     available_functions = {
        #         "no_formal" : deformalize,
        #     }
        #     function_name = response["choices"][0]["message"]["function_call"]["name"]
        #     fuction_to_call = available_functions[function_name]
        #     # function_args = json.loads(response["choices"][0]["message"]["function_call"]["arguments"])
        #     if fuction_to_call==deformalize:
        #         function_response = deformalize(user_message)

        #     # Step 4: send the info on the function call and function response to GPT
            
        #     response_content=function_response['content']
        
        memory.append({
            "role": "assistant",
            "content": response_content,
        })

        

        if nt4_check != None:
            print("MOOD CHANGED with step enhancement")
            memory.append(nt4_check)
            response = openai.ChatCompletion.create(
            model=model,
            messages=memory,
            temperature = 0.6,
            max_tokens = 100,
            # functions= functions, #either response or function
            # function_call="auto", # auto is default, but we'll be explicit # can be used as formality check
        )
        
            memory.pop()
            memory.pop()

            response_content=response['choices'][0]['message']['content']
            print("\nJuan's Changed Response: ", response_content)



        chat_memory.append({
            "role": "assistant",
            "content": response_content,
        })
        # chat_organic_memory[0]['content'] = chat_organic_memory [0]['content'] + ("\n" + "Juan : " + response_content)
        temp_memory1[-1]['content'] = temp_memory1 [-1]['content'] + ("\n" + "Juan : " + response_content)
        # emotional_temp_memory[-1]['content'] = emotional_temp_memory [-1]['content'] + ("\n" + "Juan : " + response_content)
        # em10.update_emotions(emotional_temp_memory)
        # print("Emotional Array = ", em10.array)

        memory.append({
            "role": "assistant",
            "content": response_content,
        })
    
    else:
        try:

            nt4.process_input(user_message) 
            nt4_check = ({'role': 'user', 'content': "I want you to REPHRASE your previous response as if Juan is an EXTREMELY moody person with oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1])+" and dopamine level of " + str(nt4.array[2])+ "and adrenaline level of "+str(nt4.array[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, can influence text messaging in several ways. Increased oxytocin levels might lead to empathetic, compassionate, and understanding messages. It could encourage deeper communication, as well as affectionate language. Oxytocin's stress-reducing properties might result in calmer, comforting language.\n Endorphins, natural painkillers linked to pleasure and well-being, can affect chat conversations when levels are high. They can result in more positive and upbeat language use, demonstrating an improved mood. High endorphin levels may increase conversation energy and enthusiasm, reduce expressions of physical discomfort and stress, and potentially stimulate more creative or imaginative dialogue.\n Dopamine, a neurotransmitter associated with reward, motivation, and mood, can influence text messaging. High dopamine levels may lead to creative, and risk-taking messages, reflecting increased motivation, joy, creativity, and openness. Low dopamine levels could result in less engaged, and more negative or neutral messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with stress, excitement, or danger, can significantly impact a user's chat conversations. High adrenaline levels heighten emotions, resulting in more passionate or intense exchanges. For example, a user might use more exclamation marks, capital letters, or emotionally-charged language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more focused responses. For instance, a user may stick strictly to a topic without deviating. It may enhance memory consolidation, enabling the user to recall key parts of the conversation more vividly. However, heightened arousal might increase the propensity for mistakes, like typing errors or rushed judgments. For example, a user might send messages with more typos or use less tactful language. Now the next response should be coming from a moody Juan. This response would obviously be heavily different!"})

            print("/DETECTED COMMAND")
            print(nt4.get_changed())
        except:
            print("/UNKNOWN COMMAND")

            
nt4=Neurotransmitter()
while True:
    run_conversation(nt4_check, nt4)
