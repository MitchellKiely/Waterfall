from algorithms.common.lnd import let_num_dict
import random as random
from termcolor import colored


class Caesar:
    def __init__(self):
        '''
        Initialises a random key to be within the interval [1,25]
        '''
        pass
        #self.key=random.randint(1,25)
    
    def encrypt(message, key):
        '''
        If the message is a str, this function converts each character to a number (as described in common/lnd.py) and adds onto this number 
        by the value given in the key parameter.

        If the message is a series of integers, the value of key is added onto each integer.

        Inputs:
            -message (str or list): This is the message that you want to encrypt.
            -key (int): This is the Caesar cipher key that will be used during the encryption process.
        
        Outputs:
            enc_list (list): This is a list of numbers which is the encrypted message.
        '''
        if isinstance(message, str):
            x = list(message)
            #print('The message you are trying to encrypt is:', x)
            x_num = []
            for i in x:
                x_num.append(let_num_dict[i])
            print(colored('\n The character to number conversion is:', 'green'), '\n', x_num)
            print('\n')
            enc_list = [x+key for x in x_num]
            #print(f'The encrypted message is: {enc_list}')

            return enc_list
        else:
            enc_list = [x+key for x in message]
            #print(f'The encrypted message is: {enc_list}')
            return enc_list

    def decrypt(message, key, layer): 
        '''
        If the message is the last layer of encryption, then the value of each element in the message array is subtracted and converted to a 
        character as defined in common/lnd.py. This converted list is joined into a string and returned.

        If the message is not the last layer, each element is subtracted by the value of key and returned.

        Inputs:
            -message (list): This is the encrypted message to be decrypted,
            -key (int): This is the caesar cipher key required to decrypt

        Output:
            dec_list (str or list): This is the decrypted message
        '''
        if layer == 1:
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
        else:
            dec_list = [x-key for x in message]
            return dec_list
