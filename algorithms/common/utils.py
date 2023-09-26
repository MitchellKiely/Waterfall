#Code for padding is based on the code found here: https://www.geeksforgeeks.org/python-insert-character-after-every-character-pair/

from textwrap import wrap
import string
import random

def pad(message):
    paddy = ""
    #for i in range(0, len(message), 1):
    for line in message:
        for l in line:
            random_letter = random.choice(string.ascii_letters)
            #paddy += message[l] + random_letter
            paddy += l + random_letter
    return paddy

def depad(message):
    dpaddy = ""
    for i in range(0, len(message), 2):
        dpaddy += message[i]
    
    return dpaddy

def reverse(message):
    return message[::-1]
