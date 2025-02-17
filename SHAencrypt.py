import os
import hashlib
import string

print()
print (os.getcwd())
print()

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
hash = hashlib.sha256(contents).hexdigest()
print('Key:',hash)

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

#use the cipher table
ciphertext = rot_cipher(plaintext, rot)
decoded_text = rot_cipher(ciphertext, -rot)

#output to file "encrypted.txt"
with open('encrypted.txt','w') as CoolBeans:
    print(ciphertext, file=CoolBeans)

#test prints
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
