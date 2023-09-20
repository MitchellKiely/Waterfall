from algorithms.common.lnd import let_num_dict
import random as random

class Caesar:
    def __init__(self):
        self.key=random.randint(1,25)
    
    def encrypt(message, key):
        if isinstance(message, str):
            x = list(message)
            #print('The message you are trying to encrypt is:', x)
            x_num = []
            for i in x:
                x_num.append(let_num_dict[i])
            
            enc_list = [x+key for x in x_num]
            #print(f'The encrypted message is: {enc_list}')
            return enc_list
        else:
            enc_list = [x+key for x in message]
            #print(f'The encrypted message is: {enc_list}')
            return enc_list

    def decrypt(message, key): 
        #print(f'The message to be decrypted is: {message}')
        dec_list = [x-key for x in message]
        message_letters = []
        for j in dec_list:
            for key, value in let_num_dict.items():
                if j == value:
                    message_letters.append(key)
        decrypted_message = "".join([str(i) for i in message_letters])
        #print(f'The final decrypted message is: {decrypted_message}')
        return decrypted_message
