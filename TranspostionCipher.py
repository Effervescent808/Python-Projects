import math

#Get Plaintext and Key
plaintext = input('Enter plaintext: ').replace(" ","")
key = input('key:')

if not key:
    print("Invalid key. Key cannot be empty.")
    exit()

#create sequence + grid
sequence = ''.join(sorted(key, key=str.lower))
grid = math.ceil(len(plaintext)/len(key))

#split plaintext based on key
rows = [plaintext[i * len(key):(i + 1) * len(key)] for i in range(grid)]
row_dict = {f"row{index}": row for index, row in enumerate(rows, start=1)}

#get column 1
column1= ""
for i in range(1, grid+1):
    column1 += (row_dict[f"row{i}"][0])

#get column 2
column2= ""
for i in range(1, grid+1):
    column2 += (row_dict[f"row{i}"][1])

#get column 3
column3= ""
for i in range(1, grid+1):
    column3 += (row_dict[f"row{i}"][2])

#test prints
print()
print('Plaintext:',plaintext)
print()
print(key)
print(sequence)
print()
for i in range(1, grid+1):
    print(row_dict[f'row{i}'])
print()
print(grid)
print()
print(column1,column2,column3, sep="")
