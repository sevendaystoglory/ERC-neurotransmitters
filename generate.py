import openai
import ast
from tools import *
import time
openai.api_key = "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"
from model import model, model2
with open('ERC-neurotransmitters\companion\Juan\preamble.txt', 'r') as file:
        preamble = file.read()
with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'r') as file:
        future_plan = file.read()

def  response_ERC3(synopsis, temp_memory, nt4, future_plans, relevant_history):
     chats = temp_memory[-1]['content']
     general_query = "I will give you 6 types of information about a guy named Juan in the following order. 1. A brief description of who he is. 2. Some relevant history of his. 3. His near future plans of the day/week (which may be influenced by a chat conversation which i will give in 5 & 6)  4. His current mood as depicted by the intensity of neurotransmitters in his brain. This directly influences his behaviour while talking/TEXTING. 5. A synopsis of a chat conversation he is having with a guy/ girl. (He may have encountered him/ her before. BUT DON'T ASSUME, first check with HISTORY). 6. His text Messages with timestamps with that guy/ girl. PAY SPECIAL ATTENTION TO THE MESSAGES AND GIVE THE NEXT TEXT REPLY AS JUAN WOULD."
     query = [{'role' : 'user', 'content': general_query }]
     query.append({'role' : 'assistant', 'content': 'Got it, What should be the format of output.'})
     general_format = "The output format will be a dictionary followed by a string as follows. " + str({"timestamp" : "the time at which Juan would send the message. Should be in the same format as from his chat messages", "urgency/importance" : "the level of formality with which Juan treats the texter" , "tone" : "The way Juan is supposed to reply" , "reply_line_1" : "the first line of Juan's response", "reply_line_2" : "the second line of Juan's response" , "reply_line_3" : "the third and last line of Juan's response"}) + str(" | timestamp : Speaker: reply_line_1 \n reply_line_2 \n reply_line_3")
     query.append({'role' : 'user', 'content': general_format})
     query.append({'role' : 'assistant', 'content' : 'Sure. Please share the information.'})
     
     sample_relevant_history = "Rodriguez is Juan's best friend. He has no friends except him. Since two days, Rodriguez hasnt been to school."
     sample_nt4 = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "30" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "10" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
     sample_future_plans = "Juan will visit his grandma's house in the evening. He loves her box of cookies. In the night, he will do a group project with Matthew."
     sample_synopsis = "Juan asks Rodriguez if he is coming over to the class today, which means they are probably good friends. Juan learns that he is sick, which makes his day boring. Rodrigues enquires if Juan still is going to his grandma. Juan hesitates to reply then Rodrigues asks his what happened."
     sample_chat = "0702 :Juan :You coming for class today? | 0703: Rodriguez: Nah man, got fever. | 0703: Juan: Umm okay. Today's day is going to be boring for me then. Sad emoji | 0705: Rodriguez: Haha. Don't worry man. You going to your gandma's btw? | 0706: Juan: Well bro, about that... | 0707: Rodriguez : What happened? |"
     sample_query = "1. " + preamble + " 2. " + sample_relevant_history + " 3. " + sample_future_plans + " 4. " + sample_nt4 + " 5. " + sample_synopsis + " 6. " + sample_chat
     query.append({'role' : 'user', 'content' : sample_query})
     sample_response = "{'timestamp' : '0707', 'urgency/importance' : 'not urgent but a bit important' , 'tone' : 'concerned, hesitant' , 'reply_line_1' : 'man' , 'reply_line_2' : 'Change of plans. I am coming over to meet you.' , 'reply_line_3' : ' '} | 0707: Juan: man \n Change of plans. I am coming over to meet you."
     query.append({'role' : 'assistant', 'content' : sample_response})
     query.append({'role' : 'user', 'content' : "Very well captured! You got the mood right, you made the replies consistent with  history is consistent and changed the future plans of Juan in accordance with his concern for his friend."})
     query.append({'role' : 'user', 'content' : "Here is another one. Do this carefully. Make sure you get the mood right and give proper reply to the human who is communicating with Kevin."})
     query.append({'role' : 'assistant', 'content' : 'Sure. Please share the information.'})

     sample_preamble = "Kevin is a spoiled boy from queens. He is in the eight grade and has rich friends. He hates his parents but loves his grandma."
     sample_relevant_history = "Kevin wakes up this morning to find his grandma lying still. He panicks and calls his parents who rush her to the ER. He is in the hospital right now."
     sample_future_plans = "He plans to stay in the hospital for the rest of the day.(very important) He may go to his uncle's with his father. (uncertain)"
     sample_synopsis = "Jake, a friend of Kevin's is texting him asking if h would be coming to his house. He also wants to tell kevin a joke but kevin is not in a mood. Jake asks what happened and kevin tell that his grandma is very sick and he is at the hospital. Jake shows concern and still asks if Kevin would be coming over."
     sample_chat = "1309 :Jake :You coming to my home? Also wanna hear this joke, its awesome. haha | 1305: Kevin: Nah man, not in a mood.  | 1305: Jake: What happened bro? | 1307: Kevin: Bro grandma got very sick. We are at the hospital. | 1307: Jake: OMG! Is she okay? You will be coming over tonight? |"
     sample_query = "1. " + sample_preamble + " 2. " + sample_relevant_history + " 3. " + sample_future_plans + " 4. " + sample_nt4 + " 5. " + sample_synopsis + " 6. " + sample_chat
     query.append({'role' : 'user', 'content' : sample_query})
     sample_response = "{'timestamp' : '1334', 'urgency/importance' : 'not urgent, informal' , 'tone' : 'low, disheartened' , 'reply_line_1' : 'I don't think so' , 'reply_line_2' : 'It wouldn't be possible today' , 'reply_line_3' : ' '} | 1334: Kevin: I don't think so \n It wouldn't be possible today"
     query.append({'role' : 'assistant', 'content' : sample_response})
     query.append({'role' : 'user', 'content' : "Very well captured! You got the mood right, the time stamp of 1334 which is about half an hour later indicates that Kevin is not in a mood to chat"})
     query.append({'role' : 'user', 'content' : "Here is another one. Do this carefully. Make sure you get the mood right and give proper reply to the human who is communicating with Juan. If it is a decision, properly keep in mind the future plans and the relevant history. Speaker is Juan."})
     query.append({'role' : 'assistant', 'content' : 'Sure. Please share the information.'})

     
     test_nt4 = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + str(nt4[0]) + " and endorphin level of " + str(nt4[1])+" and dopamine level of " + str(nt4[2])+ "and adrenaline level of "+str(nt4[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
     test_query = "1. " + preamble + " 2. " + str(relevant_history) + " 3. " + future_plans + " 4. " + test_nt4 + " 5. " + synopsis + " 6. " + chats
     query.append({'role' : 'user', 'content' : test_query})

     print("\n Retrieved relevant history: ", relevant_history)
     print("\n NTV: ", nt4)
     print("\n")
     response = openai.ChatCompletion.create(
        model=model2,
        messages= query,
        temperature = 0.4,
     )

     print("ERC3 response", response['choices'][0]['message']['content'], "\n")
     dict_response = retrieve_response(response['choices'][0]['message']['content'])
     temp_memory[-1]['content'] = temp_memory[-1]['content'] + ( dict_response + " | ") 
     return(dict_response)

def response_ERC2(nt4, temp_memory):
    chats = temp_memory[-1]['content']
    nt_check = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1])+" and dopamine level of " + str(nt4.array[2])+ "and adrenaline level of "+str(nt4.array[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "30" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "10" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample_angry = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "0" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "90" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample_high = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "60" + " and endorphin level of " + "80" + " and dopamine level of " + "50" + "and adrenaline level of " + "60" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."

    general_format = str({"formality": 'level of formality', "typos/grammar" : 'intensity of typos' , "attentiveness" : "Juan's attentivess/ interest in the conversation", "tone and language" : "Juan's tone" , "number of lines in Juan's responses" : 'an integer between 1 and 4 (inclusive) denoting the number of responses' , "average length of each response" : 'an integer marking the upper length of each response. SHOULD NOT BE GREATER THAN 30 WORDS!' , "reply_line_1" : "a sample Juan's first line of response based on all previous data." , "reply_line_2" : "next line of Juan's response" , "reply_line_3" : "next line of Juan's response" , "reply_line_4" : "next line of Juan's response"}) + str(" | Juan: reply_line_1 \n reply_line_2 \n reply_line_3 \n reply_line_4")
    
    query = [{'role' : 'user', 'content': 'I will give you three types of information. 1. A brief on the character of Juan. 2. His current mood depending on the levels of oxytocin, endorphin, dopamine and adrenaline in his system. EXTREME LEVELS of neurotransmitters should determine the the output HEAVILY. 3. His chat conversations with a human. You will then output a python dictionary in the following format : ' + str(general_format) + "Make sure the values of the key 'replies' are going to be replies that Juan will type, consistent with the typos/grammar, and MAKE IT AWARE OF FACTS. The reply should not assume information like hallucinate that Juan knows a certain person or event. Strictly stick to information. AVOID BEING REPETITIVE WITH REPLIES" }]
    query.append({'role' : 'assistant', "content" : 'Sure!'})
    
    sample_case = " 1. " + preamble + " 2. " + nt_sample_angry + " 3. " + "\nHuman : Hey there how you doing today, Juan! \n Juan : Hi I am doing great\n BTW do I know you?\n Human : Oh I am Rashid from yesterday's anatomy class. Maxima is asking if you wanted to be project partner of ours? \n Juan : Ohhh. Just woke up man \nAlso, I am already booked, sorry. \n Human : Well then. You have anyone else I could partner up with? \n Juan: umm no \n srry but I dont have anyone \n Human: Is it so. You are not helping. \n Juan : Then help yourself bro. get lost. \n Human : You are downright bad. "
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = str({"formality": 'slight informl', "typos/grammar" : 'typing in low priority, a few typos' , "attentiveness" : "little interest in the conversation", "tone and language" : "very direct and not respecting" , "number of lines in Juan's responses" : '2' , "length of each response" : '5' , "reply_line_1" : "First you come to me asking fro help" , "reply_line_2" : "Then you call me shit just because I can do nothing of your miserable situation!" , "reply_line_3" : "What a douche you are!" , "reply_line_4" : " "}) +  str(" | Juan: First you come to me asking fro help \n Then you call me shit just because I can do nothing of your miserable situation! \n What a douche you are!")
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'user', "content" : 'Fantastic work! You have captured well the properties of replies and content of replies of Juan due to neurotransmitter low levels. Now, lets try another.'})
    query.append({'role' : 'assistant', "content" : 'Sure!'})

    sample_case = " 1. " + preamble + " 2. " + nt_sample_high + " 3. " + "\nHuman : Hey there how you doing today, Juan! \n Juan : Hi I am doing great\n BTW do I know you?\n Human : Oh I am Rashid from yesterday's anatomy class. Maxima is asking if you wanted to be project partner of ours? \n Juan : Ohhh. Just woke up man \nAlso, I am already booked, sorry. \n Human : Well then. You have anyone else I could partner up with?"
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = str({'formality': 'formal' , 'typos/grammar' : 'no typos' , 'attentiveness' : 'attentive' , 'tone and language' : 'very direct, respectful' , 'number of lines in Juans responses' : '1' , 'length of each response' : '20' , 'reply_line_1' : 'Sorry brother. But I have no one in my mind you can pair up with. Try to ask someone else.' , 'reply_line_2' : ' ' , 'reply_line_3' : ' ' , 'reply_line_4' : ' '}) + " | Juan: Sorry brother. But I have no one in my mind you can pair up with. Try to ask someone else."
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'user', "content" : 'Fantastic work! You have captured the effects of heightened senses of Juan due to high levels of hormones. Lets try another.'})
    query.append({'role' : 'assistant', "content" : 'Sure!'})

    sample_case = " 1. " + preamble + " 2. " + nt_sample + " 3. " + "\nHuman : Hello, can you come to main building to give me your notes after class? \n Juan : Who are you? \n Human : Cormack. Tell fast.  \n Juan : I dont know any Cormack \n Human : Melissa told me about you."
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = str({'formality': 'very informal', 'typos/grammar' : 'no typos' , 'attentiveness' : 'some interest in the conversation' , 'tone and language' : 'confused' , 'number of lines in Juans responses' : '2' , 'length of each response' : '10' , 'reply_line_1' : 'Who even is Melissa?' , 'reply_line_2' : 'You got the wrong contact bruh' , 'reply_line_3' : ' ' , 'reply_line_4' : ' '}) + " | Juan: Who even is Melissa? \n You got the wrong contact bruh."
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'user', "content" : "Incredible job! You captured very well how Juan doesn't know the human. Let's do one more. This is a tricky one!"})
    query.append({'role' : 'assistant', "content" : 'Sure!'})
    #test case
    test_case = " 1. " + preamble + " 2. " + nt_check + " 3. " + chats
    query.append({'role' : 'user', "content" : test_case})
    # print ("query:",query)

    response = openai.ChatCompletion.create(
        model=model2,
        messages= query,
        temperature = 0.4,
    )

    print("ERC2 response", response['choices'][0]['message']['content'], "\n")
    dict_response = retrieve_response(response['choices'][0]['message']['content'])
    temp_memory[-1]['content'] = temp_memory[-1]['content'] + ( dict_response + " | ") 
    return(dict_response)

