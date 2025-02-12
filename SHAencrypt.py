import os
import hashlib

#read contents of the file
file = open('file.txt', 'rb')
contents = file.read()
file.close()

#pull sha256
key = hashlib.sha256(contents).hexdigest()
print('Key:',key)

