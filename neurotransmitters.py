class Neurotransmitter:
    def __init__(self):
        self.array = [50,50,50,50,50,50,50]
        self.name_to_position = {
            'adrenaline': 0,
            'oxytocin': 1,
            'serotonin': 2,
            'endorphin': 3,
            'gaba': 4,
            'norepinephrine': 5,
            'isocholine': 6
        }
        self.description_to_value = {
            'high': 90,
            'medium': 50,
            'low': 10
        }

    def set_value(self, name, value):
        if isinstance(value, str):
            # If value is a string (like 'high'), convert it to a number
            value = self.description_to_value.get(value.lower(), 0)

        self.array[self.name_to_position[name.lower()]] = value

    def process_input(self, input_str):
        inputs = input_str.split(' ')
        for i in range(0, len(inputs), 3): # We're skipping every 3 words ('set', 'name', 'value')
            self.set_value(inputs[i+1], inputs[i+2])

        return self.array