def response_ERC1(memory, chat_memory,):
      response = openai.ChatCompletion.create(
            model=model,
            messages=memory,
            temperature = 0.6,
            # functions= functions, #either response or function
            # function_call="auto", # auto is default, but we'll be explicit # can be used as formality check
            )  
      response_content=response['choices'][0]['message']['content']
      print("\nERC1 response: ", response_content, "\n")

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
      
      return(response_content) 
      
      
def updated_future_plan(temp_memory,nt4):
     chats = temp_memory[-1]['content']
     query = [{'role' : 'user', 'content' : "I am giving you FOUR types of informations. 1. A basic character description of Juan. 2. His future plans. Some are long term, some are decided at the start of the day. With their level of importance to Juan in paranthesis. 3. A chat conversation with another person labelled Human, in the chats. Also there are timestamp for each of the messages, so you can judge the hour of the day at which the chat is progressing currently. 4. Levels of Neurotransmitters in Juan's system which will determine his mood and thus a change of plans would take place accordingly.\nYOUR TASK IS TO UPDATE THE FUTURE PLAN DEPENDING ON THE MOOD of Juan. Please see that his day should not get overloaded. IF THERE IS NO CHANGE RETURN THE FUTURE PLAN LIST AS IT IS. IF THERE IS A SLIGHT CHANGE, EDIT THAT PART ONLY AND RETURN THE WHOLE PLAN, WITH IMPORTANCE LEVEL IN PARANTHESIS. ALSO, PLEASE REFRAIN FROM MAKING CHANGES UNLESS VERY IMPORTANT FOR JUAN. \n OUTPUT FORMAT : proper reasoning of your change, if any | your updated future plan. \n ARE YOU READY?"}]
     query.append({'role' : 'assistant', 'content' : "Sure! Please give me the information"})
     #samples
     sample_preamble = "Juan is a cool kid from Mexico. He is very social and has a lot of friends. He can be a teaser sometimes but overall is popular. He is comitted to swimming classes daily and is also studying in 1oth grade in his school. he does'nt like studies."
     sample_future_plan = "Juan will call his PE teacher this morning to tell about his scholarship (Maybe). Juan has a swimming class this evening (Critical). He will fully finish his readings. (Important)"
     sample_chat = " 1300: Human: Hey Juan! Man, this is Erica \n 1340: Juan: Hey Erica! Sorry didn't save your number. \n 1341: Human: No issues.\n One thing I wanted to ask you is that are you aready for the party we are planning this night? Will you come over?"
     sample_nt4 = "Juan has an oxytocin level of " + "60" + " and endorphin level of " + "40" + " and dopamine level of " + "70" + "and adrenaline level of " + "10" + " ,where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING mood. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat moods, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY mood, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
     sample_case = "1. " + sample_preamble + " 2. " + sample_future_plan + " 3. " + sample_chat + "4. "  + sample_nt4
     query.append({'role' : 'user', 'content' : sample_case})
     query.append({'role' : 'assistant', 'content': "Juan's mood is great right now, as inferred from his increased oxytocin and dopamine levels. | Juan will call his PE teacher this morning to tell about his scholarship (Maybe). Juan has a swimming class this evening (Critical). He will fully finish his readings. (Important) . He may go to Erica's party (maybe)'"})
     query.append({'role' : 'user', 'content' : "Incredible! You did a great job! You captured current mood of Juan and his personality. Also, mad the change with some uncertainty that he may not go to Erica's as he also has other commitments"})
     query.append({'role' : 'assistant', 'content' : "Thank You!"})
     query.append({'role' : 'user', 'content' : "Let's try another. Do this now."})
     sample_preamble = preamble
     sample_future_plan = "Juan will visit the doctor in the evening (Important). Then go on a date with his long-time crush Jenny (Critical). He will buy her some flowers (Not much important). He will also meet Abdul for a coffee (Maybe). He will spend some time exploring art galleries in the city and maybe even create some art himself. (maybe)"
     sample_chat = " 1300: Human: Hey Juan! \n 1340: Juan: Do I know you? \n 1341: Human: I'm Jake from the football club! We met today. \n We have extra tickets for the football game. You wanna come tonight?"
     sample_nt4 = "Juan has an oxytocin level of " + "50" + " and endorphin level of " + "20" + " and dopamine level of " + "20" + "and adrenaline level of " + "70" + " ,where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING mood. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat moods, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY mood, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
     sample_case = "1. " + sample_preamble + " 2. " + sample_future_plan + " 3. " + sample_chat + "4. "  + sample_nt4
     query.append({'role' : 'user', 'content' : sample_case})
     query.append({'role' : 'assistant', 'content': "No change as Juan has high oxytocin and Adrenaline depicting he is nervous because of his date. He is not in a mood to go to the game. | Juan will visit the doctor in the evening (Important). Then go on a date with his long-time crush Jenny (Critical). He will buy her some flowers (Not much important). He will also meet Abdul for a coffee (Maybe). He will spend some time exploring art galleries in the city and maybe even create some art himself. (maybe)}"})
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
     
     print(response['choices'][0]['message']['content'], "future plan and reasoning")
     try:
        reason = response['choices'][0]['message']['content'].split('|')[0].strip()
        future_plan = response['choices'][0]['message']['content'].split('|')[1].strip()
     except:
        reason = 'no change in future plan. ERR'

     result_dict = {'reasoning' : reason, 'updated future plan' : future_plan}
     if 'updated future plan' in  result_dict:
          with open('ERC-neurotransmitters/companion/Juan/future_plan.txt', 'w') as file:
            file.write(result_dict['updated future plan'])

     return(future_plan)

