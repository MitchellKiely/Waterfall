from algorithms.rsa import RSA
from algorithms.caesar import Caesar
import math
import json
from algorithms.common.utils import pad, depad, reverse

with open('message.txt') as f:
    plain_text = f.readlines()

algo_dict = {
    'caesar': Caesar,
    'rsa': RSA
}

sec_layers = {}
    
if __name__ == "__main__":

    message=plain_text
    print('\n Plain Text: \n', message)
    padded_message= pad(message)
    print('\n Padded Message: \n', padded_message)
    print('\n')    
    reverso = reverse(padded_message)
    print('The Reversed string is: \n ', reverso)

    #enc algo 1
    a= algo_dict['rsa']().encrypt(message = reverso, layer=1, e=77, n=143)
    print("First RSA encryption layer: \n", a)
    print('\n')
    sec_layers['layer1'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143, 'd':53}} #{'algo': 'caesar', 'key': 4}

    #enc algo 2
    b = algo_dict['caesar'].encrypt(message = a, key=4)
    print("Second Caesar Cipher encryption layer: \n ", b)
    print('\n')
    sec_layers['layer2'] = {'algo': 'caesar', 'key': 4}

    #enc algo 3
    c= algo_dict['rsa']().encrypt(b, layer=3, e=77, n=143)
    print("Third RSA encryption layer: \n", c)
    print('\n')
    sec_layers['layer3'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143, 'd':53}} #{'algo': 'caesar', 'key': 4}

    #dec algo 3
    d=algo_dict['rsa']().decrypt(message=c, layer=3, d=53,n=143)
    print('First RSA decryption layer: \n', d)
    print('\n')

    e=algo_dict['caesar'].decrypt(message=d, layer=2, key=4)
    print('Second Caesar cipher decryption layer: \n', e)
    print('\n')

    #dec algo 3
    f=algo_dict['rsa']().decrypt(message=e, layer=1, d=53,n=143)
    print('The Third & Final RSA decryption layer: \n', f)
    print('\n')

    g=reverse(f)
    print('The reverse string is: \n', g)
    print('\n')

    h = depad(g)
    print('The depadded message is: \n ', h)
    print('\n')

    with open('enc_layers.txt', 'w') as convert_file:
        convert_file.write(json.dumps(sec_layers))

    


