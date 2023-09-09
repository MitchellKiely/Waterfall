from string import ascii_lowercase
from primes import primes
import random
import numpy as np
import math

class RSA:
    def __init__(self):
        pass

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = self.egcd(b%a,a)
        return (g, x - (b//a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x%m

    def key_gen(self):
        #self.p = np.random.choice(primes, replace=False)
        #self.q = np.random.choice(primes, replace=False)
        self.p=3
        self.q = 11
        self.n = self.p*self.q
        self.m = (self.p-1) * (self.q-1)

        random_e = np.random.choice(primes, replace=False)
        coprime = False
        while not coprime:
            if np.gcd(random_e, self.m) == 1 and random_e < self.m:
                self.e = random_e
                coprime=True
            else:
                random_e = np.random.choice(primes, replace=False)
                coprime=False

        self.e=7
        self.d=3
        
        #self.d = self.modinv(self.e, self.m)
        

    def encrypt(self, let_to_num):
        print('Insert the message you want to encrypt: ')
        word = input()
        x = list(word)
        print('the word you are trying to encrypt is:', x)
        x_num = []
        for i in x:
            x_num.append(let_to_num[i])

        print('Your word converting to numbers is:', x_num)
        enc_list = []
        for j in x_num:
            enc_list.append(pow(j, self.e) % self.n)
        print('Your encrypted message is:', enc_list)
        return enc_list


    def decrypt(self, message, num_to_let):
        dec_list = []
        for i in message:
            dec_list.append(pow(i, self.d) % self.n)
        
        print("The decrypted message in number format is:", dec_list)
        message_letters = []
        for j in dec_list:
            for key, value in num_to_let.items():
                if j == value:
                    message_letters.append(key)
        decrypted_message = "".join([str(i) for i in message_letters])
        print("The decrypted message is", decrypted_message)
        return decrypted_message


    def build_dict(self):
        return {v:k for k,v in enumerate(ascii_lowercase)}

def main():
    r = RSA()
    dict_let_num = r.build_dict()
    r.key_gen()
    message = r.encrypt(dict_let_num)
    print(r.decrypt(message, dict_let_num))
    
if __name__ == "__main__":
    main()