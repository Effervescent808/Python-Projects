import os
import hashlib
import string

testmode = False

print()
print (os.getcwd())
print()

decrypt_mode = False
encrypt_mode = False

while True:
    try:
        mode = input('(d/e) mode?:')
        if mode == 'd':
            decrypt_mode = True
            break
        elif mode == 'e':
            encrypt_mode = True
            break
        else: 
            print('unknown input')
    except ValueError:
          print('unknown input')


#account for non recognised files
while True:
    try:
#get file input
        Input = input('file:')
#read contents of the file
        file = open(Input, 'rb')
        file2 = open(Input, 'r')
        contents = file.read()
        contents2 = file2.read()
        break
    except FileNotFoundError:
        print('File not found')
        print()
        

#pull sha256
if encrypt_mode == True:
    hash = hashlib.sha256(contents).hexdigest()
    print()
    print('Key:',hash)
    print()

#ask for key
if decrypt_mode == True:
    hash = input('key:')

#create letter to value table
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1

key = ""

#converts letter to number
for char in hash:
    if char.isalpha():
        key += str(values[char.lower()])
    elif char.isdigit():
        key += char

#pulls 1st and 2nd halves apart
key1 = key[:32]
key2 = key[32:]

#sums of key1 and key2
sum_key1 = 0
for char in key1:
    sum_key1 += int(char)

sum_key2 = 0
for char in key2:
    sum_key2 += int(char)

#get rot value
rot = abs(sum_key1 - sum_key2)

#make a cipher table
def rot_cipher(text, shift):

    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift % 26:] + alphabet[:shift % 26]

    table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

    return text.translate(table)

plaintext = str(contents2)

#use the cipher table for encoding
ciphertext = rot_cipher(plaintext, rot)

#use the cipher table for decoding
decoded_text = rot_cipher(plaintext, -rot)

#output to file "encrypted.txt"
if encrypt_mode == True:
    with open('encrypted.txt','w') as CoolBeans:
        print(ciphertext, file=CoolBeans)

#output to file "decrypted.txt"
if decrypt_mode == True:
    with open('decrypted.txt','w') as CoolBeans1:
        print(decoded_text, file=CoolBeans1)

#prints
if decrypt_mode == True:
    print()
    print('file successfully decrypted')

if encrypt_mode == True:
    print('file encrypted successfully')

#test prints
if testmode == True:
    print()
    print(key)
    print()
    print(key1, key2)
    print()
    print(sum_key1, sum_key2)
    print()
    print(rot)
    print()
    print('Ciphertext:',ciphertext)
    print('Decoded_text:',decoded_text)
