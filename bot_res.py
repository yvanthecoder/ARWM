import numpy as np

def response(input_message):
    message = np.array([["yo", "yoo on dit quoi ?"],
                        ["bonjour", "bjr on dit quoi ?"],
                        ["bonsoir", "bonsoir on dit quoi ?"],
                        ["tranquille gar ", "oklm type"],
                        ["okay", "yep"],
                        ["yes", "oklm"],
                        ["on dit quoi ?", "Je suis la gar et toi ?"]])
    message_ = ""
    message_recv = input_message.lower()
    res = ''

    for i in range (0, len(message_recv)):
        message_+=message_recv[i]
        for j in range (0, len(message)):
            if message_ == message[j][0]:
                res += message[j][1]
    
    return (res)

