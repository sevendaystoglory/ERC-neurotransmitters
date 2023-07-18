# ERC-neurotransmitters
Neurotransmitters flood the brain in response to external stimuli and utterances. An attempt to leverage GPT chat completions to tether such users to produce the desired persona through assistant utterances.

Notion Documentation: https://www.notion.so/AI-cognition-and-Human-companion-eeb7677ef83b43ca817d1d31e1b7c322

# MVP: layer one
This MVP captures the user's tone and generates a convincing backstory for the user. This context generation of the backstory transitions to a believable summary (Seamlessly as the threads of conversation become more complex). We also can gauge the "mood{1}" of the user with levels of neurotransmitters present in the user as estimated by the model with preferred definitions of each neurotransmitter and expected effect on producing certain types of conversations. For example, the presence of adrenaline can lead to more capitalisation and errors in typing.

# MVP: layer two
This MVP is to bring out several aspects of a genuine human conversation--> mood{1}, knowledge of events{2}, knowledge of self{3}, tone/ use of words{4}, number of replies per one reply of user{5}, length of reply{6}

After completing the checkpoint 2, following are the developments.
The replies are completetey based off of the temp_memory and the output format is as follows: {'formality': 'very informl', 'typos/grammar' : 'typing in low priority, a few typos' , 'attentiveness' : "little interest in the conversation", "tone and language" : "very direct and not respecting" , "number of lines in Juan's responses" : '2' , "length of each response" : '5' , 'response_1' : "Umm, no" , "response_2" : "sorry but I dont have anyone" , "response_3" : " " , "response_4" : " "}
