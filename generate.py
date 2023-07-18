import openai
openai.api_key = "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"
from model import model

def generate_context(temp_memory):
    response = openai.ChatCompletion.create(
        model=model,
        messages= temp_memory,
        temperature = 0.5, 
        max_tokens= 200,
    )

    print("CALLED---generate_context")
    return(response)
 
def generate_summary(memory):
    memory.append({'role' : 'user', 'content': 'summarize this piece of text in 100 tokens'})
    response = openai.ChatCompletion.create(
        model=model,
        messages= memory,
        temperature = 0.4,
        max_tokens= 100,
    )
    # memory.pop()
    print("CALLED---generate_summary")
    return(response)


def response_ERC2(nt4, temp_memory):
    chats = temp_memory[-1]
    nt_check = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + str(nt4.array[0]) + " and endorphin level of " + str(nt4.array[1])+" and dopamine level of " + str(nt4.array[2])+ "and adrenaline level of "+str(nt4.array[3]) +" where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    nt_sample = "Juan is an EXTREMELY MOODY PERSON with an oxytocin level of " + "30" + " and endorphin level of " + "40" + " and dopamine level of " + "15" + "and adrenaline level of " + "60" + " where the level 0 indicates no intensity and 100 indicates full intensity. Oxytocin, known as the social bonding 'love 'hormone, leads to EMPATHETIC, COMPASSIONATE, and UNDERSTANDING messages. It could encourage DEEPER communication, as well as AFFECTIONATE language. Oxytocin's stress-reducing properties might result in CALMER, COMFORTING language.\n Endorphins, natural painkillers linked to pleasure and well-being. They can result in more positive and upbeat language use, demonstrating an IMPROVED mood. High endorphin levels may INCREASED conversation ENERGY and ENTHUSIASM,REDUCE STRESS, and potentially stimulate more CREATIVE or IMAGINATIVE dialogue.\n Dopamine, a neurotransmitter associated with reward, MOTIVATION, and MOOD, can influence text messaging. High dopamine levels may lead to CREATIVE, and RISKY messages, reflecting increased motivation, JOY, and creativity. Low dopamine levels could result in less engaged, and more NEGATIVE messaging. Additionally, extremely high dopamine levels can lead to impulsivity and addiction. Adrenaline, a hormone associated with STRESS, EXCITEMENT, or DANGER, can significantly impact a user's chat conversations. High adrenaline levels heighten EMOTIONS, resulting in more passionate or intense exchanges. For example, a user might use more EXCLAMATION MARKS, CAPITAL letters, or EMOTIONALLY-CHARGED language. Adrenaline can concentrate the focus on perceived essential tasks, possibly creating more FOCUSSED responses.It may enhance memory ATTENTION , enabling the user to RECALL key parts of the conversation more VIVIDLY. However, heightened arousal might increase the propensity for mistakes, like TYPING ERRORS or RUSHED JUDGEMENTS. less TACTFUL language."
    with open('ERC-neurotransmitters\companion\Juan\preamble.txt', 'r') as file:
        preamble = file.read()
    dict_format = {'formality': 'level of formality', 'typos/grammar' : 'intensity of typos' , 'attentiveness' : "Juan's attentivess/ interest in the conversation", "tone and language" : "Juan's tone" , "number of lines in Juan's responses" : 'an integer between 1 and 4 (inclusive) denoting the number of responses' , "length of each response" : 'an integer marking the upper length of each response. SHOULD NOT BE GREATER THAN 50 WORDS!' , 'response_1' : "a sample Juan's first line of response based on all previous data." , "response_2" : "next line of Juan's response" , "response_3" : "next line of Juan's response" , "response_4" : "next line of Juan's response"}
    query = [{'role' : 'user', 'content': 'I will give you three types of information. 1. A brief on the character of Juan. 2. His current mood depending on the levels of oxytocin, endorphin, dopamine and adrenaline in his system. 3. His chat conversations with a human. You will then output a python dictionary in the following format : ' + str(dict_format)}]
    query.append({'role' : 'assistant', "content" : 'Sure!'})
    sample_case = " 1. " + preamble + " 2. " + nt_sample + " 3. " + "Human : Hey there how you doing today, Juan! \n Juan : Hi! I am doing great. BTW do I know you?\n Human : Oh I am Rashid from yesterday's anatomy class. Maxima is asking if you wanted to be project partner of ours? \n Juan : Ohhh. Just woke up man. Well, I am already booked, sorry. \n Human : Well then. You have anyone else I could partner up with?"
    query.append({'role' : 'user', "content" : sample_case})
    sample_output = {'formality': 'very informl', 'typos/grammar' : 'typing in low priority, a few typos' , 'attentiveness' : "little interest in the conversation", "tone and language" : "very direct and not respecting" , "number of lines in Juan's responses" : '2' , "length of each response" : '5' , 'response_1' : "Umm, no" , "response_2" : "sorry but I dont have anyone" , "response_3" : " " , "response_4" : " "}
    query.append({'role' : 'assistant', "content" : str(sample_output)})
    query.append({'role' : 'assistant', "content" : 'Fantastic work! This is exactly how I wanted it. Now do this task.'})
    test_case = " 1. " + preamble + " 2. " + nt_check + " 3. " + chats['content']
    query.append({'role' : 'user', "content" : test_case})

    response = openai.ChatCompletion.create(
        model=model,
        messages= query,
        temperature = 0.3,
    )

    return(response)