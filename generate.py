import openai
import ast
openai.api_key = "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"
from model import model, model2
with open('ERC-neurotransmitters\companion\Juan\preamble.txt', 'r') as file:
        preamble = file.read()
with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'r') as file:
        future_plan = file.read()



def generate_synopsis(temp_memory):
    response = openai.ChatCompletion.create(
        model = model,
        messages = temp_memory,
        temperature = 0.4, 
        max_tokens = 300,
    )

    print("CALLED---generate_context")
    return(response)

def generate_summary(memory):
    memory.append({'role' : 'user', 'content': 'Summarize in 300 words'})
    response = openai.ChatCompletion.create(
        model = model,
        messages = memory,
        temperature = 0.4,
        max_tokens = 500,
    )
    # memory.pop()
    print("CALLED---generate_summary")
    return(response)


def response_ERC2(nt4, temp_memory):
    chats = temp_memory[-1]
    nt_check = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1])+" and dopamine level of " + str(nt4.array[2])+ "and adrenaline level of "+str(nt4.array[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "30" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "10" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample_angry = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "0" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "90" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample_high = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "60" + " and endorphin level of " + "80" + " and dopamine level of " + "50" + "and adrenaline level of " + "60" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."

    dict_format = {"formality": 'level of formality', "typos/grammar" : 'intensity of typos' , "attentiveness" : "Juan's attentivess/ interest in the conversation", "tone and language" : "Juan's tone" , "number of lines in Juan's responses" : 'an integer between 1 and 4 (inclusive) denoting the number of responses' , "average length of each response" : 'an integer marking the upper length of each response. SHOULD NOT BE GREATER THAN 30 WORDS!' , "reply_line_1" : "a sample Juan's first line of response based on all previous data." , "reply_line_2" : "next line of Juan's response" , "reply_line_3" : "next line of Juan's response" , "reply_line_4" : "next line of Juan's response"}
    
    query = [{'role' : 'user', 'content': 'I will give you three types of information. 1. A brief on the character of Juan. 2. His current mood depending on the levels of oxytocin, endorphin, dopamine and adrenaline in his system. EXTREME LEVELS of neurotransmitters should determine the the output HEAVILY. 3. His chat conversations with a human. You will then output a python dictionary in the following format : ' + str(dict_format) + "Make sure the values of the key 'replies' are going to be replies that Juan will type, consistent with the typos/grammar, and MAKE IT AWARE OF FACTS. The reply should not assume information like hallucinate that Juan knows a certain person or event. Strictly stick to information. AVOID BEING REPETITIVE WITH REPLIES" }]
    query.append({'role' : 'assistant', "content" : 'Sure!'})
    
    sample_case = " 1. " + preamble + " 2. " + nt_sample_angry + " 3. " + "\nHuman : Hey there how you doing today, Juan! \n Juan : Hi I am doing great\n BTW do I know you?\n Human : Oh I am Rashid from yesterday's anatomy class. Maxima is asking if you wanted to be project partner of ours? \n Juan : Ohhh. Just woke up man \nAlso, I am already booked, sorry. \n Human : Well then. You have anyone else I could partner up with? \n Juan: umm no \n srry but I dont have anyone \n Human: Is it so. You are not helping. \n Juan : Then help yourself bro. get lost. \n Human : You are downright bad. "
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = {"formality": 'slight informl', "typos/grammar" : 'typing in low priority, a few typos' , "attentiveness" : "little interest in the conversation", "tone and language" : "very direct and not respecting" , "number of lines in Juan's responses" : '2' , "length of each response" : '5' , "reply_line_1" : "First you come to me asking fro help" , "reply_line_2" : "Then you call me shit just because I can do nothing of your miserable situation!" , "reply_line_3" : " What a douche you are!" , "reply_line_4" : " "}
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'user', "content" : 'Fantastic work! You have captured well the properties of replies and content of replies of Juan due to neurotransmitter low levels. Now, lets try another.'})
    query.append({'role' : 'assistant', "content" : 'Sure!'})

    sample_case = " 1. " + preamble + " 2. " + nt_sample_high + " 3. " + "\nHuman : Hey there how you doing today, Juan! \n Juan : Hi I am doing great\n BTW do I know you?\n Human : Oh I am Rashid from yesterday's anatomy class. Maxima is asking if you wanted to be project partner of ours? \n Juan : Ohhh. Just woke up man \nAlso, I am already booked, sorry. \n Human : Well then. You have anyone else I could partner up with?"
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = {"formality": 'formal', "typos/grammar" : 'no typos' , "attentiveness" : "attentive", "tone and language" : "very direct, respectful" , "number of lines in Juan's responses" : '1' , "length of each response" : '20' , "reply_line_1" : "Sorry brother. But I have no one in my mind you can pair up with. Try to ask someone else." , "reply_line_2" : " " , "reply_line_3" : " " , "reply_line_4" : " "}
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'user', "content" : 'Fantastic work! You have captured the effects of heightened senses of Juan due to high levels of hormones. Lets try another.'})
    query.append({'role' : 'assistant', "content" : 'Sure!'})

    sample_case = " 1. " + preamble + " 2. " + nt_sample + " 3. " + "\nHuman : Hello, can you come to main building to give me your notes after class? \n Juan : Who are you? \n Human : Cormack. Tell fast.  \n Juan : I dont know any Cormack \n Human : Melissa told me about you."
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = {"formality": 'very informal', "typos/grammar" : 'no typos' , "attentiveness" : "some interest in the conversation", "tone and language" : "confused" , "number of lines in Juan's responses" : '2' , "length of each response" : '10' , "reply_line_1" : "who even is Melissa?" , "reply_line_2" : "you got the wrong contact bruh" , "reply_line_3" : " " , "reply_line_4" : " "}
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'user', "content" : "Incredible job! You captured very well how Juan doesn't know the human. Let's do one more. This is a tricky one!"})
    query.append({'role' : 'assistant', "content" : 'Sure!'})

    
    
    test_case = " 1. " + preamble + " 2. " + nt_check + " 3. " + chats['content']
    query.append({'role' : 'user', "content" : test_case})
    # print ("query:",query)

    response = openai.ChatCompletion.create(
        model=model2,
        messages= query,
        temperature = 0.4,
    )

    return(response)


