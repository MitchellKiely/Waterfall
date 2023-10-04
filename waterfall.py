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
    reverso = reverse(padded_message)
    print('\n The Reversed string is: \n ', reverso)

    a= algo_dict['caesar'].encrypt(reverso, key=4)
    print("First Caesar cipher encryption layer: \n", a)
    print('\n')

    sec_layers['layer1'] = {'algo': 'caesar', 'key': 4}

    b = algo_dict['rsa']().encrypt(a, layer=2, e=77, n=143)
    print("Second RSA encryption layer: \n ", b)
    print('\n')

    with open('ciphertext.txt', 'w') as filehandle:
        json.dump(b, filehandle)

    sec_layers['layer2'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143, 'd':53}}

    c=algo_dict['rsa']().decrypt(message=b, layer=2, d=53,n=143)
    print('First RSA decryption layer: \n', c)
    print('\n')

    d=algo_dict['caesar'].decrypt(message=c, layer=1, key=4)
    print('Second Caesar cipher decryption layer: \n', d)
    print('\n')

    e=reverse(d)
    print('The reverse string is: \n', e)
    print('\n')

    f = depad(e)
    print('The depadded message is:\n', f)

    with open('enc_layers.txt', 'w') as convert_file:
        convert_file.write(json.dumps(sec_layers))

    


