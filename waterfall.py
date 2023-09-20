from algorithms.rsa import RSA
from algorithms.caesar import Caesar
import math
import json

with open('secrets.txt') as f:
    plain_text = f.readlines()

algo_dict = {
    'caesar': Caesar,
    'rsa': RSA
}

sec_layers = {}
    
if __name__ == "__main__":
    print('Plain Text', plain_text[0])
    a= algo_dict['caesar'].encrypt(message=plain_text[0], key=1)
    print('Caesar Encryption:', a)
    b=algo_dict['caesar'].encrypt(message=a, key=1)
    print('Caesar second encryption', b)
    c=algo_dict['caesar'].decrypt(message=b, key=2)
    print('Caesar decryption', c)