def response_ERC1(memory, chat_memory,):
      response = openai.ChatCompletion.create(
            model=model,
            messages=memory,
            temperature = 0.6,
            # functions= functions, #either response or function
            # function_call="auto", # auto is default, but we'll be explicit # can be used as formality check
            )
        
      response_content=response['choices'][0]['message']['content']
      print("\nERC1 response: ", response_content)


        
        
      memory.append({
            "role": "assistant",
            "content": response_content,
      })

      chat_memory.append({
            "role": "assistant",
            "content": response_content,
      })
      memory.append({
            "role": "assistant",
            "content": response_content,
        })
      
      
def affector(dict, nt_array):
        dict_format = {'formality': 'level of formality', 'typos/grammar' : 'intensity of typos' , 'attentiveness' : "Juan's attentivess/ interest in the conversation", "tone and language" : "Juan's tone" , "number of lines in Juan's responses" : 'an integer between 1 and 4 (inclusive) denoting the number of responses' , "average length of each response" : 'an integer marking the upper length of each response. SHOULD NOT BE GREATER THAN 30 WORDS!' , 'reply_line_1' : "a sample Juan's first line of response based on all previous data." , "reply_line_2" : "next line of Juan's response" , "reply_line_3" : "next line of Juan's response" , "reply_line_4" : "next line of Juan's response"}
        query = [{'role' : 'user', 'content' : "I am giving you two types of informations. First one is a dictionary which is self explanatory. I want you to change the values of all of the following keys ('formality', 'typos/grammar', 'attentiveness', 'tone and language' ) and then apply those to all the response values (reply_line_1, reply_line_2, reply_line_3, reply_line_4) "}]
        response = openai.ChatCompletion.create(
        model=model,
        messages= query,
        temperature = 0.3,
        )

