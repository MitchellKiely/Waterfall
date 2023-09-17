from lnd import let_num_dict

class Caesar:
    def __init__(self):
        pass

    def encrypt(self, key):
        print('Insert the message you want to encrypt: ')
        word = input()
        x = list(word)
        print('the word you are trying to encrypt is:', x)
        x_num = []
        for i in x:
            x_num.append(let_num_dict[i])
        
        print(x_num)
        enc_list = [(x+key)%95 for x in x_num]
        print(enc_list)
        return enc_list

    def decrypt(self, message, key): 
        enc_list = [x-key for x in message]
        message_letters = []
        for j in enc_list:
            for key, value in let_num_dict.items():
                if j == value:
                    message_letters.append(key)
        decrypted_message = "".join([str(i) for i in message_letters])
        return decrypted_message

def main():
    caesar=Caesar()
    caesar_key = 3
    message = caesar.encrypt(key=caesar_key)
    print(caesar.decrypt(message, key=caesar_key))
    
if __name__ == "__main__":
    main()