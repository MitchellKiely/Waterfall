from algorithms.rsa import RSA
from algorithms.caesar import Caesar
import math
import json
from algorithms.common.utils import pad, depad, reverse
from termcolor import colored


with open('message.txt') as f:
    plain_text = f.readlines()

algo_dict = {
    'caesar': Caesar,
    'rsa': RSA
}

sec_layers = {}
    
if __name__ == "__main__":

    message=plain_text
    print(colored(f'\n Plain Text:', 'white', attrs=['underline']), '\n', message)
    
    padded_message= pad(message)
    print(colored('\n Padded Message:', 'red'), '\n', padded_message)
    
    reverso = reverse(padded_message)
    print(colored('\n Reorder String:','yellow'), '\n', reverso)

    a= algo_dict['caesar'].encrypt(reverso, key=4)
    print(colored("Encryption Layer 0, Caesar Cipher with key, k=4:", 'cyan'), '\n', a)
    print('\n')

    sec_layers['layer1'] = {'algo': 'caesar', 'key': 4}

    b = algo_dict['rsa']().encrypt(a, layer=2, e=77, n=143)
    print(colored("Encryption Layer 1, RSA Encryption with an encryption key, e=77, and modulus n=143:", 'blue'), '\n', b)
    print('\n')


    with open('ciphertext.txt', 'w') as filehandle:
        json.dump(b, filehandle)
    print(colored("Outputted Ciphertext:",'magenta'), '\n', b)
    print('\n')

    sec_layers['layer2'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143, 'd':53}}

    c=algo_dict['rsa']().decrypt(message=b, layer=2, d=53,n=143)
    print(colored('Decryption Layer 1: RSA Decryption  with a decryption key, d=53, and a modulus n=143:','blue'), '\n', c)
    print('\n')

    d=algo_dict['caesar'].decrypt(message=c, layer=1, key=4)
    print(colored('Decryption layer 0: Caesar Cipher Decryption with key, k=4 &', 'cyan'), colored('Converting numbers to characters', 'green'), '\n', d)
    print('\n')

    e=reverse(d)
    print(colored('Reordered String:', 'yellow'), '\n', e)
    print('\n')

    f = depad(e)
    print(colored('Depadded String:', 'red'), '\n', f)

    with open('enc_layers.txt', 'w') as convert_file:
        convert_file.write(json.dumps(sec_layers))

    


