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
    print('Plain Text: ', message)
    padded_message= pad(message)
    print('Padded Message: ', padded_message)
    reverso = reverse(padded_message)
    print('The Reversed string is: ', reverso)

    a= algo_dict['caesar'].encrypt(reverso, key=4)
    print("First Caesar cipher encryption layer", a)
    sec_layers['layer1'] = {'algo': 'caesar', 'key': 4}

    b = algo_dict['rsa']().encrypt(a, layer=2, e=77, n=143)
    print("Second RSA encryption layer", b)
    sec_layers['layer2'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143, 'd':53}}

    c=algo_dict['rsa']().decrypt(message=b, layer=2, d=53,n=143)
    print('First RSA decryption layer', c)

    d=algo_dict['caesar'].decrypt(message=c, layer=1, key=4)
    print('Second Caesar cipher decryption layer', d)

    e=reverse(reverso)
    print('The reverse string is: ', e)

    f = depad(e)
    print('The depadded message is: ', f)

    with open('enc_layers.txt', 'w') as convert_file:
        convert_file.write(json.dumps(sec_layers))

    


