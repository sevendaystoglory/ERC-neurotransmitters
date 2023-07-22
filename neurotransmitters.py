class Neurotransmitter:
    def __init__(self,nt1=80, nt2=70, nt3=64, nt4=30):
        self.array = [nt1,nt2,nt3,nt4]
        self.name_to_position = {
            'dopamine': 0,
            'endorphin': 1,
            'oxytocin': 2,
            'adrenaline': 3
        }
        self.position_to_name = {v: k for k, v in self.name_to_position.items()}  # reverse map
        self.description_to_value = {
            'high': 100,
            'medium': 50,
            'low': 0
        }
        self.changed = [False]*4  # Track whether each neurotransmitter has been changed

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
        changed_names_values = [(self.position_to_name[i], self.array[i]) for i in range(4) if self.changed[i]]
        return changed_names_values


