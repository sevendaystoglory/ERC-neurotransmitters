from tools import *
from companion.Juan.memory import *
from generate import *
from neurotransmitters import Neurotransmitter
from history import construct_history
import time
nt4_check = None

history_stream = construct_history()

def run_conversation(new_file_path, nt4, msg=''):
    [chat_response_ERC1, chat_response_ERC2, chat_response_ERC3, plan, dopamine_level_user, endorphin_level_user, oxytocin_level_user, adrenaline_level_user, ntv, num_mem_objects] = ['','','','','','','','',[0,0,0,0],0]
    status = "HEALTHY"
    if msg == '':
        user_message = input("User: ")
    else: 
        user_message=msg


    if not(user_message[0].lstrip().startswith('/')):
        status = "CHATTING"
        #sysnthesis of v4 neurotransmitter vector
        message = {"role": "user", "content": user_message}
        if new_file_path != None:
            with open(new_file_path, 'a') as file:
                        x = str(time.strftime("%H%M")) + ": " + "Human: " + user_message + " | "
                        file.write(x)
      
        
        temp_memory1[-1]['content'] = temp_memory1 [-1]['content'] + ("\n" + "Human: " + user_message) #DONE
        temp_memory2[-1]['content'] = temp_memory2 [-1]['content'] + ("\n" + "Human: " + user_message + " | ") #DONE
        temp_memory3[-1]['content'] = temp_memory3 [-1]['content'] + ("\n"+ str(time.strftime("%H%M"))+ ": " + "Human: " + user_message + " | ") #DONE
        memory.append(message)
        # print("\nmemory: ", memory)
        # print("\nchat memory: ", chat_memory)
        # chat_synopsis1 = generate_synopsis(temp_memory1) #DONE
        # chat_synopsis2 = generate_synopsis(temp_memory2) #DONE
        chat_synopsis3 = generate_synopsis(temp_memory3) #DONE
        dopamine_level_user=measure_dopamine(chat_synopsis3+user_message)
        endorphin_level_user=measure_endorphin(chat_synopsis3+user_message)
        oxytocin_level_user=measure_oxytocin(chat_synopsis3+user_message)
        adrenaline_level_user=measure_adrenaline(chat_synopsis3+user_message)
        # print("\ndopamine_level: ", dopamine_level )
        # print("\nendorphin_level: ", endorphin_level )
        # print("\noxytocin_level: ", oxytocin_level )
        # print("\nadrenaline_level: ", adrenaline_level )

        # print("\n===============CHAT_SYNOPSIS (ERC1_replies)========================>", chat_synopsis1, '\n')
        # print("\n===============CHAT_SYNOPSIS (ERC2_replies)========================>", chat_synopsis2, '\n')
        # print("\n===============CHAT_SYNOPSIS (ERC3_replies)========================>", chat_synopsis3, '\n')
        # memory.append({'role':'system', 'content': chat_synopsis["choices"][0]["message"]['content'] + "The next response follows from this information."})

        # with open('companion/Juan/future_plan.txt', 'r') as file:
        #     future_plan = file.read()
        #     print("FUTURE PLAN BEFORE:", future_plan , "\n")
        # plan = updated_future_plan(temp_memory2 ,nt4)
        # with open('companion/Juan/future_plan.txt', 'r') as file:
        #     future_plan = file.read()
        #     print("FUTURE PLAN UPDATED:", future_plan, "\n")


        #ERC 1 response================================================================================
        chat_response_ERC1 = response_ERC1(memory, chat_memory)
        #ERC 2 response============================================================================
        chat_response_ERC2 = response_ERC2(nt4, temp_memory2)
        print(temp_memory2[-1]['content'])
        #ERC 3 response================================================================================
        # with open('companion/Juan/future_plan.txt', 'r') as file:
        #     future_plan = file.read()
        #     print("FUTURE PLAN BEFORE:", future_plan , "\n")
        plan = updated_future_plan(temp_memory3 ,nt4)
        # with open('companion/Juan/future_plan.txt', 'r') as file:
        #     future_plan = file.read()
        #     print("FUTURE PLAN UPDATED:", future_plan, "\n")

        with open('companion/Juan/future_plan.txt', 'r') as file:
            future_plan = file.read()
            ntv = NTV(history_stream, temp_memory3[-1]['content'])
            chat_response_ERC3 = response_ERC3(chat_synopsis3, temp_memory3, ntv, future_plan, retreive(temp_memory3 , history_stream))
            if new_file_path != None:
                with open(new_file_path, 'a') as file:
                    x = str(time.strftime("%H%M")) + ": " + "Juan: " + chat_response_ERC2 + " | "
                    file.write(x)
        print(temp_memory3[-1]['content'])
        
    
    else:
        try:
            if(user_message == '/start'):
                new_file_path = chat_opener()
                status = "COMMAND EXECUTED"
            elif(user_message == '/end'):
                new_file_path = None 
                status = "COMMAND EXECUTED"
            elif(user_message == '/reset future'):
                with open('companion/Juan/routine.txt', 'r') as file:
                    routine = file.read()
                    with open('companion/Juan/future_plan.txt', 'w') as file:
                        file.write(routine)
                status = "COMMAND EXECUTED"
            else:
                nt4.process_input(user_message) 
                # nt4_check = ({'role': 'user', 'content': "I want you to REPHRASE your previous response as if Juan is an EXTREMELY moody person with oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1])+" and dopamine level of " + str(nt4.array[2])+ "and adrenaline level of "+str(nt4.array[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, can influence text messaging in several ways. Increased oxytocin levels might lead to empathetic, compassionate, and understanding messages. It could encourage deeper communication, as well as affectionate language. Oxytocin's stress-reducing properties might result in calmer, comforting language.\n Endorphins, natural painkillers linked to pleasure and well-being, can affect chat conversations when levels are high. They can result in more positive and upbeat language use, demonstrating an improved mood. High endorphin levels may increase conversation energy and enthusiasm, reduce expressions of physical discomfort and stress, and potentially stimulate more creative or imaginative dialogue.\n Dopamine, a neurotransmitter associated with reward, motivation, and mood, can influence text messaging. High dopamine levels may lead to creative, and risk-taking messages, reflecting increased motivation, joy, creativity, and openness. Low dopamine levels could result in less engaged, and more negative or neutral messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with stress, excitement, or danger, can significantly impact a user's chat conversations. High adrenaline levels heighten emotions, resulting in more passionate or intense exchanges. For example, a user might use more exclamation marks, capital letters, or emotionally-charged language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more focused responses. For instance, a user may stick strictly to a topic without deviating. It may enhance memory consolidation, enabling the user to recall key parts of the conversation more vividly. However, heightened arousal might increase the propensity for mistakes, like typing errors or rushed judgments. For example, a user might send messages with more typos or use less tactful language. Now the next response should be coming from a moody Juan. This response would obviously be heavily different!"})
                status = "COMMAND EXECUTED"
                print("/DETECTED COMMAND\n")
                print(nt4.get_changed())
        except: 
            print("/UNKNOWN COMMAND\n")
            status = "UNKNOWN COMMAND"

            # dir_path = 'companion/Juan'
            # files = os.listdir(dir_path)
            # txt_files = [f for f in files if f.endswith('.txt')]

    num_mem_objects = len(history_stream.return_array())
    return([new_file_path, chat_response_ERC1, chat_response_ERC2, chat_response_ERC3, plan, dopamine_level_user, endorphin_level_user, oxytocin_level_user, adrenaline_level_user, ntv, num_mem_objects, status])

nt4=Neurotransmitter(40,50,60,20)
def RUN(x):
    try:
        return(x)
    except: 
        print("server overload")
        RUN(x)

# new_file_path = None
# while True:
#     new_file_path = RUN(run_conversation(new_file_path, nt4, ''))

