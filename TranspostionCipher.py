#Get Plaintext and Key
plaintext = input('Enter plaintext: ').replace(" ","")
key = input('key:')

sequence = ''.join(sorted(key, key=str.lower))

#split plaintext based on key
row1 = plaintext [:len(key)]
row2 = plaintext [len(key):2*(len(key))]


#test prints
print()
print('Plaintext:',plaintext)
print()
print(key)
print(sequence)
print(row1)
print(row2)