from string import ascii_lowercase
from primes import primes
import random
import numpy as np
import math

class RSA:
    def __init__(self):
        self.p = int
        self.q = int
        self.n = int
        self.m = int
        self.e = int
        self.d = float

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
        self.p = np.int64(np.random.choice(primes, replace=False))
        self.q = np.int64(np.random.choice(primes, replace=False))
        self.n = np.int64(np.multiply(self.p,self.q))
        self.m = np.int64((self.p-1) * (self.q-1))

        random_e = np.random.choice(primes, replace=False)
        coprime = False
        while not coprime:
            if np.gcd(random_e, self.m) == 1 and random_e < self.m:
                self.e = np.int64(random_e)
                coprime=True
            else:
                random_e = np.random.choice(primes, replace=False)
                coprime=False

        
        self.d = self.modinv(self.e, self.m)
        

    def encrypt(self, let_to_num):
        print('Insert the message you want to encrypt: ')
        word = input()
        x = list(word)
        print(x)
        x_num = []
        for i in x:
            x_num.append(let_to_num[i])

        print(x_num)
        enc_list = []
        for j in x_num:
            enc_list.append(pow(j, self.e) % self.n)
        print('Your encrypted message is:', enc_list)
        return enc_list


    def decrypt(self, message, num_to_let):
        dec_list = []
        for i in message:
            dec_list.append(pow(i, self.d) % self.n)
        
        message_letters = []
        val_list = list(num_to_let.values())
        for j in dec_list:
            message_letters.append(val_list.index(j))

        breakpoint()
        decrypted_message = "".join([str(i) for i in message_letters])
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