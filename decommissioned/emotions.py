import openai
openai.api_key = "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"

from model import model
class Emotions:
    def __init__(self):
        self.array = [0,0,0,0,0,0,0,0,0,0]
        self.name_to_position = {
            'Joyful or Happy': 0,
            'Sad or Depressed': 1,
            'Anxious or Nervous': 2,
            'Angry or Upset': 3,
            'Relaxed or Calm': 4,
            'Excited or Energetic': 5,
            'Confused or Unsure': 6,
            'Embarrassed or Ashamed': 7,
            'Bored or Uninterested': 8,
            'Overwhelmed or Stressed': 9
        }
        self.position_to_name = {v: k for k, v in self.name_to_position.items()}  # reverse map
        self.description_to_value = {
            'high': 90,
            'medium': 50,
            'low': 10
        }
        self.changed = [False]*10  # Track whether each neurotransmitter has been changed

    def set_value(self, name, value):
        if isinstance(value, str):
            # If value is a string (like 'high'), convert it to a number
            value = self.description_to_value.get(value.lower(), 0)

        pos = self.name_to_position[name.lower()]
        self.array[pos] = value
        self.changed[pos] = True

    def process_input(self, input_str):
        inputs = input_str.split(' ')
        for i in range(0, len(inputs), 3): # We're skipping every 3 words ('set', 'name', 'value')
            self.set_value(inputs[i+1], inputs[i+2])

        return self.array
    
    def update_emotions(self,emotional_temp_memory):
        response = openai.ChatCompletion.create(
            model=model,
            messages=emotional_temp_memory,
            temperature = 0.6,
            max_tokens = 100,
            # functions= functions, #either response or function
            # function_call="auto", # auto is default, but we'll be explicit # can be used as formality check
        )
        emotional_scores_str = response['choices'][0]['message']['content']
        emotional_scores_str = emotional_scores_str.replace("'", "")  # Remove single quotes
        emotional_scores_pairs = emotional_scores_str.split(",")  # Split by commas

        emotional_scores = []
        for pair in emotional_scores_pairs:
            emotion, score = pair.split(":")  # Split by colon
            emotional_scores.append(int(score.strip()))  # Strip whitespace and convert to integer
        
        return(emotional_scores) #self.array doesnt get updated 



    def get_changed(self):
        changed_names_values = [(self.position_to_name[i], self.array[i]) for i in range(10) if self.changed[i]]
        return changed_names_values