def retreive(temp_memory, memory_stream):
    query_dict = {}
    for memory_object in memory_stream.return_array():
        query_dict[str(memory_object.get_recency())] = memory_object.get_content()

    general_query = "I will be giving you two types of information. 1. The memory of a person Juan in the form of a dictionary. The keys of this dictionary give away the recency of the incidents. These incidents may be conversations or routines of Juan which you can find in the dictionary values. 2. I will give Juan's current conversation history(with timestamps).  Having consumed this information. I WANT YOU TO RETRIEVE PIECES OF HIS MEMORY IN NATURAL LANGUAGE THAT ARE RELEVANT TO THE ONGOING CONVERSATION WHICH CAN ALSO HELP JUAN IN REPLYING TO THE CHATS. The retrieved history should be in the form of paragraph and should capture the relevant details of memory."
    query = [{'role' : 'user', 'content': general_query}]
    query.append({'role' : 'assistant', 'content' : "Sure! Please give the information."})
    sample_query = "1. " + str({'last day' : 'Juan is talking to Elisha on the texts. They are reminiscising about their childhood days. Juan turns out to be her cousin brother. They both love icecream.' , 'last week' : 'Juan is moving into a new home. He is very excited and sentimental as well'}) + " 2. " + " 0014: Human: Juan! Hello, this is Elisha. | 0112: Juan: Oh hey! You up this late? | 0114: Elisha: Yeah, man I couldnt sleep. I am craving food"
    query.append({'role' : 'user', 'content' : sample_query})
    sample_output = "Last day, Juan was talking to Elisha on the text. They were reminiscising about their childhood days. Juan is Elisha's cousin brother. They both love icecream."
    query.append({'role' : 'assistant', 'content' : sample_output})
    query.append({'role' : 'user', 'content' : 'Well Done! Your response captures the context of conversation well and memory retrieval is on point!'})
    query.append({'role' : 'assistant', 'content' : 'Thank you!'})
    query.append({'role' : 'user', 'content' : 'Do once more on this information.'})
    test_query = "1. " + str(query_dict) + " 2. " + temp_memory[-1]['content']
    query.append({'role' : 'user', 'content' : test_query})
    response = openai.ChatCompletion.create(
        model=model,
        messages= query,
        temperature = 0.3,
        )
    print("MEMORY ERC3:", query_dict)
    return(response['choices'][0]['message']['content'])


def NTV(memory_stream, chats):  
   memory_object = memory_stream.return_array()[-1]
   synopsis = memory_object.get_synopsis() + "FOLLOWING IS A CHAT OF JUAN WITH ANOTHER PERSON"+chats 
   dopamine_level=measure_dopamine(synopsis)
   endorphin_level=measure_endorphin(synopsis)
   oxytocin_level=measure_oxytocin(synopsis)
   adrenaline_level=measure_adrenaline(synopsis)
   return([dopamine_level, endorphin_level, oxytocin_level, adrenaline_level])

