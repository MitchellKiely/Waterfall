from algorithms.common.primes import primes
from algorithms.common.lnd import let_num_dict
import numpy as np
import math

class RSA:
    def __init__(self):
        #self.p = np.random.choice(primes, replace=False)
        #self.q = np.random.choice(primes, replace=False)
        self.p=11
        self.q = 13
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

        self.e=77        
        self.d = self.modinv(self.e, self.m)
        #print(self.e)
        #print(self.d)

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
        
    def encrypt(self, message):
        
        x = list(message)
        #print('The word you are trying to encrypt is:', x)
        x_num = []
        for i in x:
            x_num.append(let_num_dict[i])

        #print('Your word converting to numbers is:', x_num)
        enc_list = []
        for j in x_num:
            enc_list.append(pow(j, self.e) % self.n)
        #print('Your encrypted message is:', enc_list)
        return enc_list


    def decrypt(self, message):
        dec_list = []
        for i in message:
            dec_list.append(pow(i, self.d) % self.n)
        
        #print("The decrypted message in number format is:", dec_list)
        message_letters = []
        for j in dec_list:
            for key, value in let_num_dict.items():
                if j == value:
                    message_letters.append(key)
        decrypted_message = "".join([str(i) for i in message_letters])
        #print("The decrypted message is: ", decrypted_message)
        return decrypted_message