from datetime import datetime

def get_current_time():
    current_time = datetime.now().strftime("%H%M")  # Get the current time in HH:MM:SS format
    return current_time
