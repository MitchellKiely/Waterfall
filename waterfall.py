from algorithms.rsa import RSA
from algorithms.caesar import Caesar
import math
import json

with open('message.txt') as f:
    plain_text = f.readlines()

algo_dict = {
    'caesar': Caesar,
    'rsa': RSA
}

sec_layers = {}
    
if __name__ == "__main__":

    #Input the encryption algorithms & keys you want
    #Attach these, in sequential order to the sec_layers dictinary

    #Assert to check if input layers are in algo_dict

    #Execute each encryption protcol

    #Append algorithm name
    print('Plain Text:', plain_text[0])
    a= algo_dict['caesar'].encrypt(message=plain_text[0], key=4)
    print("First Caesar cipher encryption layer", a)
    sec_layers['layer1'] = {'algo': 'caesar', 'key': 4}

    b = algo_dict['rsa']().encrypt(a, layer=2, e=77, n=143)
    print("Second RSA encryption layer", b)
    sec_layers['layer2'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143, 'd':53}}

    c=algo_dict['rsa']().decrypt(message=b, layer=2, d=53,n=143)
    print('First RSA decryption layer', c)

    d=algo_dict['caesar'].decrypt(message=c, layer=1, key=4)
    print('Second RSA decryption layer', d)

    '''
    print('Plain Text', plain_text[0])
    a= algo_dict['caesar'].encrypt(message=plain_text[0], key=2)
    sec_layers['layer1'] = {'algo': 'caesar', 'key': 4}
    print('Caesar Encryption:', a)
    b=algo_dict['caesar'].encrypt(message=a, key=1)
    sec_layers['layer2'] = {'algo': 'caesar', 'key': 1}

    print('Caesar second encryption', b)
    c=algo_dict['caesar'].decrypt(message=b, key=2, layer=1)
    print('Caesar decryption', c)
    
    rsa = RSA()
    print('Plain Text', plain_text[0])
    a= rsa.encrypt(message=plain_text[0], layer=1, e=77, n=143)
    sec_layers['layer1'] = {'algo': 'rsa', 'keys': {'e':77, 'n':143}}
    print('First RSA Encryption:', a)
    b= rsa.encrypt(message=a, layer=2, e=77, n=143)
    print('Second RSA Encryption:', b)
    sec_layers['layer2'] = {'algo': 'rsa', 'keys': {'e':7, 'n':187}}

    c=rsa.decrypt(message=b, layer=2, d=53,n=143)
    print('First RSA decryption', c)
    d=rsa.decrypt(message=c, layer=1, d=53,n=143)
    print('Second RSA decryption', d)
    #b=algo_dict['caesar'].encrypt(message=a, key=1)
    #sec_layers['layer2'] = {'algo': 'caesar', 'key': 1}

    #print('Caesar second encryption', b)
    #c=algo_dict['caesar'].decrypt(message=b, key=2, layer=1)
    #print('Caesar decryption', c)
    '''
    with open('enc_layers.txt', 'w') as convert_file:
     convert_file.write(json.dumps(sec_layers))


