class Neurotransmitter:
    def __init__(self):
        self.array = [0,0,0,0,0,0,0]
        self.name_to_position = {
            'adrenaline': 0,
            'oxytocin': 1,
            'serotonin': 2,
            'endorphin': 3,
            'gaba': 4,  
            'norepinephrine': 5,
            'isocholine': 6
        }
        self.position_to_name = {v: k for k, v in self.name_to_position.items()}  # reverse map
        self.description_to_value = {
            'high': 90,
            'medium': 50,
            'low': 10
        }
        self.changed = [False]*7  # Track whether each neurotransmitter has been changed

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

    def get_changed(self):
        changed_names_values = [(self.position_to_name[i], self.array[i]) for i in range(7) if self.changed[i]]
        return changed_names_values


