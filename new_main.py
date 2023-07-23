from tools import *
from generate import *

import time

def write_to_memory( memory, temp_memory1, temp_memory2, temp_memory3, msg=''): #no LLM
    if msg=='':
        return()
    if not(msg[0].lstrip().startswith('/')):
        user_message = msg
        message = {"role": "user", "content": user_message}
        memory.append(message)
        temp_memory1[-1]['content'] = temp_memory1 [-1]['content'] + ("\n" + "Human: " + user_message) #DONE
        temp_memory2[-1]['content'] = temp_memory2 [-1]['content'] + ("\n" + "Human: " + msg + " | ") #DONE
        temp_memory3[-1]['content'] = temp_memory3 [-1]['content'] + ("\n"+ str(time.strftime("%H%M"))+ ": " + "Human: " + msg + " | ") #DONE
        

def restore_memory(temp_memory1, temp_memory2, temp_memory3, memory,chat_memory):
    temp_memory1[-1]['content'] = ''
    temp_memory2[-1]['content'] = ''
    temp_memory3[-1]['content'] = ''
    while(len(memory)!=12):
        memory.pop()
    while(len(chat_memory)!=1):
        chat_memory.pop()
    with open('ERC-neurotransmitters/new_file_path.txt', 'w') as file:
            file.write('')
            
    

def get_user_ntv(temp_memory3, msg=''): #yes LLM
    chat_synopsis3 = generate_synopsis(temp_memory3) #DONE
    dopamine_level_user=measure_dopamine(chat_synopsis3+ "CHAT MESSAGE FROM PERSON:" +msg)
    endorphin_level_user=measure_endorphin(chat_synopsis3+ "CHAT MESSAGE FROM PERSON:" +msg)
    oxytocin_level_user=measure_oxytocin(chat_synopsis3+ "CHAT MESSAGE FROM PERSON:" +msg)
    adrenaline_level_user=measure_adrenaline(chat_synopsis3+ "CHAT MESSAGE FROM PERSON:" +msg)
    return([int(dopamine_level_user),int(endorphin_level_user),int(oxytocin_level_user),int(adrenaline_level_user),chat_synopsis3])

def get_num_mem_objects(history_stream): #no LLM
    num_mem_objects = len(history_stream.return_array())
    return(num_mem_objects)

def get_status(nt4, msg=''): #yes LLM
    if msg=='':
        return("EMPTY CHAT")
    
    if not(msg[0].lstrip().startswith('/')):
        return("CHATTING")
    else:
        try:
            if(msg == '/start'):
                new_file_path = chat_opener()
                with open('ERC-neurotransmitters/new_file_path.txt', 'w') as file:
                        file.write(new_file_path)
                status = "SYNTHESIS STARTED"

            elif(msg == '/end'):
                status = "SYNTHESIS ENDED"
                with open('ERC-neurotransmitters/new_file_path.txt', 'w') as file:
                        file.write('')
            elif(msg == '/reset future'):
                with open('ERC-neurotransmitters/companion/Juan/routine.txt', 'r') as file:
                    routine = file.read()
                    with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'w') as file:
                        file.write(routine)
                status = "FUTURE RESTORED"
            else:
                nt4.process_input(msg) 
                status = "NTV CHANGED"
        except: 
            status = "UNKNOWN COMMAND"
        return(status)
    

def update_plan(temp_memory3, nt4): #yes LLM
    plan = updated_future_plan(temp_memory3 ,nt4)
    return(plan)

def ERC1_response(memory, chat_memory, msg=''):
    if msg!='':
         if not(msg[0].lstrip().startswith('/')):   
             #ERC 1 response================================================================================
             chat_response_ERC1 = response_ERC1(memory, chat_memory)
             return (chat_response_ERC1)
         else:
            return (" ")
    else:
        return (" ")
    

def ERC2_response(temp_memory2, nt4, msg=''):
     if msg!='':
        if not(msg[0].lstrip().startswith('/')):
            chat_response_ERC2 = response_ERC2(nt4, temp_memory2)
            print(temp_memory2[-1]['content'])
            return(chat_response_ERC2)
        else:
            return(" ")
     else:
         return(" ")

def ERC3_response(temp_memory3, history_stream,new_file_path=None, msg='', chat_synopsis3=''):
    if msg!='':
        if not(msg[0].lstrip().startswith('/')):
            if new_file_path != None:
                with open(new_file_path, 'a') as file:
                        x = str(time.strftime("%H%M")) + ": " + "Human: " + msg + " | "
                        file.write(x)
            with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'r') as file:
                future_plan = file.read()
            ntv = NTV(history_stream, temp_memory3[-1]['content'])
            chat_response_ERC3 = response_ERC3(chat_synopsis3, temp_memory3, ntv, future_plan, retreive(temp_memory3 , history_stream))
            if new_file_path != None:
                with open(new_file_path, 'a') as file:
                    x = str(time.strftime("%H%M")) + ": " + "Juan: " + chat_response_ERC3 + " | "
                    file.write(x)
            return(chat_response_ERC3)
        else:
            return(" ")
    else:
         return(" ")
    

def RUN(x): #Run safely for LLMs
    try:
        return(x)
    except: 
        print("server overload")
        RUN(x)