def updated_future_plan(temp_memory,nt4):
     chats = temp_memory[-1]['content']
     query = [{'role' : 'user', 'content' : "I am giving you FOUR types of informations. 1. A basic character description of Juan. 2. His future plans. Some are long term, some are decided at the start of the day. 3. A chat conversation with another person labelled Human, in the chats. Also there are timestamp for each of the messages, so you can judge the hour of the day at which the chat is progressing currently. 4. Levels of Neurotransmitters in Juan's system which will determine his mood and thus a change of plans would take place accordingly.\nYOUR TASK IS TO UPDATE THE FUTURE PLAN DEPENDING ON THE LEVEL OF ATTENTION JUAN GIVES TO HIS CHAT COUNTERPART. IF THERE IS NO CHANGE RETURN THE FUTURE PLAN LIST AS IT IS. IF THERE IS A SLIGHT CHANGE, EDIT THAT PART ONLY AND RETURN THE WHOLE PLAN. ALSO, PLEASE REFRAIN FROM MAKING CHANGES UNLESS VERY IMPORTANT FOR JUAN. \n OUTPUT FORMAT : {'reasoning' : 'proper reasoning of your change, if any', 'updated future plan' : 'your updated future plan'}. Are you ready?"}]
     query.append({'role' : 'assistant', 'content' : "Sure! Please give me the information"})
     #samples
     sample_preamble = "Juan is a cool kid from Mexico. He is very social and has a lot of friends. He can be a teaser sometimes but overall is popular. He is comitted to swimming classes daily and is also studying in 1oth grade in his school. he does'nt like studies."
     sample_future_plan = "Juan will call his PE teacher this morning to tell about his scholarship. Juan has a swimming class this evening. He will fully finish his readings."
     sample_chat = " 1300: Human: Hey Juan! Man, this is Erica \n 1340: Juan: Hey Erica! Sorry didn't save your number. \n 1341: Human: No issues.\n One thing I wanted to ask you is that are you aready for the party we are planning this night? Will you come over?"
     sample_nt4 = "Juan has an oxytocin level of " + "20" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "10" + " ,where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING mood. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat moods, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY mood, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
     sample_case = "1. " + sample_preamble + " 2. " + sample_future_plan + " 3. " + sample_chat + "4. "  + sample_nt4
     query.append({'role' : 'user', 'content' : sample_case})
     query.append({'role' : 'assistant', 'content': "{'reasoning' : 'Juan's has other important commitments and is not in a mood for parties right now', 'updated future plan' : 'Juan will call his insurance agent this morning. Juan have a swimming class this evening. He will fully finish his readings.'}"})
     query.append({'role' : 'user', 'content' : "Incredible! You did a great job!"})
     query.append({'role' : 'assistant', 'content' : "Thank You!"})
     query.append({'role' : 'user', 'content' : "Let's try another. Do this now."})

     #test
     test_preamble = preamble
     with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'r') as file:
        future_plan = file.read()
     test_future_plan = future_plan
     test_chat = chats
     test_nt4 = "Juan has an oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1]) + " and dopamine level of " + str(nt4.array[2]) + "and adrenaline level of " + str(nt4.array[3]) + " ,where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING mood. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat moods, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY mood, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
     test_case = "1. " + test_preamble + " 2. " + test_future_plan + " 3. " + test_chat + "4. "  + test_nt4
     query.append({'role' : 'user', 'content' : test_case})

     response = openai.ChatCompletion.create(
        model=model,
        messages= query,
        temperature = 0.3,
        )
     

     try:
        result_dict = ast.literal_eval(response['choices'][0]['message']['content'])
     except:
        result_dict = {'reasoning' : 'ast_ERROR', 'updated future plan' : future_plan}
     
     if 'updated future plan' in  result_dict:
          with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'w') as file:
            file.write(result_dict['updated future plan'])
     else:
          print("dick Error")


     return(result_dict)