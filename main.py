import openai
import os

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
from history import memory_stream

nt4_check = None

def run_conversation(nt4_check, nt4, msg=''):
    if msg == '':
        user_message = input("User: ")
    else: 
        user_message=msg

    if not(user_message[0].lstrip().startswith('/')):
        #sysnthesis of v4 neurotransmitter vector
        message = {"role": "user", "content": user_message}
      
        
        temp_memory1[-1]['content'] = temp_memory1 [-1]['content'] + ("\n" + "Human: " + user_message) #DONE
        temp_memory2[-1]['content'] = temp_memory2 [-1]['content'] + ( "Human: " + user_message)
    
        memory.append(message)
        # print("\nmemory: ", memory)
        # print("\nchat memory: ", chat_memory)
        chat_synopsis1 = generate_synopsis(temp_memory1) #DONE
        chat_synopsis2 = generate_synopsis(temp_memory2) #DONE
        # dopamine_level=measure_dopamine(user_context["choices"][0]["message"]['content']+user_message)
        # endorphin_level=measure_endorphin(user_context["choices"][0]["message"]['content']+user_message)
        # oxytocin_level=measure_oxytocin(user_context["choices"][0]["message"]['content']+user_message)
        # adrenaline_level=measure_adrenaline(user_context["choices"][0]["message"]['content']+user_message)
        # print("\ndopamine_level: ", dopamine_level )
        # print("\nendorphin_level: ", endorphin_level )
        # print("\noxytocin_level: ", oxytocin_level )
        # print("\nadrenaline_level: ", adrenaline_level )

        print("\n===============CHAT_SYNOPSIS (ERC1_replies)========================>", chat_synopsis1["choices"][0]["message"], '\n')
        print("\n===============CHAT_SYNOPSIS (ERC2_replies)========================>", chat_synopsis2["choices"][0]["message"], '\n')
        # memory.append({'role':'system', 'content': chat_synopsis["choices"][0]["message"]['content'] + "The next response follows from this information."})

        with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'r') as file:
            future_plan = file.read()
            print("FUTURE PLAN BEFORE:", future_plan)
        updated_future_plan(temp_memory2 ,nt4)
        with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'r') as file:
            future_plan = file.read()
            print("FUTURE PLAN UPDATED:", future_plan)

        #ERC 2 response============================================================================

        # print("Temporal memory: ",temp_memory1)
        ERC2_response = response_ERC2(nt4, temp_memory2)['choices'][0]['message']['content']
        print("ERC2 response", ERC2_response)
        ERC2_response = string_to_dict(ERC2_response)
        temp_memory2[-1]['content'] = temp_memory2 [-1]['content'] + ( "Juan : " + ERC2_response['reply_line_1'] + "\n" + ERC2_response['reply_line_2'] + "\n" + ERC2_response['reply_line_3'] + "\n" + ERC2_response['reply_line_4']) 
        
        #Ai response================================================================================

        response_ERC1(memory, chat_memory)

        

        # if nt4_check != None:
        #     print("MOOD CHANGED with step enhancement")
        #     memory.append(nt4_check)
        #     response = openai.ChatCompletion.create(
        #     model=model,
        #     messages=memory,
        #     temperature = 0.6,
        #     max_tokens = 100,
        #     # functions= functions, #either response or function
        #     # function_call="auto", # auto is default, but we'll be explicit # can be used as formality check
        # )
        
        #     memory.pop()
        #     memory.pop()

        #     response_content=response['choices'][0]['message']['content']
        #     print("\nJuan's Changed Response: ", response_content)



        
        
        # temp_memory1[-1]['content'] = temp_memory1 [-1]['content'] + ("\n" + "Juan : " + response_content)
        
    
    else:
        try:

            nt4.process_input(user_message) 
            # nt4_check = ({'role': 'user', 'content': "I want you to REPHRASE your previous response as if Juan is an EXTREMELY moody person with oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1])+" and dopamine level of " + str(nt4.array[2])+ "and adrenaline level of "+str(nt4.array[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, can influence text messaging in several ways. Increased oxytocin levels might lead to empathetic, compassionate, and understanding messages. It could encourage deeper communication, as well as affectionate language. Oxytocin's stress-reducing properties might result in calmer, comforting language.\n Endorphins, natural painkillers linked to pleasure and well-being, can affect chat conversations when levels are high. They can result in more positive and upbeat language use, demonstrating an improved mood. High endorphin levels may increase conversation energy and enthusiasm, reduce expressions of physical discomfort and stress, and potentially stimulate more creative or imaginative dialogue.\n Dopamine, a neurotransmitter associated with reward, motivation, and mood, can influence text messaging. High dopamine levels may lead to creative, and risk-taking messages, reflecting increased motivation, joy, creativity, and openness. Low dopamine levels could result in less engaged, and more negative or neutral messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with stress, excitement, or danger, can significantly impact a user's chat conversations. High adrenaline levels heighten emotions, resulting in more passionate or intense exchanges. For example, a user might use more exclamation marks, capital letters, or emotionally-charged language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more focused responses. For instance, a user may stick strictly to a topic without deviating. It may enhance memory consolidation, enabling the user to recall key parts of the conversation more vividly. However, heightened arousal might increase the propensity for mistakes, like typing errors or rushed judgments. For example, a user might send messages with more typos or use less tactful language. Now the next response should be coming from a moody Juan. This response would obviously be heavily different!"})

            print("/DETECTED COMMAND")
            print(nt4.get_changed())
        except:
            print("/UNKNOWN COMMAND")

            
nt4=Neurotransmitter(40,50,60,20)
def RUN(x):
    try:
        x
    except: 
        print("server overload")
        RUN(x)
while True:
    RUN(run_conversation(nt4_check, nt4, ''))

