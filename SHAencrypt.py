import os
import hashlib

print (os.getcwd())

#read contents of the file
file = open('file.txt', 'rb')
contents = file.read()
file.close()

#pull sha256
key = hashlib.sha256(contents).hexdigest()
print('Key:',key)

key1 = key[:32]
key2 = key[32:]









#test prints
print(key)
print(key1, key2)
print(len(key1), len(key2))
