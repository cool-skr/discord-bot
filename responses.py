import random
def handle_responses(message)->str :
    p_message = message.lower()
    if p_message == "hello":
        return "Hey"
    if p_message =="roll":
        return str(1)
    
    else:
        return "Help is here dont worry"
    